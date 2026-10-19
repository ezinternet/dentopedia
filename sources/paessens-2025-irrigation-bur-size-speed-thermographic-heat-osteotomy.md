---
title: "Effect of Irrigation, Bur Size and Rotational Speed on Thermographic Heat at Implant Site Osteotomy Interface. An In Vitro Study"
authors: Paeßens K, van Bebber L, Zipprich H, Weigl P
year: 2025
date: 2025-06-16
doi: 10.1111/clr.14462
pmid: "40521678"
pmcid: "PMC12423576"
category: implants/osteotomy-thermal
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12423576/
source_collection: pubmed-text
full_text: true
text_path: /Users/oracleneo/llm-wiki/papers/paessens-2025-irrigation-bur-size-speed-thermographic-heat-osteotomy.txt
text_filename: paessens-2025-irrigation-bur-size-speed-thermographic-heat-osteotomy.txt
---

## Why Ingested

First study to directly measure the 골-드릴 계면 온도 (bone-drill interface temperature) during an **irrigated** expansion osteotomy using thermographic imaging, yielding logistic regression odds ratios for three modifiable risk factors (irrigation, expansion step, speed). Adds quantitative risk modeling to the existing [[implants/osteotomy-thermal/osteotomy-thermal]] evidence base, which lacks direct interface data under irrigation.

## Three-line Summary

In vitro expansion osteotomies (2.4 → 3.2 or 3.8 mm, bovine cortical bone 3.5 mm thick) showed that absence of irrigation is by far the dominant risk factor for critical bone heat (≥47°C), with an odds ratio of 177.53 — dwarfing expansion step (OR 9.94) and speed per 400 rpm increment (OR 4.94). Without irrigation, all 60 test specimens exceeded 47°C regardless of speed or step size, refuting the hypothesis that low speed + small step could keep temperatures safe without irrigation. With irrigation at 200 rpm, both small (0.8 mm) and large (1.4 mm) expansion steps remained below 47°C in all specimens, supporting shortened drilling protocols when irrigation is guaranteed.

## 세줄요약

관개수(생리식염수) 미사용이 임계 골 온도(≥47°C) 발생의 압도적 위험인자(OR 177.53)였으며, 저속+소경 확장만으로는 관개수 없이 안전을 보장할 수 없음을 규명함. 관개수 없이는 200 rpm에서도 전 그룹이 47°C 초과 — 종전 저속 무관개 안전론을 반박. 200 rpm + 관개 조건에서는 0.8 mm 및 1.4 mm 확장 모두 임계온도 미달, 단계 축약 프로토콜을 지지.

## 1. Document Information

- **Title:** Effect of Irrigation, Bur Size and Rotational Speed on Thermographic Heat at Implant Site Osteotomy Interface. An In Vitro Study
- **Authors:** Paeßens K, van Bebber L, Zipprich H, Weigl P
- **Journal:** Clinical Oral Implants Research (CLOR)
- **Year:** 2025; Volume 36, Issue 9, Pages 1126–1135
- **DOI:** [10.1111/clr.14462](https://doi.org/10.1111/clr.14462)
- **PMID:** 40521678 | **PMCID:** PMC12423576
- **Evidence level:** In vitro (cortical bovine rib bone model)
- **Affiliation:** Goethe University Frankfurt, Germany; Nobel Biocare Services AG (drills)

## 2. Key Contributions

1. **First direct thermographic measurement under irrigation**: prior setups either lacked irrigation or measured temperature at the outer bone surface or a time-delayed drill surface, systematically underestimating peak values.
2. **Logistic regression OR hierarchy**: irrigation absent OR 177.53 >> expansion step Δ1.4 mm OR 9.94 >> speed +400 rpm OR 4.94; quantifies relative importance rather than just direction.
3. **Refutes low-speed/no-irrigation safety claim**: even at 200 rpm, no-irrigation groups had 80–100% specimens exceeding 47°C; prior studies reporting "safe" temperatures without irrigation used pyrometers or surface thermocouples that underestimate interface heat.
4. **Supports shortened drilling protocols**: with irrigation at 200 rpm, skipping intermediate steps (Δ1.4 mm expansion) is thermally safe — mean temperatures of 38.81°C (ΔT 2.21°C) in the LS-WI-200rpm group.
5. **Cautions bone harvesting without irrigation**: collected bone chips are popular for GBR, but harvesting at low speed without irrigation still generates critical heat and should be restricted to favorable conditions.

## 3. Methodology and Architecture

### Specimen preparation
- Bovine rib distal cortex; cortical thickness standardized to **3.5 ± 0.05 mm** (recess milled on opposite side)
- Pre-drilled 2.4 mm pilot cavity (blind, no perforation); specimens equilibrated to 36.6°C in water bath
- Thin lamella (0.3 mm for 3.2 mm drills; 0.6 mm for 3.8 mm drills) designed for lateral perforation during expansion — allows direct camera access to interface at moment of breakthrough

### Experimental design
| Factor | Levels |
|---|---|
| Irrigation | With (56 mL/min saline) / Without |
| Drill diameter expansion | SS: 2.4 → 3.2 mm (Δ0.8 mm) / LS: 2.4 → 3.8 mm (Δ1.4 mm) |
| Rotational speed | 200 / 600 / 1000 rpm |
| n per group | 10 specimens |
| Total specimens | 120 |

- Double twist parallel step drills (Nobel Biocare 3.2/3.6 and 3.8/4.2 mm); stop collar at 4.3 mm
- Each drill reused 6 times (preliminary wear test confirmed no significant temperature effect: p = 0.88)

### Thermographic system
- Optris Pi 640 camera; resolution 640×480 px; sensitivity 0.1°C; absolute accuracy ±2°C
- Positioned 45°, 10 cm from recess; records at 125 fps
- Advantage over pyrometers: per-pixel temperature vs. area average → does not underestimate hotspot maximum

### Statistical analysis
- Outcome: binary (≥47°C vs. <47°C)
- Multivariate logistic regression in R (readxl, ggplot2, dplyr)
- Events per predictor = 15.7 (range 10–20 recommended by Peduzzi et al.); 73 positive / 47 negative events

## 4. Key Results and Benchmarks

### Group mean temperatures (°C ± SD)
| Group | Irr | Δø (mm) | rpm | Mean max (°C) | SD |
|---|---|---|---|---|---|
| SS-WI-200 | Yes | 0.8 | 200 | **38.08** | 1.01 |
| SS-WI-600 | Yes | 0.8 | 600 | 43.18 | 2.92 |
| SS-WI-1000 | Yes | 0.8 | 1000 | 45.28 | 3.56 |
| LS-WI-200 | Yes | 1.4 | 200 | **38.81** | 1.93 |
| LS-WI-600 | Yes | 1.4 | 600 | 45.97 | 3.93 |
| LS-WI-1000 | Yes | 1.4 | 1000 | 50.06 | 4.38 |
| SS-NI-200 | No | 0.8 | 200 | 50.31 | 3.45 |
| SS-NI-600 | No | 0.8 | 600 | 54.39 | 4.69 |
| SS-NI-1000 | No | 0.8 | 1000 | 66.89 | **26.57** |
| LS-NI-200 | No | 1.4 | 200 | 54.00 | 4.46 |
| LS-NI-600 | No | 1.4 | 600 | 59.94 | 6.32 |
| LS-NI-1000 | No | 1.4 | 1000 | 66.78 | 15.33 |

### Logistic regression ORs
| Predictor | OR | 95% CI | p |
|---|---|---|---|
| Irrigation absent (vs. present) | **177.53** | 35.67–1448.46 | 0.00092 |
| Expansion step Δ1.4 mm (vs. Δ0.8 mm) | **9.94** | 2.76–46.50 | 0.0012 |
| Speed +400 rpm increment | **4.94** | 2.18–13.54 | 0.00049 |

**Predictive formula:**
W (P ≥47°C) = 1 / (1 + e^−z)
z = 1.596 × (speed/400rpm) + 5.179 × (no irrigation) + 2.297 × (Δ1.4mm step) − 4.984

### Threshold crossings (% specimens ≥47°C)
- Groups 1, 2, 4 (any WI, ≤600rpm small step or 200rpm large): **0%**
- Group 3 (SS-WI-1000): ~40%
- Group 5 (LS-WI-600): ~50%
- Groups 6, 7, 9 (WI-1000 large, NI-200 small, NI-1000 small): **80%**
- Groups 8, 10, 11, 12 (all NI except small-200): **100%**

### Peak single values
- Maximum with irrigation: 55.4°C (1000 rpm)
- Maximum without irrigation: 116.4°C (1000 rpm)

## 5. Limitations and Future Work

- **In vitro only**: bovine cortical rib, 3.5 mm uniform thickness; does not reflect variable human cortical thickness, bone density, or cumulative heat from sequential drilling steps
- **Drilling depth 4.3 mm**: non-standard (experimental constraint of lamella method); authors note drilling length is generally not found to influence heat (Gehrke et al.; Kapse et al.)
- **Freehand drilling**: contact pressure calibrated to ~10 N using a scale, but not mechanically controlled; drilling time ~1–2 s
- **Exposure time not measured**: only peak temperature captured; duration above threshold equally important for osteonecrosis risk (Lundskog)
- **Drill design not varied**: serially available double twist drills used; microscopic surface variation of unused vs. used not studied
- **High SD in no-irrigation high-speed groups** (groups 9 and 12, SD >15°C): large biological and mechanical variability not yet explained; requires further study
- **Future**: clinical studies needed to link temperature findings with early implant failure rates, particularly for immediately loaded implants

## 6. Related Work

- **Chauhan 2018** [[implants/osteotomy-thermal/chauhan-2018-biomechanical-factors-heat-generation-osteotomy]]: reviews biomechanical factors including speed, force, drill design — present study extends by quantifying each factor's OR
- **Lajolo et al.**: introduced direct-perforation thermographic method (pilot only, no irrigation); Paeßens 2025 extends to irrigated expansion
- **Bogovic et al.**: found inverse speed-temperature correlation (faster = cooler); contradicted by present study (positive correlation); attributed to thermocouple limitation underestimating peaks
- **Marzook et al.**: inverse speed correlation via rabbit in vivo model; also contradicted — similar conditions produced 8.68°C increase vs. their 3.54°C
- **Mihali et al.**: suggested inverse step-temperature correlation (smaller step → hotter); contradicted by present study's direct OR
- **Bernabeu-Mira et al.**: deemed low-speed no-irrigation "safe" based on prior thermometric data; refuted by present thermographic direct-interface findings
- **Calvo-Guirado et al.**: noted cumulative temperature rise across sequential drilling steps; present study measures only single expansion step, so clinical total may exceed reported values
- **Bacci et al.** and **Lucchiari et al.**: pyrometer-based studies showing <1°C increases at drilled surfaces; substantially lower than present results due to pyrometer averaging and surface (non-interface) measurement

## 7. Glossary

- **골-드릴 계면 온도 (Bone-Drill Interface Temperature)**: temperature measured directly at the contact zone between rotating drill and bone — highest heat point
- **임계 온도 (Critical Temperature, 47°C)**: body temperature (37°C) + ΔT 10°C; established as threshold for potential osteonecrosis (Eriksson & Albrektsson 1983)
- **확장 단계 (Expansion Step, Δø)**: difference in diameter between pilot cavity and expansion drill (Δ0.8 mm = small step; Δ1.4 mm = large step)
- **열화상 카메라 (Thermographic Camera)**: per-pixel infrared temperature recording vs. pyrometer (single-area average); more accurate for hotspot detection
- **OR (Odds Ratio)**: from logistic regression; OR 177.53 for no-irrigation means 177× higher odds of critical heat when irrigation is absent
- **EPV (Events Per Variable)**: 15.7 here; Peduzzi et al. recommend 10–20 for logistic regression stability
- **SS / LS**: Small Step (2.4→3.2 mm) / Large Step (2.4→3.8 mm)
- **WI / NI**: With Irrigation / No Irrigation
