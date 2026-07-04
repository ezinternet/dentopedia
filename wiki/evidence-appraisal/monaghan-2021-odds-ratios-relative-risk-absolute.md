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

## Three-line Summary

Tutorial (Int J Environ Res Public Health 2021) framing OR, RR, absolute risk (AR), and NNT (=1/ARR) as four lenses on the same 2×2 contingency table, each answering a distinct clinical question, with algebraic derivations and urology/medicine worked examples.

The OR-RR divergence rule is the central clinical message: as baseline outcome risk grows above ~10%, OR increasingly overestimates RR in the same direction — a smoking-peri-implantitis case-control OR of 3.0 at ~15% baseline prevalence corresponds to RR ≈ 2.0–2.3, not 3.0.

For dental SR+MAs reporting OR (e.g., smoking and implant failure), clinicians should verify whether outcomes are rare enough for OR≈RR before re-quoting, and pair NNT (1/ARR) with risk communication for concrete patient-level benefit framing.

## 세줄요약

튜토리얼 (IJERPH 2021): OR·RR·절대위험(AR)·NNT(=1/ARR) 4종 효과측정치를 같은 2×2 표의 네 렌즈로 정리하고, 각 지표가 다른 임상 질문에 답함을 대수 유도 + 비뇨기/의학 예시로 시연.

핵심 임상 메시지는 OR-RR 발산 법칙: 기저 결과 위험이 ~10% 초과 시 OR이 RR보다 더 극단적으로 추정 — 치주염 기저 유병률 ~15%에서 흡연 OR=3.0은 RR ≈ 2.0–2.3에 해당.

OR을 보고한 치과 SR+MA(흡연·임플란트 실패 등)에서 결과가 희귀한지 확인 후 OR≈RR 가정 적용하고, NNT(=1/ARR)로 환자 수준 혜택을 구체화하여 위험 소통에 사용 권장.

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
