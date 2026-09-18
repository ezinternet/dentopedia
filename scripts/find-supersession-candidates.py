#!/usr/bin/env python3
"""
find-supersession-candidates.py

같은 카테고리 안에서 날짜 차이가 큰 고근거 논문 쌍을 찾아 supersession 후보로 제시.
임베딩·GPU 전혀 사용하지 않음 — frontmatter 메타데이터만 읽음.

1. wiki/ 전체 frontmatter 파싱 (category, date, evidence_level, superseded_by)
2. 이미 superseded_by 있는 페이지 제외
3. 같은 카테고리 내 고근거 논문들 사이에서 날짜 차이 >= min_gap인 쌍 추출
4. 이미 relations 엣지로 연결된 쌍 제외
5. 날짜 차이 내림차순 정렬 → 상위 max_pairs 후보 출력
6. --judge: 각 쌍의 세줄요약을 Opus에 넘겨 supersession 판단 요청

Usage
-----
    python3 scripts/find-supersession-candidates.py              # 목록만 (즉시)
    python3 scripts/find-supersession-candidates.py --judge      # Opus 판단 포함
    python3 scripts/find-supersession-candidates.py --min-gap 3  # 3년 이상만
    python3 scripts/find-supersession-candidates.py --new-window 30  # 최근 30일 인제스트된 신형만
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

REPO       = Path(__file__).resolve().parent.parent
WIKI       = REPO / "wiki"
LOGS       = REPO / "logs"
SKIP_DIRS  = {"_lint", "overviews", "_meta"}
SKIP_FILES = {"index.md", "category-map.md", "artificial-intelligence.md"}

HIGH_EVIDENCE = {"sr+ma", "sr", "rct"}  # prospective/retrospective는 제외 (노이즈 줄임)

FM_RE       = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
WIKILINK_RE = re.compile(r"\[\[([^\]\#|]+)")


# ─── helpers ────────────────────────────────────────────────────────────────

def parse_fm(text: str) -> dict:
    m = FM_RE.match(text)
    if not m:
        return {}
    fields: dict = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"^(\w[\w\-]*)\s*:\s*(.*)$", line)
        if kv:
            fields[kv.group(1)] = kv.group(2).strip().strip('"').strip("'")
    return fields


def parse_date(raw: str | None) -> datetime | None:
    if not raw:
        return None
    raw = raw.strip().strip('"').strip("'")
    for fmt in ("%Y-%m-%d", "%Y-%m", "%Y"):
        try:
            return datetime.strptime(raw, fmt)
        except ValueError:
            continue
    return None


def extract_summary(text: str) -> str:
    for heading in ("## 세줄요약", "## Three-line Summary"):
        idx = text.find(heading)
        if idx == -1:
            continue
        body = text[idx + len(heading):]
        next_h = re.search(r"\n##\s", body)
        snippet = body[: next_h.start() if next_h else 500].strip()
        if snippet:
            return snippet[:500]
    return ""


def extract_relations(text: str, fm: dict) -> set[str]:
    related: set[str] = set()
    sb = fm.get("superseded_by", "")
    if sb:
        for part in sb.split(","):
            s = part.strip().strip("[]").split("/")[-1].replace(".md", "").strip()
            if s:
                related.add(s)
    for m in re.finditer(r"target:\s*(.+)", text):
        t = m.group(1).strip().strip('"').split("/")[-1].replace(".md", "")
        related.add(t)
    return related


def collect_pages() -> dict[str, dict]:
    pages: dict[str, dict] = {}
    for f in WIKI.rglob("*.md"):
        if any(p in SKIP_DIRS for p in f.parts):
            continue
        if f.name in SKIP_FILES:
            continue
        try:
            text = f.read_text(encoding="utf-8")
        except OSError:
            continue
        fm = parse_fm(text)
        if not fm:
            continue
        ev = (fm.get("evidence_level") or fm.get("confidence") or "").lower()
        dt = parse_date(fm.get("date") or fm.get("year"))
        # category: wiki/drug/analgesics/foo.md → "drug/analgesics"
        #           wiki/implants/foo.md       → "implants"
        parts = f.relative_to(WIKI).parts
        if len(parts) > 2:
            cat = f"{parts[0]}/{parts[1]}"
        elif len(parts) > 1:
            cat = parts[0]
        else:
            cat = "uncategorized"
        pages[f.stem] = {
            "path":       f,
            "cat":        cat,
            "date":       dt,
            "mtime":      datetime.fromtimestamp(f.stat().st_mtime),
            "evidence":   ev,
            "summary":    extract_summary(text),
            "relations":  extract_relations(text, fm),
            "superseded": bool(fm.get("superseded_by", "").strip()),
            "title":      fm.get("title", f.stem),
        }
    return pages


# ─── candidate finder ───────────────────────────────────────────────────────

def find_candidates(pages: dict[str, dict], min_gap: float, max_pairs: int,
                    new_window: int | None) -> list[dict]:
    today = datetime.now()

    # 신형 필터: new_window 지정 시 mtime 기준, 없으면 전체
    if new_window is not None:
        new_cutoff = today - timedelta(days=new_window)
        new_set = {
            s for s, p in pages.items()
            if not p["superseded"]
            and p["evidence"] in HIGH_EVIDENCE
            and p["date"]
            and p["mtime"] >= new_cutoff
        }
    else:
        new_set = {
            s for s, p in pages.items()
            if not p["superseded"]
            and p["evidence"] in HIGH_EVIDENCE
            and p["date"]
        }

    # 구형: min_gap년 이상 전, 고근거, superseded 아님
    old_set = {
        s for s, p in pages.items()
        if not p["superseded"]
        and p["evidence"] in HIGH_EVIDENCE
        and p["date"]
        and (today - p["date"]).days / 365.25 >= min_gap
    }

    # 카테고리별로 그룹화
    from collections import defaultdict
    by_cat: dict[str, list] = defaultdict(list)
    for s, p in pages.items():
        by_cat[p["cat"]].append(s)

    seen_pairs: set[frozenset] = set()
    candidates: list[dict] = []

    for cat, stems in by_cat.items():
        new_in_cat = [s for s in stems if s in new_set]
        old_in_cat = [s for s in stems if s in old_set]
        if not new_in_cat or not old_in_cat:
            continue

        for ns in new_in_cat:
            new = pages[ns]
            for os_ in old_in_cat:
                if os_ == ns:
                    continue
                old = pages[os_]
                pair = frozenset({ns, os_})
                if pair in seen_pairs:
                    continue
                if ns in old["relations"] or os_ in new["relations"]:
                    continue
                gap = (new["date"] - old["date"]).days / 365.25
                if gap < min_gap:
                    continue
                seen_pairs.add(pair)
                candidates.append({
                    "old_stem":    os_,
                    "new_stem":    ns,
                    "gap_years":   round(gap, 1),
                    "cat":         cat,
                    "old_title":   old["title"],
                    "new_title":   new["title"],
                    "old_date":    old["date"].strftime("%Y-%m-%d"),
                    "new_date":    new["date"].strftime("%Y-%m-%d"),
                    "old_ev":      old["evidence"],
                    "new_ev":      new["evidence"],
                    "old_summary": old["summary"],
                    "new_summary": new["summary"],
                })

    candidates.sort(key=lambda x: -x["gap_years"])
    return candidates[:max_pairs]


# ─── Opus judgment ──────────────────────────────────────────────────────────

JUDGE_PROMPT = """\
두 치과학 논문 페이지를 비교해 supersession 여부를 판단한다.

**구형 논문 ({old_date}, {old_ev})**
제목: {old_title}
세줄요약:
{old_summary}

**신형 논문 ({new_date}, {new_ev})**
제목: {new_title}
세줄요약:
{new_summary}

날짜 차이: {gap_years}년 | 카테고리: {cat}

판단 기준:
- 같은 임상 질문을 다루면서 신형이 더 높은 근거 등급이거나 더 큰 샘플 → full supersession
- 일부 하위 질문만 대체 → partial supersession
- 단순 연관·참조 관계 → no supersession
- 결론 상충 → counterpoint (supersession 아님)

응답 형식 (JSON 한 줄만):
{{"verdict": "full"|"partial"|"no"|"counterpoint", "reason": "한 문장", "confidence": "high"|"medium"|"low"}}
"""


def judge_pair(pair: dict, model: str = "qwen2.5:3b") -> dict:
    """Ollama HTTP API로 로컬 판단 — API 키 불필요."""
    import urllib.request, urllib.error
    prompt = JUDGE_PROMPT.format(**pair)
    payload = json.dumps({
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0, "num_predict": 200},
    }).encode()
    try:
        req = urllib.request.Request(
            "http://localhost:11434/api/generate",
            data=payload,
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=60) as resp:
            raw = json.loads(resp.read())["response"].strip()
        m = re.search(r"\{.*?\}", raw, re.DOTALL)
        if m:
            return json.loads(m.group())
        return {"verdict": "unknown", "reason": raw[:150], "confidence": "low"}
    except Exception as e:
        return {"verdict": "error", "reason": str(e)[:100], "confidence": "low"}


# ─── output ─────────────────────────────────────────────────────────────────

def render_report(candidates: list[dict], args) -> str:
    lines = [
        f"# Supersession Candidates — {date.today().isoformat()}",
        f"방법: 같은 카테고리 내 고근거(sr+ma·sr·rct) 쌍, 날짜 차이 ≥ {args.min_gap}년, 기존 엣지 제외",
    ]
    if args.new_window:
        lines.append(f"신형 범위: 최근 {args.new_window}일 인제스트된 논문")
    lines += [f"후보 수: {len(candidates)}쌍", ""]

    for i, c in enumerate(candidates, 1):
        verdict = c.get("judgment", {})
        v_str = ""
        if verdict:
            v = verdict.get("verdict", "?")
            conf = verdict.get("confidence", "?")
            reason = verdict.get("reason", "")
            emoji = {"full": "🔴", "partial": "🟡", "no": "⚪", "counterpoint": "🔵"}.get(v, "❓")
            v_str = f"\n**Opus 판단**: {emoji} `{v}` ({conf}) — {reason}"

        lines += [
            f"## {i}. [{c['cat']}] {c['old_stem']} → {c['new_stem']}",
            f"날짜 차이 {c['gap_years']}년 | 구형 {c['old_ev']} → 신형 {c['new_ev']}",
            "",
            f"**구형** ({c['old_date']}): {c['old_title']}",
            f"> {c['old_summary'][:300].strip()}" if c["old_summary"] else "> (요약 없음)",
            "",
            f"**신형** ({c['new_date']}): {c['new_title']}",
            f"> {c['new_summary'][:300].strip()}" if c["new_summary"] else "> (요약 없음)",
        ]
        if v_str:
            lines.append(v_str)
        lines.append("")

    if not args.judge:
        lines += ["---",
                  "Opus 판단 추가: `python3 scripts/find-supersession-candidates.py --judge`"]
    return "\n".join(lines) + "\n"


# ─── main ───────────────────────────────────────────────────────────────────

def main() -> int:
    ap = argparse.ArgumentParser(description="카테고리 기반 supersession 후보 탐지 (임베딩 불필요)")
    ap.add_argument("--min-gap",    type=float, default=2.0,
                    help="구형·신형 최소 날짜 차이(년). 기본 2.0")
    ap.add_argument("--new-window", type=int,   default=None,
                    help="신형 논문 범위(일, 파일 mtime 기준). 미지정=전체. 예: 30=1개월")
    ap.add_argument("--max-pairs",  type=int,   default=30,
                    help="출력할 최대 후보 쌍 수. 기본 30")
    ap.add_argument("--judge",      action="store_true",
                    help="로컬 Ollama 모델로 각 쌍 판단")
    ap.add_argument("--judge-model", default="qwen2.5:3b",
                    help="Ollama 모델명. 기본 qwen2.5:3b")
    ap.add_argument("--stdout",     action="store_true",
                    help="콘솔에도 출력")
    args = ap.parse_args()

    print("📋  페이지 수집 중…", file=sys.stderr)
    pages = collect_pages()
    print(f"    {len(pages)}편 로드", file=sys.stderr)

    print("🔍  후보 탐색 중…", file=sys.stderr)
    candidates = find_candidates(pages, args.min_gap, args.max_pairs, args.new_window)
    print(f"    {len(candidates)}쌍 발견", file=sys.stderr)

    if args.judge and candidates:
        print(f"🤖  로컬 판단 중 [{args.judge_model}] ({len(candidates)}쌍)…", file=sys.stderr)
        for c in candidates:
            c["judgment"] = judge_pair(c, model=args.judge_model)
            v = c["judgment"].get("verdict", "?")
            print(f"    {c['old_stem'][:40]} → {c['new_stem'][:40]} : {v}", file=sys.stderr)

    report = render_report(candidates, args)
    LOGS.mkdir(exist_ok=True)
    out = LOGS / f"{date.today().isoformat()}_supersession-candidates.md"
    out.write_text(report, encoding="utf-8")
    print(f"✅  로그 → logs/{out.name}", file=sys.stderr)

    if args.stdout:
        print(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
