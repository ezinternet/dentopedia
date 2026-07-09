#!/usr/bin/env python3
"""
LLM Wiki — Recall Session (Leitner 간격반복 SRS)

recall/{overview-stem}.json 의 문항 뱅크를 Leitner 박스로 굴린다.
지식을 '검색 가능(QMD)'에서 '인출 가능(retention)'으로 옮기는 루프.

상태: recall/_state.json  {"<stem>::<qid>": {"box": int, "due": "YYYY-MM-DD", "last": "YYYY-MM-DD"}}
간격(일): box 1→3→7→16→35. 정답=박스+1(상한 5), 오답=box 1로 리셋(내일 due).
새 문항은 box 1·오늘 due로 자동 등록.

Usage:
    python3 scripts/recall-session.py --due 7          # 오늘 볼 문항 최대 7개 (JSON)
    python3 scripts/recall-session.py --due 7 --pretty # 사람이 읽는 형식
    python3 scripts/recall-session.py --grade "stem::qid=correct" --grade "stem::qid=wrong"
    python3 scripts/recall-session.py --stats

Signal-style: 항상 exit 0.
"""

import os
import re
import sys
import json
import glob
import argparse
from datetime import date, datetime, timedelta

WIKI_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RECALL_DIR = os.path.join(WIKI_ROOT, "recall")
STATE_PATH = os.path.join(RECALL_DIR, "_state.json")

BOX_INTERVALS = {1: 1, 2: 3, 3: 7, 4: 16, 5: 35}  # days until next due
MAX_BOX = 5


def today() -> date:
    return date.today()


def load_bank() -> dict:
    """key '<stem>::<qid>' → question dict (+_stem, _title)."""
    bank = {}
    for path in sorted(glob.glob(os.path.join(RECALL_DIR, "*.json"))):
        if os.path.basename(path).startswith("_"):
            continue
        try:
            spec = json.loads(open(path, encoding="utf-8").read())
        except (OSError, json.JSONDecodeError):
            continue
        stem = spec.get("overview") or os.path.splitext(os.path.basename(path))[0]
        for i, q in enumerate(spec.get("questions", [])):
            qid = q.get("id") or f"q{i+1}"
            key = f"{stem}::{qid}"
            q = dict(q)
            q["_stem"] = stem
            q["_title"] = spec.get("title", stem)
            bank[key] = q
    return bank


def load_state() -> dict:
    if not os.path.exists(STATE_PATH):
        return {}
    try:
        return json.loads(open(STATE_PATH, encoding="utf-8").read())
    except (OSError, json.JSONDecodeError):
        return {}


def save_state(state: dict) -> None:
    os.makedirs(RECALL_DIR, exist_ok=True)
    with open(STATE_PATH, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def register_new(bank: dict, state: dict) -> None:
    """뱅크에 있으나 상태에 없는 문항 → box1·오늘 due로 등록. 삭제된 문항은 상태에서 제거."""
    t = today().isoformat()
    for key in bank:
        if key not in state:
            state[key] = {"box": 1, "due": t, "last": None}
    for key in list(state):
        if key not in bank:
            del state[key]


def due_questions(bank: dict, state: dict, n: int) -> list:
    t = today()
    due = []
    for key, st in state.items():
        try:
            d = datetime.strptime(st["due"], "%Y-%m-%d").date()
        except (ValueError, KeyError):
            d = t
        if d <= t:
            due.append((d, st.get("box", 1), key))
    # 급한 것(due 오래됨)·낮은 box 우선
    due.sort(key=lambda x: (x[0], x[1]))
    out = []
    for d, box, key in due[:n]:
        q = bank[key]
        out.append({
            "key": key, "stem": q["_stem"], "id": key.split("::", 1)[1],
            "box": box, "due": d.isoformat(),
            "q": q["q"], "opts": q["opts"], "ans": q["ans"],
            "rat": q.get("rat", ""), "cite": q.get("cite", ""),
        })
    return out


def grade(state: dict, key: str, result: str) -> None:
    t = today()
    st = state.get(key)
    if st is None:
        st = {"box": 1, "due": t.isoformat(), "last": None}
    if result == "correct":
        st["box"] = min(MAX_BOX, st.get("box", 1) + 1)
    else:  # wrong
        st["box"] = 1
    st["due"] = (t + timedelta(days=BOX_INTERVALS[st["box"]])).isoformat()
    st["last"] = t.isoformat()
    state[key] = st


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--due", type=int, nargs="?", const=7, default=None,
                    help="오늘 볼 문항 최대 N개 (기본 7)")
    ap.add_argument("--pretty", action="store_true", help="사람이 읽는 형식")
    ap.add_argument("--grade", action="append", default=[],
                    help='"stem::qid=correct|wrong" (반복 가능)')
    ap.add_argument("--stats", action="store_true")
    args = ap.parse_args()

    bank = load_bank()
    state = load_state()
    register_new(bank, state)

    if args.grade:
        for g in args.grade:
            m = re.match(r"^(.+)=(correct|wrong)$", g.strip())
            if not m:
                print(f"⚠ 무시(형식오류): {g}")
                continue
            grade(state, m.group(1), m.group(2))
        save_state(state)
        print(f"✅ {len(args.grade)}개 채점 반영")

    if args.stats or (args.due is None and not args.grade):
        total = len(bank)
        due = len(due_questions(bank, state, 10**9))
        boxes = {}
        for st in state.values():
            boxes[st.get("box", 1)] = boxes.get(st.get("box", 1), 0) + 1
        save_state(state)
        print(f"📚 Recall bank: 문항 {total} · 오늘 due {due}")
        print(f"   박스 분포: " + ", ".join(f"box{b}:{boxes.get(b,0)}" for b in range(1, MAX_BOX+1)))
        return 0

    if args.due is not None:
        picked = due_questions(bank, state, args.due)
        save_state(state)  # 새 문항 등록분 저장
        if args.pretty:
            if not picked:
                print("오늘 due 문항 없음 — 다 굳었습니다.")
            for i, q in enumerate(picked, 1):
                print(f"\n[{i}] ({q['key']} · box{q['box']})")
                print(f"Q. {q['q']}")
                for j, o in enumerate(q["opts"]):
                    print(f"   {j}. {o}")
                print(f"   정답 {q['ans']} — {q['rat']}")
        else:
            print(json.dumps(picked, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
