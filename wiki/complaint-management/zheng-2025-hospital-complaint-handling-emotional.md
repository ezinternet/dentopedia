---
title: "Impact of hospital complaint handling on promoting high-quality development of hospitals via an emotional language analysis model"
authors: "Zheng C, Zhang Y, Lian X, et al."
year: 2025
date: 2025-08-26
doi: "10.3389/frhs.2025.1610004"
source: zheng-2025-hospital-complaint-handling-emotional.md
category: complaint-management
confidence: rct
pdf_path: /Users/oracleneo/llm-wiki/papers/zheng-2025-hospital-complaint-handling-emotional.pdf
pdf_filename: zheng-2025-hospital-complaint-handling-emotional.pdf
source_collection: external
tags: [response, NLP, emotion-analysis, DISC, sentiment-lexicon, clustering, system]
---

## One-line Summary
Randomised intervention (n=334 vs 341) at a Chinese tertiary hospital combining a DISC behavioural-language model, a Boson sentiment lexicon, and KANN-DBSCAN clustering to handle complaints; total satisfaction 93.39% vs 83.24% (p<0.001).

## 한줄요약
중국 3차병원 무작위배정 개입연구(개입 334 vs 대조 341) — DISC 행동언어모델 + Boson 감성사전 + KANN-DBSCAN 군집을 결합한 민원처리로 총 만족도 93.39% vs 83.24% (p<0.001).

## Summary
Zheng and colleagues ran a randomised, controlled intervention at a tertiary hospital in Quanzhou, Fujian, testing whether a behaviour-informed, analytics-driven complaint pipeline beats standard handling. The engine is a **three-layer stack**, not a single "emotional-language model": (1) a **DISC behavioural-language model** classifies each complainant into Dominant / Influential / Steady / Compliant types from their language, tone, and body language, prescribing a tailored response for each; (2) a **Boson public sentiment lexicon** scores complaint text token-by-token to gauge the intensity of negative emotion; (3) an improved **KANN-DBSCAN** density clustering extracts the specific keyword themes driving dissatisfaction. The intervention group (n=334) reached 93.39% total satisfaction vs 83.24% in the standard-handling control (n=341), with lower compensation and petition rates and an independent DISC effect (aOR 3.06). It remains single-site and Chinese-language, so the sentiment layer would need re-training for Korean dental complaints, but the DISC response logic transfers directly.

## Key Contributions
- Combines three engines — DISC behavioural typing (response logic) + Boson sentiment lexicon (negative-emotion intensity) + KANN-DBSCAN clustering (latent complaint themes) — rather than a single sentiment model.
- Randomised, controlled design linking behaviour-informed handling to measurable satisfaction, compensation, and petition-rate gains.
- Operationalises DISC into concrete Text → Subtext → Purpose → correct-response scripts for four complainant types (Table 1).
- Treats patient complaints as a driver of 'high-quality hospital development', not just risk.
- Extends manual complaint coding (HCAT) toward automated, prescriptive sentiment + clustering analytics.

## Methodology
Single-tertiary-hospital randomised controlled intervention (Quanzhou First Hospital; complaint data Jan–Dec 2022–2024; IRB-approved, computer-generated randomisation, baseline/temporal matching).
- **Control group**: standard pathway — receive → register → address → feedback.
- **Intervention group**: same pathway + DISC behavioural-language model. Staff actively read the complainant's language, tone, and body language, classify DISC type, and respond to the underlying psychological need (need to vent, desire for respect, compensation expectation).
- **Sentiment scoring**: each token compared to the Boson lexicon; matched words take the lexicon score, unmatched = 0; summed score >0 positive, <0 negative, =0 neutral; magnitude = negative-emotion intensity.
- **Clustering**: improved KANN-DBSCAN (density-based, auto-tunes ε/Pmin) groups complaints into themes; DBSCAN limitation of ε/Pmin sensitivity addressed.
- Analysis in SPSS 22.0 (t-test, chi-square; p<0.05; multivariable logistic regression).

## Results
Intervention (behaviour-informed) vs control (standard handling):

| Outcome | Control | Intervention | Test | p |
|---|---|---|---|---|
| Total satisfaction | 83.24% (n=161) | **93.39%** (n=198) | χ²=16.45 | <0.001 |
| Compensation rate | 8.15% | **3.56%** | χ²/t=6.324 | 0.012 |
| Petition (escalation) rate | 15.32% | **2.49%** | 30.561 | <0.001 |

- Independent DISC effect on satisfaction: **aOR 3.06 (95% CI 1.66–5.64)**, robust on sensitivity analysis.
- **Sentiment + clustering keyword shift** (negative score: higher magnitude = deeper negative emotion):

| Year | Negative score | Top clustered complaint keywords |
|---|---|---|
| 2023 | −17 | "poor attitude", "poor service", "poor environment" |
| 2024 | −8 | "negligence / lack of timeliness", "tardiness", "failure to explain clearly" |

Complaint themes shifted from *attitude/environment* toward *medical efficiency/communication*, with the negative-emotion score improving from −17 to −8.

### DISC four-type response scripts (Table 1)

| Type | Text | Subtext | Purpose | Correct handling |
|---|---|---|---|---|
| **D — Dominant** | merciless words | "I only talk to the highest responsible person" | release emotion + solve | "Thank you for your suggestion / Your feedback is highly valuable / We will improve immediately" |
| **I — Influential** | loud, attention-seeking | "my issue is very serious, give it high attention" | express emotion, gain attention | show willingness to listen, consider sincerely, respond actively |
| **S — Steady** | help-request tone, "could you come take a look?" | "I'm having difficulties here" | seek concern + assistance | acknowledge fault, apologise, reassure it's taken seriously |
| **C — Compliant** | reserved, "give me a reasonable explanation" | "I want to understand why this happened" | seek clarification, constructive feedback | provide facts + well-structured explanation |

## Related Papers
- [[complaint-management/li-2024-complaint-management-patient-satisfaction]] -- reinforces: system-level complaint handling improves outcomes.
- [[complaint-management/gillespie-2016-healthcare-complaints-analysis-tool]] -- extends: from manual coding toward automated sentiment + clustering analysis.
- [[complaint-management/reader-2014-patient-complaints-healthcare-taxonomy]] -- contrasts: taxonomy-based manual classification vs this behaviour-typing + NLP pipeline.
