---
title: "Deep learning and clustering approaches for dental implant size classification based on periapical radiographs"
authors: Ji-Hyun Park, Hong Seok Moon, Hoi-In Jung, JaeJoon Hwang, Yoon-Ho Choi, Jong-Eun Kim
year: 2023
date: 2023-10-05
doi: 10.1038/s41598-023-42385-7
source: park-2023-deep-learning-implant-size-classification.md
category: [digital-workflow]
evidence_level: retrospective
pdf_path: /Users/oracleneo/llm-wiki/papers/park-2023-deep-learning-implant-size-classification.pdf
pdf_filename: park-2023-deep-learning-implant-size-classification.pdf
source_collection: external
tags: [deep-learning, AI, implant-identification, periapical-radiograph, VGG16, k-means, implant-size, classification]
---

## Three-line Summary
Retrospective AI study (Sci Rep 2023;13:16856) comparing VGG16 deep learning and k-means++ clustering for classifying implant diameter and length from periapical radiographs across 9 size groups.

VGG16 achieved accuracy >0.994 and AUC >0.975; k-means++ clustering reached accuracy >0.983, with DL outperforming clustering in 6/9 groups after tuning.

Both methods show high clinical utility for identifying implant size when patient records are unavailable, though multicenter validation is required before deployment.

## 세줄요약
retrospective AI 연구(Sci Rep 2023;13:16856): 치근단 방사선에서 임플란트 직경·길이를 9개 그룹으로 분류하는 VGG16 딥러닝과 k-means++ 클러스터링을 비교.

VGG16 정확도 >0.994·AUC >0.975, 클러스터링 정확도 >0.983으로 DL이 6/9 그룹에서 클러스터링 대비 우위.

환자 기록이 없을 때 임플란트 시스템·규격 식별에 높은 임상 잠재성이 있으나 다기관 검증이 선행되어야 한다.

## Summary
Sci Rep study comparing deep learning (VGG16 fine-tuned) and clustering (k-means++ on 3 landmark coordinates) for classifying implant diameter and length from periapical radiographs across 9 size groups. Both AI approaches demonstrated reliable performance exceeding clinical utility threshold.

## Key Contributions
- **9 implant size groups** (diameter × length combinations)
- **Deep learning (VGG16)**: accuracy >0.994; AUC-ROC >0.975; sensitivity >0.950
- **Clustering (k-means++)**: accuracy >0.983; AUC >0.947
- Statistically significant improvement after tuning in 6/9 DL groups, 4/9 clustering groups
- DL outperforms clustering; both clinically useful
- **Multicenter validation required** before clinical deployment

## Clinical Application
- Critical when patient records unavailable — identify implant system/size from radiograph
- Enables appropriate component selection for maintenance, screw replacement, complication management
- Prerequisite tool for AI-assisted implant complication management systems

## Related Papers
- [[digital-workflow/revilla-leon-2021-artificial-intelligence-implant-dentistry-sr]] — AI implant type recognition SR: 93.8–98% accuracy
- [[digital-workflow/oh-2023-deep-learning-osseointegration-prediction-radiographs]] — DL for osseointegration prediction from radiographs
