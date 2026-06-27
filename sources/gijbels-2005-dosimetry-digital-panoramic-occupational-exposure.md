---
title: "Dosimetry of digital panoramic imaging. Part II: Occupational exposure"
authors: "Gijbels F, Jacobs R, Debaveye D, Bogaerts R, Verlinden S, Sanderink G"
year: 2005
doi: "10.1259/dmfr/65011036"
pmid: "15897285"
category: [radiology]
source_collection: pubmed-text
full_text: false
text_path: /Users/oracleneo/llm-wiki/papers/gijbels-2005-dosimetry-digital-panoramic-occupational-exposure.txt
text_filename: gijbels-2005-dosimetry-digital-panoramic-occupational-exposure.txt
---

## Why Ingested

파노라마촬영실 외부(1 m 거리)의 산란선량을 실측한 핵심 데이터. 기존 [[radiology/benavides-2023-patient-shielding-dentomaxillofacial-radiography]] 및 [[radiology/schindler-2025-panoramic-thyroid-eye-lens-dose]]의 환자 측 선량 논의를 보완하여, 직원이 파노라마 촬영 중 실제로 받는 피폭량을 정량화하는 근거로 활용.

## One-line Summary

In-vitro phantom study with 5 digital panoramic units: scatter dose at 1 m from unit was ≤0.60 μGy per exposure; 500 panoramics/year yields 5–40 μSv annual occupational organ dose to operator.

## 한줄요약

5종 디지털 파노라마 장치 팬텀 실험: 1 m 거리 산란선량 최대 0.60 μGy/촬영, 연간 500회 기준 술자 갑상선 5–15 μSv, 생식선 5–40 μSv 추가 피폭.

## 1. Document Information

- **Journal**: Dento-Maxillo-Facial Radiology, Vol. 34, No. 3, pp. 150–153
- **Published**: May 2005
- **PMID**: 15897285
- **DOI**: [10.1259/dmfr/65011036](https://doi.org/10.1259/dmfr/65011036)
- **Funding / COI**: Not reported in abstract

## 2. Key Contributions

- First systematic measurement of operator scatter dose from five different **digital** panoramic units using ionization chambers at 1 m
- Defined scatter dose at thyroid-gland level (seated operator position) and gonadal level around the unit at 5 positions
- Provides annual occupational dose estimate based on realistic workload (500 panoramics/year)
- Demonstrated variation between machines: 0.04–0.53 μGy organ equivalent dose per exposure depending on unit type and position

## 3. Methodology and Architecture

- **Study design**: In vitro phantom dosimetry
- **Equipment**: 5 digital panoramic units (4 direct digital CCD, 1 storage phosphor)
- **Phantom**: Anthropomorphic phantom as patient surrogate
- **Dosimetry**: Ionization chamber at 1 m from phantom at 5 positions around unit; measured at thyroid level and gonadal level
- **Parameters**: kVp 64–74, exposure time 8.2–19.0 s, mA 4–7 (as per manufacturer recommendations)
- **Outcome**: Organ equivalent dose (μGy) and organ effective dose (μSv) per exposure and annually (500 exposures/year)

## 4. Key Results and Benchmarks

| Metric | Value |
|---|---|
| Max organ equivalent dose per exposure at 1 m | 0.60 μGy |
| Max organ effective dose per exposure at 1 m | 0.10 μSv |
| Average organ equivalent dose (across 5 units, 5 positions) | 0.18–0.30 μGy |
| Average organ effective dose (across positions) | 0.01–0.05 μSv |
| Range across machines | 0.04–0.53 μGy (equivalent); 0.01–0.08 μSv (effective) |
| **Annual thyroid dose (500 panoramics, 1 m)** | **5–15 μSv** |
| **Annual gonadal dose (500 panoramics, 1 m)** | **5–40 μSv** |

Key inference: even at maximum workload (500 panoramics/year), annual operator dose is **<0.1 mSv** — far below the 20 mSv/year occupational limit and even below the 1 mSv/year public limit.

## 5. Limitations and Future Work

- Abstract-only retrieval; full methodology details not confirmed
- Only 5 units tested; dose may differ for analogue or newer flat-panel panoramic units
- 1 m was the only measured distance; closer positions (e.g., 0.5 m if operator leaves room late) not assessed
- 500 panoramics/year assumption may underestimate high-volume practices
- No measurement with operator wearing lead apron vs not

## 6. Related Work

- Companion paper: "Dosimetry of digital panoramic imaging. Part I: Patient dosimetry" (same authors) — measures patient effective dose
- Gijbels et al. 2004 (DMFR) — Belgian dentists attitude to radiation protection; same group

## 7. Glossary

- **Organ equivalent dose**: absorbed dose × radiation weighting factor (Gy for X-rays → μGy)
- **Organ effective dose**: organ equivalent dose × tissue weighting factor (Sv → μSv)
- **CCD**: charge-coupled device (direct digital detector)
- **Storage phosphor**: indirect digital detector (photostimulable phosphor plate)
- **Ionization chamber**: gas-filled detector for precise air kerma measurement
