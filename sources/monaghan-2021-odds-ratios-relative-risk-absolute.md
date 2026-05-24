---
title: "Foundational Statistical Principles in Medical Research: A Tutorial on Odds Ratios, Relative Risk, Absolute Risk, and Number Needed to Treat"
authors: Monaghan TF, Rahman SN, Agudelo CW, Wein AJ, Lazar JM, Everaert K, Dmochowski RR
year: 2021
doi: 10.3390/ijerph18115669
category: evidence-appraisal
pdf_path: /Users/oracleneo/llm-wiki/papers/monaghan-2021-odds-ratios-relative-risk-absolute.pdf
pdf_filename: monaghan-2021-odds-ratios-relative-risk-absolute.pdf
source_collection: external
---

## One-line Summary
Open-access tutorial (Int J Environ Res Public Health 2021;18:5669) defining and contrasting the four most common effect/risk measures in medical research — odds ratio, relative risk, absolute risk, and number needed to treat — with real-world worked examples.

## 1. Document Information
- Journal: Int J Environ Res Public Health 2021, 18, 5669
- DOI: 10.3390/ijerph18115669
- Open Access (CC-BY)
- Authors: multi-institution (UT Southwestern, Yale, SUNY Downstate, Penn, Ghent, Vanderbilt)

## 2. Key Contributions
- Disentangles OR vs RR vs AR vs NNT — the four measures that share notation but answer different questions.
- States the case-control vs cohort/RCT design dependency: OR is the natural metric for case-control (where incidence is not directly estimable); RR/AR/NNT are for cohort/RCT.
- Demonstrates how OR can substantially overstate RR when the outcome is common (>10% baseline risk) — a clinically critical pitfall.

## 3. Methodology and Architecture
- Tutorial format with multiple worked examples from urology and general medicine.
- Defines each measure with 2×2 table arithmetic:
  - RR = risk in exposed / risk in unexposed
  - OR = odds in exposed / odds in unexposed
  - AR (or ARR) = risk in unexposed − risk in exposed
  - NNT = 1 / ARR
- Shows divergence of OR from RR as baseline risk increases.

## 4. Key Results and Benchmarks
- No original empirical results — pedagogical paper.
- Establishes the rule: for rare outcomes (<10%) OR ≈ RR; for common outcomes OR overstates RR substantially.

## 5. Limitations and Future Work
- Frequentist only.
- Does not cover hazard ratios (covered by Barraclough 2011) or correlation/regression coefficients.

## 6. Related Work
- Companion to Flechner 2011 (p-value/CI/NNT) and Barraclough 2011 (HR) — together they form a complete clinician's primer on effect-size interpretation.
- D'Arrigo 2024 cites the same OR-RR divergence as one of the top 10 biostatistics mistakes.

## 7. Glossary
- OR: Odds Ratio.
- RR: Relative Risk (Risk Ratio).
- AR / ARR: Absolute Risk / Absolute Risk Reduction.
- NNT: Number Needed to Treat = 1 / ARR.
