---
title: "Deep learning-based assessment of periapical radiographic image quality"
authors: Xiuting Chi, Mingchao Wang, Yue Gao, Zhipu Ge
year: 2026
doi: 10.1038/s41598-026-35100-9
category: [digital-workflow]
pdf_path: /Users/oracleneo/llm-wiki/papers/chi-2026-deep-learning-periapical-radiograph-quality.pdf
pdf_filename: chi-2026-deep-learning-periapical-radiograph-quality.pdf
source_collection: external
---

## Three-line Summary

Sci Rep 2026 AI development study training 7 ResNet50-based deep learning models (1 multi-class + 6 binary) on 3594 periapical radiographs classified into 10 tooth-position classes and 6 quality defects (vertical angle, horizontal angle, crown coverage, apical coverage, cone cut, scratch) for automated periapical radiograph quality assessment.

The models achieved AUC 0.997 for tooth-position classification and AUC 0.924–1.000 for each of the 6 defect categories, demonstrating excellent discriminative performance across all defect types.

Automated AI quality control could reduce retake rates and minimize patient radiation exposure, but independent multicenter validation is required before clinical deployment.

## 세줄요약

Sci Rep 2026 AI 개발 연구: 3594개 치근단 방사선사진을 치아 위치 10클래스 × 불량 유형 6종(수직 각도·수평 각도·치관 포함·근첨 포함·콘 컷·스크래치)으로 분류하는 ResNet50 기반 딥러닝 모델 7개(다중분류 1+이진 6) 훈련.

치아 위치 분류 AUC 0.997; 6가지 불량 유형 AUC 0.924–1.000 — 전체 불량 유형에서 우수한 판별력.

AI 자동 품질관리로 재촬영률 감소·방사선 피폭 최소화 가능성 있으나, 임상 적용 전 독립적 다기관 검증 필요.

## 1. Key Results
- 3594 periapical radiographs; 10 tooth-position classes; 6 quality defects
- 6 defects: vertical angle, horizontal angle, crown coverage, apical coverage, cone cut, scratch
- 7 ResNet50 models (1 multi-class + 6 binary); data augmentation + oversampling
- AUC: tooth position 0.997; defects 0.924–1.000; excellent overall performance
- Potential to reduce retake rates and minimize patient radiation exposure

## 2. Clinical Implications
- AI can objectively grade periapical radiograph quality at point-of-care
- Real-time feedback during radiograph acquisition can reduce retakes
- Standardizes quality assessment across clinical settings
- Independent multicenter validation required before deployment
