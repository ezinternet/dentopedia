---
title: "Denosumab Dosage and Tooth Extraction Predict MRONJ in Breast Cancer with Bone Metastases"
authors: Suguru Yokoo, Shinichiro Kubo, Daisuke Yamamoto, Masahiko Ikeda, Tetsumasa Yamashita, Kumiko Yoshikawa, Hiroshi Mese, Sakiko Ohara
year: 2025
date: 2025-07-04
doi: 10.3390/cancers17132242
source: yokoo-2025-denosumab-mronj-breast-cancer-bone.md
category: [drug/mronj]
confidence: retrospective
pdf_path: /Users/oracleneo/llm-wiki/papers/yokoo-2025-denosumab-mronj-breast-cancer-bone.pdf
pdf_filename: yokoo-2025-denosumab-mronj-breast-cancer-bone.pdf
source_collection: external
tags: [mronj, denosumab, breast-cancer, bone-metastasis, cumulative-dose, tooth-extraction, roc-threshold]
---

## Three-line Summary

Retrospective cohort of 324 breast cancer patients with bone metastases on denosumab 120 mg q4w (Fukuyama City Hospital, Japan, 2012–2024), evaluating MRONJ incidence and predictors with ROC analysis.

MRONJ developed in 31.2% (101/324); ROC analysis identified ≥32 cumulative doses as the optimal threshold (AUC 0.83, sensitivity 71.3%, specificity 81.6%), and multivariate regression confirmed cumulative dose (OR 1.047/dose) and tooth extraction history (OR 4.40) as the only independent predictors.

Enhanced MRONJ surveillance is warranted from approximately 32 months of monthly Xgeva therapy, and pre-treatment dental extraction should be completed before initiation when feasible.

## 세줄요약

유방암 골전이 환자 324명에게 denosumab 120 mg 4주 간격 투여 후 MRONJ 발생 및 예측 인자를 ROC 분석으로 평가한 후향 코호트(후쿠야마 시립병원, 2012–2024).

MRONJ 발생률 31.2%(101/324); ROC 분석으로 누적 32회 투여가 최적 임계값(AUC 0.83, 민감도 71.3%, 특이도 81.6%)이었으며, 다변량 분석에서 누적 투여 횟수(OR 1.047/회)와 발치 기왕력(OR 4.40)만이 독립적 예측인자였다.

Xgeva 32개월 투여 시점부터 강화 모니터링이 권장되며, 치료 전 발치가 가능하다면 사전에 완료해야 한다.

## Summary
Retrospective cohort of 324 female patients with breast cancer and bone metastases receiving Xgeva®/Ranmark® (denosumab 120 mg SC q4w) at Fukuyama City Hospital (May 2012 – August 2024). MRONJ developed in 31.2% (101/324). ROC analysis identified 32 cumulative doses as the optimal threshold (AUC 0.83; sensitivity 71.3%, specificity 81.6%). Multivariate analysis confirmed cumulative dose (OR 1.047/dose) and tooth extraction history (OR 4.40) as the only independent MRONJ predictors. This is the first study to use ROC analysis to define a specific cumulative dose cutoff for denosumab-MRONJ in breast cancer.

## Key Contributions
- ROC-derived threshold: **≥32 cumulative doses** (≈32 months) substantially elevates MRONJ risk (AUC 0.83)
- Each additional dose independently adds **4.7%** to MRONJ odds
- Tooth extraction history: **OR 4.40** (2.23–8.71)
- Diabetes, hormone therapy, poor oral hygiene not significant in multivariate analysis
- High overall MRONJ rate (31.2%) reflects oncology dose; not generalizable to osteoporosis-dose denosumab

## Methodology
- **Setting**: Multidisciplinary (breast surgery + dental/oral surgery), all patients received pre-treatment dental evaluation
- **Exclusions**: No comprehensive dental evaluation; ONJ before denosumab
- **Drug**: Denosumab 120 mg SC q4w (oncology dose for SRE prevention)
- **Statistical approach**: Logistic regression + ROC analysis + bootstrap validation (n=1000 iterations)

## Results

### Incidence by Cumulative Dose
| Dose range | MRONJ rate |
|---|---|
| ≤10 doses | 19.6% (21/107) |
| 11–30 doses | 37.5% (39/104) |
| >30 doses | 36.0% (41/114) |
| **Overall** | **31.2% (101/324)** |

### ROC Analysis
| Parameter | Value |
|---|---|
| AUC | 0.83 (95% CI 0.78–0.88) |
| Optimal cutoff | **32 doses** |
| Sensitivity | 71.3% |
| Specificity | 81.6% |
| PPV | 63.7% |
| NPV | 86.3% |
| Bootstrap mean AUC | 0.83 ± 0.02 |
| Bootstrap mean threshold | 27.8 ± 5.7 doses |

### Multivariate Logistic Regression
| Variable | OR | 95% CI | p |
|---|---|---|---|
| Cumulative doses | 1.047 | 1.033–1.061 | <0.001 |
| Tooth extraction history | 4.402 | 2.225–8.711 | <0.001 |
| Diabetes mellitus | 1.500 | 0.834–2.697 | 0.176 (NS) |
| Hormone therapy | 1.279 | 0.639–2.562 | 0.487 (NS) |
| Poor oral hygiene | 1.517 | 0.792–2.907 | 0.209 (NS) |

## Clinical Implications
- At 32 cumulative doses (~32 months of monthly Xgeva®): heightened surveillance recommended
- Tooth extraction before or during therapy is a strong modifiable risk factor
- Prior literature: MRONJ 0.5–2.1% (year 1) → 1.3–3.2% (year 3); this study's 31.2% likely reflects referral bias and long follow-up (up to 2024 for treatments started 2012)

## Related Papers
- [[drug/ruggiero-2022-aaoms-mronj-position-paper-update]] — MRONJ definition and staging
- [[drug/jung-2022-denosumab-mronj-osteoporosis-5year]] — osteoporosis-dose denosumab MRONJ (4.1%)
- [[drug/li-2024-antiresorptive-implants-mronj-sr]] — implant failure from ARD-induced MRONJ
- [[drug/baghalipour-2025-mronj-prevention-management-review]] — MRONJ management
