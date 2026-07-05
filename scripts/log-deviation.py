#!/usr/bin/env python3
"""
log-deviation.py — subagent deviation logger (Rule-of-Three feeder)

Usage:
    python3 scripts/log-deviation.py <stem> <type> "<description>"

Deviation types:
    empty-pmc-text       PMC full_text returned empty; built from abstract only
    doi-conflict         DOI already existed; updated existing page instead of new ingest
    wrong-category       Initial category judgment was wrong; corrected (desc = old→new)
    why-ingested-skipped ## Why Ingested could not be written (desc = reason)
    step-skipped         A pipeline step was skipped (desc = which step + reason)
    rename-collision     PDF stem collision resolved (desc = old→new stem)
    other                Anything else that deviated from SOP

Appends one row to logs/ingest-deviations.md.
deviation-audit.py reads this file and flags types with >= 3 occurrences.
"""

import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LOG = REPO / "logs" / "ingest-deviations.md"

VALID_TYPES = {
    "empty-pmc-text", "doi-conflict", "wrong-category",
    "why-ingested-skipped", "step-skipped", "rename-collision", "other",
}

HEADER = (
    "# Ingest Deviations\n\n"
    "Logged by subagents at deviation time. "
    "`deviation-audit.py` flags types with ≥3 occurrences as SOP revision candidates.\n\n"
    "| date | stem | type | description |\n"
    "|------|------|------|-------------|\n"
)


def main():
    if len(sys.argv) < 4:
        print("Usage: log-deviation.py <stem> <type> <description>", file=sys.stderr)
        sys.exit(1)

    stem = sys.argv[1]
    dtype = sys.argv[2]
    desc = " ".join(sys.argv[3:])
    today = date.today().isoformat()

    if dtype not in VALID_TYPES:
        print(f"Warning: unknown type '{dtype}', logging as 'other'", file=sys.stderr)
        dtype = "other"

    if not LOG.exists():
        LOG.write_text(HEADER)

    desc_safe = desc.replace("|", "\\|")
    with open(LOG, "a") as f:
        f.write(f"| {today} | {stem} | {dtype} | {desc_safe} |\n")

    print(f"[deviation logged] {today} | {stem} | {dtype}")


if __name__ == "__main__":
    main()
