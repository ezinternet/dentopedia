---
title: "Finite Element Analysis of Implant Stability Quotient (ISQ) and Bone Stresses for Implant Inclinations of 0°, 15°, and 20°"
authors: Mario Ceddia, Tea Romasco, Giulia Marchioli, Luca Comuzzi, Alessandro Cipollina, Adriano Piattelli, Luciano Lamberti, Natalia Di Pietro, Bartolomeo Trentadue
year: 2025
doi: 10.3390/ma18071625
category: implants/isq
pdf_path: /Users/oracleneo/llm-wiki/papers/ceddia-2025-finite-element-analysis-of-implant.pdf
pdf_filename: ceddia-2025-finite-element-analysis-of-implant.pdf
source_collection: external
---

## Why Ingested

FEA-to-ISQ correlation methodology for tilted implants is underrepresented in the wiki; this paper directly validates micro-mobility FEA as a substitute for in vitro Osstell/RFA testing across two bone densities and three inclinations, extending the mechanistic groundwork in [[implants/isq/alimoradi-2024-acoustic-modal-analysis]] and [[implants/isq/bhandarkar-2023-rfa-mathematical-modeling-implant-stability]].

## Three-line Summary

(Line 1: FEA + in vitro validation study using Cyroth implants (4 mm × 15 mm) in D2/D3 polyurethane blocks at 0°, 15°, and 20° inclinations, comparing FEA-derived ISQ via micro-mobility equation to Osstell RFA measurements)
(Line 2: FEA ISQ differed from in vitro by only 1.27% for D3 bone and 2.86% for D2 bone; ISQ increased with inclination angle (D2: 60.96→61.10; D3: 55.68→55.90 at 0°→20°); bone stress also rose with inclination (cortical D3: 55.4→68.4 MPa; peak implant: 150.1→220.2 MPa))
(Line 3: FEA validated as a faster, cost-effective ISQ estimator; isotropic homogeneous bone assumption and single implant brand/size limit generalizability)

## 세줄요약

(줄1: Cyroth 임플란트(4 mm×15 mm)를 D2·D3 폴리우레탄 블록에 0°·15°·20° 경사로 식립 — FEA 미세운동 방정식 유도 ISQ vs Osstell RFA 실측치 비교)
(줄2: FEA ISQ 오차 D3 1.27%, D2 2.86%; 경사 증가에 따라 ISQ 소폭 상승(D2 60.96→61.10), 피질골 응력도 55.4→68.4 MPa 증가(20° 피크 220.2 MPa))
(줄3: FEA가 ISQ 실험 대체 가능성 검증; 등방성·균질 골 가정·단일 임플란트 사양으로 일반화 제한)

## 1. Document Information

- **Journal**: Materials 2025;18(7):1625
- **DOI**: 10.3390/ma18071625
- **Institution**: Polytechnic University of Bari (Italy); "G. d'Annunzio" University of Chieti-Pescara (Italy)

## 2. Key Contributions

- Establishes a validated FEA pipeline for computing ISQ from implant micro-mobility (Eq. 4: ISQ = 74.94 − 5.21 × ln(Micromovements − 0.24)) for tilted implants at three inclinations
- Demonstrates that ISQ slightly increases with implant inclination (0°→20°) under horizontal loading in both D2 and D3 bone densities
- Validates FEA against in vitro Osstell RFA: error ≤2.86%, confirming FEA as a reliable, cost-effective screening method

## 3. Methodology and Architecture

- **Design**: In vitro FEA simulation + in vitro polyurethane block comparison
- **Implant**: Cyroth 4 mm × 15 mm (AoN Implants Srl, Italy), Ti-6Al-4V
- **Inclinations**: 0°, 15°, 20°
- **Bone blocks**: D2 (polyurethane, E=5500 MPa) and D3 (E=1600 MPa); cortical layer 1 mm, E=16,000 MPa
- **FEA software**: ANSYS Workbench 2023 R1; 163,424 elements, 23,497 nodes; mesh 0.5 mm (interface 0.3 mm)
- **Load**: 100 N horizontal at implant neck (not masticatory — pure ISQ measurement protocol)
- **ISQ derivation**: Micro-displacements at implant neck → Eq. 4 (Pagliani et al.)
- **Comparison**: FEA ISQ vs in vitro Osstell Smart Peg No. 78 (Comuzzi et al. 2025)
- **Outcomes**: ISQ values, bone von Mises stress, implant micro-displacement

## 4. Key Results and Benchmarks

| Condition | FEA ISQ | In vitro ISQ | Error |
|---|---|---|---|
| D2 bone (0°–20° avg) | 61.10 | 62.90 | 2.86% |
| D3 bone (0°–20° avg) | 55.78 | 56.50 | 1.27% |

| Bone/Inclination | ISQ (FEA) |
|---|---|
| D2 / 0° | 60.96 |
| D2 / 15° | 61.05 |
| D2 / 20° | 61.10 |
| D3 / 0° | 55.68 |
| D3 / 15° | 55.77 |
| D3 / 20° | 55.90 |

| Inclination | Cortical von Mises (D3) | Peak implant stress (D3) |
|---|---|---|
| 0° | 55.4 MPa | 150.1 MPa |
| 15° | 60.2 MPa | — |
| 20° | 68.4 MPa | 220.2 MPa |

Bone stress at all inclinations remained below plastic deformation limits (cortical: 130 MPa; trabecular: 13 MPa), confirming Eq. 4 is applicable in all tested configurations.

## 5. Limitations and Future Work

- Single implant system (Cyroth, one diameter/length) — results may not generalize
- Isotropic, homogeneous, linear elastic bone model — real bone is anisotropic and viscoelastic
- Static horizontal load only; does not replicate dynamic masticatory forces
- FEA assumes perfect bone-implant contact (friction 0.3); biological interface varies
- Polyurethane in vitro model does not capture trabecular microstructure or healing biology

## 6. Related Work

- Comuzzi et al. 2025 (Romasco lead): in vitro polyurethane RFA study that this FEA validates against — same experimental conditions
- Alimoradi 2024: acoustic modal analysis FEA for ISQ estimation — parallel FEA-to-ISQ approach
- Bhandarkar 2023: mathematical modeling of RFA-ISQ relationship — foundational ISQ modeling reference
- Pammer et al.: ISQ vs bone density study — key reference for bone-density–ISQ correlation used here
- Pagliani et al.: established Eq. 4 (micro-mobility ↔ ISQ), the mathematical backbone of this study

## 7. Glossary

- **ISQ (Implant Stability Quotient, 임플란트 안정성 지수)**: 0–100 scale from RFA; ≥60 = medium-high stability; derived from implant resonance frequency
- **FEA (Finite Element Analysis, 유한요소분석)**: computational method decomposing complex geometry into discrete elements to model mechanical behavior
- **RFA (Resonance Frequency Analysis, 공명주파수분석)**: clinical measurement technique using Osstell device to assess ISQ
- **Micro-mobility (미세운동)**: horizontal implant neck displacement under horizontal load; used here as ISQ surrogate
- **D2/D3 bone**: Misch classification — D2 = E 5500 MPa (dense trabecular), D3 = E 1600 MPa (loose trabecular)
- **von Mises stress (폰 미제스 응력)**: equivalent stress used to assess if bone exceeds elastic limit (cortical: 130 MPa; trabecular: 13 MPa)
- **Smart Peg No. 78**: Osstell transducer peg specific to this implant connection for ISQ measurement
