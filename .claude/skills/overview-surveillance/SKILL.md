---
name: overview-surveillance
description: 'Surveillance of existing wiki/overviews/ against PubMed — scout gaps per
  domain, show a candidate list for approval, ingest only approved papers, then fold
  them into the overviews. Invoke when the user says "오버뷰 서베일런스", "오버뷰 펍메드
  대조", "overview surveillance", or asks to check existing overviews against PubMed and
  update them. Defaults: domain required, last 2 years, ≤3 papers per overview,
  SR/RCT first, approval gate before any ingest.'
argument-hint: [ domain(s), e.g. "균열 시린이" ] [--years N] [--per N]
allowed-tools: Bash, Read, Write, Edit
---

# Overview Surveillance

Checks existing overviews against PubMed, ingests what is worth it, and updates the
overviews. **Defaults exist because the first unscoped run (2026-11-24) cost a lot.** It
scouted 21 papers and was cut to 10 mid-flight. Killed subagents left partial files that
needed cleanup and recovery, and one parallel ingest wrote another paper's summary into
a page. Keep the defaults unless the user overrides them.

| Default | Value | Override |
|---|---|---|
| Scope | Named domain(s) only; never "all overviews" | user names domains |
| Window | Last **2 years** (publication date) | `--years N` |
| Cap | **≤3 papers per overview**, ≤10 per run | `--per N` / user says so |
| Priority | SR+MA / SR / NMA > RCT > prospective cohort > rest | — |
| Abstract-only (no PMCID) | Only if it is a major SR filling a stated gap — flag it | — |
| Gate | **Candidate list → user approval → ingest** (never skip) | user says "바로 진행" explicitly |

Model routing (CLAUDE.md): scout = Sonnet, ingest = Sonnet, overview update = **Opus · high**.

## Phase 0 — Scope

- Resolve each domain to its category(ies) via `wiki/_meta/categories.md` and its overview(s):
  `ls wiki/overviews | grep -i <keyword>`. Show the mapping in one line.
- No domain given → list the 10 overviews with the oldest `date:` and ask which to run:
  ```bash
  for f in wiki/overviews/*.md; do echo "$(grep -m1 '^date:' $f | cut -d' ' -f2) $f"; done | sort | head -10
  ```

## Phase 1 — Scout (1 Sonnet subagent per domain, parallel, read-only)

Brief each scout with the following (fill in `<…>`):

> You are a read-only SCOUT for /Users/oracleneo/llm-wiki. Do not ingest, edit repo files or git.
> Domain `<category>`; overview(s) `<paths>` — read fully, note axes and stated gaps.
> 1. Held set: `grep -h -E '^(doi|pmid|pmcid):' sources/*.md | sort -u` → scratchpad.
> 2. Load PubMed MCP via ToolSearch `select:mcp__8ed3ab32-35c8-480e-9a26-27b201a118d3__search_articles,mcp__8ed3ab32-35c8-480e-9a26-27b201a118d3__get_article_metadata`. Search the last `<N>` years with domain terms `AND (free full text[sb])` plus SR/MA/RCT filters.
> 3. Drop held (DOI/PMID/PMCID, also `grep -ri` sources/), retracted, and no-PMCID papers unless they are a major SR filling a stated gap (flag them abstract-only).
> 4. Keep only papers that (a) fill a stated gap, (b) add higher or newer evidence, or (c) may supersede a held stem (name it).
> 5. Return at most `<per>` ranked candidates, under 400 words. Give pmid, pmcid, doi, year, first author, short title, design, target category, overview section fed, value type and a 1-line reason, plus 2 rejected near-misses.

## Phase 2 — Approval gate (STOP here)

Show one table per domain: rank · paper · design · full text or abstract-only · what it changes
in the overview. Add your recommendation (which to take, which to drop, and why). **End the
turn and wait.** Ingest only what the user approves. If they cut the list, nothing is wasted
because nothing has started.

## Phase 3 — Ingest approved papers (Sonnet, 1 subagent per paper)

- **Concurrency:** at most 20 subagents can run at once (hard limit). Keep batches ≤10.
- Per-paper brief: INGEST.md Steps 0, 1-T, 2, 3. Run `python3 scripts/pubmed-fetch-fulltext.py <PMID>` into `papers/{stem}.txt`. With no PMC body, build the `.txt` from the abstract and set `full_text: false`.
  - Write `source_collection: pubmed-text` and **both `text_path` and `text_filename` on both pages**.
  - Pick a descriptive canonical stem.
  - Judge supersession and **report** it; do not edit other pages.
  - Log deviations, run lint, and do not touch index.md, git or qmd.
  - Return: stem, category, status, full_text, index_line (Korean, house format), 3 key numbers with effect sizes, and the supersession judgment.
- **Recovery** (subagent killed or session limit): check what is on disk. If only the txt exists, have a new subagent write the pages from the local txt (no re-fetch). If the txt and source exist, write the wiki page only. If pages exist, verify completeness. If the user drops a paper, delete its untracked papers/sources/wiki files.
- **Contamination check (mandatory, before finalize).** Print each new page's first Three-line Summary line next to its `title:`. Any mismatch → replace the summary block from `sources/` and log `source-data-issue`.
  ```bash
  for f in <new wiki pages>; do echo "== $(grep -m1 '^title:' $f)"; sed -n '/^## Three-line Summary/,/^## 세줄요약/p' $f | grep -v -e '^##' -e '^$' | head -1 | cut -c1-160; done
  ```
- **Finalize serially (parent only):** for each paper, insert its index line directly under the category's `## ` header in index.md, then run `python3 scripts/ingest-one.py --finish <stem>`. That handles the per-file commits, the category landing page, the push and qmd.

## Phase 4 — Overview update (Opus · high, 1 subagent per overview or domain)

Brief:

> Fold the new papers `<stems + key findings + caveats>` into `<overview>`.
> - Read the overview and every new wiki page fully. Rule #1: cite only held pages.
> - Use **bare** `[[category/stem]]` in evidence tables, never aliases.
> - State qualifications or contradictions explicitly, with appraisal caveats (abstract-only, industry funding, low AMSTAR, re-cited numbers).
> - Fix stale self-referential counts and "no data on X" gap sentences.
> - Update `> [!summary] 한국어 핵심요약`, and the Three-line Summary and 세줄요약 if the thesis shifted. Set `date:` to today.
> - Leave unrelated sections alone. No git, index or qmd. Run lint.
> - Return ≤200 words: changes per section, revised claims, open gaps, and any problem seen in the new pages.

Act on reported page problems (wrong summary, wrong `evidence_level`) yourself, or ask the user.

## Phase 5 — Close

- `python3 scripts/lint.py`. Commit each overview as its own file with `git commit -- <file>`; never bundle another session's uncommitted files.
- `git push`, then `qmd update && qmd embed` until "All content hashes already have embeddings".
- Report a table per domain: paper · what changed in the overview · open gaps. Add `[확인]`/`[미검증]` tags.
