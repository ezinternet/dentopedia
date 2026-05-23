# LLM Wiki — Dentistry (치과학)

A personal knowledge base of dental research papers, following [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/1dd0294ef9567971c1e4348a90d69285):

```
Original PDF → sources/*.md (LLM summary) → wiki/{category}/*.md (final page)
```

**Language policy**: Wiki body content is in English (RAG-friendly, preserves technical terms). Each wiki page includes a `## 한줄요약` section (Korean one-line summary) immediately above `## Summary`. Conversation can be in any language (including Korean).

**Term notation rule**: When using technical/medical terms in conversation, ALWAYS write them as **한국어 (English, 약어)** format. Example: 골-임플란트 접촉률 (Bone-to-Implant Contact, BIC), 골밀도화 (Osseodensification, OD), 임플란트 안정성 지수 (Implant Stability Quotient, ISQ). No exceptions.

---

## THE FOUR RULES (do not violate)

These rules prevent hallucination and keep every claim traceable.

1. **No web search.** Never use `WebSearch` or `WebFetch` to fill gaps. Every answer must be grounded in papers we actually have.
2. **Answer from the wiki first.** Use `sources/` and `wiki/` as the only sources of truth.
3. **If the wiki is insufficient, re-read the PDF.** Go to `papers/{stem}.pdf` and extract more detail with `pypdf`. Then update the wiki.
4. **If the wiki has no paper on the topic, say so.** Tell the user *"I don't have a paper on this — please give me the PDF."* Do not improvise.

These rules apply to **every** response, including overview pages.

---

## Repository Structure

The repo has two layers: **KNOWLEDGE** (papers/sources/wiki — the substrate, reusable knowledge atoms) and **OPERATIONS** (agenda/slides/interactives/peer-review/note-meeting/scripts/logs — where knowledge is converted into outputs).

```
llm-wiki/
├── CLAUDE.md                   # This file — agent行動 rules
├── SOP.md                      # Human-facing operating procedure
├── index.md                    # Page catalog
│
│ ── KNOWLEDGE (the substrate) ──
├── papers/                     # Original PDFs (cp, never symlink)
│   └── {author}-{year}-{title-5-words}.pdf
├── sources/                    # PDF summaries (English)
│   └── {author}-{year}-{title-5-words}.md
├── wiki/                       # Wiki pages (English)
│   ├── implants/               # 임플란트
│   ├── endodontics/            # 근관치료
│   ├── periodontics/           # 치주치료
│   ├── dental-materials/       # 치과재료 (general)
│   ├── resin/                  # 레진
│   ├── resin-bonding/          # 레진접착
│   ├── sinus-lift/             # 상악동거상술
│   ├── immediate-implant/      # 즉시식립
│   ├── prosthetic-materials/   # 보철재료
│   ├── inlay/                  # 인레이
│   └── overviews/              # Synthesis pages (cross-category)
│
│ ── OPERATIONS (knowledge → output) ──
├── agenda/                     # 작업 명세서 (Goal·Input·Output·Done)
├── interactives/               # HTML 시각화·계산기·의사결정 도구
├── slides/                     # 강의·발표 자료 (wiki가 1차 입력)
├── peer-review/                # 외부 paper 리뷰 (저널 reviewer 의뢰)
├── note-meeting/               # 미팅 기록 (1 미팅 = 1 파일)
├── scripts/                    # 자동화 (ingest watcher, lint)
└── logs/                       # audit 산출 로그
```

## File Naming Convention

All three tiers share the same stem:

```
{first-author-lastname}-{year}-{first-5-title-words}.{ext}
```

- Lowercase, special chars stripped, spaces → `-`
- Year is 4 digits
- Example: `jung-2023-immediate-implant-placement-sinus.pdf`

## Categories

| Category folder | Korean | Includes |
|---|---|---|
| `implants` | 임플란트 | Implant design, bone type, survival, failure risk, MBL, soft tissue |
| `implants/isq` | 임플란트·ISQ | ISQ/RFA measurement, stability dip, loading decision thresholds |
| `implants/surface` | 임플란트·표면처리 | SLA, CA, UV surface technology, osseointegration |
| `bone-regeneration` | 골재생 | GBR, ridge preservation, socket management, peri-implantitis GBR |
| `immediate-implant` | 즉시식립 | Immediate implant placement protocols, outcomes, esthetic risk |
| `sinus-lift/lateral` | 상악동거상술·측방 | Lateral window approach, membrane, grafting materials |
| `sinus-lift/transcrestal` | 상악동거상술·경치조골 | Transcrestal (osteotome/balloon/osseodensification) approaches |
| `endodontics/eal` | 근관치료·근관장측정 | EAL accuracy, working length, apex locator devices |
| `endodontics/irrigation` | 근관치료·세정 | Irrigant activation (PUI, ANP, sonic), NaOCl protocols |
| `endodontics/anatomy` | 근관치료·해부 | Canal morphology, access cavity, MB2, CBCT-guided access |
| `periodontics` | 치주치료 | Periodontal disease, regeneration, SPT |
| `dental-materials` | 치과재료 | Impression materials, zirconia, ceramics |
| `digital-workflow` | 디지털워크플로우 | IOS accuracy, CBCT, CAD/CAM, guided surgery |
| `resin` | 레진 | Composite resin, polymerization, shrinkage |
| `resin-bonding` | 레진접착 | Adhesive systems, bonding mechanisms, dentin adhesion |
| `prosthetic-materials` | 보철재료 | Screw vs cement retention, zirconia crowns, CAD/CAM prosthetics |
| `drug` | 전신질환·약물 | Systemic disease management, drug interactions, MRONJ, anticoagulants |
| `oral-surgery` | 구강외과 | Extractions, nerve injuries, surgical complications |
| `inlay` | 인레이 | Inlay/onlay restorations, ceramic inlays |
| `evidence-appraisal` | 근거평가·통계방법론 | EBM/EBD critical appraisal, SR/MA methodology, biostatistics (p-value/CI/OR/RR/HR/NNT), common mistakes |
| `overviews` | 종합 | Synthesis pages spanning multiple categories |

Classify by **method/procedure**, not by disease or anatomy.

---

## Adding a New Paper

Say: *"Add this paper to the wiki: /path/to/paper.pdf"*

The agent will do all four steps automatically.

### Step 1 — Copy PDF to `papers/` and extract text

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

### Step 2 — Write `sources/{stem}.md`

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

## One-line Summary
## 1. Document Information
## 2. Key Contributions
## 3. Methodology and Architecture
## 4. Key Results and Benchmarks
## 5. Limitations and Future Work
## 6. Related Work
## 7. Glossary
```

### Step 3 — Write `wiki/{category}/{stem}.md`

```yaml
---
title: "Paper Title"
authors: Author list
year: YYYY
date: YYYY-MM-DD       # publication date; fall back to ingest date (YYYY-MM-DD) when unknown
doi: DOI
source: {stem}.md
category: [category-folder]
confidence: sr+ma      # see vocabulary below
pdf_path: /Users/oracleneo/llm-wiki/papers/{stem}.pdf
pdf_filename: {stem}.pdf
source_collection: external
tags: []
---

## 한줄요약
(Korean one-liner: study type, n, key finding in plain Korean)

## Summary
## Key Contributions
## Methodology
## Results
## Related Papers
- [[category/page]] — relationship
```

### `confidence:` vocabulary

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

### Step 4 — Update `index.md`

Add a one-line entry under the correct category.

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

Each session should produce 5–15 new or updated wiki pages.

## Browsing with Obsidian

Install [Obsidian](https://obsidian.md/) (free) and open `/Users/oracleneo/llm-wiki` as a Vault. You get graph view, `[[wikilinks]]` navigation, and full-text search. Obsidian only reads files — it does not interfere with agent edits.

---

## Design Principles

- **3-tier**: Raw PDF (immutable) → sources/*.md → wiki/**/*.md
- **English only** in wiki content (RAG-friendly; Korean conversation is fine)
- **Obsidian compatible**: `[[wikilinks]]`, plain markdown
- **No web search**: rule #1 above

When in doubt, follow rule #1.

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- ALWAYS read graphify-out/GRAPH_REPORT.md before reading any source files, running grep/glob searches, or answering codebase questions. The graph is your primary map of the codebase.
- IF graphify-out/wiki/index.md EXISTS, navigate it instead of reading raw files
- For cross-module "how does X relate to Y" questions, prefer `graphify query "<question>"`, `graphify path "<A>" "<B>"`, or `graphify explain "<concept>"` over grep — these traverse the graph's EXTRACTED + INFERRED edges instead of scanning files
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
