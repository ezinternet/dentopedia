---
title: "Comparative analysis of stress distribution in teeth restored with glass fiber post, short fiber-reinforced composite post, and ribbond fiber post: A three-dimensional finite element study"
authors: Guduri Susita, Kasam Swetha, Swathi Aravelli, Nimeshika Ramachandruni, Laxmi Ghuguloth, Masuna Rukmini Amulya
year: 2026
doi: 10.4103/JCDE.JCDE_102_26
category: [resin]
pdf_path: /Users/oracleneo/llm-wiki/papers/susita-2026-comparative-analysis-stress-distribution-teeth.pdf
pdf_filename: susita-2026-comparative-analysis-stress-distribution-teeth.pdf
source_collection: external
---

## Why Ingested

근관치료된 치아에서 파이버 포스트 시스템의 응력 분포 비교는 [[wiki/resin/metwaly-2024-clinical-performance-polyethylene-fiber-reinforced-resin]]의 폴리에틸렌 파이버 복합레진 RCT 임상 결과를 생역학적 FEA 근거로 보강한다. 특히 SFRC(단섬유강화복합레진, Short Fiber-Reinforced Composite) 포스트의 상아질 탄성계수 유사성이 임상적 우수성의 기전적 설명을 제공한다.

## One-line Summary

3D FEA (n=3 models) comparing von Mises stress in maxillary central incisors restored with glass fiber post, SFRC post, and Ribbond fiber post under 100 N oblique load; SFRC post showed lowest internal post stress (5.22 MPa vs 12.28 MPa glass fiber) and most favorable dentin-compatible stress distribution.

## 한줄요약

3D FEA — 상악 중절치 근관치료 후 유리섬유 포스트·SFRC 포스트·Ribbond 포스트 응력분포 비교; SFRC 포스트가 가장 낮은 내부 응력(5.22 MPa) 및 상아질 친화적 응력 분포 보여.

## 1. Document Information

- **Journal**: Journal of Conservative Dentistry and Endodontics
- **Volume/Issue**: Volume 29, Issue 6, June 2026, pp. 608–614
- **DOI**: 10.4103/JCDE.JCDE_102_26
- **Affiliation**: Department of Conservative Dentistry and Endodontics, Malla Reddy Dental College for Women, Hyderabad, Telangana, India
- **Study type**: 3D Finite Element Analysis (in vitro computational study)

## 2. Key Contributions

- First 3D FEA directly comparing three clinically relevant fiber post systems — glass fiber post, SFRC post, and Ribbond fiber post — under identical loading conditions.
- Demonstrates that SFRC post (단섬유강화복합레진 포스트, Short Fiber-Reinforced Composite Post, SFRC) achieves lowest internal post stress (5.22 MPa) compared to glass fiber post (12.28 MPa) and Ribbond (9.73 MPa).
- Confirms the cervical region as the universal maximum-stress concentration zone regardless of post material type.
- Validates that post material elastic modulus proximity to dentin (상아질 탄성계수, Young's Modulus of Dentin) governs stress transfer favorability.

## 3. Methodology and Architecture

- **Software**: ANSYS ver. 10.0 (2022)
- **Model**: 3D maxillary central incisor based on Wheeler's Dental Anatomy; 23.5 mm total length, 13 mm apical root in socket with uniform PDL (치주인대, Periodontal Ligament, PDL) thickness 0.2 mm
- **Mesh**: 648,094 nodes; 411,102 tetrahedral solid elements
- **Components modeled**: enamel, dentin, cementum, PDL, cancellous bone, gutta-percha, composite resin core, ceramic crown + three post types
- **Loading**: 100 N oblique static load at 45° to the longitudinal axis on the palatal crown surface
- **Boundary conditions**: Outer root surface nodes fixed in all directions
- **Elastic properties**:
  - Enamel: E = 41 GPa, ν = 0.31
  - Dentin: E = 18.6 GPa, ν = 0.31
  - Glass fiber post: E = 30.9 GPa, ν = 0.30
  - SFRC post: E = 11.4 GPa, ν = 0.32
  - Ribbond fiber post: E = 23.6 GPa, ν = 0.32
- **Outcome**: von Mises stress distribution at five locations: post base, cervical region, post middle, post end, root apex

## 4. Key Results and Benchmarks

| Parameter | Glass Fiber Post | SFRC Post | Ribbond Fiber Post |
|---|---|---|---|
| Max equivalent stress (crown, MPa) | 87.205 | 87.201 | 87.202 |
| Max deformation (mm) | 0.1428 | 0.1429 | 0.1428 |
| Max internal post stress (MPa) | 12.28 | **5.22** | 9.73 |
| Core stress (MPa) | 10.99 | 11.40 | 10.99 |
| Dentin stress (MPa) | 8.96 | **8.55** | 8.80 |
| Post stress (MPa) | 11.74 | **5.02** | 9.17 |
| Cervical stress (MPa) | 5.21 | **5.15** | 5.20 |
| Stress at post end (MPa) | 3.61 | **1.49** | 1.95 |

- Maximum equivalent von Mises stresses were essentially identical across all groups in the crown region (~87.2 MPa).
- Deformation was virtually identical across groups (~0.1428–0.1429 mm).
- Stress concentration peaked cervically in all groups — confirming cervical region as the most failure-prone zone.
- SFRC post exhibited lowest stress throughout the post length; glass fiber post showed highest localized stresses.
- Posts with higher elastic modulus (glass fiber: 30.9 GPa) concentrate stress within the post itself rather than transferring to dentin.

## 5. Limitations and Future Work

- Static loading only — does not simulate complex cyclic masticatory forces.
- Materials assumed homogeneous, isotropic, and linearly elastic — simplification of real anisotropic dental tissues.
- Moisture, aging, and thermal changes not modeled.
- No statistical analysis (FEA inherently produces 100% reproducible results).
- Single tooth geometry (maxillary central incisor) — extrapolation to posterior teeth not directly supported.

## 6. Related Work

- Belli et al. (2011) — FEA of monoblocks in root canals; established cervical stress concentration concept.
- Tammineedi et al. (2020) — 3D FEA comparing fiber post vs dentin post with orthotropic properties.
- Kharboutly et al. (2023) — 3D FEA of maxillary central incisors with different post and crown materials (Cureus).
- Usman et al. (2025) — FEA of fiberglass post systems with different designs on endodontically treated maxillary central incisors.
- Abd-Alla et al. (2026) — Short vs long fiber-reinforced composite post and core fracture resistance in premolars.

## 7. Glossary

- **SFRC (단섬유강화복합레진, Short Fiber-Reinforced Composite, SFRC)**: Composite resin reinforced with randomly oriented short fibers; elastic modulus ~11.4 GPa — closest to dentin (18.6 GPa) among the three post systems tested.
- **Ribbond fiber post (리본드 파이버 포스트)**: Customized polyethylene fiber post system; elastic modulus ~23.6 GPa; creates primary monoblock via direct dentin bonding.
- **Von Mises stress (폰 미세스 응력)**: Equivalent stress criterion accounting for all stress components (tensile, compressive, shear) — used to predict material failure.
- **Monoblock (모노블록)**: Homogeneous stress-transfer unit created when post, cement, and dentin have similar elastic moduli and are adhesively bonded.
- **FEA (유한요소분석, Finite Element Analysis, FEA)**: Computational numerical method for stress and deformation simulation in virtual models.
- **PDL (치주인대, Periodontal Ligament, PDL)**: Connective tissue between root cementum and alveolar bone; E = 0.0689 GPa in this model.
