---
title: "Predicting no-shows for dental appointments"
authors: Alabdulkarim Y, Almukaynizi M, Alameer A, Makanati B, Althumairy R, Almaslukh A
year: 2022
doi: 10.7717/peerj-cs.1147
category: [practice-management]
source_collection: pubmed-text
full_text: true
pmid: "36426240"
pmcid: "PMC9680883"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9680883/
text_path: /Users/oracleneo/llm-wiki/papers/alabdulkarim-2022-predicting-no-shows-dental-appointments.txt
text_filename: alabdulkarim-2022-predicting-no-shows-dental-appointments.txt
---

## Why Ingested

[[practice-management/alkhurayji-2024-factors-patient-failure-attend-dental]] characterizes *which* patient/clinic factors drive dental did-not-attend (DNA) behavior; this paper operationalizes that knowledge into a deployable machine-learning model that *predicts* the no-show per appointment (AUC 0.718, F1 66.5%) on a large Saudi dental dataset. It reinforces the DNA-factor evidence (lead time and prior no-show history are the dominant predictors here too) and extends it toward actionable scheduling mitigation (reduced time slots for high-risk appointments).

## One-line Summary

Retrospective ML study (n=196,018 dental appointments, single-year Riyadh dental clinic; 42.7% no-show) building per-appointment no-show predictors — best model AUC 0.718, F1 66.5% — with a novel binary-sequence representation of no-show history and a proposal to shorten high-risk appointment slots.

## 한줄요약

후향적 머신러닝 연구(사우디 리야드 치과 1년치 예약 196,018건, 노쇼율 42.7%)로 예약별 노쇼 예측 모델을 구축 — 최고 모델 AUC 0.718, F1 66.5%. 노쇼 이력을 이진 시퀀스로 표현하는 새 방법과, 고위험 예약의 진료시간 단축이라는 스케줄링 활용안을 제시.

## 1. Document Information

- **Title:** Predicting no-shows for dental appointments
- **Authors:** Alabdulkarim Y, Almukaynizi M, Alameer A, Makanati B, Althumairy R, Almaslukh A
- **Journal:** PeerJ Computer Science 8:e1147 (2022-11-09)
- **DOI:** 10.7717/peerj-cs.1147 — PMID 36426240, PMCID PMC9680883
- **Study type:** Retrospective machine-learning model development & validation on real-world appointment records.
- **Source:** PMC full text (open access).

## 2. Key Contributions

1. A per-appointment dental no-show predictor framed as binary classification ({show, no-show}), best AUC 0.718 and F1 66.5% vs a 42.68% prior-no-show baseline (>55% relative F1 improvement; >62% by the conclusion's framing).
2. A **novel binary-sequence representation of no-show history** — each prior appointment encoded as 1 (attended) / 0 (missed), e.g. (1,0,0,1,0) — letting the model learn behavior from the *pattern* rather than collapsing history into a single moving-average percentage.
3. Cross-clinic generalization: models trained on one Riyadh clinic transferred to a second, smaller clinic (49,007 appts, 41% no-show) with negligible degradation (RF AUC 0.748, F1 0.665).
4. A scheduling-utility argument: because dental appointments are long (~36–49 min vs ~17 min primary care), blind overbooking is impractical; instead **shorten the slot for high-no-show-probability appointments** to cap the cost of an absence.
5. Public release of dataset + reproduction notebook.

## 3. Methodology and Architecture

- **Data:** 262,140 dental appointments (one Riyadh clinic, 2019); after removing 66,122 invalid records (duration <10 min, future DOB, missing date/time, walk-ins) → 196,018 appointments, 42.68% no-show (positive class).
- **Features (10 raw + computed):** patient (DOB/age, marital status, gender, nationality), appointment (date, time/hour, booking datetime, duration, doctor ID, SMS-confirmation flag); computed: lead time, days-since-last, weekday, is-weekend, month, holiday, Ramadan, temperature/weather, and no-show history (No-show All #/%, No-show10 #/%, and binary sequences Seq3/Seq5/Seq7/Seq10).
- **Models:** logistic regression (LR), random forest (RF), gradient boosting (GB) — selected as the 3 best of ≥8 tested; scikit-learn; grid-search hyperparameter tuning.
- **Split:** temporal 90/10 (sorted by appointment date) to respect time-series concept drift — no appointment in test precedes any in train (k-fold deliberately avoided).
- **Metrics:** precision, recall, F1, ROC/AUC.

## 4. Key Results and Benchmarks

- **Best model AUC 0.718, F1 66.5%** (vs 42.68% baseline no-show rate; the three models perform near-identically on AUC, GB more threshold-tolerant).
- **Binary-sequence history** improved LR AUC by 2–5% over numeric history features; for RF/GB the gain was negligible (their baselines already ~0.72–0.73). Length of sequence (3/5/7/10) made little difference. The sequence approach roughly matched a prior Markov-model approach.
- **Ablation — strongest predictors:** removing **lead time** dropped AUC 7.5–7.9% (LR/RF/GB) — the single most important feature; removing no-show history dropped LR AUC 4.1% but was insignificant for RF/GB.
- **Feature-correlation observations:** patients needing a companion (children, elderly) attend more; appointments booked closer to the date attend more; high prior no-show rate → more future no-shows; early-morning (<10 AM) slots have the highest no-show likelihood.
- **Long appointments:** no-show rate was similar (~42–44%) across duration cut-offs (≥15…≥60 min); AUC comparable, so duration did not change predictability.
- **Generalization (second clinic):** RF AUC 0.748 / F1 0.665, LR/GB similar — >62% F1 improvement over that clinic's 41% baseline.

## 5. Limitations and Future Work

- Missing potentially predictive variables: home address / distance to clinic, and external factors (specific weather, major events).
- Single-country (Saudi Arabia), 2019 pre-pandemic data; no-show behavior varies by demographics, specialty, and clinic — limits external generalization beyond the two studied clinics.
- F1 ~66% still leaves substantial misclassification; the scheduling intervention (reduced slots) is proposed, not prospectively evaluated.
- Future work: COVID-era/post-pandemic data, and combining the no-show model with a cancellation model.

## 6. Related Work

- Builds on a large no-show-prediction literature (LR, decision trees, RF, neural nets, GB, Naïve Bayes, Bayesian networks, SVM) across primary care, radiology, pediatrics, veterans' health, etc.; dentistry was previously under-studied.
- Most consistent cross-study finding (echoed here): **prior no-show history and appointment lead time are the strongest predictors**; socioeconomic status also recurs.
- Most similar prior work uses binary no-show sequences with a Markov model to precompute probabilities; this paper instead keeps the sequences as learnable features inside a full feature set.
- Within the wiki: [[practice-management/alkhurayji-2024-factors-patient-failure-attend-dental]] (DNA factor characterization) and [[practice-management/khries-2024-identifying-barriers-pediatric-dental-appointments]] (barriers to pediatric attendance).

## 7. Glossary

- **No-show / DNA:** a booked appointment the patient does not attend.
- **AUC:** area under the ROC curve; 1.0 = perfect, 0.5 = random.
- **F1:** harmonic mean of precision and recall.
- **Lead time:** days between booking date and appointment date.
- **Binary-sequence history:** encoding of the last *k* appointments as 1 (attended) / 0 (missed) as a model feature.
- **Concept drift:** change in the data distribution over time, motivating the temporal train/test split.
- **Overbooking:** scheduling more appointments than slots to offset expected no-shows.
