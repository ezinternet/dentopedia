---
title: "Survival analysis of dental implants placed in a private practice: A multicenter prospective cohort study"
authors: Li F, Roguljić M, Medvedec-Mikić I, Sánchez-Garcés MÁ, Toledano-Serrabona J, Camps-Font O
year: 2024
doi: 10.4317/jced.61457
category: implants/survival
source_collection: pubmed-text
full_text: true
pmid: "38988756"
pmcid: "PMC11231890"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11231890/
text_path: /Users/oracleneo/llm-wiki/papers/multicenter-2024-survival-analysis-private-practice-prospective.txt
text_filename: multicenter-2024-survival-analysis-private-practice-prospective.txt
---

## Why Ingested

Private-practice, multicenter prospective cohort quantifying 24-month implant survival (97.44%) and — critically — reporting hazard ratios for absence of primary stability (HR 23.54) and bruxism (HR 96.62), adding event-level evidence to the primary-stability debate that our wiki currently holds as observational-dose comparisons; reinforces [[wiki/implants/survival/cobo-vazquez-2018-effect-lack-primary-stability-survival]] and [[wiki/implants/survival/alrowis-2025-factors-affecting-dental-implant-failure-retrospective]].

## Three-line Summary

Prospective multicenter cohort of 80 patients / 166 Avinent implants placed in two private clinics (2015–2017), 24-month follow-up, STROBE-reported.

Cumulative survival at 24 months was 97.44% (95% CI 93.30–99.03); 4 implants failed (2.41%), with bruxism (HR 96.62, p<0.001) and absence of primary stability (HR 23.54, p<0.001) significantly associated with failure in univariate Cox analysis.

Implication: single-brand private-practice implant treatment is predictable (>95% survival), but the reported HRs are univariate wide-CI estimates from a small failure count — confounder adjustment and longer follow-up are needed.

## 세줄요약

민간 치과 2곳에서 시행된 80명(임플란트 166개) 전향적 다기관 코호트 연구, 24개월 추적 (2015–2017).

24개월 누적 생존율 97.44% (95% CI 93.30–99.03), 실패 4개(2.41%)였고, 이갈이(HR 96.62, p<0.001)와 일차 안정성(primary stability) 결여(HR 23.54, p<0.001)가 실패와 유의한 연관을 보였다.

의미: 민간 진료환경에서 임플란트 생존율은 95% 이상으로 예측 가능하지만, HR 값은 소수 실패에서 나온 단변량 분석이라 다변량 조정과 장기 추적이 필요하다.

## 1. Document Information

- **Journal**: Journal of Clinical and Experimental Dentistry 2024;16(5):e556–e561
- **DOI**: 10.4317/jced.61457
- **Institution**: Private dental clinics (Vancouver, Canada; Split, Croatia) + School of Medicine and Health Sciences, Universitat de Barcelona, Spain; IDIBELL (multicenter)

## 2. Key Contributions

- Private-practice, multicenter prospective cohort (STROBE) reporting 97.44% cumulative implant survival at 24 months across two clinics using a single implant system (Avinent Biomimetic).
- Quantifies that 54.82% of implants achieved primary stability >35 Ncm, none exceeded 45 Ncm, and only 4.82% failed to attain primary stability.
- Identifies absence of primary stability (HR 23.54; 95% CI 3.28–169.16; p<0.001) and bruxism (HR 96.62; 95% CI 9.88–945.08; p<0.001) as implant-failure risk factors with hazard ratios derived from the cohort, in line with prior SR/MA on these topics.
- Reports a 50/50 split of early (pre-restoration) vs late (post-loading) failures among the 4 failures, supporting the early-6-month critical window for implant loss.

## 3. Methodology and Architecture

- **Design**: Prospective multicenter cohort (2 private dental clinics), STROBE-adherent
- **n**: 80 patients (41 females; mean age 58.17, SD 13.86) / 166 implants (Sep 2015–Nov 2017)
- **Implants**: Single brand — Avinent bone-level grade-5 titanium, sandblasted+anodized Biomimetic surface; Coral (parallel-walled) and Ocean IC (tapered, reverse coronal) designs
- **Outcomes**: Cumulative survival (Kaplan–Meier), failure (implant mobility), risk factors (univariate log-rank + univariate Cox HR)
- **Power**: post-hoc — 96% to detect HR 4 at 166 implants, corrected to 84% assuming moderate intra-subject correlation (ρ=0.5)
- **Software**: STATA 14, analyses by a researcher unblinded to but uninvolved in treatment

## 4. Key Results and Benchmarks

| Outcome | Value |
|---|---|
| 24-month cumulative survival | 97.44% (95% CI 93.30–99.03) |
| Failed implants | 4 / 166 (2.41%; 95% CI 0.94–6.03) |
| Bruxism — implant failure | HR 96.62 (95% CI 9.88–945.08; p<0.001) |
| Absence of primary stability — implant failure | HR 23.54 (95% CI 3.28–169.16; p<0.001) |
| Primary stability >35 Ncm | 54.82% (none exceeded 45 Ncm; 4.82% <35 Ncm) |
| Early vs late failure | 2 before restoration (<3 months) vs 2 after loading |

Context: 78.31% implants in healed pristine bone, 19.88% immediate in fresh sockets; 13.25% immediate-loading prostheses; peri-implantitis prevalence in study: 1.8% (implant) / 3.75% (patient), vs ~30% reported in broader literature (attributed to short follow-up).

## 5. Limitations and Future Work

- Small sample with only 4 failures → wide HR confidence intervals (e.g., bruxism CI 9.88–945.08); univariate only, no multivariable adjustment.
- 24-month follow-up too short to capture late failures; authors note lack of data beyond month 12 when the failure curve stabilizes.
- Heterogeneous sample (mixed edentulism types, immediate vs delayed protocols, single brand) limits generalizability; single brand (Avinent) — results may not transfer to other systems.
- Post-hoc (not a priori) sample-size calculation; intra-subject correlation corrected power declined to 84%.
- Future work: longer follow-up evaluating peri-implant status (peri-implantitis prevalence) in private settings, and identification/multifactorial combination of failure indicators.

## 6. Related Work

- Cobo-Vázquez 2018: direct topic — lack of primary stability and implant survival; this cohort confirms the association with HRs, reinforcing the relationship (reference 24 in the paper).
- Alrowis 2025 (retrospective): failure-cause attribution; this prospective cohort reinforces the risk-factor direction with HR estimates.
- Jang 2025 (flapless immediate implants, low primary stability): outcome of low-primary-stability cases; this paper extends that line by showing low PS drives early failure risk in routine (mostly delayed-loading) practice.
- Barboza 2026 (bruxism–implant failure umbrella review): this cohort's bruxism HR aligns with the risk direction synthesized by the umbrella-level evidence.
- Wittenberg/Albrektsson context: 10-yr weighted survival 96.35% (Wennerberg, ref 22) against which the 97.44% 24-month figure should be read.

## 7. Glossary

- **Primary stability**: mechanical anchorage of an implant at placement, here operationally ≥35 Ncm insertion torque
- **Cumulative survival rate**: proportion of implants still present (regardless of condition) at the end of follow-up, Kaplan–Meier estimate
- **Failure**: implant mobility diagnosed at examination
- **Bruxism**: parafunctional clenching/grinding habit, a patient-level risk factor
- **STROBE**: Strengthening the Reporting of Observational Studies in Epidemiology — reporting checklist for observational cohorts
- **Hazard ratio (HR)**: hazard of the failure event in the exposed vs unexposed group in Cox regression