---
title: "Immediate dental implants: insights into early and late failures from a large-scale Chinese cohort"
authors: Yang Y, Zhou L, Hong X, Ye M, Yang Y, Deng X, Xu M
year: 2026
doi: "10.1186/s12903-026-08792-8"
pmid: "42231271"
pmcid: "PMC13505097"
source_collection: pubmed-text
full_text: true
text_path: /Users/oracleneo/llm-wiki/papers/yang-2026-immediate-dental-implants-insights-into.txt
text_filename: yang-2026-immediate-dental-implants-insights-into.txt
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13505097/
category: [immediate-implant]
---

## Why Ingested

즉시식립 임플란트에서 치유방식 (매몰형 vs 비매몰형)이 조기 실패에 미치는 영향과 흡연 효과가 치유방식에 따라 다른지에 대한 근거가 위키에 없어 인제스트. 기존 [[implants/survival/yari-2023-risk-factors-early-implant-failure]] (즉시 임시보철·상악 구치부가 조기 실패 예측)와 [[implants/survival/wahlberg-2025-multicenter-early-implant-failures-part-2-patient]]를 즉시식립 전용 대형 코호트로 보강·대비하며, 본 논문은 흡연을 수집하지 않았음을 확인.

## Three-line Summary


Retrospective single-center cohort (Xiamen, 2013-2022; 1,513 immediate implants in 781 patients; 50 early and 36 late failures; 10-year implant-level cumulative survival 93.15%): factors for early (pre-loading) and late failure analysed with marginal Cox regression.

Early failure: male sex HR 2.48, sinus elevation HR 2.49, maxillary anterior HR 3.15 and posterior HR 2.75 (vs mandibular posterior) increased risk; submerged healing lowered it (HR 0.53, 95% CI 0.30-0.95). Smoking was not collected, so no smoking analysis or smoking-by-healing-protocol interaction was possible.

Submerged healing was chosen when insertion torque was below 20-25 Ncm, so the association is subject to confounding by indication and cannot be read as causal; late-failure findings rest on only 36 events.

## 세줄요약

후향적 단일기관 코호트 (중국 샤먼, 2013-2022; 환자 781명, 즉시식립 임플란트 1,513개; 조기 실패 50개·후기 실패 36개; 10년 임플란트 단위 누적생존율 93.15%): 주변 Cox 회귀 (marginal Cox regression)로 조기 (보철 부하 전)·후기 실패 관련 인자 분석.

조기 실패는 남성 (HR 2.48), 상악동 거상 (Sinus Floor Elevation, HR 2.49), 상악 전치부 (HR 3.15)·상악 구치부 (HR 2.75; 기준 하악 구치부)에서 증가하고, 매몰형 치유 (submerged healing)에서 감소 (HR 0.53, 95% CI 0.30-0.95). 흡연은 수집되지 않아 흡연 분석과 흡연×치유방식 상호작용 검정은 불가능했음.

매몰형 치유는 삽입 토크 20-25 Ncm 미만일 때 선택되어 적응증 교란 (confounding by indication)이 있고 인과로 읽을 수 없음; 후기 실패는 36건뿐이라 결과가 탐색적임.

## 1. Document Information

- **Journal**: BMC Oral Health 2026;26(1)
- **DOI**: [10.1186/s12903-026-08792-8](https://doi.org/10.1186/s12903-026-08792-8)
- **PMC**: PMC13505097 / **PMID**: 42231271
- **Authors' institution**: Xiamen Stomatological Hospital / Xiamen Medical College, China
- **Text**: PMC full text; contents of Tables 1-4 and Figures 1-6 were not in the retrieved text (in-text results only).

## 2. Key Contributions

- Large single-center cohort restricted to immediate implants (1,513 implants / 781 patients), separating early (before prosthetic loading) from late failure.
- Reports submerged healing as independently associated with lower early failure (HR 0.53, 95% CI 0.30-0.95).
- Explicitly states smoking, oral hygiene, bruxism, systemic disease and medication data were unavailable.

## 3. Methodology and Architecture

- **Design**: retrospective cohort, EMR review, Jan 2013 - Dec 2022, observation to 31 Oct 2023; STROBE; no sample-size calculation.
- **Definitions**: early failure = implant loss before prosthetic loading (within 3-6 months); late failure = loss after loading. Survival = implant retained.
- **Healing mode**: "Healing mode (submerged or non-submerged) was selected based on primary stability. Submerged healing was generally selected when insertion torque was < 20-25 Ncm." Torque > 35 Ncm: immediate temporary restoration; otherwise "healing abutments were placed on the implants". The paper does not otherwise define submerged (no explicit "cover screw / fully closed flap" wording); implants were placed flapless whenever feasible.
- **Statistics**: marginal Cox (Wei-Lin-Weissfeld) for within-patient clustering, implant level; multivariable adjusted for surgeon experience, implant position, bone quality; FDR-corrected univariate p-values; Schoenfeld test.
- **Variables**: sex, age, position, periodontitis (CBCT bone loss > 2 mm), bone grafting method (none / graft only / GBR), sinus elevation, healing method, surgeon experience, diameter, length. Implant system dropped (not significant).

## 4. Key Results and Benchmarks

| Item | Value |
|---|---|
| Implants / patients | 1,513 / 781 (from 10,831 implants / 4,687 patients) |
| Lost implants | 86 (71 patients): 50 early (41 patients), 36 late (30 patients) |
| CSR implant level | 95.57% (1 y), 94.85% (3 y), 93.86% (5 y), 93.15% (10 y) |
| CSR patient level | 92.96%, 91.60%, 90.36%, 89.46% |
| Early failure, multivariable HR | male 2.48 (1.31-4.69); sinus elevation 2.49 (1.05-5.87); maxillary anterior 3.15 (1.29-7.69); maxillary posterior 2.75 (1.08-6.98); submerged healing 0.53 (0.30-0.95) |
| Early failure, non-significant | age, periodontitis, diameter, length, surgeon experience, bone grafting (graft-only trend) |
| Late failure, exploratory HR | graft without membrane 3.54 (1.07-11.74); diameter 4.0-4.5 mm vs <= 3.75 mm 0.30 (0.13-0.69) |
| Late failure, non-significant | age, sex, periodontitis, position, sinus elevation, surgeon experience, healing method, length |

No smoking variable; no smoking-by-healing-method interaction or stratification.

## 5. Limitations and Future Work

- Retrospective, residual confounding; healing mode assigned by insertion torque (confounding by indication).
- Smoking, oral hygiene, bruxism, occlusal force, systemic disease and medication not available; male-sex effect may reflect unmeasured smoking/hygiene.
- Only 36 late failures; per-arm counts for submerged vs non-submerged not available in retrieved text (tables missing).
- Single center; survival only, no marginal bone loss or peri-implantitis outcomes.

## 6. Related Work

- [[implants/survival/yari-2023-risk-factors-early-implant-failure]]
- [[implants/survival/wahlberg-2025-multicenter-early-implant-failures-part-2-patient]]
- [[implants/survival/fan-2024-smoking-early-implant-failure-sr-ma]]
- [[overviews/early-implant-failure-risk-prevention-overview]]

## 7. Glossary

- **Immediate implant placement (IIP)**: implant placed at the time of extraction.
- **Submerged healing**: implant covered by soft tissue during osseointegration (per this paper, chosen at low insertion torque).
- **Marginal Cox model (Wei-Lin-Weissfeld)**: Cox regression accounting for clustering of multiple implants per patient.
- **CSR**: cumulative survival rate (life table).
