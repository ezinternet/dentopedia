---
title: "The Influence of Insertion Torque on Stress Distribution in Peri-Implant Bones Around Ultra-Short Implants: An FEA Study"
authors: Ceddia Mario, Montesani Lorenzo, Comuzzi Luca, Cipollina Alessandro, Deporter Douglas A., Di Pietro Natalia, Trentadue Bartolomeo
year: 2025
doi: 10.3390/jfb16070260
date: 2025-01-01
source: ceddia-2025-the-influence-of-insertion-torque.md
category: [implants]
evidence_level: in-vitro
source_collection: pubmed-text
full_text: true
pmid: "40710474"
pmcid: "PMC12296050"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12296050/
text_path: /Users/oracleneo/llm-wiki/papers/ceddia-2025-the-influence-of-insertion-torque.txt
text_filename: ceddia-2025-the-influence-of-insertion-torque.txt
tags: [insertion-torque, FEA, ultra-short-implant, bone-stress, microfracture, D2-D4, von-mises, cortical-bone, computational]
relations:
  - type: reinforces
    target: spresser-2025-high-insertional-torque-early
    note: Independent computational stress model consistent with the clinical high-torque early-failure signal; different design (FEA vs prospective cohort)
---

## Three-line Summary
Finite element analysis (FEA) of a 4 mm long, 6 mm diameter ultra-short implant simulating stepwise insertion into D2 and D4 mandibular bone blocks at insertion torques (IT) of 35 N·cm and 75 N·cm; von Mises stress was compared with ultimate strength thresholds (cortical 90 MPa, trabecular 10 MPa).
Raising IT from 35 to 75 N·cm raised peak stress in both bones: D4 cortical bone went from about 79 MPa (step 1) / 65 MPa (fully inserted) at 35 N·cm to 110 / 124 / 142 MPa across insertion steps at 75 N·cm, exceeding the 90 MPa threshold; D2 cortical stress at 75 N·cm reached 86 MPa and trabecular 27 MPa.
The authors conclude that moderate IT (about 35 N·cm) keeps stress within safe limits and that excessive IT, especially in low-density D4 bone, risks microfracture and necrosis; this is a single-implant, isotropic, perfect-contact computational model with no experimental validation, and trabecular stress at 35 N·cm in D4 (37 MPa) still exceeded the 10 MPa threshold.

## 세줄요약
초단형 임플란트 (ultra-short implant, 길이 4 mm·직경 6 mm)를 D2·D4 하악골 블록에 단계별로 삽입하는 상황을 35 N·cm와 75 N·cm 삽입 토크 (insertion torque, IT)에서 유한요소분석 (Finite Element Analysis, FEA)으로 모사하고, von Mises 응력을 피질골 90 MPa·해면골 10 MPa 극한강도와 비교했다.
IT를 35에서 75 N·cm로 올리자 양쪽 골에서 최대 응력이 증가했다: D4 피질골은 35 N·cm에서 약 79 MPa (1단계)/65 MPa (완전 삽입)였으나 75 N·cm에서는 단계별 110/124/142 MPa로 90 MPa 기준을 초과했고, D2에서 75 N·cm의 피질골 86 MPa·해면골 27 MPa에 도달했다.
저자들은 약 35 N·cm의 적정 IT가 응력을 안전 범위에 두고 과도한 IT(특히 저밀도 D4)는 미세골절·괴사 위험을 높인다고 결론지었으나, 단일 임플란트·등방성·완전접촉 가정의 컴퓨터 모델이며 실험적 검증이 없고, D4 해면골 응력은 35 N·cm에서도 37 MPa로 10 MPa 기준을 넘는다.

## Summary
This finite element analysis simulated stepwise insertion of a 6 mm x 4 mm ultra-short implant into D2 and D4 mandibular bone blocks at 35 and 75 N·cm and compared von Mises stress with cortical (90 MPa) and trabecular (10 MPa) ultimate strengths. Higher IT raised stress in both cortical and trabecular bone, most strikingly in D4 cortical bone (about 79 to 142 MPa range across conditions), which exceeded the cortical threshold at 75 N·cm. The authors conclude IT should be controlled, particularly in low-density bone, and suggest cortical drills or densification techniques to lower stress. It is a computational model with simplifying assumptions and no experimental validation.

## Key Contributions
- Stepwise (dynamic) insertion FEA for an ultra-short implant across two IT levels and two bone densities.
- Separate cortical and trabecular stress readouts against ultimate-strength thresholds.
- Mechanistic support for the clinical concern that high IT, especially in D4 bone, risks microdamage.

## Methodology
3D FEA (ANSYS Workbench 2023 R1) of a CT-derived posterior mandibular segment (cortical shell 1.5/0.5 mm, graded trabecular density D2 to D4, isotropic properties), AoN 6 mm x 4 mm Ti-6Al-4V implant, friction contact 0.35, 20 rpm rotation, IT 35 vs 75 N·cm, three insertion steps; about 85,000 bone and 31,000 implant tetrahedral elements, convergence variation under 5%.

## Results
| Condition | Cortical stress | Trabecular stress |
|---|---|---|
| D2, 35 N·cm | 46 MPa (step 1), about 38 MPa later | peak 6 MPa; about 3.34 MPa at full insertion |
| D2, 75 N·cm | 67 MPa (step 1), 86 MPa at full insertion | 27 MPa at full insertion |
| D4, 35 N·cm | about 79 MPa (step 1), about 65 MPa (full) | 37 MPa (full) |
| D4, 75 N·cm | 110, 124, 142 MPa (steps 1 to 3) | 25 to 56 MPa |

Only D4 at 75 N·cm exceeded the 90 MPa cortical threshold; trabecular stress exceeded the 10 MPa threshold in D2 at 75 N·cm and in D4 at both ITs.

## Limitations
- Author-stated: static-derived bone properties, simplified biomechanics, no variation of implant microgeometry; further experimental and dynamic modeling needed.
- Perfect bone-implant adhesion assumed (acknowledged as not clinically realistic); isotropic bone; single implant design.
- No experimental validation in the retrieved text.
- The "35 N·cm is safe" conclusion rests on cortical values; D4 trabecular stress at 35 N·cm (37 MPa) exceeds the paper's own 10 MPa threshold.

## Related Papers
- [[implants/survival/spresser-2025-high-insertional-torque-early]] — clinical high-torque early-failure cohort; this FEA offers a stress-level mechanism
- [[implants/survival/carr-2022-low-insertional-torque-early]] — low-torque end of the same IT-failure relationship; the authors here also note insufficient IT can compromise stability
- [[implants/yang-2024-implant-diameter-tapered-stress-insertion]] — another insertion-stress FEA (macrogeometry axis)
- [[implants/isq/ceddia-2025-finite-element-analysis-of-implant]] — same group's FEA of bone stress and ISQ for implant inclination
- [[overviews/high-insertion-torque-primary-stability-crestal-bone-overview]] — synthesis of high-IT evidence
