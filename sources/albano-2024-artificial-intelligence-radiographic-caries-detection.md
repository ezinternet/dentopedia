---
title: "Artificial intelligence for radiographic imaging detection of caries lesions: a systematic review"
authors: "Domenico Albano, Vanessa Galiano, Mariachiara Basile, Filippo Di Luca, Salvatore Gitto, Carmelo Messina, Maria Grazia Cagetti, Massimo Del Fabbro, Gianluca Martino Tartaglia, Luca Maria Sconfienza"
year: 2024
doi: "10.1186/s12903-024-04046-7"
category: [artificial-intelligence]
source_collection: pubmed-text
full_text: true
pmid: "38402191"
pmcid: "PMC10894487"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10894487/
text_path: /Users/oracleneo/llm-wiki/papers/albano-2024-artificial-intelligence-radiographic-caries-detection.txt
text_filename: albano-2024-artificial-intelligence-radiographic-caries-detection.txt
---

## Why Ingested

Adds a QUADAS-2–graded systematic review restricted to **radiographic** caries detection (20 studies, PROSPERO CRD42023470708) that refines and independently contextualizes the pooled SR+MA of [[artificial-intelligence/abbott-2024-ai-platforms-dental-caries-detection]] — it partitions performance by imaging modality (periapical/bitewing/OPG) and by algorithm family (ANN/CNN/DCNN), showing where the meta-analytic averages come from and how heterogeneous (and mostly small) the underlying datasets are. It also parallels the imaging-based radiolucent-lesion detection work in [[artificial-intelligence/sadr-2022-deep-learning-periapical-radiolucent-lesions]].

## One-line Summary

Systematic review (PRISMA/QUADAS-2, 20 studies, 6346 radiographs) of AI models for radiographic caries-lesion detection: sensitivity 0.44–0.86, specificity 0.85–0.98, accuracy 0.73–0.98, AUC 0.84–0.98, F1 0.64–0.92; CNNs dominate (70%) and most studies were low risk of bias, but datasets were small/heterogeneous so no meta-analysis was possible.

## 한줄요약

방사선 우식 병소 검출용 AI 모델을 다룬 체계적 문헌고찰(PRISMA/QUADAS-2, 20편·영상 6346장): 민감도 0.44–0.86, 특이도 0.85–0.98, 정확도 0.73–0.98, AUC 0.84–0.98, F1 0.64–0.92로 대체로 우수했고 CNN이 70%를 차지·대부분 낮은 비뚤림 위험이었으나, 데이터셋이 작고 이질적이라 메타분석은 불가능했다.

## 1. Document Information

- **Type**: Systematic review (PRISMA-guided; no meta-analysis feasible), QUADAS-2 quality appraisal.
- **Journal**: BMC Oral Health 2024;24(1):274.
- **Registration**: PROSPERO CRD42023470708.
- **Search**: PubMed, Web of Science, SCOPUS, LILACS, Embase (+ OpenGrey, WONDER gray literature), inception to January 2023, English only.
- **Screening yield**: 2660 records → 1364 duplicates removed → 70 full-text assessed → **20 included**.
- **Aim**: Evaluate diagnostic performance of AI models designed for caries-lesion (CL) detection on dental radiographs.

## 2. Key Contributions

1. First systematic synthesis focused specifically on **radiographic** (not clinical/photographic/NIRI) AI caries detection, stratified by imaging modality and by AI architecture.
2. Modality breakdown: **5 periapical, 9 bitewing, 6 orthopantomography (OPG)** studies; total 6346 images (per-study 15–2900).
3. Architecture breakdown: **4 ANN, 15 CNN (~70%), 2 DCNN** (text elsewhere states 14 CNN — see note in §4); confirms CNN dominance in the field.
4. QUADAS-2 appraisal across 4 domains (patient selection, index test, reference standard, flow & timing): **most studies low risk of bias**, few high risk.
5. Positions AI as an *assistive* tool (workload reduction, help for less-experienced examiners) rather than a replacement for the dentist/radiologist.

## 3. Methodology and Architecture

- **Design types included**: 12 retrospective cohort, 6 cross-sectional, 2 prospective (two of the prospective/interventional labeled RCT in Table 1 — Devlin 2021, Mertens 2021).
- **Index test**: AI/DL model on dental radiograph. **Reference standard**: radiograph assessment by expert dentists.
- **Inclusion**: original diagnostic-accuracy studies reporting training/validation/test datasets, human participants, English, ethics approval/consent. **Exclusion**: insufficient data, <10 images, reviews/guidelines/consensus/editorials/letters/abstracts.
- **AI families represented**: ANN (incl. BPNN), CNN (GoogLeNet Inception-v3, U-Net/nnU-Net, Faster R-CNN, VGG-16, ResNet, YOLO, AlexNet, CariesNet, AssistDent, Diagnocat), DCNN.
- **Planned meta-analysis** (random-effects, mean difference with 95% CI, I² heterogeneity, RevMan 5.3) **could not be executed** due to too few comparable studies and high heterogeneity (differing networks, datasets, and outcome metrics).

## 4. Key Results and Benchmarks

Pooled performance ranges (descriptive only, per-metric study counts in parentheses):

| Metric | Range | Mean ± SD | Median | n studies |
|---|---|---|---|---|
| Sensitivity | 0.44–0.86 | 0.75 ± 0.13 | 0.75 | 11 |
| Specificity | 0.83–0.98 | 0.90 ± 0.07 | 0.88 | 5 |
| Precision | 0.50–0.94 | 0.73 ± 0.17 | 0.72 | 4 |
| Accuracy | 0.73–0.98 | 0.89 ± 0.08 | 0.91 | 10 |
| AUC | 0.84–0.98 | 0.92 ± 0.04 | 0.88 | 8 |
| F1-score | 0.64–0.92 | ~0.80 ± 0.09 | 0.83 | 6 |
| IoU | 0.3–0.4 and 0.78 | — | — | 2 |
| Dice | 0.66 and 0.88 | — | — | 2 |
| PPV / NPV | 0.86 / 0.95 | — | — | 1 each |

- Abstract reports specificity from 0.85; the Results text gives the low end as 0.83 (Cantu 2020). The architecture count is stated as "15 CNN" in the abstract/results summary but "14 CNN" in one Results paragraph — a minor internal inconsistency; either way CNN ≈ 70%.
- Standout single studies: Zhu 2022 (CariesNet, 124 OPG) Dice 0.93 / accuracy 0.93 / F1 0.92 / precision 0.94; Geetha 2020 (BPNN) accuracy 0.97, FP 0.02; De Araujo Faria 2021 accuracy/AUC 0.98 (only 15 OPG); Bayraktar 2022 (YOLO, interproximal) sensitivity 0.72, specificity 0.98, PPV 0.86, NPV 0.95, accuracy 0.94. Low end: Zadrozny 2022 (Diagnocat) sensitivity 0.44, specificity 0.98.
- Several studies reported AI matching or exceeding experienced dentists/specialists (Bayrakdar 2021 VGG-16/U-Net; Moran 2021; Mertens 2021 RCT).
- **QUADAS-2**: most studies low risk of bias across the four domains, few high risk.

## 5. Limitations and Future Work

- **No meta-analysis** possible — small (as few as 15 images), heterogeneous datasets; heterogeneous networks and outcome metrics.
- English-only search; mixed study designs and AI types pooled descriptively.
- Datasets often from a single device/institution (e.g., Lian 2021 single OPG unit) → external-validity concern.
- Many models could not classify caries **depth/location** (enamel vs dentin).
- Future work: large, comparable, clinically meaningful multi-center datasets; standardized reference standards and metrics; model-architecture optimization; the human user remains the ultimate decision-maker.

## 6. Related Work

- AI as diagnostic aid rather than replacement; FDA-cleared products cited (Videa Caries Assist: 0.43 fewer undetected CLs, 0.15 fewer misdiagnoses regardless of dentist experience).
- Bitewing established as best modality for interproximal caries; nearly half the included studies used bitewings.
- Economic justification of AI caries detection (Mohammad-Rahimi et al.).

## 7. Glossary

- **CL** — Caries Lesion.
- **ANN** — Artificial Neural Network (incl. BPNN, back-propagation NN).
- **CNN** — Convolutional Neural Network (GoogLeNet Inception-v3, U-Net, Faster R-CNN, VGG-16, ResNet, YOLO, AlexNet, CariesNet, etc.).
- **DCNN** — Deep (convolutional) Neural Network.
- **QUADAS-2** — Quality Assessment of Diagnostic Accuracy Studies, v2 (4 domains: patient selection, index test, reference standard, flow & timing).
- **AUC** — Area Under the (ROC) Curve.
- **IoU** — Intersection over Union (segmentation overlap).
- **Dice** — Dice/Sørensen similarity coefficient (segmentation overlap).
- **F1-score** — harmonic mean of precision and recall.
- **PPV / NPV** — Positive / Negative Predictive Value.
- **OPG** — Orthopantomography (panoramic radiograph).
