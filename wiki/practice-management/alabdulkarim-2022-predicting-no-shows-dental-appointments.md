---
title: "Predicting no-shows for dental appointments"
authors: Alabdulkarim Y, Almukaynizi M, Alameer A, Makanati B, Althumairy R, Almaslukh A
year: 2022
date: 2022-11-09
doi: 10.7717/peerj-cs.1147
source: alabdulkarim-2022-predicting-no-shows-dental-appointments.md
category: [practice-management]
confidence: retrospective
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

## One-line Summary

Retrospective machine-learning study (n=196,018 dental appointments, single Riyadh clinic, 2019; 42.7% no-show) building per-appointment no-show predictors — best model AUC 0.718, F1 66.5% — using a novel binary-sequence representation of no-show history, with cross-clinic generalization and a proposal to shorten high-risk appointment slots.

## 한줄요약

후향적 머신러닝 연구(사우디 리야드 치과 1년치 예약 196,018건, 노쇼율 42.7%)로 예약별 노쇼 예측 모델을 구축 — 최고 모델 AUC 0.718, F1 66.5%. 노쇼 이력을 이진 시퀀스로 표현하는 새 방법을 쓰고, 다른 치과로의 일반화를 확인했으며, 고위험 예약의 진료시간을 단축하는 스케줄링 활용안을 제시한다.

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
