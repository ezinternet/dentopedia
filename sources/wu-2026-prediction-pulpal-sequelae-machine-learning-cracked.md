---
title: "Prediction of Pulpal Sequelae in Cracked Teeth with Reversible Pulpitis using Machine Learning Models"
authors: Wu Siwen, Dascalu Tudor, Seet Rachel Fangying, Chan Pei Yuan, Yu Na, Hartanto Jeffry, Ibragimov Bulat
year: 2026
doi: 10.1016/j.joen.2026.01.010
category: [cracked-tooth]
source_collection: pubmed-abstract
---

## Why Ingested

Machine learning approaches to endodontic decision-making for cracked teeth are sparse. This paper directly addresses the clinical problem also explored in [[fiyaz-ghani-2025-cracked-teeth-external-splinting-pulp-survival]] (pulp survival after conservative management) and [[gavriil-2025-single-vs-multiple-stage-cracked-teeth-pulp]] (treatment timing and pulp outcomes). Those papers establish the clinical stakes (preserving pulp vitality improves survival); this paper asks whether a predictive model can identify which reversible-pulpitis CTS patients will eventually need RCT — a clinically actionable question with no prior ML answer in the literature.

## One-line Summary

Four machine learning models trained on 593 cracked teeth predict pulp survival in reversible-pulpitis cases; Logistic Regression achieves AUC=0.64 and PPV=0.76, but NPV=0.48 means the model cannot reliably rule out eventual RCT need.

## 한줄요약

가역적 치수염을 가진 균열치 593개에서 머신러닝 4종으로 치수 생존을 예측한 결과, 로지스틱 회귀가 AUC=0.64·PPV=0.76를 달성했으나 NPV=0.48로 RCT 불필요 판정에는 신뢰도가 제한적이었다.

## Document Information

- **Journal**: Journal of Endodontics
- **Volume/Issue**: Vol 52, Issue 5, pp 733–739
- **Published**: 2026-01-20
- **PMID**: 41571087
- **DOI**: 10.1016/j.joen.2026.01.010
- **Source note**: Abstract-only build (no PMC full text available). Deviation logged.

## Key Contributions

1. First study to apply machine learning for predicting pulp survival specifically in cracked teeth with **reversible pulpitis** — the early-stage subset where the clinical decision (monitor vs. RCT) is hardest.
2. Identifies **age** and **presence of preoperative restorations** as the two strongest predictors of pulp non-survival (i.e., eventual RCT need).
3. Demonstrates that logistic regression is competitive with or superior to more complex models (Gaussian Processes, Random Forests, Gradient Boosting) on this dataset, suggesting the signal is modest and linear.
4. PPV of 0.74–0.77 across all models: clinically useful for **identifying who will need RCT**; NPV of 0.45–0.48: insufficient to confidently rule it out.

## Methodology

- **Dataset**: 569 patients, 593 cracked teeth; binary outcome = pulp survival (no RCT required)
- **Models tested**: Logistic Regression (LR), Gaussian Processes (GP), Random Forests (RF), Gradient Boosting (GB)
- **Validation**: 10-fold stratified nested cross-validation — outer loop = performance estimation, inner loop = hyperparameter optimization
- **Threshold tuning**: Classification thresholds tuned for probabilistic models
- **Input features**: Age, gender, tooth type, preoperative restorative material
- **Metrics reported**: AUC, F1-score, sensitivity, specificity, PPV, NPV

## Key Results

| Model | AUC | F1 | PPV | NPV |
|---|---|---|---|---|
| Logistic Regression | **0.64** | **0.60** | 0.76 | 0.48 |
| Gaussian Processes | ~0.62 | ~0.58 | 0.74–0.77 | 0.45–0.47 |
| Random Forests | ~0.62 | ~0.58 | 0.74–0.77 | 0.45–0.47 |
| Gradient Boosting | ~0.62 | ~0.58 | 0.74–0.77 | 0.45–0.47 |

- **Overall predictive accuracy**: 74–77% across models
- **Significant predictors**: Older age → higher likelihood of requiring RCT; presence of existing restoration → higher likelihood of requiring RCT
- **Non-significant or weaker**: Gender, tooth type (not highlighted as main predictors)

## Limitations

- Retrospective dataset; potential selection bias in which teeth were followed
- Limited feature set — no crack depth, crack length, percussion sensitivity score, or CBCT data included
- AUC of 0.64 indicates modest discrimination only; well above chance but clinically insufficient as a standalone tool
- NPV of 0.48 is too low to use the model for ruling out RCT need (close to a coin flip for negative predictions)
- External validation not reported — generalizability to other clinical settings unknown
- Abstract-only build: full methods detail (exact sample split, class balance) not available

## Related Work

- [[fiyaz-ghani-2025-cracked-teeth-external-splinting-pulp-survival]] — pulp survival with splinting; provides conservative management context this model could complement
- [[gavriil-2025-single-vs-multiple-stage-cracked-teeth-pulp]] — pulp outcomes by treatment stage; similar outcome variable (pulp survival/RCT need)
- [[zhang-2024-cracked-teeth-treatment-outcomes-sr-ma]] — systematic review of CTS treatment outcomes; broader context for survival rates

## Glossary

- **AUC (Area Under the Curve)**: Discrimination ability of the classifier; 0.5 = chance, 1.0 = perfect
- **PPV (Positive Predictive Value)**: Of patients predicted to need RCT, the fraction that actually does
- **NPV (Negative Predictive Value)**: Of patients predicted NOT to need RCT, the fraction that actually does not
- **Reversible pulpitis**: Pulpal inflammation where vitality is maintainable if the etiologic factor is removed
- **10-fold stratified nested CV**: Two-loop cross-validation ensuring class-balanced folds; outer = test, inner = hyperparameter search
