#!/usr/bin/env python3
"""
LLM Wiki — DOI Duplicate Check (signal)

orphan-check.py는 stem 기준 papers↔sources 1:1만 본다. 같은 논문이
서로 다른 stem으로 두 번 ingest되면(예: gaspar 2022/2025, inchingolo
materials/sr-ma) orphan-check를 통과해버린다. 이 사각지대를 메우기 위해
sources/ frontmatter의 DOI를 스캔해 "동일 DOI·다른 stem"을 검출한다.

판정:
  - sources/*.md frontmatter의 doi: 값을 정규화(소문자·따옴표/공백/후행구두점 제거).
  - 정규화 DOI가 2개 이상 stem에 걸리면 중복 후보로 보고.
  - 제목 fallback: 정규화 제목(괄호/한글병기 제거, 영숫자만)이 2개 이상 stem에
    걸리는데 단일 DOI로 이미 안 잡힌 경우(한쪽 DOI 비었거나 DOI 불일치)를
    별도 섹션으로 보고. 한쪽 DOI가 비면 DOI-check가 못 잡는 사각을 메운다.
    (예: nassani-2025 한쪽 doi="", singh/unknown-2026 한쪽 doi="")

설계: signal(비차단). 차단 게이트는 정당한 erratum/version 공존 등에서
오탐으로 워크플로를 멈출 수 있어, 가시성으로 자가교정하는 원칙을 따른다.
중복 확인 시 사람이 병합·삭제 결정.

Usage:
    python3 scripts/doi-duplicate-check.py
"""

import os
import re
import sys
import unicodedata
from collections import defaultdict
from datetime import date

SOURCES_DIR = "sources"
LOGS_DIR = "logs"


def _stem_nfc(fname: str) -> str:
    return unicodedata.normalize("NFC", os.path.splitext(fname)[0])


def _read_frontmatter(path: str) -> tuple[str | None, str | None]:
    """첫 번째 --- ... --- 블록에서 (doi, title) 추출. 없으면 (None, None)."""
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except Exception:
        return None, None
    if not text.startswith("---"):
        return None, None
    end = text.find("\n---", 3)
    if end == -1:
        return None, None
    doi = title = None
    for line in text[3:end].splitlines():
        m = re.match(r"\s*doi\s*:\s*(.*)$", line, re.IGNORECASE)
        if m and doi is None:
            doi = m.group(1)
        m = re.match(r"\s*title\s*:\s*(.*)$", line, re.IGNORECASE)
        if m and title is None:
            title = m.group(1)
    return doi, title


def _normalize_doi(raw: str | None) -> str:
    """DOI 정규화: 따옴표/공백/후행 구두점 제거, 소문자화. 빈 값은 ''."""
    if raw is None:
        return ""
    v = raw.strip().strip('"').strip("'").strip()
    # 흔한 prefix 제거 (https://doi.org/, doi:)
    v = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:\s*)", "", v, flags=re.IGNORECASE)
    v = v.rstrip(" .,;").lower()
    # 진짜 DOI만 인정: 10.NNNN/suffix 형태가 아니면 빈 값 취급.
    # ('unknown', '(manufacturer document)', 'n/a' 등 placeholder 전부 제외)
    if not re.match(r"^10\.\d{4,9}/\S+$", v):
        return ""
    return v


def _normalize_title(raw: str | None) -> str:
    """제목 정규화: 따옴표·괄호(한글 병기 등) 제거, 영숫자만, 소문자.

    너무 짧으면('' 또는 <=10자) 빈 값 취급 — 일반어 false positive 방지.
    """
    if raw is None:
        return ""
    v = raw.strip().strip('"').strip("'")
    v = re.sub(r"\(.*?\)", " ", v)            # 괄호 안(한글 병기/부제) 제거
    v = re.sub(r"[^a-z0-9]+", " ", v.lower()).strip()
    return v if len(v) > 10 else ""


def main() -> int:
    by_doi: dict[str, list[str]] = defaultdict(list)
    by_title: dict[str, list[str]] = defaultdict(list)
    stem_doi: dict[str, str] = {}
    n_sources = 0
    for f in os.listdir(SOURCES_DIR):
        if not f.endswith(".md"):
            continue
        n_sources += 1
        stem = _stem_nfc(f)
        raw_doi, raw_title = _read_frontmatter(os.path.join(SOURCES_DIR, f))
        doi = _normalize_doi(raw_doi)
        title = _normalize_title(raw_title)
        stem_doi[stem] = doi
        if doi:
            by_doi[doi].append(stem)
        if title:
            by_title[title].append(stem)

    doi_dups = {d: sorted(set(s)) for d, s in by_doi.items() if len(set(s)) > 1}

    # 제목 fallback: 정규화 제목이 겹치는데, 그 그룹이 단일 DOI로 이미
    # 잡히지 않은 경우만 보고(빈 DOI·DOI 불일치 포함 — DOI-check 사각).
    title_dups: dict[str, list[str]] = {}
    for title, stems in by_title.items():
        uniq = sorted(set(stems))
        if len(uniq) < 2:
            continue
        dois = {stem_doi.get(s, "") for s in uniq}
        nonempty = {d for d in dois if d}
        # 모두 동일한 1개 DOI면 이미 doi_dups가 처리 → 제외
        if len(nonempty) == 1 and "" not in dois:
            continue
        title_dups[title] = uniq

    total_with_doi = sum(len(s) for s in by_doi.values())

    if not doi_dups and not title_dups:
        print(f"✅  No duplicate DOIs/titles — {n_sources} sources "
              f"({total_with_doi} with DOI, {len(by_doi)} unique)")
        return 0

    # signal: 보고만, 차단하지 않음
    lines: list[str] = []
    if doi_dups:
        lines.append(f"DOI Duplicate Check — {len(doi_dups)} duplicate DOI group(s)")
        for doi, stems in sorted(doi_dups.items()):
            lines.append(f"  DOI {doi}  ({len(stems)} stems):")
            for s in stems:
                lines.append(f"    - sources/{s}.md")
    if title_dups:
        lines.append(f"TITLE fallback — {len(title_dups)} same-title group(s) NOT covered by DOI "
                     f"(empty/mismatched DOI — DOI-check blind spot)")
        for title, stems in sorted(title_dups.items()):
            lines.append(f"  TITLE \"{title[:60]}...\"  ({len(stems)} stems):")
            for s in stems:
                lines.append(f"    - sources/{s}.md  (doi={stem_doi.get(s, '') or '∅'})")

    msg = []
    if doi_dups:
        msg.append(f"{len(doi_dups)} DOI group(s)")
    if title_dups:
        msg.append(f"{len(title_dups)} title-only group(s)")
    print(f"🔁  Duplicates: {', '.join(msg)} — review/merge")
    for line in lines:
        print(line)

    # 로그 기록
    try:
        os.makedirs(LOGS_DIR, exist_ok=True)
        log_path = os.path.join(LOGS_DIR, f"{date.today().isoformat()}_doi-duplicate-check.log")
        with open(log_path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")
        print(f"        log → {log_path}")
    except Exception as e:
        print(f"        (log write failed: {e})")

    return 0  # signal: 항상 0


if __name__ == "__main__":
    sys.exit(main())
