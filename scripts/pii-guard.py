#!/usr/bin/env python3
"""
pii-guard.py — 환자·직원 식별정보가 공개 리포에 들어가는 것을 막는다 (ERROR, blocks)

T3 of agenda/2026-09-03_audit-gap-closure.md

왜 error인가
------------
이 위키의 기본값은 *signal, not gate*다. 그 원칙은 **판단이 개입하는** 감사
(인제스트 압력·종합 백로그)를 겨눈 것이고, 이건 정규식의 결정론적 존재 검사다.
무엇보다 **이 리포의 유일한 비가역 실패 모드**다 — 배포 실패도 틀린 수치도
되돌릴 수 있지만, 공개된 환자 식별정보는 git 히스토리·GitHub Pages 캐시·검색엔진
색인에 남아 되돌릴 수 없다.

왜 지금인가
-----------
도입 시점 실측 위반 **0건** (2026-09-03, 추적 파일 11,616개 전수). block으로 둬도
오늘 아무것도 막지 않는다 — `operations-lint` §7이 위반 0에서 error가 된 것과 같다.
반대로 위험은 실재한다: 리포는 공개 Pages 배포이고, dentweb MCP는 실환자 DB를
읽으며, 익명화 규칙은 `note-meeting/_template.md`의 산문 한 줄뿐이었다. 규칙이
문서에만 있고 읽는 코드가 없는 배치 — 2026-08-31 다크모드 사고와 정확히 같다.

스캔 범위 = **git이 추적하는 텍스트 파일**
------------------------------------------
디렉터리 목록이 아니라 추적 여부로 정한다. 위협은 "공개 리포에 커밋되는 것"이고,
`git ls-files`가 정확히 그 집합이다. 디렉터리 목록으로 잡으면 새 폴더가 생길 때마다
조용히 사각지대가 늘어난다 — `lint.py`의 `SKIP_DIRS`가 2026-08-25에 만든 그 구멍이다.
(부수 효과로 `papers/*.pdf`와 gitignore된 `logs/*.log`는 자동 제외된다.)

오탐 억제가 설계의 절반
-----------------------
초안 grep의 히트는 **전부 DOI였다** — `10.3760/cma.j.cn112144-20230915-00158`이
주민번호형에, `10.1007/s15010-025-02568-y`가 휴대폰형에 걸린다. 3겹으로 막는다:
  ① 경계 lookaround — 숫자에 이어 붙은 매치를 배제 (이것만으로 위 둘이 다 죽는다)
  ② 마스킹 — URL·DOI·PMID·PMCID·ISBN 구간을 매칭 전에 지운다 (심층 방어)
  ③ 주민번호 체크섬 — 통과해야 ERROR, 모양만 맞으면 WARN.
     `기간 202001-2024012` 같은 날짜범위가 모양에 걸리므로 이 계층이 없으면
     block이 오탐으로 터진다.

이메일은 **임상 디렉터리에서만** 본다
--------------------------------------
`sources/` 15개 파일에 교신저자 이메일이 있다 — 학술지에 이미 공개된 연락처이지
환자 정보가 아니다. 패턴으로는 구분이 불가능하고 위치로만 갈린다. 그래서 이메일은
진료 운영 디렉터리(`agenda/`·`note-meeting/`·`interactives/`·`slides/`)에서만 ERROR다.
문헌 티어에서 이메일을 금지하면 정당한 내용 수천 건을 고치게 만들 뿐이다.

Usage:
    python3 scripts/pii-guard.py              # 추적 파일 전수
    python3 scripts/pii-guard.py --staged     # 스테이지된 파일만 (pre-commit 훅용)
    python3 scripts/pii-guard.py --selftest
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LOG = REPO / "logs" / f"{date.today().isoformat()}_pii-guard.log"
ALLOWLIST = REPO / "scripts" / "pii-allowlist.txt"

TEXT_EXTS = {".md", ".html", ".htm", ".json", ".csv", ".txt", ".yml", ".yaml"}

# 진료 운영 디렉터리 — 여기의 연락처·식별번호는 환자/직원의 것일 개연성이 높다.
# 문헌 티어(papers/·sources/·wiki/)는 논문에 실린 저자 연락처라 성격이 다르다.
CLINIC_DIRS = ("agenda/", "note-meeting/", "interactives/", "slides/")

# ── 마스킹 (심층 방어 — ①의 lookaround가 이미 대부분을 막는다) ──────────────
MASKS = [
    re.compile(r"https?://\S+"),
    re.compile(r"\b10\.\d{4,9}/[^\s)\]\",]+"),        # DOI
    re.compile(r"\bPMC\d+\b"),
    re.compile(r"\bPMID:?\s*\d+"),
    re.compile(r"\bISBN[\s:-]*[\d-]+", re.I),
]

RRN = re.compile(r"(?<!\d)(\d{6})-([1-4]\d{6})(?!\d)")
PHONE = re.compile(r"(?<!\d)01[016789][-. ]\d{3,4}[-. ]\d{4}(?!\d)")
EMAIL = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
CHART = re.compile(r"(차트\s*번호|환자\s*번호|chart[_\s-]?no|patient[_\s-]?id)\s*[:=]?\s*(\d{3,})", re.I)


def rrn_checksum_ok(thirteen: str) -> bool:
    """주민등록번호 검증부호. 통과해야 ERROR로 올린다."""
    if len(thirteen) != 13 or not thirteen.isdigit():
        return False
    w = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    d = [int(c) for c in thirteen]
    return (11 - sum(a * b for a, b in zip(d[:12], w)) % 11) % 10 == d[12]


def mask(text: str) -> str:
    for pat in MASKS:
        text = pat.sub(lambda m: "·" * len(m.group()), text)
    return text


def load_allowlist() -> set:
    """의도적으로 실린 값(예: 의원 대표번호). `값  # 사유` 한 줄에 하나."""
    if not ALLOWLIST.exists():
        return set()
    out = set()
    for line in ALLOWLIST.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.split("#", 1)[0].strip()
        if line:
            out.add(line)
    return out


def target_files(staged: bool) -> list:
    cmd = ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"] if staged \
        else ["git", "ls-files"]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, cwd=REPO, timeout=60)
        names = r.stdout.split("\n") if r.returncode == 0 else []
    except (OSError, subprocess.TimeoutExpired):
        names = []
    return [n for n in names if n and Path(n).suffix.lower() in TEXT_EXTS]


def in_clinic(rel: str) -> bool:
    return rel.startswith(CLINIC_DIRS)


def scan_text(rel: str, text: str, allow: set) -> list:
    """→ [(severity, rule, matched, line_no)]"""
    hits = []
    masked = mask(text)
    # 줄 번호는 마스킹이 길이를 보존하므로 원문과 일치한다 (마스킹은 문자 치환).
    line_of = lambda pos: masked.count("\n", 0, pos) + 1

    for m in RRN.finditer(masked):
        val = m.group(0)
        if val in allow:
            continue
        digits = m.group(1) + m.group(2)
        sev = "ERROR" if rrn_checksum_ok(digits) else "WARN"
        hits.append((sev, "주민등록번호" + ("" if sev == "ERROR" else "형(체크섬 불일치)"),
                     val, line_of(m.start())))

    for m in PHONE.finditer(masked):
        if m.group(0) in allow:
            continue
        hits.append(("ERROR", "전화번호", m.group(0), line_of(m.start())))

    if in_clinic(rel):
        for m in EMAIL.finditer(masked):
            if m.group(0) in allow:
                continue
            hits.append(("ERROR", "이메일", m.group(0), line_of(m.start())))
        for m in CHART.finditer(masked):
            if m.group(0) in allow:
                continue
            hits.append(("ERROR", "차트/환자번호", m.group(0), line_of(m.start())))
    return hits


def main() -> int:
    ap = argparse.ArgumentParser(description="환자 식별정보 가드 (error)")
    ap.add_argument("--staged", action="store_true", help="스테이지된 파일만 (pre-commit)")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()

    allow = load_allowlist()
    files = target_files(args.staged)
    errors, warns = [], []

    for rel in files:
        p = REPO / rel
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for sev, rule, val, ln in scan_text(rel, text, allow):
            (errors if sev == "ERROR" else warns).append((rel, ln, rule, val))

    lines = [f"# PII Guard — {date.today().isoformat()}", "",
             f"scanned files : {len(files)}  ({'staged' if args.staged else 'git-tracked'})",
             f"ERRORS        : {len(errors)}",
             f"WARN (모양만) : {len(warns)}", ""]
    if errors:
        lines.append("=== ERROR — 커밋 금지 ===")
        for rel, ln, rule, val in errors:
            lines.append(f"  {rel}:{ln}  [{rule}]  {val}")
    if warns:
        lines.append("")
        lines.append("=== WARN — 모양은 맞으나 검증부호 불일치 (날짜범위 등 오탐 가능) ===")
        for rel, ln, rule, val in warns:
            lines.append(f"  {rel}:{ln}  [{rule}]  {val}")

    if not args.staged:
        try:
            LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
        except OSError:
            pass

    if not args.quiet:
        if errors:
            print(f"    🔒  PII Guard: ❌ {len(errors)}건 — 커밋 금지")
            for rel, ln, rule, val in errors[:10]:
                print(f"          {rel}:{ln}  [{rule}]  {val}")
            print("        의도적으로 실린 값이면 scripts/pii-allowlist.txt 에 사유와 함께 등재")
        else:
            tail = f" · WARN {len(warns)}" if warns else ""
            print(f"    🔒  PII Guard: ✅ {len(files)} files, 위반 0{tail}")
        if not args.staged:
            print(f"          → logs/{LOG.name}")
    return 1 if errors else 0


# ── 회귀 ─────────────────────────────────────────────────────────────────────
# 잡아야 하는 것과 **잡으면 안 되는 것**을 함께 고정한다. 후자가 없으면 error 감사가
# 오탐으로 푸시를 막는 순간 신뢰를 잃고 꺼진다.

def selftest() -> int:
    bad = 0

    def check(name, got, want):
        nonlocal bad
        ok = got == want
        bad += not ok
        print(f"  {'✓' if ok else '✗'} {name:<34} got={got!r:<10} want={want!r}")

    def sev(rel, text):
        h = scan_text(rel, text, set())
        if not h:
            return None
        return "ERROR" if any(s == "ERROR" for s, *_ in h) else "WARN"

    print("── 잡아야 하는 것")
    check("주민번호(체크섬 통과)", sev("note-meeting/a.md", "환자 800101-1234560 내원"), "ERROR")
    check("전화 하이픈", sev("note-meeting/a.md", "연락처 010-1234-5678"), "ERROR")
    check("전화 점", sev("agenda/a.md", "010.9876.5432"), "ERROR")
    check("전화 공백", sev("slides/a.md", "011 234 5678"), "ERROR")
    check("이메일(임상 디렉터리)", sev("note-meeting/a.md", "환자 kim@naver.com"), "ERROR")
    check("차트번호", sev("note-meeting/a.md", "차트번호: 88123"), "ERROR")

    print("── 잡으면 안 되는 것")
    check("DOI(주민번호형)", sev("wiki/a.md", "DOI 10.3760/cma.j.cn112144-20230915-00158"), None)
    check("DOI(전화형)", sev("sources/a.md", "DOI 10.1007/s15010-025-02568-y"), None)
    check("PMID/PMCID", sev("sources/a.md", "PMID 40418274, PMCID PMC12675790"), None)
    check("ISBN", sev("wiki/a.md", "ISBN 978-89-1234-567-0"), None)
    check("교신저자 이메일(sources)", sev("sources/a.md", "corresponding: rich.lamont@louisville.edu"), None)
    check("교신저자 이메일(wiki)", sev("wiki/a.md", "geoh@upenn.edu"), None)
    # 템플릿의 금지 '문구' 자체는 숫자를 동반하지 않으므로 걸리면 안 된다
    check("템플릿 금지문구", sev("note-meeting/_template.md",
                              "환자·직원 식별정보(이름·연락처·차트번호·생년월일) 평문 금지"), None)

    print("── 모양만 맞는 것 → WARN (block 아님)")
    check("날짜범위", sev("wiki/a.md", "기간 202001-2024012 코호트"), "WARN")

    print("── 체크섬")
    check("valid", rrn_checksum_ok("8001011234560"), True)
    check("invalid", rrn_checksum_ok("8001011234561"), False)

    print("── 허용목록")
    check("allowlist 억제", (lambda: "ERROR" if any(
        s == "ERROR" for s, *_ in scan_text("agenda/a.md", "대표번호 010-1234-5678", {"010-1234-5678"})
    ) else None)(), None)

    print(f"\n{'✅ selftest OK' if not bad else f'❌ {bad} case(s) failed'}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
