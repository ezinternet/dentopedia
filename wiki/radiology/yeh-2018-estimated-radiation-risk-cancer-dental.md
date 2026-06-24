---
title: "Estimated radiation risk of cancer from dental cone-beam computed tomography imaging in orthodontics patients"
authors: Jih-Kuei Yeh, Chia-Hui Chen
year: 2018
date: 2018-08-03
doi: 10.1186/s12903-018-0592-5
source: yeh-2018-estimated-radiation-risk-cancer-dental.md
category: [radiology]
confidence: in-vitro
source_collection: pubmed-text
full_text: true
pmid: "30075771"
pmcid: "PMC6091080"
text_path: /Users/oracleneo/llm-wiki/papers/yeh-2018-estimated-radiation-risk-cancer-dental.txt
text_filename: yeh-2018-estimated-radiation-risk-cancer-dental.txt
tags: [cbct, effective-dose, cancer-risk, orthodontics, radiation-safety]
relations:
  - type: extends
    target: ozaki-2021-cbct-effective-dose-monte-carlo-simulation
---

## One-line Summary

Monte Carlo (PCXMC 2.0 Rotation) + BEIR-VII in-silico study on an i-CAT dental CBCT (16x13 cm FOV, 120 kV, 18.54 mAs): total effective dose ~31 uSv at beam centerline, salivary glands the dominant organ; lifetime cancer REID is ~2x higher in 10-year-olds than 30-year-olds and highest for female breast cancer.

## 한줄요약

i-CAT 치과 콘빔CT(CBCT) 몬테카를로(PCXMC 2.0 Rotation)+BEIR-VII 전산 선량·위험 추정 — 빔 중심선 유효선량 약 31 uSv, 침샘이 최대 기여 장기, 방사선 유발 사망위험(REID)은 10세가 30세의 약 2배이며 여아 유방암이 가장 민감.

## Summary

This in-silico computational study takes dental CBCT dosimetry one step beyond the dose number: it converts Monte Carlo organ doses into a **lifetime cancer-risk estimate**. Using PCXMC 2.0 Rotation (STUK, Finland) on age/gender-adjustable ICRP phantoms, the authors computed organ and effective doses for an i-CAT scanner (120 kV, 18.54 mAs, 16x13 cm FOV), then fed the organ doses into the **BEIR-VII** linear-no-threshold risk model to derive the **risk of exposure-induced death (REID)** by age and gender.

The clinical message is age- and child-centric: REID for all cancers in 10-year-olds is roughly **double** that in 30-year-olds and plateaus after age ~30, with **female breast cancer** the most age-sensitive radiogenic cancer. Because orthodontic CBCT is disproportionately performed on growing children, the paper supplies the quantitative justification for restricting and protocol-optimizing pediatric CBCT. It complements pure effective-dose Monte Carlo work (e.g. Ozaki 2021) by adding the stochastic-risk / justification dimension.

## Key Contributions

- First couples **PCXMC Monte Carlo organ doses** with **BEIR-VII REID** for dental CBCT to express exposure as lifetime cancer-death risk, not just dose.
- Quantifies the **~2x child-vs-adult** risk gradient (10 vs 30 years) and the **female > male** overall risk.
- Identifies **salivary glands** (beam centerline) and **thyroid** (across heights) as dominant organs under ICRP 103 weighting — the organs to shield.
- Flags **female breast cancer** as the most age-sensitive radiogenic cancer (10-20 years).

## Methodology

- **Scanner/protocol**: i-CAT; 120 kV, 18.54 mAs, 16x13 cm FOV, 0.4 mm voxel.
- **Dosimetry**: PCXMC 2.0 Rotation Monte Carlo on pediatric/adult phantoms; 29 ICRP organs; effective dose with ICRP 103 weighting. Geometry: 360° rotation, 14 mm Al filter, beam 16x8 cm, Xref 0 / Yref -5 cm, Zref 75.0-92.5 cm (centerline 83.0 cm), FRD 52 cm.
- **Risk**: BEIR-VII, LNT linear-quadratic; REID by age/gender/Asian mortality; cancers = leukemia, colon, liver, lung, stomach, breast (female), other. t-test, SPSS 19.0.
- No human or animal subjects — simulation only (hence `confidence: in-vitro`).

## Results

- **Total effective dose**: 30.99 uSv at beam centerline.
- **Organ dose, Zref 83 cm**: salivary glands 738.29 uGy (max), brain 269.58 uGy. Range across heights: thyroid 928.77 uGy (Zref 75) to esophagus 0.5 uGy (Zref 92.5).
- **Effective-dose peaks**: thyroid 37.50 uSv (Zref 75); salivary glands 7.84 uSv (Zref 80); brain 5.27 uSv (Zref 90); esophagus 0.85 uSv (Zref 75).
- **REID, all cancers**: 10-year-olds 22.6 x 10^-5 (F) / 19 x 10^-5 (M); 30-year-olds 10.4 x 10^-5 (F) / 8.88 x 10^-5 (M). Decreases with age (p=0.01 F; p<0.0001 M), higher in females (p=0.03), plateaus after ~30.
- **Per cancer**: leukemia/colon/liver higher in males; lung/stomach/other higher in females; female breast cancer most age-sensitive, peak at age 10.
- **Limitations**: simulation without measured validation; BEIR-VII derived from atomic-bomb survivors (different population; ICRP warns against effective dose for individual risk); FOV-dose relationship not modeled.

## Related Papers

- [[radiology/ozaki-2021-cbct-effective-dose-monte-carlo-simulation]] — extends: this paper layers BEIR-VII stochastic cancer-risk (REID) estimation on top of the same Monte-Carlo CBCT effective-dose approach, adding the justification dimension to plain dosimetry.
