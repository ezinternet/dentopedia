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

## Three-line Summary

- In vivo clinical study (n=5 healthy volunteers, ages 21–33) using a novel intraoral loading device to apply controlled horizontal deflections (0–0.15 mm) to upper central incisors at six loading rates (0.1–5.0 s), with individual 3D finite element models (FEM) fitted to experimental force/displacement curves.
- Young's modulus was 1.2 MPa at fast loading (0.1 s) and 0.9 MPa at slow loading (5.0 s); force at 0.1 s ranged 7.0–16.2 N across subjects; monotonic force decrease with longer loading time confirmed viscoelastic/poroelastic periodontal ligament (PDL) behavior in all subjects.
- These in vivo benchmarks provide the only empirically validated rate-dependent Young's modulus values for the human PDL, serving as critical input parameters for multiphasic constitutive laws in orthodontic tooth movement and implant biomechanics simulations.

## 세줄요약

- In vivo 임상 연구 (건강한 지원자 5명, 21–33세): 구강 내 측정장치로 상악 중절치에 6가지 하중 속도 (0.1–5.0 s)로 제어된 수평 변위 (0–0.15 mm)를 가하고 개인별 3D 유한요소모델 (Finite Element Model, FEM)로 실험 곡선에 피팅.
- 탄성계수 (Young's Modulus) 빠른 하중 (0.1 s) 1.2 MPa → 느린 하중 (5.0 s) 0.9 MPa; 0.1 s 기준 전치 하중 7.0–16.2 N; 하중 시간 증가에 따른 힘 단조 감소 — 치주인대 (Periodontal Ligament, PDL) 점탄성 (Viscoelastic)/공극탄성 (Poroelastic) 거동 확인.
- 이 in vivo 기준값은 교정 치아이동 (Orthodontic Tooth Movement, OTM) 및 임플란트 생체역학 시뮬레이션에 쓰이는 다상 구성방정식 (Multiphasic Constitutive Law)의 검증된 속도의존성 탄성계수 입력 파라미터를 제공하는 희귀 데이터.
