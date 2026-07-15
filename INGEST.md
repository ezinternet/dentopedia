# INGEST — Paper Ingestion Pipeline (치과학 llm-wiki)

CLAUDE.md의 **Adding a New Paper** 세부 절차를 분리한 파일. CLAUDE.md 본문은 3-tier 원칙·라우팅·audit만 담고, ingest 실행 세부(Step 0–5, 분기, PDF 규칙, 필드 정의)는 여기서 단일 관리한다. `wiki/_meta/categories.md`를 분리한 것과 같은 이유 — context 절약 + 단일 출처.

**When to read this file**: 논문을 위키에 추가(`인제스트`, `Add this paper`, PDF 경로 언급)하는 작업이면 이 파일을 먼저 연다. 답변 생성(질문 대답)에는 필요 없다.

---

## Adding a New Paper

Say: *"Add this paper to the wiki: /path/to/paper.pdf"*
Or: *"인제스트 해줘"* (processes all pending papers in the queue — parallel subagents)

**Parallel-subagent protocol — content in parallel, finalize in serial**

When multiple papers are pending, fan them out to **one subagent per paper** for the content work, then have the **parent serially finalize** (index + commit + push + qmd). This is faster than one-at-a-time *without* reintroducing context exhaustion, because each subagent gets its own fresh context window — the old single-context batch failure mode (5+ papers fill the main context and later papers fail silently) cannot happen when each paper lives in its own subagent.

```
PHASE 1 — fan out (parallel):  one subagent per pending stem
  Each subagent, for its ONE paper, runs Steps 0–3 below:
    • Step 0  dedup + retraction gate (DOI grep) — if duplicate, STOP and report "skip:<reason>"
    • rename PDF papers/{raw}.pdf → papers/{canonical-stem}.pdf
    • Step 2–3  write sources/{stem}.md + wiki/{category}/{stem}.md
  Subagent does NOT touch index.md, does NOT git-commit/push, does NOT run qmd.
  Subagent RETURNS: {stem, category, index_line, status: ok|skip:<reason>}
  Subagent LOGS deviations: whenever a non-standard situation is handled (empty PMC text,
    DOI conflict, category change, step skipped), call immediately:
    python3 scripts/log-deviation.py <stem> <type> "<description>"
    This is non-blocking (<1s) and feeds the Rule-of-Three SOP evolution trigger.

PHASE 2 — finalize (serial, parent only — avoids git/index races):
  for each returned ok-paper (one at a time, in order):
    • Step 4  add its index_line to index.md
    • Step 5a  lint that page (scripts/lint.py) + orphan check (scripts/orphan-check.py)
    • python3 scripts/ingest-one.py --finish <stem>
        ← per-file git commit + push + qmd update/embed (incremental) + mark processed
  for each returned skip-paper: delete the duplicate PDF, mark queue processed (no page)
```

Why this split: file writes to distinct paths (`sources/*`, `wiki/*`, distinct PDFs) are conflict-free in parallel, so PHASE 1 parallelizes the real bottleneck (PDF read + page authoring — this is what was slow). But `index.md` edits and `git add/commit/push` share mutable state — running them concurrently races/corrupts the index and the git tree — so PHASE 2 keeps them strictly serial in the parent. Subagents do NOT use `isolation: worktree` (they must write into the main working tree the parent then commits). `qmd embed` is incremental (only changed docs, seconds), so running it inside each `--finish` is cheap; never force a full re-embed (`-f`).

Helper: `python3 scripts/ingest-one.py --next` prints one stem+text for a single subagent; read `.ingest-queue` `pending[]` to enumerate all stems to fan out in PHASE 1. For a single paper, skip the fan-out and run Steps 0–4 + `--finish` inline (no subagent needed).

The agent will do all steps automatically.

---

## Step 0 — Pre-ingest gate (dedup + retraction)

Before copying anything, run two checks. Skipping these is how the wiki accumulates duplicate and discredited pages.

1. **DOI / cross-stem duplicate check.** Extract the paper's DOI, then grep `sources/` for it. `orphan-check.py` only enforces stem-level 1:1 — it does NOT catch the same paper ingested under a different stem (e.g. `gaspar-2022-...` vs `gaspar-2025-...`, `materials-14-...` vs `inchingolo-...-sr-ma`). If the DOI already exists, do NOT create a second page — update the existing one instead. `scripts/doi-duplicate-check.py` (daily-audit signal) reports same-DOI/different-stem groups after the fact.

   ```bash
   grep -rl "10.xxxx/the-doi" sources/    # 결과 있으면 중복 → 기존 페이지 갱신, 신규 ingest 금지
   ```

   **No-DOI fallback.** Some papers print no DOI (older regional journals — e.g. *J Dent Tehran* 2013 — or PubMed records with no `doi` identifier). When there is no DOI, set the frontmatter `doi:` to `null` (or `n/a (Journal Year;Vol(Iss):pp; PMID xxxxx)` per the `vetromilla-2021`/`merli-2018` precedent) and run the Step-0 dedup by **title + first-author grep** over `sources/` instead of DOI grep. Log with `python3 scripts/log-deviation.py <stem> no-doi "..."`.

2. **Retraction check.** Do NOT ingest a retracted article, retraction notice, erratum-only page, or a bare PubMed/publisher listing page as a knowledge page — it propagates discredited claims and violates the living-document/critical-appraisal principle. If a retracted paper must be recorded, make a single explicit "RETRACTED — do not cite" stub, never a normal wiki page. Delete retraction/erratum notice PDFs (they are not ingestable papers).

## Step 1 — Copy PDF to `papers/` and extract text

```bash
cp /path/to/paper.pdf /Users/oracleneo/llm-wiki/papers/{stem}.pdf

python3 -c "
import pypdf, sys
reader = pypdf.PdfReader(sys.argv[1])
text = ''
for page in reader.pages[:15]:
    t = page.extract_text()
    if t: text += t + '\n'
    if len(text) > 12000: break
print(text[:12000])
" "/Users/oracleneo/llm-wiki/papers/{stem}.pdf"
```

### Step 1-T — PubMed-text 분기 (PDF 없는 OA/전문)

PubMed MCP `get_full_text_article`로 전문을 받은 경우 PDF가 없다. PDF 복사 대신 받은 전문을 `papers/{stem}.txt`로 저장하고, 그 텍스트로 Step 2·3을 작성한다. PMC 전문은 JATS 기반이라 pypdf 추출본보다 깨끗한 경우가 많다.

sources/·wiki/ frontmatter는 Step 2·3과 동일하되 아티팩트 필드만 교체:

```yaml
source_collection: pubmed-text   # external(PDF) 대신
full_text: true                  # 페이월로 초록만 받았으면 false
pmid: "xxxxxxxx"
pmcid: "PMCxxxxxxx"             # 없으면 생략
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMCxxxxxxx/
text_path: /Users/oracleneo/llm-wiki/papers/{stem}.txt
text_filename: {stem}.txt
# pdf_path / pdf_filename 생략
```

- `full_text: false`(초록만): Summary·Results를 초록 수준으로만 채우고 본문에 `abstract-only — full text not retrieved` 명시. confidence는 study type 그대로.
- dedup(Step 0)은 DOI/PMCID grep 그대로. 1:1 매칭·linter는 `.txt`를 PDF와 동등한 아티팩트로 인식한다 (`scripts/lint.py`, `wiki/_lint/lint.py`에 `pubmed-text` 분기 반영, 2026-06-17).

### Step 1-A — Abstract-only PDF 분기 (페이월 랜딩/초록 저장본)

가끔 받은 PDF가 전문이 아니라 **출판사 랜딩/초록 저장 페이지**(paywall, 흔히 1–2쪽, 본문 없음)다 — Step 1-T의 PMC-빈본문과 결과는 같지만 **아티팩트가 PDF**라 `source_collection: pubmed-text`를 쓸 수 없다. 이때:

- `source_collection: external` 유지(아티팩트는 PDF), `pdf_path`/`pdf_filename` 정상 기재.
- **frontmatter에 `full_text: false` 필드를 추가**하고, 본문 맨 위(Three-line Summary 위)에 `abstract-only — publisher landing/abstract page, full text not retrieved` 한 줄 명시. (초록만으로 Summary·Results 채움, confidence는 study type 그대로.)
  - 과거엔 이걸 frontmatter flag 없이 본문 caveat로만 처리해 일관성이 없었다(de-elio-2023 vs quesada-garcia-2012). 앞으로는 **frontmatter `full_text: false` + 본문 한 줄** 둘 다 박는다.
- DOI 없으면 위 Step 0 no-DOI fallback 병행.
- 로그: `python3 scripts/log-deviation.py <stem> abstract-only "publisher landing page, built from abstract"` (PMC 빈본문은 `empty-pmc-text`로 구분).

## Step 2 — Write `sources/{stem}.md`

```yaml
---
title: "Paper Title"
authors: Author List
year: YYYY
doi: DOI
category: [category-folder]
pdf_path: /Users/oracleneo/llm-wiki/papers/{stem}.pdf
pdf_filename: {stem}.pdf
source_collection: external
---

## Why Ingested
## Three-line Summary
## 세줄요약
## 1. Document Information
## 2. Key Contributions
## 3. Methodology and Architecture
## 4. Key Results and Benchmarks
## 5. Limitations and Future Work
## 6. Related Work
## 7. Glossary
```

**`## Why Ingested` is MANDATORY for sources ingested on/after 2026-05-27** (enforced by `scripts/ingest-rationale-lint.py`). Pre-cutoff sources are grandfathered (no backfill).

Required content of the section:
- 1–2 sentences explaining *why* this paper was ingested now (gap, conflict, new evidence, requested by user, related to current clinical case, etc.)
- At least one `[[wiki/category/stem]]` wikilink to an existing wiki page that this paper reinforces, contradicts, or extends.

**Wikilink lookup MUST use `qmd query` (MCP tool) — never `grep`, `find`, or `ls` over wiki/.** At this repo's scale a filesystem scan is slow and misses cross-category matches; qmd hybrid search returns relevant candidates in under 1 second. (Live page/paper counts are computed at deploy time into `interactives/wiki-stats-live.html` — never hard-coded here, so this file can't go stale.)

**Soft reminder (non-blocking, not lint-enforced):** before writing `## Why Ingested`, skim the paper's Methods against [[overviews/evidence-appraisal-toolkit]]'s study-type reading-order table (RCT: randomization/allocation concealment/ITT/CONSORT; observational: confounder adjustment/clustering/immortal-time bias; SR+MA: I²/funnel plot/pre-specified subgroups). This is a habit prompt, not a required field — it exists to catch inflated effect sizes or unchecked assumptions before they get cited elsewhere in the wiki.

Example:
```
## Why Ingested

기존 [[implants/isq/andersson-2019-rfa-factors-5year-neoss-survival]]의 ISQ ≥65 threshold가 5Y-PSZ implant에 적용되는지 의문. 본 RCT (Konuklu 2026)는 5개 osteotomy protocol을 직접 비교해 임계값 보강 근거로 활용.
```

Rationale: a 2-minute cost at ingest turns later overview synthesis from a cold start into a warm assembly. See `agenda/2026-05-26_synthesis-enforcement-setup.md` for the design.

## Step 3 — Write `wiki/{category}/{stem}.md`

```yaml
---
title: "Paper Title"
authors: Author list
year: YYYY
date: YYYY-MM-DD       # publication date; fall back to ingest date (YYYY-MM-DD) when unknown
doi: DOI
source: {stem}.md
category: [category-folder]
evidence_level: sr+ma  # study-type label; see vocabulary below (renamed from `confidence:` 2026-07-15)
pdf_path: /Users/oracleneo/llm-wiki/papers/{stem}.pdf
pdf_filename: {stem}.pdf
source_collection: external
tags: []
---

## Three-line Summary
(Line 1: study type, n, context — what was studied)
(Line 2: primary result / key finding with numbers)
(Line 3: clinical implication or key limitation)

## 세줄요약
(줄1: 연구유형·n·맥락 — 연구 대상/설계)
(줄2: 핵심 결과/수치)
(줄3: 임상적 의미 또는 핵심 한계)

## Summary
## Key Contributions
## Methodology
## Results
## Related Papers
- [[category/page]] — relationship
```

### `evidence_level:` vocabulary

> **Rename note (2026-07-15):** 이 필드는 이전 `confidence:`였다. userPreferences v4의 세션 확신도 2태그([확인]/[미검증], = *검증 상태* 축)와 개념 충돌을 없애기 위해 study-type = *근거 수준* 축임을 명시하는 `evidence_level:`로 리네이밍. Forward-only — 기존 페이지의 `confidence:`는 grandfather(감사 스크립트가 두 키를 모두 인식하게 하거나, 일괄 치환 마이그레이션은 별도 agenda로). 두 축을 구분: `evidence_level:`은 논문의 연구설계 강도, 세션 [확인]/[미검증]은 이번 세션에서 도구로 출처를 확인했는지.

Pick the **single best label** for the study type. Ordered roughly from highest to lowest evidence weight:

| Value | Applies to |
|---|---|
| `sr+ma` | Systematic review + meta-analysis (incl. umbrella review) |
| `sr` | Systematic review without meta-analysis |
| `rct` | Randomized controlled trial |
| `prospective` | Prospective cohort / prospective case series |
| `retrospective` | Retrospective cohort / chart review |
| `cross-sectional` | Cross-sectional study, survey |
| `case-report` | Case report or small case series (n < 10) |
| `in-vivo` | In vivo clinical/animal experimental study not covered above |
| `animal` | Animal-only experimental study (dog, rat, etc.) |
| `in-vitro` | Bench / laboratory study |
| `narrative-review` | Narrative review, perspective, expert commentary |
| `consensus` | Consensus statement / position paper |
| `synthesis` | Multi-paper synthesis page (wiki overviews); not external study type |

### `date:` field

- Publication date in `YYYY-MM-DD` format when known (use journal publication or e-pub date).
- `YYYY-01-01` when only year is known.
- If neither is recoverable from the paper, fall back to ingestion date (`YYYY-MM-DD` of when added to wiki).

### `superseded_by:` — living-document supersession (optional field)

The wiki is a living document: a paper page is not an ingest-time snapshot, it gets updated by later evidence. When a newer paper we hold **overturns the clinical bottom line** of an older page we hold, mark the *older* page. This converts the manual prose-update habit into a machine-checkable signal (`scripts/supersession-audit.py`).

**This is a clinical judgment, not a mechanical year comparison.** Newer ≠ superior — a 2026 narrative-review does NOT supersede a 2022 SR+MA. Set the field only when the newer page genuinely beats the older one on evidence weight or currency, and only between pages we actually hold.

**Forward-only trigger (no backfill needed).** At ingest of a new page, ask: *"does this overturn an existing page's bottom line?"* If yes, edit the *older* page — add the field + banner. Pre-existing pages are never bulk-scanned (same grandfather logic as `## Why Ingested`).

Two frontmatter fields on the **superseded (older)** page:

```yaml
superseded_by: tisci-2026-isq-it-mbl-survival-sr-ma   # newer stem(s); comma-separated if >1; must exist in wiki/
superseded_scope: full                                # full | partial
```

- `full` — the older page's conclusion is replaced; prefer the newer page for all current decisions.
- `partial` — only part of the page is outdated, or the page retains standalone value (e.g. first-of-kind synthesis, historical anchor). Use this rather than overstating `full`.

Plus a banner callout at the **top of the body** (right after frontmatter, before `## Three-line Summary` / `## 세줄요약`). Obsidian and Quartz both render `[!warning]`/`[!note]` callouts natively — no build change:

```markdown
> [!warning] Superseded (full) → [[tisci-2026-isq-it-mbl-survival-sr-ma]]
> 48-study SR+MA (r=0.44, p<0.001) overturns this 12-study NS result. (set 2026-05-31)
```

For `partial`, use `> [!note] Partially superseded → [[newer-stem]]` and state what the page still offers.

**Decay is computed, never stored.** Do NOT add a decay/staleness field — a stored decay value rots (the same reason `overview-thesis-staleness.py` exists). `supersession-audit.py` computes it each run: high-evidence pages (`sr+ma`/`sr`/`rct`) older than 5y and not superseded are flagged as "verify still current" candidates.

Design: `agenda/2026-05-31_supersession-decay-setup.md`.

### `relations:` — typed entity edges (optional field)

`[[wikilinks]]` encode *that* two pages relate; they don't encode *how*. The `## Why Ingested` section already states the relationship in prose ("X를 보강", "Y로 확장", "Z와 대비"). Lifting that into a structured frontmatter block turns overview synthesis from a cold start (re-read every page to infer relationships) into a warm assembly (the typed graph is already there). `superseded_by` is intentionally NOT part of this — it has its own audited field and banner.

To find `target` stems, use `qmd query` — do NOT scan wiki/ with grep/find. Example: `qmd query "PDRN bone regeneration"` returns the top candidate stems in under 1 second.

Optional block on the **citing (newer) page**, pointing out to the pages it relates to:

```yaml
relations:
  - type: extends
    target: manfredini-2023-polydeoxyribonucleotides-pre-clinical-findings-bone-healing
  - type: reinforces
    target: ku-2025-polydeoxyribonucleotide-pdrn-dentistry-narrative-review
```

Relation vocabulary (5 types; pick the single best per edge):

| `type` | meaning | Why-Ingested 표현 예 |
|---|---|---|
| `extends` | builds on / expands target's scope or depth | "확장", "deep-dive", "적응증 확장" |
| `reinforces` | independently confirms / strengthens target | "보강", "재확인", "일관", "짝을 이룸" |
| `contradicts` | findings conflict with target | "반박", "상충", "대비되는 결과" |
| `refines` | narrows / qualifies target's conclusion | "한정 시나리오 강화", "조건부", "scope 제한" |
| `applies-to` | clinical/methodological application of target | "프로토콜 적용", "한국 임상 contextualization" |

- `target` must be an existing wiki stem (validated by `scripts/relations-audit.py`).
- Forward-only / grandfather: structure relations for **new** pages at ingest; old pages are not bulk-scanned. The audit reports a machine-readable typed-edge export (`logs/{date}_relations-graph.json`) for Quartz/custom rendering — Obsidian's graph view can't distinguish edge types, so the JSON export is where typed-edge value is harvested.

## Step 4 — Update `index.md`

Add a one-line entry under the correct category.

## Step 5 — Refresh search index (qmd)

A new page is invisible to semantic search until qmd re-indexes and embeds it. Run after the wiki/sources files are written:

```bash
export PATH="/opt/homebrew/bin:$PATH"   # brew node(v25+) 강제 — 구 node v18이 앞서면 ABI 불일치로 qmd 깨짐
cd /Users/oracleneo/llm-wiki
qmd update   # 파일시스템 재스캔 (신규/변경/삭제 반영)
qmd embed    # 신규 문서만 임베딩 (incremental — 1~2편이면 수 초). 전체 재임베딩(-f)은 ~2.5h이므로 금지
```

The MCP daemon picks up new vectors automatically — no restart needed.

---

## PDF Management Rules

- **Always copy, never symlink.** `cp` from Downloads or external into `papers/`.
- `pdf_path` always points inside `/Users/oracleneo/llm-wiki/papers/`. Never use `~/Downloads/`.
- `pdf_filename` must match `basename(pdf_path)`.
- **1:1 matching enforced.** Every PDF in `papers/` must have a matching `sources/{stem}.md`. After any ingest or rename operation, run:
  ```python
  pdfs = {stem for stem in [os.path.splitext(f)[0] for f in os.listdir('papers/') if f.endswith('.pdf')]}
  srcs = {stem for stem in [os.path.splitext(f)[0] for f in os.listdir('sources/') if f.endswith('.md')]}
  orphan_pdfs = pdfs - srcs   # → delete these
  orphan_srcs = srcs - pdfs   # → warn (missing PDF)
  ```
  Delete all `orphan_pdfs` immediately. Pre-rename originals and duplicate `(1)` copies count as orphans and must be deleted.

## File Naming Convention

All three tiers share the same stem:

```
{first-author-lastname}-{year}-{first-5-title-words}.{ext}
```

- Lowercase, special chars stripped, spaces → `-`
- Year is 4 digits
- Example: `jung-2023-immediate-implant-placement-sinus.pdf`
