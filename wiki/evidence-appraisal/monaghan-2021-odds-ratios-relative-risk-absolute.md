---
title: "Foundational Statistical Principles in Medical Research: A Tutorial on Odds Ratios, Relative Risk, Absolute Risk, and Number Needed to Treat"
authors: Monaghan TF, Rahman SN, Agudelo CW, Wein AJ, Lazar JM, Everaert K, Dmochowski RR
year: 2021
date: 2021-05-25
doi: 10.3390/ijerph18115669
source: monaghan-2021-odds-ratios-relative-risk-absolute.md
category: evidence-appraisal
confidence: narrative-review
pdf_path: /Users/oracleneo/llm-wiki/papers/monaghan-2021-odds-ratios-relative-risk-absolute.pdf
pdf_filename: monaghan-2021-odds-ratios-relative-risk-absolute.pdf
source_collection: external
tags: [odds-ratio, relative-risk, absolute-risk, nnt, biostatistics, ebm-tutorial]
---

## One-line Summary
Tutorial (IJERPH 2021) framing odds ratio (OR), relative risk (RR), absolute risk (AR), and number-needed-to-treat (NNT = 1/ARR) as four lenses on the same 2×2 table; states the OR-RR divergence rule (OR increasingly overestimates RR as baseline outcome risk rises above ~10%), directly relevant to common dental outcomes like peri-implantitis.

## 한줄요약
OR / RR / AR / NNT 4종 효과측정치 영어 튜토리얼 (IJERPH 2021): 같은 데이터에서 네 지표가 어떻게 다르게 나오는지 — 특히 baseline risk가 클수록 OR이 RR을 과대평가하는 현상을 worked example로 보여줌.

## Summary
The clearest single-paper treatment of why "OR ≈ RR" is a lie whenever the baseline outcome is common (>10%). Dental implant complication rates (peri-implantitis 5y prevalence ~10–20%, dry socket 2–5%) sit right in the zone where OR-RR divergence starts to matter — so this paper is directly relevant to how we read our own SR+MAs.

## Key Contributions
- Reframes OR/RR/AR/NNT as four lenses on the same 2×2 table that answer four different clinical questions.
- States the OR-RR divergence rule: as baseline risk grows, OR moves away from RR (in the same direction but more extreme).
- NNT = 1/ARR — makes the "how many patients must I treat" question explicit.

## Methodology
- Tutorial. Multiple urology/medicine worked examples; 2×2 tables; algebraic derivations.

## Results
No original results.

## Clinical Applicability
- When reading a dental case-control study reporting OR for, e.g., smoking and peri-implantitis: if baseline peri-implantitis prevalence is ~15%, an OR of 3.0 corresponds to RR ≈ 2.0–2.3, not 3.0. Communicate the RR/AR/NNT version to patients.
- For RCTs of bone augmentation, prefer ARR/NNT over RR when discussing with patients — concrete and actionable.
- In our smoking-and-implants SR+MAs (Fan 2024, Mustapha 2022, Naseri 2020), the reported metrics include OR; check whether outcomes are rare enough for OR ≈ RR before re-quoting.

## Caveats
- Does not cover HR (use Barraclough 2011).
- Frequentist only.

## Related Papers
- [[evidence-appraisal/flechner-2011-pvalues-confidence-intervals-number-needed]] — p-value/CI/NNT.
- [[evidence-appraisal/barraclough-2011-hazard-ratios-clinicians-biostatistics-primer]] — HR (다른 효과측정치).
- [[evidence-appraisal/darrigo-2024-common-mistakes-biostatistics]] — OR/RR 오용 사례.
- [[overviews/evidence-appraisal-toolkit]] — 9편 종합.
