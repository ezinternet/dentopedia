#!/usr/bin/env python3
"""
log-deviation.py — subagent deviation logger (Rule-of-Three feeder)

Usage:
    python3 scripts/log-deviation.py <stem> <type> "<description>"

Deviation types:
    empty-pmc-text       PMC full_text returned empty; built from abstract only
    abstract-only        Paywalled/landing-page PDF or metadata-only (no full text); built
                         from structured abstract (full_text: false). Distinct from
                         empty-pmc-text: here the artifact itself never had a body.
    doi-conflict         DOI already existed; updated existing page instead of new ingest
    no-doi               No DOI printed in PDF/PubMed; dedup via title/author grep fallback
    duplicate-skip       Byte- or DOI-identical PDF matched an existing page; skipped, no
                         new page written (desc = matched stem + how detected)
    wrong-category       Initial category judgment was wrong; corrected (desc = old→new)
    confidence-judgment  Non-default confidence label chosen (e.g. umbrella review graded
                         sr not sr+ma because no new pooled MA); desc = label + reason
    batch-relation-pending  relations: target not yet in wiki/ at write time (sibling paper
                         in same parallel batch); parent verifies it lands
    qmd-unavailable      qmd MCP timed out / not reachable in subagent; used grep/ls fallback
    source-data-issue    Internal inconsistency/typo in the source (bad PRISMA counts,
                         mis-typeset number) reproduced verbatim + flagged, not corrected
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
    "empty-pmc-text", "abstract-only", "doi-conflict", "no-doi",
    "duplicate-skip", "wrong-category", "confidence-judgment",
    "batch-relation-pending", "qmd-unavailable", "source-data-issue",
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
