#!/usr/bin/env python3
"""
LLM Wiki — Orphan Check
Enforces 1:1 matching between papers/*.pdf and sources/*.md.

Rules:
  - Every PDF in papers/ must have a matching sources/{stem}.md
  - Every sources/{stem}.md must have a matching papers/{stem}.pdf
  - Orphan PDFs (no source) should be deleted
  - Orphan sources (no PDF) are a warning — PDF may have been lost

CI behaviour:
  papers/*.pdf is gitignored, so a CI checkout has 0 PDFs while sources/
  has all .md files. The 1:1 check is therefore impossible in CI and
  used to fail every Wiki Lint run. When $CI is set we short-circuit
  with an informational message and exit 0. The local invariant still
  matters — run `python3 scripts/orphan-check.py` on the host before
  pushing.

Usage:
    python3 scripts/orphan-check.py
"""

import os
import sys
import unicodedata

PAPERS_DIR = "papers"
SOURCES_DIR = "sources"


def _stem_nfc(fname: str) -> str:
    """파일명 stem을 NFC 정규화로 반환.

    macOS HFS+/APFS는 한글 파일명을 NFD(자모 분리)로 저장,
    Linux는 NFC(완성형)가 기본. 두 플랫폼에서 동일 set 비교가
    되도록 정규화 후 stem 추출.
    """
    return unicodedata.normalize("NFC", os.path.splitext(fname)[0])


def main():
    pdfs = {
        _stem_nfc(f)
        for f in os.listdir(PAPERS_DIR)
        if f.endswith(".pdf") or f.endswith(".txt")
    }
    srcs = {
        _stem_nfc(f)
        for f in os.listdir(SOURCES_DIR)
        if f.endswith(".md")
    }

    # CI short-circuit: PDFs are gitignored — only .txt pubmed-text files are
    # tracked. This means CI can never see all papers/, making the 1:1 check
    # impossible. Short-circuit unconditionally in CI; the local check enforces
    # the invariant. (Old condition `and not pdfs` broke when .txt files were
    # first tracked: pdfs became non-empty but still incomplete.)
    if os.getenv("CI"):
        print(
            f"ℹ️   CI environment detected — PDFs are gitignored; only "
            f"{len(pdfs)} .txt artifacts tracked vs {len(srcs)} sources. "
            f"Skipping 1:1 check. Run locally to verify papers↔sources match."
        )
        return

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
