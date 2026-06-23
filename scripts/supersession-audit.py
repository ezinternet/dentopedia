#!/usr/bin/env python3
"""
LLM Wiki — Supersession + Confidence-Decay Audit (signal, non-blocking)

Living-document 원칙을 수동 산문 갱신에서 신호 기반으로 전환한다.
저장하는 건 사실(`superseded_by`)뿐이고, decay는 이 audit이 매 실행마다 계산한다.
(저장된 decay 값은 그 자체가 stale해진다 — overview-thesis-staleness.py와 동일한 교훈.)

스키마 (superseded=구판 페이지의 frontmatter):
    superseded_by: <newer-stem>        # 복수면 comma-separated. wiki 내 실존 stem.
    superseded_scope: full             # full | partial

본문 배너 (frontmatter 직후):
    > [!warning] Superseded (full) → [[newer-stem]]
    > 사유. (set YYYY-MM-DD)
  partial이면 [!note] Partially superseded.

세 가지 검사:
  (A) DANGLING   — superseded_by가 가리키는 stem이 wiki에 없음.
  (B) BANNER-SYNC— 필드 있는데 배너 없음 / 배너 있는데 필드 없음 / target stem 불일치.
  (C) DECAY      — confidence ∈ {sr+ma, sr, rct} AND date ≥ N년 경과 AND superseded_by 없음
                   → "still current 검증 필요" 후보.

Output: logs/{date}_supersession.log
Exit: 항상 0 (signal, non-blocking). daily-audit.py 통합 시 must_pass=False.

Usage:
    python3 scripts/supersession-audit.py
    python3 scripts/supersession-audit.py --stdout
    python3 scripts/supersession-audit.py --decay-years 5
"""

import re
import sys
import argparse
from datetime import date, datetime
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = WIKI_ROOT / "wiki"
LOGS_DIR = WIKI_ROOT / "logs"

SKIP_DIRS = {"_lint"}
SKIP_FILES = {"index.md"}

# decay 후보로 볼 고근거 confidence 등급
DECAY_CONFIDENCE = {"sr+ma", "sr", "rct"}

FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
# 배너 헤더 라인: "> [!warning] Superseded ..." / "> [!note] Partially superseded ..."
# (한 라인에 [[stem]]이 여러 개일 수 있어 헤더 라인을 먼저 잡고 wikilink를 전부 추출)
BANNER_LINE_RE = re.compile(
    r"^>\s*\[!(?:warning|note)\][^\n]*?Superseded\b[^\n]*$",
    re.IGNORECASE | re.MULTILINE,
)
WIKILINK_RE = re.compile(r"\[\[([^\]\#|]+)")


def parse_fm(content: str) -> dict | None:
    m = FM_RE.match(content)
    if not m:
        return None
    fields = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"^(\w+)\s*:\s*(.*)$", line)
        if kv:
            fields[kv.group(1)] = kv.group(2).strip().strip('"').strip("'")
    return fields


def split_stems(raw: str) -> list[str]:
    """superseded_by 값에서 stem 리스트 추출. comma-sep, [[..]] 래핑 허용."""
    if not raw:
        return []
    out = []
    for part in raw.split(","):
        s = part.strip()
        s = s.strip("[]").strip()
        # "[[category/stem]]" → 마지막 path 조각만 (Obsidian은 filename으로 resolve)
        if "/" in s:
            s = s.split("/")[-1]
        s = s.replace(".md", "").strip()
        if s:
            out.append(s)
    return out


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


def collect_pages() -> dict[str, Path]:
    """stem → path (wiki 전체). stem은 파일명에서 .md 제거."""
    pages = {}
    for f in WIKI_DIR.rglob("*.md"):
        if any(p in SKIP_DIRS for p in f.parts):
            continue
        if f.name in SKIP_FILES:
            continue
        pages[f.stem] = f
    return pages


def compute_inbound(pages: dict[str, Path]) -> dict[str, int]:
    """각 stem의 inbound wikilink 수(중심성). 자기참조·중복 제외."""
    inbound = {s: 0 for s in pages}
    for stem, path in pages.items():
        seen = set()
        for raw in WIKILINK_RE.findall(path.read_text(encoding="utf-8")):
            t = raw.split("/")[-1].replace(".md", "").strip()
            if t in pages and t != stem:
                seen.add(t)
        for t in seen:
            inbound[t] += 1
    return inbound


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--decay-years", type=int, default=5)
    ap.add_argument("--stdout", action="store_true")
    ap.add_argument(
        "--ci",
        action="store_true",
        help="CI mode: exit 1 on dangling links / banner-desync. Decay candidates still exit 0.",
    )
    args = ap.parse_args()

    if not WIKI_DIR.exists():
        print(f"  No wiki dir: {WIKI_DIR}")
        return 0

    pages = collect_pages()
    inbound = compute_inbound(pages)
    today = datetime.combine(date.today(), datetime.min.time())
    decay_cutoff = today.replace(year=today.year - args.decay_years)

    dangling = []        # (stem, bad_target)
    banner_missing = []  # field set, no banner
    banner_orphan = []   # banner present, no field
    banner_mismatch = [] # field/banner target stems differ
    superseded_ok = []   # (stem, scope, targets)
    chain_stale = []     # (stem, direct_target, chain_tail) — transitivity issue
    decay = []           # (years, stem, confidence, date_str)

    for stem, path in pages.items():
        content = path.read_text(encoding="utf-8")
        fm = parse_fm(content)
        if fm is None:
            continue

        field_targets = split_stems(fm.get("superseded_by", ""))
        scope = (fm.get("superseded_scope", "") or "").lower()
        banner_targets = []
        for line in BANNER_LINE_RE.findall(content):
            for raw in WIKILINK_RE.findall(line):
                st = split_stems(raw)
                banner_targets.append(st[0] if st else raw.strip())

        has_field = bool(field_targets)
        has_banner = bool(banner_targets)

        # (A) DANGLING
        for t in field_targets:
            if t not in pages:
                dangling.append((stem, t))

        # (B) BANNER-SYNC
        if has_field and not has_banner:
            banner_missing.append(stem)
        if has_banner and not has_field:
            banner_orphan.append(stem)
        if has_field and has_banner and set(field_targets) != set(banner_targets):
            banner_mismatch.append((stem, sorted(field_targets), sorted(banner_targets)))

        if has_field:
            superseded_ok.append((stem, scope or "full", field_targets))
            continue  # superseded 페이지는 decay 후보에서 제외

        # (C) DECAY
        conf = (fm.get("confidence", "") or "").lower()
        if conf in DECAY_CONFIDENCE:
            dt = parse_date(fm.get("date") or fm.get("year"))
            if dt is not None and dt <= decay_cutoff:
                yrs = round((today - dt).days / 365.25, 1)
                cat = str(path.relative_to(WIKI_DIR)).split("/")[0]
                decay.append((yrs, stem, conf, dt.strftime("%Y-%m-%d"), cat, inbound.get(stem, 0)))

    # centrality(inbound) 우선, 동률이면 age — "남이 많이 의존하는 오래된 고근거" 먼저
    decay.sort(key=lambda x: (-x[5], -x[0]))

    # (D) TRANSITIVITY — A → B, but B is also superseded (B → C). A's pointer is stale.
    superseded_stems = {stem for stem, _, _ in superseded_ok}
    field_map = {}  # stem → [target_stems]
    for stem, _, targets in superseded_ok:
        field_map[stem] = targets
    for stem, _, targets in superseded_ok:
        for t in targets:
            if t in field_map:
                # follow chain to the tail
                visited = {stem, t}
                node = t
                while node in field_map:
                    nexts = [x for x in field_map[node] if x not in visited]
                    if not nexts:
                        break
                    node = nexts[0]
                    visited.add(node)
                chain_stale.append((stem, t, node))

    LOGS_DIR.mkdir(exist_ok=True)
    log_path = LOGS_DIR / f"{date.today().isoformat()}_supersession.log"

    L = []
    L.append(f"# Supersession + Decay Audit — {date.today().isoformat()}")
    L.append(f"wiki pages scanned        : {len(pages)}")
    L.append(f"superseded (field set)    : {len(superseded_ok)}")
    L.append(f"  DANGLING links          : {len(dangling)}")
    L.append(f"  banner MISSING          : {len(banner_missing)}")
    L.append(f"  banner ORPHAN (no field): {len(banner_orphan)}")
    L.append(f"  field/banner MISMATCH   : {len(banner_mismatch)}")
    L.append(f"  TRANSITIVITY chain stale: {len(chain_stale)}")
    L.append(f"decay candidates (≥{args.decay_years}y, {'/'.join(sorted(DECAY_CONFIDENCE))}, not superseded): {len(decay)}")
    L.append("")

    if superseded_ok:
        L.append("=== SUPERSEDED pages (field set) ===")
        for stem, scope, targets in sorted(superseded_ok):
            L.append(f"  [{scope}] {stem}  →  {', '.join(targets)}")
        L.append("")
    if dangling:
        L.append("=== ⚠ DANGLING superseded_by (target stem not in wiki) ===")
        for stem, t in dangling:
            L.append(f"  {stem}  →  {t}  (NOT FOUND)")
        L.append("")
    if banner_missing:
        L.append("=== ⚠ field set but NO banner in body ===")
        for stem in banner_missing:
            L.append(f"  {stem}")
        L.append("")
    if banner_orphan:
        L.append("=== ⚠ banner present but NO superseded_by field ===")
        for stem in banner_orphan:
            L.append(f"  {stem}")
        L.append("")
    if banner_mismatch:
        L.append("=== ⚠ field/banner target MISMATCH ===")
        for stem, ft, bt in banner_mismatch:
            L.append(f"  {stem}  field={ft}  banner={bt}")
        L.append("")
    if chain_stale:
        L.append("=== ⚠ TRANSITIVITY — pointer points to already-superseded page ===")
        L.append("    (A → B, but B is also superseded. Update A to point to chain tail.)")
        for stem, direct, tail in sorted(chain_stale):
            L.append(f"  {stem}  →  {direct}  (should be → {tail})")
        L.append("")
    if decay:
        # 카테고리별 집계
        from collections import defaultdict
        bycat = defaultdict(list)
        for row in decay:
            bycat[row[4]].append(row)
        L.append("=== DECAY by category (count / median age / max inbound) ===")
        for cat in sorted(bycat, key=lambda k: -len(bycat[k])):
            rows = bycat[cat]
            ages = sorted(r[0] for r in rows)
            med = ages[len(ages) // 2]
            mx = max(r[5] for r in rows)
            L.append(f"  {len(rows):>3}  {cat:<22} median {med:>5}y   maxInbound {mx}")
        L.append("")
        L.append(f"=== DECAY candidates — verify still current (by centrality, top 60) ===")
        for yrs, stem, conf, dstr, cat, ib in decay[:60]:
            L.append(f"  ib={ib:>2}  {yrs:>5}y  [{conf:>5}]  {cat}/{stem}  ({dstr})")
        L.append("")

    body = "\n".join(L) + "\n"
    log_path.write_text(body, encoding="utf-8")

    issues = len(dangling) + len(banner_missing) + len(banner_orphan) + len(banner_mismatch) + len(chain_stale)
    flag = "⚠" if issues else "✓"
    print(f"🔁  Supersession: {len(superseded_ok)} superseded, {issues} sync issues {flag}, {len(decay)} decay candidates")
    print(f"      log → logs/{log_path.name}")
    if args.stdout:
        print()
        print(body)

    if args.ci and issues:
        print(f"  [CI] {issues} hard error(s) — dangling/desync/chain. Fix and re-push.")
        return 1
    return 0  # signal — always non-blocking (no --ci)


if __name__ == "__main__":
    sys.exit(main())
