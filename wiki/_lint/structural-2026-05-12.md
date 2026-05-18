# Wiki Structural Lint Report
**Date**: 2026-05-12  
**Scope**: `wiki/` — 40 pages across 11 category folders  
**Checks**: orphan pages · broken wikilinks · missing frontmatter · confidence-tag coverage

---

## Summary

| Check | Status | Count |
|---|---|---|
| Orphan pages | ✅ None | 0 |
| Broken wikilinks | ⚠️ Issues found | 12 occurrences in 7 files |
| Missing `source` field | ⚠️ Partial | 10 pages |
| Missing `date` field | ❌ Systemic | 40 / 40 pages |
| Missing `confidence` field | ❌ Systemic | 40 / 40 pages |
| Confidence-tagged sentences | ❌ Not adopted | 40 / 40 pages |

---

## 1. Orphan Pages

**Result: None.** All 40 pages are referenced from at least one of: `index.md`, another wiki page's `## Related Papers` section.

---

## 2. Broken Wikilinks

12 broken references found across 7 sources. Two root causes dominate.

### Root Cause A: Folder name inconsistency (`_` vs `-`)

Two category folders were created with underscores (`immediate_implant/`, `prosthetic_materials/`) but most cross-page links use hyphens (`immediate-implant/`, `prosthetic-materials/`). Six broken links stem from this mismatch.

| Source page | Broken link | Correct path |
|---|---|---|
| `immediate-implant/thoma-2026-timing-dental-implant-placement-past` | `[[immediate-implant/kim-2016-immediately-placed-implant-without-primary]]` | `immediate_implant/kim-2016-...` |
| `immediate-implant/thoma-2026-timing-dental-implant-placement-past` | `[[immediate-implant/lee-2021-immediate-implant-placement-in-fresh]]` | `immediate_implant/lee-2021-...` |
| `implants/di-stefano-2021-stability-dental-implants-cortical-bone` | `[[immediate-implant/kim-2016-immediately-placed-implant-without-primary]]` | `immediate_implant/kim-2016-...` |
| `implants/saenz-ravello-2023-short-implants-compared-to-regular` | `[[immediate-implant/kim-2016-immediately-placed-implant-without-primary]]` | `immediate_implant/kim-2016-...` |
| `implants/yu-2021-extra-short-implants-alternative-longer` | `[[immediate-implant/kim-2016-immediately-placed-implant-without-primary]]` | `immediate_implant/kim-2016-...` |
| `implants/mortazavi-2021-bone-loss-tissue-bone-level-implants` | `[[prosthetic-materials/kim-2019-astra-implant-dissection-solutions]]` | `prosthetic_materials/kim-2019-...` |

**Fix**: Rename `wiki/immediate_implant/` → `wiki/immediate-implant/` and `wiki/prosthetic_materials/` → `wiki/prosthetic-materials/` (or update all links to match the existing underscore names). **Renaming the folders is preferred** — hyphens are the CLAUDE.md convention and used by the majority of links.

---

### Root Cause B: Wrong or non-existent stem

| Source page | Broken link | Note |
|---|---|---|
| `implants/rosa-2024-do-dental-implants-bone-types` | `[[implants/sennerby-2008-resonance-frequency-analysis]]` | Stem is `sennerby-2008-implant-stability-resonance-frequency-analysis` |
| `implants/rosa-2024-do-dental-implants-bone-types` | `[[sinus-lift/]]` | Category-level link (no stem) — invalid |
| `implants/rosa-2024-do-dental-implants-bone-types` | `[[immediate-implant/]]` | Category-level link (no stem) — invalid |
| `endodontics/ahn-2016-survey-working-length-determination` | `[[endodontics/comparative-study-wirelesse-rootzx]]` | Target page does not exist |
| `endodontics/ahn-2016-survey-working-length-determination` | `[[endodontics/resonance-frequency-analysis]]` | Target page does not exist |

**Fix for rosa-2024**: Update the three broken links to correct stems or remove category-level placeholders.  
**Fix for ahn-2016**: The two endodontics links are forward-references to papers not yet ingested. Leave as-is or annotate with `<!-- not yet ingested -->`.

---

### Bonus: `index.md` template artifact

`index.md` contains the format example `[[category/stem]]` in its header section. Not a real page — harmless, but can be removed to keep lint clean.

---

## 3. Frontmatter Missing Fields

### 3a. `source` field missing — 10 pages

These are early-ingested pages whose frontmatter predates the `source:` convention. The field should point to `{stem}.md` in `sources/`.

| Page |
|---|
| `endodontics/jo-2017-fundamentals-and-clinical-applications` |
| `endodontics/song-2008-cross-sectional-morphology-and-minimum-canal` |
| `immediate_implant/kim-2016-immediately-placed-implant-without-primary` |
| `immediate_implant/lee-2021-immediate-implant-placement-in-fresh` |
| `implants/attik-2022-comparison-of-biological-behavior-and` |
| `implants/oh-2008-comparison-of-initial-implant-stability` |
| `periodontics/jo-2008-management-of-dental-biofilm-through` |
| `periodontics/unknown-2009-non-surgical-and-surgical-periodontal` |
| `prosthetic_materials/kim-2019-astra-implant-dissection-solutions` |
| `resin_bonding/unknown-2009-effect-of-silane-treatment-timing` |

### 3b. `date` field missing — 40 / 40 pages

**Systemic gap.** The `date` field (ingestion date or paper date) is not part of the current `CLAUDE.md` frontmatter spec. All pages lack it.

**Recommendation**: Decide whether `date` means paper publication year (already captured as `year:`) or ingestion date. If the former, the field is redundant with `year:`. If ingestion date is desired, add it to the ingest script and backfill from `git log`.

### 3c. `confidence` field missing — 40 / 40 pages

**Systemic gap.** No confidence field exists in any page. This field is not defined in `CLAUDE.md`.

**Recommendation**: Define the vocabulary (`high` / `moderate` / `low` / `sr+ma` / `rct` / `observational` / `case-report`) and add it to the CLAUDE.md spec before backfilling. Suggested mapping from existing paper types:
- SR+MA → `high`
- RCT → `high`
- Prospective cohort → `moderate`
- Retrospective / Cross-sectional → `low`
- Case report → `case-report`

---

## 4. Confidence-Tagged Sentences

**Result: Not adopted (0 / 40 pages have sentence-level confidence tags).**

No page currently uses inline confidence tags like `[High]`, `[Moderate]`, or `[SR+MA]` at the sentence level. This convention is not described in `CLAUDE.md` and has not been applied.

**Recommendation**: Adopt only if needed for downstream RAG filtering. If adopted, apply to the `## Summary` and `## Results` sections only — tagging every sentence across 40 pages is a large backfill. Suggest adding to `CLAUDE.md` spec first.

---

## Action Plan (Priority Order)

| Priority | Action | Effort |
|---|---|---|
| 🔴 High | Rename `immediate_implant/` → `immediate-implant/` and `prosthetic_materials/` → `prosthetic-materials/` | Low (mv + update index.md) |
| 🔴 High | Fix 5 wrong-stem/placeholder links in `rosa-2024` and `ahn-2016` | Low |
| 🟡 Medium | Add `source:` field to 10 early-ingested pages | Medium |
| 🟡 Medium | Define `confidence` vocabulary in CLAUDE.md | Low |
| 🟢 Low | Add `date` field to CLAUDE.md spec and ingest script | Low |
| 🟢 Low | Remove template artifact `[[category/stem]]` from index.md header | Trivial |
| ⚪ Defer | Sentence-level confidence tagging across all pages | High effort |

---

*Generated by wiki structural lint — `/Users/oracleneo/llm-wiki/wiki/_lint/structural-2026-05-12.md`*
