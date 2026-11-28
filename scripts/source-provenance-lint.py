#!/usr/bin/env python3
from __future__ import annotations
"""
LLM Wiki — Source Provenance Lint (signal)

sources/*.md 의 두 가지 품질을 결정론으로 확인한다.

  A. Limitations 섹션 — '## Limitations' (또는 '## Study Limitations') heading
     이 없으면 한계점 보존이 안 돼 있을 가능성이 높다. 고근거(sr+ma/sr/rct/
     prospective/retrospective) 에서 먼저 확인해야 한다.

  B. Provenance 주석 — 본문에 'Results', 'Table', 'Figure', 'Fig.' 중 하나를
     대괄호/소괄호로 감싸서 출처를 밝힌 주석이 1건 이상 있는가.
     예: (Results, Table 2)  [Table 3]  (Fig. 4A)
     이 주석이 하나도 없으면 "어느 수치가 어느 표에서 왔는지" 30초 추적이
     불가능한 상태다.

설계:
  - signal — daily-audit 에 물려 가시화만 하고 절대 block 하지 않는다.
  - 오래된 인제스트(2026-05-27 이전) 소급 없음 — 한꺼번에 300건+ 경고가 뜨면
    signal 이 노이즈가 된다. --since 로 기준일 조정 가능(기본: 2026-05-27).
  - 증례보고·in-vitro·animal·narrative-review·patent·manual 같이 임상 결과
    테이블이 없는 유형은 B(provenance) 검사만 INFO 로 낮춘다.

Usage:
    python3 scripts/source-provenance-lint.py          # full run
    python3 scripts/source-provenance-lint.py --quiet  # WARN 만
    python3 scripts/source-provenance-lint.py --since 2026-10-01  # 최근 인제스트만
"""

import argparse
import os
import re
import sys
from datetime import date, datetime

SOURCES_DIR = "sources"
LOGS_DIR = "logs"
LOG_FILE = "logs/source-provenance-lint.md"

# 소급 기준 — 이 날짜 이전 인제스트는 체크 대상에서 제외
DEFAULT_SINCE = date(2026, 5, 27)

# Limitations 섹션을 가리키는 heading 패턴
LIMITATIONS_HEADING = re.compile(
    r"^#{2,}\s+(study\s+)?limitations?", re.IGNORECASE | re.MULTILINE
)

# Provenance 주석 패턴 — (Results ...) / [Table 2] / (Fig. 4A) 등
# 대괄호/소괄호 안에 Results/Table/Figure/Fig./Supplementary/Methods 가 있으면 인정
PROVENANCE_PATTERN = re.compile(
    r"[\(\[]\s*(?:Results?|Tables?|Figures?|Fig\.|Supplementary|Methods?)[^\)\]]{0,60}[\)\]]",
    re.IGNORECASE,
)

# 고근거 — Limitations 미보존이 임상 위험도가 더 높은 유형
HIGH_EVIDENCE = {"sr+ma", "sr", "rct", "prospective", "retrospective"}

# 임상 테이블이 없는 유형 — Provenance 주석 없어도 INFO 로만
LOW_TABLE_EVIDENCE = {
    "case-report", "in-vitro", "animal", "narrative-review",
    "consensus", "regulation", "official-qa", "manual", "patent",
    "cross-sectional",
}


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
            k, v = m.group(1).strip(), m.group(2).strip().strip('"').strip("'")
            if k not in out:
                out[k] = v
    return out


def _ingest_date(fm: dict[str, str]) -> date | None:
    raw = fm.get("date", "")
    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%Y-%m"):
        try:
            return datetime.strptime(raw[:10], fmt).date()
        except ValueError:
            continue
    return None


def _body(text: str) -> str:
    m = re.match(r"^---\n.*?\n---\n?(.*)", text, re.DOTALL)
    return m.group(1) if m else text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--quiet", action="store_true",
                        help="WARN 항목만 출력 (INFO 생략)")
    parser.add_argument("--since", default=str(DEFAULT_SINCE),
                        help=f"이 날짜 이후 인제스트만 검사 (기본: {DEFAULT_SINCE})")
    args = parser.parse_args()

    try:
        since = datetime.strptime(args.since[:10], "%Y-%m-%d").date()
    except ValueError:
        print(f"ERROR: --since 날짜 형식 오류: {args.since}")
        return 0

    # (stem, evidence_level, days_old, detail)
    no_limitations_warn: list[tuple[str, str, int]] = []
    no_limitations_info: list[tuple[str, str, int]] = []
    no_provenance_warn: list[tuple[str, str, int]] = []
    no_provenance_info: list[tuple[str, str, int]] = []

    today = date.today()
    total_scanned = total_skipped = 0

    if not os.path.isdir(SOURCES_DIR):
        print(f"SKIP: {SOURCES_DIR}/ 없음 — 올바른 wiki root 에서 실행하세요.")
        return 0

    for fname in sorted(os.listdir(SOURCES_DIR)):
        if not fname.endswith(".md"):
            continue
        path = os.path.join(SOURCES_DIR, fname)
        try:
            text = open(path, encoding="utf-8").read()
        except Exception:
            continue

        fm = _parse_frontmatter(text)
        stem = os.path.splitext(fname)[0]

        d = _ingest_date(fm)
        if d is None or d < since:
            total_skipped += 1
            continue

        total_scanned += 1
        ev = fm.get("evidence_level", fm.get("confidence", "")).lower()
        days_old = (today - d).days
        body = _body(text)

        # ── A. Limitations 섹션 ─────────────────────────────────────────
        has_lim = bool(LIMITATIONS_HEADING.search(body))
        if not has_lim:
            if ev in HIGH_EVIDENCE:
                no_limitations_warn.append((stem, ev, days_old))
            else:
                no_limitations_info.append((stem, ev, days_old))

        # ── B. Provenance 주석 ─────────────────────────────────────────
        has_prov = bool(PROVENANCE_PATTERN.search(body))
        if not has_prov:
            if ev in LOW_TABLE_EVIDENCE:
                no_provenance_info.append((stem, ev, days_old))
            else:
                no_provenance_warn.append((stem, ev, days_old))

    # ── 출력 ────────────────────────────────────────────────────────────
    print("=" * 66)
    print(f"Source Provenance Lint  (since {since})")
    print("=" * 66)

    # A — Limitations
    print(f"\n── A. Limitations 섹션 없음 ────────────────────────────────")
    if no_limitations_warn:
        print(f"⚠  WARN (고근거 — sr+ma/sr/rct/prospective/retrospective) — {len(no_limitations_warn)}건")
        for stem, ev, days in sorted(no_limitations_warn, key=lambda x: (-x[2], x[0])):
            print(f"   [{ev}]  {stem}  ({days}d)")
    elif not args.quiet:
        print(f"✓  WARN 고근거 — 0건")

    if no_limitations_info and not args.quiet:
        print(f"   INFO (기타 근거유형) — {len(no_limitations_info)}건")
        for stem, ev, days in sorted(no_limitations_info, key=lambda x: (-x[2], x[0]))[:10]:
            print(f"   [{ev or '?'}]  {stem}  ({days}d)")
        if len(no_limitations_info) > 10:
            print(f"   … 외 {len(no_limitations_info) - 10}건 (로그 참조)")

    # B — Provenance
    print(f"\n── B. Provenance 주석 없음 ─────────────────────────────────")
    if no_provenance_warn:
        print(f"⚠  WARN — {len(no_provenance_warn)}건")
        for stem, ev, days in sorted(no_provenance_warn, key=lambda x: (-x[2], x[0])):
            print(f"   [{ev or '?'}]  {stem}  ({days}d)")
    elif not args.quiet:
        print(f"✓  WARN — 0건")

    if no_provenance_info and not args.quiet:
        print(f"   INFO (임상 테이블 없는 유형 — case-report/in-vitro 등) — {len(no_provenance_info)}건")

    # 요약
    print()
    print("─" * 66)
    print(f"  scanned (since {since})  : {total_scanned}")
    print(f"  skipped (before cutoff)  : {total_skipped}")
    print(f"  no Limitations  WARN     : {len(no_limitations_warn)}")
    print(f"  no Limitations  INFO     : {len(no_limitations_info)}")
    print(f"  no Provenance   WARN     : {len(no_provenance_warn)}")
    print(f"  no Provenance   INFO     : {len(no_provenance_info)}")
    print("─" * 66)

    # 로그 작성
    os.makedirs(LOGS_DIR, exist_ok=True)
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write(f"# Source Provenance Lint — {today}  (since {since})\n\n")
        f.write(f"- scanned: {total_scanned}\n")
        f.write(f"- no Limitations WARN: {len(no_limitations_warn)}\n")
        f.write(f"- no Limitations INFO: {len(no_limitations_info)}\n")
        f.write(f"- no Provenance WARN: {len(no_provenance_warn)}\n")
        f.write(f"- no Provenance INFO: {len(no_provenance_info)}\n\n")
        if no_limitations_warn:
            f.write("## A. No Limitations — WARN (고근거)\n\n")
            for stem, ev, days in sorted(no_limitations_warn, key=lambda x: (-x[2], x[0])):
                f.write(f"- `{stem}` [{ev}] ({days}d)\n")
            f.write("\n")
        if no_limitations_info:
            f.write("## A. No Limitations — INFO\n\n")
            for stem, ev, days in sorted(no_limitations_info, key=lambda x: (-x[2], x[0])):
                f.write(f"- `{stem}` [{ev or '?'}] ({days}d)\n")
            f.write("\n")
        if no_provenance_warn:
            f.write("## B. No Provenance annotation — WARN\n\n")
            for stem, ev, days in sorted(no_provenance_warn, key=lambda x: (-x[2], x[0])):
                f.write(f"- `{stem}` [{ev or '?'}] ({days}d)\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
