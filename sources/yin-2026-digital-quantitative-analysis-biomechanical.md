---
title: "Digital quantitative analysis of biomechanical factors of proximal contact loss of first molar implant crown"
authors: Derong Yin, Lingrui Gao, Hongwei Gao, Lijun Xue, Zhongda Wang, Meie Jia, Feng Wu
year: 2026
doi: 10.1186/s12903-026-08773-x
category: food-impaction
pdf_path: /Users/oracleneo/llm-wiki/papers/yin-2026-digital-quantitative-analysis-biomechanical.pdf
pdf_filename: yin-2026-digital-quantitative-analysis-biomechanical.pdf
source_collection: external
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13527992/
---

## Why Ingested
User initiated a PubMed ingest sweep on the food-retention (식편압입) topic; this paper supplies the biomechanical/digital-quantitative angle on PCL of first molar implant crowns that the existing PCL pages (prevalence/risk-factor/management) lack — it extends the mechanism behind risk factors documented in [[wiki/food-impaction/liu-2025-risk-factors-proximal-contact-loss-implant-prosthetic|Liu 2025]] and [[wiki/food-impaction/cui-2025-prevalence-risk-factors-interproximal-contact-loss|Cui 2025]] by quantifying an anterior component of force (ACF) proxy via digital model superimposition and tying it to 6-month proximal gap changes.

## Three-line Summary
Prospective observational cohort: 78 patients (mean 41.39 ± 13.36 y), 90 first-molar implant zirconia crowns (Straumann, all cases), intraoral 3D scanning + digital model analysis of occlusal-load-induced changes, 6-month follow-up.
6-month PCL incidence was 17.78% (16/90); ΔdP (proximal contact area gap change pre/post occlusion) was the core predictor (OR 1.05/μm, P < 0.001); RCS showed stable contacts at ΔdP ∈ [−13, 9] μm and PCL beyond ~30 μm (model κ = 0.59, P = 0.003).
First digital-quantitative thresholds linking ACF/PCF imbalance to PCL — but 6-month follow-up, female overrepresentation, and ~5 μm scanning error overlapping the stability window are key limits.

## 세줄요약
전향적 관찰 코호트(78명, 제1대구치 임플란트 지르코니아 크라운 90개, 6개월 추적)에서 구강 내 3D 스캔+디지털 모델 중첩으로 교합부하 유발 변화를 정량화.
6개월 근접접촉 소실(Proximal Contact Loss, PCL) 발생률 17.78%(16/90), 교합 전후 접촉 간극 변화(ΔdP)가 핵심 예측인자(OR 1.05/μm, P < 0.001), ΔdP ∈ [−13, 9] μm면 접촉 안정·그 밖은 불균형(모델 κ = 0.59).
전방 힘 성분(Anterior Component of Force, ACF) 불균형을 PCL에 처음으로 정량 연결했으나, 6개월 추적·여성 과대표집·스캔 오차(~5 μm)가 안정 구간과 겹치는 한계.

## 1. Document Information
- **Journal**: BMC Oral Health 2026;26:1634
- **DOI**: 10.1186/s12903-026-08773-x
- **PMID**: 42298520 / **PMCID**: PMC13527992
- **Institution**: Shanxi Medical University School and Hospital of Stomatology, Taiyuan, Shanxi, China
- **Joint first authors**: Derong Yin, Lingrui Gao; **Corresponding**: Meie Jia, Feng Wu
- **Clinical trial**: ChiCTR2500113501 (retrospective registration 2025-11-29)

## 2. Key Contributions
- Indirect, non-invasive quantification of the anterior/posterior component of force (ACF/PCF) effect on PCL via digital model superimposition of pre/post-occlusion intraoral scans — computed at the proximal contact area (ΔdP) rather than via centroid (ΔdC), which failed to predict outcomes.
- Defined clinically actionable ΔdP thresholds: contact stable when ΔdP ∈ [−13, 9] μm, weakened at [−28, −13) or (9, 30] μm, and PCL when ΔdP > 30 μm (up to 42 μm); RCS model with κ = 0.59 (P = 0.003).
- First molar crown data showing that 48.89% (44/90) of sites show some proximal contact status change by 6 months, with only 17.78% meeting PCL definition.

## 3. Methodology and Architecture
- **Design**: Prospective observational cohort (single-center, consecutive enrollment, non-interventional 6-month follow-up; approved by Ethics Committee of Shanxi Medical University Hospital of Stomatology, No. 2024SLL017)
- **n**: 78 participants (30 M / 48 F, mean age 41.39 ± 13.36 y); 90 first-molar implant-supported restorations (maxilla 34 / mandible 56); treated April 2024 – January 2025
- **Restoration**: single implant system (Straumann), CAD/CAM zirconia crowns (Lava Plus; 3M), standardized protocol; baseline proximal contact verified by floss resistance + non-insertion of a 30-µm feeler gauge; occlusal contacts refined with 12-µm shim stock film
- **Measurements**: intraoral scanning (Aoralscan 3; SHINING 3D) at rest and at intercuspal clamping (habitual bite force, ICP training with 100-µm articulating paper); Geomagic Wrap 2021 preprocessing → ΔdP (change in mesiodistal proximal contact gap pre/post-occlusion), ΔdC (change in centroid displacement); proximal contact gap D by stepped metal feeler gauge (30–100 µm) at delivery (D0 = 20 µm) and 6 months (D6); ΔD = D6 − D0; groups: tight (20–30), loose (40–50), open (>50 µm)
- **Statistics**: Shapiro-Wilk normality; chi-square, one-way/Welch ANOVA, binary logistic regression, ART ANOVA, restricted cubic spline (RCS); validated with Cohen's Kappa (n=70 train / 20 validation); SPSS 27.0, R 4.5.2; sample size PASS 2021 (α=0.05, power 0.8, f²=0.67 → min 32, +10% dropout → ≥36)

## 4. Key Results and Benchmarks
- **Incidence**: PCL (floss or 50-µm gauge passes unresisted) 17.78% (16/90); any proximal contact status change (weakening or loss) 48.89% (44/90)
- **Demographics**: sex χ² = 7.48, P = 0.024 (male 15.15% PCL but 63.63% status change; female 19.30% PCL); age and maxilla/mandible location P > 0.05
- **ΔdP**: intergroup F = 145.96, P < 0.001; ΔdP > 0: tight < loose < open (all P < 0.001); ΔdP < 0: tight vs loose P = 0.005, tight vs open P = 0.049, loose vs open P = 0.995
- **ΔdC**: Welch F = 37.99, P < 0.001 but no significant Tamhane T2 pairwise differences (all P > 0.05)
- **Binary logistic regression** (outcome = change vs no change): Sex OR 0.14 (95% CI 0.04–0.46, P = 0.001; females ~14% of male odds); ΔdP OR 1.05 (1.02–1.08, P < 0.001, +5.2% odds per 1 µm); ΔdC OR 1.00 (0.99–1.01, P = 0.873); ln(p/(1−p)) = 2.919 − 1.98×Sex + 0.05×ΔdP − 0.00×ΔdC (p = prob. of no change)
- **ART ANOVA on ΔD**: ΔdP F = 7.81, P = 0.006, η² = 0.08; ΔdC F = 1.42, P = 0.236; ΔdP×ΔdC interaction F = 8.17, P = 0.005, η² = 0.09; simple effects: ΔdP > 0 → ΔdC significant (t = −3.32, P = 0.001), ΔdP < 0 → not (t = 1.05, P = 0.296)
- **RCS (ΔdP → ΔD)**: Nonlinear P < 0.001, Overall P < 0.001, J-shaped; ΔdP ∈ [−13, 9] μm → ΔD ≤ 10 μm (stable); [−28, −13) or (9, 30] μm → ΔD 10–30 μm (weakened); (30, 42] μm → ΔD > 30 μm (PCL); validation κ = 0.59, P = 0.003

## 5. Limitations and Future Work
- Small sample (n = 90) and female overrepresentation; single-center, single-operator design; inter-operator repeatability not evaluated in this study (prior group work: ICC ≥ 0.800)
- Single-acquisition scan systematic error ~5 μm overlaps the tight-group stability window (−13 to 9 μm); occlusal registration error estimated 10–20 μm
- Feeler-gauge resolution (10 μm steps) can't quantify gap changes < 10 μm; tooth mobility graded by subjective clinical inspection
- 6-month follow-up too short for early dynamic/interproximal drift trends; single habitual bite-force record ignores individual variation in force amplitude/direction/duration
- Future: 12–24-month follow-up with multiple timepoints (1, 3, 6, 12 mo), ≥3 repeated scans with ICC, dental mobility meter, micron-level gap measurement, gender-balanced larger cohorts

## 6. Related Work
- [[wiki/food-impaction/liu-2025-risk-factors-proximal-contact-loss-implant-prosthetic|Liu 2025]]: risk-factor study for PCL in adjacent natural teeth; this paper supplies the biomechanical mechanism (ΔdP/ACF proxy) behind those clinical risk factors
- [[wiki/food-impaction/cui-2025-prevalence-risk-factors-interproximal-contact-loss|Cui 2025]]: retrospective prevalence/risk-factor study; this workflow-type study quantifies the occlusal-loading pathway instead of surveying prevalence
- [[wiki/food-impaction/liu-2025-open-contacts-posterior-implants-preventive-concepts|Liu 2025 (preventive concepts)]]: narrative review advocating preventive occlusal/concept approaches; this study independently provides prospective quantitative ΔdP thresholds supporting that premise
- [[wiki/food-impaction/ghasemi-2022-prevalence-proximal-contact-loss-meta-analysis|Ghasemi 2022]] and [[wiki/food-impaction/abduo-2022-proximal-contact-loss-qualitative-systematic|Abduo 2022]]: prevalence/influencing-factors baselines; this paper addresses the "precise etiology unclear" gap they flag
- [[wiki/food-impaction/pang-2017-prevalence-proximal-contact-loss-prospective|Pang 2017]]: 7-year prospective PCL follow-up; shorter-tracking counterpart that motivates longer follow-up here
- [[wiki/food-impaction/mehanna-2021-proximal-contact-alterations-prospective|Mehanna 2021]]: 3-month prospective proximal contact alteration study; similar short-horizon digital assessment of contact changes

## 7. Glossary
- **ACF**: anterior component of force — horizontal force vector generated along cuspal inclines during jaw closure, implicated in physiological mesial drift; magnitude can reach ~5× that of PCF
- **PCF**: posterior component of force — posteriorly directed occlusal force component
- **ΔdP**: change in the mesiodistal proximal contact gap between the implant crown (first molar) and mesial adjacent tooth (second premolar) before vs after occlusion — study's core ACF/PCF proxy (unit: μm)
- **ΔdC**: change in crown centroid distance pre/post-occlusion — simpler but not predictive (failed in logistic + ART analyses)
- **ΔD**: increment in proximal contact gap from delivery (D0 = 20 μm) to 6-month follow-up (D6), measured by stepped metal feeler gauge
- **RCS**: restricted cubic spline regression — nonlinear dose-response model of ΔdP on ΔD, validated with Cohen's Kappa (κ)