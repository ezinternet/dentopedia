---
title: "Accuracy of artificial intelligence in orthodontic extraction treatment planning: a systematic review and meta analysis"
authors: Ziaei S, Samani D, Behjati M, Ravari AO, Salimi Y, Ahmadi S, Rajaei S, Alimohammadi F, Raji S, Deravi N, Fakhimi H
year: 2025
date: 2025-10-09
doi: "10.1186/s12903-025-06880-9"
source: ziaei-2025-ai-orthodontic-extraction-treatment-planning-sr-ma.md
category: [artificial-intelligence]
evidence_level: sr+ma
source_collection: pubmed-text
full_text: true
pmid: "41068732"
pmcid: "PMC12512631"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12512631/
text_path: /Users/oracleneo/llm-wiki/papers/ziaei-2025-ai-orthodontic-extraction-treatment-planning-sr-ma.txt
text_filename: ziaei-2025-ai-orthodontic-extraction-treatment-planning-sr-ma.txt
tags: [ai, deep-learning, cnn, orthodontics, extraction-decision, treatment-planning, diagnostic-accuracy, cross-sectional]
relations:
  - type: refines
    target: alabdulkareem-2026-ai-dental-treatment-planning-decision-making-sr-ma
  - type: applies-to
    target: dufey-portilla-2026-treatment-decision-making-apical-periodontitis-clinician-groups
---

## Three-line Summary

SR+MA (PRISMA/PROSPERO CRD42024582455; search to 2 June 2025) of AI models predicting orthodontic extraction vs. non-extraction: 7 cross-sectional studies, 6 countries, 6,261 patients, graded against clinicians' actual extraction decisions as the reference standard.

Pooled sensitivity 70% (95% CI 61–78) and specificity 90% (95% CI 87–92), with extreme heterogeneity (I² = 96.7% and 93.7%); CNN-based models (ResNet, VGG) were the only zero-heterogeneity, highest-performing subgroup (sensitivity 0.758–0.824); disease prevalence significantly predicted sensitivity (meta-regression p=0.050); funnel plots showed asymmetry consistent with publication bias.

A 70% pooled sensitivity means these models miss roughly 3 of every 10 patients who genuinely need extraction — the authors' conclusion that AI "can be used to create predictive models... to increase accuracy" is not supported by a result this weak and this heterogeneous, and cross-sectional-only evidence with no patient outcomes means none of this has been validated prospectively.

## 세줄요약

> [!summary] 한국어 핵심요약
> - PRISMA/PROSPERO(CRD42024582455) 체계적 문헌고찰+메타분석(2025-06-02까지 검색): 교정 발치 여부를 예측하는 인공지능(Artificial Intelligence, AI) 모델 7편(6개국, 환자 6,261명, 전부 횡단면 연구).
> - **기준(reference standard)은 임상의의 실제 발치 결정** — AI가 "정답"과 비교되는 것이 아니라 논쟁적인 인간의 판단과 비교된다.
> - **통합 민감도(Sensitivity) 70%(95% CI 61–78)** — 발치가 필요한 환자 10명 중 약 **3명을 놓친다**는 뜻. 통합 특이도(Specificity) 90%(95% CI 87–92)로 비발치 확인은 잘하고 발치 검출은 약함 — 비대칭 실패 양상.
> - 이질성(Heterogeneity) 극단적: I²=96.7%(민감도)·93.7%(특이도) — 통합치는 서로 다른 모델·데이터셋의 평균일 뿐 대표성이 낮음.
> - 합성곱 신경망(Convolutional Neural Network, CNN) 기반 모델(ResNet·VGG)만 이질성 0%로 가장 높고 일관된 성능(민감도 0.758–0.824, 특이도 0.931–0.941) — 하위그룹 결과가 더 해석 가능함.
> - 메타회귀분석: 발치 유병률이 민감도에 유의한 영향(p=0.050) — 훈련 데이터의 발치 비율이 높을수록 민감도가 높게 보고되는 경향, 일반화 가능성 우려.
> - 깔때기그림(Funnel Plot) 비대칭 — 출판 편향 가능성 시사하나, 연구 7편은 이 검정을 신뢰하기엔 적은 수(관례상 ~10편 미만은 불안정).
> - **저자 결론("정확도를 높이는 예측 모델로 사용 가능")은 이 수치가 뒷받침하지 못한다** — CI 하한 61%, 극단적 이질성, 발치 결정처럼 임상의도 서로 갈리는 판단(하한 근거: [[practice-management/dufey-portilla-2026-treatment-decision-making-apical-periodontitis-clinician-groups]])을 "정답"으로 삼은 근본적 한계.
> - 전부 **횡단면 설계**만 — 전향적 검증·환자 예후 데이터 없음.
> - 위키 내 대비: 같은 저자군 도메인의 **검출(detection)** 과제([[artificial-intelligence/alabdulkareem-2026-ai-dental-treatment-planning-decision-making-sr-ma]], 민감도 0.85)는 이 논문의 **결정(decision)** 과제(민감도 0.70)보다 뚜렷이 우수 — AI는 "본다"는 훨씬 잘하고 "결정한다"는 상대적으로 약함.

## Summary

According to PubMed, Ziaei et al. (2025, BMC Oral Health) conducted a PRISMA-guided SR+MA (PROSPERO CRD42024582455) asking whether AI models can accurately predict the need for orthodontic extraction. Searching PubMed, Scopus, Web of Science, and Google Scholar to 2 June 2025, they included **7 cross-sectional studies from 6 countries, combined n=6,261 patients**. Pooled diagnostic accuracy was **sensitivity 70% (95% CI 61–78)** and **specificity 90% (95% CI 87–92)**, with extreme heterogeneity (**I² = 96.7%** for sensitivity, **93.7%** for specificity). Subgroup analysis by model architecture found **CNN-based models (ResNet, VGG) had the highest and only zero-heterogeneity performance** (sensitivity 0.758–0.824, specificity 0.931–0.941), while Random Forest and MLP models were both weaker and far more heterogeneous (I² 78–98%). Meta-regression found **disease prevalence significantly predicted sensitivity** (β=0.9923, p=0.050). Funnel plots showed visual asymmetry for both metrics, which the authors interpret as possible publication bias. ([DOI](https://doi.org/10.1186/s12903-025-06880-9); PMID 41068732; PMCID PMC12512631)

**The headline is the sensitivity, and the authors undersell it.** A pooled sensitivity of 70%, with a 95% CI reaching down to 61%, means an AI model built this way will miss roughly three of every ten patients who genuinely need extraction. The authors' stated conclusion — that AI "can be used to create predictive models for orthodontic extractions to increase accuracy" — is not supported by a result this weak and this heterogeneous; it should be read as a proof-of-concept finding, not a deployment recommendation.

## Key Contributions

- **The wiki's only decision-task AI paper in a category otherwise built on detection.** All 15 other pages in `artificial-intelligence` evaluate AI at *detecting* something already present in an image — caries, periapical lesions, periodontal bone loss, cephalometric landmarks. This paper evaluates AI at making a *treatment decision* (extract vs. not), which is a categorically harder and more clinically consequential task than flagging a finding. Framing this as "just another AI diagnostic-accuracy SR+MA" would miss what actually makes it worth keeping.
- **Names the asymmetry, not just a blended accuracy figure.** Reporting sensitivity (70%) and specificity (90%) separately — rather than a single "diagnostic accuracy" number — exposes that these models are good at confirming *non*-extraction and comparatively poor at catching extraction cases. That asymmetric failure mode matters clinically: a model used as a screening aid would systematically under-call extraction, and its false negatives would concentrate in exactly the borderline cases where the decision was hardest to begin with — the patients least served by a wrong or absent flag.
- **Subgroup analysis isolates the one interpretable result.** With I² > 93% overall, the pooled headline numbers are averages over largely incommensurable models. The CNN-based (ResNet/VGG) subgroup, by contrast, showed *zero* heterogeneity (I²=0%) and the best performance (sensitivity 0.758–0.824, specificity 0.931–0.941) — this is the number worth trusting more than the pooled 70%/90%.
- **The reference-standard problem.** The paper's own PICO defines its comparator as "conventional assessments by clinicians" — meaning these models are trained and graded to reproduce what a human orthodontist decided, not to produce a validated good outcome. Extraction decisions in orthodontics are themselves contested: [[practice-management/dufey-portilla-2026-treatment-decision-making-apical-periodontitis-clinician-groups]] shows generalist clinicians are roughly 4× more extraction-prone than specialists on a comparable decision. 70% agreement with a reference standard that different clinicians would answer differently is not 70% accuracy at "the right call."

## Methodology

- 7 cross-sectional studies (2021–2024), 6 countries (India, USA ×2, Chile, China, South Korea, Germany); combined n=6,261 (per-study range 192–1,636 patients).
- AI models spanned CNN architectures (ResNet-50/101, VGG16/19), Random Forest, Multilayer Perceptron, Decision Tree, SVM, and automated ML (Auto-WEKA).
- JBI Critical Appraisal Checklist for Analytical Cross-Sectional Studies; quality scores 6/8–8/8 (moderate-to-high); no study excluded on quality grounds.
- Random-effects model for pooled sensitivity/specificity (95% CI); I² for heterogeneity; subgroup meta-analysis by model architecture; mixed-effects meta-regression for the prevalence→sensitivity relationship; funnel plots for publication-bias inspection; leave-one-out sensitivity analysis.
- **Reference standard**: clinicians' actual extraction decisions (explicitly the PICO "Comparison" arm) — not a validated, outcome-based ground truth.

## Results

| Outcome | Result |
|---|---|
| Pooled sensitivity | 70% (95% CI 61–78) — misses ~3/10 true-extraction patients |
| Pooled specificity | 90% (95% CI 87–92) |
| Heterogeneity | I² = 96.7% (sensitivity), 93.7% (specificity) |
| CNN (ResNet) subgroup | Sensitivity 0.758 (0.693–0.822), specificity 0.941 (0.923–0.960), I²=0% |
| CNN (VGG) subgroup | Sensitivity 0.824 (0.767–0.882), specificity 0.931 (0.911–0.951), I²=0% |
| Random Forest subgroup | Sensitivity 0.731, specificity 0.724, I²=91.1%/78.5% |
| MLP subgroup | Sensitivity 0.797, specificity 0.794, I²=97.2%/88.0% |
| Meta-regression | Prevalence significantly predicts sensitivity (β=0.9923, p=0.050) |
| Publication bias | Funnel plots asymmetric (both metrics); weak signal given k=7 (<10) |
| Study design | 100% cross-sectional — no prospective validation, no patient outcomes |

## Related Papers

- [[artificial-intelligence/alabdulkareem-2026-ai-dental-treatment-planning-decision-making-sr-ma]] — sibling SR+MA on AI **detection** (27 studies, 60,857 images; pooled sensitivity 0.85, specificity 0.94, I²>95%). The comparison is the most valuable thing either page can say: AI detects (0.85) considerably better than it decides (0.70) — narrowing where the field's optimism about "AI accuracy" actually applies.
- [[practice-management/dufey-portilla-2026-treatment-decision-making-apical-periodontitis-clinician-groups]] — 431-clinician vignette study showing generalists and students are ~4× more extraction-prone than endodontists (OR 4.37/4.41, both p<0.001) on a comparable extraction decision. Directly undercuts treating "agreement with the clinician" as a fixed ground truth here — if humans disagree by clinician type, the target these AI models are graded against is itself a moving one.
- [[artificial-intelligence/hendrickx-2024-ai-cephalometric-analysis-manual-tracing]] — same category, but a **measurement** task (landmark detection, pooled 2D MRE 1.39mm, below the 2mm clinical threshold) rather than a decision task. The contrast is instructive: AI cephalometric landmarking already clears a clinical bar, while AI extraction-decision support does not — task type, not "AI in orthodontics" as a monolith, is what determines maturity.
