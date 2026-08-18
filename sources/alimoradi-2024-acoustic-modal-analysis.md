---
title: "Is Acoustic modal analysis a reliable substitution for Osstell® device in dental implant stability assessment? An experimental and finite element analysis study"
authors: Nima Alimoradi, Mohammadjavad (Matin) Einafshar, Reza Amid, Ata Hashemi
year: 2024
doi: 10.4317/medoral.26358
category: [implants/isq]
pdf_path: /Users/oracleneo/llm-wiki/papers/alimoradi-2024-acoustic-modal-analysis.pdf
pdf_filename: alimoradi-2024-acoustic-modal-analysis.pdf
source_collection: external
---

## Why Ingested

Validates acoustic modal analysis (AMA) — a smartphone-microphone + FFT workflow — as a low-cost, equipment-free substitute for Osstell RFA/ISQ measurement of dental implant stability. Directly extends [[implants/isq/debruyne-2017-isq-laser-vibrometry-resonance-frequency]], which validated laser vibrometry as an independent RFA capture method, by proposing an even simpler acoustic approach; also complements [[implants/isq/bhandarkar-2023-rfa-mathematical-modeling-implant-stability]], which builds a 2-DOF mathematical model of the implant–bone vibration system.

## Three-line Summary

In-vitro bench study (18 Trias implants in polyurethane bone-analog blocks at two densities: 0.16 and 0.32 g/cc, N=9/group) comparing acoustic modal analysis (AMA) with Osstell® ISQ, validated by finite element analysis (FEA).

AMA natural frequency (NF) correlated strongly with ISQ (R²=0.93; NF=49.4·ISQ−1131.4); doubling density raised NF 82% (1219→2239 Hz) vs 47% for ISQ (47.9→68.4), making AMA more sensitive; FEA overestimated NF by ~15%.

AMA using only a standard microphone and FFT software can substitute Osstell for fixation-strength research, but clinical translation requires validation against ambient noise, patient anatomy, and biological factors absent from bone-analog models.

## 세줄요약

폴리우레탄 골유사체 블록 두 밀도(0.16·0.32 g/cc) 에 트리아스 임플란트 18개(N=9/군)를 식립해 음향모달해석(AMA)·Osstell ISQ·유한요소해석(FEA)을 비교한 인비트로 연구.

AMA 고유진동수(NF)와 ISQ 간 강한 선형 상관(R²=0.93; NF=49.4·ISQ−1131.4); 밀도 2배 시 NF 82% 상승(1219→2239 Hz) vs ISQ 47% 상승(47.9→68.4) — AMA가 더 민감; FEA는 NF를 약 15% 과대추정.

단순 마이크+FFT 장비로 Osstell 대용 가능성 확인; 임상 적용 전 주변 소음·환자 해부학·생물학적 요인을 고려한 생체 내 검증 필요.

## 1. Document Information
- **Journal**: Med Oral Patol Oral Cir Bucal. 2024 May 1;29(3):e362-9
- **DOI**: 10.4317/medoral.26358
- **Institution**: Amirkabir University of Technology, Tehran, Iran; Aalborg University, Aalborg, Denmark; Shahid Beheshti University of Medical Sciences, Tehran, Iran

## 2. Key Contributions
- Demonstrates that a simple microphone + FFT algorithm (AMA) can measure implant natural frequency with strong correlation to Osstell ISQ (R²=0.93), eliminating the need for proprietary SmartPeg hardware.
- Shows AMA is more sensitive to bone density change than ISQ: 82% NF increase vs 47% ISQ increase when density doubles, suggesting AMA may detect smaller osseointegration changes.
- Provides FEA validation of the experimental AMA approach (R²=0.99 for density–NF relationship), enabling in-silico extension to densities not easily testable in vitro.

## 3. Methodology and Architecture
- **Design**: In-vitro experimental bench study + finite element analysis (FEA)
- **n**: 18 Trias implants (Servo-dental, Germany; 10 mm length, 4.5 mm diameter) in two groups of 9; each sample tested 4 times in perpendicular directions
- **Bone analog**: Sawbones PU foam blocks — 0.16 g/cc (E=23 MPa, osteoporotic-analog) and 0.32 g/cc (E=137.5 MPa, normal-spongy-analog)
- **AMA procedure**: Periotest rod tapping → microphone recording at 44.6 kHz → FFT in MATLAB → peak NF extraction
- **ISQ**: Osstell® system with SmartPeg attachment, 4 perpendicular readings per implant
- **FEA**: ABAQUS 3D models (29,503 + 22,174 10-node tetrahedral elements); perfect bonding assumption; Lanczos eigensolver
- **Statistics**: Student's t-test for density-group NF comparison; linear regression (NF vs ISQ; NF vs density)

## 4. Key Results and Benchmarks

| Outcome | Low density (0.16 g/cc) | High density (0.32 g/cc) | Change |
|---|---|---|---|
| AMA mean NF | 1219 ± 194 Hz | 2239 ± 312 Hz | +82% (p<0.001) |
| Osstell ISQ | 47.9 ± 5.26 | 68.4 ± 4.48 | +47% (p<0.001) |
| FEA NF | 1393 Hz | 2550 Hz | +83% |
| FEA overestimation | ~15.2% vs AMA | ~15.0% vs AMA | — |

- NF vs ISQ: R²=0.93, linear equation NF=49.4·ISQ−1131.4
- FEA density–NF: R²=0.99, NF=7461·(PU density)+235.3
- ISQ range observed: 37–73 (spanning unfavorable to successful)

## 5. Limitations and Future Work
- Bone-analog PU blocks do not replicate variability and complexity of human bone (trabecular architecture, cortical cap, biology).
- FEA assumes perfect bonding at implant–bone interface, explaining the ~15% NF overestimation versus experiment.
- Clinical ambient sounds (aspirators, compressors) and patient-specific anatomy were not modeled; these may introduce interference into AMA recordings.
- Biological factors (tissue integration, healing dynamics) and diverse loading conditions are outside the study scope.
- Validation in vivo and under realistic clinical acoustic environments has not been performed.

## 6. Related Work
- Debruyne 2017: Validated laser Doppler vibrometry (LDV) as an independent ISQ-capture method with r=0.99 vs Osstell IDx — AMA represents an even simpler (microphone-only) approach to the same goal.
- Bhandarkar 2023: 2-DOF mathematical model of implant–bone RFA system explains how ISQ is generated; AMA results align with the mechanistic prediction that NF rises with interfacial stiffness/density.
- Kim 2014 (Med Eng Phys): Measured NF and ISQ in same PU densities but with an adapter block, yielding lower NF (263–309 Hz) versus the present study's axial-tapping approach (1219–2239 Hz) — difference attributed to added adapter mass.

## 7. Glossary
- **AMA (Acoustic Modal Analysis)**: Method of estimating natural frequency from the sound produced by mechanical tapping; uses FFT to extract the fundamental resonance peak.
- **ISQ (Implant Stability Quotient)**: 0–100 scale output of Osstell® RFA devices; converted from resonance frequency via proprietary algorithm; >65 typically indicates successful osseointegration.
- **NF (Natural Frequency)**: Fundamental vibrational frequency of the implant–bone system; measured in Hz; higher NF indicates stiffer (better osseointegrated) interface.
- **FFT (Fast Fourier Transformation)**: Algorithm converting a time-domain signal (recorded sound) to frequency domain; identifies spectral peaks corresponding to resonance modes.
- **FEA (Finite Element Analysis)**: Computational numerical method for simulating stress, strain, and vibration behavior in complex geometries; used here for modal analysis of implant–PU block system.
- **RFA (Resonance Frequency Analysis)**: Non-destructive method of implant stability assessment using an electromagnetic transducer (SmartPeg) and measuring the system resonance frequency.
- **PU (Polyurethane foam)**: Standardized synthetic bone-analog material used in fixation research; density determines mechanical properties (Young's modulus).
