---
title: "Is Acoustic modal analysis a reliable substitution for Osstell® device in dental implant stability assessment? An experimental and finite element analysis study"
authors: Nima Alimoradi, Mohammadjavad (Matin) Einafshar, Reza Amid, Ata Hashemi
year: 2024
date: 2024-05-01
doi: 10.4317/medoral.26358
source: alimoradi-2024-acoustic-modal-analysis.md
category: [implants/isq]
evidence_level: in-vitro
pdf_path: /Users/oracleneo/llm-wiki/papers/alimoradi-2024-acoustic-modal-analysis.pdf
pdf_filename: alimoradi-2024-acoustic-modal-analysis.pdf
source_collection: external
tags: [acoustic-modal-analysis, ISQ, RFA, natural-frequency, Osstell, FEA, implant-stability, polyurethane-bone-analog]
relations:
  - target: implants/isq/debruyne-2017-isq-laser-vibrometry-resonance-frequency
    type: extends
  - target: implants/isq/bhandarkar-2023-rfa-mathematical-modeling-implant-stability
    type: reinforces
---

## Three-line Summary

In-vitro bench study (18 Trias implants, N=9/group, two polyurethane bone-analog densities: 0.16 and 0.32 g/cc) comparing acoustic modal analysis (AMA) with Osstell® ISQ, validated by 3D finite element analysis (FEA).

AMA natural frequency (NF) correlated with ISQ at R²=0.93 (NF=49.4·ISQ−1131.4); doubling bone-analog density raised NF by 82% (1219→2239 Hz) versus only 47% for ISQ (47.9→68.4); FEA overestimated NF by ~15% due to perfect-bonding assumption.

A standard microphone + FFT algorithm can replace proprietary Osstell hardware for bench fixation-strength research, but clinical translation requires in vivo validation accounting for ambient noise, patient anatomy, and biological osseointegration factors.

## 세줄요약

폴리우레탄 골유사체 두 밀도(0.16·0.32 g/cc)에 식립한 트리아스 임플란트 18개(N=9/군)를 대상으로 음향모달해석(Acoustic Modal Analysis, AMA)·Osstell ISQ·3D 유한요소해석(Finite Element Analysis, FEA)을 비교한 인비트로 연구.

AMA 고유진동수(Natural Frequency, NF)와 임플란트 안정성 지수(Implant Stability Quotient, ISQ) 간 R²=0.93 선형 상관; 밀도 2배 시 NF 82% 상승(1219→2239 Hz) vs ISQ 47% 상승(47.9→68.4); FEA는 완전결합 가정으로 NF를 약 15% 과대추정.

단순 마이크+FFT로 Osstell® 대용 가능성 확인; 임상 전환을 위해 주변 소음·환자 해부학·생물학적 요인을 포함한 생체 내 검증 필수.

## Summary

This 2024 in-vitro study from Amirkabir University of Technology and Aalborg University proposes acoustic modal analysis (AMA) — recording the tapping sound from an implant with a standard microphone and extracting the fundamental natural frequency (NF) via fast Fourier transformation (FFT) — as a low-cost alternative to Osstell® resonance frequency analysis (RFA). Eighteen Trias implants were placed into polyurethane foam blocks at two densities representing osteoporotic (0.16 g/cc) and normal-spongy (0.32 g/cc) bone, then measured by both AMA and Osstell® ISQ in parallel. A strong linear relationship (R²=0.93) was found between AMA-derived NF and ISQ, with AMA demonstrating greater sensitivity to density changes (82% NF increase vs 47% ISQ increase when density doubled). Finite element simulations corroborated the experimental NF trend (R²=0.99 for density–NF) while overestimating NF by ~15%, attributable to the perfect-bonding assumption. The authors conclude that AMA with minimal equipment is viable for fixation-strength bench research, while acknowledging that clinical use demands in vivo validation against ambient interference and biologic variability.

## Key Contributions

- AMA replaces Osstell SmartPeg hardware: using only an audio-grade microphone and MATLAB FFT, NF measurement achieves R²=0.93 correlation with ISQ.
- AMA is more sensitive than RFA/ISQ to bone density changes: 82% NF increase vs 47% ISQ increase for a ×2 density step, potentially enabling detection of smaller osseointegration changes.
- FEA validates the experimental AMA approach with R²=0.99 (density vs NF), extending the method in silico to five density points (0.12–0.32 g/cc).
- Clinical limitations are clearly enumerated: ambient noise interference, simplified bone analog, perfect-bonding FEA assumption, absence of biological healing dynamics.

## Methodology

| Parameter | Detail |
|---|---|
| Design | In-vitro bench + 3D FEA |
| Implants | 18 Trias (Servo-dental, Germany), 10 mm × 4.5 mm, N=9/group |
| Bone analog | Sawbones PU foam: 0.16 g/cc (E=23 MPa) and 0.32 g/cc (E=137.5 MPa) |
| AMA protocol | Periotest rod tapping → microphone (44.6 kHz) → FFT → peak NF |
| ISQ | Osstell® + SmartPeg, 4 perpendicular readings/implant |
| FEA mesh | 29,503 + 22,174 10-node tetrahedral elements; Lanczos eigensolver |
| Statistics | Student's t-test; linear regression (R²); 95% CI |

## Results

| Outcome | Low density (0.16 g/cc) | High density (0.32 g/cc) | Change |
|---|---|---|---|
| AMA NF (mean ± SD) | 1219 ± 194 Hz | 2239 ± 312 Hz | +82% (p<0.001) |
| Osstell ISQ (mean ± SD) | 47.9 ± 5.26 | 68.4 ± 4.48 | +47% (p<0.001) |
| FEA NF (predicted) | 1393 Hz | 2550 Hz | +83% |
| FEA overestimation | 15.2% vs AMA | 15.0% vs AMA | — |
| NF vs ISQ (R²) | 0.93 (all samples) | — | NF=49.4·ISQ−1131.4 |
| Density vs NF, FEA (R²) | 0.99 | — | NF=7461·(density)+235.3 |

## Related Papers

- [[implants/isq/debruyne-2017-isq-laser-vibrometry-resonance-frequency]] — laser Doppler vibrometry captures Smartpeg RF independently with r=0.99 vs Osstell IDx; AMA extends this concept using a simpler acoustic microphone
- [[implants/isq/bhandarkar-2023-rfa-mathematical-modeling-implant-stability]] — 2-DOF mathematical model explains how implant–bone stiffness governs RFA output; AMA NF trends reinforce the mechanistic framework
