---
title: "Nonlinear Biomechanical Characteristics of the Schneiderian Membrane: Experimental Study and Numerical Modeling"
authors: "Zhai M et al."
year: 2018
date: 2018-06-21
doi: "10.1155/2018/2829163"
source: zhai-2018-nonlinear-biomechanical-schneiderian-membrane.md
category: [sinus-lift/lateral]
confidence: in-vitro
source_collection: pubmed-abstract
tags: [schneiderian-membrane, biomechanics, tensile-strength, finite-element-analysis, elastic-modulus, adhesion-force]
relations:
  - type: extends
    target: alalshaikh-2024-membrane-perforation-risk-factors-lateral-sinus-sr-ma
---

## One-line Summary

Ex vivo cadaveric study (n=30, 16 cadavers) providing the first nonlinear biomechanical characterization of the Schneiderian membrane: tensile strength 5.05–8.57 N/mm (mode-dependent), elastic modulus 27.1–53.6 MPa, and bone adhesion force 0.052 N/mm, with a validated hyper-elastic FE model (R²=0.99).

## 한줄요약

인체 사체(n=30, 16구) ex vivo 인장시험: 슈나이데리안 막 비선형 탄성 최초 실측 — 인장강도 5.05–8.57 N/mm(시험법 의존), 탄성계수 27.1–53.6 MPa, 골부착력 0.052 N/mm; 비선형 유한요소 모델 검증(R²=0.99).

## Summary

The Schneiderian membrane behaves as a nonlinear hyper-elastic material, not a simple linear elastic solid. Zhai et al. harvested fresh cadaveric membrane specimens from 16 donors (mean age 77y) and subjected them to two loading modes: uniaxial elongation (strip pulled to tearing) and biaxial perforation (spherical indenter punched through). Elongation yielded a mean tensile strength of 5.05 N/mm and elastic modulus of 27.1 MPa; perforation yielded 8.57 N/mm and 53.6 MPa — both significantly higher under perforation mode (p<0.05), reflecting the geometric constraint of biaxial clamping. Adhesion force between membrane and underlying bone measured 0.052 N/mm. Mooney-Rivlin hyper-elastic parameters (C10=0.253, C01=0.026 MPa) were fitted to the experimental stress–strain curves; the nonlinear model achieved R²=0.99 vs R²=0.95 for the prior linear model, and was applied to simulate sinus floor elevation dynamics. The clinical implication is that the membrane can tolerate point-force perforation at nearly double the load required to tear it by uniaxial stretching — a rationale for why blunt periosteal elevation is safer than sharp puncture.

## Key Contributions

- **First nonlinear quantification** of Schneiderian membrane mechanics: prior work (Pommer et al.) measured only linear elastic moduli (49–70 MPa); this paper shows that soft-tissue nonlinearity matters for realistic simulation.
- **Two-mode tensile data**: elongation strip (simulates lateral window stretching) vs. biaxial perforation (simulates instrumentation point force) — mode-dependent difference of ~70% in both strength and stiffness.
- **Adhesion force first measurement**: 0.052 N/mm — sets the baseline detachment threshold for sinus floor elevation instruments.
- **Hyper-elastic FE material parameters**: Mooney-Rivlin C10/C01 now usable by any FEA study of sinus lifting (cf. [[sinus-lift/transcrestal/lin-2025-schneiderian-membrane-biomechanical-transcrestal-fea]]).
- Maximum stress concentrates at the **membrane detachment margin**, not at the center — explaining why perforations initiate at edges during elevation.

## Methodology

- **Design**: Ex vivo mechanical testing + finite element analysis; no clinical patients.
- **Specimens**: 32 maxillae / 16 cadavers (8M, 8W; mean age 77y); stored 4°C in physiologic saline.
- **Elongation test** (n=30 strips, 10×20 mm): uniaxial pull at 0.5 mm/min until tearing; measures tensile strength and 1D elastic modulus.
- **Perforation test** (n=30 squares, 20×20 mm): 3mm spherical indenter centrally loaded at 0.5 mm/min until rupture; measures biaxial tensile strength and 2D elastic modulus.
- **Adhesion test** (n=10 bone+membrane strips): piezosurgical isolation of 5mm bone segment; 2mm displacement applied; detachment force recorded.
- **FE model**: ANSYS 16.0; 3804 eight-node quadrilateral elements; nonlinear hyper-elastic vs linear comparison.
- **Statistics**: mixed-effects model; p<0.05.

## Results

| Parameter | Mode | Mean ± SD | Range |
|---|---|---|---|
| Membrane thickness | Both | **1.01 ± 0.44 mm** | 0.33–2.13 mm |
| Tensile strength | Elongation | **5.05 ± 0.97 N/mm** | 2.98–6.69 |
| Tensile strength | Perforation | **8.57 ± 3.75 N/mm** | 1.87–17.86 |
| Linear elastic modulus | Elongation | **27.1 ± 3.7 MPa** | — |
| Linear elastic modulus | Perforation | **53.6 ± 5.1 MPa** | — |
| Adhesion force | Detachment | **0.052 ± 0.021 N/mm** | 0.011–0.093 |

- Perforation test: tensile strength and elastic modulus both significantly higher than elongation (p<0.05).
- Nonlinear FE model: R²=0.99065; linear model: R²=0.94656.
- Hyper-elastic constants: **C10=0.253 MPa, C01=0.026 MPa** (Mooney-Rivlin).
- Stress maximum at membrane–bone detachment margin; maximum deformation at center of free membrane.

## Related Papers

- [[sinus-lift/transcrestal/lin-2025-schneiderian-membrane-biomechanical-transcrestal-fea]] — extends: uses Zhai's Mooney-Rivlin parameters for 3D FEA of hydraulic vs osteotome TSFE
- [[sinus-lift/lateral/alalshaikh-2024-membrane-perforation-risk-factors-lateral-sinus-sr-ma]] — reinforces: this paper provides the mechanical underpinning for clinical perforation risk factors
- [[sinus-lift/lateral/khiabani-2024-sinus-membrane-thickness-lsfe-mucosal]] — reinforces: membrane thickness is a confound in this study's results (wide range 0.33–2.13mm)
- [[sinus-lift/lateral/diaz-olivares-2021-schneiderian-membrane-perforation-sinus-lift]] — reinforces: clinical perforation incidence studies now have a biomechanical reference point
