#!/usr/bin/env python3
"""
retrieval-health.py — 검색층(QMD 인덱스) 상태를 로컬 감사에 표면화 (signal, never blocks)

T2 of agenda/2026-09-03_audit-gap-closure.md

왜 있는가
---------
감사 22개가 전부 "파일이 옳은가"를 본다. 그런데 **답변 경로는 파일이 아니라
인덱스를 지난다.** 페이지를 고쳐도 색인이 옛것을 들고 있으면 검색은 고치기 전
내용을 계속 내놓는다 — 페이지는 맞는데 답이 틀리는, 어느 감사에도 안 걸리는
실패다. 2026-07-17에 철회 논문 페이지를 고쳐놓고 재색인을 빠뜨려 10시간 동안
철회 경고 없는 옛 청크가 검색됐고, 인덱스 대상을 고친 55일 중 23일(42%)이
이 창에 노출됐다 (CLAUDE.md 실측).

`deploy-health.py`가 배포에 대해 한 일 — 리포 바깥의 상태를 매일 도는 감사
출력에 끌어와 *찾아가지 않아도 보이게* 하는 것 — 을 검색에 대해 한다.

무엇을 보는가 (6가지)
--------------------
  1. 설정      — index.yml의 컬렉션 목록·경로 실존. 컬렉션이 설정에서 조용히
                 빠지면 검색이 그 티어를 통째로 못 본다 (에러 없이).
  2. 신선도    — 인덱스보다 새로 수정된 .md 수. 그날 편집분이 색인에 없다는 뜻.
  3. 문서수    — 디스크 실제 .md 수 vs 인덱스가 아는 수. 신선해 보여도 문서가
                 누락/잔존일 수 있다 (mtime만으로는 안 잡힌다).
  4. Pending   — 임베딩 백로그. `qmd embed`는 exit 0을 내고도 미완료일 수 있고
                 `qmd update`가 찍는 숫자는 전체 파일 수라 거짓이다 — 진짜
                 백로그는 `qmd status`의 Pending 뿐 (CLAUDE.md).
  5. 고아 벡터 — 삭제된 문서의 잔존 청크. 방치하면 검색이 **에러 없이** 산
                 문서를 놓친다.
  6. 클린업 잡 — 주간 launchd(com.llmwiki.qmd-cleanup)의 마지막 완주 시각.
                 잡이 죽어도 아무 데서도 안 보이는 것이 원래 문제였다.

qmd가 없거나 데몬이 죽었거나 설정이 없으면 **조용히 SKIP하고 exit 0**.
감사는 거울이지 gate가 아니다 (CLAUDE.md 설계원칙).

Usage:
    python3 scripts/retrieval-health.py [--selftest]
"""

# PEP604(`str | None`) 힌트가 구 python3(3.9)에서 죽는다 — AUDITS.md의 알려진 함정.
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LOG = REPO / "logs" / f"{date.today().isoformat()}_retrieval-health.log"
CONFIG = Path.home() / ".config" / "qmd" / "index.yml"
CLEANUP_LOG = REPO / ".claude" / "scripts" / "qmd-cleanup.log"

# 주간 잡(월 10:00) + 하루 유예. 이보다 오래됐으면 잡이 죽었다고 본다.
CLEANUP_MAX_DAYS = 8
# 디스크 vs 인덱스 문서 수 허용 오차. 0으로 두면 감사 도중의 파일 생성에도 뜬다.
DOC_DELTA_TOL = 2

STATUS_ANCHOR = re.compile(r"QMD Status")


# ── 파서 ─────────────────────────────────────────────────────────────────────
#
# T1에서 배운 것을 그대로 적용한다: **없는 줄은 0이 아니라 unknown이다** —
# 단, 앵커로 "이 출력이 내가 아는 그 출력"임을 확인한 뒤에는 부재가 0이다.
# `Pending:`도 `Orphaned:`도 값이 0이면 qmd가 줄 자체를 안 찍는다. 앵커 없이
# 부재를 unknown으로 두면 **정상인 날마다 거짓 경고**가 나고, 앵커 없이 0으로
# 두면 출력 형식이 바뀐 날 **조용히 초록불**이 된다. 둘 다 배지를 죽인다.

def parse_pending(text: str):
    if not STATUS_ANCHOR.search(text):
        return None
    m = re.search(r"^\s*Pending:\s*([\d,]+)", text, re.M)
    return int(m.group(1).replace(",", "")) if m else 0


def parse_orphaned(text: str):
    """→ (청크 수, 퍼센트 or None). 0이면 qmd가 줄을 안 찍는다."""
    if not STATUS_ANCHOR.search(text):
        return None, None
    m = re.search(r"^\s*Orphaned:\s*([\d,]+)\s*embedding chunks(?:\s*\((\d+)%\))?", text, re.M)
    if not m:
        return 0, 0
    return int(m.group(1).replace(",", "")), (int(m.group(2)) if m.group(2) else None)


def parse_indexed_counts(text: str):
    """컬렉션명 → 인덱스가 아는 파일 수. 형식이 아니면 None."""
    if not STATUS_ANCHOR.search(text):
        return None
    out = {}
    for m in re.finditer(r"^\s{2}([\w-]+)\s*\(qmd://[^)]*\)\s*\n(?:.*\n)*?\s*Files:\s*([\d,]+)",
                         text, re.M):
        out[m.group(1)] = int(m.group(2).replace(",", ""))
    return out


def parse_index_path(text: str):
    m = re.search(r"^\s*Index:\s*(\S+)", text, re.M)
    return Path(m.group(1)) if m else None


def parse_collections(yml: str):
    """index.yml → {name: path}. PyYAML 없이도 돌아야 한다 (감사는 의존성이 얇을수록 좋다)."""
    out = {}
    name = None
    for line in yml.splitlines():
        m = re.match(r"^  ([\w-]+):\s*$", line)
        if m:
            name = m.group(1)
            continue
        m = re.match(r"^    path:\s*(.+?)\s*$", line)
        if m and name:
            out[name] = Path(m.group(1).strip().strip('"\''))
            name = None
    return out


def index_mtime(idx: Path):
    """인덱스 최종 쓰기 시각 = sqlite 파일 3종의 mtime 중 최대.

    ⚠ `index.sqlite` 하나만 보면 안 된다. QMD는 **WAL 모드**로 쓴다 — 쓰기는
    `index.sqlite-wal`에 들어가고 본 파일의 mtime은 체크포인트 때만 움직인다.
    실측 2026-09-03: `qmd update && qmd embed` 직후에도 본 파일은 00:07:29,
    실제 쓰기는 -wal 09:25:53. 본 파일만 보는 초안은 **재색인을 마친 직후에도
    "재색인 필요"를 띄웠다** — 정상인 날마다 우는 경고이고, 그런 경고는 곧
    무시되므로 감사가 없는 것만 못하다 (T1의 조건부 블록과 같은 교훈).
    """
    times = []
    for suffix in ("", "-wal", "-shm"):
        f = idx.with_name(idx.name + suffix)
        try:
            times.append(f.stat().st_mtime)
        except OSError:
            pass
    return max(times) if times else None


def parse_cleanup_ts(text: str):
    ts = re.findall(r"^\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]\s*qmd-cleanup done", text, re.M)
    if not ts:
        return None
    return datetime.strptime(ts[-1], "%Y-%m-%d %H:%M:%S")


def main() -> int:
    ap = argparse.ArgumentParser(description="QMD 검색층 상태 감사 (signal)")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()

    lines = [f"# Retrieval Health — {date.today().isoformat()}", ""]

    def emit(s=""):
        lines.append(s)

    def finish(headline: str) -> int:
        print(headline)
        try:
            LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
            print(f"      → logs/{LOG.name}")
        except OSError:
            pass
        return 0

    if shutil.which("qmd") is None:
        emit("SKIP: qmd CLI not installed")
        return finish("[retrieval-health] SKIP — qmd CLI 없음 (signal only, 차단 안 함)")
    if not CONFIG.exists():
        emit(f"SKIP: {CONFIG} 없음")
        return finish("[retrieval-health] SKIP — qmd 설정 없음")

    try:
        r = subprocess.run(["qmd", "status"], capture_output=True, text=True, timeout=30, cwd=REPO)
        status = (r.stdout or "") + (r.stderr or "")
    except (OSError, subprocess.TimeoutExpired):
        emit("SKIP: `qmd status` 실행 실패/타임아웃 (데몬 사망 의심)")
        return finish("[retrieval-health] SKIP — qmd status 응답 없음")

    if not STATUS_ANCHOR.search(status):
        emit("SKIP: `qmd status` 출력이 예상 형식이 아님 — 파서 갱신 필요")
        return finish("[retrieval-health] SKIP — qmd status 형식 불명 (파서 확인 요)")

    warns, infos = [], []

    # ── 1. 설정 ──────────────────────────────────────────────────────────────
    cols = parse_collections(CONFIG.read_text(encoding="utf-8", errors="replace"))
    emit(f"collections configured : {len(cols)}  ({', '.join(sorted(cols)) or '—'})")
    for name, path in sorted(cols.items()):
        if not path.exists():
            warns.append(f"컬렉션 경로 없음: {name} → {path}")

    # ── 2·3. 신선도 + 문서 수 ────────────────────────────────────────────────
    idx = parse_index_path(status)
    idx_mtime = index_mtime(idx) if idx and idx.exists() else None
    indexed = parse_indexed_counts(status) or {}

    emit("")
    emit(f"index                  : {idx if idx else '—'}")
    if idx_mtime:
        emit(f"index mtime            : {datetime.fromtimestamp(idx_mtime).isoformat(' ', 'seconds')}")
    else:
        warns.append("index.sqlite 파일을 찾을 수 없음")
    emit("")
    emit(f"  {'collection':<12} {'on-disk':>8} {'indexed':>8} {'newer':>7}")

    total_stale = 0
    for name, path in sorted(cols.items()):
        if not path.exists():
            continue
        files = list(path.rglob("*.md"))
        newer = sum(1 for f in files if idx_mtime and f.stat().st_mtime > idx_mtime)
        total_stale += newer
        n_idx = indexed.get(name)
        emit(f"  {name:<12} {len(files):>8} {('—' if n_idx is None else n_idx):>8} {newer:>7}")
        if newer:
            infos.append(f"{name}: 인덱스보다 새 파일 {newer}건")
        if n_idx is not None and abs(n_idx - len(files)) > DOC_DELTA_TOL:
            warns.append(f"{name}: 문서 수 불일치 (디스크 {len(files)} vs 인덱스 {n_idx})")

    if total_stale:
        warns.append(f"재색인 필요 — 인덱스보다 새 .md {total_stale}건 (`qmd update && qmd embed`)")

    # ── 4. 임베딩 백로그 ─────────────────────────────────────────────────────
    pending = parse_pending(status)
    emit("")
    emit(f"embedding pending      : {'불명' if pending is None else pending}")
    if pending:
        warns.append(f"임베딩 백로그 {pending}건 (`qmd embed`를 완료 문구가 뜰 때까지 반복)")

    # ── 5. 고아 벡터 ─────────────────────────────────────────────────────────
    orph, pct = parse_orphaned(status)
    emit(f"orphaned chunks        : {'불명' if orph is None else orph}"
         + (f" ({pct}%)" if pct else ""))

    # ── 6. 클린업 잡 생존 ────────────────────────────────────────────────────
    last = parse_cleanup_ts(CLEANUP_LOG.read_text(encoding="utf-8", errors="replace")) \
        if CLEANUP_LOG.exists() else None
    if last is None:
        emit("cleanup last完走       : 기록 없음")
        warns.append("qmd-cleanup 완주 기록 없음 — launchd 잡 확인 요")
        days = None
    else:
        days = (datetime.now() - last).days
        emit(f"cleanup last완주       : {last.isoformat(' ', 'seconds')} ({days}일 전)")
        if days > CLEANUP_MAX_DAYS:
            warns.append(f"qmd-cleanup {days}일째 미실행 — 주간 잡(월 10:00) 사망 의심")

    # 고아는 그 자체보다 "치우는 잡이 살아있는가"가 신호다. 잡이 정상이면 정보로만.
    if orph:
        (warns if (days is None or days > CLEANUP_MAX_DAYS) else infos).append(
            f"고아 벡터 {orph}개" + (f" ({pct}%)" if pct else "")
        )

    emit("")
    emit("=== WARN ===")
    for w in warns:
        emit(f"  ⚠ {w}")
    emit("=== INFO ===")
    for i in infos:
        emit(f"  · {i}")

    if warns:
        head = f"    🔎  Retrieval health: ⚠ {len(warns)}건 — " + " · ".join(warns[:2])
    else:
        bits = [f"인덱스 신선(0건)", f"pending {pending or 0}"]
        if orph:
            bits.append(f"고아 {orph}" + (f"({pct}%)" if pct else ""))
        if days is not None:
            bits.append(f"클린업 {days}일 전")
        head = "    🔎  Retrieval health: ✓ " + " · ".join(bits)
    return finish(head)


# ── 회귀 ─────────────────────────────────────────────────────────────────────
# 이 파서들은 다른 프로그램(qmd)의 stdout에 결합돼 있다 — 조용히 썩는 결합이다.
# 정규식을 손대기 전에 먼저 돌릴 것.

REAL_STATUS = """QMD Status

Index: /Users/x/.cache/qmd/index.sqlite
Size:  438.3 MB

Documents
  Total:    6736 files indexed
  Vectors:  27363 embedded
  Orphaned: 1094 embedding chunks (4%) — run 'qmd cleanup'
  Updated:  1m ago

Collections
  wiki (qmd://wiki/)
    Pattern:  **/*.md
    Files:    3526 (updated 9h ago)
  sources (qmd://sources/)
    Pattern:  **/*.md
    Files:    3105 (updated 9h ago)
"""

CLEAN_STATUS = REAL_STATUS.replace("  Orphaned: 1094 embedding chunks (4%) — run 'qmd cleanup'\n", "")


def selftest() -> int:
    bad = 0

    def check(name, got, want):
        nonlocal bad
        ok = got == want
        bad += not ok
        print(f"  {'✓' if ok else '✗'} {name:<28} got={got!r:<26} want={want!r}")

    check("orphaned present", parse_orphaned(REAL_STATUS), (1094, 4))
    # 0이면 qmd가 줄을 안 찍는다 → 앵커가 있으면 부재는 0 (거짓 경고 방지)
    check("orphaned absent→0", parse_orphaned(CLEAN_STATUS), (0, 0))
    # 앵커가 없으면 그건 내가 아는 출력이 아니다 → unknown (거짓 초록불 방지)
    check("orphaned wrong-out", parse_orphaned("Segmentation fault"), (None, None))
    check("pending absent→0", parse_pending(REAL_STATUS), 0)
    check("pending present", parse_pending(REAL_STATUS.replace("  Vectors:", "  Pending:  1,203 docs\n  Vectors:")), 1203)
    check("pending wrong-out", parse_pending(""), None)
    check("indexed counts", parse_indexed_counts(REAL_STATUS), {"wiki": 3526, "sources": 3105})
    check("indexed wrong-out", parse_indexed_counts("nope"), None)
    check("index path", str(parse_index_path(REAL_STATUS)), "/Users/x/.cache/qmd/index.sqlite")

    yml = ("collections:\n  wiki:\n    path: /a/wiki\n    pattern: \"**/*.md\"\n"
           "  meetings:\n    path: /a/note-meeting\n    pattern: \"**/*.md\"\n"
           "models:\n  embed: hf:x\n")
    check("collections", {k: str(v) for k, v in parse_collections(yml).items()},
          {"wiki": "/a/wiki", "meetings": "/a/note-meeting"})

    log = "[2026-08-24 10:00:07] qmd-cleanup start\n[2026-08-31 10:00:12] qmd-cleanup done\n"
    check("cleanup ts", str(parse_cleanup_ts(log)), "2026-08-31 10:00:12")
    check("cleanup none", parse_cleanup_ts("nothing here"), None)

    print(f"\n{'✅ selftest OK' if not bad else f'❌ {bad} case(s) failed'}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
