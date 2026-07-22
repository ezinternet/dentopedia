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
    # frontmatter-only 기계 작업 — tags:/confidence: 필드만 바꿈, 본문 임상 수치 무변화.
    # (2026-07-14 repo-wide 태그 마이그레이션 커밋들이 도구 18개를 가짜 STALE로 밀어 추가)
    r"|mechanical migration"
    r"|\btag scheme\b|\btag brackets?\b|confidence-tag"
    r"|de-inflate|(audit \+ )?de-inflate legacy confidence tags"
    r"|legacy [\w/ +-]*\btags?\b"
    r"|recategorize|\bdedup\b|\breorg\b"
    # confidence → evidence_level 필드 리네임 (2026-07-15, 위키 전역 43개 커밋 469~6 files)
    # — frontmatter 필드명만 바뀜, 본문 임상 수치 무변화.
    r"|confidence\s*→\s*evidence_level"
    # (relations) 스코프 커밋 — 개별 엣지 추가/제거/재라벨링 전부 포함. 이 저장소 컨벤션상
    # relations 스코프면 예외 없이 typed-edge(frontmatter relations: 리스트)만 건드리고
    # 도구가 인용하는 본문 임상 수치는 안 바뀐다. docs(relations):/fix(relations):/
    # feat(relations):/refactor(relations): 전부 해당 (2026-07-17/18 재라벨링 12건이 계기).
    r"|^(docs|fix|feat|refactor)\(relations\):"
    # wikilink 경로 이관 커밋 — 카테고리 서브폴더 이동(예: dental-materials/ →
    # dental-materials/ceramic/, implants/ → implants/mbl+survival/) 후 참조 경로만
    # 일괄 갱신한다. 본문 임상 수치는 한 글자도 안 바뀐다 — 실측: 2026-07-21 스윕의
    # kasem-2025·moy-2005·laumacher-2025는 각각 1줄(±1), implants-clinical-decision-ladder
    # 20줄, drug-antibiotic-stewardship-overview 48줄이 전부 [[...]] 또는 frontmatter
    # source_wiki: 경로였다. 이 스윕이 도구 4개를 가짜 STALE로 밀어 추가(2026-07-23).
    r"|^fix\(links\):"
    r"|update [\w/+-]* ?wikilinks?\b"
    r"|wikilink paths?\b)",
    re.IGNORECASE,
)


def build_git_log_cache(path_glob: str) -> dict:
    """git log 한 번으로 path_glob 하위 모든 파일의 커밋 이력을 수집.

    반환: {relpath: [(date_str, subject), ...]}  — newest-first 순서.
    파일마다 git log를 개별 호출하면 파일 수 × timeout 만큼 걸리는 문제를 해결.
    """
    try:
        out = subprocess.run(
            [
                "git", "log",
                "--format=%cd%x00%s%x00%x01",  # date \0 subject \0 \1 (레코드 구분자)
                "--date=short",
                "--name-only",
                "--", path_glob,
            ],
            cwd=ROOT, capture_output=True, text=True, timeout=120,
        ).stdout
    except Exception:
        return {}

    cache: dict[str, list] = {}
    current_date = None
    current_subject = None
    for line in out.splitlines():
        if "\x00" in line:
            # 헤더 라인: "date\0subject\0\1"
            parts = line.split("\x00")
            current_date = parts[0].strip()
            current_subject = parts[1].strip() if len(parts) > 1 else ""
        elif line.startswith("\x01") or not line.strip():
            continue
        elif current_date is not None:
            # 파일 경로 라인
            relpath = line.strip()
            if relpath:
                cache.setdefault(relpath, []).append((current_date, current_subject))
    return cache


def git_date_from_cache(cache: dict, relpath: str, skip_cosmetic: bool = False):
    """캐시에서 파일의 마지막 커밋 날짜 반환. 없으면 None."""
    entries = cache.get(relpath, [])
    if not entries:
        return None
    if not skip_cosmetic:
        return entries[0][0] or None
    for d, subject in entries:
        if not COSMETIC_SUBJECT_RE.search(subject):
            return d or None
    return entries[-1][0] or None


def main():
    # 두 번의 git log로 interactives/ 와 wiki/ 전체 이력을 한꺼번에 캐시
    tool_cache = build_git_log_cache("interactives/*.html")
    wiki_cache = build_git_log_cache("wiki/**/*.md")

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

        tool_date = git_date_from_cache(tool_cache, f"interactives/{p.name}")
        newer, broken = [], []
        for s in sources:
            s = s.strip()
            if not s or s in ("[]",):
                continue
            sp = ROOT / s
            if not sp.exists():
                broken.append(s)
                continue
            sd = git_date_from_cache(wiki_cache, s, skip_cosmetic=True)
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
