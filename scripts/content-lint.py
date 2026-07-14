#!/usr/bin/env python3
"""
LLM Wiki — Content Lint (SIGNAL, non-blocking)

frontmatter lint(lint.py)이 못 보는 **본문 내용 규칙**을 결정론으로 검사한다.
LLM subagent 없이 스크립트만으로 돌아가는 저비용 signal — daily-audit에 물려
가시화만 하고 절대 block하지 않는다(저장소의 signal-not-gate 철학 준수).

세 검사:
  A. 필수 섹션      — 이중언어 세줄요약 쌍은 모든 페이지 필수. 유형별 앵커 추가.
  B. 태그 정합성    — heading 끝 대괄호 태그는 '확인' 또는 '미검증' 토큰을 포함해야 함.
                      (복합 변형 '[확인, 다만 수치는 미검증]' 등은 정상 통과)
  C. 계층 정합성    — wiki `source:` → sources/ 파일 실재 + wiki↔source pmid 일치.

의미 판단(요약↔Results 일치, confidence 정당성 등)은 여기서 하지 않는다 —
그건 결정론으로 못 잡으므로, 이 검사들이 남긴 잔여 드리프트가 유의미할 때만
별도 LLM 검증자로 올린다.

Usage:
    python3 scripts/content-lint.py           # full run (signal, exit 0)
    python3 scripts/content-lint.py --quiet    # findings only, no OK lines
    python3 scripts/content-lint.py --check A  # run only check A|B|C
"""

import os
import re
import sys
import argparse
from typing import Optional

WIKI_DIR = "wiki"
SOURCES_DIR = "sources"
SKIP_DIRS = {"_lint"}
SKIP_FILES = {"index.md", "category-map.md"}

# heading에 태그로 쓰일 때 '검증 상태'를 표시하는 토큰. 이 중 하나를 포함하면 정상.
VALID_TAG_TOKENS = ("확인", "미검증")


def parse_frontmatter(content: str) -> Optional[dict]:
    m = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not m:
        return None
    fields = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"^(\w+)\s*:\s*(.*)$", line)
        if kv:
            fields[kv.group(1)] = kv.group(2).strip().strip('"').strip("'")
    return fields


def body_after_frontmatter(content: str) -> str:
    m = re.match(r"^---\n.*?\n---\n?(.*)$", content, re.DOTALL)
    return m.group(1) if m else content


def has_heading(body: str, pattern: str) -> bool:
    """본문에 `^#{2,} ...` heading 중 pattern(정규식, 대소문자 무시)에 맞는 게 있나."""
    rx = re.compile(pattern, re.IGNORECASE)
    for line in body.splitlines():
        if re.match(r"^#{2,}\s+", line) and rx.search(line):
            return True
    return False


# ── Check A: 필수 섹션 ────────────────────────────────────────────────
# 이중언어 세줄요약 쌍은 CLAUDE.md 언어정책상 모든 신규 페이지 필수.
REQ_THREELINE_EN = r"three[\s\-]?line summary"
REQ_THREELINE_KO = r"세\s?줄\s?요약"
REQ_KO_DIGEST = "한국어 핵심요약"            # overview 상단 콜아웃(`> [!summary] 한국어 핵심요약`)

# source: 필드가 실제 파일이 아니라 합성/플레이스홀더를 뜻하는 값들 — Check C 면제.
SOURCE_PLACEHOLDERS = {"n/a", "na", "none", "-", "overview", "synthesis", "multiple", "various"}


def check_a(path: str, body: str, ptype: str) -> list[str]:
    out = []
    if not has_heading(body, REQ_THREELINE_EN):
        out.append(f"A/MISSING-SECTION '## Three-line Summary': {path}")
    if not has_heading(body, REQ_THREELINE_KO):
        out.append(f"A/MISSING-SECTION '## 세줄요약': {path}")

    # overview: '한국어 핵심요약' 콜아웃은 CLAUDE.md상 무조건 필수(현재 100% 준수 → 회귀 가드).
    #           heading이 아니라 `> [!summary] 한국어 핵심요약` 콜아웃이므로 본문 substring으로 검사.
    if ptype == "overview" and REQ_KO_DIGEST not in body:
        out.append(f"A/MISSING-SECTION '한국어 핵심요약' 콜아웃 (overview 필수): {path}")
    # NOTE: '## Summary'/7섹션 템플릿은 강제하지 않는다 — 오버뷰는 주제별 구조(Scope/Cluster/…),
    #       source는 압축형 섹션을 정당하게 쓰므로 강제 시 오탐만 늘고 signal 신뢰도가 깨진다.
    #       무조건 필수인 이중언어 세줄요약 쌍만 전 페이지 공통으로 검사한다.
    return out


# ── Check B: heading 끝 태그 정합성 ───────────────────────────────────
# 정책: heading 끝 대괄호 [ ... ] 는 "그 섹션 주장의 출처검증 상태" 전용 슬롯이고
#       어휘는 확인/미검증 이진(토큰 뒤 한정어 허용: '[확인 (수치), 적용은 미검증]').
#       순수 서술적 설명은 대괄호가 아니라 소괄호 ( ... ) 를 쓴다(검증선언과 구분) —
#       그래야 이 검사가 서술 주석을 오탐하지 않는다. Claude 종합·해석은 미검증 계열.
# heading 라인 끝의 [ ... ] 태그가 '확인'/'미검증' 토큰을 하나도 포함하지 않으면 드리프트.
# wikilink([[...]])·마크다운링크([..](..))는 배제.
TRAILING_TAG = re.compile(r"\[([^\[\]]+)\]\s*$")


def check_b(path: str, body: str) -> list[str]:
    out = []
    for i, line in enumerate(body.splitlines(), 1):
        if not re.match(r"^#{1,6}\s+", line):
            continue
        stripped = line.rstrip()
        # 마크다운 링크로 끝나면(`](url)`) 태그 아님
        if re.search(r"\]\([^)]*\)\s*$", stripped):
            continue
        m = TRAILING_TAG.search(stripped)
        if not m:
            continue
        inner = m.group(1)
        if not any(tok in inner for tok in VALID_TAG_TOKENS):
            out.append(f"B/BAD-TAG heading tag '[{inner}]' has no 확인/미검증 token: {path}")
    return out


# ── Check C: wiki↔source 계층 정합성 ─────────────────────────────────
def check_c(path: str, fields: dict, source_pmids: dict) -> list[str]:
    out = []
    src = fields.get("source", "").strip()
    if not src or src.lower() in {"null"} | SOURCE_PLACEHOLDERS:
        return out  # synthesis/overview 등 source 없는 페이지는 면제
    if fields.get("confidence", "").strip() == "synthesis":
        return out  # 합성 페이지는 단일 source 없음
    src_path = os.path.join(SOURCES_DIR, src)
    if not os.path.isfile(src_path):
        out.append(f"C/DANGLING-SOURCE source: '{src}' → sources/{src} 없음: {path}")
        return out
    # pmid 교차검증: 양쪽 다 있을 때만
    wiki_pmid = fields.get("pmid", "").strip()
    src_pmid = source_pmids.get(src, "").strip()
    if wiki_pmid and src_pmid and wiki_pmid != src_pmid:
        out.append(
            f"C/PMID-MISMATCH wiki pmid={wiki_pmid} vs source pmid={src_pmid} ({src}): {path}"
        )
    return out


def page_type(path: str) -> str:
    if path.startswith(SOURCES_DIR + os.sep):
        return "source"
    if os.sep + "overviews" + os.sep in path:
        return "overview"
    return "wiki"


def index_source_pmids() -> dict:
    """sources/{stem}.md → pmid 매핑 (Check C용)."""
    m = {}
    for fn in os.listdir(SOURCES_DIR):
        if not fn.endswith(".md"):
            continue
        try:
            with open(os.path.join(SOURCES_DIR, fn), encoding="utf-8") as f:
                fields = parse_frontmatter(f.read()) or {}
            m[fn] = fields.get("pmid", "")
        except OSError:
            pass
    return m


def iter_pages():
    for base in (WIKI_DIR, SOURCES_DIR):
        for root, dirs, files in os.walk(base):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for fn in sorted(files):
                if not fn.endswith(".md") or fn in SKIP_FILES:
                    continue
                yield os.path.join(root, fn)


def main():
    ap = argparse.ArgumentParser(description="LLM Wiki content lint (signal)")
    ap.add_argument("--quiet", action="store_true", help="findings only")
    ap.add_argument("--check", choices=["A", "B", "C"], help="run only one check")
    args = ap.parse_args()

    only = args.check
    source_pmids = index_source_pmids()

    findings = []
    n_pages = 0
    for path in iter_pages():
        n_pages += 1
        with open(path, encoding="utf-8") as f:
            content = f.read()
        fields = parse_frontmatter(content) or {}
        body = body_after_frontmatter(content)
        ptype = page_type(path)

        if only in (None, "A"):
            findings += check_a(path, body, ptype)
        if only in (None, "B"):
            findings += check_b(path, body)
        if only in (None, "C") and ptype == "wiki":
            findings += check_c(path, fields, source_pmids)

    # 집계 (검사별)
    buckets = {"A": 0, "B": 0, "C": 0}
    for f in findings:
        buckets[f[0]] += 1

    status = "✅" if not findings else "⚠️"
    print(
        f"{status}  content-lint (signal): {n_pages} pages   "
        f"findings: {len(findings)}  [A/sections:{buckets['A']}  "
        f"B/tags:{buckets['B']}  C/cross-tier:{buckets['C']}]"
    )
    if findings and not args.quiet:
        print()
        for f in sorted(findings):
            print(f"  {f}")

    # SIGNAL: 절대 block하지 않음 — 항상 exit 0.
    sys.exit(0)


if __name__ == "__main__":
    main()
