---
title: "Thermal evaluation of pilot- and partially guided implant surgery - an in vitro study using automated robotic drilling"
authors: Tur D, Tian Z, Giannis K, Unger E, Mittlboeck M, Rausch-Fan X, Strbac GD
year: 2026
date: 2026-07-10
doi: 10.1186/s12903-026-09215-4
pmid: "42432641"
pmcid: "PMC13640361"
category: implants/osteotomy-thermal
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13640361/
source_collection: pubmed-text
full_text: true
text_path: /Users/oracleneo/llm-wiki/papers/tur-2026-guided-conventional-pilot-drill-thermal-evaluation.txt
text_filename: tur-2026-guided-conventional-pilot-drill-thermal-evaluation.txt
---

## Why Ingested

This paper directly extends [[implants/osteotomy-thermal/tur-2025-scais-cip-guided-conventional-drill-diameter-heat]] from the same Vienna/Strbac research group, which studied sequential drill diameters 2.2–3.5 mm; the present work zooms in specifically on the pilot drill phase (2.0 mm sleeve-guided and 2.8 mm partially guided), a drilling stage previously identified as generating the highest thermal peaks within guided surgery.

## Three-line Summary

In a standardized bovine in vitro model with automated robotic drilling (160 preparations), 2.0-mm sleeve-guided surgery produced significantly lower bone temperatures than conventional drilling under external irrigation, while 2.8-mm partially guided surgery produced significantly higher temperatures than conventional drilling with the same cooling. External irrigation kept all irrigated preparations below the 44–47 °C thermal osteonecrosis threshold. The divergent thermal behavior between the two pilot drill diameters implicates guide configuration and irrigation access — not drill diameter alone — as key determinants of osteotomy heat during guided surgery.

## 세줄요약

소 뼈 표준화 모델에서 로봇 자동 드릴링 160회 시험: 2.0 mm 슬리브 유도 수술(GS)은 외부 냉각 시 일반 드릴링(CD)보다 유의미하게 낮은 온도를 보였으나, 2.8 mm 부분 유도 수술은 외부 냉각 시 오히려 CD보다 유의미하게 높은 온도를 나타냈다. 외부 냉각을 적용한 모든 그룹은 골괴사 임계온도(44–47 °C)를 초과하지 않았다. 이 상반된 결과는 임플란트 유도 수술에서 냉각 효율이 드릴 직경만이 아니라 가이드 설계(슬리브 유형)와 관개 접근성의 상호작용에 의해 결정됨을 시사한다.

## 1. Document Information

- **Journal**: BMC Oral Health 2026;26(1)
- **DOI**: [10.1186/s12903-026-09215-4](https://doi.org/10.1186/s12903-026-09215-4)
- **PMID**: 42432641 | **PMCID**: PMC13640361
- **Institution**: Medical University of Vienna, Austria (Center for Medical Physics and Biomedical Engineering; University Clinic of Dentistry)
- **Study type**: In vitro, factorial experimental design, automated robotic drilling
- **Ethics**: Not required (commercially available bovine testing samples)
- **Experiments conducted**: 2023–2024

## 2. Key Contributions

1. **Diameter-dependent thermal reversal**: 2.0-mm sleeve-guided preparations showed LOWER temperatures than conventional drilling under external irrigation; 2.8-mm partially guided preparations showed HIGHER temperatures — opposite patterns within the same pilot drill range.
2. **Guide configuration matters**: The divergence is attributed to different guiding mechanisms — metallic guiding sleeve (2.0 mm) vs. sleeveless drill handle cylinder (2.8 mm) — and their respective effects on irrigation access at the drill–bone interface.
3. **Irrigation is universally effective**: External irrigation kept all preparations below the 44–47 °C thermal osteonecrosis threshold regardless of diameter or technique.
4. **Complement to Tur 2025**: Prior study addressed 2.2–3.5 mm sequential drills; present study closes the gap by isolating the pilot drill phase, yielding a full thermal picture of the guided osteotomy sequence.
5. **Robotic standardization**: Automated drilling (800 rpm, intermittent withdrawal, 50 mL/min irrigation) reduced variability from manual operator technique.

## 3. Methodology and Architecture

### Study Model
- **Bone substitute**: BoneSim™ (Newaygo, MI, USA) — bovine-derived artificial samples with 3 mm cortical + 15 mm cancellous layers, thermal conductivity 0.3–0.4 W/mK (human cortical equivalent), bone type 2 density
- **Sample dimensions**: 56 × 18 × 10 mm rectangular blocks (n=32 bone disks)
- **Surgical guides**: 32 individually 3D-printed photopolymer resin guides (one per block)

### Experimental Groups — Factorial Design
- **Techniques**: Guided implant surgery (GS) vs. Conventional drilling (CD)
- **Drill diameters**: 2.0 mm and 2.8 mm stainless steel pilot drills (Komet, Gebr. Brasseler)
- **Preparation depths**: 10 mm and 12 mm
- **Irrigation modes**: No irrigation vs. external irrigation (room-temperature saline, 50 mL/min)
- **Total preparations**: 160 (10 repetitions × 16 groups)

### Guiding Concepts
- **2.0 mm**: Metallic guiding sleeve (titanium inner sleeve, D3.5/d2.0/L5.0; steco-system-technik)
- **2.8 mm**: Sleeveless guide site with drill handle cylinder (Straumann Guided Implant Surgery Bone Level protocol)

### Drilling Protocol
- **Robotic system**: Material testing machine + Nexygen™ Plus software
- **Speed**: 800 rpm
- **Feed rate**: 2 mm/s cortical, 1 mm/s cancellous, 1 mm/s intermittent withdrawal
- **Timing**: 10-mm preparation = 32 s total; 12-mm preparation = 39 s total
- **Drill wear control**: New instruments for each preparation

### Temperature Measurement
- **Sensors**: Fine-wire Type K thermocouples, ± 1.5 °C accuracy
- **Positions**: 5 sensors at 3 mm intervals (depths 3, 6, 9, 12, 15 mm)
- **Distances**: 1 mm and 2 mm radial from osteotomy
- **Planning**: CT (MSCT, voxel 0.2×0.2×0.5 mm) + coDiagnostiX 10.8 for guide design

### Statistical Analysis
- Linear mixed model (four-way interactions: technique × diameter × depth × cooling)
- Kenward-Roger degrees-of-freedom adjustment
- Subgroup t-tests (unequal variances) for significant interactions
- SAS Version 9.4; significance threshold p ≤ 0.05 (two-sided)

## 4. Key Results and Benchmarks

### Maximum ΔT (°C), mean (SD) — all groups

| Depth | Diameter | Technique | No cooling | External cooling | p (external) |
|---|---|---|---|---|---|
| 10 mm | 2.0 mm | GS | 19.19 (2.42) | 9.44 (2.27) | — |
| 10 mm | 2.0 mm | CD | 23.43 (2.67) | 13.40 (3.65) | 0.0107* |
| 10 mm | 2.8 mm | GS | 26.36 (4.57) | 8.16 (2.43) | — |
| 10 mm | 2.8 mm | CD | 34.13 (5.69) | 5.62 (2.23) | 0.0256* (GS>CD) |
| 12 mm | 2.0 mm | GS | 20.03 (2.78) | 12.09 (4.52) | — |
| 12 mm | 2.0 mm | CD | 26.84 (4.42) | 22.10 (5.85) | 0.0005* |
| 12 mm | 2.8 mm | GS | 31.46 (4.60) | 10.03 (2.83) | — |
| 12 mm | 2.8 mm | CD | 36.33 (3.48) | 7.42 (3.12) | 0.0655 NS |

*Note: for 2.0 mm rows, GS < CD (p*); for 2.8 mm/10 mm external cooling row, GS > CD (p=0.0256)

### Without irrigation (all groups): CD > GS (p = 0.0016 to 0.0162)

### Four-way interaction (technique × diameter × depth × cooling): p = 0.0244 (significant)

### Thermal osteonecrosis threshold (44–47 °C): Not exceeded in any externally irrigated group

### Location of peak temperature
- 2.0 mm drills: highest ΔT at 3–6 mm depth (coronal–mid); deeper (6–9 mm) under irrigation
- 2.8 mm drills: highest ΔT at 3–6 mm without cooling; 6–12 mm under irrigation (heat penetrates deeper)

## 5. Limitations and Future Work

### Limitations
- In vitro model — no vital bone, blood circulation, or body temperature effects
- Irrigation flow distribution at drill–bone interface not directly measured; no mechanistic cooling conclusions
- Room-temperature saline used (refrigerated saline expected to produce lower absolute temperatures)
- Drilling speed fixed at 800 rpm (lower than some clinical protocols; limits absolute ΔT generalizability)
- Automated intermittent withdrawal reduces cumulative heat vs. continuous drilling
- Blinding of operators not feasible (guide configuration visible)

### Future Directions
- Different drill material compositions and alloy effects on heat generation
- Alternative guided geometries (open guide designs, sleeve configurations)
- Modified cooling strategies including internal irrigation and refrigerated saline
- Dynamic navigation and robotic implant preparation under standardized conditions
- Clinical validation studies

## 6. Related Work

- **Tur 2025** (same group, same platform): Sequential drills 2.2–3.5 mm — larger diameters show most pronounced GS vs. CD thermal differences; 3.5 mm most critical
- **Shobair 2026** (adjacent): Irrigation route (external vs. internal) effects on osteotomy heat
- Guided surgery accuracy reviews: fully guided > partially guided > freehand for implant placement precision
- Critical temperature thresholds: 44–47 °C for thermal osteonecrosis (bone growth chamber experiments)
- Infrared thermography limitations in irrigated preparations: potential inaccuracy of surface measurements

## 7. Glossary

- **GS (Guided Surgery / 유도 수술)**: Implant osteotomy using surgical guide with sleeves or drill handle cylinders
- **CD (Conventional Drilling / 일반 드릴링)**: Freehand drilling without surgical guide
- **Pilot drill (파일럿 드릴)**: First/smallest diameter drill initiating osteotomy; typically generates highest thermal peaks in incremental sequences
- **Partially guided surgery (부분 유도 수술)**: Guided osteotomy preparation without guided implant insertion
- **ΔT (온도 변화)**: Temperature change from baseline (T_max – T_initial)
- **BoneSim™**: Commercially manufactured bovine bone substitute with standardized cortical/cancellous layers
- **Thermal osteonecrosis (열성 골괴사)**: Heat-induced bone cell death potentially causing early implant failure
- **coDiagnostiX**: Guided surgery planning software (DentalWings)
- **Linear mixed model (선형 혼합 모형)**: Statistical model accounting for fixed and random effects, used for four-way interaction analysis
- **Kenward-Roger adjustment**: Degrees-of-freedom correction for unequal variances in mixed models
