#!/usr/bin/env python3
"""
LLM Wiki — Frontmatter Lint
Checks every wiki/*.md file (excluding overviews/) for required frontmatter fields.

Usage:
    python3 scripts/lint.py            # full run
    python3 scripts/lint.py --quiet    # errors only, no OK lines
    python3 scripts/lint.py --fix      # future: auto-fix missing fields
"""

import os
import re
import sys
import argparse

WIKI_DIR = "wiki"
SKIP_DIRS = {"_lint", "overviews"}

REQUIRED_FIELDS = [
    "title",
    "authors",
    "year",
    "doi",
    "source",
    "category",
    "confidence",
    "pdf_path",
    "pdf_filename",
]

VALID_CONFIDENCE = {
    "sr+ma", "sr", "rct", "prospective", "retrospective",
    "cross-sectional", "case-report", "in-vivo", "animal",
    "in-vitro", "narrative-review", "consensus",
}


def parse_frontmatter(content: str) -> dict | None:
    """Return frontmatter as raw string dict, or None if missing."""
    m = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not m:
        return None
    fm_text = m.group(1)
    fields = {}
    for line in fm_text.splitlines():
        kv = re.match(r"^(\w+)\s*:\s*(.*)$", line)
        if kv:
            fields[kv.group(1)] = kv.group(2).strip()
    return fields


def lint_file(path: str) -> list[str]:
    errors = []
    with open(path, encoding="utf-8") as f:
        content = f.read()

    fields = parse_frontmatter(content)
    if fields is None:
        return [f"NO FRONTMATTER: {path}"]

    # Check required fields exist
    missing = [f for f in REQUIRED_FIELDS if f not in fields]
    if missing:
        errors.append(f"MISSING {missing}: {path}")

    # Check confidence value is valid
    if "confidence" in fields:
        conf = fields["confidence"].strip('"').strip("'")
        if conf not in VALID_CONFIDENCE:
            errors.append(f"INVALID confidence '{conf}': {path}")

    # Check pdf_path contains the right base dir
    if "pdf_path" in fields:
        if not fields["pdf_path"].startswith("/Users/oracleneo/llm-wiki/papers/"):
            errors.append(f"BAD pdf_path (must be inside /papers/): {path}")

    # Check pdf_filename matches basename of pdf_path
    if "pdf_path" in fields and "pdf_filename" in fields:
        expected_basename = os.path.basename(fields["pdf_path"])
        if fields["pdf_filename"] != expected_basename:
            errors.append(
                f"pdf_filename mismatch (path={expected_basename}, filename={fields['pdf_filename']}): {path}"
            )

    return errors


def main():
    parser = argparse.ArgumentParser(description="LLM Wiki frontmatter lint")
    parser.add_argument("--quiet", action="store_true", help="Only show errors")
    args = parser.parse_args()

    all_errors = []
    ok_count = 0

    for root, dirs, files in os.walk(WIKI_DIR):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for fn in sorted(files):
            if not fn.endswith(".md"):
                continue
            path = os.path.join(root, fn)
            errors = lint_file(path)
            if errors:
                all_errors.extend(errors)
            else:
                ok_count += 1

    # Summary
    total = ok_count + len(all_errors)
    status = "✅" if not all_errors else "❌"
    print(f"{status}  OK: {ok_count}   ERRORS: {len(all_errors)}   TOTAL: {total}")

    if all_errors:
        print()
        for e in all_errors:
            print(f"  {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
