---
title: "Development of artificial intelligence model for supporting implant drilling protocol decision making"
authors: Takahiko Sakai, Hefei Li, Tatsuki Shimada, Suzune Kita, Maho Iida, Chunwoo Lee, Tamaki Nakano, Satoshi Yamaguchi, Satoshi Imazato
year: 2023
date: 2023-08-25
doi: 10.2186/jpr.JPR_D_22_00053
source: sakai-2023-ai-drilling-protocol-cbct-implants.md
category: [digital-workflow]
evidence_level: retrospective
pdf_path: /Users/oracleneo/llm-wiki/papers/sakai-2023-ai-drilling-protocol-cbct-implants.pdf
pdf_filename: sakai-2023-ai-drilling-protocol-cbct-implants.pdf
source_collection: external
tags: [artificial-intelligence, AI, CBCT, drilling-protocol, bone-quality, primary-stability, LeNet-5, deep-learning]
---

## Three-line Summary
Retrospective AI model development study (J Prosthodont Res 2023;67:360–365, Osaka University) training a LeNet-5 deep learning model on 1,200 CBCT slices from 60 patients to predict one of three implant drilling protocols (A/B/C) based on bone density gray values.

Overall accuracy was 93.8% and AUC ranged from 98.6–99.4% across protocols, with Protocol A achieving the highest sensitivity (97.5%) and Protocol C the lowest (85.0%), indicating the model is most reliable for straightforward bone but less certain for D3/D4 cases.

The model offers decision-support potential — particularly for less experienced clinicians selecting drilling protocols to optimize primary stability — but requires prospective multi-site validation before clinical deployment.

## 세줄요약
retrospective AI 모델 개발 연구(J Prosthodont Res 2023;67:360–365, 오사카대): 환자 60명의 CBCT 슬라이스 1,200장으로 LeNet-5 딥러닝 모델을 학습해 임플란트 드릴링 프로토콜(A/B/C)을 예측.

전체 정확도 93.8%, AUC 98.6–99.4%; 프로토콜 A 민감도 97.5%·C 85.0%로, 일반 골밀도에서 가장 신뢰성이 높고 D3/D4 골에서 불확실성 증가.

경험이 부족한 술자의 드릴링 프로토콜 선택 의사결정 지원에 잠재적 유용성이 있으나, 임상 적용 전 다기관 전향적 검증 필요.

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
