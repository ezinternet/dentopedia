---
title: "Common mistakes in biostatistics"
authors: D'Arrigo G, Abd El Hafeez S, Mezzatesta S, Abelardo D, Provenzano FP, Vilasi A, Torino C, Tripepi G
year: 2024
date: 2024-06-26
doi: 10.1093/ckj/sfae197
source: darrigo-2024-common-mistakes-biostatistics.md
category: evidence-appraisal
confidence: narrative-review
pdf_path: /Users/oracleneo/llm-wiki/papers/darrigo-2024-common-mistakes-biostatistics.pdf
pdf_filename: darrigo-2024-common-mistakes-biostatistics.pdf
source_collection: external
tags: [biostatistics, common-mistakes, p-value, hazard-ratio, confounding, mediator, immortal-time-bias, critical-appraisal]
---

## 한줄요약
임상 통계 흔한 오류 10가지 정리 (Clin Kidney J 2024): 잘못된 지표 선택·p값 오해·95% CI 오해·HR을 예후 정확도로 오해·표본수 무시·subgroup 사냥·상관-인과 혼동·confounder-mediator 혼동·변수 코딩 불량·미래 노출 기반 분류 편향(immortal time bias).

## Summary
The 2024 consolidation paper that ties together every mistake the other 8 papers in this category warn against. If you read only one paper from `evidence-appraisal/`, this is it — but you'll appreciate it more after reading at least one of Flechner 2011, Barraclough 2011, Monaghan 2021, or Shin WJ 2015 first.

## Key Contributions
The 10 mistakes (paraphrased):
- **Wrong descriptive metric** — mean ± SD for skewed data is misleading; use median (IQR).
- **p-value misreading** — p > 0.05 ≠ "no effect"; absence of evidence ≠ evidence of absence.
- **95% CI misreading** — frequentist coverage statement, not a probability statement about the parameter.
- **HR as prognostic accuracy** — HR compares groups; it says nothing about how well a model predicts which patient will fail.
- **Ignored sample size calculation** — underpowered studies generate inflated effect sizes in significant results (winner's curse).
- **Subgroup analysis abuse** — multiplicity inflates false positives; pre-specification and interaction tests required.
- **Correlation ≠ causation** — needs DAG, temporality, dose-response, plausibility.
- **Confounder vs mediator** — adjusting for a mediator biases the total effect toward null (over-adjustment).
- **Poor variable coding** — premature dichotomization loses information and power.
- **Future-exposure bias / immortal time bias** — classifying based on what happens later in follow-up biases toward exposed group.

## Methodology
Narrative review with worked examples. Nephrology-flavored but framework is universal.

## Results
No empirical results.

## Clinical Applicability
- **For dental implant retrospective studies:** immortal time bias is common. Example: classifying patients as "loaded early" vs "loaded late" based on when loading actually occurred — patients who failed before they could be loaded get misclassified.
- **For subgroup claims in dental SR+MAs:** treat any "but in subgroup X the effect was significant" as hypothesis-generating, not confirmatory, unless pre-specified.
- **For HR in implant survival studies:** never present HR alone as "this implant is better" — pair with absolute risk at clinically meaningful horizon.
- **For peri-implantitis risk-factor papers:** if the paper "adjusts for" an intermediate variable that lies between exposure (e.g., smoking) and outcome (e.g., bone loss), like "plaque level," that's over-adjustment — the resulting effect estimate underestimates the true smoking effect.

## Caveats
- Frequentist NHST framework; does not cover Bayesian alternatives in depth.
- Nephrology examples; some readers will need to transpose to dentistry.

## Related Papers
- [[evidence-appraisal/flechner-2011-pvalues-confidence-intervals-number-needed]] — p-value/CI 오해의 선행 정리.
- [[evidence-appraisal/barraclough-2011-hazard-ratios-clinicians-biostatistics-primer]] — HR 오해의 선행 정리.
- [[evidence-appraisal/monaghan-2021-odds-ratios-relative-risk-absolute]] — OR/RR/AR/NNT 정확한 해석.
- [[evidence-appraisal/nam-2012-statistical-methods-medical-studies]] — 검정 선택.
- [[evidence-appraisal/shin-wj-2015-systematic-review-meta-analysis-introduction]] — SR/MA 방법론.
- [[overviews/evidence-appraisal-toolkit]] — 9편 종합 (이 페이지가 최신·요약 역할).
