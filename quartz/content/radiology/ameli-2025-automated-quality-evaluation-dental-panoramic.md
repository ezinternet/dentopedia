---
title: "Automated quality evaluation of dental panoramic radiographs using deep learning"
authors: Ameli N, Miri Moghaddam M, Lai H, Pacheco-Pereira C
year: 2025
date: 2025-04-10
doi: 10.5624/isd.20240232
source: ameli-2025-automated-quality-evaluation-dental-panoramic.md
category: [radiology]
evidence_level: retrospective
source_collection: pubmed-text
full_text: true
pmid: "40607073"
pmcid: "PMC12210116"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12210116/
text_path: /Users/oracleneo/llm-wiki/papers/ameli-2025-automated-quality-evaluation-dental-panoramic.txt
text_filename: ameli-2025-automated-quality-evaluation-dental-panoramic.txt
tags: [panoramic, opg, image-quality, deep-learning, yolov8, positioning-error, artifact, distortion, automated-quality-assessment, dental-radiology, ai]
relations:
  - type: extends
    target: radiology/lingam-2023-common-errors-subjective-quality-panoramic
---

## Three-line Summary

Retrospective secondary-data study (n=1,000 digital OPGs, University of Alberta, 2018–2023) training five YOLOv8 deep-learning classification models on four panoramic radiograph quality criteria: artifacts, coverage area, patient positioning, and contrast/density.

YOLOv8 achieved validation accuracies of 97.9% (contrast/density), 87.2% (artifacts), 77.3% (patient positioning), 74.1% (coverage area), and 79.3% overall quality; average clinical-acceptability accuracy 81.4%; inter-rater Kappa 0.74–0.93.

First application of YOLOv8 to automated panoramic image quality assessment (IQA) — demonstrates feasibility for clinical workflow integration and dental education, though single-center data and image-level labels limit generalizability.

## 세줄요약

캐나다 앨버타 대학 치과대학(2018–2023) 파노라마 방사선 사진(Panoramic Radiograph, OPG) 1,000장을 대상으로, 인공물(Artifact)·촬영범위(Coverage)·환자 자세(Patient Positioning)·대조도/농도(Contrast/Density) 4가지 기준별로 YOLOv8 딥러닝(Deep Learning) 분류 모델 5개를 훈련한 후향적 이차자료 연구.

검증 정확도: 대조도/농도 97.9%, 인공물 87.2%, 전체 화질 79.3%, 환자 자세 77.3%, 촬영범위 74.1%; 임상적 수용 가능 여부(재촬영 필요 여부) 평균 정확도 81.4%; 평가자 간 카파(Kappa) 0.74–0.93.

파노라마 화상 품질 자동 평가(Image Quality Assessment, IQA)에 YOLOv8 적용이 실현 가능하며, 임상 워크플로 통합·방사선 재촬영(Retake) 감소·학생 교육 도구로의 잠재력이 확인됐으나, 단일 기관·단일 장비 데이터 한계로 일반화는 추가 연구 필요.

## Summary

This retrospective secondary-data study trained five YOLOv8-based deep learning classifiers on 1,000 digital panoramic radiographs from a single dental school clinic, each classifier targeting one quality criterion (artifacts, coverage area, patient positioning, contrast/density, overall clinical acceptability). Ground truth was established by two expert-supervised dentists with inter-rater Kappa of 0.74–0.93. The model achieved its highest accuracy for contrast/density (97.9%), reflecting clear pixel-intensity signal, and its lowest for coverage area (74.1%), where moderate/good boundary is inherently subjective. Positioning errors—chin too high/low causing occlusal plane curvature, midline shift causing asymmetric distortion, rotation/tilt causing differential magnification, and A-P displacement affecting anterior sharpness—were correctly classified at 77.3% overall. The study is the first to apply YOLOv8 (full-image single-stage classification) to panoramic IQA, enabling real-time evaluation without the patch-based limitations of earlier CNNs.

## Key Contributions

- **YOLOv8 first for panoramic IQA**: single-stage full-image classification outperforms patch-based CNN predecessors for global errors (positioning, coverage)
- **Four-criteria framework with mechanism-linked positioning taxonomy**: chin → occlusal plane; midline → asymmetric distortion; rotation/tilt → side-differential magnification; A-P → anterior magnification/sharpness
- **Clinical retake classifier at 81.4%** average accuracy — usable threshold for automated radiograph triage
- **Benchmarks contrast/density at 97.9%** — pixel-intensity-based criteria are highly amenable to automated DL classification

## Methodology

- **Design**: Retrospective secondary data study; University of Alberta ethics-approved
- **Imaging device**: OrthoPhos XG Series ×3 units (Dentsply Sirona)
- **n**: 1,000 OPGs (2018–2023); 5 separate balanced sub-datasets with augmentation
- **Raters**: 2 trained dentist raters; discordance resolved by board-certified OMFR
- **Model**: YOLOv8 (141 layers); Adam-W; 30 epochs; batch 16; AMP; learning rate 0.0001
- **Augmentation**: scaling, translation, flipping, mosaic (applied post-split)
- **Evaluation**: accuracy, precision, recall, F1 (confusion matrix); separate validation + new test sets

## Results

| Quality Criterion | Classes | Validation Accuracy |
|---|---|---|
| Contrast/density | 2 (poor/good) | **97.9%** |
| Artifacts | 2 (present/absent) | 87.2% |
| Overall (clinical acceptability) | 2 (unacceptable/acceptable) | 79.3% (avg 81.4%) |
| Patient positioning | 2 (poor/good) | 77.3% |
| Coverage area | 3 (poor/moderate/good) | 74.1% |

Inter-rater Kappa: 0.93 (artifacts) / 0.89 (coverage) / 0.87 (contrast) / 0.74 (positioning)

Background: up to 22% of clinical panoramic radiographs require retakes (literature estimate).

## Related Papers

- [[radiology/lingam-2023-common-errors-subjective-quality-panoramic]] — manual 10-category audit (n=2,629 OPGs; Riyadh 2023); established positioning-error prevalence baseline (15% unacceptable); this paper automates equivalent quality classification
- [[overviews/dental-radiographic-artifacts-taxonomy-overview]] — taxonomy overview of panoramic artifacts and distortion types
