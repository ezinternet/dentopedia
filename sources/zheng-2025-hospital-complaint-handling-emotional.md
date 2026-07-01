---
title: "Impact of hospital complaint handling on promoting high-quality development of hospitals via an emotional language analysis model"
authors: "Caijiao Zheng, Yi Zhang, Xiaolong Lian, Jinxiu Ke, Hongxia Chen, Yiwen Chen"
year: 2025
doi: "10.3389/frhs.2025.1610004"
category: complaint-management
pdf_path: /Users/oracleneo/llm-wiki/papers/zheng-2025-hospital-complaint-handling-emotional.pdf
pdf_filename: zheng-2025-hospital-complaint-handling-emotional.pdf
source_collection: external
---

## Why Ingested
Shows the analytic frontier of the response axis: mining the *emotional* language of complaints (NLP) to drive hospital quality improvement. Connects complaint handling to organisational development and previews how a clinic could analyse its own complaint text. Extends the manual coding of [[complaint-management/bmjqs-2015-004596]] (HCAT) toward automated sentiment, within the [[overviews/complaint-management-pipeline-classification-expectation-response-education]] response axis.

## One-line Summary
Randomised intervention (n=334 vs 341) at a Chinese tertiary hospital combining a DISC behavioural-language model, a Boson sentiment lexicon, and KANN-DBSCAN clustering to handle complaints; total satisfaction 93.39% vs 83.24% (p<0.001).

## 한줄요약
중국 3차병원 무작위배정 개입연구(개입 334 vs 대조 341) — DISC 행동언어모델 + Boson 감성사전 + KANN-DBSCAN 군집을 결합한 민원처리로 총 만족도 93.39% vs 83.24% (p<0.001).

## 1. Document Information
- Frontiers in Health Services 2025;5:1610004. Original Research. CC BY. Published 26 Aug 2025.
- Quanzhou First Hospital, Fujian, China (tertiary hospital service centre). Complaint data Jan–Dec 2022–2024; IRB-approved; computer-generated randomisation with baseline/temporal matching.

## 2. Key Contributions
- Combines three engines — **DISC behavioural typing** (response logic) + **Boson sentiment lexicon** (negative-emotion intensity) + **KANN-DBSCAN clustering** (latent complaint themes) — not a single sentiment model.
- Randomised, controlled design linking behaviour-informed handling to satisfaction, compensation, and petition-rate gains.
- Operationalises DISC into Text → Subtext → Purpose → correct-response scripts for four complainant types (Table 1).
- Treats patient complaints as a driver of 'high-quality hospital development', not just risk.
- Extends manual complaint coding (HCAT) toward automated, prescriptive sentiment + clustering analytics.

## 3. Methodology and Architecture
Single-tertiary-hospital **randomised controlled intervention** (not a descriptive case study).
- **Control**: standard pathway — receive → register → address → feedback.
- **Intervention**: same pathway + DISC behavioural-language model. Staff read the complainant's language, tone, and body language, classify DISC type (Dominant/Influential/Steady/Compliant), and respond to the underlying psychological need (need to vent, desire for respect, compensation expectation).
- **Sentiment scoring**: each token compared to the **Boson public sentiment lexicon**; matched words take the lexicon score, unmatched = 0; cumulative score >0 positive, <0 negative, =0 neutral; magnitude = negative-emotion intensity.
- **Clustering**: improved **KANN-DBSCAN** (density-based, auto-tunes ε/Pmin via K-nearest-neighbour distance + expectation method) groups complaints into themes, addressing DBSCAN's ε/Pmin sensitivity.
- Analysis in SPSS 22.0 (independent two-sample t-test; chi-square; multivariable logistic regression; p<0.05).

## 4. Key Results and Benchmarks
Intervention vs control:
- **Total satisfaction 93.39% (n=198) vs 83.24% (n=161)**, χ²=16.45, p<0.001.
- **Compensation rate 3.56% vs 8.15%**, p=0.012 (less financial payout).
- **Petition/escalation rate 2.49% vs 15.32%**, p<0.001 (far fewer escalations).
- **Independent DISC effect on satisfaction: aOR 3.06 (95% CI 1.66–5.64)**, robust on sensitivity analysis.
- **Sentiment+clustering keyword shift** (negative score, higher magnitude = deeper negative emotion): 2023 = −17 ("poor attitude", "poor service", "poor environment") → 2024 = −8 ("negligence/lack of timeliness", "tardiness", "failure to explain clearly"). Themes moved from attitude/environment toward medical efficiency/communication.

## 5. Limitations and Future Work
Single tertiary hospital → limited external validity. **Chinese-language Boson lexicon — transfer to Korean dental complaints needs re-training** (culturally specific expressions may be missed). KANN-DBSCAN offers no intrinsic cluster explanation (authors suggest XAI/SHAP/LIME). Frontline staff must still be trained to interpret and execute DISC-recommended responses under stress; authors call for real-time closed-loop systems and longitudinal, multi-department validation.

## 6. Related Work
Analytic extension of structured complaint coding (HCAT) toward automated sentiment + clustering; aligns with Li (2024) on system-level benefit. DISC roots cited from leadership/communication literature (Pathak 2025; Slowikowski 2005). Complements the status-theory-based response scripts used in the clinic's `claim-coach` skill.

## 7. Glossary
- **DISC behavioural-language model**: personality/behaviour typing into Dominant, Influential (Inducement), Steady (Submission), Compliant — used here to tailor complaint responses.
- **Boson sentiment lexicon**: public Chinese word-level sentiment dictionary; token scores summed to a polarity/intensity score.
- **KANN-DBSCAN**: K-Average-Nearest-Neighbour-tuned DBSCAN density clustering; auto-selects ε/Pmin to extract complaint keyword themes.
- **Petition rate**: proportion of complaints escalated to a higher (formal appeal/petition) level.
- **High-quality development**: Chinese health-policy term for quality-led hospital improvement.
