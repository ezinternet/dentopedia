---
title: "Estimated radiation risk of cancer from dental cone-beam computed tomography imaging in orthodontics patients"
authors: Jih-Kuei Yeh, Chia-Hui Chen
year: 2018
doi: 10.1186/s12903-018-0592-5
category: [radiology]
source_collection: pubmed-text
full_text: true
pmid: "30075771"
pmcid: "PMC6091080"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6091080/
text_path: /Users/oracleneo/llm-wiki/papers/yeh-2018-estimated-radiation-risk-cancer-dental.txt
text_filename: yeh-2018-estimated-radiation-risk-cancer-dental.txt
---

## Why Ingested

Existing [[radiology/ozaki-2021-cbct-effective-dose-monte-carlo-simulation]] quantifies CBCT organ/effective dose via Monte Carlo but stops at the dose number. This paper adds the **stochastic cancer-risk / justification layer** on top of that effective-dose data: it converts PCXMC Monte Carlo organ doses into BEIR-VII lifetime risk-of-exposure-induced-death (REID), and shows the risk is ~2x higher in 10-year-olds than 30-year-olds — the quantitative basis for the "justify CBCT especially in pediatric orthodontic patients" argument.

## One-line Summary

Monte Carlo (PCXMC 2.0 Rotation) + BEIR-VII in-silico dosimetry study on an i-CAT dental CBCT (16x13 cm FOV, 120 kV): total effective dose ~31 uSv at beam centerline; salivary glands the dominant organ; REID for all cancers ~2x higher in 10-year-olds (22.6 vs 10.4 x 10^-5 female) than 30-year-olds, highest for female breast cancer.

## 한줄요약

i-CAT 치과 콘빔CT(CBCT)에 대한 몬테카를로(PCXMC 2.0 Rotation)+BEIR-VII 전산 선량·위험 추정 연구 — 빔 중심선 유효선량 약 31 uSv, 침샘이 최대 기여 장기, 방사선 유발 사망위험(REID)은 10세가 30세의 약 2배(여성 22.6 vs 10.4 x 10^-5)이고 여아 유방암이 가장 민감.

## 1. Document Information

- **Title**: Estimated radiation risk of cancer from dental cone-beam computed tomography imaging in orthodontics patients
- **Authors**: Jih-Kuei Yeh (Division of Family Medicine, Kaohsiung Municipal United Hospital, Taiwan); Chia-Hui Chen (Dept. of Medical Imaging and Radiological Science, Central Taiwan University of Science and Technology; College of Photonics, National Chiao Tung University, Taiwan)
- **Journal**: BMC Oral Health 2018;18(1):131
- **DOI**: 10.1186/s12903-018-0592-5
- **PMID**: 30075771 / **PMCID**: PMC6091080
- **Published**: 2018-08-03
- **Study type**: In-silico computational dosimetry + radiation-risk estimation (Monte Carlo simulation; no human/animal subjects) → `confidence: in-vitro`

## 2. Key Contributions

1. Couples **organ/effective-dose Monte Carlo** (PCXMC 2.0 Rotation) with **BEIR-VII LNT cancer-risk modeling** to express dental CBCT exposure as lifetime **REID (risk of exposure-induced death)**, not just dose — a justification/risk layer over plain dosimetry.
2. Quantifies the **age dependence** of risk: REID for all cancers in 10-year-olds is roughly double that in 30-year-olds (22.6 vs 10.4 x 10^-5 female; 19 vs 8.88 x 10^-5 male), then plateaus after age ~30.
3. Identifies **salivary glands** as the dominant organ-dose/effective-dose contributor at the beam centerline (Zref 83 cm) and **thyroid** as the maximum across all simulated heights — flagging organs warranting protection under ICRP 103.
4. Shows **female > male** REID overall and **female breast cancer** as the most age-sensitive radiogenic cancer.

## 3. Methodology and Architecture

- **Scanner / protocol**: i-CAT (Imaging Sciences International, PA, USA); 120 kV, 18.54 mAs, 16x13 cm FOV, 0.4 mm voxel.
- **Dose calculation**: PCXMC 2.0 Rotation (STUK, Finland) Monte Carlo on adjustable-size pediatric/adult phantoms; 29 organs/tissues per ICRP dosimetry; effective dose with ICRP 103 tissue weighting factors. Geometry: 360° rotation, 14 mm Al filter, beam 16 cm wide x 8 cm high, Xref 0 / Yref -5 cm (to cover oral cavity), Zref varied 75.0-92.5 cm (neck-to-head), centerline Zref 83.0 cm, FRD 52 cm.
- **Risk estimation**: BEIR-VII report model, linear no-threshold (LNT), linear-quadratic dose response; REID computed in PCXMC by age, gender, and Asian mortality statistics; modeled cancers = leukemia, colon, liver, lung, stomach, breast (female only), and "other."
- **Statistics**: t-test, SPSS 19.0.

## 4. Key Results and Benchmarks

- **Total effective dose**: 30.99 uSv at the x-ray beam centerline.
- **Organ dose (Zref 83 cm)**: salivary glands 738.29 uGy (largest), brain 269.58 uGy (second). Across all Zref: range 928.77 uGy (thyroid, Zref 75) down to 0.5 uGy (esophagus, Zref 92.5).
- **Effective dose peaks (by height)**: thyroid 37.50 uSv (Zref 75); salivary glands 7.84 uSv (Zref 80); brain 5.27 uSv (Zref 90); esophagus 0.85 uSv (Zref 75).
- **REID, all cancers**: 10-year-olds 22.6 x 10^-5 (female) / 19 x 10^-5 (male); 30-year-olds 10.4 x 10^-5 (female) / 8.88 x 10^-5 (male) — ~2x higher in children; risk decreases with age (p=0.01 female, p<0.0001 male) and is higher in females overall (p=0.03), plateauing after ~30.
- **Per-cancer pattern**: leukemia/colon/liver higher in males; lung/stomach/other higher in females; female breast cancer most age-sensitive, monotonically decreasing with age, highest at 10 years.

## 5. Limitations and Future Work

- Pure simulation — no measured (TLD/phantom) validation in this study; relies on PCXMC modeling.
- BEIR-VII risk model derived from atomic-bomb survivor epidemiology, a population very different from dental CBCT patients; ICRP itself warns against using effective dose for individual risk estimation.
- Dose-FOV relationship not modeled — different FOV/units cover different radiosensitive organs and would change results.
- Authors note lead-apron use to shield brain/thyroid from primary and scatter beam.

## 6. Related Work

- Koivisto J et al. — same PCXMC approach, different CBCT scanner; thyroid dominant at Zref 74, salivary glands at Zref 83; this study found similar curve shape with lower effective doses (attributed to larger FOV, higher kV, lower mAs).
- Pauwels et al. — TLD-based CBCT cancer-risk estimate (SCANORA 3D, NewTom 9000): probability 2.7 x 10^-6 (age>60) to 9.8 x 10^-6 (age 8-11), avg 6.0 x 10^-6; method differs from this organ-dose-based REID approach.
- Roberts JA et al. — CBCT delivers 5-16x the dose of a panoramic radiograph.
- Al Najjar A et al. — children receive higher head/neck equivalent doses than adults at equivalent CBCT settings.

## 7. Glossary

- **CBCT**: Cone-Beam Computed Tomography — 3D dental imaging from a single rotational X-ray sequence.
- **PCXMC 2.0 Rotation**: Personal-computer Monte Carlo dosimetry software (STUK, Finland) with a rotational add-on for cone-beam geometries.
- **BEIR VII**: Biologic Effects of Ionizing Radiation VII — US National Academies report providing cancer-risk models for low-dose radiation.
- **REID**: Risk of Exposure-Induced Death — lifetime probability of dying from a radiation-induced cancer attributable to a given exposure.
- **LNT**: Linear No-Threshold model — assumes any radiation dose carries proportional cancer risk with no safe threshold.
- **ICRP 103**: 2007 International Commission on Radiological Protection recommendations defining tissue weighting factors for effective dose.
- **Zref**: Vertical reference coordinate of the X-ray beam centerline within the phantom (cm).
- **Effective dose (uSv)**: Tissue-weighted whole-body-equivalent dose reflecting stochastic risk.
