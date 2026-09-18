---
title: "Comparison of biomechanical characteristics of the Schneiderian membrane with different transcrestal sinus floor elevation techniques using three-dimensional finite element analysis"
authors: "Lin X, Xu S, Chen L, Que G"
year: 2025
doi: "10.1186/s12903-025-05499-0"
category: [sinus-lift/transcrestal]
source_collection: pubmed-abstract
full_text: true
pmid: "39875935"
pmcid: "PMC11773847"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11773847/
---

## Why Ingested

경치조골 상악동거상 기법(수압법 vs 오스테오톰 Ø1.6mm / Ø3mm)의 슈나이데리안 막 응력 분포를 **3D FEA로 최초 비교**한 논문. 기존 위키([[sinus-lift/transcrestal/cobo-vazquez-2025-crestal-sinus-lift-osteotome-vs-osseodensification]])에서 임상결과 비교는 있으나, 왜 수압법이 천공률이 낮은지에 대한 **역학적 설명**이 없었다. 이 논문이 그 메커니즘을 수치로 제시한다.

## One-line Summary

3D FEA study (3 models: hydraulic pressure CAS-Kit vs osteotome Ø1.6mm vs Ø3mm): hydraulic technique requires least force (130 vs 200.8 vs 273.2 kPa at 5mm elevation) and generates lowest von Mises stress, supporting its lower clinical perforation rate.

## 한줄요약

3D FEA(3개 모델: 수압법 CAS-Kit vs 오스테오톰 Ø1.6/Ø3mm): 수압법이 5mm 거상 시 필요 압력 최소(130 kPa), von Mises 응력 최소, 수평 박리 면적 최대 — 낮은 임상 천공률의 역학적 근거.

## 1. Document Information

- **Journal**: BMC Oral Health, 2025;25(1):146
- **Published**: 2025-01-28
- **DOI**: 10.1186/s12903-025-05499-0 | **PMID**: 39875935 | **PMCID**: PMC11773847
- **Study type**: 3D finite element analysis (in silico)
- **Ethics**: Stomatological Hospital of Southern Medical University (approval [2022]08); informed consent from CBCT donor

## 2. Key Contributions

- **First 3D FEA model of hydraulic pressure TSFE** (CAS-Kit system) — prior FEA studies only modeled osteotome techniques.
- Hydraulic pressure technique: **30% lower von Mises stress** than large osteotome at 5mm elevation (M1 < M3, p<0.001).
- Hydraulic pressure: largest horizontal membrane displacement (2.35mm mesio-distal at 5mm) → more membrane detachment → more graft contact area with bone walls.
- **Mechanism clarified**: osteotome causes compressive stress + rapid rebound (super-elastic rebound); hydraulic pressure causes tensile stress + plastic deformation (minimal rebound) — explains less re-attachment during osteotome use.
- Small-diameter osteotome (Ø1.6mm) more efficient than large (Ø3mm) but more stress-concentrated — surgically implies initial small then progressive larger osteotome.

## 3. Methodology and Architecture

- **Model geometry**: CBCT from 26-year-old female patient (missing maxillary left first molar); concave mesio-distal, ovoid buccal-lingual sinus morphology.
- **Software stack**: Mimics 18.0 → Geomagic 12.0 → SolidWorks 2015 (instruments) → ANSYS 17.
- **Mesh**: 111,773–126,668 elements, 188,088–210,244 nodes (8-node tetrahedral).
- **Schneiderian membrane material**: hyper-elastic (Mooney-Rivlin; C10=0.253, C01=0.026 from Zhai 2018); thickness set at 1mm.
- **Bone material**: cortical 13,700 MPa (ν=0.3), cancellous 1,370 MPa (ν=0.3); isotropic linear elastic.
- **Three models**: M1=hydraulic (CAS-Kit, 4mm channel), M2=osteotome Ø1.6mm, M3=osteotome Ø3mm.
- **Loading**: quasi-static; membrane elevated to 1, 3, and 5mm; force at each height recorded.
- **Outcomes**: von Mises stress, tensile/compressive/shear stress, horizontal membrane displacement (Y=mesio-distal, Z=buccal-palatal).

## 4. Key Results and Benchmarks

### Required Loading Force (kPa)

| Elevation | M1 Hydraulic | M2 Osteotome Ø1.6mm | M3 Osteotome Ø3mm |
|---|---|---|---|
| 1 mm | 24.9 | 32.5 | 54.5 |
| 3 mm | 77.1 | 112.9 | 160.6 |
| 5 mm | **130** | **200.8** | **273.2** |

### Horizontal Membrane Displacement at 5mm Elevation (mesio-distal)

| M1 Hydraulic | M2 Ø1.6mm | M3 Ø3mm |
|---|---|---|
| **2.35 ± 0.10 mm** | 1.81 ± 0.68 mm | 1.68 ± 0.10 mm |

- von Mises stress: M1 < M2 < M3 (p<0.001); M3 at 5mm = 1.06 MPa, 30% > M1.
- Compressive stress: M2 highest; M1 ≈ half of M2 at 5mm.
- Tensile stress: M1 > M2 > M3 at ≥3mm (p<0.001).
- Shear stress: only mild difference at 5mm (p<0.05).

## 5. Limitations and Future Work

- **Single CBCT model**: one sinus morphology (26F, good bone quality) — does not capture low-density bone (Type III/IV) where undersized preparation changes stress patterns.
- **No adjacent structures**: root proximity, existing implants not modeled.
- **Simplified membrane**: uniform 1mm thickness; no viscoelastic time-dependence.
- **FEA absolute values**: may not match in vivo due to model simplifications; trends are valid, absolute numbers less so.
- Future: multiple sinus morphologies, varying membrane thickness, bone density IV models.

## 6. Related Work

- **Zhai 2018**: source of Mooney-Rivlin parameters used in this FEA.
- **Ro et al. 2021**: clinical average hydraulic pressure 25±13 kPa — aligns with this study's M1 predictions.
- **Tavelli et al.**: in vivo osteotome membrane detachment force mean 2.01±0.67 N — this study confirms hydraulic method requires less force.
- **CAS-Kit (OSSTEM)**: the hydraulic system modeled; one drill series specifically designed for TSFE.

## 7. Glossary

- **CAS-Kit**: Computer-Aided Sinus Kit (OSSTEM) — conical reamer drill + umbrella-shaped elevator + hydraulic pressure injector
- **von Mises stress**: scalar stress measure combining all stress components; threshold exceeded → material failure
- **Quasi-static loading**: slowly varying loads simulating equilibrium at each increment (vs dynamic/impact)
- **Mooney-Rivlin**: hyper-elastic constitutive model; C10=0.253, C01=0.026 MPa from Zhai 2018
- **Horizontal displacement (strain)**: buccal-palatal + mesio-distal movement of membrane during elevation — proxy for graft space created

## Three-line Summary

- 3D finite element analysis (in silico, one patient's CBCT) comparing three transcrestal sinus floor elevation techniques: hydraulic pressure (CAS-Kit), osteotome Ø1.6mm, and osteotome Ø3mm; Schneiderian membrane modeled with hyper-elastic Mooney-Rivlin constants from Zhai 2018.
- Hydraulic technique required the least loading force (130 vs 200.8 vs 273.2 kPa at 5mm), generated the lowest von Mises stress (30% below Ø3mm osteotome), and produced the largest horizontal membrane displacement (2.35mm mesio-distally); all differences statistically significant.
- Hydraulic pressure distributes force uniformly across the membrane surface causing progressive tensile deformation, whereas osteotomes generate focal compressive stress followed by elastic rebound; this mechanistically explains the lower clinical perforation rate of hydraulic techniques.

## 세줄요약

- 3D 유한요소 분석(Finite Element Analysis, FEA; 단일 환자 CBCT 기반): 수압법(CAS-Kit) vs 오스테오톰(Osteotome) Ø1.6mm vs Ø3mm 치조정접근 상악동거상술(Transcrestal Sinus Floor Elevation, TSFE) 비교; 슈나이데리안 막(Schneiderian Membrane)은 Zhai 2018의 Mooney-Rivlin 초탄성 상수로 모델링.
- 수압법이 5mm 거상 시 필요 하중 최소(130 vs 200.8 vs 273.2 kPa), von Mises 응력 최소(Ø3mm 오스테오톰 대비 30% 낮음), 수평 막 박리 면적 최대(2.35mm); 모든 차이 통계적 유의.
- 수압법은 막 전체에 하중 균일 분산(천공 위험 감소), 오스테오톰은 집중 압축 응력 후 탄성 반발(Elastic Rebound) 유발 — 수압법의 낮은 임상 천공률을 역학적으로 설명.
