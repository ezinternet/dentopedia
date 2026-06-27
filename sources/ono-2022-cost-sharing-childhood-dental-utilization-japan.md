---
title: "Short-term effects of reduced cost sharing on childhood dental care utilization and dental caries prevention in Japan"
authors: Ono S, Sasabuchi Y, Ishimaru M, Ono Y, Matsui H, Yasunaga H
year: 2022
doi: 10.1111/cdoe.12730
category: [practice-management]
source_collection: pubmed-text
full_text: false
pmid: "35072286"
source_url: https://pubmed.ncbi.nlm.nih.gov/35072286/
text_path: /Users/oracleneo/llm-wiki/papers/ono-2022-cost-sharing-childhood-dental-utilization-japan.txt
text_filename: ono-2022-cost-sharing-childhood-dental-utilization-japan.txt
---

## Why Ingested

Seeds a dental health-economics theme on the wiki — specifically how patient cost-sharing (subsidy / out-of-pocket price) shapes dental care demand. This is an empirical natural experiment (subsidy discontinuation at a fixed age, exploited via difference-in-differences) that complements [[practice-management/chen-2024-dental-hygienist-autonomy-care-utilization]]: both are policy→utilization natural experiments, one on the supply side (provider scope of practice) and one on the demand side (price/cost-sharing). Together they begin a small evidence base on what actually moves dental utilization at the population level under a universal-healthcare system.

## One-line Summary

Difference-in-differences study of Japanese administrative dental claims (1108 children, 6276 visits) finding that discontinuing a childhood dental subsidy at age 10 produced NO significant short-term (12-month) change in first/total visits, cost, or acute severe dental conditions.

## 한줄요약

일본 행정 청구자료 이중차분(DiD) 연구(아동 1108명·내원 6276건) — 만 10세에 소아 치과 보조금을 중단해도 12개월 단기 동안 초진·총 내원·비용·급성 중증 치과상태에 유의한 변화가 없었음.

## 1. Document Information

- **Title**: Short-term effects of reduced cost sharing on childhood dental care utilization and dental caries prevention in Japan
- **Authors**: Ono S, Sasabuchi Y, Ishimaru M, Ono Y, Matsui H, Yasunaga H
- **Journal**: Community Dentistry and Oral Epidemiology 2022; 51(2):228–235
- **Year / Date**: 2022 (e-pub 2022-01-24)
- **DOI**: 10.1111/cdoe.12730
- **PMID**: 35072286
- **Design**: Retrospective natural experiment using administrative claims (difference-in-differences)
- Note: **abstract-only — full text not retrieved.**

## 2. Key Contributions

- Tests the cost-sharing → dental utilization relationship in a **universal-healthcare** setting (Japan), where most prior evidence comes from the US and may not generalize.
- Exploits a policy discontinuity — municipalities differing in the **upper age limit of a childhood dental subsidy** — as a quasi-experiment, estimated with **difference-in-differences (DiD)**.
- Reports a **null short-term result**: removing the subsidy at age 10 did not measurably reduce utilization or worsen acute oral-health outcomes within 12 months.

## 3. Methodology and Architecture

- **Data**: administrative dental claims database, Kumamoto Prefecture, Japan, 2014–2015.
- **Sample frame**: municipalities where the subsidy's upper age limit was ≥9 years; children near the age-10 threshold compared between municipalities that did vs did not discontinue the subsidy at age 10.
- **Analytic strategy**: difference-in-differences comparing the treated group (subsidy discontinued at 10) with the control group (subsidy retained), adjusting for area income and the minimal residual user charges.
- **Outcomes**:
  - Utilization — number of first visits, number of total visits, cost per visit.
  - Caries-prevention failure proxy — treatment for **acute severe dental conditions**.
- **Sample**: 1108 eligible children, 6276 visits, 455 clinics; 230 children (50.5%) in subsidy-discontinued municipalities.

## 4. Key Results and Benchmarks

(abstract-only — full text not retrieved; values as reported in abstract)

- First visits: mean ratio **1.01** (95% CI 0.97–1.04) — no significant difference.
- Total visits: mean ratio **1.01** (95% CI 0.98–1.05) — no significant difference.
- Acute severe dental conditions: mean ratio **1.06** (95% CI 0.90–1.24) — no significant difference.
- Cost: coefficient **0.7 USD** (95% CI −0.2–1.6) — no significant difference.
- All confidence intervals span the null (1 for ratios, 0 for the cost coefficient) → no detectable short-term effect of subsidy discontinuation.

## 5. Limitations and Future Work

- **Short horizon** — only 12 months post-policy; caries and downstream oral-health effects may take longer to manifest.
- **Minimal baseline cost-sharing** — even after discontinuation, residual user charges were small, so the price change exploited may have been too small to move demand (limited generalizability to high-cost-sharing contexts).
- **Universal-coverage context** (Japan) — results may not transfer to systems with large out-of-pocket exposure (e.g., the US).
- Single prefecture; administrative-claims outcomes (cannot observe clinical caries directly, only treatment for acute severe conditions as a proxy).
- abstract-only — full text not retrieved; methodological detail (covariate set, parallel-trends checks) not verified here.

## 6. Related Work

- [[practice-management/chen-2024-dental-hygienist-autonomy-care-utilization]] — companion policy→utilization natural experiment (supply-side scope-of-practice vs this paper's demand-side cost-sharing).

## 7. Glossary

- **Cost sharing** — the portion of care cost paid out-of-pocket by the patient (vs covered by insurer/subsidy); reducing it lowers the effective price of care.
- **Dental subsidy** — public program covering children's dental costs up to an age cap; its discontinuation raises the effective price.
- **Difference-in-differences (DiD)** — quasi-experimental method estimating a policy effect by comparing the before–after change in a treated group against the before–after change in an untreated control group, differencing out shared trends.
- **Acute severe dental condition** — treatment proxy used here as a marker of caries-prevention failure.
- **Mean ratio** — ratio of the outcome between groups; 1.00 = no difference.
