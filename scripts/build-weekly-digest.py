#!/usr/bin/env python3
"""
주간 근거 다이제스트 생성기 — "이번 주 새 근거 + 이게 뒤집은 프로토콜".

git 이력으로 창(window, 기본 7일) 안에 위키에 **새로 추가된** 페이지와, 창 안에
**superseded_by 배너가 달린**(=기존 프로토콜이 뒤집힌) 페이지를 뽑아, 한줄요약(한국어)
· confidence · supersede/충돌 관계를 담은 **단톡방에 그대로 던질 수 있는 마크다운**을
생성한다. 복리로 쌓이는 지식 성장을 눈에 보이게 만드는 것.

볼륨이 커도(주당 수백 편) 큐레이션한다:
  1. 🔴 판도를 바꾼 근거 — supersede / 정면충돌 (희소·고가치, 전체 나열)
  2. ⭐ 주목할 새 근거 — 고근거등급(sr+ma/sr/rct)만, 한줄요약 포함 (상한 있음)
  3. 📄 카테고리별 신규 — 카운트 표 (전량 나열 안 함)
  4. 📈 성장 지표

실행: python3 scripts/build-weekly-digest.py [--days N]
출력: logs/{YYYY-MM-DD}_weekly-digest.md  (+ 콘솔)
"""

import re, subprocess, sys, argparse
from pathlib import Path
from datetime import date, timedelta
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"

ap = argparse.ArgumentParser()
ap.add_argument("--days", type=int, default=7)
args = ap.parse_args()
DAYS = args.days

today = date.today()
start = today - timedelta(days=DAYS)
SINCE = f"{DAYS} days ago"
OUT = ROOT / "logs" / f"{today.isoformat()}_weekly-digest.md"

HIGH_EV = {"sr+ma", "sr", "rct"}
CONF_BADGE = {"sr+ma": "🟢 SR+MA", "sr": "🟢 SR", "rct": "🟢 RCT",
              "prospective": "🟡 전향", "retrospective": "🟠 후향",
              "cross-sectional": "🟠 단면", "narrative-review": "⚪ 서술리뷰"}

def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True,
                          text=True).stdout

# ── 창 안 추가된 페이지 경로 ─────────────────────────────────────────
added = git("log", f"--since={SINCE}", "--diff-filter=A", "--name-only",
            "--pretty=format:", "--", "wiki/*.md").splitlines()
added = sorted({p for p in added
                if p.endswith(".md") and p.startswith("wiki/")
                and "index.md" not in p and "category-map" not in p
                and (ROOT / p).exists()})

# ── 창 안 superseded_by 배너가 달린 페이지 (git diff 스캔) ────────────
sup_added = set()
diff = git("log", f"--since={SINCE}", "--diff-filter=M", "-p",
           "--", "wiki/*.md")
cur = None
for line in diff.splitlines():
    if line.startswith("+++ b/"):
        cur = line[6:]
    elif line.startswith("+superseded_by:") and cur:
        sup_added.add(cur)

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

def parse(relpath):
    txt = (ROOT / relpath).read_text(encoding="utf-8", errors="replace")
    m = FM_RE.match(txt)
    fm = m.group(1) if m else ""
    body = txt[m.end():] if m else txt
    def f(name):
        r = re.search(rf"^{name}:\s*(.+)$", fm, re.MULTILINE)
        return r.group(1).strip().strip('"').strip("'") if r else ""
    # relations contradicts/refines targets
    conflicts = []
    rel = re.search(r"^relations:\s*\n((?:[ \t]+.*\n?)+)", fm, re.MULTILINE)
    if rel:
        for item in re.split(r"\n(?=\s*-\s)", rel.group(1)):
            t = re.search(r"type:\s*(\S+)", item)
            g = re.search(r"target:\s*(\S+)", item)
            if t and g and t.group(1) in ("contradicts", "refines"):
                conflicts.append((t.group(1), g.group(1).rstrip("/").split("/")[-1]))
    ko = ""
    s = re.search(r"^##\s*한줄요약\s*\n(.+?)(?=\n##\s|\Z)", body, re.DOTALL | re.MULTILINE)
    if s:
        ko = re.sub(r"\s+", " ", s.group(1).strip().split("\n\n")[0]).strip()
    cat = f("category").strip("[]").split(",")[0].strip()
    return {
        "stem": Path(relpath).stem, "cat": cat,
        "title": f("title"), "year": f("year"),
        "conf": f("confidence"),
        "superseded_by": f("superseded_by"),
        "conflicts": conflicts, "ko": ko,
    }

pages = [parse(p) for p in added]

# ── 판도를 바꾼 근거: superseded_by 달린 옛 페이지 + 충돌/대체 선언한 새 페이지 ──
game_changers = []
for p in sup_added:
    if (ROOT / p).exists():
        d = parse(p); d["_kind"] = "superseded"; game_changers.append(d)
for d in pages:
    if d["superseded_by"] or d["conflicts"]:
        d["_kind"] = "new-impact"; game_changers.append(d)

# ── 카테고리별 신규 카운트 + 고근거 목록 ─────────────────────────────
by_cat = defaultdict(list)
for d in pages:
    by_cat[d["cat"] or "(미분류)"].append(d)
high = [d for d in pages if d["conf"] in HIGH_EV]
high.sort(key=lambda d: (d["cat"], d["stem"]))

# 전체 성장 지표
all_pages = [x for x in WIKI.rglob("*.md")
             if x.name not in ("index.md",) and not x.name.startswith("_")]
total = len(all_pages)
n_ov = len(list((WIKI / "overviews").glob("*.md")))

# ── 마크다운 렌더 ────────────────────────────────────────────────────
L = []
L.append(f"# 🦷 이번 주 새 근거 다이제스트")
L.append("")
L.append(f"**{start.isoformat()} ~ {today.isoformat()}** (최근 {DAYS}일)  ·  "
         f"신규 **{len(pages)}편** · 누적 {total}편 / overview {n_ov}편")
L.append("")

L.append("## 🔴 판도를 바꾼 근거 (뒤집음 · 정면충돌)")
L.append("")
if game_changers:
    seen = set()
    for d in game_changers:
        if d["stem"] in seen: continue
        seen.add(d["stem"])
        badge = CONF_BADGE.get(d["conf"], d["conf"])
        L.append(f"- **{d['title'] or d['stem']}** ({badge})")
        if d.get("_kind") == "superseded" and d["superseded_by"]:
            L.append(f"  → ⚠️ 이 페이지가 **뒤집힘**: `{d['superseded_by']}`로 대체")
        for ctype, tgt in d["conflicts"]:
            tag = "정면충돌" if ctype == "contradicts" else "조건부 반박"
            L.append(f"  → {tag}: `{tgt}`")
        if d["ko"]:
            L.append(f"  > {d['ko'][:180]}")
else:
    L.append("_이번 주 supersede·신규 충돌 없음._")
L.append("")

L.append("## ⭐ 주목할 새 근거 — 고근거등급 (SR+MA · SR · RCT)")
L.append("")
CAP = 30
if high:
    for d in high[:CAP]:
        badge = CONF_BADGE.get(d["conf"], d["conf"])
        L.append(f"- **{d['title'] or d['stem']}** ({badge}) `{d['cat']}`")
        if d["ko"]:
            L.append(f"  > {d['ko'][:180]}")
    if len(high) > CAP:
        L.append(f"\n_…외 {len(high)-CAP}편 (전체는 위키 참조)_")
else:
    L.append("_이번 주 고근거등급 신규 없음._")
L.append("")

L.append("## 📄 카테고리별 신규 (카운트)")
L.append("")
L.append("| 카테고리 | 신규 |")
L.append("|---|---|")
for cat in sorted(by_cat, key=lambda c: -len(by_cat[c])):
    L.append(f"| {cat} | {len(by_cat[cat])} |")
L.append("")

L.append("## 📈 성장")
L.append("")
L.append(f"- 이번 주 **+{len(pages)}편** (누적 {total}편)")
L.append(f"- overview {n_ov}편 · 고근거 신규 {len(high)}편 · 판도전환 {len(set(d['stem'] for d in game_changers))}건")
L.append("")
L.append(f"<sub>자동생성 · scripts/build-weekly-digest.py --days {DAYS} · {today.isoformat()}</sub>")

OUT.write_text("\n".join(L), encoding="utf-8")
print(f"✓ {OUT.relative_to(ROOT)}")
print(f"  신규 {len(pages)}편 · 고근거 {len(high)}편 · 판도전환 {len(set(d['stem'] for d in game_changers))}건")
