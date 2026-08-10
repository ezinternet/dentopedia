---
title: "Evaluation of the Influence of Location of Osseointegrated Implants Associated with Mandibular Removable Partial Dentures"
authors: Ligia Del'Arco Pignatta Cunha, Eduardo Piza Pellizzer, Fellippo Ramos Verri, João Antonio Pereira
year: 2008
doi: null
category: [implants]
pdf_path: /Users/oracleneo/llm-wiki/papers/cunha-2008-implant-location-mandibular-rpd-fea.pdf
pdf_filename: cunha-2008-implant-location-mandibular-rpd-fea.pdf
source_collection: external
---

## Why Ingested

FEA (유한요소법, Finite Element Analysis) 시뮬레이션으로 임플란트 위치가 하악 원심연장 가철성 국소의치 (Removable Partial Denture, RPD)의 응력 분포 및 변위에 미치는 영향을 정량화한 2008년 기초 연구. 하악 임플란트 스트레스 분포를 다루는 [[implants/hussein-2019-thread-depth-implant-shape-stress-mandible-fea]]의 FEA 방법론적 선행 연구로, RPD와 임플란트 결합의 역학적 근거를 제공한다.

## Three-line Summary

2D finite element analysis evaluated the influence of implant location in the distal extension on stress distribution and displacement in a mandibular Kennedy Class I RPD associated with an osseointegrated implant.

Implant placement in the mesial region (second premolar, Model E) provided the best stress distribution for the abutment tooth, while central placement (first molar, Model D) showed the lowest displacement.

Placing the implant closer to the abutment tooth positively influences stress distribution on analyzed structures and improves RPD stability; however, findings are limited to 2D static FEA without clinical validation.

## 세줄요약

줄1: 2차원 유한요소법으로 Kennedy Class I 하악 원심연장 가철성 국소의치 (RPD)에서 임플란트 위치가 응력 분포와 변위에 미치는 영향을 5가지 모델로 평가했다.

줄2: 임플란트를 근심(제2소구치, Model E)에 위치시킬 때 지대치 응력 분포가 가장 양호했고, 중심(제1대구치, Model D)에 위치시킬 때 변위가 가장 적었다.

줄3: 임플란트를 지대치에 가깝게 위치시키는 것이 구조물의 응력 분포에 긍정적 영향을 미치나, 2D 정적 FEA 한계로 임상 검증이 필요하다.

## 1. Document Information

- **Title:** Evaluation of the Influence of Location of Osseointegrated Implants Associated with Mandibular Removable Partial Dentures
- **Authors:** Ligia Del'Arco Pignatta Cunha, Eduardo Piza Pellizzer, Fellippo Ramos Verri, João Antonio Pereira
- **Year:** 2008
- **Journal:** Implant Dentistry, 17(3):278–287
- **Institution:** UNESP (Universidade Estadual Paulista), Brazil
- **DOI:** not available (no-doi; Implant Dentistry 2008;17:278-287)
- **Evidence Level:** in-vitro (FEA — 2D finite element analysis, ANSYS 8.0)
- **N:** 5 FEA models (A–E)
- **Follow-up:** N/A

## 2. Key Contributions

- Establishes that implant location along the distal-extension ridge significantly affects stress distribution and prosthetic displacement in mandibular Kennedy Class I RPD
- Demonstrates a trade-off: mesial implant position (near abutment tooth) optimizes stress relief on the abutment; central position minimizes overall RPD displacement
- Shows that any implant placement—regardless of location—reduces RPD intrusion tendency compared to implant-free controls
- Identifies the internal thread of the implant as the primary stress concentration site in all implant-bearing models

## 3. Methodology and Architecture

- **Design:** 2D finite element analysis (FEA), in vitro
- **Software:** ANSYS 8.0
- **Models:** 5 sagittal cross-section models of mandibular left hemi-arch with Kennedy Class I posterior defect:
  - Model A: Natural dentition control (no RPD, no implant)
  - Model B: RPD only (no implant)
  - Model C: RPD + implant placed distally (second molar region, #37)
  - Model D: RPD + implant placed centrally (first molar region, #36)
  - Model E: RPD + implant placed mesially (second premolar region, #35)
- **Loading:** 50 N vertical force on cusp tips of first premolar and second premolar
- **Analysis outputs:** von Mises stress maps and displacement maps for implant, abutment tooth (canine), alveolar bone, prosthetic framework, and mucosa
- **Geometry:** simplified uniform bone geometry; not patient-specific

## 4. Key Results and Benchmarks

| Model | Implant Position | Abutment Stress | Displacement |
|---|---|---|---|
| A | None (control) | Baseline | Baseline |
| B | RPD only | Higher than A | Higher than A |
| C | #37 (distal) | Moderate reduction | Moderate |
| D | #36 (central) | Moderate reduction | **Lowest** |
| E | #35 (mesial) | **Best relief** | Moderate |

- All implant models reduced RPD intrusion compared to Model B
- Stress concentration consistently at implant internal thread in Models C, D, E
- Moving the implant mesially (toward the abutment tooth) progressively improved abutment stress distribution
- Model D (central) balanced both stress and displacement outcomes

## 5. Limitations and Future Work

- **2D FEA only** — does not capture three-dimensional force components (bucco-lingual forces, torsion)
- **Simplified geometry** — homogeneous, isotropic bone material properties; non-patient-specific anatomy
- **Static loading only** — no dynamic masticatory simulation or fatigue modeling
- **No clinical validation** — all findings are simulation-based; no in vivo or in vitro mechanical testing
- Future work recommended: 3D FEA, patient-specific geometry, dynamic loading, clinical trials on RPD-implant combinations

## 6. Related Work

- [[implants/hussein-2019-thread-depth-implant-shape-stress-mandible-fea]] — FEA-based mandibular implant thread design and stress distribution
- [[implants/premnath-2012-stress-distribution-bone-density-fea]] — FEA comparing stress distribution across Misch bone density classifications in mandibular implants

## 7. Glossary

- **RPD (가철성 국소의치, Removable Partial Denture):** Removable prosthesis replacing missing teeth while retaining natural abutment teeth
- **FEA (유한요소법, Finite Element Analysis):** Computational simulation method dividing a structure into finite elements to calculate stress and displacement under applied loads
- **Distal extension (원심 연장):** RPD design with no posterior abutment tooth — the saddle extends distally unsupported
- **Kennedy Class I (케네디 1급):** Bilateral posterior edentulous area classification
- **Von Mises stress (폰 미제스 응력):** Equivalent stress measure used in FEA to predict yielding/failure under complex loading
- **Abutment tooth (지대치):** Natural tooth serving as support/retention for a prosthesis
- **Osseointegration (골유착, Osseointegration):** Direct structural/functional connection between living bone and implant surface
