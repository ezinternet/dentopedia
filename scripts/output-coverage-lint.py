#!/usr/bin/env python3
"""
LLM Wiki — Output Coverage Audit (Express-leg mirror of synthesis-backlog)

synthesis-backlog는 '입력' 방향(source가 overview에 연결됐나)을 본다.
이 audit는 '출력' 방향을 본다: overview가 downstream 산출물
(slides / interactives / lectures)로 꺼내 쓰였나.

An overview is "covered" if at least one file under slides/, interactives/,
or lectures/ references it via `wiki/overviews/<stem>.md` (source_wiki 등).
Uncovered overviews = Express backlog — 강의·교육 자산으로 전환 안 된 지식.

랭킹: uncovered를 inbound wikilink 수(centrality)로 정렬 → 허브일수록
전환 레버가 크다 (제안 B의 '전환 상위 리스트' 자동 산출).

Output: logs/{date}_output-coverage.log

Usage:
    python3 scripts/output-coverage-lint.py            # write log + summary
    python3 scripts/output-coverage-lint.py --stdout   # also dump full list
    python3 scripts/output-coverage-lint.py --top N    # top-N uncovered (default 30)

Signal, not gate. Always exits 0.
"""

import os
import re
import sys
import argparse
from datetime import date

WIKI_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OVERVIEWS_DIR = os.path.join(WIKI_ROOT, "wiki", "overviews")
WIKI_DIR = os.path.join(WIKI_ROOT, "wiki")
LOGS_DIR = os.path.join(WIKI_ROOT, "logs")

# downstream 산출물 폴더 (존재하는 것만 스캔)
OUTPUT_DIRS = ["slides", "interactives", "lectures"]

OVERVIEW_REF_RE = re.compile(r"wiki/overviews/([A-Za-z0-9._-]+?)\.md")
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")


def overview_stems() -> set[str]:
    if not os.path.isdir(OVERVIEWS_DIR):
        return set()
    return {os.path.splitext(f)[0] for f in os.listdir(OVERVIEWS_DIR)
            if f.endswith(".md") and not f.startswith("_")}


def covered_stems() -> dict[str, list[str]]:
    """overview stem → [출력물 파일명, ...] 로 어디에 꺼내 썼는지 매핑."""
    cov: dict[str, list[str]] = {}
    for d in OUTPUT_DIRS:
        base = os.path.join(WIKI_ROOT, d)
        if not os.path.isdir(base):
            continue
        for root, _, files in os.walk(base):
            for fn in files:
                if not (fn.endswith(".md") or fn.endswith(".html")):
                    continue
                path = os.path.join(root, fn)
                try:
                    with open(path, encoding="utf-8") as f:
                        content = f.read()
                except (OSError, UnicodeDecodeError):
                    continue
                for m in OVERVIEW_REF_RE.finditer(content):
                    cov.setdefault(m.group(1), []).append(f"{d}/{fn}")
    return cov


def inbound_centrality() -> dict[str, int]:
    """wiki/ 전체를 훑어 각 stem이 wikilink 타깃으로 몇 번 지목됐는지."""
    counts: dict[str, int] = {}
    for root, _, files in os.walk(WIKI_DIR):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            try:
                with open(os.path.join(root, fn), encoding="utf-8") as f:
                    content = f.read()
            except (OSError, UnicodeDecodeError):
                continue
            for m in WIKILINK_RE.finditer(content):
                stem = os.path.basename(m.group(1).strip())
                if "." in stem:
                    stem = os.path.splitext(stem)[0]
                counts[stem] = counts.get(stem, 0) + 1
    return counts


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stdout", action="store_true")
    ap.add_argument("--top", type=int, default=30)
    args = ap.parse_args()

    overviews = overview_stems()
    total = len(overviews)
    cov = covered_stems()
    centrality = inbound_centrality()

    covered = {s for s in overviews if s in cov}
    uncovered = sorted(
        (overviews - covered),
        key=lambda s: (-centrality.get(s, 0), s),
    )

    ratio = (len(covered) / total * 100) if total else 0.0
    today = date.today().isoformat()

    lines = [
        f"# Output Coverage — {today}",
        f"TOTAL overviews            : {total}",
        f"COVERED (≥1 산출물)        : {len(covered)}  ({ratio:.1f}%)",
        f"UNCOVERED (Express backlog): {len(uncovered)}",
        "",
        f"=== uncovered, 허브순 top {args.top} (전환 우선순위) ===",
        f"  {'inbound':>7}  stem",
    ]
    for s in uncovered[:args.top]:
        lines.append(f"  {centrality.get(s, 0):>7}  {s}")
    if len(uncovered) > args.top:
        lines.append(f"  ... ({len(uncovered) - args.top} more)")

    output = "\n".join(lines) + "\n"

    os.makedirs(LOGS_DIR, exist_ok=True)
    log_path = os.path.join(LOGS_DIR, f"{today}_output-coverage.log")
    with open(log_path, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"📤  Output Coverage: {len(covered)}/{total} overviews 산출물화 "
          f"({ratio:.1f}%), {len(uncovered)} uncovered")
    print(f"    log → {os.path.relpath(log_path, WIKI_ROOT)}")

    if args.stdout:
        print()
        print(output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
