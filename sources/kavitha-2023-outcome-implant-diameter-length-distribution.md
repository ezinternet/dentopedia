---
title: "Outcome of Implant Diameter and Length on the Distribution of Stress with Immediate Loaded Implants: A 3D Finite Element Analysis"
authors: Kavitha G, Subhash Sonkesriya, Anil Kumar K, Faris Jaser Almutairi, Pravin M Parmar, Anuj Singh Parihar, Tanu Priya Sonkar
year: 2023
doi: 10.4103/jpbs.jpbs_100_23
category: [implants]
pdf_path: /Users/oracleneo/llm-wiki/papers/kavitha-2023-outcome-implant-diameter-length-distribution.pdf
pdf_filename: kavitha-2023-outcome-implant-diameter-length-distribution.pdf
source_collection: external
---

## Why Ingested

[[implants/singh-2024-influence-implant-design-length-stress]]는 6 mm→10 mm 픽스쳐 길이 증가가 D4 골에서 계면 응력을 일관되게 낮춘다고 보고했다 (수직 188→35.44 MPa). 본 논문(Kavitha 2023)은 다른 임플란트 형태(LEADER/ITALIA-Fix 일체형, 즉시하중)에서 10 mm→12 mm 길이 증가가 오히려 응력을 소폭 증가(1.32→1.76 MPa)시킨다고 보고해, "길이가 길수록 응력 감소"라는 단순 도식에 반례를 제공한다. 직경 증가(3.75→4.25 mm)는 응력에 유의한 영향이 없다는 결과도 함께 기록해, 임플란트 디자인/골질/길이 구간에 따라 길이-응력 관계가 뒤집힐 수 있음을 보여주는 대비 사례로 인제스트.

## Three-line Summary

3D finite element analysis (ANSYS v12) of a one-piece LEADER/ITALIA-Fix immediate-loading implant embedded in a 25×15×15 mm bone block, comparing two lengths (10 mm, 12 mm) and two diameters (3.75 mm, 4.25 mm) under a 2.0 MPa axial occlusal load.

Implant neck was the highest-stress zone in all configurations; increasing length from 10 mm to 12 mm slightly raised interface von Mises stress (1.32→1.76 MPa max), while increasing diameter from 3.75 mm to 4.25 mm had no appreciable effect on stress (1.77→1.79 MPa max).

Single in-silico model with idealized homogeneous/isotropic materials and one implant system — the length-increases-stress direction is opposite to some other FEA studies and should not be generalized without design/bone-density context.

## 세줄요약

일체형(one-piece) LEADER/ITALIA-Fix 즉시하중 임플란트를 25×15×15 mm 골블록에 매립한 3D 유한요소해석(ANSYS v12)으로, 길이 2종(10, 12 mm)·직경 2종(3.75, 4.25 mm)을 2.0 MPa 축방향 교합하중 하에서 비교.

전 조건에서 임플란트 넥(neck)이 최고 응력 부위였고, 길이를 10→12 mm로 늘리면 계면 von Mises 응력이 소폭 증가(최대 1.32→1.76 MPa)했으며, 직경을 3.75→4.25 mm로 늘려도 응력에 뚜렷한 영향은 없었다(최대 1.77→1.79 MPa).

단일 임플란트 시스템의 in-silico 모델(균질·등방성 재료 가정)이며, 길이 증가가 응력을 높이는 방향은 일부 다른 FEA 연구와 반대이므로 디자인·골밀도 맥락 없이 일반화하면 안 된다.

## 1. Document Information
- **Journal**: Journal of Pharmacy and Bioallied Sciences 2023;15(Suppl 2):S1329-S1331
- **DOI**: 10.4103/jpbs.jpbs_100_23
- **Institution**: Department of Periodontology, People's Dental Academy, Bhopal, Madhya Pradesh, India (corresponding author); multi-institutional India + Qassim University, Saudi Arabia

## 2. Key Contributions
- Isolates both length (10 vs 12 mm) and diameter (3.75 vs 4.25 mm) in a single one-piece immediate-loading implant system, holding the other variable fixed.
- Reports the implant neck/cervical region as the consistent maximum-stress location across all four configurations.
- Finds a small but directionally negative effect of increasing length on stress (opposite of the common "longer = less stress" assumption), while diameter increase shows negligible effect.

## 3. Methodology and Architecture
- **Design**: In-vitro/in-silico 3D finite element analysis (FEA)
- **Software**: ANSYS V.12
- **Model**: LEADER/ITALIA-Fix one-piece (fixture + abutment) implant for immediate loading, embedded in a 25 mm tall × 15 mm wide × 15 mm long bone block
- **Elements**: SOLID95 (3D 20-node tetrahedral structural solid, titanium implant); SOLID191 (3D 20-node layered structural solid, up to 100 material layers, for bone)
- **Variables**: implant length 10 mm vs 12 mm (diameter fixed); implant diameter 3.75 mm vs 4.25 mm (length fixed at 12 mm)
- **Load**: 2.0 MPa axial force applied to the top of the abutment (simulating axial occlusal loading)
- **Outcome**: von Mises stress distribution and magnitude at the implant-bone interface

## 4. Key Results and Benchmarks

**Table 1 — Length effect (diameter fixed):**

| Length (mm) | Max stress (MPa) | Min stress (MPa) |
|---|---|---|
| 10 | 1.32 (cervical/neck) | 0.145 (apex) |
| 12 | 1.76 (neck) | 0.373 (apical interface) |

**Table 2 — Diameter effect (length fixed at 12 mm):**

| Diameter (mm) | Max stress (MPa) | Min stress (MPa) |
|---|---|---|
| 3.75 | 1.77 (neck) | 0.345 |
| 4.25 | 1.79 (cervical) | 0.367 |

Conclusion: length increase (10→12 mm) has a small negative effect on stress (raises it), while diameter increase (3.75→4.25 mm) has no discernible impact on stress values; the implant neck remains the highest-stress region regardless of dimension.

## 5. Limitations and Future Work
- Single implant system (LEADER/ITALIA-Fix one-piece); results may not generalize to other macrogeometries (tapered/step/two-piece designs).
- Idealized homogeneous, isotropic bone-block model rather than patient-derived anatomy or graded bone density (D1-D4).
- Only two length values (10/12 mm) and two diameters (3.75/4.25 mm) tested — narrow parameter range near the upper end of common implant lengths.
- Static axial load only (2.0 MPa); no oblique/lateral loading scenario tested (contrast with Singh 2024, which found oblique loads produced the highest stresses).
- Authors state "future research should be directed to evaluate the efficacy" — no explicit expansion plan given.

## 6. Related Work
- Mohamad et al. 2013 (Al-Rafidain Dent J): 3D FEA of implant length/diameter effect on stress distribution at the bone-implant interface for immediate loading implants — closest methodological precedent.
- Eazhil et al. 2016 (J Int Soc Prevent Community Dent): 3D FEA study concluding that von Mises stress decreased significantly as implant diameter increased — cited by this paper but contrasts with its own diameter-null finding.
- Abraham et al. 2016 (J Oral Res Rev): regular-platform implants showed lower peri-implant bone stress than narrow-platform implants.
- de Moraes et al. 2018 (Braz Dent J): wide-diameter implants favorable for stress distribution in cortical bone, varying connection type and crown-implant ratio.
- Geng et al. 2004 (J Oral Implantol): stepped screw implant suitable for cortical bone; maximum tension at implant neck region.
- Dundar et al. 2016 (Biotechnol Biotechnol Equip): FEA of stress distributions in peri-implant bone comparing modified vs standard-threaded implants.

## 7. Glossary
- **von Mises stress**: A scalar stress measure combining all stress-tensor components, commonly used in FEA to predict yielding/failure risk under complex loading.
- **FEA (Finite Element Analysis)**: Numerical method dividing a structure into small elements to simulate stress/strain distribution under load.
- **Immediate loading**: Placing a functional or provisional restoration on an implant at the time of surgery (or shortly after), rather than after a healing/osseointegration period.
- **One-piece implant**: Implant design where the fixture and abutment are manufactured as a single unit (no internal connection interface).
- **SOLID95 / SOLID191**: ANSYS finite-element types — SOLID95 is a 3D 20-node tetrahedral structural solid; SOLID191 is a 3D 20-node layered structural solid supporting multiple material layers.
