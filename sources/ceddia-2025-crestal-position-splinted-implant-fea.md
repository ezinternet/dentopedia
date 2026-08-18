---
title: "Effect of Crestal Position on Bone–Implant Stress Interface of Three-Implant Splinted Prostheses: A Finite Element Analysis"
authors: Mario Ceddia, Giulia Marchioli, Tea Romasco, Luca Comuzzi, Adriano Piattelli, Douglas A. Deporter, Natalia Di Pietro, Bartolomeo Trentadue
year: 2025
doi: 10.3390/ma18143344
category: [implants]
pdf_path: /Users/oracleneo/llm-wiki/papers/ceddia-2025-crestal-position-splinted-implant-fea.pdf
pdf_filename: ceddia-2025-crestal-position-splinted-implant-fea.pdf
source_collection: external
---

## Why Ingested

First FEA study to evaluate vertical platform misalignment effects across all four crestal/subcrestal permutations in three-implant splinted prostheses, directly addressing a gap noted in prior single-implant subcrestal studies. Extends the framework of [[implants/chang-2024-optimization-implant-design-bone-quality-fea]] on FEA bone-implant stress into the multi-unit splinted prosthesis context.

## Three-line Summary

3D FEA study comparing four vertical platform alignment configurations (all-crestal, mixed, all-subcrestal) of three-implant splinted prostheses under 400 N vertical and 45° oblique loading in a mandibular bone segment.

Mixed configuration B (central subcrestal, lateral crestal) produced the highest cortical bone stress under oblique loading (~116 MPa, near the 120 MPa physiological limit); uniform all-subcrestal placement (Model D) minimized cortical bone stress to 32 MPa.

Uniform vertical positioning — whether all-crestal or all-subcrestal — is biomechanically superior to mixed configurations; all-subcrestal offers the lowest stress and may reduce marginal bone resorption risk.

## 세줄요약

3D 유한요소해석(FEA)으로 3개 임플란트 연결 보철물의 네 가지 수직 플랫폼 정렬 구성(전 치조정·혼합·전 치조하)을 수직(400 N) 및 경사(400 N, 45°) 하중 하에서 비교한 연구.

혼합 구성 B(중앙 치조하·측방 치조정)는 경사 하중 시 피질골 응력이 최고(~116 MPa, 생리적 한계 120 MPa 근접)이었고, 전 치조하 구성 D는 피질골 응력을 32 MPa까지 낮췄음.

수직 정렬이 균일할수록(전 치조정 또는 전 치조하) 혼합 구성보다 유리하며, 특히 전 치조하 배치가 생리적 응력 범위 유지와 변연골 흡수 위험 감소에 최적임.

## 1. Document Information

- **Journal**: Materials 2025;18(14):3344
- **DOI**: 10.3390/ma18143344
- **Institution**: Polytechnic University of Bari, "G. d'Annunzio" University of Chieti-Pescara, Italy

## 2. Key Contributions

- First FEA study examining vertical implant platform misalignment in three-implant splinted prostheses (all prior subcrestal FEA focused on single implants)
- Quantified cortical bone stress approaching physiological limit (116 MPa vs. 120 MPa threshold) specifically for mixed B configuration under oblique loading
- Identified the abutment–implant connection interface as the consistent critical stress concentration point across all four models
- Demonstrated that uniform all-subcrestal placement (Model D) yields the lowest bone and implant stresses under both loading modes

## 3. Methodology and Architecture

- **Design**: 3D finite element analysis (in-vitro computational)
- **Software**: Autodesk Inventor 2023 (CAD), ANSYS Workbench R2023 (FEA)
- **Implants**: AoN Implants Srl, 3.5 mm diameter × 13 mm length; single-thread aggressive geometry; inter-implant distance 3 mm; conometric abutment connection
- **Bone model**: Simplified mandibular segment (32 × 15 × 36 mm), 1.5 mm cortical shell, anisotropic material properties; full osseointegration assumed
- **Mesh**: Tetrahedral elements, 0.5 mm optimal element size (convergence verified at <5% change); 30,623 implant elements, 14,568 cortical, 20,379 trabecular elements
- **Contacts**: Non-linear frictional — titanium–titanium 0.3, cortical bone–implant 0.65, trabecular bone–implant 0.77
- **Configurations**:
  - Model A: all three implants at crestal level
  - Model B: mesial + distal crestal, central 2 mm subcrestal
  - Model C: all three 2 mm subcrestal
  - Model D: mesial + distal 2 mm subcrestal, central 3 mm subcrestal
- **Load**: 400 N vertical; 400 N oblique at 45° (buccally + distally)
- **Outcome**: Von Mises stress in cortical bone, trabecular bone, and implant components; physiological threshold 100–120 MPa for cortical bone

## 4. Key Results and Benchmarks

**Implant Von Mises stress under vertical 400 N:**

| Model | Peak implant stress (MPa) |
|---|---|
| A (all crestal) | 71.478 |
| B (central subcrestal) | 89.213 |
| C (all 2mm subcrestal) | 52.641 |
| D (all subcrestal deepest) | 66.409 |

**Cortical bone stress under vertical 400 N:**

| Model | Cortical peak (MPa) | Trabecular peak (MPa) |
|---|---|---|
| A | 14.56 (uniform) | 1.18 (mesial implant apex) |
| B | 26.69 (central implant) | 2.26 (central implant) |
| C | ~lower | 1.30 (central implant) |
| D | ~lowest | 0.73 (central implant) |

**Implant stress under oblique 400 N (45°):**

| Model | Peak implant stress (MPa) |
|---|---|
| A (all crestal) | 823.329 |
| B (central subcrestal) | 723.721 |

**Cortical bone stress under oblique 400 N:**

| Model | Cortical peak (MPa) |
|---|---|
| B (central subcrestal, lateral crestal) | ~116 (near 120 MPa physiological limit) |
| D (all subcrestal) | 32 |
| D trabecular | 2.11 |

- Stress concentration consistently at abutment–implant connection across all models
- Oblique loading produced higher localized stress over a larger crestal area vs. vertical loading

## 5. Limitations and Future Work

- Bone modeled as homogeneous anisotropic (not micro-CT-derived heterogeneous architecture); may underestimate local peak stresses
- Static loading only — does not capture cyclic/dynamic fatigue under clinical masticatory cycles
- Single implant brand/geometry; generalizability to other macrogeometries requires further validation
- Simplified mandibular block geometry, not patient-specific anatomy
- Full osseointegration assumed — does not model healing-phase partial contact
- Findings warrant experimental extensometry and clinical studies for corroboration

## 6. Related Work

- Ceddia et al. (prior FEA): comparative FEA + experimental testing, average prediction error 1.27% — validates FEA methodology used here
- Di Pietro et al. (cited as [52]): FEA on single implants showing subcrestal placement is biomechanically more effective
- Lin et al. [5]: clinical data — splinted prostheses with ≥0.5 mm vertical discrepancy have significantly higher bone resorption; >90% of cases the most apical implant showed least peri-implant bone loss
- Yi et al. [83]: 15-year retrospective — central implant in three contiguous connected implants has significantly higher marginal bone loss and peri-implantitis risk
- Tonin et al. [72]: conometric connections + CAD/CAM → lower crestal stress vs. tungsten inert gas welding

## 7. Glossary

- **FEA (Finite Element Analysis, 유한요소해석)**: Computational method dividing a structure into elements to calculate stress/strain distribution under load
- **Von Mises stress**: Equivalent stress criterion combining multiaxial stress components; used to predict yielding/failure
- **Crestal positioning (치조정 배치)**: Implant platform placed flush with the alveolar crest
- **Subcrestal positioning (치조하 배치)**: Implant platform placed below the alveolar crest
- **Splinted prosthesis (연결 보철물)**: Multiple crowns fused into a single unit distributed across multiple implants
- **Conometric connection**: Friction-retained abutment-crown connection without screw; coping sits on tapered abutment
- **Physiological stress threshold (생리적 응력 한계)**: 100–120 MPa for mandibular cortical bone; above this triggers remodeling/resorption
- **MBL (Marginal Bone Loss, 변연골소실)**: Crestal bone resorption around an implant, key long-term implant survival indicator
