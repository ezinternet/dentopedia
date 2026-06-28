---
title: "Multivariate linear regression analysis to identify general factors for quantitative predictions of implant stability quotient values"
authors: Huang H, Xu Z, Shao X, Wismeijer D, Sun P, Wang J, Wu G
year: 2017
doi: 10.1371/journal.pone.0187010
category: [implants/isq]
pdf_path: /Users/oracleneo/llm-wiki/papers/huang-2017-multivariate-regression-isq-prediction.pdf
pdf_filename: huang-2017-multivariate-regression-isq-prediction.pdf
source_collection: external
---

## Why Ingested

ISQ 예측 모델의 정량적 근거를 확보하기 위해 인제스트. 기존 [[wiki/implants/isq/huang-2020-isq-clinical-significance-literature-review]] 는 ISQ 임상적 의미를 narrative하게 정리하지만, 어떤 요소가 ISQ 값에 수치적으로 얼마나 영향을 주는지(weight coefficient)를 정량화한 근거는 부재했음. 본 연구(557 implants, 3 groups, multivariate linear regression)가 그 gap을 채움.

## One-line Summary

Retrospective study of 557 implants (3 groups, 2 surgeons, 2 brands) using multivariate linear regression identified bone grafting (T1, coefficient −4 to −5) and implant diameter (T2, coefficient +3.4 to +4.2) as the only surgeon/system-independent general predictors of ISQ.

## 한줄요약

557개 임플란트 후향 연구에서 다변량 회귀분석으로 T1 ISQ는 골이식 필요 여부(계수 −4~−5), T2 ISQ는 임플란트 직경(계수 +3.4~+4.2)이 술자·시스템 독립적인 일반 예측인자임을 확인.

## 1. Document Information

- **Journal**: PLOS ONE 12(10): e0187010
- **Published**: October 30, 2017
- **DOI**: 10.1371/journal.pone.0187010
- **Study design**: Retrospective clinical study
- **Sample**: 557 implants (329 SICace by surgeon 1; 113 SICace + 115 Osstem TSIII by surgeon 2) in 336 patients; 3 failed implants excluded
- **Data collection period**: 2012–2015, two clinics (Hangzhou and Cixi, China)
- **Ethics**: Approved by Review Boards of Best & Easy Dental Clinic and Huayang Dental Clinic

## 2. Key Contributions

1. First multi-surgeon, multi-brand multivariate linear regression model identifying **general** (surgeon/system-independent) ISQ predictors
2. Bone grafting (X5) identified as the sole general predictor at T1 (immediate post-placement ISQ)
3. Implant diameter (X6) identified as the consistent general predictor at T2 (pre-restoration ISQ)
4. Demonstrates that sex, age, bone type, healing stage (I/II), and implant length are NOT general predictors at T2
5. Provides a rational basis for quantitative, personalized ISQ prediction models in clinical practice

## 3. Methodology and Architecture

**Groups**:
- Group 1: 329 SICace implants, surgeon 1 (data from prior study [6])
- Group 2: 113 SICace implants, surgeon 2
- Group 3: 115 Osstem TSIII implants, surgeon 2

**Timepoints**:
- T1: immediately after implant placement
- T2: before dental restoration

**11 candidate factors (X1–X11)**:
- X1 sex, X2 age, X3 maxillary/mandibular, X4 immediate/delayed, X5 bone grafting presence, X6 implant diameter, X7 implant length, X8 I/II-stage healing, X9 insertion torque, X10 bone type (Lekholm & Zarb I–IV), X11 T1–T2 time interval

**ISQ measurement**: Osstell Mentor (mesial/distal/lingual/buccal mean of 4 sites)

**Statistics**: Multivariate linear regression (SPSS 21.0), unpaired t-test, p < 0.05 significance threshold, 95% CI

**II-stage protocol trigger**: insertion torque < 20 Ncm OR ISQ < 65

## 4. Key Results and Benchmarks

**T1 (primary stability predictors)**:
- X5 (bone grafting): significant in all 3 groups, coefficient range −4 to −5 (model); unpaired t-test effect −5.5 to −7.1 (larger than model estimate)
- Other T1 factors (sex, location, immediate/delayed, healing stage, insertion torque) were group-specific, not general

**T2 (secondary stability predictors)**:
- X6 (implant diameter): significant in all 3 groups, coefficient range +3.4 to +4.2 (larger diameter → higher ISQ at T2)
- X1 sex, X2 age, X8 I/II-stage, X10 bone type: NOT significant at T2
- X7 implant length: NOT significant at T1 or T2

**Failure rates**: Group 2 SICace 0.9% (1/114); Group 3 Osstem 1.7% (2/117); excluded from analysis

## 5. Limitations and Future Work

- Retrospective design; data from two Chinese clinics may limit generalizability
- Only 11 candidate factors; implant macro/microdesign and drilling technique not fully controlled
- Model is surgeon- and system-specific in its full form; only 2 general factors emerged
- Sample size per group (81–336 implants) may limit regression power for rare bone types
- Authors suggest prospective validation and expansion of the model with more parameters

## 6. Related Work

- Huang H et al. (prior study [6]): single-surgeon SICace model — diameter and insertion torque at T1/T2; sex, location, immediate/delayed, healing stage, bone graft at T1 specifically
- Javed F & Romanos GE (2010): primary stability importance for osseointegration
- Sennerby L & Meredith N (2008): RFA and ISQ clinical background
- Lekholm & Zarb (1985): bone type classification used for X10

## 7. Glossary

- **ISQ** (Implant Stability Quotient, 임플란트 안정성 지수): 0–100 RFA-derived dimensionless score
- **RFA** (Resonance Frequency Analysis, 공명주파수분석): piezoelectric vibration-based implant stability measurement
- **T1**: immediately post-placement measurement (primary stability)
- **T2**: pre-restoration measurement (secondary stability)
- **Bone grafting (X5)**: presence/absence of augmentation graft at implant site
- **I-stage healing**: one-stage (transgingival) implant placement
- **II-stage healing**: submerged implant; used when torque < 20 Ncm or ISQ < 65
- **Weight coefficient**: multivariate regression β coefficient quantifying factor contribution to ISQ
