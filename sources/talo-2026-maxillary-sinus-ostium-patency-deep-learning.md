---
title: "Automated Classification of Maxillary Sinus Ostium Patency Using a ConvNeXt-Tiny + DeiT Gated MLP-Based Hybrid Deep Learning Model: A Retrospective CBCT Study"
authors: Talo F, Duger N, Aslan E, Yildirim M, Kaya M, Ozer AB, Yildirim TT
year: 2026
doi: 10.3390/diagnostics16101512
category: [artificial-intelligence]
source_collection: pubmed-text
full_text: true
pmid: "42196878"
pmcid: "PMC13205894"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13205894/
text_path: /Users/oracleneo/llm-wiki/papers/talo-2026-maxillary-sinus-ostium-patency-deep-learning.txt
text_filename: talo-2026-maxillary-sinus-ostium-patency-deep-learning.txt
---

## Why Ingested

A hybrid CNN+ViT model that automatically classifies maxillary sinus ostium patency (open/closed) on CBCT — ostium patency is clinically critical to assess before sinus lift/implant, since a narrowed or occluded ostium disrupts mucociliary drainage and predisposes to postoperative sinusitis, bone graft loss, and implant failure. This connects the AI-in-dentistry diagnostic-performance line to the sinus-ostium/drainage anatomy that governs sinus-lift risk, complementing the mucosal-thickening evidence in [[sinus-lift/lateral/akbari-2022-maxillary-sinus-mucosal-thickening-ridge-height]] (ostium patency ↔ mucosal thickening, both preoperative CBCT risk markers) and extending the dental-AI CBCT lesion-detection line of [[artificial-intelligence/demir-2024-artificial-intelligence-dental-lesion-detection]].

## Three-line Summary

Retrospective single-center CBCT study (704 images: 477 open / 227 closed ostium) proposing a ConvNeXt-Tiny + DeiT gated-MLP hybrid deep-learning model that classifies maxillary sinus ostium patency at 95.03% test accuracy (F1 94.18%, MCC 89.67, error 4.96%), beating the best pre-trained baseline (DenseNet121/ConvNeXt-Tiny, 89.36%).

(incomplete)

(incomplete)

## 세줄요약

단일기관 후향 CBCT 연구(704장: 개방 477/폐쇄 227)로, ConvNeXt-Tiny + DeiT 게이트-MLP 하이브리드 딥러닝 모델이 상악동 자연공(ostium) 개폐를 테스트 정확도 95.03%(F1 94.18%, MCC 89.67, 오류율 4.96%)로 분류해 최고 사전학습 기준모델(DenseNet121/ConvNeXt-Tiny, 89.36%)을 능가했다.

(incomplete)

(incomplete)

## 1. Document Information

- **Title**: Automated Classification of Maxillary Sinus Ostium Patency Using a ConvNeXt-Tiny + DeiT Gated MLP-Based Hybrid Deep Learning Model: A Retrospective CBCT Study
- **Authors**: Talo F, Duger N, Aslan E, Yildirim M, Kaya M, Ozer AB, Yildirim TT
- **Journal**: Diagnostics (Basel), 2026;16(10):1512
- **Published**: 2026-05-16
- **DOI**: 10.3390/diagnostics16101512
- **PMID**: 42196878 | **PMCID**: PMC13205894
- **Study type**: Retrospective single-center diagnostic AI / deep-learning classification study (CBCT)
- **Source**: PubMed Central full text (retrieved via PubMed MCP)

## 2. Key Contributions

1. **Novel task framing**: Automatic binary classification of maxillary sinus ostium patency (open vs. closed) on CBCT slices — an AI application that is "quite limited in the literature" (only prior work: Shetty et al. accessory-ostium detection, ResNet101V2, 81% accuracy).
2. **Hybrid architecture**: Fuses a CNN backbone (ConvNeXt-Tiny, local/low-level features) with a Vision-Transformer backbone (DeiT, global contextual relationships) via a **gated MLP fusion** mechanism that dynamically weights each backbone's features.
3. **Performance gain from gating**: Gated fusion lifts accuracy from 90.07% (plain concatenation + MLP) to **95.03%**, halving misclassified test images (14 → 7).
4. **Clinical motivation grounded in ostium physiology**: Positions the model as a decision-support tool for preoperative sinus-lift/implant planning, given documented low inter-observer agreement (as low as 0.399) in human ostium-patency assessment.

## 3. Methodology and Architecture

- **Data**: 500 CBCT scans (Firat University Faculty of Dentistry, Jan 2019–Sep 2025), ProMax 3D Mid (Planmeca), 90 kVp / 8 mA, 8–9 s exposure, 0.4 mm voxel. Yielded a **704-PNG dataset (477 open, 227 closed)** labeled by three periodontology experts.
- **Reliability**: Intra-observer ICC 0.9418 & 0.9321 (excellent); inter-observer ICC 0.9315 & 0.9251 (strong), on a 40-section subset re-read at 2 weeks.
- **Inclusion**: clearly identifiable/measurable maxillary sinus ostium; no age/sex/clinician restriction. **Exclusion**: low-quality images (exposure errors, artifacts, overlay, distortion).
- **Model (3 stages)**: (1) feature extraction — ConvNeXt-Tiny (global average pooling → feature vector) + DeiT (token representations → feature vector); (2) **gated feature fusion** — learnable gate functions weight each backbone's contribution, suppressing weak features; (3) MLP classification head with softmax.
- **Backbone selection**: ResNet50, DenseNet121, ConvNeXt-Tiny, ViT-B/16, DeiT, Swin were each evaluated; the top CNN (ConvNeXt-Tiny) and top ViT (DeiT) by test accuracy were chosen as backbones.
- **Split**: 72% train / 8% validation / 20% test (80–20 split, then 10% of train for validation), stratified sampling to preserve class balance.
- **Metrics**: macro-averaged precision, recall, NPV; accuracy; F1; MCC; error rate; confusion matrices.
- **Compute**: Google Colaboratory, NVIDIA Tesla T4 GPU.

## 4. Key Results and Benchmarks

Pre-trained baseline test accuracies (single-backbone):

| Model | Test accuracy | Misclassified (of test set) |
|---|---|---|
| DenseNet121 | 89.36% | 15 |
| ConvNeXt-Tiny | 89.36% | 15 |
| DeiT | 87.94% | 17 |
| ResNet50 | 86.52% | 19 |
| Swin | 86.52% | 19 |
| ViT-B/16 | 83.68% | 23 |

Ablation → proposed model:

| Configuration | Test accuracy | Misclassified |
|---|---|---|
| ConvNeXt-Tiny (baseline) | 89.36% | 15 |
| DeiT (baseline) | 87.94% | 17 |
| ConvNeXt-Tiny + DeiT (plain MLP fusion) | 90.07% | 14 |
| **ConvNeXt-Tiny + DeiT Gated MLP (proposed)** | **95.03%** | **7** |

- Proposed model: **accuracy 95.03%, F1 94.18%, MCC 89.67, error rate 4.96%** — highest of all models tested.
- The gated fusion (vs. plain MLP concatenation) is credited with the jump from 90.07% → 95.03%, by dynamically weighting distinctive ConvNeXt/DeiT features.
- Positive correlations among accuracy, F1, MCC; strong negative correlation of error rate with the others (metric-consistency check).

## 5. Limitations and Future Work

- **Single-center data** (one institution, one CBCT device/protocol) — external/multi-region generalizability untested.
- **Small sample / class imbalance** — 704 images, 477 open vs. 227 closed (~2:1), no explicit rebalancing beyond stratified splitting.
- **Slice-level binary label only** — classifies ostium open/closed on selected slices; no segmentation, localization, or degree-of-narrowing output; no direct linkage to actual postoperative sinusitis outcomes.
- **Decision support, not replacement** — authors frame it as a screening/prioritization aid, not a substitute for clinician judgment.
- **Future work**: multi-center datasets to test robustness.

## 6. Related Work

- **Shetty et al.** — accessory maxillary ostium (AMO) detection on CBCT with ResNet101V2, 81% accuracy (the main prior AI-ostium study); also concha bullosa detection with pre-trained models.
- **Esmaeilyfard et al.** — cystic-lesion detection on CBCT using CNN architectures.
- **Yang et al.** — maxillary sinus segmentation and bone-graft analysis with a 2D U-Net on CBCT.
- Broader CNN/ViT literature on maxillary sinus segmentation and pathology detection.

## 7. Glossary

- **Maxillary sinus ostium**: opening at the top of the sinus medial wall connecting it to the middle nasal meatus; the sinus drainage/ventilation pathway. Narrowing/occlusion → impaired mucociliary clearance → sinusitis risk.
- **Ostium patency**: whether the ostium is open (patent) or closed (obstructed).
- **CBCT**: cone-beam computed tomography; 3D dental imaging with low radiation dose and high spatial resolution.
- **ConvNeXt-Tiny**: modernized CNN architecture; here the local-feature backbone.
- **DeiT** (Data-efficient image Transformer): Vision Transformer variant; here the global-context backbone.
- **ViT** (Vision Transformer): transformer-based image model that learns long-range relationships.
- **Gated fusion / gated MLP**: fusion mechanism using learnable gate functions to dynamically weight features from each backbone before the classification head.
- **MCC** (Matthews correlation coefficient): balanced classification metric using all confusion-matrix components.
- **ICC** (intraclass correlation coefficient): inter-/intra-observer reliability measure.
- **Schneiderian membrane**: sinus mucosal lining elevated during sinus-lift surgery.
