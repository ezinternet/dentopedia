---
title: "Multivariate linear regression analysis to identify general factors for quantitative predictions of implant stability quotient values"
authors: Huang H, Xu Z, Shao X, Wismeijer D, Sun P, Wang J, Wu G
year: 2017
date: 2017-10-30
doi: 10.1371/journal.pone.0187010
source: huang-2017-multivariate-regression-isq-prediction.md
category: [implants/isq]
confidence: retrospective
pdf_path: /Users/oracleneo/llm-wiki/papers/huang-2017-multivariate-regression-isq-prediction.pdf
pdf_filename: huang-2017-multivariate-regression-isq-prediction.pdf
source_collection: external
tags: []
relations:
  - type: extends
    target: huang-2020-isq-clinical-significance-literature-review
---

## One-line Summary

Retrospective multivariate regression of 557 implants (3 groups, 2 surgeons, 2 brands) showed bone grafting (T1 coefficient −4 to −5) and implant diameter (T2 coefficient +3.4 to +4.2) are the only surgeon- and system-independent general ISQ predictors.

## 한줄요약

557개 임플란트 다변량 회귀분석에서 T1 ISQ의 일반 예측인자는 골이식 필요 여부(계수 −4~−5), T2 ISQ의 일반 예측인자는 임플란트 직경(계수 +3.4~+4.2)으로 확인되었으며, 성별·연령·골질·식립 단계는 T2에 유의하지 않았음.

## Summary

This retrospective study by Huang et al. (ACTA Amsterdam / Zhejiang University, PLoS ONE 2017) used multivariate linear regression to identify which of 11 candidate clinical factors are **general** ISQ predictors — i.e., consistent across different surgeons and implant systems. Data from 557 implants across three groups (SICace surgeon 1, SICace surgeon 2, Osstem TSIII surgeon 2) were analyzed at T1 (immediate post-placement) and T2 (pre-restoration). The key finding is that most factors influencing ISQ are surgeon- or system-specific, but two factors emerged as general: bone grafting need at T1, and implant diameter at T2.

## Key Contributions

- Identified **bone grafting** (X5) as the sole general T1 ISQ predictor across all groups (β = −4 to −5); unpaired t-test confirmed effect of −5.5 to −7.1 ISQ units
- Identified **implant diameter** (X6) as the consistent general T2 ISQ predictor across all groups (β = +3.4 to +4.2); larger diameter → higher secondary stability ISQ
- Demonstrated that sex, age, bone type (Lekholm & Zarb I–IV), and healing stage (I/II) do NOT significantly influence T2 ISQ across groups
- Confirmed implant **length** is not a significant predictor at T1 or T2 in any group
- Provides quantitative weight coefficients enabling construction of mathematical ISQ prediction equations

## Methodology

- **Design**: Retrospective clinical study; 3 groups, 2 clinics (Hangzhou + Cixi, China), 2012–2015
- **Sample**: 557 implants in 336 patients (329 SICace group 1; 113 SICace + 115 Osstem group 2/3); 3 failures excluded
- **11 factors analyzed**: sex, age, jaw location, immediate/delayed placement, bone grafting, diameter, length, I/II-stage healing, insertion torque, bone type, T1-T2 interval
- **ISQ measurement**: Osstell Mentor, mean of 4 sites (mesial/distal/lingual/buccal)
- **II-stage trigger**: insertion torque < 20 Ncm OR ISQ < 65
- **Statistics**: Multivariate linear regression + unpaired t-test (SPSS 21.0), p < 0.05

## Results

| Factor | T1 general? | T2 general? | Coefficient range |
|---|---|---|---|
| Bone grafting (X5) | **Yes** | Not tested | −4 to −5 (model); −5.5 to −7.1 (t-test) |
| Implant diameter (X6) | Group-specific | **Yes** | +3.4 to +4.2 |
| Implant length (X7) | No | No | NS all groups |
| Sex (X1) | Group-specific | No | NS at T2 |
| Age (X2) | Group-specific | No | NS at T2 |
| Bone type (X10) | Group-specific | No | NS at T2 |
| I/II-stage (X8) | Group-specific | No | NS at T2 |

Failure rates: SICace 0.9%, Osstem TSIII 1.7% (both excluded from regression).

## Related Papers

- [[implants/isq/huang-2020-isq-clinical-significance-literature-review]] — narrative review of ISQ clinical significance; this paper provides the quantitative regression foundation that review's clinical thresholds rest on
- [[implants/isq/javed-2013-primary-stability-osseointegration-factors-influence]] — qualitative overview of factors influencing primary stability; present study quantifies weight coefficients for those same factors
- [[implants/isq/shiffler-2016-implant-length-diameter-location-isq]] — reports diameter and length effects on ISQ; aligns with present study finding that length is NS but diameter is significant at T2
- [[implants/isq/lages-2018-isq-insertion-torque-correlation-sr]] — SR on ISQ–insertion torque correlation; complements the present paper's multivariate model including torque as one of 11 factors
