---
title: "Deep learning-based prediction of osseointegration of dental implants using plain radiography"
authors: Oh et al., Bong Chul Kim, Kwang Gi Kim
year: 2023
date: 2023-04-08
doi: 10.1186/s12903-023-02921-3
source: oh-2023-deep-learning-osseointegration-prediction-radiographs.md
category: [digital-workflow]
evidence_level: retrospective
pdf_path: /Users/oracleneo/llm-wiki/papers/oh-2023-deep-learning-osseointegration-prediction-radiographs.pdf
pdf_filename: oh-2023-deep-learning-osseointegration-prediction-radiographs.pdf
source_collection: external
tags: [deep-learning, AI, osseointegration, radiograph, panoramic, periapical, bone-integration, loading-timing]
---

## Three-line Summary
Retrospective deep learning study (BMC Oral Health 2023;23:208, Gachon/Wonkwang University) training 7 models to classify implant osseointegration status (pre vs confirmed) from panoramic and periapical radiographs of 580 patients and 1,206 implants.

All 7 DL models demonstrated reliable performance in distinguishing pre-osseointegration (338 patients, 591 implants) from confirmed osseointegration (242 patients, 615 implants) images.

Clinical potential lies in non-invasive osseointegration assessment to assist loading-timing decisions, but multicenter prospective validation is required before clinical deployment.

## 세줄요약
retrospective 딥러닝 연구(BMC Oral Health 2023;23:208, 가천대/원광대): 580명 1,206개 임플란트의 파노라마·치근단 방사선으로 골유착 전/후를 분류하는 7개 DL 모델을 학습.

7개 모델 모두 골유착 전(591개)과 골유착 확인(615개) 이미지 분류에서 신뢰할 만한 성능을 보임.

비침습적으로 부하 시기를 결정하는 임상 보조 도구로 가능성이 있으나, 실제 임상 적용 전 다기관 전향적 검증이 필요함.

## Summary
Retrospective deep learning study (Gachon/Wonkwang University) predicting osseointegration status from plain radiographs in 580 patients (1206 implants). Seven DL models trained to distinguish pre-osseointegration (Group 1) from confirmed osseointegration (Group 2) images — all showed reliable performance.

## Key Contributions
- **580 patients, 1206 implants**; panoramic + periapical radiographs
- Group 1: 338 patients, 591 implants (pre-osseointegration)
- Group 2: 242 patients, 615 implants (confirmed osseointegration)
- **7 DL models** tested; 60:20:20 train/val/test; 10 experiments each
- All models showed reliable osseointegration classification performance
- **Clinical gap**: multicenter prospective validation required

## Clinical Potential
- Non-invasive osseointegration status check via routine radiograph
- May assist clinicians in deciding loading timing without RFA/ISQ device
- Complementary to ISQ measurement rather than replacement

## Related Papers
- [[digital-workflow/revilla-leon-2021-artificial-intelligence-implant-dentistry-sr]] — SR: AI success prediction 62.4–80.5%; context for this study
- [[digital-workflow/park-2023-deep-learning-implant-size-classification]] — DL for implant size from periapical; same modality
- [[endodontics/eal/versiani-2022-wireless-apex-locator-micro-ct-accuracy]] — ISQ comparison; related stability assessment
