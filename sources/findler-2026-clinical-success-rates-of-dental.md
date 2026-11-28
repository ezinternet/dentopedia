---
title: "Clinical Success Rates of Dental Implants with Bone Grafting in a Large-Scale National Dataset"
authors: Findler M, Doron H, Mann J, Chackartchi T, Tobias G, Taba M Jr, Kasaj A, Park CH
year: 2026
doi: 10.3390/jfb17010046
category: [immediate-implant]
source_collection: pubmed-text
full_text: true
pmid: "41590814"
pmcid: "PMC12843187"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12843187/
text_path: /Users/oracleneo/llm-wiki/papers/findler-2026-clinical-success-rates-of-dental.txt
text_filename: findler-2026-clinical-success-rates-of-dental.txt
---

## Why Ingested

Surveillance for "IIP success criteria" surfaced this very large national-cohort study (n=158,824 implants) because it quantifies immediate placement as an independent risk indicator for implant failure (3.08% vs 2.07%, odds ratio 1.487) — a population-level counterweight to the smaller RCT and SR evidence on immediate-vs-delayed timing already held in the wiki. Ingested as risk-factor evidence, not as a criteria/guideline document.

→ [[immediate-implant/tonetti-2017-immediate-vs-delayed-implant-timing-rct]]
→ [[immediate-implant/lang-2012-immediate-implant-survival-success-sr]]

## Three-line Summary

Retrospective cohort analysis of 158,824 implants (53,874 patients, 2014–2022) from a nationwide Israeli dental network, of which 45,715 were placed with simultaneous bone augmentation (DBGIs); generalized estimating equations adjusted for patient clustering.

Augmented implants achieved 97.83% clinical success (2.17% failure), statistically comparable to the general implant population, but immediate placement was an independent risk indicator — 3.08% failure vs 2.07% for early/delayed (OR 1.487, p<0.000) — and 70% of failures occurred within the first year.

The "stabilization hypothesis" (augmentation does not inherently raise failure) is supported, while timing, male sex, maxillary location, and low socioeconomic status are the modifiable/nonmodifiable risk dimensions that should feed personalized IIP case selection; administrative-coding design limits granular confounding control.

## 세줄요약

이스라엘 전국 치과 네트워크 기록(2014–2022)을 이용한 후향적 코호트 분석 — 임플란트 158,824개(환자 53,874명), 그중 동시 골이식 45,715개; GEE(Generalized Estimating Equations)로 환자 내 상관 보정.

동시 골이식 임플란트의 임상 성공률은 97.83%(실패 2.17%)로 전체 임플란트 집단과 통계적으로 유사했으나, 즉시식립은 독립 위험인자였음(실패 3.08% vs 조기/지연식립 2.07%, 오즈비 1.487, p<0.000); 실패의 70%는 1년 이내 발생.

골이식 자체가 실패 위험을 높이지 않는다는 "안정화 가설"을 지지하는 반면, 식립 시기·남성·상악 위치·낮은 사회경제적 지위가 즉시식립 증례 선택 시 고려할 위험 차원임을 시사; 행정 코딩 기반 설계 때문에 세부 교란 변수 통제는 제한됨.

## 1. Document Information

- **Title**: Clinical Success Rates of Dental Implants with Bone Grafting in a Large-Scale National Dataset
- **Authors**: Findler M, Doron H, Mann J, Chackartchi T, Tobias G, Taba M Jr, Kasaj A, Park CH
- **Journal**: Journal of Functional Biomaterials, 2026;17(1):46 (published 2026-01-15)
- **DOI**: 10.3390/jfb17010046
- **PMID / PMCID**: 41590814 / PMC12843187
- **Study type**: Retrospective cohort (national registry) with multivariable GEE
- **Retrieval**: PMC open-access full text (JATS), 2026-11-17

## 2. Key Contributions

- Quantifies clinical success of implants placed with **simultaneous bone augmentation** in a real-world national dataset (45,715 augmented implants within 158,824 total).
- Identifies **immediate placement as an independent failure risk indicator** even after augmentation adjustment: 3.08% vs 2.07% failure (OR 1.487, p<0.000), reinforcing that IIP is technique-sensitive.
- Demonstrates a **temporal failure pattern**: ~70% of failures occur within the first year in both augmented and non-augmented cohorts, pointing to osseointegration establishment rather than late biologic complications as the dominant challenge.
- Adds **socioeconomic status (SES)** as a novel risk dimension (3.07% low vs 2.06% high SES), independent of clinical covariates, in a universal healthcare setting.
- Frames the augmentation debate via the **stabilization vs complexity hypotheses**, concluding augmentation is safe once timing is accounted for.

## 3. Methodology and Architecture

- **Data source**: Maccabi Dent electronic dental records (Maccabi Health Services, Israel); all implant placements 2014-01-01 to 2022-12-31 extracted with linked grafting and prosthetic codes.
- **DBGI definition**: bone-graft procedure code on the same day and anatomical site as implant placement; augmentation techniques included socket grafting, GBR, ridge expansion with grafting, block grafts, sinus floor elevation.
- **Timing definition**: immediate = placement recorded on the same date/site as extraction; all others early/delayed.
- **Outcome**: binary failure (implant removal or documented failure); early ≤1 year vs late >1 year; before vs after prosthetic restoration.
- **Statistics**: chi-square univariate; multivariable Generalized Estimating Equations (binary logistic link, exchangeable correlation, robust SE) for sex, SES, timing, six jaw regions, restoration type, concurrent grafting; OR with 95% CI; no imputation (listwise exclusion).

## 4. Key Results and Benchmarks

- **Cohort**: 158,824 implants in 53,874 patients (29,501 female, 24,177 male, 196 unclassified); mean age 55.54 ± 11.93 years (18–88).
- **Augmented group**: 45,715 implants in 17,600 patients; 11.4% (n=4,682) immediate vs 88.6% (n=41,033) early/delayed.
- **Overall augmented success**: 97.83% (994 failures); immediate augmented failure 3.08% vs early/delayed 2.07% (p<0.001; multivariable OR 1.487, p<0.000).
- **Timing of failure**: 696/994 augmented failures (70%) within first year; 298 (30%) after 1 year; 324 (32.6%) after prosthetic reconstruction. Across all 158,824 implants: 3,507 failures, 2,476 (70%) early.
- **Mean intervals**: placement→failure 13.77 ± 17.31 months; restoration delivered at 6.19 ± 3.57 months; loading→failure 22.9 ± 21.81 months.
- **Anatomy**: failure higher in maxilla than mandible (p<0.01); highest in maxillary molar 3.36% and maxillary incisor 3.09%; mandibular regions uniform 1.61–1.69%; maxillary premolar 2.16% vs mandibular 1.16% (p<0.0056).
- **Sex / SES**: male 2.5% vs female 1.9% failure (p=0.0002); low SES 3.07% vs high SES 2.06%.
- **Restoration type**: removable overdentures 2.18% vs fixed crowns 0.80% post-loading failure.

## 5. Limitations and Future Work

- Retrospective administrative-coding design; no granular data on smoking, periodontitis history, or specific graft materials.
- Procedural heterogeneity (sinus elevation, horizontal augmentation mixed) prevented dedicated subgroup analysis for simultaneous horizontal augmentation.
- Binary failure definition (removal only) cannot capture retained implants with marginal bone loss, likely underestimating peri-implantitis prevalence.
- Variable follow-up; a 10-year Kaplan–Meier curve was not feasible for the whole cohort.
- Authors call for prospective evaluations of specific graft materials and personalized risk-assessment models incorporating demographic and clinical variables.

## 6. Related Work

- Confirms the high-survival bottom line of [[immediate-implant/lang-2012-immediate-implant-survival-success-sr]] at population scale, but narrows it by identifying immediate placement as a failure risk indicator.
- Qualifies the immediate-vs-delayed comparison in [[immediate-implant/tonetti-2017-immediate-vs-delayed-implant-timing-rct]] with real-world registry data (technique sensitivity in augmented sites).
- Uses the ITI Type 1–4 placement-timing classification referenced across the immediate-implant category ([[immediate-implant]]).
- Relevant to case-selection frameworks such as [[immediate-implant/liu-2025-iip-iipp-classification-surgical-restorative]] by supplying population-level risk modifiers.

## 7. Glossary

- **DBGI** — Dental Bone Grafting Implant; implant placed with same-day grafting code.
- **GEE** — Generalized Estimating Equations (일반화 추정방정식); handles within-patient clustering of multiple implants.
- **SES** — Socioeconomic status (사회경제적 지위); proxy via clinic location index aligned to Israel CBS clusters 1–9.
- **Early failure** — implant failure ≤1 year post-placement, taken as impaired osseointegration.
- **Stabilization hypothesis** — augmentation restores anatomy and mechanical anchorage, lowering failure risk; contrasted with the complexity hypothesis.
