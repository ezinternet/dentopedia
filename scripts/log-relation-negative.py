#!/usr/bin/env python3
"""
log-relation-negative.py — 논쟁 레이더 "검토했고 엣지 불필요" 대장 (억제 피더)

Usage:
    python3 scripts/log-relation-negative.py <source-stem> <target-stem|NOTARGET> "<충돌문장>" "<사유>"

왜 필요한가
-----------
`find-contradiction-candidates.py`는 "typed 엣지가 있으면 억제"한다. 그런데 검토
결과가 **NONE**(엣지 불필요)이면 엣지가 안 생기므로 **다음날 같은 후보가 그대로
다시 뜬다.** 판정 노동이 통째로 증발하는 구조다. 그 스크립트 주석이 이미 이 함정을
경고하고 있다 — "판단을 기록할 수단이 없어 같은 쌍이 매일 영구 재방출된다. 끌 수
없는 신호는 시간이 지나면 노이즈가 된다."

이 대장이 그 빠진 반쪽이다: **부정 판정도 지식이다.**

키 설계 — 왜 문장 해시인가
--------------------------
키는 `(source, target, 충돌문장 해시)`다. `(source, target)`만으로 키를 잡으면
페이지 내용이 바뀌어 **진짜 충돌이 새로 생겨도** 영원히 억제된다. 문장이 바뀌면
해시가 달라져 자동으로 재검토 대상이 되는 것이 옳은 동작이다.

해시는 공백 정규화 후 sha1 앞 12자. 대소문자·구두점은 보존한다(의미가 바뀌는
수정을 놓치지 않기 위해).

대상이 특정되지 않은 후보(HIGH-no-target)는 target을 `NOTARGET`으로 적는다.

Appends one row to logs/relation-negatives.md.
find-contradiction-candidates.py reads this file and suppresses matching candidates.
"""

import hashlib
import re
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LOG = REPO / "logs" / "relation-negatives.md"

HEADER = (
    "# Relation Negatives — 검토했고 엣지 불필요\n\n"
    "논쟁 레이더 후보를 두 페이지 다 읽고 판정한 결과 **엣지가 필요 없다**고 결론난 건들.\n"
    "`find-contradiction-candidates.py`가 이 파일을 읽어 해당 후보를 억제한다.\n\n"
    "키는 `(source, target, 문장해시)`다 — 문장이 바뀌면 해시가 달라져 **자동으로\n"
    "재검토 대상이 된다.** 페이지가 개정돼 진짜 충돌이 새로 생기는 경우를 놓치지 않기 위함.\n\n"
    "부정 판정도 지식이다. 지우지 말 것 — 지우면 그 판정 노동이 사라진다.\n\n"
    "| date | source | target | snippet_hash | reason |\n"
    "|------|--------|--------|--------------|--------|\n"
)


def snippet_hash(snippet: str) -> str:
    """충돌 문장 → 안정적 12자 해시. 공백만 정규화."""
    norm = re.sub(r"\s+", " ", snippet).strip()
    return hashlib.sha1(norm.encode("utf-8")).hexdigest()[:12]


def load_suppressed(path: Path = LOG) -> set:
    """{(source, target, hash)} — 감사가 import해서 쓴다."""
    out = set()
    if not path.exists():
        return out
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| 20"):          # 데이터 행만 (헤더/구분선 제외)
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 4:
            continue
        _date, src, tgt, h = cells[0], cells[1], cells[2], cells[3]
        out.add((src, tgt, h))
    return out


def main() -> int:
    if len(sys.argv) < 5:
        print(
            "Usage: log-relation-negative.py <source-stem> <target-stem|NOTARGET> "
            '"<충돌문장>" "<사유>"',
            file=sys.stderr,
        )
        return 1

    src, tgt, snippet = sys.argv[1], sys.argv[2], sys.argv[3]
    reason = " ".join(sys.argv[4:])
    h = snippet_hash(snippet)

    if not LOG.exists():
        LOG.write_text(HEADER, encoding="utf-8")

    if (src, tgt, h) in load_suppressed():
        print(f"already logged: {src} → {tgt} ({h})")
        return 0

    safe = lambda s: s.replace("|", "\\|")
    with LOG.open("a", encoding="utf-8") as f:
        f.write(
            f"| {date.today().isoformat()} | {safe(src)} | {safe(tgt)} | {h} | {safe(reason)} |\n"
        )
    print(f"logged: {src} → {tgt} ({h})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
