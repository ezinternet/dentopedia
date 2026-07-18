#!/usr/bin/env python3
"""
LLM Wiki — Typed Relations Audit (signal, non-blocking)

`[[wikilinks]]`는 두 페이지가 "관계 있다"만 표현하고 "어떻게"는 못 담는다.
wiki 페이지 frontmatter의 `relations:` 블록(typed edge)을 검증·집계한다.
supersession은 별도(superseded_by)라 여기서 제외.

스키마 (citing=신규 페이지에서 바깥으로):
    relations:
      - type: extends
        target: <stem>
      - type: reinforces
        target: <stem>

vocab: extends | reinforces | contradicts | refines | applies-to

검사 — 구조적 유효성 (issues 카운트에 합산):
  (A) DANGLING   — target stem이 wiki에 없음.
  (B) BAD-TYPE   — type이 vocab 밖.
  (C) SELF       — target이 자기 자신.

검사 — 의미 신호 (issues와 **별도** 집계):
  (D) CIRCULAR reinforces — 파생문서가 자기 원료를 "독립적으로 확인"한다는 주장.
      `reinforces`의 정의는 *독립적으로* 확인·보강이다. 자기가 그 논문으로 만들어진
      문서는 그 논문을 독립 확인할 수 없다 — 순환이다.
        C1: overview → 자기 본문이 인용한 구성 논문
        C2: 논문 → 그 논문을 본문에 인용한 overview (방향까지 뒤집힌 경우)
      2026-07-17 실측 152건(C1 131 / C2 21) = 전체 reinforces의 13.3%.
      30건 무작위 표본을 두 페이지 다 읽고 판정한 독립 추정치(~115건)와 수렴.

      **POSTDATED 제외 (2026-07-18)**: 논문이 overview보다 **나중에** 리포에
      들어왔으면 overview가 그것으로 만들어졌을 수 없어 순환이 아니다. 14건
      표본 판정에서 정당(KEEP) 2건이 **둘 다** 이 서명이었다 — rosas-diaz(ladder
      source_wiki 3편에 없음, 나중에 Related Papers로 추가), lu-2025(overview
      2026-05-31 vs 논문 2026-06-23). 본문 wikilink만으로는 구성 재료와 나중에
      덧붙인 관련 논문을 구분할 수 없어 생기던 오탐이다. 걸러진 건은 버리지 않고
      POSTDATED 버킷으로 별도 보고한다 (무성 절삭 금지).
      **남는 한계**: overview보다 먼저 인제스트됐지만 재료로 쓰이진 않고 나중에
      Related Papers로만 링크된 논문은 여전히 순환으로 잡힌다 — 시간순으로는
      구분 불가.
      **signal일 뿐 — 자동 수정하지 않는다.** extends/refines/applies-to로 바꿀지,
      엣지를 뺄지는 사람/LLM이 두 페이지를 읽고 판단한다 (overview가 교차 독해로
      구성 논문의 결론을 한정하는 것은 진짜 refines일 수 있다 — 순환인 건
      `reinforces`뿐이다).
      멤버십 정보는 안 사라진다: 실측상 그런 엣지의 대상 227/227(100%)이 본문
      wikilink로도 존재하며, synthesis-backlog가 읽는 것이 바로 그 wikilink다.

그리고 그래프 통계 + typed-edge JSON export(logs/{date}_relations-graph.json).

Output: logs/{date}_relations.log  +  logs/{date}_relations-graph.json
Exit: 항상 0 (signal). daily-audit.py 통합 시 must_pass=False.

Usage:
    python3 scripts/relations-audit.py [--stdout]
"""

import re
import sys
import json
import argparse
from datetime import date
from pathlib import Path
from collections import defaultdict

try:
    import yaml
except ImportError:
    yaml = None

WIKI_ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = WIKI_ROOT / "wiki"
LOGS_DIR = WIKI_ROOT / "logs"

SKIP_DIRS = {"_lint"}
SKIP_FILES = {"index.md"}

VOCAB = {"extends", "reinforces", "contradicts", "refines", "applies-to"}
FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
WIKILINK_RE = re.compile(r"\[\[([^\]|]+)")
SYNTHESIS_RE = re.compile(r"^type:\s*synthesis\s*$", re.MULTILINE)


def get_fm_block(content: str) -> str | None:
    m = FM_RE.match(content)
    return m.group(1) if m else None


def norm_stem(s: str) -> str:
    s = str(s).strip().strip("[]").strip()
    if "/" in s:
        s = s.split("/")[-1]
    return s.replace(".md", "").strip()


def collect_pages() -> dict[str, Path]:
    pages = {}
    for f in WIKI_DIR.rglob("*.md"):
        if any(p in SKIP_DIRS for p in f.parts):
            continue
        if f.name in SKIP_FILES:
            continue
        pages[f.stem] = f
    return pages


def is_overview(path: Path, fm_text: str) -> bool:
    """파생문서(종합) 판정: wiki/overviews/ 아래이거나 type: synthesis."""
    if "overviews" in path.parts:
        return True
    return bool(SYNTHESIS_RE.search(fm_text or ""))


def body_wikilinks(content: str) -> set[str]:
    """frontmatter를 제외한 본문의 [[wikilink]] stem 집합.

    본문이 그 논문을 인용한다 = 그 논문이 이 페이지의 재료다. 이것이
    '파생'의 기계적 판정 기준이다 (source_papers: 필드는 overview 239장 중
    80장에만 있어 기준으로 못 쓴다 — 2026-07-17 실측).
    """
    m = FM_RE.match(content)
    body = content[m.end():] if m else content
    return {norm_stem(w) for w in WIKILINK_RE.findall(body)}


def file_add_dates() -> dict[str, str]:
    """{stem: YYYY-MM-DD} — 그 페이지 파일이 리포에 **추가된** 날.

    순환 판정의 필수 보조축이다. C1/C2는 "본문이 그 논문을 wikilink한다"로
    파생을 추정하는데, 본문 wikilink는 **구성 재료**와 **나중에 덧붙인 관련
    논문**을 구분하지 못한다. 논문이 overview보다 나중에 리포에 들어왔다면
    overview가 그것으로 만들어졌을 수 없으므로 순환이 아니다 — 오히려 나중에
    도착한 독립 근거의 확인이라 `reinforces`가 정당할 수 있다.

    frontmatter `date:`로는 이 판정을 못 한다: 논문 페이지의 date는 *출판일*,
    overview의 date는 *작성일*이라 축이 다르다 (2016년 논문을 2026년에
    인제스트하면 date는 2016이지만 리포 추가는 overview보다 나중일 수 있다).

    git 호출은 **전체 1회**다. per-file 호출은 f10ecfc가 캐시로 제거한 그
    느림의 원인이므로 되살리지 않는다 (전 wiki 1회 traversal ≈ 4s 실측).
    git이 없거나 리포가 아니면 빈 dict → 필터는 자동으로 비활성(기존 동작).
    """
    import subprocess
    try:
        out = subprocess.run(
            ["git", "-C", str(WIKI_ROOT), "log", "--diff-filter=A",
             "--format=C|%ad", "--date=short", "--name-only", "--", "wiki/"],
            capture_output=True, text=True, timeout=120,
        )
        if out.returncode != 0:
            return {}
    except (OSError, subprocess.SubprocessError):
        return {}

    added: dict[str, str] = {}
    cur = None
    for ln in out.stdout.splitlines():
        if ln.startswith("C|"):
            cur = ln[2:].strip()
        elif ln.endswith(".md") and cur:
            # git log는 최신순 → 같은 경로를 나중에 덮어쓸수록 더 이른 추가일
            added[Path(ln).stem] = cur
    return added


def parse_relations(fm_text: str) -> list[dict]:
    """relations: 블록을 yaml로 파싱. 실패 시 빈 리스트."""
    if yaml is None:
        return []
    try:
        data = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError:
        return []
    rels = data.get("relations")
    if not isinstance(rels, list):
        return []
    out = []
    for item in rels:
        if isinstance(item, dict) and "type" in item and "target" in item:
            out.append({"type": str(item["type"]).strip().lower(),
                        "target": norm_stem(item["target"])})
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stdout", action="store_true")
    args = ap.parse_args()

    if not WIKI_DIR.exists():
        print(f"  No wiki dir: {WIKI_DIR}")
        return 0
    if yaml is None:
        print("⚠  PyYAML 미설치 — relations-audit skip")
        return 0

    pages = collect_pages()

    # 1-pass 캐시: C2(논문 → 자기를 인용한 overview)는 **대상** 페이지의 본문을
    # 봐야 하므로, 엣지 루프 전에 전 페이지의 fm/overview여부/본문 wikilink를 모은다.
    fm_of: dict[str, str] = {}
    is_ov: dict[str, bool] = {}
    wl_of: dict[str, set[str]] = {}
    for stem, path in pages.items():
        content = path.read_text(encoding="utf-8")
        fm_text = get_fm_block(content) or ""
        fm_of[stem] = fm_text
        is_ov[stem] = is_overview(path, fm_text)
        wl_of[stem] = body_wikilinks(content)

    edges = []            # {source, type, target}
    dangling = []         # (source, type, target)
    bad_type = []         # (source, type, target)
    self_ref = []         # (source, target)
    circular = []         # (kind, source, target)  — 의미 신호, issues와 별도
    postdated = []        # (kind, source, target, ov_date, paper_date) — 순환 아님(논문이 나중)
    added_on = file_add_dates()
    type_count = defaultdict(int)
    nodes_with_rel = set()

    for stem, path in pages.items():
        fm_text = fm_of[stem]
        if not fm_text or "relations:" not in fm_text:
            continue
        for r in parse_relations(fm_text):
            t, tgt = r["type"], r["target"]
            nodes_with_rel.add(stem)
            if t not in VOCAB:
                bad_type.append((stem, t, tgt))
            if tgt == stem:
                self_ref.append((stem, tgt))
            if tgt not in pages:
                dangling.append((stem, t, tgt))
            elif t == "reinforces":
                # (D) 순환: 파생문서는 자기 원료를 독립 확인할 수 없다.
                #     단 논문이 overview보다 **나중에** 리포에 들어왔다면 overview가
                #     그것으로 만들어졌을 수 없다 → 순환 아님(postdated 버킷).
                kind = ov = paper = None
                if is_ov[stem] and not is_ov[tgt] and tgt in wl_of[stem]:
                    kind, ov, paper = "C1", stem, tgt
                elif not is_ov[stem] and is_ov[tgt] and stem in wl_of[tgt]:
                    kind, ov, paper = "C2", tgt, stem
                if kind:
                    d_ov, d_paper = added_on.get(ov), added_on.get(paper)
                    if d_ov and d_paper and d_paper > d_ov:
                        postdated.append((kind, stem, tgt, d_ov, d_paper))
                    else:
                        circular.append((kind, stem, tgt))
            edges.append({"source": stem, "type": t, "target": tgt})
            type_count[t] += 1

    # edge JSON export (typed graph — Quartz/custom 렌더용)
    LOGS_DIR.mkdir(exist_ok=True)
    graph_path = LOGS_DIR / f"{date.today().isoformat()}_relations-graph.json"
    graph_path.write_text(json.dumps(edges, ensure_ascii=False, indent=2), encoding="utf-8")

    log_path = LOGS_DIR / f"{date.today().isoformat()}_relations.log"
    L = []
    L.append(f"# Typed Relations Audit — {date.today().isoformat()}")
    L.append(f"wiki pages scanned     : {len(pages)}")
    L.append(f"pages with relations:  : {len(nodes_with_rel)}")
    L.append(f"typed edges            : {len(edges)}")
    L.append(f"  DANGLING target      : {len(dangling)}")
    L.append(f"  BAD type (off-vocab) : {len(bad_type)}")
    L.append(f"  SELF reference       : {len(self_ref)}")
    L.append(f"CIRCULAR reinforces    : {len(circular)}   (신호 — 위 issues와 별도)")
    L.append(f"  postdated (순환 아님) : {len(postdated)}   (논문이 overview보다 나중 — 아래 별도 목록)")
    L.append("")
    L.append("=== type distribution ===")
    for t in sorted(type_count, key=lambda k: -type_count[k]):
        flag = "" if t in VOCAB else "  ⚠ off-vocab"
        L.append(f"  {type_count[t]:>4}  {t}{flag}")
    L.append("")
    if dangling:
        L.append("=== ⚠ DANGLING relation targets ===")
        for s, t, tgt in dangling:
            L.append(f"  {s}  --{t}-->  {tgt}  (NOT FOUND)")
        L.append("")
    if bad_type:
        L.append(f"=== ⚠ BAD type (allowed: {', '.join(sorted(VOCAB))}) ===")
        for s, t, tgt in bad_type:
            L.append(f"  {s}  --{t}-->  {tgt}")
        L.append("")
    if self_ref:
        L.append("=== ⚠ SELF reference ===")
        for s, tgt in self_ref:
            L.append(f"  {s}")
        L.append("")
    if circular:
        L.append("=== CIRCULAR reinforces — 파생문서가 자기 원료를 '독립 확인'한다는 주장 ===")
        L.append("")
        L.append("`reinforces` = *독립적으로* 확인·보강. 자기가 그 논문으로 만들어진 문서는")
        L.append("그 논문을 독립 확인할 수 없다. **이 목록은 신호일 뿐 — 두 페이지를 읽고 판단한다.**")
        L.append("  · overview가 교차 독해로 구성 논문의 결론을 한정한다면 그건 진짜 `refines`다.")
        L.append("  · 구성 논문을 단지 재서술한다면 엣지를 빼도 된다 — 멤버십은 본문 wikilink가")
        L.append("    이미 담고 있고(실측 227/227), synthesis-backlog가 읽는 것도 그 wikilink다.")
        L.append("  · C1 = overview → 자기가 인용한 구성 논문")
        L.append("  · C2 = 논문 → 그 논문을 재료로 쓴 overview (방향까지 뒤집힘)")
        L.append("")
        c1 = [(s, t) for k, s, t in circular if k == "C1"]
        c2 = [(s, t) for k, s, t in circular if k == "C2"]
        L.append(f"--- C1 (overview → 구성 논문): {len(c1)}건 ---")
        for s, t in sorted(c1):
            L.append(f"  {s}  --reinforces-->  {t}")
        L.append("")
        L.append(f"--- C2 (논문 → 자기를 재료로 쓴 overview): {len(c2)}건 ---")
        for s, t in sorted(c2):
            L.append(f"  {s}  --reinforces-->  {t}")
        L.append("")

    if postdated:
        L.append("=== POSTDATED — 순환 아님 (논문이 overview보다 나중에 리포 진입) ===")
        L.append("")
        L.append("overview가 이 논문으로 만들어졌을 수 없으므로 순환이 아니다. 나중에")
        L.append("도착한 독립 근거가 기존 종합을 확인하는 형태라 `reinforces`가 정당할 수 있다.")
        L.append("**여기 있다고 라벨이 옳다는 뜻은 아니다** — 순환 혐의만 벗은 것이고,")
        L.append("실제로 확인이 아니라 범위 확장이면 `extends`가 맞다. 위 목록보다 우선순위 낮음.")
        L.append("")
        L.append("표기: (overview 추가일 → 논문 추가일)")
        L.append("")
        for k, s, t, d_ov, d_p in sorted(postdated, key=lambda x: (x[0], x[1])):
            L.append(f"  [{k}] {s}  --reinforces-->  {t}   ({d_ov} → {d_p})")
        L.append("")

    body = "\n".join(L) + "\n"
    log_path.write_text(body, encoding="utf-8")

    issues = len(dangling) + len(bad_type) + len(self_ref)
    flag = "⚠" if issues else "✓"
    print(f"🔗  Relations: {len(edges)} typed edges across {len(nodes_with_rel)} pages, {issues} issues {flag}")
    print(f"      circular reinforces (signal): {len(circular)}"
          + (f"  · postdated(순환 아님): {len(postdated)}" if postdated else ""))
    print(f"      log → logs/{log_path.name} · graph → logs/{graph_path.name}")
    if args.stdout:
        print()
        print(body)
    return 0  # signal


if __name__ == "__main__":
    sys.exit(main())
