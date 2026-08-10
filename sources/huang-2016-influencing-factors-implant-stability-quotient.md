---
title: "Mathematical evaluation of the influence of multiple factors on implant stability quotient values in clinical practice: a retrospective study"
authors: Hairong Huang, Daniel Wismeijer, Xianhong Shao, Gang Wu
year: 2016
doi: 10.2147/TCRM.S113764
category: [implants/isq]
pdf_path: /Users/oracleneo/llm-wiki/papers/huang-2016-influencing-factors-implant-stability-quotient.pdf
pdf_filename: huang-2016-influencing-factors-implant-stability-quotient.pdf
source_collection: external
---

## Why Ingested

임플란트 안정성 지수 (Implant Stability Quotient, ISQ)에 영향을 미치는 요인들을 정량화(가중계수, weight coefficient)한 초기 단일술자 모델. 기존 [[wiki/implants/isq/huang-2017-multivariate-regression-isq-prediction]] (2017, PLOS ONE)이 바로 이 연구의 데이터(Group 1, SICace 329 implants)를 확장해 다술자·다시스템 비교를 수행하며 "prior study [6]"로 명시 인용한 원논문으로, 두 논문 간 파생관계를 완성하기 위해 인제스트. 본 논문은 단일술자·단일임플란트시스템 조건에서 T1(식립직후)에 7개, T2(보철직전)에 3개 요인이 유의함을 최초로 정량화했으나, 2017년 후속연구는 이 중 골이식 여부(T1)와 임플란트 직경(T2) 단 2개만 술자·시스템 독립적 general predictor임을 보여 원논문 결론의 일반화 범위를 좁힘.

## Three-line Summary

Retrospective single-surgeon, single-implant-system study of 329 SICace implants in 177 patients used multivariate linear regression to identify which of 11 candidate factors significantly influence resonance-frequency-analysis (RFA)-derived ISQ at T1 (immediately post-placement) and T2 (pre-restoration).

Seven factors were significant at T1 (sex, maxillary/mandibular location, immediate/delayed implantation, bone grafting, implant diameter, I-/II-stage healing, insertion torque; standardized coefficients 0.111–0.286), while only three factors remained significant at T2 (implant diameter β=0.414, insertion torque β=0.150, T1–T2 interval β=0.191); implant diameter and insertion torque were the only two factors significant at both time points.

Provides regression equations (Y(T1) and Y(T2)) to estimate ISQ from clinical parameters, but the authors explicitly caution the model is likely surgeon-, implant-system-, and clinic-specific — a caveat later confirmed by Huang et al. 2017, which found only bone grafting (T1) and implant diameter (T2) generalized across surgeons/systems.

## 세줄요약

177명 환자, SICace 임플란트 329개 대상 단일술자 후향적 연구에서 다변량 선형회귀로 11개 후보 요인 중 T1(식립직후) ISQ에 영향을 미치는 요인 7개, T2(보철직전) ISQ에 영향을 미치는 요인 3개를 규명.

T1 유의 요인: 성별, 상악/하악 위치, 즉시/지연 식립, 골이식 필요 여부, 임플란트 직경, I/II기 치유방식, 식립토크 (표준화계수 0.111~0.286); T2 유의 요인은 임플란트 직경(β=0.414), 식립토크(β=0.150), T1-T2 시간간격(β=0.191) 3개뿐이며 T1·T2 모두에서 유의한 요인은 직경·토크 2개뿐.

ISQ 추정 회귀식을 제시했으나 저자 스스로 술자·임플란트시스템·클리닉 특이적 모델일 가능성을 명시했고, 이는 2017년 후속연구([[wiki/implants/isq/huang-2017-multivariate-regression-isq-prediction]])에서 골이식(T1)·직경(T2) 단 2개 요인만 술자/시스템 독립적임이 확인되며 실제로 입증됨.

## 1. Document Information

- **Journal**: Therapeutics and Clinical Risk Management 2016;12:1525–1532
- **DOI**: 10.2147/TCRM.S113764
- **Institution**: Academic Centre for Dentistry Amsterdam (ACTA), VU University Amsterdam and University of Amsterdam, The Netherlands; Best & Easy Dental Clinic, Hangzhou, Zhejiang Province, China

## 2. Key Contributions

- First mathematical (multivariate linear regression) model quantifying the weight coefficient of each of 11 candidate clinical factors on ISQ at both T1 (immediate post-placement) and T2 (pre-restoration)
- Provides closed-form regression equations to estimate ISQ from measurable clinical parameters at each time point
- Demonstrates that T1 and T2 are governed by largely different factor sets — only implant diameter and insertion torque are significant at both
- Bone type (Lekholm & Zarb I–IV) and implant length were NOT significant at either T1 or T2, consistent with some prior literature but contrasting with others

## 3. Methodology and Architecture

- **Design**: Retrospective single-clinic, single-surgeon, single-implant-system cohort study
- **Sample**: 329 implants (SICace, SIC Invent AG) in 177 patients treated 2012–2015 at Best & Easy Dental Clinic, Hangzhou, China; 2 implant failures (0.6%) excluded
- **Candidate factors (X1–X11)**: sex, age, maxillary/mandibular location, immediate/delayed implantation, bone grafting presence, implant diameter, implant length, I-/II-stage healing pattern, insertion torque, bone type (Lekholm & Zarb), T1–T2 time interval
- **ISQ measurement**: Osstell Mentor, mean of mesial/distal/labial/lingual readings at T1 (immediately post-placement) and T2 (pre-restoration, typically 6–12 weeks later)
- **Statistics**: Kruskal–Wallis (site comparison), paired t-tests (T1 vs T2, immediate vs delayed), multivariate linear regression (SPSS 21.0), significance p<0.05, 95% CI

## 4. Key Results and Benchmarks

**T1 regression** — Y(T1) = 57.263 + 1.317(X1) + 1.471(X3) + 1.836(X4) − 4.990(X5) + 1.669(X6) + 2.961(X8) + 0.131(X9); significant factors and standardized β: sex 0.111, maxillary/mandibular 0.121, immediate/delayed 0.148, bone grafting −0.235, implant diameter 0.119, I-/II-stage 0.241, insertion torque 0.286 (all p<0.05).

**T2 regression** — Y(T2) = 56.988 + 4.080(X6) + 0.048(X9) + 0.014(X11); significant factors and standardized β: implant diameter 0.414, insertion torque 0.150, T1–T2 interval 0.191.

**Descriptive**: mean ISQ T1 74.34±6.75, T2 77.00±4.89 (no significant inter-site difference at either timepoint). Immediate implants had significantly lower T1 ISQ than delayed (73.68±6.50 vs 75.82±5.49, p=0.038) but no significant T2 difference (77.00±4.30 vs 77.63±4.07, p=0.334); both groups showed significant T1→T2 increase (p<0.001 and p=0.001).

## 5. Limitations and Future Work

- Retrospective, single-surgeon, single-implant-system (SICace) design — authors explicitly state the regression equations may be specific to this implantologist/system/clinic and caution against extrapolation
- Missing data for several factors (age, insertion torque, bone type, T1–T2 interval) reduces effective n for some regressions
- Bone type used a simplified Lekholm & Zarb classification via dummy variables, not histomorphometric/CBCT quantification
- Authors call for future studies testing the model's reliability across other implant types/surgeons — directly addressed by the follow-up multi-surgeon, multi-system study (Huang et al. 2017)

## 6. Related Work

- Huang H et al. 2017 (PLOS ONE, [[wiki/implants/isq/huang-2017-multivariate-regression-isq-prediction]]): direct follow-up using this study's Group 1 SICace cohort plus 2 additional surgeon/system groups (557 implants total); found only bone grafting (T1) and implant diameter (T2) generalize across surgeons/systems — refines this paper's 7-factor (T1) / 3-factor (T2) findings to 2 truly general predictors
- Gehrke SA et al. (implant macrodesign and primary stability)
- Han J, Lulic M, Lang NP 2010 (RFA factors: surface modification, implant diameter)
- Meredith N, Alleyne D, Cawley P 1996 (original RFA/ISQ concept)

## 7. Glossary

- **ISQ** (Implant Stability Quotient, 임플란트 안정성 지수): 0–100 dimensionless score derived from RFA
- **RFA** (Resonance Frequency Analysis, 공명주파수분석): piezoelectric transducer-based noninvasive implant stability measurement
- **T1**: ISQ measured immediately after implant placement (primary stability)
- **T2**: ISQ measured immediately before restoration/loading (secondary stability, post-osseointegration)
- **I-stage/II-stage healing**: one-stage (transgingival) vs submerged (two-stage) implant placement protocol; II-stage triggered when insertion torque <20 Ncm or ISQ <65
- **Standardized coefficient (β)**: regression weight expressed in standard-deviation units, allowing direct comparison of relative influence across factors measured on different scales
