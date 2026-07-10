---
title: "Comparison between All-on-Four and All-on-Six Treatment Concepts on Stress Distribution for Full-Mouth Rehabilitation Using Three-Dimensional Finite Element Analysis: A Biomechanical Study"
authors: Aishwarya Pandey, Farhan Durrani, Sanjay Kumar Rai, Nishant Kumar Singh, Preeti Singh, Rati Verma, Jitendra Kumar
year: 2023
date: 2023-03-04
doi: 10.4103/jisp.jisp_278_22
source: pandey-2023-comparison-all-on-four-all-on-six.md
category: [implants]
confidence: in-vitro
pdf_path: /Users/oracleneo/llm-wiki/papers/pandey-2023-comparison-all-on-four-all-on-six.pdf
pdf_filename: pandey-2023-comparison-all-on-four-all-on-six.pdf
source_collection: external
tags: [all-on-four, all-on-six, finite-element-analysis, tilted-implants, edentulous-mandible, biomechanics, stress-distribution]
---

## Three-line Summary

In vitro 3D finite element analysis (FEA) study comparing All-on-Four (Model A, 2 axial + 2 tilted 17° implants) versus All-on-Six (Model B, 6 vertical implants) for edentulous mandible full-arch rehabilitation, under vertical/horizontal 100 N and oblique 141 N (45°) loading.

All-on-Six showed markedly lower maximum principal stress on cortical bone and implants across all loading conditions (e.g., oblique load: cortical bone 5.47 MPa vs 139.85 MPa, all implants 35.51 MPa vs 244.43 MPa), but slightly higher stress on trabecular bone under vertical/horizontal loading (2.0 MPa vs 1.28 MPa vertical).

All-on-Six is biomechanically more favorable overall and may be preferred in biomechanical-risk cases (bruxism, low bone quality), while All-on-Four with a rigid framework remains a viable alternative in atrophic ridges; limitation is idealized FEA assumptions (100% osseointegration, no implant-abutment gap, isotropic homogeneous materials) that do not fully reflect clinical variability.

## 세줄요약

In vitro 3차원 유한요소분석(FEA) 연구로, 무치악 하악에서 All-on-Four(모델 A, 축성 임플란트 2개+17° 경사 임플란트 2개)와 All-on-Six(모델 B, 수직 임플란트 6개)를 수직/수평 100N, 사면 141N(45°) 하중 조건에서 비교.

All-on-Six가 전 하중 조건에서 피질골·임플란트의 최대주응력(σmax)이 뚜렷이 낮았으나(예: 사면하중 시 피질골 5.47 vs 139.85 MPa, 전체 임플란트 35.51 vs 244.43 MPa), 해면골에서는 수직/수평 하중 시 오히려 All-on-Six가 소폭 높음(수직 2.0 vs 1.28 MPa).

전반적으로 All-on-Six가 생역학적으로 더 유리하며 생역학적 위험군(이갈이, 저품질골)에서 선호될 수 있으나, 위축된 치조제에서는 강성 프레임워크를 동반한 All-on-Four도 대안 가능; FEA의 이상화된 가정은 임상적 변동성을 완전히 반영하지 못하는 한계가 있음.

## Summary

This in vitro biomechanical study used 3D finite element analysis (FEA) to compare two full-mouth rehabilitation concepts for the edentulous mandible: the "All-on-Four" concept (2 vertical anterior implants + 2 distally tilted implants at 17°) versus the "All-on-Six" concept (6 vertically placed implants extending to the second molar). A patient-CT-derived mandible model was rebuilt in MIMICS, implants and rigid cobalt-chromium frameworks were designed and meshed in ANSYS, and three independent loading conditions (100 N vertical, 100 N horizontal, 141 N oblique at 45°) were applied to evaluate maximum principal stress (σmax) on cortical bone, trabecular bone, and implants. All-on-Six consistently produced lower stress on cortical bone and implants, attributable to the additional distal implant eliminating the cantilever effect and distributing load over a larger area; however, trabecular bone stress was slightly higher for All-on-Six under vertical and horizontal loads. All values in both models remained below literature-reported pathologic thresholds (cortical bone 100–130 MPa, trabecular bone ~5 MPa).

## Key Contributions

- Direct head-to-head FEA comparison of All-on-Four (with 17°-tilted distal implants) vs All-on-Six (all-vertical) implant configurations for the edentulous mandible, using a clinically-derived 3D model and a rigid cobalt-chromium framework.
- Quantified σmax across cortical bone, trabecular bone, all implants, and individual implant positions (distal-most left/right, central/anterior left/right) under three loading directions.
- Demonstrated the trade-off between cortical/implant stress reduction (favoring All-on-Six) and trabecular bone stress (slightly favoring All-on-Four) — a nuance not captured by single-metric comparisons.
- Reinforced that implant-neck stress concentration occurs regardless of implant number/tilt, consistent with prior FEA literature.
- Provides a biomechanical-risk framework for clinical decision-making: more implants (All-on-Six) recommended when risk factors (bruxism, low bone quality) are present.

## Methodology

- **Model**: Patient CT-derived edentulous mandible reconstructed in MIMICS 19.0; region-growing algorithm interpolated DICOM data into 3D geometry; NURBS surface patching converted to solid model; 1.006 mm cortical bone layer defined around cancellous core.
- **Implants**: Designed in Creo Parametric 5.0, dimensions matched to a clinically used implant system (RAPID DENTIN, Israel).
  - Model A (All-on-4): 2 vertical implants (lateral incisor, 3.3×11.5 mm), 2 implants tilted 17° distally (second premolar, 3.8×11.5 mm), straight + 17°-angled titanium abutments.
  - Model B (All-on-6): 6 vertical implants (lateral incisor 3.3×11.5 mm ×2, second premolar 3.8×11.5 mm ×2, second molar 4.2×11.5 mm ×2), all straight abutments.
  - Rigid cobalt-chromium arc framework (3 mm thick, 10 mm long) joined to all abutments.
- **FEA (ANSYS)**: Linear tetrahedral mesh; 0.5 mm elements for bone, 0.2 mm for abutment/framework/implant. Model A: 1,039,145 nodes/605,946 elements; Model B: 2,182,276 nodes/1,384,964 elements. Materials isotropic/linearly elastic/homogeneous (Ti6Al4V-ELI E=113,800 MPa; cortical bone E=13,700 MPa; trabecular bone E=1,370 MPa; Co-Cr E=218,000 MPa; all ν=0.3). Fully osseointegrated boundary condition assumed (no crestal bone loss, perfect fit, no implant-abutment gap).
- **Loading**: Applied individually to all implants — (1) 100 N vertical, (2) 100 N horizontal, (3) 141 N oblique at 45° buccolingual. Outcome: maximum principal stress (σmax), analyzed via UMAT subroutine.

## Results

| Component | Model | Vertical (100N) | Horizontal (100N) | Oblique 45° (141N) |
|---|---|---|---|---|
| Cortical bone | All-on-4 | 77.56 MPa | 16.11 MPa | 139.85 MPa |
| Cortical bone | All-on-6 | 8.76 MPa | 6.87 MPa | 5.47 MPa |
| Trabecular bone | All-on-4 | 1.28 MPa | 0.88 MPa | 1.52 MPa |
| Trabecular bone | All-on-6 | 2.00 MPa | 1.94 MPa | 0.96 MPa |
| All implants | All-on-4 | 438.85 MPa | 52.21 MPa | 244.43 MPa |
| All implants | All-on-6 | 21.80 MPa | 37.75 MPa | 35.51 MPa |

- All-on-Six showed lower σmax on cortical bone and implants across all three loading conditions.
- All-on-Four showed lower σmax on trabecular bone under vertical and horizontal loading — an inverted trend versus cortical bone/implant stress.
- Maximum stress consistently localized at the implant neck in both models, for all loading conditions.
- The extra distal implant in All-on-Six (position 6) eliminated the cantilever seen in All-on-Four, spreading stress over a larger area (implant #1 to #6) and reducing stress notably at the most mesial implant.
- All measured stress values in both models were below literature-derived pathologic overload thresholds (cortical bone 100–130 MPa; trabecular bone ~5 MPa), meaning neither design was predicted to cause bone failure under the tested loads.
- Authors conclude All-on-Six is the more favorable biomechanical option overall, particularly for biomechanical-risk patients (bruxism, low-quality bone); All-on-Four remains a reasonable alternative in atrophic ridges, especially with a rigid framework.

## Related Papers

- [[implants/cabbarova-2026-all-on-four-six-framework-fea]] — later FEA study (2026) extending the same All-on-4 vs All-on-6 comparison with 6 framework materials (Ti, Zr, PEEK, PEKK, Trilor, Trinia); reinforces this study's core finding that All-on-6 distributes stress more favorably (80–87% framework stress reduction reported), and adds that rigid frameworks (Ti/Zr) are essential regardless of implant number.
- [[implants/szabo-2022-all-on-four-tilted-distal-implants-mbl]] — clinical (non-FEA) marginal bone loss outcomes for tilted distal implants in the All-on-Four concept.
- [[implants/murat-2025-all-on-4-implant-angulation-load-direction-fea]] — FEA study on implant angulation and load direction effects specifically within the All-on-4 configuration.
- [[implants/baki-2025-all-on-4-trefoil-five-implant-fea]] — FEA comparison involving All-on-4/Trefoil/five-implant configurations, extending the implant-number biomechanics question.
