#!/usr/bin/env python3
"""
LLM Wiki — Recall Coverage Audit (retention 백로그 신호)

overview 중 recall/{stem}.json 리콜 스펙이 없는 것 = '기억 백로그'.
output-coverage(Express)와 짝을 이루는 retention 축 신호.
forward-only: 신규 overview 저작 시 3문항을 함께 만든다(소급 백필 없음).

인출 활성도 신호(D4, 2026-08-27):
_state.json 기반 루프 생사 진단 — 스펙 존재만으로는 "스펙 있는데 루프 죽음"
패턴을 감사가 못 잡기 때문에 추가됨 (agenda/2026-08-27_recall-loop-reactivation.md).
  • last_graded / days_since: 마지막 채점 날짜 & 경과일 → 14일 초과면 WARN
  • never_graded: 한 번도 안 채점된 문항(last=None)
  • box_ge2_ratio: box≥2 비율(적어도 한 번 맞힌 문항)
  • graded_30d: 최근 30일 채점 수

Output: logs/{date}_recall-coverage.log
Signal, not gate. 항상 exit 0.
"""

import os
import re
import sys
import glob
import json
from datetime import date, datetime, timedelta

WIKI_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OVERVIEWS_DIR = os.path.join(WIKI_ROOT, "wiki", "overviews")
RECALL_DIR = os.path.join(WIKI_ROOT, "recall")
WIKI_DIR = os.path.join(WIKI_ROOT, "wiki")
LOGS_DIR = os.path.join(WIKI_ROOT, "logs")

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")


def overview_stems() -> set[str]:
    if not os.path.isdir(OVERVIEWS_DIR):
        return set()
    return {os.path.splitext(f)[0] for f in os.listdir(OVERVIEWS_DIR)
            if f.endswith(".md") and not f.startswith("_")}


def recall_stems() -> set[str]:
    if not os.path.isdir(RECALL_DIR):
        return set()
    return {os.path.splitext(os.path.basename(p))[0]
            for p in glob.glob(os.path.join(RECALL_DIR, "*.json"))
            if not os.path.basename(p).startswith("_")}


STALE_WARN_DAYS = 14  # 마지막 채점 이후 이 일수 초과면 루프 정지 의심 WARN


def activity_signal(state_path: str) -> dict:
    """_state.json에서 인출 활성도 지표를 계산한다. 파일 없으면 zero값 반환."""
    if not os.path.exists(state_path):
        return {}
    try:
        state = json.loads(open(state_path, encoding="utf-8").read())
    except (OSError, json.JSONDecodeError):
        return {}

    today = date.today()
    cutoff_30d = (today - timedelta(days=30)).isoformat()

    total = len(state)
    never_graded = 0
    box_ge2 = 0
    graded_30d = 0
    last_dates: list[str] = []

    for entry in state.values():
        last = entry.get("last")
        box = entry.get("box", 1)
        if last is None:
            never_graded += 1
        else:
            last_dates.append(last)
            if last >= cutoff_30d:
                graded_30d += 1
        if box >= 2:
            box_ge2 += 1

    last_graded = max(last_dates) if last_dates else None
    days_since = (today - date.fromisoformat(last_graded)).days if last_graded else None

    return {
        "total": total,
        "never_graded": never_graded,
        "box_ge2": box_ge2,
        "graded_30d": graded_30d,
        "last_graded": last_graded,
        "days_since": days_since,
    }


def inbound_centrality() -> dict[str, int]:
    counts: dict[str, int] = {}
    for root, _, files in os.walk(WIKI_DIR):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            try:
                content = open(os.path.join(root, fn), encoding="utf-8").read()
            except (OSError, UnicodeDecodeError):
                continue
            for m in WIKILINK_RE.finditer(content):
                stem = os.path.basename(m.group(1).strip())
                if "." in stem:
                    stem = os.path.splitext(stem)[0]
                counts[stem] = counts.get(stem, 0) + 1
    return counts


def main() -> int:
    overviews = overview_stems()
    total = len(overviews)
    covered = overviews & recall_stems()
    centrality = inbound_centrality()
    uncovered = sorted(overviews - covered, key=lambda s: (-centrality.get(s, 0), s))

    ratio = (len(covered) / total * 100) if total else 0.0
    today = date.today().isoformat()

    state_path = os.path.join(RECALL_DIR, "_state.json")
    sig = activity_signal(state_path)

    # --- 인출 활성도 블록 구성 ---
    act_lines: list[str] = []
    if not sig:
        act_lines.append("인출 활성도    : _state.json 없음 (채점 이력 없음)")
    else:
        s_total = sig["total"]
        never = sig["never_graded"]
        ge2 = sig["box_ge2"]
        g30 = sig["graded_30d"]
        last = sig["last_graded"]
        days = sig["days_since"]
        ge2_ratio = ge2 / s_total * 100 if s_total else 0.0
        never_ratio = never / s_total * 100 if s_total else 0.0

        stale_flag = ""
        if days is None:
            stale_flag = "  ⚠  한 번도 채점 없음"
        elif days > STALE_WARN_DAYS:
            stale_flag = f"  ⚠  WARN: {days}일 경과 — 루프 정지 의심"

        act_lines += [
            f"인출 활성도    : (아래 지표는 _state.json 기반, 스펙 존재와 독립)",
            f"  last_graded  : {last or '없음'}{stale_flag}",
            f"  graded_30d   : {g30}문항 (최근 30일 채점)",
            f"  never_graded : {never}/{s_total}  ({never_ratio:.0f}%) — 스펙 있어도 한 번도 안 풂",
            f"  box≥2        : {ge2}/{s_total}  ({ge2_ratio:.0f}%) — 적어도 한 번 맞힌 문항",
        ]

    lines = [
        f"# Recall Coverage — {today}",
        f"TOTAL overviews            : {total}",
        f"COVERED (리콜 스펙 존재)   : {len(covered)}  ({ratio:.1f}%)",
        f"UNCOVERED (기억 백로그)    : {len(uncovered)}",
        "",
    ] + act_lines + [
        "",
        f"=== uncovered, 허브순 top 30 (문항 저작 우선순위) ===",
        f"  {'inbound':>7}  stem",
    ]
    for s in uncovered[:30]:
        lines.append(f"  {centrality.get(s, 0):>7}  {s}")
    if len(uncovered) > 30:
        lines.append(f"  ... ({len(uncovered) - 30} more)")

    output = "\n".join(lines) + "\n"
    os.makedirs(LOGS_DIR, exist_ok=True)
    with open(os.path.join(LOGS_DIR, f"{today}_recall-coverage.log"), "w", encoding="utf-8") as f:
        f.write(output)

    # stdout 요약 (daily-audit.py가 파싱하는 한 줄)
    stale_warn = ""
    if sig:
        days = sig.get("days_since")
        if days is None or days > STALE_WARN_DAYS:
            stale_warn = f"  ⚠ 루프 {days if days is not None else '∞'}일 정지"
    print(f"🧠 Recall Coverage: {len(covered)}/{total} overviews 리콜화 "
          f"({ratio:.1f}%), {len(uncovered)} uncovered{stale_warn}")
    if sig:
        print(f"   활성도: last {sig['last_graded'] or '없음'} · "
              f"30d채점 {sig['graded_30d']} · box≥2 {sig['box_ge2']}/{sig['total']}")
    print(f"    log → logs/{today}_recall-coverage.log")
    return 0


if __name__ == "__main__":
    sys.exit(main())
