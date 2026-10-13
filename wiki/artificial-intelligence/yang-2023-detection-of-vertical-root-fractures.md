---
title: "Detection of vertical root fractures by cone-beam computed tomography based on deep learning"
authors: Yang Pan, Guo Xiaolong, Mu Chuangchuang, Qi Senrong, Li Gang
year: 2023
date: 2023-02-01
doi: 10.1259/dmfr.20220345
source: yang-2023-detection-of-vertical-root-fractures.md
category: artificial-intelligence
evidence_level: in-vivo
source_collection: pubmed-text
full_text: false
pmid: "36802858"
pmcid: "PMC9944014"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9944014/
text_path: /Users/oracleneo/llm-wiki/papers/yang-2023-detection-of-vertical-root-fractures.txt
text_filename: yang-2023-detection-of-vertical-root-fractures.txt
tags: [vertical-root-fracture, deep-learning, CNN, ResNet, CBCT, diagnostic-accuracy, radiologist-comparison, in-vitro-augmentation]
relations:
  - type: extends
    target: mun-2024-deep-learning-cracked-tooth-extraction-panoramic
---

abstract-only — full text not retrieved (PMC record exists but the body returned empty)

## Three-line Summary

Diagnostic-accuracy deep-learning study (abstract-only): ResNet-18/50/101 trained on CBCT slices from 28 teeth of 14 patients (14 intact, 14 VRF; 1641 slices) and 60 in vitro teeth (30 intact, 30 VRF; 3665 slices), tested against two oral and maxillofacial radiologists.

ResNet-50 was best: AUC 0.929 (95% CI 0.908-0.950) on patient data and 0.936 (0.924-0.948) on mixed patient + in vitro data, comparable to the two radiologists (AUC 0.937 and 0.950 on patient data; 0.915 and 0.935 on mixed data); adding in vitro data raised AUC for all three networks.

Deep learning on CBCT can match expert readers for VRF detection and in vitro teeth can enlarge the training set, but the in vivo sample is only 14 patients, slice-level evaluation, and the abstract reports no external validation.

## 세줄요약

진단정확도 딥러닝 연구(초록 전용): 환자 14명 28개 치아(정상 14·수직치근파절 14; 1641 슬라이스)와 in vitro 60개 치아(정상 30·VRF 30; 3665 슬라이스)의 콘빔 CT (Cone-Beam Computed Tomography, CBCT) 슬라이스로 ResNet-18/50/101을 학습하고 구강악안면방사선과 전문의 2명과 비교.

ResNet-50이 최고: 환자 데이터 곡선하면적 (Area Under the Curve, AUC) 0.929 (95% CI 0.908-0.950), 환자+in vitro 혼합 데이터 0.936 (0.924-0.948)로 전문의 2명(환자 0.937·0.950, 혼합 0.915·0.935)과 비슷했고, in vitro 데이터 추가로 세 모델 모두 AUC가 향상.

CBCT 딥러닝이 수직치근파절 (Vertical Root Fracture, VRF) 검출에서 전문가 판독에 근접하고 in vitro 치아가 학습 데이터를 늘려주나, 환자 표본 14명·슬라이스 단위 평가·외부 검증 언급 없음(초록 기준)이 한계.

## Summary

Yang et al. (Beijing, Dentomaxillofac Radiol 2023) fine-tuned ResNet-18, -50 and -101 to classify CBCT slices as vertical root fracture (VRF) or intact. Training data were a small in vivo set (14 patients; 14 intact and 14 VRF teeth; 1641 slices) and an in vitro VRF model set (60 teeth; 3665 slices), evaluated alone and as a mixed set. ResNet-50 performed best, reaching AUC 0.929 on patient data and 0.936 on mixed data, comparable to two oral and maxillofacial radiologists reading the same test images. Adding the in vitro data improved AUC for every network, which the authors present as a way to scale training data. Only the PubMed abstract was available, so sensitivity/specificity, split strategy and interobserver ICC values are not recorded here.

## Key Contributions

- Primary CBCT deep-learning evidence for VRF detection, with two radiologists as human comparator.
- Shows in vitro fractured teeth can augment a scarce in vivo VRF dataset (ResNet-18 AUC 0.827 to 0.927 with mixed data).

## Methodology

Slice-level classification with fine-tuned ResNet-18/50/101; datasets: 28 teeth/14 patients/1641 slices (in vivo) and 60 teeth/3665 slices (in vitro). Metrics: sensitivity, specificity, accuracy, PPV, NPV, AUC; two radiologists read the test set and ICC assessed their agreement. Evidence label `in-vivo` is a judgment call: the study mixes patient and in vitro teeth and the abstract does not state retrospective vs prospective design.

## Results

| Dataset | ResNet-18 AUC | ResNet-50 AUC | ResNet-101 AUC | Radiologist AUC |
|---|---|---|---|---|
| Patient data | 0.827 | 0.929 (0.908-0.950) | 0.882 | 0.937 / 0.950 |
| Mixed data | 0.927 | 0.936 (0.924-0.948) | 0.893 | 0.915 / 0.935 |

Abstract-only: threshold-dependent metrics are not available in this record. The SR [[artificial-intelligence/alshahrani-2026-use-of-artificial-intelligence-in]] lists this study with sensitivity 94.5% and specificity 73.2% (per that SR; unverified here), the pattern of high sensitivity with moderate specificity seen in the panoramic model of [[artificial-intelligence/mun-2024-deep-learning-cracked-tooth-extraction-panoramic]].

## Related Papers

- [[artificial-intelligence/mun-2024-deep-learning-cracked-tooth-extraction-panoramic]] — extends: same ResNet family and VRF target, but on CBCT instead of panoramic images and with a radiologist comparator (panoramic ResNet50 AUC 0.82 vs CBCT 0.93-0.94 here; different datasets, not a head-to-head).
- [[artificial-intelligence/alshahrani-2026-use-of-artificial-intelligence-in]] — SR of AI for VRF that includes this study; it is the source of the pooled-narrative context (no typed edge, to avoid a circular reinforcement).
- [[cracked-tooth/de-2025-exploring-diagnostic-reliability-of-cbct]] — human CBCT VRF detection baseline from in vitro studies (complete VRF SSe 0.749 vs incomplete 0.522); this paper tests whether a CNN can reach reader-level performance on the same modality.
- [[cracked-tooth/shokri-2024-is-cone-beam-computed-tomography]] — CBCT vs periapical sensitivity 0.708 vs 0.518; context for why CBCT is the modality AI is trained on here.
