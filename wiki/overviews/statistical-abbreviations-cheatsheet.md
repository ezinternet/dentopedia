---
title: "Statistical Abbreviations Cheatsheet for Dental Literature"
authors: Synthesis page (no single source)
year: 2026
date: 2026-05-23
doi: null
source: null
category: evidence-appraisal
confidence: synthesis
pdf_path: null
pdf_filename: null
source_collection: internal
tags: [statistics, cheatsheet, abbreviations, biostatistics, critical-appraisal, p-value, confidence-interval, effect-size, meta-analysis, survival-analysis, diagnostic-accuracy]
---

## 한줄요약
치과 논문에서 자주 만나는 통계 약자(descriptive·inferential·effect size·diagnostic·meta-analysis·regression·survival·agreement·trial set)를 카테고리별로 정리하고, 임상 해석에서 가장 자주 오용되는 5개 패턴(OR↔RR 혼동, p<0.05=임상유의 오역, CI 폭 무시, SD↔SE 혼동, ITT↔PP 차이 무시)을 신호로 표시.

## Summary
Reference cheatsheet for interpreting statistical reporting in dental research papers. Organized by analytical context: descriptive, inferential, effect size, diagnostic accuracy, meta-analysis, regression, survival analysis, reliability/agreement, and clinical trial analysis sets. Each entry pairs the standard definition with the most common misinterpretation observed in dental literature.

This is a synthesis page and is not derived from a single source paper; definitions are drawn from standard biostatistics references and cross-checked against the methodology papers already in `evidence-appraisal/`. For the underlying methods, Nam 2012 surveys the statistical methods used across medical studies, and Kiriakou 2014 frames the critical-appraisal skills an evidence-based-dentistry reader needs to interpret these abbreviations correctly rather than mechanically.

## 1. Descriptive Statistics

| Abbr | Term | Notes |
|---|---|---|
| **M** | Mean | Pulled by outliers in skewed distributions; compare to Median |
| **SD** | Standard Deviation | Spread of individual data; in normal distribution, M±1SD ≈ 68%, ±2SD ≈ 95% |
| **SE** | Standard Error (= SD/√n) | Precision of the mean estimate; **SE shrinks with n, SD does not** |
| **CI** | Confidence Interval (usually 95%) | "If sampling were repeated infinitely, 95% of CIs would contain the true value" — **not** "95% probability the true value lies in this interval" |
| **IQR** | Interquartile Range (Q1–Q3) | Used instead of SD for non-normal distributions |

**Trap.** Papers sometimes report error bars as SE while readers assume SD, making the apparent spread look smaller than it is. Always check the figure caption.

## 2. Inferential Statistics

| Abbr | Term | Notes |
|---|---|---|
| **p** | p-value | Probability of observing data this extreme **under the null hypothesis**; not "probability the null is true" |
| **α** | Type I error rate | Conventionally 0.05; adjust for multiple comparisons (Bonferroni, Holm, FDR) |
| **β** | Type II error rate | Conventionally 0.20 |
| **Power** | 1 − β | Conventionally 0.80; underpowered negative studies cannot conclude "no effect" |

**Trap.** With large n, clinically meaningless differences (e.g., 0.1 mm MBL difference) can reach p < 0.001. Always read effect size + CI alongside p. Flechner 2011 walks through why a p-value alone, without the confidence interval and NNT, under-informs a clinical decision — the same triad (p + CI + NNT) should be demanded of every comparative result.

## 3. Effect Size — Most Important for Clinical Interpretation

| Abbr | Term | Notes |
|---|---|---|
| **OR** | Odds Ratio | Case-control studies, logistic regression. **Approximates RR only when outcome is rare (<10%); overstates risk for common outcomes** (e.g., peri-implant mucositis ~43%) |
| **RR** | Risk Ratio / Relative Risk | Cohort, RCT; intuitive interpretation |
| **HR** | Hazard Ratio | Survival analysis (implant survival, peri-implantitis-free survival); requires proportional hazards assumption |
| **RD / ARR** | Risk Difference / Absolute Risk Reduction | Basis for NNT |
| **NNT** | Number Needed to Treat (= 1/ARR) | NNT inflates when baseline risk is low |
| **NNH** | Number Needed to Harm | Same logic for adverse outcomes |
| **MD** | Mean Difference | Continuous outcome, same units |
| **SMD** | Standardized Mean Difference | Pools studies with different units (meta-analysis); Cohen's d: 0.2 / 0.5 / 0.8 ≈ small / medium / large |

See [[evidence-appraisal/monaghan-2021-odds-ratios-relative-risk-absolute]] and [[evidence-appraisal/barraclough-2011-hazard-ratios-clinicians-biostatistics-primer]] for clinician-oriented walkthroughs.

## 4. Diagnostic Accuracy — Relevant to EAL, CBCT, MB2 Detection, Caries Detection

| Abbr | Term | Notes |
|---|---|---|
| **Sn** | Sensitivity | True-positive rate; **SnNOUT** (high Sn → negative test rules out) |
| **Sp** | Specificity | True-negative rate; **SpPIN** (high Sp → positive test rules in) |
| **PPV** | Positive Predictive Value | Depends on prevalence — same test, different population, different PPV |
| **NPV** | Negative Predictive Value | Same prevalence dependence |
| **LR+** | Positive Likelihood Ratio | **Prevalence-independent**; LR+ > 10 = strong diagnostic evidence |
| **LR−** | Negative Likelihood Ratio | LR− < 0.1 = strong rule-out |
| **AUC** | Area Under ROC Curve | 0.5 = chance; 0.7–0.8 acceptable; 0.8–0.9 excellent; >0.9 outstanding |
| **ROC** | Receiver Operating Characteristic | Plot of Sn vs (1 − Sp) across thresholds |

## 5. Meta-Analysis and Systematic Review

| Abbr | Term | Notes |
|---|---|---|
| **I²** | Heterogeneity index | 0–40% low; 30–60% moderate; 50–90% substantial; 75–100% considerable. **Low I² ≠ clinical homogeneity** |
| **τ²** | Between-study variance | Reported in random-effects models |
| **Q** | Cochran's Q | Heterogeneity test; underpowered when number of studies is small |
| **GRADE** | Grading of Recommendations, Assessment, Development and Evaluations | High / Moderate / Low / Very Low; RCTs start High, observational studies start Low |
| **PRISMA** | Preferred Reporting Items for Systematic Reviews and Meta-Analyses | 2020 update is current standard |
| **RoB 2** | Cochrane Risk of Bias 2 (for RCTs) | Five domains; outcome-specific |
| **ROBINS-I** | Risk Of Bias In Non-randomised Studies — of Interventions | Seven domains; for observational studies |
| **Forest plot** | Visual summary of effect sizes and CIs | Diamond = pooled estimate |
| **Funnel plot** | Effect size vs precision | Asymmetry suggests publication bias |

See [[evidence-appraisal/shin-wj-2015-systematic-review-meta-analysis-introduction]] and [[evidence-appraisal/shin-ih-2009-meta-analysis-critical-interpretation]].

## 6. Regression

| Abbr | Term | Notes |
|---|---|---|
| **β** | Regression coefficient | Standardized β allows cross-variable comparison; unstandardized retains units |
| **R²** | Coefficient of determination | Proportion of variance explained |
| **adj R²** | Adjusted R² | Penalizes for added variables |
| **AIC / BIC** | Akaike / Bayesian Information Criterion | Model comparison (lower = better); BIC more conservative |
| **VIF** | Variance Inflation Factor | Multicollinearity diagnostic; >5 or >10 = problematic |

## 7. Survival Analysis — Implant Survival, Peri-Implantitis-Free Survival

| Abbr | Term | Notes |
|---|---|---|
| **KM** | Kaplan-Meier curve | Cumulative survival, handles censoring |
| **Log-rank test** | Compares two KM curves | Non-parametric |
| **HR** | Hazard Ratio | Proportional hazards assumption critical; violation requires time-varying coefficients |
| **Median survival** | Time at which 50% survive | Standard summary statistic |

## 8. Reliability and Agreement — Common in ISQ, CBCT Measurement Studies

| Abbr | Term | Notes |
|---|---|---|
| **ICC** | Intraclass Correlation Coefficient | <0.5 poor; 0.5–0.75 moderate; 0.75–0.9 good; >0.9 excellent |
| **κ** (kappa) | Cohen's kappa for categorical agreement | <0.4 poor; 0.4–0.6 fair; 0.6–0.8 substantial; >0.8 almost perfect. **Prevalence paradox**: extreme prevalence can yield low κ despite high % agreement |
| **Bland-Altman plot** | Agreement between two measurement methods | Bias + 95% Limits of Agreement (LoA); preferred over correlation |
| **CV** | Coefficient of Variation (= SD/M × 100%) | Compares measurements with different units |

## 9. Clinical Trial Analysis Sets

| Abbr | Term | Notes |
|---|---|---|
| **ITT** | Intention-to-Treat | Analysis by randomization assignment; conservative; preserves randomization benefit |
| **PP** | Per-Protocol | Only protocol-adherent participants; risks overestimating efficacy |
| **mITT** | Modified ITT | Definition varies across studies (e.g., at least one dose received); check paper's definition |
| **CONSORT** | Consolidated Standards of Reporting Trials | RCT reporting checklist |

## Five Most Common Misuses (Red Flags When Reading Papers)

Darrigo 2024 catalogs the recurring biostatistics mistakes in the dental literature; the five below are the subset a clinician meets most often when reading implant, perio, and endo papers.

1. **OR interpreted as RR for common outcomes.** When outcome prevalence > 10% (peri-implant mucositis, MBL > threshold, marginal bone loss events), OR overstates RR. Convert via OR = RR × [(1 − p₀) / (1 − p₁)] or insist on RR/risk difference reporting.
2. **p < 0.05 conflated with clinical significance.** Large cohorts detect trivial differences as statistically significant. Always inspect effect size and its CI.
3. **CI width ignored.** A "significant" result with a CI spanning from trivial to huge effect carries weak information. Point estimates without CI context are misleading.
4. **SD vs SE confusion.** Figure error bars frequently default to SE because they look tighter. Check captions and recompute spread if needed.
5. **ITT vs PP discrepancy ignored.** When ITT and PP results diverge, non-adherence or dropout is likely outcome-related, undermining causal inference. Both should be reported and reconciled.

## Related Pages

- [[evidence-appraisal/flechner-2011-pvalues-confidence-intervals-number-needed]] — p-values, CIs, NNT primer
- [[evidence-appraisal/monaghan-2021-odds-ratios-relative-risk-absolute]] — OR vs RR vs ARR for clinicians
- [[evidence-appraisal/barraclough-2011-hazard-ratios-clinicians-biostatistics-primer]] — HR interpretation
- [[evidence-appraisal/darrigo-2024-common-mistakes-biostatistics]] — common biostatistics mistakes
- [[evidence-appraisal/shin-wj-2015-systematic-review-meta-analysis-introduction]] — SR/MA methodology
- [[evidence-appraisal/shin-ih-2009-meta-analysis-critical-interpretation]] — critical interpretation of meta-analyses
- [[evidence-appraisal/nam-2012-statistical-methods-medical-studies]] — statistical methods overview
- [[evidence-appraisal/kiriakou-2014-evidence-based-dentistry-skills-interpret]] — EBD critical appraisal skills
- [[evidence-appraisal/anonymous-nd-systematic-review-critical-appraisal-worksheet]] — SR appraisal checklist
