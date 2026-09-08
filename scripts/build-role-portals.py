#!/usr/bin/env python3
"""
역할별 포털 생성기 — 원장 / 치위생사 / 데스크·코디

각 역할의 관심 카테고리 최신 5개 페이지 + 세줄요약을 긁어
interactives/role-{dentist,hygienist,desk}.html 을 만든다.

실행: python3 scripts/build-role-portals.py
출력: interactives/role-dentist.html
       interactives/role-hygienist.html
       interactives/role-desk.html
"""
import re, subprocess
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
OUT  = ROOT / "interactives"
BASE = "https://ezinternet.github.io/dentopedia"
TODAY = date.today().isoformat()

FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)

def field(fm, name):
    m = re.search(rf'^{name}:\s*["\']?(.*?)["\']?\s*$', fm, re.MULTILINE)
    return m.group(1).strip().strip('"\'') if m else ""

def ko_summary(txt):
    m = re.search(r'^## 세줄요약\s*\n(.+?)(?=\n##\s|\Z)', txt, re.DOTALL|re.MULTILINE)
    if not m:
        return ""
    return re.sub(r'\s+', ' ', m.group(1).strip().split("\n\n")[0]).strip()[:220]

def ev_badge(ev):
    return {"sr+ma":"🟢 SR+MA","sr":"🟢 SR","rct":"🟢 RCT",
            "prospective":"🟡 전향","retrospective":"🟠 후향",
            "synthesis":"🔵 종합"}.get(ev.lower(), "⚪")

def recent_pages(cats, limit=5):
    """각 카테고리에서 git 최신 순 페이지를 뽑아 정보를 리턴."""
    out = []
    seen = set()
    for cat in cats:
        folder = WIKI / cat
        if not folder.exists():
            continue
        files = [f for f in folder.glob("*.md") if not f.name.startswith("index") and f.stem != cat.split("/")[-1]]
        # git mtime 기준 최신
        def mtime(f):
            r = subprocess.run(["git","log","-1","--format=%ct","--",str(f)],
                               cwd=ROOT, capture_output=True, text=True)
            return int(r.stdout.strip() or "0")
        files = sorted(files, key=mtime, reverse=True)[:4]
        for f in files:
            if f.stem in seen:
                continue
            seen.add(f.stem)
            txt = f.read_text(encoding="utf-8", errors="replace")
            m = FM_RE.match(txt)
            fm = m.group(1) if m else ""
            title = field(fm, "title") or f.stem.replace("-", " ").title()
            ev = field(fm, "evidence_level") or field(fm, "confidence")
            ko = ko_summary(txt)
            url = f"{BASE}/{cat}/{f.stem}" if "/" not in cat else f"{BASE}/{cat}/{f.stem}"
            out.append({"title": title[:80], "cat": cat, "ev": ev, "badge": ev_badge(ev),
                        "ko": ko, "url": url, "stem": f.stem})
        if len(out) >= limit:
            break
    return out[:limit]

def overview_recent(n=4):
    """최신 overview n개."""
    files = sorted(
        (f for f in (WIKI / "overviews").glob("*.md")
         if not f.name.startswith("index")),
        key=lambda f: subprocess.run(
            ["git","log","-1","--format=%ct","--",str(f)],
            cwd=ROOT, capture_output=True, text=True
        ).stdout.strip() or "0",
        reverse=True
    )[:n]
    out = []
    for f in files:
        txt = f.read_text(encoding="utf-8", errors="replace")
        m = FM_RE.match(txt)
        fm = m.group(1) if m else ""
        title = field(fm,"title") or f.stem
        ko = ko_summary(txt)
        out.append({"title": title[:80], "ko": ko,
                    "url": f"{BASE}/overviews/{f.stem}", "stem": f.stem})
    return out

# ── 역할 정의 ────────────────────────────────────────────────────────
ROLES = {
    "hygienist": {
        "label": "치위생사", "emoji": "🦷",
        "subtitle": "치주·치간·구강위생·임플란트 유지관리",
        "cats": [
            ("periodontics/non-surgical-instrumentation","치주 기구처치"),
            ("periodontics/oral-hygiene-instruction","구강위생 지도"),
            ("interdental-cleaning","치간 청소"),
            ("implants/peri-implantitis","임플란트 주위염"),
            ("periodontics","치주치료 일반"),
            ("caries","우식 예방"),
        ],
        "links": [
            (f"{BASE}/periodontics", "치주치료 전체"),
            (f"{BASE}/interdental-cleaning", "치간청소 근거"),
            (f"{BASE}/caries", "우식 예방"),
            ("https://ezinternet.github.io/dentopedia", "전체 위키"),
        ],
        "accent": "#1a6e5e",
        "accent_soft": "#ddf3ee",
    },
    "desk": {
        "label": "데스크·코디", "emoji": "📋",
        "subtitle": "환자 안내·동의서·불만 응대",
        "cats": [
            ("practice-management","진료실 운영"),
            ("complaint-management","불만 응대"),
            ("behavioral-dentistry","환자 커뮤니케이션"),
            ("drug/systemic-disease","전신질환 환자 안내"),
        ],
        "links": [
            (f"{BASE}/practice-management", "진료실 운영 근거"),
            (f"{BASE}/complaint-management", "환자 불만 응대"),
            (f"{BASE}/behavioral-dentistry", "환자 소통"),
            ("https://ezinternet.github.io/dentopedia", "전체 위키"),
        ],
        "accent": "#5a3a8e",
        "accent_soft": "#ede7f6",
    },
    "dentist": {
        "label": "원장·치과의사", "emoji": "🔬",
        "subtitle": "임플란트·골재생·근관·종합근거",
        "cats": [
            ("implants","임플란트"),
            ("immediate-implant","즉시식립"),
            ("sinus-lift","상악동거상"),
            ("bone-regeneration","골재생"),
            ("endodontics","근관치료"),
        ],
        "links": [
            (f"{BASE}/overviews", "종합 오버뷰"),
            (f"{BASE}/implants", "임플란트"),
            (f"{BASE}/bone-regeneration", "골재생"),
            ("https://ezinternet.github.io/dentopedia", "전체 위키"),
        ],
        "accent": "#0F6E6E",
        "accent_soft": "#ddf2ee",
    },
}

# ── HTML 템플릿 ───────────────────────────────────────────────────────
def render_portal(role_id, role):
    pages = recent_pages([c for c,_ in role["cats"]], limit=6)
    if role_id == "dentist":
        ovs = overview_recent(4)
    else:
        ovs = []

    cards_html = ""
    for p in pages:
        cat_label = next((lbl for c,lbl in role["cats"] if c==p["cat"]), p["cat"])
        ko_esc = p["ko"].replace("<","&lt;").replace(">","&gt;")
        cards_html += f"""
<a class="page-card" href="{p['url']}" target="_blank">
  <div class="pc-head"><span class="badge">{p['badge']}</span><span class="cat-lbl">{cat_label}</span></div>
  <div class="pc-title">{p['title']}</div>
  {'<div class="pc-ko">' + ko_esc + '</div>' if ko_esc else ''}
</a>"""

    ov_html = ""
    if ovs:
        ov_html = '<h2 class="section-title">최신 종합 근거 (Overview)</h2><div class="ov-list">'
        for ov in ovs:
            ko_esc = ov["ko"].replace("<","&lt;").replace(">","&gt;")
            ov_html += f"""
<a class="ov-card" href="{ov['url']}" target="_blank">
  <div class="ov-title">{ov['title']}</div>
  {'<div class="ov-ko">' + ko_esc + '</div>' if ko_esc else ''}
</a>"""
        ov_html += '</div>'

    links_html = "".join(
        f'<a class="quick-link" href="{url}" target="_blank">{lbl} →</a>'
        for url, lbl in role["links"]
    )

    acc = role["accent"]
    acc_s = role["accent_soft"]

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Dentopedia — {role['label']} 포털</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nanum+Myeongjo:wght@700;800&family=IBM+Plex+Sans+KR:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{{--acc:{acc};--acc-s:{acc_s};--ink:#1B2430;--ink2:#4A5866;--ink3:#8A9AA8;--line:#DCE3E8;--paper:#F5F7F9;--panel:#fff;
  --sans:"IBM Plex Sans KR","Apple SD Gothic Neo","Noto Sans KR",system-ui,sans-serif;
  --serif:"Nanum Myeongjo","Apple Myungjo",Georgia,serif;}}
*{{box-sizing:border-box;margin:0;padding:0;}}
body{{background:var(--paper);color:var(--ink);font-family:var(--sans);font-size:15px;line-height:1.65;-webkit-font-smoothing:antialiased;}}
.page{{max-width:640px;margin:0 auto;padding:0 0 60px;}}
header.hero{{background:var(--acc);color:#fff;padding:28px 24px 22px;}}
.hero-eyebrow{{font-size:11px;letter-spacing:.12em;text-transform:uppercase;opacity:.7;margin-bottom:4px;}}
.hero-role{{font-family:var(--serif);font-size:28px;font-weight:800;line-height:1.2;margin-bottom:4px;}}
.hero-sub{{font-size:14px;opacity:.8;}}
.hero-date{{font-size:12px;opacity:.55;margin-top:6px;}}
.quick-links{{display:flex;gap:8px;flex-wrap:wrap;padding:16px 20px;background:var(--acc-s);border-bottom:1px solid var(--line);}}
.quick-link{{font-size:13px;color:var(--acc);background:var(--panel);border:1px solid var(--acc);padding:5px 12px;text-decoration:none;border-radius:3px;font-weight:500;white-space:nowrap;}}
.quick-link:hover{{background:var(--acc);color:#fff;}}
.section-title{{font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink3);padding:20px 20px 8px;font-weight:600;}}
.cards{{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--line);}}
@media(max-width:480px){{.cards{{grid-template-columns:1fr;}}}}
.page-card{{background:var(--panel);padding:16px 18px 14px;text-decoration:none;color:inherit;display:block;}}
.page-card:hover{{background:#f0f4f8;}}
.pc-head{{display:flex;gap:6px;align-items:center;margin-bottom:7px;flex-wrap:wrap;}}
.badge{{font-size:11px;font-weight:600;padding:2px 7px;border-radius:3px;background:var(--acc);color:#fff;}}
.cat-lbl{{font-size:11px;color:var(--acc);background:var(--acc-s);padding:2px 7px;border-radius:3px;}}
.pc-title{{font-size:14px;font-weight:600;line-height:1.45;margin-bottom:6px;color:var(--ink);}}
.pc-ko{{font-size:13px;color:var(--ink2);line-height:1.6;}}
.ov-list{{display:flex;flex-direction:column;gap:1px;background:var(--line);}}
.ov-card{{background:var(--panel);padding:14px 20px 12px;text-decoration:none;color:inherit;border-left:3px solid var(--acc);display:block;}}
.ov-card:hover{{background:#f0f4f8;}}
.ov-title{{font-size:14.5px;font-weight:600;color:var(--ink);margin-bottom:5px;line-height:1.4;}}
.ov-ko{{font-size:13px;color:var(--ink2);line-height:1.6;}}
.footer{{padding:20px 20px 0;font-size:12px;color:var(--ink3);}}
.footer a{{color:var(--acc);}}
</style>
</head>
<body>
<div class="page">
<header class="hero">
  <div class="hero-eyebrow">Dentopedia 근거 위키</div>
  <div class="hero-role">{role['emoji']} {role['label']}</div>
  <div class="hero-sub">{role['subtitle']}</div>
  <div class="hero-date">업데이트 {TODAY}</div>
</header>
<div class="quick-links">{links_html}</div>
<h2 class="section-title">최신 근거 — 내 분야</h2>
<div class="cards">{cards_html}</div>
{ov_html}
<div class="footer">자동 생성 {TODAY} · <a href="{BASE}" target="_blank">전체 위키 열기</a></div>
</div>
</body>
</html>"""

for role_id, role in ROLES.items():
    html = render_portal(role_id, role)
    out = OUT / f"role-{role_id}.html"
    out.write_text(html, encoding="utf-8")
    print(f"✓ {out.relative_to(ROOT)}")
