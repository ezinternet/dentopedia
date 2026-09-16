---
title: "In vivo measurements and numerical analysis of the biomechanical characteristics of the human periodontal ligament"
authors: "L. Keilig, M. Drolshagen, K.L. Tran, I. Hasan, S. Reimann, J. Deschner, K.T. Brinkmann, R. Krause, M. Favino, C. Bourauel"
year: 2016
doi: "10.1016/j.aanat.2015.08.004"
category: orthodontics
pdf_path: /Users/oracleneo/llm-wiki/papers/keilig-2016-in-vivo-measurements-pdl.pdf
pdf_filename: keilig-2016-in-vivo-measurements-pdl.pdf
source_collection: external
---

## Why Ingested
PDL의 시간 의존적(점탄성) 생체역학 특성을 구강 내 실측한 희귀한 in vivo 데이터. 기존 [[orthodontics/li-2021-periodontium-orthodontic-tooth-movement-biomechanics]] 의 수치 모델링 근거를 실측값으로 보강하고, [[orthodontics/feller-2015-periodontal-ligament-bone-orthodontic-forces]]에서 설명한 PDL의 힘 전달 메커니즘에 수치를 제공한다.

## One-line Summary
In vivo clinical study (n=5 healthy volunteers) measuring time-dependent force/deflection characteristics of the human PDL using a novel intraoral device, yielding Young's modulus values of 0.9–1.2 MPa across loading times of 5.0–0.1 s.

## 한줄요약
구강 내 측정장치를 이용해 건강한 지원자 5명의 PDL 시간의존성 힘-변위 특성을 in vivo로 측정; 탄성계수(Young's modulus) 0.9–1.2 MPa 도출 (하중 시간 5.0→0.1 s).

## 1. Document Information
- **Journal**: Annals of Anatomy – Anatomischer Anzeiger, Vol. 207, July 2016
- **DOI**: 10.1016/j.aanat.2015.08.004
- **Published online**: August 2015 (Epub ahead of print)
- **Funding**: German Research Foundation Clinical Research Unit 208 (DFG KFO 208, TP5); Medical Faculty, University of Bonn
- **Conflicts of interest**: None declared

## 2. Key Contributions
- First in vivo characterization of PDL mechanical properties across a wide range of loading velocities (0.1–5.0 s) using a novel intraoral measurement device
- Demonstrated clear time-dependence: maximum force decreases with increasing loading time (viscoelastic/poroelastic behavior)
- Quantified Young's modulus: 1.2 MPa (fast loading, 0.1 s) → 0.9 MPa (slow loading, 5.0 s)
- Developed individual FEM models per subject, fitted to experimental force/displacement curves
- Provided material parameters usable for multiphasic/viscoelastic constitutive law development

## 3. Methodology and Architecture
- **Study design**: Experimental in vivo study
- **Population**: n=5 healthy volunteers, aged 21–33 years, healthy periodontal tissue
- **Tooth**: Upper left central incisors (tooth 21)
- **Device**: Novel intraoral loading device (Drolshagen et al. 2011) — applies controlled labial deflection at the crown center
- **Deflection**: Linear increase from 0 to 0.15 mm
- **Loading periods**: 0.1, 0.2, 0.5, 1.0, 2.0, 5.0 seconds
- **Repeatability**: Validated on idealised Frasaco ANA-4 model with silicone PDL analog (<5% variation)
- **Numerical**: Individual finite element models per subject; material parameters fitted by minimizing deviation between numerical and experimental force/displacement curves

## 4. Key Results and Benchmarks
- **Force at 0.1 s loading**: 7.0–16.2 N (range across n=5 subjects)
- **Young's modulus**:
  - 0.1 s loading: 1.2 MPa
  - 5.0 s loading: 0.9 MPa
- Force decreased monotonically with increasing loading time (consistent across all subjects)
- Measurement repeatability: <5% variation
- FEM curves fitted well to experimental data, confirming validity of the numerical approach

## 5. Limitations and Future Work
- Very small sample (n=5), all young adults — no age-related or disease-related variation captured
- Only one tooth type (upper central incisor) — generalizability to posterior teeth unclear
- PDF accessed as web-page abstract; full Methods and Results text (Section snippets only) available
- Authors note data can be used for further development and verification of a **multiphasic constitutive law** — poroelastic or biphasic models not yet validated
- No subjects with periodontal disease included; disease-altered PDL properties remain unmeasured in vivo

## 6. Related Work
- Drolshagen et al. 2011 (J Biomech): Development of the intraoral measurement device used in this study
- Bergomi et al. 2011 (J Biomech): Porohyperelastic FEM model of PDL
- Natali et al. 2004 (Dent Mater): Non-linear constitutive law for PDL
- Lin et al. 2013 (J Biomech): Biomechanics of bone–PDL–tooth fibrous joint
- Qian et al. 2009: Viscoelastic approach to PDL material behavior

## 7. Glossary
- **PDL**: Periodontal Ligament — fibrous connective tissue anchoring tooth root to alveolar bone
- **Young's modulus (E)**: Linear elastic stiffness parameter; here used as an effective modulus from FEM fitting
- **Force/deflection curve**: Relationship between applied load and resulting tooth displacement
- **Intraoral loading device**: Custom device applying controlled horizontal forces to crown at specified velocities
- **Multiphasic constitutive law**: Material model accounting for solid (collagen fibres) and fluid phases of PDL
- **FEM**: Finite element method — computational structural analysis
- **KFO 208**: German Research Foundation Clinical Research Unit on dental biomechanics, University of Bonn
