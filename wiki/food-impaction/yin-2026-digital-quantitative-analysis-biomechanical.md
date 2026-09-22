---
title: "Digital quantitative analysis of biomechanical factors of proximal contact loss of first molar implant crown"
authors: Derong Yin, Lingrui Gao, Hongwei Gao, Lijun Xue, Zhongda Wang, Meie Jia, Feng Wu
year: 2026
date: 2026-06-15
doi: 10.1186/s12903-026-08773-x
source: yin-2026-digital-quantitative-analysis-biomechanical.md
category: food-impaction
evidence_level: prospective
pdf_path: /Users/oracleneo/llm-wiki/papers/yin-2026-digital-quantitative-analysis-biomechanical.pdf
pdf_filename: yin-2026-digital-quantitative-analysis-biomechanical.pdf
source_collection: external
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13527992/
relations:
  - type: extends
    target: liu-2025-risk-factors-proximal-contact-loss-implant-prosthetic
  - type: reinforces
    target: liu-2025-open-contacts-posterior-implants-preventive-concepts
  - type: extends
    target: cui-2025-prevalence-risk-factors-interproximal-contact-loss
tags: [proximal-contact-loss, first-molar-implant, anterior-component-of-force, digital-model-analysis, intraoral-scanning, occlusal-adjustment, restricted-cubic-spline, food-impaction]
---

## Three-line Summary
Prospective observational cohort: 78 patients (mean 41.39 ± 13.36 y), 90 first-molar implant zirconia crowns (Straumann, all cases), intraoral 3D scanning + digital model analysis of occlusal-load-induced changes, 6-month follow-up.
6-month PCL incidence was 17.78% (16/90); ΔdP (proximal contact area gap change pre/post occlusion) was the core predictor (OR 1.05/μm, P < 0.001); RCS showed stable contacts at ΔdP ∈ [−13, 9] μm and PCL beyond ~30 μm (model κ = 0.59, P = 0.003).
First digital-quantitative thresholds linking ACF/PCF imbalance to PCL — but 6-month follow-up, female overrepresentation, and ~5 μm scanning error overlapping the stability window are key limits.

## 세줄요약
전향적 관찰 코호트(78명, 제1대구치 임플란트 지르코니아 크라운 90개, 6개월 추적)에서 구강 내 3D 스캔+디지털 모델 중첩으로 교합부하 유발 변화를 정량화.
6개월 근접접촉 소실(Proximal Contact Loss, PCL) 발생률 17.78%(16/90), 교합 전후 접촉 간극 변화(ΔdP)가 핵심 예측인자(OR 1.05/μm, P < 0.001), ΔdP ∈ [−13, 9] μm면 접촉 안정·그 밖은 불균형(모델 κ = 0.59).
전방 힘 성분(Anterior Component of Force, ACF) 불균형을 PCL에 처음으로 정량 연결했으나, 6개월 추적·여성 과대표집·스캔 오차(~5 μm)가 안정 구간과 겹치는 한계.

## Summary
This prospective observational cohort enrolled 78 patients (mean age 41.39 ± 13.36 y) with 90 first-molar, implant-supported zirconia crowns, all on a single Straumann implant system. Using intraoral scanning (Aoralscan 3) and Geomagic Wrap superimposition, the authors quantified occlusal-load-induced changes in the proximal contact gap (ΔdP) — an indirect, non-invasive proxy for the anterior component of force (ACF) acting on the mesial adjacent natural tooth — and in crown centroid position (ΔdC). A stepped metal feeler gauge tracked the resting proximal gap from delivery (D0 = 20 μm) to 6 months (ΔD). PCL incidence was 17.78% (16/90) and any contact status change 48.89% (44/90). ΔdP was the only biomechanical variable that predicted outcome (logistic OR 1.05 per μm, P < 0.001; ART ANOVA η² = 0.08), and a restricted cubic spline defined a stability window of ΔdP ∈ [−13, 9] μm below 10 μm of gap increment, with PCL beyond ~30 μm (validation κ = 0.59). Clinically, the study offers the first quantitative thresholds to guide occlusal assessment of ACF/PCF balance for preventing 식편압입 (food impaction) and PCL on first molar implant crowns, though the short follow-up and measurement error bounds caution against over-extrapolation.

## Key Contributions
- First quantitative thresholds for ACF/PCF-related PCL risk on first-molar implant crowns: ΔdP ∈ [−13, 9] μm → contact stable; [−28, −13) or (9, 30] μm → weakened; (30, 42] μm → PCL (RCS, Nonlinear P < 0.001).
- Shows ΔdP (tested at the proximal contact area, mesiodistal) outperforms ΔdC (centroid displacement) — ΔdC had no independent predictive value (logistic P = 0.873; ART main effect P = 0.236), tied to its inability to capture rotational tooth movement.
- Confirms sex as a PCL correlate (χ² = 7.48, P = 0.024): males had more contact-status changes (63.63%) yet lower PCL (15.15%) than females (19.30%).
- Establishes a reproducible digital protocol (local 4-unit scan, single operator, Geomagic registration, triple measurement) for indirect ACF quantification without in-vivo force transducers.

## Methodology
**Design**: Prospective observational cohort — consecutive enrollment, single-center, non-interventional 6-month follow-up (ethics No. 2024SLL017; clinical trial ChiCTR2500113501).
**n**: 78 subjects (30 M / 48 F), 90 first-molar restorations (maxilla 34 / mandible 56); procedures April 2024 – January 2025; Straumann implants + CAD/CAM zirconia crowns (Lava Plus; 3M).
**Inclusion**: 25–60 y, missing first molar requiring implant restoration, no TMD/parafunction, adequate opposing dentition, adjacent teeth without mobility ≥ Miller I; exclusion of bruxism, RPD/CD opposing, TMD.
**Predictors**: ΔdP (mesiodistal proximal contact gap change pre/post habitual-bite occlusion from superimposed scans), ΔdC (centroid displacement change), plus age/sex/location.
**Outcome**: ΔD = D6 − D0 (feeler-gauge proximal gap; groups tight 20–30 / loose 40–50 / open >50 μm); PCL defined as floss or 50-μm gauge passing unresisted.
**Analysis**: Shapiro-Wilk normality, chi-square, one-way/Welch ANOVA with Scheffé/Tamhane post hoc, binary logistic regression, aligned-rank transform (ART) ANOVA, restricted cubic spline (RCS) with Cohen's Kappa validation (n = 70 train / 20 validation); SPSS 27.0, R 4.5.2; sample size PASS 2021 (f² = 0.67 → min 32 plans).

## Results

| Outcome | Result |
|---|---|
| 6-month PCL incidence | 17.78% (16/90); any contact status change 48.89% (44/90) |
| Sex (PCL / status change) | χ² = 7.48, P = 0.024; male 15.15% PCL / 63.63% change; female 19.30% PCL |
| Age, location | P > 0.05 (no significant effect) |
| ΔdP intergroup | F = 145.96, P < 0.001 (tight < loose < open when ΔdP > 0, all P < 0.001) |
| ΔdC intergroup | Welch F = 37.99, P < 0.001 but pairwise all P > 0.05 |
| Logistic regression | Sex OR 0.14 (CI 0.04–0.46, P = 0.001); ΔdP OR 1.05 (CI 1.02–1.08, P < 0.001, +5.2% odds per μm); ΔdC OR 1.00 (P = 0.873) |
| ART ANOVA on ΔD | ΔdP F = 7.81, P = 0.006, η² = 0.08; ΔdC F = 1.42, P = 0.236; interaction F = 8.17, P = 0.005, η² = 0.09 |
| Simple effects (ΔdC) | ΔdP > 0: t = −3.32, P = 0.001; ΔdP < 0: t = 1.05, P = 0.296 |
| RCS ΔdP→ΔD | Nonlinear P < 0.001, Overall P < 0.001 (J-shaped): ΔdP [−13, 9] μm → ΔD ≤ 10 μm stable; [−28, −13)/(9, 30] μm → ΔD 10–30 μm weakened; (30, 42] μm → ΔD > 30 μm PCL |
| Model validation | Cohen's κ = 0.59, P = 0.003 |

## Related Papers
- [[food-impaction/liu-2025-risk-factors-proximal-contact-loss-implant-prosthetic|Liu 2025 (risk factors)]] — **extends**: risk-factor study for PCL in adjacent natural teeth; this paper deep-dives into the biomechanical pathway (ΔdP as ACF proxy) that mechanistically explains those clinical predictors.
- [[food-impaction/liu-2025-open-contacts-posterior-implants-preventive-concepts|Liu 2025 (preventive concepts)]] — **reinforces**: narrative review arguing for preventive occlusal-management concepts against posterior open contacts; this prospective cohort independently supplies quantitative ΔdP thresholds (e.g. [−13, 9] μm stable zone) supporting that premise.
- [[food-impaction/cui-2025-prevalence-risk-factors-interproximal-contact-loss|Cui 2025]] — **extends**: retrospective prevalence/risk-factor survey of ICL in posterior dentitions; this study extends it from prevalence description to functional-biomechanics quantification via digital occlusion analysis.
- [[food-impaction/kim-2025-factors-influencing-proximal-contact-loss|Kim 2025]] and [[food-impaction/liang-2020-prevalence-associated-factors-retrospective|Liang 2020]] — risk-factor companions; consistent with a multifactorial PCL picture in which occlusal loading is one driver (no direct numeric overlap).
- [[food-impaction/ghasemi-2022-prevalence-proximal-contact-loss-meta-analysis|Ghasemi 2022]] / [[food-impaction/abduo-2022-proximal-contact-loss-qualitative-systematic|Abduo 2022]] — prevalence/influencing-factor baselines; this paper answers the "etiology unclear" gap they identify with a mechanism-level measurement.
- [[food-impaction/pang-2017-prevalence-proximal-contact-loss-prospective|Pang 2017]] — 7-year prospective PCL cohort; a longer-tracking counterpart measuring what this 6-month design can only predict.