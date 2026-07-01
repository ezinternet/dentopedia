#!/usr/bin/env python3
"""
논쟁 레이더 백필 후보 finder (SIGNAL — 엣지를 자동으로 쓰지 않는다).

위키 본문(및 매칭되는 sources/의 Why Ingested)에서 "명시적 충돌 표현"을 스캔해,
아직 relations: contradicts/refines 엣지가 없는 논쟁 후보를 등급별로 뽑는다.
사람/LLM이 이 목록을 읽고 판단해 실제 엣지를 단다 (Rule #1·품질 기준 준수 —
기계가 충돌을 확정하지 않는다).

Tier 1 (actionable): 충돌 표현 + 같은 문맥에 [[wikilink]]로 대상이 지목됨, 엣지 없음.
                      → 두 페이지를 읽고 판단 후 relations 엣지를 달 수 있는 후보.
Tier 2 (review):      충돌 표현은 있으나 대상 링크가 불명확. → 대상 식별 필요.

실행: python3 scripts/find-contradiction-candidates.py
출력: logs/{YYYY-MM-DD}_contradiction-candidates.md  (+ 콘솔 요약)
"""

import re
from pathlib import Path
from datetime import date
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
SOURCES = ROOT / "sources"
OUT = ROOT / "logs" / f"{date.today().isoformat()}_contradiction-candidates.md"

# 명시적 충돌 신호. HIGH = 오탐 적음(자동 write 후보), SOFT = 노이즈 많음(review only).
HIGH = re.compile(
    r"contradict|counterpoint|counter to|contrary to|in contrast to|at odds|"
    r"conflicting (?:evidence|result|finding)|refut|overturn|"
    r"반박|상충|상반|반론|대비되는|배치되|뒤집", re.IGNORECASE)
SOFT = re.compile(
    r"\bunlike\b|\bwhereas\b|challenges the|disagree|inconsistent with|"
    r"however,? (?:this|the|our)|대조적", re.IGNORECASE)

WIKILINK = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]")
FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

def parse(path):
    txt = path.read_text(encoding="utf-8", errors="replace")
    m = FM_RE.match(txt)
    fm = m.group(1) if m else ""
    body = txt[m.end():] if m else txt
    cat = ""
    c = re.search(r"^category:\s*(.+)$", fm, re.MULTILINE)
    if c:
        cat = c.group(1).strip().strip("[]").split(",")[0].strip()
    # 기존 contradicts/refines 엣지 target(stem) 집합
    edges = set()
    rel = re.search(r"^relations:\s*\n((?:[ \t]+.*\n?)+)", fm, re.MULTILINE)
    if rel:
        for item in re.split(r"\n(?=\s*-\s)", rel.group(1)):
            t = re.search(r"type:\s*(\S+)", item)
            g = re.search(r"target:\s*(\S+)", item)
            if t and g and t.group(1) in ("contradicts", "refines"):
                edges.add(g.group(1).strip().rstrip("/").split("/")[-1])
    return fm, body, cat, edges

# stem 인덱스
stems = {md.stem for md in WIKI.rglob("*.md") if not md.name.startswith("_")}

tier1 = []   # (page_stem, cat, target_stem, kw, snippet)
tier2 = []   # (page_stem, cat, tier, kw, snippet)

for md in WIKI.rglob("*.md"):
    if md.name.startswith("_") or md.stem in ("index",):
        continue
    fm, body, cat, edges = parse(md)
    # 본문 + 매칭 sources의 Why Ingested 를 함께 스캔
    scan = body
    src = SOURCES / md.name
    if src.exists():
        s = src.read_text(encoding="utf-8", errors="replace")
        w = re.search(r"^##\s*Why Ingested\s*\n(.+?)(?=\n##\s|\Z)", s, re.DOTALL | re.MULTILINE)
        if w:
            scan += "\n" + w.group(1)

    for line in scan.split("\n"):
        hi = HIGH.search(line)
        so = None if hi else SOFT.search(line)
        if not hi and not so:
            continue
        kw = (hi or so).group(0)
        links = [WIKILINK.finditer(line)]
        targets = [m.group(1).rstrip("/").split("/")[-1] for m in WIKILINK.finditer(line)]
        targets = [t for t in targets if t in stems and t != md.stem and t not in edges]
        snip = re.sub(r"\s+", " ", line).strip()[:200]
        if hi and targets:
            for t in targets:
                tier1.append((md.stem, cat, t, kw, snip))
        elif hi:
            tier2.append((md.stem, cat, "HIGH-no-target", kw, snip))
        # SOFT는 target 있을 때만 review 목록에
        elif so and targets:
            for t in targets:
                tier2.append((md.stem, cat, f"SOFT→{t}", kw, snip))

# dedup tier1 by (page,target)
seen = set(); t1 = []
for row in tier1:
    k = (row[0], row[2])
    if k not in seen:
        seen.add(k); t1.append(row)
t1.sort(key=lambda r: r[1])

# ── 리포트 ───────────────────────────────────────────────────────────
lines = [f"# 논쟁 레이더 백필 후보 — {date.today().isoformat()}",
         "",
         f"명시적 충돌 표현이 있으나 `relations: contradicts/refines` 엣지가 없는 후보. "
         f"**이 목록은 신호일 뿐 — 두 페이지를 읽고 판단해 엣지를 단다.**",
         "",
         f"- Tier 1 (대상 지목됨, actionable): **{len(t1)}**",
         f"- Tier 2 (대상 불명/soft, review): **{len(tier2)}**",
         "",
         "## Tier 1 — 판단 후 엣지 달 후보 (page → 지목된 target)",
         ""]
by_cat = defaultdict(list)
for stem, cat, tgt, kw, snip in t1:
    by_cat[cat].append((stem, tgt, kw, snip))
for cat in sorted(by_cat):
    lines.append(f"### {cat or '(no category)'}")
    for stem, tgt, kw, snip in by_cat[cat]:
        lines.append(f"- `{stem}`  —[{kw}]→  **`{tgt}`**")
        lines.append(f"  > {snip}")
    lines.append("")

lines.append("## Tier 2 — 대상 식별 필요 / soft signal (review only)")
lines.append("")
for stem, cat, tier, kw, snip in tier2[:120]:
    lines.append(f"- `{stem}` [{cat}] ({tier}, '{kw}')")
    lines.append(f"  > {snip}")

OUT.write_text("\n".join(lines), encoding="utf-8")
print(f"✓ {OUT.relative_to(ROOT)}")
print(f"  Tier 1 (actionable, page→target): {len(t1)}")
print(f"  Tier 2 (review): {len(tier2)}")
