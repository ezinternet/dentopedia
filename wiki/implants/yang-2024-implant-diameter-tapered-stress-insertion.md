---
title: "Effects of Dental Implant Diameter and Tapered Body Design on Stress Distribution During Insertion"
authors: "Yang et al."
year: 2024
date: 2024-05-18
doi: "10.1016/j.medengphy.2024.104181"
source: yang-2024-implant-diameter-tapered-stress-insertion.md
category: [implants]
confidence: in-vitro
pdf_path: /Users/oracleneo/llm-wiki/papers/yang-2024-implant-diameter-tapered-stress-insertion.pdf
pdf_filename: yang-2024-implant-diameter-tapered-stress-insertion.pdf
source_collection: external
tags: [insertion-torque, tapered-implant, FEA, stress-distribution, implant-diameter, anchorage, primary-stability]
relations:
  - type: extends
    target: high-insertion-torque-primary-stability-crestal-bone-overview
  - type: reinforces
    target: baldi-2018-insertion-torque-isq-tapered-knife-edge
---

## One-line Summary
In vitro FEA + experimental study (4 Nobel Biocare implants, PU foam): tapered body design dominates normalized insertion torque (β₂=0.93, R²=0.90), distributing compressive stress further from threads compared to parallel-walled implants.

## 한줄요약
PU 폼 삽입 실험 + FEA (4종 임플란트): 정규화 삽입 토크는 테이퍼 바디 설계가 지배(β₂=0.93)하며, 병렬 벽 대비 나사산에서 더 멀리 압축 응력을 분산시킴.

## Summary
Yang et al. investigated why tapered implants generate higher insertion torque (IT) than parallel-walled designs, using a combined experimental and finite element analysis (FEA) approach with polyurethane foam bone surrogates. Two parallel-walled (P1 Ø3.5mm, P2 Ø4.3mm) and two tapered (T1 Ø3.5mm, T2 Ø4.3mm) Nobel Biocare implants were inserted at 12 rpm into corresponding straight pilot holes. By fitting IT to an analytical model and decomposing standardized regression coefficients, the study showed that raw IT is influenced by both diameter and taper (R²=0.77), but normalized IT (IT divided by radial interference δ) is dominated by taper design (β₂=0.93, p<0.001) while diameter contributes minimally (β₁=0.20). The tapered body creates compressive stress that propagates further from the thread tip, a distinct pattern not seen in parallel-walled implants. This provides the biomechanical mechanism underlying the clinically observed higher IT in tapered implants.

## Key Contributions
- Decouples diameter vs. taper design contributions to IT: for raw IT, diameter dominates; for normalized IT, taper dominates
- Quantifies taper body compression zone — stress distributed further from thread, explaining IT elevation independent of press-fit magnitude
- Validates explicit FEA insertion model against 2D-DIC surface strain (provides pre-clinical tool for implant design evaluation)
- Supports rationale for tapered design in low-density bone: more bone engagement per unit press-fit
- Identifies that high raw IT in larger-diameter implants is partly an artifact of greater absolute press-fit, not improved design efficiency

## Methodology
- 4 Nobel Biocare implants: parallel-walled (Ø3.5, Ø4.3mm) and tapered (Ø3.5, Ø4.3mm)
- Substrate: rigid polyurethane foam ASTM F1839-08 (no cortical layer, single density)
- Insertion: MACH-1 tester, 12 rpm constant angular + axial speed, n=5 per implant
- Measurements: IT + depth at 100 Hz; 2D-DIC surface strain; explicit FEA (Abaqus 2017)
- Analytical model: IT = f(δ, implant geometry); R²=0.88–1.0
- Standardized regression: β₁ (diameter) and β₂ (taper) reported for IT, normalized IT, effective force F′, effective pressure p′

## Results
- Raw IT: β₁ diameter=0.78 (p<0.001), β₂ taper=0.41 (p=0.0024), R²=0.77
- Normalized IT: β₁ diameter=0.20 (p=0.020), β₂ taper=0.93 (p<0.001), R²=0.90
- Effective pressure p′: taper β₂=0.97 (p<0.001) — tapered body generates higher unit pressure
- Tapered implants: FEA shows compressive stress zone distal to thread tip propagating into surrounding foam
- Parallel-walled implants: stress concentrated near thread, no distal compression zone

## Related Papers
- [[implants/isq/baldi-2018-insertion-torque-isq-tapered-knife-edge]] — clinical IT vs ISQ study with tapered knife-edge implants; this paper provides mechanical explanation for why tapered design generates higher IT
- [[overviews/high-insertion-torque-primary-stability-crestal-bone-overview]] — synthesis on IT clinical consequences; this study provides the biomechanical rationale
- [[implants/coyac-2019-preclinical-model-links-osseo-densification-misfit]] — biological consequence: tapered compression/misfit can cause osteocyte death (animal model)
- [[implants/isq/rosasdiaz-2024-insertion-compression-primary-stability]] — in vitro: under-milling drives IT but not ISQ; this paper explains the mechanism (compression zone)
