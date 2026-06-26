---
title: "Finite Element Analysis of Dental Implants with Zirconia Crown Restorations: Conventional Cement-Retained vs. Cementless Screw-Retained"
authors: Jae-Hyun Lee, Ho Yeol Jang, Su Young Lee
year: 2021
doi: 10.3390/ma14102666
category: [prosthetic-materials]
pdf_path: /Users/oracleneo/llm-wiki/papers/lee-2021-cement-vs-cementless-screw-retained-fea.pdf
pdf_filename: lee-2021-cement-vs-cementless-screw-retained-fea.pdf
source_collection: external
---

## Why Ingested

기존 [[prosthetic-materials/hamed-2020-screw-vs-cement-implant-sr]]는 임상 SR로 나사유지형의 치주·합병증 우위를 보여주나, FEA 관점의 응력분포 차이는 다루지 않는다. 본 연구(Lee 2021)는 신형 시멘트-프리 나사유지형(base abutment + titanium link screw) 지르코니아 크라운이 기존 시멘트 유지형 대비 임플란트·골 응력을 수치적으로 얼마나 줄이는지를 3D FEA로 정량화해, 유지 방식 선택의 생역학적 근거를 보강한다.

## One-line Summary

3D FEA study (n=2 models, mandibular premolar) found cement-retained zirconia implant crowns generated substantially higher von Mises stress in both the implant and surrounding bone than a novel cementless screw-retained design under 100 N vertical and 30° oblique loading.

## 한줄요약

3D 유한요소분석 연구에서 기존 시멘트 유지형 지르코니아 임플란트 크라운이 신형 시멘트-프리 나사유지형(베이스 어버트먼트+링크 스크류)보다 임플란트와 주변골에 유의하게 높은 응력을 발생시킴.

## 1. Document Information

- **Journal**: Materials 2021, 14, 2666
- **Study type**: 3D finite element analysis (in silico/in vitro)
- **Location**: Seoul National University / Catholic University of Korea
- **Funding**: Not specified

## 2. Key Contributions

- First FEA directly comparing conventional cement-retained vs. novel **cementless** screw-retained (base abutment + titanium link screw, "screw-in-screw") zirconia implant crowns
- Provides quantitative von Mises stress and strain data for both implant and supporting bone under two clinically relevant loading conditions
- Demonstrates that the cementless screw-retained design distributes occlusal forces more favorably across the implant-bone complex

## 3. Methodology and Architecture

**Models**: Two 3D solid models of mandibular second premolar region built in SolidWorks, analyzed in ANSYS Workbench:
- Model A: Cement-retained zirconia crown on titanium abutment (4.5×11 mm fixture, 5.5×11.25 mm abutment, 2.3×9.5 mm screw, 8×10 mm crown)
- Model B: Cementless screw-retained zirconia crown with titanium link (same fixture, 5.7×10.7 mm abutment, 4.3×3.5 mm link, 2.3×8.5 mm screw, 8×10 mm crown)

**Bone**: Type II quality, homogeneous cortical layer 2 mm thick; cancellous core.

**Material properties (ANSYS)**:

| Component | E (GPa) | ν | Density (kg/m³) |
|---|---|---|---|
| Cancellous bone | 1.3 | 0.30 | 500 |
| Cortical bone | 13 | 0.30 | 1180 |
| Ti alloy (Ti6Al4V) | 103 | 0.33 | 4620 |
| Zirconia crown | 200 | 0.31 | 6090 |

**Loading**: 100 N vertical and 100 N at 30° oblique to implant axis; friction coefficient 0.3; full osseointegration assumed.

**Mesh**: Parabolic tetrahedral elements; 0.6 mm crown, 0.2 mm screw/implant, refined to 0.1 mm at implant neck. Model B: 387,592 elements / 246,174 nodes; Model A: 316,058 elements / 213,152 nodes.

**Outcome**: Maximum von Mises stress (MPa) and strain (mm/mm) at implant surface and cortical/cancellous bone.

## 4. Key Results and Benchmarks

**100 N Vertical load:**

| Component | Cement-retained | Cementless screw-retained |
|---|---|---|
| Implant stress | 65.3 MPa | 26.3 MPa |
| Bone stress | 34.04 MPa | 9.97 MPa |
| Bone strain | 0.0084 mm/mm | 0.0015 mm/mm |

**100 N Oblique (30°) load:**

| Component | Cement-retained | Cementless screw-retained |
|---|---|---|
| Implant stress | 110.6 MPa | 79.83 MPa |
| Bone stress | 52.71 MPa | 20.63 MPa |
| Bone strain | 0.012 mm/mm | 0.002 mm/mm |

- Stress concentrations in cement-retained model located at **implant neck**; in cementless model at **apical area** of implant.
- Oblique load produced higher stress in both models than vertical load (consistent with literature).
- Stress decreased rapidly in bone with distance from the implant in both models.
- Null hypothesis rejected: retention type significantly affects stress/strain distribution.

## 5. Limitations and Future Work

- In silico only — no clinical or laboratory validation of the FEA results
- Assumes full osseointegration (ideal condition); does not model partial contact or bone defects
- Isotropic, homogeneous, linear-elastic material properties assumed for bone (real bone is anisotropic and viscoelastic)
- Single mandibular premolar region modeled; results may differ by implant location or jaw geometry
- No fatigue analysis or cyclic loading; single-load scenarios only
- Zirconia crown fracture risk not assessed (only implant/bone stress, not crown stress reported in detail)
- Clinical studies needed to confirm FEA-predicted advantages of cementless design

## 6. Related Work

- Hamed 2020 SR: clinical outcomes of screw vs cement retention — systematic review basis
- Tomar 2025 SR+MA: cement vs screw zirconia crowns — updated clinical evidence
- Ziada 2025 FEA: abutment material effects on stress distribution

## 7. Glossary

- **von Mises stress**: Equivalent stress criterion combining all stress components; used to predict yielding/failure in ductile materials
- **Cementless screw-retained**: Novel design where zirconia crown attaches to a titanium base abutment via a link screw without any cement layer ("screw-in-screw")
- **Base abutment**: Prefabricated titanium abutment that receives the titanium link and zirconia crown assembly
- **Titanium link**: Intermediate component connecting zirconia crown to base abutment, fastened by a prosthetic (link) screw
- **Type II bone**: Moderately dense bone with 2 mm cortical layer; common in posterior mandible
- **FEA (Finite Element Analysis)**: Computational method dividing complex geometry into small elements to solve stress/strain equations numerically
