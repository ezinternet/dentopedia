---
title: "Effects of attachment type and number of dental implants supporting mandibular overdenture on peri-implant health: A systematic review and network meta-analysis"
authors: Ye Bi, Taghrid Aldhohrah, Mubarak Ahmed Mashrah, Yucheng Su, Zhe Yang, Xueqi Guo, Linhu Ge, Liping Wang
year: 2022
doi: 10.2186/jpr.JPR_D_21_00073
category: [complete-denture]
pdf_path: /Users/oracleneo/llm-wiki/papers/bi-2022-attachment-type-implant-number-overdenture.pdf
pdf_filename: bi-2022-attachment-type-implant-number-overdenture.pdf
source_collection: external
---

## Why Ingested

This network meta-analysis directly addresses the clinical question of which combination of implant number and attachment system (ball, bar, locator, telescopic, magnet) yields the best peri-implant health in mandibular overdentures — a topic not yet covered in the wiki. Extends [[complete-denture/alhajj-2017-occlusal-vertical-dimension-complete-denture-review]] by adding the implant-supported overdenture arm of complete denture rehabilitation.

## One-line Summary

Bayesian network meta-analysis (28 studies, n=1166, 2666 implants) found that 4-implant bar and telescopic ODs showed significantly less marginal bone loss than 2-implant locator, but no clear superiority emerged across most attachment-implant combinations for peri-implant health.

## 한줄요약

28개 연구를 포함한 베이지안 네트워크 메타분석에서 4임플란트+바/텔레스코픽 피개의치가 2임플란트+로케이터보다 유의하게 낮은 변연골 소실을 보였으나, 대부분의 임플란트 수-어태치먼트 조합 간에는 치주 건강 결과에서 명확한 우열이 없었다.

## 1. Document Information

- **Journal**: Journal of Prosthodontic Research (J Prosthodont Res)
- **Volume/Issue**: 2022; 66(3): 357–373
- **Received**: 25 March 2021
- **Accepted**: 4 June 2021
- **Available online**: 30 September 2021
- **DOI**: 10.2186/jpr.JPR_D_21_00073
- **Study type**: Systematic review + Bayesian network meta-analysis
- **PROSPERO registered**: Yes
- **Corresponding author**: Liping Wang, Guangzhou Medical University

## 2. Key Contributions

1. First NMA to compare **all combinations** of implant number (1–4) × attachment type (ball, bar, locator, telescopic, magnet) simultaneously for peri-implant health outcomes.
2. Establishes that **4-implant bar and 4-implant telescopic** show significantly lower MBL than **2-implant locator** — the only statistically significant MBL finding.
3. Overall pooled implant survival rate of **98.4%** across all interventions; individual intervention ISRs ranged from 88.9% (1 ball + immediate loading) to 100%.
4. Rank probability analysis: **4 bar and 4 telescopic** = lowest MBL; **2 magnet and 2 bar** = highest plaque index; **4 locator** = least PPD.
5. No statistically significant differences in PPD, bleeding index, or gingival index among the 12 intervention groups.

## 3. Methodology and Architecture

- **Search**: Medline/PubMed, Embase, Cochrane Library, Scopus; inception to October 2020
- **Included studies**: 28 (19 RCTs, 6 retrospective, 3 prospective)
- **Participants**: 1166 patients, 2666 implants; mean age 52.3–72.5 years; follow-up 12 months–10 years
- **Interventions (12 nodes)**: 2 bar, 3 bar, 4 bar, 1 ball, 2 ball, 3 ball, 1 locator, 2 locator, 4 locator, 2 telescopic, 4 telescopic, 2 magnet
- **Outcomes**: MBL (primary), PPD, plaque index (PI), bleeding index (BI), gingival index (GI), implant survival rate (ISR)
- **Statistical method**: Bayesian NMA using GeMTC package in R; outputs = weighted mean difference (WMD) + 95% credible intervals (CrI); node-splitting for inconsistency; rank probability test
- **Risk of bias**: 19 studies low risk, 9 moderate risk (MAOSE/STROBE/PRISMA criteria)
- **Pairwise meta-analysis**: Also performed using Comprehensive Meta-Analysis software (CMA, Biostat Inc.)

## 4. Key Results and Benchmarks

### Implant Survival Rate
- Overall pooled ISR: **98.4%** (43/2666 implants failed)
- Best ISR: 4 bar + delayed loading, 3 bar, 2 locator + delayed, 4 telescopic — all **100%**
- Lowest ISR: 1 ball + immediate loading — **88.9%**
- 2 ball (all loading protocols combined): ~92.9–94.4%

### Marginal Bone Loss (MBL)
- **4 bar** and **4 telescopic** showed statistically significantly lower MBL than **2 locator**
- All other pairwise MBL comparisons: **not significant** (P > 0.05)
- 2 bar vs 2 ball (pairwise): MD 0.081 mm, 95%CI −0.152 to 0.314 (NS)
- 2 ball vs 2 telescopic (pairwise): MD −0.036 mm, 95%CI −0.173 to 0.102 (NS)

### Periodontal Probing Depth (PPD)
- No statistically significant difference among groups
- Rank probability: **4 locator** had the lowest (best) PPD

### Plaque Index / Bleeding Index
- **2 magnet** and **2 bar** ranked highest (worst) plaque accumulation
- No statistically significant differences for BI, GI

### Network Inconsistency
- Node-splitting analysis showed no significant inconsistency between direct and indirect evidence

## 5. Limitations and Future Work

1. Heterogeneity in implant systems, loading protocols, and follow-up durations across included studies
2. Only one study with 3-implant design — limits generalizability of that node
3. Study designs varied (RCT, retrospective, prospective) — quality differences acknowledged
4. Mostly short-to-medium follow-up; long-term (>10 years) data sparse
5. Publication bias could not be fully excluded despite comparison-adjusted funnel plots
6. Outcomes limited to peri-implant health; patient-reported outcomes (QoL, satisfaction) not synthesized
7. Authors call for future high-quality RCTs directly comparing all 12 intervention combinations

## 6. Related Work

- York Consensus Statement (2002): 2-implant mandibular OD as standard of care minimum
- Earlier pairwise MAs comparing 2–3 attachment types only — this NMA overcomes their limitation
- Aldhohrah T et al. (2021): NMA on patient satisfaction with mandibular ODs (companion paper)

## 7. Glossary

- **OD**: Overdenture — removable prosthesis supported by dental implants
- **OAS**: Overdenture attachment system (ball, bar, locator, telescopic, magnet)
- **MBL**: Marginal bone loss — change in crestal bone height around implant
- **PPD**: Pocket probing depth — sulcus depth around implant
- **PI**: Plaque index (Mombelli)
- **BI**: Bleeding index (Mombelli)
- **GI**: Gingival index
- **ISR**: Implant survival rate
- **NMA**: Network meta-analysis — indirect comparison across multiple interventions
- **WMD**: Weighted mean difference
- **CrI**: Credible interval (Bayesian equivalent of confidence interval)
- **GeMTC**: R package for Bayesian NMA using JAGS
- **PRISMA**: Preferred Reporting Items for Systematic Reviews and Meta-Analyses
- **PROSPERO**: International register of systematic reviews
