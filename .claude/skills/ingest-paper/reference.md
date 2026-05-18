# Ingest Paper — Reference

## Confidence Vocabulary

Pick the **single best label**:

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

---

## Category List

| Folder | Korean | Classify when… |
|---|---|---|
| `implants` | 임플란트 | Implant design, bone type, survival, failure risk, MBL, soft tissue |
| `implants/isq` | 임플란트·ISQ | ISQ/RFA measurement, stability dip, loading thresholds |
| `implants/surface` | 임플란트·표면처리 | SLA, CA, UV surface tech, osseointegration |
| `bone-regeneration` | 골재생 | GBR, ridge preservation, socket management, peri-implantitis GBR |
| `immediate-implant` | 즉시식립 | Immediate implant placement protocols, outcomes, esthetic risk |
| `sinus-lift/lateral` | 상악동거상술·측방 | Lateral window approach |
| `sinus-lift/transcrestal` | 상악동거상술·경치조골 | Transcrestal (osteotome/balloon/OD) approaches |
| `endodontics/eal` | 근관치료·근관장측정 | EAL accuracy, working length, apex locator |
| `endodontics/irrigation` | 근관치료·세정 | Irrigant activation (PUI, ANP, sonic, laser) |
| `endodontics/anatomy` | 근관치료·해부 | Canal morphology, access cavity, MB2, CBCT-guided access |
| `periodontics` | 치주치료 | Periodontal disease, regeneration, SPT |
| `dental-materials` | 치과재료 | Impression materials, zirconia, ceramics (general) |
| `digital-workflow` | 디지털워크플로우 | IOS accuracy, CBCT, CAD/CAM, guided surgery |
| `resin` | 레진 | Composite resin, polymerization, shrinkage |
| `resin-bonding` | 레진접착 | Adhesive systems, bonding, dentin adhesion |
| `prosthetic-materials` | 보철재료 | Screw vs cement retention, zirconia crowns, CAD/CAM prosthetics |
| `drug` | 전신질환·약물 | Systemic disease, drug interactions, MRONJ, anticoagulants |
| `oral-surgery` | 구강외과 | Extractions, nerve injuries, surgical complications, coronectomy |
| `inlay` | 인레이 | Inlay/onlay restorations, ceramic inlays |

**Classify by method/procedure, not by disease or anatomy.**

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

## One-line Summary
{Study type, n, key finding in one English sentence.}

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
confidence: {confidence-label}
pdf_path: /Users/oracleneo/llm-wiki/papers/{stem}.pdf
pdf_filename: {stem}.pdf
source_collection: external
tags: [keyword1, keyword2, keyword3]
---

## 한줄요약
{Korean one-liner: study type, n, key finding. Use 한국어 (English, 약어) notation.}

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

---

## Index Section Headers

Match category to the correct `##` section heading in `index.md`:

| Category | Index Section Header |
|---|---|
| `implants` | `## 임플란트 — 디자인·생존율·실패위험` |
| `implants/isq` | `## 임플란트 — ISQ·안정성 (Implants: ISQ / Stability)` |
| `implants/surface` | `## 임플란트 — 표면처리·골유착 심화` |
| `bone-regeneration` | `## 골재생 (Bone Regeneration)` |
| `immediate-implant` | `## 즉시식립 (Immediate Implant)` |
| `sinus-lift/lateral` | `## 상악동거상술 — 측방창 접근 (Sinus Lift: Lateral)` |
| `sinus-lift/transcrestal` | `## 상악동거상술 — 경치조골 접근 (Sinus Lift: Transcrestal)` |
| `endodontics/eal` | `## 근관치료 — 근관장 측정 (Endodontics: EAL / Working Length)` |
| `endodontics/irrigation` | `## 근관치료 — 세정·활성화 (Endodontics: Irrigation)` |
| `endodontics/anatomy` | `## 근관치료 — 해부·접근·진단 (Endodontics: Anatomy / Access / Detection)` |
| `periodontics` | `## 치주치료 (Periodontics)` |
| `dental-materials` | `## 치과재료 (Dental Materials)` |
| `digital-workflow` | `## 디지털 워크플로우 (Digital Workflow)` |
| `resin` | `## 레진 (Resin)` |
| `resin-bonding` | `## 레진접착 (Resin Bonding)` |
| `prosthetic-materials` | `## 보철재료 (Prosthetic Materials)` |
| `drug` | `## 전신질환·약물 (Drug / Systemic Medicine)` |
| `oral-surgery` | `## 구강외과 (Oral Surgery)` |
| `inlay` | `## 인레이 (Inlay)` |
