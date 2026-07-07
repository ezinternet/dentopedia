---
title: "A clinical observational analysis of aerosol emissions from dental procedures"
authors: Dudding T, Sheikh S, Gregson F, Haworth J, Haworth S, Main BG, Shrimpton AJ, Hamilton FW, Ireland AJ, Maskell NA, Reid JP, Bzdek BR, Gormley M
year: 2022
doi: 10.1371/journal.pone.0265076
category: [infection-control]
source_collection: pubmed-text
full_text: true
pmid: "35271682"
pmcid: "PMC8912243"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8912243/
text_path: /Users/oracleneo/llm-wiki/papers/dudding-2022-clinical-observational-analysis-aerosol-emissions.txt
text_filename: dudding-2022-clinical-observational-analysis-aerosol-emissions.txt
---

## Why Ingested

쓰리웨이 시린지 오염의 "에어(공기)" 축을 다루는 논문. [[infection-control/dang-2022-assessment-microbiota-diversity-dental-unit]]가 시린지 물 오염을 정량했다면, 본 임상연구는 3-in-1 air/water syringe가 실제로 에어로졸을 얼마나 발생시키는지, 그리고 그 에어로졸이 기구 유래(비타액성)인지 타액 오염인지 크기분포 지문으로 구분한다. "시린지 물이 오염되면 에어로졸로 퍼진다"는 감염관리 연결고리를 실측으로 보강.

## Three-line Summary

Clinical observational study (41 patients, 15 procedures) measuring aerosol number concentration (0.5–20 μm APS) with phantom-head controls to fingerprint aerosol source.

3-in-1 air+water syringe generated aerosol 75.3% of use time (air only 24.8%; water only produced none), but its size distribution matched the non-salivary instrument source — unlike high/slow-speed drilling, which showed unexplained (salivary) aerosol (P<0.002).

The three-way syringe is a real aerosol generator, but the aerosol is instrument-derived, so its infection risk is governed by DUWL water quality rather than salivary contamination.

## 세줄요약

임상 관찰연구(환자 41명, 시술 15종)로 에어로졸 수농도(0.5–20 μm, APS)를 팬텀헤드 대조와 비교해 에어로졸 발생원을 크기분포 지문으로 규명.

3-in-1 air+water 시린지는 사용시간의 75.3% 동안 에어로졸 발생(air만 24.8%, water만은 미검출)했으나 크기분포가 비타액성 기구 발생원과 일치 — 타액성 에어로졸이 나온 고속·저속 드릴(P<0.002)과 대비.

쓰리웨이 시린지는 실제 에어로졸 발생원이지만 그 에어로졸은 기구(수관 물) 유래 → 감염 위험은 타액 오염보다 DUWL 수질이 좌우.

## 1. Document Information

- **Journal**: PLoS One, 2022 Mar 10; 17(3):e0265076
- **Type**: Prospective clinical observational study (AERATOR study; STROBE)
- **Setting**: Bristol Dental Hospital; 41 adult patients (periodontal, oral surgery, orthodontic)
- **DOI**: [10.1371/journal.pone.0265076](https://doi.org/10.1371/journal.pone.0265076)

## 2. Key Contributions

1. Measured aerosol from real patients (not just phantom heads) using an aerodynamic particle sizer with a low enough background to resolve a cough.
2. Introduced **aerosol size-distribution fingerprinting** to separate instrument-generated vs salivary-contaminated aerosol.
3. Quantified the **3-in-1 air/water syringe** specifically: air+water aerosolises heavily but water-only does not, and the aerosol is instrument-derived.
4. Reframed AGP as a continuum, not a binary.

## 3. Methodology and Architecture

- TSI 3321 APS (0.5–20 μm), 3D-printed funnel 22 cm from nasion at 45° (11 o'clock).
- Baseline: breathing, speaking, three coughs. Each patient: 3-in-1 air 30 s, water 30 s, air+water 30 s to all teeth.
- High-volume aspiration 300 L/min (60 L/min Yankauer for oral surgery).
- Phantom-head controls in triplicate; size distributions compared by mode number, width log(σ), peak Dp,c; unpaired t-test, Bonferroni p<0.002.

## 4. Key Results and Benchmarks

- 41 patients, median age 47; background 0.18 particles/cm³.
- 9 of 15 procedures produced NO aerosol above background — including probe exam, hand scaling, LA, extraction, flap raising, bracket removal, alginate impression, **3-in-1 water only**, suturing.
- 6 aerosol-producing procedures (% of procedure time aerosol detected): ultrasonic scaling 12.7%, **3-in-1 air only 24.8%, 3-in-1 air+water 75.3%**, high-speed drilling 40.1%, slow-speed drilling 49.9%, surgical drilling 55.6%. (Abstract cites 42.9% as the overall 3-in-1 air+water figure.)
- High-speed drilling produced the most aerosol (median 118.38 /cm³).
- Size distributions for ultrasonic scaling, 3-in-1 air/air+water, and surgical drilling **matched** phantom controls → instrument-derived, non-salivary.
- High and slow speed drilling **differed** from phantom controls (e.g., slow-speed Mode1 mean diff log σ 0.17, P=5.54×10⁻⁴) → unexplained salivary aerosol.

## 5. Limitations and Future Work

- Did not test for SARS-CoV-2 or biological content of aerosol.
- Limited to 0.5–20 μm; larger droplets and <0.5 μm particles not captured.
- Single centre; instrument use may vary by clinician; results may not extrapolate to other instrument uses.

## 6. Related Work

- Air-side counterpart to [[infection-control/dang-2022-assessment-microbiota-diversity-dental-unit]] (syringe water microbiota).
- Complements [[infection-control/ji-2018-three-key-factors-influencing-bacterial]] (output-water contamination and its aerosol exposure risk).
- Reinforces [[infection-control/samaranayake-2024-dental-unit-waterlines-disinfection]] (occupational aerosol exposure).

## 7. Glossary

- **AGP**: aerosol-generating procedure — releases airborne particles <5 μm.
- **APS**: aerodynamic particle sizer.
- **3-in-1 / triple / air-water syringe**: dental instrument delivering air, water, or a combined spray.
- **Size-distribution fingerprint**: log-normal mode parameters (peak Dp,c, width log σ) used to attribute aerosol to a source.
- **Phantom head control**: instrument operated on a manikin to capture non-salivary instrument aerosol.
