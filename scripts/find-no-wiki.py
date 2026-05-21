#!/usr/bin/env python3
"""
LLM Wiki — Find Papers Without Wiki Page
Lists all PDFs in papers/ that don't have a corresponding wiki/**/{stem}.md.

CI behaviour:
  papers/*.pdf is gitignored, so a CI checkout has 0 PDFs. Without a guard
  the script silently reports "All 0 papers have wiki pages" — a false
  green that hides the case the script exists to catch. When $CI is set
  AND papers/ is empty we short-circuit with an informational message.
  Run locally to actually verify papers->wiki coverage.

Usage:
    python3 scripts/find-no-wiki.py
"""

import os

PAPERS_DIR = "papers"
WIKI_DIR = "wiki"


def main():
    papers = {
        os.path.splitext(f)[0]
        for f in os.listdir(PAPERS_DIR)
        if f.endswith(".pdf")
    }

    wiki_stems = {
        os.path.splitext(fn)[0]
        for root, dirs, files in os.walk(WIKI_DIR)
        for fn in files
        if fn.endswith(".md")
    }

    # CI short-circuit: papers/ is empty under gitignore, so the diff is
    # always vacuously empty. Surface the limitation instead of pretending.
    if os.getenv("CI") and not papers:
        print(
            f"ℹ️   CI environment detected — papers/ is empty (gitignored). "
            f"Cannot verify papers->wiki coverage in CI. "
            f"({len(wiki_stems)} wiki pages present.) Run locally to verify."
        )
        return

    no_wiki = sorted(papers - wiki_stems)

    if not no_wiki:
        print(f"✅  All {len(papers)} papers have wiki pages.")
        return

    print(f"📄  Papers without wiki page: {len(no_wiki)}")
    for stem in no_wiki:
        print(f"    {stem}")


if __name__ == "__main__":
    main()
