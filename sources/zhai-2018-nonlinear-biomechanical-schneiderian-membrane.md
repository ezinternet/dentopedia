---
title: "Nonlinear Biomechanical Characteristics of the Schneiderian Membrane: Experimental Study and Numerical Modeling"
authors: "Zhai M, Cheng H, Yuan J, Wang X, Li B, Li D"
year: 2018
doi: "10.1155/2018/2829163"
category: [sinus-lift/lateral]
source_collection: pubmed-abstract
full_text: true
pmid: "30035119"
pmcid: "PMC6033247"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6033247/
---

## Why Ingested

슈나이데리안 막 물성(탄성·인장강도·골부착력)의 **최초 비선형 생체역학 실측** 논문. 기존 위키가 천공 위험 인자([[sinus-lift/lateral/alalshaikh-2024-membrane-perforation-risk-factors-lateral-sinus-sr-ma]])·막 두께([[sinus-lift/lateral/khiabani-2024-sinus-membrane-thickness-lsfe-mucosal]])를 다루지만, 막이 실제로 얼마나 늘어나야 찢어지는지의 수치적 기반이 없었다. 이 논문이 그 빈 칸을 채운다.

## One-line Summary

Ex vivo cadaveric study (n=30 specimens, 16 cadavers) quantified nonlinear tensile strength (elongation 5.05 N/mm, perforation 8.57 N/mm), linear elastic modulus (27.1–53.6 MPa), and adhesion force (0.052 N/mm) of the Schneiderian membrane, implementing these data in a validated FE model.

## 한줄요약

인체 사체 표본(n=30, 16구) ex vivo 인장시험: 슈나이데리안 막 인장강도 신장시험 5.05 N/mm·천공시험 8.57 N/mm, 탄성계수 27.1–53.6 MPa, 골부착력 0.052 N/mm를 측정하고 비선형 유한요소 모델로 검증.

## 1. Document Information

- **Journal**: BioMed Research International, 2018;2018:2829163
- **Published**: 2018-06-21
- **DOI**: 10.1155/2018/2829163 | **PMID**: 30035119 | **PMCID**: PMC6033247
- **Study type**: Ex vivo experimental + FE numerical modeling
- **Funding/COI**: Fourth Military Medical University (State Key Laboratory of Military Stomatology); no conflicts declared

## 2. Key Contributions

- **First nonlinear characterization** of Schneiderian membrane mechanical behavior — prior work (Pommer et al.) used only linear parameters (49–70 MPa), which underestimate realistic soft-tissue response.
- **Tensile strength differential by loading mode**: elongation (strip) 5.05±0.97 N/mm vs. perforation (indenter) 8.57±3.75 N/mm — a 70% gap, reflecting biaxial constraint geometry.
- **Adhesion force** between membrane and sinus floor bone: 0.052±0.021 N/mm (range 0.011–0.093 N/mm) — first direct measurement.
- **Nonlinear FE model** (R²=0.99065) outperforms linear model (R²=0.94656) in fitting experimental stress–strain curves.
- **Hyper-elastic material parameters** derived (Mooney-Rivlin: C10=0.253, C01=0.026), enabling realistic simulation of large-deformation membrane behavior during sinus lifting.

## 3. Methodology and Architecture

- **Specimens**: 32 maxillae from 16 cadavers (8M, 8W; mean age 77y) from Fourth Military Medical University anatomy institute; fresh, stored at 4°C.
- **Three specimen types**: 10×20 mm strips (n=30, elongation), 20×20 mm squares (n=30, perforation), 10×20 mm bone+membrane strips (n=10, adhesion).
- **Thickness measurement**: #15 endodontic reamer + silicone disk stop + micrometer caliper.
- **Elongation test**: displacement rate 0.5 mm/min; both ends fixed; stretched until membrane tearing.
- **Perforation test**: spherical indenter 3mm diameter; centrally loaded membrane square until perforation.
- **Adhesion/detachment test**: piezosurgery to isolate 5mm bone segment; 2mm displacement load applied; force at mucosal detachment recorded.
- **FE software**: ANSYS 16.0; 3804 eight-node quadrilateral elements / 20,368 nodes; nonlinear vs. linear model compared.
- **Statistics**: mixed-effects model; p<0.05.

## 4. Key Results and Benchmarks

| Parameter | Test | Mean ± SD | Range |
|---|---|---|---|
| Membrane thickness (SMT) | Elongation group | 0.94 ± 0.38 mm | 0.33–2.02 mm |
| Membrane thickness (SMT) | Perforation group | 1.07 ± 0.49 mm | 0.35–2.13 mm |
| Tensile strength | Elongation | **5.05 ± 0.97 N/mm** | 2.98–6.69 |
| Tensile strength | Perforation | **8.57 ± 3.75 N/mm** | 1.87–17.86 |
| Linear elastic modulus | Elongation | **27.1 ± 3.7 MPa** | — |
| Linear elastic modulus | Perforation | **53.6 ± 5.1 MPa** | — |
| Adhesion force | Detachment | **0.052 ± 0.021 N/mm** | 0.011–0.093 |
| FE model fit (R²) | Nonlinear | **0.99065** | — |
| FE model fit (R²) | Linear | 0.94656 | — |

- Perforation test showed significantly higher tensile strength AND elastic modulus than elongation test (p<0.05 both).
- Adhesion force data: mean detachment force 1.04 N over the circumference of the elevated area.
- Maximum stress concentrated at **membrane detachment margin** (not center) during FE simulation.

## 5. Limitations and Future Work

- **Cadaveric age bias**: mean 77 years; membrane properties may differ in younger surgical patients.
- **Viscoelastic parameters not measured**: stress relaxation, creep, and recovery characteristics omitted — these affect long-term graft retention.
- **Only elastic deformation phase modeled**: plastic and failure behaviors not fully characterized.
- **Single anatomy**: one CBCT-derived sinus geometry used for FE application.
- Authors call for future studies on viscoelastic behavior and its relationship to new bone absorption post-sinus lift.

## Three-line Summary

- Ex vivo cadaveric study (n=30 specimens from 16 cadavers, mean age 77y) quantifying the nonlinear biomechanical properties of the Schneiderian membrane via uniaxial elongation and biaxial perforation tensile tests, plus adhesion force measurement and finite element model validation.
- Tensile strength was loading-mode dependent: elongation 5.05 N/mm vs perforation 8.57 N/mm; elastic modulus 27.1 vs 53.6 MPa; bone adhesion force 0.052 N/mm; nonlinear hyper-elastic FE model (Mooney-Rivlin C10=0.253, C01=0.026 MPa) achieved R²=0.99.
- Blunt periosteal elevation is biomechanically safer than sharp puncture because point-force perforation requires nearly double the load of uniaxial stretching; maximum stress concentrates at the membrane–bone detachment margin, explaining the edge-origin of intraoperative perforations.

## 세줄요약

- 인체 사체 표본 ex vivo 연구(n=30, 16구, 평균 77세): 슈나이데리안 막(Schneiderian Membrane)의 비선형 생체역학 특성을 단축 신장(elongation)·이축 천공(perforation) 인장시험 및 골부착력 측정, 유한요소 분석(Finite Element Analysis, FEA) 검증으로 최초 정량화.
- 인장강도는 하중 방식 의존적: 신장 5.05 N/mm vs 천공 8.57 N/mm; 탄성계수(Elastic Modulus) 27.1 vs 53.6 MPa; 골부착력 0.052 N/mm; 비선형 초탄성 FEA 모델(Mooney-Rivlin C10=0.253, C01=0.026 MPa) 적합도 R²=0.99.
- 둔기 골막 박리가 예리한 천공보다 역학적으로 안전; 최대 응력은 막-골 박리 경계에 집중 — 이 지점이 수술 중 천공 발생 기원 설명.

## 6. Related Work

- **Pommer et al.**: linear elastic modulus values (49 MPa elongation, 70 MPa biaxial) — this paper extends to nonlinear regime.
- **Hu et al.**: used 70 MPa linear modulus in maxillary sinus FE model — Zhai argues this underestimates realistic behavior.
- Lin 2025 (PMC11773847) uses Mooney-Rivlin parameters from this paper for FEA of transcrestal techniques.

## 7. Glossary

- **Elongation test**: uniaxial strip tensile test; simulates membrane stretched off sinus floor edge
- **Perforation test**: biaxial dome-punch test (3mm spherical indenter); simulates point-force perforation during instrumentation
- **Adhesion force (0.052 N/mm)**: force per unit circumference to detach membrane from underlying bone
- **Mooney-Rivlin (C10, C01)**: hyper-elastic constitutive model for large-deformation soft tissue: C10=0.253 MPa, C01=0.026 MPa
- **SMT**: Schneiderian Membrane Thickness
