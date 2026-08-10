---
title: "Reasons for Crown Failures in Primary Teeth: Systematic Review and Meta-Analysis"
authors: Lampl S, Gurunathan D, Mehta D, Jogikalmat K
year: 2025
doi: 10.2196/57958
category: [prosthetic-materials]
source_collection: pubmed-text
full_text: true
pmid: "40311116"
pmcid: "PMC12061352"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12061352/
text_path: /Users/oracleneo/llm-wiki/papers/lampl-2025-crown-failures-primary-teeth-sr-ma.txt
text_filename: lampl-2025-crown-failures-primary-teeth-sr-ma.txt
---

## Why Ingested

사용자가 유치(primary teeth) 스테인리스강관(SSC) 보철에 대한 PMC 전문 논문 추가를 요청. 본 SR+MA(13 RCT + 5 clinical study, 1172+2667개 크라운)는 SSC를 포함한 5개 재료(compomer, composite resin, RMGIC, SSC, zirconia, strip crown)의 5년 유지율과 실패 원인을 정량화한 최신(2025) 근거로, 기존 prosthetic-materials 카테고리에 소아 유치관 관련 페이지가 없어 신규 하위 주제를 개설한다. [[wiki/prosthetic-materials/tomar-2025-cement-vs-screw-zirconia-crown-sr-ma]]와 함께 향후 소아 지르코니아관(pediatric zirconia crown) 관련 근거 축적의 출발점이 된다.

## Three-line Summary

Systematic review and meta-analysis (13 RCTs, n=454 children/1172 crowns;

5 clinical studies, n=810 children/2667 crowns) found pooled 5-year retention rates of 97.88% for stainless steel crowns (SSC), 97.09% for zirconia, 92.18% for composite resin, 90.30% for RMGIC, 88.90% for compomer, and 83.48% for strip crowns, with SSC showing zero decementation/chipping/fracture events among RCT retention complications while zirconia had the highest gingival inflammation (21.8% in clinical studies) and composite resin had the highest technical/esthetic complication burden.

(incomplete)

## 세줄요약

13개 RCT(454명 아동, 크라운 1172개)와 5개 임상연구(810명, 크라운 2667개)를 포함한 체계적 문헌고찰 및 메타분석 결과, 5년 유지율은 스테인리스강관(SSC) 97.88%, 지르코니아 97.09%, 복합레진 92.18%, RMGIC 90.30%, 컴포머 88.90%, 스트립관 83.48%였으며, SSC는 RCT에서 탈락·칩핑·파절 등 유지 관련 합병증이 전무했던 반면 지르코니아는 치은염증(임상연구 21.8%)이 가장 높고 복합레진은 기술적·심미적 합병증 부담이 가장 컸다.

(incomplete)

(incomplete)

## 1. Document Information

- **Title**: Reasons for Crown Failures in Primary Teeth: Systematic Review and Meta-Analysis
- **Authors**: Lampl S, Gurunathan D, Mehta D, Jogikalmat K
- **Journal**: Interactive Journal of Medical Research (Interact J Med Res)
- **Publication date**: 2025-05-01
- **DOI**: 10.2196/57958
- **PMID**: 40311116
- **PMCID**: PMC12061352
- **Protocol registration**: PROSPERO CRD42023442266, per MOOSE and PRISMA-P guidelines
- **Study type**: Systematic review + meta-analysis (SR+MA) of RCTs and prospective/retrospective clinical studies

## 2. Key Contributions

- Provides an updated (2025) pooled quantitative estimate of 3-year and 5-year crown-retention rates across five common pediatric primary-tooth crown materials — compomer, composite resin, RMGIC, stainless steel, and zirconia — plus strip crowns, using Poisson regression on exposure-time data.
- Separates **retentive** complications (chipping, fracture, decementation, partial/complete material loss) from **biological** (secondary caries, gingival inflammation, plaque index, bleeding on probing) and **technical** (marginal adaptation, marginal discoloration, marginal integrity, staining, plaque retention, shade mismatch, opposing-tooth wear, surface roughness, occlusal wear) complications, offering a material-specific complication profile rather than a single failure number.
- Confirms and extends Chisini et al's earlier (2018) finding that stainless steel crowns have the highest success/retention rate, using a larger and more recent RCT/clinical-study pool (RCTs published 2014–2022; clinical studies 2008–2020).
- Applies Risk of Bias 2 (Cochrane) for RCTs and a Moga et al-adapted checklist for clinical studies, plus funnel-plot/Egger-test publication-bias assessment (significant asymmetry detected for zirconia).

## 3. Methodology and Architecture

- **Design**: PICOS-based systematic search of Cochrane, Embase, and PubMed/MEDLINE (search conducted July–August 2023).
- **Population**: children aged 1–10 years with primary-tooth decay requiring crown restoration.
- **Intervention/Comparators**: crowns fabricated from stainless steel, zirconia, composite resin, compomer, and RMGIC (plus strip crowns as encountered in included studies).
- **Inclusion**: RCTs and prospective/retrospective clinical studies with English abstracts reporting crown retention, reasons for retentive loss, and biological/technical complications. Excluded: qualitative interviews, quasi-experimental studies, single-case/case-series studies, conference abstracts, dissertations.
- **Screening**: two independent reviewers (SL, KJ) for title/abstract and full-text stages; disagreements resolved by discussion, third reviewer (DG) as tiebreaker for selection, quality assessment, and data extraction.
- **Risk of bias**: Cochrane Risk of Bias 2 tool for RCTs (domains: random sequence, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, selective reporting, other bias); Moga et al-adapted checklist for clinical studies (7 domains). Only moderate/low risk-of-bias studies were retained.
- **Meta-analytic approach**: retention defined as crowns remaining in situ regardless of complications. Failure rate = failures / total exposure time (cumulative crown-days in mouth, summed across studies). Pearson goodness-of-fit test assessed heterogeneity; since no statistically significant heterogeneity was found in any group/rate (p>.05), a **fixed-effects Poisson regression model** was used to estimate 3-year and 5-year retention rates (assuming constant event rates). Analyses performed in R (v4.1.2).
- **Included studies**: 13 RCTs (454 children, 1172 crowns, follow-up range 6–36 months, median 12 months, IQR 9; cumulative dropout 10.6%, 124/1172) and 5 clinical studies (810 children, 2667 crowns, follow-up range 12–24 months, median 20.8 months, IQR 5).

## 4. Key Results and Benchmarks

**Pooled 5-year retention rates (Poisson regression, meta-analysis of RCTs):**

| Material | 5-year retention |
|---|---|
| Stainless steel crown (SSC) | 97.88% |
| Zirconia | 97.09% |
| Composite resin | 92.18% |
| RMGIC | 90.30% |
| Compomer | 88.90% |
| Strip crowns | 83.48% |
| Overall (unstratified) | 92.20% (95% CI 92.14%–92.26%) |

**Descriptive retention-rate ranges from individual RCTs**: compomer 77.8%–100%; composite resin 80.6%–100%; stainless steel 92.3%–100%; strip crowns 78%–100%; zirconia 86.4%–100%.

**RCT retentive complications by material (counts, Table 5)**: Compomer — 0 decementation/chipping/complete or partial loss, 8 crown fractures. Composite resin — 12 chipping, 3 fractures, 3 poor anatomic form, 1 complete loss, 2 partial material loss. **Stainless steel — zero of every retentive complication type recorded** (decementation, chipping, fracture, poor anatomic form, complete/partial loss all = 0). Strip crowns — 3 chipping, 7 complete loss, 19 partial material loss (highest burden). Zirconia — 5 decementation, 1 complete loss, 1 partial material loss.

**Biological complications (RCTs, Table 6)**: secondary caries highest in strip crowns (6.18%) and compomer (5.97%), lowest in zirconia (0%). Gingival inflammation highest in composite resin (24.24%), lowest in compomer (0%); zirconia 3.5%. In the separate prospective/retrospective clinical studies, secondary caries was 8.3% (6/67) for compomer and 8.8% (11/121) for composite resin, while gingival inflammation was 21.8% (80/368) for zirconia and 3.3% (10/289) for stainless steel — the paper explicitly flags this 21.8% zirconia figure as notable in the abstract.

**Technical complications (RCTs, Table 7)**: compomer showed 29% marginal adaptation issues (19/67) with none of the other technical-complication categories; stainless steel had essentially no technical complications except opposing-tooth wear (13.6%, 33/242) and staining (2.9%); composite resin had the broadest complication spread including 29.2% shade mismatch (45/154) and 15.6% staining; zirconia had low rates across categories except opposing-tooth wear (8.5%) and shade mismatch (4.8%).

**Publication bias**: Egger test for zirconia crowns was significant (p<.001), suggesting potential publication bias; too few studies existed for stainless steel, composite resin, and strip crowns to robustly assess small-study effects.

**Risk of bias**: RCTs showed notable prevalence of allocation-concealment, performance, and detection bias (inherent to interventions that preclude full double-blinding). Clinical studies were mostly low/moderate risk of bias; one study (Holsinger et al) had serious risk of bias in the competing-interests domain.

## 5. Limitations and Future Work

- Age distribution of study populations was often unreported, limiting analysis of retention-rate variation across the primary-to-permanent transition age range (RCTs: ages 1–10; clinical studies: ages 3–10).
- Wide variability in sample sizes across included studies; Poisson regression was used to adjust for this but does not fully resolve generalizability concerns.
- Fixed-effects model was justified by non-significant heterogeneity tests, but with small per-material study counts (as few as 2–3 RCTs for some materials), the power to detect heterogeneity or publication bias is limited — the authors explicitly urge caution interpreting the zirconia funnel-plot asymmetry.
- RCTs are inherently limited by inability to fully blind participants/personnel/outcome assessors for a physical crown-placement intervention, so allocation-concealment/performance/detection bias risk cannot be design-eliminated.
- Authors recommend larger sample sizes, longer follow-up, and exploration of new fabrication techniques (3D printing, CAD/CAM) to improve fit and longevity in future studies.

## 6. Related Work

- Chisini et al. (2018, cited within) — earlier systematic review reporting composite resin lowest annual failure rate (1.7–12.9%) and stainless steel highest success rate (96.1%); this paper is presented as an update incorporating RCTs published since then (2021–2023 material-specific SRs already existed for SSC, zirconia, prefabricated crowns individually).
- Alzanbaqi et al. (cited within) — reported improved gingival/periodontal health, excellent retention, and high fracture resistance for zirconia crowns in primary teeth, corroborated by this review's zirconia retention data (though contrasted by this review's higher gingival-inflammation finding in clinical-study data).

## 7. Glossary

- **SSC (Stainless Steel Crown)**: Prefabricated metal crown widely used for restoring severely broken-down primary molars/incisors; the material benchmark in this review (97.88% 5-year retention).
- **RMGIC (Resin-Modified Glass Ionomer Cement)**: Hybrid glass-ionomer/resin material used both as crown material (in this review) and luting cement.
- **Compomer**: Polyacid-modified resin composite combining resin-composite and glass-ionomer properties.
- **Strip crown**: Clear polycarbonate/cellulose acetate crown form filled with composite resin, primarily for anterior primary teeth.
- **Poisson regression (fixed-effects)**: Statistical model used here to estimate constant failure rates per crown-year from cumulative exposure time, projecting 3-year/5-year retention.
- **Total exposure time**: Cumulative duration (crown-days) that all crowns in a study remained in place, used as the denominator for failure-rate calculation.
- **RoB 2 (Risk of Bias 2)**: Cochrane Collaboration tool for assessing bias domains in RCTs.
- **PICOS**: Population, Intervention, Comparison, Outcomes, Study design — framework used to structure the systematic search.
- **Egger test**: Statistical test for funnel-plot asymmetry, used here to assess publication bias (significant for zirconia).
