---
title: "Reinterpretation of the results of randomized clinical trials"
authors: Farrokh Habibzadeh
year: 2024
doi: 10.1371/journal.pone.0305575
category: evidence-appraisal
pdf_path: /Users/oracleneo/llm-wiki/papers/habibzadeh-2024-reinterpretation-results-randomized-clinical-trials.pdf
pdf_filename: habibzadeh-2024-reinterpretation-results-randomized-clinical-trials.pdf
source_collection: external
---

## Why Ingested

evidence-appraisal 카테고리가 "p<0.05 = 유의"라는 이분법의 오독을 다루는 문헌([[evidence-appraisal/singh-2026-is-your-research-statistically-significant]], [[evidence-appraisal/darrigo-2024-common-mistakes-biostatistics]], [[evidence-appraisal/flechner-2011-pvalues-confidence-intervals-number-needed]])은 갖고 있지만, "유의수준 문턱 자체를 어디에 둘 것인가"(0.05 vs 0.005 vs 유연 문턱)를 22,500편의 실제 RCT로 정량 검증한 논문은 없었다. 이 논문은 문턱을 낮추면 거짓양성은 줄지만 거짓음성(검정력 저하)이 늘어난다는 trade-off를 수치로 보여, 위키가 보유한 p값 해석 규칙의 배경 근거를 보강한다 (비치과 일반 의학통계 논문이지만 위키가 RCT 결과를 읽는 방식에 직접 적용됨).

## Three-line Summary

Methodological (meta-research) study reanalysing 22,500 RCTs from the Cochrane Database of Systematic Reviews (median n = 82; range 10 to 317,400) under three p value significance thresholds: fixed 0.05, fixed 0.005, and a flexible threshold that minimizes the weighted sum of type I and type II errors.

28.5% of RCTs were significant at p < 0.05, 14.2% at p < 0.005, and only 9.9% under the flexible threshold constrained to alpha <= 0.05 and power >= 80% (about two-thirds of conventionally significant RCTs became non-significant); lowering the threshold lowers false positives but raises false negatives, and in the hypothetical RCT the weighted error at 0.005 exceeded that at 0.05.

The optimal threshold needs the variance of each arm, which is only known a posteriori, so the flexible approach cannot be fixed in advance; the author concludes the frequentist framework has an inherent conflict and argues for Bayesian methods — with the caveat that the work covers only Student's t test and assumes equal variances.

## 세줄요약

방법론적(메타연구) 분석: 코크란 체계적 문헌고찰 데이터베이스 (Cochrane Database of Systematic Reviews, CDSR)의 무작위 대조 임상시험 (Randomized Controlled Trial, RCT) 22,500편(중앙값 n = 82; 범위 10–317,400)을 고정 p값 유의수준 문턱 (p value Significance Threshold, PST) 0.05·0.005와, 유형 I·II 오류의 가중합을 최소화하는 유연 문턱 세 가지로 재해석.

p < 0.05에서 28.5%, p < 0.005에서 14.2%, 유형 I 오류 ≤ 0.05·검정력 ≥ 80% 제약을 건 유연 문턱에서는 9.9%만 유의 (기존 유의 RCT의 약 2/3가 비유의로 전환); 문턱을 낮추면 거짓양성은 줄지만 거짓음성이 늘며, 가상 RCT에서는 0.005의 가중 오류가 0.05보다 오히려 컸다.

최적 문턱은 각 군의 분산(사후에만 알 수 있음)이 필요해 사전에 확정할 수 없으므로 빈도주의 틀 자체에 내재적 모순이 있다고 결론 짓고 베이즈 방법을 제안하나, 한계로 Student t 검정만 다루고 등분산을 가정한 점이 있다.

## 1. Document Information

- **Journal**: PLOS ONE 2024;19(6):e0305575 (published 2024-06-14; received 2024-03-28; accepted 2024-05-23; open access, CC BY)
- **DOI**: 10.1371/journal.pone.0305575
- **Institution**: Global Virus Network, Middle East Region, Shiraz, Iran (single author; no specific funding; no competing interests declared)
- **Data**: public subset of >400,000 CDSR records on the Open Science Framework (DOI 10.17605/OSF.IO/XJV9G); R code in S1 File

## 2. Key Contributions

- Generalizes the author's earlier ROC-analogy method for the "most appropriate" p value significance threshold from a one-tailed to a two-tailed Student's t test, with a cost function eps(t) = C x pr x beta(t) + (1 - pr) x alpha(t).
- Applies three interpretation rules (PST 0.05, PST 0.005, flexible PST) to 22,500 real RCTs, giving an empirical picture of how many "significant" results survive each rule.
- Shows that a stricter fixed threshold (0.005, proposed by Ioannidis and Benjamin) is not generally associated with a lower weighted sum of errors: it raises the false-negative rate (lowers power) and may leave important treatments undiscovered.
- Identifies the structural obstacle: the optimal threshold depends on the variance of each study arm (Eq 5), available only a posteriori, so different replicates of one RCT would yield different optimal thresholds.
- Argues for moving toward Bayesian (or similar) approaches instead of dichotomizing results into "significant"/"not significant".

## 3. Methodology and Architecture

- **Design**: Theoretical/methodological study plus a secondary analysis of an existing data set; no human or animal participants (ethics not applicable).
- **Cost function**: eps(t) = C x pr x beta(t) + (1 - pr) x alpha(t), with alpha(t) = 2 x F(-|t|, nu), beta(t) = F(|t| - delta, nu) - F(-|t| - delta, nu); F = Student's t CDF; delta = effect size rescaled to the t scale (Eq 5; Eq 8 under equal variances).
- **Assumptions**: prior odds of H1:H0 = 1 (prior probability 50%, following Ioannidis and Benjamin); seriousness of type II relative to type I error C = 0.25 (alpha 0.05 vs beta 0.2); minimum acceptable effect size d = 0.5 when total n >= 100, otherwise 0.8; equal variances in both arms (data set had n1, n2 and se of the difference, but no s1, s2).
- **Constrained version (C-PSTopt)**: PSTopt restricted to alpha <= 0.05 and power >= 0.8.
- **Hypothetical RCT**: two parallel arms (n = 100 and 70), Cohen's d = 0.5, variance ratios 0.5/1.0/2.0, prior odds 1.
- **Real RCTs**: CDSR subset filtered with van Zwet et al.'s criteria (single efficacy outcome, dichotomous or continuous; z <= 20 retained), plus n >= 10 per the current study; z replaced by the t distribution (nu = n1 + n2 - 2).
- **Software**: R 4.3.2 (pt, optim L-BFGS-B, irr::kappa2 for Cohen's kappa).

## 4. Key Results and Benchmarks

**Hypothetical RCT** (n = 100 vs 70, d = 0.5, prior odds 1):

| Variance ratio (s2/s1) | Optimal t | PSTopt | Power |
|---|---|---|---|
| 1.0 (equal) | 2.26 | 0.025 | 83% |
| 1.5 | 2.11 | 0.037 | 69% |
| 0.5 | 2.48 | 0.014 | 92% |

At equal variances the weighted error was minimal at PSTopt 0.025 and larger at both 0.05 and 0.005; the error at 0.005 was even higher than at 0.05.

**22,500 real RCTs** (median n = 82; range 10 to 317,400):

| Criterion | Significant RCTs |
|---|---|
| p < 0.05 | 28.5% (n = 6,407) |
| p < 0.005 | 14.2% (n = 3,198) |
| PSTopt (flexible, unconstrained) | 21.8% (n = 4,897) |
| C-PSTopt (alpha <= 0.05, power >= 0.8) | 9.9% (n = 2,237) |
| Max alpha assumed 0.005 | 1.4% |

- PSTopt vs p < 0.05 agreement: Cohen's kappa 0.82; no RCT with p >= 0.05 was significant by PSTopt, and all 4,897 PSTopt-significant RCTs had p < 0.05.
- Median PSTopt among significant RCTs: 3.07 (IQR 1.93 to 3.90) x 10^-2; power of PSTopt-significant RCTs ranged from 9% to near 100% (median 78%; IQR 66% to 88%), i.e. many had unacceptably low power.
- Median C-PSTopt among significant RCTs: 1.91 (IQR 1.27 to 2.44) x 10^-2; power median 88% (IQR 84% to 92%).
- Half of the RCTs significant at 0.05 remained significant at 0.005; 34.9% remained significant under C-PSTopt.
- Table 1 example: for n1 = 100, n2 = 500, C-PSTopt = 10^-2.2 = 0.0063; for 300 per arm, 10^-3.153 = 0.0007; for 50 vs 100, no design can detect d = 0.5 under the constraints.
- Context cited from van Zwet et al.: replication probability of significant RCTs a little over 40%; reported 95% CIs contained the true value about 90% of the time.

## 5. Limitations and Future Work

- Only Student's t test was examined; the optimal threshold would differ by test, even within one study.
- Equal variances were assumed for all 22,500 RCTs because the data set lacked s1 and s2; PSTopt changes materially when variance ratios differ (0.014 to 0.037 in the hypothetical RCT), so the real-RCT estimates are approximate.
- Results depend on the chosen cost function (C = 0.25, prior odds = 1, minimum effect sizes 0.5/0.8); other weights would give other thresholds.
- The author's own conclusion is that the flexible threshold cannot be computed a priori, so it is not a practical replacement for 0.05.
- Future work (stated): general-form derivation and simulation studies of false-positive/false-negative rates under different threshold rules.
- Reader's note: the Bayesian recommendation is asserted in the Discussion; no Bayesian reanalysis of the RCTs is performed.

## 6. Related Work

- [[evidence-appraisal/singh-2026-is-your-research-statistically-significant]]: both warn against reading p < 0.05 alone; Habibzadeh adds a quantitative view of how the threshold choice trades false positives against false negatives.
- [[evidence-appraisal/darrigo-2024-common-mistakes-biostatistics]]: catalogues p-value misreading (p > 0.05 is not "no effect"); consistent with the false-negative cost of lowering the threshold shown here.
- [[evidence-appraisal/flechner-2011-pvalues-confidence-intervals-number-needed]]: p-value, CI and NNT as three lenses; this paper adds that CIs reported in RCTs can under-cover (~90% vs 95%, citing van Zwet).
- van Zwet et al. 2024 (NEJM Evidence): source of the CDSR data set and filtering criteria (not held in the wiki).
- Ioannidis 2018 / Benjamin et al. 2018: proposal to lower the fixed threshold to 0.005 (not held in the wiki).

## 7. Glossary

- **p value Significance Threshold (PST)**: the cut-off below which a p value is called "significant"; conventionally 0.05 (Fisher, 1925).
- **PSTopt / C-PSTopt**: flexible PST minimizing the weighted sum of type I and type II errors; the constrained form (C-PSTopt) additionally requires alpha <= 0.05 and power >= 0.8.
- **Weighted sum of errors**: eps = C x pr x beta + (1 - pr) x alpha; C is the seriousness of a type II error relative to a type I error (0.25 here), pr the prior probability of H1.
- **Prior odds of H1 relative to H0**: pre-study odds that a true effect exists (set to 1 = 50% prior probability).
- **Frequentist vs Bayesian inference**: frequentist uses p values and dichotomous decisions; Bayesian updates the likelihood of a hypothesis in light of the new data.
