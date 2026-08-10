---
title: "Analysis of factors determining thermal changes at osteotomy site in dental implant placement - An in-vitro study"
authors: Radhu Raj, V Manju, Vinod Kumar-Gopal, Manu Eswar
year: 2021
doi: 10.4317/jced.57346
category: [implants]
pdf_path: /Users/oracleneo/llm-wiki/papers/raj-2021-analysis-factors-determining-thermal-changes.pdf
pdf_filename: raj-2021-analysis-factors-determining-thermal-changes.pdf
source_collection: external
---

## Why Ingested

[[implants/chauhan-2018-biomechanical-factors-heat-generation-osteotomy]]의 다인자 SR 프레임워크(drill 속도·압력·irrigation이 모두 발열에 관여, 단독 지배인자 없음)를 뒷받침하는 정량적 in-vitro 데이터 — 본 논문은 speed×pressure×irrigant-temperature 3요인을 통제된 우골 (bovine femur) 실험으로 직접 비교해 최적 조합을 제시한다.

## Three-line Summary

In-vitro bovine femur study (72 drillings, 12 groups of n=6, factorial design) testing drilling speed (1500/2000/2500 rpm), operator hand pressure (1.2/2.4 kgf), and irrigant temperature (room temp vs 0°C) on osteotomy site temperature rise, measured by FLIR infrared thermography.

Highest ΔT occurred at 2000 rpm + 1.2 kgf + room-temperature saline; lowest ΔT occurred at 2500 rpm + 2.4 kgf + chilled (0°C) saline — none of the tested combinations exceeded the 47°C bone-necrosis threshold.

Clinical implication: high drilling speed combined with high hand pressure and continuous chilled-saline irrigation is the recommended combination to minimize thermal insult; limitation is bovine (not human) bone and a bench (non-clinical) test rig.

## 세줄요약

인비트로 우골 (Bovine Femur) 연구 (72회 시추, 12개 군 n=6, 요인설계): 시추 속도 (1500/2000/2500 rpm), 술자 수압 (Hand Pressure, 1.2/2.4 kgf), 세정액 온도 (실온 vs 0°C)가 절제부 발열에 미치는 영향을 FLIR 적외선 열화상으로 측정.

최고 온도상승 (ΔT)은 2000 rpm + 1.2 kgf + 실온 saline 조합에서, 최저 ΔT는 2500 rpm + 2.4 kgf + 냉각(0°C) saline 조합에서 관찰 — 모든 조합이 골괴사 임계온도 (47°C) 미만.

임상적 의미: 고속 회전 + 강한 수압 + 지속적 냉각 saline 세정 조합이 발열 최소화에 권장되나, 우골(사람 뼈 아님)·비임상 벤치 실험이라는 한계 존재.

## 1. Document Information
- **Journal**: J Clin Exp Dent 2021;13(3):e234-9
- **DOI**: 10.4317/jced.57346
- **Institution**: Amrita School of Dentistry, Amrita Institute of Medical Sciences and Research Centre, Kochi, Kerala, India

## 2. Key Contributions
- Factorial in-vitro design directly comparing three clinically modifiable variables (speed, hand pressure, irrigant temperature) simultaneously rather than one at a time.
- Confirms none of the tested parameter combinations exceed the 47°C thermal-necrosis threshold, even at the "worst" combination (2000 rpm/1.2 kgf/room-temp saline).
- Identifies the counterintuitive finding that higher speed (2500 rpm) combined with higher pressure (2.4 kgf) and chilled irrigation produced the LOWEST heat — speed alone is not the dominant driver; pressure and irrigation modulate its effect.

## 3. Methodology and Architecture
- **Design**: In-vitro experimental study, factorial (2 drill diameters × 3 speeds × 2 pressures × 2 irrigant temps).
- **Specimen**: Bovine femur, cut into 12 cm blocks, stored in neutral buffered formalin; each block used for up to 5 osteotomies.
- **n**: 72 total drillings across 12 groups (n=5–6 per group); drill diameters 2 mm (initial) and 2.8 mm (final).
- **Apparatus**: COXO dental physiodispenser mounted on an automated drill jig with load-cell-controlled hand pressure (1.2 or 2.4 kgf), constant feed rate (0.9 mm/s), constant torque (35 Ncm), depth 10 mm; irrigant delivered via burette at 40 mL/min.
- **Outcome**: Maximum temperature change from baseline (Δt max, °C) measured via FLIR TG165 infrared thermography.
- **Statistics**: F-test (speed vs drill diameter), T-test (pressure/irrigant temp vs drill diameter), Kruskal-Wallis (ANOVA-type, across groups), Mann-Whitney U (pairwise group comparisons); significance p<0.05.

## 4. Key Results and Benchmarks
- Drilling speed: ΔT = 38.9±4.5°C (1500 rpm), 41.1±5.7°C (2000 rpm) — highest recorded ΔT among the tested speeds (text truncated before full 2500 rpm value was captured in this extraction, but article states 2500 rpm + 2.4 kgf + chilled saline gave the overall lowest ΔT of all 12 groups).
- Highest overall ΔT group: 2000 rpm, 1.2 kgf hand pressure, room-temperature (28.2°C) saline irrigation.
- Lowest overall ΔT group: 2500 rpm, 2.4 kgf hand pressure, chilled (0°C) saline irrigation.
- All 12 groups stayed below the critical 47°C bone-necrosis threshold.

## 5. Limitations and Future Work
- Bovine femur bone used as a human-bone surrogate — differs in density/vascularity from human jaw bone.
- Bench test apparatus with fixed feed rate/torque; does not capture full variability of freehand clinical drilling.
- Only 2 drill diameters and 2 discrete pressure levels tested — dose-response across a continuous range not established.
- No irrigant flow-rate variation tested (fixed at 40 mL/min).

## 6. Related Work
- chauhan-2018: multi-factor SR framework (drill design/material/wear/method/irrigation/bone-quality/speed/load) — this paper provides quantitative factorial data for the speed/pressure/irrigation-temperature sub-factors.
- bernabeu-mira-2020: in-vitro drill design/material/wear study (no irrigation) — complementary factor (this paper adds irrigation and hand-pressure factors).

## 7. Glossary
- **Osteotomy site**: the drilled hole in bone prepared for implant placement.
- **ΔT (delta t max)**: maximum temperature rise from baseline recorded during drilling, the primary thermal-insult metric in this study.
- **FLIR thermography**: Forward-Looking Infrared camera imaging used to non-invasively measure surface temperature distribution.
- **kgf (kilogram-force)**: unit of operator hand pressure applied to the drill during osteotomy, calibrated via load cell.
- **Thermal necrosis threshold (47°C)**: temperature above which functional bone regeneration is compromised if sustained for ≥1 minute.
