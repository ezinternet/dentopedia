---
title: "Comparative Biomechanical Evaluation of Novel Screwless Retained Dental Implant Prosthesis: A 3D Finite Element Analysis"
authors: Ki-Sun Lee, Jaeyeol Kim, JaeHyung Lim, Jae-Jun Ryu
year: 2025
date: 2025-01-22
doi: 10.3390/jfb16020039
source: lee-2025-screwless-hook-retained-implant-fea.md
category: [prosthetic-materials]
confidence: in-vitro
pdf_path: /Users/oracleneo/llm-wiki/papers/lee-2025-screwless-hook-retained-implant-fea.pdf
pdf_filename: lee-2025-screwless-hook-retained-implant-fea.pdf
source_collection: external
tags: []
---

## One-line Summary

3D FEA comparing three implant retention systems (n=3 models, 100N loads): novel screwless hook-retained prosthesis (HRP) showed lower implant fixture stress (21.33 MPa vertical, 187.50 MPa oblique) than screw-and-cement system (SCRP: 32.91 / 262.24 MPa) and comparable to cementless screw-retained (SRP: 21.92 / 187.64 MPa), with equivalent peri-implant bone stress across all groups.

## 한줄요약

3D 유한요소분석에서 신규 후크유지 보철(HRP)의 임플란트 최대 폰미제스 응력이 스크류-시멘트 유지(SCRP)보다 낮고 시멘트리스 스크류유지(SRP)와 동등하여, HRP가 기존 SCRP의 생역학적 대안이 될 수 있음을 최초로 보고함.

## Summary

This FEA study by Lee et al. (Korea University, 2025) is the first biomechanical evaluation of a novel screwless, hook-retained implant prosthetic system (HRP). Three single-crown retention systems on an identical NeoBiotech IS-III fixture (Ø4.0 × 10 mm, lower second premolar, fully osseointegrated) were simulated under 100 N vertical and 100 N oblique (30°) loading in ANSYS Workbench 2022 R2.

**Systems compared:**
- **SCRP** (screw-and-cement-retained): conventional abutment screw + dental cement to retain zirconia crown — most widely used but risks residual cement and retrievability issues
- **SRP** (cementless screw-retained, "screw-in-screw"): link + link screw retain crown without cement — eliminates cement complications but requires screw access hole
- **HRP** (screwless hook-retained): novel design with YK abutment + cylinder + hook; crown cemented only to cylinder (not to abutment); no abutment screw, no link screw

Under both loading conditions, HRP generated lower implant fixture stress than SCRP and nearly identical stress to SRP. Peri-implant bone stress and strain were equivalent across all three systems. The authors conclude HRP is a viable biomechanical alternative to SCRP, potentially combining the retrievability advantage of SRP with simplification of screw-related complications.

## Key Contributions

- **First FEA data on HRP system**: no prior clinical or laboratory study existed
- **Implant fixture stress advantage**: HRP 21.33 MPa vs SCRP 32.91 MPa under vertical load (−35%)
- **Bone stress equivalence**: all three systems produced similar peri-implant bone stress (~10.5 MPa vertical; ~31–32 MPa oblique) — HRP does not compromise bone loading
- **Oblique load advantage preserved**: HRP 187.50 MPa vs SCRP 262.24 MPa at 30° oblique (−28%)

## Methodology

- **Software**: ANSYS Workbench 2022 R2; parabolic tetrahedral elements; bonded contact
- **Bone model**: lower second premolar region, cortical + cancellous layers
- **Fixture**: NeoBiotech IS-III, Ø4.0 × 10 mm
- **Materials**: isotropic, homogeneous, linearly elastic (E cortical 13 GPa, cancellous 1.3 GPa; Ti 103 GPa; zirconia 200 GPa)
- **Loading**: 100 N vertical (perpendicular to fixture) and 100 N oblique (30° to fixture axis)
- **Outcome**: maximum von Mises stress (MPa) in abutment component, implant fixture, and bone; maximum bone strain (mm/mm)

## Results

**Vertical load (100 N):**

| Component | SCRP | SRP | HRP |
|---|---|---|---|
| Abutment stress | 18.96 MPa | 18.52 MPa | 23.49 MPa |
| Implant fixture | 32.91 MPa | 21.92 MPa | **21.33 MPa** |
| Bone stress | 10.43 MPa | 10.60 MPa | 10.54 MPa |
| Bone strain | 0.00108 mm/mm | 0.00110 mm/mm | 0.00109 mm/mm |

**Oblique load (100 N at 30°):**

| Component | SCRP | SRP | HRP |
|---|---|---|---|
| Abutment stress | 218.42 MPa | 185.07 MPa | 187.60 MPa |
| Implant fixture | 262.24 MPa | 187.64 MPa | **187.50 MPa** |
| Bone stress | 32.32 MPa | 32.22 MPa | 30.72 MPa |
| Bone strain | 0.00238 | 0.00237 | 0.00235 |

Notable: HRP abutment component stress under vertical load (23.49 MPa) was slightly higher than SCRP/SRP (~19 MPa), but all values were well within titanium yield strength limits.

## Related Papers

- [[prosthetic-materials/hamed-2020-screw-vs-cement-implant-sr]] — SR+MA of screw vs cement retention; clinical context for SCRP/SRP tradeoffs
- [[prosthetic-materials/chan-2026-fea-cad-cam-zirconia-3d-printed-hybrid]] — FEA comparison of CAD/CAM zirconia vs hybrid prosthetic systems; similar FEA methodology
