---
title: "Comparison of Adhesive Strategies with Different Etching Approaches on the Clinical Performance of Restorations in Non-Carious Cervical Lesions: A Systematic Review and Network Meta-Analysis"
authors: Alain Manuel Chaple Gil, Laura Pereda Vázquez, Meylin Santiesteban Velázquez, Jorge J. Menéndez, George Eliades
year: 2026
doi: 10.3390/jfb17040160
category: [resin-bonding]
pmid: "42042267"
pmcid: "PMC13117247"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13117247/
full_text: true
text_path: /Users/oracleneo/llm-wiki/papers/chaple-gil-2026-adhesive-strategies-etching-nccl-sr-nma.txt
text_filename: chaple-gil-2026-adhesive-strategies-etching-nccl-sr-nma.txt
source_collection: pubmed-text
---

## Why Ingested

The wiki holds two NCCL SR+MAs that disagree on etching strategy for universal adhesives: [[resin-bonding/assis-2023-acid-etching-universal-adhesive-nccl-sr-ma]] (etch-and-rinse better for retention) and [[resin-bonding/doshi-2023-universal-adhesive-nccl-strategy-sr-ma]] (no difference). This 74-RCT network meta-analysis (2026, search to Jan 2026) is the largest and newest NCCL synthesis and adds selective enamel etching and RMGI as nodes, so it can refine that split → [[resin-bonding/chaple-gil-2026-adhesive-strategies-etching-nccl-sr-nma]]

## Three-line Summary

PROSPERO-registered frequentist random-effects network meta-analysis of 74 RCTs in permanent-tooth NCCLs (marginal adaptation network: 57 studies, 28 strategies, 6798 patients; retention-loss network: 61 studies, 33 strategies, 7338 patients), with strategies defined as etching approach x adhesive category x restorative material and RMGI as reference.

Versus RMGI, selective-etch + universal adhesive + nanocomposite reduced marginal adaptation failure, and etch-and-rinse or selective-etch + 1-/2-step universal adhesive + nanocomposite reduced retention loss; some self-etch or non-universal combinations (e.g. self-etch + compomer, non-universal self-etch or etch-and-rinse with certain composite codes (CR_CH, CR_MF)) had significantly higher failure; no incoherence (p = 0.830 and 0.494), CINeMA confidence mostly high.

Selective enamel etching or etch-and-rinse with a universal adhesive and nanocomposite showed the most consistent advantages, but most contrasts overlapped 1, the RMGI anchor rests on few trials, restoration-level analysis ignored clustering, and the comparisons are RMGI-anchored rather than direct E&R-vs-SE contrasts.

## 세줄요약

PROSPERO 등록 빈도론적 랜덤효과 네트워크 메타분석(Network Meta-Analysis, NMA): 영구치 비우식성 치경부 병소(Non-Carious Cervical Lesion, NCCL) RCT 74편 — 변연적합도 네트워크 57편·28개 전략·6798명, 유지 소실 네트워크 61편·33개 전략·7338명; 전략 = 산부식 방식 x 접착제 범주 x 수복재, 기준(reference)은 레진강화형 글라스아이오노머(Resin-Modified Glass Ionomer, RMGI).

RMGI 대비 선택적 산부식(Selective-Etch) + 유니버설 접착제 + 나노 복합레진은 변연적합도 실패 위험을 줄였고, 산부식-세척(Etch-and-Rinse, E&R) 또는 선택적 산부식 + 1·2단계 유니버설 접착제 + 나노 복합레진은 유지 소실 위험을 줄였다; 일부 자가산부식(Self-Etch, SE)·비유니버설 조합(예: SE + 컴포머)은 유의하게 실패 위험이 높았다; 비일관성 없음(p = 0.830, 0.494), CINeMA 확신도 대체로 높음.

선택적 법랑질 산부식 또는 E&R + 유니버설 접착제 + 나노 복합레진이 가장 일관된 우위를 보였으나, 대부분의 대비는 신뢰구간이 1을 포함하고, RMGI 기준 근거가 적으며, 수복물 단위 분석으로 클러스터링 미보정이고, 직접적인 E&R 대 SE 대비가 아니라 RMGI 기준 대비라는 한계가 있다.

## 1. Document Information
- **Journal**: Journal of Functional Biomaterials, 2026;17(4):160 (published 2026-03-25)
- **DOI**: 10.3390/jfb17040160 | **PMID**: 42042267 | **PMCID**: PMC13117247
- **Registration**: PROSPERO CRD420251158473; PRISMA 2020 + PRISMA-NMA
- **Search**: PubMed, Web of Science, Cochrane Library, Embase, Scopus; 25 January 2026; no language or date limits
- **Affiliations**: Universidad Autonoma de Chile; Penn Dental Medicine; Universidad Autonoma del Paraguay; Nova Southeastern University

## 2. Key Contributions
- First network meta-analysis of NCCL restorations that models the full strategy (etching approach x adhesive category x restorative material) instead of pooling adhesive categories.
- Adds selective enamel etching (SelE, SelEse) and RMGI as explicit network nodes; RMGI is the reference comparator.
- 74 RCTs; two connected networks (marginal adaptation, retention loss); CINeMA certainty and global incoherence tests reported.
- Other outcomes (anatomic form, fracture, discoloration, postoperative sensitivity, secondary caries, surface texture) were too sparse or disconnected for network modeling and are only descriptive in the supplement.

## 3. Methodology and Architecture
- Eligibility: RCTs in permanent teeth with at least two etching-based strategies (E&R, SE, selective-etch) or RMGI; trials with extra bioactive or antibacterial co-interventions were excluded to protect transitivity.
- Selection: 831 records, 482 duplicates removed, 349 screened, 88 full texts assessed, 73 + 1 (supplementary retrieval) = 74 included; Cohen's kappa calibration >= 0.80.
- Risk of bias: RoB 2 (mostly low; missing outcome data was the commonest "some concerns").
- Outcomes: clinically unacceptable USPHS/FDI scores (repair or replacement needed) coded as failure; longest available follow-up per study.
- Statistics: netmeta in R, random effects, DerSimonian-Laird, risk ratio (RR) with 95% CI, continuity correction 0.5 for zero cells, P-scores as descriptive ranking; certainty by CINeMA.
- Node coding: etching strategy | adhesive category (1U/2U universal, 1NU/2NU non-universal) | material (e.g. CR_NANO, CR_MF, CMP, RMGI). Brand names not used.

## 4. Key Results and Benchmarks
- Marginal adaptation network: 57 studies, 28 interventions, 6798 patients, 1772 events; 62 of 378 possible pairs directly informed; fully connected.
- Retention-loss network: 61 studies, 33 interventions, 7338 patients, 584 events; 75 of 528 possible pairs directly informed; 32 trials had a zero-event arm.
- Marginal adaptation vs RMGI: SelE|2U|CR_NANO and SelE|1U|CR_NANO significantly lower failure; SE|1U|CMP significantly higher; all others overlapped 1.
- Retention loss vs RMGI: EARd|1U|CR_NANO, EARm|1U|CR_NANO, EAR|1U|CR_NANO and SelEse|1U|CR_NANO significantly lower failure; SE|2NU|CR_CH, EAR|2NU|CR_CH and SE|1NU|CR_MF significantly higher; others overlapped 1.
- Numeric RRs and CIs are shown in forest plots (Figures 3-4) and league tables (Supplement S6); they are not given in the text, so none are reproduced here.
- Global incoherence: marginal adaptation chi2 = 31.478, df 40, p = 0.830; retention loss chi2 = 42.481, df 43, p = 0.494.
- CINeMA: confidence predominantly high; downgrades mainly for imprecision and heterogeneity.
- P-scores (descriptive only): treatment 28 (SelEse|1NU|LYR_SYS) ranked favorably across outcomes.

## 5. Limitations and Future Work
- Only two outcomes yielded connected networks.
- Restoration-level analysis; clustering of several restorations per patient not adjusted, so precision may be overstated.
- Residual heterogeneity (follow-up length, operator setting, protocol); transitivity judged qualitatively.
- RMGI informed by few trials; estimates versus RMGI are sensitive to sparse data.
- Many estimates overlap 1; absolute differences may be small because baseline NCCL failure rates are low (authors' own caution).
- Contrasts are RMGI-anchored; E&R-vs-SE contrasts within universal adhesives are not reported in the main text.
- Future: balanced multi-arm trials of E&R vs SelE vs SE, and trials directly comparing RMGI with universal-adhesive composites.

## 6. Related Work
- [[resin-bonding/assis-2023-acid-etching-universal-adhesive-nccl-sr-ma]] — E&R better than SE for medium-term retention with universal adhesives (the paper cites it as directionally compatible).
- [[resin-bonding/doshi-2023-universal-adhesive-nccl-strategy-sr-ma]] — no TE vs SE difference (the paper cites it as partly convergent, extended by protocol-level contrasts).
- [[resin-bonding/hong-2021-universal-adhesive-etching-modes-sr-ma]] — general-restoration E&R advantage.

## 7. Glossary
- **NMA**: network meta-analysis combining direct and indirect comparisons.
- **SelE / SelEse**: selective enamel etch with a self-etch adhesive on dentin.
- **EAR / EARd / EARm**: etch-and-rinse (etch-and-rinse protocol variants as coded by the authors; the text does not spell out the d/m suffixes).
- **1U/2U, 1NU/2NU**: one-/two-step universal, one-/two-step non-universal adhesive.
- **CR_NANO, CR_MF, CMP, RMGI**: nanocomposite, microfilled composite, compomer, resin-modified glass ionomer. CR_CH is used in the text without a definition.
- **CINeMA**: Confidence in Network Meta-Analysis framework.
- **P-score**: frequentist analogue of SUCRA.
