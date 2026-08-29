#!/usr/bin/env python3
from __future__ import annotations  # PEP 604 unions must run on Python 3.9
"""Generate category landing pages for all MISS wiki category folders.

Creates wiki/{category}/{basename}.md for every folder that doesn't already
have one, using descriptions from wiki/_meta/categories.md.

Usage:
    python3 scripts/gen-category-landing.py                     # create missing only
    python3 scripts/gen-category-landing.py --dry-run           # preview, write nothing
    python3 scripts/gen-category-landing.py --force             # rewrite ALL 121 landings
    python3 scripts/gen-category-landing.py --only overviews    # rewrite ONE landing

A landing page's paper table goes stale as papers land in its folder — nothing
regenerates it per-ingest, so drift accumulates silently (measured 2026-08-29:
35 of 121 landing pages drifted, worst `overviews` at 267 rows vs 280 papers).
`--only <rel-path>` exists so a single stale landing can be refreshed without
`--force` rewriting the other 120 — a rewrite resets `date:` and discards any
hand-edits, so blast radius should match intent.
"""

import os
import re
import sys
from pathlib import Path
from datetime import date

WIKI_ROOT = Path(__file__).parent.parent / "wiki"
CATEGORIES_FILE = WIKI_ROOT / "_meta" / "categories.md"
TODAY = date.today().isoformat()

# ── Parse categories.md ────────────────────────────────────────────────────

def parse_categories(filepath: Path) -> dict[str, dict]:
    """Return {folder_path: {korean, description}} from the table rows."""
    categories = {}
    in_table = False
    for line in filepath.read_text(encoding="utf-8").splitlines():
        # Table row: | `folder` | Korean | Description |
        m = re.match(r'^\|\s*`([^`]+)`\s*\|\s*([^|]+)\s*\|\s*(.+?)\s*\|?\s*$', line)
        if m:
            folder = m.group(1).strip()
            korean = m.group(2).strip()
            desc   = m.group(3).strip()
            # Skip header rows
            if folder in ("Category folder", "---"):
                continue
            categories[folder] = {"korean": korean, "description": desc}
    return categories


# ── Helpers ────────────────────────────────────────────────────────────────

def get_frontmatter_title(md_file: Path) -> str | None:
    """Extract `title:` from YAML frontmatter."""
    try:
        text = md_file.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return None
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    fm = text[3:end]
    m = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', fm, re.MULTILINE)
    if m:
        return m.group(1).strip().strip('"\'')
    return None


def get_papers(folder: Path) -> list[tuple[str, str]]:
    """Return [(filename_stem, title_or_stem)] sorted by stem.

    The folder's own landing page (`{folder.name}.md`) is excluded — a landing
    page listing itself as one of its papers is a self-reference, and all 121
    existing landing pages follow that convention. Without this the `--force`
    / `--only` refresh path would inject a self-row into every page it rewrote.
    """
    landing_name = f"{folder.name}.md"
    papers = []
    for f in sorted(folder.glob("*.md")):
        if f.name == landing_name:
            continue
        stem = f.stem
        title = get_frontmatter_title(f) or stem
        papers.append((stem, title))
    return papers


def get_subcategories(folder: Path) -> list[str]:
    """Return immediate child directory names."""
    return sorted(d.name for d in folder.iterdir() if d.is_dir() and not d.name.startswith("_"))


def strip_routing_hints(desc: str) -> str:
    """Remove parenthetical routing hints like (foo → `bar/baz`) for display."""
    # Remove (... → `...`) patterns
    return re.sub(r'\s*\([^)]*→[^)]*\)', '', desc).strip()


# ── Landing page template ──────────────────────────────────────────────────

def make_landing_page(
    folder_path: str,        # relative to wiki/, e.g. "implants/surface"
    korean: str,
    description: str,
    papers: list[tuple[str, str]],
    subcats: list[str],
) -> str:
    basename = folder_path.split("/")[-1]
    short_desc = strip_routing_hints(description)
    # Truncate very long descriptions for the title line
    title_suffix = f"{korean} — {basename}"

    # Build subcategory display lines
    subcat_ko_lines = ""
    if subcats:
        subcat_ko_lines = "\n> - **하위 카테고리**: " + " · ".join(f"[[{s}]]" for s in subcats)

    subcat_en_lines = ""
    if subcats:
        subcat_en_lines = f"\n**Sub-categories**: {', '.join('[[' + s + ']]' for s in subcats)}"

    subcat_section = ""
    if subcats:
        subcat_section = "\n## Sub-categories\n\n" + "\n".join(
            f"- [[{s}|{s}]]" for s in subcats
        ) + "\n"

    # Build paper table
    papers_section = ""
    if papers:
        rows = "\n".join(f"| [[{stem}|{title}]] |" for stem, title in papers)
        papers_section = f"\n## Papers in this Category ({len(papers)})\n\n| Paper |\n|---|\n{rows}\n"

    # Short 1-sentence English summary (first sentence of desc)
    first_sentence = re.split(r'(?<=[.!?])\s', short_desc)[0]

    page = f"""---
title: "{title_suffix}"
authors: navigation
year: 2026
date: {TODAY}
doi: N/A
source: navigation
category: {folder_path}
evidence_level: narrative-review
tags: [navigation, category-index, {basename}]
---

## 한국어 핵심요약

> [!summary] 한국어 핵심요약
> - **분야**: {korean}
> - **범위**: {short_desc[:300]}{'…' if len(short_desc) > 300 else ''}{subcat_ko_lines}
> - **수록 논문**: {len(papers)}편

## Three-line Summary

**Scope**: {first_sentence}
**Indexed papers**: {len(papers)} papers in `wiki/{folder_path}/`.{subcat_en_lines}

## 세줄요약

**분야**: {korean}
**수록 논문**: {len(papers)}편
**하위 카테고리**: {', '.join(subcats) if subcats else '없음'}
{papers_section}{subcat_section}"""
    return page.strip() + "\n"


# ── Main ───────────────────────────────────────────────────────────────────

def main():
    dry_run = "--dry-run" in sys.argv
    force   = "--force"   in sys.argv

    # --only <rel-path> / --only=<rel-path>: refresh exactly one landing page.
    only = None
    for i, arg in enumerate(sys.argv):
        if arg == "--only" and i + 1 < len(sys.argv):
            only = sys.argv[i + 1].strip("/")
        elif arg.startswith("--only="):
            only = arg.split("=", 1)[1].strip("/")

    cat_map = parse_categories(CATEGORIES_FILE)
    # Parent folders that exist on disk but have no direct entry in categories.md
    # (they exist only as containers for subcategories)
    PARENT_FALLBACKS = {
        "behavioral-dentistry": {
            "korean": "행동치의학",
            "description": "Behavioral aspects of dentistry — dental anxiety, communication, patient-reported outcomes, motivational interviewing, body dysmorphic disorder screening. See subcategories for details.",
        },
        "drug": {
            "korean": "약물·전신질환",
            "description": "Drug use and systemic disease management in dentistry — antibiotics, analgesics/NSAIDs, anticoagulants, MRONJ, and medically compromised patients. See subcategories for details.",
        },
        "sinus-lift": {
            "korean": "상악동거상술",
            "description": "Maxillary sinus augmentation — lateral window and transcrestal approaches, pseudocyst management. See subcategories for details.",
        },
    }
    for folder, info in PARENT_FALLBACKS.items():
        if folder not in cat_map:
            cat_map[folder] = info

    print(f"Parsed {len(cat_map)} category definitions from categories.md")

    # Collect all MISS folders
    miss = []
    for dirpath in sorted(WIKI_ROOT.rglob("*")):
        if not dirpath.is_dir():
            continue
        if any(part.startswith("_") for part in dirpath.parts):
            continue
        rel = dirpath.relative_to(WIKI_ROOT)
        rel_str = str(rel)
        landing = dirpath / f"{dirpath.name}.md"
        if only is not None:
            if rel_str == only:
                miss.append((rel_str, dirpath, landing))
            continue
        if not landing.exists() or force:
            miss.append((rel_str, dirpath, landing))

    if only is not None and not miss:
        print(f"[ERROR] --only {only!r} matched no folder under wiki/")
        sys.exit(1)

    scope = f"--only {only}" if only else ("--force (all)" if force else "missing only")
    print(f"Found {len(miss)} folders needing landing pages [{scope}]")
    created = 0
    skipped = 0

    for rel_str, dirpath, landing in miss:
        basename = dirpath.name

        # Look up category definition
        if rel_str in cat_map:
            korean = cat_map[rel_str]["korean"]
            description = cat_map[rel_str]["description"]
        else:
            # Fallback: use basename as Korean (will be imprecise but functional)
            korean = basename.replace("-", " ").title()
            description = f"Papers in the `{rel_str}` category."
            print(f"  [WARN] No category definition for: {rel_str}")

        papers = get_papers(dirpath)
        subcats = get_subcategories(dirpath)

        content = make_landing_page(rel_str, korean, description, papers, subcats)

        if dry_run:
            print(f"  [DRY] would write {landing.relative_to(WIKI_ROOT)}"
                  f" ({len(papers)} papers, {len(subcats)} subcats)")
            skipped += 1
        else:
            landing.write_text(content, encoding="utf-8")
            print(f"  [OK]  {landing.relative_to(WIKI_ROOT)}"
                  f" ({len(papers)} papers, {len(subcats)} subcats)")
            created += 1

    print(f"\nDone. Created={created}, Dry-skipped={skipped}")


if __name__ == "__main__":
    main()
