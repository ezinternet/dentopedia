#!/usr/bin/env python3
"""
LLM Wiki — Category Overflow Audit

For each wiki/<category>/ folder, count:
  - total papers  : .md files in that category (excluding overviews/_template/index)
  - unsynthesized : papers whose stem is NOT referenced from any
                    wiki/overviews/ page

A category with ≥ 5 unsynthesized papers is flagged as an
OVERVIEW CANDIDATE — i.e. enough material has accumulated that
a synthesis page would be high-value.

This is SIGNAL-ONLY. No agenda files are created automatically.
The original (안전 모드) decision was that hard gates / auto-creation
risk burnout and orphan-agenda churn. Use this log to decide
when to manually `cp agenda/_template.md` and start synthesizing.

Output: logs/{date}_category-overflow.log

Usage:
    python3 scripts/category-overflow.py
"""

import os
import re
import sys
from datetime import date

WIKI_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI_DIR = os.path.join(WIKI_ROOT, "wiki")
OVERVIEWS_DIR = os.path.join(WIKI_DIR, "overviews")
LOGS_DIR = os.path.join(WIKI_ROOT, "logs")

CANDIDATE_THRESHOLD = 5
SKIP_DIRS = {"overviews", "_lint"}
SKIP_FILES = {"index.md", "_template.md", ".gitkeep"}

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")


def extract_stem(target: str) -> str:
    t = target.strip()
    if "." in os.path.basename(t):
        t = os.path.splitext(t)[0]
    return os.path.basename(t)


def collect_overview_links() -> set[str]:
    stems: set[str] = set()
    if not os.path.isdir(OVERVIEWS_DIR):
        return stems
    for fname in os.listdir(OVERVIEWS_DIR):
        if not fname.endswith(".md"):
            continue
        path = os.path.join(OVERVIEWS_DIR, fname)
        try:
            with open(path, encoding="utf-8") as f:
                content = f.read()
        except (OSError, UnicodeDecodeError):
            continue
        for m in WIKILINK_RE.finditer(content):
            stems.add(extract_stem(m.group(1)))
    return stems


def collect_category_papers() -> dict[str, list[str]]:
    """Return {category_rel_path: [stem, ...]} for every category under wiki/."""
    cats: dict[str, list[str]] = {}
    for root, dirs, files in os.walk(WIKI_DIR):
        # Prune
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        rel = os.path.relpath(root, WIKI_DIR)
        if rel == ".":
            continue
        stems = []
        for f in files:
            if not f.endswith(".md") or f in SKIP_FILES:
                continue
            stems.append(os.path.splitext(f)[0])
        if stems:
            cats[rel] = sorted(stems)
    return cats


def main() -> int:
    overview_stems = collect_overview_links()
    cats = collect_category_papers()

    rows: list[tuple[str, int, int, int]] = []  # (cat, total, synth, unsynth)
    for cat, stems in sorted(cats.items()):
        total = len(stems)
        synth = sum(1 for s in stems if s in overview_stems)
        unsynth = total - synth
        rows.append((cat, total, synth, unsynth))

    candidates = [r for r in rows if r[3] >= CANDIDATE_THRESHOLD]
    candidates.sort(key=lambda r: r[3], reverse=True)

    today = date.today().isoformat()
    lines = [
        f"# Category Overflow — {today}",
        f"CANDIDATE_THRESHOLD: ≥{CANDIDATE_THRESHOLD} unsynthesized papers in a category",
        f"CATEGORIES total       : {len(rows)}",
        f"CATEGORIES candidates  : {len(candidates)}",
        "",
        f"=== overview candidates (most unsynthesized first) ===",
        f"  {'category':<40} {'total':>5} {'synth':>6} {'unsynth':>8}",
    ]
    for cat, total, synth, unsynth in candidates:
        lines.append(f"  {cat:<40} {total:>5} {synth:>6} {unsynth:>8}")

    lines.append("")
    lines.append(f"=== all categories ===")
    lines.append(f"  {'category':<40} {'total':>5} {'synth':>6} {'unsynth':>8}")
    for cat, total, synth, unsynth in rows:
        marker = " ◄" if unsynth >= CANDIDATE_THRESHOLD else ""
        lines.append(f"  {cat:<40} {total:>5} {synth:>6} {unsynth:>8}{marker}")

    output = "\n".join(lines) + "\n"

    os.makedirs(LOGS_DIR, exist_ok=True)
    log_path = os.path.join(LOGS_DIR, f"{today}_category-overflow.log")
    with open(log_path, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"📂  Category Overflow: {len(candidates)}/{len(rows)} categories "
          f"have ≥{CANDIDATE_THRESHOLD} unsynthesized papers")
    print(f"    log → {os.path.relpath(log_path, WIKI_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
