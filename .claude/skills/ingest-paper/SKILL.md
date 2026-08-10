---
name: ingest-paper
description: Add dental research PDF(s) to the LLM Wiki. Full pipeline: copy PDF → write sources/*.md → write wiki/{category}/*.md → update index.md → qmd re-index. One paper runs serially; 2+ papers take a parallel fan-out (one subagent per paper, then serial finalize) so wall-clock ≈ the single slowest paper. Invoke when the user says "논문 추가", "ingest", "인제스트", or provides PDF path(s). Always run lint after completing.
argument-hint: [/path/to/paper.pdf]
allowed-tools: Bash, Read, Write, Edit
---

# Ingest Paper Skill

Full pipeline to add a dental research PDF into the LLM Wiki knowledge base.

## Step 0 — Model routing (fixed — do not ask the user)

모든 작업은 아래 **3축 판단 원칙**으로 모델을 자율 결정한다. 표에 없는 작업도 이 원칙으로 판단한다.

### 3축 판단 원칙

| 축 | 모델 | 판단 기준 |
|---|---|---|
| **전사·정형** | **Haiku** | 답이 입력에 이미 있다. 수치 옮기기, 링크 고치기, 로그 읽기, 파일 복사, frontmatter 채우기, 스크립트 실행 결과 해석 — 추론 없이 기계적으로 완료 가능한 작업 |
| **표현·품질** | **Sonnet** | 문장을 새로 써야 한다. 위키 본문, 세줄요약, 카테고리 정리 결정, 임상 insights 작성 — 입력을 이해해 좋은 문장으로 변환해야 하는 작업 |
| **추론·종합** | **Opus** | 여러 논문·페이지를 비교해 판단해야 한다. supersession, 카테고리 경계, overview 종합, 논문 간 관계 결정 — 오판이 위키 구조에 누적되는 작업 |

**자율 결정 규칙**: 작업을 시작하기 전 이 세 축 중 어디에 속하는지 먼저 판단하고 모델을 선택한다. 판단이 애매하면 한 축 위로 올린다(Haiku→Sonnet, Sonnet→Opus).

### 주요 작업 매핑 (참고용 — 원칙이 우선)

| 작업 | 모델 |
|---|---|
| 텍스트 추출, PDF 복사, dedup, lint, qmd, 로그 읽기, 링크 수정 | **Haiku** |
| `sources/` 작성 (Step 5) | **Haiku** |
| `wiki/` 페이지 본문 (Step 6), 카테고리 정리 결정 | **Sonnet** |
| supersession 판단, 카테고리 경계 분류, `wiki/overviews/` 작성 | **Opus** |

**Serial 모드**: Steps 1–5 후 `/model sonnet` 전환 안내. Supersession/boundary/overview 직전 `/model opus` 안내.

**Batch 모드 서브에이전트**: 1a파도 `model: haiku`(Steps 2–5), 1b파도 `model: sonnet`(Step 6). Boundary/supersession 케이스는 1b를 `model: opus`로 교체.

If multiple PDFs are being ingested in one go, this is a **batch** — note the count. A batch of **2+ papers takes the parallel path (§ Batch mode)**, which changes both execution shape (fan-out) and finalize (PHASE 2's `ingest-one.py --finish` per paper, not the manual Step 10 block — see Step 10's batch note).

---

## Execution mode — pick ONE before starting

| Papers | Mode | Why |
|---|---|---|
| **1** | **Serial** (Steps 1–11 below, inline) | No fan-out overhead; one page's authoring can't be parallelized against itself. |
| **2+** | **Batch / parallel** (§ Batch mode — parallel fan-out) | The bottleneck is PDF-read + page-authoring, which is **per-paper independent**. Fan out one subagent per paper (Phase 1), then finalize serially (Phase 2). Wall-clock ≈ the single slowest paper, not the sum. |

The two modes run the **same 11 steps with the same content quality** — batch mode only changes *who* runs Steps 1–9 (a per-paper subagent instead of the main loop) and *when* the git/index/embed work happens (batched into a serial Phase 2). Nothing is dropped or shortened.

---

## Batch mode — parallel fan-out (2+ papers)

The rule from CLAUDE.md § *Parallel-subagent protocol*: **content in parallel, finalize in serial.** Each paper's `sources/*.md` + `wiki/*.md` writes go to distinct paths → conflict-free in parallel. But `index.md` edits and `git add/commit/push` share mutable state → must stay serial in the parent. Running them concurrently races and corrupts the index/git tree.

### Enumerate the batch

```bash
cd /Users/oracleneo/llm-wiki
python3 -c "import json; q=json.load(open('.ingest-queue')); print('\n'.join(q.get('pending', [])))" 2>/dev/null
# or, for user-supplied PDF paths, just use the list the user gave.
```

### PHASE 1 — fan out (parallel): one subagent per paper

Dispatch **all papers at once** — one `Agent` call per paper, in a **single message** so they run concurrently. Each subagent is told to run **Steps 1–6 for its ONE paper only**:

- Step 2 (extract + stem), Step 3 (copy PDF), Step 3.5 (dedup + related/supersession lookup — if it returns a same-DOI cross-stem duplicate, the subagent **STOPs and returns `skip:<reason>`**), Step 4 (category), Step 5 (`sources/{stem}.md`), Step 6 (`wiki/{category}/{stem}.md`).
- The subagent does **NOT** touch `index.md`, does **NOT** git-commit/push, does **NOT** run qmd. Those are Phase 2, parent-only.
- The subagent does **NOT** use `isolation: worktree` — it must write into the main working tree the parent then commits.
- The subagent **logs deviations** immediately when it handles a non-standard case (empty PMC text, DOI conflict, category boundary, skipped step): `python3 scripts/log-deviation.py <stem> <type> "<desc>"` (non-blocking, <1s).
- The subagent **RETURNS** a compact record: `{stem, category, evidence_level, index_line, status: ok|skip:<reason>}`.

Model routing per subagent (from Step 0 table):
- **Haiku+Sonnet 분리 선택 시**: Phase 1을 두 파도로 나눈다.
  - **1a파도** (`model: haiku`): Steps 2–5만 수행 (텍스트 추출, dedup, PDF 복사, 카테고리, sources/ 작성). wiki/는 건드리지 않음.
  - **1b파도** (`model: sonnet` + `effort: high`): 1a파도 완료 후 sources/{stem}.md를 읽고 Step 6(wiki/ 페이지)만 작성. supersession/boundary 케이스는 `model: opus`로 에스컬레이션.
- **Sonnet 전체 선택 시**: 단일 파도 `model: sonnet` + `effort: high`. boundary/supersession 케이스는 `model: opus`.
- Overviews are never authored inside a fan-out.

### PHASE 2 — finalize (serial, parent only)

For each returned **ok** paper, one at a time, in order:

```bash
cd /Users/oracleneo/llm-wiki
python3 scripts/ingest-one.py --finish <stem>
#   → per-file git commit (sources, wiki, index) + push + qmd update + qmd embed (incremental) + mark processed
```

- Before `--finish`, the parent adds the paper's `index_line` to `index.md` (Step 7) if the subagent didn't — keep this serial to avoid index races.
- Then run Step 8 (lint) + Step 9 (orphan check) on that page.
- For each returned **skip** paper: delete the duplicate PDF, mark the queue entry processed, write no page.

`qmd embed` inside `--finish` is **incremental** (only changed docs, seconds), so per-paper finalize is cheap. **Never** force a full re-embed (`-f`).

> **Why this split is the whole speedup.** PHASE 1 parallelizes the real bottleneck (PDF read + authoring). PHASE 2 keeps the shared-state work (index, git) serial so it can't race. A 6-paper batch that took ~6× one paper serially now takes ≈1× (slowest paper) + a short serial finalize tail.

If invoked in a context where you cannot spawn subagents (already inside one), fall back to the serial loop: `ingest-one.py --next` → author → `--finish`, repeated. Correct, just not parallel.

---

### Model routing — 3단 고정 분리

Step 0 표가 최종 권위다. 아래는 실행 시 판단 기준:

| Sub-step | 모델 | 판단 기준 |
|---|---|---|
| 텍스트 추출, stem, PDF 복사, lint, qmd | **Haiku** | 정형 작업, 추론 불필요 |
| `sources/` 작성 (Step 5) | **Haiku** | 수치 전사·섹션 분류 — Haiku 충분 |
| `wiki/` 페이지 본문 (Step 6) | **Sonnet** | 세줄요약·임상 insights 품질 중요 |
| 카테고리 boundary 판단 (Step 4) | **Opus** | 오분류는 구조적으로 누적됨 |
| `superseded_by` + `relations:` 판단 (Step 6) | **Opus** | 논문 간 추론 — 전사 아닌 판단 |
| `wiki/overviews/` 종합·한국어 핵심요약 | **Opus** | 크로스-페이퍼 종합, 절대 Sonnet 불가 |

How to escalate in practice:
- **Main session**: Steps 1–5 진행 중 boundary/supersession 징후 발견 시 `/model opus` 전환을 사용자에게 안내. Step 6 시작 시 `/model sonnet` 안내.
- **Subagent ingest**: 1a파도 `model: haiku`(Steps 2–5), 1b파도 `model: sonnet`(Step 6). Boundary/supersession 확인된 논문은 1b 서브에이전트를 `model: opus`로 교체. Overviews are authored in a separate Opus session, never inside a fan-out.

---

## Workflow

### Step 1 — Receive and validate input

The argument is an absolute path to a PDF file. Confirm it exists:

```bash
ls -lh "/path/to/paper.pdf"
```

If the file does not exist, stop and tell the user.

**No-PDF variant.** If there's no local PDF at all — full text pulled via PubMed MCP, or nothing beyond an abstract — this isn't a Step 1 failure, it's a different entry point. Skip to INGEST.md Step 1-T (PubMed-text) or Step 1-A (abstract-only PDF) for the frontmatter field substitutions (`source_collection`, `full_text`, `pmid`/`pmcid`, `text_path`/`text_filename` in place of `pdf_path`/`pdf_filename`), then rejoin at Step 4 below.

---

### Step 2 — Extract text + MD5 dedup (single call)

Do the text extraction **and** the byte-identical dedup check in **one** bash round-trip — they both only need to read the source PDF, so there's no reason to pay two round-trips:

```bash
python3 -c "
import pypdf, sys, os, hashlib
src = sys.argv[1]
# (a) MD5 dedup vs everything already in papers/
new = hashlib.md5(open(src,'rb').read()).hexdigest()
dup = next((f for f in os.listdir('papers') if f.endswith('.pdf')
            and hashlib.md5(open(f'papers/{f}','rb').read()).hexdigest()==new), None)
print('DUPLICATE:' , dup) if dup else print('DEDUP OK: no byte-identical copy')
# (b) extract up to 12k chars from first 15 pages
reader = pypdf.PdfReader(src); text=''
for page in reader.pages[:15]:
    t = page.extract_text()
    if t: text += t + '\n'
    if len(text) > 12000: break
print('----- TEXT -----'); print(text[:12000])
" "/path/to/paper.pdf"
```

If the output starts with `DUPLICATE:` → stop, inform the user which stem it matched, delete the new file if it's in a temp location. Otherwise read the `----- TEXT -----` block and identify:
- **First author last name** (lowercase)
- **Publication year** (4 digits)
- **First 5 meaningful title words** (lowercase, spaces → hyphens, strip special chars)

Build the **canonical stem**: `{first-author-lastname}-{year}-{first-5-title-words}`
Examples: `wu-2025-mb2-prevalence-maxillary-molar-han`, `kaur-2024-eal-vs-radiograph-working-length`.

---

### Step 3 — Copy PDF to `papers/`

```bash
cp "/path/to/paper.pdf" "/Users/oracleneo/llm-wiki/papers/{stem}.pdf"
```

Verify the copy succeeded.

---

### Step 3.5 — Related-page & supersession lookup (mechanical — runs on EVERY model)

The MD5 check in Step 2 only catches a byte-identical file. It does **not** catch the same paper under a different stem, and it does **not** surface the existing pages this paper might **overturn**. Those are the two things a Sonnet ingest silently misses — because nothing put them in front of it. This step fixes that by turning the lookup into **data, not judgment**: run it on every ingest, whatever the model.

**(a) Same-DOI cross-stem duplicate** — grep the DOI extracted in Step 2 across `sources/`:

```bash
# Replace <DOI> with the DOI from Step 2 (skip if DOI is unknown).
grep -rl "<DOI>" sources/ 2>/dev/null
```

- **Match found** → this paper is already in the wiki under another stem. **Do NOT create a second page.** Stop, tell the user the matching stem, and *update the existing page* instead. Delete the just-copied PDF (it's an orphan).
- No match → continue.

**(b) Related / superseded pages** — semantic lookup of what we already hold on this topic:

```bash
export PATH="/opt/homebrew/bin:$PATH"   # brew node — qmd ABI
cd /Users/oracleneo/llm-wiki
qmd query "<paper topic in 5-8 words>" -c wiki 2>/dev/null | head -8
```

Read the top hits and ask, explicitly, two questions:

1. **Boundary check** → do the hits cluster in a *different* category than you were about to pick? If so, treat Step 4 as a boundary case (escalate the classification to Opus).
2. **Supersession check** → does this new paper **overturn the clinical bottom line** of any hit we hold (higher evidence weight, or newer + same weight)? If plausibly yes, this is a **supersession judgment** → escalate to **Opus**, and on confirmation mark the *older* page's `superseded_by` + banner (CLAUDE.md § living-document supersession; memory [[supersession-judgment-at-ingest]]).
3. **Contradiction check** → does this paper's conclusion **conflict with** a hit we hold *without* fully superseding it (both remain valid evidence, they just disagree — e.g. big-data HR gap vs SR+MA "no difference", pro-ARP MA vs ARP-overtreatment critique)? If yes, add a typed edge on the **newer/citing** page's `relations:` block: `type: contradicts` (head-on conflict) or `type: refines` (narrows/qualifies the other's conclusion). This is what feeds the **논쟁 레이더** (`interactives/contradiction-radar.html`) — an omitted edge = a real controversy invisible on the radar. Do NOT force it: only add when conclusions genuinely oppose; a mere different-angle paper is `reinforces`/`extends`, not `contradicts`.

If qmd is down, fall back to a BM25 search (`qmd search "<author/device/term>"`) or `qmd vsearch "<concept>"` or `grep -ri "<key term>" wiki/`. (Note: `qmd query`'s LLM rerank can hang in non-interactive/subagent runs — prefer `search`/`vsearch` there; memory [[qmd-query-hangs-headless]].) The point is that *some* mechanical lookup always runs — the escalation triggers must never depend on the model spontaneously remembering a related page exists.

---

### Step 4 — Determine category

See [wiki/_meta/categories.md](../../../wiki/_meta/categories.md) for the full category list and subcategory routing (single source of truth — do not use a copy from elsewhere). Choose the **single best category** based on the paper's primary method or procedure — not by disease or anatomy.

> **Model note (Step 0 routing).** If the paper sits on a **category boundary** — two or more sibling folders plausibly fit (e.g. `immediate-implant` vs `immediate-implant/esthetic-soft-tissue` vs `implants/soft-tissue`) — this is a high-judgment call: escalate this decision to **Opus** rather than guessing on Sonnet. Misclassification silently corrupts the wiki's structure.

---

### Step 5 — Write `sources/{stem}.md`

Use the template in [reference.md](reference.md) → **Sources Template** section.

Fill in all fields from the extracted text:
- `title`: exact paper title
- `authors`: all authors, comma-separated
- `year`: publication year
- `doi`: DOI string only (no URL prefix)
- `category`: chosen category folder
- `pdf_path`: `/Users/oracleneo/llm-wiki/papers/{stem}.pdf`
- `pdf_filename`: `{stem}.pdf`

Sections to write:
1. **Why Ingested** — 1–2 sentences on why this paper, now (gap/conflict/new evidence/requested/current case); at least one `[[wiki/category/stem]]` wikilink to a page it reinforces/contradicts/extends, found via `qmd query` (never grep/find). **Mandatory** for papers ingested on/after 2026-05-27 (lint-enforced by `scripts/ingest-rationale-lint.py`).
2. **Three-line Summary** (English) + **세줄요약** (Korean) — two separate sections, this order, each exactly 3 lines: study type/n/context, primary result with numbers, clinical implication or key limitation.
3. **Document Information** — journal, DOI, institution
4. **Key Contributions** — bullet points of novel claims
5. **Methodology** — design, databases, n, outcomes
6. **Key Results** — numbers, tables, p-values
7. **Limitations** — explicitly stated or inferred
8. **Related Work** — wikilinks to relevant existing pages
9. **Glossary** — 3–6 key terms with definitions

---

### Step 6 — Write `wiki/{category}/{stem}.md`

Use the template in [reference.md](reference.md) → **Wiki Template** section.

Required frontmatter fields (all 9 must be present — lint checks these):
```
title, authors, year, doi, source, category, evidence_level, pdf_path, pdf_filename
```
(`evidence_level` — renamed from `confidence` 2026-07-15; `scripts/lint.py` accepts either key but prefers `evidence_level` — always write the new name on new pages.)

Additional required fields:
- `date`: publication date `YYYY-MM-DD`; use `YYYY-01-01` if only year known; use ingest date if neither recoverable
- `tags`: relevant keywords as YAML list

Body sections (in order):
1. `## Three-line Summary` (English) + `## 세줄요약` (Korean) — two separate sections, this order, each exactly 3 lines (same content/format as the Sources page — see Step 5). Use **한국어 (English, 약어)** notation for technical terms in the Korean section.
2. `## Summary` — English paragraph, 3–5 sentences
3. `## Key Contributions`
4. `## Methodology`
5. `## Results` — include tables where helpful
6. `## Related Papers` — `[[category/stem]]` wikilinks with relationship description

Evidence level vocabulary (`evidence_level:`) — pick the single best label. See [reference.md](reference.md) → **Evidence Level Vocabulary**. Optional judgment-call fields (`superseded_by`/`superseded_scope`, `relations:`) are in the same reference section — don't guess their vocabulary from memory.

> **Model note (Step 0 routing).** Two parts of this page are **cross-paper judgment, not transcription**, and want **Opus** even in a Sonnet ingest: (1) deciding whether this paper **supersedes an existing page** (`superseded_by` + banner — see CLAUDE.md § living-document supersession and memory [[supersession-judgment-at-ingest]]), and (2) writing the relationship prose / `relations:` edges that say *how* it relates to existing pages. Transcribing this paper's own results stays on Sonnet; judging it against the rest of the wiki escalates.

---

### Step 7 — Update `index.md`

Add a one-line entry under the correct section heading in `/Users/oracleneo/llm-wiki/index.md`:

```
- [[{category}/{stem}]] — {one-line Korean summary with key numbers}
```

Find the correct section by matching the category to the section header. Use Edit tool to insert the new line at the **bottom** of the correct section (just before the blank line before the next `##`).

---

### Step 8+9 — Lint + orphan check (single call)

Use the canonical scripts — **not** a hand-rolled inline check. (An earlier inline snippet duplicated this logic with a hardcoded field list that drifted to the pre-2026-07-15 `confidence` name and started false-flagging correctly-written `evidence_level` pages; don't reintroduce a second copy.)

```bash
python3 scripts/lint.py && python3 scripts/orphan-check.py
```

Both are fast, read-only, whole-repo scans (`lint.py` checks frontmatter completeness — accepts either `confidence` or `evidence_level`, preferring the latter; `orphan-check.py` checks PDF↔sources 1:1). If lint reports errors → fix them before reporting completion. (In **batch mode**, `ingest-one.py --finish` handles commit/push/embed per paper; run this lint+orphan block once per paper in Phase 2, or once at the end over the whole batch.)

---

### Step 10 — Refresh search index (qmd)

A new wiki page is invisible to semantic search until qmd re-indexes and embeds it.

**This manual block is for the single-paper serial path** (Steps 1–11 run by hand — no PHASE 2 script involved). Run it once, after Steps 1–9.

**Batch mode does not use this block.** In Batch mode (§ PHASE 2 above), `ingest-one.py --finish <stem>` runs `qmd update && qmd embed` itself, once per paper — do not also run this block between (or after) papers. `qmd embed` is incremental (only changed docs), so per-paper calls are cheap, not a full re-embed. If the daemon leaves a backlog half-done across a large batch (session-expiry mid-pass, exit 0 ≠ complete), that's handled by checking `qmd status | grep Pending` after the whole batch and draining — see INGEST.md Phase 2 / § Step 5, not this block.

Run after the wiki/sources files are written and lint passes:

```bash
# brew node(v25+)를 강제 — PATH에 구 node v18이 앞설 경우 ABI 불일치로 qmd가 깨짐.
export PATH="/opt/homebrew/bin:$PATH"
cd /Users/oracleneo/llm-wiki
qmd update      # 파일시스템 재스캔 — 신규 wiki/sources md 등록
qmd embed       # 변경분만 임베딩 (incremental). batch면 마지막에 1회만.
```

Then confirm the new page is searchable (should return the new stem):

```bash
export PATH="/opt/homebrew/bin:$PATH"
qmd query "{paper topic in a few words}" -c wiki 2>/dev/null | grep -i "{stem}" | head -1
```

Notes:
- `qmd embed` is **incremental** — it only embeds documents whose content changed, so a single new paper finishes in seconds. Never use `-f` here (that forces a full re-embed of all ~1,800 docs, ~2.5 h).
- If `qmd` errors with `NODE_MODULE_VERSION` / `ERR_UNKNOWN_FILE_EXTENSION`, the wrong Node is on PATH. The `export PATH=...` line above fixes it; if it persists, run `cd /opt/homebrew/lib/node_modules/@tobilu/qmd && npm rebuild better-sqlite3`.
- The qmd MCP daemon picks up the new vectors automatically — no restart needed.

---

### Step 11 — Report completion

Tell the user:
```
✅ Ingest complete: {stem}
   Category      : {category}
   Evidence Level: {evidence_level}
   Lint          : OK {n} files, 0 errors
   Index         : added to {section heading}
   Search        : qmd re-indexed + embedded (searchable now)
```

---

## Rules

1. **No web search.** All content must come from the PDF only. Never use WebSearch or WebFetch to fill gaps.
2. Work from `/Users/oracleneo/llm-wiki/` as the base directory (all relative paths are from here).
3. All bash commands must be run from `/Users/oracleneo/llm-wiki/`.
4. **Term notation in Korean text**: always write technical terms as **한국어 (English, 약어)** — e.g., 골-임플란트 접촉률 (Bone-to-Implant Contact, BIC).
5. Never guess DOI — extract from PDF text. If not found, write `unknown`.
6. If the paper is non-dental, do not ingest — delete the PDF and tell the user.
7. If duplicate detected (MD5 match), do not overwrite existing files — tell the user which stem it matches.
