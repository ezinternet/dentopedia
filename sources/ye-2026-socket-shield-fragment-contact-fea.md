---
title: "Biomechanical Effects of Implant-Root Fragment Contact in the Socket Shield Technique: A Finite Element Analysis"
authors: "Ye Z, Zhang Y, Feng Z, Shangguan G, Huang C, Chen X, Ye H"
year: 2026
doi: 10.1016/j.identj.2026.109623
pmid: "42172860"
pmcid: "PMC13223945"
category: immediate-implant/socket-shield
evidence_level: in-vitro
source_collection: pubmed-text
full_text: true
text_path: /Users/oracleneo/llm-wiki/papers/ye-2026-socket-shield-fragment-contact-fea.txt
text_filename: ye-2026-socket-shield-fragment-contact-fea.txt
---

## Why Ingested

기존 소켓 실드(Socket Shield Technique, SST) 유한요소분석(Finite Element Analysis, FEA) 문헌([[immediate-implant/socket-shield/neves-2023-socket-shield-stress-distribution-fea]])은 실드 유무·이식재 조건 비교에 집중했지만, 임플란트-실드 편 직접 접촉 시 편 각도(arc angle)가 응력 분포에 미치는 영향은 정량화된 바 없었다. 이 논문은 60°–180° 5가지 호각도를 FEA로 체계적으로 비교해, 임상적으로 피할 수 없는 직접 접촉 상황에서 120°–150°가 생역학적으로 유리한 범위임을 제시한다.

## Three-line Summary

3D finite element analysis of maxillary anterior socket-shield immediate implants modeled five buccal root-fragment arc angles (60°–180°, 1.5-mm thick, 6-mm long) under 30 N·cm insertion torque and 100-N occlusal load; natural-tooth PDL served as the biomechanical reference (PDL peak stress 2.472 MPa).

Under torque loading, fragment and PDL peak stress decreased monotonically as arc angle increased (60°: 101.9 MPa / 4.073 MPa → 180°: 42.43 MPa / 1.067 MPa); under occlusal loading, PDL stress remained below the natural-tooth reference at all angles (1.143–1.996 MPa), while cortical bone stress showed a non-linear minimum at 120° (47.62 MPa) and a marked increase at 180° (64.51 MPa).

An arc angle of 120°–150° provides the most favorable biomechanical balance — reducing fragment/PDL stress during insertion while avoiding the cortical bone stress escalation seen at larger arcs — though cyclic loading validation and clinical prospective studies are needed.

## 세줄요약

상악 전치부 소켓 실드 임플란트의 5가지 치근편 호각도(60°–180°, 두께 1.5 mm, 길이 6 mm)를 삽입 토크(30 N·cm)와 교합 하중(100 N) 조건에서 3D 유한요소분석; 자연치 치주인대(Periodontal Ligament, PDL) 최대 응력 2.472 MPa를 생역학 기준치로 사용.

삽입 토크 하: 치근편·PDL 최대 응력이 호각도 증가에 따라 단조 감소(60°: 101.9 MPa / 4.073 MPa → 180°: 42.43 MPa / 1.067 MPa). 교합 하중 하: PDL 응력은 전 각도에서 자연치 기준 이하(1.143–1.996 MPa)이나, 피질골 응력은 비선형 — 120°에서 최소(47.62 MPa), 180°에서 급등(64.51 MPa).

호각도 120°–150°가 생역학적으로 가장 균형 잡힌 범위 — 삽입 시 치근편·PDL 응력 감소와 교합 시 피질골 응력 급등 방지를 동시에 충족. 단, 반복 하중 검증 및 임상 전향 연구 필요.

## Document Information

- **Journal**: International Dental Journal
- **DOI**: [10.1016/j.identj.2026.109623](https://doi.org/10.1016/j.identj.2026.109623)
- **Year**: 2026, Volume 76, Issue 4, Page 109623
- **Institution**: Wenzhou Medical University affiliated hospitals (China)

## Key Contributions

- First FEA systematically varying SST fragment arc angle under both insertion torque and occlusal loading
- Demonstrates non-linear cortical bone stress response — optimal range is 120°–150°, not maximum coverage
- Natural tooth PDL stress (2.472 MPa) established as a reference point; SST direct-contact PDL stays below this threshold at all arc angles under occlusal load
- Direct contact (no jumping gap) dramatically increases cortical bone stress vs gap-graft SST (previous model: 23.11 MPa cortical; present 120° model: 47.62 MPa)
- Confirms fragment displacement risk with small arcs (60°–90°) during placement — 52.7% less displacement from 60° to 180°

## Methodology

- **Design**: 3D FEA, comparative computational study
- **CBCT source**: Single healthy adult (Kava PP3-1 CBCT, 0.125-mm voxel)
- **Software**: Mimics 21.0 (segmentation), 3-Matic (fragment modelling), HyperMesh 11.0 (meshing), Abaqus 6.14 (FEA)
- **Implant**: Nobel BLT 3.5 × 11.5 mm, threaded tapered design
- **Shield models**: 5 arc angles (60°, 90°, 120°, 150°, 180°); thickness 1.5 mm; length 6 mm; C-shaped; 0.2-mm PDL modelled as offset
- **Loading**: (1) Insertion torque 30 N·cm (frictional contact μ=0.3); (2) 100-N occlusal load on lingual fossa
- **Mesh**: 4-node linear tetrahedral (C3D4); 0.125-mm refinement at implant/bone/fragment/PDL interface; convergence verified (<5% difference)
- **Outcome measures**: von Mises peak stress, stress distribution, displacement in PDL, fragment, implant, cortical bone, cancellous bone

## Key Results

**Under 30 N·cm insertion torque:**
| Arc angle | Fragment peak (MPa) | PDL peak (MPa) | Displacement (mm) |
|---|---|---|---|
| 60° | 101.9 | 4.073 | 0.01651 |
| 90° | 75.48 (−25.9%) | — | 0.01362 |
| 120° | 69.62 (−31.7%) | — | 0.01115 |
| 150° | 67.14 (−34.1%) | — | 0.009781 |
| 180° | 42.43 (−58.4%) | 1.067 (−73.8%) | 0.007814 |

**Under 100-N occlusal load:**
| Arc angle | Fragment peak (MPa) | PDL peak (MPa) | Cortical bone (MPa) |
|---|---|---|---|
| 60° | 87.40 | **1.143** (lowest) | 49.74 |
| 90° | 72.05 | — | 47.77 |
| 120° | 63.55 | — | **47.62** (minimum) |
| 150° | 62.20 | — | 50.83 |
| 180° | 61.57 | **1.996** (highest) | **64.51** (+29.7%) |

- Natural tooth PDL reference: 2.472 MPa (all SST conditions remain below this)
- Adjacent natural teeth: <0.4% variation across all models (fragment geometry does not affect neighbor biomechanics)

## Limitations

- Static (not cyclic/fatigue) loading model
- Single CBCT dataset — no anatomical variability
- Homogeneous isotropic linear-elastic material assumptions
- No in vitro or clinical validation
- Fragment modelled as dentin-cementum complex (simplified homogeneous)

## Related Work

- [[immediate-implant/socket-shield/neves-2023-socket-shield-stress-distribution-fea]] — compared SS vs HBG vs healed-bone conditions; present study extends to direct-contact arc angle analysis
- [[immediate-implant/socket-shield/gharpure-2022-socket-shield-conventional-implant-sr-ma]] — clinical SST outcomes
- [[immediate-implant/socket-shield/oliva-2023-socket-shield-buccal-bone-preservation-sr]] — buccal bone preservation with SST

## Glossary

- **Socket shield technique (SST)**: Retaining the buccal root fragment to preserve the periosteum-PDL complex and prevent buccal plate resorption after immediate implant placement
- **Arc angle (θ)**: In cross-section, the angle subtended about the implant long axis by the mesial-to-distal endpoints of the retained fragment
- **Jumping gap**: The space between the implant and buccal root fragment; this study models direct contact (no gap)
- **von Mises stress**: A scalar stress criterion indicating structural yielding risk under multi-axial loading
- **PDL (치주인대)**: The fibrous connective tissue connecting tooth root cementum to alveolar bone; in SST, remains attached to the retained buccal root fragment
