# LLM Wiki — Dentistry (치과학)

A personal knowledge base of dental research papers, following [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/1dd0294ef9567971c1e4348a90d69285).

**Canonical publish URL** (single source — every hard-coded absolute URL below references THIS; if the deploy domain changes, change it here and grep for the old host):

```
PUBLISH_BASE = https://ezinternet.github.io/dentopedia
```

This repo has **two layers** — read both before acting; skimming only the first pipeline misses OPERATIONS routing:

```
KNOWLEDGE (the substrate — reusable knowledge atoms):
  Original PDF → sources/*.md (LLM summary) → wiki/{category}/*.md (final page)

OPERATIONS (knowledge → outputs):
  agenda/ (작업 명세) → slides/ · interactives/ · peer-review/ → logs/
  note-meeting/ records decisions that feed back into wiki/ and agenda/
```

Full routing rules for OPERATIONS are in the **OPERATIONS — Routing & Cross-link Rules** section below. Any new artifact must be routed to KNOWLEDGE or OPERATIONS — never authored ad-hoc.

**Ingest procedure lives in `INGEST.md`** — the full paper-ingestion pipeline (Step 0–5, PubMed-text / abstract-only 분기, PDF rules, `evidence_level:`/`superseded_by:`/`relations:` field definitions, file-naming convention) was split out to keep this file lean and loaded every session. When the task is *adding a paper to the wiki* (`인제스트`, `Add this paper`, a PDF path), open `INGEST.md` first. Answering a question does not require it.

**Category map lives in `wiki/_meta/categories.md`** — the full 60+ category list and subcategory routing rules are the single source of truth there (see *Categories* below). This file intentionally does NOT enumerate categories, to avoid the two-copies-drift problem.

**Language policy**: Wiki body content is in English (RAG-friendly, preserves technical terms). Every wiki page AND every source page carries a **bilingual three-line summary** as two separate sections, in this order: `## Three-line Summary` (English) immediately followed by `## 세줄요약` (Korean). On wiki pages this pair sits immediately above `## Summary`; on source pages it sits immediately above `## 1. Document Information`. Both languages are mandatory for new pages. Conversation can be in any language (including Korean).

**Three-line Summary format**: Each section contains exactly three lines (blank line between each):
- Line 1: Study type, n, context — what population/design was studied
- Line 2: Primary result / key finding with numbers
- Line 3: Clinical implication or key limitation

**Overview Korean digest (mandatory for `wiki/overviews/` pages)**: English body is too dense to skim in Korean, so every overview/synthesis page additionally carries a **`## 한국어 핵심요약` block at the very TOP** — placed immediately after the frontmatter, ABOVE `## Three-line Summary`. Format it as an Obsidian callout `> [!summary] 한국어 핵심요약` with **~10 bullets** (longer is fine) capturing: the thesis/bottom line, key numbers, the main branches/decision points, contrasts/exceptions, and the clinical takeaway. Use the **한국어 (English, 약어)** term-notation rule inside the bullets. The English body stays intact (RAG policy unchanged) — this block is a Korean reading aid layered on top. Mandatory for all new overviews going forward.

**Term notation rule**: When using technical/medical terms in conversation, ALWAYS write them as **한국어 (English, 약어)** format. Example: 골-임플란트 접촉률 (Bone-to-Implant Contact, BIC), 골밀도화 (Osseodensification, OD), 임플란트 안정성 지수 (Implant Stability Quotient, ISQ). No exceptions.

---

## THE FOUR RULES (do not violate)

These rules prevent hallucination and keep every claim traceable.

1. **Answer only from ingested knowledge.** When *answering a question*, never use `WebSearch`/`WebFetch` to fill gaps — every claim in an answer must be grounded in papers we actually hold. This is a rule about *answer generation*, not about *acquiring* papers: gathering **new** literature is a separate, explicit act (see note below) and is allowed only through the ingest pipeline.
2. **Answer from the wiki first.** Use `sources/` and `wiki/` as the only sources of truth. Retrieve with QMD (local semantic search — see *Searching the Wiki*), never from the web.
3. **If the wiki is insufficient, re-read the PDF.** Go to `papers/{stem}.pdf` and extract more detail with `pypdf`. Then update the wiki.
4. **If the wiki has no paper on the topic, say so.** Tell the user *"I don't have a paper on this — please give me the PDF, or run an ingest sweep."* Do not improvise clinical claims from memory.

These rules apply to **every** response, including overview pages.

**Scope of Rule #4 — factual claims, not clinical reasoning.** Rule #4 governs *citable factual claims* (an efficacy number, a survival %, a threshold, "study X found Y"). It does NOT forbid **clinical reasoning synthesized from papers we hold**: weighing options for a case, explaining a mechanism, walking through a decision the held evidence supports, or answering "how would you approach / explain this?" That reasoning is encouraged — it is the point of the wiki. The boundary: reasoning may combine and apply what our papers say, but must not smuggle in a specific factual claim (a number, a named-study result) that no held paper supports. When a case question needs a fact we don't hold, name the gap (Rule #4) and reason around it from what we do hold — don't fabricate the number, and don't refuse the whole question.

**Ingest is not a Rule-#1 violation — it is a different path.** QMD and PubMed MCP are not exceptions carved out of the "no web" rule; they operate on different axes. QMD is *local retrieval* (indexes only this repo — see *Searching the Wiki*). PubMed MCP / `literature-surveillance` is the *ingest entry point*: it may reach external sources, but only to **acquire** papers, which must then pass through the full 3-tier pipeline (`papers/` → `sources/` → `wiki/`) before any claim from them is used in an answer. Never let PubMed text bypass the pipeline to answer a live question directly.

---

## Repository Structure

The repo has two layers: **KNOWLEDGE** (papers/sources/wiki — the substrate, reusable knowledge atoms) and **OPERATIONS** (agenda/slides/interactives/peer-review/note-meeting/scripts/logs — where knowledge is converted into outputs).

```
llm-wiki/
├── CLAUDE.md                   # This file — agent 행동 rules
├── INGEST.md                   # Paper-ingestion pipeline (Step 0–5, fields, PDF rules)
├── SOP.md                      # Human-facing operating procedure
├── index.md                    # Page catalog
│
│ ── KNOWLEDGE (the substrate) ──
├── papers/                     # Original PDFs (cp, never symlink) — {author}-{year}-{title-5-words}.pdf
├── sources/                    # PDF summaries (English) — same stem, .md
├── wiki/                       # Wiki pages (English), one folder per category
│   ├── _meta/categories.md     # ← SINGLE SOURCE OF TRUTH for the category list
│   ├── {category}/             # 60+ clinical categories (see wiki/_meta/categories.md)
│   └── overviews/              # Synthesis pages (cross-category)
│
│ ── OPERATIONS (knowledge → output) ──
├── agenda/                     # 작업 명세서 (Goal·Input·Output·Done)
├── interactives/               # HTML 시각화·계산기·의사결정 도구
├── slides/                     # 강의·발표 자료 (wiki가 1차 입력)
├── peer-review/                # 외부 paper 리뷰 (저널 reviewer 의뢰)
├── note-meeting/               # 미팅 기록 (1 미팅 = 1 파일)
├── scripts/                    # 자동화 (ingest watcher, lint, audits)
└── logs/                       # audit 산출 로그
```

The concrete list of `wiki/{category}/` folders is **not** duplicated here — it lives only in `wiki/_meta/categories.md`. Adding it in two places is how the two copies drift (they had, before 2026-07-15).

## Categories

전체 카테고리 목록(60여 개)·서브카테고리 분기 규칙은 **`wiki/_meta/categories.md`**가 단일 출처다. 이 파일은 라우팅 원칙만 담는다.

**라우팅 규칙 (요약)**
1. 신규 paper는 먼저 `qmd query`로 유사 페이지를 찾아 그 페이지의 `category`를 따른다.
2. 유사 페이지가 없으면 `wiki/_meta/categories.md`에서 가장 가까운 folder 선택.
3. 분류 기준은 **method/procedure** — disease·anatomy가 아니다.
4. 서브카테고리 분기(예: `implants/surface/plasma`, `immediate-implant/socket-shield`, `endodontics/cold-plasma`)는 categories.md의 `Includes` 괄호 안 `→` 지시를 따른다.
5. 어느 folder에도 안 맞으면 임의 신설하지 말고 `wiki/_meta/categories.md`에 항목을 추가하며 신설한다.

---

## Adding a New Paper → see `INGEST.md`

The full ingest pipeline moved to **`INGEST.md`**. In brief: *"Add this paper to the wiki: /path/to/paper.pdf"* or *"인제스트 해줘"* (parallel subagents, one per pending paper). The pipeline is Step 0 (dedup + retraction gate) → 1 (copy PDF + extract, with PubMed-text / abstract-only 분기) → 2 (`sources/{stem}.md`) → 3 (`wiki/{category}/{stem}.md`) → 4 (`index.md`) → 5 (qmd re-index). Field definitions (`evidence_level:`, `superseded_by:`, `relations:`) and the file-naming convention are all in `INGEST.md`.

> **Field rename (2026-07-15):** the wiki page's study-type field is `evidence_level:` (was `confidence:`), to stop it colliding with userPreferences' 세션 확신도 2태그 ([확인]/[미검증]). Two different axes: `evidence_level:` = 논문 연구설계 강도; [확인]/[미검증] = 이번 세션 도구 검증 여부. Forward-only; existing pages' `confidence:` grandfathered. Definition + vocabulary in `INGEST.md`.

---

## OPERATIONS — Routing & Cross-link Rules

KNOWLEDGE is the substrate; OPERATIONS is where it gets converted into outputs (slides, calculators, review reports, meeting decisions). Without these rules every output drifts away from its source wiki page.

### 1. Routing — 어디에 만드는가

When creating any new artifact, ask in order:

1. **재사용되는 지식인가?** → `wiki/{category}/` (단일 paper) or `wiki/overviews/` (cross-paper synthesis)
2. **시간·이벤트 기록인가?** → `note-meeting/`
3. **외부 deliverable인가? (슬라이드·인터랙티브·peer review)** → 해당 OPERATIONS 폴더
4. **외부 deliverable의 작업 명세인가?** → `agenda/`

**Hard rule**: `slides/`, `interactives/`, `peer-review/` 산출물은 반드시 `agenda/` 파일이 선행되어야 한다. agenda 없는 산출물은 출처·done 기준 추적이 끊긴다.

### 2. File Naming — OPERATIONS

```
agenda/YYYY-MM-DD_<kebab-case-topic>.md
interactives/YYYY-MM-DD_<kebab-case-topic>.html
slides/YYYY-MM-DD_<event-or-audience>_<topic>.md
peer-review/YYYY-MM_<journal-code>_<topic>.md
note-meeting/YYYY-MM-DD_<meeting-type>.md
```

날짜 prefix는 정렬·검색을 위함. `_template.md` 같은 시스템 파일은 날짜 prefix 면제.

### 3. Frontmatter Cross-link — OPERATIONS 파일 전 필수

```yaml
---
title: "..."
type: agenda | interactive | slides | peer-review | meeting
date: YYYY-MM-DD
status: draft | in-progress | review | done | archived
# 아래 3개 중 최소 하나는 비어있지 않아야 함
source_wiki:                              # 이 산출물의 근거가 된 wiki 페이지들
  - wiki/<category>/<stem>.md
agenda: agenda/<date>_<topic>.md          # slides/interactives/peer-review 필수
output_wiki:                              # 이 산출물이 갱신·생성한 wiki 페이지 (meeting에서 자주 발생)
  - wiki/<category>/<stem>.md
---
```

`source_wiki` · `agenda` · `output_wiki` 세 필드가 모두 비어있는 OPERATIONS 파일은 **orphan**으로 간주하고 lint에서 경고한다.

### 4. agenda Workflow

새 작업은 agenda 파일 1개로 시작:

```bash
cp agenda/_template.md agenda/$(date +%Y-%m-%d)_<topic>.md
```

agenda는 Goal·Input·Output·Done이 박힌 단일 명세서. 진행되며 status 갱신 (`draft` → `in-progress` → `review` → `done` → `archived`).

agenda에서 파생된 산출물(slides·interactive·overview)은 자신의 frontmatter에 `agenda:` 백링크를, 그리고 agenda 파일의 `# Output` 섹션에 산출물 경로를 양쪽으로 박는다.

### 5. note-meeting Workflow

미팅 1회 = 파일 1개. 결정 사항(decisions)이 wiki SOP나 임상 프로토콜에 반영되어야 하는 경우:

- meeting note frontmatter의 `output_wiki:` 에 갱신될 wiki 페이지 경로
- followup이 필요하면 `followup_agenda:` 에 신설할 agenda 파일 경로 (그리고 실제로 agenda 신설)

미팅 → agenda → 산출물의 chain이 끊기면 미팅은 메모로만 남고 클리닉 SOP에 반영이 안 된다.

---

## Knowledge Compounding

The most valuable pages are `wiki/overviews/` pages that synthesize across papers. After a good Q&A session, say:

> *"Save this as an overview page in wiki/overviews/"*

A productive session typically yields several new or updated wiki pages — but this is an observation, **not a quota**. The wiki's whole philosophy is *signal, not gate* (gates trigger burnout/avoidance in clinical workflows); a per-session page count would be exactly the kind of gate the audit design deliberately avoids. Write pages when there is real synthesis to capture, not to hit a number.

### Overviews domain map (auto-generated — do NOT hand-edit)

`interactives/overviews-map.html` is the at-a-glance browser for all `wiki/overviews/` pages, grouped by clinical domain (search + expand/collapse, titles link to each page). It is **auto-generated** by `scripts/build-overviews-map.py` from each overview's frontmatter (`title`/`date`); the deploy workflow regenerates it on every push to `wiki/**`, and the homepage `wiki/index.md` embeds it via `<iframe>`. The iframe src uses the full absolute `PUBLISH_BASE` URL (Quartz `CrawlLinks` rewrites root-relative/`.html` srcs, so the iframe and the interactives-index link both need the full `{PUBLISH_BASE}/...` URL).

Never edit `overviews-map.html` by hand (it's overwritten). A new overview appears automatically once its file lands in `wiki/overviews/`; if its `stem` matches no domain keyword in the script's `DOMAINS` map, it falls into the `기타 · 미분류` bucket (never dropped). To re-home it, add its keyword to `DOMAINS` in `scripts/build-overviews-map.py`. Regenerate locally with `python3 scripts/build-overviews-map.py`.

### Interactive tools — deploy-time freshness (two classes)

The `interactives/` chairside calculators/decision-trees/simulators split into two classes with different freshness mechanisms:

- **메타·통계 도구 (Class A)** — numbers ARE repo state (paper/overview/category counts, ingest timeline, 발행연도 histogram). `scripts/build-wiki-stats.py` regenerates **`interactives/wiki-stats-live.html`** on every deploy from live repo state + git history (reuses the v4 render engine; only the JS DATA blocks + header scalars are injected). It is the single always-current dashboard. The date-stamped lineage (`wiki-evolution` v1~v4, `wiki-growth-curve`) stays **frozen as the evolution archive** — never regenerated (mutating a dated snapshot would make its filename lie). Never hand-edit `wiki-stats-live.html` (overwritten). git cumulative needs full history → deploy uses `fetch-depth: 0`.
- **임상 결정 도구 (Class B)** — numbers are clinical thresholds an LLM extracted from specific papers (ISQ ≥65, r=0.44, doses, risk %). A deploy script **cannot** safely re-extract these (would hallucinate/corrupt clinical values → violates Rule #1), so they are **not auto-rewritten**. Instead `scripts/interactive-staleness.py` emits a signal when a tool's `source_wiki:` page is newer than the tool (STALE → re-author with LLM) or a source path vanished (BROKEN). Re-authoring stays a human/LLM-in-the-loop step. This matches the wiki's signal-not-gate philosophy.

Deploy order (in `deploy-pages.yml`): `build-wiki-stats.py` → `build-interactives-index.py` (so the live tool is indexed) → `interactive-staleness.py` (non-blocking) → copy `interactives/` into the site.

## Daily Audit

A single entry-point runs all 15 audits and writes their logs to `logs/`:

```bash
python3 scripts/daily-audit.py
```

The 15 audits — 3 classic + 1 rationale (errors block) + 11 signals:

| Audit | Type | Purpose |
|---|---|---|
| `lint.py` | error | wiki frontmatter required fields |
| `operations-lint.py` | error | OPS files (agenda/slides/interactives) cross-link chain |
| `orphan-check.py` | error | PDFs ↔ sources 1:1 matching |
| `synthesis-backlog.py` | signal | sources/ not referenced by any overview, stale ≥30d |
| `ingest-rationale-lint.py` | error (post-cutoff only) | `## Why Ingested` on sources ingested ≥ 2026-05-27 |
| `category-overflow.py` | signal | wiki categories with ≥5 unsynthesized papers → overview candidates |
| `overview-thesis-staleness.py` | signal | overview의 git log를 wikilink-only vs thesis edit으로 분류해 진짜 stale overview 식별 (mtime은 wikilink-only ingest로 갱신돼 부정확) |
| `overview-coverage-lint.py` | signal | overview 본문 cov% (linked paper 중 본문 author·year로 인용된 비율) — 낮으면 thesis 분기·표·결정 트리에 paper 반영 안 됨 |
| `doi-duplicate-check.py` | signal | 동일 DOI·다른 stem 검출 + 제목 정규화 fallback(한쪽 DOI 비거나 불일치라 DOI로 못 잡는 동일논문) — orphan-check가 못 잡는 cross-stem 중복 가시화 |
| `supersession-audit.py` | signal | `superseded_by` 깨진 링크 + 필드↔본문 배너 sync + decay 후보(sr+ma/sr/rct 중 5년↑ 미대체, 카테고리·중심성 집계) — living-document 갱신을 신호화 |
| `relations-audit.py` | signal | `relations:` typed edge target 실존·vocab 검증 + 타입 분포 + typed-edge JSON export(Quartz/custom 렌더용) |
| `link-integrity.py` | signal | 본문 `[[wikilink]]` 깨짐 + index.md 양방향 커버리지 (Astro-Han lint 개념 차용) |
| `interactive-staleness.py` | signal | 임상 interactive 도구의 `source_wiki` 근거가 도구보다 git상 최신이면 STALE(LLM 재작성 후보), 근거 경로 소실이면 BROKEN. meta/통계 도구는 제외(build-wiki-stats.py가 배포 때 재생성). 임상 수치 자동 재작성은 Rule #1 위배라 신호만 |
| `find-contradiction-candidates.py` | signal | 본문에 명시적 충돌 표현(contradict/counterpoint/반박 등)이 있으나 `relations: contradicts/refines` 엣지가 없는 논쟁 레이더 백필 후보. Tier1(대상 wikilink 지목)·Tier2(대상 불명/soft). 기계가 충돌을 확정하지 않고 신호만 — LLM이 두 페이지 읽고 판단해 엣지를 단다 |
| `deviation-audit.py` | signal | `logs/ingest-deviations.md` 집계 — 동일 유형 3회 이상이면 SOP 개정 후보 출력 (Rule-of-Three trigger) |

Signals never block. They're a mirror — the principle is that ingest pressure self-corrects via visibility, not via gates (which trigger burnout/avoidance in clinical workflows).

Run daily (manual or cron). The three key compounding metrics over time:
- **synthesis-backlog %**: should trend up (more sources getting linked from overviews).
- **category-overflow count**: should trend down as overviews get written.
- **thesis-staleness warn/info**: should stay low — overview 본문이 정기적으로 refresh되는지 보는 signal.

**Closing the loop — audit signals → morning briefing.** Audits only compound if someone reads them; leaving that to memory is the weak link. The intended terminal is a one-line badge in the morning-briefing pipeline (STALE overview N건, category-overflow N건, BROKEN link N건) so the day's top signals surface without opening `logs/`. Design: `agenda/2026-07-15_audit-to-briefing-bridge.md`.

Design rationale (audit set): see `agenda/2026-05-26_synthesis-enforcement-setup.md`.

## Searching the Wiki (QMD)

At this repo's scale plain `grep` starts missing cross-category overview matches, so the wiki uses **QMD** ([tobi/qmd](https://github.com/tobi/qmd)) — an on-device hybrid search engine (BM25 + vector + LLM re-ranking), all local, no cloud. Regardless of size, lookup goes through qmd first; `grep`/`index.md` is only a fallback when the daemon is down.

**QMD does NOT violate Rule #1.** It is local-first: it indexes and searches only the markdown files in this repo (`~/.cache/qmd/index.sqlite`), never the web. It *reinforces* Rule #1 by making local retrieval strong enough that web search is never tempting. QMD is a better `grep`, not a `WebSearch`.

Setup (one-time, run on the Mac): `bash scripts/setup-qmd.sh`. Embedding model is Qwen3 multilingual (CJK/Korean queries supported). MCP runs as an HTTP daemon at `localhost:8181`, exposed to Claude Code as the `qmd` MCP server.

Collections indexed: `wiki/`, `sources/`, `agenda/`, `note-meeting/` (markdown only; `papers/` PDFs are not indexed by QMD).

Search precedence when answering:

1. **QMD `query`** (hybrid, best quality) for concept/synthesis questions — e.g. "ISQ loading threshold across osteotomy protocols".
2. **QMD `search`** (BM25) for exact terms — author names, device names, specific values.
3. Fall back to `grep` / `index.md` only if the QMD daemon is down.

After every ingest (or daily), refresh the index so new pages are searchable:

```bash
qmd update && qmd embed     # re-scan + embed new docs only
```

This pairs cleanly with the daily audit — run it alongside `scripts/daily-audit.py`.

## Browsing with Obsidian

Install [Obsidian](https://obsidian.md/) (free) and open `/Users/oracleneo/llm-wiki` as a Vault. You get graph view, `[[wikilinks]]` navigation, and full-text search. Obsidian only reads files — it does not interfere with agent edits. QMD (search) and Obsidian (browse) layer cleanly: both only read files.

---

## Design Principles

- **3-tier**: Raw PDF (immutable) → sources/*.md → wiki/**/*.md
- **English only** in wiki content (RAG-friendly; Korean conversation is fine)
- **Obsidian compatible**: `[[wikilinks]]`, plain markdown
- **No web search**: rule #1 above
- **Signal, not gate**: audits surface state; they never block. Quotas and hard gates cause avoidance.
- **Single source of truth**: categories → `wiki/_meta/categories.md`; ingest → `INGEST.md`; publish URL → `PUBLISH_BASE` at top. Never a second copy.

When in doubt, follow rule #1.
