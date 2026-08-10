---
title: "Accuracy of artificial intelligence in orthodontic extraction treatment planning: a systematic review and meta analysis"
authors: Ziaei S, Samani D, Behjati M, Ravari AO, Salimi Y, Ahmadi S, Rajaei S, Alimohammadi F, Raji S, Deravi N, Fakhimi H
year: 2025
doi: "10.1186/s12903-025-06880-9"
category: [artificial-intelligence]
source_collection: pubmed-text
full_text: true
pmid: "41068732"
pmcid: "PMC12512631"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12512631/
text_path: /Users/oracleneo/llm-wiki/papers/ziaei-2025-ai-orthodontic-extraction-treatment-planning-sr-ma.txt
text_filename: ziaei-2025-ai-orthodontic-extraction-treatment-planning-sr-ma.txt
---

## Why Ingested

The wiki's `artificial-intelligence` category holds 15 pages and every one of them evaluates AI at a **detection** task (caries, lesions, periodontal bone loss, cephalometric landmarks). This SR+MA is one of the very few papers evaluating AI at an actual **treatment decision** — whether to extract — which is a categorically harder and more consequential judgment than flagging a lesion on an image. It also directly complicates the reference-standard problem already surfaced in [[wiki/practice-management/dufey-portilla-2026-treatment-decision-making-apical-periodontitis-clinician-groups]]: that paper shows human clinicians disagree sharply on extraction decisions, and this paper's own PICO explicitly defines the "ground truth" AI is graded against as "conventional assessments by clinicians" — so a pooled sensitivity of 70% here is agreement with a moving target, not accuracy at a fixed one.

## Three-line Summary

PRISMA/PROSPERO (CRD42024582455) SR+MA, searches to 2 June 2025: 7 cross-sectional studies, 6 countries, 6,261 patients, of AI models predicting orthodontic extraction vs. non-extraction against clinicians' actual decisions as the reference standard.

Pooled sensitivity 70% (95% CI 61–78), specificity 90% (95% CI 87–92); I² = 96.7% (sensitivity) and 93.7% (specificity); CNN-based models (ResNet, VGG) had the highest and only zero-heterogeneity subgroup performance (sensitivity 0.758–0.824, specificity 0.931–0.941); meta-regression found disease prevalence significantly predicted sensitivity (p=0.050); funnel plots showed asymmetry consistent with possible publication bias.

The authors conclude AI "can be used to create predictive models for orthodontic extractions to increase accuracy," but a 70% pooled sensitivity (CI down to 61%) means the model misses roughly 3 in 10 patients who need extraction — not a result that supports that recommendation as stated.

## 세줄요약

PRISMA/PROSPERO(CRD42024582455) 체계적 문헌고찰+메타분석(2025년 6월 2일까지 검색): 교정 발치 여부를 예측하는 인공지능(Artificial Intelligence, AI) 모델 7편(6개국, 환자 6,261명, 횡단면 연구), 기준(reference standard)은 임상의의 실제 결정.

통합 민감도(Sensitivity) 70%(95% 신뢰구간(Confidence Interval, CI) 61–78), 통합 특이도(Specificity) 90%(95% CI 87–92); 이질성(Heterogeneity) I²=96.7%(민감도)·93.7%(특이도); 합성곱 신경망(Convolutional Neural Network, CNN) 기반 모델(ResNet·VGG)만 이질성 0%로 가장 높고 일관된 성능(민감도 0.758–0.824, 특이도 0.931–0.941); 메타회귀분석에서 질환 유병률이 민감도에 유의한 영향(p=0.050); 깔때기그림(Funnel Plot) 비대칭 — 출판 편향 가능성.

저자들은 AI가 "교정 발치 예측 모델로 정확도를 높이는 데 사용될 수 있다"고 결론짓지만, 민감도 70%(CI 하한 61%)는 발치가 필요한 환자 10명 중 약 3명을 놓친다는 뜻이라 이 결론을 그대로 뒷받침하지 못한다.

## 1. Document Information

- **Type**: Systematic review + meta-analysis (FULL TEXT, PMC).
- **Journal**: BMC Oral Health 2025;25(1):1576. PROSPERO CRD42024582455.
- **PMID**: 41068732 · **PMCID**: PMC12512631 · **DOI**: [10.1186/s12903-025-06880-9](https://doi.org/10.1186/s12903-025-06880-9)
- **Search**: PubMed, Scopus, Web of Science, Google Scholar, up to 2 June 2025.
- **PICO**: P = patients undergoing orthodontic treatment planning; I = AI-based extraction-prediction models; C = conventional assessment by clinicians; O = sensitivity/specificity.

## 2. Key Contributions

- One of the few dental-AI SR+MAs evaluating a **treatment decision** (extract vs. not) rather than image-based detection — a harder, more consequential task than the caries/lesion/cephalometric-landmark detection papers that make up the rest of the `artificial-intelligence` category.
- Reports the sensitivity/specificity **asymmetry** explicitly (70% vs. 90%) rather than a single blended accuracy figure, surfacing that these models are much better at confirming non-extraction than at catching extraction cases.
- Subgroup analysis by model architecture isolates CNN-based models (ResNet, VGG) as the only zero-heterogeneity, higher-performing subgroup — the pooled headline numbers are an average across architectures of very different quality.
- Meta-regression links disease (extraction) prevalence in the training/test population to reported sensitivity, flagging a generalizability risk baked into the pooled estimate.

## 3. Methodology and Architecture

- 7 cross-sectional studies (2021–2024), 6 countries (India, USA ×2, Chile, China, South Korea, Germany), n=6,261 combined (per-study range 192–1,636).
- AI models: CNN-based (ResNet-50/101, VGG16/19), Random Forest, Multilayer Perceptron, Decision Tree, SVM, Auto-WEKA.
- JBI Critical Appraisal Checklist for Analytical Cross-Sectional Studies; quality scores 6/8–8/8 (moderate–high); no study excluded on quality grounds.
- Random-effects model for pooled sensitivity/specificity with 95% CI; I² for heterogeneity; subgroup analysis by model type; mixed-effects meta-regression for prevalence effect on sensitivity; funnel plots for publication-bias inspection; leave-one-out sensitivity analysis.
- Reference standard against which AI predictions were graded: **clinicians' actual extraction decisions** (stated directly in the PICO "Comparison" arm as "conventional assessments by clinicians").

## 4. Key Results and Benchmarks

- Pooled sensitivity 0.70 (95% CI 0.61–0.78); pooled specificity 0.90 (95% CI 0.87–0.92).
- Heterogeneity: I² = 96.7% (sensitivity), 93.7% (specificity).
- Subgroup by model type: CNN(ResNet) sensitivity 0.758/specificity 0.941 (I²=0%); CNN(VGG) sensitivity 0.824/specificity 0.931 (I²=0%); Random Forest sensitivity 0.731/specificity 0.724 (I²=91.1%/78.5%); MLP sensitivity 0.797/specificity 0.794 (I²=97.2%/88.0%); Other sensitivity 0.754/specificity 0.882 (I²=98.7%/94.5%).
- Meta-regression: disease prevalence significantly associated with sensitivity (β=0.9923, p=0.050).
- Funnel plots: visual asymmetry for both sensitivity and specificity, interpreted as possible publication bias.
- Leave-one-out analysis: pooled sensitivity estimate robust to removal of any single study.
- Individual-study range: specificity 0.44–0.97; sensitivity 0.31–0.94 — extreme study-to-study spread underlying the pooled figures.

## 5. Limitations and Future Work

- **Small k (7 studies)**: limits statistical power and makes the funnel-plot asymmetry / publication-bias finding itself weakly grounded — funnel-plot bias tests are conventionally considered unreliable below ~10 studies. The concern is still worth flagging (AI research under-publishes negative results), but the test result should not be over-read.
- **Extreme heterogeneity (I² 93.7–96.7%)** means the pooled sensitivity/specificity are averages across incommensurable models and datasets; the authors' own subgroup analysis shows the CNN-only figures (I²=0%) are the more interpretable and internally consistent result.
- **Cross-sectional design only** across all 7 included studies — no prospective validation, no patient outcomes, no data on what happened to patients whose AI-predicted decision diverged from the clinician's.
- **Reference standard is the clinician's own decision**, not a validated ground truth of correct treatment — the paper does not interrogate whether the human decisions it is grading against are themselves reliable or consistent (a question [[wiki/practice-management/dufey-portilla-2026-treatment-decision-making-apical-periodontitis-clinician-groups]] answers negatively for a related extraction decision: extraction propensity varies ~4-fold by clinician type).
- **Sensitivity/specificity asymmetry is not discussed as a clinical-deployment risk** by the authors — a 70%-sensitivity model used as a screening aid would systematically under-flag extraction cases, and those false negatives would concentrate in exactly the borderline cases where clinical judgment is hardest.
- **Small number of countries and geographically narrow evidence base** limits generalizability despite the 6-country spread.
- Authors' own conclusion ("can be used to create predictive models... to increase accuracy") is stated without qualifying the 61% lower-bound CI on sensitivity or the extreme heterogeneity — a stronger caveat is warranted before any clinical-implementation reading.

## 6. Related Work

- [[wiki/artificial-intelligence/alabdulkareem-2026-ai-dental-treatment-planning-decision-making-sr-ma]] — sibling SR+MA (27 studies, 60,857 images) on AI **detection** performance (pooled sensitivity 0.85, specificity 0.94). Direct contrast: AI detects considerably better than it decides (0.85 vs. 0.70 sensitivity) — the two papers together bound where AI optimism in dental-AI SRs applies.
- [[wiki/practice-management/dufey-portilla-2026-treatment-decision-making-apical-periodontitis-clinician-groups]] — 431-clinician vignette study showing generalists are significantly more extraction-prone than specialists (OR 4.37, p<0.001) for a related extraction decision. Undercuts treating "agreement with the clinician" as a fixed, reliable ground truth for this paper's AI models.
- Evangelista et al. (cited in Discussion) — prior SR+MA of 6 studies reporting overall accuracy 0.87 (95% CI 0.75–0.96) for AI in orthodontic extraction decision-making, but flagged as very-low-certainty evidence; broadly consistent direction with this paper's own low-certainty read.
- [[wiki/artificial-intelligence/hendrickx-2024-ai-cephalometric-analysis-manual-tracing]] — same category, contrasting **measurement** task (landmark detection, pooled MRE 1.39mm, below the 2mm clinical threshold) rather than a decision task; illustrates that AI performance in orthodontics is not uniform across task type.

## 7. Glossary

- **Sensitivity**: proportion of patients who actually needed extraction that the AI model correctly flagged; here 70% (95% CI 61–78) pooled — meaning roughly 3 in 10 true-extraction patients were missed.
- **Specificity**: proportion of patients who did not need extraction that the AI model correctly did not flag; here 90% (95% CI 87–92).
- **I² statistic**: percentage of total variation across studies due to heterogeneity rather than chance; >90% here indicates the pooled estimate averages over substantially different model/population combinations.
- **Meta-regression**: statistical technique used here to test whether disease (extraction) prevalence in a study's sample predicts the sensitivity that study reports.
- **Funnel plot asymmetry**: visual/statistical indicator sometimes used to infer publication bias — small-study effects can produce apparent asymmetry even absent true bias, so with only 7 studies this signal is weak on its own.
