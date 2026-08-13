---
title: "Applied artificial intelligence in dentistry: emerging data modalities and modeling approaches"
authors: "Feher B, Tussie C, Giannobile WV"
year: 2024
doi: "10.3389/frai.2024.1427517"
category: [artificial-intelligence]
pdf_path: /Users/oracleneo/llm-wiki/papers/feher-2024-applied-ai-dentistry-data-modalities.pdf
pdf_filename: feher-2024-applied-ai-dentistry-data-modalities.pdf
source_collection: external
---

## Why Ingested
치과 AI 위키의 개별 SR들([[artificial-intelligence/abbott-2024-ai-platforms-dental-caries-detection]], [[artificial-intelligence/khubrani-2025-periodontal-bone-loss-periodontitis-detection]] 등)이 각 적응증별 성능수치에 집중하는 반면, 데이터 양식(image/numerical/text)과 모델링 패러다임(진단·예후·생성) 전체를 체계적으로 정리한 cross-discipline 리뷰가 없어 인제스트. Giannobile(Harvard) 그룹의 ML 관점 총론.

## One-line Summary
Narrative review (Front Artif Intell 2024, Harvard) covering the spectrum of AI/ML data modalities — image, structured numerical, unstructured text — and three modeling paradigms — diagnostic, prognostic, generative — applied across dental medicine disciplines.

## 한줄요약
서술적 총론(Front Artif Intell 2024, Harvard): 치과 AI/ML을 데이터 양식(영상·수치·텍스트) × 모델링 과제(진단·예후·생성) 행렬로 정리; 한계·미래 방향 포함.

## 1. Document Information
- **Journal**: Frontiers in Artificial Intelligence, vol. 7, article 1427517
- **Publication date**: 2024-07-23
- **Affiliation**: Harvard School of Dental Medicine (Feher, Tussie, Giannobile); Medical University of Vienna (Feher); ITU/WHO/WIPO Global Initiative on AI for Health (Feher)
- **Funding/COI**: Not reported
- **Type**: Narrative review — no meta-analysis or systematic search protocol reported

## 2. Key Contributions
- Provides a **data-modality-first taxonomy** for dental AI, classifying inputs as: (1) image data (radiography, photography, CBCT, CBCT, histology, 3D point clouds), (2) structured numerical data (clinical parameters, billing codes, sensor output), (3) unstructured textual data (clinical notes, EDRs)
- Frames dental AI through three **modeling paradigms**: diagnostic modeling (classification/detection), prognostic modeling (outcome prediction, risk stratification), generative modeling (synthesis, augmentation)
- Highlights dentistry's unique data richness: ~1.1 billion radiographs/year (26% of all radiographic procedures worldwide), high-frequency longitudinal patient contact enabling multimodal longitudinal datasets
- Explains ML learning paradigms (supervised, unsupervised, semi-supervised, reinforcement) and their clinical relevance in a clinician-friendly framework
- Identifies current **gaps**: heterogeneous reporting, small datasets, lack of external validation, insufficient interpretability (black-box problem), regulatory uncertainty

## 3. Methodology and Architecture
- **Design**: Narrative review — ML-perspective cross-discipline overview; no PICO/PRISMA protocol
- **Scope**: All dental disciplines, all ML paradigms, all data modalities
- **Coverage**: Diagnostic modeling (computer vision for radiographs, caries detection, bone loss, implants, cephalometry, oral lesions), prognostic modeling (treatment outcome, periodontal progression, implant failure risk), generative modeling (synthetic data, image augmentation, large language models)
- **Framework**: Three axes — (A) data modality type, (B) learning style, (C) clinical task category

## 4. Key Results and Benchmarks
*Narrative review — no pooled statistics. Key benchmarks cited from included literature:*
- Dental radiographs: ~1.1 billion/year globally; dentistry generates 26% of all radiographic procedures worldwide
- Computer vision (CNN-based) dental AI applications well-established for caries, bone loss, implant classification, cephalometric analysis
- Multimodal longitudinal data (radiograph + EDR + clinical parameters) emerging as highest-value input for prognostic models
- Large language models (LLMs) and generative AI: emerging for clinical note parsing, patient communication, synthetic dataset generation; validation immature
- Black-box interpretability remains the primary adoption barrier in clinical settings; explainable AI (XAI) methods (SHAP, Grad-CAM) increasingly applied

## 5. Limitations and Future Work
- Narrative review without systematic literature search — potential selection bias; no quality assessment of cited studies
- Field evolves faster than review cycles; some cited benchmarks may already be superseded
- LLM/generative AI section necessarily preliminary (field emerged mid-2023 onward)
- External validation and prospective clinical trials remain scarce across nearly all covered applications
- Regulatory pathways (FDA, CE marking) for AI-as-SaMD (Software as Medical Device) not fully addressed

## 6. Related Work
- Abbott 2024 (SR+MA, caries detection AI platforms) — covers one diagnostic modality in depth
- Khubrani 2025 (SR+MA, periodontal bone loss ML) — covers one diagnostic application
- Garg 2026 (SR umbrella, pediatric dentistry AI) — discipline-specific overview
- Herrera 2025 EFP consensus — addresses AI as one of several emerging diagnostic technologies in periodontology

## 7. Glossary
- **Data modality**: Category of input data type — image, structured numerical, or unstructured text
- **Supervised learning**: ML paradigm using labeled training data; learns from input-output pairs
- **Unsupervised learning**: ML paradigm finding patterns in unlabeled data (clustering, dimensionality reduction)
- **Reinforcement learning**: Learning by optimizing a sequence of decisions against a pre-set reward signal
- **Computer vision**: ML branch processing image data; includes classification and regression on pixel features
- **Generative modeling**: AI producing new data instances (synthetic radiographs, augmented datasets, LLM text output)
- **XAI (Explainable AI)**: Methods making model decisions interpretable — SHAP (feature attribution), Grad-CAM (image saliency)
- **SaMD (Software as Medical Device)**: Regulatory classification for AI diagnostic tools requiring FDA/CE approval
- **EDR (Electronic Dental Record)**: Digital patient record containing clinical notes, imaging, billing, treatment history
