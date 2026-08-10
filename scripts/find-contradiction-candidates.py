#!/usr/bin/env python3
"""
논쟁 레이더 백필 후보 finder (SIGNAL — 엣지를 자동으로 쓰지 않는다).

위키 본문(및 매칭되는 sources/의 Why Ingested)에서 "명시적 충돌 표현"을 스캔해,
아직 relations: 타입 엣지가 없는 논쟁 후보를 등급별로 뽑는다.
사람/LLM이 이 목록을 읽고 판단해 실제 엣지를 단다 (Rule #1·품질 기준 준수 —
기계가 충돌을 확정하지 않는다).

Tier 1 (actionable): 충돌 표현 + 키워드에 가장 가까운 [[wikilink]]로 대상이 지목됨
                      + 그 쌍에 **어떤 타입의 relations 엣지도 없음**.
                      → 두 페이지를 읽고 판단 후 relations 엣지를 달 수 있는 후보.
Tier 2 (review):      충돌 표현은 있으나 대상이 불명확하거나(링크 없음 / 키워드에서
                      너무 멂 / 동일 줄 비최근접) SOFT 신호. → 대상 식별 필요.

**type_hint(충돌 유형)를 그대로 엣지로 옮기지 마라.** 표현 매칭 기반 근사치다.
2026-07-17 전수 검토: contradicts 계열로 지목된 122건 중 실제 contradicts는 1건.
흔한 실제 유형은 refines(신형 SR/MA가 구형 술식을 정량 순위)·extends(다른 인구집단).

각 카드는 한국어로 (a) 충돌 유형 뜻, (b) 근거 문장, (c) 양쪽 페이지의 ## 세줄요약을
함께 보여준다 — 페이지를 열지 않고도 두 논문이 각각 뭐라고 주장하는지 한글로 파악.

실행: python3 scripts/find-contradiction-candidates.py
출력: logs/{YYYY-MM-DD}_contradiction-candidates.md  (+ 콘솔 요약)
"""

import re
import sys
import hashlib
from pathlib import Path
from datetime import date
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
SOURCES = ROOT / "sources"
OUT = ROOT / "logs" / f"{date.today().isoformat()}_contradiction-candidates.md"

# 명시적 충돌 신호. HIGH = 오탐 적음(자동 write 후보), SOFT = 노이즈 많음(review only).
#
# 단어 경계 주의 (2026-07-17 수정):
#   - 한글은 \b가 무용하다. 모든 한글 음절이 \w라 음절 사이에 경계가 생기지 않아
#     '반론'이 '일반론'에, '상반'이 '상반신/상반기'에 부분 매칭됐다.
#     → 앞 경계는 (?<![가-힣]) 로, 뒤 경계는 어미를 명시해 만든다.
#   - '배치되'는 제거했다. 배치(背馳, 어긋남)와 배치(配置, 식립·배열)가 동음이의어라
#     정규식으로 구분 불가능하고, 치과 위키에서는 후자가 압도적이다.
HIGH = re.compile(
    r"\bcontradict|\bcounterpoint|\bcounter to\b|\bcontrary to\b|\bin contrast to\b|"
    r"\bat odds\b|\bconflicting (?:evidence|result|finding)|\brefut|\boverturn|"
    r"(?<![가-힣])반박|(?<![가-힣])상충|(?<![가-힣])상반[되된적]|(?<![가-힣])반론|"
    r"(?<![가-힣])대비되는|(?<![가-힣])뒤집", re.IGNORECASE)
SOFT = re.compile(
    r"\bunlike\b|\bwhereas\b|\bchallenges the\b|\bdisagree|\binconsistent with\b|"
    r"\bhowever,? (?:this|the|our)|(?<![가-힣])대조적", re.IGNORECASE)

# 충돌 표현 → 한글 뜻 (카드 가독성용). 부분 문자열 매칭, 첫 일치 사용.
KW_KO = [
    ("contradict", "반박·충돌"), ("counterpoint", "반대 논점"), ("counter to", "반대"),
    ("contrary to", "상반된 결과"), ("in contrast to", "대조"), ("at odds", "상충"),
    ("conflicting", "상충 결과"), ("refut", "반증"), ("overturn", "결론 뒤집음"),
    ("반박", "반박"), ("상충", "상충"), ("상반", "상반"), ("반론", "반론"),
    ("대비되는", "대비"), ("뒤집", "뒤집음"),
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

# 부정문 억제 (2026-07-18): 충돌 키워드가 **부정 안에** 있으면 충돌이 아니라
# 충돌의 부인이다. 30건 표본 판정에서 6건이 이 패턴이었다 —
#   "reinforcing rather than **overturning** the existing technique pages"
#   "this *qualifies* rather than **contradicts** Chakraborty"
#   "(These are not **contradictory**: …)"  /  "**not a real contradiction**"
#   "…이 아니라 **상충**하는 것으로 보이나 …"
# **부정어는 키워드에 통사적으로 붙어 있어야 한다** — 단지 근처에 있는 것으로는
# 부족하다. 초안은 앞 60자 창에서 맨 `not`/`no`를 찾았는데, 회귀 테스트에서
# 진짜 충돌을 죽였다:
#   "Song found **no** pain difference …, **whereas** this RCT detects a penalty"
# 여기서 `no`는 *연구 결과*("no pain difference")의 일부이지 whereas의 부정이 아니다.
# 연구 산문에서 "no significant difference"는 극도로 흔해, 맨 `no`를 넣으면
# 진짜 신호를 대량으로 잃는다(거짓 음성 = 임상적으로 위험한 방향).
#
# 그래서 (a) 맨 `no`는 뺐고, (b) 창을 30자로 좁혔으며, (c) 뒤쪽 창은 한국어
# 전용으로 뒀다 — 한국어는 부정이 키워드 **뒤**에 온다("뒤집는 것이 아니라").
# 영어 `no`가 키워드 뒤에 오는 건 대개 괄호 안 결과 서술이라 부정이 아니다:
#   "Shiffler **contradicts** this paper on diameter (**no** significant effect …)"
NEG_LOOKBACK = 30
NEG_LOOKAHEAD = 20
NEG_BEFORE = re.compile(
    r"\bnot\b|\bnever\b|\brather than\b|\binstead of\b|\bdoes not\b|\bdid not\b|"
    r"\bcannot\b|\bfar from\b|\bwithout\b", re.IGNORECASE)
NEG_AFTER = re.compile(r"아니라|아니다|아님|이 아닌|은 아닌")


def negated(line: str, kw_lo: int, kw_hi: int) -> bool:
    """충돌 키워드가 부정 문맥 안에 있는가 (통사적으로 붙은 부정만)."""
    left = line[max(0, kw_lo - NEG_LOOKBACK):kw_lo]
    right = line[kw_hi:kw_hi + NEG_LOOKAHEAD]
    return bool(NEG_BEFORE.search(left) or NEG_AFTER.search(right))


# 부정 필터 회귀 테스트 (2026-07-18) — `--selftest`로 실행.
# 초안이 진짜 충돌("found **no** pain difference …, **whereas** …")을 죽인 사고가
# 있었기에 남긴다. 필터를 손대면 반드시 이걸 먼저 돌릴 것.
NEG_SELFTEST = [
    # (문장, 억제되어야 하는가)
    ("This is a genuine contradiction inside the wiki's own holdings", False),
    ("Song found no pain difference between sealers, whereas this RCT detects a penalty", False),
    ("Shiffler contradicts this paper on diameter (no significant effect vs P<.001)", False),
    ("Garcia-Sanchez 2022와 정면으로 대비되는 결과", False),
    ("Read at face value they contradict each other flatly", False),
    ("reinforcing rather than overturning the existing technique pages", True),
    ("This qualifies rather than contradicts Chakraborty", True),
    ("the rates differ because of screening, not a real contradiction", True),
    ("이는 결론을 뒤집는 것이 아니라 경계조건을 긋는다", True),
    ("(These are not contradictory: both describe the same biology)", True),
    ("extends the map without contradicting the spine", True),
    ("this is not a resolved contradiction but an unbridged gap", True),
]


def run_selftest() -> int:
    bad = []
    for line, expect in NEG_SELFTEST:
        m = HIGH.search(line) or SOFT.search(line)
        if not m:
            bad.append((line, "키워드 매칭 안 됨"))
            continue
        got = negated(line, *m.span())
        if got != expect:
            bad.append((line, f"기대 {expect} 실제 {got}"))
    for line, why in bad:
        print(f"  ✗ {why}: {line[:70]}")
    print(f"부정 필터 self-test: {len(NEG_SELFTEST) - len(bad)}/{len(NEG_SELFTEST)} 통과")
    return 1 if bad else 0


FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
ONELINER_RE = re.compile(r"^##\s*세줄요약\s*\n+(.+?)(?=\n##\s|\Z)", re.DOTALL | re.MULTILINE)

def oneliner_of(text):
    """페이지 본문에서 ## 세줄요약 첫 단락을 뽑아 한 줄로 정리 (없으면 '')."""
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
    # 기존 typed 엣지 target(stem) 집합 — **타입 무관** (2026-07-17 수정).
    #
    # 과거엔 contradicts/refines 엣지만 "충족"으로 인정해, extends/reinforces/
    # applies-to로 이미 연결된 쌍도 Tier 1으로 계속 방출했다. 2026-07-17 실측:
    # Tier 1 122건 중 96건이 이 오탐이었고, 전수 검토 결과 96건 모두 기존 타입이
    # 옳았다(=본문의 충돌 표현이 키워드 오탐이었다).
    #
    # 더 나쁜 건 이 신호를 **끌 수 없다**는 점이다. "아니오, extends가 맞다"는
    # 판단을 기록할 수단이 없어 같은 쌍이 매일 영구 재방출된다 — 끌 수 없는 신호는
    # 시간이 지나면 노이즈가 된다(AUDITS.md의 "signal, not gate"에 반한다).
    # 어떤 타입이든 엣지가 있다면 저자가 이미 그 쌍을 보고 판단한 것으로 간주한다.
    edges = set()
    rel = re.search(r"^relations:\s*\n((?:[ \t]+.*\n?)+)", fm, re.MULTILINE)
    if rel:
        for item in re.split(r"\n(?=\s*-\s)", rel.group(1)):
            t = re.search(r"type:\s*(\S+)", item)
            g = re.search(r"target:\s*(\S+)", item)
            if t and g:
                edges.add(g.group(1).strip().rstrip("/").split("/")[-1])
    return fm, body, cat, edges

if "--selftest" in sys.argv:
    raise SystemExit(run_selftest())

# stem 인덱스 + stem→세줄요약(한국어) 인덱스
#
# 철회 페이지 제외 (2026-07-17): `retraction_status: RETRACTED` 페이지는 typed 그래프에서
# 양방향 격리하는 것이 위키 관례다(INGEST.md Step 0, scripts/retraction-audit.py). 레이더가
# 이를 모르면 "철회 논문과 엣지를 달아라"를 **영원히 거절해야 하는 제안**으로 계속 올리고,
# 미래의 백필 세션이 그걸 보고 격리를 되돌린다. 출발·대상 양쪽에서 뺀다.
RETRACTED_RE = re.compile(r"^retraction_status:\s*RETRACTED\s*$", re.MULTILINE | re.IGNORECASE)

stems = set()
oneliner = {}
retracted_stems = set()
for md in WIKI.rglob("*.md"):
    if md.name.startswith("_"):
        continue
    try:
        txt = md.read_text(encoding="utf-8", errors="replace")
    except Exception:
        txt = ""
    fm_m = FM_RE.match(txt)
    if fm_m and RETRACTED_RE.search(fm_m.group(1)):
        retracted_stems.add(md.stem)
        continue                      # 대상 후보에서 제외 (stems에 넣지 않는다)
    stems.add(md.stem)
    oneliner[md.stem] = oneliner_of(txt)

def ko_line(stem, label):
    """stem의 세줄요약 첫 줄을 카드 서브라인으로. 없으면 안내."""
    ol = oneliner.get(stem, "")
    if ol:
        return f"  - ▸ {label}(`{stem}`) 세줄: {ol}"
    return f"  - ▸ {label}(`{stem}`) 세줄: _(세줄요약 없음 — 페이지 확인 필요)_"

# 충돌 표현의 **대상 특정** (2026-07-17 추가).
#
# 과거엔 키워드가 있는 줄의 [[wikilink]]를 **전부** 대상으로 간주해, 링크 n개짜리
# 줄이 Tier 1 후보 n건을 낳았다. 그중 진짜 대상은 많아야 1건이다. 실측 사례:
# vorovenci-2024의 한 줄이 후보 7건을 만들었고, sinus-lift-lateral-2026-synthesis에
# 붙은 "contradicts Maska null finding"은 실제로 akbari↔maska 쌍인데
# synthesis↔akbari로 기록됐다.
#
# → 키워드와 **가장 가까운** 링크만 대상으로 삼고, 나머지는 대상이라는 근거가
#   없으므로 Tier 2(대상 불명)로 강등한다. 버리지 않고 강등하는 이유는 놓친
#   진짜 대상이 조용히 사라지면 안 되기 때문이다.
MAX_DIST = 120   # 키워드↔링크 최대 문자 간극. 넘으면 같은 문장으로 보지 않는다.

def gap(a, b, lo, hi):
    """링크 span [a,b) 와 키워드 span [lo,hi) 사이 문자 간극 (겹치면 0)."""
    if b <= lo:
        return lo - b
    if a >= hi:
        return a - hi
    return 0

# "검토했고 엣지 불필요" 대장 (2026-07-18).
#
# 이 감사의 억제 조건은 "typed 엣지가 있으면 제외"뿐이었다. 그래서 검토 결과가
# NONE(엣지 불필요)이면 엣지가 안 생겨 **다음날 같은 후보가 그대로 재방출**됐다 —
# 판정 노동이 매일 증발하는 구조다. 위 parse() 주석이 경고한 "끌 수 없는 신호"의
# 나머지 절반이 이것이다.
#
# logs/relation-negatives.md 에 (source, target, 문장해시)로 기록하면 억제한다.
# 문장이 바뀌면 해시가 달라져 자동 재검토된다 — 페이지 개정으로 진짜 충돌이
# 새로 생기는 경우를 놓치지 않기 위함. 기록은 scripts/log-relation-negative.py.
def _snippet_hash(snippet: str) -> str:
    return hashlib.sha1(re.sub(r"\s+", " ", snippet).strip().encode("utf-8")).hexdigest()[:12]


def _load_negatives() -> set:
    p = ROOT / "logs" / "relation-negatives.md"
    out = set()
    if not p.exists():
        return out
    for line in p.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| 20"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) >= 4:
            out.add((cells[1], cells[2], cells[3]))
    return out


NEGATIVES = _load_negatives()

tier1 = []   # (page_stem, cat, target_stem, kw, snippet)
tier2 = []   # (page_stem, cat, tier, kw, snippet)
n_ambig = 0        # 동일 줄 비최근접 링크 — 대상 불명으로 강등된 수
n_typed_skip = 0   # 이미 typed 엣지가 있어 제외된 (page,target) 쌍 수
n_neg_skip = 0     # 충돌 키워드가 부정문 안이라 제외된 줄 수 (2026-07-18)
n_ledger_skip = 0  # 대장에 "검토·불필요"로 기록돼 제외된 수 (2026-07-18)

for md in WIKI.rglob("*.md"):
    if md.name.startswith("_") or md.stem in ("index",):
        continue
    if md.stem in retracted_stems:      # 철회 페이지는 출발점으로도 쓰지 않는다
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
        m = hi or so
        kw = m.group(0)
        kw_lo, kw_hi = m.span()
        snip = re.sub(r"\s+", " ", line).strip()[:400]

        # (1) 부정문 억제 — 키워드가 부정 안에 있으면 충돌의 *부인*이다
        if negated(line, kw_lo, kw_hi):
            n_neg_skip += 1
            continue

        links = []
        dropped_typed = False       # 이 줄의 링크가 '이미 엣지 있음'으로 걸러졌나
        for lm in WIKILINK.finditer(line):
            s = lm.group(1).rstrip("/").split("/")[-1]
            if s not in stems or s == md.stem:
                continue
            if s in edges:          # 이미 어떤 타입으로든 판단된 쌍
                n_typed_skip += 1
                dropped_typed = True
                continue
            links.append((s, lm.start(), lm.end()))

        if not links:
            # (2) 억제 누수 버그 수정 (2026-07-18).
            #     줄의 링크가 **전부** 기존 엣지로 걸러진 경우, 과거엔 links가 비어
            #     아래 HIGH-no-target으로 재방출됐다 — 억제해야 할 것이 "대상 미지정"
            #     으로 둔갑해 Tier 2를 오염시켰다. 30건 표본에서 대상없음 15건 중
            #     7건(47%)이 실제로는 이미 엣지가 있는 쌍이었다.
            if dropped_typed:
                continue
            if hi:
                if (md.stem, "NOTARGET", _snippet_hash(snip)) in NEGATIVES:
                    n_ledger_skip += 1
                    continue
                tier2.append((md.stem, cat, "HIGH-no-target", kw, snip))
            continue

        # 키워드에 가장 가까운 링크 = 충돌 표현의 대상
        links.sort(key=lambda t: gap(t[1], t[2], kw_lo, kw_hi))
        nearest, na, nb = links[0]
        nd = gap(na, nb, kw_lo, kw_hi)

        if (md.stem, nearest, _snippet_hash(snip)) in NEGATIVES:
            n_ledger_skip += 1
            continue

        if hi and nd <= MAX_DIST:
            tier1.append((md.stem, cat, nearest, kw, snip))
        elif hi:
            # 키워드와 너무 멀다 — 같은 문장이라는 근거가 약하다
            tier2.append((md.stem, cat, f"HIGH-far→{nearest}", kw, snip))
        else:
            tier2.append((md.stem, cat, f"SOFT→{nearest}", kw, snip))

        # 같은 줄의 나머지 링크는 충돌 표현의 대상이라는 근거가 없다 → 강등
        for s, a, b in links[1:]:
            tier2.append((md.stem, cat, f"AMBIG→{s}", kw, snip))
            n_ambig += 1

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
    "명시적 충돌 표현이 있으나 그 쌍에 `relations:` 타입 엣지가 (어떤 타입이든) 없는 후보. "
    "**이 목록은 신호일 뿐 — 두 페이지를 읽고 판단해 엣지를 단다.**",
    "",
    "**카드 읽는 법**: 각 카드는 `출발페이지 —[충돌유형·한글뜻]→ 대상페이지` 형태다. "
    "아래에 (1) **근거 문장**(위키 본문에서 충돌 표현이 나온 실제 문장), "
    "(2) **양쪽 페이지의 `## 세줄요약`**(한국어)을 붙여, 페이지를 열지 않고도 "
    "두 논문이 각각 무엇을 주장하는지·정말 충돌하는지 한글로 판단할 수 있게 했다. "
    "충돌 유형 한글뜻은 표현 매칭 기반 근사치이며, **최종 판단은 사람/LLM 몫**이다. "
    "(reinforces가 맞는 경우도 있으니 키워드를 그대로 엣지로 옮기지 말 것 — "
    "2026-07-17 전수 검토에서 contradicts 계열로 지목된 122건 중 실제 contradicts는 1건이었다.)",
    "",
    "**대상은 키워드에 가장 가까운 링크로 특정한다.** 같은 줄의 나머지 링크는 "
    "충돌 표현의 대상이라는 근거가 없어 Tier 2(`AMBIG→`)로 강등된다 — 버리지 않으니 "
    "진짜 대상이 강등됐다면 Tier 2에서 찾을 수 있다.",
    "",
    f"- Tier 1 (대상 지목됨, actionable): **{len(t1)}**",
    f"- Tier 2 (대상 불명/soft, review): **{len(tier2)}**",
    f"- (억제됨) 이미 typed 엣지가 있어 제외: **{n_typed_skip}** · 부정문 제외: **{n_neg_skip}** · 검토·불필요 대장: **{n_ledger_skip}** · "
    f"동일 줄 비최근접으로 Tier 2 강등: **{n_ambig}**",
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
print(f"  억제: typed 엣지 기존재 {n_typed_skip} · 부정문 {n_neg_skip} · 검토·불필요 대장 {n_ledger_skip} · 동일 줄 비최근접 강등 {n_ambig}")
print(f"  세줄요약 인덱스: {sum(1 for v in oneliner.values() if v)}/{len(oneliner)} pages")
