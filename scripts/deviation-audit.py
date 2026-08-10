#!/usr/bin/env python3
"""
deviation-audit.py — Rule-of-Three SOP revision trigger

Reads logs/ingest-deviations.md, counts occurrences per type.
Flags any type with >= 3 occurrences as "SOP REVISION CANDIDATE".

Signal only — never blocks. Output goes to logs/{date}_deviation-audit.log.

Usage:
    python3 scripts/deviation-audit.py
"""

import sys
from pathlib import Path
from collections import Counter
from datetime import date

REPO = Path(__file__).resolve().parent.parent
LOG = REPO / "logs" / "ingest-deviations.md"
THRESHOLD = 3


def main():
    if not LOG.exists():
        print("No deviations logged yet. (logs/ingest-deviations.md not found)")
        return 0

    lines = LOG.read_text().splitlines()
    rows = []
    for line in lines:
        if not line.startswith("| 20"):
            continue
        parts = [p.strip() for p in line.split("|")[1:-1]]
        if len(parts) >= 4:
            rows.append({"date": parts[0], "stem": parts[1], "type": parts[2], "desc": parts[3]})

    counts = Counter(r["type"] for r in rows)
    total = len(rows)

    print(f"Total deviations logged: {total}")
    print()

    candidates = []
    for dtype, count in counts.most_common():
        marker = "  ← RULE-OF-THREE: SOP REVISION CANDIDATE" if count >= THRESHOLD else ""
        print(f"  {count:3d}  {dtype}{marker}")
        if count >= THRESHOLD:
            candidates.append((dtype, count))

    if candidates:
        print()
        print("=" * 60)
        print("SOP REVISION CANDIDATES (≥3 occurrences):")
        for dtype, count in candidates:
            # Show the most recent 3 examples for context
            examples = [r for r in rows if r["type"] == dtype][-3:]
            print(f"\n  [{count}x] {dtype}")
            for ex in examples:
                print(f"    {ex['date']}  {ex['stem']}")
                print(f"    → {ex['desc'][:80]}")
        print()
        print("Action: identify root cause, update CLAUDE.md / relevant SKILL.md.")
        print("=" * 60)
    else:
        print(f"\nNo SOP revision candidates (all types < {THRESHOLD} occurrences).")

    return 0


if __name__ == "__main__":
    sys.exit(main())
