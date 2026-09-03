#!/usr/bin/env python3
"""
log-decay-review.py — decay 후보 검토 결과 대장 (억제 피더)

Usage:
    python3 scripts/log-decay-review.py <stem> <still-current|needs-update> "<사유>"

`supersession-audit.py`의 decay 신호는 판정 결과가 "아직 유효"일 때 **페이지에 아무
변화를 남기지 않으므로** 다음날 같은 후보가 다시 뜬다. 이 대장이 그 판정을 기록해
억제로 되먹인다. 설계 근거는 logs/decay-reviewed.md 머리말 참조.
"""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LEDGER = REPO / "logs" / "decay-reviewed.md"
VERDICTS = {"still-current", "needs-update"}


def main() -> int:
    if len(sys.argv) != 4:
        print(__doc__.strip())
        return 2
    stem, verdict, reason = sys.argv[1].strip(), sys.argv[2].strip(), sys.argv[3].strip()
    if verdict not in VERDICTS:
        print(f"verdict must be one of {sorted(VERDICTS)}")
        return 2
    if not reason:
        print("사유 없는 등재 금지 — 왜 아직 유효한지 남지 않으면 다음 사람이 판단할 수 없다")
        return 2
    if not any((REPO / "wiki").rglob(f"{stem}.md")):
        print(f"⚠ wiki/에서 {stem}.md 를 찾을 수 없다 — stem을 확인할 것")
        return 2

    row = f"| {date.today().isoformat()} | {stem} | {verdict} | {reason.replace('|', '/')} |\n"
    with LEDGER.open("a", encoding="utf-8") as f:
        f.write(row)
    print(f"✓ 기록: {stem} [{verdict}]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
