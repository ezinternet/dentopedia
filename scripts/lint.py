#!/usr/bin/env python3
"""
LLM Wiki — Frontmatter Lint

두 가지 범위를 돈다:

1. **빌드 안전성 (wiki/ 전체 — 예외 없음)** — frontmatter 키 중복 + YAML 파싱.
   Quartz 배포는 `cp -r wiki/.`로 `wiki/` **전부**를 content로 넣으므로,
   overviews·_meta·_lint 어디에 있든 YAML이 깨지면 빌드 전체가 죽는다.
2. **논문 필드 (SKIP_DIRS 제외)** — 필수 frontmatter 필드·근거등급·아티팩트 경로.
   overviews 등은 논문이 아니라 이 검사에서 면제된다.

이 분리가 필요한 이유 (2026-08-25 사고):
`wiki/overviews/patient-safety-culture-dentistry-overview.md`에 `date:`가 두 번
들어가 GitHub Pages 배포가 하루 넘게 실패했다. 키 중복 검사는 그때도 이미 있었지만
**overviews가 SKIP_DIRS에 있어 아예 스캔되지 않았다.** 검사가 있어도 안 도는 곳에
있으면 없는 것과 같다 — 로컬 감사 21개 전부 초록불인 채 공개 배포만 조용히 깨졌다.

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
SKIP_DIRS = {"_lint", "_meta", "overviews", "evidence-appraisal"}
SKIP_FILES = {"index.md", "category-map.md"}  # Quartz homepage / nav-map, not paper pages

REQUIRED_FIELDS = [
    "title",
    "authors",
    "year",
    "doi",
    "source",
    "category",
]
# 근거등급 필드: evidence_level(2026-07-15 rename) 또는 legacy confidence — 둘 중 하나 필수.
# 둘 다 있으면 evidence_level 우선. 기존 페이지의 confidence:는 grandfather (INGEST.md 참조).
EVIDENCE_LEVEL_KEYS = ("evidence_level", "confidence")
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


def duplicate_top_level_keys(fm_text: str) -> list[str]:
    """Return top-level frontmatter keys that appear more than once.

    PyYAML's safe_load silently keeps the LAST value on a duplicate key, so it
    does NOT flag this — but Quartz's js-yaml parser fails the entire build on it
    ("duplicated mapping key" → exit 1 → GitHub Pages deploy blocked). We detect
    it with plain string parsing so the check works even without PyYAML.
    """
    counts: dict[str, int] = {}
    for line in fm_text.splitlines():
        # top-level key = column-0 (no leading whitespace), not a comment,
        # not a list item ("- ..."), of the form "key:".
        if not line or line[0].isspace():
            continue
        if line.lstrip().startswith("#"):
            continue
        m = re.match(r"^([A-Za-z0-9_-]+)\s*:", line)
        if not m:
            continue
        k = m.group(1)
        counts[k] = counts.get(k, 0) + 1
    return sorted(k for k, c in counts.items() if c > 1)


def lint_build_safety(path: str) -> list[str]:
    """Quartz 빌드를 죽이는 frontmatter 결함만 검사 — wiki/ 전 파일 대상.

    두 가지를 본다:
      · 최상위 키 중복 — Quartz의 js-yaml은 "duplicated mapping key"에서 빌드
        전체를 exit 1로 죽이는데, PyYAML의 safe_load는 마지막 값만 조용히 채택해
        아래 파싱 검사로는 절대 안 잡힌다. 그래서 문자열 파싱으로 따로 본다.
      · YAML 파싱 실패 — 따옴표 없는 값의 ":" 등.

    논문 필드 검사와 달리 **예외 디렉터리가 없다**. 배포가 wiki/ 전체를 빌드하므로
    검사 범위도 같아야 한다.
    """
    errors = []
    try:
        with open(path, encoding="utf-8") as f:
            content = f.read()
    except OSError as e:
        return [f"UNREADABLE: {path}: {e}"]

    m = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not m:
        return []  # frontmatter 부재는 논문 필드 검사의 소관
    fm_text = m.group(1)

    dup_keys = duplicate_top_level_keys(fm_text)
    if dup_keys:
        errors.append(f"DUPLICATE frontmatter key {dup_keys}: {path}")

    if yaml is not None and fm_text:
        try:
            yaml.safe_load(fm_text)
        except yaml.YAMLError as e:
            errors.append(f"YAML PARSE FAIL: {path}: {str(e).splitlines()[0]}")

    return errors


def lint_file(path: str) -> list[str]:
    errors = []
    with open(path, encoding="utf-8") as f:
        content = f.read()

    fields = parse_frontmatter(content)
    if fields is None:
        return [f"NO FRONTMATTER: {path}"]

    # 빌드 안전성(키 중복·YAML 파싱)은 여기서 하지 않는다 — lint_build_safety()가
    # wiki/ 전체를 따로 돈다. 여기서 중복 실행하면 같은 오류가 두 번 보고된다.

    # 논문 유형 판정 (evidence_level 우선, legacy confidence fallback)
    conf = (fields.get("evidence_level") or fields.get("confidence", "")).strip('"').strip("'")
    is_synthesis = conf == "synthesis"
    src_coll = fields.get("source_collection", "").strip('"').strip("'")
    is_pubmed_text = src_coll == "pubmed-text"
    # pubmed-abstract = 초록만 있는 논문, 로컬 아티팩트(PDF/txt) 없음 → 아티팩트 필드 면제
    is_abstract_only = src_coll == "pubmed-abstract"
    # navigation = 카테고리 인덱스·허브 페이지, 논문 아님 → 아티팩트 필드 면제
    is_navigation = fields.get("source", "").strip('"').strip("'") == "navigation"

    # 필수 아티팩트 필드는 유형별로 다름:
    #   synthesis        → 없음 (내부 합성 페이지)
    #   pubmed-abstract  → 없음 (초록 전용, 로컬 파일 없음)
    #   navigation       → 없음 (카테고리 허브, 논문 아님)
    #   pubmed-text      → text_path / text_filename
    #   external         → pdf_path / pdf_filename
    required = list(REQUIRED_FIELDS)
    if not is_synthesis and not is_abstract_only and not is_navigation:
        required += TEXT_FIELDS if is_pubmed_text else PDF_FIELDS

    # Check required fields exist
    missing = [f for f in required if f not in fields]
    if not any(k in fields for k in EVIDENCE_LEVEL_KEYS):
        missing.append("evidence_level")
    if missing:
        errors.append(f"MISSING {missing}: {path}")

    # Check evidence_level/confidence value is valid
    if conf and conf not in VALID_CONFIDENCE:
        errors.append(f"INVALID evidence_level '{conf}': {path}")

    # 아티팩트 path/filename 쌍 검증 (synthesis·pubmed-abstract·navigation 면제)
    if not is_synthesis and not is_abstract_only and not is_navigation:
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

    # ── 패스 1: 빌드 안전성 — wiki/ 전체, 예외 없음 ──
    build_errors = []
    build_checked = 0
    for root, _dirs, files in os.walk(WIKI_DIR):
        for fn in sorted(files):
            if not fn.endswith(".md"):
                continue
            build_checked += 1
            build_errors.extend(lint_build_safety(os.path.join(root, fn)))

    # ── 패스 2: 논문 필드 — SKIP_DIRS/SKIP_FILES 적용 ──
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
    bstatus = "✅" if not build_errors else "❌"
    print(f"{bstatus}  build-safety (키 중복·YAML): {build_checked} files   ERRORS: {len(build_errors)}")

    if build_errors:
        print()
        print("  ⚠ 아래는 Quartz 빌드를 죽여 GitHub Pages 배포를 막는다:")
        for e in build_errors:
            print(f"  {e}")
    if all_errors:
        print()
        for e in all_errors:
            print(f"  {e}")
    if all_errors or build_errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
