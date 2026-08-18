---
title: "Effect of Crestal Position on Bone–Implant Stress Interface of Three-Implant Splinted Prostheses: A Finite Element Analysis"
authors: Mario Ceddia, Giulia Marchioli, Tea Romasco, Luca Comuzzi, Adriano Piattelli, Douglas A. Deporter, Natalia Di Pietro, Bartolomeo Trentadue
year: 2025
date: 2025-07-16
doi: 10.3390/ma18143344
source: ceddia-2025-crestal-position-splinted-implant-fea.md
category: [implants]
evidence_level: in-vitro
pdf_path: /Users/oracleneo/llm-wiki/papers/ceddia-2025-crestal-position-splinted-implant-fea.pdf
pdf_filename: ceddia-2025-crestal-position-splinted-implant-fea.pdf
source_collection: external
tags: [FEA, splinted-implant, crestal-position, subcrestal, bone-implant-interface, stress-distribution, von-mises, cortical-bone, oblique-loading, mandible]
relations:
  - type: extends
    target: chang-2024-optimization-implant-design-bone-quality-fea
  - type: reinforces
    target: hussein-2019-thread-depth-implant-shape-stress-mandible-fea
---

## Three-line Summary

3D FEA comparing four vertical platform alignment configurations (all-crestal to all-subcrestal) of three-implant splinted prostheses under 400 N vertical and 45° oblique loading in an anisotropic mandibular bone model (n=4 configurations).

Mixed configuration B (central 2 mm subcrestal, lateral crestal) reached cortical bone stress of ~116 MPa under oblique loading — near the 120 MPa physiological limit; uniform all-subcrestal Model D reduced cortical stress to 32 MPa and trabecular to 2.11 MPa.

Uniform vertical alignment (all-crestal or all-subcrestal) is biomechanically superior to mixed configurations; all-subcrestal placement minimizes peri-implant stress and lowers marginal bone resorption risk.

## 세줄요약

유한요소해석(FEA)으로 3개 임플란트 연결 보철물의 4가지 수직 플랫폼 정렬(전 치조정→전 치조하)을 400 N 수직·경사(45°) 하중 하에서 비교한 연구(이방성 하악 골 블록 모델, n=4 구성).

혼합 구성 B(중앙 치조하·측방 치조정)는 경사 하중 시 피질골 응력 ~116 MPa(생리적 한계 120 MPa 근접)로 최고; 전 치조하 구성 D는 피질골 응력 32 MPa, 해면골 2.11 MPa로 최소.

수직 정렬이 균일할수록(혼합 금지) 응력이 분산되며, 특히 전 치조하 배치가 생리적 응력 한계 이내 유지와 변연골 흡수 위험 최소화에 최적.

## Summary

This 3D finite element analysis is the first to examine the biomechanical impact of vertical platform misalignment in three-implant splinted prostheses across all clinically relevant crestal–subcrestal permutations. Four configurations of AoN Implants (3.5 mm × 13 mm) in a simplified mandibular segment were modeled with anisotropic bone properties and subjected to 400 N vertical and 45° oblique loads. Results showed that mixed vertical alignment — specifically Model B (central implant 2 mm subcrestal, lateral implants crestal) — generated the highest peri-implant stresses under both loading modes, with cortical bone stress reaching ~116 MPa under oblique loading and approaching the physiological tolerance threshold. Conversely, Model D (all implants uniformly subcrestal, central at 3 mm) achieved the lowest stresses: 32 MPa cortical, 2.11 MPa trabecular. The abutment–implant connection was the universal stress concentration site across all models. These findings support uniform subcrestal placement as the preferred biomechanical strategy and provide a computational basis for the clinical observation that vertical discrepancy ≥0.5 mm in splinted configurations predisposes to marginal bone resorption.

## Key Contributions

- First FEA study on vertical alignment in three-implant splinted prostheses (prior work confined to single implants)
- Quantified cortical bone stress approaching physiological limit in mixed B configuration under oblique loading (~116 MPa vs. 120 MPa threshold)
- Identified abutment–implant connection as the universal critical stress concentration zone regardless of crestal position
- Demonstrated all-subcrestal uniform placement (Model D) as the biomechanically optimal configuration: 32 MPa cortical / 2.11 MPa trabecular under oblique 400 N

## Methodology

3D FEA (in-vitro computational). Three AoN Implants Srl titanium implants (3.5 mm ⌀ × 13 mm, single sharp thread, conometric connection) in anisotropic mandibular bone block (cortical 1.5 mm, full osseointegration). ANSYS Workbench R2023; 0.5 mm tetrahedral mesh (convergence verified <5%); non-linear frictional contacts (Ti–Ti 0.3, cortical–implant 0.65, trabecular–implant 0.77). Loads: 400 N vertical + 400 N oblique 45° (buccal + distal direction). Four configurations: A all-crestal, B central-subcrestal/lateral-crestal, C all 2 mm subcrestal, D central 3 mm / lateral 2 mm subcrestal.

## Results

**Peak Von Mises stress — implant components (400 N vertical):**

| Configuration | Peak (MPa) |
|---|---|
| A — all crestal | 71.5 |
| B — central subcrestal, lateral crestal | 89.2 |
| C — all 2 mm subcrestal | 52.6 |
| D — all subcrestal (deepest) | 66.4 |

**Cortical bone Von Mises stress (400 N vertical):**

| Configuration | Cortical (MPa) | Trabecular (MPa) |
|---|---|---|
| A — all crestal | 14.56 (uniform) | 1.18 |
| B — mixed | 26.69 (central) | 2.26 |
| C — all subcrestal | lower | 1.30 |
| D — all subcrestal deep | lowest | 0.73 |

**Cortical bone Von Mises stress (400 N oblique 45°):**

| Configuration | Cortical (MPa) | Note |
|---|---|---|
| B — mixed | ~116 | Near 120 MPa physiological limit |
| D — all subcrestal | 32 | Well within physiological range |
| D — trabecular | 2.11 | Minimal |

**Implant peak stress under oblique 400 N:** Model A 823 MPa, Model B 724 MPa (both highest; stress at abutment–implant connection). Models C and D substantially lower.

## Related Papers

- [[implants/chang-2024-optimization-implant-design-bone-quality-fea]] — FEA implant design optimization in three bone qualities; ceddia-2025 extends FEA approach to multi-implant splinted context
- [[implants/hussein-2019-thread-depth-implant-shape-stress-mandible-fea]] — FEA thread depth and implant shape effects on mandibular stress; reinforces importance of implant geometry parameters on crestal bone loading
- [[implants/full-arch/baki-2025-all-on-4-trefoil-five-implant-fea]] — Full-arch FEA under 45° oblique loading; comparable oblique-load FEA methodology and physiological threshold analysis
- [[implants/mbl/schwarz-2013-implant-abutment-connection-platform-switching]] — Crestal/subcrestal positioning and MBL outcomes; provides clinical complement to ceddia-2025's biomechanical predictions
