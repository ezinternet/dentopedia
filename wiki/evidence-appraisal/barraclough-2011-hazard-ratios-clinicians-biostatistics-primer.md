---
title: "Biostatistics Primer — What a Clinician Ought to Know: Hazard Ratios"
authors: Barraclough H, Simms L, Govindan R
year: 2011
date: 2011-06-01
doi: 10.1097/JTO.0b013e31821b10ab
source: barraclough-2011-hazard-ratios-clinicians-biostatistics-primer.md
category: evidence-appraisal
confidence: narrative-review
pdf_path: /Users/oracleneo/llm-wiki/papers/barraclough-2011-hazard-ratios-clinicians-biostatistics-primer.pdf
pdf_filename: barraclough-2011-hazard-ratios-clinicians-biostatistics-primer.pdf
source_collection: external
tags: [hazard-ratio, kaplan-meier, survival-analysis, biostatistics, ebm-tutorial]
---

## One-line Summary
Narrative biostatistics primer (J Thoracic Oncology 2011) for clinicians on hazard ratios (HR): defines HR as an instantaneous hazard-rate ratio time-averaged under the proportional-hazards (PH) assumption, contrasts it with relative risk (RR), and explains how PH violation (crossing/diverging Kaplan-Meier curves) makes a single HR misleading.

## 한줄요약
J Thoracic Oncology의 임상의 대상 통계 primer (2011): HR이 무엇이고 무엇이 아닌지 — 즉시 hazard rate 비율로서의 정의, KM curve와의 관계, proportional hazards 가정 위반 시 해석 무력화까지 짚는 5쪽짜리 표준 튜토리얼.

## Summary
Implant and bone-graft outcome studies in this wiki routinely report HR (e.g., for time-to-failure, time-to-MBL-threshold, time-to-peri-implantitis). This paper is the reference for how to read those numbers honestly.

## Key Contributions
- HR is a hazard-rate ratio, not a percentage difference in outcome.
- HR averages across the entire follow-up under the proportional hazards (PH) assumption — if PH fails (curves cross, late divergence), the single HR is misleading.
- Distinguishes HR from RR: HR uses time-to-event with censoring; RR uses cumulative incidence at a fixed time point. They can yield different conclusions on the same data.

## Methodology
- Narrative review with hypothetical two-arm RCT (weekly death rates, censoring, KM curve construction).
- Walks through how PH violation looks on KM plots (crossing or fanning curves) and what to do (stratified analysis, milestone survival, RMST).

## Results
No empirical results.

## Clinical Applicability
- Implant survival HRs of 1.5–3.0 (e.g., smoking effect on early failure) sound large until you remember HR is multiplicative and time-averaged — translate to absolute risk at a relevant horizon (1y, 5y) before counseling patients.
- For dental survival curves with very few late events, the PH assumption is often unchecked. Treat HR as an approximation, not a precise summary.

## Caveats
- Pre-immunotherapy era — does not cover the now-standard practice of reporting RMST when PH is violated.

## Related Papers
- [[evidence-appraisal/flechner-2011-pvalues-confidence-intervals-number-needed]] — 같은 시리즈 격, p-value/CI/NNT 편.
- [[evidence-appraisal/monaghan-2021-odds-ratios-relative-risk-absolute]] — OR/RR/AR/NNT — HR과의 차이 이해.
- [[evidence-appraisal/darrigo-2024-common-mistakes-biostatistics]] — HR 오용 사례 명시.
- [[overviews/evidence-appraisal-toolkit]] — 9편 종합.
