#!/usr/bin/env python3
"""
log-deviation.py — subagent deviation logger (Rule-of-Three feeder)

Usage:
    python3 scripts/log-deviation.py <stem> <type> "<description>"

Deviation types — pick the CLOSEST one; `other` is a last resort, not a default.
(If you are about to log `other`, re-read this list first. As of 2026-07-17 a
reclassification found 87 of 92 `other` rows belonged to a type below — the
rule-of-three trigger was blind for months because everything landed in `other`.)

  -- full-text retrieval outcome (mutually exclusive, pick by WHY the body is missing)
    empty-pmc-text       PMC record exists but get_full_text_article returned an EMPTY body
    partial-pmc-text     PMC body came back but INCOMPLETE — truncated mid-section, symbols
                         dropped by extraction, or suspiciously short (desc = what's missing
                         + whether Results/tables survived)
    abstract-only        No body ever existed to fetch: paywalled/landing-page PDF, or
                         metadata-only. Built from structured abstract (full_text: false).

  -- duplicate handling (mutually exclusive)
    duplicate-skip       Same paper already held; skipped, no new page (desc = matched stem
                         + how detected: DOI / byte-identical / title)
    duplicate-distinct   Looked like a duplicate (same author/topic/batch) but CONFIRMED
                         DISTINCT and ingested (desc = what distinguished them)
    doi-conflict         DOI already existed; updated the existing page instead of new ingest
    rename-collision     Artifact renamed rather than removed/skipped (desc = old→new stem
                         + why keeping it was right)

  -- judgment recorded (the call itself is the deviation — log it even if the call was easy)
    supersession-judgment  superseded_by / superseded_scope set, OR explicitly judged "no
                         supersession" (desc = direction + why). Reverse ingest-order counts.
    relation-judgment    A non-obvious relations: edge (esp. contradicts) added or withheld
    category-judgment    Category boundary call where more than one folder was defensible,
                         incl. keeping an imperfect one (desc = chosen vs rejected + why)
    wrong-category       Category was WRONG and got corrected (desc = old→new). Distinct from
                         category-judgment: that one was a defensible call, this one was a fix.
    confidence-judgment  Non-default confidence label (e.g. umbrella graded sr not sr+ma
                         because no new pooled MA); desc = label + reason
    reporting-judgment   How a result was presented without changing its value — direction of
                         OHIP scores, rounding, table vs narrative, author-stated vs raw number
                         carried forward (desc = instrument + what was carried + why)
    evidence-level-judgment  Non-obvious evidence_level: field (e.g. graded as narrative-review
                         despite pooling, or consensus despite RCT-like design); desc = assigned
                         level + why not a higher/lower level

  -- metadata gaps
    no-doi               No DOI in PDF/PubMed; dedup via title/author grep fallback
    date-fallback        No explicit publication date; used acceptance/received date or the
                         YYYY-01-01 fallback (desc = which date + why)

  -- source / tooling problems
    source-data-issue    Internal inconsistency/typo IN THE SOURCE (bad PRISMA counts,
                         mis-typeset number, abstract↔body conflict) reproduced verbatim +
                         flagged, not silently corrected
    qmd-unavailable      qmd MCP timed out / not reachable; used grep/ls fallback
    batch-relation-pending  relations: target not yet in wiki/ at write time (sibling paper
                         in same parallel batch); parent verifies it lands

  -- pipeline
    why-ingested-skipped ## Why Ingested could not be written (desc = reason)
    step-skipped         A pipeline step was skipped (desc = which step + reason)
    other                Genuinely none of the above. Do NOT log non-deviations here
                         ("standard ingest, no deviations" is not a deviation — log nothing).

Appends one row to logs/ingest-deviations.md.
deviation-audit.py reads this file and flags types with >= 3 occurrences.
"""

import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LOG = REPO / "logs" / "ingest-deviations.md"

VALID_TYPES = {
    # full-text retrieval outcome
    "empty-pmc-text", "partial-pmc-text", "abstract-only",
    # duplicate handling
    "duplicate-skip", "duplicate-distinct", "doi-conflict", "rename-collision",
    # judgment recorded
    "supersession-judgment", "relation-judgment", "category-judgment",
    "wrong-category", "confidence-judgment",
    "reporting-judgment", "evidence-level-judgment",
    # metadata gaps
    "no-doi", "date-fallback",
    # source / tooling problems
    "source-data-issue", "qmd-unavailable", "batch-relation-pending",
    # pipeline
    "why-ingested-skipped", "step-skipped", "other",
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
        print(
            f"Warning: unknown type '{dtype}' — logging as 'other'.\n"
            f"'other' is a last resort: it makes the row invisible to the rule-of-three\n"
            f"trigger, which is what deviation-audit.py exists to fire. Valid types:\n"
            + "\n".join(f"    {t}" for t in sorted(VALID_TYPES))
            + "\nSee the docstring at the top of this file for what each one means.",
            file=sys.stderr,
        )
        dtype = "other"

    if not LOG.exists():
        LOG.write_text(HEADER)

    desc_safe = desc.replace("|", "\\|")
    with open(LOG, "a") as f:
        f.write(f"| {today} | {stem} | {dtype} | {desc_safe} |\n")

    print(f"[deviation logged] {today} | {stem} | {dtype}")


if __name__ == "__main__":
    main()
