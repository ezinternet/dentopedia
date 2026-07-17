---
title: "Artificial Intelligence in Dental Treatment Planning and Diagnostic Decision-Making: A Systematic Review and Meta-Analysis"
authors: Alabdulkareem M, Atieh M, AbuMostafa A, Aldalaan K, Alturki N
year: 2026
date: 2026-04-01
doi: "10.1002/cre2.70343"
source: alabdulkareem-2026-ai-dental-treatment-planning-decision-making-sr-ma.md
category: [artificial-intelligence]
evidence_level: sr+ma
source_collection: pubmed-text
full_text: true
pmid: "41914450"
pmcid: "PMC13140480"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13140480/
text_path: /Users/oracleneo/llm-wiki/papers/alabdulkareem-2026-ai-dental-treatment-planning-decision-making-sr-ma.txt
text_filename: alabdulkareem-2026-ai-dental-treatment-planning-decision-making-sr-ma.txt
tags: [artificial-intelligence, deep-learning, diagnostic-accuracy, meta-analysis, treatment-planning, YOLO, heterogeneity, GRADE]
relations:
  - type: reinforces
    target: alfaraj-2026-harnessing-ai-prosthodontics-implant-dentistry
  - type: refines
    target: ziaei-2025-ai-orthodontic-extraction-treatment-planning-sr-ma
  - type: reinforces
    target: dufey-portilla-2026-treatment-decision-making-apical-periodontitis-clinician-groups
  - type: reinforces
    target: abbott-2024-ai-platforms-dental-caries-detection
---

## Three-line Summary

Systematic review and meta-analysis (PROSPERO CRD420251240547; PRISMA 2020 + PRISMA-DTA; MEDLINE/Embase/Cochrane CENTRAL/Web of Science/Scopus to Dec 2025) of 27 studies (60,857 radiographic images; 15/27 poolable) evaluating artificial intelligence (AI) for dental diagnostic detection and, nominally, treatment-planning decision-making across specialties (caries, periodontal, periapical, tooth detection/numbering, restorative, structural anomalies).

Pooled random-effects estimates were sensitivity 0.85 (95% CI 0.76–0.91, n=13 studies), specificity 0.94 (0.86–0.97, n=13), F1 0.90 (0.77–0.96, n=11), and precision 0.88 (0.71–0.96, n=11), all GRADE "moderate" certainty; segmentation Dice Similarity Coefficient (DSC) was 0.89 but with a near-uninformative 95% CI of 0.13–1.00 (n=5, GRADE "low"); heterogeneity was I² > 95% on every pooled outcome. YOLO architectures (v5–v12) were the strongest performers for tooth detection/segmentation (sensitivity ~99%, mean average precision (mAP) > 0.96).

Despite the title, only 3/27 studies were rated under the paper's own "Treatment planning support" GRADE category (quality: low), plus 4/27 under interobserver-agreement and 2/27 under diagnostic-time-reduction — all pooled headline metrics (sensitivity/specificity/F1/precision/Dice) come exclusively from image-detection and segmentation studies, not treatment-decision studies; the authors' own limitations (retrospective designs, limited external validation) argue for "rigorous prospective evaluation before widespread clinical implementation" rather than current-day adoption for treatment planning.

## 세줄요약

체계적 문헌고찰(Systematic Review, SR) + 메타분석(Meta-Analysis, MA) (PROSPERO CRD420251240547; PRISMA 2020+PRISMA-DTA; MEDLINE/Embase/Cochrane CENTRAL/Web of Science/Scopus, 2025년 12월까지) — 논문 27편(방사선 영상 60,857장; 정량 풀링 가능 15편)으로 치과 진단 탐지 및 (명목상) 치료계획 의사결정에서 인공지능(Artificial Intelligence, AI) 성능을 다전문과목(우식·치주·치근단·치아탐지/번호·보철·구조이상)에 걸쳐 평가.

무작위효과모형 풀링 결과 민감도(Sensitivity) 0.85(95% CI 0.76–0.91, 13편), 특이도(Specificity) 0.94(0.86–0.97, 13편), F1 점수 0.90(0.77–0.96, 11편), 정밀도(Precision) 0.88(0.71–0.96, 11편) — 모두 GRADE "중등도(moderate)" 확실성; 분할(segmentation) 다이스 유사도 계수(Dice Similarity Coefficient, DSC)는 0.89였으나 95% CI가 0.13–1.00으로 사실상 정보값이 거의 없음(5편, GRADE "낮음"); 모든 풀링 지표에서 이질성(Heterogeneity, I²) > 95%. YOLO 계열(v5–v12) 아키텍처가 치아 탐지·분할에서 최고 성능(민감도 ~99%, 평균정밀도(mean Average Precision, mAP) > 0.96).

제목과 달리 저자 자신의 GRADE 표에서 "치료계획 지원(Treatment planning support)" 항목으로 평가된 연구는 27편 중 단 3편(근거 질: 낮음)뿐이고, 관찰자간 일치도 4편·진단 시간단축 2편이 추가될 뿐 — 풀링된 대표 지표(민감도/특이도/F1/정밀도/DSC)는 전부 영상 탐지·분할 연구에서만 나온 것이지 치료결정 연구가 아니다; 저자들 스스로도 후향적 설계·외부검증 부족을 한계로 지목하며 "광범위한 임상 도입 전 엄격한 전향적 평가"를 요구한다.

## Summary

According to PubMed, this systematic review and meta-analysis ([DOI](https://doi.org/10.1002/cre2.70343); PMID 41914450; PMCID PMC13140480) synthesized 27 studies (60,857 radiographic images across panoramic, periapical, bitewing, CBCT, and intraoral-photograph modalities) to evaluate AI diagnostic accuracy and clinical decision-making impact in dentistry. Fifteen of the 27 studies contributed to quantitative random-effects meta-analysis (generalized linear mixed models with logit transformation, R 4.5.2); the remaining 12 were narrative-synthesis only. Pooled diagnostic-accuracy estimates were high but built almost entirely on detection/segmentation tasks: sensitivity 0.85 (95% CI 0.76–0.91), specificity 0.94 (0.86–0.97), F1 0.90 (0.77–0.96), precision 0.88 (0.71–0.96), and — for segmentation — Dice Similarity Coefficient 0.89 with an extremely wide 95% CI of 0.13–1.00. Heterogeneity was I² > 95% across every pooled outcome, which the authors themselves flag as severely limiting extrapolation of the aggregate figures to any single AI system or clinical setting. YOLO-family architectures (v5 through v12) achieved the strongest, most consistent results, with sensitivities approaching 99% and mAP exceeding 0.96 for tooth detection/segmentation. Decision-making-adjacent findings — AI-assisted improvements in clinician sensitivity (60.7%→85.9% in one dataset), interobserver kappa (e.g., caries ~0.585–0.590→0.713–0.726; periapical periodontitis ~0.563–0.623→0.740–0.752), and a ~35-fold reduction in per-image interpretation time (53.8 s → 1.5 s) — are real but rest on a small subset of studies (GRADE Table 1: interobserver agreement n=4, time reduction n=2, treatment-planning support n=3, all rated low-to-low/moderate certainty). The authors conclude AI shows strong diagnostic performance for tooth detection, segmentation, and pathology identification, but that substantial heterogeneity, retrospective designs, and limited external validation mean rigorous prospective evaluation is needed before widespread clinical implementation — notably, this caution is stronger than what the abstract's headline pooled numbers alone would suggest.

**Note on an internal inconsistency in the source**: the paper's own Conclusion cites pooled "specificity of 0.96, accuracy of 0.92, and... AUC of 0.93" — none of these three figures appear anywhere in the Results section or GRADE Table 1, which report pooled specificity as 0.94 and never compute a pooled accuracy or pooled AUC at all. This wiki page reports only the values that are actually traceable to Results/GRADE Table 1; the Conclusion's higher figures are not used and should be treated as a reporting inconsistency in the source article, reproduced verbatim in `papers/` but not treated as additional evidence here.

## Key Contributions

- **A primary-study SR+MA, not an umbrella review** — unlike [[artificial-intelligence/alfaraj-2026-harnessing-ai-prosthodontics-implant-dentistry]] (11 SRs, 261 primary studies, prosthodontics/implant scope, AMSTAR-2 + narrative synthesis), this paper pools 27 primary studies directly with GLMM random-effects meta-analysis and GRADE certainty ratings, extending quantitative pooling beyond prosthodontics/implants into caries, periodontal, periapical, tooth-detection/numbering, and restorative-evaluation tasks.
- **It replicates, rather than overturns, the field's known asymmetry**: image-recognition/segmentation AI performs very well (sensitivity 0.85, specificity 0.94, YOLO ~99% sensitivity for tooth detection) while genuine treatment-decision evidence stays thin — the same "detection strong / outcome-prediction weak" pattern alfaraj-2026 found for implant prognosis (62.4–80.5% accuracy, rated "emerging" readiness). This paper's own GRADE table quantifies that thinness directly: only 3/27 studies rated for "treatment planning support," quality "low."
- **The one genuinely decision-relevant number**: a clinician-in-the-loop dataset (Leemput et al., cited within this paper) showed AI assistance raised individual-radiologist sensitivity from 60.7% to 85.9% (specificity fell slightly, 94.5%→92.7%) and localization-ROC AUC from 0.60 to 0.86 — a rare instance in the dental-AI literature of measuring AI's effect on a human decision-maker's performance rather than the algorithm's standalone accuracy.
- **Honest self-critique embedded in the paper**: GRADE-downgraded certainty for every pooled estimate due to I² > 95%, an admission that the Dice CI (0.13–1.00) reflects "substantial uncertainty" rather than a usable pooled value, and a Limitations section naming retrospective designs and limited external validation as reasons to defer "widespread clinical implementation."
- **What this page adds beyond the existing artificial-intelligence category**: a cross-specialty, primary-study-level pooled diagnostic-accuracy estimate with GRADE certainty (new), plus explicit documentation of how little of the reviewed evidence base (3/27 studies) actually measures treatment-planning impact — a caution the title alone does not convey and prior pages ([[artificial-intelligence/abbott-2024-ai-platforms-dental-caries-detection]], caries-only; [[artificial-intelligence/garg-2026-artificial-intelligence-pediatric-dentistry-umbrella-review]], pediatric-only) did not have occasion to state at this cross-specialty scale.

## Methodology

- **Design**: Systematic review + diagnostic-accuracy meta-analysis. PROSPERO CRD420251240547. PRISMA 2020, PRISMA-DTA, and Cochrane DTA methodology.
- **PICOS**: Patients of any age undergoing dental imaging/diagnostic assessment/treatment planning across all specialties; AI/ML/DL algorithms for diagnosis or treatment-planning support; comparator = reference standard/human clinicians (diagnostic-accuracy studies) or usual clinician decision-making without AI (decision-impact studies); outcomes = sensitivity, specificity, AUC, precision, recall, F1, accuracy, DOR, plus decision-making outcomes (treatment-plan changes, kappa/ICC, time-to-decision, clinician confidence, patient outcomes where reported).
- **Databases/search**: MEDLINE (PubMed), Embase, Cochrane CENTRAL, Web of Science, Scopus, inception to 15 Dec 2025; grey literature via Google Scholar (first 200 results/term combination). No language/date restriction; non-English articles translated. Reference-list and citation-tracking supplementation.
- **Selection**: 2326 records identified (PubMed 935, Scopus 960, Cochrane 87, Embase 70, Web of Science 274) → 1487 duplicates removed → 839 screened (title/abstract) → 785 excluded → 54 sought for full text (100% retrieved) → 27 excluded at full-text stage (12 no independent validation, 8 reviews/editorials/opinion, 7 non-clinical technical) → **27 studies included**; 15/27 quantitatively poolable, 12/27 narrative-only.
- **Quality appraisal**: QUADAS-2 for diagnostic-accuracy studies; ROBINS-I for non-randomized studies; GRADE for outcome-level certainty of evidence. Two independent reviewers + third-reviewer arbitration; Cohen's kappa for inter-rater screening agreement.
- **Statistics**: Random-effects meta-analysis of proportions via generalized linear mixed models (GLMM) with logit transformation (PLOGIT) and maximum-likelihood tau²; `meta`/`metafor`/`ggplot2` in R 4.5.2. Significance p<0.05; heterogeneity threshold p<0.10 for Cochran's Q. Publication bias via funnel plot + Egger's test (meta-analyses with ≥10 studies); trim-and-fill if bias suspected.
- **Risk of bias findings**: ROBINS-I — low risk across D2–D7 for all studies; D1 (confounding) unassessable ("no information") for every study due to insufficient reporting; isolated "some concern" flags for outcome measurement (1 study) and missing data (2 studies). QUADAS-2 — patient-selection domain mostly "unclear" (unreported consecutive/random sampling) but case-control designs avoided; index-test, reference-standard, and flow/timing domains all low risk.

## Results

| Outcome (GRADE Table 1) | Studies (n) | Pooled effect (95% CI) | Heterogeneity (I²) | GRADE certainty |
|---|---|---|---|---|
| Detection — sensitivity | 13 | 0.85 (0.76–0.91) | 95.4% | Moderate |
| Detection — specificity | 13 | 0.94 (0.86–0.97) | 99.2% | Moderate |
| Detection — F1 score | 11 | 0.90 (0.77–0.96) | 99.4% | Moderate |
| Detection — precision | 11 | 0.88 (0.71–0.96) | 99.3% | Moderate |
| Segmentation — Dice Similarity Coefficient | 5 | 0.89 (**0.13–1.00**) | 99.4% | **Low** — CI too wide to be informative |
| Clinical decision support — interobserver agreement | 4 | not calculable | — | Low–Moderate |
| Diagnostic efficiency — time reduction | 2 | not calculable | — | Low |
| **Treatment planning support** | **3** | not calculable | — | **Low** |

Selected task-level findings from narrative synthesis (not all independently poolable):
- YOLO-based tooth detection/segmentation: sensitivity up to 99%, mAP > 0.96; YOLOv10 teeth-staging precision 0.90/recall 0.94/F1 0.919; progressive YOLOv8→v11→v12 precision gains (86.8%→88.5%→89.1%).
- Caries detection: F1 0.82–0.93, sensitivity 81–92%, specificity 82–96%; enamel-caries precision 96% vs dentin-caries precision 80% (same YOLOv8 model — large within-task variance).
- Periapical pathology: sensitivity 67.9–86.6%, specificity 98.3–99.87%; commercial software sensitivities ranged 80.2% (calculus) to 97.1% (crowns).
- Periodontal: ensemble-model accuracy 89.45%; radiographic bone-loss detection 97%; SAM-based CBCT segmentation accuracy 99.65% but sensitivity only 72.36% (systematic conservative bias — high specificity, lower sensitivity, repeated across tasks).
- Decision-impact: clinician sensitivity 60.7%→85.9% with AI assistance (specificity 94.5%→92.7%); interobserver kappa gains of roughly 0.12–0.19 across caries/periapical-periodontitis categories; interpretation time cut ~35-fold (53.8 s → 1.5 s per periapical radiograph, p<0.001).
- Failure modes reported: 3D CBCT implant-planning software failed to output bone-height/thickness measurements in 15.7%/3% of cases; one commercial panoramic tool had specificity >98% but sensitivity only 33.33%.

## Related Papers

- [[artificial-intelligence/alfaraj-2026-harnessing-ai-prosthodontics-implant-dentistry]] — *reinforces*: independent umbrella-review evidence (11 SRs, prosthodontics/implant scope) found the same shape — image-recognition tasks near-mature (~95% pooled accuracy), outcome/prognosis prediction weak (62–80%) and rated "emerging." This SR+MA replicates that asymmetry with quantitative pooling across a broader specialty set, but does not resolve the underlying evidence gap either.
- [[artificial-intelligence/ziaei-2025-ai-orthodontic-extraction-treatment-planning-sr-ma]] *(companion, same ingest batch)* — *refines*: this is the actual treatment-*decision* evidence the present paper's title implies but mostly lacks — AI predicting orthodontic extraction decisions pooled at only 70% sensitivity (95% CI 61–78%), far below this paper's 0.85 pooled *detection* sensitivity. Read together: AI detects findings on images substantially better than it replicates a clinician's treatment decision.
- [[practice-management/dufey-portilla-2026-treatment-decision-making-apical-periodontitis-clinician-groups]] — *reinforces*: shows human clinician groups (GPs/students vs endodontists) disagree substantially on extraction-vs-retention for apical periodontitis — the human baseline this paper's "improved interobserver agreement" finding is implicitly measured against is itself unstable, which both contextualizes and tempers how much credit AI assistance deserves for "agreement improvement."
- [[artificial-intelligence/abbott-2024-ai-platforms-dental-caries-detection]] — *reinforces*: an independent caries-specific SR+MA (45 studies, 21 AI platforms) previously pooled sensitivity 76% (65–85%)/specificity 91% (86–95%) for caries detection alone; this paper's broader multi-specialty pooled sensitivity (0.85) and specificity (0.94) — which include caries detection among the 13 detection studies — are consistent in direction and magnitude, corroborating the caries-detection estimate within a wider cross-specialty context.
