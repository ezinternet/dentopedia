---
title: "Immediate Precision of the Digital Osteotomy Template in the Digital Stackable Template: A Clinical Study"
authors: Lu Jiayi et al.
year: 2021
doi: 10.7518/hxkq.2021.06.018
category: [digital-workflow]
pdf_path: /Users/oracleneo/llm-wiki/papers/lu-2021-digital-stackable-osteotomy-template-precision.pdf
pdf_filename: lu-2021-digital-stackable-osteotomy-template-precision.pdf
source_collection: external
---

## One-line Summary
Chinese clinical case series (n=4 edentulous patients) on a 3D-printed digital stackable template (osteotomy + implant + provisional in one stack) — mean volume deviation 492.94 mm³ (21.21% of preset), mean displacement 0.0248 mm, mean angle deviation 6.03°.

## 1. Document Information
- **Type**: Clinical case series (technique evaluation)
- **Journal**: West China Journal of Stomatology, 2021;39(6):732 (Chinese journal, English abstract available)
- **DOI**: 10.7518/hxkq.2021.06.018
- **Sample**: 4 edentulous patients (2 maxillary, 2 mandibular; age 43–57, mean 50), enrolled Nov 2018 to Jan 2020 at West China Hospital of Stomatology, Sichuan University
- **Primary Question**: How accurate is the osteotomy layer of a digital stackable guide in producing the planned bone level for immediate implant + immediate restoration?

## 2. Key Contributions
- Describes a **three-layer digital stackable template**: (1) osteotomy guide, (2) implant guide, (3) provisional restoration — designed to transfer the full pre-op virtual plan to surgery in one device.
- First clinical accuracy report (in this lab) of the osteotomy-guide layer specifically — prior reports focus on implant-guide accuracy.
- Volume deviation: mean **492.94 mm³**, = **21.21%** of preset osteotomy volume.
- Displacement deviation: mean **0.0248 mm** (range −0.5394 to +0.5033 mm across 4 cases).
- Angle deviation: mean **6.03°**, range 1.39° to 10.52°.
- Includes a per-case table (RU/RL/MU/ML) showing resin vs metal-printed guides on upper and lower arches.

## 3. Methodology and Architecture
Pre-op workflow: CBCT (with radiographic guide), intraoral scan (3Shape Trios), digital wax-up in ExoCAD, registration in BlueSky 4.5.9. The clinician defines **B-VTRS (bone-level vertical height of target restorative space)** — distance from bone surface to planned occlusal plane — to determine preset osteotomy level. Geomagic Studio 2013 used for stacked guide assembly. Three layers were 3D-printed (either resin or metal): osteotomy guide (base), implant guide (mated mechanically to osteotomy guide), provisional crown (on implant guide). Osteotomy performed under guidance, then pre/post CBCT superimposed for volumetric, displacement, and angular deviation analysis.

The B-VTRS thresholds drive prosthetic material selection: >15 mm → metal-acrylic bridge; 13–15 mm → PFM; 11–13 mm → monolithic zirconia. The osteotomy layer is the **reference plane** for the whole stack — its accuracy is the floor of the system's accuracy.

## 4. Key Results and Benchmarks
Per-case (Table 1):

| Case | Volume dev (mm³) | Displacement (mm) | Angle (°) |
|---|---|---|---|
| RU (max, resin) | 254.72 | 0.5033 | 4.12 |
| RL (mand, resin) | 84.51 | −0.0733 | 1.39 |
| MU (max, metal) | 1419.54 | −0.5394 | 8.07 |
| ML (mand, metal) | 213.00 | 0.0104 | 10.52 |
| **Mean** | **492.94** | **−0.0248** | **6.03** |

- Volume deviation = 21.21% of preset volume on average.
- Angle deviation range 1.39° to 10.52° — wide.
- One outlier case (MU, maxillary metal-printed) drives much of the mean volume deviation (1419.54 mm³).
- Authors note that surgical site (max vs mand) and guide material (resin vs metal) appear to influence accuracy.

## 5. Limitations and Future Work
- **n = 4** patients — case series, lowest evidence tier; cannot estimate accuracy distribution or compute CIs meaningfully.
- Wide spread in volume deviation (84.51 to 1419.54 mm³) — the mean of 492.94 mm³ hides one >1400 mm³ outlier (case MU).
- Mean displacement of 0.0248 mm is misleading — individual values range ±0.5 mm; the small mean reflects sign cancellation, not low absolute deviation.
- Angle deviation up to 10.52° is clinically significant — could mis-orient subsequent implant placement.
- No comparator (freehand or alternative guide design) — accuracy reported in isolation.
- Single center, single-team workflow.
- Mostly Chinese-language paper; English content limited to abstract — full discussion details not extractable from front/back text.
- Authors honestly conclude "later large-sample trials needed."

## 6. Related Work
- [[digital-workflow]] — category overview for guided surgery accuracy
- Related concepts in BlueSky/ExoCAD planning, B-VTRS-driven prosthetic decision-making
- Concept link to immediate implant + immediate provisional workflows

## 7. Glossary
- **数字化堆积导板 (digital stackable template)**: multi-layer 3D-printed guide stack — osteotomy guide → implant guide → provisional restoration, mechanically interlocking.
- **B-VTRS (bone-level vertical height of target restorative space)**: vertical distance from bone surface to planned occlusal plane; drives osteotomy depth and prosthetic material selection.
- **DSD (digital smile design)**: digital esthetic planning used here as input to wax-up.
- **CBCT superimposition**: pre/post 3D registration used to compute volumetric and angular deviations.
- **Volume / displacement / angle deviation**: three orthogonal metrics for osteotomy plane accuracy.
