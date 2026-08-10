---
title: "Predicting no-shows for dental appointments"
authors: Alabdulkarim Y, Almukaynizi M, Alameer A, Makanati B, Althumairy R, Almaslukh A
year: 2022
date: 2022-11-09
doi: 10.7717/peerj-cs.1147
source: alabdulkarim-2022-predicting-no-shows-dental-appointments.md
category: [practice-management]
evidence_level: retrospective
source_collection: pubmed-text
full_text: true
pmid: "36426240"
pmcid: "PMC9680883"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9680883/
text_path: /Users/oracleneo/llm-wiki/papers/alabdulkarim-2022-predicting-no-shows-dental-appointments.txt
text_filename: alabdulkarim-2022-predicting-no-shows-dental-appointments.txt
tags: []
relations:
  - type: reinforces
    target: alkhurayji-2024-factors-patient-failure-attend-dental
---

## Three-line Summary

Retrospective machine-learning study (n=196,018 dental appointments from a single Riyadh clinic in 2019; 42.7% no-show rate) training logistic regression, random forest, and gradient boosting classifiers to predict per-appointment no-shows, validated on a second clinic (n=49,007).

The best model reached AUC 0.718 and F1 66.5%; lead time was the single strongest predictor (removing it dropped AUC by 7.5–7.9%); the novel binary-sequence encoding of prior no-show history improved logistic-regression AUC by 2–5%; models generalized to the second clinic with RF AUC 0.748 / F1 0.665.

Predictions should inform scheduling by shortening appointment-slot durations for high-risk patients rather than overbooking, capping the cost of a missed slot while minimizing disruption.

## 세줄요약

후향적 머신러닝 연구 (사우디 리야드 치과 예약 196,018건, 2019년, 노쇼율 42.7%): 로지스틱 회귀·랜덤 포레스트·그래디언트 부스팅으로 예약별 노쇼 예측 모델 구축, 2차 기관(49,007건) 검증.

최우수 모델 AUC 0.718, F1 66.5%; 예약 리드타임(lead time)이 단일 최강 예측인자(제거 시 AUC −7.5~7.9%); 노쇼 이력 이진 시퀀스(binary sequence) 표현이 LR AUC 2~5% 향상; 2차 기관 RF AUC 0.748 / F1 0.665.

고위험 예약에는 과예약(overbooking) 대신 예약 슬롯 단축으로 결석 비용을 줄이고 후속 환자 불편을 최소화하는 스케줄링 전략을 권고.

## Summary

Patient no-shows are costly and operationally disruptive, and dental appointments are especially affected because they are long (~36–49 min vs ~17 min for primary care), making blind overbooking impractical. Using one year of records from a Riyadh dental clinic (196,018 appointments after cleaning, 42.68% no-show), the authors framed no-show prediction as a binary classification problem and trained logistic regression (LR), random forest (RF), and gradient boosting (GB) models. The best model reached **AUC 0.718 and F1 66.5%**, substantially beating the 42.68% prior-no-show baseline. The work's central methodological contribution is representing each patient's prior no-show history as a **binary sequence of events** (1 = attended, 0 = missed; e.g. (1,0,0,1,0)) so the model learns behavior from the pattern rather than from a collapsed moving-average percentage. Models generalized to a second, smaller clinic with negligible degradation. The authors argue the predictions should drive **reduced appointment-slot duration for high-no-show-risk appointments** rather than aggressive overbooking.

## Key Contributions

- Per-appointment dental no-show predictor: **AUC 0.718, F1 66.5%** (vs 42.68% baseline; >55% relative F1 gain, framed as >62% in the conclusion).
- **Binary-sequence no-show-history feature** — encodes the last *k* appointments as 1/0 so the model learns the behavior associated with each pattern; improved LR AUC by 2–5% over numeric history features (negligible for RF/GB, whose baselines were already ~0.72–0.73). Roughly matched a prior Markov-model approach.
- **Lead time was the single strongest predictor** (ablation: removing it dropped AUC 7.5–7.9%); prior no-show history second (removing it dropped LR AUC 4.1%, insignificant for RF/GB).
- **Cross-clinic generalization:** models trained on clinic 1 transferred to clinic 2 (49,007 appts, 41% no-show) with RF AUC 0.748 / F1 0.665 — >62% F1 improvement over that clinic's baseline.
- **Scheduling utility:** for high-risk appointments, shorten the time slot (rather than overbook), capping the cost of an absence while limiting disruption to following patients.

## Methodology

- **Design:** retrospective ML model development/validation on real appointment-system records.
- **Data:** 262,140 appointments (Riyadh clinic, 2019) → 196,018 after removing invalid records (duration <10 min, future DOB, missing date/time, walk-ins); 42.68% no-show.
- **Features:** patient (age, marital status, gender, nationality), appointment (date, hour, booking datetime, duration, doctor ID, SMS-confirmation flag), plus computed lead time, weekday/weekend, month, holiday, Ramadan, weather/temperature, and no-show history (counts, percentages, and binary sequences Seq3/5/7/10).
- **Models:** LR, RF, GB (3 best of ≥8 tested) via scikit-learn with grid-search tuning.
- **Split:** temporal 90/10 sorted by appointment date (respects concept drift; k-fold avoided).
- **Metrics:** precision, recall, F1, ROC/AUC.

## Results

- Best model **AUC 0.718, F1 66.5%**; LR/RF/GB near-identical on AUC, GB most threshold-tolerant.
- Binary-sequence history: +2–5% AUC for LR; little benefit for RF/GB; sequence length (3–10) made little difference.
- Ablation: **lead time** most important (−7.5 to −7.9% AUC if removed); no-show history −4.1% (LR only).
- Behavioral signals: companion-needing patients (children/elderly) attend more; closer-booked appointments attend more; high prior no-show rate predicts future no-shows; early-morning (<10 AM) slots most missed.
- Long appointments (≥15…≥60 min) showed similar no-show rates (~42–44%) and comparable AUC — duration did not change predictability.
- Generalization to second clinic: RF AUC 0.748 / F1 0.665.

## Related Papers

- [[practice-management/alkhurayji-2024-factors-patient-failure-attend-dental]] — reinforces: characterizes the patient/clinic factors behind dental did-not-attend (DNA); this paper turns that factor knowledge into a deployable per-appointment prediction model (lead time + prior no-show history dominate in both).
- [[practice-management/khries-2024-identifying-barriers-pediatric-dental-appointments]] — related: barriers to attending pediatric dental appointments, a complementary view of the same no-show problem from the patient-barrier angle.
