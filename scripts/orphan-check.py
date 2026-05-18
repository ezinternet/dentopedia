#!/usr/bin/env python3
"""
LLM Wiki — Orphan Check
Enforces 1:1 matching between papers/*.pdf and sources/*.md.

Rules:
  - Every PDF in papers/ must have a matching sources/{stem}.md
  - Every sources/{stem}.md must have a matching papers/{stem}.pdf
  - Orphan PDFs (no source) should be deleted
  - Orphan sources (no PDF) are a warning — PDF may have been lost

Usage:
    python3 scripts/orphan-check.py
"""

import os
import sys

PAPERS_DIR = "papers"
SOURCES_DIR = "sources"


def main():
    pdfs = {
        os.path.splitext(f)[0]
        for f in os.listdir(PAPERS_DIR)
        if f.endswith(".pdf")
    }
    srcs = {
        os.path.splitext(f)[0]
        for f in os.listdir(SOURCES_DIR)
        if f.endswith(".md")
    }

    orphan_pdfs = sorted(pdfs - srcs)   # PDF exists, no source → delete
    orphan_srcs = sorted(srcs - pdfs)   # Source exists, no PDF → warn

    has_errors = bool(orphan_pdfs or orphan_srcs)

    if not has_errors:
        print(f"✅  1:1 match — {len(pdfs)} PDFs, {len(srcs)} sources")
        return

    if orphan_pdfs:
        print(f"❌  ORPHAN PDFs ({len(orphan_pdfs)}) — source file missing, delete these:")
        for stem in orphan_pdfs:
            print(f"    papers/{stem}.pdf")

    if orphan_srcs:
        print(f"⚠️   ORPHAN sources ({len(orphan_srcs)}) — PDF missing:")
        for stem in orphan_srcs:
            print(f"    sources/{stem}.md")

    sys.exit(1)


if __name__ == "__main__":
    main()
