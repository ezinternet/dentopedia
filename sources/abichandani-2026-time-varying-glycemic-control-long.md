---
title: "Effect of Time-Varying Glycemic Control on Long-Term Dental Implant Outcomes: A Retrospective Cohort Study"
authors: "Abichandani SJ, Dutta A"
year: 2026
doi: "10.11607/jomi.11625"
category: [implants/survival]
pdf_path: /Users/oracleneo/llm-wiki/papers/abichandani-2026-time-varying-glycemic-control-long.txt
pdf_filename: abichandani-2026-time-varying-glycemic-control-long.txt
source_collection: external
---

## Why Ingested
HbA1c를 고정 노출이 아닌 **시간가변(time-varying) 노출**로 모델링한 첫 대형 코호트 연구로, 기존 [[implants/survival/al-ansari-2022-diabetes-mellitus-dental-implants-sr-ma]] 및 [[implants/survival/shahi-2026-implant-outcomes-diabetes-mellitus-sr]]의 SR 데이터를 실제 임상 세팅의 5-year absolute risk 수치로 구체화함.

## One-line Summary
Retrospective cohort (782 adults, 1,312 implants, 5.6 yr) showing time-varying HbA1c ≥8.0% roughly doubles 5-year implant failure risk (8.1% vs 3.2%) and peri-implantitis risk (26.0% vs 12.1%) compared to HbA1c <7.0%, with a non-linear steepening above the 8% threshold.

## 한줄요약
782명 1312개 임플란트 5.6년 추적 코호트: HbA1c ≥8%에서 실패율 8.1%, 치주염 발생률 26.0%로 HbA1c <7% 대비 각각 2배 위험 증가, 8% 이상 구간에서 비선형 기울기 급변.

## Three-line Summary

Retrospective cohort (782 adults, 1,312 implants, mean 5.6 years) analysing time-varying HbA1c against implant failure and peri-implantitis.

Five-year failure was 3.2% at HbA1c <7.0%, 4.8% at 7.0–<8.0% and 8.1% at ≥8.0%; peri-implantitis was 12.1%, 17.2% and 26.0%, with aHR ≈ 2.0 for ≥8.0% vs <7.0% and a steeper non-linear gradient above ~8%.

Glycemic control around and after placement, not diabetes status alone, tracks risk; limits are retrospective design, residual confounding, no T1DM/T2DM split and 90-day HbA1c carry-forward.

## 세줄요약

후향적 코호트 (성인 782명, 임플란트 1,312개, 평균 5.6년 추적)로 시간가변 당화혈색소 (HbA1c)와 임플란트 실패·임플란트 주위염 (peri-implantitis)의 관계를 분석했다.

5년 실패율은 HbA1c <7.0% 3.2%, 7.0–<8.0% 4.8%, ≥8.0% 8.1%이고 임플란트 주위염은 각각 12.1%, 17.2%, 26.0%였으며, ≥8.0%의 aHR은 약 2.0이고 8% 부근 이상에서 위험이 비선형으로 가팔라졌다.

당뇨 유무보다 식립 전후의 혈당 조절 상태가 위험을 좌우한다; 한계는 후향적 설계, 잔여 교란, 제1형·제2형 미구분, 90일 HbA1c 이월 방식이다.

## 1. Document Information
- Journal: International Journal of Oral & Maxillofacial Implants
- Published: 2026-01-05
- Funding: Not reported
- COI: Not reported

## 2. Key Contributions
- Time-varying HbA1c (updated every visit, 30-day lag, 90-day carry-forward) — more biologically valid than baseline-only HbA1c
- Dose-response modeled with restricted cubic splines: non-linear, threshold effect at ~8%
- First to report **absolute 5-year risks** by HbA1c band for both failure and peri-implantitis
- Competing risks (Fine-Gray) and surgeon frailty terms reduce confounding from high-volume providers
- Multi-provider network (2015–2024) improves external validity

## 3. Methodology and Architecture
- **Design**: Retrospective cohort, multi-provider practice network
- **Population**: 782 adults, 1,312 implants, ≥1 year follow-up (2015–2024)
- **Exposure**: Time-varying HbA1c; modeled continuously (RCS) and categorically (<7.0%, 7.0–<8.0%, ≥8.0%)
- **Outcomes**: Implant failure (cause-specific Cox), peri-implantitis (Aalen-Johansen)
- **Follow-up**: Median 5.6 years; 68 failures, 171 peri-implantitis events
- **Statistics**: Cause-specific Cox + Fine-Gray competing-risk + RCS splines; clustered SE by patient + surgeon frailty

## 4. Key Results and Benchmarks
**Implant failure (5-year absolute risk):**
| HbA1c | 5-yr failure | 5-yr PI |
|---|---|---|
| <7.0% | 3.2% | 12.1% |
| 7.0–<8.0% | 4.8% | 17.2% |
| ≥8.0% | 8.1% | 26.0% |

- Each 1% HbA1c increment → increased hazard of failure and PI
- HbA1c ≥8.0% vs <7.0%: aHR ≈ 2.0 for both failure and PI
- Spline model: non-linear, steeper gradient above ~8.0%
- Findings consistent in competing-risk and sensitivity analyses

## 5. Limitations and Future Work
- Retrospective design; residual confounding (implant site, bone quality, prosthesis type not fully captured)
- HbA1c carry-forward 90 days may misclassify rapidly fluctuating control
- No distinction between T1DM and T2DM
- Exclusion of <1-year follow-up may undercount early failures
- No data on supportive periodontal therapy frequency

## 6. Related Work
- al-ansari-2022 SR+MA: DM associated with higher failure rates overall
- shahi-2026 SR: HbA1c >8% consistently worse across 54 studies
- enteghad-2024 review: diabetes + peri-implant disease mechanisms
- sbricoli-2026 clinical: T2DM peri-implantitis prevalence

## 7. Glossary
- **Time-varying exposure**: HbA1c updated at each clinical visit rather than fixed at baseline
- **Restricted cubic splines (RCS)**: flexible non-parametric dose-response modeling
- **Aalen-Johansen estimator**: cumulative incidence estimator accounting for competing risks
- **Surgeon frailty**: random effect for clustering within surgeons
