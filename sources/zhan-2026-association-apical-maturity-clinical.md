---
title: "Association of Apical Maturity With Clinical and Biological Outcomes After Regenerative Endodontic Procedures: A Systematic Review and Meta-Analysis"
authors: "Zhan S, Yan Q, Zhang Y"
year: 2026
doi: "10.1016/j.identj.2026.109660"
category: [endodontics/regenerative]
pdf_path: ""
pdf_filename: ""
source_collection: pubmed-abstract
---

## Why Ingested
기존 [[endodontics/regenerative/regenerative.md]] 랜딩 페이지와 [[overviews/regenerative-endodontics-rep-overview]]가 치근첨 성숙도와 결과 간 dose-response 관계를 다루지 않음; 이 논문이 DRMA로 그 공백을 채움.

## One-line Summary
SR+MA of 10 studies (508 teeth): REP clinical success 90%, tooth survival 98%, but apical closure only 53% and pulp vitality recovery only 21% — high success does not equal true regeneration.

## 한줄요약
SR+MA (10편, 508치아): REP 임상성공 90%·생존 98%이지만 치근첨 폐쇄 53%·치수활력 회복 21%에 그침 — 임상성공 ≠ 진성 재생.

## 1. Document Information
- **Journal**: International Dental Journal, Vol. 76(4), 2026
- **PMC**: PMC13279176
- **Publication date**: 2026-06-13
- **Funding**: None declared
- **Conflicts of interest**: None declared

## 2. Key Contributions
- REP clinical success (90%) and tooth survival (98%) are high and stable across varying apical diameters — supports REP as a broad-indication therapy
- Apical closure (53%) and pulp vitality recovery (21%) are much lower and highly variable — underscores that REPs rarely achieve true pulp-dentin regeneration
- Dose-response meta-analysis (DRMA): larger apical diameter → lower apical closure rate (approximately 70% → 30% across the diameter range); clinical success stable across diameters
- Trial sequential analysis confirms evidence for clinical success and survival is statistically robust; apical closure and vitality remain underpowered
- Vitality assessment methods (cold test, EPT, laser Doppler) vary substantially — calls for standardization

## 3. Methodology and Architecture
- **Design**: Systematic review + traditional meta-analysis + dose-response meta-analysis (DRMA) + trial sequential analysis (TSA)
- **Databases**: PubMed, Embase, Web of Science, Scopus, Cochrane CENTRAL (up to July 2025)
- **Inclusion**: RCTs, prospective/retrospective cohorts, case series ≥5 teeth; permanent teeth with necrotic pulps; REP of any type
- **Exclusion**: Animal/in vitro, reviews, case reports, <5 teeth, protocols/abstracts only
- **Studies included**: 10 (4 RCTs, 6 observational); 508 teeth
- **Outcomes**: Clinical success (primary), tooth survival, complete apical closure, pulp vitality recovery
- **Statistical methods**: Random-effects (DerSimonian-Laird), DRMAvia 2-stage GLS regression + restricted cubic splines (3 knots), TSA via RTSA package (R 4.3.0)
- **Quality assessment**: RoB 2.0 (RCTs), Newcastle-Ottawa Scale (observational); registration INPLASY202640005

## 4. Key Results and Benchmarks
| Outcome | Pooled rate | 95% CI | I² |
|---|---|---|---|
| Clinical success | 90% | 83–95% | 40.3% |
| Tooth survival | 98% | 95–99% | 0% |
| Complete apical closure | 53% | 36–70% | 79.6% |
| Pulp vitality recovery | 21% | 7–49% | 69.2% |

- DRMA: apical closure shows ~negative slope (wider apex → less closure); clinical success stable at >80% across all diameters
- Subgroup by material (exploratory): Blood clot ~90% success regardless of diameter; FGF showed steeper decrease
- Publication bias: clinical success and survival funnel plots symmetric; apical closure and vitality showed asymmetry

## 5. Limitations and Future Work
- Only 10 studies included; only 2 involving mature teeth
- Short-to-medium follow-up (mostly ≤36 months) — may underestimate long-term vitality recovery
- Apical diameter measurement heterogeneous across studies (radiographic, Cvek staging, clinical estimation) — source of DRMA bias
- Vitality outcome definition varies (cold, EPT, laser Doppler)
- Future needs: standardized apical diameter reporting, standardized vitality assessment, ≥60-month follow-up, material-specific RCTs

## 6. Related Work
- Kim et al. and Tewari et al.: prior REP SRs reporting success ~85-96%, survival >95% (consistent with this paper)
- Asgary 2024 umbrella SR: MTA apexification vs REP, consistent with REP advantage for root maturation

## 7. Glossary
- **REP (Regenerative Endodontic Procedures)**: protocols using blood clot, PRF, MTA barrier to regenerate pulp-like tissue in necrotic teeth
- **SCAP (Stem Cells from the Apical Papilla)**: key regenerative cell source; concentrated at narrow apices
- **DRMA (Dose-Response Meta-Analysis)**: quantifies continuous exposure-outcome relationships via spline regression
- **TSA (Trial Sequential Analysis)**: determines whether cumulative evidence has reached required information size (RIS)
