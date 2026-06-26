---
title: "Comparative Biomechanical Evaluation of Novel Screwless Retained Dental Implant Prosthesis: A 3D Finite Element Analysis"
authors: Ki-Sun Lee, Jaeyeol Kim, JaeHyung Lim, Jae-Jun Ryu
year: 2025
doi: 10.3390/jfb16020039
category: [prosthetic-materials]
pdf_path: /Users/oracleneo/llm-wiki/papers/lee-2025-screwless-hook-retained-implant-fea.pdf
pdf_filename: lee-2025-screwless-hook-retained-implant-fea.pdf
source_collection: external
---

## Why Ingested

기존 [[prosthetic-materials/hamed-2020-screw-vs-cement-implant-sr]]에서 스크류 유지 vs 시멘트 유지 비교가 주된 논쟁이었으나, 스크류와 시멘트를 모두 사용하지 않는 신규 후크(hook) 유지 방식(HRP)에 대한 FEA 근거가 없었음. 본 연구는 SCRP·SRP·HRP 세 시스템을 동일 조건에서 직접 비교한 최초 FEA 논문으로, HRP의 생역학적 타당성을 뒷받침하는 기초 근거를 제공함.

## One-line Summary

3D FEA (n=3 systems, 100N vertical/30° oblique): novel hook-retained prosthesis (HRP) showed lower implant stress (21.33 MPa) than screw-and-cement (SCRP, 32.91 MPa) and comparable to cementless screw-retained (SRP, 21.92 MPa), with similar peri-implant bone stress across all groups.

## 한줄요약

3D 유한요소분석에서 새로운 후크유지 보철(HRP)의 임플란트 최대 폰미제스 응력(21.33 MPa)이 스크류-시멘트 유지(SCRP, 32.91 MPa)보다 낮고 시멘트리스 스크류유지(SRP, 21.92 MPa)와 유사하여 HRP가 SCRP의 대안으로 타당함을 확인함.

## 1. Document Information

- **Journal**: Journal of Functional Biomaterials, 2025, 16, 39
- **Institution**: Korea University Ansan Hospital / Anam Hospital, Republic of Korea
- **Study type**: In vitro 3D Finite Element Analysis (FEA)
- **Published**: 22 January 2025

## 2. Key Contributions

- First biomechanical study on the novel screwless hook-retained prosthetic (HRP) system
- Demonstrates HRP generates lower implant fixture stress than SCRP under identical loading conditions
- Shows peri-implant bone stress is equivalent across all three retention systems
- Provides FEA evidence supporting HRP as an alternative to overcome cement- and screw-related complications

## 3. Methodology and Architecture

**Models**: Three implant prosthetic systems on NeoBiotech IS-III fixture (Ø4.0 × 10 mm) in lower second premolar region:
- **SCRP**: screw-and-cement-retained — multi abutment + cement-retained zirconia crown
- **SRP**: cementless screw-retained — Highness Digital Link abutment + link screw
- **HRP**: screwless hook-retained — YK abutment + cylinder + hook component + cement to cylinder only

**Software**: ANSYS Workbench 2022 R2; parabolic tetrahedral mesh; bonded surface contact; full osseointegration assumed.

**Material properties** (isotropic, homogeneous, linearly elastic):

| Component | E (GPa) | ν | Density (kg/m³) |
|---|---|---|---|
| Cancellous bone | 1.3 | 0.30 | 500 |
| Cortical bone | 13 | 0.30 | 1180 |
| Ti-Gr4 (fixture) | 103 | 0.33 | 4620 |
| Ti-6Al-4V (abutment parts) | 103 | 0.33 | 4620 |
| Zirconia (crown) | 200 | 0.31 | 6090 |

**Loading**: 100 N vertical; 100 N oblique at 30°. Outcome: maximum von Mises stress and strain.

## 4. Key Results and Benchmarks

**Vertical load (100 N):**

| Component | SCRP | SRP | HRP |
|---|---|---|---|
| Abutment stress | 18.96 MPa | 18.52 MPa | 23.49 MPa |
| Implant stress | **32.91 MPa** | 21.92 MPa | **21.33 MPa** |
| Bone stress | 10.43 MPa | 10.60 MPa | 10.54 MPa |
| Bone strain | 0.00108 mm/mm | 0.00110 mm/mm | 0.00109 mm/mm |

**Oblique load (100 N at 30°):**

| Component | SCRP | SRP | HRP |
|---|---|---|---|
| Abutment stress | 218.42 MPa | 185.07 MPa | 187.60 MPa |
| Implant stress | **262.24 MPa** | 187.64 MPa | **187.50 MPa** |
| Bone stress | 32.32 MPa | 32.22 MPa | 30.72 MPa |
| Bone strain | 0.00238 | 0.00237 | 0.00235 |

Key findings:
- SCRP showed highest implant fixture stress under both loading conditions
- HRP implant stress nearly identical to SRP; peri-implant bone stress slightly lower with HRP under oblique load
- HRP abutment component stress slightly higher than SCRP/SRP under vertical load (23.49 vs 18.96/18.52 MPa) but acceptable
- Stress concentration in all models occurred at implant crest under vertical load and at outer abutment under oblique load

## 5. Limitations and Future Work

- Pure FEA study — no clinical trials exist for HRP; in vivo validation needed
- Isotropic, homogeneous, and linearly elastic material assumptions (bone is viscoelastic and anisotropic)
- Full osseointegration assumed (no partial bonding simulation)
- Only one implant diameter/length tested (Ø4.0 × 10 mm)
- Single bone region modeled (lower second premolar); results may differ in maxillary or molar sites
- Hook retention long-term fatigue behavior not assessed

## 6. Related Work

- Hamed 2020 — screw vs cement SR+MA: [[prosthetic-materials/hamed-2020-screw-vs-cement-implant-sr]]
- Chan 2026 — FEA CAD/CAM zirconia vs 3D-printed hybrid: [[prosthetic-materials/chan-2026-fea-cad-cam-zirconia-3d-printed-hybrid]]

## 7. Glossary

- **SCRP**: Screw-and-cement-retained prosthetic system — conventional; abutment screw + cement crown
- **SRP**: Cementless screw-retained prosthetic system ("screw-in-screw") — link screw connects crown to abutment; no cement
- **HRP**: Hook-retained prosthetic system — novel; hook + cylinder connect crown to abutment; no abutment screw, no link screw; cement used only inside cylinder
- **Von Mises stress**: Scalar stress measure used in FEA to predict yielding in ductile materials
- **FEA**: Finite element analysis — numerical simulation of mechanical behavior
