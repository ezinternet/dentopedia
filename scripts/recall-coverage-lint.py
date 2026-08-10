#!/usr/bin/env python3
"""
LLM Wiki — Recall Coverage Audit (retention 백로그 신호)

overview 중 recall/{stem}.json 리콜 스펙이 없는 것 = '기억 백로그'.
output-coverage(Express)와 짝을 이루는 retention 축 신호.
forward-only: 신규 overview 저작 시 3문항을 함께 만든다(소급 백필 없음).

Output: logs/{date}_recall-coverage.log
Signal, not gate. 항상 exit 0.
"""

import os
import re
import sys
import glob
from datetime import date

WIKI_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OVERVIEWS_DIR = os.path.join(WIKI_ROOT, "wiki", "overviews")
RECALL_DIR = os.path.join(WIKI_ROOT, "recall")
WIKI_DIR = os.path.join(WIKI_ROOT, "wiki")
LOGS_DIR = os.path.join(WIKI_ROOT, "logs")

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")


def overview_stems() -> set[str]:
    if not os.path.isdir(OVERVIEWS_DIR):
        return set()
    return {os.path.splitext(f)[0] for f in os.listdir(OVERVIEWS_DIR)
            if f.endswith(".md") and not f.startswith("_")}


def recall_stems() -> set[str]:
    if not os.path.isdir(RECALL_DIR):
        return set()
    return {os.path.splitext(os.path.basename(p))[0]
            for p in glob.glob(os.path.join(RECALL_DIR, "*.json"))
            if not os.path.basename(p).startswith("_")}


def inbound_centrality() -> dict[str, int]:
    counts: dict[str, int] = {}
    for root, _, files in os.walk(WIKI_DIR):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            try:
                content = open(os.path.join(root, fn), encoding="utf-8").read()
            except (OSError, UnicodeDecodeError):
                continue
            for m in WIKILINK_RE.finditer(content):
                stem = os.path.basename(m.group(1).strip())
                if "." in stem:
                    stem = os.path.splitext(stem)[0]
                counts[stem] = counts.get(stem, 0) + 1
    return counts


def main() -> int:
    overviews = overview_stems()
    total = len(overviews)
    covered = overviews & recall_stems()
    centrality = inbound_centrality()
    uncovered = sorted(overviews - covered, key=lambda s: (-centrality.get(s, 0), s))

    ratio = (len(covered) / total * 100) if total else 0.0
    today = date.today().isoformat()

    lines = [
        f"# Recall Coverage — {today}",
        f"TOTAL overviews            : {total}",
        f"COVERED (리콜 스펙 존재)   : {len(covered)}  ({ratio:.1f}%)",
        f"UNCOVERED (기억 백로그)    : {len(uncovered)}",
        "",
        f"=== uncovered, 허브순 top 30 (문항 저작 우선순위) ===",
        f"  {'inbound':>7}  stem",
    ]
    for s in uncovered[:30]:
        lines.append(f"  {centrality.get(s, 0):>7}  {s}")
    if len(uncovered) > 30:
        lines.append(f"  ... ({len(uncovered) - 30} more)")

    output = "\n".join(lines) + "\n"
    os.makedirs(LOGS_DIR, exist_ok=True)
    with open(os.path.join(LOGS_DIR, f"{today}_recall-coverage.log"), "w", encoding="utf-8") as f:
        f.write(output)

    print(f"🧠 Recall Coverage: {len(covered)}/{total} overviews 리콜화 "
          f"({ratio:.1f}%), {len(uncovered)} uncovered")
    print(f"    log → logs/{today}_recall-coverage.log")
    return 0


if __name__ == "__main__":
    sys.exit(main())
