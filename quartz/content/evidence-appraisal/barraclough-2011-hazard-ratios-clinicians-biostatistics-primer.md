---
title: "Biostatistics Primer — What a Clinician Ought to Know: Hazard Ratios"
authors: Barraclough H, Simms L, Govindan R
year: 2011
date: 2011-06-01
doi: 10.1097/JTO.0b013e31821b10ab
source: barraclough-2011-hazard-ratios-clinicians-biostatistics-primer.md
category: evidence-appraisal
evidence_level: narrative-review
pdf_path: /Users/oracleneo/llm-wiki/papers/barraclough-2011-hazard-ratios-clinicians-biostatistics-primer.pdf
pdf_filename: barraclough-2011-hazard-ratios-clinicians-biostatistics-primer.pdf
source_collection: external
tags: [hazard-ratio, kaplan-meier, survival-analysis, biostatistics, ebm-tutorial]
---

## Three-line Summary

Narrative biostatistics primer (J Thoracic Oncology 2011) for clinicians: defines hazard ratio (HR) as a time-averaged instantaneous hazard-rate ratio under the proportional-hazards (PH) assumption, built using Kaplan-Meier censoring, and distinguishes it from relative risk (RR), which uses cumulative incidence at a fixed time point.

PH assumption violation (crossing or fanning Kaplan-Meier curves) makes a single HR misleading; the paper recommends stratified analysis, milestone survival, or RMST when PH fails.

For dental implant survival studies where PH is often unchecked, HR of 1.5–3.0 (e.g., smoking effect on early failure) should be translated to absolute risk at a clinically relevant horizon before patient counseling.

## 세줄요약

임상의 대상 biostatistics primer (J Thoracic Oncology 2011): HR을 비례위험(PH) 가정 하에서 시간 평균된 즉시 hazard rate 비율로 정의하고, KM 생존곡선·중도절단과의 관계를 설명하며 RR(고정 시점 누적 발생률 비)과 구분.

PH 가정 위반(KM 곡선 교차·발산) 시 단일 HR은 오도적 — 층화 분석·마일스톤 생존율·RMST로 대체 권고.

임플란트 생존 연구에서 HR 1.5–3.0(흡연 조기 실패 위험 등)은 PH 검증 없이 보고되는 경우가 많으므로, 환자 상담 전 임상적으로 의미 있는 시점(1년·5년)의 절대위험으로 변환 필요.

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
