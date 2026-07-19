---
title: "Evaluation of postoperative bleeding risk after dental extractions in patients on antithrombotic medication: A comparison of machine learning and clinical experience"
authors: Marie Sophie Katz, Orian Nathan Mahlow, Rajae Benidamou, Mark Ooms, Marius Heitzer, Dirk Elvers, Frank Hölzle, Ali Modabber
year: 2025
date: 2025-10-27
doi: 10.1007/s00784-025-06590-0
source: katz-2025-bleeding-risk-machine-learning-antithrombotic.md
category: [drug/anticoagulants]
evidence_level: retrospective
source_collection: pubmed-text
full_text: true
pmid: "41139707"
pmcid: "PMC12554821"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12554821/
pdf_path: /Users/oracleneo/llm-wiki/papers/katz-2025-bleeding-risk-machine-learning-antithrombotic.txt
pdf_filename: katz-2025-bleeding-risk-machine-learning-antithrombotic.txt
text_path: /Users/oracleneo/llm-wiki/papers/katz-2025-bleeding-risk-machine-learning-antithrombotic.txt
text_filename: katz-2025-bleeding-risk-machine-learning-antithrombotic.txt
tags: [antithrombotic, antiplatelet, anticoagulant, doac, vka, heparin, dual-therapy, post-extraction-bleeding, machine-learning, risk-prediction, gelatin-sponge, german-cohort]
relations:
  - type: reinforces
    target: krishnan-2024-bleeding-uninterrupted-single-dual-antiplatelet
  - type: refines
    target: moldovan-2023-anticoagulant-oral-surgery-bleeding-sr
  - type: applies-to
    target: dinkova-2025-local-hemostasis-oral-surgery-review
---

## Three-line Summary

Single-centre retrospective chart review at RWTH Aachen (Jan 2014–Aug 2024) of 2000 dental extraction procedures under antiplatelet or anticoagulant therapy, all treated with a uniform gelatin sponge + 4-0 Vicryl suture hemostatic protocol; 80/20 train/test split feeding four algorithms (LR, RF, XGB, KNN) benchmarked against one senior oral surgeon (>15 years) on the same 400-procedure test set.

Postoperative bleeding occurred in 87/2000 procedures (4.35%); on univariate testing only dual therapy reached significance (p<0.001), and on the test set (17 bleeders) balanced accuracy was KNN 62% > XGB 61% > RF 59% > LR 58% > surgeon 53%, with the surgeon generating 92 false positives against KNN's 114 and XGB's 52.

All models sat only modestly above chance (best AUC 0.62–0.671) and missed 8–13 of 17 true bleeders, so the headline "algorithms outperformed the surgeon" is a narrow ranking claim on one low-event single-centre dataset — not evidence that ML is ready to triage bleeding risk at the chair.

## 세줄요약

독일 RWTH Aachen 단일기관 후향 차트리뷰(2014-01~2024-08): 항혈전제(antiplatelet/anticoagulant) 복용 하 발치 2000건, 전례에 젤라틴 스폰지 + 4-0 Vicryl 봉합의 표준 국소지혈 프로토콜 적용; 80/20 분할로 4개 알고리즘(LR·RF·XGB·KNN) 학습 후 15년 경력 구강외과 전문의와 동일한 400건 테스트셋에서 대결.

술후 출혈 87/2000건(4.35%); 단변량에서는 이중요법(dual therapy)만 유의(p<0.001), 테스트셋(출혈 17건) 균형정확도는 KNN 62% > XGB 61% > RF 59% > LR 58% > 술자 53%이며 위양성은 술자 92건, KNN 114건, XGB 52건.

모든 모델이 우연 대비 소폭 우위(최고 AUC 0.62–0.671)에 그치고 실제 출혈 17건 중 8–13건을 놓쳤으므로, "알고리즘이 술자를 이겼다"는 저사건률 단일기관 데이터셋 한 개에서의 순위 진술일 뿐 — ML로 출혈 위험을 선별해도 된다는 근거가 아니다.

## Summary

This retrospective study from the Department of Oral and Maxillofacial Surgery at University Hospital RWTH Aachen asks whether machine learning can predict which antithrombotic-medicated patients will bleed after a dental extraction better than an experienced surgeon can. From 2000 procedures performed between January 2014 and August 2024 — all managed with an identical local hemostatic protocol (gelatin sponge plus 4-0 Vicryl suture) — 87 postoperative bleeding events were recorded, an incidence of 4.35%. Four algorithms (logistic regression, random forest, eXtreme gradient boost, K-nearest neighbors) were trained on 1600 procedures and tested on the remaining 400, which contained 17 bleeders; a senior oral surgeon with more than 15 years of experience assessed the same 400 cases.

On univariate testing only dual antithrombotic therapy raised bleeding risk significantly (20/213, p<0.001); monotherapy class, triple therapy, sex, age, surgical region, and number of teeth removed by extraction or osteotomy were all non-significant. On the test set, every algorithm exceeded the surgeon on balanced accuracy (KNN 0.616, XGB 0.608, RF 0.591, LR 0.580 vs surgeon 0.527). The clinically interesting finding is the asymmetry of error, not the ranking: the surgeon flagged 97 of 400 procedures as likely bleeders when only 17 bled, producing 92 false positives — consistent with the authors' prior observation that most patients preventively admitted for bleeding risk never bleed.

The result should be read narrowly. Balanced accuracy in the 58–62% band is only modestly above the 50% chance line, the best AUC was 0.671, and the highest-sensitivity model (KNN, 0.529) still missed 8 of 17 bleeders. The authors themselves interpret AUC 0.62 as evidence of substantial unmeasured heterogeneity, and explicitly state that clinicians should never rely solely on ML output, since decisions about prolonged observation or preventive hospitalization hinge on unstructured factors — the patient's home environment, independence, anxiety, and care needs — that no structured dataset captures.

## Key Contributions

- First application of machine learning to complication prediction after oral surgery (authors' claim), specifically post-extraction bleeding under antithrombotic medication.
- Direct head-to-head benchmark of four algorithm families against a single senior oral surgeon on an identical held-out test set, rather than a model-only performance report.
- Quantifies surgeon over-prediction of bleeding risk: 97 predicted bleeders vs 17 actual, i.e. 92 false positives — an empirical handle on the cost of defensive preventive admission.
- Confirms dual antithrombotic therapy as the sole significant univariate risk factor in a 2000-procedure cohort, while showing that this group-level signal does not translate into reliable individual-level prediction.
- Documents a 4.35% bleeding incidence — far below the 10.4–23% range in comparable literature — and attributes it to universal gelatin sponge use, then reasons about how that low event rate itself degrades predictability.

## Methodology

- **Design**: single-centre retrospective clinical study (centralized chart review) plus supervised ML benchmark; RWTH Aachen ethics approval EK 24-353.
- **Setting/period**: University Hospital RWTH Aachen, dental extractions January 2014 – August 2024.
- **N**: 2000 procedures; 7125 teeth removed (6607 simple extraction, 518 osteotomy). Mean age 68.5 years (SD ±13.5); 1305 male (65.3%) / 695 female (34.7%).
- **Medication distribution (Table 1)**: monotherapy 1778 — antiplatelet 670, VKA 328, heparin 233 (LMWH 184 + UFH 49), DOAC 547; dual therapy 213; triple therapy 9. *(The abstract instead states monotherapy 1788 / dual 426 / triple 27; only the Table 1 split sums to 2000 and is used here.)*
- **Exclusions**: age <18, no antithrombotic medication, inherited bleeding disorder, incomplete postoperative documentation (missing bleeding data or 10-day follow-up), non-extraction intraoral procedures (biopsy, root resection).
- **Standardized hemostasis, all cases**: gelatin sponge (Gelastypt, Sanofi-Aventis) into the alveolus + 4-0 Vicryl suture (Ethicon). Uniform across the cohort, therefore not a study variable but a cohort-wide confounder.
- **Outcome**: binary — any documented postoperative bleeding requiring clinical attention, irrespective of severity; no severity grading applied.
- **Features**: sex, age at procedure, medication type, number of teeth removed by extraction vs osteotomy, region (anterior / posterior / both).
- **Sample size**: G*Power 3.1.9.6 (alpha 0.05, effect size 0.1, power 95%) → minimum 1135 procedures; raised to 2000 to offset the bleeding-lowering effect of routine gelatin sponge use. Anchored on Yagyuu et al. (10.4% DOAC, 12% VKA).
- **Statistics**: Chi-square / Fisher's exact (categorical), Wilcoxon-Mann-Whitney (continuous, non-Gaussian per Shapiro-Wilk); p<0.05.
- **ML protocol**: random 80/20 split (1600 train / 400 test); LR, RF, XGB, KNN trained on the training set and evaluated on the test set; senior oral surgeon (>15 years) independently assessed the same test set. Metrics: balanced accuracy (primary), accuracy with 95% CI, sensitivity, specificity, AUC, Brier score.

## Results

**Cohort-level bleeding**: 87/2000 procedures (4.35%). Test set: 17/400 (4.25%).

**Univariate risk factors** — only dual therapy significant:

| Factor | Bleeders / total | p |
|---|---|---|
| Monotherapy — antiplatelet | 19 / 670 | 0.072 (across monotherapy classes) |
| Monotherapy — VKA | 12 / 328 | " |
| Monotherapy — heparin (LMWH+UFH) | 6 / 233 | " |
| Monotherapy — DOAC | 30 / 547 | " |
| **Dual therapy** | **20 / 213 (9.4%)** | **<0.001** |
| Triple therapy | 0 / 9 | 1.000 |
| Sex (M 62/1305, F 25/695) | — | 0.251 |
| Mean age (68.4 vs 69.7 y) | — | 0.361 |
| Location (ant / post / both) | 9/265, 44/1009, 34/735 | 0.735 |
| Teeth removed by extraction (3.3 vs 3.8) | — | 0.376 |
| Teeth removed by osteotomy (0.3 vs 0.3) | — | 0.359 |

**Prediction performance on the 400-procedure test set (17 true bleeders)**:

| Model / assessor | Balanced accuracy | Accuracy (95% CI) | Sensitivity | Specificity | AUC | Brier | TP | FP | FN |
|---|---|---|---|---|---|---|---|---|---|
| KNN | **0.616** | 0.70 (0.65–0.74) | 0.529 | 0.702 | 0.623 | 0.042 | 9 | 114 | 8 |
| XGB | 0.608 | 0.84 (0.80–0.88) | 0.353 | 0.864 | 0.646 | 0.042 | 6 | 52 | 11 |
| RF | 0.591 | 0.81 (0.77–0.85) | 0.353 | 0.830 | **0.671** | 0.043 | 6 | 65 | 11 |
| LR | 0.580 | 0.90 (0.86–0.92) | 0.235 | 0.924 | 0.624 | 0.041 | 4 | 29 | 13 |
| Senior surgeon | 0.527 | 0.74 (0.69–0.78) | 0.294 | 0.760 | — | — | 5 | 92 | 12 |

- **Error asymmetry**: the surgeon predicted 97 bleeders in total against 17 actual. KNN traded the most false positives (114) for the most true positives (9); XGB was the cost-efficiency optimum (52 false positives at balanced accuracy 0.608); LR was the most conservative (29 false positives but only 4 of 17 bleeders caught).
- **Every assessor missed the majority of bleeders**: false negatives ranged from 8 (KNN) to 13 (LR), with the surgeon at 12.
- **Incidence in context**: 4.35% here vs Yanamoto 17.4%, Ueda 19%, and 10.4–23% elsewhere; closest match is Svensson et al. at 4% with an absorbable gelatin sponge in warfarin patients, supporting the authors' attribution of the low rate to universal local hemostasis.
- **AUC in context**: the authors compare their best AUC (0.62 for KNN) with dental ML studies at 0.86 (direct pulp capping), 0.97 (extraction decision support), and 0.55 (mucoepidermoid carcinoma survival), and read 0.62 as substantial unexplained heterogeneity.

### Limitations and interpretive caution

- **Balanced accuracy of 58–62% is only modestly above chance (50%).** "All four algorithms outperformed the surgeon" is a narrow claim about ranking on this single-centre retrospective dataset — **not** evidence that machine learning is ready to guide clinical bleeding decisions, to triage patients to inpatient observation, or to override surgical judgement. This page should not be read as endorsing algorithmic triage.
- **The event rate is low (4.35%), so the test set contains very few positive events** — 17 bleeders, yielding true-positive counts of 4–9. Sensitivity and balanced accuracy estimates at this scale are highly unstable, and no confidence interval is reported for balanced accuracy at all.
- **No external validation**: one centre, one dataset, no independent institutional or temporal validation cohort. Generalizability is untested.
- **The human comparator is a single clinician** performing a chart-based assessment, acknowledged by the authors as a bias source in either direction. It measures one surgeon's paper judgement, not chairside clinical decision-making.
- **Universal gelatin sponge use is a cohort-wide confounder**: it suppressed the event rate, strengthening internal validity but compressing the signal available to the models and limiting transfer to settings without routine local hemostasis.
- **Published numerical inconsistency**: the abstract gives monotherapy 1788 / dual 426 / triple 27 (does not sum to 2000); the Results text and Table 1 give 1778 / 213 / 9 (sums correctly). Anterior-only procedures are 256 in the text vs 265 in Table 1.
- **Coarse features and binary outcome**: no data on incisions, preoperative inflammation, or operating surgeon experience; dual/triple therapy not subdivided by drug combination; minor oozing and bleeding requiring re-suturing or admission are pooled into one outcome, so a "predicted bleed" carries no information about consequence.
- **Authors' own position**: ML output is complementary only; decisions about prolonged observation or preventive hospitalization depend on non-quantifiable factors (home environment, independence, anxiety, care needs) absent from structured data.

## Related Papers

- [[drug/anticoagulants/krishnan-2024-bleeding-uninterrupted-single-dual-antiplatelet]] — reinforces: both compare single- vs dual-agent antithrombotic regimens for post-extraction bleeding; this 2000-procedure cohort independently confirms dual therapy as the one significant risk factor (9.4% vs ~3–5% under monotherapy).
- [[drug/anticoagulants/moldovan-2023-anticoagulant-oral-surgery-bleeding-sr]] — refines: the SR establishes group-level bleeding risk under anticoagulation; this study adds the boundary condition that knowing those risk factors still does not permit reliable individual-level prediction (best balanced accuracy 62%, best AUC 0.671).
- [[oral-surgery/dinkova-2025-local-hemostasis-oral-surgery-review]] — applies-to: the standardized gelatin sponge + suture protocol applied to all 2000 procedures here is credited by the authors with the unusually low 4.35% bleeding incidence, a large real-world instance of the local hemostasis principle.
- [[drug/anticoagulants/kim-2024-post-extraction-bleeding-direct-oral-anticoagulants]] — Korean DOAC cohort reporting a comparable 4.9% bleeding rate under continued therapy with local hemostatic management.
- [[drug/anticoagulants/yong-2022-dapt-dental-extraction-umbrella-review]] — umbrella review of dual antiplatelet therapy at extraction, the regimen class that drove the only significant signal here.
