---
title: "Biomechanical analysis of the maxillary sinus floor membrane during internal sinus floor elevation with implants at different angles of the maxillary sinus angles"
authors: Yinxin Deng, Ruihong Ma, Yilin He, Shujia Yu, Shiyu Cao, Kang Gao, Yiping Dou, Pan Ma
year: 2024
doi: 10.1186/s40729-024-00530-5
category: [sinus-lift/transcrestal]
pdf_path: /Users/oracleneo/llm-wiki/papers/deng-2024-biomechanical-analysis-maxillary-sinus-floor.pdf
pdf_filename: deng-2024-biomechanical-analysis-maxillary-sinus-floor.pdf
source_collection: external
---

## Why Ingested

상악동 **각도(형태)가 내부(경치조골) 거상 시 상악동저 점막 응력에 미치는 영향**을 3D FEA로 정량화한 첫 논문. 기존 FEA 페이지([[wiki/sinus-lift/transcrestal/lin-2025-schneiderian-membrane-biomechanical-transcrestal-fea]])는 기법(수압 vs osteotome) 비교였고, [[wiki/sinus-lift/lateral/yang-2024-sinus-septa-wall-thickness-perforation-risk]]는 해부학적 위험(septa·벽두께)의 임상 SR/MA였으나, "좁은 상악동에서 천공 위험이 왜 높은가"를 막 응력 수치로 설명하는 축이 없었다. 점막 박리(stripping) 0mm vs 4mm 비교로 수정 내부거상 술식의 역학적 근거도 제시한다.

## Three-line Summary

3D FEA study (3 sinus angle models — 45°/85°/125°, implant elevated 1–10 mm, membrane separation 0 vs 4 mm) simulating internal (transcrestal) sinus floor elevation with simultaneous implant placement.

At 10 mm elevation with 0 mm separation, peak membrane stress was 78.32 / 73.89 / 51.87 MPa for narrow / medium / wide sinus; with 4 mm separation the narrow-sinus stress dropped to 7.25 MPa, while wide-sinus stress rose to 22.74 MPa.

Membrane stripping before elevation (modified internal sinus elevation) greatly reduces rupture risk in narrow sinuses; wide sinuses are relatively safe regardless of technique — supporting preoperative CBCT assessment of sinus angle + deliberate mucoperiosteal separation.

## 세줄요약

3D FEA 연구(상악동 각도 3모델 — 45°/85°/125°, 임플란트 1–10mm 거상, 점막 박리 0 vs 4mm)로 내부(경치조골) 상악동거상 시 동시 임플란트 식립을 모사.

10mm 거상·박리 0mm에서 첨두 막 응력이 좁은/중간/넓은 상악동 각각 78.32 / 73.89 / 51.87 MPa, 박리 4mm에서는 좁은 상악동이 7.25 MPa로 급감한 반면 넓은 상악동은 22.74 MPa로 상승.

거상 전 점막 박리(수정 내부거상술)가 좁은 상악동의 천공·파열 위험을 크게 낮추고, 넓은 상악동은 술식과 무관하게 상대적으로 안전 — 술 전 CBCT로 상악동 각도 평가 + 의도적 점막 박리의 근거.

## 1. Document Information
- **Journal**: International Journal of Implant Dentistry 2024;10(1):11
- **DOI**: 10.1186/s40729-024-00530-5
- **Institution**: Dental Implant Center, Beijing Stomatological Hospital, School of Stomatology, Capital Medical University, Beijing, China

## 2. Key Contributions
- First 3D FEA to model internal (transcrestal) sinus floor elevation with the sinus membrane separation phase explicitly simulated (0 mm traditional vs 4 mm modified stripping), rather than only the final elevated state.
- Quantifies peak sinus-floor membrane stress across three maxillary sinus angles (45° narrow, 85° medium, 125° wide) and elevation heights 1–10 mm, providing a mechanical explanation for the clinically observed higher perforation risk in narrow sinuses.
- Mechanically validates the modified internal sinus elevation procedure (mucoperiosteal stripping before elevation): at 10 mm elevation, 4 mm separation cut narrow-sinus peak stress ~91% (78.32 → 7.25 MPa).
- CBCT-derived angle distribution from 80 patients (angle <70°:5, 70–85°:34, 86–100°:36, >100°:5) documents the clinical frequency of the narrow-sinus scenario.

## 3. Methodology and Architecture
- **Design**: 3D finite element analysis (numerical simulation)
- **Model**: ITI Straumann bone-level cylindrical implant (bottom Ø 4.8 mm, height ~10.2 mm, rounded apex Ø 4.45 mm); maxillary sinus + 1 mm membrane from CBCT (NewTom VG, 110 kV, 0.125 mm layer); 45°/125° bowl-shaped symmetric sinus models derived by geometry adjustment in Geomagic Studio 2014
- **Materials**: cortical bone E=13,700 MPa (ν=0.30); cancellous bone E=1,370 MPa (ν=0.30); titanium implant E=110,000 MPa (ν=0.35); sinus membrane hyperelastic Mooney–Rivlin (C10=0.253, C01=0.027)
- **Meshing**: membrane hexahedral (Hex8), implant + maxilla tetrahedral (Tet4); nodes 295,809–590,735
- **Loading**: implant tip friction contact with membrane floor; vertical displacement only; elevation 1–10 mm at 3 angles × separation 0 / 4 mm
- **Outcome**: peak von Mises stress of maxillary sinus floor membrane

## 4. Key Results and Benchmarks
| Condition (10 mm elevation) | Sinus I (45°, narrow) | Sinus II (85°, medium) | Sinus III (125°, wide) |
|---|---|---:|---:|---:|
| Separation 0 mm — peak stress (MPa) | 78.32 | 73.89 | 51.87 |
| Separation 4 mm — peak stress (MPa) | 7.25 | 16.55 | 22.74 |

- **0 mm separation**: membrane stress rises nonlinearly with elevation; narrow sinus (I) stress exceeds medium/wide sinuses at all heights (−57.2 % to −5.7 % and −61.5 % to −10.6 % lower for II/III vs I).
- **4 mm separation**: up to 6 mm elevation, II/III still below I (−72.3 % to −9.4 % / −57.7 % to −2.0 %); above 6.5 mm, wide-sinus (III) stress overtakes I (+29.6–213.7 % vs I at 6.5–10 mm); II exceeds I by +89.6–128.3 % at ≥8 mm.
- Stress concentration localizes at implant-tip contact and intensifies with elevation; 4 mm separation markedly disperses it (nephogram comparison).
- Narrow-sinus stress at 4 mm separation peaks around 6–8 mm then slightly declines — attributed to convex-floor-like stress dispersion of sinus I morphology.

## 5. Limitations and Future Work
- FEA absolute values are not representative of in vivo tissue stresses — only qualitative trends guide clinical decisions; membrane failure strength itself was not measured (cited cadaveric data gaps).
- Model simplification: 45°/125° sinuses are symmetric bowl-shaped reconstructions, not patient-derived; only the sinus region (not full maxilla) was simulated; single implant macrogeometry; membrane thickness fixed at 1 mm despite interindividual variation.
- Implant insertion was simulated as push-up displacement, not the actual rotational seating; lateral displacement restricted.
- No clinical outcome data — perforation risk conclusions are inferential from simulated stress.

## 6. Related Work
- [[wiki/sinus-lift/transcrestal/lin-2025-schneiderian-membrane-biomechanical-transcrestal-fea]] — sibling FEA comparing hydraulic vs osteotome transcrestal techniques; together they cover technique (Lin) and anatomy-angle (Deng) axes of perforation mechanics. deng-2024 extends lin-2025.
- [[wiki/sinus-lift/transcrestal/shalash-2023-crestal-sinus-elevation-densah-oblique]] — clinical prospective study of crestal elevation in oblique floors (RBH 4–7 mm); slanted/oblique floor is the clinical anatomical counterpart of the low-angle (narrow) sinus morphology modeled here.
- [[wiki/sinus-lift/lateral/yang-2024-sinus-septa-wall-thickness-perforation-risk]] — SR/MA of anatomical perforation risk factors (septa, lateral wall thickness); sinus angle adds a third anatomical axis.
- [[wiki/sinus-lift/lateral/diaz-olivares-2021-schneiderian-membrane-perforation-sinus-lift]] — repaired perforation does not independently reduce implant survival; this FEA explains the rupture event the repair protocol manages.
- Deng Y, Tong C, Gao K, et al. 2023 (Clin Implant Dent Relat Res) — the authors' own retrospective clinical study of the modified internal sinus elevation procedure (cited as ref 16; not yet in wiki).

## 7. Glossary
- **Internal sinus elevation**: transcrestal (crestal/osteotome) maxillary sinus floor elevation performed through the alveolar ridge, as opposed to external (lateral window) approach.
- **Modified internal sinus elevation**: internal sinus elevation preceded by deliberate mucoperiosteal stripping of the sinus floor membrane (via the crest) to reduce membrane tension before lifting.
- **Maxillary sinus angle (∠ACB)**: angle between a horizontal line 10 mm above the sinus-floor lowest point and the buccal/palatal wall bone plates at the intended implant site.
- **Mooney–Rivlin model**: hyperelastic material constitutive model (C10, C01 parameters) used to represent the large-deformation nonlinear behavior of the sinus membrane.
- **Peak von Mises stress**: scalar equivalent stress used here as the indicator of sinus-floor membrane rupture/perforation risk.