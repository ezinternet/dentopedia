---
title: "Effect of Screw Coatings (GapSeal Silicone vs PTFE Tape) on Preload and Removal Torque of Implant-Abutment Screws: A Laboratory Study"
authors: Coelho et al.
year: 2024
doi: 10.3390/ma17061414
pmid: "38541567"
pmcid: "PMC10972164"
category: [prosthetic-materials]
source_collection: pubmed-text
full_text: true
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10972164/
text_path: /Users/oracleneo/llm-wiki/papers/coelho-2024-preload-removal-torque-screw-coatings-laboratory.txt
text_filename: coelho-2024-preload-removal-torque-screw-coatings-laboratory.txt
---

## Why Ingested

임플란트 보철 나사 풀림은 가장 흔한 기계적 합병증 중 하나. 기존 wiki에 [[prosthetic-materials/varvara-2020-retightening-preload-loss-abutment-screws-invitro]]가 있어 재조임 시간과 프리로드 손실 관계를 다루지만, GapSeal·PTFE 테이프 코팅이 프리로드 및 제거 토크에 미치는 직접 비교 근거가 부재했음. 본 연구는 임상에서 흔히 사용되는 두 코팅 소재를 직접 비교해 GapSeal 권장·PTFE 회피 근거를 제공.

## One-line Summary

In vitro study (n=45, 3 groups) found PTFE tape significantly reduced implant-abutment screw preload while GapSeal silicone gel maintained preload and increased removal torque, supporting GapSeal use over PTFE.

## 한줄요약

체외 연구(n=45, 3군)에서 PTFE 테이프는 임플란트 지대주 나사 프리로드를 유의하게 감소시킨 반면, GapSeal 실리콘 젤은 프리로드를 유지하면서 제거 토크를 증가시켜 GapSeal 사용을 지지함.

## 1. Document Information

- **Journal**: Materials (Basel) 2024;17(6):1414
- **DOI**: 10.3390/ma17061414
- **PMID**: 38541567 / **PMCID**: PMC10972164
- **Study Type**: In vitro laboratory study
- **Setting**: Laboratory of Investigation in Oral Rehabilitation and Prosthodontics, IUCS-CESPU, Portugal

## 2. Key Contributions

1. First direct comparison of GapSeal (silicone sealing gel) vs PTFE tape on both preload AND removal torque value (RTV) in the same experiment.
2. PTFE tape acts as a lubricant — reduces preload (mean 28.88 vs control 30.41 N·cm, p<0.05), consistent with its known tribological properties.
3. GapSeal does NOT reduce preload (no significant difference from control) but significantly INCREASES RTV (mean 28.67 vs control 26.59 N·cm, p<0.05) — the sealing gel creates additional mechanical resistance to unscrewing.
4. Strong positive correlation between preload and RTV confirmed across groups.
5. Clinical recommendation: use GapSeal to reduce loosening risk; avoid PTFE tape as it compromises preload.

## 3. Methodology and Architecture

- **Sample**: 45 external hexagonal implant-abutment-screw complexes (DIUIMPLANT, Korea; implant 4.0×11.5 mm; abutment 1mm cuff/7mm length; Ti screw 1.7 Torx)
- **Groups** (n=15 each):
  - GC (Control): no coating
  - GG (GapSeal): silicone sealing gel injected into implant internal compartment; GapSeal® Hager & Werken — silicone matrix + thymol, viscous, never hardens
  - GP (PTFE): PTFE tape wound twice around screw shaft, tail cut at bottom
- **Tightening torque**: 30 N·cm (manufacturer-recommended) via calibrated digital torque meter (iSD900)
- **Preload measurement**: Centor Touch Star TH force gauge (Andilog), 1000 Hz acquisition
- **RTV measurement**: loosening torque recorded immediately after tightening
- **Statistics**: ANOVA, ANCOVA (RTV adjusted for preload), Tukey post-hoc, effect size η², Shapiro-Wilk normality, Levene homogeneity; R v4.3.0

## 4. Key Results and Benchmarks

| Group | Preload (N·cm) | RTV (N·cm) | Adj. RTV (ANCOVA) |
|---|---|---|---|
| GC (control) | 30.41 ± 1.04 | 26.59 ± 1.25 | 26.40 |
| GG (GapSeal) | 30.22 ± ~1.0 (NS) | 28.67 ± 1.47* | 28.70* |
| GP (PTFE) | 28.88 ± 1.07* | 16.15 ± 2.89* | 17.20* |

*p<0.05 vs control

- Preload ANOVA: F=6.45, p=0.004, η²=0.23 (large effect); R²=19.86%
- RTV ANOVA: F=167.00, p<0.001, η²=0.83 (large effect); R²=88.30%
- ANCOVA (RTV adj for preload): F=177.04, p<0.001, η²p=0.90; preload trend p=0.068 (moderate effect η²p=0.08)
- Key: all three groups differed significantly in RTV (Tukey p<0.05)

## 5. Limitations and Future Work

- In vitro only — no chewing simulation, cyclic loading, or biological aging
- Single implant system (external hex, DIUIMPLANT) — may not generalize to internal connections
- Only one GapSeal lot and one PTFE tape brand tested
- No assessment of biocompatibility changes after coating application (GapSeal is marketed as biocompatible; PTFE also generally biocompatible)
- Authors call for in vivo / clinical studies to confirm

## 6. Related Work

- Siamos et al.: higher initial torque → higher RTV (confirmed here)
- Prior PTFE studies showed favorable anti-loosening results — this study contradicts (preload reduction with PTFE)
- GapSeal preliminary results in literature were contradictory — this study favors GapSeal
- Gold/tungsten carbide/DLC manufacturer coatings: shown to increase preload via friction reduction (different mechanism from PTFE)

## 7. Glossary

- **Preload**: clamping force generated in implant-abutment screw when torque is applied; key to joint stability
- **RTV (Removal Torque Value)**: torque required to loosen a tightened screw; proxy for resistance to loosening
- **Settling effect**: 2–10% preload loss due to microrough surface asperities flattening after initial tightening
- **GapSeal**: silicone + thymol sealing gel; viscous, never hardens; used to seal implant internal spaces against bacteria
- **PTFE (polytetrafluoroethylene)**: Teflon tape; hydrophobic, chemically inert, biocompatible; acts as lubricant when wrapped around screw
- **ANCOVA**: analysis of covariance — compares RTV between groups while controlling for preload differences
