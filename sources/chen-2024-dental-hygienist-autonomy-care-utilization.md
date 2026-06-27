---
title: "The effects of dental hygienist autonomy on dental care utilization."
authors: Chen J, Meyerhoefer CD, Timmons EJ
year: 2024
doi: 10.1002/hec.4832
category: [practice-management]
source_collection: pubmed-text
full_text: false
pmid: "38536894"
source_url: https://pubmed.ncbi.nlm.nih.gov/38536894/
text_path: /Users/oracleneo/llm-wiki/papers/chen-2024-dental-hygienist-autonomy-care-utilization.txt
text_filename: chen-2024-dental-hygienist-autonomy-care-utilization.txt
---

## Why Ingested

Extends the regulatory/scope-of-practice axis of [[practice-management/ha-2023-dentist-issues-constitutional-court-decisions]] from a Korean constitutional-court framing to a U.S. health-economics framing: this paper supplies causal (difference-in-differences) evidence on how loosening dental hygienist supervision rules reshapes the volume and mix (preventive vs. treatment) of dental care — the delegation/skill-mix economics that any scope-of-practice ruling implicitly trades off. Useful as the empirical counterpart to the legal-decision page.

## One-line Summary

Difference-in-differences study on MEPS 2001–2014 (DHPPI-coded state regulations): granting dental hygienists *moderate* practice autonomy raises total dental visits through more *preventive* care, while the *highest* autonomy level reduces *treatment* use — both effects larger in provider-shortage areas.

## 한줄요약

MEPS 2001–2014 자료를 이용한 이중차분(difference-in-differences) 연구. 치과위생사(dental hygienist)에게 *중간 수준*의 진료 자율성을 부여하면 예방치료(preventive care) 증가를 통해 전체 치과 방문이 늘지만, *최고 수준* 자율성에서는 치료(treatment) 이용이 줄어들며, 두 효과 모두 치과의료 취약지(shortage area)에서 더 크게 나타난다.

> abstract-only — full text not retrieved (pmid 38536894, full_text: false).

## 1. Document Information

- **Title**: The effects of dental hygienist autonomy on dental care utilization.
- **Authors**: Chen J, Meyerhoefer CD, Timmons EJ
- **Journal**: Health Economics 2024;33(8):1726–1747
- **DOI**: 10.1002/hec.4832
- **PMID**: 38536894
- **Study type**: Retrospective quasi-experimental (difference-in-differences) analysis of repeated cross-sectional survey data (MEPS).
- **Source**: PubMed structured abstract (full text not retrieved).

## 2. Key Contributions

- Quantifies the causal effect of dental hygienist (DH) practice-autonomy regulation on dental care utilization in the U.S.
- Extends the Dental Hygiene Professional Practice Index (DHPPI) to cover 2001–2014, enabling exploitation of *within-state* regulatory changes over time rather than only cross-state comparisons.
- Separates the effect by care type (preventive vs. treatment) and by autonomy level (moderate vs. highest), revealing a non-monotonic relationship.
- Shows heterogeneity by access context: effects are amplified in dental-care provider shortage areas, and visits shift toward DH-performed tasks there.

## 3. Methodology and Architecture

- **Data**: Medical Expenditure Panel Survey (MEPS), 2001–2014.
- **Exposure measure**: DHPPI, extended by the authors to 2001–2014, scoring the strength of state regulations governing DH practice autonomy and capturing within-state regulatory change over time.
- **Design**: Difference-in-differences (DiD) framework on selected states, comparing utilization before vs. after states relax supervision requirements against states that did not change.
- **Outcomes**: Total dental visits; visits decomposed into preventive care and treatment; DH-performed tasks (cleanings, exams); subgroup analysis by provider-shortage area.
- (Detailed model specification, controls, and effect sizes not available — abstract-only.)

## 4. Key Results and Benchmarks

- **Moderate autonomy** (relaxed supervision requirements) → **increase in total dental visits**, driven by greater use of **preventive** care.
- **Highest autonomy** level → **decrease in dental treatment** use.
- **Shortage areas**: both estimates increase in magnitude; dental visits shift toward dental hygienists, with an increase in hygienist-performed tasks (cleanings, exams).
- (Point estimates, confidence intervals, and significance not reported in the abstract.)

## 5. Limitations and Future Work

- Abstract-only ingestion — model details, magnitudes, and robustness checks not captured.
- Observational/quasi-experimental design; DiD validity rests on parallel-trends assumptions not verifiable here.
- U.S.-specific regulatory context (DHPPI); transfer to other jurisdictions (e.g., Korea) requires care.
- The drop in treatment use at the highest autonomy level is reported but not mechanistically explained in the abstract (possible substitution, referral friction, or measurement effects).

## 6. Related Work

- [[practice-management/ha-2023-dentist-issues-constitutional-court-decisions]] — regulatory/scope-of-practice decisions affecting the dental workforce; this paper is the empirical (utilization) counterpart to that legal framing.

## 7. Glossary

- **DHPPI (Dental Hygiene Professional Practice Index)**: composite index scoring the strength of state regulations governing dental hygienist practice autonomy.
- **Difference-in-differences (DiD)**: quasi-experimental method estimating a policy effect by comparing the change in outcomes over time between treated and untreated groups.
- **MEPS (Medical Expenditure Panel Survey)**: nationally representative U.S. survey of health care use and expenditures.
- **Scope of practice / practice autonomy**: the range of tasks a provider is legally permitted to perform and the degree of supervision required.
- **Provider shortage area**: geographic area designated as having insufficient dental care providers relative to population need.
