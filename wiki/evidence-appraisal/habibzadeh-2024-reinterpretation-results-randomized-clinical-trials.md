---
title: "Reinterpretation of the results of randomized clinical trials"
authors: Farrokh Habibzadeh
year: 2024
date: 2024-06-14
doi: 10.1371/journal.pone.0305575
source: habibzadeh-2024-reinterpretation-results-randomized-clinical-trials.md
category: evidence-appraisal
evidence_level: cross-sectional
pdf_path: /Users/oracleneo/llm-wiki/papers/habibzadeh-2024-reinterpretation-results-randomized-clinical-trials.pdf
pdf_filename: habibzadeh-2024-reinterpretation-results-randomized-clinical-trials.pdf
source_collection: external
tags: [p-value, significance-threshold, false-positive, false-negative, statistical-power, rct, meta-research, frequentist, bayesian, cochrane, evidence-appraisal]
relations:
  - type: extends
    target: singh-2026-is-your-research-statistically-significant
  - type: reinforces
    target: darrigo-2024-common-mistakes-biostatistics
---

## Three-line Summary

Methodological (meta-research) study reanalysing 22,500 RCTs from the Cochrane Database of Systematic Reviews (median n = 82; range 10 to 317,400) under three p value significance thresholds: fixed 0.05, fixed 0.005, and a flexible threshold that minimizes the weighted sum of type I and type II errors.

28.5% of RCTs were significant at p < 0.05, 14.2% at p < 0.005, and only 9.9% under the flexible threshold constrained to alpha <= 0.05 and power >= 80% (about two-thirds of conventionally significant RCTs became non-significant); lowering the threshold lowers false positives but raises false negatives, and in the hypothetical RCT the weighted error at 0.005 exceeded that at 0.05.

The optimal threshold needs the variance of each arm, which is only known a posteriori, so the flexible approach cannot be fixed in advance; the author concludes the frequentist framework has an inherent conflict and argues for Bayesian methods — with the caveat that the work covers only Student's t test and assumes equal variances.

## 세줄요약

방법론적(메타연구) 분석: 코크란 체계적 문헌고찰 데이터베이스 (Cochrane Database of Systematic Reviews, CDSR)의 무작위 대조 임상시험 (Randomized Controlled Trial, RCT) 22,500편(중앙값 n = 82; 범위 10–317,400)을 고정 p값 유의수준 문턱 (p value Significance Threshold, PST) 0.05·0.005와, 유형 I·II 오류의 가중합을 최소화하는 유연 문턱 세 가지로 재해석.

p < 0.05에서 28.5%, p < 0.005에서 14.2%, 유형 I 오류 ≤ 0.05·검정력 ≥ 80% 제약을 건 유연 문턱에서는 9.9%만 유의 (기존 유의 RCT의 약 2/3가 비유의로 전환); 문턱을 낮추면 거짓양성은 줄지만 거짓음성이 늘며, 가상 RCT에서는 0.005의 가중 오류가 0.05보다 오히려 컸다.

최적 문턱은 각 군의 분산(사후에만 알 수 있음)이 필요해 사전에 확정할 수 없으므로 빈도주의 틀 자체에 내재적 모순이 있다고 결론 짓고 베이즈 방법을 제안하나, 한계로 Student t 검정만 다루고 등분산을 가정한 점이 있다.

## Summary

This single-author methodological study (PLOS ONE 2024) generalizes a previously proposed ROC-analogy method for choosing a p value significance threshold (PST) to a two-tailed Student's t test, then applies it to 22,500 efficacy RCTs drawn from the Cochrane Database of Systematic Reviews. Reinterpreting the same trials under a fixed 0.05, a fixed 0.005, and a flexible threshold that minimizes the weighted sum of type I and type II errors, the proportion of "significant" trials falls from 28.5% to 14.2% to 9.9% (the last with alpha <= 0.05 and power >= 80% imposed). Lowering the fixed threshold decreases false positives but raises the false-negative rate, so it is not generally associated with a lower weighted error. Because the optimal threshold depends on arm-specific variances available only after the trial, the author concludes that the frequentist framework has an inherent conflict and that Bayesian methods would be more appropriate for RCT analysis. Evidence is theoretical and secondary-analytic; it is not dental-specific, and it supports how the wiki's other p-value pages should be read (a p value near a threshold is weak, arbitrary-cut-off evidence, and "not significant" may reflect low power).

## Key Contributions

- Extends the author's earlier one-tailed derivation to a two-tailed Student's t test with the cost function eps(t) = C x pr x beta(t) + (1 - pr) x alpha(t).
- Empirical anchor: 22,500 real RCTs show how many "significant" results survive each threshold rule (28.5% / 14.2% / 21.8% unconstrained flexible / 9.9% constrained flexible).
- Demonstrates the trade-off: lowering the fixed threshold to 0.005 is not necessarily better — in the hypothetical RCT its weighted error exceeds that of 0.05.
- Shows that the flexible optimum cannot be fixed a priori (needs arm variances, known a posteriori), so replicates of one RCT would yield different thresholds.
- Calls for Bayesian or similar approaches rather than dichotomizing results.

## Methodology

- **Design**: theoretical derivation plus secondary analysis of a public Open Science Framework subset of the CDSR (van Zwet et al. filtering: single efficacy outcome, continuous or dichotomous; z <= 20; n >= 10 per this study). No participants; ethics not applicable.
- **Assumptions**: prior odds of H1:H0 = 1; type II relative to type I seriousness C = 0.25; minimum effect size d = 0.5 (total n >= 100) or 0.8 (otherwise); equal variances (the data set lacked group SDs).
- **Hypothetical RCT**: arms of 100 and 70, d = 0.5, variance ratios 0.5/1.0/2.0.
- **Software**: R 4.3.2 (pt, optim L-BFGS-B, irr::kappa2).

## Results

| Criterion | Significant RCTs (of 22,500) |
|---|---|
| p < 0.05 | 28.5% (n = 6,407) |
| p < 0.005 | 14.2% (n = 3,198) |
| PSTopt (flexible, unconstrained) | 21.8% (n = 4,897) |
| C-PSTopt (alpha <= 0.05, power >= 0.8) | 9.9% (n = 2,237) |
| Max alpha assumed 0.005 | 1.4% |

| Hypothetical RCT (n = 100 vs 70, d = 0.5) | Optimal t | PSTopt | Power |
|---|---|---|---|
| Equal variances | 2.26 | 0.025 | 83% |
| Variance ratio 1.5 | 2.11 | 0.037 | 69% |
| Variance ratio 0.5 | 2.48 | 0.014 | 92% |

- Agreement of PSTopt with p < 0.05: Cohen's kappa 0.82; no RCT with p >= 0.05 became significant under PSTopt.
- PSTopt-significant RCTs had power from 9% to near 100% (median 78%; IQR 66% to 88%); under C-PSTopt the median power was 88% (IQR 84% to 92%).
- Half of the RCTs significant at 0.05 stayed significant at 0.005; 34.9% stayed significant under C-PSTopt.
- Limitations stated by the author: only the t test was studied; equal variances assumed for all real RCTs; results depend on the chosen cost function and weights.

## Related Papers

- [[evidence-appraisal/singh-2026-is-your-research-statistically-significant]] — extends: Singh argues significance and clinical relevance diverge; this paper quantifies how the choice of threshold shifts the false-positive/false-negative balance across 22,500 RCTs.
- [[evidence-appraisal/darrigo-2024-common-mistakes-biostatistics]] — reinforces: both caution against reading p > 0.05 as "no effect"; here lowering the threshold is shown to increase the false-negative rate.
- [[evidence-appraisal/flechner-2011-pvalues-confidence-intervals-number-needed]] — background: p-value, CI and NNT as complementary lenses; this paper adds that reported 95% CIs in RCTs cover the true value only about 90% of the time (citing van Zwet et al.).
- [[overviews/evidence-appraisal-toolkit]] — hub: situates this paper as a threshold-choice caveat to the toolkit's p-value reading rules.
