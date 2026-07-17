#!/usr/bin/env python3
"""
LLM Wiki — Daily Audit Runner

One entry-point that runs all 14 audits and writes their logs to logs/.

Three classic audits (errors):
  - lint.py                  → wiki frontmatter sanity
  - operations-lint.py       → OPS cross-link chain
  - orphan-check.py          → PDF ↔ source 1:1

Three synthesis-enforcement audits (signals, errors only on rationale lint):
  - synthesis-backlog.py     → overview-unlinked sources
  - ingest-rationale-lint.py → '## Why Ingested' on post-cutoff sources
  - category-overflow.py     → categories with ≥5 unsynthesized papers

One thesis-staleness signal (git-diff based, non-blocking):
  - overview-thesis-staleness.py → overview thesis edit (non-wikilink) staleness

One supersession + decay signal (non-blocking):
  - supersession-audit.py → dangling superseded_by, field↔banner sync, decay candidates

Two graph/integrity signals (non-blocking):
  - relations-audit.py    → typed relation targets, vocab, typed-edge JSON export
  - link-integrity.py     → broken body wikilinks, index.md two-way coverage

One interactive-tool freshness signal (non-blocking):
  - interactive-staleness.py → clinical interactive's source_wiki newer than tool
                               (STALE → LLM re-author candidate) or BROKEN source path.
                               meta/stats tools excluded (build-wiki-stats.py regenerates them).

One contradiction-radar backfill signal (non-blocking):
  - find-contradiction-candidates.py → pages with explicit conflict language but no
                               relations: typed edge of ANY type on that pair (radar gap).
                               Signal only — LLM judges each candidate, does not auto-write.

One retraction signal (non-blocking):
  - retraction-audit.py     → pages with retraction_status: RETRACTED must carry the warning
                               in their SECTION HEADINGS (a top callout does not survive RAG
                               chunking), the three required sections, and zero typed edges
                               in either direction. Also flags pages that declare themselves
                               retracted but lack the field.

One content-lint signal (non-blocking, deterministic):
  - content-lint.py → body content rules lint.py can't see: (A) mandatory bilingual
                               세줄요약 pair + overview 한국어 핵심요약 callout, (B) heading
                               tag consistency (확인/미검증), (C) wiki↔source cross-tier
                               integrity (source: → sources/ existence, pmid match).
                               No LLM — the deterministic 80% of an ingest-verification gate.

Exit code:
    0 if all classic audits + ingest-rationale pass.
    1 if any of those fail.
    Synthesis-backlog / category-overflow never fail (they are signals).

Usage:
    python3 scripts/daily-audit.py
"""

import os
import sys
import subprocess
from concurrent.futures import ThreadPoolExecutor
from datetime import date

WIKI_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(WIKI_ROOT, "scripts")

# (script, args, must_pass)
AUDITS = [
    ("lint.py",                   ["--quiet"], True),
    ("operations-lint.py",        [],          True),
    ("orphan-check.py",           [],          True),
    ("synthesis-backlog.py",      [],          False),
    ("ingest-rationale-lint.py",  ["--strict"], True),
    ("category-overflow.py",      [],          False),
    ("overview-thesis-staleness.py", [],       False),
    ("overview-coverage-lint.py",    [],       False),
    ("output-coverage-lint.py",      [],       False),
    ("recall-coverage-lint.py",      [],       False),
    ("doi-duplicate-check.py",       [],       False),
    ("supersession-audit.py",        [],       False),
    ("relations-audit.py",           [],       False),
    ("link-integrity.py",            [],       False),
    ("interactive-staleness.py",     [],       False),
    ("find-contradiction-candidates.py", [],   False),
    ("content-lint.py",                  [],          False),
    ("retraction-audit.py",              [],   False),
    ("deviation-audit.py",               [],   False),
]


def run_audit(script: str, args: list[str]) -> tuple[int, str]:
    cmd = [sys.executable, os.path.join(SCRIPTS, script)] + args
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, cwd=WIKI_ROOT)
        out = (r.stdout or "") + (r.stderr or "")
        return r.returncode, out.strip()
    except Exception as e:
        return 99, f"ERROR launching {script}: {e}"


def main() -> int:
    today = date.today().isoformat()
    print(f"╔══════════════════════════════════════════════════════════════╗")
    print(f"║  LLM Wiki Daily Audit — {today}                            ║")
    print(f"╚══════════════════════════════════════════════════════════════╝")
    print()

    failures = 0
    summary: list[tuple[str, int, bool]] = []

    # Run all audits concurrently (they are read-only), then print in AUDITS order
    # so output stays deterministic. Wall-clock converges to the single slowest
    # script (e.g. ingest-rationale-lint) instead of the sum of all of them.
    print(f"▸ running {len(AUDITS)} audits in parallel…\n")
    max_workers = min(len(AUDITS), (os.cpu_count() or 4))
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        results = list(pool.map(lambda a: run_audit(a[0], a[1]), AUDITS))

    for (script, args, must_pass), (code, out) in zip(AUDITS, results):
        print(f"▸ {script}")
        for line in out.splitlines():
            print(f"    {line}")
        passed = (code == 0)
        if must_pass and not passed:
            failures += 1
        summary.append((script, code, passed))
        print()

    print("─" * 66)
    print(f"  {'audit':<32} {'exit':>5}  {'status':>8}")
    print("─" * 66)
    for script, code, passed in summary:
        status = "PASS" if passed else "FAIL"
        if script in {"synthesis-backlog.py", "category-overflow.py", "overview-thesis-staleness.py", "overview-coverage-lint.py", "output-coverage-lint.py", "recall-coverage-lint.py", "doi-duplicate-check.py", "supersession-audit.py", "relations-audit.py", "link-integrity.py", "interactive-staleness.py", "find-contradiction-candidates.py", "content-lint.py", "retraction-audit.py"}:
            status = "SIGNAL"
        print(f"  {script:<32} {code:>5}  {status:>8}")
    print("─" * 66)

    if failures:
        print(f"❌  {failures} blocking audit(s) failed")
        return 1
    print(f"✅  all blocking audits passed (signals are informational)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
