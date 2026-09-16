---
title: "Biomechanical analysis of the maxillary sinus floor membrane during internal sinus floor elevation with implants at different angles of the maxillary sinus angles"
authors: Yinxin Deng, Ruihong Ma, Yilin He, Shujia Yu, Shiyu Cao, Kang Gao, Yiping Dou, Pan Ma
year: 2024
date: 2024-03-05
doi: 10.1186/s40729-024-00530-5
source: deng-2024-biomechanical-analysis-maxillary-sinus-floor.md
category: [sinus-lift/transcrestal]
evidence_level: in-vitro
pdf_path: /Users/oracleneo/llm-wiki/papers/deng-2024-biomechanical-analysis-maxillary-sinus-floor.pdf
pdf_filename: deng-2024-biomechanical-analysis-maxillary-sinus-floor.pdf
source_collection: external
tags: [maxillary-sinus-angle, internal-sinus-elevation, finite-element-analysis, sinus-membrane, perforation-risk, biomechanics, membrane-stripping]
relations:
  - type: extends
    target: lin-2025-schneiderian-membrane-biomechanical-transcrestal-fea
---

## Three-line Summary

3D FEA study (3 sinus angle models — 45°/85°/125°, implant elevated 1–10 mm, membrane separation 0 vs 4 mm) simulating internal (transcrestal) sinus floor elevation with simultaneous implant placement.

At 10 mm elevation with 0 mm separation, peak membrane stress was 78.32 / 73.89 / 51.87 MPa for narrow / medium / wide sinus; with 4 mm separation the narrow-sinus stress dropped to 7.25 MPa, while wide-sinus stress rose to 22.74 MPa.

Membrane stripping before elevation (modified internal sinus elevation) greatly reduces rupture risk in narrow sinuses; wide sinuses are relatively safe regardless of technique — supporting preoperative CBCT assessment of sinus angle plus deliberate mucoperiosteal separation.

## 세줄요약

3D FEA 연구(상악동 각도 3모델 — 45°/85°/125°, 임플란트 1–10mm 거상, 점막 박리 0 vs 4mm)로 내부(경치조골) 상악동거상 시 동시 임플란트 식립을 모사.

10mm 거상·박리 0mm에서 첨두 막 응력이 좁은/중간/넓은 상악동 각각 78.32 / 73.89 / 51.87 MPa, 박리 4mm에서는 좁은 상악동이 7.25 MPa로 급감한 반면 넓은 상악동은 22.74 MPa로 상승.

거상 전 점막 박리(수정 내부거상술)가 좁은 상악동의 천공·파열 위험을 크게 낮추고, 넓은 상악동은 술식과 무관하게 상대적으로 안전 — 술 전 CBCT로 상악동 각도 평가 + 의도적 점막 박리의 근거.

## Summary

This 3D finite element study (Deng et al., IJID 2024) simulated internal (transcrestal) sinus floor elevation with simultaneous implant placement in three maxillary sinus angle models — 45° (narrow), 85° (medium), 125° (wide), derived from CBCT distributions of 80 patients. It compared the traditional procedure (no membrane separation) with the authors' modified procedure (4 mm mucoperiosteal stripping) across elevation heights of 1–10 mm, using peak von Mises stress of the sinus-floor membrane as the rupture-risk indicator. Without separation, the narrow sinus showed the highest membrane stress at every elevation (e.g., 78.32 MPa vs 51.87 MPa at 10 mm), providing a mechanical explanation for the clinically reported higher perforation risk in narrow sinuses. With 4 mm separation, narrow-sinus peak stress dropped ~91 % at 10 mm elevation, while wide-sinus stress increased with elevation, exceeding the narrow-sinus values above ~6.5 mm. The clinical takeaway: deliberate membrane stripping markedly reduces rupture risk in narrow sinuses, whereas wide sinuses are relatively forgiving regardless of technique — preoperative CBCT assessment of sinus angle informs the stripping decision.

## Key Contributions
- First 3D FEA to explicitly simulate the membrane-separation phase of internal sinus elevation (0 vs 4 mm) alongside elevation height, instead of modeling only the final elevated geometry.
- Mechanical explanation for higher perforation risk in narrow (low-angle) sinuses: without stripping, narrow-sinus membrane stress exceeds medium/wide sinuses at all heights (up to −57 % to −61 % relative reduction in wider sinuses).
- Quantified validation of the modified internal sinus elevation procedure: 4 mm stripping reduced narrow-sinus peak stress from 78.32 to 7.25 MPa at 10 mm elevation (−91 %).
- CBCT angle distribution in 80 Chinese patients shows 45/80 (56 %) sinuses at angles ≤ 85°, i.e., the higher-risk morphology is common, not rare.
- Stress-concentration nephograms: implant-tip contact zone is the risk locus; stripping disperses the concentration.

## Methodology

3D FEA (Mimics 21 + Geomagic Studio 2014 + HyperMesh 14 + MSC Patran/Nastran 2012). Patient-derived CBCT sinus/membrane geometry (NewTom VG, 0.125 mm layer) with 45° and 125° bowl-symmetric models created by angle adjustment. ITI Straumann bone-level cylindrical implant model (bottom Ø 4.8 mm, height 10.2 mm, rounded apex Ø 4.45 mm). Membrane 1 mm thick, hyperelastic Mooney–Rivlin (C10=0.253, C01=0.027); cortical bone 13,700 MPa ν0.30, cancellous 1,370 MPa ν0.30, titanium 110,000 MPa ν0.35. Membrane meshed with hexahedral (Hex8), implant/maxilla tetrahedral (Tet4). Implant moved vertically only, tip in frictional contact with membrane; separation (0 or 4 mm) modeled by un-sharing membrane–bone nodes in the stripped zone. Outcome: peak von Mises stress of the sinus-floor membrane at elevation heights 1–10 mm for each angle × separation combination.

## Results

| Peak membrane stress, 10 mm elevation (MPa) | Sinus I 45° (narrow) | Sinus II 85° (medium) | Sinus III 125° (wide) |
|---|---:|---:|---:|
| Separation 0 mm | 78.32 | 73.89 | 51.87 |
| Separation 4 mm | 7.25 | 16.55 | 22.74 |

- 0 mm separation: stress rises nonlinearly with elevation in all groups; narrow sinus highest throughout (II/III lower by −5.7 % to −57.2 % and −10.6 % to −61.5 % vs I).
- 4 mm separation: up to 6 mm elevation, II/III still lower than I (−72.3 % to −9.4 % / −57.7 % to −2.0 %); beyond 6.5 mm, wide sinus (III) stress exceeds I by +29.6–213.7 %, and II exceeds I by +89.6–128.3 % at ≥8 mm.
- Narrow-sinus stress at 4 mm separation peaks at ~6–8 mm then slowly declines (convex-floor-like dispersion), while wider sinuses keep climbing.
- Across all conditions, 4 mm separation stress < 0 mm separation stress for the same sinus; stress concentrates at the implant-tip contact zone and intensifies with elevation.

## Related Papers
- [[sinus-lift/transcrestal/lin-2025-schneiderian-membrane-biomechanical-transcrestal-fea]] — sibling transcrestal FEA (hydraulic vs osteotome techniques); this paper adds the anatomy-angle axis to the same hyperelastic-membrane modeling framework. `extends`
- [[sinus-lift/transcrestal/shalash-2023-crestal-sinus-elevation-densah-oblique]] — clinical prospective study of crestal lift in oblique-floor sinuses (RBH 4–7 mm), 1/16 (6.3 %) perforation with Densah; oblique floor is the clinical counterpart of narrow/low-angle sinus morphology modeled here.
- [[sinus-lift/lateral/yang-2024-sinus-septa-wall-thickness-perforation-risk]] — SR/MA linking septa and lateral wall thickness to perforation risk; sinus angle is a complementary anatomical axis for the same decision (preoperative CBCT anatomy screen).
- [[sinus-lift/lateral/diaz-olivares-2021-schneiderian-membrane-perforation-sinus-lift]] — repaired perforations do not independently impair implant survival (97.68 % vs 98.88 %); this FEA speaks to the *prevention* side — what anatomy and technique make a rupture likely in the first place.