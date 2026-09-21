---
title: "Prediction of Pulpal Sequelae in Cracked Teeth with Reversible Pulpitis using Machine Learning Models"
authors: Wu Siwen, Dascalu Tudor, Seet Rachel Fangying, Chan Pei Yuan, Yu Na, Hartanto Jeffry, Ibragimov Bulat
year: 2026
date: 2026-01-20
doi: 10.1016/j.joen.2026.01.010
source: sources/wu-2026-prediction-pulpal-sequelae-machine-learning-cracked.md
category: [cracked-tooth]
evidence_level: retrospective
source_collection: pubmed-abstract
tags: [cracked-tooth, machine-learning, pulp-survival, reversible-pulpitis, predictive-model, clinical-decision-support]
relations:
  - target: fiyaz-ghani-2025-cracked-teeth-external-splinting-pulp-survival
    type: reinforces
    note: Both address pulp survival in conservatively managed CTS; this ML model could complement splinting decision protocols
  - target: gavriil-2025-single-vs-multiple-stage-cracked-teeth-pulp
    type: related
    note: Shares outcome variable (pulp survival / RCT need) in cracked teeth
  - target: zhang-2024-cracked-teeth-treatment-outcomes-sr-ma
    type: related
    note: SR/MA of CTS treatment outcomes; broader context for survival base rates used in model training
---

## Three-line Summary

Four machine learning models were trained on 593 cracked teeth with reversible pulpitis to predict which patients would ultimately require root canal treatment (RCT). Logistic Regression achieved the best performance with AUC=0.64 and PPV=0.76, indicating moderate ability to identify patients who do need RCT. However, NPV=0.48 means the model cannot reliably rule out eventual RCT need, and older age plus presence of pre-existing restorations were the only significant predictors identified.

## 세줄요약

가역적 치수염을 가진 균열치 593개에서 4가지 머신러닝 모델로 치수 생존을 예측했다. 로지스틱 회귀가 AUC=0.64·PPV=0.76로 최우수 성능을 보여 RCT 필요 환자 식별에 유용하다. 그러나 NPV=0.48로 RCT 불필요 판정 신뢰도는 낮고, 고령과 기존 수복물 존재만이 유의미한 예측인자였다.

## Summary

Cracked teeth with retained pulp vitality have higher survival rates than those treated with RCT, yet the clinical challenge is identifying when RCT becomes necessary before irreversible pulpitis ensues. This retrospective study from Singapore developed and validated machine learning models to predict pulp survival (i.e., avoiding RCT) in cracked teeth presenting with reversible pulpitis.

Using data from 569 patients (593 cracked teeth), the authors tested Logistic Regression (LR), Gaussian Processes (GP), Random Forests (RF), and Gradient Boosting (GB). All models used age, gender, tooth type, and preoperative restorative status as input features, with binary pulp survival as the outcome. A 10-fold stratified nested cross-validation framework was employed — the outer loop estimated performance while the inner loop optimized hyperparameters, minimizing data leakage.

Across all four models, predictive accuracy ranged from 74–77%. LR achieved the highest AUC (0.64) and F1-score (0.60). PPV was 0.74–0.77 across models; NPV was 0.45–0.48. The only statistically significant predictors were older age and presence of preoperative restorations — both associated with a higher likelihood of eventual RCT. The similarity in performance across simple (LR) and complex (GB, RF) models suggests the underlying predictive signal is modest and largely linear with the available features.

## Key Contributions

1. **First ML application** for pulp survival prediction in cracked teeth specifically at the reversible-pulpitis stage — the window where conservative management decisions are most consequential.
2. **PPV of 0.76**: clinically useful positive-prediction performance — roughly 3 in 4 patients the model flags as needing RCT actually will need it.
3. **Age and preop restoration** confirmed as primary risk factors for pulp non-survival; aligns with biological reasoning (older dentinal tubules, reduced pulpal reserve; restored teeth have higher crack propagation risk).
4. Demonstrates that complex ensemble methods do not outperform LR on this dataset — suggesting that richer clinical features (crack depth, mobility, sensitivity scores, CBCT) are needed before complexity adds value.

## Methodology

- **Population**: 569 patients, 593 cracked teeth; all presenting with reversible pulpitis
- **Setting**: Single institution (Singapore); retrospective
- **Outcome**: Binary — pulp survival (no RCT required) vs. pulp non-survival (RCT required)
- **Models**: Logistic Regression, Gaussian Processes, Random Forests, Gradient Boosting
- **Validation**: 10-fold stratified nested cross-validation (outer loop: test performance; inner loop: hyperparameter optimization)
- **Threshold tuning**: Classification thresholds optimized for probabilistic models to balance sensitivity/specificity
- **Input features**: Age, gender, tooth type, preoperative restorative material
- **Performance metrics**: AUC, F1-score, sensitivity, specificity, PPV, NPV

## Results

| Model | AUC | F1 | PPV | NPV |
|---|---|---|---|---|
| Logistic Regression | **0.64** | **0.60** | 0.76 | 0.48 |
| Gaussian Processes | ~0.62 | ~0.58 | 0.74–0.77 | 0.45–0.47 |
| Random Forests | ~0.62 | ~0.58 | 0.74–0.77 | 0.45–0.47 |
| Gradient Boosting | ~0.62 | ~0.58 | 0.74–0.77 | 0.45–0.47 |

- **Overall accuracy**: 74–77%
- **Significant predictors**: Older age (↑ RCT risk), preoperative restoration present (↑ RCT risk)
- **Clinical interpretation of PPV=0.76**: When the model predicts RCT is needed, it is correct ~3 in 4 times — actionable for escalation decisions
- **Clinical interpretation of NPV=0.48**: When the model predicts pulp will survive, it is correct only ~half the time — insufficient to reassure or defer intervention

## Strengths and Caveats

**Strengths**
- Nested CV design reduces overfitting risk compared to simple train/test split
- Includes threshold tuning, improving calibration of probabilistic predictions
- Largest single-institution cracked-tooth dataset for this specific ML application in the literature

**Caveats**
- AUC=0.64 is modest; the model adds limited discrimination beyond clinical heuristics alone
- Feature set is sparse — no crack depth/length, no CBCT data, no periodontal status, no pain scores
- No external validation; generalizability to non-Singaporean populations unconfirmed
- Retrospective design introduces inherent selection bias in which teeth were monitored vs. treated
- Abstract-only build: granular class balance and exact split details unavailable
- NPV too low for clinical "rule-out" use — negative predictions carry substantial false-negative risk

## Related Papers

- [[fiyaz-ghani-2025-cracked-teeth-external-splinting-pulp-survival]] — examines pulp survival with conservative splinting; shares the clinical question this model targets
- [[gavriil-2025-single-vs-multiple-stage-cracked-teeth-pulp]] — treatment-stage effect on pulp survival; complementary outcome data
- [[zhang-2024-cracked-teeth-treatment-outcomes-sr-ma]] — SR/MA of CTS treatment outcomes; survival base rates provide context for model prevalence assumptions
