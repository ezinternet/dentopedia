#!/usr/bin/env python3
"""
LLM Wiki — Overview Catalogue Lint (signal, non-blocking)

wiki/overviews/*.md 각 페이지가 index.md의 **카탈로그 목록 항목**(`- [[overviews/{stem}]]`)
으로 등재됐는지 검사한다. 즉 "색인을 훑어 내려가며 브라우징하는 독자가 이 overview를
발견할 수 있는가".

왜 link-integrity.py로 충분하지 않은가 (중복 감사가 아닌 이유):
  link-integrity는 index.md 안의 `[[wikilink]]`를 **위치 무관하게** 수집해
  "pages MISSING from index"를 판정한다. 따라서 다른 항목의 설명문 안에 한 번
  언급되기만 해도 통과한다 — 도달 가능성(reachability)은 맞는 검사다.
  이 스크립트는 더 좁은 성질을 본다: **자기 목록 항목을 갖는가**(catalogue entry).

  실측 근거 (2026-07-18): `patient-consultation-communication-protocol`은 2026-06-03
  생성 후 약 6주간 카탈로그 bullet 항목이 없이 blockquote 언급만 있었고,
  link-integrity 로그 42개 어디에도 등장하지 않았다(설계상 정상 — 언급이 있었으므로).
  동시점 관례는 242개 중 239개가 bullet 항목, blockquote-only는 그 1개뿐이었다.
  즉 규칙은 "모든 overview는 bullet 카탈로그 항목을 갖는다"이고, 위반은 이 검사로만 보인다.

검사 항목:
  (1) WARN  overview 파일에 카탈로그 bullet 항목이 없음 (blockquote-only / 미언급 포함)
  (2) WARN  카탈로그 bullet 항목이 실존하지 않는 overview를 가리킴 (dangling)
  (3) INFO  bullet은 있고 blockquote 언급도 있는 이중 배치 — 관례상 정상(토픽 섹션 + 카탈로그)

Output: logs/{date}_overview-catalogue.log

Usage:
    python3 scripts/overview-catalogue-lint.py
    python3 scripts/overview-catalogue-lint.py --stdout

Signal, non-blocking — 항상 exit 0. (AUDITS.md: signal, not gate)
"""

from __future__ import annotations
import re
import sys
import argparse
from datetime import date
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
OVERVIEWS_DIR = WIKI_ROOT / "wiki" / "overviews"
INDEX = WIKI_ROOT / "index.md"
LOGS_DIR = WIKI_ROOT / "logs"

# [[overviews/stem]] / [[overviews/stem#anchor]] / [[overviews/stem|alias]]
OVERVIEW_LINK_RE = re.compile(r"\[\[overviews/([^\]|#]+?)(?:[#|][^\]]*)?\]\]")
# 목록 항목만: 선행 공백 허용, '-' 또는 '*' 로 시작
BULLET_PREFIX_RE = re.compile(r"^\s*[-*]\s")
QUOTE_PREFIX_RE = re.compile(r"^\s*>")

# 카탈로그 등재가 면제되는 파일 (stem 하드코딩이 필요한 예외가 생기면 여기에)
EXEMPT: set[str] = set()

# 카테고리 랜딩 페이지(`wiki/overviews/overviews.md` 등)는 카탈로그의 *대상*이 아니라
# 카탈로그를 **여는 문**이라 자기 자신을 목록에 넣지 않는다. stem을 EXEMPT에 박으면
# 다음 랜딩 페이지에서 같은 오탐이 되살아나므로, 규약(frontmatter)으로 판별한다 —
# `source: navigation` 또는 tags에 `category-index`. 리포 전역 120개가 이 규약을 쓴다.
FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)


def is_landing_page(path: Path) -> bool:
    m = FM_RE.match(path.read_text(encoding="utf-8"))
    if not m:
        return False
    fm = m.group(1)
    if re.search(r"^source:\s*navigation\s*$", fm, re.MULTILINE | re.IGNORECASE):
        return True
    tags = re.search(r"^tags:\s*(.*)$", fm, re.MULTILINE)
    return bool(tags and "category-index" in tags.group(1))


def collect_overview_files() -> set[str]:
    if not OVERVIEWS_DIR.is_dir():
        return set()
    stems = {f.stem for f in OVERVIEWS_DIR.glob("*.md") if not is_landing_page(f)}
    return stems - EXEMPT


def scan_index() -> tuple[set[str], set[str], set[str]]:
    """index.md를 줄 단위로 훑어 형식별 overview 참조를 분류."""
    bullet: set[str] = set()
    quote: set[str] = set()
    other: set[str] = set()
    if not INDEX.exists():
        return bullet, quote, other
    for line in INDEX.read_text(encoding="utf-8").splitlines():
        stems = OVERVIEW_LINK_RE.findall(line)
        if not stems:
            continue
        if BULLET_PREFIX_RE.match(line):
            bucket = bullet
        elif QUOTE_PREFIX_RE.match(line):
            bucket = quote
        else:
            bucket = other
        bucket.update(s.strip() for s in stems)
    return bullet, quote, other


def main() -> int:
    ap = argparse.ArgumentParser(description="Overview catalogue lint (signal)")
    ap.add_argument("--stdout", action="store_true", help="로그 본문을 stdout에도 출력")
    args = ap.parse_args()

    files = collect_overview_files()
    bullet, quote, other = scan_index()

    missing = sorted(files - bullet)              # (1) 카탈로그 항목 없음
    dangling = sorted(bullet - files)             # (2) 실존하지 않는 대상
    dual = sorted(files & bullet & quote)         # (3) 이중 배치 (정상)
    # 카탈로그엔 없지만 어딘가 언급은 된 것 — link-integrity가 통과시키는 사각지대
    mentioned_not_catalogued = sorted(set(missing) & (quote | other))
    never_mentioned = sorted(set(missing) - (quote | other))

    LOGS_DIR.mkdir(exist_ok=True)
    log_path = LOGS_DIR / f"{date.today().isoformat()}_overview-catalogue.log"

    L: list[str] = []
    L.append(f"# Overview Catalogue — {date.today().isoformat()}")
    L.append(f"overview files            : {len(files)}")
    L.append(f"catalogue bullet entries  : {len(bullet)}")
    L.append(f"  MISSING from catalogue  : {len(missing)}")
    L.append(f"    ├ mentioned elsewhere : {len(mentioned_not_catalogued)}   (link-integrity는 통과시킴)")
    L.append(f"    └ never mentioned     : {len(never_mentioned)}")
    L.append(f"  dangling bullet entries : {len(dangling)}")
    L.append(f"  (info) dual placement   : {len(dual)}   (토픽 섹션 blockquote + 카탈로그 — 정상)")
    L.append("")

    if mentioned_not_catalogued:
        L.append("=== ⚠ 카탈로그 항목 없음 — 다른 항목 설명문에서만 언급됨 ===")
        L.append("    (도달은 가능하나 목록을 훑는 독자에겐 안 보임. link-integrity가 못 잡는 부류)")
        for s in mentioned_not_catalogued:
            L.append(f"    {s}")
        L.append("")
    if never_mentioned:
        L.append("=== ⚠ 카탈로그 항목 없음 — index.md에 전혀 언급되지 않음 ===")
        for s in never_mentioned:
            L.append(f"    {s}")
        L.append("")
    if dangling:
        L.append("=== ⚠ 카탈로그 항목이 실존하지 않는 overview를 가리킴 ===")
        for s in dangling:
            L.append(f"    {s}")
        L.append("")
    if dual:
        L.append(f"=== (info) 이중 배치 {len(dual)}건 — 관례상 정상 ===")
        for s in dual:
            L.append(f"    {s}")
        L.append("")
    if not missing and not dangling:
        L.append("✅  모든 overview가 카탈로그에 1:1 등재됨.")
        L.append("")

    body = "\n".join(L) + "\n"
    log_path.write_text(body, encoding="utf-8")

    icon = "✅" if (not missing and not dangling) else "⚠️ "
    print(
        f"{icon}  Overview Catalogue: {len(files) - len(missing)}/{len(files)} 등재, "
        f"missing {len(missing)}, dangling {len(dangling)}"
    )
    print(f"      log → logs/{log_path.name}")
    if args.stdout:
        print()
        print(body)
    return 0  # signal — never blocks


if __name__ == "__main__":
    sys.exit(main())
