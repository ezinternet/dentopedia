#!/usr/bin/env python3
from __future__ import annotations  # PEP 604 unions must run on Python 3.9
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


def read_decay_reviews(path):
    """logs/decay-reviewed.md → {stem: (date, verdict, reason)}. 없으면 빈 dict."""
    import datetime as _dt
    out = {}
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return out
    for line in text.splitlines():
        m = re.match(r"^\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*$", line)
        if not m:
            continue
        try:
            d = _dt.date.fromisoformat(m.group(1))
        except ValueError:
            continue
        out[m.group(2).strip()] = (d, m.group(3).strip(), m.group(4).strip())
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--decay-years", type=int, default=5)
    # ── decay 억제 3겹 (2026-09-03) ─────────────────────────────────────────
    # 원판은 후보 334건을 통째로 뱉었다. deviation-audit이 334건에서 배운 것과
    # 같은 상태다: *억제되지 않는 신호는 끌 수 없고, 끌 수 없는 신호는 노이즈가
    # 된다.* 억제는 **뮤트가 아니라 이동** — 제외분도 계속 세어 출력한다.
    ap.add_argument("--decay-inbound-min", type=int, default=10,
                    help="중심성 하한. 아무도 안 거는 오래된 논문은 검증 우선순위가 아니다")
    ap.add_argument("--decay-per-category", type=int, default=3,
                    help="카테고리당 상위 N만. 실제 갱신은 클러스터 단위로 일어난다 "
                         "(2026-05-31 triage: ARP SR 한 편이 여러 편을 동시에 supersede)")
    ap.add_argument("--decay-ledger", default=None,
                    help="대장 경로 override (억제 경로 테스트용)")
    ap.add_argument("--decay-review-window", type=int, default=365,
                    help="logs/decay-reviewed.md 등재 후 재검토까지의 일수")
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
    chain_declared = []  # (stem, direct_target, chain_tail) — mid-chain pointer declared intentional
    chain_intentional = set()  # stems carrying `supersession_chain: intentional`
    decay = []           # (years, stem, confidence, date_str)

    for stem, path in pages.items():
        content = path.read_text(encoding="utf-8")
        fm = parse_fm(content)
        if fm is None:
            continue

        field_targets = split_stems(fm.get("superseded_by", ""))
        scope = (fm.get("superseded_scope", "") or "").lower()
        # partial supersession은 축(axis)별로 일어나므로 전이되지 않는다: A가 B에 대체된 축을
        # C가 넘겨받지 않았다면 A의 포인터는 B에 남는 게 맞다. 그 판단을 내렸으면
        # `supersession_chain: intentional`로 선언하고 **배너에 이유를 적는다**(선언만 하고
        # 이유가 없으면 다음 사람이 재판단할 수 없다). 선언은 숨기지 않고 별도 집계로 보인다.
        if (fm.get("supersession_chain", "") or "").strip().lower() == "intentional":
            chain_intentional.add(stem)
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
        conf = (fm.get("evidence_level") or fm.get("confidence") or "").lower()
        if conf in DECAY_CONFIDENCE:
            dt = parse_date(fm.get("date") or fm.get("year"))
            if dt is not None and dt <= decay_cutoff:
                yrs = round((today - dt).days / 365.25, 1)
                cat = str(path.relative_to(WIKI_DIR)).split("/")[0]
                decay.append((yrs, stem, conf, dt.strftime("%Y-%m-%d"), cat, inbound.get(stem, 0)))

    # centrality(inbound) 우선, 동률이면 age — "남이 많이 의존하는 오래된 고근거" 먼저
    decay.sort(key=lambda x: (-x[5], -x[0]))

    # ── 억제 3겹 ────────────────────────────────────────────────────────────
    reviews = read_decay_reviews(Path(args.decay_ledger) if args.decay_ledger else LOGS_DIR / "decay-reviewed.md")
    # `today`는 이 스크립트에서 datetime, 대장은 date를 낸다 — 빼기 전에 맞춘다.
    # (빈 대장에서는 이 루프가 아예 안 돌아 타입 불일치가 드러나지 않는다. 억제
    #  경로는 대장이 비어 있는 한 실행되지 않으므로 반드시 채워서 시험할 것.)
    today_d = today.date() if hasattr(today, "date") else today
    reviewed_recent = {
        stem for stem, (d, verdict, _) in reviews.items()
        if verdict == "still-current" and (today_d - d).days <= args.decay_review_window
    }
    from collections import defaultdict as _dd
    per_cat = _dd(int)
    actionable, sup_reviewed, sup_low, sup_cat = [], [], [], []
    for row in decay:                      # (yrs, stem, conf, dstr, cat, ib)
        stem, cat, ib = row[1], row[4], row[5]
        if stem in reviewed_recent:
            sup_reviewed.append(row)
        elif ib < args.decay_inbound_min:
            sup_low.append(row)
        elif per_cat[cat] >= args.decay_per_category:
            sup_cat.append(row)
        else:
            per_cat[cat] += 1
            actionable.append(row)

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
                if stem in chain_intentional:
                    chain_declared.append((stem, t, node))
                else:
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
    L.append(f"  chain intentional (선언) : {len(chain_declared)}")
    L.append(f"decay candidates (≥{args.decay_years}y, {'/'.join(sorted(DECAY_CONFIDENCE))}, not superseded): {len(decay)}")
    L.append(f"  └ 지금 검증할 것: {len(actionable)}   (억제: 검증됨 {len(sup_reviewed)} · 카테고리 상위밖 {len(sup_cat)} · 저중심성 {len(sup_low)})")
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
    if chain_declared:
        L.append("=== chain intentional — mid-chain pointer declared deliberate ===")
        L.append("    (`supersession_chain: intentional`. 대체 축이 서로 달라 전이되지 않는 경우.")
        L.append("     이유는 각 페이지 배너에 있다 — 재판단하려면 거기부터 읽을 것.)")
        for stem, direct, tail in sorted(chain_declared):
            L.append(f"  {stem}  →  {direct}  (chain tail {tail} — 의도적으로 미채택)")
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
        L.append(f"=== DECAY — 지금 검증할 것 ({len(actionable)}건) ===")
        L.append(f"  기준: 중심성 ib≥{args.decay_inbound_min} · 카테고리당 상위 {args.decay_per_category} · "
                 f"최근 {args.decay_review_window}일 내 'still-current' 판정 제외")
        for yrs, stem, conf, dstr, cat, ib in actionable:
            L.append(f"  ib={ib:>2}  {yrs:>5}y  [{conf:>5}]  {cat}/{stem}  ({dstr})")
        L.append("")
        L.append("--- 참고 — 억제된 후보 (뮤트 아님, 이동) ---")
        L.append(f"  {len(sup_reviewed):>3}  최근 검증됨 (logs/decay-reviewed.md)")
        L.append(f"  {len(sup_cat):>3}  같은 카테고리 상위 {args.decay_per_category}건 밖 — 클러스터 갱신 시 함께 처리")
        L.append(f"  {len(sup_low):>3}  중심성 ib<{args.decay_inbound_min} — 아무도 의존하지 않는 오래된 고근거")
        if sup_cat:
            L.append("")
            L.append("  카테고리별 잔여(상위 밖):")
            rest = _dd(int)
            for r in sup_cat:
                rest[r[4]] += 1
            for cat in sorted(rest, key=lambda k: -rest[k])[:12]:
                L.append(f"    {rest[cat]:>3}  {cat}")
        L.append("")

    body = "\n".join(L) + "\n"
    log_path.write_text(body, encoding="utf-8")

    issues = len(dangling) + len(banner_missing) + len(banner_orphan) + len(banner_mismatch) + len(chain_stale)
    flag = "⚠" if issues else "✓"
    declared = f", {len(chain_declared)} chain-intentional" if chain_declared else ""
    print(f"🔁  Supersession: {len(superseded_ok)} superseded, {issues} sync issues {flag}{declared}, {len(actionable)} decay 검증대상 (전체 {len(decay)})")
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
