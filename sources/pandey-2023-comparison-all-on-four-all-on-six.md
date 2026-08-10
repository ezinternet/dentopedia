---
title: "Comparison between All-on-Four and All-on-Six Treatment Concepts on Stress Distribution for Full-Mouth Rehabilitation Using Three-Dimensional Finite Element Analysis: A Biomechanical Study"
authors: Aishwarya Pandey, Farhan Durrani, Sanjay Kumar Rai, Nishant Kumar Singh, Preeti Singh, Rati Verma, Jitendra Kumar
year: 2023
doi: 10.4103/jisp.jisp_278_22
category: [implants]
pdf_path: /Users/oracleneo/llm-wiki/papers/pandey-2023-comparison-all-on-four-all-on-six.pdf
pdf_filename: pandey-2023-comparison-all-on-four-all-on-six.pdf
source_collection: external
---

## Why Ingested

기존 [[wiki/implants/cabbarova-2026-all-on-four-six-framework-fea]]가 프레임워크 소재(PEEK/Ti/Zr 등) 변수를 더해 All-on-4 vs All-on-6를 비교한 반면, 본 Pandey 2023 연구는 프레임워크 재료 변수 없이 순수하게 임플란트 개수(4 vs 6)만을 변수로 둔 초기 FEA 근거로, 두 결과의 일관성(All-on-6 우위)을 재확인하는 근거 축적 목적으로 인제스트.

## Three-line Summary

In vitro 3D finite element analysis (FEA) study comparing All-on-Four (Model A, 2 axial + 2 tilted 17° implants) versus All-on-Six (Model B, 6 vertical implants) for edentulous mandible full-arch rehabilitation, under vertical/horizontal 100 N and oblique 141 N (45°) loading.

All-on-Six showed markedly lower maximum principal stress on cortical bone and implants across all loading conditions (e.g., oblique load: cortical bone 5.47 MPa vs 139.85 MPa, all implants 35.51 MPa vs 244.43 MPa), but slightly higher stress on trabecular bone under vertical/horizontal loading (2.0 MPa vs 1.28 MPa vertical).

All-on-Six is biomechanically more favorable overall and may be preferred in biomechanical-risk cases (bruxism, low bone quality), while All-on-Four with a rigid framework remains a viable alternative in atrophic ridges; limitation is idealized FEA assumptions (100% osseointegration, no implant-abutment gap, isotropic homogeneous materials) that do not fully reflect clinical variability.

## 세줄요약

In vitro 3차원 유한요소분석(FEA) 연구로, 무치악 하악에서 All-on-Four(모델 A, 축성 임플란트 2개+17° 경사 임플란트 2개)와 All-on-Six(모델 B, 수직 임플란트 6개)를 수직/수평 100N, 사면 141N(45°) 하중 조건에서 비교.

All-on-Six가 전 하중 조건에서 피질골·임플란트의 최대주응력(σmax)이 뚜렷이 낮았으나(예: 사면하중 시 피질골 5.47 vs 139.85 MPa, 전체 임플란트 35.51 vs 244.43 MPa), 해면골에서는 수직/수평 하중 시 오히려 All-on-Six가 소폭 높음(수직 2.0 vs 1.28 MPa).

전반적으로 All-on-Six가 생역학적으로 더 유리하며 생역학적 위험군(이갈이, 저품질골)에서 선호될 수 있으나, 위축된 치조제에서는 강성 프레임워크를 동반한 All-on-Four도 대안 가능; FEA의 이상화된 가정(100% 골유착, 임플란트-지대주 간극 없음, 등방성 균질 재료)은 임상적 변동성을 완전히 반영하지 못하는 한계가 있음.

## 1. Document Information

- **Title**: Comparison between all-on-four and all-on-six treatment concepts on stress distribution for full-mouth rehabilitation using three-dimensional finite element analysis: A biomechanical study
- **Authors**: Aishwarya Pandey, Farhan Durrani, Sanjay Kumar Rai, Nishant Kumar Singh, Preeti Singh, Rati Verma, Jitendra Kumar
- **Affiliations**: Division of Periodontology, Faculty of Dental Science, Institute of Medical Sciences, Banaras Hindu University, Varanasi, India; School of Biomedical Engineering, IIT-BHU; Dept. of Biomedical Engineering, NIT Raipur, India
- **Journal**: Journal of Indian Society of Periodontology, Volume 27, Issue 2, March-April 2023, pp. 180-188
- **DOI**: 10.4103/jisp.jisp_278_22
- **Published**: 04-Mar-2023 (Submitted 04-Jun-2022, Accepted 27-Nov-2022)
- **Study type**: In vitro biomechanical study using 3D finite element analysis (FEA)
- **License**: Open access, CC BY-NC-SA 4.0

## 2. Key Contributions

- Direct FEA comparison of two treatment concepts for edentulous mandible full-arch rehabilitation: All-on-Four (with 17°-tilted distal implants) vs All-on-Six (all vertical implants), using a patient-CT-derived 3D mandible model.
- Quantified maximum principal stress (σmax) across cortical bone, trabecular bone, all implants, and specific implant positions (distal-most, central/anterior) under three independent loading conditions (vertical, horizontal, oblique).
- Identified a trade-off: All-on-Six reduces cortical bone/implant stress substantially but slightly increases trabecular bone stress relative to All-on-Four under vertical/horizontal loads.
- Confirmed implant-neck stress concentration in both models, consistent with prior literature.
- Frames clinical decision-making around biomechanical risk stratification — recommending more implants (All-on-Six) for higher-risk patients (bruxism, low bone quality).

## 3. Methodology and Architecture

- **Model fabrication**: Patient CT data used to reconstruct an edentulous mandible in MIMICS 19.0 (Materialise). Semi-autonomic region-growing algorithm interpolated 2D DICOM data into a 3D model; anterior mandible remeshed at 0.5 mm triangle edge length; NURBS surface patching converted the surface model to a solid model. A 1.006 mm cortical bone layer was defined around a cancellous core.
- **Implant design**: Implants modeled in Creo Parametric 5.0 (student version), dimensions from literature/catalog of implant used clinically (RAPID DENTIN, Dental Implants Technologies Ltd, Israel).
  - Model A (All-on-4): 2 vertical implants (lateral incisor position, 3.3×11.5 mm) + 2 implants tilted 17° distally (second premolar position, 3.8×11.5 mm).
  - Model B (All-on-6): 6 vertical implants (lateral incisor 3.3×11.5 mm ×2, second premolar 3.8×11.5 mm ×2, second molar 4.2×11.5 mm ×2).
  - Titanium abutments (3 mm high): straight for vertical implants, 17°-angled for tilted implants in Model A; all straight in Model B. Rigid cobalt-chromium framework (3 mm thick, 10 mm long arc shape) joined to abutments.
- **FEA software**: ANSYS (ANSYS Inc.). Mesh: linear tetrahedral elements; element size 0.5 mm for cortical/trabecular bone, 0.2 mm for abutment/framework/implant. Model A: 1,039,145 nodes / 605,946 elements. Model B: 2,182,276 nodes / 1,384,964 elements.
- **Material properties** (isotropic, linearly elastic, homogeneous): Ti Grade 23 (Ti6Al4V-ELI) E=113,800 MPa; cortical bone E=13,700 MPa; trabecular bone E=1,370 MPa; cobalt-chromium E=218,000 MPa (all Poisson's ratio 0.3).
- **Boundary conditions**: Fully osseointegrated interface assumed (no crestal bone loss, no implant-abutment gap, perfect fit).
- **Loading conditions** (applied individually to all implants):
  1. Vertical load, 100 N
  2. Horizontal load, 100 N
  3. Oblique load, 141 N at 45° buccolingual
- Outcome measured: maximum principal stress (σmax), analyzed via UMAT subroutine; visualized as color-coded stress maps (red = highest).

## 4. Key Results and Benchmarks

Maximum principal stress (MPa) by component and loading condition:

| Component | Model | Vertical (100N) | Horizontal (100N) | Oblique 45° (141N) |
|---|---|---|---|---|
| Cortical bone | A (4) | 77.56 | 16.11 | 139.85 |
| Cortical bone | B (6) | 8.76 | 6.87 | 5.47 |
| Trabecular bone | A (4) | 1.28 | 0.88 | 1.52 |
| Trabecular bone | B (6) | 2.00 | 1.94 | 0.96 |
| All implants | A (4) | 438.85 | 52.21 | 244.43 |
| All implants | B (6) | 21.80 | 37.75 | 35.51 |
| Left distal-most implant | A (4) | 13.87 | 47.64 | 49.96 |
| Left distal-most implant | B (6) | 21.08 | 23.66 | 22.25 |
| Right distal-most implant | A (4) | 18.00 | 49.39 | 244.33 |
| Right distal-most implant | B (6) | 14.32 | 37.75 | 31.51 |

- All-on-Six consistently showed lower σmax on cortical bone and implants across all loading conditions.
- All-on-Four showed lower σmax on trabecular bone under vertical and horizontal loading (opposite trend vs cortical bone).
- Stress consistently concentrated at the implant neck in both models across all loading conditions.
- All-on-Six's additional distal implant (position 6) provided extra support, distributing stress over a greater area (implant #6 to #1) versus the cantilevered distal implant in All-on-Four.
- Reported physiological overload thresholds from literature: cortical bone 100–130 MPa, trabecular bone ~5 MPa (ultimate bone strength). All values in both models were below these pathologic thresholds.

## 5. Limitations and Future Work

- Idealized FEA assumptions: 100% bone-to-implant contact (fully osseointegrated), no crestal bone loss, perfect fit at implant-abutment and prosthesis-abutment interfaces, rigid (unmodeled) screw connections.
- Materials treated as isotropic, linearly elastic, and homogeneous — does not capture anisotropic bone behavior or viscoelastic soft tissue.
- Static, single-instance loading (not cyclic/fatigue) — does not model long-term loading history or implant micromotion.
- Absolute stress values were explicitly stated by authors as intended for comparative purposes only, not as generalizable clinical thresholds.
- No consideration of framework material variation (contrast with the later Cabbarova 2026 study, which added framework material as a second variable).
- Study did not include cantilever-length variation analysis directly, though discussion draws on prior cantilever-stress literature.

## 6. Related Work

- Malo et al. (2003) — original "All-on-Four" immediate-function concept with Brånemark system implants.
- Bhering et al. (2016) — All-on-4 vs All-on-6 framework material FEA in atrophic maxilla (precursor to Cabbarova 2026 approach).
- Silva et al. (2010) — stress patterns in 4- vs 6-implant-supported prostheses, found similar stress distribution patterns but reduced von Mises stress with more implants; cantilever increased stress significantly.
- Özdemir Doğan et al. (2014) — 6-implant model outperformed 4-implant model in mandible (minimal principal stress, titanium framework only).
- Almeida et al. — lower max/min principal stress with 6-implant vs 4-implant model (simplified models, no anatomical framework/implant threads).
- Demenko et al. — calculated ultimate oblique masticatory force (118.2 N at 75° to occlusal plane), informing the loading protocol design rationale.

## 7. Glossary

- **FEA (Finite Element Analysis)**: numerical simulation method dividing a structure into small elements to compute stress/strain/displacement under load.
- **σmax (Maximum principal stress)**: the largest normal stress value at a point, used as the primary outcome metric in this study.
- **All-on-Four**: full-arch implant-supported fixed prosthesis concept using 4 implants (2 axial anterior + 2 distally tilted posterior) to avoid vital anatomical structures and eliminate the need for bone grafting.
- **All-on-Six**: full-arch implant-supported fixed prosthesis concept using 6 vertically placed implants, extending support to the molar region and eliminating cantilevers.
- **Cortical bone / trabecular (cancellous) bone**: dense outer bone layer vs porous inner bone layer, each with distinct mechanical properties (Young's modulus).
- **Young's modulus**: measure of a material's stiffness (resistance to elastic deformation under load).
- **Osseointegration**: direct structural and functional connection between living bone and the surface of a load-bearing implant.
- **Cantilever**: the unsupported extension of a prosthesis beyond the terminal implant, a known stress concentrator.
