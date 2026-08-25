#!/usr/bin/env python3
"""
dedup-check.py — Step 0 중복 게이트 (DOI + 제목 정규화 fallback)

INGEST.md Step 0의 `grep -rl "10.xxxx/doi" sources/`를 대체한다.

왜 필요한가 (2026-08-25)
------------------------
Step 0의 dedup은 DOI grep이 전부였고, no-DOI fallback은 "title + first-author
grep"이라는 **문장으로만** 적혀 있었다. 실제 grep은 제목 표기 차이(대소문자·
문장부호·괄호 병기·하이픈)에 그대로 깨져서, `ingest-deviations`에 duplicate-skip
22건 + duplicate-distinct 3건이 쌓였다. 로그의 근본원인 문구가 그대로다:

    "DOI conflict/cross-stem duplicate: ... (doi was null, missed by Step0 grep)"

`doi-duplicate-check.py`(일간 감사)에는 이미 제목 정규화 fallback이 있는데
**사후 감사에만 있고 인제스트 시점에는 없었다.** 같은 로직을 앞단으로 당긴다.
정규화 함수는 복제하지 않고 그 파일에서 그대로 import한다 (단일 출처).

exit code: 0 = 중복 없음(진행 가능), 1 = 중복 의심(STOP), 2 = 사용법 오류

Usage:
    python3 scripts/dedup-check.py --doi 10.1016/j.adaj.2023.10.009
    python3 scripts/dedup-check.py --title "Pharmacologic management of acute dental pain"
    python3 scripts/dedup-check.py --pdf /path/to/paper.pdf        # DOI·제목 자동 추출
    python3 scripts/dedup-check.py --doi null --title "..."        # no-DOI 논문
"""

import argparse
import importlib.util
import os
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SOURCES = REPO / "sources"

# 정규화 로직은 doi-duplicate-check.py가 단일 출처 — 복제하지 않고 import.
# 파일명에 하이픈이 있어 일반 import가 안 되므로 importlib을 쓴다.
_spec = importlib.util.spec_from_file_location(
    "_doi_dup", Path(__file__).resolve().parent / "doi-duplicate-check.py"
)
_ddc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_ddc)

_normalize_doi = _ddc._normalize_doi
_normalize_title = _ddc._normalize_title
_read_frontmatter = _ddc._read_frontmatter
_stem_nfc = _ddc._stem_nfc

DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Za-z0-9]+")
# 근사 매칭 임계값. 0.75면 부제 유무·전치사 차이는 잡고 다른 논문은 거른다.
FUZZY_THRESHOLD = 0.75
STOPWORDS = {"a", "an", "the", "of", "in", "on", "for", "and", "or", "to", "with", "vs", "versus"}


def _tokens(norm_title: str) -> set[str]:
    return {t for t in norm_title.split() if t not in STOPWORDS and len(t) > 2}


def _jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def from_pdf(path: str) -> tuple[str, str]:
    """PDF 앞 2면 + 메타데이터에서 DOI·제목 추출. 실패해도 빈 문자열로 진행."""
    try:
        from pypdf import PdfReader
    except ImportError:
        print("⚠ pypdf 없음 — --doi/--title을 직접 넘겨라", file=sys.stderr)
        return "", ""
    try:
        r = PdfReader(path)
    except Exception as e:
        print(f"⚠ PDF 읽기 실패: {e}", file=sys.stderr)
        return "", ""
    text = " ".join((r.pages[i].extract_text() or "") for i in range(min(2, len(r.pages))))
    meta = r.metadata or {}
    blob = text + " " + " ".join(str(v) for v in meta.values())
    m = DOI_RE.search(blob)
    doi = m.group(0).rstrip(".,);") if m else ""
    title = (meta.get("/Title") or "") if meta else ""
    if not title or title.lower().endswith((".indd", ".pdf", ".doc")):
        # 메타 제목이 조판 파일명이면 본문 첫 유의미 줄을 쓴다
        for line in (l.strip() for l in text.splitlines()):
            if len(line) > 25 and not line.lower().startswith(("http", "doi", "downloaded")):
                title = line
                break
    return doi, title


def load_sources() -> list[tuple[str, str, str]]:
    """[(stem, normalized_doi, normalized_title)]"""
    out = []
    for f in os.listdir(SOURCES):
        if not f.endswith(".md"):
            continue
        raw_doi, raw_title = _read_frontmatter(str(SOURCES / f))
        out.append((_stem_nfc(f), _normalize_doi(raw_doi), _normalize_title(raw_title)))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--doi", default="")
    ap.add_argument("--title", default="")
    ap.add_argument("--pdf", default="")
    args = ap.parse_args()

    doi, title = args.doi, args.title
    if args.pdf:
        pdoi, ptitle = from_pdf(args.pdf)
        doi = doi or pdoi
        title = title or ptitle

    if not doi and not title:
        print("사용법: --doi / --title / --pdf 중 최소 하나", file=sys.stderr)
        return 2

    ndoi = _normalize_doi(doi)
    ntitle = _normalize_title(title)
    print(f"입력 DOI  : {doi or '(없음)'}  → 정규화 {ndoi or '(무효/없음)'}")
    print(f"입력 제목 : {(title or '(없음)')[:70]}")
    print(f"          → 정규화 {ntitle or '(너무 짧음 — 제목 매칭 생략)'}")
    print()

    rows = load_sources()
    print(f"sources/ {len(rows)}편 대조")

    hits: list[tuple[str, str]] = []

    if ndoi:
        for stem, sdoi, _ in rows:
            if sdoi and sdoi == ndoi:
                hits.append((stem, "DOI 일치"))

    if ntitle:
        qt = _tokens(ntitle)
        for stem, _, stitle in rows:
            if not stitle:
                continue
            if stitle == ntitle:
                hits.append((stem, "제목 정규화 완전일치"))
                continue
            j = _jaccard(qt, _tokens(stitle))
            if j >= FUZZY_THRESHOLD:
                hits.append((stem, f"제목 근사일치 {j:.0%}"))

    # stem 중복 제거 (DOI·제목 양쪽에 걸린 경우 사유를 합친다)
    merged: dict[str, list[str]] = {}
    for stem, why in hits:
        merged.setdefault(stem, []).append(why)

    if not merged:
        print("\n✅ 중복 없음 — 신규 인제스트 진행 가능")
        if not ndoi:
            print("   (DOI가 없으므로 제목 근사매칭만 수행됨. "
                  "frontmatter doi: null 로 두고 log-deviation.py <stem> no-doi 기록할 것)")
        return 0

    print("\n🛑 중복 의심 — 신규 페이지 생성 금지, 기존 페이지를 갱신하라")
    for stem, whys in sorted(merged.items()):
        print(f"   • {stem}")
        print(f"     사유: {', '.join(sorted(set(whys)))}")
        w = REPO / "sources" / f"{stem}.md"
        print(f"     {w.relative_to(REPO)}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
