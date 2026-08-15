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

## Three-line Summary

Narrative review (Frontiers in Artificial Intelligence 2024;7:1427517, Harvard School of Dental Medicine) proposing a data-modality-first taxonomy of dental AI, with no systematic search protocol and no meta-analysis.

Inputs are classified as image data (radiography, photography, CBCT, histology, 3D point clouds), structured numerical data (clinical parameters, billing codes, sensor output) and unstructured text (clinical notes, electronic dental records), crossed with three modeling paradigms — diagnostic, prognostic and generative; the review frames dentistry as unusually data-rich, citing ~1.1 billion dental radiographs per year, 26% of all radiographic procedures worldwide.

Use it as a clinician-facing map of where dental AI inputs come from, not as evidence of performance — the review itself flags heterogeneous reporting, small datasets, scarce external validation, black-box interpretability and unresolved regulatory pathways as the blocking gaps, and its LLM/generative section is necessarily preliminary.

## 세줄요약

서술적 고찰 (Narrative Review — Frontiers in Artificial Intelligence 2024;7:1427517, 하버드 치의학대학원): 체계적 검색 프로토콜이나 메타분석 없이, 치과 인공지능 (Artificial Intelligence, AI)을 **데이터 양식(data modality) 중심**으로 분류하는 체계를 제안.

입력을 영상 데이터(방사선·사진·CBCT·조직학·3D 점군), 정형 수치 데이터(임상 파라미터·청구 코드·센서 출력), 비정형 텍스트(진료기록·전자치과기록)로 나누고 이를 진단·예후·생성이라는 세 모델링 패러다임과 교차시킨다. 치과를 유난히 데이터가 풍부한 분야로 규정하며 연간 약 11억 장의 치과 방사선 촬영, 전 세계 방사선 촬영 건수의 26%를 근거로 든다.

성능의 근거가 아니라 **치과 AI 입력이 어디서 오는지에 대한 임상가용 지도**로 쓸 문헌이다 — 논문 스스로 보고의 이질성, 작은 데이터셋, 부족한 외부 검증, 블랙박스 해석성, 미해결 규제 경로를 병목으로 지목하며, 대규모 언어모델 (Large Language Model, LLM)·생성형 AI 부분은 본질적으로 잠정적이다.

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
