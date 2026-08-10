---
title: "Deep learning-based assessment of periapical radiographic image quality"
authors: Xiuting Chi, Mingchao Wang, Yue Gao, Zhipu Ge
year: 2026
date: 2026-01-01
doi: 10.1038/s41598-026-35100-9
source: chi-2026-deep-learning-periapical-radiograph-quality.md
category: [digital-workflow]
evidence_level: retrospective
pdf_path: /Users/oracleneo/llm-wiki/papers/chi-2026-deep-learning-periapical-radiograph-quality.pdf
pdf_filename: chi-2026-deep-learning-periapical-radiograph-quality.pdf
source_collection: external
tags: [deep-learning, AI, periapical-radiograph, image-quality, ResNet50, quality-control, radiation-reduction]
---

## Three-line Summary
Retrospective deep learning study (Sci Rep 2026, 3,594 expert-annotated periapical radiographs) training 7 ResNet50 models — 1 multi-class for 10 tooth positions and 6 binary models for image quality defect detection (vertical/horizontal angle, crown/apical coverage, cone cut, scratch).

AUC performance was excellent across all tasks: tooth position classification AUC 0.997; quality defect detection range AUC 0.924–1.000 (best: horizontal angle and crown coverage = 1.000; lowest: scratch = 0.924).

Automated real-time quality assessment at point-of-care could standardize PA grading, reduce unnecessary retakes, and minimize patient radiation dose through immediate operator feedback.

## 세줄요약
후향적 딥러닝 연구 (Sci Rep 2026, 전문가 주석 치근단 방사선 3,594장): ResNet50 모델 7개 훈련 — 10개 치위 다중분류 1개, 품질 결함(수직/수평각도, 치관/첨부 포함 여부, 코너 절단, 스크래치) 이진분류 6개.

모든 과제에서 우수한 성능: 치위 분류 AUC 0.997; 품질 결함 탐지 AUC 0.924–1.000 (최고: 수평각도·치관 포함 = 1.000; 최저: 스크래치 = 0.924).

포인트 오브 케어에서 자동 실시간 품질 평가를 구현하면 치근단 방사선 평가 표준화, 불필요한 재촬영 감소, 즉각적 피드백을 통한 방사선 피폭 최소화가 가능하다.

## Summary
ResNet50-based deep learning system for automated quality assessment of periapical radiographs across 6 common image defects (vertical/horizontal angle, crown/apical coverage, cone cut, scratch) and 10 tooth positions, validated on 3594 PAs with excellent AUC performance.

## Key Contributions
- **3594 periapical radiographs**; expert annotation for 10 tooth positions + 6 defects
- **7 ResNet50 models**: 1 multi-class (tooth position) + 6 binary (defect detection)
- **AUC performance**: tooth position 0.997; defects range **0.924–1.000**
  - Best: horizontal angle, crown coverage = 1.000
  - Lowest: scratch = 0.924
- Data augmentation + oversampling for class imbalance
- Real-time feedback potential at point-of-care

## Clinical Application
- Standardizes PA quality assessment — reduces examiner subjectivity
- Real-time automated feedback → operator corrects before patient leaves chair
- Reduces unnecessary retakes → lowers patient radiation dose
- Quality improvement program enabled by systematic digital grading

## Related Papers
- [[digital-workflow/park-2023-deep-learning-implant-size-classification]] — DL applied to periapical radiographs for implant identification
- [[digital-workflow/singh-2025-intraoral-scanners-accuracy-umbrella-review]] — digital imaging accuracy context (IOS)
