#!/usr/bin/env python3
"""
interactives/wiki-stats-live.html 자동 생성기 (Class A — 메타·통계 도구의 라이브 갱신).

날짜 박힌 스냅샷(wiki-evolution v1~v4 · wiki-growth-curve)은 '진화 이력'으로 동결
유지하고, 이 스크립트는 배포 때마다 리포 실측치로 데이터가 새로 채워지는 단 하나의
영구(perpetual) 대시보드를 만든다. v4의 렌더 엔진(데이터↔SVG 분리 구조)을 그대로
재사용하되 DATA 블록과 헤더 스칼라만 리포 상태에서 재계산해 주입한다.

데이터(전부 기계적·안전 — 임상 수치 추출 아님):
  - 총 papers(sources/*.md), overviews, wiki pages, 고근거(sr+ma·sr·rct)
  - PAPER_PTS / OVR_PTS : git add/del 날짜 기준 net 누적 곡선
  - YEARS : sources frontmatter year: 히스토그램 (≤2002 묶음)
  - CATS  : wiki top-level 폴더별 페이지 수 (top 20 + 기타 버킷, _ 폴더 제외)
편집성(과거 사실 → 영구 유효) MILESTONES/PHASES/SCRIPTS는 정적 베이스라인으로 둔다.

실행: python3 scripts/build-wiki-stats.py   (repo 루트 무관)
출력: interactives/wiki-stats-live.html  (덮어쓰기)

git 누적은 full history가 필요 — 배포 워크플로우의 actions/checkout fetch-depth:0 전제.
git 사용 불가/얕은 클론이면 곡선은 현재값 2점으로 degrade(빌드는 실패하지 않음).
"""

import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "sources"
WIKI = ROOT / "wiki"
OUT = ROOT / "interactives" / "wiki-stats-live.html"

HIGH_EVIDENCE = {"sr+ma", "sr", "rct"}


def fm_first(text: str, key: str):
    m = re.search(r"^%s:\s*(.+)$" % re.escape(key), text, re.M)
    return m.group(1).strip().strip('"').strip("'") if m else None


# ---------- scalar / histogram computations (filesystem) ----------

def compute_fs_stats():
    sources = sorted(SOURCES.glob("*.md"))
    n_papers = len(sources)

    years = defaultdict(int)
    for p in sources:
        head = p.read_text(encoding="utf-8")[:1500]
        y = fm_first(head, "year")
        if y:
            m = re.search(r"\d{4}", y)
            if m:
                years[int(m.group())] += 1

    cats = defaultdict(int)
    n_wiki = n_hi = 0
    for p in WIKI.rglob("*.md"):
        rel = p.relative_to(WIKI).parts
        if not rel or rel[0].startswith("_"):
            continue
        top = rel[0]
        cats[top] += 1
        n_wiki += 1
        head = p.read_text(encoding="utf-8")[:1500]
        c = fm_first(head, "confidence")
        if c and c.strip() in HIGH_EVIDENCE:
            n_hi += 1

    n_ovr = cats.get("overviews", 0)
    return {
        "n_papers": n_papers,
        "n_wiki": n_wiki,
        "n_ovr": n_ovr,
        "n_hi": n_hi,
        "years": dict(years),
        "cats": dict(cats),
    }


# ---------- git net-cumulative curves ----------

def git_cumulative(pathspec: str):
    """현재 존재하는 파일집합의 net 누적을 add/del 이벤트로 날짜별 재구성.
    rename은 D(old)+A(new) 동일 커밋이라 net 0 — 정확. git 실패 시 None."""
    try:
        out = subprocess.run(
            ["git", "log", "--diff-filter=AD", "--name-status",
             "--format=C|%ad", "--date=short", "--", pathspec],
            cwd=ROOT, capture_output=True, text=True, timeout=120, check=True,
        ).stdout
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError):
        return None

    delta = defaultdict(int)
    cur = None
    for line in out.splitlines():
        if line.startswith("C|"):
            cur = line[2:].strip()
        elif line and cur:
            st = line.split("\t")[0]
            if st.startswith("A"):
                delta[cur] += 1
            elif st.startswith("D"):
                delta[cur] -= 1
    if not delta:
        return None
    net = 0
    pts = {}
    for d in sorted(delta):
        net += delta[d]
        pts[d] = net
    return pts


# ---------- HTML assembly ----------

def build_years_arr(years: dict):
    """≤2002 묶음 + 2003..max 개별. [["≤2002",n],["2003",n],...]"""
    if not years:
        return []
    pre = sum(v for k, v in years.items() if k <= 2002)
    arr = []
    if pre:
        arr.append(["≤2002", pre])
    mx = max(years)
    for y in range(2003, mx + 1):
        arr.append([str(y), years.get(y, 0)])
    return arr


def build_cats_arr(cats: dict, top_n=20):
    items = sorted(cats.items(), key=lambda x: -x[1])
    head = items[:top_n]
    tail = items[top_n:]
    arr = [[k, v] for k, v in head]
    if tail:
        arr.append([f"기타({len(tail)}+ cats)", sum(v for _, v in tail)])
    return arr


# 편집성(과거 사실 — 영구 유효) 정적 베이스라인. 새 분기점은 손으로 append 가능.
STATIC_PHASES = [
    {"s": "2026-05-18", "e": "2026-05-30", "name": "① 부트스트랩",
     "desc": "3-tier 적재 + day-1 lint/orphan-check", "color": "var(--c1)"},
    {"s": "2026-05-31", "e": "2026-06-01", "name": "② 자가감사 생명체",
     "desc": "daily-audit 외 8 audit 동시 출생 · overview 20→58", "color": "var(--c2)"},
    {"s": "2026-06-02", "e": "2026-06-11", "name": "③ 출력공장",
     "desc": "interactives · build-interactives-index", "color": "var(--c4)"},
    {"s": "2026-06-12", "e": "2026-06-27", "name": "④ 산업화·자동감시",
     "desc": "ingest-one 병렬 · overviews-map · fetch-oa · wiki-stats-live", "color": "var(--c5)"},
]
STATIC_SCRIPTS = [
    {"date": "2026-05-18", "label": "lint · orphan-check", "up": True},
    {"date": "2026-05-19", "label": "queue-watcher", "up": False},
    {"date": "2026-05-23", "label": "operations-lint", "up": True},
    {"date": "2026-05-31", "label": "daily-audit + 8 audits", "up": False},
    {"date": "2026-06-08", "label": "build-interactives-index", "up": True},
    {"date": "2026-06-12", "label": "ingest-one (병렬 finalize)", "up": False},
    {"date": "2026-06-16", "label": "build-overviews-map", "up": True},
    {"date": "2026-06-19", "label": "fetch-oa · sweep_state", "up": False},
]
STATIC_MILESTONES = [
    {"date": "2026-05-18", "label": "repo init · seed 350"},
    {"date": "2026-05-31", "label": "+203 · 8 audits 출생"},
    {"date": "2026-06-12", "label": "ingest-one 병렬화"},
    {"date": "2026-06-19", "label": "OA 자동수급(fetch-oa)"},
]


def main():
    fs = compute_fs_stats()
    paper_pts = git_cumulative("sources/*.md")
    ovr_pts = git_cumulative("wiki/overviews/*.md")

    today = date.today().isoformat()
    # git 불가(얕은 클론 등) → 현재값 단일점으로 degrade
    if not paper_pts:
        paper_pts = {today: fs["n_papers"]}
    if not ovr_pts:
        ovr_pts = {today: fs["n_ovr"]}

    # 곡선 끝점을 항상 '오늘 = 현재 실측'으로 보정 (워킹트리/커밋 미세차 흡수)
    paper_pts[today] = fs["n_papers"]
    ovr_pts[today] = fs["n_ovr"]

    dates = sorted(paper_pts)
    start_d, end_d = dates[0], dates[-1]
    start_v = paper_pts[start_d]
    end_v = fs["n_papers"]
    days = (date.fromisoformat(end_d) - date.fromisoformat(start_d)).days
    mult = end_v / start_v if start_v else 1.0

    milestones = list(STATIC_MILESTONES) + [
        {"date": end_d, "label": f"현재 {end_v:,}", "last": True}
    ]

    years_arr = build_years_arr(fs["years"])
    cats_arr = build_cats_arr(fs["cats"])

    # 최근 5년 합 (note용)
    cy = date.today().year
    recent5 = sum(v for k, v in fs["years"].items() if k >= cy - 4)
    recent_pct = round(recent5 / fs["n_papers"] * 100) if fs["n_papers"] else 0

    data_js = f"""/* ===== DATA — AUTO-GENERATED {today} by scripts/build-wiki-stats.py (리포 실측) ===== */
const PAPER_PTS = {json.dumps(paper_pts, ensure_ascii=False)};
const OVR_PTS   = {json.dumps(ovr_pts, ensure_ascii=False)};
const MILESTONES = {json.dumps(milestones, ensure_ascii=False)};
const YEARS = {json.dumps(years_arr, ensure_ascii=False)};
const CATS = {json.dumps(cats_arr, ensure_ascii=False)};
const PHASES = {json.dumps(STATIC_PHASES, ensure_ascii=False)};
const SCRIPTS = {json.dumps(STATIC_SCRIPTS, ensure_ascii=False)};
const PMAX = {end_v};
const META = {json.dumps({
    "papers": end_v, "ovr": fs["n_ovr"], "wiki": fs["n_wiki"], "hi": fs["n_hi"],
    "start_d": start_d, "end_d": end_d, "start_v": start_v, "days": days,
    "mult": round(mult, 1), "recent5": recent5, "recent_pct": recent_pct,
}, ensure_ascii=False)};"""

    html = HTML_TEMPLATE.replace("/*__DATA__*/", data_js)
    html = html.replace("__SUB__",
        f"{start_d} ~ {end_d} · {end_v:,} papers · {fs['n_ovr']} overviews · "
        f"{fs['n_wiki']:,} wiki pages ({days}일)")
    html = html.replace("__KPI_PAPERS__", f"{end_v:,}")
    html = html.replace("__KPI_OVR__", f"{fs['n_ovr']:,}")
    html = html.replace("__KPI_HI__", f"{fs['n_hi']:,}")
    html = html.replace("__KPI_MULT__", f"~{mult:.1f}×")
    html = html.replace("__KPI_MULT_L__",
        f"{days}일간 papers 성장 ({start_v:,}→{end_v:,})")
    html = html.replace("__STAMP__", today)

    OUT.write_text(html, encoding="utf-8")
    print(f"[build-wiki-stats] {end_v:,} papers · {fs['n_ovr']} overviews · "
          f"{fs['n_wiki']:,} wiki pages · {fs['n_hi']:,} high-evidence → "
          f"{OUT.relative_to(ROOT)}")


# v4 렌더 엔진을 그대로 재사용 — DATA 블록(/*__DATA__*/)·헤더 스칼라(__...__)만 주입.
HTML_TEMPLATE = r"""<!--
---
title: "llm-wiki Stats (Live) — Ingest 타임라인 · 발행연도 · 카테고리 · System Evolution"
type: interactive
date: AUTO
status: done
category: meta
note: "AUTO-GENERATED by scripts/build-wiki-stats.py — 손으로 편집하지 말 것. 배포 때마다 리포 실측치로 데이터가 갱신되는 영구 라이브 대시보드. 날짜 박힌 v1~v4·growth-curve는 진화 이력 스냅샷으로 동결."
source_wiki:
  - index.md
---
-->
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>llm-wiki Stats (Live)</title>
<style>
  :root{
    --bg:#f5ecd9; --ink:#1a1a1a; --muted:#6b6b6b; --grid:#c9bfa8;
    --card:#fbf4e2;
    --c1:#d97d52; --c2:#3d7b7d; --c3:#7fa177; --c4:#c89e3a; --c5:#9b6e8b;
  }
  *{box-sizing:border-box;}
  body{margin:0;padding:28px;background:var(--bg);color:var(--ink);
    font-family:-apple-system,BlinkMacSystemFont,"Pretendard","Apple SD Gothic Neo","Helvetica Neue",Arial,sans-serif;}
  .card{background:var(--card);border-radius:18px;padding:26px 34px 22px;max-width:1180px;margin:0 auto;
    box-shadow:0 1px 0 rgba(0,0,0,.04);}
  h1{font-size:18px;font-weight:600;margin:0 0 3px;letter-spacing:-.01em;}
  .live{display:inline-block;font-size:10px;font-weight:700;color:#fff;background:var(--c2);
    border-radius:999px;padding:2px 9px;margin-left:8px;vertical-align:middle;letter-spacing:.04em;}
  .subtitle{color:var(--muted);font-size:12px;margin-bottom:16px;font-feature-settings:"tnum";}
  .tabs{display:flex;gap:6px;margin-bottom:14px;flex-wrap:wrap;}
  .tab{font-size:12.5px;padding:7px 14px;border:1px solid var(--grid);background:transparent;border-radius:999px;
    cursor:pointer;color:var(--muted);font-family:inherit;transition:all .15s;}
  .tab:hover{border-color:var(--c1);color:var(--ink);}
  .tab.active{background:var(--ink);color:var(--bg);border-color:var(--ink);font-weight:600;}
  .kpis{display:flex;gap:24px;flex-wrap:wrap;margin:2px 0 16px;}
  .kpi{display:flex;flex-direction:column;}
  .kpi .v{font-size:22px;font-weight:700;font-feature-settings:"tnum";letter-spacing:-.02em;}
  .kpi .l{font-size:11px;color:var(--muted);}
  svg{display:block;width:100%;height:auto;}
  .axis text{font-size:11px;fill:var(--muted);font-feature-settings:"tnum";}
  .axis line{stroke:var(--grid);}
  .grid line{stroke:var(--grid);stroke-dasharray:2 3;opacity:.6;}
  .ms-line{stroke:var(--ink);stroke-dasharray:2 3;stroke-width:1;opacity:.5;}
  .ms-dot{fill:var(--ink);}
  .ms-label{font-size:10px;fill:var(--ink);font-feature-settings:"tnum";}
  .dot{cursor:pointer;}
  .bar{cursor:pointer;transition:opacity .12s;}
  .bar:hover{opacity:.78;}
  .legend{display:flex;gap:22px;flex-wrap:wrap;padding-top:14px;border-top:1px solid var(--grid);margin-top:6px;font-size:12.5px;}
  .legend .item{display:inline-flex;align-items:center;gap:7px;}
  .legend .sw{width:13px;height:13px;border-radius:3px;display:inline-block;}
  .legend .name{font-weight:600;}
  #tip{position:fixed;pointer-events:none;background:var(--ink);color:var(--bg);padding:7px 10px;border-radius:8px;
    font-size:12px;line-height:1.45;opacity:0;transition:opacity .1s;font-feature-settings:"tnum";z-index:9;max-width:260px;}
  #tip b{color:#ffd9a8;}
  .note{font-size:11px;color:var(--muted);margin-top:10px;line-height:1.5;}
  .stamp{font-size:10.5px;color:var(--muted);margin-top:12px;opacity:.8;}
</style>
</head>
<body>
<div class="card">
  <h1>llm-wiki — Knowledge Stats <span class="live">LIVE</span></h1>
  <div class="subtitle" id="sub">__SUB__</div>

  <div class="kpis">
    <div class="kpi"><span class="v">__KPI_PAPERS__</span><span class="l">Papers (sources)</span></div>
    <div class="kpi"><span class="v">__KPI_OVR__</span><span class="l">Overview 합성</span></div>
    <div class="kpi"><span class="v">__KPI_HI__</span><span class="l">고근거 (SR+MA·SR·RCT)</span></div>
    <div class="kpi"><span class="v">__KPI_MULT__</span><span class="l">__KPI_MULT_L__</span></div>
  </div>

  <div class="tabs">
    <button class="tab active" data-v="timeline">① Ingest Evolution</button>
    <button class="tab" data-v="years">② 발행연도 Coverage</button>
    <button class="tab" data-v="cats">③ Category Composition</button>
    <button class="tab" data-v="system">④ System Evolution</button>
  </div>

  <svg id="chart" viewBox="0 0 1180 520" preserveAspectRatio="xMidYMid meet"></svg>
  <div class="legend" id="legend"></div>
  <div class="note" id="note"></div>
  <div class="stamp">자동 생성 · 배포 시점 리포 실측 (build-wiki-stats.py) · 갱신 __STAMP__</div>
</div>
<div id="tip"></div>

<script>
/*__DATA__*/

/* ===== SVG helpers ===== */
const NS="http://www.w3.org/2000/svg";
const svg=document.getElementById("chart");
const tip=document.getElementById("tip");
const legend=document.getElementById("legend");
const noteEl=document.getElementById("note");
const W=1180,H=520;
function el(tag,a={},p=svg){const n=document.createElementNS(NS,tag);for(const k in a)n.setAttribute(k,a[k]);p.appendChild(n);return n;}
function clear(){while(svg.firstChild)svg.removeChild(svg.firstChild);legend.innerHTML="";}
function showTip(e,html){tip.innerHTML=html;tip.style.opacity=1;tip.style.left=(e.clientX+14)+"px";tip.style.top=(e.clientY+14)+"px";}
function hideTip(){tip.style.opacity=0;}
function lgItem(color,name,val){const s=document.createElement("span");s.className="item";s.innerHTML=`<span class="sw" style="background:${color}"></span><span class="name">${name}</span> <span style="color:var(--muted)">${val??""}</span>`;legend.appendChild(s);}

function dateRange(a,b){const out=[],d=new Date(a);const end=new Date(b);while(d<=end){out.push(d.toISOString().slice(0,10));d.setDate(d.getDate()+1);}return out;}
function carry(pts,dates){const out=[];let last=0;for(const d of dates){if(pts[d]!=null)last=pts[d];out.push(last);}return out;}

/* ===== VIEW 1: timeline ===== */
function viewTimeline(){
  clear();
  const M={top:96,right:54,bottom:48,left:62},iW=W-M.left-M.right,iH=H-M.top-M.bottom;
  const dates=dateRange(META.start_d,META.end_d);
  const papers=carry(PAPER_PTS,dates),ovr=carry(OVR_PTS,dates);
  const N=dates.length, xs=i=>M.left+(i/(N-1))*iW, yMax=PMAX*1.08, ys=v=>M.top+iH-(v/yMax)*iH;
  for(let t=0;t<=4;t++){const yv=yMax/4*t,yy=ys(yv);const g=el("g",{class:"grid"});el("line",{x1:M.left,x2:M.left+iW,y1:yy,y2:yy},g);
    const tx=el("text",{x:M.left-10,y:yy+4,"text-anchor":"end"});tx.setAttribute("font-size","11");tx.setAttribute("fill","var(--muted)");tx.textContent=Math.round(yv);}
  function area(arr,color,op){let d="";for(let i=0;i<N;i++)d+=(i?` L`:`M`)+` ${xs(i)} ${ys(arr[i])}`;d+=` L ${xs(N-1)} ${ys(0)} L ${xs(0)} ${ys(0)} Z`;el("path",{d,fill:color,"fill-opacity":op});}
  function line(arr,color,w){let d="";for(let i=0;i<N;i++)d+=(i?` L`:`M`)+` ${xs(i)} ${ys(arr[i])}`;el("path",{d,fill:"none",stroke:color,"stroke-width":w,"stroke-linejoin":"round"});}
  area(papers,"var(--c1)",.20); line(papers,"var(--c1)",2.4);
  area(ovr,"var(--c2)",.22); line(ovr,"var(--c2)",2.2);
  el("line",{x1:M.left,x2:M.left+iW,y1:ys(0),y2:ys(0),stroke:"var(--ink)","stroke-width":1});
  // x ticks: 시작·끝 + 균등 4분할
  const tickI=[0,Math.round((N-1)/4),Math.round((N-1)/2),Math.round(3*(N-1)/4),N-1];
  [...new Set(tickI)].forEach(i=>{const last=(i===N-1);const tx=el("text",{x:xs(i),y:ys(0)+22,"text-anchor":"middle"});tx.setAttribute("font-size","11");tx.setAttribute("fill",last?"var(--ink)":"var(--muted)");tx.setAttribute("font-weight",last?"700":"400");tx.textContent=dates[i].slice(5);});
  MILESTONES.forEach(ms=>{const i=dates.indexOf(ms.date);if(i<0)return;const x=xs(i);
    el("line",{x1:x,x2:x,y1:24,y2:ys(0),class:"ms-line"});el("circle",{cx:x,cy:24,r:3,class:"ms-dot"});
    const t=el("text",{x:x,y:16,"text-anchor": x>W-180?"end":"middle",class:"ms-label"});t.setAttribute("font-weight",ms.last?"700":"400");t.textContent=ms.date.slice(5);
    const t2=el("text",{x:x,y:40,"text-anchor":x>W-180?"end":"middle",class:"ms-label"});t2.setAttribute("fill","var(--muted)");t2.textContent=ms.label;});
  for(let i=0;i<N;i++){
    const hd=el("circle",{cx:xs(i),cy:ys(papers[i]),r:9,fill:"transparent",class:"dot"});
    hd.addEventListener("mousemove",e=>showTip(e,`<b>${dates[i]}</b><br>papers ${papers[i]}<br>overviews ${ovr[i]}`));
    hd.addEventListener("mouseleave",hideTip);
    el("circle",{cx:xs(i),cy:ys(papers[i]),r:2.5,fill:"var(--c1)"});
    el("circle",{cx:xs(i),cy:ys(ovr[i]),r:2.5,fill:"var(--c2)"});
  }
  lgItem("var(--c1)","Papers (sources)",META.papers.toLocaleString());
  lgItem("var(--c2)","Overview 합성",META.ovr);
  noteEl.textContent=`git add-date 기준 net 누적. ${META.start_d} repo-init seed ${META.start_v.toLocaleString()}편에서 ${META.days}일간 ${META.papers.toLocaleString()}편으로 (~${META.mult}× 성장). 곡선 위 점에 마우스를 올리면 일별 값 표시. 배포 때마다 리포 실측으로 갱신.`;
}

/* ===== VIEW 2: years ===== */
function viewYears(){
  clear();
  const M={top:40,right:54,bottom:64,left:50},iW=W-M.left-M.right,iH=H-M.top-M.bottom;
  const N=YEARS.length, bw=iW/N*0.66, gap=iW/N;
  const yMax=Math.max(...YEARS.map(d=>d[1]))*1.12, ys=v=>M.top+iH-(v/yMax)*iH;
  let acc=0;const cum=YEARS.map(d=>{acc+=d[1];return acc;});const cumMax=acc;
  for(let t=0;t<=4;t++){const yv=yMax/4*t,yy=ys(yv);const g=el("g",{class:"grid"});el("line",{x1:M.left,x2:M.left+iW,y1:yy,y2:yy},g);const tx=el("text",{x:M.left-8,y:yy+4,"text-anchor":"end"});tx.setAttribute("font-size","11");tx.setAttribute("fill","var(--muted)");tx.textContent=Math.round(yv);}
  const cy=new Date().getFullYear();
  YEARS.forEach((d,i)=>{const x=M.left+gap*i+(gap-bw)/2,h=iH-(ys(d[1])-M.top),y=ys(d[1]);
    const yr=parseInt(d[0].replace(/\D/g,""))||0; const recent=(yr>=cy-4);
    const r=el("rect",{x,y,width:bw,height:Math.max(h,0),rx:2,fill:recent?"var(--c3)":"var(--c1)",class:"bar"});
    r.addEventListener("mousemove",e=>showTip(e,`<b>${d[0]}</b><br>${d[1]}편${recent?" · 최근 5년":""}<br>누적 ${cum[i]}`));
    r.addEventListener("mouseleave",hideTip);});
  const ysC=v=>M.top+iH-(v/(cumMax*1.05))*iH;let dd="";YEARS.forEach((d,i)=>{const x=M.left+gap*i+gap/2;dd+=(i?` L`:`M`)+` ${x} ${ysC(cum[i])}`;});
  el("path",{d:dd,fill:"none",stroke:"var(--c5)","stroke-width":2,"stroke-dasharray":"4 3"});
  el("line",{x1:M.left,x2:M.left+iW,y1:ys(0),y2:ys(0),stroke:"var(--ink)","stroke-width":1});
  YEARS.forEach((d,i)=>{if(i%2&&i!==YEARS.length-1)return;const x=M.left+gap*i+gap/2;const tx=el("text",{x,y:ys(0)+20,"text-anchor":"middle"});tx.setAttribute("font-size","10");tx.setAttribute("fill","var(--muted)");tx.setAttribute("transform",`rotate(35 ${x} ${ys(0)+20})`);tx.textContent=d[0];});
  lgItem("var(--c1)","< 최근 5년");
  lgItem("var(--c3)","최근 5년");
  lgItem("var(--c5)","누적선");
  noteEl.textContent=`발행연도 분포. 최근 5년이 ${META.recent5.toLocaleString()}편으로 전체의 ~${META.recent_pct}% — corpus가 최신 근거에 강하게 치우침. ≤2002는 묶음.`;
}

/* ===== VIEW 3: categories ===== */
function viewCats(){
  clear();
  const M={top:24,right:70,bottom:24,left:150},iW=W-M.left-M.right;
  const N=CATS.length, rh=(H-M.top-M.bottom)/N, bh=rh*0.62;
  const xMax=Math.max(...CATS.map(d=>d[1]))*1.04, xs=v=>(v/xMax)*iW;
  CATS.forEach((d,i)=>{const y=M.top+rh*i+(rh-bh)/2;
    const colorIdx=i%5; const colors=["var(--c1)","var(--c2)","var(--c3)","var(--c4)","var(--c5)"];
    const r=el("rect",{x:M.left,y,width:Math.max(xs(d[1]),1),height:bh,rx:3,fill:colors[colorIdx],"fill-opacity":.85,class:"bar"});
    r.addEventListener("mousemove",e=>showTip(e,`<b>${d[0]}</b><br>${d[1]} pages`));r.addEventListener("mouseleave",hideTip);
    const lab=el("text",{x:M.left-10,y:y+bh/2+4,"text-anchor":"end"});lab.setAttribute("font-size","11.5");lab.setAttribute("fill","var(--ink)");lab.textContent=d[0];
    const val=el("text",{x:M.left+xs(d[1])+8,y:y+bh/2+4});val.setAttribute("font-size","11");val.setAttribute("fill","var(--muted)");val.setAttribute("font-feature-settings",'"tnum"');val.textContent=d[1];});
  noteEl.textContent=`카테고리별 현재 페이지 수(overviews 포함, top-level 폴더, _ 폴더 제외, 총 ${META.wiki.toLocaleString()}). top 20 외 나머지는 '기타' 버킷으로 합산.`;
}

/* ===== VIEW 4: system evolution ===== */
function viewSystem(){
  clear();
  const M={top:64,right:40,bottom:54,left:40},iW=W-M.left-M.right;
  const dates=dateRange(META.start_d,META.end_d);
  const N=dates.length, xs=dt=>{let i=dates.indexOf(dt);if(i<0)i=N-1;return M.left+(i/(N-1))*iW;};
  const bandY=240, bandH=64;
  PHASES.forEach(p=>{const x1=xs(p.s),x2=xs(p.e),w=x2-x1;
    const r=el("rect",{x:x1,y:bandY,width:Math.max(w,4),height:bandH,rx:6,fill:p.color,"fill-opacity":.30,stroke:p.color,"stroke-width":1.2,class:"bar"});
    r.addEventListener("mousemove",e=>showTip(e,`<b>${p.name}</b><br>${p.s.slice(5)} ~ ${p.e.slice(5)}<br>${p.desc}`));
    r.addEventListener("mouseleave",hideTip);
    if(w<110){
      const g=el("text",{x:x1+w/2,y:bandY+bandH/2+6,"text-anchor":"middle"});g.setAttribute("font-size","16");g.setAttribute("font-weight","700");g.setAttribute("fill","var(--ink)");g.textContent=p.name.split(" ")[0];
    } else {
      const nm=el("text",{x:x1+8,y:bandY+24});nm.setAttribute("font-size","13");nm.setAttribute("font-weight","700");nm.setAttribute("fill","var(--ink)");nm.textContent=p.name;
      const ds=el("text",{x:x1+8,y:bandY+44});ds.setAttribute("font-size","10.5");ds.setAttribute("fill","var(--muted)");
      const maxc=Math.round((w-16)/5.4); ds.textContent = p.desc.length>maxc ? p.desc.slice(0,maxc)+"…" : p.desc;
    }
  });
  el("line",{x1:M.left,x2:M.left+iW,y1:bandY+bandH+8,y2:bandY+bandH+8,stroke:"var(--ink)","stroke-width":1,opacity:.4});
  const tickI=[0,Math.round((N-1)/4),Math.round((N-1)/2),Math.round(3*(N-1)/4),N-1];
  [...new Set(tickI)].forEach(i=>{const x=M.left+(i/(N-1))*iW;const tx=el("text",{x,y:bandY+bandH+26,"text-anchor":"middle"});tx.setAttribute("font-size","10.5");tx.setAttribute("fill","var(--muted)");tx.textContent=dates[i].slice(5);});
  SCRIPTS.forEach(s=>{const x=xs(s.date);
    const y0 = s.up ? bandY : bandY+bandH;
    const yEnd = s.up ? bandY-78 : bandY+bandH+82;
    el("line",{x1:x,x2:x,y1:y0,y2:yEnd,stroke:"var(--ink)","stroke-dasharray":"2 3","stroke-width":1,opacity:.45});
    el("circle",{cx:x,cy:yEnd,r:3.5,fill:"var(--ink)"});
    const ta = x>W-260 ? "end" : (x<260?"start":"middle");
    const tx=el("text",{x:x+(ta==="start"?6:ta==="end"?-6:0),y:yEnd+(s.up?-8:16),"text-anchor":ta});
    tx.setAttribute("font-size","10.5");tx.setAttribute("fill","var(--ink)");tx.setAttribute("font-weight","600");tx.textContent=s.date.slice(5);
    const tx2=el("text",{x:x+(ta==="start"?6:ta==="end"?-6:0),y:yEnd+(s.up?-21:30),"text-anchor":ta});
    tx2.setAttribute("font-size","10");tx2.setAttribute("fill","var(--muted)");tx2.textContent=s.label;
  });
  lgItem("var(--c1)","① 부트스트랩");
  lgItem("var(--c2)","② 자가감사");
  lgItem("var(--c4)","③ 출력공장");
  lgItem("var(--c5)","④ 산업화·자동감시");
  noteEl.textContent="시스템 자체의 4단계 탈피(과거 사실 — 정적). 점선·점 = 스크립트 출생 시점(최초 커밋). band/점에 마우스를 올리면 상세.";
}

const views={timeline:viewTimeline,years:viewYears,cats:viewCats,system:viewSystem};
document.querySelectorAll(".tab").forEach(b=>b.addEventListener("click",()=>{
  document.querySelectorAll(".tab").forEach(x=>x.classList.remove("active"));
  b.classList.add("active");hideTip();views[b.dataset.v]();
}));
viewTimeline();
</script>
</body>
</html>
"""


if __name__ == "__main__":
    main()
