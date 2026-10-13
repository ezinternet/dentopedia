---
title: "Detection of vertical root fractures by cone-beam computed tomography based on deep learning"
authors: Yang Pan, Guo Xiaolong, Mu Chuangchuang, Qi Senrong, Li Gang
year: 2023
doi: 10.1259/dmfr.20220345
category: artificial-intelligence
source_collection: pubmed-text
full_text: false
pmid: "36802858"
pmcid: "PMC9944014"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9944014/
text_path: /Users/oracleneo/llm-wiki/papers/yang-2023-detection-of-vertical-root-fractures.txt
text_filename: yang-2023-detection-of-vertical-root-fractures.txt
---

abstract-only — full text not retrieved (PMC record exists but the body returned empty)

## Why Ingested

The held VRF-AI literature was panoramic-only as a primary study ([[wiki/artificial-intelligence/mun-2024-deep-learning-cracked-tooth-extraction-panoramic]]: high sensitivity, specificity about 53-61%), while the SR [[wiki/artificial-intelligence/alshahrani-2026-use-of-artificial-intelligence-in]] cites this CBCT ResNet study only as a table row. This paper adds the primary CBCT deep-learning evidence, with human radiologists as comparator and an in vitro augmentation arm, against the CBCT-detection baseline in [[wiki/cracked-tooth/de-2025-exploring-diagnostic-reliability-of-cbct]] and [[wiki/cracked-tooth/shokri-2024-is-cone-beam-computed-tomography]].

## Three-line Summary

Diagnostic-accuracy deep-learning study (abstract-only): ResNet-18/50/101 trained on CBCT slices from 28 teeth of 14 patients (14 intact, 14 VRF; 1641 slices) and 60 in vitro teeth (30 intact, 30 VRF; 3665 slices), tested against two oral and maxillofacial radiologists.

ResNet-50 was best: AUC 0.929 (95% CI 0.908-0.950) on patient data and 0.936 (0.924-0.948) on mixed patient + in vitro data, comparable to the two radiologists (AUC 0.937 and 0.950 on patient data; 0.915 and 0.935 on mixed data); adding in vitro data raised AUC for all three networks.

Deep learning on CBCT can match expert readers for VRF detection and in vitro teeth can enlarge the training set, but the in vivo sample is only 14 patients, slice-level evaluation, and the abstract reports no external validation.

## 세줄요약

진단정확도 딥러닝 연구(초록 전용): 환자 14명 28개 치아(정상 14·수직치근파절 14; 1641 슬라이스)와 in vitro 60개 치아(정상 30·VRF 30; 3665 슬라이스)의 콘빔 CT (Cone-Beam Computed Tomography, CBCT) 슬라이스로 ResNet-18/50/101을 학습하고 구강악안면방사선과 전문의 2명과 비교.

ResNet-50이 최고: 환자 데이터 곡선하면적 (Area Under the Curve, AUC) 0.929 (95% CI 0.908-0.950), 환자+in vitro 혼합 데이터 0.936 (0.924-0.948)로 전문의 2명(환자 0.937·0.950, 혼합 0.915·0.935)과 비슷했고, in vitro 데이터 추가로 세 모델 모두 AUC가 향상.

CBCT 딥러닝이 수직치근파절 (Vertical Root Fracture, VRF) 검출에서 전문가 판독에 근접하고 in vitro 치아가 학습 데이터를 늘려주나, 환자 표본 14명·슬라이스 단위 평가·외부 검증 언급 없음(초록 기준)이 한계.

## 1. Document Information
- **Journal**: Dentomaxillofac Radiol 2023;52(3):20220345
- **DOI**: 10.1259/dmfr.20220345
- **Institution**: Peking University School and Hospital of Stomatology and Beijing Stomatology Hospital (Capital Medical University), Beijing, China

## 2. Key Contributions
- Fine-tuned ResNet-18/50/101 for slice-level VRF detection on CBCT, with direct comparison against two oral and maxillofacial radiologists.
- Combined a small in vivo patient dataset with a larger in vitro VRF model dataset and showed the mixed training data improved AUC (ResNet-18 0.827 to 0.927; ResNet-50 0.929 to 0.936; ResNet-101 0.882 to 0.893).

## 3. Methodology and Architecture
- **Design**: deep-learning diagnostic-accuracy study; in vivo plus in vitro CBCT datasets (retrospective/prospective status not stated in the abstract).
- **n**: patient dataset 28 teeth (14 intact, 14 VRF; 1641 slices) from 14 patients; in vitro dataset 60 teeth (30 intact, 30 VRF; 3665 slices).
- **Models**: ResNet with 18, 50 and 101 layers, fine-tuned.
- **Outcomes**: sensitivity, specificity, accuracy, PPV, NPV, AUC of VRF slices in the test set; two radiologists read the same test-set CBCT, interobserver agreement by ICC.

## 4. Key Results and Benchmarks
| Dataset | ResNet-18 | ResNet-50 | ResNet-101 | Radiologists (AUC) |
|---|---|---|---|---|
| Patient data AUC | 0.827 | 0.929 (0.908-0.950) | 0.882 | 0.937 / 0.950 |
| Mixed (patient + in vitro) AUC | 0.927 | 0.936 (0.924-0.948) | 0.893 | 0.915 / 0.935 |

Sensitivity, specificity, accuracy, PPV, NPV and ICC values are measured per the abstract but not reported in it (abstract-only record). The SR [[wiki/artificial-intelligence/alshahrani-2026-use-of-artificial-intelligence-in]] reports sensitivity 94.5% and specificity 73.2% for this study (per that SR, not verified here).

## 5. Limitations and Future Work
- Abstract-only: no methods detail on reference standard, splitting (slice vs tooth level), or leakage control.
- Only 14 patients (28 teeth) in vivo; slice-level metrics can inflate performance if slices from one tooth cross train/test.
- In vitro teeth differ from clinical VRF presentation; no external validation is stated in the abstract.

## 6. Related Work
- [[wiki/artificial-intelligence/mun-2024-deep-learning-cracked-tooth-extraction-panoramic]]: panoramic CNN counterpart (ResNet50 AUC 0.82).
- [[wiki/artificial-intelligence/alshahrani-2026-use-of-artificial-intelligence-in]]: SR of AI for VRF that includes this study.
- [[wiki/cracked-tooth/de-2025-exploring-diagnostic-reliability-of-cbct]]: SR+MA of human CBCT VRF detection in vitro.
- [[wiki/cracked-tooth/shokri-2024-is-cone-beam-computed-tomography]]: SR+MA of CBCT vs periapical VRF detection.

## 7. Glossary
- **VRF**: vertical root fracture, a longitudinal fracture of the root, often hard to see on 2D imaging.
- **ResNet**: residual convolutional neural network; the number is its layer depth.
- **AUC**: area under the ROC curve; 0.5 is chance, 1.0 is perfect discrimination.
- **ICC**: intraclass correlation coefficient, used here for interobserver agreement.
- **In vitro VRF model**: extracted teeth with experimentally induced fractures used to enlarge the dataset.
