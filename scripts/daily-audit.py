#!/usr/bin/env python3
"""
LLM Wiki — Daily Audit Runner

One entry-point that runs all 21 audits and writes their logs to logs/.

The list below is in AUDITS order — keep them in sync. (2026-07-17: the docstring said
"14 audits" and omitted five entirely — doi-duplicate-check, overview-coverage-lint,
output-coverage-lint, recall-coverage-lint, deviation-audit. AUDITS.md had drifted the
same way. Bumping the count without listing the missing ones would have been worse:
it would claim 19 while naming 14.)

NOT here: the build-* scripts (9 of them; counted 2026-07-17, not eyeballed). They
regenerate artifacts rather than report state, and they run on three different paths:

  - 6 in .github/workflows/deploy-pages.yml, which fires on push to wiki/** —
    build-category-map, build-overviews-map, build-contradiction-radar,
    build-wiki-stats, build-interactives-index, build-lectures-index.
    (That workflow also invokes interactive-staleness.py, but that is an AUDIT run
    there with `|| true`, not a build. Counting `python3 scripts/...` lines in the
    YAML gives 7 and is wrong — this exact miscount shipped here once already.)
  - 1 on launchd (Mon 09:00) — build-weekly-digest, via .claude/scripts/weekly-digest.sh
  - 2 manual — build-lecture-quiz (which calls build-quiz)

Why they are not here: the line is not read-only-vs-writes — it is what breaks when it
does not run. A skipped audit leaves you ignorant; a skipped build leaves the published
site lying. So a build belongs at the moment its artifact reaches a consumer (deploy),
not in a local daily report. Same principle already stated in interactive-staleness.py:
meta/stats tools are exempt from staleness because deploy regenerates them wholesale.

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

Three coverage signals (non-blocking) — the input/output/retention axes:
  - overview-coverage-lint.py → overview body cov%: of the papers a page links, how many
                               are actually cited inline (author+year) outside Related
                               Papers/source_papers. Low = paper linked but not reasoned with.
  - output-coverage-lint.py  → the Express mirror of synthesis-backlog: is an overview
                               pulled through into slides/ · interactives/ · lectures?
  - recall-coverage-lint.py  → overviews with no recall/{stem}.json spec = 'memory backlog'
                               (retention axis, paired with output-coverage). Forward-only.

One cross-stem duplicate signal (non-blocking):
  - doi-duplicate-check.py   → same DOI under different stems, plus a normalized-title
                               fallback for papers whose DOI is missing/mismatched.
                               orphan-check only enforces stem-level papers↔sources 1:1.

One supersession + decay signal (non-blocking):
  - supersession-audit.py → dangling superseded_by, field↔banner sync, decay candidates

Three graph/integrity signals (non-blocking):
  - relations-audit.py    → typed relation targets, vocab, typed-edge JSON export,
                            plus CIRCULAR reinforces (derived doc claiming to
                            independently confirm its own source) as a separate count
  - link-integrity.py     → broken body wikilinks, index.md two-way coverage
                            (counts a wikilink ANYWHERE in index.md as coverage)
  - overview-catalogue-lint.py → narrower companion to the above: does each overview have
                            its own '- [[overviews/x]]' catalogue bullet, i.e. is it
                            findable by someone scanning the list rather than searching?
                            A page mentioned only inside another entry's prose passes
                            link-integrity and fails here (verified 2026-07-18 against the
                            6-week patient-consultation-communication-protocol case).

One interactive-tool freshness signal (non-blocking):
  - interactive-staleness.py → clinical interactive's source_wiki newer than tool
                               (STALE → LLM re-author candidate) or BROKEN source path.
                               meta/stats tools excluded (build-wiki-stats.py regenerates them).

One contradiction-radar backfill signal (non-blocking):
  - find-contradiction-candidates.py → pages with explicit conflict language but no
                               relations: typed edge of ANY type on that pair (radar gap).
                               Signal only — LLM judges each candidate, does not auto-write.

One content-lint signal (non-blocking, deterministic):
  - content-lint.py → body content rules lint.py can't see: (A) mandatory bilingual
                               세줄요약 pair + overview 한국어 핵심요약 callout, (B) heading
                               tag consistency (확인/미검증), (C) wiki↔source cross-tier
                               integrity (source: → sources/ existence, pmid match),
                               (D) legacy frontmatter key confidence: (renamed to
                               evidence_level: 2026-07-15) — invisible to every other
                               audit because consumers read both keys.
                               No LLM — the deterministic 80% of an ingest-verification gate.

One retraction signal (non-blocking):
  - retraction-audit.py     → pages with retraction_status: RETRACTED must carry the warning
                               in their SECTION HEADINGS (a top callout does not survive RAG
                               chunking), the three required sections, and zero typed edges
                               in either direction. Also flags pages that declare themselves
                               retracted but lack the field.

One overview-volatility signal (non-blocking):
  - overview-volatility-audit.py → overview 단위 흔들림 지수(OVI). 새 신호를 모으지 않고
                               기존 감사들이 페이지 단위로 흩어놓은 것을 종합 단위로 롤업해
                               "내가 내린 결론 중 어느 것이 먼저 뒤집힐까"로 정렬한다.
                               성분: (1)마지막 thesis 편집 이후 유입 논문 (2)thesis 노후
                               (3)구성 논문 간 contradicts/refines (4)고근거 decay 비율
                               (5)최신 공백. 철회 논문 포함은 점수가 아니라 하드 플래그
                               (점수에 녹이면 묻힌다). 정비 커밋(overview 10편 이상 동시
                               수정)은 thesis 판정에서 제외 — 넣으면 229편 필드 마이그레이션
                               하나에 전편 나이가 붕괴한다. 가중치·티어 경계는 캘리브레이션
                               전 잠정값. HTML은 --html 로만 (아티팩트는 deploy 시점).

One SOP-revision trigger (non-blocking):
  - deviation-audit.py       → reads logs/ingest-deviations.md and counts per type;
                               any type at ≥3 occurrences is flagged as an SOP revision
                               candidate (Rule of Three).

Exit code:
    0 if all classic audits + ingest-rationale pass.
    1 if any of those fail.
    The 17 signals never fail — they are informational (AUDITS.md: signal, not gate).

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
    ("overview-catalogue-lint.py",   [],       False),
    ("interactive-staleness.py",     [],       False),
    ("find-contradiction-candidates.py", [],   False),
    ("content-lint.py",                  [],          False),
    ("retraction-audit.py",              [],   False),
    ("deviation-audit.py",               [],   False),
    ("overview-volatility-audit.py",     [],   False),
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
        if script in {"synthesis-backlog.py", "category-overflow.py", "overview-thesis-staleness.py", "overview-coverage-lint.py", "output-coverage-lint.py", "recall-coverage-lint.py", "doi-duplicate-check.py", "supersession-audit.py", "relations-audit.py", "link-integrity.py", "overview-catalogue-lint.py", "interactive-staleness.py", "find-contradiction-candidates.py", "content-lint.py", "retraction-audit.py"}:
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
