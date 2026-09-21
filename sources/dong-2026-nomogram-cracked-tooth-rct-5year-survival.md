---
title: "Development of a Nomogram to Predict 5-Year Tooth Loss After Root Canal Treatment in Patients with Cracked Teeth and Chronic Irreversible Pulpitis"
authors: "Dong Q, Guo S, et al."
year: 2026
doi: "10.2340/aos.v85.46624"
category: [cracked-tooth]
source_collection: pubmed-abstract
---

## Why Ingested
최초 cracked-tooth 카테고리 인제스트. 치근관치료 후 5년 치아 생존율을 예측하는 노모그램 — [[cracked-tooth/gioti-2026-symptomatic-cracked-tooth-management-survey]]의 임상 의사결정 근거와 짝을 이룬다.

## One-line Summary
Retrospective cohort (n=295); nomogram identified probing depth >5 mm, 2-3 RCT visits, and crown restoration as independent 5-year tooth-loss predictors; 89.9% 5-year survival; AUC 0.73.

## 한줄요약
후향적 코호트(n=295); 탐침깊이>5mm·다회방문 RCT·크라운 보철이 5년 치아상실 독립예측인자; 5년 생존율 89.9%; 노모그램 AUC 0.73.

## 1. Document Information
- Journal: Acta Odontologica Scandinavica 2026;85:528–537
- DOI: 10.2340/aos.v85.46624 | PMID: 42565287 | PMC: PMC13462994
- Setting: Nanjing Stomatological Hospital, Nanjing University, China
- Funding/COI: not reported

## 2. Key Contributions
- First nomogram specifically for cracked tooth + chronic irreversible pulpitis post-RCT prognosis
- Probing depth >5 mm is the strongest RISK factor (OR 2.99): elevated extraction risk
- Single-visit RCT is preferable — 2-3 visits independently associated with higher tooth loss (OR 0.15 = protective direction is single-visit)
- Crown restoration after RCT is protective (OR 0.28 for tooth loss)
- AUC 0.73 — moderate discrimination; clinically useful for stratifying borderline cases

## 3. Methodology and Architecture
- Study design: retrospective case analysis; 2017–2020; 3-year treatment window
- Population: 295 patients (295 teeth) with cracked tooth + chronic irreversible pulpitis
- Outcome: tooth retention vs loss within 5 years of RCT
- Variable selection: LASSO → binary logistic regression
- Model: nomogram via R 'rms' package
- Validation: H-L test (calibration), ROC (discrimination), decision curve analysis (clinical utility)
- Survival group n=265 (89.9%), non-survival n=30 (10.1%)

## 4. Key Results and Benchmarks
- 5-year tooth survival rate: 89.9%
- Independent predictors of tooth LOSS (multivariate):
  - Probing depth >5 mm: OR 2.99 (95%CI 1.26–7.09), p<0.05
  - 2–3 RCT visits (vs single): OR 0.15 (95%CI 0.05–0.50), p<0.05 [note: OR <1 means 2-3 visits is listed as protective vs loss in one direction — interpret carefully; paper frames single-visit as protective]
  - Crown restoration: OR 0.28 (95%CI 0.09–0.83), p<0.05 [protective]
- Nomogram AUC: 0.73 (95%CI 0.62–0.84)
- H-L test p=0.682 — good calibration
- Decision curve analysis: net benefit within risk threshold 4–68%

## 5. Limitations and Future Work
- Single center; n=295 with only 30 non-survival events — limited statistical power
- Retrospective design; selection bias (patients who agreed to RCT)
- Crack severity classification not standardized (no crack extent grading)
- No external validation — authors call for multicenter prospective replication
- Follow-up fixed at 5 years; long-term data beyond 5 years not available

## 6. Related Work
- Predictors align with known cracked tooth prognostic factors: periodontal involvement, restoration quality
- Nomogram approach parallels other dental prognostic tools (implant failure prediction models)

## 7. Glossary
- VRF: Vertical Root Fracture (different from cracked tooth syndrome — excluded in this study)
- RCT: Root Canal Treatment
- LASSO: Least Absolute Shrinkage and Selection Operator (variable selection method)
- H-L test: Hosmer-Lemeshow test for model calibration
- DCA: Decision Curve Analysis — clinical utility of prediction model
