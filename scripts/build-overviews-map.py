#!/usr/bin/env python3
"""
interactives/overviews-map.html 자동 생성기.

wiki/overviews/*.md 의 frontmatter(title/date)를 단일 진실원천으로 삼아,
종합(overview) 페이지를 임상 도메인별 카드로 묶은 self-contained HTML 탐색기를
생성한다. 홈(wiki/index.md)에서 iframe 으로 임베드해 배포 사이트에 노출한다.

실행: python3 scripts/build-overviews-map.py   (repo 루트 무관, 스크립트 위치 기준)
출력: interactives/overviews-map.html  (덮어쓰기, AUTO-GENERATED)

설계 원칙(build-interactives-index.py 와 동일):
- 새 overview 는 frontmatter 만 달면 빌드가 카드를 만든다. 수기 편집 불필요.
- stem 키워드로 도메인 자동 분류. 어느 규칙에도 안 걸리면 '기타' 버킷으로
  떨궈 절대 누락(invisible)되지 않는다.
"""

import re
import json
import html
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent.parent
OVDIR = ROOT / "wiki" / "overviews"
OUT = ROOT / "interactives" / "overviews-map.html"

# 배포 사이트 baseUrl 경로 prefix (quartz.config.ts baseUrl 과 일치).
# overview 페이지 링크: {SITE_BASE}/overviews/{stem}
SITE_BASE = "/llm-wiki"

# 도메인 정의: (라벨, [stem 키워드...]). 위에서부터 첫 매치가 그 도메인.
# 순서 = 카드 표시 순서(임상 흐름). 키워드는 stem 부분일치.
DOMAINS = [
    ("임플란트 · 안정성 · 표면", [
        "isq", "implant-surface", "plasma-surface", "photofunctionalization", "implant-design", "implant-length",
        "implant-loading", "implant-occlusion", "implants-", "narrow-diameter",
        "tissue-level", "zirconia-implant", "osseodensification", "versah",
        "robotic-vs-navigation", "bone-quality-implant",
        "implant-failure", "implant-macrogeometry", "macrogeometry", "osseointegration", "vitamin-d"]),
    ("즉시식립 · 타이밍", [
        "immediate-implant", "placement-timing", "socket-shield", "type-1a", "socket-iip"]),
    ("임플란트주위 연조직", [
        "keratinized-mucosa", "peri-implant-soft", "peri-implantitis", "peri-implant",
        "emergence-profile", "supportive-peri-implant"]),
    ("골재생 · GBR · ARP", [
        "bone-regeneration", "dbbm", "gbr-", "open-healing-arp",
        "socket-preservation", "vertical-ridge", "ridge-split"]),
    ("상악동거상술", [
        "sinus-lift", "short-implant-vs-sinus", "odontogenic-maxillary"]),
    ("근관치료", [
        "c-shaped", "canal-shaping", "eal-", "endodontic", "irrigation", "mb2",
        "regenerative-endodontics", "single-vs-multivisit", "vital-pulp"]),
    ("치주 · 교합외상", [
        "periodontics", "occlusal-trauma", "toothpick", "toothbrush", "watanabe",
        "plaque-control", "oral-hygiene", "interdental-cleaning", "interdental",
        "periodontal", "biofilm-management", "gbt", "air-polishing"]),
    ("교합 · TMJ · 이갈이", [
        "bruxism", "tmd-", "unilateral-mastication", "overeruption", "unopposed-tooth",
        "cr-co-micp", "centric", "reference-position",
        "occlusal-contact", "articulating-paper"]),
    ("보철 · 수복재료 · 심미", [
        "adhesive-bonding", "ceramic-bonding", "crown-preparation", "dental-materials",
        "direct-resin", "immediate-dentin", "lithium-disilicate", "prosthetic-materials",
        "reis-2024", "veneer", "zirconia-material", "zirconia-types", "resin-dentin",
        "complete-denture", "food-impaction",
        "post-and-core", "gothic-arch", "jaw-relation", "tooth-whitening", "restorative-margin",
        "abutment-screw", "screw-preload"]),
    ("우식 · 경조직 · 시린이 · 균열", [
        "caries", "cracked-tooth", "dental-erosion", "dentin-hypersensitivity",
        "glass-ionomer", "nccl"]),
    ("구강외과 · 마취 · 통증", [
        "buffered-modified", "mandibular-anesthesia", "oral-surgery", "third-molar",
        "topical-anesthetic", "suture-wound", "dental-trauma"]),
    ("약물 · 전신질환", ["drug-", "autoimmune", "systemic-disease", "hypertension", "hemodynamic"]),
    ("구강내과 · 미생물 · 노년 · 구강안면통증", [
        "oral-medicine", "oral-microbiome", "oral-frailty", "bms", "orofacial-pain",
        "halitosis", "mucositis"]),
    ("교정", ["miniscrew", "orthodontic-tooth", "clear-aligner", "aligner", "myofunctional", "elastodontic"]),
    ("방사선 · 디지털 · AI", [
        "cbct", "dental-imaging", "digital-workflow", "ai-dentistry"]),
    ("행동 · 커뮤니케이션 · 경영", [
        "behavioral-dentistry", "patient-consultation", "dentist-burnout",
        "complaint-management", "korean-dental-practice"]),
    ("PDRN · BTX", ["pdrn", "btx-"]),
    ("근거평가 · 통계", ["evidence-appraisal", "statistical-abbrev"]),
    ("장비 · 핸드피스 · 절삭기구", ["handpiece", "dental-bur", "bur-selection", "rotary-cutting"]),
]
FALLBACK_LABEL = "기타 · 미분류"


def parse_frontmatter(text):
    m = re.search(r"^---\s*\n(.*?)\n---\s*\n", text, flags=re.S)
    block = m.group(1) if m else ""
    fm = {}
    for line in block.split("\n"):
        km = re.match(r"^([a-zA-Z_]+):\s*(.*)$", line)
        if km:
            fm[km.group(1)] = km.group(2).strip().strip('"').strip("'")
    return fm


def classify(stem):
    for label, keys in DOMAINS:
        if any(k in stem for k in keys):
            return label
    return FALLBACK_LABEL


def collect():
    buckets = {label: [] for label, _ in DOMAINS}
    buckets[FALLBACK_LABEL] = []
    for f in sorted(OVDIR.glob("*.md")):
        stem = f.stem
        fm = parse_frontmatter(f.read_text(encoding="utf-8"))
        title = fm.get("title") or stem
        d = fm.get("date") or (fm.get("year", "") + "-01-01" if fm.get("year") else "")
        buckets[classify(stem)].append({"s": stem, "t": title, "d": d})
    # 도메인 내 최신순 정렬
    for label in buckets:
        buckets[label].sort(key=lambda x: x["d"], reverse=True)
    # 빈 도메인 제거, 정의 순서 유지(+ fallback 마지막)
    ordered = [(label, buckets[label]) for label, _ in DOMAINS if buckets[label]]
    if buckets[FALLBACK_LABEL]:
        ordered.append((FALLBACK_LABEL, buckets[FALLBACK_LABEL]))
    data = [{"name": label, "items": items} for label, items in ordered]
    return data


HTML_TEMPLATE = """<!--
---
title: "LLM Wiki — Overviews Map (종합 페이지 도메인 지도)"
type: interactive
date: AUTO
status: done
category: meta
note: "AUTO-GENERATED by scripts/build-overviews-map.py — 손으로 편집하지 말 것. 새 overview는 wiki/overviews/에 frontmatter 달고 떨구면 빌드가 카드를 만든다."
---
-->
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Overviews Map — 종합 페이지 도메인 지도</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: transparent; --card: #ffffff; --line: #e5e5e5; --muted: #6b6b6b;
    --dark: #2b2b2b; --secondary: #284b63; --chip-bg: #eef3f6; --chip-fg: #284b63;
    --rowhover: #f3f1f1;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0; padding: 4px 2px 10px; background: var(--bg); color: var(--dark);
    font-family: "Noto Sans KR", system-ui, sans-serif; font-size: 14px; line-height: 1.5;
  }
  .bar { display: flex; align-items: center; gap: 10px; flex-wrap: wrap; margin-bottom: 12px; }
  #q {
    flex: 1; min-width: 200px; height: 36px; padding: 0 12px; font-size: 14px;
    font-family: inherit; color: var(--dark); background: var(--card);
    border: 1px solid var(--line); border-radius: 8px;
  }
  #q:focus { outline: none; border-color: var(--secondary); }
  button {
    height: 32px; padding: 0 12px; font-size: 13px; font-family: inherit; cursor: pointer;
    color: var(--dark); background: var(--card); border: 1px solid var(--line); border-radius: 8px;
  }
  button:hover { border-color: var(--secondary); }
  .stats { display: flex; gap: 8px; margin-bottom: 12px; flex-wrap: wrap; }
  .stat { background: var(--chip-bg); border-radius: 8px; padding: 6px 12px; }
  .stat .n { font-size: 20px; font-weight: 700; color: var(--secondary); }
  .stat .l { font-size: 12px; color: var(--muted); }
  #grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; }
  .card { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 12px 14px; align-self: start; }
  .head { display: flex; align-items: center; justify-content: space-between; gap: 8px; cursor: pointer; }
  .head .nm { font-size: 14px; font-weight: 700; color: var(--dark); line-height: 1.35; }
  .cnt { flex: none; font-size: 12px; font-weight: 700; background: var(--chip-bg); color: var(--chip-fg); border-radius: 999px; padding: 2px 9px; }
  .list { margin-top: 10px; border-top: 1px solid var(--line); padding-top: 8px; }
  .row { display: block; padding: 6px 8px; margin: 0 -4px; border-radius: 6px; color: var(--dark); text-decoration: none; }
  .row:hover { background: var(--rowhover); }
  .row .rt { font-size: 13px; line-height: 1.4; }
  .row .rd { font-size: 11px; color: var(--muted); margin-left: 6px; white-space: nowrap; }
  .empty { color: var(--muted); font-size: 13px; padding: 8px 2px; }
  .foot { margin-top: 12px; font-size: 11px; color: var(--muted); }
</style>
</head>
<body>
<div class="bar">
  <input id="q" type="text" placeholder="제목·도메인 검색 (예: ISQ, sinus, 마취, 약물)" aria-label="overview 검색">
  <button id="expandAll" type="button">전체 펼치기</button>
  <button id="collapseAll" type="button">접기</button>
</div>
<div class="stats">
  <div class="stat"><span class="n" id="total">0</span> <span class="l">종합 페이지</span></div>
  <div class="stat"><span class="n" id="ndom">0</span> <span class="l">도메인</span></div>
  <div class="stat"><span class="n" id="hits">0</span> <span class="l">검색 결과</span></div>
</div>
<div id="grid"></div>
<div class="foot">자동 생성 · __GENDATE__ · 새 overview 추가 시 배포 빌드에서 갱신됨</div>
<script>
const SITE_BASE = "__SITE_BASE__";
const DATA = __DATA__;
const grid = document.getElementById('grid');
let totalItems = 0;
DATA.forEach((dom) => {
  totalItems += dom.items.length;
  const card = document.createElement('div'); card.className = 'card';
  const head = document.createElement('div'); head.className = 'head';
  head.innerHTML = '<span class="nm">' + dom.name + '</span><span class="cnt">' + dom.items.length + '</span>';
  const list = document.createElement('div'); list.className = 'list'; list.style.display = 'none';
  dom.items.forEach((it) => {
    const a = document.createElement('a'); a.className = 'row';
    a.href = SITE_BASE + '/overviews/' + it.s; a.target = '_top';
    a.dataset.txt = (it.t + ' ' + it.s + ' ' + dom.name).toLowerCase();
    a.innerHTML = '<span class="rt">' + it.t + '</span><span class="rd">' + (it.d || '') + '</span>';
    list.appendChild(a);
  });
  head.addEventListener('click', () => { list.style.display = list.style.display === 'none' ? 'block' : 'none'; });
  card.appendChild(head); card.appendChild(list); grid.appendChild(card);
});
document.getElementById('total').textContent = totalItems;
document.getElementById('ndom').textContent = DATA.length;
document.getElementById('hits').textContent = totalItems;
function setAll(show){ document.querySelectorAll('.list').forEach(l => l.style.display = show ? 'block' : 'none'); }
document.getElementById('expandAll').addEventListener('click', () => setAll(true));
document.getElementById('collapseAll').addEventListener('click', () => setAll(false));
const q = document.getElementById('q'), hits = document.getElementById('hits');
q.addEventListener('input', () => {
  const v = q.value.trim().toLowerCase(); let n = 0;
  document.querySelectorAll('.card').forEach((card) => {
    let cn = 0;
    card.querySelectorAll('.row').forEach((r) => {
      const m = !v || r.dataset.txt.includes(v);
      r.style.display = m ? 'block' : 'none'; if (m) cn++;
    });
    card.style.display = cn ? 'block' : 'none';
    card.querySelector('.list').style.display = (v && cn) ? 'block' : 'none';
    n += cn;
  });
  hits.textContent = n;
});
</script>
</body>
</html>
"""


def main():
    data = collect()
    total = sum(len(d["items"]) for d in data)
    out = (HTML_TEMPLATE
           .replace("__SITE_BASE__", SITE_BASE)
           .replace("__GENDATE__", date.today().isoformat())
           .replace("__DATA__", json.dumps(data, ensure_ascii=False)))
    OUT.write_text(out, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}  ({len(data)} domains, {total} overviews)")
    for d in data:
        print(f"  {len(d['items']):2d}  {d['name']}")


if __name__ == "__main__":
    main()
