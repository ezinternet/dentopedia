---
title: "In vivo measurements and numerical analysis of the biomechanical characteristics of the human periodontal ligament"
authors: "Keilig L et al."
year: 2016
date: 2016-07-01
doi: "10.1016/j.aanat.2015.08.004"
source: keilig-2016-in-vivo-measurements-pdl.md
category: orthodontics
confidence: in-vivo
pdf_path: /Users/oracleneo/llm-wiki/papers/keilig-2016-in-vivo-measurements-pdl.pdf
pdf_filename: keilig-2016-in-vivo-measurements-pdl.pdf
source_collection: external
tags: [pdl, biomechanics, young-modulus, fem, tooth-mobility, viscoelastic]
relations:
  - type: extends
    target: li-2021-periodontium-orthodontic-tooth-movement-biomechanics
  - type: reinforces
    target: feller-2015-periodontal-ligament-bone-orthodontic-forces
---

## One-line Summary
In vivo study (n=5) using a novel intraoral loading device to measure time-dependent PDL force/deflection characteristics, yielding a Young's modulus of 0.9–1.2 MPa that decreases with slower loading rates.

## 한줄요약
구강 내 측정장치로 건강한 지원자 5명의 치주인대 (Periodontal Ligament, PDL) 시간의존적 특성 in vivo 측정; 탄성계수 0.9–1.2 MPa, 하중 속도가 느릴수록 감소.

## Summary
Keilig et al. (2016) used a custom intraoral loading device to apply controlled horizontal deflections (0–0.15 mm) to the upper central incisor of 5 healthy volunteers at six loading rates (0.1–5.0 s). Experimental force/displacement curves demonstrated clear time-dependence: forces decreased monotonically with longer loading periods, consistent with the viscoelastic/poroelastic nature of the PDL. Individual finite element models were developed per subject and material parameters were fitted to the experimental data, yielding a Young's modulus of 1.2 MPa at fast loading (0.1 s) and 0.9 MPa at slow loading (5.0 s). The authors conclude the data provide empirical in vivo benchmarks for developing and validating multiphasic constitutive laws of the PDL.

## Key Contributions
- Rare in vivo quantification of PDL viscoelastic properties across clinically relevant loading rates
- Established that PDL effective Young's modulus ranges 0.9–1.2 MPa (rate-dependent) in healthy adults
- At 0.1 s loading, incisor forces ranged 7.0–16.2 N — relevant to parafunctional/orthodontic contexts
- Individual FEM models validated against experimental curves; <5% measurement repeatability
- Provided input parameters for multiphasic PDL constitutive law development

## Methodology
- **Design**: Experimental in vivo study
- **n**: 5 healthy volunteers, aged 21–33, healthy periodontium
- **Tooth**: Upper left central incisor (#21)
- **Device**: Novel intraoral loading device (Drolshagen et al. 2011) — applies labial crown deflection
- **Deflection range**: 0 to 0.15 mm (linear ramp)
- **Loading times**: 0.1 / 0.2 / 0.5 / 1.0 / 2.0 / 5.0 seconds
- **FEM**: Individual 3D models; Young's modulus derived by fitting numerical to experimental curves
- **Repeatability validation**: Frasaco ANA-4 model with silicone PDL analog (<5% variation)

## Results
| Loading time | Young's modulus (E) |
|---|---|
| 0.1 s | 1.2 MPa |
| 5.0 s | 0.9 MPa |

- Incisor force at 0.1 s: **7.0–16.2 N** (range across subjects)
- Force decreased monotonically with increasing loading time in all subjects
- FEM curves fitted well to experimental data in all 5 subjects
- Repeatability: <5% variation on phantom model

## Related Papers
- [[orthodontics/li-2021-periodontium-orthodontic-tooth-movement-biomechanics]] — extends: numerical model of PDL biomechanics in orthodontic tooth movement
- [[orthodontics/feller-2015-periodontal-ligament-bone-orthodontic-forces]] — reinforces: PDL force transmission mechanisms to alveolar bone
- [[orthodontics/feller-2015-periodontal-cytoskeleton-ecm-orthodontic]] — related: PDL cellular response to mechanical loading
