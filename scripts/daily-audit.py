#!/usr/bin/env python3
"""
LLM Wiki — Daily Audit Runner

One entry-point that runs all 9 audits and writes their logs to logs/.

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
    ("doi-duplicate-check.py",       [],       False),
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

    for script, args, must_pass in AUDITS:
        print(f"▸ {script}")
        code, out = run_audit(script, args)
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
        if script in {"synthesis-backlog.py", "category-overflow.py", "overview-thesis-staleness.py", "overview-coverage-lint.py", "doi-duplicate-check.py"}:
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
