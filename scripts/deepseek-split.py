#!/usr/bin/env python3
"""
LLM Wiki — DeepSeek Ingest Splitter
Splits a DeepSeek v2 preprocessing dump into sources/*.md + wiki/{category}/*.md.

Why this exists: the DeepSeek hybrid workflow's remaining token cost was that
Claude had to READ the whole dump and RE-EMIT both pages through Write. This
script does the mechanical half — parse, validate, substitute __CATEGORY__,
write both files — so Claude only reads a short report and makes the judgment
calls (category, Why Ingested, relations, supersession).

Guard rails (why it refuses rather than warns):
  - `[[wikilink]]` in a DeepSeek body means invented stems → link-integrity.py
    breakage. DeepSeek does not know this repo's pages, so any wikilink it
    wrote is a hallucination. Hard error.
  - stem must be identical across the two file headers, `source:`, and
    `pdf_filename` — a mismatch silently breaks orphan-check.py's 1:1 rule.
  - required frontmatter mirrors scripts/lint.py so a written page can't fail
    lint after the fact.

Two phases:

  1. REPORT (default — no --category):
       python3 scripts/deepseek-split.py <dump.md>
     Parses, validates, prints ===CLAUDE-BRIEF===, and does the two greps
     Claude would otherwise spend tokens on:
       • Step-0 dedup — this paper's DOI against sources/
       • REF_DOIS    — which cited papers we already hold (exact DOI match)

  2. WRITE (with --category):
       python3 scripts/deepseek-split.py <dump.md> --category implants/mbl
       python3 scripts/deepseek-split.py <dump.md> --category implants/mbl --pdf ~/Downloads/x.pdf
     Substitutes __CATEGORY__, writes both pages, optionally copies the PDF to
     papers/{stem}.pdf, and prints the index.md line ready to insert.

Still Claude's job after this runs: `## Why Ingested`, `## Related Papers`,
`relations:`, supersession, index.md, lint, commit, qmd.

Usage:
  python3 scripts/deepseek-split.py <dump.md> [--category CAT] [--pdf PATH]
                                              [--dry-run] [--force] [--new-category]
Exit codes: 0 ok · 1 validation failure · 2 usage/IO error
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCES_DIR = os.path.join(REPO, "sources")
WIKI_DIR = os.path.join(REPO, "wiki")
PAPERS_DIR = os.path.join(REPO, "papers")

PLACEHOLDER = "__CATEGORY__"
FILL_MARKER = "<!-- CLAUDE-FILL -->"

FILE_HEADER = re.compile(r"^={2,}\s*FILE:\s*(.+?)\s*={2,}\s*$")
BRIEF_HEADER = re.compile(r"^={2,}\s*CLAUDE-BRIEF\s*={2,}\s*$")

# Mirrors scripts/lint.py REQUIRED_FIELDS + artifact fields (PDF branch).
WIKI_REQUIRED = [
    "title", "authors", "year", "date", "doi", "source", "category",
    "evidence_level", "pdf_path", "pdf_filename", "source_collection", "tags",
]
SOURCES_REQUIRED = [
    "title", "authors", "year", "doi", "category",
    "pdf_path", "pdf_filename", "source_collection",
]

# Mirrors scripts/lint.py VALID_CONFIDENCE (study types DeepSeek may pick).
VALID_EVIDENCE = {
    "sr+ma", "sr", "rct", "prospective", "retrospective", "cross-sectional",
    "case-report", "in-vivo", "animal", "in-vitro", "narrative-review",
    "consensus",
}

DOI_RE = re.compile(r"10\.\d{4,9}/[^\s\"'<>,;)\]]+")


# ---------------------------------------------------------------- parsing


def strip_outer_fence(text: str) -> str:
    """Drop a code fence wrapping the whole dump (DeepSeek sometimes adds one)."""
    lines = text.splitlines()
    start, end = 0, len(lines)
    while start < end and not lines[start].strip():
        start += 1
    while end > start and not lines[end - 1].strip():
        end -= 1
    if start < end and lines[start].strip().startswith("```"):
        start += 1
        if end > start and lines[end - 1].strip() == "```":
            end -= 1
    return "\n".join(lines[start:end])


def split_blocks(text: str) -> tuple[list[tuple[str, str]], str]:
    """Return ([(declared_path, body)], brief_text)."""
    files: list[tuple[str, list[str]]] = []
    brief: list[str] = []
    current: list[str] | None = None
    in_brief = False

    for line in text.splitlines():
        m = FILE_HEADER.match(line)
        if m:
            in_brief = False
            current = []
            files.append((m.group(1), current))
            continue
        if BRIEF_HEADER.match(line):
            in_brief = True
            current = None
            continue
        if in_brief:
            brief.append(line)
        elif current is not None:
            current.append(line)

    return [(p, "\n".join(b).strip() + "\n") for p, b in files], "\n".join(brief).strip()


def parse_brief(brief: str) -> tuple[dict[str, str], list[tuple[str, str]]]:
    """Return (scalar fields, [(doi, note)]) from the CLAUDE-BRIEF block."""
    fields: dict[str, str] = {}
    refs: list[tuple[str, str]] = []
    in_refs = False
    for line in brief.splitlines():
        if re.match(r"^REF_DOIS\s*:", line):
            in_refs = True
            continue
        if in_refs:
            m = DOI_RE.search(line)
            if m:
                note = line.split("—", 1)[1].strip() if "—" in line else ""
                refs.append((m.group(0).rstrip("."), note))
            continue
        kv = re.match(r"^([A-Z_]+)\s*:\s*(.*)$", line)
        if kv:
            fields[kv.group(1)] = kv.group(2).strip()
    return fields, refs


def frontmatter(body: str) -> dict[str, str]:
    m = re.match(r"^---\n(.*?)\n---", body, re.DOTALL)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"^([A-Za-z0-9_-]+)\s*:\s*(.*)$", line)
        if kv:
            out[kv.group(1)] = kv.group(2).strip()
    return out


# ---------------------------------------------------------------- repo greps


def source_doi_map() -> dict[str, str]:
    """{normalized doi: stem} over sources/*.md frontmatter."""
    out: dict[str, str] = {}
    if not os.path.isdir(SOURCES_DIR):
        return out
    for name in os.listdir(SOURCES_DIR):
        if not name.endswith(".md"):
            continue
        path = os.path.join(SOURCES_DIR, name)
        try:
            with open(path, encoding="utf-8") as fh:
                head = "".join(next(fh, "") for _ in range(25))
        except OSError:
            continue
        for line in head.splitlines():
            if line.startswith("doi:"):
                m = DOI_RE.search(line)
                if m:
                    out.setdefault(m.group(0).rstrip(".").lower(), name[:-3])
                break
    return out


# ---------------------------------------------------------------- validation


def validate(files: list[tuple[str, str]], brief: dict[str, str]) -> tuple[list[str], dict]:
    errors: list[str] = []
    info: dict = {}

    src = next((f for f in files if f[0].startswith("sources/")), None)
    wik = next((f for f in files if f[0].startswith("wiki/")), None)
    if not src:
        errors.append("missing '===FILE: sources/{stem}.md===' block")
    if not wik:
        errors.append("missing '===FILE: wiki/__CATEGORY__/{stem}.md===' block")
    if errors:
        return errors, info

    for path, body in (src, wik):
        for i, line in enumerate(body.splitlines(), 1):
            if "[[" in line:
                errors.append(
                    f"{path}:{i}: contains a [[wikilink]] — DeepSeek does not know this "
                    f"repo's stems, so this is invented. Remove it (Claude adds links)."
                )
        for bad in ("relations:", "superseded_by:"):
            if re.search(rf"^{re.escape(bad)}", body, re.MULTILINE):
                errors.append(f"{path}: contains '{bad}' — Claude's field, not DeepSeek's")

    src_path, src_body = src
    wik_path, wik_body = wik

    stem = os.path.basename(src_path)[:-3]
    info["stem"] = stem
    if PLACEHOLDER in stem:
        errors.append(f"sources path still holds {PLACEHOLDER}: {src_path}")
    if "{stem}" in src_path or "{stem}" in wik_path:
        errors.append("literal '{stem}' left in a FILE header — DeepSeek did not substitute")

    wik_stem = os.path.basename(wik_path)[:-3]
    if wik_stem != stem:
        errors.append(f"stem mismatch: sources '{stem}' vs wiki '{wik_stem}'")
    if PLACEHOLDER not in wik_path:
        errors.append(f"wiki path has no {PLACEHOLDER} — expected wiki/{PLACEHOLDER}/{stem}.md")
    info["wiki_path_template"] = wik_path

    src_fm, wik_fm = frontmatter(src_body), frontmatter(wik_body)
    if not src_fm:
        errors.append("sources block has no YAML frontmatter")
    if not wik_fm:
        errors.append("wiki block has no YAML frontmatter")

    for label, fm, required in (("sources", src_fm, SOURCES_REQUIRED),
                                ("wiki", wik_fm, WIKI_REQUIRED)):
        for field in required:
            if field not in fm:
                errors.append(f"{label}: missing frontmatter field '{field}'")

    ev = wik_fm.get("evidence_level", "")
    if ev and ev not in VALID_EVIDENCE:
        errors.append(f"wiki: evidence_level '{ev}' not in vocabulary (INGEST.md Step 3)")

    if wik_fm.get("source") and wik_fm["source"] != f"{stem}.md":
        errors.append(f"wiki: source '{wik_fm['source']}' != '{stem}.md'")
    for label, fm in (("sources", src_fm), ("wiki", wik_fm)):
        want = f"{stem}.pdf"
        if fm.get("pdf_filename") and fm["pdf_filename"] != want:
            errors.append(f"{label}: pdf_filename '{fm['pdf_filename']}' != '{want}'")
        expect_path = f"{PAPERS_DIR}/{want}"
        if fm.get("pdf_path") and fm["pdf_path"] != expect_path:
            errors.append(f"{label}: pdf_path '{fm['pdf_path']}' != '{expect_path}'")

    for label, body in (("sources", src_body), ("wiki", wik_body)):
        if FILL_MARKER not in body:
            errors.append(f"{label}: no {FILL_MARKER} — Why Ingested / Related Papers "
                          f"must be left for Claude")
    for label, body, heads in (
        ("sources", src_body, ["## Why Ingested", "## Three-line Summary", "## 세줄요약"]),
        ("wiki", wik_body, ["## Three-line Summary", "## 세줄요약", "## Summary",
                            "## Results", "## Related Papers"]),
    ):
        for h in heads:
            if not re.search(rf"^{re.escape(h)}\s*$", body, re.MULTILINE):
                errors.append(f"{label}: missing section '{h}'")

    doi = ""
    m = DOI_RE.search(src_fm.get("doi", "") or brief.get("DOI", ""))
    if m:
        doi = m.group(0).rstrip(".")
    info["doi"] = doi
    info["src"] = (src_path, src_body)
    info["wiki"] = (wik_path, wik_body)
    return errors, info


# ---------------------------------------------------------------- reporting


def report(info: dict, brief: dict, refs: list[tuple[str, str]]) -> None:
    doi_map = source_doi_map()
    print(f"STEM            {info['stem']}")
    print(f"DOI             {info.get('doi') or 'none'}")
    for k in ("EVIDENCE_LEVEL", "PUB_DATE", "N_TOTAL", "FOLLOW_UP",
              "DOC_TYPE", "RETRACTION_FLAG", "PMID", "PMCID"):
        if brief.get(k):
            print(f"{k:<15} {brief[k]}")
    print()

    print("— Step 0 dedup (this DOI in sources/)")
    doi = (info.get("doi") or "").lower()
    hit = doi_map.get(doi)
    if not doi:
        print("  no DOI — run title+first-author dedup instead (INGEST.md Step 0 fallback)")
    elif hit:
        print(f"  ⚠ DUPLICATE — already held as sources/{hit}.md → update that page, do NOT ingest")
    else:
        print("  clean — no existing page with this DOI")
    if brief.get("RETRACTION_FLAG", "no").lower().startswith("y"):
        print("  ⚠ RETRACTION_FLAG=yes → default is DO NOT INGEST (INGEST.md Step 0)")
    if brief.get("DOC_TYPE", "").strip() in ("abstract-only", "landing-page"):
        print(f"  ⚠ DOC_TYPE={brief['DOC_TYPE']} → add full_text: false + caveat (Step 1-A)")
    print()

    print(f"— REF_DOIS already in the wiki ({len(refs)} cited DOIs checked)")
    held = [(d, doi_map[d.lower()], n) for d, n in refs if d.lower() in doi_map]
    if held:
        for d, stem, note in held:
            print(f"  ✓ {stem}" + (f"  — {note}" if note else ""))
        print(f"  → {len(held)} exact matches: relations:/Related Papers candidates")
    else:
        print("  none held — use qmd query for Why Ingested wikilinks")
    print()

    if brief.get("CATEGORY_CANDIDATES"):
        print(f"CATEGORY_CANDIDATES  {brief['CATEGORY_CANDIDATES']}")
    for k in ("CLAIM", "CHALLENGES"):
        if brief.get(k):
            print(f"{k}  {brief[k]}")
    if brief.get("INDEX_LINE"):
        print(f"INDEX_LINE  {brief['INDEX_LINE']}")
    print()
    print(f"Next: python3 scripts/deepseek-split.py <dump.md> --category <folder>")


# ---------------------------------------------------------------- writing


def write_files(info: dict, brief: dict, category: str, args) -> int:
    cat_dir = os.path.join(WIKI_DIR, category)
    if not os.path.isdir(cat_dir) and not args.new_category:
        print(f"ERROR: wiki/{category}/ does not exist. Check wiki/_meta/categories.md, "
              f"or pass --new-category to create it.", file=sys.stderr)
        return 1

    stem = info["stem"]
    src_path, src_body = info["src"]
    _, wik_body = info["wiki"]

    src_out = os.path.join(SOURCES_DIR, f"{stem}.md")
    wik_out = os.path.join(cat_dir, f"{stem}.md")
    src_body = src_body.replace(PLACEHOLDER, category)
    wik_body = wik_body.replace(PLACEHOLDER, category)

    for out in (src_out, wik_out):
        if os.path.exists(out) and not args.force:
            print(f"ERROR: {os.path.relpath(out, REPO)} already exists (use --force to overwrite)",
                  file=sys.stderr)
            return 1

    if args.dry_run:
        print(f"[dry-run] would write {os.path.relpath(src_out, REPO)} ({len(src_body)} chars)")
        print(f"[dry-run] would write {os.path.relpath(wik_out, REPO)} ({len(wik_body)} chars)")
    else:
        os.makedirs(cat_dir, exist_ok=True)
        with open(src_out, "w", encoding="utf-8") as fh:
            fh.write(src_body)
        with open(wik_out, "w", encoding="utf-8") as fh:
            fh.write(wik_body)
        print(f"wrote {os.path.relpath(src_out, REPO)}")
        print(f"wrote {os.path.relpath(wik_out, REPO)}")

    if args.pdf:
        dest = os.path.join(PAPERS_DIR, f"{stem}.pdf")
        if not os.path.isfile(args.pdf):
            print(f"ERROR: --pdf not found: {args.pdf}", file=sys.stderr)
            return 1
        if args.dry_run:
            print(f"[dry-run] would copy PDF → papers/{stem}.pdf")
        else:
            os.makedirs(PAPERS_DIR, exist_ok=True)
            shutil.copy2(args.pdf, dest)
            print(f"copied PDF → papers/{stem}.pdf")
    else:
        print(f"NOTE: no --pdf given — papers/{stem}.pdf must exist or orphan-check.py fails")

    print()
    index_line = brief.get("INDEX_LINE", "")
    if index_line:
        print("index.md line (insert under the category heading):")
        print("  " + index_line.replace(PLACEHOLDER, category))
    print()
    print("Claude still owes this page:")
    print(f"  1. sources/{stem}.md  → ## Why Ingested (qmd query for a [[wikilink]])")
    print(f"  2. wiki/{category}/{stem}.md → ## Related Papers + relations: (after tags:)")
    print("  3. supersession check against CLAIM/CHALLENGES")
    print("  4. index.md → lint.py → orphan-check.py → per-file commit → qmd update && qmd embed")
    return 0


# ---------------------------------------------------------------- main


def main() -> int:
    ap = argparse.ArgumentParser(description="Split a DeepSeek v2 ingest dump into wiki pages.")
    ap.add_argument("dump", help="DeepSeek output .md file")
    ap.add_argument("--category", help="wiki category folder (e.g. implants/mbl) — enables write mode")
    ap.add_argument("--pdf", help="original PDF to copy into papers/{stem}.pdf")
    ap.add_argument("--dry-run", action="store_true", help="write mode without touching disk")
    ap.add_argument("--force", action="store_true", help="overwrite existing pages")
    ap.add_argument("--new-category", action="store_true", help="allow creating a new wiki/ folder")
    args = ap.parse_args()

    try:
        with open(args.dump, encoding="utf-8") as fh:
            raw = fh.read()
    except OSError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    files, brief_text = split_blocks(strip_outer_fence(raw))
    if not files:
        print("ERROR: no '===FILE: ...===' blocks found — is this a v1 dump "
              "(---METADATA--- style)? Those are assembled by Claude, not this script.",
              file=sys.stderr)
        return 2

    brief, refs = parse_brief(brief_text)
    errors, info = validate(files, brief)
    if errors:
        print(f"VALIDATION FAILED ({len(errors)}):", file=sys.stderr)
        for e in errors:
            print(f"  ✗ {e}", file=sys.stderr)
        return 1

    if not args.category:
        report(info, brief, refs)
        return 0
    return write_files(info, brief, args.category.strip("/"), args)


if __name__ == "__main__":
    sys.exit(main())
