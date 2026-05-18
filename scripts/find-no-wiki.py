#!/usr/bin/env python3
"""
LLM Wiki — Find Papers Without Wiki Page
Lists all PDFs in papers/ that don't have a corresponding wiki/**/{stem}.md.

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

    no_wiki = sorted(papers - wiki_stems)

    if not no_wiki:
        print(f"✅  All {len(papers)} papers have wiki pages.")
        return

    print(f"📄  Papers without wiki page: {len(no_wiki)}")
    for stem in no_wiki:
        print(f"    {stem}")


if __name__ == "__main__":
    main()
