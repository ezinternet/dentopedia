#!/usr/bin/env python3
"""
LLM Wiki — Recall Session (Leitner 간격반복 SRS)

recall/{overview-stem}.json 의 문항 뱅크를 Leitner 박스로 굴린다.
지식을 '검색 가능(QMD)'에서 '인출 가능(retention)'으로 옮기는 루프.

상태: recall/_state.json  {"<stem>::<qid>": {"box": int, "due": "YYYY-MM-DD", "last": "YYYY-MM-DD"}}
간격(일): box 1→3→7→16→35. 정답=박스+1(상한 5), 오답=box 1로 리셋(내일 due).
새 문항은 box 1·오늘 due로 자동 등록.

Pending 큐 (2026-08-27, agenda/2026-08-27_recall-loop-reactivation.md D1-A):
무인 발화(사용자 부재)에서 제시된 문항이 채점 없이 끝나면 채팅 로그로 증발하고
다음 발화가 --due로 새 배치를 뽑아 그 문항들은 영구 미착수가 된다. recall/_pending.json
이 "제시했지만 아직 채점 안 된 배치"를 파일로 고정해 그 유실을 막는다.
    --due N --write-pending   due 문항을 뽑아 제시 + _pending.json에 저장
    --read-pending            _pending.json이 있으면 그걸(새 --due 대신) 반환 — 지난 배치 재개
    --grade                   채점된 key는 pending에서도 자동 제거, 비면 파일 삭제
    --clear-pending           수동 폐기(배치 자체를 버릴 때만)
호출 측(weekly-recall SKILL.md) 순서: read-pending 먼저 → 있으면 그 배치 재개,
없으면 due+write-pending으로 새 배치 시작. 이러면 어느 시점에 끊겨도 다음 발화가
정확히 그 지점부터 이어받는다 — 세션 크기가 아니라 "미해결 배치 존재 여부"가 핵심.

Usage:
    python3 scripts/recall-session.py --due 7          # 오늘 볼 문항 최대 7개 (JSON)
    python3 scripts/recall-session.py --due 7 --pretty # 사람이 읽는 형식
    python3 scripts/recall-session.py --due 3 --write-pending   # 뽑은 배치를 pending에 고정
    python3 scripts/recall-session.py --read-pending             # 고정된 배치 재개
    python3 scripts/recall-session.py --grade "stem::qid=correct" --grade "stem::qid=wrong"
    python3 scripts/recall-session.py --clear-pending
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
PENDING_PATH = os.path.join(RECALL_DIR, "_pending.json")

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


def load_pending() -> dict | None:
    """{"created": "YYYY-MM-DD", "items": [...]} 또는 파일 없으면 None."""
    if not os.path.exists(PENDING_PATH):
        return None
    try:
        return json.loads(open(PENDING_PATH, encoding="utf-8").read())
    except (OSError, json.JSONDecodeError):
        return None


def save_pending(items: list) -> None:
    os.makedirs(RECALL_DIR, exist_ok=True)
    with open(PENDING_PATH, "w", encoding="utf-8") as f:
        json.dump({"created": today().isoformat(), "items": items}, f,
                   ensure_ascii=False, indent=2)


def clear_pending() -> None:
    if os.path.exists(PENDING_PATH):
        os.remove(PENDING_PATH)


def remove_from_pending(keys: set) -> None:
    """채점된 key들을 pending에서 제거. 비면 파일째 삭제. pending 없으면 no-op."""
    p = load_pending()
    if p is None:
        return
    remaining = [it for it in p.get("items", []) if it.get("key") not in keys]
    if remaining:
        save_pending(remaining)
        # save_pending이 created를 오늘로 갱신해버리므로 원래 created 보존
        p2 = load_pending()
        p2["created"] = p.get("created", p2["created"])
        with open(PENDING_PATH, "w", encoding="utf-8") as f:
            json.dump(p2, f, ensure_ascii=False, indent=2)
    else:
        clear_pending()


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
    ap.add_argument("--write-pending", action="store_true",
                    help="--due로 뽑은 배치를 recall/_pending.json에 고정 (무인 발화 유실 방지)")
    ap.add_argument("--read-pending", action="store_true",
                    help="_pending.json이 있으면 그 배치를 반환(--due 무시), 없으면 빈 결과")
    ap.add_argument("--clear-pending", action="store_true",
                    help="_pending.json 수동 폐기")
    args = ap.parse_args()

    bank = load_bank()
    state = load_state()
    register_new(bank, state)

    if args.clear_pending:
        clear_pending()
        print("🗑  pending 배치 폐기")

    if args.read_pending:
        p = load_pending()
        picked = p["items"] if p else []
        if args.pretty:
            if not picked:
                print("대기 중인 pending 배치 없음.")
            else:
                print(f"(pending 배치 재개 — {p['created']}에 제시된 미채점 {len(picked)}문항)")
            for i, q in enumerate(picked, 1):
                print(f"\n[{i}] ({q['key']} · box{q.get('box','?')})")
                print(f"Q. {q['q']}")
                for j, o in enumerate(q["opts"]):
                    print(f"   {j}. {o}")
                print(f"   정답 {q['ans']} — {q['rat']}")
        else:
            print(json.dumps(picked, ensure_ascii=False, indent=2))
        return 0

    if args.grade:
        graded_keys = set()
        for g in args.grade:
            m = re.match(r"^(.+)=(correct|wrong)$", g.strip())
            if not m:
                print(f"⚠ 무시(형식오류): {g}")
                continue
            grade(state, m.group(1), m.group(2))
            graded_keys.add(m.group(1))
        save_state(state)
        remove_from_pending(graded_keys)
        print(f"✅ {len(args.grade)}개 채점 반영")

    if args.stats or (args.due is None and not args.grade):
        total = len(bank)
        due = len(due_questions(bank, state, 10**9))
        boxes = {}
        for st in state.values():
            boxes[st.get("box", 1)] = boxes.get(st.get("box", 1), 0) + 1
        save_state(state)
        pending = load_pending()
        pending_n = len(pending["items"]) if pending else 0
        print(f"📚 Recall bank: 문항 {total} · 오늘 due {due}")
        print(f"   박스 분포: " + ", ".join(f"box{b}:{boxes.get(b,0)}" for b in range(1, MAX_BOX+1)))
        if pending_n:
            print(f"   ⏳ pending 배치: {pending_n}문항 ({pending['created']}에 제시, 미채점)")
        return 0

    if args.due is not None:
        picked = due_questions(bank, state, args.due)
        save_state(state)  # 새 문항 등록분 저장
        if args.write_pending:
            save_pending(picked)
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
