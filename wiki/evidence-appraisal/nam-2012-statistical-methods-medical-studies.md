---
title: "Statistical methods for medical studies (의학논문에 필요한 통계)"
authors: 남정모 (Nam CM), 정수연 (Chung SY)
year: 2012
date: 2012-06-01
doi: 10.5124/jkma.2012.55.6.573
source: nam-2012-statistical-methods-medical-studies.md
category: evidence-appraisal
confidence: narrative-review
pdf_path: /Users/oracleneo/llm-wiki/papers/nam-2012-statistical-methods-medical-studies.pdf
pdf_filename: nam-2012-statistical-methods-medical-studies.pdf
source_collection: external
tags: [statistical-test-selection, t-test, anova, regression, cox-regression, korean, biostatistics]
---

## Three-line Summary

Korean-language statistical test-selection guide (J Korean Med Assoc 2012, Yonsei Preventive Medicine and Biostatistics) presenting a "which test do I use?" flowchart driven by three decision axes: measurement scale of the dependent variable, sample dependency (paired vs independent), and number of independent variables.

Covers the canonical clinician toolkit: t-test/ANOVA families with non-parametric analogues (Wilcoxon, Mann-Whitney, Kruskal-Wallis), chi-square family, survival analysis (log-rank test, Cox proportional-hazards), and multivariable regression (linear, logistic, mixed, Cox) — each illustrated with hypothetical clinical scenarios.

A paired comparison reported with an unpaired t-test, or a survival outcome analyzed with chi-square, is a methodology red flag detectable by this flowchart; the 2012 date means it predates the modern emphasis on effect sizes, confidence intervals, and causal inference frameworks (DAGs, propensity scores).

## 세줄요약

한국어 통계검정 선택 가이드 (JKMA 2012, 연세의대 남정모·정수연): 종속변수 측정 척도·표본 의존성(대응/독립)·독립변수 수라는 세 결정 축의 flowchart로 어떤 검정을 써야 하는지 안내.

임상의 핵심 도구 모음 망라: t-test/ANOVA 계열 + 비모수 대응(Wilcoxon·Mann-Whitney·Kruskal-Wallis)·카이제곱 계열·생존분석(log-rank·Cox 비례위험)·다변량 회귀(선형·로지스틱·혼합·Cox) — 각 시나리오 예시 포함.

대응 비교를 독립표본 t-test로 분석하거나 생존 결과를 카이제곱으로 처리하는 방법론 적신호를 이 flowchart로 감지 가능; 2012년 기준이라 효과크기·신뢰구간 우선 및 인과추론 프레임워크(DAG·성향점수) 이전임.



## Summary
The "which test do I use?" reference for clinicians who didn't take graduate-level biostatistics. Bridges the gap between Flechner/Monaghan (what does this number mean?) and Shin WJ 2015 (how do I pool across studies?).

## Key Contributions
- Operationalizes test selection as a flowchart driven by: (a) measurement scale of dependent variable, (b) sample dependency (paired vs independent), (c) number of independent variables.
- Covers the canonical clinician toolkit: t-test family, ANOVA family, non-parametric analogues, chi-square family, survival (log-rank, Cox), multivariable regression (linear, logistic, mixed, Cox).

## Methodology
- Narrative with hypothetical clinical scenarios. No new statistical theory.

## Results
No original results.

## Clinical Applicability
- When auditing a dental RCT or retrospective study before quoting its conclusions, check the test choice against Nam 2012's flowchart. A paired comparison reported with an unpaired t-test, or a survival outcome analyzed with chi-square, is a methodology red flag.
- For our own retrospective chart reviews in the clinic: this paper is the quick reference for picking the right test before running the analysis.

## Caveats
- 2012 — predates the modern emphasis on confidence intervals over p-values, effect sizes alongside test statistics, and causal inference frameworks (DAGs, propensity scores, IPW).
- Does not cover Bayesian methods or post-2015 statistical reform recommendations.

## Related Papers
- [[evidence-appraisal/shin-wj-2015-systematic-review-meta-analysis-introduction]] — 같은 한국어 방법론, SR/MA 편.
- [[evidence-appraisal/flechner-2011-pvalues-confidence-intervals-number-needed]] — 검정 결과 해석.
- [[evidence-appraisal/darrigo-2024-common-mistakes-biostatistics]] — 검정 선택·해석 흔한 오류.
- [[overviews/evidence-appraisal-toolkit]] — 9편 종합.
