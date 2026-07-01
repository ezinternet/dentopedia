---
title: "Artificial intelligence for radiographic imaging detection of caries lesions: a systematic review"
authors: "Domenico Albano et al."
year: 2024
date: 2024-02-24
doi: "10.1186/s12903-024-04046-7"
source: albano-2024-artificial-intelligence-radiographic-caries-detection.md
category: [artificial-intelligence]
confidence: sr
source_collection: pubmed-text
full_text: true
pmid: "38402191"
pmcid: "PMC10894487"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10894487/
text_path: /Users/oracleneo/llm-wiki/papers/albano-2024-artificial-intelligence-radiographic-caries-detection.txt
text_filename: albano-2024-artificial-intelligence-radiographic-caries-detection.txt
tags: [artificial-intelligence, deep-learning, CNN, caries-detection, radiography, QUADAS-2, systematic-review]
relations:
  - type: refines
    target: abbott-2024-ai-platforms-dental-caries-detection
---

## One-line Summary

Systematic review (PRISMA/QUADAS-2, 20 studies, 6346 radiographs) of AI models for radiographic caries-lesion detection — sensitivity 0.44–0.86, specificity 0.85–0.98, accuracy 0.73–0.98, AUC 0.84–0.98, F1 0.64–0.92; CNNs dominate (~70%) and most studies were low risk of bias, but small/heterogeneous datasets precluded meta-analysis.

## 한줄요약

방사선 우식 병소 검출 AI 모델의 체계적 문헌고찰(PRISMA/QUADAS-2, 20편·영상 6346장) — 민감도 0.44–0.86, 특이도 0.85–0.98, 정확도 0.73–0.98, AUC 0.84–0.98, F1 0.64–0.92, CNN 약 70%·대부분 낮은 비뚤림 위험이었으나 데이터셋이 작고 이질적이라 메타분석은 불가능했다.

## Summary

Albano et al. systematically reviewed the diagnostic performance of AI models for detecting caries lesions (CL) on dental radiographs. From 2660 records (inception–January 2023), 20 studies met eligibility. Across modalities and architectures, AI achieved good-to-excellent performance, with several studies reporting AI matching or exceeding experienced dentists. However, datasets were small (as few as 15 images) and heterogeneous, no meta-analysis was feasible despite planning one, and results are presented descriptively. The authors frame AI as an assistive tool — reducing workload and helping less-experienced examiners — not a replacement for the clinician, who remains the ultimate decision-maker.

## Key Contributions

- First systematic review focused specifically on **radiographic** AI caries detection, stratified by **imaging modality** (periapical / bitewing / OPG) and by **AI architecture** (ANN / CNN / DCNN).
- QUADAS-2 quality appraisal: **most studies low risk of bias**, few high risk.
- Confirms CNN dominance (~70% of studies) and reports the field's per-metric performance envelope.
- Notes real-world context: FDA-cleared products (e.g., Videa Caries Assist — 0.43 fewer undetected CLs, 0.15 fewer misdiagnoses regardless of dentist experience) and economic justification of AI caries detection.

## Methodology

- **Design**: PRISMA-guided systematic review, PROSPERO CRD42023470708; databases PubMed, Web of Science, SCOPUS, LILACS, Embase + gray literature (OpenGrey, WONDER); English only, inception–Jan 2023.
- **Included designs**: 12 retrospective, 6 cross-sectional, 2 prospective (2 labeled RCT in Table 1: Devlin 2021, Mertens 2021).
- **Index test**: AI/DL model on radiograph; **reference standard**: expert-dentist radiograph assessment.
- **Inclusion**: original diagnostic-accuracy studies reporting train/validation/test datasets, ≥10 images, human participants. **Quality**: QUADAS-2 (patient selection, index test, reference standard, flow & timing).
- A random-effects meta-analysis (RevMan 5.3, mean difference / 95% CI, I²) was planned but **could not be performed** due to too few comparable studies and high heterogeneity.

## Results

- **20 studies** included: **5 periapical, 9 bitewing, 6 OPG**; total **6346 radiographs**, per-study range **15–2900**.
- **Architectures**: **4 ANN, 15 CNN (~70%), 2 DCNN** (one Results paragraph states 14 CNN — minor internal inconsistency; CNN ≈ 70% either way). Architectures span GoogLeNet Inception-v3, U-Net/nnU-Net, Faster R-CNN, VGG-16, ResNet, YOLO, AlexNet, CariesNet, AssistDent, Diagnocat, BPNN.
- **Performance ranges** (descriptive):

| Metric | Range | Mean ± SD | Median | n |
|---|---|---|---|---|
| Sensitivity | 0.44–0.86 | 0.75 ± 0.13 | 0.75 | 11 |
| Specificity | 0.85–0.98 (Results text: 0.83) | 0.90 ± 0.07 | 0.88 | 5 |
| Precision | 0.50–0.94 | 0.73 ± 0.17 | 0.72 | 4 |
| Accuracy | 0.73–0.98 | 0.89 ± 0.08 | 0.91 | 10 |
| AUC | 0.84–0.98 | 0.92 ± 0.04 | 0.88 | 8 |
| F1-score | 0.64–0.92 | ~0.80 ± 0.09 | 0.83 | 6 |
| IoU | 0.3–0.4 and 0.78 | — | — | 2 |
| Dice | 0.66 and 0.88 | — | — | 2 |
| PPV / NPV | 0.86 / 0.95 | — | — | 1 |

- **Standouts**: Zhu 2022 (CariesNet, 124 OPG) Dice 0.93 / accuracy 0.93 / F1 0.92 / precision 0.94; Bayraktar 2022 (YOLO, interproximal) sens 0.72, spec 0.98, PPV 0.86, NPV 0.95, accuracy 0.94; Geetha 2020 (BPNN) accuracy 0.97, FP 0.02; De Araujo Faria 2021 accuracy/AUC 0.98 (15 OPG). **Low end**: Zadrozny 2022 (Diagnocat) sens 0.44, spec 0.98.
- Several studies (Bayrakdar 2021, Moran 2021, Mertens 2021 RCT) reported AI matching or exceeding experienced dentists/specialists.
- **QUADAS-2**: most studies low risk of bias; few high risk.
- **Key limitations**: small/heterogeneous datasets (as few as 15 images), single-device/institution sources, inability of many models to classify caries depth/location (enamel vs dentin). Bitewing highlighted as the best modality for interproximal caries; AI especially valuable for less-experienced examiners.

## Related Papers

- [[artificial-intelligence/abbott-2024-ai-platforms-dental-caries-detection]] — refines: this QUADAS-2 SR (radiographs only, no pooling) decomposes by modality and architecture the pooled AI-caries-detection performance that Abbott's SR+MA aggregates, showing the small, heterogeneous datasets behind the meta-analytic averages.
- [[artificial-intelligence/sadr-2022-deep-learning-periapical-radiolucent-lesions]] — reinforces: parallel deep-learning imaging-detection task (periapical radiolucent lesions), sharing the CNN/AUC evaluation paradigm and the assistive-tool framing.
