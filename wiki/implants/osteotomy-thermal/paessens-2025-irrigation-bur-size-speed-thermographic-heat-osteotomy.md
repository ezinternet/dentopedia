---
title: "Effect of Irrigation, Bur Size and Rotational Speed on Thermographic Heat at Implant Site Osteotomy Interface"
authors: Paeßens K, van Bebber L, Zipprich H, Weigl P
year: 2025
date: 2025-06-16
doi: 10.1111/clr.14462
source: paessens-2025-irrigation-bur-size-speed-thermographic-heat-osteotomy.md
category: implants/osteotomy-thermal
evidence_level: in-vitro
pmid: "40521678"
pmcid: "PMC12423576"
source_collection: pubmed-text
text_path: /Users/oracleneo/llm-wiki/papers/paessens-2025-irrigation-bur-size-speed-thermographic-heat-osteotomy.txt
text_filename: paessens-2025-irrigation-bur-size-speed-thermographic-heat-osteotomy.txt
tags: [irrigation, thermal-osteonecrosis, drilling-heat, bur-size, rotational-speed, logistic-regression]
relations:
  - target: implants/osteotomy-thermal/chauhan-2018-biomechanical-factors-heat-generation-osteotomy
    type: extends
    note: "Paeßens 2025 quantifies OR for each risk factor (irrigation dominant OR 177.5)"
---

## Three-line Summary

Paeßens 2025 is the first in vitro study to directly measure bone-drill interface temperature during **irrigated** expansion osteotomy via thermographic camera, using cortical bovine bone (3.5 mm thick). Logistic regression over 120 specimens (2.4 mm pilot → 3.2 or 3.8 mm, 200/600/1000 rpm) identified absence of irrigation as the dominant risk factor for critical heat (≥47°C), with OR 177.53 — far exceeding expansion step size (OR 9.94) and speed per 400 rpm (OR 4.94). The study refutes prior claims that low-speed drilling without irrigation is thermally safe, while confirming that 200 rpm with irrigation keeps both expansion step sizes below the critical threshold.

## 세줄요약

관개수(생리식염수) 미사용이 임계 골 온도(≥47°C) 발생의 압도적 위험인자(OR 177.53)이며, 저속만으로는 무관개 안전을 보장하지 못함 — 200 rpm 무관개에서도 전 시편 80~100%가 47°C 초과. 200 rpm + 관개 조건에서는 Δ0.8 mm 및 Δ1.4 mm 확장 모두 임계온도 미달(평균 38.08°C, 38.81°C)이어서 단계 축약 프로토콜을 지지. 직접 열화상 계면 측정법을 통해 기존 열전대·파이로미터 연구들이 최대 온도를 구조적으로 과소평가했음을 제시.

## Summary

This in vitro study evaluated three modifiable factors affecting critical heat generation (≥47°C) at the dynamic bone-drill interface during dental implant osteotomy expansion: (1) irrigation, (2) expansion step size, and (3) rotational speed.

**Setup**: 120 cortical bovine rib specimens (3.5 mm thick) with pre-drilled 2.4 mm pilot cavities were expanded to 3.2 mm (small step, Δ0.8 mm) or 3.8 mm (large step, Δ1.4 mm) using double twist drills at 200, 600, or 1000 rpm, with or without saline irrigation (56 mL/min). An Optris Pi 640 thermographic camera (125 fps, 0.1°C sensitivity) measured the interface temperature at the moment the drill perforated the bone lamella — a novel direct-measurement method that avoids the underestimation inherent to thermocouples and pyrometers.

**Key finding**: Irrigation was by far the most important factor (OR 177.53, p = 0.00092). Without irrigation, all 60 no-irrigation specimens exceeded 47°C regardless of speed or step. With irrigation at 200 rpm, neither small nor large expansion steps exceeded the critical threshold (mean 38.08°C and 38.81°C respectively). The study hypothesis — that low speed + small step alone would prevent critical temperatures even without irrigation — was rejected.

## Key Contributions

1. **Novel thermographic direct-interface method**: first setup to capture irrigated expansion osteotomy temperature at the bone-drill interface in real time, eliminating the systematic underestimation of thermocouples (can be 19.4°C below source per FEM models) and pyrometers (area-averaged, not hotspot-resolved).

2. **OR hierarchy quantified**: irrigation absence OR 177.53 >> expansion step Δ1.4 mm OR 9.94 >> speed +400 rpm OR 4.94 — prior studies identified directional effects but not relative magnitude.

3. **Shortened drilling protocols validated thermally**: 200 rpm + irrigation renders Δ1.4 mm single-step expansion (2.4 → 3.8 mm) thermally safe, supporting reduction of intermediate drilling steps.

4. **Refutes low-speed no-irrigation safety**: at 200 rpm without irrigation, 80% of small-step specimens still exceeded 47°C; model predicts W = 0.60 even at 50 rpm without irrigation. Bone harvesting without irrigation is therefore not thermally benign.

5. **Contradicts several prior studies**: Bogovic et al. (inverse speed-temperature correlation), Marzook et al. (inverse, rabbit in vivo), Mihali et al. (inverse step size) — attributing discrepancies to thermocouple/pyrometer limitations in those studies.

## Methodology

| Parameter | Detail |
|---|---|
| Bone model | Bovine rib cortex, 3.5 ± 0.05 mm standardized thickness |
| Pilot cavity | 2.4 mm diameter, blind (no perforation) |
| Expansion targets | 3.2 mm (Δ0.8 mm, SS) / 3.8 mm (Δ1.4 mm, LS) |
| Speeds | 200, 600, 1000 rpm |
| Irrigation | With (56 mL/min saline) / Without |
| n per group | 10 specimens × 12 groups = 120 total |
| Drills | Nobel Biocare double twist 3.2/3.6 mm and 3.8/4.2 mm; stop at 4.3 mm |
| Temperature sensor | Optris Pi 640 thermographic camera; 640×480 px; 0.1°C sensitivity; 125 fps |
| Outcome | Binary: ≥47°C (critical) vs. <47°C; multivariate logistic regression in R |
| Drill reuse | 6× per drill; preliminary test confirmed no wear effect (p = 0.88) |

**Critical innovation**: thin lamella (0.3–0.6 mm) left between pilot cavity and milled recess is perforated laterally during expansion — camera positioned on opposite side records the bone-drill interface temperature at breakthrough moment, avoiding irrigation fluid contamination of the thermal image.

## Results

### Odds ratios (multivariate logistic regression)

| Predictor | OR | 95% CI | p |
|---|---|---|---|
| Irrigation absent vs. present | **177.53** | 35.67–1448.46 | 0.00092 |
| Expansion step Δ1.4 mm vs. Δ0.8 mm | **9.94** | 2.76–46.50 | 0.0012 |
| Speed per +400 rpm | **4.94** | 2.18–13.54 | 0.00049 |

**Predictive formula**: W = 1 / (1 + e^−z); z = 1.596×(speed/400rpm) + 5.179×(no irr) + 2.297×(Δ1.4mm) − 4.984

### Group mean temperatures (°C)

| Group | Irrig | Δø | rpm | Mean (°C) | SD | % ≥47°C |
|---|---|---|---|---|---|---|
| SS-WI-200 | Yes | 0.8 | 200 | **38.08** | 1.01 | **0%** |
| SS-WI-600 | Yes | 0.8 | 600 | 43.18 | 2.92 | 0% |
| SS-WI-1000 | Yes | 0.8 | 1000 | 45.28 | 3.56 | ~40% |
| LS-WI-200 | Yes | 1.4 | 200 | **38.81** | 1.93 | **0%** |
| LS-WI-600 | Yes | 1.4 | 600 | 45.97 | 3.93 | ~50% |
| LS-WI-1000 | Yes | 1.4 | 1000 | 50.06 | 4.38 | ~80% |
| SS-NI-200 | No | 0.8 | 200 | 50.31 | 3.45 | ~80% |
| SS-NI-600 | No | 0.8 | 600 | 54.39 | 4.69 | 100% |
| SS-NI-1000 | No | 0.8 | 1000 | 66.89 | 26.57 | ~80% |
| LS-NI-200 | No | 1.4 | 200 | 54.00 | 4.46 | 100% |
| LS-NI-600 | No | 1.4 | 600 | 59.94 | 6.32 | 100% |
| LS-NI-1000 | No | 1.4 | 1000 | 66.78 | 15.33 | 100% |

- Peak single values: 55.4°C (WI, 1000 rpm); 116.4°C (NI, 1000 rpm)
- Groups never exceeding 47°C: SS-WI-200, SS-WI-600, LS-WI-200

### Clinical takeaway

Safe zone: **200 rpm + irrigation** — allows both Δ0.8 mm and Δ1.4 mm expansion without critical heat. Irrigation is non-negotiable: even at 200 rpm, no-irrigation crosses the threshold in 80% of specimens. Drilling speeds of 600–1000 rpm require irrigation but even then carry increasing risk at larger expansion steps.

## Related Papers

- [[implants/osteotomy-thermal/chauhan-2018-biomechanical-factors-heat-generation-osteotomy]] — biomechanical factor review; Paeßens 2025 extends with direct OR quantification
- [[implants/osteotomy-thermal/heuzeroth-2021-thermal-exposure-osteotomy-osseointegration]] — thermal exposure thresholds and osseointegration outcomes
- [[implants/osteotomy-thermal/bernabeu-mira-2020-bone-heating-drilling-implant]] — low-speed no-irrigation bone harvesting; directly contradicted by Paeßens 2025 findings
- [[implants/osteotomy-thermal/raj-2021-analysis-factors-determining-thermal-changes]] — multi-factor thermal analysis; compared in Discussion
- [[implants/osteotomy-thermal/gehrke-2020-technique-drill-design-osteotomy]] — drill design and wear; Paeßens confirms worn drills not tested here; sharper drills recommended
- [[implants/osteotomy-thermal/sener-2009-effects-irrigation-temperature-heat-control]] — irrigation as heat control mechanism; Paeßens 2025 provides strongest OR evidence to date
