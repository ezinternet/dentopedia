---
title: "Finite Element Analysis of Implant Stability Quotient (ISQ) and Bone Stresses for Implant Inclinations of 0°, 15°, and 20°"
authors: Mario Ceddia, Tea Romasco, Giulia Marchioli, Luca Comuzzi, Alessandro Cipollina, Adriano Piattelli, Luciano Lamberti, Natalia Di Pietro, Bartolomeo Trentadue
year: 2025
date: 2025-04-02
doi: 10.3390/ma18071625
source: ceddia-2025-finite-element-analysis-of-implant.md
category: implants/isq
evidence_level: in-vitro
pdf_path: /Users/oracleneo/llm-wiki/papers/ceddia-2025-finite-element-analysis-of-implant.pdf
pdf_filename: ceddia-2025-finite-element-analysis-of-implant.pdf
source_collection: external
tags: [FEA, ISQ, implant-inclination, micro-mobility, bone-stress, primary-stability, polyurethane, in-vitro]
relations:
  - type: extends
    target: implants/isq/alimoradi-2024-acoustic-modal-analysis
    note: Both use FEA to derive ISQ from mechanical simulation; this paper uses micro-mobility vs acoustic modal analysis
  - type: extends
    target: implants/isq/bhandarkar-2023-rfa-mathematical-modeling-implant-stability
    note: Applies mathematical ISQ modeling principles to tilted implants with FEA validation
---

## Three-line Summary

FEA simulation study (Cyroth 4 mm × 15 mm implants, AoN Implants Srl) comparing FEA-derived ISQ via micro-mobility equation to in vitro Osstell RFA in D2 and D3 polyurethane bone blocks at 0°, 15°, and 20° inclinations.

FEA ISQ matched in vitro within 2.86% (D2 bone) and 1.27% (D3 bone); ISQ increased slightly with inclination (D2: 60.96→61.10; D3: 55.68→55.90 at 0°→20°); peri-implant cortical bone stress rose from 55.4 to 68.4 MPa at 20° inclination — below plastic deformation threshold (130 MPa).

FEA validated as a faster, cost-effective alternative to in vitro ISQ testing for various clinical inclination scenarios; generalizability limited by single implant brand/size and isotropic bone assumption.

## 세줄요약

Cyroth 임플란트(4 mm×15 mm)를 D2·D3 폴리우레탄 블록에 0°·15°·20° 경사 식립 후, 유한요소분석(FEA) 미세운동→ISQ 방정식 결과를 Osstell RFA 실측치와 비교한 in vitro 연구.

FEA ISQ 오차 D3 1.27%, D2 2.86%; 경사 증가 시 ISQ 소폭 상승(D2 60.96→61.10); 피질골 응력 55.4→68.4 MPa(20°), 피크 임플란트 응력 220.2 MPa — 소성변형 한계(130 MPa) 미만.

FEA로 다양한 경사 조건 ISQ 예측 가능성 검증; 단일 임플란트 사양·등방성 골 가정으로 일반화 제한.

## Summary

This in vitro study validated finite element analysis (FEA) as a method for predicting the implant stability quotient (ISQ) of tilted dental implants without physical testing. Cyroth implants (4 mm × 15 mm, Ti-6Al-4V) were virtually inserted at 0°, 15°, and 20° inclinations into 3D-modeled D2 and D3 bone blocks (18.5 × 30 × 30 mm, 1 mm cortical layer). A 100 N horizontal load was applied at the implant neck; micro-displacements were converted to ISQ via a validated equation (Pagliani et al.: ISQ = 74.94 − 5.21 × ln(Micromovements − 0.24)). FEA-derived ISQ differed from in vitro Osstell measurements by ≤2.86%, confirming strong agreement. ISQ increased modestly with inclination in both bone types, and peri-implant cortical bone stress increased but remained below the plastic deformation limit at all angles tested. The study establishes FEA as a clinically informative, resource-efficient screening tool for ISQ across variable inclination scenarios.

## Key Contributions

- Validates FEA micro-mobility pipeline for ISQ estimation in tilted implants (0°, 15°, 20°) with <3% error vs Osstell RFA
- Demonstrates that ISQ increases slightly with inclination under horizontal load — counter to intuitive concern about instability
- Quantifies peri-implant bone stress increase with inclination: cortical stress 55.4→68.4 MPa (D3 bone, 0°→20°), all below failure threshold
- Provides a user-friendly FEA framework adaptable for both laboratory and clinical inclination-planning scenarios

## Methodology

- **Design**: FEA simulation (ANSYS Workbench 2023 R1) + in vitro polyurethane comparison
- **Implant**: Cyroth 4 mm × 15 mm, Ti-6Al-4V (E=110 GPa, v=0.3)
- **Bone blocks**: D2 (E=5500 MPa) and D3 (E=1600 MPa); cortical layer 1 mm (E=16,000 MPa)
- **Inclinations**: 0°, 15°, 20°
- **Mesh**: 163,424 elements, 23,497 nodes; 0.5 mm global, 0.3 mm at implant-bone interface
- **Load**: 100 N horizontal (ISQ protocol, not masticatory)
- **Contact**: Frictional (μ=0.3) at bone-implant; fixed at implant-abutment
- **ISQ equation**: ISQ = 74.94 − 5.21 × ln(Micromovements − 0.24) [Pagliani et al.]
- **Validation**: Average FEA ISQ compared to in vitro Osstell Smart Peg No. 78 (Comuzzi et al. 2025)

## Results

| Condition | FEA ISQ | In vitro ISQ | Error |
|---|---|---|---|
| D2 bone average | 61.10 | 62.90 | 2.86% |
| D3 bone average | 55.78 | 56.50 | 1.27% |

| Bone / Inclination | ISQ (FEA) |
|---|---|
| D2 / 0° | 60.96 |
| D2 / 15° | 61.05 |
| D2 / 20° | 61.10 |
| D3 / 0° | 55.68 |
| D3 / 15° | 55.77 |
| D3 / 20° | 55.90 |

| Inclination | Cortical stress (D3) | Peak implant stress (D3) |
|---|---|---|
| 0° | 55.4 MPa | 150.1 MPa |
| 15° | 60.2 MPa | — |
| 20° | 68.4 MPa | 220.2 MPa |

All stresses remained below plastic deformation limits (cortical 130 MPa; trabecular 13 MPa).

## Related Papers

- [[implants/isq/alimoradi-2024-acoustic-modal-analysis]] — parallel FEA-to-ISQ approach via acoustic modal analysis; both validate computational ISQ prediction
- [[implants/isq/bhandarkar-2023-rfa-mathematical-modeling-implant-stability]] — mathematical modeling of RFA-ISQ relationship; foundational reference for ISQ modeling methodology
- [[implants/full-arch/bilgi-ozyetim-2025-biomechanical-comparison-implant-inclinations]] — FEA stress distribution for tilted implants in full-arch context (All-on-4)
