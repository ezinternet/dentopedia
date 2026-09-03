#!/usr/bin/env python3
"""
self-claim-lint.py — overview가 본문에 적은 **자기 수치**가 실제와 맞는지 (signal)

T4 of agenda/2026-09-03_audit-gap-closure.md

왜 있는가
---------
overview 287편 중 **127편이 "N papers 종합"이라는 자기 수치를 본문에 적고 있다.**
그런데 인제스트는 위키링크만 밀어넣고 **문장의 숫자는 아무도 고치지 않는다.**
실측 2026-09-03: 23편이 실제와 어긋났고, 방향은 대부분 주장 < 실제다
(`keratinized-mucosa` 주장 10 / 실제 24 — 원래 10편이던 페이지에 wound-healing
축이 뒤에 붙어 24편이 됐는데 요약 첫 문장만 10에 멈춰 있었다).

이건 `lint`(frontmatter)·`content-lint`(섹션 존재)·`overview-coverage-lint`(인용률)
어디에도 안 걸리고, **독자가 페이지에서 가장 먼저 신뢰하는 문장**이다.

억제가 설계의 전부다 (실측으로 세 번 좁혔다)
--------------------------------------------
본문의 "N papers/studies"는 대부분 **문헌 서술**이다 — 전수 2,735건 중 자기서술은
극소수. 세 겹으로 좁힌다:

  ① **위치** — `## Three-line Summary` 섹션 안에서만 본다. 이 섹션은 정의상
     페이지 자신에 대한 서술이다. 초안은 본문 전체를 봤고, 그러면
     "Ke 2024 SR+MA(11편)" 같은 문헌 인용이 전부 후보가 된다.
  ② **괄호 제거** — 자기서술은 자기 구성을 괄호로 밝힌다:
     `Synthesis of six papers (1 systematic synthesis of 92 studies, 4 narrative …)`.
     괄호를 안 지우면 **안쪽의 92를 페이지의 주장으로 읽는다** (실제로 읽었다 —
     주장 92 / 링크 6이라는 최대 이상치가 이 오탐이었다).
  ③ **어휘가 아니라 문형** — 초안은 "숫자 근처에 SR/RCT가 있으면 문헌"이라는
     가드를 뒀는데 **거꾸로였다**: 자기서술이 자기 구성을 SR·RCT로 밝히는 것이
     오히려 흔하다 (`Synthesis of 10 papers (1 SR+MA, 2 SR …)`). 그 가드를 버리고
     자기서술 동사(synthesizes / synthesis of / covers / draws on)로만 잡는다.

무엇과 비교하는가 — 기준 2개, 둘 다와 어긋날 때만 WARN
-------------------------------------------------------
`source_papers:` 필드와 본문 위키링크 중 `sources/`에 실존하는 것의 수, 둘 다 센다.
**어느 한쪽과라도 맞으면 WARN을 내지 않는다.** 두 기준이 서로 다른 이유가 있기
때문이다 — overview-volatility-audit이 2026-08-02에 실측했듯 구성 논문을
`source_papers`로만 읽으면 안 된다(262편 중 90편만 보유, 나머지는 본문 링크뿐).
어느 해석으로도 설명이 안 될 때만 신호를 낸다.

두 기준이 서로 어긋나는 것 자체는 INFO로 따로 낸다 — `source_papers` 필드가
낡았다는 뜻이라 그것도 알 가치가 있지만, 주장의 잘못은 아니다.

`--fix`는 없다. 숫자를 기계가 고쳐 쓰면 문장 맥락(구성 내역·괄호 설명)과 어긋난다.

Usage:
    python3 scripts/self-claim-lint.py [--selftest]
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OVERVIEWS = REPO / "wiki" / "overviews"
SOURCES = REPO / "sources"
LOG = REPO / "logs" / f"{date.today().isoformat()}_self-claim.log"

# 허용 오차: ±2편 또는 15%. 반올림·"약 N편"·구성 재분류를 흡수한다.
def within_tolerance(claim: int, actual: int) -> bool:
    return abs(claim - actual) <= max(2, claim * 0.15)


WORDS = {w: i for i, w in enumerate(
    "zero one two three four five six seven eight nine ten eleven twelve thirteen "
    "fourteen fifteen sixteen seventeen eighteen nineteen twenty".split())}

_NUM = r"(\d{1,3}|" + "|".join(WORDS) + r")"
EN_CLAIM = re.compile(
    r"\b(?:synthesi[sz]es?|synthesis\s+of|covers|draws\s+on)\s+(?:the\s+)?"
    + _NUM + r"\s+(?:papers|studies|constituents?)\b", re.I)
KO_CLAIM = re.compile(r"(\d{1,3})\s*편\s*(?:기반\s*)?종합")
PARENS = re.compile(r"\([^()]*\)")
SOURCE_PAPERS = re.compile(r"^source_papers:\s*\n((?:\s*-\s+.*\n)+)", re.M)
WIKILINK = re.compile(r"\[\[([^\]|#]+)")


def to_int(tok: str) -> int:
    return int(tok) if tok.isdigit() else WORDS[tok.lower()]


def section(text: str, heading: str):
    m = re.search(r"^##\s*" + re.escape(heading) + r"\s*$", text, re.M)
    if not m:
        return None
    nxt = re.search(r"^##\s", text[m.end():], re.M)
    return text[m.end(): m.end() + nxt.start()] if nxt else text[m.end():]


def strip_parens(s: str) -> str:
    """중첩 괄호까지 공백으로 치환 (길이 보존 — 오프셋이 어긋나지 않게)."""
    prev = None
    while prev != s:
        prev, s = s, PARENS.sub(lambda m: " " * len(m.group()), s)
    return s


def extract(text: str, sources: set):
    """→ (en_claim, ko_claim, source_papers_n, linked_papers_n)"""
    en_sec = section(text, "Three-line Summary")
    ko_sec = section(text, "세줄요약")
    m = EN_CLAIM.search(strip_parens(en_sec)) if en_sec else None
    en = to_int(m.group(1)) if m else None
    m2 = KO_CLAIM.search(strip_parens(ko_sec)) if ko_sec else None
    ko = int(m2.group(1)) if m2 else None

    sp = SOURCE_PAPERS.search(text)
    spn = len(re.findall(r"^\s*-\s+", sp.group(1), re.M)) if sp else None
    links = {l.strip().split("/")[-1] for l in WIKILINK.findall(text)}
    return en, ko, spn, len(links & sources)


def main() -> int:
    ap = argparse.ArgumentParser(description="overview 자기서술 수치 감사 (signal)")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()

    sources = {p.stem for p in SOURCES.glob("*.md")}
    pages = sorted(OVERVIEWS.glob("*.md"))
    warns, infos, enko = [], [], []
    claimed = checked = ko_only_n = 0

    for p in pages:
        text = p.read_text(encoding="utf-8", errors="replace")
        en, ko, spn, links = extract(text, sources)
        if en is None and ko is None:
            continue
        claimed += 1

        if en is not None and ko is not None and en != ko:
            enko.append((p.stem, en, ko))

        # 주장은 **EN(Three-line Summary)에서만** 읽는다. 한국어 `N편 종합`은
        # 문형이 훨씬 자유로워 검증이 안 된다 — 실측 상위 3건이 각각
        # "SR/MA 3편 종합"(구성이 SR 3편이라는 뜻), "재사용 논문 8편 + …"(합산
        # 표현), 문헌 인용이었다. KO 폴백을 넣으면 WARN이 23 → 39로 늘지만
        # 늘어난 16건이 전부 검증 불가라, 상위 목록이 오탐으로 채워져 감사
        # 자체가 안 읽히게 된다. KO는 EN↔KO 대조에만 쓴다.
        if en is None:
            ko_only_n += 1
            continue
        claim = en
        checked += 1
        bases = [(n, v) for n, v in (("source_papers", spn), ("링크논문", links)) if v]
        if not bases:
            continue
        if not any(within_tolerance(claim, v) for _, v in bases):
            warns.append((p.stem, claim, spn, links))
        elif len(bases) == 2 and not within_tolerance(bases[0][1], bases[1][1]):
            infos.append((p.stem, claim, spn, links))

    lines = [f"# Self-Claim Lint — {date.today().isoformat()}", "",
             f"overviews            : {len(pages)}",
             f"자기 수치 주장 보유  : {claimed}",
             f"  ├ EN 주장 (검사 대상): {checked}",
             f"  └ KO만 보유 (미검사) : {ko_only_n}   ← 한국어 문형은 검증 불가라 대상 밖",
             f"WARN (두 기준 모두와 어긋남) : {len(warns)}",
             f"INFO (기준끼리 어긋남)       : {len(infos)}",
             f"EN↔KO 내부 불일치            : {len(enko)}", ""]
    if warns:
        lines.append("=== WARN — 주장이 어느 기준으로도 설명되지 않음 ===")
        lines.append(f"  {'overview':<58} {'주장':>4} {'sp':>5} {'링크':>5} {'차':>5}")
        for stem, c, sp, lk in sorted(warns, key=lambda r: -abs(r[1] - r[3])):
            lines.append(f"  {stem:<58} {c:>4} {str(sp):>5} {lk:>5} {lk - c:>+5}")
    if enko:
        lines.append("")
        lines.append("=== EN↔KO 내부 불일치 (같은 페이지가 두 언어로 다른 수를 말함) ===")
        for stem, en, ko in enko:
            lines.append(f"  {stem:<58} EN {en:>3} vs KO {ko:>3}")
    if infos:
        lines.append("")
        lines.append("=== INFO — 주장은 한쪽과 맞으나 두 기준이 서로 어긋남 (source_papers 노후 의심) ===")
        for stem, c, sp, lk in infos:
            lines.append(f"  {stem:<58} 주장 {c:>3} | sp {str(sp):>4} | 링크 {lk:>3}")

    try:
        LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
    except OSError:
        pass

    print(f"    🔢  Self-claim: {checked}편 검사 (주장 {claimed}편 중 KO전용 {ko_only_n} 제외) · "
          f"WARN {len(warns)} · EN↔KO {len(enko)} · INFO {len(infos)}")
    if warns:
        for stem, c, sp, lk in sorted(warns, key=lambda r: -abs(r[1] - r[3]))[:3]:
            print(f"          {stem[:52]:52} 주장 {c} → 실제 {lk}")
    print(f"          → logs/{LOG.name}")
    return 0


# ── 회귀 ─────────────────────────────────────────────────────────────────────
# 이 감사는 억제가 전부다. **잡으면 안 되는 것**이 케이스의 절반인 이유.

def selftest() -> int:
    bad = 0

    def check(name, got, want):
        nonlocal bad
        ok = got == want
        bad += not ok
        print(f"  {'✓' if ok else '✗'} {name:<36} got={got!r:<14} want={want!r}")

    def en_of(body):
        return extract(f"## Three-line Summary\n\n{body}\n\n## Results\n", set())[0]

    print("── 자기서술 추출")
    check("숫자", en_of("Synthesis of 21 papers on X."), 21)
    check("영어 수사", en_of("Synthesis of six papers organized around Y."), 6)
    check("covers", en_of("This page covers 24 papers."), 24)
    check("draws on", en_of("Draws on 9 studies."), 9)
    # 자기서술이 자기 구성을 괄호로 밝히는 형태 — 괄호 안 숫자를 읽으면 안 된다
    check("괄호 안 숫자 무시",
          en_of("Synthesis of six papers (1 systematic synthesis of 92 studies, 4 narrative)."), 6)
    check("구성 내역 SR/RCT 포함",
          en_of("Synthesis of 10 papers (2 umbrella meta-analyses, 3 SR+MAs, 1 SR)."), 10)

    print("── 잡으면 안 되는 것")
    body = "## Results\n\nKe 2024 SR+MA (11 studies) found membrane thinning.\n"
    check("Three-line 밖 문헌서술", extract(body, set())[0], None)
    check("요약 없는 페이지", extract("# x\n\ntext\n", set())[0], None)

    print("── 허용 오차")
    check("±2 이내", within_tolerance(10, 12), True)
    check("±2 초과·15% 이내", within_tolerance(40, 45), True)
    check("둘 다 초과", within_tolerance(10, 24), False)

    print("── EN↔KO")
    doc = "## Three-line Summary\n\nSynthesis of 6 papers.\n\n## 세줄요약\n\n3편 종합: x\n\n## Results\n"
    en, ko, _, _ = extract(doc, set())
    check("EN/KO 각각 추출", (en, ko), (6, 3))

    print(f"\n{'✅ selftest OK' if not bad else f'❌ {bad} case(s) failed'}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
