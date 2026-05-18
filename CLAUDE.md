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

```
llm-wiki/
├── CLAUDE.md                   # This file
├── index.md                    # Page catalog
├── papers/                     # Original PDFs (cp, never symlink)
│   └── {author}-{year}-{title-5-words}.pdf
├── sources/                    # PDF summaries (English)
│   └── {author}-{year}-{title-5-words}.md
└── wiki/                       # Wiki pages (English)
    ├── implants/               # 임플란트
    ├── endodontics/            # 근관치료
    ├── periodontics/           # 치주치료
    ├── dental-materials/       # 치과재료 (general)
    ├── resin/                  # 레진
    ├── resin-bonding/          # 레진접착
    ├── sinus-lift/             # 상악동거상술
    ├── immediate-implant/      # 즉시식립
    ├── prosthetic-materials/   # 보철재료
    ├── inlay/                  # 인레이
    └── overviews/              # Synthesis pages (cross-category)
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
