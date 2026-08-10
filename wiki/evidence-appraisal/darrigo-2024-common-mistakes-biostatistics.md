---
title: "Common mistakes in biostatistics"
authors: D'Arrigo G, Abd El Hafeez S, Mezzatesta S, Abelardo D, Provenzano FP, Vilasi A, Torino C, Tripepi G
year: 2024
date: 2024-06-26
doi: 10.1093/ckj/sfae197
source: darrigo-2024-common-mistakes-biostatistics.md
category: evidence-appraisal
evidence_level: narrative-review
pdf_path: /Users/oracleneo/llm-wiki/papers/darrigo-2024-common-mistakes-biostatistics.pdf
pdf_filename: darrigo-2024-common-mistakes-biostatistics.pdf
source_collection: external
tags: [biostatistics, common-mistakes, p-value, hazard-ratio, confounding, mediator, immortal-time-bias, critical-appraisal]
---

## Three-line Summary

Narrative review (Clinical Kidney Journal 2024) cataloguing 10 common biostatistics mistakes in clinical research: wrong descriptive metric (mean±SD for skewed data), p-value misreading (p>0.05 ≠ no effect), 95% CI misinterpretation (frequentist coverage, not probability), HR as prognostic accuracy, ignored sample-size calculation, subgroup-analysis multiplicity, correlation-causation conflation, confounder vs mediator over-adjustment, poor variable coding (premature dichotomization), and immortal-time/future-exposure bias.

Worked nephrology examples are directly transferable to dental retrospective studies: immortal-time bias in early-vs-late loading classification; subgroup claims in SR+MAs are hypothesis-generating only unless pre-specified; adjusting for plaque level as a mediator on the smoking→bone-loss pathway underestimates the true smoking effect.

This is the single most comprehensive error-catalogue in the wiki's evidence-appraisal toolkit — read after at least one of Flechner 2011, Barraclough 2011, or Shin WJ 2015 to appreciate each mistake's contextual depth.

## 세줄요약

Narrative review (Clin Kidney J 2024): 임상연구의 흔한 생통계 오류 10가지 목록 — 잘못된 기술통계 지표·p값 오독(p>0.05 ≠ 효과 없음)·95% CI 오해(빈도론적 포함 진술)·HR을 예후 정확도로 혼동·표본수 계산 무시·subgroup 다중검정·상관-인과 혼동·confounder-mediator 과보정·변수 이분화 손실·immortal time bias.

신장학 예시는 치과 후향 연구에 직접 이전 가능: 조기/지연 로딩 분류의 immortal time bias; SR+MA subgroup 주장은 사전 명시 없으면 가설 생성용; 흡연→골소실 경로에서 치태수준을 mediator로 보정 시 진짜 흡연 효과 과소추정.

위키 증거평가 툴킷의 가장 포괄적인 오류 목록으로, Flechner 2011·Barraclough 2011·Shin WJ 2015 중 최소 한 편 선독 후 읽으면 각 오류의 맥락적 깊이를 이해하는 데 최적.

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
