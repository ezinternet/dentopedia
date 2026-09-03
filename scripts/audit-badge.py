#!/usr/bin/env python3
"""
LLM Wiki — Audit Badge Emitter  (T1 of agenda/2026-09-03_audit-gap-closure.md)

NOT an audit. This collects no new signal — it reads the day's audit logs and
emits ONE badge for the morning-briefing pipeline, so the top signals surface
without anyone opening logs/.

Why this exists: AUDITS.md names the weak link itself — "Audits only compound if
someone reads them; leaving that to memory is the weak link." As of 2026-09-03 a
single day's run produces STALE 5 + decay 308 + uncovered 234 + Tier2 50. The
bottleneck stopped being detection and became reading. Designed 2026-07-15
(agenda/2026-07-15_audit-to-briefing-bridge.md), unimplemented for 7 weeks.

Two design rules carry the whole script:

  1. SILENT WHEN CLEAN. Zero counts → visible:false → the briefing renders no
     badge. A badge that shows up every morning saying "0 · 0 · 0" trains the
     reader to skip it, and then it is worth less than nothing. Same principle
     that runs through deviation-audit and the contradiction radar: an
     unsuppressed signal cannot be turned off, and a signal that cannot be
     turned off becomes noise.

  2. A MISSING LOG IS NOT A ZERO. If an audit did not run, crashed, or renamed
     its log, the naive parse yields 0 and the badge reports all-clear — the
     exact failure this repo keeps re-learning (2026-08-25: 21 green audits
     while the deploy had been dead 29 hours; 2026-08-31: a rule that lived in
     prose with nothing reading it). So an unparseable or absent log sets
     `degraded` and the badge SHOWS ITSELF for that reason alone.

Exit code is always 0. This runs after the audits and must never turn a healthy
run red — it is a mirror on a mirror.

Usage:
    python3 scripts/audit-badge.py [--date YYYY-MM-DD] [--logs-dir logs] [--quiet]
"""

from __future__ import annotations   # keep working on the system python3 (3.9)

import argparse
import datetime as _dt
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LOGS = REPO / "logs"

# ── Signal registry ──────────────────────────────────────────────────────────
#
# Each entry: (key, log suffix, label, severity, extractor).
# The extractor returns an int, or None when the number could not be found —
# None means "unknown", never "zero" (design rule 2).
#
# Severity drives ordering in the badge string, not filtering. Everything
# non-zero shows; severity only decides what the reader's eye hits first.
#
# The set is deliberately SMALL. Every audit's count could go here; then the
# badge would be a second logs/ and would need its own badge. These five are the
# ones whose non-zero state means "open something today":
#   retracted-in-overview → a live overview is assembled from a retracted paper
#   broken-link           → deployed site 404s
#   ovi-red               → a conclusion is the most likely one to flip
#   thesis-warn           → an overview's thesis has gone unrevised 90-180d
#   category-overflow     → ≥5 unsynthesized papers piled up in one category
#
# decay candidates (308 on 2026-09-03) are deliberately NOT here until T6 gives
# them a suppression window — adding an unsuppressed 308 would drown the badge
# on day one, which is the failure this file is supposed to prevent.

SEV_CRITICAL, SEV_HIGH, SEV_MEDIUM = "critical", "high", "medium"


def _rel(p: Path) -> str:
    """Repo-relative when possible, absolute otherwise.

    `Path.relative_to` RAISES for a path outside the repo, and --logs-dir may
    point anywhere (selftest fixtures, a copied log set). A cosmetic path label
    must never be able to crash a script whose entire contract is "exit 0".
    """
    try:
        return str(p.relative_to(REPO))
    except ValueError:
        return str(p)


def _grep_int(text: str, pattern: str):
    """First capture group of `pattern` as int, or None if it never matches."""
    m = re.search(pattern, text, re.M)
    return int(m.group(1)) if m else None


def x_thesis_warn(t: str):
    return _grep_int(t, r"^WARN\s*\([^)]*\)\s*:\s*(\d+)")


def x_category_overflow(t: str):
    return _grep_int(t, r"^CATEGORIES candidates\s*:\s*(\d+)")


def x_broken_link(t: str):
    """Broken wikilinks + wrong paths.

    WRONG PATH is folded in on purpose: link-integrity resolves by stem only, so
    a wrong folder passes the broken check while 404-ing on the deployed Quartz
    site. Both mean the same thing to a reader — a link that does not arrive.
    """
    broken = _grep_int(t, r"BROKEN body wikilinks\s*:\s*(\d+)")
    fixable = _grep_int(t, r"WRONG PATH \(auto-fixable\)\s*:\s*(\d+)")
    ambiguous = _grep_int(t, r"WRONG PATH \(ambiguous\)\s*:\s*(\d+)")
    parts = [p for p in (broken, fixable, ambiguous) if p is not None]
    if not parts:
        return None
    return sum(parts)


def x_ovi_red(t: str):
    return _grep_int(t, r"^##\s*적색[^(]*\((\d+)편\)")


# Stable anchor for the volatility log. Used to tell "this section is
# legitimately absent" apart from "this is not the log I think it is" — the one
# distinction that decides whether absence means 0 or unknown.
VOLATILITY_ANCHOR = re.compile(r"Overview Volatility Index")


def x_retracted_in_overview(t: str):
    """Overviews whose constituent papers include a retracted one.

    Counted from the volatility log's hard-flag block rather than
    retraction-audit: retraction-audit answers "is the retracted PAGE built
    correctly", which is structural hygiene. The question that needs a badge is
    the downstream one — "is a live conclusion still standing on it".

    ⚠ This block is CONDITIONAL at the source: overview-volatility-audit.py:456
    emits it under `if flagged:`, so a clean day has no block at all — unlike
    the tier sections, which always print even at (0편). Treating its absence as
    "parse failed" would fire a false degraded EVERY clean day, i.e. the moment
    the current 4 flags get fixed the badge would start crying wolf forever.
    So absence means 0 — but only once the anchor proves we are reading a
    volatility log. Without that check, a truncated or renamed file would read
    as all-clear, which is design rule 2's failure in the other direction.
    """
    if not VOLATILITY_ANCHOR.search(t):
        return None
    m = re.search(r"^##[^\n]*철회 하드 플래그[^\n]*\n(.*?)(?=^##|\Z)", t, re.M | re.S)
    if not m:
        return 0        # anchor present, block absent → genuinely none flagged
    return len(re.findall(r"^\s*-\s*\[\[", m.group(1), re.M))


SIGNALS = [
    ("retracted-in-overview", "volatility",                 "철회논문 포함 overview", SEV_CRITICAL, x_retracted_in_overview),
    ("broken-link",           "link-integrity",             "깨진 링크",              SEV_HIGH,     x_broken_link),
    ("ovi-red",               "volatility",                 "OVI 적색",               SEV_HIGH,     x_ovi_red),
    ("thesis-warn",           "overview-thesis-staleness",  "thesis stale",           SEV_MEDIUM,   x_thesis_warn),
    ("category-overflow",     "category-overflow",          "카테고리 적체",          SEV_MEDIUM,   x_category_overflow),
]

SEV_ORDER = {SEV_CRITICAL: 0, SEV_HIGH: 1, SEV_MEDIUM: 2}


def collect(date: str, logs_dir: Path) -> dict:
    cache: dict[str, str] = {}
    signals, degraded = [], []

    for key, suffix, label, severity, extract in SIGNALS:
        path = logs_dir / f"{date}_{suffix}.log"
        if suffix not in cache:
            try:
                cache[suffix] = path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                cache[suffix] = ""
        text = cache[suffix]

        if not text:
            degraded.append(f"{label}: 로그 없음 ({path.name})")
            count = None
        else:
            count = extract(text)
            if count is None:
                # The log exists but the line we key on is gone — an audit
                # changed its output format. Louder than a zero, on purpose.
                degraded.append(f"{label}: 파싱 실패 ({path.name})")

        signals.append({
            "key": key,
            "label": label,
            "severity": severity,
            "count": count,
            "log": _rel(path) if path.exists() else None,
        })

    signals.sort(key=lambda s: (SEV_ORDER[s["severity"]], -(s["count"] or 0)))
    hits = [s for s in signals if s["count"]]

    if degraded:
        text = "🔍 위키 감사: ⚠ 신호 불명 — " + " · ".join(degraded)
    elif hits:
        text = "🔍 위키 감사: " + " · ".join(f"{s['label']} {s['count']}" for s in hits)
    else:
        text = ""

    return {
        "date": date,
        "generated_at": _dt.datetime.now().isoformat(timespec="seconds"),
        # visible drives the briefing's render decision — the consumer should
        # need no logic of its own beyond `if badge["visible"]`.
        "visible": bool(hits or degraded),
        "degraded": degraded,
        "badge": text,
        "signals": signals,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Emit the daily audit badge (post-processing, not an audit).")
    ap.add_argument("--date", default=_dt.date.today().isoformat(), help="YYYY-MM-DD (default: today)")
    ap.add_argument("--logs-dir", default=str(LOGS), help="directory holding {date}_*.log")
    ap.add_argument("--quiet", action="store_true", help="write the JSON, print nothing")
    ap.add_argument("--selftest", action="store_true", help="run parser regression cases and exit")
    args = ap.parse_args()

    if args.selftest:
        return selftest()

    badge = collect(args.date, Path(args.logs_dir))
    out = Path(args.logs_dir) / f"{args.date}_badge.json"
    try:
        out.write_text(json.dumps(badge, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    except OSError as e:
        if not args.quiet:
            print(f"    ⚠ 배지 파일 쓰기 실패: {e}")
        return 0        # never fail the run

    if not args.quiet:
        if badge["visible"]:
            print(f"    {badge['badge']}")
            print(f"      → {_rel(out)}")
        else:
            # Silence is the whole point — say so once, tersely, so the operator
            # can tell "clean" apart from "the emitter did not run".
            print("    ✅  표면화할 신호 없음 — 배지 숨김")
    return 0


# ── Regression cases ─────────────────────────────────────────────────────────
# Pinned against the real 2026-09-03 log formats. Run this before touching a
# regex: every extractor here is coupled to another script's stdout, which is
# exactly the coupling that rots silently.

def selftest() -> int:
    cases = [
        ("thesis WARN",      x_thesis_warn,           "TOTAL overviews : 287\nWARN (90-180d)         : 3\nINFO (≥180d)            : 0\n", 3),
        ("thesis WARN zero", x_thesis_warn,           "WARN (90-180d)         : 0\n", 0),
        ("thesis missing",   x_thesis_warn,           "TOTAL overviews : 287\n", None),
        ("category cand",    x_category_overflow,     "CATEGORIES total       : 121\nCATEGORIES candidates  : 4\n", 4),
        ("link sum",         x_broken_link,           "  BROKEN body wikilinks : 2\n  WRONG PATH (auto-fixable) : 3\n  WRONG PATH (ambiguous)    : 1\n", 6),
        ("link zero",        x_broken_link,           "  BROKEN body wikilinks : 0\n  WRONG PATH (auto-fixable) : 0\n  WRONG PATH (ambiguous)    : 0\n", 0),
        ("link missing",     x_broken_link,           "wiki pages : 3515\n", None),
        ("ovi red",          x_ovi_red,               "## 적색 — 재검토 우선 (1편)\n\n### 33.3 [[x]]\n", 1),
        ("ovi red absent",   x_ovi_red,               "## 주황 — 관찰 (5편)\n", None),
        ("retracted flags",  x_retracted_in_overview, "# Overview Volatility Index — 2026-09-03\n\n## ⚠️ 철회 하드 플래그 (점수 무관·최우선)\n- [[a]] — x\n- [[b]] — y\n\n## 적색 — 재검토 우선 (1편)\n### 33.3 [[c]]\n", 2),
        # the flag block must not swallow the section after it
        ("retracted none",   x_retracted_in_overview, "# Overview Volatility Index — 2026-09-03\n\n## ⚠️ 철회 하드 플래그 (점수 무관·최우선)\n\n## 적색 — 재검토 우선 (2편)\n### 30 [[c]]\n### 29 [[d]]\n", 0),
        # the block is emitted only `if flagged:` — a clean volatility log has no
        # block at all and MUST read 0, or every clean day fires a false degraded
        ("retracted clean-day", x_retracted_in_overview, "# Overview Volatility Index — 2026-09-03\n\n## 적색 — 재검토 우선 (0편)\n", 0),
        # …but a file that is not a volatility log at all stays unknown
        ("retracted wrong-log", x_retracted_in_overview, "## 적색 — 재검토 우선 (1편)\n", None),
        ("retracted truncated", x_retracted_in_overview, "", None),
    ]
    bad = 0
    for name, fn, text, want in cases:
        got = fn(text)
        ok = got == want
        bad += not ok
        print(f"  {'✓' if ok else '✗'} {name:<18} got={got!r:<8} want={want!r}")

    # A missing log must degrade, never read as all-clear.
    empty = collect("1999-01-01", Path("/nonexistent"))
    for label, cond in (
        ("missing logs → degraded", bool(empty["degraded"])),
        ("missing logs → visible",  empty["visible"] is True),
        ("missing logs → count None", all(s["count"] is None for s in empty["signals"])),
    ):
        bad += not cond
        print(f"  {'✓' if cond else '✗'} {label}")

    print(f"\n{'✅ selftest OK' if not bad else f'❌ {bad} case(s) failed'}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
