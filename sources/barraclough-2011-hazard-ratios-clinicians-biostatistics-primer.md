---
title: "Biostatistics Primer — What a Clinician Ought to Know: Hazard Ratios"
authors: Barraclough H, Simms L, Govindan R
year: 2011
doi: 10.1097/JTO.0b013e31821b10ab
category: evidence-appraisal
pdf_path: /Users/oracleneo/llm-wiki/papers/barraclough-2011-hazard-ratios-clinicians-biostatistics-primer.pdf
pdf_filename: barraclough-2011-hazard-ratios-clinicians-biostatistics-primer.pdf
source_collection: external
---

## One-line Summary
J Thoracic Oncology biostatistics primer (2011) explaining hazard ratio (HR) interpretation in the context of Kaplan-Meier survival analysis, with worked hypothetical RCT examples and warnings against common misreadings.

## 1. Document Information
- Journal: J Thorac Oncol. 2011;6:978–982
- Series: "Biostatistics for Clinicians" primer
- Affiliations: Eli Lilly / Washington University, St. Louis

## 2. Key Contributions
- Defines HR as the ratio of instantaneous event rates between two groups across the entire follow-up — not a percentage reduction at a single time point.
- Distinguishes HR from relative risk (HR uses censored time-to-event data; RR uses cumulative incidence).
- States the proportional hazards assumption explicitly and explains why violation makes HR uninterpretable.

## 3. Methodology and Architecture
- Narrative + hypothetical-RCT walkthrough.
- Uses a two-arm OS example (control vs experimental) with weekly event rates to show how HR is computed and how censoring is handled.
- Explains Kaplan-Meier (KM) curve steps, censoring marks, and median survival.

## 4. Key Results and Benchmarks
- No empirical results.
- Key takeaway: HR=0.5 does not mean "patients live twice as long" — it means the experimental group has half the hazard rate at any moment relative to the control, averaged across follow-up under the proportional hazards assumption.

## 5. Limitations and Future Work
- Pre-immunotherapy era (PH violations are common with checkpoint inhibitors).
- Does not cover restricted mean survival time (RMST), milestone survival, or modern alternatives to HR when PH fails.

## 6. Related Work
- D'Arrigo 2024 explicitly lists "misinterpreting hazard ratio as a prognostic accuracy index" as one of the top 10 biostatistics mistakes — direct conceptual continuation.

## 7. Glossary
- HR: Hazard Ratio — ratio of event hazards between groups.
- KM curve: Kaplan-Meier survival curve.
- Censoring: event status unknown at end of observation.
- PH assumption: Proportional Hazards — HR is constant over time.
