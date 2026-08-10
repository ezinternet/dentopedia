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
  papers/*.pdf is gitignored, so a CI checkout never has the full set of
  PDFs that sources/ was ingested against. Only the pubmed-text `.txt`
  artifacts are committed, so papers/ is no longer reliably *empty* in
  CI (it used to be, before any pubmed-text papers existed) — checking
  "CI and not pdfs" stopped short-circuiting once the first `.txt` was
  committed, and the 1:1 check silently started failing every Wiki Lint
  run again. The 1:1 check is fundamentally impossible in CI regardless
  of how many `.txt` files happen to be present, so we short-circuit
  unconditionally whenever $CI is set. The local invariant still
  matters — run `python3 scripts/orphan-check.py` on the host before
  pushing.

Usage:
    python3 scripts/orphan-check.py
"""

import os
import re
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


def _source_collection(fname: str) -> str:
    """sources/{fname}의 source_collection 값을 반환. 없으면 빈 문자열."""
    path = os.path.join(SOURCES_DIR, fname)
    try:
        with open(path, encoding="utf-8") as f:
            content = f.read(2000)
    except OSError:
        return ""
    m = re.search(r"^source_collection:\s*(.+)$", content, re.MULTILINE)
    if m:
        return m.group(1).strip().strip('"').strip("'")
    return ""


def main():
    pdfs = {
        _stem_nfc(f)
        for f in os.listdir(PAPERS_DIR)
        if f.endswith(".pdf") or f.endswith(".txt")
    }

    # pubmed-abstract sources는 로컬 아티팩트(PDF/txt)가 없는 초록 전용 인제스트 — 1:1 체크 면제
    all_src_fnames = [f for f in os.listdir(SOURCES_DIR) if f.endswith(".md")]
    abstract_only_stems = {
        _stem_nfc(f)
        for f in all_src_fnames
        if _source_collection(f) == "pubmed-abstract"
    }
    srcs = {_stem_nfc(f) for f in all_src_fnames} - abstract_only_stems

    # CI short-circuit: PDFs are gitignored, so a CI checkout never has the
    # full papers/ set sources/ was ingested against. This holds regardless
    # of how many pubmed-text .txt artifacts happen to be committed, so we
    # skip unconditionally in CI rather than gating on "papers/ is empty".
    if os.getenv("CI"):
        print(
            f"ℹ️   CI environment detected — papers/*.pdf is gitignored, so "
            f"the 1:1 check is not meaningful here. Skipping. "
            f"({len(srcs)} sources, {len(pdfs)} papers/ artifacts present.) "
            f"Run locally to verify papers↔sources match."
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
