---
title: "Common mistakes in biostatistics"
authors: D'Arrigo G, Abd El Hafeez S, Mezzatesta S, Abelardo D, Provenzano FP, Vilasi A, Torino C, Tripepi G
year: 2024
doi: 10.1093/ckj/sfae197
category: evidence-appraisal
pdf_path: /Users/oracleneo/llm-wiki/papers/darrigo-2024-common-mistakes-biostatistics.pdf
pdf_filename: darrigo-2024-common-mistakes-biostatistics.pdf
source_collection: external
---

## Three-line Summary

Narrative review (Clinical Kidney Journal 2024) enumerating 10 frequent biostatistical errors encountered in clinical research: using the wrong descriptive metric, misinterpreting p-values and 95% CIs, treating hazard ratio as a prognostic-accuracy index, ignoring sample-size calculation, abusing subgroup analyses, confusing correlation with causation, confusing confounders with mediators, poor variable coding, and immortal-time bias.

No empirical data; each pitfall is paired with a concrete example and a mitigation rule, providing a practical reference for readers and manuscript reviewers.

The article is nephrology-flavored but the errors described are universal across clinical research, including dental randomized trials and observational studies; over-adjustment bias (controlling for mediators) and immortal-time bias are the two most commonly overlooked issues.

## 세줄요약

서술적 리뷰(Clinical Kidney Journal 2024) — 임상 연구에서 빈번하게 발생하는 10가지 생물통계 오류를 열거: 잘못된 기술 지표·p값·95% CI 오독·위험비(HR)의 예후 정확도 지표 오용·표본 크기 계산 무시·하위군 분석 남용·상관-인과 혼동·교란변수-매개변수 혼동·변수 코딩 오류·미래 노출 기준 편향(Immortal Time Bias).

실증 데이터 없이 각 오류마다 구체적 예시와 해결 원칙을 제시, 원고 작성·심사 시 실무 참고 자료로 활용 가능.

신장학 중심 예시이지만 기술된 오류는 치과 RCT·관찰연구 포함 임상 연구 전반에 적용되며, 과잉조정 편향(Over-adjustment Bias)과 불멸시간 편향이 가장 간과되기 쉬운 항목.

## 1. Document Information
- Journal: Clinical Kidney Journal 2024; 17(7), sfae197
- DOI: 10.1093/ckj/sfae197
- Open Access (CC-BY)
- Authors: CNR-IFC Reggio Calabria and Alexandria University

## 2. Key Contributions
- Concise enumeration of 10 mistakes with practical mitigation strategies.
- Re-states canonical pitfalls in current (2024) terminology and integrates them with modern critiques of NHST (null hypothesis significance testing).

## 3. Methodology and Architecture
The 10 enumerated mistakes:
1. Using the wrong metric to describe data (mean for skewed distribution, etc.).
2. Misinterpreting p-values (treating p>0.05 as evidence of no effect).
3. Misinterpreting 95% CI (treating it as a Bayesian credible interval).
4. Misinterpreting HR as an index of prognostic accuracy (HR is a comparison, not a calibration/discrimination metric).
5. Ignoring sample size calculation (running underpowered studies and over-interpreting null results).
6. Misinterpreting analysis by strata in RCTs (subgroup hunting without adjustment).
7. Confusing correlation and causation.
8. Misunderstanding confounders vs mediators (over-adjustment bias when controlling for mediators).
9. Inadequate codification of variables during data collection (collapsing ordinal into binary too early).
10. Bias when group membership is attributed on the basis of future exposure in retrospective studies (immortal time bias).

## 4. Key Results and Benchmarks
- No empirical results.
- Each pitfall comes with a concrete example and a mitigation rule.

## 5. Limitations and Future Work
- Nephrology-flavored examples; clinicians in other fields must transpose.
- Does not address Bayesian alternatives at depth, nor machine learning–specific pitfalls.

## 6. Related Work
- Modern (2024) consolidation of issues raised in piecemeal form by Flechner 2011 (p/CI), Barraclough 2011 (HR), Monaghan 2021 (OR/RR), and Nam 2012 (test selection).

## 7. Glossary
- Immortal time bias: misclassifying exposure status based on time during which an event cannot occur, biasing exposed group toward better outcomes.
- Over-adjustment bias: controlling for a mediator (which lies on the causal path) attenuates true effect.
- NHST: Null Hypothesis Significance Testing.
