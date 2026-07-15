---
title: "Relationships between orofacial pain and sleep: Analysis of UK biobank and genome-wide association studies data"
authors: Jiang Yang, Gong Xu, Yu Min, Gao Xuemei
year: 2024
date: 2024-05-06
doi: 10.1016/j.jds.2024.04.027
source: jiang-2024-orofacial-pain-sleep-biobank.md
category: [tmj]
evidence_level: cross-sectional
source_collection: pubmed-text
full_text: true
pmid: "39873079"
pmcid: "PMC11762203"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11762203/
text_path: /Users/oracleneo/llm-wiki/papers/jiang-2024-orofacial-pain-sleep-biobank.txt
text_filename: jiang-2024-orofacial-pain-sleep-biobank.txt
tags: []
relations:
  - type: reinforces
    target: albadi-2026-sleep-disorders-tmj-pain-dysfunction
---

## Three-line Summary

Cross-sectional analysis of 196,490 UK Biobank participants plus bidirectional/multivariable Mendelian randomization (MR) using GWAS data (TMD-related pain n=377,277; atypical facial pain n=331,749; nine sleep-trait GWAS).

Whole-body pain was associated with unhealthy sleep pattern (OR=1.18, p<0.001); chronic orofacial pain risk showed a non-linear relationship with sleep duration (p=0.032, risk rises at ≥9h/day); MR showed long sleep was causally associated with TMD-related pain (OR=6.77, 95% CI 1.73-26.55, p=0.006, FDR=0.024).

Orofacial pain as a single heterogeneous group showed no significant cross-sectional sleep association — the signal only emerged after splitting acute vs. chronic pain and using TMD-specific causal (MR) analysis; short sleep/insomnia causal signals did not survive adjustment for BMI and diabetes.

## 세줄요약

영국 바이오뱅크(UK Biobank) 참가자 196,490명의 단면연구와 GWAS 자료 기반 양방향·다변량 멘델리안 무작위화(Mendelian randomization, MR) 분석(측두하악장애(TMD) 관련 통증 n=377,277; 비정형 안면통 n=331,749; 9개 수면 형질 GWAS)을 결합했다.

전신 통증군은 불량한 수면 패턴과 연관됐고(OR=1.18, p<0.001), 만성 구강안면통증 위험은 수면시간과 비선형 관계(p=0.032, 하루 9시간 이상에서 위험 증가)를 보였으며, MR 분석에서 장시간 수면이 TMD 관련 통증과 인과적으로 연관됨을 확인했다(OR=6.77, 95% CI 1.73-26.55, p=0.006, FDR=0.024).

구강안면통증을 단일 그룹으로 분석했을 때는 수면과 유의한 단면적 연관이 없었고, 급성/만성으로 나누고 TMD 특이적 인과분석(MR)을 적용했을 때만 신호가 나타났다 — 단시간 수면·불면증의 인과 신호는 BMI·당뇨병 보정 후 사라져 임상 적용 시 주의가 필요하다.

## Summary

This study is the largest-scale genetic/epidemiological investigation in the wiki linking sleep to orofacial pain, and the first to test *causal* directionality rather than mere correlation. Using UK Biobank cross-sectional data (n=196,490) combined with Mendelian randomization on FinnGen GWAS data (TMD-related pain n=377,277; atypical facial pain n=331,749), the authors show a bidirectional pain-sleep relationship at the whole-body level (unhealthy sleep pattern OR=1.18 for pain-all-over-body, p<0.001), but a more nuanced picture for orofacial pain specifically: no significant cross-sectional association when orofacial pain is analyzed as one group, but a clear non-linear dose-response with sleep duration once split into chronic vs. acute (p=0.032, risk rising at ≥9h sleep/day), and — most notably — a causal MR signal for long sleep on TMD-related pain (OR=6.77, p=0.006, FDR=0.024) that survives adjustment for BMI and type 2 diabetes. Short sleep and insomnia showed suggestive univariable MR associations that did NOT survive multivariable adjustment, distinguishing genuinely causal (long sleep) from likely-confounded (short sleep/insomnia) sleep-TMD relationships.

## Key Contributions

- Largest population-scale UKB cohort (196,490) + largest GWAS (TMD-related pain n=377,277) combination applied to the orofacial-pain/sleep question.
- First application of Mendelian randomization to test causal directionality between sleep traits and orofacial pain — a design analogous to a natural randomized trial, reducing reverse-causation and confounding bias inherent to observational sleep-pain literature.
- Demonstrates that acute and chronic orofacial pain must be analyzed separately: pooling (as most prior literature does) masks a real chronic-pain-specific sleep-duration signal.
- Identifies long sleep duration (not short sleep, contrary to common clinical assumption) as the causally robust risk factor for TMD-related pain after adjusting for metabolic confounders (BMI, T2D).

## Methodology

- **Design**: Two-part study — (1) cross-sectional epidemiological analysis of UK Biobank participants (n=196,490 after exclusions for psychological/neurological/sleep disorders, severe vascular/heart disease, diabetes, missing data, or multisite pain); (2) bidirectional and multivariable Mendelian randomization using FinnGen GWAS (TMD-related pain, atypical facial pain) and UKB GWAS (9 sleep traits) summary statistics.
- **Pain groups**: orofacial pain, other-sites pain, pain-all-over-body, pain-free (self-reported UKB questionnaire); orofacial pain further split into acute (<3 months) and chronic (≥3 months).
- **Sleep score**: composite 0-5 score from 5 low-risk sleep traits (duration, snoring, insomnia, dozing, chronotype); higher = healthier.
- **Statistics**: Poisson regression, multinomial logistic regression, restricted cubic spline (non-linear dose-response), adjusted for demographics/psychosocial/health covariates.
- **MR**: IVW as primary method, SNP instrumental variables selected by genome-wide significance/LD clumping/F-statistic>10, FDR-corrected multiple testing, multivariable MR adjusting for BMI and type 2 diabetes.

## Results

- Cohort: 558 orofacial pain / 76,317 other-sites pain / 2,444 pain-all-over-body / 117,171 pain-free (of 196,490).
- Pain-all-over-body group had the worst sleep profile on every metric; associated with unhealthy sleep pattern OR=1.18 (95% CI 1.16-1.21, p<0.001). Orofacial pain (as a single group) showed no significant sleep-score association (wide, heterogeneous CI).
- Non-linear relationship between sleep duration and chronic orofacial pain risk (restricted cubic spline, p=0.032); risk increases at ≥9h/day sleep. No significant relationship for acute orofacial pain.
- Bidirectional MR: strong causal evidence for short sleep → TMD-related pain; suggestive evidence for sleep duration, long sleep, and insomnia → TMD-related pain. No causal association for atypical facial pain with any sleep trait.
- Multivariable MR (adjusted for BMI, T2D): **long sleep** retained a strong, significant causal association with TMD-related pain — OR=6.77 (95% CI 1.73-26.55, p=0.006, FDR=0.024). Short sleep, sleep duration, and insomnia associations disappeared after adjustment, suggesting they were confounded by metabolic factors rather than independently causal.

## Related Papers

- [[wiki/tmj/minakuchi-2022-sleep-bruxism-management-sr]] — sleep bruxism management SR; this paper adds population-scale causal evidence for a broader sleep-trait (long sleep duration, not just bruxism) link to TMD-related pain, complementing the bruxism-specific mechanistic focus.
- albadi-2026-sleep-disorders-tmj-pain-dysfunction (systematic review on sleep disorders and TMD pain/dysfunction) — this paper provides large-scale genetic/epidemiological causal evidence (MR) that reinforces the observational sleep-TMD associations synthesized in that SR.
