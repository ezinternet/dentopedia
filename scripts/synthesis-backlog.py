#!/usr/bin/env python3
"""
LLM Wiki — Synthesis Backlog Audit

For each source in sources/, check whether it (or its corresponding
wiki page) is referenced from at least one overview in wiki/overviews/.
Sources not referenced anywhere are "unsynthesized backlog".

Stale threshold: 30+ days unsynthesized → "stale source".

Output: logs/{date}_synthesis-backlog.log

Usage:
    python3 scripts/synthesis-backlog.py            # write log + print summary
    python3 scripts/synthesis-backlog.py --stdout   # also dump full list to stdout
"""

import os
import re
import sys
import argparse
from datetime import date, datetime, timedelta

WIKI_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCES_DIR = os.path.join(WIKI_ROOT, "sources")
OVERVIEWS_DIR = os.path.join(WIKI_ROOT, "wiki", "overviews")
LOGS_DIR = os.path.join(WIKI_ROOT, "logs")

STALE_DAYS = 30
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")


def extract_stem(wikilink_target: str) -> str:
    """Normalize a wikilink target to its bare stem.
    e.g. 'implants/jung-2023-foo' → 'jung-2023-foo'
         'wiki/implants/jung-2023-foo' → 'jung-2023-foo'
         'jung-2023-foo' → 'jung-2023-foo'
    """
    t = wikilink_target.strip()
    # Strip any extension
    if "." in os.path.basename(t):
        t = os.path.splitext(t)[0]
    return os.path.basename(t)


def collect_overview_links() -> set[str]:
    """Read every overview markdown and collect all wikilink stems referenced."""
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


def collect_sources() -> list[tuple[str, float]]:
    """Return [(stem, mtime), ...] for every source in sources/."""
    out: list[tuple[str, float]] = []
    if not os.path.isdir(SOURCES_DIR):
        return out
    for fname in os.listdir(SOURCES_DIR):
        if not fname.endswith(".md"):
            continue
        stem = os.path.splitext(fname)[0]
        mtime = os.path.getmtime(os.path.join(SOURCES_DIR, fname))
        out.append((stem, mtime))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stdout", action="store_true",
                    help="Also dump full unsynthesized list to stdout")
    args = ap.parse_args()

    overview_stems = collect_overview_links()
    sources = collect_sources()
    total = len(sources)

    unsynthesized: list[tuple[str, float]] = [
        (stem, mt) for stem, mt in sources if stem not in overview_stems
    ]
    unsynthesized.sort(key=lambda x: x[1])  # oldest first

    now = datetime.now().timestamp()
    stale_cutoff = now - STALE_DAYS * 86400
    stale = [(s, m) for s, m in unsynthesized if m < stale_cutoff]

    linked = total - len(unsynthesized)
    ratio = (linked / total * 100) if total else 0.0

    today = date.today().isoformat()
    lines = [
        f"# Synthesis Backlog — {today}",
        f"TOTAL sources           : {total}",
        f"LINKED to ≥1 overview   : {linked}  ({ratio:.1f}%)",
        f"UNSYNTHESIZED           : {len(unsynthesized)}",
        f"STALE (≥{STALE_DAYS}d unsynthesized): {len(stale)}",
        "",
    ]

    if unsynthesized:
        lines.append(f"=== unsynthesized (oldest first, top 50) ===")
        for stem, mt in unsynthesized[:50]:
            age = (now - mt) / 86400
            tag = "STALE" if mt < stale_cutoff else "    "
            lines.append(f"  {tag} {age:5.1f}d  {stem}")
        if len(unsynthesized) > 50:
            lines.append(f"  ... ({len(unsynthesized) - 50} more)")

    output = "\n".join(lines) + "\n"

    os.makedirs(LOGS_DIR, exist_ok=True)
    log_path = os.path.join(LOGS_DIR, f"{today}_synthesis-backlog.log")
    with open(log_path, "w", encoding="utf-8") as f:
        f.write(output)

    # Summary to stdout
    print(f"📊  Synthesis Backlog: {len(unsynthesized)}/{total} unsynthesized "
          f"({ratio:.1f}% linked), {len(stale)} stale ≥{STALE_DAYS}d")
    print(f"    log → {os.path.relpath(log_path, WIKI_ROOT)}")

    if args.stdout:
        print()
        print(output)

    # Exit code: 0 always. Backlog is a signal, not an error.
    return 0


if __name__ == "__main__":
    sys.exit(main())
