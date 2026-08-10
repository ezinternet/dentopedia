---
title: "Finite Element Analysis of Platform Switching Effects on Stress Distribution in Posterior Implants Placed in Different Bone Types Under Axial and Oblique Loading Conditions"
authors: Kanika Yadav, Sandeep Kumar, Rajnish Aggarwal, Iqbal Kaur, Ankit Goyal, Rahul Sharma, Satyendra Banjara
year: 2025
doi: 10.7759/cureus.86821
category: [implants/mbl]
source_collection: pubmed-text
full_text: true
pmid: "40718348"
pmcid: "PMC12296853"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12296853/
text_path: /Users/oracleneo/llm-wiki/papers/yadav-2025-finite-element-analysis-platform-switching.txt
text_filename: yadav-2025-finite-element-analysis-platform-switching.txt
---

## Why Ingested

기존 wiki의 platform switching(PS) 근거는 임상 RCT/SR+MA 중심으로 "PS가 왜 MBL을 줄이는가"에 대한 생체역학적(biomechanical) 메커니즘 설명이 얕았던 gap. 본 FEA 연구는 그 기전을 응력분포(stress distribution)로 정량화해 보강하며, [[wiki/implants/mbl/juan-montesinos-2022-platform-switching-conventional-sr-ma]] 등 임상 결과의 생체역학적 근거를 제공.

## Three-line Summary

In vitro finite element analysis (FEA) study using CBCT-derived 3D models of posterior maxilla (D3 bone) and mandible (D2 bone), comparing platform-switched (PS, 3.2mm abutment on 4.2mm implant) vs non-platform-switched (NPS, matched 4.2mm abutment) configurations under 200N axial and 200N/30° oblique loading.

PS consistently reduced peak von Mises stress in cortical and cancellous bone compared to NPS, especially near the crestal region and under oblique loading, but shifted higher stress onto the implant, abutment, and abutment screw components — most pronounced in the maxilla under axial loading and in the mandible under oblique loading.

PS provides a biomechanical rationale for the clinically observed crestal-bone-preservation effect, but the higher internal stress on prosthetic components under PS suggests a need for more durable abutment materials/designs, particularly under oblique (non-axial) functional loading.

## 세줄요약

유한요소분석(Finite Element Analysis, FEA) in vitro 연구 — CBCT 기반 상악 구치부(D3골) · 하악 구치부(D2골) 3차원 모델에서 플랫폼 스위칭(Platform Switching, PS, 4.2mm 임플란트+3.2mm 지대주) vs 비-플랫폼 스위칭(Non-Platform-Switching, NPS, 4.2mm 지대주 매칭) 비교, 200N 축방향(axial) 및 200N/30° 사방향(oblique) 하중 적용.

PS는 NPS 대비 피질골·해면골, 특히 치조정 부위의 최대 von Mises 응력을 일관되게 낮췄고 이는 사방향 하중에서 더 뚜렷했으나, 임플란트·지대주·지대주나사에는 오히려 응력이 증가(상악에서는 축방향, 하악에서는 사방향 하중 시 최대).

PS의 임상적 치조정골 보존 효과에 생체역학적 근거를 제공하나, 보철 구성요소(특히 지대주)의 응력 증가는 사방향 하중 하에서 더 견고한 지대주 소재·설계가 필요함을 시사.

## 1. Document Information

- **Journal**: Cureus, 2025;17(6):e86821
- **DOI**: 10.7759/cureus.86821
- **Institutions**: Surendera Dental College and Research Institute (Sri Ganganagar, India), Dr. S.S. Tantia Medical College Hospital and Research Center

## 2. Key Contributions

- Directly addresses a gap the authors identify: "comparatively limited data evaluating the biomechanical impact of PS versus NPS under varied bone densities and loading conditions," and specifically oblique (non-axial) loading, which is more clinically representative of masticatory forces than axial-only FEA studies.
- Compares PS vs NPS across **both** bone-density contexts (D3 maxilla vs D2 mandible) and **both** loading directions (axial vs 30° oblique) in a single factorial design — 4 maxillary + 4 mandibular models.
- Quantifies the trade-off: PS lowers bone-side stress but raises implant/abutment/screw-side stress, with the direction and magnitude of the shift depending on jaw type and loading direction.
- Provides component-level (cortical bone, cancellous bone, implant, abutment, abutment screw) von Mises stress tables under both loading conditions — useful reference data absent from the clinical PS literature already in this wiki.

## 3. Methodology and Architecture

- **Design**: In vitro FEA study, 6-month span (Oct 2023–Mar 2024), Institutional Ethical Committee clearance waived (CBCT from institutional database, SDCRI/IEC/23/66).
- **Digital models**: 3D models of posterior maxilla (D3 bone) and mandible (D2 bone) built in CATIA V5 from CBCT scans. Bone block: 14mm height × 8mm mesiodistal × 8mm buccolingual. Maxilla: cortical 3.6mm (palatal 1.98mm/buccal 1.62mm), cancellous core 4.4mm. Mandible: cortical 4.8mm (lingual 2.54mm/buccal 2.26mm), cancellous core 3.2mm.
- **Implant/abutment**: titanium implant modeled on Adin Internal-Hex (Touareg-S), 11.5mm length × 4.2mm diameter, collar height 1.5mm, thread pitch 1.2mm, thread height 0.7mm, tip diameter 2mm. NPS = 4.2mm abutment (matched); PS = 3.2mm abutment. PFM crown (7.0mm height × 8.0mm buccolingual width) modeled for first molar.
- **Mesh/boundary conditions**: ANSYS Workbench, tetrahedral mesh, convergence confirmed at <5% variation in peak stress. Bone block base fully fixed (X/Y/Z). All interfaces modeled with perfect bonding (complete osseointegration assumed, no micromovement/slip).
- **Material properties** (isotropic, homogeneous, linear elastic): cortical bone E=13.7GPa (both jaws) ν=0.30; cancellous bone E=1.6GPa (maxilla)/5.5GPa (mandible) ν=0.30; titanium E=110GPa ν=0.35; mucosa E=10GPa ν=0.40; Ni-Cr (crown) E=203.6GPa ν=0.30.
- **Loading**: 200N axial (long-axis) and 200N oblique (30°), applied to the first molar; both representative of literature-standard functional occlusal forces.
- **Outcomes**: von Mises stress and strain, measured on cortical bone, cancellous bone, implant, abutment, abutment screw — 4 maxillary + 4 mandibular models total.

## 4. Key Results and Benchmarks

**Axial load (200N), von Mises max stress (MPa):**

| Structure | Maxilla NPS | Maxilla PS | Mandible NPS | Mandible PS |
|---|---|---|---|---|
| Cortical bone | 9.259 | 8.082 | 5.432 | 4.817 |
| Cancellous bone | 5.357 | 3.658 | 1.287 | 0.933 |
| Implant | 18.679 | 19.138 | 12.712 | 13.919 |
| Abutment | 22.310 | 23.699 | 21.628 | 22.892 |
| Abutment screw | 6.720 | 9.599 | 9.075 | 6.500 |

**Oblique load (200N/30°), von Mises max stress (MPa):**

| Structure | Maxilla NPS | Maxilla PS | Mandible NPS | Mandible PS |
|---|---|---|---|---|
| Cortical bone | 19.293 | 16.924 | 16.374 | 11.201 |
| Cancellous bone | 4.406 | 3.271 | 1.247 | 1.139 |
| Implant | 47.091 | 61.108 | 39.704 | 64.646 |
| Abutment | 47.811 | 96.632 | 46.678 | 106.072 |
| Abutment screw | 6.720 | 9.599 | 6.500 | 9.075 |

- PS consistently lowered cortical and cancellous bone stress in both jaws and both loading modes, with the largest relative reduction seen in mandibular cortical bone under oblique loading (16.374 → 11.201 MPa).
- PS consistently *raised* peak stress on implant, abutment, and (mostly) abutment screw components — most dramatically on the abutment under oblique loading (maxilla: 47.811→96.632 MPa; mandible: 46.678→106.072 MPa, roughly doubling).
- Oblique loading produced substantially higher stresses than axial loading across all structures in both designs.
- Maxilla (D3, lower-density bone) showed higher stress overall than mandible (D2) under axial loading; the pattern was more mixed under oblique loading depending on the structure.

## 5. Limitations and Future Work

- In vitro/computational FEA — assumes perfect bonding (100% osseointegration), homogeneous/isotropic linear-elastic materials, no frictional/micromovement modeling; does not replicate the biological/clinical environment.
- No fatigue or long-term cyclic loading analysis — single static loads only (200N axial, 200N/30° oblique).
- Authors note titanium yield strength (620–725 MPa) and Ni-Cr yield strength (415–620 MPa) are well above the observed peak stresses, suggesting the elevated implant/abutment stresses under PS may not translate into immediate mechanical failure, though this was not directly tested.
- Single implant system modeled (Adin Internal-Hex); results may not generalize to other connection geometries (e.g., external hex, conical).

## 6. Related Work

- [[wiki/implants/mbl/juan-montesinos-2022-platform-switching-conventional-sr-ma]] — clinical SR+MA confirming PS's MBL benefit; this FEA study supplies a biomechanical mechanism (lower crestal bone stress) consistent with that clinical finding.
- [[wiki/implants/mbl/strietzel-2015-platform-switching-mbl-sr-ma]] and [[wiki/implants/mbl/di-girolamo-2016-platform-switching-matching-sr-ma]] — clinical SR+MAs on PS bone-preservation; this paper's stress-distribution data offers the "why" behind their pooled effect sizes.
- [[wiki/prosthetic-materials/abutment-screw]] category — this study's finding of elevated abutment/screw stress under PS (especially oblique loading) is directly relevant to screw-loosening/preload literature in that subcategory.

## 7. Glossary

- **Von Mises stress**: a scalar stress measure combining all stress-tensor components, commonly used in FEA to predict yielding/failure risk under complex 3D loading.
- **Platform Switching (PS) / Non-Platform-Switching (NPS)**: PS uses an abutment narrower than the implant platform (here 3.2mm on 4.2mm); NPS uses a matched-diameter abutment.
- **D2/D3 bone (Misch and Judy classification)**: bone-density categories — D2 (denser, more trabecular structure, typical posterior mandible) vs D3 (lower density, more common in posterior maxilla).
- **Axial vs oblique loading**: axial = force along the implant's long axis (vertical bite force); oblique = force applied at an angle (here 30°), simulating lateral/off-axis masticatory forces.
- **Mesh convergence**: FEA validation step confirming further mesh refinement changes peak-stress results by <5%, indicating the mesh density is fine enough for reliable results.
