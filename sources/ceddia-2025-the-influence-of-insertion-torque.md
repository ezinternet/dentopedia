---
title: "The Influence of Insertion Torque on Stress Distribution in Peri-Implant Bones Around Ultra-Short Implants: An FEA Study"
authors: Ceddia Mario, Montesani Lorenzo, Comuzzi Luca, Cipollina Alessandro, Deporter Douglas A., Di Pietro Natalia, Trentadue Bartolomeo
year: 2025
doi: 10.3390/jfb16070260
category: implants
source_collection: pubmed-text
full_text: true
pmid: "40710474"
pmcid: "PMC12296050"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12296050/
text_path: /Users/oracleneo/llm-wiki/papers/ceddia-2025-the-influence-of-insertion-torque.txt
text_filename: ceddia-2025-the-influence-of-insertion-torque.txt
---

## Why Ingested
Requested for the wiki's high-insertion-torque / crestal-bone-harm question: it supplies a mechanistic (computational) account of how IT magnitude and bone density change peri-implant cortical and trabecular stress during insertion, complementing the clinical early-failure evidence. It reinforces the high-torque-harm side of [[wiki/implants/survival/spresser-2025-high-insertional-torque-early]] (IT ≥60 N·cm and early failure) and extends [[wiki/overviews/high-insertion-torque-primary-stability-crestal-bone-overview]] with FEA-level stress values for ultra-short implants.

## Three-line Summary
Finite element analysis (FEA) of a 4 mm long, 6 mm diameter ultra-short implant simulating stepwise insertion into D2 and D4 mandibular bone blocks at insertion torques (IT) of 35 N·cm and 75 N·cm; von Mises stress was compared with ultimate strength thresholds (cortical 90 MPa, trabecular 10 MPa).
Raising IT from 35 to 75 N·cm raised peak stress in both bones: D4 cortical bone went from about 79 MPa (step 1) / 65 MPa (fully inserted) at 35 N·cm to 110 / 124 / 142 MPa across insertion steps at 75 N·cm, exceeding the 90 MPa threshold; D2 cortical stress at 75 N·cm reached 86 MPa and trabecular 27 MPa.
The authors conclude that moderate IT (about 35 N·cm) keeps stress within safe limits and that excessive IT, especially in low-density D4 bone, risks microfracture and necrosis; this is a single-implant, isotropic, perfect-contact computational model with no experimental validation, and trabecular stress at 35 N·cm in D4 (37 MPa) still exceeded the 10 MPa threshold.

## 세줄요약
초단형 임플란트 (ultra-short implant, 길이 4 mm·직경 6 mm)를 D2·D4 하악골 블록에 단계별로 삽입하는 상황을 35 N·cm와 75 N·cm 삽입 토크 (insertion torque, IT)에서 유한요소분석 (Finite Element Analysis, FEA)으로 모사하고, von Mises 응력을 피질골 90 MPa·해면골 10 MPa 극한강도와 비교했다.
IT를 35에서 75 N·cm로 올리자 양쪽 골에서 최대 응력이 증가했다: D4 피질골은 35 N·cm에서 약 79 MPa (1단계)/65 MPa (완전 삽입)였으나 75 N·cm에서는 단계별 110/124/142 MPa로 90 MPa 기준을 초과했고, D2에서 75 N·cm의 피질골 86 MPa·해면골 27 MPa에 도달했다.
저자들은 약 35 N·cm의 적정 IT가 응력을 안전 범위에 두고 과도한 IT(특히 저밀도 D4)는 미세골절·괴사 위험을 높인다고 결론지었으나, 단일 임플란트·등방성·완전접촉 가정의 컴퓨터 모델이며 실험적 검증이 없고, D4 해면골 응력은 35 N·cm에서도 37 MPa로 10 MPa 기준을 넘는다.

## 1. Document Information
- **Journal**: Journal of Functional Biomaterials 2025;16(7):260
- **DOI**: 10.3390/jfb16070260
- **PMID / PMCID**: 40710474 / PMC12296050
- **Institution**: not stated in the retrieved text

## 2. Key Contributions
- Dynamic, stepwise FEA of the insertion process (three insertion depth steps over the 4 mm implant length) rather than a static post-placement load model.
- Compares two ITs (35 and 75 N·cm) across two bone qualities (D2, D4) for an ultra-short implant, a combination the authors state has few prior FEA studies.
- Reports cortical and trabecular von Mises stress separately against ultimate-strength thresholds (cortical 90 MPa, trabecular 10 MPa).

## 3. Methodology and Architecture
- **Design**: 3D finite element analysis (Autodesk Inventor 2024 geometry; ANSYS Workbench 2023 R1 simulation). No clinical or bench specimens.
- **Bone model**: mandibular segment from CT of a healthy edentulous posterior mandible; block 20 mm height x 15 mm mesiodistal x 10 mm buccolingual at crest; cortical shell 1.5 mm (superior) and 0.5 mm (lateral); trabecular density graded toward the base (D2 to D4, Misch classification); isotropic properties derived from density-stiffness equations.
- **Implant**: AoN Implants Srl, 6 mm diameter x 4 mm length, Ti-6Al-4V; perfect bone-implant adhesion assumed in the osteotomy geometry.
- **Boundary/loading**: base fixed; friction contact (coefficient 0.35); rotation at 20 rpm; ITs of 35 and 75 N·cm per manufacturer protocol.
- **Insertion simulation**: three models (step 1 = 0.2 mm into cortical bone, through full 4 mm).
- **Mesh**: 10-node quadratic tetrahedra (SOLID 187); about 85,000 elements bone (0.5 mm), about 31,000 implant; 0.2 mm refinement at threads; convergence variation less than 5%.
- **Outcome**: von Mises stress vs ultimate strength (cortical 90 MPa, cancellous 10 MPa).

## 4. Key Results and Benchmarks
| Bone / IT | Cortical peak stress | Trabecular stress |
|---|---|---|
| D2, 35 N·cm | 46 MPa (step 1), about 38 MPa later; about 3.34 MPa at full insertion | peak 6 MPa; about 3.34 MPa at full insertion |
| D2, 75 N·cm | 67 MPa (step 1); 86 MPa at full insertion | 27 MPa at full insertion |
| D4, 35 N·cm | about 79 MPa (step 1) to about 65 MPa (full insertion) | 37 MPa (full insertion) |
| D4, 75 N·cm | about 110 (step 1), 124 (step 2), 142 MPa (step 3) | 25 to 56 MPa across steps |

- Against the 90 MPa cortical threshold, only D4 at 75 N·cm exceeded it (142 MPa); D2 at 75 N·cm reached 86 MPa.
- Against the 10 MPa trabecular threshold, D2 at 75 N·cm (27 MPa), D4 at 35 N·cm (37 MPa) and D4 at 75 N·cm (25 to 56 MPa) were above it.
- The authors attribute the fall in D4 cortical stress during insertion at 35 N·cm to load absorption by trabecular bone.
- Discussion notes that many studies recommend a maximum IT of 80 N·cm, and that a rise in IT does not necessarily cause damage if stress stays below tissue strength (bone remodeling adaptation); cortical drills and densification techniques are suggested to reduce stress.

## 5. Limitations and Future Work
- Author-stated: dynamic mechanical properties of mandibular bone are not well defined; static-derived Young's modulus/Poisson's ratio used; simplified biomechanical assumptions; implant microgeometry not varied; further experimental and dynamic modeling studies needed.
- Perfect bone-implant adhesion in the osteotomy geometry is acknowledged by the authors as not occurring clinically.
- Isotropic bone assumption (the Methods text itself cites that isotropic models underestimate stress).
- Single implant design and a single bone-block geometry; no experimental validation reported in the retrieved text.
- Reviewer note: the stated conclusion that 35 N·cm stays "within safe limits" is based on cortical values; the trabecular values at 35 N·cm in D4 (37 MPa) exceed the 10 MPa threshold the paper itself uses.

## 6. Related Work
- Demirbas et al. (cited): dynamic FEA, 75 N·cm in D4 bone exceeded strength thresholds; cortical drill reduced crestal stress.
- Van Staden et al. (cited): stress in cortical and trabecular bone varies with insertion depth and torque, peak near implant neck late in insertion.
- Joshi et al. (cited review): bone density determines appropriate IT.

## 7. Glossary
- **IT (insertion torque)**: rotational force applied while seating the implant, N·cm.
- **Von Mises stress**: equivalent stress used to predict yielding of the material.
- **D2 / D4**: Misch bone density classes (D2 dense, D4 low-density trabecular).
- **FEA**: finite element analysis.
