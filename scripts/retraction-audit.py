#!/usr/bin/env python3
"""
철회(retraction) 감사 — SIGNAL, 절대 block하지 않는다.

`INGEST.md` Step 0는 철회 논문을 인제스트하지 말라고 하되, 기록해야만 하는 경우
"RETRACTED — do not cite" 형태로 남기는 것을 허용한다. 이 감사는 그렇게 남긴
페이지들이 **인용 사고를 실제로 막는 구조**를 갖췄는지 검사한다.

왜 필요한가 — RAG 누출:
  QMD는 청크 단위로 검색한다. 페이지 맨 위의 경고 콜아웃은 `## Results` 청크가
  단독으로 retrieve될 때 **따라오지 않는다**. 사람이 페이지를 열 때만 작동하는
  경고는 답변 생성 경로(Rule #1·#4가 지키려는 바로 그 경로)를 못 막는다.
  → 경고는 **섹션 제목 안**에 있어야 청크와 함께 이동한다. 이 감사가 그것을 본다.

왜 grep으로는 안 되는가:
  `grep -i retracted`는 교정과의 "canine retraction"(견인)·"molar retraction"에
  걸린다. 실측으로 오탐이 확인됐다. 그래서 기계가 읽는 단일 고리는
  frontmatter의 `retraction_status:` 필드다.

검사 항목 (페이지당):
  A. `retraction_status: RETRACTED` 필드 존재            (기계 판독 고리)
  B. title이 `[RETRACTED]`로 시작                        (제목이 곧 경고)
  C. tags에 `RETRACTED` 포함                             (태그 검색 시 노출)
  D. `## ⚠️ RETRACTION NOTICE` 섹션 존재                  (사람이 페이지 열 때)
  E. 필수 3섹션: Why This Page Exists / What We Can NOT Use /
     What This Paper Does Tell Us                        (근거 공백을 결론으로)
  F. 데이터 섹션 제목이 경고를 운반 — Summary/Results/Methodology/Key* 제목에
     "Withdrawn" 또는 "Do Not Cite" 포함                  ★ RAG 누출 방어선
  G. typed 엣지 격리 — 나가는 `relations:` 엣지 0
  H. typed 엣지 격리 — 다른 페이지가 이 페이지를 `target:`으로 삼지 않음

또한 **역방향**을 검사한다:
  I. `retraction_status` 없이 본문에 강한 철회 표현이 있는 페이지 = 필드 누락 의심

실행: python3 scripts/retraction-audit.py
출력: logs/{YYYY-MM-DD}_retraction.log  (+ 콘솔 요약)
"""

import re
import sys
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
SOURCES = ROOT / "sources"
OUT = ROOT / "logs" / f"{date.today().isoformat()}_retraction.log"

# 두 티어를 **모두** 스캔한다 (2026-07-17 추가).
#
# QMD는 wiki/ 와 sources/ 를 **별개 컬렉션으로** 색인한다. wiki/ 페이지만 고치고
# sources/ 를 놔두면 검색이 sources/ 청크를 그대로 내놓는다 — 실측으로
# `qmd search "HaeNaem"` 결과에 sources/ 페이지가 96% 점수로 잡혔다.
#
# 실제 사고: sources/changrani 는 상단에 철회 경고가 있으면서도 본문
# "Correction note" 줄이 "The paper itself is valid… not a retraction"이라고
# **정반대**를 말하고 있었다(철회 발견 전에 쓰인 줄이 플래그만 위에 달리고
# 방치됨). 맨몸 Results 청크보다 나쁘다 — 능동적으로 틀린 주장이라서.
#
# 티어별로 스키마가 다르므로 검사 항목도 다르다:
#   wiki/    : 전 항목 (title/tags/notice/3섹션/제목경고/엣지 격리)
#   sources/ : title·notice·제목경고만 (tags·relations 필드 자체가 없다)
TIERS = [("wiki", WIKI), ("sources", SOURCES)]

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

# 데이터를 담는 섹션 = 청크로 잘려 나갔을 때 근거로 오독될 수 있는 섹션.
# sources/ 티어는 번호가 붙는다(`## 4. Key Results and Benchmarks`) — 선택적으로 처리.
# `Original ` 접두는 이미 경고를 단 제목(`## 4. Original Key Results (...)`)을 계속
# 검사 대상으로 잡기 위한 것이다(경고가 나중에 지워지면 다시 걸려야 하므로).
DATA_SECTION = re.compile(
    r"^##\s+(?:\d+\.\s*)?(?:Original\s+)?(Summary|Results|Methodology|Key\s+\w+|Findings)\b",
    re.IGNORECASE)
# 그 제목이 반드시 운반해야 하는 경고 ("NOT TO BE CITED" 변형 포함 — panagioti 관례)
HEADING_WARN = re.compile(
    r"withdrawn|do not cite|not to be cited|retracted", re.IGNORECASE)

REQUIRED_SECTIONS = [
    ("Why This Page Exists", re.compile(r"^##\s+Why This Page Exists", re.I | re.M)),
    ("What We Can NOT Use",  re.compile(r"^##\s+What We Can ?NOT Use", re.I | re.M)),
    ("What This Paper Does Tell Us",
     re.compile(r"^##\s+What This Paper Does Tell Us", re.I | re.M)),
]

# 본문에 이게 있으면 철회 페이지일 가능성 — 단어 경계 주의(교정과 retraction 오탐 회피)
SUSPECT = re.compile(
    r"\bRETRACTED\b|\bretraction notice\b|철회된 논문|철회됨", re.IGNORECASE)

# 역방향 검사(I)의 정밀도 장치.
#
# 순진하게 본문 전체를 훑으면 **철회 논문을 링크한 페이지가 전부 걸린다** — 실측 6/6이
# 오탐이었다(Related Papers의 "[[panagioti...]] — RETRACTED, do not cite" 주석,
# 서지분석 논문의 코퍼스 서술 "1 retracted publication" 등). 끌 수 없는 신호는
# 노이즈가 된다(2026-07-17 논쟁 레이더에서 같은 실패를 고쳤다).
#
# → 페이지가 **자기 자신에 대해** 말하는 위치만 본다: 제목 / 섹션 제목 /
#   세줄요약 블록 / 경고 콜아웃. 그리고 [[wikilink]]가 있는 줄은 남 얘기이므로 제외.
SELF_SUMMARY = re.compile(
    r"^##\s*(Three-line Summary|세줄요약)\s*\n(.*?)(?=\n##\s|\Z)", re.DOTALL | re.MULTILINE)
WIKILINK_LINE = re.compile(r"\[\[[^\]]+\]\]")


def self_referential_hit(body):
    """페이지가 **자신을** 철회라고 선언하는 근거만 찾는다. 없으면 None.

    자기 선언 위치는 좁다 — 실측된 철회 페이지 2장 모두 (a) 섹션 제목
    (`## ⚠️ RETRACTION NOTICE`)과 (b) 세줄요약 **첫 줄**에서 선언한다
    ("[RETRACTED] Originally...", "**[철회(Retracted) — 인용 금지.]** 원래...").
    반면 '남의 철회를 언급하는' 페이지는 본문 중간 콜아웃·Related Papers에 쓴다.
    이 차이가 유일하게 신뢰할 수 있는 구분선이다.
    """
    regions = [l for l in body.split("\n") if l.startswith("#")]   # 섹션 제목
    for m in SELF_SUMMARY.finditer(body):
        first = next((l for l in m.group(2).split("\n") if l.strip()), "")
        regions.append(first)                                      # 세줄요약 첫 줄
    for line in regions:
        if WIKILINK_LINE.search(line):        # 다른 페이지를 가리키는 줄 = 남 얘기
            continue
        m = SUSPECT.search(line)
        if m:
            return m.group(0), line.strip()[:90]
    return None


def parse(path):
    txt = path.read_text(encoding="utf-8", errors="replace")
    m = FM_RE.match(txt)
    fm = m.group(1) if m else ""
    body = txt[m.end():] if m else txt
    return fm, body, txt


def field(fm, key):
    m = re.search(rf"^{key}:\s*(.+)$", fm, re.MULTILINE)
    return m.group(1).strip() if m else None


def outgoing_edges(fm):
    rel = re.search(r"^relations:\s*\n((?:[ \t#].*\n?)+)", fm, re.MULTILINE)
    if not rel:
        return []
    out = []
    for item in re.split(r"\n(?=\s*-\s)", rel.group(1)):
        if re.match(r"\s*#", item):        # 주석 처리된 엣지는 엣지가 아니다
            continue
        t = re.search(r"^\s*-\s*type:\s*(\S+)", item)
        g = re.search(r"target:\s*(\S+)", item)
        if t and g:
            out.append((t.group(1), g.group(1).strip().rstrip("/").split("/")[-1]))
    return out


# ── 스캔 ──────────────────────────────────────────────────────────────
pages = {}          # (tier, stem) -> (path, fm, body)
wiki_pages = {}     # stem -> (path, fm, body)   — 엣지 검사용(wiki 티어만)
for tier, root in TIERS:
    if not root.exists():
        continue
    for md in root.rglob("*.md"):
        if md.name.startswith("_") or md.stem == "index":
            continue
        fm, body, _ = parse(md)
        pages[(tier, md.stem)] = (md, fm, body)
        if tier == "wiki":
            wiki_pages[md.stem] = (md, fm, body)

retracted = {k: v for k, v in pages.items()
             if (field(v[1], "retraction_status") or "").upper() == "RETRACTED"}

# 들어오는 엣지 인덱스: target stem -> [(source stem, type)]  — wiki 티어에만 존재
incoming = {}
for stem, (path, fm, body) in wiki_pages.items():
    for typ, tgt in outgoing_edges(fm):
        incoming.setdefault(tgt, []).append((stem, typ))

problems = []   # (relpath, code, message)
for (tier, stem), (path, fm, body) in sorted(retracted.items()):
    rel = str(path.relative_to(ROOT))
    title = field(fm, "title") or ""
    tags = field(fm, "tags") or ""

    if not title.lstrip('"').startswith("[RETRACTED]"):
        problems.append((rel, "B", "title이 [RETRACTED]로 시작하지 않음"))
    if not re.search(r"^##\s+.*RETRACTION NOTICE", body, re.I | re.M):
        problems.append((rel, "D", "## RETRACTION NOTICE 섹션 없음"))

    # C/E/G/H 는 wiki 티어 전용 — sources/ 는 tags·relations 필드 자체가 없고
    # 서사 3섹션은 wiki 페이지의 역할이다(sources 는 논문 요약 티어).
    if tier == "wiki":
        if "RETRACTED" not in tags:
            problems.append((rel, "C", "tags에 RETRACTED 없음"))
        for label, rx in REQUIRED_SECTIONS:
            if not rx.search(body):
                problems.append((rel, "E", f"필수 섹션 없음: {label}"))

    # F — RAG 누출 방어선: 데이터 섹션 제목이 경고를 운반하는가
    for line in body.split("\n"):
        if DATA_SECTION.match(line) and not HEADING_WARN.search(line):
            problems.append((
                rel, "F",
                f"데이터 섹션 제목이 경고를 운반하지 않음 → RAG 청크 누출: 「{line.strip()}」"))

    # G/H — typed 그래프 격리 (wiki 티어 전용; sources 에는 relations 가 없다)
    if tier == "wiki":
        for typ, tgt in outgoing_edges(fm):
            problems.append((rel, "G", f"철회 페이지에 나가는 typed 엣지: {typ} → {tgt}"))
        for src, typ in incoming.get(stem, []):
            problems.append((rel, "H", f"다른 페이지가 철회 페이지를 가리킴: {src} —{typ}→ 여기"))

# I — 필드 누락 의심 (본문은 철회를 말하는데 필드가 없음) — 두 티어 모두
suspects = []
for (tier, stem), (path, fm, body) in sorted(pages.items()):
    if (tier, stem) in retracted:
        continue
    title = field(fm, "title") or ""
    hit = self_referential_hit(body)
    if SUSPECT.search(title):
        suspects.append((str(path.relative_to(ROOT)), "title", title[:90]))
    elif hit:
        suspects.append((str(path.relative_to(ROOT)), hit[0], hit[1]))

# ── 리포트 ────────────────────────────────────────────────────────────
lines = [f"# Retraction Audit — {date.today().isoformat()}", ""]
lines.append(f"RETRACTED pages          : {len(retracted)}")
lines.append(f"구조 문제                : {len(problems)}")
lines.append(f"필드 누락 의심 (참고)    : {len(suspects)}")
lines.append("")

if retracted:
    lines.append("=== retraction_status: RETRACTED 페이지 (wiki/ + sources/ 두 티어) ===")
    for (tier, stem), (path, fm, body) in sorted(retracted.items()):
        n = sum(1 for p in problems if p[0] == str(path.relative_to(ROOT)))
        mark = "✓ 구조 OK" if n == 0 else f"⚠ 문제 {n}건"
        lines.append(f"  {mark:<12} {path.relative_to(ROOT)}")
    lines.append("")

if problems:
    lines.append("=== 구조 문제 (판단 후 수정) ===")
    for rel, code, msg in problems:
        lines.append(f"  [{code}] {rel}")
        lines.append(f"        {msg}")
    lines.append("")

if suspects:
    lines.append("=== (참고) 페이지가 자신을 철회라 말하는데 retraction_status 필드가 없음 ===")
    lines.append("    — 제목·섹션 제목·세줄요약·경고 콜아웃만 검사하며, [[wikilink]]가 있는 줄은")
    lines.append("      '남 얘기'로 보고 제외한다. 그래도 오탐 가능 — 사람이 확인.")
    for rel, kw, ctx in suspects:
        lines.append(f"  '{kw}'  {rel}")
        lines.append(f"        「{ctx}」")
    lines.append("")

OUT.write_text("\n".join(lines), encoding="utf-8")

print(f"🚫  Retraction: {len(retracted)} retracted page(s), "
      f"{len(problems)} structural issue(s), {len(suspects)} field-missing suspect(s)"
      f" {'✓' if not problems else '⚠'}")
print(f"      log → {OUT.relative_to(ROOT)}")

# SIGNAL — 절대 block하지 않는다 (AUDITS.md: 감사는 거울이지 gate가 아니다)
sys.exit(0)
