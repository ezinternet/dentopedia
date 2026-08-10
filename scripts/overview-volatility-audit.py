#!/usr/bin/env python3
"""
LLM Wiki — Overview Volatility Index (OVI). SIGNAL, 절대 block하지 않는다.

무엇을 재는가: "내가 내린 종합 결론(overview) 중 어느 것이 가장 뒤집힐 위험이 큰가."
채점 단위는 개별 논문 페이지가 아니라 wiki/overviews/*.md 다. 논문이 뭐라고 했는지는
바뀌지 않는다. 바뀌는 건 그 논문들을 묶어 내린 결론이다.

이 스크립트는 새 신호를 수집하지 않는다. 기존 감사들이 페이지 단위로 흩어놓은 신호를
overview 단위로 롤업하고 하나의 축으로 정렬한다. 유일한 신규 신호는 ①(근거 이탈)이다.

성분 (각 0~1 정규화 후 가중합 × 100):
  ① churn      0.30  마지막 thesis 편집 이후 source_papers에 추가된 논문 수
                     → 종합이 자기 근거 기반보다 뒤처진 정도. 가장 직접적인 신호.
  ② age        0.20  thesis 최종수정 후 경과일 (wikilink-only 커밋 제외)
  ③ contention 0.20  구성 논문 사이의 contradicts(×2)·refines(×1) 엣지 수
  ④ decay      0.20  고근거(sr+ma/sr/rct) 구성 논문 중 N년 경과 + superseded_by 없는 비율
  ⑤ void       0.10  구성 논문 최신 연도로부터의 공백 (해석 양방향 → 낮은 가중치)

  ⑥ 철회는 점수 성분이 아니다. retraction_status 걸린 논문이 구성에 있으면
     점수와 무관하게 별도 하드 플래그로 최상단 고정한다. 점수에 녹이면 묻힌다.

가중치·임계값은 1차 실행 시점에서 임의값이다. 상위 20편 캘리브레이션 리뷰를 거치기
전까지 절대값을 신뢰하지 말 것. 출력이 원점수 랭킹이 아니라 3티어인 이유가 그것이다.

evidence_level 이 없고 레거시 confidence 필드만 있는 페이지(2026-08-02 기준 22편)는
confidence 로 폴백해 읽는다. 필드 마이그레이션이 끝나면 폴백을 제거할 것.

실행: python3 scripts/overview-volatility-audit.py [--top N] [--html]
     daily-audit.py 에서는 --html 없이 호출한다 — HTML 재생성은 아티팩트 빌드이고,
     아티팩트는 소비 시점(deploy)에 속한다. 파일명이 build-* 가 아닌 이유이기도 하다.
출력: logs/{YYYY-MM-DD}_volatility.log
      interactives/volatility-index.html  (--html 지정 시, 덮어쓰기 AUTO-GENERATED)
Exit: 항상 0 (signal, non-blocking)
"""

import re
import sys
import html
import argparse
import subprocess
import importlib.util
from datetime import date, datetime, timezone
from pathlib import Path
from collections import defaultdict

WIKI_ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = WIKI_ROOT / "wiki"
OVERVIEWS_DIR = WIKI_DIR / "overviews"
LOGS_DIR = WIKI_ROOT / "logs"
INTERACTIVES_DIR = WIKI_ROOT / "interactives"

# 스코어링에서 제외할 폴더 (템플릿·린트 픽스처)
EXCLUDED_DIRS = {"_meta", "_lint"}

HIGH_EVIDENCE = {"sr+ma", "sr", "rct"}
DECAY_YEARS = 7          # 고근거 논문이 이 연수를 넘기면 decay 후보
DECAY_PRIOR = 2          # 4번 성분 축소추정 유사관측수 - 소분모 폭주 방지
TODAY = date.today()

# 가중치 — 임의 초기값. 캘리브레이션 후 갱신할 것.
# 2026-08-02 캘리브레이션 1차 조정. 근거: 1차 실행 상위 16편이 성분 패턴으로 두 부류로
# 깨끗하게 갈렸다 — (a) churn 만 높고 contention/decay 가 0인 군(ceraseal 28편, drug-
# antibiotic 49편, gp-cone, ian-nerve, odontogenic-sinusitis)은 결론이 뒤처진 게 아니라
# 지금 활발히 만드는 중인 신규 종합이었고, (b) contention/decay 가 동반된 군(immediate-
# implant, nccl, gbr-barrier, unopposed-tooth)만 설계 의도대로의 흔들림이었다.
# 즉 churn 단독은 "미반영 근거의 양"과 "구축 활동량"을 구분하지 못한다 → 비중을 낮추고
# 논쟁·decay 로 옮긴다. 로그 스케일은 순위만 흔들 뿐 이 구분을 못 해서 채택하지 않았다.
WEIGHTS = {"churn": 0.20, "age": 0.20, "contention": 0.25, "decay": 0.25, "void": 0.10}

# 정규화 상한 — 이 값에서 성분 점수가 1.0으로 포화
# churn 8·contention 10 은 1차 실행에서 너무 낮았다 — 상위 16편 중 9편이 churn 1.00 으로
# 포화돼 9편 유입과 49편 유입이 같은 점수를 받았다. 실측 분포에 맞춰 상한을 올린다.
CAP = {"churn": 24, "age_days": 120, "contention": 14, "void_years": 5}

# ② 의 상한은 리포가 실제로 관측 가능한 히스토리 창에 연동한다(git_history_window 가 덮어씀).
# 이 리포의 첫 커밋은 2026-05-18 — 고정 365일 상한을 쓰면 ②는 최대 0.13까지만 올라가
# 사실상 죽는다. 창 길이로 나누면 "관측 가능한 기간 중 얼마나 방치됐나"가 되고,
# 히스토리가 쌓일수록 자동으로 엄격해진다.

# 티어 경계 (0~100). 1차 실측 분포(p50=9.7 p90=24.6 max=63)에 맞춘 잠정값 — 캘리브레이션 대상.
# 재가중(2026-08-02) 후 실측 분포에 재정렬. 월 1회 리뷰에서 적색 5편 내외 = 실제로
# 손댈 수 있는 분량, 주황은 다음 sweep 관찰 대상. 경계값 자체에 의미는 없다.
TIER_RED = 33
TIER_ORANGE = 25


# ---- thesis/wikilink 분류기: overview-thesis-staleness.py 를 단일 출처로 재사용 ----

def _load_staleness_module():
    """하이픈 파일명이라 일반 import 불가 → importlib 로 로드."""
    path = WIKI_ROOT / "scripts" / "overview-thesis-staleness.py"
    spec = importlib.util.spec_from_file_location("_ots", path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_OTS = _load_staleness_module()
is_wikilink_only_change_line = _OTS.is_wikilink_only_change_line

# source_papers YAML 리스트 항목 / Related Papers wikilink bullet
SOURCE_PAPER_LINE_RE = re.compile(
    r"^\s*-\s+(?:\[\[[^\]]+\]\]|[a-z][\w./-]*)\s*(?:[—:\-]\s*.*)?$"
)


# ---- frontmatter 파싱 (경량 — pyyaml 의존 없이 필요한 필드만) ----------------

FM_DELIM_RE = re.compile(r"^---\s*$")


def read_frontmatter(path: Path) -> dict:
    """필요한 필드만 뽑는다: year, evidence_level|confidence, superseded_by,
    retraction_status, title, source_papers[], relations[(type,target)]."""
    out = {
        "title": path.stem, "year": None, "evidence_level": None,
        "superseded_by": None, "retraction_status": None,
        "source_papers": [], "relations": [],
    }
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return out
    if not lines or not FM_DELIM_RE.match(lines[0]):
        return out

    mode = None          # 'source_papers' | 'relations' | None
    pending_type = None
    for raw in lines[1:]:
        if FM_DELIM_RE.match(raw):
            break
        # 리스트 블록 계속 여부: 들여쓰기 + '-' 또는 'target:'
        stripped = raw.strip()
        if mode == "source_papers" and raw.startswith((" ", "\t")) and stripped.startswith("- "):
            out["source_papers"].append(stripped[2:].strip().strip("'\""))
            continue
        if mode == "relations" and raw.startswith((" ", "\t")):
            m = re.match(r"-\s*type:\s*(.+)$", stripped)
            if m:
                pending_type = m.group(1).strip().strip("'\"")
                continue
            m = re.match(r"target:\s*(.+)$", stripped)
            if m and pending_type:
                out["relations"].append((pending_type, m.group(1).strip().strip("'\"")))
                pending_type = None
                continue
            continue
        mode = None
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", raw)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if key == "source_papers":
            mode = "source_papers"
        elif key == "relations":
            mode = "relations"
        elif key == "year":
            try:
                out["year"] = int(re.sub(r"\D", "", val)[:4])
            except (ValueError, TypeError):
                pass
        elif key in ("evidence_level", "confidence"):
            # evidence_level 우선, 없을 때만 레거시 confidence 채택
            if key == "evidence_level" or out["evidence_level"] is None:
                out["evidence_level"] = val.strip("'\"").lower() or None
        elif key == "superseded_by":
            out["superseded_by"] = val or None
        elif key == "retraction_status":
            out["retraction_status"] = val or None
        elif key == "title":
            out["title"] = val.strip("'\"") or path.stem
    return out


# ---- git: overview 전체 히스토리를 한 번에 (파일별 --follow 는 편당 ~3.8초로 과다) ----

DIFF_HEADER_RE = re.compile(r"^diff --git a/(\S+) b/(\S+)$")
COMMIT_RE = re.compile(r"^COMMIT\t([0-9a-f]{40})\t(\S+)$")


BULK_TOUCH_MIN = 10   # 한 커밋이 이 편수 이상 건드리면 정비 커밋으로 간주


def collect_overview_commits() -> dict[str, list[tuple[datetime, str, bool]]]:
    """{rel_path: [(author_date, diff_text, is_bulk), ...]} — 커밋 최신순.

    is_bulk: 한 커밋이 overview 를 BULK_TOUCH_MIN 편 이상 건드렸으면 True.
    왜 필요한가 — 이 리포에는 229편 일괄 필드 마이그레이션, 116건 relations 재라벨링,
    28파일 restructuring 후 wikilink cascade 같은 정비 커밋이 있다. 전부 본문을 기계적으로
    바꾸므로 순진한 diff 분류기에서 'thesis 편집'으로 잡히고, 그 결과 모든 overview 의
    thesis 나이가 같은 날짜로 붕괴한다(실측 1차 실행: 262편 전부 15~19일).
    한 번에 열 편 이상을 고친 커밋은 어느 한 편의 종합을 다시 쓴 작업이 아니다.

    git 사용 불가/얕은 클론이면 빈 dict 를 반환하고, 호출부는 ①②를 degrade 한다
    (빌드는 실패시키지 않는다 — build-wiki-stats.py 와 동일한 방침)."""
    try:
        r = subprocess.run(
            ["git", "log", "--format=COMMIT\t%H\t%aI", "-p", "--no-renames",
             "--", "wiki/overviews/"],
            cwd=WIKI_ROOT, capture_output=True, text=True, check=True, timeout=300,
        )
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError):
        return {}

    per_file: dict[str, list[list]] = defaultdict(list)
    cur_date: datetime | None = None
    cur_sha: str | None = None
    cur_path: str | None = None
    buf: list[str] = []
    touch_count: dict[str, int] = defaultdict(int)
    entry_sha: list[tuple[str, list]] = []   # (sha, entry) — 나중에 is_bulk 채움

    def flush():
        if cur_path is not None and cur_date is not None and buf and cur_sha is not None:
            entry = [cur_date, "\n".join(buf), False]
            per_file[cur_path].append(entry)
            entry_sha.append((cur_sha, entry))
            touch_count[cur_sha] += 1

    for line in r.stdout.splitlines():
        m = COMMIT_RE.match(line)
        if m:
            flush()
            buf = []
            cur_path = None
            cur_sha = m.group(1)
            try:
                cur_date = datetime.fromisoformat(m.group(2))
            except ValueError:
                cur_date = None
            continue
        m = DIFF_HEADER_RE.match(line)
        if m:
            flush()
            buf = []
            cur_path = m.group(2)
            continue
        if cur_path is not None:
            buf.append(line)
    flush()
    for sha, entry in entry_sha:
        entry[2] = touch_count[sha] >= BULK_TOUCH_MIN
    return {k: [tuple(e) for e in v] for k, v in per_file.items()}


def git_history_window() -> int | None:
    """첫 커밋부터 오늘까지의 일수. ② 정규화 상한으로 쓴다."""
    try:
        r = subprocess.run(["git", "log", "--reverse", "--format=%aI", "--max-parents=0"],
                           cwd=WIKI_ROOT, capture_output=True, text=True, check=True, timeout=60)
        first = r.stdout.strip().splitlines()[0]
        days = (TODAY - datetime.fromisoformat(first).astimezone(timezone.utc).date()).days
        return max(days, 30)
    except Exception:
        return None


def analyze_history(diffs: list[tuple[datetime, str]]) -> tuple[datetime | None, int]:
    """(마지막 thesis 편집일, 그 이후 추가된 source_paper 라인 수).

    커밋은 최신순. 최신부터 훑다가 첫 thesis 커밋을 만나면 거기서 멈춘다.
    그 전까지 지나온 wikilink-only 커밋들의 추가 논문 라인이 churn."""
    churn = 0
    for dt, diff, is_bulk in diffs:
        if is_bulk:
            continue        # 정비 커밋: thesis 판정에서도, churn 집계에서도 제외
        added_body, added_papers, nontrivial = 0, 0, 0
        in_hunk = False
        for raw in diff.splitlines():
            if raw.startswith("@@"):
                in_hunk = True
                continue
            if not in_hunk or raw.startswith(("+++", "---")):
                continue
            if raw.startswith("+"):
                body = raw[1:]
                added_body += 1
                if not is_wikilink_only_change_line(body):
                    nontrivial += 1
                elif SOURCE_PAPER_LINE_RE.match(body):
                    added_papers += 1
            elif raw.startswith("-"):
                if not is_wikilink_only_change_line(raw[1:]):
                    nontrivial += 1
        if added_body == 0 and nontrivial == 0:
            continue
        if nontrivial > 0:
            return (dt, churn)          # 최초로 만난 thesis 커밋 = 마지막 thesis 편집
        churn += added_papers
    return (None, churn)                # thesis 커밋 없음 (파일 생성 커밋만 등)


# ---- 위키 전체 인덱스 -------------------------------------------------------

def build_page_index() -> tuple[dict[str, Path], dict[str, dict]]:
    """(stem -> path, stem -> frontmatter). _meta·_lint 제외."""
    stem_to_path: dict[str, Path] = {}
    meta: dict[str, dict] = {}
    for p in WIKI_DIR.rglob("*.md"):
        if any(part in EXCLUDED_DIRS for part in p.relative_to(WIKI_DIR).parts[:-1]):
            continue
        stem_to_path.setdefault(p.stem, p)
    for stem, p in stem_to_path.items():
        meta[stem] = read_frontmatter(p)
    return stem_to_path, meta


def to_stem(ref: str) -> str:
    """source_papers 항목('wiki/implants/foo.md', '[[foo]]', 'foo') → stem."""
    ref = ref.strip()
    m = re.match(r"^\[\[(.+?)\]\]$", ref)
    if m:
        ref = m.group(1)
    ref = ref.split("|")[0].split("#")[0]
    ref = re.sub(r"\.md$", "", ref)
    return ref.rsplit("/", 1)[-1]


WIKILINK_IN_BODY_RE = re.compile(r"\[\[([^\]|#]+)")


def extract_members(ov_path: Path, ov_fm: dict, meta: dict) -> tuple[list[str], list[str]]:
    """(해결된 구성 논문 stem, 미해결 참조 stem).

    source_papers frontmatter 는 262편 중 90편에만 있다(2026-08-02 실측). 나머지 172편은
    본문 Related Papers 섹션의 wikilink 로만 논문을 건다. frontmatter 만 읽으면 그 172편이
    구성원 0으로 잡혀 ③④⑤가 통째로 죽는다 — 그래서 본문 wikilink 를 합집합으로 넣는다.
    다른 overview 를 가리키는 링크는 제외한다(구성 논문이 아니라 형제 종합이다)."""
    refs = [to_stem(x) for x in ov_fm["source_papers"]]
    try:
        body = ov_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        body = ""
    refs += [to_stem(m) for m in WIKILINK_IN_BODY_RE.findall(body)]

    known, missing, seen = [], [], set()
    for r in refs:
        if not r or r in seen or r == ov_path.stem:
            continue
        seen.add(r)
        if r in meta:
            if r.endswith("-overview") or r.endswith("-synthesis"):
                continue
            known.append(r)
        else:
            missing.append(r)
    return known, missing


def norm(value: float, cap: float) -> float:
    if cap <= 0:
        return 0.0
    return max(0.0, min(1.0, value / cap))


def score_overview(ov_path: Path, ov_fm: dict, meta: dict,
                   thesis_dt: datetime | None, churn: int,
                   git_ok: bool) -> dict:
    ov_stem = ov_path.stem
    known, missing = extract_members(ov_path, ov_fm, meta)

    # ② thesis 노후
    age_days = None
    if thesis_dt is not None:
        age_days = (TODAY - thesis_dt.astimezone(timezone.utc).date()).days

    # ③ 논쟁 밀도 — 구성 논문 사이 엣지 + overview 자체 엣지
    member_set = set(known)
    contradicts = refines = 0
    for src in known + [ov_stem]:
        for rtype, target in meta.get(src, {}).get("relations", []):
            tgt = to_stem(target)
            if src != ov_stem and tgt not in member_set:
                continue          # 구성 논문끼리의 충돌만 (외부 엣지는 이 종합의 논쟁이 아님)
            if rtype == "contradicts":
                contradicts += 1
            elif rtype == "refines":
                refines += 1
    contention_raw = contradicts * 2 + refines

    # ④ 고근거 decay
    high = [s for s in known if (meta[s].get("evidence_level") or "") in HIGH_EVIDENCE]
    decayed = [
        s for s in high
        if meta[s].get("year") and meta[s]["year"] <= TODAY.year - DECAY_YEARS
        and not meta[s].get("superseded_by")
    ]
    # 축소추정(shrinkage). 1차 실행에서 고근거 논문이 1편뿐인 overview 가 그 1편이
    # 오래됐다는 이유만으로 4번 성분 1.00 을 받아 적색 4편 중 2편을 차지했다. 비율
    # 추정치의 분산은 분모에 반비례하는데 원시 비율은 그걸 무시한다. 분모에 DECAY_PRIOR
    # 를 더해 0 쪽으로 당긴다: 1/1 -> 0.33, 2/5 -> 0.29, 8/16 -> 0.44, 20/25 -> 0.74.
    decay_frac = len(decayed) / (len(high) + DECAY_PRIOR) if high else 0.0

    # ⑤ 최신 논문 공백
    years = [meta[s]["year"] for s in known if meta[s].get("year")]
    newest = max(years) if years else None
    void_years = (TODAY.year - newest) if newest else 0

    # ⑥ 철회 하드 플래그
    retracted = [s for s in known if meta[s].get("retraction_status")]

    comp = {
        "churn": norm(churn, CAP["churn"]) if git_ok else 0.0,
        "age": norm(age_days or 0, CAP["age_days"]) if git_ok else 0.0,
        "contention": norm(contention_raw, CAP["contention"]),
        "decay": decay_frac,
        "void": norm(max(0, void_years - 1), CAP["void_years"]),
    }
    active = WEIGHTS if git_ok else {k: v for k, v in WEIGHTS.items() if k not in ("churn", "age")}
    total_w = sum(active.values())
    score = 100 * sum(comp[k] * w for k, w in active.items()) / total_w

    return {
        "stem": ov_stem, "title": ov_fm["title"], "score": round(score, 1),
        "components": comp, "churn": churn, "age_days": age_days,
        "contradicts": contradicts, "refines": refines,
        "n_members": len(known), "n_missing": len(missing),
        "n_high": len(high), "n_decayed": len(decayed),
        "newest_year": newest, "retracted": retracted,
        "tier": "관찰",
    }


# ---- 출력 -------------------------------------------------------------------

def render_log(rows: list[dict], git_ok: bool, top: int) -> str:
    L = []
    L.append(f"# Overview Volatility Index — {TODAY.isoformat()}")
    L.append("")
    L.append(f"대상 overview: {len(rows)}편 · git 히스토리: {'사용' if git_ok else '불가 (①② degrade)'}")
    L.append(f"가중치 {WEIGHTS} · decay 기준 {DECAY_YEARS}년 · 티어 경계 {TIER_RED}/{TIER_ORANGE}")
    L.append("※ 가중치·경계는 캘리브레이션 전 임의값. 절대점수 아닌 티어로 읽을 것.")
    L.append("")

    flagged = [r for r in rows if r["retracted"]]
    if flagged:
        L.append("## ⚠️ 철회 하드 플래그 (점수 무관·최우선)")
        for r in flagged:
            L.append(f"- [[{r['stem']}]] — 구성 논문 중 철회: {', '.join(r['retracted'])}")
        L.append("")

    for tier, label in (("적색", "적색 — 재검토 우선"), ("주황", "주황 — 다음 sweep 시 확인"), ("관찰", "관찰")):
        sub = [r for r in rows if r["tier"] == tier]
        if tier == "관찰":
            L.append(f"## 관찰 ({len(sub)}편) — 상세 생략")
            L.append("")
            continue
        L.append(f"## {label} ({len(sub)}편)")
        L.append("")
        for r in sub[:top]:
            c = r["components"]
            L.append(f"### {r['score']}  [[{r['stem']}]]")
            L.append(f"  {r['title']}")
            age = f"{r['age_days']}일" if r["age_days"] is not None else "미상"
            L.append(
                f"  ① churn {r['churn']}편 ({c['churn']:.2f}) · ② thesis {age} ({c['age']:.2f}) · "
                f"③ 논쟁 c{r['contradicts']}/r{r['refines']} ({c['contention']:.2f}) · "
                f"④ decay {r['n_decayed']}/{r['n_high']} ({c['decay']:.2f}) · "
                f"⑤ 최신 {r['newest_year'] or '?'} ({c['void']:.2f})"
            )
            note = []
            if r["n_missing"]:
                note.append(f"미해결 참조 {r['n_missing']}건")
            if r["n_members"] == 0:
                note.append("source_papers 없음")
            if note:
                L.append(f"  ! {' · '.join(note)}")
            L.append("")
    return "\n".join(L)


HTML_TMPL = """<!DOCTYPE html>
<meta charset="utf-8"><title>Overview Volatility Index</title>
<style>
:root{--red:#c0392b;--orange:#d68910;--gray:#7f8c8d;--bg:#fbfbfa;--line:#e4e4e2}
body{font-family:-apple-system,'Apple SD Gothic Neo','Noto Sans KR',sans-serif;
  max-width:1000px;margin:0 auto;padding:28px 20px;background:var(--bg);color:#2c3e50;line-height:1.55}
h1{font-size:1.5rem;margin:0 0 4px}
.meta{color:var(--gray);font-size:.82rem;margin-bottom:6px}
.warn{background:#fff6e5;border-left:3px solid var(--orange);padding:8px 12px;font-size:.82rem;margin:14px 0}
.f{display:flex;gap:6px;margin:18px 0 10px;flex-wrap:wrap}
.f button{border:1px solid var(--line);background:#fff;border-radius:14px;padding:5px 13px;font:inherit;font-size:.82rem;cursor:pointer}
.f button.on{background:#2c3e50;color:#fff;border-color:#2c3e50}
.card{background:#fff;border:1px solid var(--line);border-left-width:4px;border-radius:5px;padding:12px 15px;margin-bottom:9px}
.card.적색{border-left-color:var(--red)}.card.주황{border-left-color:var(--orange)}.card.관찰{border-left-color:var(--line)}
.hd{display:flex;align-items:baseline;gap:10px}
.sc{font-weight:700;font-size:1.1rem;min-width:48px}
.tt{font-size:.9rem}
.stem{color:var(--gray);font-size:.75rem;font-family:ui-monospace,monospace}
.bars{display:grid;grid-template-columns:repeat(5,1fr);gap:7px;margin-top:9px}
.b{font-size:.68rem;color:var(--gray)}
.b .track{height:5px;background:#eee;border-radius:3px;margin-top:2px;overflow:hidden}
.b .fill{height:100%;background:#5d6d7e}
.rt{color:var(--red);font-weight:600;font-size:.8rem;margin-top:7px}
</style>
<h1>Overview Volatility Index</h1>
<div class="meta">__META__</div>
<div class="warn">가중치·티어 경계는 캘리브레이션 전 임의값입니다. 절대점수(62.3 vs 58.1)를 비교하지 말고 티어와 성분 내역으로 읽으십시오.</div>
<div class="f" id="f"></div>
<div id="list"></div>
<script>
const DATA = __DATA__;
const LBL = {churn:'① 근거이탈',age:'② thesis노후',contention:'③ 논쟁',decay:'④ decay',void:'⑤ 공백'};
let cur = '적색';
function draw(){
  document.getElementById('f').innerHTML = ['적색','주황','관찰','전체']
    .map(t=>`<button class="${t===cur?'on':''}" onclick="cur='${t}';draw()">${t} (${t==='전체'?DATA.length:DATA.filter(d=>d.tier===t).length})</button>`).join('');
  const rows = cur==='전체'?DATA:DATA.filter(d=>d.tier===cur);
  document.getElementById('list').innerHTML = rows.map(d=>`
    <div class="card ${d.tier}">
      <div class="hd"><span class="sc">${d.score}</span>
        <span><div class="tt">${d.title}</div><div class="stem">${d.stem}</div></span></div>
      ${d.retracted.length?`<div class="rt">⚠️ 철회 논문 포함: ${d.retracted.join(', ')}</div>`:''}
      <div class="bars">${Object.keys(LBL).map(k=>`
        <div class="b">${LBL[k]}<div class="track"><div class="fill" style="width:${(d.components[k]*100).toFixed(0)}%"></div></div></div>`).join('')}</div>
    </div>`).join('') || '<p style="color:#7f8c8d">해당 티어 없음.</p>';
}
draw();
</script>
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=20, help="티어별 로그 상세 출력 편수")
    ap.add_argument("--html", action="store_true", help="interactives/volatility-index.html 생성")
    args = ap.parse_args()

    if not OVERVIEWS_DIR.is_dir():
        print(f"[SKIP] {OVERVIEWS_DIR} 없음", file=sys.stderr)
        return 0

    stem_to_path, meta = build_page_index()
    commits = collect_overview_commits()
    git_ok = bool(commits)
    if git_ok:
        window = git_history_window()
        if window:
            CAP["age_days"] = window
    if not git_ok:
        print("[WARN] git 히스토리 없음 → ①churn ②age degrade, ③④⑤로만 채점", file=sys.stderr)

    rows = []
    for p in sorted(OVERVIEWS_DIR.glob("*.md")):
        fm = meta.get(p.stem) or read_frontmatter(p)
        rel = str(p.relative_to(WIKI_ROOT))
        thesis_dt, churn = analyze_history(commits.get(rel, []))
        rows.append(score_overview(p, fm, meta, thesis_dt, churn, git_ok))

    rows.sort(key=lambda r: r["score"], reverse=True)
    for r in rows:
        r["tier"] = "적색" if r["score"] >= TIER_RED else ("주황" if r["score"] >= TIER_ORANGE else "관찰")

    LOGS_DIR.mkdir(exist_ok=True)
    log_path = LOGS_DIR / f"{TODAY.isoformat()}_volatility.log"
    log_path.write_text(render_log(rows, git_ok, args.top), encoding="utf-8")

    if args.html:
        import json
        INTERACTIVES_DIR.mkdir(exist_ok=True)
        payload = [
            {k: r[k] for k in ("stem", "title", "score", "tier", "components", "retracted")}
            for r in rows
        ]
        meta_line = (f"{TODAY.isoformat()} · overview {len(rows)}편 · "
                     f"적색 {sum(1 for r in rows if r['tier']=='적색')} / "
                     f"주황 {sum(1 for r in rows if r['tier']=='주황')} / "
                     f"관찰 {sum(1 for r in rows if r['tier']=='관찰')}"
                     + ("" if git_ok else " · git 불가로 ①② degrade"))
        out = (HTML_TMPL
               .replace("__DATA__", json.dumps(payload, ensure_ascii=False))
               .replace("__META__", html.escape(meta_line)))
        (INTERACTIVES_DIR / "volatility-index.html").write_text(out, encoding="utf-8")

    n_red = sum(1 for r in rows if r["tier"] == "적색")
    n_org = sum(1 for r in rows if r["tier"] == "주황")
    n_ret = sum(1 for r in rows if r["retracted"])
    print(f"[OVI] overview {len(rows)}편 · 적색 {n_red} · 주황 {n_org} · 철회플래그 {n_ret}")
    print(f"[OVI] → {log_path.relative_to(WIKI_ROOT)}")
    if args.html:
        print("[OVI] → interactives/volatility-index.html")
    for r in rows[:5]:
        print(f"       {r['score']:5.1f}  {r['stem']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
