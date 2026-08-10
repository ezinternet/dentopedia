#!/usr/bin/env python3
"""
자가테스트 퀴즈 HTML 생성기 — 스펙(JSON) → 완성 self-contained HTML.

hygienist-education 스킬이 위키 근거로 문항 데이터(JSON 스펙)만 저작하면, 이 스크립트가
검증된 HTML/CSS/JS 골격에 채워 넣어 interactives/{date}_{slug}-quiz.html 를 생성한다.
LLM은 데이터만 만들고 구조는 스크립트가 보장 → 항상 유효한 퀴즈, 템플릿은 여기 한 곳.

스펙 스키마 (interactives/quiz-specs/{slug}.json):
{
  "slug": "local-anesthesia",              # 파일명 = {date}_{slug}-quiz.html
  "date": "2026-07-01",
  "title": "국소마취 자가테스트",
  "emoji": "💉",                            # 선택 (기본 🦷)
  "category": "drug",                       # interactives-index 버킷 키
  "agenda": "agenda/2026-07-01_....md",     # Hard rule — 필수
  "source_wiki": ["wiki/drug/.../x.md", ...],
  "overview": {"path": "drug/.../overview", "label": "국소마취 종합"},  # 선택 (푸터 링크)
  "questions": [
    {"q":"질문","opts":["A","B","C","D"],"ans":1,"rat":"해설",
     "cite":"drug/local-anesthesia/foo-2025-..."}   # cite = wiki 경로(category/stem)
  ]
}

실행: python3 scripts/build-quiz.py --spec interactives/quiz-specs/{slug}.json
출력: interactives/{date}_{slug}-quiz.html  (덮어쓰기)
"""

import json, argparse, sys, html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ap = argparse.ArgumentParser()
ap.add_argument("--spec", required=True, help="퀴즈 스펙 JSON 경로")
args = ap.parse_args()

spec = json.loads(Path(args.spec).read_text(encoding="utf-8"))

REQUIRED = ["slug", "date", "title", "category", "agenda", "questions"]
missing = [k for k in REQUIRED if not spec.get(k)]
if missing:
    sys.exit(f"❌ 스펙 필수 키 누락: {missing}")

qs = spec["questions"]
for i, q in enumerate(qs):
    for k in ("q", "opts", "ans", "cite"):
        if k not in q:
            sys.exit(f"❌ 문항 {i+1}에 '{k}' 없음")
    if not (0 <= q["ans"] < len(q["opts"])):
        sys.exit(f"❌ 문항 {i+1}: ans={q['ans']}가 opts 범위를 벗어남")

# agenda 파일 존재 확인 (Hard rule — 없으면 경고만, 생성은 진행)
if not (ROOT / spec["agenda"]).exists():
    print(f"⚠ agenda 파일 없음: {spec['agenda']} — Hard rule상 먼저 작성 권장")

emoji = spec.get("emoji", "🦷")
N = len(qs)
esc = lambda s: html.escape(str(s))
sw_block = "\n".join(f"  - {p}" for p in spec.get("source_wiki", [])) or "  - wiki/"
ov = spec.get("overview")
footer_link = (f'출처: <a href="/dentopedia/{esc(ov["path"])}" target="_blank">{esc(ov["label"])}</a> · '
               if ov else "")
questions_json = json.dumps(qs, ensure_ascii=False, indent=2)
out_name = f"{spec['date']}_{spec['slug']}-quiz.html"
OUT = ROOT / "interactives" / out_name

HTML = f"""<!--
---
title: "{esc(spec['title'])}"
type: interactive
date: {spec['date']}
status: done
category: {esc(spec['category'])}
agenda: {esc(spec['agenda'])}
source_wiki:
{sw_block}
note: "hygienist-education 스킬 산출 퀴즈. 문항은 위키 근거로 LLM 저작(자동생성 아님) — scripts/build-quiz.py가 스펙(interactives/quiz-specs/{spec['slug']}.json)에서 HTML 생성. source_wiki가 도구보다 최신이면 interactive-staleness가 STALE 신호."
---
-->
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(spec['title'])}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&display=swap" rel="stylesheet">
<style>
  :root{{
    --bg:#0e1116; --panel:#161b22; --panel2:#1c232d; --line:#2b333d;
    --txt:#e6edf3; --dim:#9aa7b4; --ok:#3fb950; --no:#ff5d5d; --accent:#4aa3ff;
    --chip:#243040;
  }}
  *{{box-sizing:border-box;}}
  body{{margin:0;background:var(--bg);color:var(--txt);
    font-family:'Noto Sans KR',system-ui,sans-serif;line-height:1.55;}}
  .wrap{{max-width:760px;margin:0 auto;padding:26px 18px 80px;}}
  h1{{font-weight:900;font-size:1.6rem;margin:.2em 0 .1em;}}
  .sub{{color:var(--dim);font-size:.92rem;margin-bottom:16px;}}
  .bar{{height:8px;background:var(--panel);border-radius:20px;overflow:hidden;margin:14px 0 22px;}}
  .bar > i{{display:block;height:100%;width:0;background:var(--accent);transition:width .3s;}}
  .q{{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:18px;margin-bottom:16px;}}
  .qn{{font-size:.78rem;color:var(--dim);margin-bottom:4px;}}
  .qt{{font-weight:700;margin-bottom:12px;}}
  .opt{{display:block;width:100%;text-align:left;background:var(--panel2);
    border:1px solid var(--line);color:var(--txt);border-radius:9px;
    padding:11px 13px;margin:7px 0;cursor:pointer;font-size:.93rem;
    font-family:inherit;transition:border-color .15s,background .15s;}}
  .opt:hover:not(:disabled){{border-color:var(--accent);}}
  .opt:disabled{{cursor:default;}}
  .opt.correct{{border-color:var(--ok);background:rgba(63,185,80,.12);}}
  .opt.wrong{{border-color:var(--no);background:rgba(255,93,93,.12);}}
  .rat{{margin-top:10px;font-size:.86rem;color:var(--dim);
    border-left:3px solid var(--line);padding:8px 12px;display:none;}}
  .rat.show{{display:block;}}
  .rat b{{color:var(--txt);}}
  .rat a{{color:var(--accent);text-decoration:none;}}
  .score{{position:sticky;bottom:0;background:var(--panel);border:1px solid var(--line);
    border-radius:12px;padding:14px 18px;text-align:center;font-weight:700;margin-top:8px;}}
  .score .big{{font-size:1.5rem;color:var(--accent);}}
  .reset{{margin-top:12px;background:var(--chip);border:1px solid var(--line);
    color:var(--txt);border-radius:8px;padding:9px 16px;cursor:pointer;font-family:inherit;}}
  .foot{{margin-top:26px;color:var(--dim);font-size:.78rem;text-align:center;}}
  .foot a{{color:var(--accent);text-decoration:none;}}
</style>
</head>
<body>
<div class="wrap">
  <h1>{emoji} {esc(spec['title'])}</h1>
  <div class="sub">치위생사 교육 · {N}문항 · 답을 고르면 정답·해설·근거가 열립니다.</div>
  <div class="bar"><i id="bar"></i></div>
  <div id="quiz"></div>
  <div class="score" id="score">진행: <span id="done">0</span>/{N} · 정답 <span class="big" id="pts">0</span></div>
  <button class="reset" onclick="location.reload()">↻ 다시 풀기</button>
  <div class="foot">{footer_link}교육용 요약 — 개별 판단은 위키 원문·원장 확인</div>
</div>
<script>
// 문항 = LLM이 위키 근거로 저작. 스펙: interactives/quiz-specs/{spec['slug']}.json
// cite = 위키 경로(category/stem) → 링크는 /dentopedia/{{cite}} 로 조립.
const QUESTIONS = {questions_json};
const SITE_BASE="/dentopedia";
let done=0, pts=0;
const quiz=document.getElementById('quiz');
QUESTIONS.forEach((item,i)=>{{
  const card=document.createElement('div'); card.className='q';
  const cite=`<a href="${{SITE_BASE}}/${{item.cite}}" target="_blank">근거 보기 →</a>`;
  card.innerHTML=`<div class="qn">Q${{i+1}}</div><div class="qt">${{item.q}}</div>`;
  item.opts.forEach((o,j)=>{{
    const b=document.createElement('button'); b.className='opt'; b.textContent=o;
    b.onclick=()=>answer(card,i,j,b);
    card.appendChild(b);
  }});
  const r=document.createElement('div'); r.className='rat';
  r.innerHTML=`<b>해설.</b> ${{item.rat||''}} ${{cite}}`;
  card.appendChild(r);
  quiz.appendChild(card);
}});
function answer(card,i,pick,btn){{
  if(card.dataset.answered) return;
  card.dataset.answered="1";
  const item=QUESTIONS[i];
  card.querySelectorAll('.opt').forEach((b,j)=>{{ b.disabled=true;
    if(j===item.ans) b.classList.add('correct');
    else if(j===pick) b.classList.add('wrong'); }});
  if(pick===item.ans) pts++;
  done++;
  card.querySelector('.rat').classList.add('show');
  document.getElementById('done').textContent=done;
  document.getElementById('pts').textContent=pts;
  document.getElementById('bar').style.width=(done/QUESTIONS.length*100)+'%';
}}
</script>
</body>
</html>"""

OUT.write_text(HTML, encoding="utf-8")
print(f"✓ interactives/{out_name}  ({N}문항 · category:{spec['category']})")
