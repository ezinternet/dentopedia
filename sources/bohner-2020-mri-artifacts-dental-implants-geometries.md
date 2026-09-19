---
title: "Magnetic resonance imaging artifacts produced by dental implants with different geometries"
authors: Lauren Bohner, Norbert Meier, Felix Gremse, Pedro Tortamano, Johannes Kleinheinz, Marcel Hanisch
year: 2020
doi: 10.1259/dmfr.20200121
category: radiology/mri
pdf_path: /Users/oracleneo/llm-wiki/papers/bohner-2020-mri-artifacts-dental-implants-geometries.pdf
pdf_filename: bohner-2020-mri-artifacts-dental-implants-geometries.pdf
source_collection: external
---

## Why Ingested
First paper in the new `radiology/mri` category together with its sibling on ceramic vs titanium artifact properties — MRI artifacts from implant materials are the clinical bridge between implantology and head-and-neck MRI diagnostics. Extends the zirconia-vs-titanium implant comparison already held in [[implants/surface/kniha-2026-zirconia-titanium-microbial-anterior-rct]] from the clinical/microbial domain to the imaging/diagnostic domain.

## Three-line Summary
- Ex vivo bench study (n = 9 porcine rib bone samples, G*Power-calculated): three titanium (Titan SLA, Straumann) and three zirconia (Pure Ceramic Implant, Straumann) dental implants in three geometries (3.3x8 / 4.1x8 / 4.1x14 mm) scanned at 3T T1W turbo spin echo; micro-CT (16 um voxel) as reference.
- Artifacts measured 2.57 ± 1.09 mm for titanium vs 0.37 ± 0.20 mm for zirconia (p<0.05); neither measurement site (p=0.73) nor implant geometry (p=0.43) influenced artifact extent.
- Clinical implication: implant geometry is not a controllable variable for MRI artifact reduction, but material choice is — the ceramic option reduces artifact burden ~7-fold; the clover-like artifact pattern depends on scanning/phase-encoding direction.

## 세줄요약
- 체외(돼지 갈비뼈 9개 표본, G*Power 산정) 벤치 연구 — 티타늄(Titan SLA) 3개와 지르코니아(Pure Ceramic Implant) 3개 임플란트를 3가지 크기(3.3x8 / 4.1x8 / 4.1x14 mm)로 3T T1W TSE 스캔, 미세CT(마이크로CT, 16 µm)를 대조로 함.
- 인공음영(artifact) 범위 티타늄 2.57±1.09 mm vs 지르코니아 0.37±0.20 mm (p<0.05); 측정 위치(p=0.73)나 임플란트 형상(p=0.43)은 영향 없음.
- 임상적 의미: 형상은 인공음영 조절 변수가 아니지만 재료 선택은 가능 — 지르코니아가 약 7배 적은 인공음영, 클로버형 패턴은 스캔/위상부호화 방향 의존.

## 1. Document Information
- **Journal**: Dentomaxillofacial Radiology 2020;49:20200121
- **DOI**: 10.1259/dmfr.20200121
- **Institution**: Department of Cranio-Maxillofacial Surgery, Muenster University Hospital, Germany; University of São Paulo, Brazil; RWTH Aachen University, Germany

## 2. Key Contributions
- First controlled ex vivo comparison isolating implant GEOMETRY (diameter x height: 3.3x8, 4.1x8, 4.1x14 mm) as an independent factor in MRI artifact magnitude, alongside material.
- Quantified titanium vs zirconia artifact extent at 3T T1W — titanium ~7x larger artifact zone (2.57 vs 0.37 mm) with high intrarater reliability (Cronbach's alpha 0.92).
- Demonstrated geometry does NOT affect artifact extent (p=0.43), contradicting the extrapolation from larger fixation-screw data (Ganapathi 2002) that longer implants would produce longer artifacts.

## 3. Methodology and Architecture
- **Design**: Ex vivo bench/experimental study (porcine rib bone specimens)
- **n**: 9 bone samples; 6 implants (3 titanium + 3 zirconia), 3 geometries each
- **Sample size**: G*Power, 80% power, alpha 0.05
- **Imaging**: MRI 3T (Philips, 8-channel SENSE foot/ankle coil), T1W turbo spin echo, TR/TE 25/3.5 ms, FOV 100x100x90 mm, voxel 0.22x0.22x0.50 mm, scan time 11:18, phase-encoding RL; micro-CT (SkyScan 1272, Bruker) 80 kV, 125 mA, voxel 16 um as control
- **Measurement**: Linear distance (mm) between implant bed preparation surface (micro-CT) and artifact border (MRI), at vestibular-lingual, mesio-distal, and apex sites; measured three times per site by one examiner
- **Statistics**: Within-subjects ANOVA; Shapiro-Wilk, Levene, Mauchly (Greenhouse-Geisser correction); Cronbach's alpha; implant design as covariate (p <= 0.05)

## 4. Key Results and Benchmarks
- Overall artifact extent: titanium 2.57 ± 1.09 mm vs zirconia 0.37 ± 0.20 mm (p<0.05 / p<0.01); mean difference 2.32 mm (95% CI 1.88–2.76)
- Material: significant (F=127.023, p<0.01); measurement site: p=0.73; implant geometry: p=0.43
- Site-specific data (mm), design A/B/C = 3.3x8 / 4.1x8 / 4.1x14 mm:

| Implant | Design | Vestibulo-lingual | Apex | Mesio-distal |
|---|---|---|---|---|
| Titanium | A | 3.00 ± 1.31 | 2.33 ± 0.76 | 2.95 ± 0.86 |
| Titanium | B | 2.67 ± 0.80 | 2.79 ± 0.51 | 1.60 ± 1.40 |
| Titanium | C | 3.47 ± 0.68 | 1.02 ± 1.35 | 3.31 ± 0.55 |
| Zirconia | A | 0.38 ± 0.27 | 0.58 ± 0.09 | 0.29 ± 0.19 |
| Zirconia | B | 0.62 ± 0.14 | 0.17 ± 0.13 | 0.48 ± 0.14 |
| Zirconia | C | 0.35 ± 0.10 | 0.35 ± 0.04 | 0.30 ± 0.16 |

- Intra-rater reliability: Cronbach's alpha 0.92

## 5. Limitations and Future Work
- Ex vivo porcine bone, no living tissue/flow — real clinical artifact severity with patient-specific factors (blood flow, coil loading, head motion) not captured.
- Single 3T T1W TSE protocol — artifact pattern has been shown to depend on sequence, phase-encoding direction, and scan plane; results may not generalize to other sequences/field strengths.
- Small sample (n=9) with per-material cell sizes; the A/B/C geometry labels follow the paper's reported listing order (3.3x8, 4.1x8, 4.1x14 mm) rather than an explicit diagrammatic key.

## 6. Related Work
- Duttenhoefer et al. 2015: titanium implant MRI size overestimation 36.9% (transversal) and 29.7% (longitudinal) — consistent directional finding.
- Ganapathi et al. 2002: longer titanium screws (16–22 mm) produced longer artifacts — opposite trend to this study, attributed by authors to the much larger screw sizes; not applicable to dental-implant ranges.
- Demirturk Kocasarac et al. 2019: titanium, zirconium, and titanium-zirconia implants produce greater signal voids in MRI/CBCT — agrees with material-rank ordering here.
- geibel (sibling, in parallel ingest): ceramic vs titanium artifact properties — direct sibling page in radiology/mri.

## 7. Glossary
- **Susceptibility artifact**: signal loss from the magnetic-susceptibility mismatch between neighboring structures (metal vs tissue).
- **Non-susceptibility artifact**: artifact from eddy currents induced by alternation of gradients and radiofrequency fields.
- **T1W TSE**: T1-weighted turbo spin echo sequence — standard clinical MRI sequence used here (TR/TE 25/3.5 ms).
- **Micro-CT (uCT)**: high-resolution X-ray microtomography (16 um voxel) used as the artifact-free geometric reference for measuring implant bed preparation.
- **Clover-like pattern**: characteristic clover/flower-shaped metal-artifact distribution in MRI, related to phase-encoding/scanning direction.