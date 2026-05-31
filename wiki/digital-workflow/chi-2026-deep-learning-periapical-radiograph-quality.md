---
title: "Deep learning-based assessment of periapical radiographic image quality"
authors: Xiuting Chi, Mingchao Wang, Yue Gao, Zhipu Ge
year: 2026
date: 2026-01-01
doi: 10.1038/s41598-026-35100-9
source: chi-2026-deep-learning-periapical-radiograph-quality.md
category: [digital-workflow]
confidence: retrospective
pdf_path: /Users/oracleneo/llm-wiki/papers/chi-2026-deep-learning-periapical-radiograph-quality.pdf
pdf_filename: chi-2026-deep-learning-periapical-radiograph-quality.pdf
source_collection: external
tags: [deep-learning, AI, periapical-radiograph, image-quality, ResNet50, quality-control, radiation-reduction]
---

## One-line Summary
Retrospective (Sci Rep 2026, 3,594 periapical radiographs): ResNet50 deep learning classification of 6 image quality defects and 10 tooth positions — AUC 0.924–1.000; potential for automated quality assessment, reduced retakes, and minimized radiation exposure.

## 한줄요약
retrospective(Sci Rep 2026, 3594 PA): ResNet50 DL로 치근단 방사선 6가지 품질결함·10치위 분류 — AUC 0.924–1.000; 자동 품질평가·재촬영 감소·방사선 피폭 최소화 잠재성.

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
