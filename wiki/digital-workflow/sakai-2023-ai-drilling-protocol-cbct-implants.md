---
title: "Development of artificial intelligence model for supporting implant drilling protocol decision making"
authors: Takahiko Sakai, Hefei Li, Tatsuki Shimada, Suzune Kita, Maho Iida, Chunwoo Lee, Tamaki Nakano, Satoshi Yamaguchi, Satoshi Imazato
year: 2023
date: 2023-08-25
doi: 10.2186/jpr.JPR_D_22_00053
source: sakai-2023-ai-drilling-protocol-cbct-implants.md
category: [digital-workflow]
confidence: retrospective
pdf_path: /Users/oracleneo/llm-wiki/papers/sakai-2023-ai-drilling-protocol-cbct-implants.pdf
pdf_filename: sakai-2023-ai-drilling-protocol-cbct-implants.pdf
source_collection: external
tags: [artificial-intelligence, AI, CBCT, drilling-protocol, bone-quality, primary-stability, LeNet-5, deep-learning]
---

## One-line Summary
Retrospective (J Prosthodont Res 2023;67:360–365, Osaka Univ.): LeNet-5 AI model predicts implant drilling protocol (A/B/C) from CBCT images — overall accuracy 93.8%, AUC 98.6–99.4%; potential as decision-support tool for improving primary stability.

## 한줄요약
retrospective(J Prosthodont Res 2023;67:360-365, Osaka U): LeNet-5 AI 모델 CBCT 이미지로 임플란트 드릴링 프로토콜(A/B/C) 예측 — 정확도 93.8%, AUC 98.6–99.4%; 1차 안정성 향상을 위한 의사결정 지원 가능성.

## Summary
AI model development study (Osaka University) using LeNet-5 deep learning to predict appropriate implant drilling protocol (A, B, or C) from CBCT gray value images. 93.8% accuracy achieved — potential as decision-support tool for primary stability optimization, especially for less experienced clinicians.

## Key Contributions
- **n=60 patients, 1200 CBCT slices** (20/patient); 3 drilling protocols based on actual case
- **AI model**: LeNet-5; 80% training/validation, 20% test
- **Overall accuracy: 93.8%**
- **Sensitivity** by protocol: A=97.5%, B=95.0%, C=85.0%
- **AUC**: A=98.6%, B=98.6%, C=99.4%
- CBCT gray values (not HU) used as proxy for bone quality
- Prospective clinical validation and multi-site testing needed

## Clinical Application
- CBCT-based AI drilling guidance particularly useful for D3/D4 bone where protocol choice is critical
- Reduces surgeon experience-dependency in drilling protocol selection
- Decision-support (not autonomous) system concept

## Related Papers
- [[digital-workflow/revilla-leon-2021-artificial-intelligence-implant-dentistry-sr]] — SR on AI in implant dentistry
- [[implants/raghavan-2025-bone-density-implant-dentistry-review]] — bone density classification and drilling modifications
- [[implants/fontes-pereira-2023-osseodensification-osteotomy-alternative-sr]] — alternative drilling protocol (osseodensification)
