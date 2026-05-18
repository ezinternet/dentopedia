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

## One-line Summary
Sci Rep 2026: ResNet50-based DL system for PA image quality assessment (6 defects × 10 tooth positions) on 3594 PAs — AUC 0.924–1.000 per defect; automated quality control with real-time feedback potential.

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
