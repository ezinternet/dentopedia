---
title: "Determining the optimal irrigation activation or agitation techniques for postoperative pain control: A network meta-regression of clinical trials"
authors: Fatma Pertek Hatipoğlu, Merve Çoban Öksüzer, Mohmed Isaqali Karobari, Ömer Hatipoğlu
year: 2025
doi: 10.1016/j.jdsr.2025.12.001
category: endodontics/irrigation
source_collection: pubmed-text
full_text: true
pmid: "41510144"
pmcid: "PMC12774670"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12774670/
text_path: /Users/oracleneo/llm-wiki/papers/hatipoglu-2025-irrigation-activation-postoperative-pain-network-meta.txt
text_filename: hatipoglu-2025-irrigation-activation-postoperative-pain-network-meta.txt
---

## Why Ingested

Direct head-to-head ranking of seven irrigation activation/agitation techniques for the patient-centred outcome of postoperative pain — extends [[endodontics/irrigation/lazaro-2026-laser-activated-irrigation-endodontics-umbrella]] (which found LAI/diode lasers beneficial for postop pain at the umbrella-SR level) with a connected Bayesian network meta-regression that places LAI at the top of the SUCRA ranking and quantifies the LAI-vs-MDI advantage against a 1.0-VAS MCID. Also complements [[endodontics/irrigation/paixao-2022-sonic-ultrasonic-activation-sr-ma]] by situating sonic/ultrasonic activation within the full activation spectrum rather than in isolation.

## One-line Summary

Bayesian network meta-regression of 57 trials (31 in network, 2595 patients) ranking 7 irrigation activation techniques for Day-1 postop pain: laser-activated irrigation (LAI) ranked best (SUCRA 85%) and was the only clinically important contrast (vs manual dynamic irrigation, MD −2.46 VAS, >1.0 MCID); manual dynamic irrigation (MDI) ranked worst; CINeMA confidence mostly low/very low.

## 한줄요약

57편(네트워크 31편, 2595명) 베이지안 네트워크 메타회귀: 7가지 근관세정 활성화 기법 중 레이저 활성화 세정(LAI)이 술후 1일 통증 최저(SUCRA 85%)로 1위, 임상적으로 유의한 유일한 비교는 LAI vs 수동 역동 세정(MDI, MD −2.46 VAS, MCID 1.0 초과); MDI가 최하위; CINeMA 신뢰도는 대부분 낮음~매우낮음.

## 1. Document Information

- **Title**: Determining the optimal irrigation activation or agitation techniques for postoperative pain control: A network meta-regression of clinical trials
- **Authors**: Fatma Pertek Hatipoğlu, Merve Çoban Öksüzer, Mohmed Isaqali Karobari, Ömer Hatipoğlu
- **Journal**: The Japanese Dental Science Review (Jpn Dent Sci Rev) 2025;62:26–45
- **DOI**: 10.1016/j.jdsr.2025.12.001 | **PMID**: 41510144 | **PMCID**: PMC12774670
- **Type**: Bayesian systematic review + network meta-regression (PRISMA-NMA, OSF-registered)
- **Search**: PubMed, Cochrane, Scopus, Web of Science to 10 Dec 2024 (English + Turkish captured)

## 2. Key Contributions

- First review to simultaneously compare the **full spectrum of seven** contemporary irrigation activation/agitation techniques within a **single connected evidence network** for postoperative pain.
- First to incorporate **preoperative symptomatic status as a formal effect modifier** within a Bayesian framework (ordinal covariate, exchangeable slopes).
- Clinical interpretation anchored to a **1.0-point VAS MCID** rather than statistical significance alone, distinguishing statistically-significant from clinically-important contrasts.
- Produces a SUCRA ranking with explicit credible intervals, exposing how much ranking uncertainty exists.

## 3. Methodology and Architecture

- **Seven interventions**: positive pressure (PPI, comparator), manual dynamic (MDI), sonic (SI), ultrasonic (UI), multisonic (MI, e.g. GentleWave), negative-pressure (NPI), laser-activated (LAI).
- **Outcome**: Day-1 postoperative pain, rescaled to a 0–10 metric (only timepoint uniformly reported; allowed full network connectivity). Median±IQR/range converted to mean±SD (Luo et al. / Wan et al.).
- **Model**: Bayesian random-effects network meta-regression in R (`bnma`); symptomatic status as ordinal covariate (0=asymptomatic, 1=mixed, 2=symptomatic); weakly informative priors (σ ~ |N(0,5)|); ≥40,000 post-burn-in MCMC iterations/chain; SUCRA rankings (lower = less pain).
- **Bias/quality**: revised JBI tool for RoB; ROB-MEN for publication bias; ASD traffic-light transitivity; node-splitting (p<0.05 inconsistent, p<0.10 borderline) with LOO/LOD influence analyses; manual CINeMA across six domains (MCID-anchored imprecision).
- **Network**: 31 studies, 2595 patients, 21 possible pairs (14 with direct evidence), 19 two-arm + 12 multi-arm.

## 4. Key Results and Benchmarks

- **SUCRA ranking (median, lower pain = higher)**: LAI 85% (CrI 50–100) > MI 73% > NPI 70% > UI ≈50% ≈ SI 50% > PPI 21% > **MDI 1.5%** (CrI 0–16.7, ranked last).
- **Only clinically important contrast (>1.0 VAS MCID)**: **LAI vs MDI**, MD −2.46 (95% CrI −3.64 to −1.27; Pr(|MD|>1.0)=0.99).
- Statistically significant but sub-MCID: LAI vs PPI (MD −1.47), LAI vs UI (MD −0.87); MDI worse than MI/NPI/SI/UI.
- **Mean Day-1 pain by technique**: MI 0.84 (n=2 studies) < SI 1.54 < NPI 1.65 < LAI 1.88 < UI 2.26 < PPI 2.57 < MDI 3.12.
- **Symptomatic status = strong effect modifier**: all slopes positive, CrI excluding zero; steepest UI (β=4.13), LAI (β=3.25), SI (β=2.59); modest for MI/NPI/PPI/MDI (β≈0.88–1.42) — symptomatic teeth had substantially higher pain regardless of technique.
- **Confidence**: only LAI-vs-MDI reached **moderate** CINeMA confidence; most contrasts low/very low (imprecision, heterogeneity, sparse data for MI/NPI). RoB: 28% low, 60% moderate, 12% high.

## 5. Limitations and Future Work

- Day-1 only (single uniformly reported timepoint) — cannot generalize to later pain trajectories or cumulative burden.
- Many comparisons informed by few/single small RCTs → wide credible and prediction intervals; MI and NPI especially sparse (2 studies each).
- Substantial clinical heterogeneity (irrigant concentration, activation time, instrument systems, analgesic regimens) poorly reported.
- Median-to-mean and 0–100→0–10 conversions introduce approximation error; pain self-reported.
- Only English/Turkish publications → language selection bias.
- Calls for larger, adequately powered RCTs with standardised irrigant protocols and pain-assessment schedules.

## 6. Related Work

- [[endodontics/irrigation/lazaro-2026-laser-activated-irrigation-endodontics-umbrella]] — umbrella SR also identifies LAI/diode benefit for postop pain; this NMR ranks LAI #1 across the activation spectrum.
- [[endodontics/irrigation/paixao-2022-sonic-ultrasonic-activation-sr-ma]] — sonic/ultrasonic activation evaluated in isolation; situated here within the 7-technique network.
- [[endodontics/irrigation/cheung-2021-irrigant-activation-methods-clinical-review]] — clinical review of irrigant activation methods.

## 7. Glossary

- **LAI** — laser-activated irrigation (photoacoustic/photon-induced streaming, e.g. Er:YAG PIPS).
- **MDI** — manual dynamic irrigation (gutta-percha cone piston motion).
- **PPI / SI / UI / MI / NPI** — positive pressure / sonic / ultrasonic / multisonic (GentleWave) / negative-pressure irrigation.
- **SUCRA** — surface under the cumulative ranking curve; probabilistic treatment ranking.
- **MCID** — minimal clinically important difference (1.0 point on a 0–10 VAS for acute postop pain, Myles et al.).
- **CINeMA** — Confidence In Network Meta-Analysis framework (six domains).
- **NMR / network meta-regression** — NMA extended with study-level covariate (here symptomatic status).
- **ASD** — absolute standardized difference (transitivity traffic-light: green/amber/red).
