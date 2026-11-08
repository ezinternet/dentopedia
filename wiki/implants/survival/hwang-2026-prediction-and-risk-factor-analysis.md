---
title: "Prediction and risk factor analysis of dental implant failure using Cox regression and machine learning"
authors: Hwang IK, Ahn SH, Kim SK, Kim TI
year: 2026
date: 2026-02-28
doi: 10.1002/jper.70112
journal: "Journal of periodontology"
source: hwang-2026-prediction-and-risk-factor-analysis.md
category: [implants/survival]
evidence_level: retrospective
source_collection: pubmed-text
full_text: false
pmid: "41761925"
pmcid: "PMC13502411"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13502411/
text_path: /Users/oracleneo/llm-wiki/papers/hwang-2026-prediction-and-risk-factor-analysis.txt
text_filename: hwang-2026-prediction-and-risk-factor-analysis.txt
tags: [implant-survival, cox-regression, machine-learning, random-survival-forest, risk-factors, periodontitis, anterior-placement, disability]
relations:
  - type: reinforces
    target: implants/survival/serroni-2024-history-of-periodontitis-as
---

abstract-only — full text not retrieved

## Three-line Summary

Retrospective review of 543 implants in 256 patients (32 failures, mean follow-up 8.0 ± 2.5 years) comparing Cox regression with a patient-level frailty term against Random Survival Forest (RSF), DeepSurv and TabNet for implant failure prediction.

The best Cox model reached a C-index of 0.81 but limited AUC; RSF was the best machine-learning model (C-index 0.72, AUC 0.79, Integrated Brier Score 0.044); both Cox and RSF identified anterior placement and periodontitis-related tooth loss as the main risk factors.

Machine learning did not outperform the best Cox model in this low-event dataset; choose the analytical method by sample size and event rate, and treat anterior sites and replacement of periodontitis-related tooth loss as higher-risk situations.

## 세줄요약

후향적 검토: 환자 256명의 임플란트 543개(실패 32개, 평균 추적 8.0 ± 2.5년) — 환자 단위 취약성 항 Cox 회귀와 랜덤 생존 포레스트 (Random Survival Forest, RSF)·DeepSurv·TabNet의 임플란트 실패 예측 비교.

최적 Cox 모델 C-index 0.81(AUC는 제한적); 기계학습 중 RSF 최고(C-index 0.72, AUC 0.79, Integrated Brier Score 0.044); Cox와 RSF 모두 전방부 식립과 치주염 관련 치아 상실 대체를 주요 위험요인으로 확인.

사건 수가 적은 데이터에서 기계학습은 최적 Cox 모델을 능가하지 못함 — 표본 크기와 사건 발생률로 분석법을 선택하고, 전방부 및 치주염 관련 상실 치아 대체 부위를 고위험으로 인식할 것.

## Summary

Cohort of 543 implants placed in 256 patients (described as patients with disabilities), with 32 failures over a mean follow-up of 8.0 ± 2.5 years, reviewed from clinical records. Cox models with a patient-level frailty term were chosen by exhaustive subset search and compared with RSF, DeepSurv and TabNet, each tuned with 50 Optuna Bayesian trials and refitted on a 90% training split, then tested on the remaining 10%. Importance was read from hazard ratios (Cox) and SHAP values (machine learning).

## Key Contributions

- Direct Cox versus machine-learning comparison on one implant survival dataset.
- Evidence that machine-learning survival models are not inherently superior when events are few.
- Concordant risk factors across methods: anterior placement and replacement of periodontitis-related tooth loss.

## Methodology

Retrospective clinical-record review; Cox with frailty and exhaustive subset search; RSF, DeepSurv, TabNet tuned by Optuna (50 trials); 90/10 train-test split; hazard ratios and SHAP for variable importance. The abstract does not report the institution, failure definition, covariate list or hazard ratio values.

## Results

- Best Cox model: C-index 0.81, limited AUC.
- RSF: C-index 0.72, AUC 0.79, Integrated Brier Score 0.044, better than DeepSurv and TabNet on all metrics.
- RSF good but not superior to the best Cox model.
- Top risk factors in both Cox and RSF: anterior placement and periodontitis-related tooth loss.

## Limitations

- Abstract-only: no hazard ratios, CIs, covariates or failure definition available.
- Retrospective design; only 32 events, which constrains machine-learning training.
- Evaluation on a 10% hold-out gives imprecise test metrics; no external validation reported.
- Disability population may limit generalisability.

## Clinical Implication (Korean Practice)

For Korean implant practice, anterior sites and sites replacing teeth lost to periodontitis warrant closer follow-up and periodontal maintenance. The study does not support replacing conventional Cox-based risk analysis with machine learning in small, low-event clinic datasets.

## Related Papers

- [[implants/survival/serroni-2024-history-of-periodontitis-as]] — periodontitis history and implant failure.
- [[implants/survival/alrowis-2025-factors-affecting-dental-implant-failure-retrospective]] — retrospective failure factors.
- [[implants/survival/larsson-2023-risk-factors-associated-with-failure]] — risk factors for failure.
- [[implants/survival/marty-2024-implant-treated-periodontitis-sr-ma]] — implants in periodontitis-treated patients.
