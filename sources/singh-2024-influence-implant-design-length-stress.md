---
title: "Influence of implant design and length on stress distribution in immediately loaded implants in posterior maxilla – A two-dimensional finite element analysis"
authors: Rika Singh, Shrikar R Desai, R G Shiva Manjunath
year: 2024
doi: 10.4103/jisp.jisp_531_22
category: [implants]
source_collection: pubmed-text
full_text: true
pmid: "38434497"
pmcid: "PMC10906790"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10906790/
text_path: /Users/oracleneo/llm-wiki/papers/singh-2024-influence-implant-design-length-stress.txt
text_filename: singh-2024-influence-implant-design-length-stress.txt
---

## Why Ingested

기존 [[implants/leblebicioglu-kurtulus-2022-fea-implant-design-bone-density-stress]]는 FEA로 임플란트 *디자인(나사)·골밀도*의 crestal 응력 효과를 정량화했으나 **픽스쳐 길이** 변수는 다루지 않았다. 본 2D FEA (Singh 2024)는 동일 직경(3.75 mm)·동일 디자인에서 **6 mm vs 10 mm 길이만 바꿔** crestal/bone-implant 계면 von Mises 응력을 직접 정량화(예: step 6 mm 188 MPa vs step 10 mm 35.44 MPa, 수직하중)해 길이-응력 관계의 정량 근거를 위키에 보강한다. [[overviews/implant-macrogeometry-clinical-outcomes-overview]]의 거대형태-crestal 응력 논지에 길이 축을 추가.

Study-type note: FEA(전산 시뮬레이션, in-vitro) — 절대 MPa 값은 모델 가정(2D, homogeneous·isotropic·linear elastic, 단순 하중)에 종속되므로 **모델 내 상대 비교(길이·디자인·하중방향)** 로만 해석. 임상 절대 임계값으로 전용 금지.

## Three-line Summary

2D finite element analysis (ANSYS) of standard-diameter (3.75 mm) tapered and step implants in D4 posterior maxilla under immediate loading, comparing 6 mm vs 10 mm fixture length under 100 N vertical and 45° oblique loads.

Von Mises stress at the bone-implant interface was consistently lower for 10 mm than 6 mm implants; step design gave the widest length gap (vertical 188 MPa at 6 mm vs 35.44 MPa at 10 mm; oblique 319.2 vs 96.9 MPa), and step 6 mm was the highest-stress model while step 10 mm was the lowest across all conditions; oblique loads exceeded vertical in every model.

In low-density bone with adequate height, standard-diameter long step implants are biomechanically preferable; crestal microthreads concentrate stress in the thin D4 cortical layer, and standard-diameter short implants did not achieve favorable stress distribution (needing wider diameter or alternative threads).

## 세줄요약

D4 상악 구치부·즉시하중 조건에서 표준직경(3.75 mm) 테이퍼드·스텝 임플란트를 6 mm vs 10 mm 길이로 비교한 2D 유한요소해석(FEA, ANSYS), 100 N 수직 및 45° 사면 하중.

골-임플란트 계면 von Mises 응력은 10 mm가 6 mm보다 일관되게 낮았고, 스텝 디자인에서 길이 차가 가장 컸으며(수직 188 vs 35.44 MPa, 사면 319.2 vs 96.9 MPa), 스텝 6 mm가 전 조건 최고·스텝 10 mm가 최저 응력 모델, 사면하중이 수직하중보다 항상 높았다.

저밀도골에 골높이가 충분하면 표준직경 긴 스텝 임플란트가 역학적으로 유리하고, crestal 마이크로스레드는 얇은 D4 피질골에 응력을 집중시키며, 표준직경 짧은 임플란트는 응력 분산이 불리해 광직경·대체 나사 형태가 필요하다.

## 1. Document Information

- **Type**: Two-dimensional finite element analysis (in-vitro / computational simulation)
- **Journal**: Journal of Indian Society of Periodontology, 2024;27(6):600-606
- **DOI**: [10.4103/jisp.jisp_531_22](https://doi.org/10.4103/jisp.jisp_531_22) · PMID 38434497 · PMCID PMC10906790
- **Source**: PubMed Central full text (JATS); no PDF (pubmed-text branch)
- **Software**: ANSYS classic v11

## 2. Key Contributions

- Isolates **fixture length (6 vs 10 mm)** as a variable at fixed diameter (3.75 mm) and fixed thread scheme, quantifying its effect on bone-implant interface von Mises stress/strain — the length axis that design/density FEA pages in this wiki did not cover.
- Crosses length with **design (step vs tapered)** and **load direction (vertical vs 45° oblique)** in worst-case D4 bone (0.5 mm cortical), the failure-prone scenario (Jaffin & Berman: 55% of failures in D4).
- Shows the length benefit is design-dependent: the **step** design amplifies the long-vs-short stress gap far more than the tapered design.

## 3. Methodology and Architecture

- 2D FE models, cancellous D4 core + 0.5 mm cortical shell, maxillary posterior region.
- Implants: 3.75 mm diameter; 6 mm and 10 mm lengths; tapered and step designs; crestal microthreads (0.2 mm pitch, 29°) + acme body threads (0.8 mm pitch, 29°).
- Material properties (homogeneous, linear elastic): D4 trabecular 1.10 GPa; cortical 13.7 GPa; titanium 110 GPa; Poisson 0.3–0.33.
- Interface friction coefficient 0.6 (immediate loading, not fully osseointegrated).
- Loads: 100 N vertical (long axis) and 45° oblique. Outputs: total deformation, von Mises stress, von Mises strain.

## 4. Key Results and Benchmarks

**Von Mises stress (bone-implant interface), by length:**

| Design | Load | 6 mm | 10 mm |
|---|---|---|---|
| Tapered | Vertical | 94.2 MPa | 47.2 MPa |
| Tapered | Oblique (45°) | 306.6 MPa | 204.4 MPa |
| Step | Vertical | 188 MPa | 35.44 MPa |
| Step | Oblique (45°) | 319.2 MPa | 96.9 MPa |

- **Length**: 10 mm < 6 mm for stress and strain in every design/load combination. Step 10 mm = lowest-stress model overall; step 6 mm = highest.
- **Total deformation (micromovement)**: 36.43% (vertical) / 26.9% (oblique) lower for 10 mm vs 6 mm; least for step 10 mm, greatest for step 6 mm.
- **Load direction**: oblique > vertical stress/strain in all models (oblique loading drives peak cortical stress).
- Crestal microthreads → stress concentrated in the thin D4 cortical layer where trabecular support is sparse.

## 5. Limitations and Future Work

- 2D model; homogeneous/isotropic/linear-elastic assumptions unlike living bone; simplified axial+oblique loads; no cement layer — so absolute MPa are model-relative, not clinical thresholds.
- Standard-diameter short implants did not achieve favorable distribution in D4; authors call for evaluation of wide-diameter short implants and alternative thread forms, plus animal/clinical validation.

## 6. Related Work

- [[implants/leblebicioglu-kurtulus-2022-fea-implant-design-bone-density-stress]] — FEA of implant design × bone density × abutment angle on crestal stress; this page adds the length axis.
- [[overviews/implant-macrogeometry-clinical-outcomes-overview]] — macrogeometry (design/thread) vs clinical outcomes synthesis.

## 7. Glossary

- **FEA (Finite Element Analysis, 유한요소해석)**: numerical method subdividing a structure into elements to compute stress/strain.
- **Von Mises stress**: scalar equivalent stress used to predict yielding under combined loading.
- **D4 bone**: fine trabecular, low-density bone (Lekholm & Zarb) — highest implant failure risk.
- **Microthread / Acme thread**: fine crestal-module threads vs trapezoidal body threads for stress distribution.
- **Immediate loading**: functional prosthetic loading shortly after placement (frictional, not yet osseointegrated interface).
