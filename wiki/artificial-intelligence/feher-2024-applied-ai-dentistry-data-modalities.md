---
title: "Applied artificial intelligence in dentistry: emerging data modalities and modeling approaches"
authors: "Feher B et al."
year: 2024
date: 2024-07-23
doi: "10.3389/frai.2024.1427517"
source: feher-2024-applied-ai-dentistry-data-modalities.md
category: [artificial-intelligence]
evidence_level: narrative-review
pdf_path: /Users/oracleneo/llm-wiki/papers/feher-2024-applied-ai-dentistry-data-modalities.pdf
pdf_filename: feher-2024-applied-ai-dentistry-data-modalities.pdf
source_collection: external
tags: [artificial-intelligence, machine-learning, computer-vision, deep-learning, dental-radiography, diagnostic-modeling, prognostic-modeling, generative-ai, data-modalities, llm, explainable-ai]
relations:
  - type: extends
    target: abbott-2024-ai-platforms-dental-caries-detection
  - type: extends
    target: khubrani-2025-periodontal-bone-loss-periodontitis-detection
---

## One-line Summary

Narrative review (Front Artif Intell 2024, Harvard/Vienna) providing a cross-discipline ML-perspective taxonomy of dental AI by data modality (image/numerical/text) and modeling task (diagnostic/prognostic/generative), with current challenges and future directions.

## 한줄요약

서술적 총론(Front Artif Intell 2024, Harvard): 치과 AI/ML을 데이터 양식(영상·수치·텍스트) × 모델링 유형(진단·예후·생성) 행렬로 정리; 치과는 연 11억 장 방사선 영상을 생성해 ML 최적 분야; 한계·미래방향 포함.

## Three-line Summary

Narrative review (Frontiers in Artificial Intelligence 2024;7:1427517, Harvard School of Dental Medicine) proposing a data-modality-first taxonomy of dental AI, with no systematic search protocol and no meta-analysis.

Inputs are classified as image data (radiography, photography, CBCT, histology, 3D point clouds), structured numerical data (clinical parameters, billing codes, sensor output) and unstructured text (clinical notes, electronic dental records), crossed with three modeling paradigms — diagnostic, prognostic and generative; the review frames dentistry as unusually data-rich, citing ~1.1 billion dental radiographs per year, 26% of all radiographic procedures worldwide.

Use it as a clinician-facing map of where dental AI inputs come from, not as evidence of performance — the review itself flags heterogeneous reporting, small datasets, scarce external validation, black-box interpretability and unresolved regulatory pathways as the blocking gaps, and its LLM/generative section is necessarily preliminary.

## 세줄요약

서술적 고찰 (Narrative Review — Frontiers in Artificial Intelligence 2024;7:1427517, 하버드 치의학대학원): 체계적 검색 프로토콜이나 메타분석 없이, 치과 인공지능 (Artificial Intelligence, AI)을 **데이터 양식(data modality) 중심**으로 분류하는 체계를 제안.

입력을 영상 데이터(방사선·사진·CBCT·조직학·3D 점군), 정형 수치 데이터(임상 파라미터·청구 코드·센서 출력), 비정형 텍스트(진료기록·전자치과기록)로 나누고 이를 진단·예후·생성이라는 세 모델링 패러다임과 교차시킨다. 치과를 유난히 데이터가 풍부한 분야로 규정하며 연간 약 11억 장의 치과 방사선 촬영, 전 세계 방사선 촬영 건수의 26%를 근거로 든다.

성능의 근거가 아니라 **치과 AI 입력이 어디서 오는지에 대한 임상가용 지도**로 쓸 문헌이다 — 논문 스스로 보고의 이질성, 작은 데이터셋, 부족한 외부 검증, 블랙박스 해석성, 미해결 규제 경로를 병목으로 지목하며, 대규모 언어모델 (Large Language Model, LLM)·생성형 AI 부분은 본질적으로 잠정적이다.

## Summary

Feher et al. (Harvard School of Dental Medicine / Medical University of Vienna) provide a comprehensive ML-perspective review of applied AI in dentistry, organized around **data modalities** rather than dental disciplines. The three primary data classes are: (1) **image data** — dental radiographs (the largest single source: ~1.1 billion/year, 26% of global radiographic output), intraoral/extraoral photography, CBCT, ultrasonography, histology, and 3D point clouds; (2) **structured numerical data** — clinical parameters, billing records, sensor readings; (3) **unstructured textual data** — clinical notes, electronic dental records (EDRs). Three modeling paradigms are covered: diagnostic (classification/detection), prognostic (outcome prediction, risk stratification), and generative (synthetic data, image augmentation, LLMs). The review emphasizes dentistry's exceptional suitability for ML owing to high-frequency longitudinal patient encounters enabling multimodal dataset construction. Key barriers to clinical adoption are black-box interpretability, small/heterogeneous datasets, absent external validation, and immature regulatory pathways.

## Key Contributions

- **Data-modality taxonomy**: First systematic cross-discipline dental AI framework organized by input type (image/numerical/text) rather than dental specialty — enables clinicians to reason about which AI tool fits their data environment.
- **Scale context**: Quantifies dentistry's radiographic data advantage — 1.1 billion radiographs/year (26% of all worldwide), supporting large-scale supervised training unavailable in most medical specialties.
- **Three-paradigm framework**: Separates diagnostic (detect/classify existing disease), prognostic (predict future outcomes), and generative (create/augment data, parse text) AI — clarifying which clinical questions map to which ML approaches.
- **LLM/generative AI entry**: First major dental AI review to substantively cover large language models for EDR parsing, patient communication, and synthetic dataset generation — situates dentistry within the post-GPT-4 AI landscape.
- **XAI roadmap**: Identifies SHAP and Grad-CAM as leading explainability methods and frames interpretability as the primary adoption bottleneck for clinical AI.

## Methodology

Narrative review; no PICO/PRISMA protocol. Authors at Harvard School of Dental Medicine and Medical University of Vienna. Published in Frontiers in Artificial Intelligence (open access, CC BY). Covers literature through approximately mid-2024. No quality assessment of cited studies; narrative synthesis by topic area.

## Results

No pooled statistics (narrative review). Key benchmarks from cited literature:

| Domain | Representative Finding |
|---|---|
| Dental radiographs | ~1.1 billion/year globally; 26% of all radiographic procedures worldwide |
| Caries detection CNN | High sensitivity/specificity reported; Abbott 2024 SR+MA: sensitivity 76%, specificity 91%, AUC 92% |
| Periodontal bone loss | Khubrani 2025: sensitivity 87%, specificity 76%, accuracy 84% (30 studies) |
| Cephalometric analysis | Hendrickx 2024: mean error 1.39 mm (within 2 mm clinical tolerance) |
| LLM/generative AI | Emerging; clinical validation immature as of 2024 |

## Related Papers

- [[artificial-intelligence/abbott-2024-ai-platforms-dental-caries-detection]] — extends: Feher covers caries detection as one modality; Abbott provides meta-analytic performance data
- [[artificial-intelligence/khubrani-2025-periodontal-bone-loss-periodontitis-detection]] — extends: Feher covers bone loss AI; Khubrani provides SR+MA benchmarks
- [[artificial-intelligence/garg-2026-artificial-intelligence-pediatric-dentistry-umbrella-review]] — extends: Feher provides the cross-discipline framework; Garg applies AI assessment within pediatric dentistry
- [[periodontics/herrera-2025-consensus-report-periodontal-diagnosis]] — reinforces: EFP consensus treats AI as one of several emerging diagnostic tools in periodontology, consistent with Feher's positioning of AI as augmentative
