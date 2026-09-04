---
title: "Are arch width measurements from Invisalign arch width tables reliable?"
authors: Cristina de-la-Rosa-Gay, Sofia Valmaseda-de-la-Rosa, Andrea Hernández-Mangas, Octavi Camps-Font, Eduard Valmaseda-Castellón, Rui Figueiredo
year: 2026
doi: 10.1007/s00784-026-06904-w
category: [orthodontics/clear-aligner]
source_collection: pubmed-text
full_text: true
pmid: "42126458"
pmcid: "PMC13171758"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13171758/
text_path: /Users/oracleneo/llm-wiki/papers/de-la-rosa-gay-2026-arch-width-measurements-invisalign-tables.txt
text_filename: de-la-rosa-gay-2026-arch-width-measurements-invisalign-tables.txt
---

## Why Ingested

Same-author companion to [[orthodontics/clear-aligner/de-la-rosa-gay-2025-expansion-predictability-clear-aligner]], which quantified clinical arch-expansion predictability (0.92 mm mean absolute planned-vs-achieved discrepancy) using arch-width values read off the ClinCheck arch-width table. That paper never asked whether the table's own numbers can be trusted — this paper closes exactly that gap, metrology-validating ClinCheck arch-width output against independent Geomagic Control X measurements. It is a measurement-validation study, not an efficacy study: it says the numbers in the table are trustworthy (best at occlusal/cusp references), not that the aligner achieves the planned expansion.

## Three-line Summary

Retrospective method-agreement study (35 adults treated with Invisalign SmartTrack, single orthodontist, Barcelona metropolitan area, Nov 2017–Sep 2025; 126 screened, 35 analyzed) — digital models measured with Geomagic Control X at canines, first/second premolars, and first molars across three ClinCheck timepoints (pretreatment, predicted, pre-first-refinement), yielding 840 paired arch-width measurements.

Mixed-effects Bland–Altman analysis (patient random intercepts, accounting for within-patient clustering, ICC 0.37–0.46) showed narrow bias across reference points: occlusal 0.03 mm (95% LoA −0.78 to +0.84 mm, total variance), cusp +0.21 mm (~−1.0 to +1.5 mm), gingival −0.30 to −0.48 mm (up to ±1.8 mm); the discrepancy variable (observed minus predicted expansion) showed the most stable results with bias closest to zero across all three reference-point sets.

Clinical implication: ClinCheck arch-width table values are metrologically consistent with independent measurement — most reliably at occlusal and cusp references, least at gingival — but this validates the measurement tool, not the aligner's ability to achieve the clinically planned expansion.

## 세줄요약

후향적 측정법-일치도(Method-Agreement) 연구(Invisalign SmartTrack 치료 성인 35명, 단일 교정의, 바르셀로나, 2017.11–2025.9; 126명 선별 중 35명 분석) — 치료 전·ClinCheck 예측·첫 리파인먼트 전 3개 시점의 디지털 모델을 Geomagic Control X로 견치·제1/2소구치·제1대구치에서 측정, 치아궁 폭(Arch Width) 쌍 840개 확보.

혼합효과 일치도 분석(Mixed-Effects Bland-Altman Analysis, 환자별 무작위 절편으로 환자 내 군집 보정, 급내상관계수(Intraclass Correlation Coefficient, ICC) 0.37–0.46)에서 기준점별 편향(bias)이 좁게 나타남: 교합면(Occlusal) 기준 0.03 mm(95% 일치한계(Limits of Agreement, LoA) −0.78~+0.84 mm), 교두(Cusp) 기준 +0.21 mm(약 −1.0~+1.5 mm), 치은(Gingival) 기준 −0.30~−0.48 mm(±1.8 mm까지); 실제확장-예측확장 불일치(Discrepancy) 변수가 세 기준점 모두에서 편향 0에 가장 근접하고 가장 안정적.

임상적 의미: ClinCheck 치아궁 폭 표 수치는 독립 계측과 대체로 일치하며(교합면·교두 기준이 가장 신뢰도 높고 치은 기준이 가장 낮음) — 다만 이는 "측정도구"의 신뢰성 검증이지, 얼라이너가 계획한 확장을 실제로 "달성"한다는 증거는 아니다.

## 1. Document Information

- **Journal**: Clin Oral Investig 2026;30(6)
- **DOI**: 10.1007/s00784-026-06904-w
- **Institution**: Universitat de Barcelona / IDIBELL, Barcelona, Spain

## 2. Key Contributions

- First independent metrology validation of ClinCheck **transverse (arch-width)** table values — prior validation work covered only overjet/overbite.
- Compared three anatomical reference levels (occlusal, cusp, gingival) and ranked their reliability: occlusal ≈ cusp (tight agreement) >> gingival (widest limits of agreement).
- Used mixed-effects Bland–Altman modeling with patient-level random intercepts to properly account for 24 non-independent repeated measurements per patient (ICC 0.37–0.46; design effect 9.6–11.7).
- Validated across two separate ClinCheck records (pretreatment→predicted, and pretreatment→pre-refinement/observed), broader in scope than a prior single-timepoint overjet/overbite validation study.

## 3. Methodology and Architecture

- **Design**: retrospective cohort / method-agreement (metrology validation) study; STROBE-reported; single orthodontist, single private clinic.
- **n**: 126 screened, 91 excluded, 35 analyzed; 840 paired arch-width measurements (35 patients × 8 tooth-pair widths [4 maxillary + 4 mandibular] × 3 timepoints = 24 repeated measurements/patient).
- **Outcomes**: predicted expansion, observed expansion, and discrepancy (observed minus predicted), each assessed at occlusal, cusp, and gingival reference points.
- **Statistics**: Shapiro–Wilk normality testing → non-parametric Bland–Altman (median bias, 2.5th/97.5th percentile LoA, bootstrap 95% CI, 2000 iterations) plus mixed-effects Bland–Altman models with patient random intercepts; test–retest reliability check in 10 randomly selected cases after ≥15 days (ICC 0.989–0.997).

## 4. Key Results and Benchmarks

- Occlusal reference: mixed-effects bias 0.03 mm; 95% LoA −0.78 to +0.84 mm (total variance), −0.74 to +0.81 mm (within-patient variance).
- Cusp reference: bias +0.21 mm (predicted and observed expansion); LoA approximately −1.0 to +1.5 mm.
- Gingival reference: bias −0.30 mm (predicted expansion), −0.48 mm (observed expansion), −0.18 mm (discrepancy); LoA up to ±1.8 mm.
- Non-parametric Bland–Altman (individual-measurement level): occlusal and cusp LoA within approximately ±1 mm; gingival LoA up to ±1.8 mm; discrepancy showed the narrowest ranges and bias closest to zero across all three reference-point sets.

## 5. Limitations and Future Work

- Single operator retrieved all data; retrospective, non-independent repeated measurements (addressed statistically via mixed-effects models, but residual correlation may remain).
- ClinCheck's proprietary reference-point/rotation-center algorithm is undisclosed and unverifiable — comparisons were necessarily indirect (via derived expansion/discrepancy variables, not raw widths).
- Generalizable only to adults treated with SmartTrack by a single clinician; multi-operator, longitudinal-clinical-outcome studies needed.
- Gingival margin in ClinCheck STL files is digitally processed, limiting reference-plane accuracy at that landmark specifically.
- Authors explicitly caution: agreement with Geomagic is not proof of absolute measurement accuracy, nor of the aligner's clinical predictive/efficacy performance.

## 6. Related Work

- de-la-rosa-gay-2025 (expansion predictability, clear aligner): prior paper from the same group quantifying planned-vs-achieved arch expansion using ClinCheck-table-derived values; this paper validates the measurement instrument that study's outcome depended on.
- Prior ClinCheck overjet/overbite validation study (cited in-text, not yet in this wiki): established no significant fixed bias for sagittal/vertical ClinCheck measurements; this paper extends that validation approach to the transverse dimension.

## 7. Glossary

- **ClinCheck**: Align Technology's proprietary digital treatment-planning software for Invisalign, which outputs predicted tooth positions and arch-width tables.
- **Bland–Altman analysis**: statistical method for assessing agreement between two measurement methods via bias (mean/median difference) and limits of agreement.
- **Limits of Agreement (LoA)**: the range within which most differences between two measurement methods are expected to fall (typically 95%).
- **Discrepancy (this study)**: observed expansion minus predicted expansion — isolates clinical execution error from baseline measurement variability.
