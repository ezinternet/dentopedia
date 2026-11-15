#!/usr/bin/env python3
from __future__ import annotations
"""
LLM Wiki — Parse Gap Flag Audit (signal)

인제스트 시 PDF 파싱이 불완전해 LLM이 수치를 추론으로 채우는 사고를 막기 위해,
sources/*.md 에서 '[원문 표 대조 필요]' 플래그가 사용되고 있는지 추적한다.

두 가지를 본다:

  PENDING — '[원문 표 대조 필요]' 플래그가 있는 파일
    → 수동으로 원본 PDF와 대조해야 하는 미해결 항목.
    → days_pending 가 WARN_DAYS(30) 이상이면 WARN, 미만이면 INFO.

  ABSTRACT_ONLY — source_collection 이 pubmed-abstract 인 파일
    → 전문이 없으므로 결과 수치 보존 무결성을 PDF로 검증할 수 없는 구조.
    → 오래됐다고 WARN 이 나오는 것이 아니라, 개수 추적용 INFO 버킷.

[원문 표 대조 필요]는 기계가 채울 수 없는 빈칸이므로 플래그 존재 자체를 오류로
보지 않는다 — 플래그가 오랫동안 미해결 상태로 남아 있을 때만 signal 을 올린다.

Usage:
    python3 scripts/parse-gap-flag-audit.py          # full run
    python3 scripts/parse-gap-flag-audit.py --quiet  # WARN / PENDING 만
    python3 scripts/parse-gap-flag-audit.py --days 60  # 임계값 조정
"""

import argparse
import os
import re
import sys
from datetime import date, datetime

SOURCES_DIR = "sources"
LOGS_DIR = "logs"
LOG_FILE = "logs/parse-gap-flag-audit.md"

WARN_DAYS = 30          # PENDING 항목이 이 일수 이상 미해결이면 WARN
FLAG_PATTERN = re.compile(r"\[원문\s*표\s*대조\s*필요\]", re.IGNORECASE)

# 이 source_collection 값은 전문이 없는 것으로 간주
ABSTRACT_ONLY_VALUES = {"pubmed-abstract"}

# 임상 수치 보존이 중요한 근거 등급 — ABSTRACT_ONLY 버킷에서 별도 카운트
HIGH_EVIDENCE = {"sr+ma", "sr", "rct", "prospective", "retrospective"}


def _parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    out: dict[str, str] = {}
    for line in text[3:end].splitlines():
        m = re.match(r"^(\w[\w_-]*)\s*:\s*(.+)$", line)
        if m:
            k = m.group(1).strip()
            v = m.group(2).strip().strip('"').strip("'")
            if k not in out:
                out[k] = v
    return out


def _ingest_date(fm: dict[str, str]) -> date | None:
    """frontmatter 의 date: 필드에서 날짜 추출."""
    raw = fm.get("date", "")
    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%Y-%m"):
        try:
            return datetime.strptime(raw[:10], fmt).date()
        except ValueError:
            continue
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--quiet", action="store_true",
                        help="WARN / PENDING 항목만 출력 (OK 생략)")
    parser.add_argument("--days", type=int, default=WARN_DAYS,
                        help=f"미해결 경과일 임계값 (기본 {WARN_DAYS})")
    args = parser.parse_args()
    warn_days = args.days

    today = date.today()

    pending_warn: list[tuple[str, int]] = []   # (stem, days_pending)
    pending_info: list[tuple[str, int]] = []
    abstract_only: list[tuple[str, str, str]] = []  # (stem, evidence_level, date_str)
    total_sources = 0

    if not os.path.isdir(SOURCES_DIR):
        print(f"SKIP: {SOURCES_DIR}/ 없음 — 올바른 wiki root 에서 실행하세요.")
        return 0

    for fname in sorted(os.listdir(SOURCES_DIR)):
        if not fname.endswith(".md"):
            continue
        total_sources += 1
        path = os.path.join(SOURCES_DIR, fname)
        try:
            text = open(path, encoding="utf-8").read()
        except Exception:
            continue

        fm = _parse_frontmatter(text)
        stem = os.path.splitext(fname)[0]

        # ── PENDING 검사 ────────────────────────────────────────────────
        if FLAG_PATTERN.search(text):
            d = _ingest_date(fm)
            days_pending = (today - d).days if d else -1
            if days_pending < 0 or days_pending >= warn_days:
                pending_warn.append((stem, days_pending))
            else:
                pending_info.append((stem, days_pending))

        # ── ABSTRACT_ONLY 검사 ──────────────────────────────────────────
        sc = fm.get("source_collection", "").lower()
        if sc in ABSTRACT_ONLY_VALUES:
            ev = fm.get("evidence_level", fm.get("confidence", "?"))
            d = _ingest_date(fm)
            abstract_only.append((stem, ev, str(d) if d else "?"))

    # ── 출력 ────────────────────────────────────────────────────────────
    print("=" * 66)
    print("Parse Gap Flag Audit")
    print("=" * 66)

    # PENDING WARN
    if pending_warn:
        print(f"\n⚠  PENDING (미해결 ≥{warn_days}일 또는 날짜 미상) — {len(pending_warn)}건")
        for stem, days in sorted(pending_warn, key=lambda x: -x[1]):
            age = f"{days}일" if days >= 0 else "날짜 미상"
            print(f"   {stem}  ({age})")
    elif not args.quiet:
        print(f"\n✓  PENDING (미해결 ≥{warn_days}일) — 0건")

    # PENDING INFO
    if pending_info and not args.quiet:
        print(f"\n   PENDING (최근 {warn_days}일 이내 — 처리 중) — {len(pending_info)}건")
        for stem, days in sorted(pending_info, key=lambda x: x[1]):
            print(f"   {stem}  ({days}일)")

    # ABSTRACT_ONLY
    high_ev = [(s, e, d) for s, e, d in abstract_only if e in HIGH_EVIDENCE]
    if abstract_only and not args.quiet:
        print(f"\n   ABSTRACT_ONLY (pubmed-abstract) — {len(abstract_only)}건")
        if high_ev:
            print(f"   └ 고근거 (sr+ma/sr/rct/prospective/retrospective): {len(high_ev)}건")
            for stem, ev, dt in sorted(high_ev):
                print(f"     {stem}  [{ev}]  {dt}")

    # 요약
    print()
    print("─" * 66)
    total_flag = len(pending_warn) + len(pending_info)
    print(f"  total sources       : {total_sources}")
    print(f"  [원문 표 대조 필요] 플래그 : {total_flag}  (WARN {len(pending_warn)} / INFO {len(pending_info)})")
    print(f"  abstract-only       : {len(abstract_only)}  (고근거 {len(high_ev)})")
    print("─" * 66)

    # 로그 작성
    os.makedirs(LOGS_DIR, exist_ok=True)
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write(f"# Parse Gap Flag Audit — {today}\n\n")
        f.write(f"- total sources: {total_sources}\n")
        f.write(f"- pending flags (WARN ≥{warn_days}d): {len(pending_warn)}\n")
        f.write(f"- pending flags (INFO <{warn_days}d): {len(pending_info)}\n")
        f.write(f"- abstract-only: {len(abstract_only)} (high-evidence: {len(high_ev)})\n\n")
        if pending_warn:
            f.write("## PENDING (미해결)\n\n")
            for stem, days in sorted(pending_warn, key=lambda x: -x[1]):
                age = f"{days}d" if days >= 0 else "unknown"
                f.write(f"- `{stem}` ({age})\n")
            f.write("\n")
        if high_ev:
            f.write("## Abstract-Only 고근거\n\n")
            for stem, ev, dt in sorted(high_ev):
                f.write(f"- `{stem}` [{ev}] {dt}\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
