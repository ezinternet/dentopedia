---
title: "Relationships between orofacial pain and sleep: Analysis of UK biobank and genome-wide association studies data"
authors: Jiang Yang, Gong Xu, Yu Min, Gao Xuemei
year: 2024
doi: 10.1016/j.jds.2024.04.027
category: [tmj]
source_collection: pubmed-text
full_text: true
pmid: "39873079"
pmcid: "PMC11762203"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11762203/
text_path: /Users/oracleneo/llm-wiki/papers/jiang-2024-orofacial-pain-sleep-biobank.txt
text_filename: jiang-2024-orofacial-pain-sleep-biobank.txt
relations:
  - type: reinforces
    target: albadi-2026-sleep-disorders-tmj-pain-dysfunction
---

## Why Ingested

This is the largest-scale genetic/epidemiological evidence in the wiki linking sleep to TMD-related orofacial pain *causally* (Mendelian randomization using GWAS instrumental variables, not just cross-sectional correlation). It directly reinforces the sleep-disorders/TMD synthesis in `albadi-2026-sleep-disorders-tmj-pain-dysfunction` (a systematic review from a different journal covering the same clinical question from the observational side) and complements the sleep-bruxism management literature already in the wiki, e.g. [[wiki/tmj/minakuchi-2022-sleep-bruxism-management-sr]]. Combining a 196,490-participant UK Biobank cross-sectional analysis with bidirectional/multivariable MR gives the wiki a rare causal-inference anchor (long sleep duration → TMD-related pain, OR=6.77, p=0.006) for a topic otherwise dominated by observational associations.

## Three-line Summary

Cross-sectional analysis of 196,490 UK Biobank participants plus bidirectional/multivariable Mendelian randomization (MR) using GWAS data (TMD-related pain n=377,277; atypical facial pain n=331,749; nine sleep-trait GWAS).

Whole-body pain was associated with unhealthy sleep pattern (OR=1.18, p<0.001); chronic orofacial pain risk showed a non-linear relationship with sleep duration (p=0.032, risk rises at ≥9h/day); MR showed long sleep was causally associated with TMD-related pain (OR=6.77, 95% CI 1.73-26.55, p=0.006, FDR=0.024), while short sleep/insomnia associations did not survive multivariable adjustment for BMI and type 2 diabetes.

Orofacial pain itself (as a heterogeneous single group) showed no significant cross-sectional association with sleep scores/traits — the signal only emerged after splitting into acute vs. chronic and using TMD-specific MR, underscoring that acute and chronic orofacial pain must be analyzed separately.

## 세줄요약

영국 바이오뱅크(UK Biobank) 참가자 196,490명의 단면연구와, GWAS 자료를 이용한 양방향·다변량 멘델리안 무작위화(Mendelian randomization, MR) 분석(측두하악장애(TMD) 관련 통증 n=377,277; 비정형 안면통 n=331,749; 9개 수면 형질 GWAS)을 결합했다.

전신 통증군에서 불량한 수면 패턴과의 연관성이 확인됐고(OR=1.18, p<0.001), 만성 구강안면통증 위험은 수면시간과 비선형 관계(p=0.032, 하루 9시간 이상에서 위험 증가)를 보였으며, MR 분석에서는 장시간 수면이 TMD 관련 통증과 인과적으로 연관됨을 확인했다(OR=6.77, 95% CI 1.73-26.55, p=0.006, FDR=0.024) — 반면 단시간 수면·불면증의 연관성은 BMI·제2형 당뇨병 보정 후 사라졌다.

구강안면통증을 단일 그룹으로 볼 때는 수면 점수·형질과 단면적 연관성이 유의하지 않았고, 급성/만성으로 구분하고 TMD 특이적 MR을 적용했을 때에만 신호가 나타나 급성과 만성 구강안면통증을 반드시 분리 분석해야 함을 시사한다.

## 1. Document Information

- **Title**: Relationships between orofacial pain and sleep: Analysis of UK biobank and genome-wide association studies data
- **Authors**: Jiang Yang, Gong Xu, Yu Min, Gao Xuemei
- **Journal**: Journal of Dental Sciences (Taiwan)
- **Year**: 2024 (e-pub 2024-05-06)
- **DOI**: 10.1016/j.jds.2024.04.027
- **PMID**: 39873079
- **PMCID**: PMC11762203
- **Study type**: Cross-sectional epidemiological study + bidirectional/multivariable Mendelian randomization (MR)

## 2. Key Contributions

- One of the largest population-scale investigations of the orofacial-pain/sleep relationship, using the UK Biobank (n=196,490 after exclusions) combined with FinnGen GWAS data for TMD-related pain (n=377,277) and atypical facial pain (n=331,749).
- First study (per the authors) to move beyond cross-sectional association and apply Mendelian randomization to test *causal* directionality between sleep traits and orofacial pain, using SNP instrumental variables as unconfounded proxies (a design conceptually similar to a randomized trial).
- Demonstrates that acute and chronic orofacial pain must be analyzed separately — pooling them (as most prior observational literature does) masks the sleep-duration signal that is specific to chronic pain.
- Confirms bidirectionality of the pain-sleep relationship for whole-body/multisite pain, while showing orofacial pain specifically behaves differently (weaker/heterogeneous cross-sectional signal, but a strong causal MR signal for TMD-related pain).

## 3. Methodology and Architecture

**Data sources**: UK Biobank (>500,000 participants, aged 40-69, recruited 2006-2010 from 22 UK assessment centers; ethics approval 21/NW/0157, application #93749). GWAS summary statistics: TMD-related pain and atypical facial pain from FinnGen; nine sleep traits (duration, short sleep, long sleep, snoring, ease of getting up, insomnia, daytime dozing, daytime napping, chronotype) from UKB GWAS; BMI and type 2 diabetes GWAS as covariates for multivariable MR.

**Participant selection**: Excluded participants with psychological/neurological/sleep disorders (ICD-10), severe vascular/heart disease, or physician-diagnosed diabetes; excluded those with missing sleep/pain/covariate data; excluded those reporting ≥2 discrete pain sites. Final n=196,490, split into four groups: orofacial pain, other-sites pain, pain all over the body, pain-free. Orofacial pain further split into acute (<3 months) vs. chronic (≥3 months).

**Pain definitions**: Self-reported via UKB touchscreen questionnaire ("facial pain" = orofacial pain group). For MR, orofacial pain operationalized via ICD-10 TMD codes (K07.60, K07.63) and atypical facial pain (ICD-10 G50.1, ICD-9 3502).

**Sleep score**: Composite 0-5 score from five low-risk sleep traits (7-8h/day duration, no snoring, no/rare insomnia, no/rare daytime dozing, morning chronotype); higher = healthier sleep pattern.

**Statistics**: R 4.3.0. Poisson regression (sleep score vs. pain group), multinomial logistic regression (pain group vs. sleep traits), restricted cubic spline (sleep duration vs. acute/chronic orofacial pain risk), adjusted for age, sex, BMI, Townsend index, anxiety, stress events, smoking, alcohol.

**MR design**: Bidirectional MR (sleep traits → orofacial pain, then orofacial pain → sleep traits) plus multivariable MR (direct effect of sleep traits on TMD-related pain adjusting for BMI/T2D). IVs selected by genome-wide significance (p<5×10⁻⁸, relaxed to 5×10⁻⁶ where needed), LD clumping (r²<0.001, 10,000kb window), F-statistic >10, palindromic/incompatible SNP harmonization. Primary method: inverse variance weighted (IVW); FDR correction for multiple testing (significance threshold p<0.05 AND FDR<0.05 for "strong evidence"; p<0.05 but FDR>0.05 = "suggestive evidence").

## 4. Key Results and Benchmarks

- Cohort composition: 558 orofacial pain, 76,317 other-sites pain, 2,444 pain-all-over-body, 117,171 pain-free (of 196,490 total).
- Pain-all-over-body group had the worst sleep profile across all metrics (shortest duration, most snoring, hardest getting up, most insomnia/dozing/napping, most evening chronotype).
- Poisson regression: pain-all-over-body → unhealthy sleep pattern OR=1.18 (95% CI 1.16-1.21, p<0.001). Orofacial pain vs. sleep score: not significant (wider, heterogeneous CI).
- Restricted cubic spline: sleep duration vs. chronic orofacial pain risk — significant non-linear association (p=0.032); no significant association for acute orofacial pain.
- Bidirectional MR: strong evidence that short sleep causally affects TMD-related pain; suggestive evidence for sleep duration, long sleep, and insomnia on TMD-related pain. No causal association found for atypical facial pain with any sleep trait.
- Multivariable MR (adjusted for BMI, T2D): long sleep retained a strong causal association with TMD-related pain, OR=6.77 (95% CI 1.73-26.55, p=0.006, FDR=0.024). Short sleep, sleep duration, and insomnia associations disappeared after adjustment.

## 5. Limitations and Future Work

- Low prevalence of orofacial pain in the UKB population (558/196,490) limits statistical power and may underestimate correlations.
- Study population is European and elderly (UKB recruits aged 40-69 at baseline), limiting generalizability to other ethnicities/age groups (including younger dental patients, where TMD prevalence peaks).
- Self-reported, single-timepoint pain and sleep questionnaire data (no objective actigraphy/polysomnography); orofacial pain group used a single "facial pain" item without granular subtype capture beyond acute/chronic duration.
- Authors call for prospective-design studies in more representative populations.
- MR assumes no horizontal pleiotropy; while standard sensitivity/pleiotropy tests were performed, MR causal estimates (especially with wide CIs, e.g. long-sleep OR 95% CI 1.73-26.55) should be interpreted as directionally suggestive rather than precise effect sizes.

## 6. Related Work

- Cites/aligns with prior UKB-based sleep-score methodology (composite 5-trait sleep score).
- Graham et al. (pain severity uniquely associated with sleep quality in chronic pain sufferers) — consistent finding.
- Simonelli et al. (sleep extension increases pain tolerance) and Park et al. (Korea NHANES: long sleep duration positively associated with osteoarthritis in middle-aged/older women) — cited as supporting mechanistic context for the long-sleep/pain association.
- Grandner et al. (elevated CRP associated with long sleep duration, NHANES) — cited as a possible inflammatory mechanism linking long sleep to orofacial pain.

## 7. Glossary

- **UKB (UK Biobank)**: Large-scale prospective biomedical database/cohort of >500,000 UK participants aged 40-69 at recruitment.
- **GWAS (Genome-Wide Association Study)**: Study scanning genetic variants across the genome for association with a trait/disease.
- **MR (Mendelian Randomization)**: Causal-inference method using genetic variants as instrumental variables to estimate the causal effect of an exposure (e.g. sleep trait) on an outcome (e.g. orofacial pain), reducing confounding/reverse-causation bias.
- **SNP (Single Nucleotide Polymorphism)**: A genetic variant used as an instrumental variable in MR.
- **IVW (Inverse Variance Weighted)**: Primary MR estimation method combining multiple SNP-based causal estimates.
- **FDR (False Discovery Rate)**: Multiple-testing correction method.
- **TMD (Temporomandibular Disorders)**: Disorders of the temporomandibular joint and associated musculature, a major cause of chronic orofacial pain.
- **Atypical facial pain**: A form of chronic idiopathic orofacial pain without a clear structural or dental cause (ICD-10 G50.1).
- **Restricted cubic spline**: A regression technique modeling non-linear dose-response relationships (here: sleep duration vs. pain risk).
