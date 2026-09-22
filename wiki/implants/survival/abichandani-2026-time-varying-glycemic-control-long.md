---
title: "Effect of Time-Varying Glycemic Control on Long-Term Dental Implant Outcomes"
authors: "Abichandani SJ, Dutta A"
year: 2026
date: 2026-01-05
doi: "10.11607/jomi.11625"
source: abichandani-2026-time-varying-glycemic-control-long.md
category: [implants/survival]
confidence: retrospective
pdf_path: /Users/oracleneo/llm-wiki/papers/abichandani-2026-time-varying-glycemic-control-long.txt
pdf_filename: abichandani-2026-time-varying-glycemic-control-long.txt
source_collection: external
tags: [diabetes, HbA1c, glycemic-control, implant-failure, peri-implantitis, dose-response, time-varying]
relations:
  - type: extends
    target: al-ansari-2022-diabetes-mellitus-dental-implants-sr-ma
  - type: extends
    target: shahi-2026-implant-outcomes-diabetes-mellitus-sr
---

## One-line Summary
Retrospective cohort (782 adults, 1,312 implants, 5.6 yr median) demonstrating that time-varying HbA1c ≥8.0% doubles 5-year implant failure risk (8.1%) and peri-implantitis risk (26.0%) compared with HbA1c <7.0% (3.2% / 12.1%), with a non-linear dose-response steepening above the 8% threshold.

## 한줄요약
782명 1312개 임플란트 코호트(중앙값 5.6년): 시간가변 HbA1c (당화혈색소, Glycated Hemoglobin, HbA1c) ≥8%에서 5년 실패율 8.1%, 임플란트 주위염 (Peri-Implantitis, PI) 발생률 26.0%로 HbA1c <7% 대비 약 2배 — 8% 이상에서 비선형 위험 급증.

## Summary
This retrospective cohort study enrolled 782 adults receiving endosseous implants across a multi-provider network (2015–2024), with 1,312 implants and a median follow-up of 5.6 years. HbA1c was modeled as a **time-varying exposure** updated at each clinical visit (30-day lag, 90-day carry-forward), representing a methodological advance over single-baseline HbA1c studies. Using cause-specific Cox models with surgeon frailty terms and Fine-Gray competing-risk models, the authors found a dose-dependent association between glycemic control and both implant failure (68 events) and peri-implantitis (171 events). Five-year absolute risks stratified by HbA1c band provide directly actionable numbers for shared decision-making.

## Key Contributions
- Time-varying HbA1c modeling captures longitudinal glycemic fluctuations — more biologically valid than baseline-only classification
- Restricted cubic spline analysis reveals **non-linear threshold** at ~8%: risk rises more steeply above this level
- **Absolute 5-year risk tables** by HbA1c band: enables patient-specific informed consent
- Competing-risk and sensitivity analyses confirm robustness of findings
- Multi-provider design (with surgeon frailty) reduces provider-level confounding

## Methodology
- Retrospective cohort; multi-provider practice network, 2015–2024
- n = 782 patients, 1,312 implants; ≥1 year potential follow-up
- Exposure: time-updated HbA1c (30-day lag, 90-day carry-forward) modeled continuously (RCS) and categorically: <7.0%, 7.0–<8.0%, ≥8.0%
- Primary outcomes: implant failure (cause-specific Cox), peri-implantitis (Aalen-Johansen)
- Clustered robust SE by patient; surgeon random effects (frailty); competing-risk Fine-Gray models

## Results
**5-Year absolute risks by HbA1c band:**

| HbA1c band | Failure (5-yr) | Peri-implantitis (5-yr) |
|---|---|---|
| <7.0% | 3.2% | 12.1% |
| 7.0–<8.0% | 4.8% | 17.2% |
| ≥8.0% | 8.1% | 26.0% |

- Each 1% HbA1c increment: increased hazard of failure and PI (continuous dose-response)
- HbA1c ≥8.0% vs <7.0%: aHR ≈ 2.0 for both failure and PI
- Spline model: non-linear, significantly steeper gradient above ~8.0%
- All findings consistent in competing-risk and sensitivity analyses

## Related Papers
- [[implants/survival/al-ansari-2022-diabetes-mellitus-dental-implants-sr-ma]] — SR+MA this cohort extends with absolute risk quantification
- [[implants/survival/shahi-2026-implant-outcomes-diabetes-mellitus-sr]] — SR confirming HbA1c >8% threshold across 54 studies
- [[implants/survival/wagner-2022-diabetes-mellitus-dental-implants-sr]] — earlier SR establishing baseline risk estimates
- [[implants/survival/meza-mauricio-2019-diabetes-implant-failure-peri-implant]] — reinforces
- [[drug/systemic-disease/enteghad-2024-diabetes-mellitus-periodontal-periimplant-disease-review]] — mechanistic context
- [[implants/peri-implantitis/sbricoli-2026-peri-implant-disease-prevalence-type2-diabetes]] — prevalence data reinforced
