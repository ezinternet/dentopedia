#!/usr/bin/env python3
"""
deviation-audit.py — Rule-of-Three SOP revision trigger (억제 도입판)

Reads logs/ingest-deviations.md and surfaces types that are worth an SOP change.

왜 억제가 필요한가 (2026-08-25)
--------------------------------
원판은 "유형별 누적 ≥3이면 SOP 개정 후보"였다. 로그가 334건까지 자라자
**20종 중 16종이 후보**로 찍혔다. 전부가 후보면 아무것도 후보가 아니다.
AUDITS.md가 논쟁 레이더에서 이미 배운 교훈과 같다 —
*"억제되지 않는 신호는 끌 수 없고, 끌 수 없는 신호는 노이즈가 된다."*

억제는 세 겹이다. **뮤트가 아니라 이동** — 제외된 유형도 아래에 계속 출력한다
(supersession-audit의 `chain intentional` 처리와 같은 원칙).

  ① 판단 기록형 6종 제외
     relation/category/confidence/supersession/evidence-level/reporting-judgment.
     이건 SOP 위반이 아니라 **SOP가 시킨 대로 판단을 남긴 것**이다.
     인제스트마다 LLM이 내린 판단의 감사추적이지 결함이 아니다.
     2026-08-25 실측 100건(전체의 30%)이 전부 여기였다.

  ② 자기소멸형 제외
     batch-relation-pending은 "배치라 relations를 나중에 달겠다"는 예고다.
     2026-08-25 전수 확인 결과 17건 **전부** relations 8~26개로 해소됐는데,
     로그가 append-only라 영구히 카운트됐다.

  ③ 임계값을 최근 30일 창으로
     누적수는 위키가 살아있는 한 단조증가라 임계값이 의미를 잃는다.
     "지금 반복되고 있는가"가 SOP 개정의 실제 판단 기준이다.

Signal only — never blocks.

Usage:
    python3 scripts/deviation-audit.py
    python3 scripts/deviation-audit.py --window 60
"""

import argparse
import sys
from collections import Counter
from datetime import date, datetime, timedelta
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LOG = REPO / "logs" / "ingest-deviations.md"

THRESHOLD = 3
WINDOW_DAYS = 30

# ① 판단 기록형 — SOP 위반이 아니라 SOP 준수의 산물.
JUDGMENT_TYPES = {
    "relation-judgment",
    "category-judgment",
    "confidence-judgment",
    "supersession-judgment",
    "evidence-level-judgment",
    "reporting-judgment",
}

# ② 자기소멸형 — 예고일 뿐, 후속 작업으로 해소된다.
SELF_RESOLVING_TYPES = {
    "batch-relation-pending",
}

# 참고용 분류 — 후보에서 빼지는 않지만, 근본원인이 위키 밖(페이월·PMC 추출)에
# 있어 SOP로 고칠 수 있는 폭이 좁다는 것을 읽는 사람에게 알린다.
EXTERNAL_CONSTRAINT_TYPES = {
    "abstract-only",
    "empty-pmc-text",
    "partial-pmc-text",
    "no-doi",
    "date-fallback",
}


def parse_rows(text: str) -> list[dict]:
    rows = []
    for line in text.splitlines():
        if not line.startswith("| 20"):
            continue
        parts = [p.strip() for p in line.split("|")[1:-1]]
        if len(parts) < 4:
            continue
        try:
            d = datetime.strptime(parts[0], "%Y-%m-%d").date()
        except ValueError:
            d = None
        rows.append({"date": parts[0], "d": d, "stem": parts[1], "type": parts[2], "desc": parts[3]})
    return rows


def show(label: str, counts: Counter, rows: list[dict], window_counts: Counter) -> None:
    if not counts:
        return
    print(f"\n  {label}")
    for dtype, n in counts.most_common():
        w = window_counts.get(dtype, 0)
        print(f"    {n:3d} 누적 / {w:2d} 최근  {dtype}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--window", type=int, default=WINDOW_DAYS, help="최근 N일 창 (기본 30)")
    args = ap.parse_args()

    if not LOG.exists():
        print("No deviations logged yet. (logs/ingest-deviations.md not found)")
        return 0

    rows = parse_rows(LOG.read_text())
    total = len(rows)
    cutoff = date.today() - timedelta(days=args.window)
    recent = [r for r in rows if r["d"] and r["d"] >= cutoff]

    all_counts = Counter(r["type"] for r in rows)
    win_counts = Counter(r["type"] for r in recent)

    print(f"Total deviations logged: {total}   (최근 {args.window}일: {len(recent)}건)")
    print(f"억제: 판단기록형 {len(JUDGMENT_TYPES)}종 + 자기소멸형 {len(SELF_RESOLVING_TYPES)}종 제외, "
          f"임계값 = 최근 {args.window}일 내 ≥{THRESHOLD}회")

    suppressed = JUDGMENT_TYPES | SELF_RESOLVING_TYPES
    candidates = [
        (t, win_counts[t], all_counts[t])
        for t in win_counts
        if t not in suppressed and win_counts[t] >= THRESHOLD
    ]
    candidates.sort(key=lambda x: -x[1])

    if candidates:
        print()
        print("=" * 68)
        print(f"SOP REVISION CANDIDATES — 최근 {args.window}일 내 {THRESHOLD}회 이상:")
        for dtype, wn, an in candidates:
            tag = "  [외부제약 — SOP 개정 폭 좁음]" if dtype in EXTERNAL_CONSTRAINT_TYPES else ""
            print(f"\n  [{wn}x 최근 / {an}x 누적] {dtype}{tag}")
            for ex in [r for r in recent if r["type"] == dtype][-3:]:
                print(f"    {ex['date']}  {ex['stem']}")
                print(f"    → {ex['desc'][:80]}")
        print()
        print("Action: identify root cause, update CLAUDE.md / relevant SKILL.md.")
        print("=" * 68)
    else:
        print(f"\n✅ SOP 개정 후보 없음 — 최근 {args.window}일 내 {THRESHOLD}회 이상 반복된 "
              f"비판단형 편차가 없다.")

    # ── 뮤트가 아니라 이동: 제외분·나머지를 전부 계속 보여준다 ──
    print()
    print("-" * 68)
    print("참고 — 후보에서 제외된 유형 (뮤트 아님)")
    show("① 판단 기록형 (SOP 준수의 산물, 결함 아님)",
         Counter({t: all_counts[t] for t in JUDGMENT_TYPES if t in all_counts}), rows, win_counts)
    show("② 자기소멸형 (후속 작업으로 해소됨)",
         Counter({t: all_counts[t] for t in SELF_RESOLVING_TYPES if t in all_counts}), rows, win_counts)
    below = Counter({
        t: all_counts[t] for t in all_counts
        if t not in suppressed and win_counts.get(t, 0) < THRESHOLD
    })
    show(f"③ 최근 {args.window}일 내 {THRESHOLD}회 미만 (아직 반복 아님)", below, rows, win_counts)
    print("-" * 68)

    return 0


if __name__ == "__main__":
    sys.exit(main())
