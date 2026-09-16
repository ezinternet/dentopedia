---
title: "Efficacy of clear functional orthodontic appliances versus traditional functional appliances in the treatment of Class II malocclusion: A systematic review and meta-analysis"
authors: "Sohn BJ, Han YK, Kim NJ, Park JB, Mo SS"
year: 2025
doi: "10.4041/kjod25.197"
category: [orthodontics/clear-aligner]
pdf_path: ""
pdf_filename: ""
source_collection: pubmed-abstract
---

## Why Ingested

Companion SR+MA to [[orthodontics/clear-aligner/huang-2026-clear-aligner-mandibular-advancement-vs-functional-class-ii-sr-ma]] comparing clear aligner mandibular advancement (Invisalign) vs traditional functional appliances (Twin Block, Herbst, van Beek) for skeletal Class II malocclusion; published in Korean Journal of Orthodontics and covers an overlapping but distinct evidence pool (n=5 non-randomized studies, post-2017 only).

## One-line Summary

SR+MA of 5 non-randomized controlled trials (n=166) found no statistically significant differences in cephalometric outcomes (SNA, SNB, ANB, overjet, incisor inclination, mandibular length) between clear aligners with mandibular advancement and traditional functional appliances for skeletal Class II malocclusion.

## 한줄요약

비무작위 대조연구 5편(n=166) 메타분석: 투명교정 하악전진(Invisalign MA) vs 전통기능장치(Twin Block·Herbst·van Beek) 간 SNA/SNB/ANB·overjet·전치경사·하악길이 모두 유의 차이 없음 — 투명교정이 Class II 치료 대안으로 고려 가능하나 고질적 이질성(I²=70–86%) 및 소규모 연구로 RCT 필요.

## 1. Document Information

- **Journal**: Korean Journal of Orthodontics
- **Volume/Issue/Pages**: 56(2): 167–180
- **Publication date**: 2025-12-22
- **PMID**: 41877683 | **PMC**: PMC13021320 | **DOI**: 10.4041/kjod25.197
- **PROSPERO**: CRD42024622755
- **Funding**: Not specified in full text
- **Conflicts of interest**: Not declared

## 2. Key Contributions

- First SR+MA restricting comparators to post-2017 studies (year Invisalign Mandibular Advancement System was launched), ensuring only modern CA-MA technology is evaluated
- Includes van Beek appliance alongside Twin Block and Herbst as traditional FA comparators — broader comparator pool than huang-2026
- Confirms equivalence across 8 cephalometric domains: SNA, SNB, ANB, Wits, mandibular plane angle (FMA/SN-MP), overjet, maxillary incisor inclination, mandibular incisor inclination, and mandibular length (Co-Po/Co-Gn)
- Subgroup-level funnel asymmetry detected (ANB) but Egger's test non-significant (p=0.39); trim-and-fill correction negligible — publication bias unlikely to drive conclusions
- Identifies treatment duration confounding (Twin Block = 2-phase with growth observation; CA = single-phase ~2 years) as major unresolved methodological gap

## 3. Methodology and Architecture

- **Design**: Systematic review + meta-analysis; PRISMA-compliant; PROSPERO-registered
- **Databases**: PubMed, Embase, Cochrane Library, Web of Science
- **Language restriction**: Korean and English
- **Eligibility (PICOS)**:
  - P: Skeletal Class II malocclusion, no trauma/surgery/periodontitis/systemic disease
  - I: Clear aligners with mandibular advancement (Invisalign, Align Technology)
  - C: Traditional functional appliances (Twin Block, Herbst, van Beek)
  - O: Cephalometric skeletal + dental changes pre- and post-treatment
  - S: Non-randomized prospective and retrospective cohort studies only (RCTs excluded)
- **Studies excluded**: RCTs, case reports, reviews, pre-2017 publications, non-comparative studies
- **Initial yield**: 1,578 articles → 5 included after de-duplication and full-text screening
- **Participants**: 166 total — 89 traditional FA, 77 CA mandibular advancement
- **Risk of bias**: ROBINS-I; 1/5 low risk, 4/5 moderate risk
- **Statistical analysis**: R 4.3.3 + RStudio; random-effects model; standardized mean difference (SMD) + 95% CI; I² and τ² for heterogeneity; Egger's test + trim-and-fill for publication bias

## 4. Key Results and Benchmarks

| Outcome | SMD (95% CI) | p-value | I² | Interpretation |
|---|---|---|---|---|
| SNA angle | 0.54 (−0.28, 1.36) | 0.1943 | 80% | NS — slight trend favoring FA |
| SNB angle | 0.29 (−0.34, 0.93) | 0.3607 | 70% | NS — slight trend favoring CA |
| ANB angle | 0.33 (−0.43, 1.09) | 0.3970 | 72% | NS |
| Overjet | 0.17 (−0.61, 0.96) | 0.6657 | 78% | NS |
| Wits appraisal | −0.03 (−0.92, 0.86) | 0.9471 | 78% | NS — effectively identical |
| Mandibular plane angle | −0.59 (−1.46, 0.29) | 0.1912 | 76% | NS — slight trend favoring CA (better vertical control) |
| Mandibular incisor inclination | 0.09 (−0.89, 1.07) | 0.8519 | 86% | NS |
| Maxillary incisor inclination | 0.56 (−0.53, 1.66) | 0.3139 | 82% | NS |
| Mandibular length (Co-Po/Co-Gn) | 0.01 (−0.36, 0.37) | 0.9715 | 21% | NS — lowest heterogeneity |

- Publication bias (ANB): funnel plot asymmetry observed; Egger's z=0.86, p=0.39 (NS); trim-and-fill adds 2 imputed studies, effect size minimally changed

## 5. Limitations and Future Work

- Small number of included studies (n=5); limits statistical power and generalizability
- All non-randomized controlled trials; residual confounding cannot be excluded despite low-to-moderate ROBINS-I rating
- High heterogeneity in most outcomes (I²=70–86%); pooled numerical trends should not be interpreted as clinically meaningful differences
- Treatment duration not standardized: Twin Block studies often 2-phase (growth observation included); CA studies typically single-phase ~2 years — mandibular growth contribution vs appliance effect unquantifiable
- Different appliance generations across studies may introduce technology confounding
- Future research priority: high-quality RCTs with standardized treatment duration definitions, larger n, and subgroup analyses by growth stage

## 6. Related Work

- Yu 2023 (DOI 10.7518/hxkq.2023.2022453): 9 controlled studies, n=283; same equivalence conclusion; found 1.94° less mandibular incisor proclination and 1.10 mm less Co-Go increase in CA group — finer dental outcomes absent from Sohn-2025
- Huang 2026 (DOI 10.1186/s12903-026-08175-z): 8 studies, n=326; overlapping pool but broader inclusion; consistent with Sohn-2025 equivalence findings

## 7. Glossary

- **CA-MA**: Clear aligner with mandibular advancement — Invisalign with the Mandibular Advancement feature (introduced 2018 for adolescents)
- **FA**: Traditional functional appliance — Twin Block, Herbst, or van Beek; use inclined occlusal planes to posture mandible forward
- **SMD**: Standardized mean difference — post-pre change in CA group minus post-pre change in FA group, divided by pooled SD; positive = FA shows greater absolute change for that parameter
- **ROBINS-I**: Risk of Bias in Non-randomized Studies of Interventions — domain-based tool for NRCTs
- **ANB angle**: Angle between points A (maxilla) and B (mandible) relative to nasion; primary measure of sagittal skeletal Class II
- **Wits appraisal**: Perpendicular projections of A and B points onto occlusal plane; supplements ANB for sagittal diagnosis
- **Co-Po / Co-Gn**: Condylion to pogonion / gnathion — linear measures of mandibular length
- **Trim-and-fill**: Non-parametric method to estimate effect of publication bias by imputing missing asymmetric studies
