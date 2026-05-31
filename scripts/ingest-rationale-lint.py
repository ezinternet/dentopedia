#!/usr/bin/env python3
"""
LLM Wiki — Ingest Rationale Lint

Enforces that every NEW source (ingested on or after CUTOFF_DATE) contains
a "## Why Ingested" section with at least one wikilink to an existing
wiki page. Sources older than the cutoff are exempt.

Why this exists:
    See agenda/2026-05-26_synthesis-enforcement-setup.md and the
    "ingest가 자기 자신을 합성하도록 강제하는 구조" thesis.
    A 1-line rationale at ingest time turns later overview synthesis
    from a cold start into a warm assembly.

Required structure of the section:
    ## Why Ingested
    (1-2 sentences explaining *why* this paper was ingested)
    (at least one [[wiki/category/stem]] link showing what it
     conflicts with, reinforces, or fills a gap in)

Output: logs/{date}_ingest-rationale-lint.log

Usage:
    python3 scripts/ingest-rationale-lint.py
    python3 scripts/ingest-rationale-lint.py --strict   # exit 1 on any error
"""

import os
import re
import sys
import argparse
from datetime import date, datetime

WIKI_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCES_DIR = os.path.join(WIKI_ROOT, "sources")
LOGS_DIR = os.path.join(WIKI_ROOT, "logs")

# Cutoff: sources with mtime >= this date are subject to the rule.
# Older sources are grandfathered (no backfill — see agenda).
CUTOFF_DATE = date(2026, 5, 27)
CUTOFF_TS = datetime.combine(CUTOFF_DATE, datetime.min.time()).timestamp()

WHY_HEADER_RE = re.compile(r"^##\s+Why Ingested\s*$", re.MULTILINE)
WIKILINK_RE = re.compile(r"\[\[[^\]]+\]\]")


def extract_why_section(content: str) -> str | None:
    """Return the body of '## Why Ingested' (until next ## header), or None."""
    m = WHY_HEADER_RE.search(content)
    if not m:
        return None
    start = m.end()
    # Find next top-level header (## ...) after this section
    rest = content[start:]
    next_h = re.search(r"^##\s+", rest, re.MULTILINE)
    body = rest[: next_h.start()] if next_h else rest
    return body.strip()


def lint_source(path: str) -> list[str]:
    errors: list[str] = []
    try:
        with open(path, encoding="utf-8") as f:
            content = f.read()
    except (OSError, UnicodeDecodeError) as e:
        return [f"READ ERROR ({e}): {path}"]

    body = extract_why_section(content)
    if body is None:
        errors.append(f"MISSING '## Why Ingested' section: {path}")
        return errors

    if len(body) < 20:
        errors.append(f"'## Why Ingested' too short (<20 chars): {path}")

    if not WIKILINK_RE.search(body):
        errors.append(
            f"'## Why Ingested' has no [[wikilink]] to a related wiki page: {path}"
        )

    return errors


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true",
                    help="Exit 1 if any errors found")
    args = ap.parse_args()

    if not os.path.isdir(SOURCES_DIR):
        print(f"❌  sources/ not found at {SOURCES_DIR}")
        return 1

    checked = 0
    skipped = 0
    errors: list[str] = []

    for fname in sorted(os.listdir(SOURCES_DIR)):
        if not fname.endswith(".md"):
            continue
        path = os.path.join(SOURCES_DIR, fname)
        mtime = os.path.getmtime(path)
        if mtime < CUTOFF_TS:
            skipped += 1
            continue
        checked += 1
        errors.extend(lint_source(path))

    today = date.today().isoformat()
    ok = checked - sum(1 for e in errors if not e.startswith("'## Why Ingested' too short"))

    lines = [
        f"# Ingest Rationale Lint — {today}",
        f"CUTOFF: {CUTOFF_DATE.isoformat()} (sources mtime ≥ this date are checked)",
        f"GRANDFATHERED (skipped): {skipped}",
        f"CHECKED               : {checked}",
        f"ERRORS                : {len(errors)}",
        "",
    ]
    if errors:
        lines.append("=== errors ===")
        for e in errors:
            lines.append(f"  {e}")

    output = "\n".join(lines) + "\n"

    os.makedirs(LOGS_DIR, exist_ok=True)
    log_path = os.path.join(LOGS_DIR, f"{today}_ingest-rationale-lint.log")
    with open(log_path, "w", encoding="utf-8") as f:
        f.write(output)

    status = "✅" if not errors else "❌"
    print(f"{status}  Ingest Rationale: checked {checked}, skipped {skipped} "
          f"(pre-{CUTOFF_DATE}), errors {len(errors)}")
    print(f"    log → {os.path.relpath(log_path, WIKI_ROOT)}")

    return 1 if (errors and args.strict) else 0


if __name__ == "__main__":
    sys.exit(main())
