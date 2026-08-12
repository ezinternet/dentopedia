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
SITE_BASE = "/dentopedia"

# 도메인 정의: (라벨, [stem 키워드...]). 위에서부터 첫 매치가 그 도메인.
# 순서 = 카드 표시 순서(임상 흐름). 키워드는 stem 부분일치.
#
# 설계 규칙(이질성 방지): 한 카드 = 한 임상 술식/주제. 메가카드(보철 20·근관 14 등)는
# 진료 하위분류로 분할하고, 서로 다른 주제가 한 카드에 섞이지 않게(예: PDRN↔BTX,
# 우식↔비우식경조직, 외과↔마취) 별도 카드로 떼어낸다.
# classify() 는 위에서부터 첫 매치를 반환하므로, 더 구체적인 카드를 위에 두고
# 키워드는 'implants-'(복수+하이픈)·'implant-surface'·'pulp-periapical' 처럼 specific
# 형태만 써서 다른 카드를 가로채지 않게 한다.
DOMAINS = [
    # ── 임플란트: 진료 하위분류 5장 ──
    ("임플란트 · 1차안정성 · ISQ · 부하", [
        "isq", "implant-loading"]),
    ("임플란트 · 표면처리 · 골유착", [
        "implant-surface", "plasma-surface", "photofunctionalization",
        "osseointegration", "vitamin-d"]),
    ("임플란트 · 디자인 · 매크로지오메트리 · 재료", [
        "implant-design", "implant-macrogeometry", "macrogeometry", "implant-length",
        "narrow-diameter", "tissue-level", "zirconia-implant"]),
    ("임플란트 · 식립술기 · 골밀도화 · 내비게이션", [
        "osseodensification", "versah", "robotic-vs-navigation", "navigation"]),
    ("임플란트 · 골질 · 실패위험 · 교합", [
        "bone-quality-implant", "implant-failure", "implant-occlusion",
        "implants-clinical", "implants-"]),
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
    # ── 근관치료: 메가카드(14)를 술식 단계 3장으로 분할 ──
    ("근관 · 해부 · 성형 · 근관장", [
        "c-shaped", "mb2", "canal-shaping", "access-cavity", "eal-working",
        "endodontics-comprehensive"]),
    ("근관 · 세정 · 소독 · 실러", [
        "irrigation", "cold-plasma", "ceraseal", "bioceramic-sealer", "endotoxin"]),
    ("근관 · 진단 · 생활치수 · 재생 · 내원", [
        "pulp-periapical", "vital-pulp", "regenerative-endodontics", "single-vs-multivisit"]),
    ("치주 · 교합외상", [
        "periodontics", "occlusal-trauma", "toothpick", "toothbrush", "watanabe",
        "plaque-control", "oral-hygiene", "interdental-cleaning", "interdental",
        "periodontal", "biofilm-management", "gbt", "air-polishing"]),
    ("교합 · TMJ · 이갈이", [
        "bruxism", "tmd-", "unilateral-mastication", "overeruption", "unopposed-tooth",
        "cr-co-micp", "centric", "reference-position",
        "occlusal-contact", "articulating-paper"]),
    # ── 보철·수복: 메가카드(20)를 3장으로 분할(보철↔세라믹↔레진접착) ──
    ("보철 · 의치 · 교합기록", [
        "complete-denture", "gothic-arch", "jaw-relation", "prosthetic-materials",
        "abutment-screw", "screw-preload", "crown-preparation", "post-and-core",
        "food-impaction"]),
    ("세라믹 · 지르코니아 · 심미수복", [
        "zirconia-material", "zirconia-types", "veneer", "lithium-disilicate",
        "dental-materials", "tooth-whitening"]),
    ("레진 · 접착", [
        "resin-dentin", "ceramic-bonding", "immediate-dentin", "adhesive-bonding",
        "direct-resin", "reis-2024"]),
    # ── 우식↔비우식경조직 분리 ──
    ("우식 · 예방 · 불소", [
        "caries", "glass-ionomer"]),
    ("비우식 경조직 · 시린이 · 균열", [
        "dental-erosion", "nccl", "dentin-hypersensitivity", "cracked-tooth"]),
    # ── 외과↔마취 분리 ──
    ("구강외과 · 발치 · 봉합 · 외상", [
        "oral-surgery", "third-molar", "suture-wound", "dental-trauma"]),
    ("국소마취 · 진정", [
        "buffered-modified", "mandibular-anesthesia", "topical-anesthetic", "local-anesthetic"]),
    ("약물 · 전신질환", ["drug-", "autoimmune", "systemic-disease", "hypertension", "hemodynamic"]),
    # ── 구강내과 메가카드(6)를 점막↔미생물↔노년 3장으로 분할 ──
    ("구강내과 · 점막 · 구강안면통증", [
        "oral-medicine", "bms", "orofacial-pain", "mucositis"]),
    ("구강미생물 · 구취", [
        "oral-microbiome", "halitosis"]),
    ("노년치의학", ["oral-frailty", "geriatric"]),
    ("교정", ["miniscrew", "orthodontic-tooth", "clear-aligner", "aligner", "myofunctional", "elastodontic"]),
    # ── 방사선↔디지털/AI 분리 ──
    ("방사선 · CBCT · 선량", ["cbct", "dental-imaging"]),
    ("디지털 · AI", ["digital-workflow", "ai-dentistry"]),
    # ── 행동/커뮤니케이션↔경영 분리 ──
    ("행동치의학 · 커뮤니케이션", ["behavioral-dentistry", "patient-consultation"]),
    ("경영 · 운영 · 민원 · 번아웃", [
        "korean-dental-practice", "complaint-management", "dentist-burnout",
        "no-show", "teledentistry", "workforce-delegation",
        "patient-safety-culture", "health-economics"]),
    # ── PDRN↔BTX 분리(이질) ──
    ("PDRN", ["pdrn"]),
    ("보툴리눔독소 · BTX", ["btx-"]),
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
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root {
  color-scheme: light;
  --bg:         #F6F7FC;
  --surface:    #FFFFFF;
  --border:     #DCE4F2;
  --text:       #1B2038;
  --muted:      #6473A3;
  --accent:     #1A55C5;
  --accent-dim: #EBF0FD;
  --hover:      #EDF2FC;
  --shadow:     0 1px 3px rgba(26,85,197,.07), 0 1px 2px rgba(0,0,0,.05);
  --focus-ring: 0 0 0 3px rgba(26,85,197,.20);
  --stripe:     3px;
  --radius:     10px;
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
body {
  background: #F6F7FC !important;
  color: #1B2038 !important;
  font-family: "Noto Sans KR", "Apple SD Gothic Neo", "Malgun Gothic", system-ui, sans-serif;
  font-size: 17px;
  line-height: 1.55;
  min-height: 100vh;
  padding-bottom: 58px;
}
.topbar {
  position: sticky;
  top: 0;
  z-index: 20;
  background: #F6F7FC !important;
  border-bottom: 1px solid #DCE4F2;
  padding: 12px 19px;
  display: flex;
  align-items: center;
  gap: 10px;
}
.search-wrap { flex: 1; position: relative; min-width: 0; }
.search-icon {
  position: absolute; left: 12px; top: 50%; transform: translateY(-50%);
  color: var(--muted); pointer-events: none; width: 17px; height: 17px;
}
#q {
  width: 100%; height: 43px; padding: 0 14px 0 38px;
  font-size: 16px; font-family: inherit; color: var(--text);
  background: var(--surface); border: 1px solid var(--border); border-radius: 10px;
  transition: border-color .15s, box-shadow .15s;
}
#q::placeholder { color: var(--muted); }
#q:focus { outline: none; border-color: var(--accent); box-shadow: var(--focus-ring); }
.btn {
  height: 38px; padding: 0 14px; font-size: 14px; font-family: inherit; font-weight: 500;
  cursor: pointer; color: var(--muted); background: var(--surface);
  border: 1px solid var(--border); border-radius: 9px; white-space: nowrap;
  letter-spacing: .01em; transition: color .12s, border-color .12s, background .12s;
}
.btn:hover { color: var(--accent); border-color: var(--accent); background: var(--accent-dim); }
.btn:focus-visible { outline: none; box-shadow: var(--focus-ring); }
.stats-bar { display: flex; align-items: center; gap: 10px; padding: 14px 19px; flex-wrap: wrap; }
.stat {
  display: inline-flex; align-items: baseline; gap: 6px;
  background: var(--surface); border: 1px solid var(--border);
  border-radius: 10px; padding: 6px 16px; box-shadow: var(--shadow);
}
.stat .n {
  font-family: "Inter", system-ui, sans-serif; font-size: 24px; font-weight: 700;
  color: var(--accent); font-variant-numeric: tabular-nums; letter-spacing: -.02em;
}
.stat .l { font-size: 14px; color: var(--muted); font-weight: 500; }
#grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(305px, 1fr));
  gap: 12px; padding: 0 19px;
}
.card {
  background: #FFFFFF !important; border: 1px solid #DCE4F2;
  border-radius: var(--radius); box-shadow: var(--shadow); align-self: start; overflow: hidden;
}
.head {
  display: flex; align-items: center; gap: 10px; cursor: pointer;
  padding: 11px 14px; border-left: 4px solid var(--accent);
  user-select: none; transition: background .1s;
}
.head:hover { background: var(--hover); }
.head:focus-visible { outline: none; box-shadow: var(--focus-ring); }
.head .nm { flex: 1; font-size: 16px; font-weight: 600; color: var(--text); line-height: 1.35; text-wrap: balance; }
.cnt {
  flex: none; font-family: "Inter", system-ui, sans-serif; font-size: 14px; font-weight: 700;
  font-variant-numeric: tabular-nums; background: var(--accent-dim); color: var(--accent);
  border-radius: 999px; padding: 2px 10px; letter-spacing: .01em;
}
.list { display: none; border-top: 1px solid var(--border); }
.row {
  display: flex; align-items: baseline; gap: 12px;
  padding: 9px 14px 9px 18px; color: var(--text); text-decoration: none; transition: background .1s;
}
.row:hover { background: var(--hover); }
.row:focus-visible { outline: none; background: var(--hover); }
.rt { flex: 1; min-width: 0; font-size: 15px; line-height: 1.45; color: var(--text); }
.rd {
  flex: none; font-family: "Inter", system-ui, sans-serif; font-size: 14px;
  color: var(--muted); font-variant-numeric: tabular-nums; white-space: nowrap; letter-spacing: .01em;
}
.no-results { grid-column: 1 / -1; padding: 48px 19px; text-align: center; color: var(--muted); font-size: 16px; display: none; }
.foot { margin-top: 24px; padding: 0 19px; font-size: 14px; color: var(--muted); letter-spacing: .015em; }
@media (prefers-reduced-motion: reduce) { *, *::before, *::after { transition: none !important; } }
</style>
</head>
<body>
<div class="topbar">
  <div class="search-wrap">
    <svg class="search-icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true">
      <circle cx="7" cy="7" r="4.5"/><path d="M10.5 10.5l3 3" stroke-linecap="round"/>
    </svg>
    <input id="q" type="text" placeholder="제목 · 도메인 검색 (ISQ, sinus, 마취, 약물…)" aria-label="overview 검색" autocomplete="off" spellcheck="false">
  </div>
  <button class="btn" id="expandAll" type="button">전체 펼치기</button>
  <button class="btn" id="collapseAll" type="button">접기</button>
</div>
<div class="stats-bar">
  <div class="stat"><span class="n" id="total">0</span><span class="l">종합 페이지</span></div>
  <div class="stat"><span class="n" id="ndom">0</span><span class="l">도메인</span></div>
  <div class="stat"><span class="n" id="hits">0</span><span class="l">검색 결과</span></div>
</div>
<div id="grid">
  <div class="no-results" id="noResults">검색 결과 없음</div>
</div>
<div class="foot">자동 생성 · __GENDATE__ · 새 overview 추가 시 배포 빌드에서 갱신됨</div>
<script>
const SITE_BASE = "__SITE_BASE__";
const DATA = __DATA__;
const grid = document.getElementById('grid');
const noResults = document.getElementById('noResults');
let totalItems = 0;
DATA.forEach((dom) => {
  totalItems += dom.items.length;
  const card = document.createElement('div'); card.className = 'card';
  const head = document.createElement('div'); head.className = 'head';
  head.setAttribute('tabindex', '0');
  head.setAttribute('role', 'button');
  head.setAttribute('aria-expanded', 'false');
  head.innerHTML = '<span class="nm">' + dom.name + '</span><span class="cnt">' + dom.items.length + '</span>';
  const list = document.createElement('div'); list.className = 'list';
  dom.items.forEach((it) => {
    const a = document.createElement('a'); a.className = 'row';
    a.href = SITE_BASE + '/overviews/' + it.s; a.target = '_top';
    a.dataset.txt = (it.t + ' ' + it.s + ' ' + dom.name).toLowerCase();
    a.innerHTML = '<span class="rt">' + it.t + '</span><span class="rd">' + (it.d || '') + '</span>';
    list.appendChild(a);
  });
  const toggle = () => {
    const open = list.style.display === 'block';
    list.style.display = open ? 'none' : 'block';
    head.setAttribute('aria-expanded', String(!open));
  };
  head.addEventListener('click', toggle);
  head.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggle(); } });
  card.appendChild(head); card.appendChild(list);
  grid.insertBefore(card, noResults);
});
document.getElementById('total').textContent = totalItems;
document.getElementById('ndom').textContent = DATA.length;
document.getElementById('hits').textContent = totalItems;
function setAll(show) {
  document.querySelectorAll('.list').forEach(l => l.style.display = show ? 'block' : 'none');
  document.querySelectorAll('.head').forEach(h => h.setAttribute('aria-expanded', String(show)));
}
document.getElementById('expandAll').addEventListener('click', () => setAll(true));
document.getElementById('collapseAll').addEventListener('click', () => setAll(false));
const q = document.getElementById('q'), hitsEl = document.getElementById('hits');
q.addEventListener('input', () => {
  const v = q.value.trim().toLowerCase(); let n = 0; let vis = 0;
  document.querySelectorAll('.card').forEach((card) => {
    let cn = 0;
    card.querySelectorAll('.row').forEach((r) => {
      const m = !v || r.dataset.txt.includes(v);
      r.style.display = m ? '' : 'none'; if (m) cn++;
    });
    if (cn > 0) {
      card.style.display = '';
      card.querySelector('.list').style.display = v ? 'block' : 'none';
      card.querySelector('.head').setAttribute('aria-expanded', v ? 'true' : 'false');
      vis++;
    } else { card.style.display = 'none'; }
    n += cn;
  });
  hitsEl.textContent = n;
  noResults.style.display = vis === 0 ? 'block' : 'none';
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
