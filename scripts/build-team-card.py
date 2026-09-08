#!/usr/bin/env python3
"""
주간 팀 카드 생성기 — build-weekly-digest.py 이후 실행.

최신 weekly-digest.md에서 ⭐ 고근거 항목 최대 4개를 뽑아,
모바일 친화 HTML 카드(인트로 + 근거 카드 3개 + 퀴즈 1문항)를 생성한다.

출력: interactives/YYYY-MM-DD_team-weekly-card.html
실행: python3 scripts/build-team-card.py [--days N]
"""

import re, argparse, sys
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent.parent
LOGS = ROOT / "logs"
OUT_DIR = ROOT / "interactives"
QUARTZ_BASE = "https://ezinternet.github.io/dentopedia"

ap = argparse.ArgumentParser()
ap.add_argument("--days", type=int, default=7)
ap.add_argument("--digest", type=Path, default=None, help="specific digest file to parse")
args = ap.parse_args()

today = date.today()

# ── 최신 digest 찾기 ──────────────────────────────────────────────────
if args.digest:
    digest_path = args.digest
else:
    digests = sorted(LOGS.glob("*_weekly-digest.md"), reverse=True)
    if not digests:
        print("ERROR: no weekly-digest.md found in logs/", file=sys.stderr)
        sys.exit(1)
    digest_path = digests[0]

text = digest_path.read_text(encoding="utf-8")
digest_date = digest_path.stem.split("_")[0]

# ── header: period + counts ───────────────────────────────────────────
header_m = re.search(r"\*\*(.+?)\*\*.*신규\s*\*\*(\d+)편\*\*.*누적\s*(\d+)편", text)
period = header_m.group(1) if header_m else f"최근 {args.days}일"
new_count = header_m.group(2) if header_m else "?"
total_count = header_m.group(3) if header_m else "?"

# ── ⭐ 주목할 새 근거 파싱 ─────────────────────────────────────────────
STAR_RE = re.compile(
    r"-\s+\*\*(.+?)\*\*\s+\((🟢 [^\)]+)\)\s+`([^`]+)`\s*\n"
    r"\s+>\s*(.+?)(?=\n-\s+\*\*|\n##|\Z)",
    re.DOTALL
)

items = []
star_block = re.search(r"##\s+⭐ 주목할 새 근거.*?\n(.*?)(?=\n##\s|\Z)", text, re.DOTALL)
if star_block:
    for m in STAR_RE.finditer(star_block.group(1)):
        title = m.group(1).strip()
        badge = m.group(2).strip()
        cat = m.group(3).strip()
        ko_raw = m.group(4).strip()
        ko = re.sub(r"\s+", " ", ko_raw)[:280]
        # 카테고리 → 한국어
        cat_ko = {
            "bone-regeneration": "골재생", "bone-regeneration/ridge-preservation": "치조제보존",
            "digital-workflow": "디지털워크플로", "drug/analgesics": "진통소염제",
            "drug/antibiotics": "항생제", "drug/systemic-disease": "전신질환",
            "immediate-implant": "즉시식립", "implants": "임플란트",
            "implants/peri-implantitis": "주위염", "implants/isq": "ISQ안정성",
            "oral-surgery": "구강외과", "periodontics": "치주치료",
            "periodontics/non-surgical-instrumentation": "치주기구처치",
            "orthodontics": "교정", "sinus-lift": "상악동거상",
            "sinus-lift/lateral": "측방거상", "sinus-lift/transcrestal": "치조정접근거상",
        }.get(cat, cat.replace("/", " › ").replace("-", " "))
        items.append({"title": title, "badge": badge, "cat": cat, "cat_ko": cat_ko, "ko": ko})
        if len(items) >= 4:
            break

# ── 🔴 판도를 바꾼 근거 — 첫 1개를 퀴즈 소재로 ───────────────────────
RED_RE = re.compile(
    r"-\s+\*\*(.+?)\*\*\s+\((🟢 [^\)]+)\)\s*\n"
    r"(?:\s+→.+\n)*"
    r"\s+>\s*(.+?)(?=\n-\s+\*\*|\n##|\Z)",
    re.DOTALL
)
quiz_title, quiz_q, quiz_hint = "", "", ""
red_block = re.search(r"##\s+🔴 판도를 바꾼 근거.*?\n(.*?)(?=\n##\s|\Z)", text, re.DOTALL)
if red_block and items:
    # 퀴즈는 ⭐ 1번 항목 기반
    first = items[0]
    quiz_title = first["title"][:60] + "…"
    # 세줄요약에서 핵심 수치 추출해 퀴즈 만들기
    ko = first["ko"]
    pct_m = re.search(r"(\d[\d\.]+%|\d+\s*(?:mm|Ncm|ISQ))", ko)
    if pct_m:
        quiz_q = f"{first['cat_ko']} 분야에서 이번 주 핵심 수치는? (힌트: {pct_m.group(0)[:30]})"
        quiz_hint = f"근거: {first['badge']} | {ko[:120]}…"
    else:
        quiz_q = f"{first['cat_ko']} 신규 근거의 핵심 임상 결론은 무엇인가요?"
        quiz_hint = ko[:120] + "…"

if not items:
    print("WARNING: ⭐ 항목을 파싱하지 못했습니다.", file=sys.stderr)

# ── HTML 생성 ────────────────────────────────────────────────────────
BADGE_COLOR = {"🟢 SR+MA": "#1a7a4a", "🟢 SR": "#2a8a5a", "🟢 RCT": "#3a9a6a"}

def badge_style(b):
    col = BADGE_COLOR.get(b, "#5a6a7a")
    return f'background:{col};color:#fff;'

item_cards = ""
for i, it in enumerate(items[:3], 1):
    short_title = it["title"][:90] + ("…" if len(it["title"]) > 90 else "")
    stem = it["cat"].replace("/", "-")
    ko_escaped = it["ko"].replace("<", "&lt;").replace(">", "&gt;")
    bstyle = badge_style(it["badge"])
    item_cards += f"""
<article class="card" style="--n:{i}">
  <header class="card-head">
    <span class="chip" style="{bstyle}">{it['badge']}</span>
    <span class="cat-chip">{it['cat_ko']}</span>
  </header>
  <h3 class="card-title">{short_title}</h3>
  <p class="card-ko">{ko_escaped}</p>
  <a class="card-link" href="{QUARTZ_BASE}/{it['cat']}" target="_blank">위키에서 더 보기 →</a>
</article>"""

quiz_html = ""
if quiz_q:
    quiz_hint_esc = quiz_hint.replace("<", "&lt;").replace(">", "&gt;")
    quiz_title_esc = quiz_title.replace("<", "&lt;").replace(">", "&gt;")
    quiz_html = f"""
<section class="quiz-box">
  <div class="quiz-label">📝 이번 주 1문항</div>
  <p class="quiz-q">{quiz_q}</p>
  <details class="quiz-details">
    <summary>정답 보기</summary>
    <p class="quiz-ans">{quiz_hint_esc}</p>
  </details>
  <p class="quiz-source">출처: {quiz_title_esc}</p>
</section>"""

html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>이번 주 핵심 근거 — {digest_date}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nanum+Myeongjo:wght@700;800&family=IBM+Plex+Sans+KR:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root {{
  --paper: #F5F7F9; --panel: #fff; --ink: #1B2430; --ink2: #4A5866; --ink3: #8A9AA8;
  --teal: #0F6E6E; --teal-s: #DDF2EE; --line: #DCE3E8;
  --sans: "IBM Plex Sans KR","Apple SD Gothic Neo","Noto Sans KR",system-ui,sans-serif;
  --serif: "Nanum Myeongjo","Apple Myungjo",Georgia,serif;
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ background: var(--paper); color: var(--ink); font-family: var(--sans); font-size: 15px; line-height: 1.65; -webkit-font-smoothing: antialiased; }}
.page {{ max-width: 440px; margin: 0 auto; padding: 24px 16px 48px; }}
header.top {{ background: var(--teal); color: #fff; padding: 20px 20px 16px; margin-bottom: 20px; }}
.top-eyebrow {{ font-size: 11px; letter-spacing: .1em; text-transform: uppercase; opacity: .75; margin-bottom: 4px; }}
.top-title {{ font-family: var(--serif); font-size: 22px; font-weight: 800; line-height: 1.2; margin-bottom: 6px; }}
.top-meta {{ font-size: 12.5px; opacity: .8; }}
.top-meta strong {{ opacity: 1; font-weight: 600; }}
.card {{ background: var(--panel); border: 1px solid var(--line); padding: 16px 18px 14px; margin-bottom: 12px; }}
.card-head {{ display: flex; gap: 6px; align-items: center; margin-bottom: 8px; flex-wrap: wrap; }}
.chip {{ font-size: 11px; padding: 2px 8px; border-radius: 3px; font-weight: 600; }}
.cat-chip {{ font-size: 11px; color: var(--teal); background: var(--teal-s); padding: 2px 8px; border-radius: 3px; }}
.card-title {{ font-size: 14px; font-weight: 600; line-height: 1.45; margin-bottom: 8px; color: var(--ink); }}
.card-ko {{ font-size: 13.5px; color: var(--ink2); line-height: 1.65; margin-bottom: 10px; }}
.card-link {{ font-size: 12px; color: var(--teal); text-decoration: none; }}
.quiz-box {{ background: var(--panel); border-left: 3px solid var(--teal); padding: 16px 18px; margin-top: 8px; }}
.quiz-label {{ font-size: 12px; font-weight: 600; color: var(--teal); letter-spacing: .06em; text-transform: uppercase; margin-bottom: 8px; }}
.quiz-q {{ font-size: 15px; font-weight: 600; color: var(--ink); margin-bottom: 10px; line-height: 1.5; }}
.quiz-details summary {{ font-size: 13px; color: var(--teal); cursor: pointer; padding: 4px 0; }}
.quiz-ans {{ font-size: 13px; color: var(--ink2); margin-top: 8px; line-height: 1.65; }}
.quiz-source {{ font-size: 11.5px; color: var(--ink3); margin-top: 8px; border-top: 1px solid var(--line); padding-top: 6px; }}
.footer {{ margin-top: 24px; font-size: 11.5px; color: var(--ink3); text-align: center; }}
.footer a {{ color: var(--teal); }}
</style>
</head>
<body>
<div class="page">
<header class="top">
  <div class="top-eyebrow">Dentopedia · 주간 팀 브리핑</div>
  <div class="top-title">이번 주 핵심 근거</div>
  <div class="top-meta">{period} &ensp;·&ensp; 신규 <strong>{new_count}편</strong> &ensp;·&ensp; 누적 <strong>{total_count}편</strong></div>
</header>
{item_cards}
{quiz_html}
<div class="footer">
  <a href="{QUARTZ_BASE}" target="_blank">전체 위키 열기</a> &ensp;·&ensp; 자동 생성 {today.isoformat()}
</div>
</div>
</body>
</html>"""

out = OUT_DIR / f"{today.isoformat()}_team-weekly-card.html"
out.write_text(html, encoding="utf-8")
print(f"✓ {out.relative_to(ROOT)}")
