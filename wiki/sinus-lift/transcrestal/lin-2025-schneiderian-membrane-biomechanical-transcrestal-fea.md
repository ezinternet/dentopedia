---
title: "Comparison of biomechanical characteristics of the Schneiderian membrane with different transcrestal sinus floor elevation techniques using three-dimensional finite element analysis"
authors: "Lin X et al."
year: 2025
date: 2025-01-28
doi: "10.1186/s12903-025-05499-0"
source: lin-2025-schneiderian-membrane-biomechanical-transcrestal-fea.md
category: [sinus-lift/transcrestal]
evidence_level: in-vitro
source_collection: pubmed-abstract
tags: [schneiderian-membrane, finite-element-analysis, hydraulic-pressure, osteotome, biomechanics, cas-kit, von-mises-stress]
relations:
  - type: extends
    target: zhai-2018-nonlinear-biomechanical-schneiderian-membrane
---

## One-line Summary

First 3D FEA comparing hydraulic pressure (CAS-Kit) vs osteotome (Ø1.6mm, Ø3mm) transcrestal sinus elevation: hydraulic technique required least loading force (130 vs 273.2 kPa at 5mm) and generated lowest von Mises stress, mechanistically explaining its lower clinical perforation rate.

## 한줄요약

3D FEA로 수압법(CAS-Kit) vs 오스테오톰(Ø1.6mm, Ø3mm) TSFE 최초 비교: 수압법이 5mm 거상 시 가장 낮은 부하(130 kPa)·최소 von Mises 응력·최대 수평 박리 면적 — 낮은 천공률의 역학적 설명.

## Summary

Lin et al. built three 3D finite element models of transcrestal sinus floor elevation from a patient's CBCT data: M1 (hydraulic pressure via CAS-Kit), M2 (Summers osteotome Ø1.6mm), and M3 (Ø3mm osteotome). The Schneiderian membrane was modeled as a hyper-elastic material using Mooney-Rivlin constants from Zhai 2018 (C10=0.253, C01=0.026 MPa). Across all three elevation heights (1, 3, 5mm), M1 consistently required the least loading force and produced the lowest von Mises stress. At 5mm elevation, M3 produced 30% higher von Mises stress than M1 (1.06 vs ~0.82 MPa). The hydraulic technique also produced greater horizontal membrane displacement (2.35mm vs 1.68mm mesio-distally at 5mm), indicating more membrane detachment area and thus more graft accommodation space. Mechanistically, the osteotome acts as a point source causing focal compressive stress followed by elastic rebound; the hydraulic pressure distributes force uniformly over the membrane area, causing progressive tensile (plastic) deformation with minimal rebound. This explains both the lower perforation risk and the higher effective elevation of hydraulic techniques seen in clinical studies.

## Key Contributions

- **First hydraulic pressure 3D FEA model** — establishes quasi-static force loading approach for fluid-membrane simulation (vs displacement loading used for osteotomes).
- Quantifies **force advantage of hydraulic over osteotome**: at 5mm, M1 requires 47% less force than M3.
- **Stress distribution topology differs by technique**: hydraulic stress is central/uniform early then radiates outward; osteotome stress is peripheral/concentrated early then converges centrally at height — the latter pattern predicts perforation at higher elevations.
- **Horizontal membrane displacement** as surrogate for graft space: M1 strips 40% more membrane mesio-distally than M3.
- **Osteotome size effect**: Ø1.6mm more force-efficient but more stress-concentrated — justifies clinical sequence of small→large diameter osteotomes.

## Methodology

- **Design**: In silico 3D FEA; no patients involved (CBCT geometry only from one consented patient).
- **Model geometry**: 26-year-old female CBCT; missing maxillary left first molar; concave mesio-distal sinus morphology.
- **Membrane model**: hyper-elastic (Mooney-Rivlin C10=0.253, C01=0.026), 1mm uniform thickness.
- **Bone model**: cortical 13,700 MPa, cancellous 1,370 MPa; isotropic linear elastic; membrane–bone contact frictionless (M1) or friction coefficient 0.2 (M2/M3).
- **Mesh**: 111,773–126,668 tetrahedral elements; 188,088–210,244 nodes.
- **Loading**: quasi-static; outcomes at elevation heights 1mm, 3mm, 5mm.
- **Software**: ANSYS 17; statistics SPSS 25 + GraphPad Prism 7; two-way ANOVA.

## Results

### Required Loading Force

| Elevation | Hydraulic (M1) | Osteotome Ø1.6mm (M2) | Osteotome Ø3mm (M3) |
|---|---|---|---|
| 1 mm | 24.9 kPa | 32.5 kPa | 54.5 kPa |
| 3 mm | 77.1 kPa | 112.9 kPa | 160.6 kPa |
| **5 mm** | **130 kPa** | **200.8 kPa** | **273.2 kPa** |

### Horizontal Membrane Displacement at 5mm (mesio-distal)

| M1 Hydraulic | M2 Ø1.6mm | M3 Ø3mm |
|---|---|---|
| **2.35 ± 0.10 mm** | 1.81 ± 0.68 mm | 1.68 ± 0.10 mm |

- All differences significant p<0.001 (stress) or p<0.05 (shear at 5mm).
- von Mises at 5mm: M3 ≈ 1.06 MPa (30% > M1).
- Compressive stress M1 ≈ half of M2 at 5mm elevation.
- Tensile stress M1 > M2 > M3 at ≥3mm.

## Related Papers

- [[sinus-lift/lateral/zhai-2018-nonlinear-biomechanical-schneiderian-membrane]] — extends: uses Zhai's Mooney-Rivlin parameters as material input for this FEA
- [[sinus-lift/transcrestal/cobo-vazquez-2025-crestal-sinus-lift-osteotome-vs-osseodensification]] — reinforces: clinical osteotome vs alternative data now has biomechanical backing
- [[sinus-lift/transcrestal/huang-2026-graftless-transcrestal-sinus-membrane-perforation-ma]] — reinforces: pooled 1% perforation rate with graftless TSFE is consistent with this study's lower hydraulic stress profile
- [[sinus-lift/transcrestal/gaspar-2025-osseodensification-crestal-maxillary-sinus-elevation-narrative-review]] — reinforces: OD technique force discussion complemented by FEA comparison

## Three-line Summary

- 3D finite element analysis (in silico, one patient's CBCT) comparing three transcrestal sinus floor elevation techniques: hydraulic pressure (CAS-Kit), osteotome Ø1.6mm, and osteotome Ø3mm; Schneiderian membrane modeled with hyper-elastic Mooney-Rivlin constants from Zhai 2018.
- Hydraulic technique required the least loading force (130 vs 200.8 vs 273.2 kPa at 5mm), generated the lowest von Mises stress (30% below Ø3mm osteotome), and produced the largest horizontal membrane displacement (2.35mm mesio-distally); all differences statistically significant.
- Hydraulic pressure distributes force uniformly across the membrane surface causing progressive tensile deformation, whereas osteotomes generate focal compressive stress followed by elastic rebound; this mechanistically explains the lower clinical perforation rate of hydraulic techniques.

## 세줄요약

- 3D 유한요소 분석(Finite Element Analysis, FEA; 단일 환자 CBCT 기반): 수압법(CAS-Kit) vs 오스테오톰(Osteotome) Ø1.6mm vs Ø3mm 치조정접근 상악동거상술(Transcrestal Sinus Floor Elevation, TSFE) 비교; 슈나이데리안 막(Schneiderian Membrane)은 Zhai 2018의 Mooney-Rivlin 초탄성 상수로 모델링.
- 수압법이 5mm 거상 시 필요 하중 최소(130 vs 200.8 vs 273.2 kPa), von Mises 응력 최소(Ø3mm 오스테오톰 대비 30% 낮음), 수평 막 박리 면적 최대(2.35mm); 모든 차이 통계적 유의.
- 수압법은 막 전체에 하중 균일 분산(천공 위험 감소), 오스테오톰은 집중 압축 응력 후 탄성 반발(Elastic Rebound) 유발 — 수압법의 낮은 임상 천공률을 역학적으로 설명.
