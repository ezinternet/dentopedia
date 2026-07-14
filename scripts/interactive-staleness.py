#!/usr/bin/env python3
"""
interactive-staleness.py — Class B 신호 (임상 interactive 도구의 근거 최신성).

임상 결정 도구(ISQ 로딩·약물 트리·침식 위험도 등)의 숫자는 특정 논문에서 의미를
이해해 추출한 임상 수치다. 배포 스크립트가 이를 기계적으로 재작성하면 임상 수치를
환각/오염시켜 Rule #1(no hallucination)에 위배되므로 자동 재작성하지 않는다.
대신 각 도구의 frontmatter `source_wiki:` 근거 페이지가 도구 파일보다 git상 더 최근에
수정됐으면 "근거가 도구보다 새로움 → 재작성(LLM-in-the-loop) 후보"로 신호만 낸다.
overview-thesis-staleness.py와 동일한 signal 철학 — 차단(gate)하지 않는다.

판정(파일별 git last-commit date 비교):
  - STALE  : source_wiki 중 하나라도 도구보다 나중에 커밋됨 (근거 갱신됨)
  - BROKEN : source_wiki 경로가 실제로 존재하지 않음 (rename 등)
  - OK     : 모든 근거가 도구보다 오래됨
  - meta/통계 도구(category: meta)와 source_wiki 없는 도구는 평가 제외
    (meta는 build-wiki-stats.py가 배포 때 통째로 재생성하므로 staleness 무의미)

실행: python3 scripts/interactive-staleness.py
출력: stdout 요약 + logs/{today}_interactive-staleness.json
      배포 시 도구 본문 <!-- STALENESS:... --> 배지 주입은 하지 않음(읽기 전용 신호).
종료코드: 항상 0 (signal — never blocks).
"""

import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INTERACTIVES = ROOT / "interactives"
LOGS = ROOT / "logs"

SKIP = {"index.html", "overviews-map.html", "wiki-stats-live.html"}


def parse_comment_fm(text: str):
    """상단 <!-- --- ... --- --> 블록에서 category(scalar)와 source_wiki(list) 추출."""
    m = re.search(r"<!--\s*\n---\s*\n(.*?)\n---\s*\n-->", text, flags=re.S)
    block = m.group(1) if m else text[:1200]
    category = None
    sources = []
    in_sw = False
    for line in block.split("\n"):
        cm = re.match(r"^category:\s*(.+)$", line)
        if cm:
            category = cm.group(1).strip().strip('"').strip("'")
            in_sw = False
            continue
        if re.match(r"^source_wiki:\s*(.*)$", line):
            in_sw = True
            inline = re.match(r"^source_wiki:\s*(\S.*)$", line)
            if inline and not inline.group(1).startswith("["):
                sources.append(inline.group(1).strip())
                in_sw = False
            continue
        if in_sw:
            im = re.match(r"^\s*-\s*(.+)$", line)
            if im:
                sources.append(im.group(1).strip().strip('"').strip("'"))
            elif re.match(r"^\S", line):  # 다음 top-level 키 → 리스트 종료
                in_sw = False
    return category, sources


# 근거 페이지에 대한 "임상적으로 무의미한(cosmetic)" 커밋 — git mtime만 밀 뿐 도구가
# 인코딩한 임상 수치는 바꾸지 않는다. 요약 섹션 재포맷·cross-link·relations 배선·카테고리
# 정리가 여기 해당. overview-thesis-staleness.py의 wikilink-only vs thesis 구분과 같은 철학이나,
# 요약 재작성 편집은 diff 라인 모양이 산문(thesis와 구분 불가)이라 커밋 subject로 식별한다.
# 예: 2026-07-05 "Expand Three-line Summary…" 대량 포맷팅 커밋(4,887 파일)이 이 필터로 걸러진다.
COSMETIC_SUBJECT_RE = re.compile(
    r"(Expand Three-line Summary"
    r"|One-line Summary|Three-line Summary"
    r"|한국어 핵심요약|한줄요약|세줄요약"
    r"|cross-link"
    r"|\bwire\b.*(reinforces|contradicts|refines|extends|applies-to|relation)"
    r"|add relations edge"
    r"|recategorize|\bdedup\b|\breorg\b)",
    re.IGNORECASE,
)


def git_date(relpath: str, skip_cosmetic: bool = False):
    """파일의 마지막 커밋 날짜(YYYY-MM-DD). 추적 안 됨/git 실패 시 None.

    skip_cosmetic=True면 cosmetic 커밋(요약 재포맷·cross-link·relations 배선 등)을 건너뛰고
    마지막 '실질' 변경일을 돌려준다 — 대량 포맷팅 커밋이 근거를 도구보다 새것으로
    보이게 하는 오탐지를 막기 위함. 근거(source_wiki) 날짜 계산에만 적용한다.
    """
    try:
        out = subprocess.run(
            ["git", "log", "--format=%cd%x00%s", "--date=short", "--", relpath],
            cwd=ROOT, capture_output=True, text=True, timeout=30, check=True,
        ).stdout.strip()
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError):
        return None
    entries = [line.split("\x00", 1) for line in out.splitlines() if "\x00" in line]
    if not entries:
        return None
    if not skip_cosmetic:
        return entries[0][0] or None
    for d, subject in entries:  # newest → oldest
        if not COSMETIC_SUBJECT_RE.search(subject):
            return d or None
    return entries[-1][0] or None  # 전부 cosmetic이면 생성(가장 오래된) 커밋일 사용


def main():
    results = []
    for p in sorted(INTERACTIVES.glob("*.html")):
        if p.name in SKIP:
            continue
        text = p.read_text(encoding="utf-8")
        category, sources = parse_comment_fm(text)
        if category == "meta":
            continue  # build-wiki-stats.py가 재생성 — staleness 무의미
        if not sources:
            results.append({"tool": p.name, "verdict": "NO_SOURCE", "detail": "source_wiki 비어있음"})
            continue

        tool_date = git_date(f"interactives/{p.name}")
        newer, broken = [], []
        for s in sources:
            s = s.strip()
            if not s or s in ("[]",):
                continue
            sp = ROOT / s
            if not sp.exists():
                broken.append(s)
                continue
            sd = git_date(s, skip_cosmetic=True)
            if tool_date and sd and sd > tool_date:
                newer.append({"src": s, "src_date": sd})

        if broken:
            verdict = "BROKEN"
        elif newer:
            verdict = "STALE"
        else:
            verdict = "OK"
        results.append({
            "tool": p.name, "verdict": verdict, "tool_date": tool_date,
            "newer_sources": newer, "broken_sources": broken,
        })

    LOGS.mkdir(exist_ok=True)
    today = date.today().isoformat()
    logpath = LOGS / f"{today}_interactive-staleness.json"
    logpath.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")

    stale = [r for r in results if r["verdict"] == "STALE"]
    broken = [r for r in results if r["verdict"] == "BROKEN"]
    nosrc = [r for r in results if r["verdict"] == "NO_SOURCE"]
    ok = [r for r in results if r["verdict"] == "OK"]

    print(f"[interactive-staleness] {len(results)} clinical tools: "
          f"{len(ok)} OK · {len(stale)} STALE · {len(broken)} BROKEN · {len(nosrc)} NO_SOURCE")
    for r in stale:
        srcs = ", ".join(f"{n['src'].split('/')[-1]}({n['src_date']})" for n in r["newer_sources"])
        print(f"  STALE  {r['tool']} (도구 {r['tool_date']}) ← 더 최근 근거: {srcs}", file=sys.stderr)
    for r in broken:
        print(f"  BROKEN {r['tool']} ← 없는 근거 경로: {', '.join(r['broken_sources'])}", file=sys.stderr)
    for r in nosrc:
        print(f"  NO_SOURCE {r['tool']}", file=sys.stderr)
    print(f"  → {logpath.relative_to(ROOT)}")
    sys.exit(0)  # signal — never blocks


if __name__ == "__main__":
    main()
