---
title: "Automated Classification of Maxillary Sinus Ostium Patency Using a ConvNeXt-Tiny + DeiT Gated MLP-Based Hybrid Deep Learning Model: A Retrospective CBCT Study"
authors: Talo F, Duger N, Aslan E, Yildirim M, Kaya M, Ozer AB, Yildirim TT
year: 2026
date: 2026-05-16
doi: 10.3390/diagnostics16101512
source: talo-2026-maxillary-sinus-ostium-patency-deep-learning.md
category: [artificial-intelligence]
evidence_level: retrospective
source_collection: pubmed-text
full_text: true
pmid: "42196878"
pmcid: "PMC13205894"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13205894/
text_path: /Users/oracleneo/llm-wiki/papers/talo-2026-maxillary-sinus-ostium-patency-deep-learning.txt
text_filename: talo-2026-maxillary-sinus-ostium-patency-deep-learning.txt
tags: [deep-learning, maxillary-sinus-ostium, ostium-patency, cbct, convnext, vision-transformer, sinus-lift-planning]
relations:
  - type: applies-to
    target: akbari-2022-maxillary-sinus-mucosal-thickening-ridge-height
---

## Three-line Summary

Retrospective single-center CBCT study (704 images: 477 open / 227 closed) training a ConvNeXt-Tiny + DeiT gated-MLP hybrid deep-learning classifier for maxillary sinus ostium patency assessment, motivated by the low inter-observer reliability (κ as low as 0.399) of manual CBCT interpretation.

The proposed model achieved 95.03% test accuracy, F1 94.18%, and MCC 89.67 — substantially outperforming the best single-backbone baseline (89.36%) and misclassifying only 7 of 141 test images; the gated fusion mechanism (not the backbone choice) was the critical improvement.

Clinically the model is framed as a preoperative screening aid for sinus-lift planning, but external multi-center validation, linkage to postoperative sinusitis outcomes, and assessment of narrowing degree are absent; the dataset is small, imbalanced, and from a single device.

## 세줄요약

단일기관 후향 CBCT 연구(704장: 개방 477/폐쇄 227)에서 상악동 자연공(ostium) 개폐 판별의 낮은 판독자 간 신뢰도(일치도 κ 최저 0.399)를 해결하기 위해 ConvNeXt-Tiny + DeiT 게이트-MLP 하이브리드 딥러닝 분류기를 개발·검증했다.

제안 모델은 테스트 정확도 95.03%·F1 94.18%·매튜스 상관계수(Matthews Correlation Coefficient, MCC) 89.67로 최고 단일-백본 기준(89.36%)을 능가했으며, 7/141장만 오분류했다; 단순 연결+MLP 융합(90.07%) 대비 게이팅 기전이 결정적 향상 요인이었다.

임상적으로 상악동 거상술 전 CBCT 선별 보조도구로 제안되나, 다기관 외부 검증·수술 후 부비동염 결과와의 연계·협착 정도 평가가 없고 단일 장비·소규모 불균형 데이터셋이라는 한계가 있다.

## Summary

The maxillary sinus ostium is the opening that drains and ventilates the sinus into the middle nasal meatus. Before a sinus lift or posterior-maxilla implant, a narrowed or occluded ostium is a risk marker: elevation of the Schneiderian membrane provokes mucosal thickening/inflammation, and if drainage is compromised the patient can develop acute/chronic maxillary sinusitis, graft loss, and implant failure (reported sinusitis incidence after sinus lift 4.2–8.4%). Human assessment of ostium "open vs. closed" on CBCT is subjective, with inter-observer agreement reported as low as 0.399 — motivating an objective decision-support model.

Talo et al. built a hybrid deep-learning classifier that fuses a CNN backbone (ConvNeXt-Tiny, local features) and a Vision-Transformer backbone (DeiT, global context) through a **gated MLP** fusion layer that learns how much to weight each backbone's features. On a 704-image CBCT dataset (477 open, 227 closed) labeled by three periodontologists (intra-observer ICC ≥0.93, inter-observer ICC ≥0.92), the proposed model reached **95.03% test accuracy, 94.18% F1, MCC 89.67, and a 4.96% error rate** — the best of all configurations, misclassifying only 7 of the test images. The gating mechanism was the key ingredient: plain concatenation + MLP fusion of the same two backbones reached only 90.07%. The authors frame the tool as a screening/prioritization aid for preoperative CBCT review, not a replacement for the clinician.

## Key Contributions

- **First hybrid CNN+ViT model for ostium-patency classification** on CBCT; the only close prior work is Shetty et al. (ResNet101V2 for accessory ostium, 81% accuracy).
- **Gated MLP fusion** dynamically weights ConvNeXt-Tiny vs. DeiT features, lifting accuracy from 90.07% (plain MLP fusion) to 95.03% and halving errors (14 → 7 misclassified).
- **Clinically framed** as preoperative decision support for sinus-lift/implant planning, targeting the documented low inter-observer reliability (κ/agreement as low as 0.399) of manual ostium assessment.

## Methodology

- **Design**: retrospective, single-center (Firat University, Turkey), diagnostic deep-learning classification.
- **Data**: 500 CBCT scans (ProMax 3D Mid, 90 kVp/8 mA, 0.4 mm voxel) → 704 PNG images (477 open / 227 closed), labeled by three periodontology experts. Excellent intra-observer (ICC 0.9418, 0.9321) and strong inter-observer (ICC 0.9315, 0.9251) reliability.
- **Architecture**: 3 stages — feature extraction (ConvNeXt-Tiny via global average pooling + DeiT token vectors) → gated feature fusion (learnable gates) → MLP classification head with softmax.
- **Backbone choice**: top CNN (ConvNeXt-Tiny) and top ViT (DeiT) selected after benchmarking ResNet50, DenseNet121, ConvNeXt-Tiny, ViT-B/16, DeiT, Swin.
- **Split**: 72% train / 8% val / 20% test, stratified. Metrics: macro-averaged precision/recall/NPV, accuracy, F1, MCC, error rate. Trained on Google Colab (NVIDIA Tesla T4).

## Results

| Model | Test accuracy | Misclassified |
|---|---|---|
| ViT-B/16 | 83.68% | 23 |
| ResNet50 | 86.52% | 19 |
| Swin | 86.52% | 19 |
| DeiT | 87.94% | 17 |
| DenseNet121 | 89.36% | 15 |
| ConvNeXt-Tiny | 89.36% | 15 |
| ConvNeXt-Tiny + DeiT (plain MLP fusion) | 90.07% | 14 |
| **ConvNeXt-Tiny + DeiT Gated MLP (proposed)** | **95.03%** | **7** |

- Proposed model: accuracy 95.03%, F1 94.18%, MCC 89.67, error rate 4.96% — highest across all metrics.
- The gated fusion (not the backbones alone) drove the gain: 90.07% → 95.03%.
- **Limitations**: single center / single device, small imbalanced dataset (~2:1 open:closed), slice-level binary label only (no localization or degree of narrowing), no linkage to actual postoperative sinusitis outcomes. Authors plan multi-center validation.

## Related Papers

- [[sinus-lift/lateral/akbari-2022-maxillary-sinus-mucosal-thickening-ridge-height]] — applies-to: both are preoperative CBCT sinus risk markers; ostium patency (this paper) and mucosal thickening (Akbari) are the two anatomical predictors of postoperative sinusitis/graft failure that a clinician screens before a sinus lift.
- [[artificial-intelligence/demir-2024-artificial-intelligence-dental-lesion-detection]] — same dental-AI CBCT diagnostic-performance line; extends AI lesion/anomaly detection to a specific sinus-drainage anatomical target.
