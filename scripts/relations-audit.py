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

검사:
  (A) DANGLING   — target stem이 wiki에 없음.
  (B) BAD-TYPE   — type이 vocab 밖.
  (C) SELF       — target이 자기 자신.
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
    edges = []            # {source, type, target}
    dangling = []         # (source, type, target)
    bad_type = []         # (source, type, target)
    self_ref = []         # (source, target)
    type_count = defaultdict(int)
    nodes_with_rel = set()

    for stem, path in pages.items():
        fm_text = get_fm_block(path.read_text(encoding="utf-8"))
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

    body = "\n".join(L) + "\n"
    log_path.write_text(body, encoding="utf-8")

    issues = len(dangling) + len(bad_type) + len(self_ref)
    flag = "⚠" if issues else "✓"
    print(f"🔗  Relations: {len(edges)} typed edges across {len(nodes_with_rel)} pages, {issues} issues {flag}")
    print(f"      log → logs/{log_path.name} · graph → logs/{graph_path.name}")
    if args.stdout:
        print()
        print(body)
    return 0  # signal


if __name__ == "__main__":
    sys.exit(main())
