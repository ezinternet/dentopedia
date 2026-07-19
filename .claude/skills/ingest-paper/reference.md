# Ingest Paper — Reference

## Evidence Level Vocabulary

`evidence_level:` (wiki pages only — renamed from `confidence:` 2026-07-15; pre-existing pages that still say `confidence:` are grandfathered, do not bulk-migrate them). Pick the **single best label**.

Study types, roughly highest → lowest evidence weight:

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
| `synthesis` | Multi-paper wiki/overviews synthesis page — not an external study type |

Non-research document labels (administrative/legal/engineering primary sources, not on the evidence ladder):

| Value | Applies to |
|---|---|
| `regulation` | Korean health-insurance regulation — MOHW notice/decree/amendment (고시·훈령·개정) |
| `official-qa` | Official Q&A from MOHW/HIRA (유권해석) |
| `manual` | Practical guidebook / 실무편람 |
| `patent` | Patent disclosure (공개/등록특허공보) |

`in-vivo` vs `rct` note: a randomized-order crossover on human *testers* (operator-ergonomics, method-comparison) is `in-vivo`, not `rct` — `rct` is reserved for patient/disease-outcome allocation trials. `in-vitro` vs `in-vivo`: a manikin/typodont/bench setup with no living subject is `in-vitro` even if the paper's own prose says "in vivo study" loosely.

Full vocabulary + supersession-judgment rules: INGEST.md § `evidence_level:` vocabulary.

---

## Category

**Full list lives at [wiki/_meta/categories.md](../../../wiki/_meta/categories.md) — single source of truth. Do not copy it here.** A condensed table used to live in this section; it drifted (missing `implants/peri-implantitis` and others — self-flagged in `logs/ingest-deviations.md`, 2026-07-12 `fathi-2024-electronic-cigarettes-peri-implantitis-umbrella-review` entry) and was removed rather than re-synced, per CLAUDE.md's explicit anti-duplication rule for this exact list.

Classify by **method/procedure**, not disease/anatomy. Read categories.md's `Includes` column carefully — several categories carve specific sub-cases out to a sibling folder (e.g. dental-handpiece ↔ periodontics ↔ infection-control on aerosol/ultrasonic-scaler topics; check the carve-out note before assuming the obvious folder). Boundary calls escalate to Opus (SKILL.md Step 4).

---

## Sources Template

```markdown
---
title: "EXACT PAPER TITLE"
authors: First Author, Second Author, Third Author et al.
year: YYYY
doi: 10.XXXX/xxxxx
category: [category-folder]
pdf_path: /Users/oracleneo/llm-wiki/papers/{stem}.pdf
pdf_filename: {stem}.pdf
source_collection: external
---

## Why Ingested
{1–2 sentences: why this paper, now (gap / conflict / new evidence / requested / current case). At least one [[wiki/category/stem]] wikilink to a page this reinforces, contradicts, or extends. Look up the target via `qmd query` — never grep/find/ls over wiki/.}

## Three-line Summary
(Line 1: study type, n, context — what was studied)
(Line 2: primary result / key finding with numbers)
(Line 3: clinical implication or key limitation)

## 세줄요약
(줄1: 연구유형·n·맥락 — 연구 대상/설계)
(줄2: 핵심 결과/수치)
(줄3: 임상적 의미 또는 핵심 한계)

## 1. Document Information
- **Journal**: Journal Name Year;Vol(No):Pages
- **DOI**: {doi}
- **Institution**: Lead institution, Country

## 2. Key Contributions
- {Novel claim 1}
- {Novel claim 2}
- {Novel claim 3}

## 3. Methodology and Architecture
- **Design**: {RCT / SR+MA / retrospective / etc.}
- **Databases**: {PubMed, Cochrane, Scopus, etc.} (if SR)
- **n**: {number of studies / patients / teeth}
- **Outcomes**: {primary and secondary outcomes}

## 4. Key Results and Benchmarks
{Numbers, tables, p-values, effect sizes.}

## 5. Limitations and Future Work
- {Limitation 1}
- {Limitation 2}

## 6. Related Work
- {author-year}: {relationship}

## 7. Glossary
- **TERM**: definition
- **TERM**: definition
```

`## Why Ingested` is **mandatory** for papers ingested on/after 2026-05-27 (lint-enforced by `scripts/ingest-rationale-lint.py`). Pre-cutoff sources are grandfathered — no backfill.

**PubMed-text variant** (full text pulled via PubMed MCP, no PDF): replace `source_collection: external` → `pubmed-text`; drop `pdf_path`/`pdf_filename`; add `full_text:` (`false` if abstract-only), `pmid:`, `pmcid:` (if any), `source_url:`, `text_path:`/`text_filename:` pointing at `papers/{stem}.txt`. See INGEST.md Step 1-T.

**Abstract-only PDF variant** (paywalled landing page, no body text): keep `source_collection: external` + `pdf_path`/`pdf_filename`, add `full_text: false`, and state `abstract-only — full text not retrieved` above the Three-line Summary. See INGEST.md Step 1-A.

---

## Wiki Template

```markdown
---
title: "EXACT PAPER TITLE"
authors: First Author, Second Author, Third Author et al.
year: YYYY
date: YYYY-MM-DD
doi: 10.XXXX/xxxxx
source: {stem}.md
category: [category-folder]
evidence_level: {evidence-level-label}
pdf_path: /Users/oracleneo/llm-wiki/papers/{stem}.pdf
pdf_filename: {stem}.pdf
source_collection: external
tags: [keyword1, keyword2, keyword3]
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
{English paragraph, 3–5 sentences. State study design, population, key result, clinical implication.}

## Key Contributions
- {Contribution 1}
- {Contribution 2}

## Methodology
{Brief: design, databases, n, outcomes.}

## Results
| Outcome | Result |
|---|---|
| {metric} | {value} |

## Related Papers
- [[category/stem]] — {relationship description}
```

`date:` — publication date `YYYY-MM-DD`; `YYYY-01-01` if only the year is known; ingest date if neither is recoverable from the paper.

**Optional frontmatter — judgment calls, not mechanical fill-in, add only when they genuinely apply:**

- `superseded_by: {newer-stem}` + `superseded_scope: full|partial` — set on the **older** page when a new page overturns its clinical bottom line, plus a `[!warning]`/`[!note]` banner at the top of the body. INGEST.md § `superseded_by:`.
- `relations:` — typed edges to existing wiki stems, found via `qmd query` (never grep/find/ls). Five types: `extends` / `reinforces` / `contradicts` / `refines` / `applies-to` — **no 6th type** (a `complements` type was tested and rejected 2026-07-17). `reinforces` must be *independent* confirmation — a page can never `reinforces` its own source material (circular). `target` must already exist as a wiki stem; sibling papers in the same parallel-ingest batch can't typed-edge each other (use prose `## Related Papers` instead, a later ingest can add the edge). Full vocabulary, the circular-`reinforces` rule, and the direction-doesn't-track-publication-date caveat: INGEST.md § `relations:` — read it before typing an edge, don't guess from memory or from how strong the target looks.

---

## Index

`index.md` entries go under the section heading matching the paper's category. Read `index.md` directly and match by category — no separate lookup table here; categories/headings change often enough that a synced copy would drift the same way the category list above did.
