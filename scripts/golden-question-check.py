#!/usr/bin/env python3
"""
golden-question-check.py — 답변 경로의 회귀 감사 (signal)

T5 of agenda/2026-09-03_audit-gap-closure.md

왜 있는가
---------
감사 24개 중 **이 위키의 산출물(답변)을 보는 것이 하나도 없다.** 페이지가 다 옳고
(`lint`·`content-lint`), 인덱스가 신선해도(`retrieval-health`), "임상 질문 → 엉뚱한
페이지"는 전 감사 초록불로 통과한다. 구조가 건강한 것과 **찾아지는 것**은 다른 축이다.

이 감사는 고정 문항을 검색에 태워 **기대 페이지가 상위 K에 잡히는지만** 본다.
답의 내용은 판정하지 않는다 — LLM도 웹도 쓰지 않으므로 Rule #1과 무관하다.

lex와 vec를 나눈 이유 (둘 다 실측)
-----------------------------------
  - `qmd search`(BM25) 1회 **0.24초** / `qmd vsearch`(벡터) 1회 **19.6초**.
    벡터는 호출마다 임베딩 모델을 콜드스타트한다. 30문항이면 7초 vs 10분이라,
    일일 감사에 벡터를 넣으면 감사 전체가 벡터 대기시간이 된다.
  - 게다가 두 축은 **질의 형태가 다르다**. 실측: 한국어 *전체 문장*을 BM25에 넣으면
    `No results found`이고(조사·의문형이 토큰을 죽인다), 같은 뜻의 *키워드*는 잘 잡힌다.
    영어 본문 + 한국어 세줄요약이라는 이 리포의 구조 때문이다.
    그래서 문항마다 `lex`(키워드형)와 `q`(자연어형)를 함께 갖고, 기본은 lex,
    `--vec`을 주면 자연어형을 벡터로 돌린다. CLAUDE.md가 규정한 두 용법
    (lex=정확 매치, vec=개념 질문)에 각각 대응한다.

실패를 어떻게 읽는가
--------------------
실패는 **문서 또는 인덱스**가 깨졌다는 신호다. 어느 쪽인지 판별하려고, 실패 시
기대 페이지가 인덱스에 존재하기는 하는지(`qmd get`)를 함께 찍는다.
  - 파일 없음        → 페이지가 삭제·개명됨 (link-integrity가 놓친 경우)
  - 인덱스에 없음    → 재색인 누락 (retrieval-health와 교차 확인)
  - 둘 다 있는데 미검출 → 진짜 검색 품질 저하 (본문이 바뀌었거나 경쟁 문서가 늘었다)

**문항을 통과시키려고 고치지 말 것.** 통과하도록 다듬은 문항은 아무것도 측정하지
않는다. 실패는 조사 대상이지 수정 대상이 아니다 — 문항이 임상적으로 틀렸을 때만 고친다.

Usage:
    python3 scripts/golden-question-check.py [--vec] [--top-k 5] [--selftest]
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
FIXTURE = REPO / "scripts" / "golden-questions.json"
LOG = REPO / "logs" / f"{date.today().isoformat()}_golden-questions.log"

# `qmd search` 출력 첫 줄: qmd://<collection>/<path>.md:<line> #<docid>
HIT_LINE = re.compile(r"^qmd://[^/]+/(\S+?\.md):")


def run_query(mode: str, query: str, timeout: int):
    cmd = ["qmd", "vsearch" if mode == "vec" else "search", query]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, cwd=REPO)
    except (OSError, subprocess.TimeoutExpired):
        return None
    if r.returncode != 0:
        return None
    stems = []
    for line in r.stdout.splitlines():
        m = HIT_LINE.match(line)
        if m:
            stem = Path(m.group(1)).stem
            if stem not in stems:
                stems.append(stem)
    return stems


def diagnose(stem: str) -> str:
    """실패 원인을 문서/인덱스 축으로 가른다."""
    on_disk = any((REPO / "wiki").rglob(f"{stem}.md"))
    try:
        r = subprocess.run(["qmd", "get", f"wiki/overviews/{stem}.md"],
                           capture_output=True, text=True, timeout=30, cwd=REPO)
        indexed = r.returncode == 0 and bool(r.stdout.strip())
    except (OSError, subprocess.TimeoutExpired):
        indexed = False
    if not on_disk:
        return "파일 없음 (삭제·개명 의심)"
    if not indexed:
        return "인덱스에 없음 (재색인 누락 — retrieval-health 교차확인)"
    return "문서·인덱스 정상인데 미검출 (검색 품질 저하)"


def main() -> int:
    ap = argparse.ArgumentParser(description="검색 회귀 감사 (signal)")
    ap.add_argument("--vec", action="store_true", help="자연어형을 벡터로 (느림: 1문항 ~20초)")
    ap.add_argument("--top-k", type=int, default=None)
    ap.add_argument("--fixture", default=None, help="다른 문항 파일 (회귀 경로 테스트용)")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()

    def finish(head: str, lines: list) -> int:
        print(head)
        try:
            LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
            print(f"          → logs/{LOG.name}")
        except OSError:
            pass
        return 0

    if shutil.which("qmd") is None:
        return finish("    🎯  Golden questions: SKIP — qmd CLI 없음",
                      ["SKIP: qmd CLI not installed"])
    try:
        fx = json.loads(Path(args.fixture or FIXTURE).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        return finish(f"    🎯  Golden questions: SKIP — 문항 파일 읽기 실패 ({e})",
                      [f"SKIP: {e}"])

    mode = "vec" if args.vec else "lex"
    k = args.top_k or fx.get("top_k", 5)
    qs = fx.get("questions", [])
    timeout = 120 if mode == "vec" else 30

    known = {k: v for k, v in (fx.get("known_miss") or {}).items() if not k.startswith("_")}
    hits, misses, errors = [], [], []
    for item in qs:
        query = item.get("q" if mode == "vec" else "lex") or item.get("q")
        got = run_query(mode, query, timeout)
        if got is None:
            errors.append((item["id"], query))
            continue
        top = got[:k]
        if any(e in top for e in item["expect"]):
            hits.append(item["id"])
        else:
            misses.append((item["id"], query, item["expect"], top[:3]))

    # 도입 시점의 기존 실패는 REGRESSION과 분리한다. 늘 빨간 감사는 곧 안 읽히고,
    # 안 읽히는 감사는 없는 것과 같다 — decay 308건이 그렇게 죽었다. 다만 억제는
    # **뮤트가 아니라 이동**이라 known도 계속 세어 출력한다.
    regressions = [m for m in misses if m[0] not in known]
    known_misses = [m for m in misses if m[0] in known]
    recovered = [q for q in known if q in hits]

    total = len(hits) + len(misses)
    rate = (len(hits) / total * 100) if total else 0.0
    lines = [f"# Golden Question Check — {date.today().isoformat()}", "",
             f"mode        : {mode}  (top-{k})",
             f"questions   : {len(qs)}",
             f"HIT         : {len(hits)}",
             f"MISS        : {len(misses)}  (REGRESSION {len(regressions)} · 알려진 실패 {len(known_misses)})",
             f"RECOVERED   : {len(recovered)}  {sorted(recovered) if recovered else ''}",
             f"ERROR       : {len(errors)}  (검색 실행 실패)",
             f"hit rate    : {rate:.0f}%", ""]
    for label, bucket in (("REGRESSION — 새로 실패한 문항 (조사 대상)", regressions),
                          ("알려진 실패 — 도입 시점부터 (뮤트 아님, 분리 집계)", known_misses)):
        if not bucket:
            continue
        lines.append(f"=== {label} ===")
        for qid, query, exp, top in bucket:
            lines.append(f"  [{qid}] {query}")
            lines.append(f"        기대 : {', '.join(exp)}")
            lines.append(f"        상위 : {', '.join(top) if top else '(결과 없음)'}")
            if qid in known:
                lines.append(f"        기존 : {known[qid]}")
            else:
                lines.append(f"        진단 : {diagnose(exp[0])}")
        lines.append("")
    if errors:
        lines.append("")
        lines.append("=== ERROR — 검색이 실행되지 않음 ===")
        for qid, query in errors:
            lines.append(f"  [{qid}] {query}")

    head = (f"    🎯  Golden questions ({mode}): {len(hits)}/{total} 적중 ({rate:.0f}%)"
            + (f" · ⚠ REGRESSION {len(regressions)}" if regressions else "")
            + (f" · 알려진실패 {len(known_misses)}" if known_misses else "")
            + (f" · RECOVERED {len(recovered)}" if recovered else "")
            + (f" · ERROR {len(errors)}" if errors else ""))
    return finish(head, lines)


def selftest() -> int:
    bad = 0

    def check(name, got, want):
        nonlocal bad
        ok = got == want
        bad += not ok
        print(f"  {'✓' if ok else '✗'} {name:<34} got={got!r:<26} want={want!r}")

    print("── 출력 파싱")
    line = "qmd://wiki/sinus-lift/lateral/lim-2011-sinus-membrane-perforation.md:13 #03aba4"
    m = HIT_LINE.match(line)
    check("경로 추출", Path(m.group(1)).stem if m else None, "lim-2011-sinus-membrane-perforation")
    check("본문 줄 무시", HIT_LINE.match("Title: Three-line Summary"), None)
    check("점수 줄 무시", HIT_LINE.match("Score:  95%"), None)

    print("── 문항 파일")
    try:
        fx = json.loads(Path(args.fixture or FIXTURE).read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        print(f"  ✗ 문항 파일 로드 실패: {e}")
        return 1
    qs = fx.get("questions", [])
    check("문항 수 ≥10", len(qs) >= 10, True)
    check("id 중복 없음", len({q["id"] for q in qs}) == len(qs), True)
    check("모든 문항 lex+q 보유", all(q.get("lex") and q.get("q") for q in qs), True)
    ov = {p.stem for p in (REPO / "wiki" / "overviews").glob("*.md")}
    dangling = [e for q in qs for e in q["expect"] if e not in ov]
    check("기대 stem 전부 실존", dangling, [])

    print(f"\n{'✅ selftest OK' if not bad else f'❌ {bad} case(s) failed'}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
