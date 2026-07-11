---
name: ingest-paper
description: Add dental research PDF(s) to the LLM Wiki. Full pipeline: copy PDF → write sources/*.md → write wiki/{category}/*.md → update index.md → qmd re-index. One paper runs serially; 2+ papers take a parallel fan-out (one subagent per paper, then serial finalize) so wall-clock ≈ the single slowest paper. Invoke when the user says "논문 추가", "ingest", "인제스트", or provides PDF path(s). Always run lint after completing.
argument-hint: [/path/to/paper.pdf]
allowed-tools: Bash, Read, Write, Edit
---

# Ingest Paper Skill

Full pipeline to add a dental research PDF into the LLM Wiki knowledge base.

**Default pipeline is unchanged and 100% Claude.** An optional Gemini-draft assist exists (§ Step 2.5) but only activates when the user's request explicitly contains a trigger phrase — never by default, never inferred.

## Step 0 — Model & batch check (ask first, before any work)

Before starting, ask the user **once** (use the AskUserQuestion tool) and wait for the answer:

> **"논문 ingest 모델을 무엇으로 할까요?"**
> - **Sonnet 최고등급 (권장)** — ingest는 정형 작업이라 Sonnet이면 충분하고 비용이 Opus의 약 1/5. 최고 effort로 품질 확보.
> - **현재 모델 유지** — 지금 세션 모델 그대로 사용.

How to honor the answer:
- If the user picks **Sonnet 최고등급**, tell them to run `/model sonnet` (and raise effort to high/max) before continuing, OR — if invoked as a subagent — set the agent's `model: sonnet` + `effort: high`. The skill itself cannot switch the main-session model mid-run, so surface this clearly rather than silently ignoring it.
- If multiple PDFs are being ingested in one go, this is a **batch** — note the count. A batch of **2+ papers takes the parallel path (§ Batch mode)**, which changes both execution shape (fan-out) and Step 10 (embed once at the very end, not per paper).

Skip Step 0 only if the user already specified the model in their request.

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
- The subagent **RETURNS** a compact record: `{stem, category, confidence, index_line, status: ok|skip:<reason>}`.

Model routing per subagent (from Step 0 table): default `model: sonnet` + `effort: high`. If the dispatcher already knows a given paper is a **category-boundary** or **supersession** candidate, set *that paper's* agent to `model: opus`. Overviews are never authored inside a fan-out.

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

### Model routing — "추출이면 Sonnet, 종합·판단이면 Opus"

The default above (Sonnet) is correct for the *extraction* bulk of ingest. But certain sub-steps are **high-judgment** and should escalate to **Opus** even inside a Sonnet ingest. The single test: *does the model have to reason across papers or make a clinical judgment, vs. just transcribe this one PDF?* (Full rationale: [agenda/2026-06-30_model-routing-ingest-overview.md](../../../agenda/2026-06-30_model-routing-ingest-overview.md).)

| Sub-step | Default | Escalate to **Opus** when… |
|---|---|---|
| Text extraction, stem, copy, index, qmd, lint | Sonnet | never |
| `sources/` + single-paper `wiki/` page (Step 5–6) | Sonnet | the paper sits on a **category boundary** (Step 4) |
| Category choice (Step 4) | Sonnet | boundary case (e.g. `immediate-implant` vs `/esthetic-soft-tissue` vs `implants/soft-tissue`) — misclassification compounds |
| `## Why Ingested` + `superseded_by` judgment (Step 6) | — | **always Opus-grade** — it is cross-paper reasoning, not transcription |
| `wiki/overviews/` synthesis, 한국어 digest, Class-B clinical interactive | — | **always Opus** — never produce these on Sonnet |

How to escalate in practice:
- **Main session**: when you hit a boundary classification or a supersession judgment and you're on Sonnet, surface it — tell the user this sub-step wants Opus (`/model opus`), or note that you're handling just that judgment with extra care.
- **Subagent ingest**: default the per-paper agent to `model: sonnet`. If the dispatcher already knows a paper is a boundary/supersession candidate, set *that paper's* agent to `model: opus`. Overviews are authored in a separate Opus session, never inside a fan-out.

---

## Workflow

### Step 1 — Receive and validate input

The argument is an absolute path to a PDF file. Confirm it exists:

```bash
ls -lh "/path/to/paper.pdf"
```

If the file does not exist, stop and tell the user.

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

### Step 2.5 — (Optional, trigger-gated) Gemini draft assist

**Trigger check — do this FIRST, every time.** This step runs **only if** the user's request for this ingest contains one of: `"제미나이 초안"`, `"제미나이 인제스트"`, `"제미나이로"`, `"gemini draft"`. If none of these phrases are present, **skip this step entirely** and proceed straight to Step 3 as normal — do not offer or default into Gemini mode, and do not ask the user if they want it.

**Why this is trigger-only, not default.** Token savings are worth it only when the user opts in per-paper; the fidelity guard below (Claude re-verifies every number) costs Claude tokens too, so silently defaulting to it would save nothing while adding risk. Opt-in keeps the normal path's quality guarantee untouched.

**What it does.** Gemini drafts the *raw prose* for the summary sections (not frontmatter, not category, not wikilinks, not the supersession/relations judgment — those stay Claude-only regardless of trigger). Claude then verifies and finalizes.

```bash
cd /Users/oracleneo/llm-wiki
cat > /tmp/gemini-draft-{stem}.txt << 'EOF'
You are drafting RAW MARKDOWN BODY TEXT for a dental research knowledge-base page.
Use ONLY the paper text below — do not invent numbers, authors, or claims not present in it.
Output exactly these sections, in this order, nothing else:

## Document Information
## Key Contributions
## Methodology
## Key Results
## Limitations
## Glossary
## Three-line Summary
(3 lines, blank line between each: study type/n/context — primary result with numbers — clinical implication or key limitation)
## 세줄요약
(한국어 3줄, 위와 동일 구조, 기술 용어는 반드시 "한국어 (English, 약어)" 표기)

PAPER TEXT:
<PASTE the extracted text from Step 2 here>
EOF
gemini -p "$(cat /tmp/gemini-draft-{stem}.txt)" -o text > /tmp/gemini-draft-out-{stem}.md
cat /tmp/gemini-draft-out-{stem}.md
```

**Fidelity guard — mandatory, not optional, whenever this step ran.** Before using any of this draft in Steps 5–6:
1. Spot-check every number, p-value, and n in the draft against the Step 2 extracted PDF text. If a figure can't be found in the source text, discard or fix that line — do not paste it through.
2. Claude still performs Step 3.5 (dedup/supersession/contradiction lookup), Step 4 (category), the `## Why Ingested` wikilink, `relations:`/`superseded_by` judgment, and all frontmatter — none of that is delegated, ever.
3. Rewrite anything that doesn't match this repo's tone/format conventions (the draft is raw material for Steps 5–6, not a copy-paste source).
4. Note in the Step 11 completion report that this paper used Gemini-draft assist, so it's visible in history.

If `gemini` CLI is not on PATH or the call fails, tell the user and fall back to the normal Claude-only path for this paper — do not block the ingest on it.

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

See [reference.md](reference.md) for the full category list. Choose the **single best category** based on the paper's primary method or procedure — not by disease or anatomy.

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
1. **One-line Summary** — study type, n, key finding in one English sentence
2. **Document Information** — journal, DOI, institution
3. **Key Contributions** — bullet points of novel claims
4. **Methodology** — design, databases, n, outcomes
5. **Key Results** — numbers, tables, p-values
6. **Limitations** — explicitly stated or inferred
7. **Related Work** — wikilinks to relevant existing pages
8. **Glossary** — 3–6 key terms with definitions

---

### Step 6 — Write `wiki/{category}/{stem}.md`

Use the template in [reference.md](reference.md) → **Wiki Template** section.

Required frontmatter fields (all 9 must be present — lint checks these):
```
title, authors, year, doi, source, category, confidence, pdf_path, pdf_filename
```

Additional required fields:
- `date`: publication date `YYYY-MM-DD`; use `YYYY-01-01` if only year known; use ingest date if neither recoverable
- `tags`: relevant keywords as YAML list

Body sections (in order):
1. `## 한줄요약` — Korean one-liner: study type, n, key finding in plain Korean. Use **한국어 (English, 약어)** notation for technical terms.
2. `## Summary` — English paragraph, 3–5 sentences
3. `## Key Contributions`
4. `## Methodology`
5. `## Results` — include tables where helpful
6. `## Related Papers` — `[[category/stem]]` wikilinks with relationship description

Confidence vocabulary — pick the single best label. See [reference.md](reference.md) → **Confidence Vocabulary**.

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

Frontmatter lint and the PDF↔sources 1:1 orphan check are independent read-only scans — run both in **one** bash round-trip:

```bash
python3 -c "
import os, re
# --- (8) frontmatter lint ---
REQ = ['title','authors','year','doi','source','category','confidence','pdf_path','pdf_filename']
SKIP = {'_lint','overviews'}
errors=[]; ok=0
for root,dirs,files in os.walk('wiki'):
    dirs[:] = [d for d in dirs if d not in SKIP]
    for fn in files:
        if not fn.endswith('.md'): continue
        p=os.path.join(root,fn); c=open(p).read()
        m=re.match(r'^---\n(.*?)\n---', c, re.DOTALL)
        if not m: errors.append(f'NO FRONTMATTER: {p}'); continue
        miss=[f for f in REQ if not re.search(rf'^{f}\s*:', m.group(1), re.MULTILINE)]
        errors.append(f'MISSING {miss}: {p}') if miss else (ok:=ok+1)
print(f'LINT — OK: {ok}  ERRORS: {len(errors)}')
for e in errors: print(' ', e)
# --- (9) orphan check ---
papers={f[:-4] for f in os.listdir('papers') if f.endswith('.pdf')}
srcs  ={f[:-3] for f in os.listdir('sources') if f.endswith('.md')}
op, osr = papers-srcs, srcs-papers
if op:  print('ORPHAN PDFs (delete):', op)
if osr: print('ORPHAN sources (missing PDF):', osr)
if not op and not osr: print('ORPHAN — OK: 1:1 match')
"
```

If lint reports errors → fix them before reporting completion. (In **batch mode**, `ingest-one.py --finish` handles commit/push/embed per paper; run this lint+orphan block once per paper in Phase 2, or once at the end over the whole batch.)

---

### Step 10 — Refresh search index (qmd)

A new wiki page is invisible to semantic search until qmd re-indexes and embeds it.

**Batch rule (important).** `qmd embed` re-embeds *every* changed doc in the repo each run, so calling it once per paper during a multi-paper batch wastes huge amounts of time (the wiki is edited daily by lints/audits, so each run re-embeds hundreds of unrelated docs). Therefore:

- **Single paper** → run the block below after Steps 1–9.
- **Batch (2+ papers, see Step 0)** → do Steps 1–9 for *every* paper first, and run this index-refresh block **exactly once, after the last paper**. Do NOT run `qmd update`/`qmd embed` between papers.

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
   Category  : {category}
   Confidence: {confidence}
   Lint      : OK {n} files, 0 errors
   Index     : added to {section heading}
   Search    : qmd re-indexed + embedded (searchable now)
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
