#!/usr/bin/env python3
"""
interactives/contradiction-radar.html 자동 생성기 (논쟁 레이더).

위키 전체 frontmatter의 `relations:` 블록에서 type: contradicts(정면충돌)와
type: refines(조건부 반박) edge만 뽑아, "위키 안에서 근거가 서로 싸우는 지점"을
임상 도메인별 카드로 묶은 self-contained HTML 탐색기를 생성한다.

- 각 edge = source(도전자) vs target(피도전자). 양측의 One-line Summary/한줄요약을
  살로 붙여 나란히 보여준다.
- 무순서 쌍 {a,b}로 dedup. 양쪽이 서로 contradicts면 mutual(상호반박)로 표기.
  같은 쌍에 contradicts와 refines가 섞이면 강한 쪽(contradicts) 채택.
- stem→파일 인덱스로 target 파일을 찾고, 못 찾으면 로그만 남기고 스킵.

실행: python3 scripts/build-contradiction-radar.py
출력: interactives/contradiction-radar.html  (덮어쓰기, AUTO-GENERATED)

설계: agenda/2026-07-01_contradiction-radar.md
"""

import re
import html
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
OUT = ROOT / "interactives" / "contradiction-radar.html"
SITE_BASE = "/dentopedia"   # quartz.config.ts baseUrl 과 일치

# ── 임상 도메인 그룹: (라벨, [top-level 카테고리 폴더...]). 첫 매치가 그 도메인.
# 카테고리 경로 첫 세그먼트로 분류(예: endodontics/irrigation → endodontics).
DOMAINS = [
    ("임플란트 · 골재생 · 상악동", [
        "implants", "immediate-implant", "bone-regeneration", "sinus-lift",
        "bone-biology", "pdrn"]),
    ("보철 · 재료 · 교합", [
        "prosthetic-materials", "dental-materials", "complete-denture",
        "occlusion", "post-and-core", "inlay", "veneers", "digital-workflow"]),
    ("근관 · 외상 · 균열", [
        "endodontics", "dental-trauma", "cracked-tooth"]),
    ("치주 · 치간 · 미생물", [
        "periodontics", "interdental-cleaning", "oral-microbiology"]),
    ("우식 · 재료(수복) · 접착", [
        "caries", "resin", "resin-bonding", "glass-ionomer",
        "dental-erosion", "nccl", "dentin-hypersensitivity", "tooth-whitening"]),
    ("외과 · 마취 · 약물", [
        "oral-surgery", "local-anesthesia", "suture-wound-closure",
        "drug", "infection-control", "dental-handpiece"]),
    ("구강내과 · 통증 · 방사선", [
        "oral-medicine", "orofacial-pain", "radiology", "halitosis",
        "tmj", "botulinum-toxin"]),
    ("교정 · 행동 · 경영 · AI", [
        "orthodontics", "behavioral-dentistry", "practice-management",
        "professional-wellbeing", "artificial-intelligence", "evidence-appraisal",
        "geriatric-dentistry", "complaint-management", "food-impaction"]),
]

def domain_for(category: str) -> str:
    top = category.split("/")[0] if category else ""
    for label, keys in DOMAINS:
        if top in keys:
            return label
    return "기타 · 미분류"

# ── frontmatter + One-line Summary 파서 ─────────────────────────────
FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

def parse_page(path: Path) -> dict:
    txt = path.read_text(encoding="utf-8", errors="replace")
    m = FM_RE.match(txt)
    fm = m.group(1) if m else ""
    body = txt[m.end():] if m else txt

    def field(name):
        r = re.search(rf"^{name}:\s*(.+)$", fm, re.MULTILINE)
        return r.group(1).strip().strip('"').strip("'") if r else ""

    # relations 블록 파싱: "- type: X\n    target: Y" 반복
    relations = []
    rel_m = re.search(r"^relations:\s*\n((?:[ \t]+.*\n?)+)", fm, re.MULTILINE)
    if rel_m:
        block = rel_m.group(1)
        for item in re.split(r"\n(?=\s*-\s)", block):
            t = re.search(r"type:\s*(\S+)", item)
            g = re.search(r"target:\s*(\S+)", item)
            if t and g:
                # target은 bare stem 또는 category/stem 경로형 둘 다 허용 → basename 정규화
                tgt = g.group(1).strip().rstrip("/").split("/")[-1]
                relations.append((t.group(1).strip(), tgt))

    def section(title):
        s = re.search(rf"^##\s*{re.escape(title)}\s*\n(.+?)(?=\n##\s|\Z)",
                      body, re.DOTALL | re.MULTILINE)
        if not s:
            return ""
        # 첫 비어있지 않은 문단만
        para = s.group(1).strip().split("\n\n")[0].strip()
        return re.sub(r"\s+", " ", para)

    return {
        "title": field("title"),
        "authors": field("authors"),
        "year": field("year"),
        "confidence": field("confidence"),
        "category": field("category").strip("[]"),
        "relations": relations,
        "one_en": section("One-line Summary"),
        "one_ko": section("한줄요약"),
    }

# ── 전체 스캔 ────────────────────────────────────────────────────────
pages = {}          # stem -> parsed dict (+ rel_path)
for md in WIKI.rglob("*.md"):
    if md.name.startswith("_"):
        continue
    stem = md.stem
    rel = md.relative_to(WIKI).with_suffix("")   # e.g. endodontics/irrigation/foo
    p = parse_page(md)
    p["stem"] = stem
    p["path"] = str(rel)
    pages[stem] = p

# ── contradicts/refines edge 수집 → 무순서 쌍 dedup ─────────────────
# pair_key = tuple(sorted([a,b])); 값 = {type, mutual, a_stem(source), b_stem}
STRENGTH = {"contradicts": 2, "refines": 1}
pairs = {}
missing = []

for stem, p in pages.items():
    for rtype, target in p["relations"]:
        if rtype not in STRENGTH:
            continue
        if target not in pages:
            missing.append((stem, rtype, target))
            continue
        key = tuple(sorted([stem, target]))
        cur = pairs.get(key)
        if cur is None:
            pairs[key] = {"type": rtype, "src": stem, "tgt": target, "mutual": False}
        else:
            # 이미 반대 방향 엣지 존재 → mutual, 강한 타입 채택
            if STRENGTH[rtype] >= STRENGTH[cur["type"]]:
                cur["type"] = rtype
            cur["mutual"] = True

# ── 도메인별 카드 데이터 구성 ────────────────────────────────────────
by_domain = defaultdict(list)
for key, e in pairs.items():
    a, b = pages[e["src"]], pages[e["tgt"]]
    # 카드 도메인은 두 논문 중 하나(source 기준)
    dom = domain_for(a["category"] or b["category"])
    by_domain[dom].append({"a": a, "b": b, "type": e["type"], "mutual": e["mutual"]})

# 도메인 순서: DOMAINS 정의 순 + 기타
order = [lbl for lbl, _ in DOMAINS] + ["기타 · 미분류"]
domains_sorted = [(d, by_domain[d]) for d in order if by_domain.get(d)]

total = sum(len(v) for _, v in domains_sorted)
n_contra = sum(1 for _, v in domains_sorted for c in v if c["type"] == "contradicts")
n_refine = total - n_contra

# ── HTML 렌더 ────────────────────────────────────────────────────────
def esc(s): return html.escape(s or "")

def conf_badge(c):
    return f'<span class="conf">{esc(c)}</span>' if c else ""

def paper_html(p, side):
    url = f"{SITE_BASE}/{p['path']}"
    meta = " · ".join(x for x in [esc(p["authors"][:40]), esc(str(p["year"]))] if x)
    thesis = esc(p["one_en"]) or "<em>(thesis 미기재)</em>"
    thesis_ko = esc(p["one_ko"])
    return f"""
      <div class="paper {side}">
        <a class="ptitle" href="{url}" target="_blank" rel="noopener">{esc(p['title']) or p['stem']}</a>
        <div class="pmeta">{meta} {conf_badge(p['confidence'])}</div>
        <div class="thesis">{thesis}</div>
        {f'<div class="thesis-ko">{thesis_ko}</div>' if thesis_ko else ''}
      </div>"""

def card_html(c):
    badge = ('<span class="tag contra">🔴 정면충돌</span>' if c["type"] == "contradicts"
             else '<span class="tag refine">🟡 조건부 반박</span>')
    mutual = '<span class="tag mutual">↔ 상호</span>' if c["mutual"] else ""
    cat = esc((c["a"]["category"] or c["b"]["category"]).split(",")[0])
    search = esc(" ".join([
        c["a"]["title"], c["b"]["title"], c["a"]["authors"], c["b"]["authors"],
        c["a"]["one_en"], c["b"]["one_en"], c["a"]["one_ko"], c["b"]["one_ko"], cat
    ])).lower()
    return f"""
    <div class="card" data-type="{c['type']}" data-search="{search}">
      <div class="cardhead">{badge}{mutual}<span class="chip">{cat}</span></div>
      <div class="vs">
        {paper_html(c['a'], 'left')}
        <div class="vsdiv">VS</div>
        {paper_html(c['b'], 'right')}
      </div>
    </div>"""

sections = []
for dom, cards in domains_sorted:
    cards_html = "".join(card_html(c) for c in cards)
    sections.append(f"""
    <section class="domain" data-count="{len(cards)}">
      <h2 class="domhead"><span class="caret">▾</span>{esc(dom)} <span class="dcount">{len(cards)}</span></h2>
      <div class="cards">{cards_html}</div>
    </section>""")

missing_note = ""
if missing:
    lines = "".join(f"<li>{esc(s)} —[{esc(t)}]→ <b>{esc(tg)}</b> (target 미존재)</li>"
                    for s, t, tg in missing[:20])
    missing_note = f'<details class="missing"><summary>⚠ 깨진 relations target {len(missing)}건</summary><ul>{lines}</ul></details>'

HTML = f"""<!--
---
title: "논쟁 레이더 — 위키 내부 상충 근거 지도"
type: interactive
date: AUTO
status: done
category: meta
source_wiki:
  - wiki/
note: "AUTO-GENERATED by scripts/build-contradiction-radar.py — 손편집 금지. relations: contradicts/refines edge를 달면 빌드가 카드를 만든다."
---
-->
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>논쟁 레이더 — Contradiction Radar</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&display=swap" rel="stylesheet">
<style>
  :root {{
    --bg:#0e1116; --panel:#161b22; --panel2:#1c232d; --line:#2b333d;
    --txt:#e6edf3; --dim:#9aa7b4; --contra:#ff5d5d; --refine:#f0b400;
    --left:#4aa3ff; --right:#ff8a5d; --chip:#243040;
  }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--bg); color:var(--txt);
    font-family:'Noto Sans KR',system-ui,sans-serif; line-height:1.5; }}
  .wrap {{ max-width:1080px; margin:0 auto; padding:28px 18px 80px; }}
  h1 {{ font-weight:900; font-size:1.9rem; margin:.2em 0 .1em;
    background:linear-gradient(90deg,var(--contra),var(--refine));
    -webkit-background-clip:text; background-clip:text; -webkit-text-fill-color:transparent; }}
  .sub {{ color:var(--dim); font-size:.95rem; margin-bottom:18px; }}
  .stats {{ display:flex; gap:10px; flex-wrap:wrap; margin-bottom:18px; }}
  .stat {{ background:var(--panel); border:1px solid var(--line); border-radius:10px;
    padding:10px 14px; font-size:.9rem; }}
  .stat b {{ font-size:1.3rem; }}
  .stat.c b {{ color:var(--contra); }} .stat.r b {{ color:var(--refine); }}
  .controls {{ position:sticky; top:0; z-index:5; background:var(--bg);
    padding:10px 0; display:flex; gap:10px; flex-wrap:wrap; align-items:center;
    border-bottom:1px solid var(--line); margin-bottom:8px; }}
  #q {{ flex:1; min-width:200px; background:var(--panel); border:1px solid var(--line);
    color:var(--txt); border-radius:8px; padding:9px 12px; font-size:.95rem; }}
  .filt {{ display:flex; gap:6px; }}
  .fbtn {{ background:var(--panel); border:1px solid var(--line); color:var(--dim);
    border-radius:8px; padding:8px 12px; cursor:pointer; font-size:.85rem; }}
  .fbtn.on {{ color:var(--txt); border-color:var(--txt); }}
  .fbtn.contra.on {{ color:var(--contra); border-color:var(--contra); }}
  .fbtn.refine.on {{ color:var(--refine); border-color:var(--refine); }}
  .domain {{ margin:22px 0; }}
  .domhead {{ font-size:1.15rem; font-weight:700; cursor:pointer; user-select:none;
    display:flex; align-items:center; gap:8px; padding:8px 0; border-bottom:1px solid var(--line); }}
  .caret {{ transition:transform .15s; font-size:.8em; color:var(--dim); }}
  .domain.collapsed .caret {{ transform:rotate(-90deg); }}
  .domain.collapsed .cards {{ display:none; }}
  .dcount {{ background:var(--chip); color:var(--dim); border-radius:20px;
    padding:1px 9px; font-size:.75rem; font-weight:400; }}
  .cards {{ display:flex; flex-direction:column; gap:12px; margin-top:12px; }}
  .card {{ background:var(--panel); border:1px solid var(--line); border-radius:12px;
    padding:14px 16px; }}
  .cardhead {{ display:flex; gap:8px; align-items:center; margin-bottom:10px; flex-wrap:wrap; }}
  .tag {{ font-size:.75rem; font-weight:700; padding:2px 9px; border-radius:20px; }}
  .tag.contra {{ background:rgba(255,93,93,.14); color:var(--contra); }}
  .tag.refine {{ background:rgba(240,180,0,.14); color:var(--refine); }}
  .tag.mutual {{ background:var(--chip); color:var(--dim); }}
  .chip {{ margin-left:auto; font-size:.72rem; color:var(--dim);
    background:var(--chip); padding:2px 9px; border-radius:20px; }}
  .vs {{ display:grid; grid-template-columns:1fr 44px 1fr; align-items:stretch; gap:6px; }}
  .paper {{ background:var(--panel2); border-radius:9px; padding:11px 12px;
    border-top:3px solid var(--line); }}
  .paper.left {{ border-top-color:var(--left); }}
  .paper.right {{ border-top-color:var(--right); }}
  .ptitle {{ color:var(--txt); font-weight:700; font-size:.92rem; text-decoration:none;
    display:block; margin-bottom:3px; }}
  .ptitle:hover {{ text-decoration:underline; }}
  .pmeta {{ color:var(--dim); font-size:.75rem; margin-bottom:7px; }}
  .conf {{ background:var(--chip); border-radius:5px; padding:0 6px; font-size:.7rem; }}
  .thesis {{ font-size:.85rem; }}
  .thesis-ko {{ font-size:.8rem; color:var(--dim); margin-top:5px;
    border-top:1px dashed var(--line); padding-top:5px; }}
  .vsdiv {{ display:flex; align-items:center; justify-content:center;
    font-weight:900; color:var(--dim); font-size:.85rem; }}
  .missing {{ margin-top:30px; color:var(--dim); font-size:.8rem; }}
  .missing summary {{ cursor:pointer; }}
  .foot {{ margin-top:40px; color:var(--dim); font-size:.78rem; text-align:center; }}
  .noresult {{ color:var(--dim); padding:30px; text-align:center; display:none; }}
  @media (max-width:640px) {{
    .vs {{ grid-template-columns:1fr; }}
    .vsdiv {{ padding:2px 0; }}
  }}
</style>
</head>
<body>
<div class="wrap">
  <h1>🎯 논쟁 레이더</h1>
  <div class="sub">위키 안에서 <b>근거가 서로 싸우고 있는 지점</b>만 모았습니다. 정답이 아니라 <b>회색지대</b>의 지도 — <code>relations: contradicts / refines</code> typed edge에서 자동 생성.</div>
  <div class="stats">
    <div class="stat"><b>{total}</b> 논쟁</div>
    <div class="stat c"><b>{n_contra}</b> 🔴 정면충돌</div>
    <div class="stat r"><b>{n_refine}</b> 🟡 조건부 반박</div>
    <div class="stat"><b>{len(domains_sorted)}</b> 도메인</div>
  </div>
  <div class="controls">
    <input id="q" placeholder="검색 — 주제·저자·논지 (예: centric relation, CoQ10, 즉시식립)…">
    <div class="filt">
      <button class="fbtn on" data-f="all">전체</button>
      <button class="fbtn contra" data-f="contradicts">🔴 정면충돌</button>
      <button class="fbtn refine" data-f="refines">🟡 조건부</button>
    </div>
  </div>
  <div class="noresult" id="noresult">검색 결과 없음</div>
  {"".join(sections)}
  {missing_note}
  <div class="foot">AUTO-GENERATED · scripts/build-contradiction-radar.py · 논쟁을 추가하려면 논문 frontmatter에 <code>relations: type: contradicts</code> edge를 다세요.</div>
</div>
<script>
  const q = document.getElementById('q');
  const cards = [...document.querySelectorAll('.card')];
  const noresult = document.getElementById('noresult');
  let filter = 'all';
  function apply() {{
    const term = q.value.trim().toLowerCase();
    let visible = 0;
    cards.forEach(c => {{
      const okF = filter === 'all' || c.dataset.type === filter;
      const okQ = !term || c.dataset.search.includes(term);
      const show = okF && okQ;
      c.style.display = show ? '' : 'none';
      if (show) visible++;
    }});
    document.querySelectorAll('.domain').forEach(d => {{
      const any = [...d.querySelectorAll('.card')].some(c => c.style.display !== 'none');
      d.style.display = any ? '' : 'none';
    }});
    noresult.style.display = visible ? 'none' : 'block';
  }}
  q.addEventListener('input', apply);
  document.querySelectorAll('.fbtn').forEach(b => b.addEventListener('click', () => {{
    document.querySelectorAll('.fbtn').forEach(x => x.classList.remove('on'));
    b.classList.add('on'); filter = b.dataset.f; apply();
  }}));
  document.querySelectorAll('.domhead').forEach(h =>
    h.addEventListener('click', () => h.parentElement.classList.toggle('collapsed')));
</script>
</body>
</html>"""

OUT.write_text(HTML, encoding="utf-8")
print(f"✓ {OUT.relative_to(ROOT)}  ({total} debates: {n_contra} contradicts / {n_refine} refines, {len(domains_sorted)} domains)")
if missing:
    print(f"  ⚠ {len(missing)} edges point to missing targets (listed in page)")
