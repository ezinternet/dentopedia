---
title: "Stress distribution pattern of screw-retained restorations with segmented vs. non-segmented abutments: A finite element analysis"
authors: Shima Aalaei, Zahra Rajabi Naraki, Fatemeh Nematollahi, Elaheh Beyabanaki, Afsaneh Shahrokhi Rad
year: 2017
doi: 10.15171/joddd.2017.027
category: [prosthetic-materials]
pdf_path: /Users/oracleneo/llm-wiki/papers/aalaei-2017-segmented-nonsegmented-abutment-fea.pdf
pdf_filename: aalaei-2017-segmented-nonsegmented-abutment-fea.pdf
source_collection: external
---

## Why Ingested

세그먼트형(분리형) 어버트먼트와 비세그먼트형(일체형) 어버트먼트가 나사 유지형 보철물의 골 응력 분포에 미치는 영향을 FEA로 비교한 드문 연구. 기존 [[prosthetic-materials/velez-2020-implant-connection-abutment-design-screw]]가 임플란트 연결부·어버트먼트 디자인 일반론을 다루지만, 분절형 vs 비분절형 나사 어버트먼트 간 골 응력 차이를 직접 정량화한 데이터는 없어 보강 근거로 활용.

## One-line Summary

3D FEA study (Straumann 4.1×10 mm, mandibular molar): segmented abutment reduced peri-implant bone stress (31 vs 126 MPa at 45° angular load) but increased abutment screw stress (430 vs 375 MPa) compared to non-segmented abutment.

## 한줄요약

3D 유한요소분석: 세그먼트형 어버트먼트는 각도 하중 시 골 응력을 대폭 감소(31 vs 126 MPa)시키지만 어버트먼트 나사 응력은 다소 증가(430 vs 375 MPa)시킨다.

## 1. Document Information

- **Journal**: Journal of Dental Research, Dental Clinics, Dental Prospects (JODDD) 2017;11(3):149-155
- **DOI**: 10.15171/joddd.2017.027
- **Published**: 2017 (accepted 4 July 2017)
- **Study type**: In vitro 3D finite element analysis (FEA)
- **Institution**: Shahid Beheshti University of Medical Sciences (Tehran), Qazvin University, Harvard School of Dental Medicine

## 2. Key Contributions

- First FEA study to directly compare segmented vs. non-segmented screw-retained abutments on stress distribution in both peri-implant bone AND abutment screws
- Demonstrated a critical trade-off: non-segmented abutment protects the screw but transfers far more stress to bone (especially under angular load)
- Micro-strain data supports segmented abutment advantage: 2400 vs 9400 microstrain under angular loading (non-segmented nearly 4× higher)
- Clinically relevant implication: for angular/off-axis loading situations (realistic oral function), segmented abutment better protects crestal bone

## 3. Methodology and Architecture

**FEA model:**
- CT-based 3D mandibular first molar model
- Implant: Straumann regular neck tissue-level, 4.1 mm diameter × 10 mm length (4.8 mm platform)
- Cortical bone: 1 mm thick buccal and lingual; cancellous bone core
- Two separate models: (1) segmented abutment (RNSynocta 1.5, 1.5-mm height + Synocta Gold coping); (2) non-segmented abutment (RNSynocta Gold Abutment, 4.3-mm height)
- Crown: PFM (porcelain-fused-to-metal), 12 mm mesiodistal × 9 mm buccolingual; 1-mm uniform porcelain on high-noble alloy framework

**Loading conditions:**
- 100 N vertical (axial)
- 100 N angular (45° oblique)
- Applied at central fossa; complete osseointegration assumed

**Analysis software:** ANSYS Workbench v12.0.1; von Mises stress criterion; parabolic tetrahedral elements (segmented: 233,057 elements / 373,095 nodes; non-segmented: 201,172 elements / 325,080 nodes)

**Material properties (Table 1):**
- Cancellous bone: E = 1370 MPa, ν = 0.30
- Cortical bone: E = 13700 MPa, ν = 0.30
- Porcelain: E = 69000 MPa, ν = 0.28
- High-noble alloy: E = 100000 MPa, ν = 0.30
- Titanium: E = 103400 MPa, ν = 0.33

All materials: homogeneous, isotropic, linearly elastic. Screw-implant/abutment contact: frictional; all other surfaces: bonded.

## 4. Key Results and Benchmarks

**Peri-implant bone stress (von Mises, MPa):**

| Loading | Segmented | Non-segmented |
|---|---|---|
| Vertical 100 N | 21 MPa (mesiolingual) | 24 MPa (buccal) |
| Angular 100 N (45°) | 31 MPa (mesiolingual) | 126 MPa (distolingual) |

**Abutment screw stress (von Mises, MPa):**

| Loading | Segmented | Non-segmented |
|---|---|---|
| Vertical 100 N | 100 MPa | 87 MPa |
| Angular 100 N (45°) | 430 MPa | 375 MPa |

**Micro-strain in peri-implant bone:**

| Loading | Segmented | Non-segmented |
|---|---|---|
| Vertical | 2200 μɛ | 4400 μɛ |
| Angular | 2400 μɛ | 9400 μɛ |

**Pattern**: Maximum stress always concentrated at implant neck. Stress decreased with distance from implant. Angular loading produced markedly higher stresses in both models. The non-segmented abutment showed dramatically higher bone stress under angular load (4× greater than segmented).

**Interpretation**: The additional micro-motion permitted by segmented abutment design (two-piece with separate coping) allows stress absorption/distribution at the component junction, reducing force transfer to crestal bone — consistent with Rangert et al.'s flexibility principle.

## 5. Limitations and Future Work

- Static FEA; does not model dynamic/cyclic occlusal forces or fatigue
- Homogeneous, isotropic, linearly elastic material assumption; bone is anisotropic and viscoelastic
- Complete osseointegration assumed (no consideration of healing phase or bone quality variability)
- Only one implant system (Straumann); results may differ with other designs/connections
- Mandibular first molar only; different bone and load patterns in maxillary or anterior sites
- No comparison with cement-retained restorations
- Did not model abutment screw preload/torque, which significantly affects real screw stress distribution
- Clinical outcomes data needed to validate FEA predictions

## 6. Related Work

- Rangert et al. (1997): implant component flexibility reduces stress — framework for interpreting segmented abutment benefit
- Ochiai et al. (photoelastic): non-segmented abutments under vertical loading create more non-lateral bone stress than segmented
- Heckmann et al.: no significant difference in fit precision between screw-retained and cement-retained; bone stress similar
- Numerous FEA studies on implant biomechanics (cited refs 19–33 in paper) addressing various abutment/connection parameters

## 7. Glossary

- **세그먼트형 어버트먼트 (Segmented abutment)**: Two-piece design — separate abutment + coping/crown; screw connects coping to abutment
- **비세그먼트형 어버트먼트 (Non-segmented abutment)**: One-piece design — crown and abutment fabricated as single unit connected directly to implant
- **von Mises 응력 (von Mises stress)**: Equivalent stress criterion used to predict yielding/failure in ductile materials; used here for FEA bone stress evaluation
- **미변형률 (Micro-strain, μɛ)**: Deformation per unit length ×10⁻⁶; bone remodeling threshold ~1500–3000 μɛ (physiologic); >3000 μɛ = overload risk
- **나사 유지형 보철물 (Screw-retained restoration)**: Implant crown retained by screw rather than cement; retrievable
- **FEA (Finite Element Analysis, 유한요소분석)**: Computational method dividing a structure into small elements to calculate stress/strain distribution
