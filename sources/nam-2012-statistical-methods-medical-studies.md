---
title: "Statistical methods for medical studies (의학논문에 필요한 통계)"
authors: 남정모 (Nam CM), 정수연 (Chung SY)
year: 2012
doi: 10.5124/jkma.2012.55.6.573
category: evidence-appraisal
pdf_path: /Users/oracleneo/llm-wiki/papers/nam-2012-statistical-methods-medical-studies.pdf
pdf_filename: nam-2012-statistical-methods-medical-studies.pdf
source_collection: external
---

## One-line Summary
Korean-language Continuing Education Column (J Korean Med Assoc 2012;55:573-581) by Yonsei biostatistics faculty walking through which statistical test fits which study design — t-test, ANOVA, non-parametric, chi-square, log-rank, multiple/logistic/Cox regression — through hypothetical examples.

## 1. Document Information
- Journal: J Korean Med Assoc 2012 Jun; 55(6): 573-581
- DOI: 10.5124/jkma.2012.55.6.573
- Affiliation: Yonsei University College of Medicine, Departments of Preventive Medicine and Biostatistics
- Open Access (CC-BY-NC)

## 2. Key Contributions
- Provides a test-selection flowchart for clinical researchers: dependent variable scale + sample dependency + number of independent variables → appropriate test.
- Covers the full mainstream parametric/non-parametric toolkit clinicians encounter.
- Distinguishes scenarios where Cox regression (time-to-event), logistic regression (binary outcome), and multiple linear regression (continuous outcome) are correct.

## 3. Methodology and Architecture
- Narrative review structured around hypothetical clinical research scenarios.
- Walks through:
  - Continuous outcomes: paired/unpaired t-test, ANOVA (one-way, repeated measures), non-parametric analogues (Mann-Whitney U, Wilcoxon signed-rank, Kruskal-Wallis).
  - Categorical outcomes: chi-square, Fisher's exact, McNemar.
  - Survival: log-rank test, Cox proportional hazards regression.
  - Multivariable: multiple linear, logistic, mixed model, Cox regression.

## 4. Key Results and Benchmarks
- Educational; no empirical results.
- Provides a decision flowchart that maps study design → appropriate test.

## 5. Limitations and Future Work
- 2012; does not cover Bayesian methods, machine learning, causal inference (DAGs, IPW), or modern multiple comparison procedures.

## 6. Related Work
- Companion methodology paper to Shin WJ 2015 (which focuses on SR/MA pooling rather than per-study tests).

## 7. Glossary
- 비모수 (non-parametric): 분포 가정 없는 검정.
- 로그순위 검정 (log-rank test): 생존 곡선 비교.
- 혼합 모형 (mixed model): 고정·랜덤 효과 결합 회귀.
