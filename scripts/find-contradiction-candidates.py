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

각 카드는 한국어로 (a) 충돌 유형 뜻, (b) 근거 문장, (c) 양쪽 페이지의 ## 한줄요약을
함께 보여준다 — 페이지를 열지 않고도 두 논문이 각각 뭐라고 주장하는지 한글로 파악.

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

# 충돌 표현 → 한글 뜻 (카드 가독성용). 부분 문자열 매칭, 첫 일치 사용.
KW_KO = [
    ("contradict", "반박·충돌"), ("counterpoint", "반대 논점"), ("counter to", "반대"),
    ("contrary to", "상반된 결과"), ("in contrast to", "대조"), ("at odds", "상충"),
    ("conflicting", "상충 결과"), ("refut", "반증"), ("overturn", "결론 뒤집음"),
    ("반박", "반박"), ("상충", "상충"), ("상반", "상반"), ("반론", "반론"),
    ("대비되는", "대비"), ("배치되", "배치"), ("뒤집", "뒤집음"),
    ("unlike", "다름"), ("whereas", "반면(대조)"), ("challenges the", "도전"),
    ("disagree", "불일치"), ("inconsistent with", "불일치"),
    ("however", "그러나(단서)"), ("대조적", "대조"),
]

def ko_gloss(kw):
    k = kw.lower()
    for key, val in KW_KO:
        if key in k:
            return val
    return kw

WIKILINK = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]")
FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
ONELINER_RE = re.compile(r"^##\s*한줄요약\s*\n+(.+?)(?=\n##\s|\Z)", re.DOTALL | re.MULTILINE)

def oneliner_of(text):
    """페이지 본문에서 ## 한줄요약 첫 단락을 뽑아 한 줄로 정리 (없으면 '')."""
    m = ONELINER_RE.search(text)
    if not m:
        return ""
    para = re.sub(r"\s+", " ", m.group(1)).strip()
    # 콜아웃/배너 기호 제거
    para = para.lstrip("> ").strip()
    return para[:280]

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

# stem 인덱스 + stem→한줄요약(한국어) 인덱스
stems = set()
oneliner = {}
for md in WIKI.rglob("*.md"):
    if md.name.startswith("_"):
        continue
    stems.add(md.stem)
    try:
        oneliner[md.stem] = oneliner_of(md.read_text(encoding="utf-8", errors="replace"))
    except Exception:
        oneliner[md.stem] = ""

def ko_line(stem, label):
    """stem의 한줄요약을 카드 서브라인으로. 없으면 안내."""
    ol = oneliner.get(stem, "")
    if ol:
        return f"  - ▸ {label}(`{stem}`) 한줄: {ol}"
    return f"  - ▸ {label}(`{stem}`) 한줄: _(한줄요약 없음 — 페이지 확인 필요)_"

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
        targets = [m.group(1).rstrip("/").split("/")[-1] for m in WIKILINK.finditer(line)]
        targets = [t for t in targets if t in stems and t != md.stem and t not in edges]
        snip = re.sub(r"\s+", " ", line).strip()[:400]
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
lines = [
    f"# 논쟁 레이더 백필 후보 — {date.today().isoformat()}",
    "",
    "명시적 충돌 표현이 있으나 `relations: contradicts/refines` 엣지가 없는 후보. "
    "**이 목록은 신호일 뿐 — 두 페이지를 읽고 판단해 엣지를 단다.**",
    "",
    "**카드 읽는 법**: 각 카드는 `출발페이지 —[충돌유형·한글뜻]→ 대상페이지` 형태다. "
    "아래에 (1) **근거 문장**(위키 본문에서 충돌 표현이 나온 실제 문장), "
    "(2) **양쪽 페이지의 `## 한줄요약`**(한국어)을 붙여, 페이지를 열지 않고도 "
    "두 논문이 각각 무엇을 주장하는지·정말 충돌하는지 한글로 판단할 수 있게 했다. "
    "충돌 유형 한글뜻은 표현 매칭 기반 근사치이며, **최종 판단은 사람/LLM 몫**이다. "
    "(reinforces가 맞는 경우도 있으니 키워드를 그대로 엣지로 옮기지 말 것.)",
    "",
    f"- Tier 1 (대상 지목됨, actionable): **{len(t1)}**",
    f"- Tier 2 (대상 불명/soft, review): **{len(tier2)}**",
    "",
    "## Tier 1 — 판단 후 엣지 달 후보 (page → 지목된 target)",
    "",
]
by_cat = defaultdict(list)
for stem, cat, tgt, kw, snip in t1:
    by_cat[cat].append((stem, tgt, kw, snip))
for cat in sorted(by_cat):
    lines.append(f"### {cat or '(no category)'}")
    lines.append("")
    for stem, tgt, kw, snip in by_cat[cat]:
        lines.append(f"- `{stem}`  —[{kw} · {ko_gloss(kw)}]→  **`{tgt}`**")
        lines.append(f"  - **근거 문장**: {snip}")
        lines.append(ko_line(stem, "출발"))
        lines.append(ko_line(tgt, "대상"))
        lines.append("")
    lines.append("")

lines.append("## Tier 2 — 대상 식별 필요 / soft signal (review only)")
lines.append("")
for stem, cat, tier, kw, snip in tier2:
    lines.append(f"- `{stem}` [{cat}] ({tier}, '{kw}' · {ko_gloss(kw)})")
    lines.append(f"  - **근거 문장**: {snip}")
    lines.append(ko_line(stem, "출발"))
    if tier.startswith("SOFT→"):
        tgt = tier.split("→", 1)[1]
        lines.append(ko_line(tgt, "대상"))
    lines.append("")

OUT.write_text("\n".join(lines), encoding="utf-8")
print(f"✓ {OUT.relative_to(ROOT)}")
print(f"  Tier 1 (actionable, page→target): {len(t1)}")
print(f"  Tier 2 (review): {len(tier2)}")
print(f"  한줄요약 인덱스: {sum(1 for v in oneliner.values() if v)}/{len(oneliner)} pages")
