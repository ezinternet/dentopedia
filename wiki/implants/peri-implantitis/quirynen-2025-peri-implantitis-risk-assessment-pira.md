---
title: "Peri-implantitis Risk Assessment (PiRA) Part 2: Retrospective Study and Framework for an Evidence-Based Prediction Model for Clinicians"
authors: Marc Quirynen, Mihai Tarce, Manoetjer Siawasch, Ana B. Castro, Andy Temmerman, Wim Coucke, Wim Teughels
year: 2025
date: 2025-01-01
doi: 10.11607/jomi.11211
source: quirynen-2025-peri-implantitis-risk-assessment-pira.md
category: [implants/peri-implantitis]
evidence_level: retrospective
pdf_path: /Users/oracleneo/llm-wiki/papers/quirynen-2025-peri-implantitis-risk-assessment-pira.pdf
pdf_filename: quirynen-2025-peri-implantitis-risk-assessment-pira.pdf
source_collection: external
tags: [peri-implantitis, risk-prediction, PiRA, susceptibility-to-periodontitis, smoking, PPD, online-tool]
relations:
  - type: extends
    target: tarce-2025-peri-implantitis-risk-assessment-pira-part1
  - type: reinforces
    target: galarraga-vinueza-2025-peri-implant-disease-risk-factors
---

## Three-line Summary

Retrospective single-center cohort (Leuven implant review clinic; 460 patients, 1,432 implants; partially edentulous n=350, fully edentulous n=50) building a preoperative peri-implantitis prediction model from patient-related risk factors identified in a prior umbrella review (PiRA Part 1).

Peri-implantitis prevalence 17% overall (13.1% partially edentulous, 20% fully edentulous); significant risk factors in partially edentulous patients were susceptibility to periodontitis (OR 0.48), ≥3 sites with PPD ≥5 mm (OR 0.2), and smoking (OR 0.25–0.34); the 8-factor predictive model reached sensitivity 90.2% / specificity 55.0% (PPV 22.7%, NPV 97.5%).

A free online preoperative risk tool (pira.gbiomed.kuleuven.be) is being deployed for partially edentulous candidates; the fully-edentulous model (n=50, sensitivity 100%/specificity 51.3%) is underpowered for clinical use, and a prospective multicenter trial is planned.

## 세줄요약

후향 단일기관 코호트(Leuven 임플란트 리뷰 클리닉; 환자 460명, 임플란트 1,432개; 부분무치악 350명, 완전무치악 50명) — 선행 umbrella review(PiRA Part 1)에서 확인된 환자 관련 위험인자로 술전(preoperative) 임플란트 주위염(peri-implantitis) 예측모델을 구축.

전체 유병률 17%(부분무치악 13.1%, 완전무치악 20%); 부분무치악군 유의 위험인자는 치주염 감수성(susceptibility to periodontitis, OR 0.48), 탐침깊이(PPD) ≥5mm 부위 3곳 이상(OR 0.2), 흡연(OR 0.25–0.34); 8개 인자 예측모델은 민감도(sensitivity) 90.2% / 특이도(specificity) 55.0%(양성예측도 22.7%, 음성예측도 97.5%).

부분무치악 대상 무료 온라인 술전 위험평가 도구(pira.gbiomed.kuleuven.be)가 배포 중이나, 완전무치악 모델(n=50, 민감도 100%/특이도 51.3%)은 표본 부족으로 임상 적용에는 이르며, 다기관 전향연구로 보완할 예정.

## Summary

This retrospective study from the KU Leuven Implant Review Clinic (460 patients, 1,432 implants; December 2018–2019 records) operationalizes the patient-related risk factors identified in a companion umbrella review (PiRA Part 1) into a quantified preoperative peri-implantitis prediction model. Patients were split into partially edentulous (n=350, 8 candidate risk factors) and fully edentulous (n=50, 4 candidate risk factors) groups because data availability and pathophysiology differ. Overall peri-implantitis prevalence was 17% (13.1% partially edentulous, 20% fully edentulous). In partially edentulous patients, susceptibility to periodontitis (bone loss/age), ≥3 sites with probing pocket depth ≥5 mm, and smoking were significant univariate risk factors; a multivariable model combining all 8 factors achieved 90.2% sensitivity and 55.0% specificity (PPV 22.7%, NPV 97.5%). In fully edentulous patients, only maxillary implant location was a significant univariate factor, and the 4-factor model (sensitivity 100%, specificity 51.3%) is based on too few patients (n=50) to be clinically reliable yet. The authors have deployed a free online tool implementing the partially-edentulous model for preoperative risk discussion with candidates, and plan a prospective multicenter trial to refine both models and extend the fully-edentulous model to clinical use.

## Key Contributions
- First study to convert the literature-derived patient-related risk factor list (PiRA Part 1 umbrella review) into a quantified, cohort-validated preoperative prediction model.
- Separately models partially edentulous (8 factors) vs fully edentulous (4 factors) patients, reflecting real differences in available risk-factor data.
- Provides both univariate ORs with ROC-optimized thresholds and a multivariable predictive model with full diagnostic-accuracy metrics (sensitivity, specificity, PPV, NPV, LR+, LR−), plus a leave-one-variable-out sensitivity analysis identifying susceptibility to periodontitis and smoking as the most influential predictors.
- Deploys the model as a free, clinician-facing online tool (pira.gbiomed.kuleuven.be) for use at the treatment-planning stage — an actionable preoperative complement to postoperative tools like IDRA.

## Methodology
- Retrospective single-center cohort; records reviewed Dec 2018–2019 at University Hospitals Leuven Implant Review Clinic.
- Peri-implantitis defined as radiographic implant-platform-to-bone distance ≥3 mm + bleeding on probing, reported at patient level.
- Exclusions: iatrogenic factors (malposition, no keratinized mucosa, non-biocompatible abutment, hygiene-preventing prosthesis, submucosal cement) and incomplete records.
- Statistics: categorical PCA to confirm risk-factor independence; univariate GLM (logit link) for ORs using both a prior periodontal risk-tool's thresholds and ROC-derived optimal cutoffs; multivariable GLM + ROC for the final model; leave-one-out variable importance analysis.

## Results

| Outcome | Result |
|---|---|
| Overall peri-implantitis prevalence | 78/460 patients (17%) |
| Partially edentulous prevalence | 46/350 (13.1%) |
| Fully edentulous prevalence | 10/50 (20%) |
| Susceptibility to periodontitis (bone loss/age), OR | 0.48 [0.24;0.94], P=.03 |
| ≥3 sites PPD ≥5 mm, OR | 0.2 [0.10;0.40], P<.01 |
| Smoking (nonsmoker vs smoker), OR | 0.34 [0.13;0.87], P=.03 |
| Maxillary vs mandibular location (fully edentulous), OR | 0.15 [0.02;0.87], P=.03 |
| Partially edentulous model (n=321) | Sens 90.2%, Spec 55.0%, PPV 22.7%, NPV 97.5% |
| Fully edentulous model (n=49) | Sens 100%, Spec 51.3%, PPV 34.5%, NPV 100% |

## Related Papers
- [[implants/galarraga-vinueza-2025-peri-implant-disease-risk-factors]] — independent AO/AAP SR+MA confirming periodontitis and smoking as consistent peri-implant-disease risk indicators, reinforcing this study's univariate findings.
- [[implants/peri-implantitis/basak-2024-restoration-margin-alveolar-bone-distance-implant]] — validates a threshold from IDRA, an existing risk tool targeting already-restored implants; contrasts with PiRA's preoperative, candidate-selection focus.
- [[overviews/peri-implantitis-management-overview]] — synthesis page covering peri-implant disease risk factors and management; candidate for updating with the preoperative-prediction-model angle.
