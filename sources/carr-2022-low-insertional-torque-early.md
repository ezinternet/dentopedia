---
title: "Low Insertional Torque and Early Dental Implant Failure"
authors: Carr Brian R, Jeon-Slaughter Haekyung, Neal Timothy W, Gulko Joseph A, Kolar Nicholas C, Finn Richard A
year: 2022
doi: 10.1016/j.joms.2022.02.001
pmid: "35248500"
source_collection: pubmed-text
full_text: false
category: implants/survival
source_url: https://pubmed.ncbi.nlm.nih.gov/35248500/
text_path: /Users/oracleneo/llm-wiki/papers/carr-2022-low-insertional-torque-early.txt
text_filename: carr-2022-low-insertional-torque-early.txt
---

## Why Ingested

The low-torque half of a deliberate contrast pair on insertion torque (IT) and early implant failure. This VA North Texas retrospective cohort found that implants placed below 30 N·cm carried ~14× the early-failure hazard of implants at ≥30 N·cm — the opposite direction to [[wiki/implants/norton-2017-low-insertion-torque-primary-stability]], where 30 implants at IT ≤20 N·cm (including three spinners below 5 N·cm) achieved 96.7% survival. Paired with [[wiki/implants/survival/spresser-2025-high-insertional-torque-early]] (same institution and senior author, IT ≥60 N·cm → ~9× early failure), the two papers bracket the relationship from both ends and jointly imply a biphasic, not monotonic, torque–failure curve. It also feeds [[wiki/overviews/early-implant-failure-risk-prevention-overview]].

## Three-line Summary
abstract-only — full text not retrieved
(Line 1: retrospective cohort, 214 implants in 103 patients, VA North Texas 2015–2016; predictor = insertional torque <30 vs ≥30 N·cm, outcome = early failure before prosthetic loading)
(Line 2: 14 early failures (6.5%); IT <30 N·cm carried hazard ratio 13.909 (95% CI 1.835–105.416, P=0.0108) vs ≥30 N·cm)
(Line 3: suggests low insertional torque (<30 N·cm) is a marker of early failure — but the CI is enormous across ~14-fold effect size, so the estimate is imprecise)

## 세줄요약
후향적 코호트 (임플란트 214개, 환자 103명, 미국 VA North Texas 2015–2016): 예측변수 = 삽입 토크 (insertional torque, IT) <30 vs ≥30 N·cm, 결과 = 보철 부하 전 조기 실패.
조기 실패 14개 (6.5%); IT <30 N·cm군은 ≥30 N·cm군 대비 조기 실패 위험 약 14배 (hazard ratio 13.909, 95% CI 1.835–105.416, P=0.0108).
저삽입토크 (<30 N·cm)가 조기 실패 표지자임을 시사 — 다만 약 14배 효과크기에 비해 신뢰구간이 지나치게 넓어 추정이 부정확함.

## 1. Document Information
- **Journal**: Journal of Oral and Maxillofacial Surgery 2022;80:1069-1077
- **DOI**: 10.1016/j.joms.2022.02.001
- **PMID**: 35248500
- **Institution**: Veterans Affairs North Texas Health Care System, Dallas, USA

## 2. Key Contributions
- Quantified early-failure risk for low insertion torque (<30 N·cm) vs ≥30 N·cm in a defined VA cohort — a direction rarely isolated in the torque literature, which mostly debates the *high*-torque end.
- Used a time-to-event design (Kaplan-Meier curves + frailty model) with follow-up censored at 6 months, rather than a simple failure-rate comparison.
- Establishes the ≥30 N·cm threshold as the low-side risk boundary for early failure in this population.

## 3. Methodology and Architecture
- **Design**: Retrospective cohort study (time-to-event analysis)
- **Setting**: VA North Texas Health Care System, Dallas — implants placed 2015–2016
- **n**: 214 implants in 103 patients
- **Predictor**: Insertional torque, dichotomised as ≥30 N·cm vs <30 N·cm at placement
- **Outcome**: Early implant failure — exfoliation noted by the patient, or failure due to implant movement or pain necessitating explantation before prosthesis loading
- **Statistics**: Kaplan-Meier curves and a frailty model comparing time to failure between torque groups; follow-up censored at 6 months

## 4. Key Results and Benchmarks
- Early failures: 14 implants (6.5% of 214)
- IT <30 N·cm vs ≥30 N·cm: **hazard ratio = 13.909** (95% CI 1.835–105.416), **P = 0.0108** (statistically significant)

## 5. Limitations and Future Work
- Interimplant correlation is handled only via the frailty model; the abstract reports no adjustment list or confounder breakdown.
- Effect estimate is very imprecise — the 95% CI spans 1.8 to 105, crossing from modest to overwhelming association.
- Abstract-only ingest: full text not retrieved, so implant system, site distribution, bone quality and loading protocol are unknown.
- Authors call for prospective studies to further elucidate the association.

## 6. Related Work
- Spresser-2025 (same institution, same senior author): the high-torque counterpart — IT ≥60 N·cm carried ~9× early-failure odds vs a 30–59 N·cm control, implying low *and* high torque both raise risk.
- Norton-2017: contradiction — IT ≤20 N·cm cohort (n=30) with 96.7% survival.
- Krisam-2019: IT <30 vs ≥30 N·cm early-failure rates were identical (4.8% vs 4.8%) — a null contrast at the same 30 N·cm cut.

## 7. Glossary
- **IT**: Insertional/insertion torque — the rotational force (N·cm) required to seat an implant; a readout of the bone that resists it.
- **N·cm (Ncm)**: Newton-centimetre, the unit of insertion torque.
- **Hazard ratio (HR)**: Ratio of instantaneous failure risk between groups over time (frailty model here).
- **Early implant failure**: Failure before prosthetic loading — exfoliation, or movement/pain necessitating explantation.
