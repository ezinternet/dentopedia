---
title: "FEA: Cement-Retained vs. Cementless Screw-Retained Zirconia Implant Crowns"
authors: Jae-Hyun Lee, Ho Yeol Jang, Su Young Lee
year: 2021
date: 2021-05-19
doi: 10.3390/ma14102666
source: lee-2021-cement-vs-cementless-screw-retained-fea.md
category: [prosthetic-materials]
confidence: in-vitro
pdf_path: /Users/oracleneo/llm-wiki/papers/lee-2021-cement-vs-cementless-screw-retained-fea.pdf
pdf_filename: lee-2021-cement-vs-cementless-screw-retained-fea.pdf
source_collection: external
tags: []
---

## One-line Summary

3D FEA of mandibular premolar implant models shows cementless screw-retained (base abutment + titanium link screw) zirconia crowns produce substantially lower implant and bone stress than conventional cement-retained crowns under both vertical and oblique loading.

## 한줄요약

하악 소구치 임플란트 3D 유한요소분석에서 신형 시멘트-프리 나사유지형(베이스 어버트먼트+링크 스크류) 지르코니아 크라운이 기존 시멘트 유지형보다 임플란트 및 골 응력을 수직·사방 부하 모두에서 현저히 낮게 보임.

## Summary

Lee et al. (2021) used 3D finite element analysis (FEA) to compare stress and strain distributions in two implant-supported zirconia crown designs:

1. **Conventional cement-retained**: Zirconia crown cemented to a titanium abutment (standard approach)
2. **Novel cementless screw-retained**: Zirconia crown fixed to a titanium base abutment via a titanium link and prosthetic (link) screw — no cement involved ("screw-in-screw" design)

Under 100 N vertical and 30° oblique loading, the cementless screw-retained model consistently produced lower maximum von Mises stress in both the implant and the supporting bone. The differences were substantial: implant stress was ~60% lower vertically (26.3 vs 65.3 MPa) and ~28% lower obliquely (79.83 vs 110.6 MPa); bone stress was ~71% lower vertically (9.97 vs 34.04 MPa) and ~61% lower obliquely (20.63 vs 52.71 MPa).

## Key Contributions

- Quantified biomechanical advantage of cementless screw-retained zirconia crown design over conventional cement-retained via 3D FEA
- Stress concentration locations differed: cement-retained concentrated at implant **neck**; cementless at implant **apical area**
- Eliminated the cement-related disadvantages (retained cement, microorganism colonization, crown debonding) while providing stress-distribution benefit
- Oblique loading generated higher stresses in both models, confirming clinical importance of implant axis alignment

## Methodology

- **Models**: Two 3D ANSYS Workbench models of mandibular second premolar region (SolidWorks CAD)
- **Bone**: Type II quality; 2 mm homogeneous cortical layer; full osseointegration assumed
- **Materials**: Ti6Al4V alloy (E=103 GPa), zirconia crown (E=200 GPa), cortical bone (E=13 GPa), cancellous bone (E=1.3 GPa)
- **Loading**: 100 N vertical and 100 N at 30° oblique; friction coefficient 0.3
- **Mesh**: Parabolic tetrahedral; refined to 0.1 mm at implant neck
- **Output**: Maximum von Mises stress (MPa) and strain (mm/mm) at implant and bone

## Results

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

**Key finding**: Under all loading conditions, cementless screw-retained design produced lower implant and bone stress. Null hypothesis (no difference between retention types) was rejected.

## Related Papers

- [[prosthetic-materials/hamed-2020-screw-vs-cement-implant-sr]] — systematic review of clinical outcomes for screw vs cement retention; this FEA provides biomechanical mechanistic data
- [[prosthetic-materials/tomar-2025-cement-vs-screw-zirconia-crown-sr-ma]] — SR+MA on cement vs screw zirconia crowns; updated clinical evidence for same comparison
- [[prosthetic-materials/ziada-2025-abutment-material-stress-distribution-fea]] — FEA study of abutment material effects on stress; complementary FEA approach
- [[prosthetic-materials/khurshid-2025-screw-vs-cement-crown-complications]] — clinical complications comparison of screw vs cement crowns
