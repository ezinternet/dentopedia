---
title: "Deep Learning–Enhanced Resonance Frequency Analysis for Dental Implant Stability Assessment"
authors: Zheng Cao, Bi Zhao
year: 2026
doi: 10.1002/cre2.70342
category: artificial-intelligence
pdf_path: /Users/oracleneo/llm-wiki/papers/cao-2026-deep-learning-rfa-isq.pdf
pdf_filename: cao-2026-deep-learning-rfa-isq.pdf
source_collection: external
---

## Why Ingested

First study to apply a deep-learning denoising + metadata-aware prediction pipeline directly to raw RFA waveforms for ISQ estimation, extending the computational RFA literature initiated by [[implants/isq/bhandarkar-2023-rfa-mathematical-modeling-implant-stability]] from mathematical modeling toward trainable neural prediction. The paper provides quantitative benchmarks (MAE, RMSE, R², tolerance accuracy) for an AI-assisted ISQ workflow that also incorporates bone density and insertion torque metadata, directly relevant to the [[overviews/implants-isq-stability-ladder]] decision framework.

## Three-line Summary

(Line 1: Retrospective proof-of-concept study; 100 implants / 300 repeated RFA signal samples from a single Chinese center, Osstell Beacon device, training a two-stage deep learning framework — a denoising CNN followed by a metadata-aware ISQ prediction network incorporating bone density category and insertion torque.)
(Line 2: Denoising reduced noise by 85% and improved SNR from 12.3 dB to 22.8 dB; ISQ prediction achieved MAE 1.85, RMSE 2.40, R² 0.91, and 92% tolerance accuracy within ±3 ISQ units, versus the traditional RFA baseline of MAE 2.65, RMSE 3.35, R² 0.83, 77% accuracy.)
(Line 3: Proof-of-concept only — small single-center cohort with simulated noise, no prospective validation, and no clinical outcome linkage; multi-center prospective trials required before any clinical deployment.)

## 세줄요약

(줄1: 후향적 개념증명 연구; 중국 단일기관 100개 임플란트 / 300회 반복 공명주파수분석 (Resonance Frequency Analysis, RFA) 신호 샘플, Osstell Beacon 기기 — 잡음제거 합성곱신경망 (Convolutional Neural Network, CNN) + 메타데이터 인식 임플란트 안정성 지수 (Implant Stability Quotient, ISQ) 예측망 2단계 딥러닝 프레임워크 학습.)
(줄2: 잡음 85% 감소 및 신호대잡음비 (Signal-to-Noise Ratio, SNR) 12.3 dB → 22.8 dB 향상; ISQ 예측 평균절대오차 (Mean Absolute Error, MAE) 1.85, 평균제곱근오차 (Root Mean Square Error, RMSE) 2.40, R² 0.91, ±3 ISQ 허용 정확도 92% — 전통 RFA 기준(MAE 2.65, RMSE 3.35, R² 0.83, 77%) 대비 유의한 개선.)
(줄3: 개념증명 단계에 불과 — 소규모 단일기관·모의잡음·임상결과 연계 없음; 다기관 전향적 검증 및 실제 잡음 프로파일링이 임상 적용의 필수 전제조건.)

## 1. Document Information

- **Journal**: Clinical and Experimental Dental Research 2026;12:e70342
- **DOI**: 10.1002/cre2.70342
- **Institution**: Department of Stomatology, Liyang People's Hospital, Jiangsu, China

## 2. Key Contributions

- First application of a paired denoising CNN + metadata-aware prediction network to raw RFA waveforms, reducing measurement noise by 85% and improving ISQ prediction accuracy substantially over the traditional Osstell firmware baseline.
- Demonstrated that including patient-level metadata (bone density category by Lekholm-Zarb I–IV one-hot encoding + insertion torque normalized within training set) alongside denoised signals improves ISQ estimation compared to signal-only approaches.
- Established quantitative benchmarks for AI-assisted ISQ prediction: MAE 1.85 ISQ, RMSE 2.40 ISQ, R² 0.91, 92% tolerance accuracy within ±3 ISQ on a held-out 20-implant test set.
- Provided a reproducible signal preprocessing pipeline (zero-mean/unit-variance amplitude normalization + 1024-sample length standardization) that can serve as a methodological reference for future RFA signal processing studies.

## 3. Methodology and Architecture

- **Design**: Retrospective proof-of-concept study; single-center, single-RFA-device
- **n**: 100 implants; 300 signal samples (3 repeated acquisitions per implant, same visit)
- **Split**: 70 implants (210 samples) training / 10 implants (30 samples) validation / 20 implants (60 samples) test (implant-level partitioning)
- **Device**: Osstell Beacon (Integration Diagnostics, Gothenburg, Sweden) with compatible SmartPeg transducers
- **Framework Stage 1 — Denoising CNN**: Supervised denoising trained on matched noisy–clean signal pairs; clean reference = clinically acquired standardized signal; noisy input = clean + simulated Gaussian noise (σ ∈ [0.05, 0.15]) + sinusoidal frequency jitter
- **Framework Stage 2 — Metadata-aware prediction network**: Input = denoised waveform + one-hot bone density (Type I–IV, Lekholm-Zarb) + min-max normalized insertion torque; output = ISQ estimate
- **Signal preprocessing**: Amplitude normalization (zero mean, unit variance), length standardization to 1024 samples; preprocessing parameters computed on training set only
- **Metadata**: Bone density distribution 33/34/33 (low/medium/high); insertion torque mean 35.2 ± 10.4 Ncm (range 15–60 Ncm)
- **Reference ISQ ground truth**: Device-output ISQ from Osstell Beacon proprietary firmware, no post-hoc modification or averaging across replicates
- **Evaluation metrics**: MAE, RMSE, R², tolerance accuracy within ±3 ISQ units; compared against a traditional RFA baseline

## 4. Key Results and Benchmarks

| Metric | Proposed DL Framework | Traditional RFA Baseline |
|---|---|---|
| MAE (ISQ units) | 1.85 | 2.65 |
| RMSE (ISQ units) | 2.40 | 3.35 |
| R² | 0.91 | 0.83 |
| Tolerance accuracy (±3 ISQ) | 92% | 77% |
| Noise reduction | 85% | — |
| SNR improvement | 12.3 dB → 22.8 dB | — |

## 5. Limitations and Future Work

- Single-center, n=100; no a priori power calculation; insufficient for definitive clinical validation
- Noise superimposed on clean signals is simulated (Gaussian + sinusoidal jitter), not empirically measured in diverse clinical environments; real-world noise profiles may differ substantially
- Ground-truth ISQ derived from the same Osstell device firmware as baseline — model optimizes against proprietary outputs, not an independent stability reference (no histomorphometry or biomechanical comparator)
- No clinical outcome data (osseointegration success, failure, loading outcomes) — ISQ accuracy ≠ clinical decision accuracy
- No multi-device generalizability tested; SmartPeg compatibility and device-specific normalization not addressed for other RFA systems (e.g., Penguin RFA, Anycheck)
- Three repeated acquisitions per implant on the same visit may not capture full acquisition variability seen across operators or visits
- Multi-center prospective validation with real-world noise profiling and clinical outcome assessment identified as essential next step by authors

## 6. Related Work

- Bhandarkar 2023 (`implants/isq/bhandarkar-2023-rfa-mathematical-modeling-implant-stability`): Mathematical spring-mass modeling of the implant–bone interface underlying ISQ; this paper extends that foundation to trainable neural estimation
- Sennerby & Meredith 2008 (`implants/isq/sennerby-2008-implant-stability-resonance-frequency-analysis`): Foundational RFA review defining the three ISQ determinants (bone mechanical properties, implant-bone contact, effective implant length); Cao 2026 addresses the signal-contamination limitation noted therein
- Meredith 1996 (`implants/isq/meredith-1996-quantitative-stability-implant-tissue-rfa`): Primary-source origin of RFA method whose measurement limitations this DL framework aims to mitigate
- Mathur 2026 (`artificial-intelligence/mathur-2026-artificial-intelligence-dental-implant`): Broader AI-in-implant-dentistry review, of which ISQ prediction represents one subdomain

## 7. Glossary

- **CNN (Convolutional Neural Network, 합성곱신경망)**: Deep learning architecture using sliding convolutional filters to extract spatial/temporal features from multidimensional data; used here for both denoising and ISQ prediction
- **RFA (Resonance Frequency Analysis, 공명주파수분석)**: Non-invasive implant stability assessment method that measures the resonance frequency of a transducer (SmartPeg) magnetically excited on the implant
- **ISQ (Implant Stability Quotient, 임플란트 안정성 지수)**: Dimensionless 1–100 scale derived from RFA resonance frequency; higher values = greater stability
- **SNR (Signal-to-Noise Ratio, 신호대잡음비)**: Ratio of signal power to noise power, expressed in decibels; higher = cleaner signal
- **MAE (Mean Absolute Error, 평균절대오차)**: Average of absolute differences between predicted and true ISQ values; primary prediction accuracy metric
- **RMSE (Root Mean Square Error, 평균제곱근오차)**: Square root of mean squared prediction errors; penalizes large outliers more than MAE
- **Lekholm-Zarb classification**: Four-type bone density classification (I–IV) based on cortical/trabecular ratio; Type I = dense cortical, Type IV = sparse trabecular
- **Metadata-aware network**: Prediction network that integrates signal features with patient-level structured data (bone density, insertion torque) to improve context-specific estimates
- **Tolerance accuracy**: Proportion of predictions within ±3 ISQ units of ground truth; clinically meaningful threshold given typical ISQ reproducibility
- **SmartPeg**: Proprietary Osstell transducer that attaches to the implant or abutment; its resonance frequency when magnetically excited is the primary RFA measurement input
