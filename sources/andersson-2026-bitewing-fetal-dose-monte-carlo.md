---
title: "Monte Carlo calculations of the radiation absorbed dose to a fetus of a pregnant patient from a dental bitewing X-ray exposure"
authors: "Andersson M, Maroussi E"
year: 2026
doi: 10.1093/rpd/ncaf174
category: [radiology]
pmid: "41821463"
pmcid: "PMC13046037"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13046037/
text_path: /Users/oracleneo/llm-wiki/papers/andersson-2026-bitewing-fetal-dose-monte-carlo.txt
text_filename: andersson-2026-bitewing-fetal-dose-monte-carlo.txt
source_collection: pubmed-text
full_text: true
---

## Why Ingested

Most recent dental fetal-dose estimate (ICRP pregnant phantom), quantifying the fetal dose from the commonest intraoral exposure in nGy — supports the "far below threshold" message of the pregnant-staff guide.

→ [[radiology/benavides-2023-patient-shielding-dentomaxillofacial-radiography]] — no abdominal shielding
→ [[radiology/johnson-2020-intraoral-radiograph-dose-collimation-thyroid-shielding]] — intraoral dose context

## Three-line Summary

Monte Carlo simulation (MCNP6.3; Gothenburg; Radiat Prot Dosimetry 2026) of a 60 kV bitewing on the ICRP 25-week pregnant reference phantom wearing a 0.25 mm Pb thyroid collar, for phosphor-plate (0.25 s) and digital-sensor (0.05 s) receptors.

Highest fetal organ doses were ~27 nGy (brain) and 25 nGy (red bone marrow, bone endosteum) with phosphor plates and ~5 nGy with digital sensors; the fetus received about 0.0015 of the mother's dose because maternal tissue absorbs the scatter.

Fetal exposure from a bitewing is negligible and needs no extra protection (e.g. abdominal lead apron) beyond the Swedish mandatory thyroid collar; findings support reassurance-based communication with pregnant patients.

## 세줄요약

몬테카를로 시뮬레이션(MCNP6.3, 예테보리, Radiat Prot Dosimetry 2026) — ICRP 25주 임신 기준 팬텀(0.25 mm Pb 갑상선 칼라 착용)에 60 kV 교익촬영, 형광판(0.25초)·디지털 센서(0.05초).

태아 장기 최고 선량은 형광판 기준 뇌 약 27 nGy, 적색골수·골내막 25 nGy, 디지털 센서는 약 5 nGy. 모체 조직이 산란선을 흡수해 태아는 모체 선량의 약 0.0015배만 받음.

교익촬영의 태아 피폭은 무시할 수준이며, 스웨덴 필수 갑상선 칼라 외 추가 방호(복부 납 앞치마 등)는 필요 없다 — 임신 환자에게 수치 기반 안심 설명의 근거.

## 1. Document Information

- Journal: Radiation Protection Dosimetry (2026)
- PMID 41821463 · PMC13046037 · DOI 10.1093/rpd/ncaf174
- Study type: in-vitro

## 2. Key Contributions

- First ICRP pregnant-phantom Monte Carlo estimate for a dental bitewing.
- Fetal organ doses ≤0.027 µGy (PSP) and ≤0.0054 µGy (digital).
- Shorter digital-sensor exposure cuts fetal dose ~5×.

## 3. Methodology and Architecture

MCNP6.3 Monte Carlo; ICRP 25-week pregnant mesh phantom; 60 kV RQR60 spectrum, 10^7 photons; virtual 0.25 mm Pb thyroid collar; organ energy deposition converted to absorbed dose (µGy).

## 4. Key Results and Benchmarks

| Fetal organ (25 wk) | Phosphor plate 0.25 s (µGy) | Digital sensor 0.05 s (µGy) |
|---|---|---|
| Brain | 0.027 | 0.0054 |
| Red bone marrow | 0.025 | 0.0050 |
| Bone endosteum | 0.025 | 0.0050 |
| Lymph nodes / muscle | 0.0053 | 0.0011 |
| Breast / lung | 0.0030 | 0.00059 |
| Gonads, bladder, colon | 0 | 0 |

Fetus/mother dose ratio ≈ 0.0015.

## 5. Limitations and Future Work

Single gestational age (25 weeks), single male fetus model, single bitewing geometry; simulation not measurement; patient (not operator) exposure.

## 6. Related Work

- [[radiology/kelaranta-2016-dental-xray-fetal-breast-dose-lead-shield]] — phantom measurement, µGy-range upper bounds, consistent
- [[radiology/gamba-2024-dental-imaging-pregnancy-fetal-dose-sr]] — SR of dental fetal doses
- [[radiology/mainprize-2023-ionizing-radiation-pregnancy-fetal-effects]] — thresholds (≥50 mGy) ~10^6× higher

## 7. Glossary

- Tissue reaction (deterministic effect) — threshold effect (pregnancy loss, malformation, microcephaly, intellectual disability)
- Stochastic effect — probability scales with dose, no threshold assumed (childhood cancer)
- mGy / µGy / nGy — absorbed dose (1 mGy = 1,000 µGy = 1,000,000 nGy); for X-rays 1 mGy ≈ 1 mSv
