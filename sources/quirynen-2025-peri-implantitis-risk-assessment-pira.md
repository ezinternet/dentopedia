---
title: "Peri-implantitis Risk Assessment (PiRA) Part 2: Retrospective Study and Framework for an Evidence-Based Prediction Model for Clinicians"
authors: Marc Quirynen, Mihai Tarce, Manoetjer Siawasch, Ana B. Castro, Andy Temmerman, Wim Coucke, Wim Teughels
year: 2025
doi: 10.11607/jomi.11211
category: [implants/peri-implantitis]
pdf_path: /Users/oracleneo/llm-wiki/papers/quirynen-2025-peri-implantitis-risk-assessment-pira.pdf
pdf_filename: quirynen-2025-peri-implantitis-risk-assessment-pira.pdf
source_collection: external
---

## Why Ingested

기존 [[implants/galarraga-vinueza-2025-peri-implant-disease-risk-factors]]가 임플란트 주위염의 위험지표(periodontitis, smoking, diabetes 등)를 SR+MA로 확인했다면, 본 논문(Quirynen 2025, PiRA Part 2)은 그 위험지표들을 실제 460명 환자 후향 코호트에서 계량화하여 술전(preoperative) 예측 모델로 변환한다는 점에서 임상적용 단계의 근거를 보강한다. 저자 그룹의 동반 논문인 PiRA Part 1(Tarce & Quirynen, umbrella review, 같은 호 555–561쪽)을 직접 잇는 후속 연구로, 위험지표 목록을 실데이터로 검증·정량화(OR, 민감도/특이도)한다.

## Three-line Summary

Retrospective single-center study (Leuven implant review clinic; 460 patients, 1,432 implants; partially edentulous n=350, fully edentulous n=50) building a preoperative peri-implantitis prediction model from patient-related risk factors identified in a prior umbrella review.

Peri-implantitis prevalence 17% overall (13.1% partially edentulous, 20% fully edentulous); for partially edentulous patients, susceptibility to periodontitis (OR 0.48), ≥3 sites with PPD ≥5 mm (OR 0.2), and smoking (OR 0.25–0.34) were significant risk factors; the 8-factor predictive model reached 90.2% sensitivity / 55.0% specificity (PPV 22.7%, NPV 97.5%).

The resulting model is being deployed as a free online preoperative risk-assessment tool (pira.gbiomed.kuleuven.be) for partially edentulous candidates; the fully-edentulous model (4 factors, sensitivity 100%/specificity 51.3%, n=50) is underpowered and not yet clinically deployable, and a prospective multicenter trial is planned to refine both.

## 세줄요약

후향 단일기관 연구(Leuven 임플란트 리뷰 클리닉; 환자 460명, 임플란트 1,432개; 부분무치악 350명, 완전무치악 50명) — 선행 umbrella review에서 확인된 환자 관련 위험인자를 이용해 술전(preoperative) 임플란트 주위염(peri-implantitis) 예측모델을 구축.

전체 유병률 17%(부분무치악 13.1%, 완전무치악 20%); 부분무치악군에서 치주염 감수성(susceptibility to periodontitis, OR 0.48), 탐침깊이(PPD) ≥5mm 부위 3곳 이상(OR 0.2), 흡연(OR 0.25–0.34)이 유의한 위험인자였고, 8개 인자 예측모델은 민감도(sensitivity) 90.2% / 특이도(specificity) 55.0%(양성예측도 22.7%, 음성예측도 97.5%).

부분무치악 대상 무료 온라인 술전 위험평가 도구(pira.gbiomed.kuleuven.be)가 개발되었으나, 완전무치악 모델(4개 인자, n=50, 민감도 100%/특이도 51.3%)은 표본 부족으로 임상 사용에는 아직 이르며 다기관 전향연구로 보완 예정.

## 1. Document Information
- **Journal**: The International Journal of Oral & Maxillofacial Implants 2025;40(5):571–578
- **DOI**: 10.11607/jomi.11211
- **Institution**: Department of Oral Health Sciences, KU Leuven & University Hospitals Leuven (Periodontology), Leuven, Belgium

## 2. Key Contributions
- Converts the patient-related risk factors identified in a companion umbrella review (PiRA Part 1) into a quantified, retrospective-cohort-derived preoperative prediction model for peri-implantitis.
- Separately models partially edentulous (8 factors) and fully edentulous (4 factors) patients, reflecting differing available data and pathophysiology.
- Reports both univariate odds ratios (with ROC-derived optimal thresholds) and a multivariable predictive model with sensitivity/specificity/PPV/NPV/likelihood ratios, including leave-one-variable-out sensitivity analysis (Table 3).
- Deploys the model as a free online clinician-facing tool (pira.gbiomed.kuleuven.be) for partially edentulous case screening at the treatment-planning stage.

## 3. Methodology and Architecture
- **Design**: Retrospective single-center cohort study (Implant Review Clinic, University Hospitals Leuven), records Dec 2018–2019.
- **n**: 460 patients (1,432 implants) total; partially edentulous 391 (350 analyzed after excluding 41 with iatrogenic factors); fully edentulous 69 (50 analyzed after excluding 19).
- **Peri-implantitis definition**: radiographic implant-platform-to-bone distance ≥3 mm + bleeding on probing (patient-level prevalence, per 8th European Workshop on Periodontology consensus).
- **Exclusions**: improper implant position, absence of keratinized mucosa, non-biocompatible abutment material, prosthesis preventing oral hygiene, submucosal cement on radiographs, incomplete records.
- **Statistics**: categorical PCA (biplot/loadings) to check variable independence; univariate generalized linear models (logit link) for OR by risk factor, using thresholds from an existing periodontal risk assessment tool plus ROC-derived optimal cutoffs; Spearman/Cramer's V for correlation with marginal bone loss; multivariable GLM + ROC for the final predictive model; leave-one-out analysis per variable.
- **Outcomes**: peri-implantitis prevalence, per-factor OR, model sensitivity/specificity/PPV/NPV/LR+/LR-.

## 4. Key Results and Benchmarks
- Overall prevalence: 78/460 patients (17%) had peri-implantitis.
- Partially edentulous (n=350): 46 patients (13.1%) peri-implantitis. Significant univariate risk factors: susceptibility to periodontitis (bone loss/age, ROC threshold 0.27) OR 0.48 [0.24;0.94], P=.03; number of sites with PPD ≥5 mm (threshold 3) OR 0.2 [0.10;0.40], P<.01 (also significant at thresholds 4 and 8); smoking (nonsmoker vs smoker) OR 0.34 [0.13;0.87], P=.03, and at ROC threshold (4 cig/day) OR 0.25 [0.09;0.66], P<.01. Full-mouth bleeding score, recall interval, general health (diabetes), implant location, and teeth lost were not significant.
- Fully edentulous (n=50): 10 patients (20%) peri-implantitis. Only implant location (mandibular vs maxillary) was significant: OR 0.15 [0.02;0.87], P=.03.
- Predictive model — partially edentulous (n=321 analyzable): PPV 22.7%, NPV 97.5%, sensitivity 90.2%, specificity 55.0% (LR+ 2.0, LR− 0.2); 4/41 true peri-implantitis cases missed.
- Predictive model — fully edentulous (n=49 analyzable): PPV 34.5%, NPV 100%, sensitivity 100%, specificity 51.3% (LR+ 2.0, LR− 0.0); no true cases missed, but small n limits stability.
- Leave-one-variable-out analysis (Table 3) shows sensitivity drops most when susceptibility to periodontitis or smoking are removed, indicating these are the model's most influential variables for partially edentulous patients.

## 5. Limitations and Future Work
- Single-center, retrospective design; relatively small fully-edentulous subgroup (n=50) yields an unstable, currently non-deployable model for that group.
- Two literature-identified risk factors (oral hygiene, occlusal overload) could not be assessed due to unavailable chart data.
- Moderate specificity (51–55%) means many false positives; model is intended to flag candidates for discussion/precautions, not to replace clinical judgment.
- Authors explicitly plan a prospective multicenter trial to increase data quantity/quality and extend applicability to fully edentulous patients.
- Industry funding disclosed (Dentsply Sirona, Nobel Biocare grant; departmental research chairs from Dentsply Sirona, Straumann, Henry Schein) — no conflicts of interest declared by authors.

## 6. Related Work
- Tarce & Quirynen 2025 (PiRA Part 1, Int J Oral Maxillofac Implants 2025;40:555–561): umbrella review that identified the 10 patient-related risk factors this study tests; direct predecessor in the same 2-part series (see `papers/tarce-2025-peri-implantitis-risk-assessment-pira-part1.pdf`, ingested separately).
- Heitz-Mayfield et al 2020 (IDRA — Implant Disease Risk Assessment): an existing preoperative-adjacent risk tool targeting patients with already-restored implants; contrasted here as a tool this study's preoperative model complements. See [[implants/peri-implantitis/basak-2024-restoration-margin-alveolar-bone-distance-implant]] for IDRA threshold validation.
- Galarraga-Vinueza et al 2025 (AO/AAP SR+MA): confirms periodontitis and smoking as consistent risk indicators for peri-implant disease, reinforcing this study's univariate findings. See [[implants/galarraga-vinueza-2025-peri-implant-disease-risk-factors]].
- Mameno et al 2021: machine-learning-based peri-implantitis prediction, an alternative modeling approach to this study's GLM/logistic approach.

## 7. Glossary
- **PiRA**: Peri-implantitis Risk Assessment — the online tool/framework developed in this 2-part study.
- **OR**: Odds ratio.
- **PPV / NPV**: Positive/negative predictive value.
- **LR+ / LR-**: Positive/negative likelihood ratio.
- **PPD**: Probing pocket depth.
- **ROC analysis**: Receiver operating characteristic analysis, used here to derive optimal risk-factor thresholds and evaluate model discrimination.
- **IDRA**: Implant Disease Risk Assessment, an existing peri-implant risk tool (Heitz-Mayfield et al 2020) aimed at already-restored implants.
