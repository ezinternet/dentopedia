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
from typing import Optional

try:
    import yaml
except ImportError:
    yaml = None  # YAML parse check skipped if PyYAML not installed

WIKI_DIR = "wiki"
SKIP_DIRS = {"_lint", "overviews", "evidence-appraisal"}
SKIP_FILES = {"index.md"}  # Quartz homepage, not a paper page

REQUIRED_FIELDS = [
    "title",
    "authors",
    "year",
    "doi",
    "source",
    "category",
    "confidence",
]
# 아티팩트 필드: PDF 논문 vs PubMed-text 논문(PMC 전문을 .txt로 저장)
PDF_FIELDS = ["pdf_path", "pdf_filename"]
TEXT_FIELDS = ["text_path", "text_filename"]

VALID_CONFIDENCE = {
    "sr+ma", "sr", "rct", "prospective", "retrospective",
    "cross-sectional", "case-report", "in-vivo", "animal",
    "in-vitro", "narrative-review", "consensus",
    "synthesis",  # internal multi-paper synthesis pages (no source PDF)
    # Korean health-insurance administrative documents (non-research):
    "regulation",  # MOHW notice / decree / amendment
    "official-qa", # official Q&A from MOHW / HIRA
    "manual",      # practical guidebook / 실무편람 / 청구길라잡이
    "patent",      # patent disclosure (공개/등록특허공보) — primary engineering document, non-research
}


def parse_frontmatter(content: str) -> Optional[dict]:
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

    # YAML parse check — catches issues that break Quartz build
    # (e.g., unquoted values with embedded ":" or other YAML specials)
    if yaml is not None:
        m = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
        if m:
            try:
                yaml.safe_load(m.group(1))
            except yaml.YAMLError as e:
                first_line = str(e).splitlines()[0]
                errors.append(f"YAML PARSE FAIL: {path}: {first_line}")

    # 논문 유형 판정
    conf = fields.get("confidence", "").strip('"').strip("'")
    is_synthesis = conf == "synthesis"
    src_coll = fields.get("source_collection", "").strip('"').strip("'")
    is_pubmed_text = src_coll == "pubmed-text"

    # 필수 아티팩트 필드는 유형별로 다름:
    #   synthesis   → 없음 (내부 합성 페이지, source 아티팩트 없음)
    #   pubmed-text → text_path / text_filename (PMC 전문을 .txt로 보관)
    #   external    → pdf_path / pdf_filename
    required = list(REQUIRED_FIELDS)
    if not is_synthesis:
        required += TEXT_FIELDS if is_pubmed_text else PDF_FIELDS

    # Check required fields exist
    missing = [f for f in required if f not in fields]
    if missing:
        errors.append(f"MISSING {missing}: {path}")

    # Check confidence value is valid
    if conf and conf not in VALID_CONFIDENCE:
        errors.append(f"INVALID confidence '{conf}': {path}")

    # 아티팩트 path/filename 쌍 검증 (synthesis 면제)
    if not is_synthesis:
        path_field, name_field = (
            ("text_path", "text_filename") if is_pubmed_text else ("pdf_path", "pdf_filename")
        )
        if path_field in fields:
            pv = fields[path_field]
            if pv in ("null", "None", ""):
                errors.append(f"EMPTY {path_field}: {path}")
            elif not pv.startswith("/Users/oracleneo/llm-wiki/papers/"):
                errors.append(f"BAD {path_field} (must be inside /papers/): {path}")
            elif name_field in fields and fields[name_field] != os.path.basename(pv):
                errors.append(
                    f"{name_field} mismatch (path={os.path.basename(pv)}, filename={fields[name_field]}): {path}"
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
            if fn in SKIP_FILES:
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
