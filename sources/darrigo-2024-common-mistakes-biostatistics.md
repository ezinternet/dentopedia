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

## One-line Summary
CKJ Review (Clin Kidney J 2024;17:sfae197) enumerating 10 frequent biostatistical errors clinicians and authors make — wrong metric, p-value misreading, CI misreading, HR-as-prognostic-accuracy fallacy, ignored sample size calculation, subgroup analysis abuse, correlation-causation confusion, confounder-mediator confusion, poor variable coding, future-exposure bias.

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
