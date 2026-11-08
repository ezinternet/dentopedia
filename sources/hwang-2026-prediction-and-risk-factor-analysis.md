---
title: "Prediction and Risk Factor Analysis of Dental Implant Failure Using Cox Regression and Machine Learning"
authors: Hwang IK, Ahn SH, Kim SK, Kim TI
year: 2026
doi: 10.1002/jper.70112
category: [implants/survival]
source_collection: pubmed-text
full_text: false
pmid: "41761925"
pmcid: "PMC13502411"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13502411/
text_path: /Users/oracleneo/llm-wiki/papers/hwang-2026-prediction-and-risk-factor-analysis.txt
text_filename: hwang-2026-prediction-and-risk-factor-analysis.txt
---

abstract-only — full text not retrieved

## Why Ingested

Adds a long-term (mean 8.0 years) implant-level survival cohort that compares conventional Cox regression with machine-learning survival models, a methodological angle absent from the survival folder. Its risk-factor findings (anterior placement, replacement of periodontitis-related tooth loss) reinforce the periodontitis-history evidence in [[implants/survival/serroni-2024-history-of-periodontitis-as]] and complement the retrospective failure-factor analysis in [[implants/survival/alrowis-2025-factors-affecting-dental-implant-failure-retrospective]]. → [[implants/survival/hwang-2026-prediction-and-risk-factor-analysis]]

## Three-line Summary

Retrospective clinical-record review of 543 implants in 256 patients (32 failures, mean follow-up 8.0 ± 2.5 years) comparing Cox regression with a patient-level frailty term against Random Survival Forest (RSF), DeepSurv and TabNet for predicting implant failure — abstract-only ingest.

The best Cox model reached a C-index of 0.81 but limited AUC; RSF was the best machine-learning model (C-index 0.72, AUC 0.79, Integrated Brier Score 0.044), outperforming DeepSurv and TabNet; both Cox and RSF identified anterior placement and periodontitis-related tooth loss as the main risk factors.

RSF was good but not superior to the best Cox model; with few events, analytical method choice should weigh model complexity against sample size and event rate rather than algorithm novelty.

## 세줄요약

후향적 진료기록 검토: 환자 256명의 임플란트 543개(실패 32개, 평균 추적 8.0 ± 2.5년) — 환자 단위 취약성(frailty) 항을 넣은 Cox 회귀와 랜덤 생존 포레스트 (Random Survival Forest, RSF)·DeepSurv·TabNet의 임플란트 실패 예측 성능 비교 (초록만 수집).

최적 Cox 모델 C-index 0.81(단, AUC 제한적); 기계학습 중 RSF 최고(C-index 0.72, AUC 0.79, Integrated Brier Score 0.044)로 DeepSurv·TabNet 능가; Cox와 RSF 모두 전방부 식립과 치주염 관련 치아 상실 대체를 주요 위험요인으로 확인.

RSF는 양호하나 최적 Cox 모델보다 우수하지 않음 — 사건 수가 적은 데이터에서는 알고리즘의 새로움보다 표본 크기와 사건 발생률에 맞춰 분석법을 선택해야 함.

## 1. Document Information

- **Type**: Retrospective cohort (clinical record review) with survival modelling comparison. [ABSTRACT-ONLY — full text not retrieved]
- **Journal**: Journal of Periodontology 2026
- **PMID**: 41761925 · **PMCID**: PMC13502411 · **DOI**: [10.1002/jper.70112](https://doi.org/10.1002/jper.70112)
- **Population**: 256 patients with disabilities (per the lay summary), 543 implants. The institution is not named in the retrieved text.

## 2. Key Contributions

- Head-to-head comparison of Cox regression (with patient-level frailty) and three machine-learning survival models (RSF, DeepSurv, TabNet) on the same implant dataset.
- Shows that newer machine-learning tools did not inherently outperform the best-adjusted Cox model in a low-event dataset.
- Cross-method agreement on the leading risk factors: anterior placement and replacement of periodontitis-related tooth loss.

## 3. Methodology and Architecture

- Clinical records of 543 implants placed in 256 patients; 32 failures; mean follow-up 8.0 ± 2.5 years.
- Cox models with a patient-level frailty term, selected by an exhaustive subset search.
- RSF, DeepSurv and TabNet tuned with 50 Optuna Bayesian trials; best settings refitted on a 90% training split and evaluated on the remaining 10%.
- Variable importance: hazard ratios for Cox; Shapley Additive Explanations (SHAP) for the machine-learning models.
- The abstract does not state the survival (failure) definition, covariate list or hazard ratio values.

## 4. Key Results and Benchmarks

| Model | C-index | AUC | Integrated Brier Score |
|---|---|---|---|
| Best Cox (frailty) | 0.81 | limited (value not reported in abstract) | not reported |
| RSF | 0.72 | 0.79 | 0.044 |
| DeepSurv, TabNet | lower than RSF on all metrics | | |

- Both Cox and RSF ranked anterior placement and periodontitis-related tooth loss as the primary risk factors.
- RSF showed good, but not superior, accuracy compared with the best Cox model.

## 5. Limitations and Future Work

- Abstract-only ingest: hazard ratios, covariates, failure definition and confidence intervals not available.
- Retrospective record review; 32 events across 543 implants is a low event count for machine-learning training.
- Held-out evaluation used only 10% of the data, so test-set metrics are likely imprecise.
- Population consists of patients with disabilities, which may limit generalisability.
- Authors conclude method choice should depend on dataset size and event rate.

## 6. Related Work

- [[implants/survival/serroni-2024-history-of-periodontitis-as]] — periodontitis history as a failure risk factor.
- [[implants/survival/alrowis-2025-factors-affecting-dental-implant-failure-retrospective]] — retrospective failure-factor analysis.
- [[implants/survival/larsson-2023-risk-factors-associated-with-failure]] — risk factors for implant failure.

## 7. Glossary

- **C-index**: concordance index; probability that the model ranks a pair of implants' failure times correctly.
- **RSF**: Random Survival Forest, a tree-ensemble survival model.
- **SHAP**: Shapley Additive Explanations, a model-agnostic variable importance method.
- **Frailty term**: random effect accounting for clustering of implants within a patient.
