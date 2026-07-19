---
title: "Evaluation of postoperative bleeding risk after dental extractions in patients on antithrombotic medication: A comparison of machine learning and clinical experience"
authors: Marie Sophie Katz, Orian Nathan Mahlow, Rajae Benidamou, Mark Ooms, Marius Heitzer, Dirk Elvers, Frank Hölzle, Ali Modabber
year: 2025
doi: 10.1007/s00784-025-06590-0
category: [drug/anticoagulants]
source_collection: pubmed-text
full_text: true
pmid: "41139707"
pmcid: "PMC12554821"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12554821/
text_path: /Users/oracleneo/llm-wiki/papers/katz-2025-bleeding-risk-machine-learning-antithrombotic.txt
text_filename: katz-2025-bleeding-risk-machine-learning-antithrombotic.txt
---

## Why Ingested

기존 [[drug/anticoagulants/krishnan-2024-bleeding-uninterrupted-single-dual-antiplatelet]]와 [[drug/anticoagulants/moldovan-2023-anticoagulant-oral-surgery-bleeding-sr]]가 확립한 "단일요법보다 이중요법이 위험하다"는 군 수준(group-level) 결론을, 2000건 단일기관 코호트에서 **개별 환자 예측**이 가능한지로 밀어붙인 첫 시도. 결과는 기계학습(Machine Learning, ML)조차 균형정확도(balanced accuracy) 58–62%로 우연에 근접 — 위험인자를 안다는 것과 누가 출혈할지 안다는 것이 다르다는 점을 정량화하므로, 예방적 입원·연장관찰 의사결정의 근거로서 보관 가치가 있다.

## Three-line Summary

Single-centre retrospective chart review at RWTH Aachen (Jan 2014–Aug 2024) of 2000 dental extraction procedures under antiplatelet or anticoagulant therapy, all treated with a uniform gelatin sponge + 4-0 Vicryl suture hemostatic protocol; 80/20 train/test split feeding four algorithms (LR, RF, XGB, KNN) benchmarked against one senior oral surgeon (>15 years) on the same 400-procedure test set.

Postoperative bleeding occurred in 87/2000 procedures (4.35%); on univariate testing only dual therapy reached significance (p<0.001), and on the test set (17 bleeders) balanced accuracy was KNN 62% > XGB 61% > RF 59% > LR 58% > surgeon 53%, with the surgeon generating 92 false positives against KNN's 114 and XGB's 52.

All models sat only modestly above chance (best AUC 0.62–0.671) and missed 8–13 of 17 true bleeders, so the headline "algorithms outperformed the surgeon" is a narrow ranking claim on one low-event single-centre dataset — not evidence that ML is ready to triage bleeding risk at the chair.

## 세줄요약

독일 RWTH Aachen 단일기관 후향 차트리뷰(2014-01~2024-08): 항혈전제(antiplatelet/anticoagulant) 복용 하 발치 2000건, 전례에 젤라틴 스폰지 + 4-0 Vicryl 봉합의 표준 국소지혈 프로토콜 적용; 80/20 분할로 4개 알고리즘(LR·RF·XGB·KNN) 학습 후 15년 경력 구강외과 전문의와 동일한 400건 테스트셋에서 대결.

술후 출혈 87/2000건(4.35%); 단변량에서는 이중요법(dual therapy)만 유의(p<0.001), 테스트셋(출혈 17건) 균형정확도는 KNN 62% > XGB 61% > RF 59% > LR 58% > 술자 53%이며 위양성은 술자 92건, KNN 114건, XGB 52건.

모든 모델이 우연 대비 소폭 우위(최고 AUC 0.62–0.671)에 그치고 실제 출혈 17건 중 8–13건을 놓쳤으므로, "알고리즘이 술자를 이겼다"는 저사건률 단일기관 데이터셋 한 개에서의 순위 진술일 뿐 — ML로 출혈 위험을 선별해도 된다는 근거가 아니다.

## 1. Document Information

- **Title**: Evaluation of postoperative bleeding risk after dental extractions in patients on antithrombotic medication: A comparison of machine learning and clinical experience
- **Authors**: Marie Sophie Katz, Orian Nathan Mahlow, Rajae Benidamou, Mark Ooms, Marius Heitzer, Dirk Elvers, Frank Hölzle, Ali Modabber (Dept. of Oral and Maxillofacial Surgery, University Hospital RWTH Aachen, Germany; Mahlow: Chair of Electronic Commerce, Goethe University Frankfurt)
- **Journal**: Clinical Oral Investigations 2025;29(11):531 (published 2025-10-27)
- **DOI**: 10.1007/s00784-025-06590-0
- **PMID**: 41139707 / **PMCID**: PMC12554821
- **Study type**: Single-centre retrospective clinical study / comparative study (retrospective chart review + supervised ML benchmark)
- **Ethics**: Ethics Committee, Medical Faculty RWTH Aachen (Decision Number EK 24-353)
- **Source**: PubMed Central full text (PMC12554821)

## 2. Key Contributions

- First study (per the authors) to apply machine learning to the prediction of complications after oral surgery, specifically post-extraction bleeding under antithrombotic medication.
- Head-to-head benchmark of four algorithm families (LR, RF, XGB, KNN) against a single senior oral surgeon on an identical held-out test set of 400 procedures — an explicit human-vs-model comparison rather than a model-only performance report.
- Quantifies the clinical intuition that surgeons over-predict bleeding: the surgeon flagged 97 of 400 procedures as bleeders when only 17 bled (92 false positives), which the authors link to over-liberal preventive inpatient admission.
- Documents a notably low bleeding incidence (4.35%) attributed to universal gelatin sponge application, and reasons explicitly about how that low event rate degrades predictability.

## 3. Methodology and Architecture

- **Setting/period**: University Hospital RWTH Aachen, Department of Oral and Maxillofacial Surgery; dental extractions January 2014 – August 2024, centralized retrospective chart review.
- **N**: 2000 procedures; 7125 teeth removed (6607 simple extraction, 518 osteotomy). Mean age 68.5 years (SD ±13.5); 1305 male (65.3%) / 695 female (34.7%).
- **Medication groups (Table 1, internally consistent set)**: monotherapy 1778 — antiplatelet (AP) 670, VKA 328, heparin 233 (LMWH 184 + UFH 49), DOAC 547; dual therapy 213; triple therapy 9. *(The published abstract instead states monotherapy 1788 / dual 426 / triple 27; only the Table 1 figures sum to 2000 — see Limitations.)*
- **Region**: anterior only 256 (Table 1 lists 265), posterior only 1009, both 735.
- **Exclusions**: age <18, no antithrombotic medication, inherited bleeding disorders, incomplete postoperative documentation (missing bleeding/follow-up data within 10 days), intraoral procedures other than extraction (biopsy, root resection).
- **Standardized hemostasis (all cases)**: gelatin sponge (Gelastypt, Sanofi-Aventis) into the alveolus + 4-0 Vicryl (Ethicon) suture. This is uniform across the cohort, i.e. not a study variable.
- **Outcome**: binary — any documented postoperative bleeding event requiring clinical attention, irrespective of severity. No severity grading (too few severe cases).
- **Sample size**: G*Power 3.1.9.6, alpha 0.05, effect size 0.1, power 95% → minimum 1135 procedures; inflated to 2000 to offset the bleeding-lowering effect of universal gelatin sponge use. Anchored on Yagyuu et al. (10.4% DOAC / 12% VKA bleeding).
- **Statistics**: Chi-square / Fisher's exact for categorical; Wilcoxon-Mann-Whitney for continuous (non-Gaussian per Shapiro-Wilk); p<0.05 significant.
- **ML design**: random 80/20 split (1600 train / 400 test). Four models — logistic regression (LR), random forest (RF), eXtreme gradient boost (XGB), K-nearest neighbors (KNN) — trained on the training set, then evaluated on the test set. A senior oral surgeon with >15 years' experience independently assessed the same 400 procedures. Features: sex, age, medication type, number of teeth by removal method (extraction vs osteotomy), region (anterior/posterior/both).
- **Metrics**: balanced accuracy (primary), accuracy with 95% CI, sensitivity, specificity, AUC, Brier score.

## 4. Key Results and Benchmarks

- **Overall bleeding incidence**: 87/2000 (4.35%). Test set: 17/400 (4.25%).
- **Univariate risk factors**: only dual therapy significant (p<0.001, 20/213 bled = 9.4%). Not significant: monotherapy type (p=0.072; AP 19/670, VKA 12/328, heparin 6/233, DOAC 30/547), triple therapy (p=1.000; 0/9), sex (p=0.251), age (p=0.361), location (p=0.735), teeth by extraction (p=0.376), teeth by osteotomy (p=0.359).
- **Balanced accuracy (test set, n=400)**: KNN 0.616 > XGB 0.608 > RF 0.591 > LR 0.580 > senior surgeon 0.527.
- **Full performance table**:
  - LR — accuracy 0.90 (CI 0.86–0.92), sensitivity 0.235, specificity 0.924, AUC 0.624, Brier 0.041
  - RF — accuracy 0.81 (CI 0.77–0.85), sensitivity 0.353, specificity 0.830, AUC 0.671, Brier 0.043
  - XGB — accuracy 0.84 (CI 0.80–0.88), sensitivity 0.353, specificity 0.864, AUC 0.646, Brier 0.042
  - KNN — accuracy 0.70 (CI 0.65–0.74), sensitivity 0.529, specificity 0.702, AUC 0.623, Brier 0.042
  - Surgeon — accuracy 0.74 (CI 0.69–0.78), sensitivity 0.294, specificity 0.760, AUC/Brier not applicable
- **Confusion matrices (Fig. 2)**: LR 4 TP / 354 TN / 29 FP / 13 FN; RF 6/318/65/11; XGB 6/331/52/11; KNN 9/269/114/8; surgeon 5/291/92/12.
- **False-positive burden**: surgeon predicted 97 bleeders total (92 FP); KNN 114 FP; RF 65 FP; XGB 52 FP; LR 29 FP. The authors nominate XGB as the cost-efficiency optimum and KNN as the "safest" (highest sensitivity, 0.529).
- **Comparison to literature**: this cohort's 4.35% is well below Yanamoto (17.4%), Ueda (19%), and the 10.4–23% range reported elsewhere; the authors attribute the gap to universal gelatin sponge use, citing Svensson et al. (4% under gelatin sponge in warfarin patients).
- **AUC in context**: the authors place their best AUC (0.62 for KNN) against ML studies in dentistry reporting 0.86 (direct pulp capping, Long), 0.97 (extraction decision support, Cui), and 0.55 (mucoepidermoid carcinoma survival, Alshwayyat), and read 0.62 as evidence of substantial unexplained heterogeneity.

## 5. Limitations and Future Work

- **Interpretive caution (most important)**: balanced accuracy of 58–62% is only modestly above chance (50%). "All four algorithms outperformed the surgeon" is a narrow ranking claim on a single-centre retrospective dataset — **not** evidence that machine learning is ready to guide clinical bleeding decisions or to triage patients to inpatient observation. Every model, including the best one, missed the majority of true bleeders (KNN 8/17 missed; LR 13/17 missed).
- **Very few positive events**: the 4.35% base rate leaves only 17 bleeders in the 400-procedure test set, so every performance estimate rests on single-digit true-positive counts (4–9). Sensitivity figures at this scale are extremely unstable, and no confidence interval is reported for balanced accuracy at all.
- **No external validation**: single-centre, single dataset, no held-out institution or temporal validation. Generalizability is untested.
- **Single-clinician comparator**: the human benchmark is one surgeon's judgement on a chart review, acknowledged by the authors as a bias source in either direction. It is not a measure of "clinical experience" in general, nor of a real chairside decision with the patient present.
- **Universal gelatin sponge as confounder**: the uniform hemostatic protocol suppressed the event rate, strengthening internal validity but compressing the outcome signal the models had to learn and limiting transfer to settings without routine local hemostasis.
- **Numerical inconsistency in the published paper**: the abstract reports monotherapy 1788 / dual 426 / triple 27, which does not sum to 2000; the Results text and Table 1 give 1778 / 213 / 9, which does. Anterior-only procedures are stated as 256 in the text and 265 in Table 1. Table 1 is treated as authoritative here.
- **Coarse feature set**: no data on incisions, preoperative inflammation, or operating surgeon's experience; dual/triple therapy not subdivided by drug combination (e.g. dual antiplatelet vs antiplatelet–anticoagulant), obscuring differential risk.
- **Binary outcome**: no severity grading (minor oozing vs bleeding requiring re-suturing or admission are pooled), which limits clinical resolution — a "predicted bleed" carries no information about consequence.
- **Authors' own caveat**: clinicians should never rely solely on ML output; "soft" factors (home environment, independence, anxiety, care needs) drive observation and admission decisions and are absent from structured data. Future work: multicentre cohorts, richer perioperative variables, severity-graded outcomes.

## 6. Related Work

- Yagyuu et al. — post-extraction bleeding 10.4% (DOAC) / 12% (VKA) in 541 patients, 634 procedures; used as the sample-size anchor.
- Ueda et al. — osteotomies, vertical incisions, posterior and multiple extractions raise bleeding risk; 19% bleeding rate.
- Yanamoto et al. — 17.4% post-extraction bleeding rate under antithrombotic therapy.
- Kataoka et al. — HAS-BLED score found insufficient for predicting dental extraction bleeding in warfarin patients.
- Svensson et al. — 4% bleeding in warfarin patients with absorbable gelatin sponge; closest match to this cohort's rate.
- Mahmoudi et al. — gelatin sponge significantly reduces measured blood absorption vs control.
- Bayrakdar et al. — CNN caries detection outperformed dentists on radiographs.
- Elgarba et al. — AI-driven single-implant planning matched expert quality with better time-efficiency and consistency.
- Long et al. (direct pulp capping, AUC 0.86), Cui et al. (extraction decision support, AUC 0.97), Alshwayyat et al. (mucoepidermoid carcinoma survival, AUC 0.55) — same four-algorithm family, used to contextualize this study's AUC 0.62.
- German S3 guidelines — recommend preventive hospitalization as an option under dual or triple anticoagulation therapy.

## 7. Glossary

- **Balanced accuracy (균형정확도)**: mean of sensitivity and specificity; used instead of raw accuracy because a 4.35% event rate lets a "never bleeds" model score ~96% accuracy. 50% = chance.
- **AP (Antiplatelet, 항혈소판제)**: e.g. aspirin, clopidogrel; inhibits platelet aggregation.
- **AC (Anticoagulant, 항응고제)**: VKA, heparin, or DOAC; inhibits the coagulation cascade.
- **VKA (Vitamin K Antagonist, 비타민 K 길항제)**: warfarin/phenprocoumon; INR-monitored.
- **DOAC (Direct Oral Anticoagulant, 직접경구항응고제)**: dabigatran (thrombin/IIa), rivaroxaban/apixaban/edoxaban (factor Xa).
- **LMWH / UFH**: low molecular weight heparin (subcutaneous) / unfractionated heparin (intravenous).
- **Dual / triple therapy (이중·삼중요법)**: two or three concurrent antithrombotic agents; dual therapy was the only significant univariate bleeding risk factor here.
- **LR (Logistic Regression, 로지스틱 회귀)**: statistical model for a binary outcome; the baseline comparator.
- **RF (Random Forest, 랜덤 포레스트)**: ensemble of decision trees aggregated by majority vote/average to reduce overfitting.
- **XGB (eXtreme Gradient Boost)**: gradient-boosted trees combining weak learners iteratively to minimize prediction error.
- **KNN (K-Nearest Neighbors, K-최근접 이웃)**: non-parametric classifier assigning the majority label among the k closest training examples.
- **AUC (Area Under the ROC Curve, 곡선하면적)**: discrimination measure; 0.5 = chance, 1.0 = perfect. Best here 0.671 (RF).
- **Brier score**: mean squared error of probabilistic predictions; lower is better, but is dominated by the majority class at low event rates.
- **Sensitivity / specificity (민감도·특이도)**: proportion of true bleeders correctly flagged / proportion of non-bleeders correctly cleared.
- **HAS-BLED**: clinical bleeding-risk score from cardiology; found inadequate for dental extraction risk.
