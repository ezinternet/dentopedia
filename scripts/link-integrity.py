#!/usr/bin/env python3
"""
LLM Wiki — Link & Index Integrity Audit (signal, non-blocking)

Astro-Han karpathy-llm-wiki의 lint 개념 중 본 wiki에 없던 두 검사를 신호화:
  (1) 본문 wikilink 무결성 — wiki/ 본문의 모든 [[stem]]이 실존 문서로 resolve되는가.
      (supersession-audit·relations-audit는 전용 필드만 검사 → 일반 본문 링크는 사각지대였음)
  (2) index.md 양방향 커버리지 — 모든 wiki 페이지가 index에 등재됐는가 / index 항목이
      실존 페이지를 가리키는가.
  (3) 경로형 wikilink의 경로 정확도 — [[cat/sub/stem]]에 적힌 폴더 경로가 실제 파일
      위치와 일치하는가. (1)은 stem만 resolve하므로 경로가 틀려도 통과시킨다.
      Quartz는 markdownLinkResolution: "shortest"에서 경로 없는 bare link만 파일명
      매칭으로 구제하고, 경로형 링크는 그 경로 그대로 absolute 해석한다 → 경로가
      틀리면 배포 사이트에서 404다. 2026-08-27에 이 사각지대로 55건이 쌓여 있었다.

false positive를 줄이기 위해 link target은 wiki ∪ sources ∪ agenda ∪ note-meeting ∪
slides ∪ peer-review 전체 stem으로 resolve한다(cross-tier 링크 허용).

gate 아닌 signal — "ingest 압력은 가시성으로 자가교정"(CLAUDE.md 원칙)에 맞춰 비차단.

Output: logs/{date}_link-integrity.log
Exit: 항상 0. daily-audit.py 통합 시 must_pass=False.

Usage:
    python3 scripts/link-integrity.py [--stdout]
"""

import re
import sys
import argparse
from datetime import date
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = WIKI_ROOT / "wiki"
INDEX = WIKI_ROOT / "index.md"
LOGS_DIR = WIKI_ROOT / "logs"

# link target resolve 범위 (cross-tier 허용)
KNOWN_DIRS = ["wiki", "sources", "agenda", "note-meeting", "slides", "peer-review"]
SKIP_DIRS = {"_lint"}
SKIP_PAGE_FILES = {"index.md"}
# index.md 등재 의무에서만 면제되는 디렉터리 (링크 대상으로는 계속 유효 —
# SKIP_DIRS에 넣으면 [[_meta/categories]] 같은 링크가 broken으로 잡힌다).
# wiki/_meta/ 는 카테고리 라우팅 등 에이전트용 참조 문서이지 독자용 콘텐츠 페이지가 아니다.
INDEX_EXEMPT_DIRS = {"_meta"}

WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")

# 경로 검사 제외 접두어 — wiki/ 밖 티어. Quartz content 루트에 복사되지 않으므로
# 경로 규약 자체가 다르다(사이트가 아닌 Obsidian vault 기준 경로).
# "wiki"는 여기 넣지 않는다 — 배포 시 wiki/ '내용물'이 content 루트가 되므로
# [[wiki/...]] 접두어는 사이트에서 틀린 경로다.
CROSS_TIER_PREFIXES = {"sources", "agenda", "note-meeting", "slides",
                       "peer-review", "interactives", "lectures", "logs"}


def link_to_stem(raw: str) -> str:
    """[[wiki/cat/stem#heading|alias]] → stem."""
    s = raw.split("|")[0].split("#")[0].strip()
    if "/" in s:
        s = s.split("/")[-1]
    return s.replace(".md", "").strip()


def link_to_path(raw: str) -> str:
    """[[wiki/cat/stem#heading|alias]] → 'wiki/cat/stem' (경로 보존, alias·anchor만 제거)."""
    s = raw.split("|")[0].split("#")[0].strip()
    if s.endswith(".md"):
        s = s[:-3]
    return s.strip()


def collect_wiki_paths() -> tuple[dict[str, list[str]], set[str]]:
    """wiki/ 하위 실제 경로 맵 (stem → [wiki 기준 상대경로]) + 폴더 경로 집합."""
    paths: dict[str, list[str]] = {}
    for f in WIKI_DIR.rglob("*.md"):
        if any(p in SKIP_DIRS for p in f.parts):
            continue
        paths.setdefault(f.stem, []).append(f.relative_to(WIKI_DIR).with_suffix("").as_posix())
    dirs = {d.relative_to(WIKI_DIR).as_posix()
            for d in WIKI_DIR.rglob("*") if d.is_dir()}
    return paths, dirs


def collect_known_stems() -> set[str]:
    known = set()
    for d in KNOWN_DIRS:
        base = WIKI_ROOT / d
        if not base.exists():
            continue
        for f in base.rglob("*.md"):
            if any(p in SKIP_DIRS for p in f.parts):
                continue
            known.add(f.stem)
    # .html 페이지(interactives, wiki 내 임베드 도구 등)도 wikilink 대상 → known에 포함
    for base in (WIKI_ROOT / "interactives", WIKI_DIR):
        if base.exists():
            for f in base.rglob("*.html"):
                known.add(f.stem)
    return known


def collect_wiki_pages() -> dict[str, Path]:
    pages = {}
    for f in WIKI_DIR.rglob("*.md"):
        if any(p in SKIP_DIRS for p in f.parts):
            continue
        if f.name in SKIP_PAGE_FILES:
            continue
        pages[f.stem] = f
    return pages


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stdout", action="store_true")
    args = ap.parse_args()

    if not WIKI_DIR.exists():
        print(f"  No wiki dir: {WIKI_DIR}")
        return 0

    known = collect_known_stems()
    pages = collect_wiki_pages()
    wiki_paths, wiki_dirs = collect_wiki_paths()

    # 화이트리스트: 카테고리 폴더명(랜딩페이지 없는 폴더 참조) + 메모리 시스템 참조
    # → broken이 아니라 별도 info 버킷으로 분리(가시성 유지, ⚠ 카운트 제외)
    category_folders = {p.name for p in WIKI_DIR.rglob("*") if p.is_dir()}

    def is_memory_ref(t: str) -> bool:
        return t.startswith("feedback_") or t.startswith("project_") or t == "MEMORY"

    # (1) 본문 깨진 wikilink  +  (3) 경로형 링크의 경로 정확도
    broken = []      # (source, bad_target) — 진짜 깨짐
    cat_ref = []     # (source, folder) — 카테고리 폴더 참조
    mem_ref = []     # (source, memory_stem) — 메모리 시스템 참조
    path_bad = []    # (source, written, actual) — 경로 오기, 대상이 유일하게 결정됨
    path_ambig = []  # (source, written, [candidates]) — stem이 여러 파일에 존재
    path_checked = 0
    path_folder = 0  # 폴더 자체를 가리키는 링크 (Quartz FolderPage로 정상 해석)
    total_links = 0
    for stem, path in pages.items():
        for raw in WIKILINK_RE.findall(path.read_text(encoding="utf-8")):
            tgt = link_to_stem(raw)
            if not tgt:
                continue
            total_links += 1

            # (3) 경로 검사 — stem이 실존하는 경우에만(깨진 링크는 (1)에서 계상)
            wpath = link_to_path(raw)
            if "/" in wpath and wpath.split("/")[0] not in CROSS_TIER_PREFIXES:
                cands = wiki_paths.get(tgt)
                if cands:
                    path_checked += 1
                    if wpath in wiki_dirs:
                        path_folder += 1          # 폴더 링크 — FolderPage가 받는다
                    elif wpath not in cands:
                        if len(cands) == 1:
                            path_bad.append((stem, wpath, cands[0]))
                        else:
                            path_ambig.append((stem, wpath, sorted(cands)))

            if tgt == stem or tgt in known:
                continue
            if tgt in category_folders:
                cat_ref.append((stem, tgt))
            elif is_memory_ref(tgt):
                mem_ref.append((stem, tgt))
            else:
                broken.append((stem, tgt))

    # (2) index 양방향 커버리지
    index_stems = set()
    if INDEX.exists():
        for raw in WIKILINK_RE.findall(INDEX.read_text(encoding="utf-8")):
            index_stems.add(link_to_stem(raw))
    # 등재 의무 면제: INDEX_EXEMPT_DIRS 하위 페이지. pages 자체에서는 빼지 않는다 —
    # 빼면 그 페이지의 본문 위키링크가 broken 검사에서까지 누락되기 때문.
    missing_from_index = sorted(
        s for s, p in pages.items()
        if s not in index_stems
        and not any(part in INDEX_EXEMPT_DIRS for part in p.parts)
    )
    # index는 wiki 페이지뿐 아니라 interactives(.html) 등도 참조 → known 기준으로 판정
    index_points_nowhere = sorted(s for s in index_stems if s not in known)

    LOGS_DIR.mkdir(exist_ok=True)
    log_path = LOGS_DIR / f"{date.today().isoformat()}_link-integrity.log"
    L = []
    L.append(f"# Link & Index Integrity — {date.today().isoformat()}")
    L.append(f"wiki pages              : {len(pages)}")
    L.append(f"body wikilinks scanned  : {total_links}")
    L.append(f"  BROKEN body wikilinks : {len(broken)}")
    L.append(f"  (info) category-folder refs : {len(cat_ref)}")
    L.append(f"  (info) memory-system refs   : {len(mem_ref)}")
    L.append(f"path-form wikilinks checked : {path_checked}")
    L.append(f"  WRONG PATH (auto-fixable) : {len(path_bad)}")
    L.append(f"  WRONG PATH (ambiguous)    : {len(path_ambig)}")
    L.append(f"  (info) folder links       : {path_folder}")
    L.append(f"index entries           : {len(index_stems)}")
    L.append(f"  pages MISSING from index    : {len(missing_from_index)}")
    L.append(f"  index entries → nonexistent : {len(index_points_nowhere)}")
    L.append("")
    if broken:
        L.append("=== ⚠ BROKEN body wikilinks (top 100) ===")
        for s, tgt in broken[:100]:
            L.append(f"  {s}  →  [[{tgt}]]  (NOT FOUND)")
        if len(broken) > 100:
            L.append(f"  ... +{len(broken) - 100} more")
        L.append("")
    if path_bad:
        L.append("=== ⚠ WRONG PATH — 적힌 경로 ≠ 실제 위치 (배포 사이트 404, top 100) ===")
        L.append("    stem은 맞아서 BROKEN 검사는 통과한다. 대상이 유일하게 결정되므로 그대로 치환하면 된다.")
        for s, w, a in path_bad[:100]:
            L.append(f"  {s}")
            L.append(f"      적힌 것: [[{w}]]")
            L.append(f"      실제:    [[{a}]]")
        if len(path_bad) > 100:
            L.append(f"  ... +{len(path_bad) - 100} more")
        L.append("")
    if path_ambig:
        L.append("=== ⚠ WRONG PATH (모호) — 같은 stem이 여러 파일에 존재, 사람이 판단 ===")
        for s, w, c in path_ambig:
            L.append(f"  {s}  →  [[{w}]]  후보: {', '.join(c)}")
        L.append("")
    if missing_from_index:
        L.append("=== ⚠ wiki pages MISSING from index.md (top 100) ===")
        for s in missing_from_index[:100]:
            L.append(f"  {s}")
        if len(missing_from_index) > 100:
            L.append(f"  ... +{len(missing_from_index) - 100} more")
        L.append("")
    if index_points_nowhere:
        L.append("=== ⚠ index.md entries pointing to nonexistent pages ===")
        for s in index_points_nowhere:
            L.append(f"  [[{s}]]")
        L.append("")
    if cat_ref:
        L.append("=== (info) category-folder refs (no landing page — not counted as broken) ===")
        for s, t in cat_ref:
            L.append(f"  {s}  →  [[{t}]]")
        L.append("")
    if mem_ref:
        L.append("=== (info) memory-system refs (cross-system — not counted as broken) ===")
        for s, t in mem_ref:
            L.append(f"  {s}  →  [[{t}]]")
        L.append("")

    body = "\n".join(L) + "\n"
    log_path.write_text(body, encoding="utf-8")

    issues = (len(broken) + len(missing_from_index) + len(index_points_nowhere)
              + len(path_bad) + len(path_ambig))
    flag = "⚠" if issues else "✓"
    print(f"🔍  Link/Index: {len(broken)} broken links, {len(path_bad) + len(path_ambig)} wrong paths, "
          f"{len(missing_from_index)} unindexed, {len(index_points_nowhere)} dead index entries {flag}")
    print(f"      log → logs/{log_path.name}")
    if args.stdout:
        print()
        print(body)
    return 0  # signal


if __name__ == "__main__":
    sys.exit(main())
