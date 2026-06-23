---
title: "Deep learning-based prediction of indication for cracked tooth extraction using panoramic radiography"
authors: Mun et al.
year: 2024
doi: 10.1186/s12903-024-04721-9
category: artificial-intelligence
source_collection: pubmed-text
full_text: true
pmid: "39152384"
pmcid: "PMC11328441"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11328441/
text_path: /Users/oracleneo/llm-wiki/papers/mun-2024-deep-learning-cracked-tooth-extraction-panoramic.txt
text_filename: mun-2024-deep-learning-cracked-tooth-extraction-panoramic.txt
---

## Why Ingested

[[cracked-tooth/raj-2025-cracked-tooth-syndrome-diagnostic-dilemma]]는 균열치(특히 수직치근파절, VRF)가 임상·방사선 진단에서 가장 어려운 문제임을 강조한다. 본 논문(Mun 2024)은 그 진단 난제에 deep-learning을 적용해 파노라마 한 장만으로 발치 적응증(VRF) 예측이 가능한지를 정량 평가한 retrospective AI 모델 연구로, 그 진단 딜레마를 보조하는 도구 가능성을 제시한다. AI/CNN 방법론 페이지([[artificial-intelligence/sadr-2022-deep-learning-periapical-radiolucent-lesions]] 등 영상 CNN 계열)와도 짝을 이룬다.

## One-line Summary

Retrospective single-center AI study: three CNNs (InceptionV3, ResNet50, EfficientNetB0) trained on 418 individual-tooth crops from panoramic radiographs (200 patients, 209 VRF vs 209 normal, 1:1) predicted cracked-tooth (VRF) extraction indication with high sensitivity (90–94%) but low specificity (53–61%), accuracy 72–76%, AUC 0.80–0.82 (ResNet50 best at 0.82).

## 한줄요약

단일기관 후향 AI 연구: 파노라마에서 개별 치아 절편 418개(환자 200명, 수직치근파절 VRF 209 vs 정상 209, 1:1)로 CNN 3종(InceptionV3·ResNet50·EfficientNetB0)을 학습시켜 균열치 발치 적응증을 예측 — 민감도는 높으나(90~94%) 특이도는 낮고(53~61%), 정확도 72~76%, AUC 0.80~0.82(ResNet50가 0.82로 최고).

## 1. Document Information

- **Title**: Deep learning-based prediction of indication for cracked tooth extraction using panoramic radiography
- **Authors**: Mun et al.
- **Journal**: BMC Oral Health, 2024-08-16
- **DOI**: [10.1186/s12903-024-04721-9](https://doi.org/10.1186/s12903-024-04721-9) (PMID 39152384, PMCID PMC11328441)
- **Study type**: Retrospective single-center diagnostic AI/deep-learning model development study (IRB-approved, non-interventional retrospective design; informed consent waived).
- **Source**: Full text retrieved from PubMed Central (PMC).

## 2. Key Contributions

- First study to compare **multiple modern CNN architectures** (InceptionV3, ResNet50, EfficientNetB0) for predicting the *extraction indication* of cracked teeth (specifically VRF) from panoramic radiographs — extends prior single-model VRF detection (Fukuda et al., DetectNet/DIGITS).
- Frames the task as a clinically meaningful binary endpoint: "needs extraction (VRF)" vs "normal," rather than mere crack-line detection.
- Demonstrates that a low-resolution, 2D, single-image modality (panoramic) carries enough signal for a screening-grade model (high sensitivity), with explicit acknowledgement that low specificity limits it to a triage / "recommend CBCT" role rather than a definitive diagnosis.

## 3. Methodology and Architecture

- **Cohort**: 200 patients (113 M, 87 F; 21–89 y) seen Jan 2019–Apr 2023; 418 teeth → Group 1 = 209 normal, Group 2 = 209 VRF requiring extraction. 1:1 balance enforced by sampling the contralateral healthy tooth of the same type within the same patient.
- **Ground truth**: a single endodontist diagnosed VRF using history, periodontal probing, pulp sensibility test, bite test, periapical/panoramic radiographs, microscope, transillumination, and CBCT in selected cases; an oral & maxillofacial surgeon re-confirmed VRF at extraction. Teeth with caries, prostheses, fillings, or prior endodontic treatment (other than the VRF tooth) were excluded.
- **Imaging**: panoramic from two devices (Vatech PCH-2500; Planmeca Promax) — deliberately mixed to test cross-environment robustness. 12-bit DICOM.
- **Preprocessing**: manual tooth polygons → crop each tooth → zero-pad to square → resample to 224×224 → normalize 0–1.
- **Models**: InceptionV3, ResNet50, EfficientNetB0; ImageNet pre-trained weights (transfer learning); 400 epochs, LR 1e-5, batch size 8, Adam optimizer, early stopping, MAE loss.
- **Validation**: fivefold cross-validation; data split train:val:test = 3:1:1.
- **Metrics**: sensitivity, specificity, accuracy, F1 (from confusion matrix); ROC/AUC; optimal cutoff via Youden's Index.

## 4. Key Results and Benchmarks

| Model | Sensitivity | Specificity | Accuracy | F1 | AUC |
|---|---|---|---|---|---|
| InceptionV3 | 94.26% | 52.63% | 73.44% | 78.02 | ~0.80–0.82 |
| ResNet50 | 90.91% | 60.77% | 75.84% | 79.00 | **0.82 (best)** |
| EfficientNetB0 | 90.43% | 53.59% | 72.01% | 76.36 | ~0.80–0.82 |

- Across models: sensitivity 90.43–94.26%, specificity 52.63–60.77%, accuracy 72.01–75.84%, F1 76.36–79.00%, AUC 0.80–0.82.
- **ResNet50** had the highest AUC (0.82) and best accuracy/F1 — selected as most suitable.
- Consistent pattern: **sensitivity >> specificity** → good at not missing VRF, but high false-positive rate.

## 5. Limitations and Future Work

- **Low specificity (≈53–61%)**: many normal teeth misclassified as VRF → unnecessary additional exams; model is screening/triage-grade, not definitive.
- **Small, single-center sample** (200 patients / 418 teeth) → limited generalizability; authors call for **multi-center** datasets and continued retraining.
- **2D representation of a 3D defect**: panoramic loses depth information; VRF boundaries are low-contrast and hard to distinguish from surrounding structures.
- Study addressed **only technical model performance**, not downstream clinical/patient-care impact.
- Future: incorporate **3D imaging (CBCT)** for more accurate prediction; positioned as a complement to (not replacement for) existing diagnostic methods, and as a basis for recommending CBCT.

## 6. Related Work

- Fukuda et al. — earlier AI detection of VRF on panoramic radiography using DetectNet/DIGITS 5.0.
- Deep-learning prediction of third molar extraction difficulty / post-extraction paresthesia; implant osseointegration prediction from plain radiography; orthognathic surgery outcome prediction — cited as the broader DL-in-dentistry context.

## 7. Glossary

- **VRF (Vertical Root Fracture)**: a longitudinal fracture through the root; in this study the subset of cracked teeth that requires extraction and the positive class.
- **Cracked tooth**: plastic deformation appearing as a break within tooth structure without actual separation/loss of hard tissue. AAE crack entities: enamel craze lines, fractured cusp, cracked tooth, split tooth, VRF.
- **CNN (Convolutional Neural Network)**: deep-learning architecture for image classification (here InceptionV3 / ResNet50 / EfficientNetB0).
- **Transfer learning**: initializing with ImageNet pre-trained weights then fine-tuning on the dental dataset.
- **Sensitivity / Specificity**: TP rate / TN rate.
- **AUC-ROC**: area under the ROC curve; discrimination ability of a binary classifier.
- **Youden's Index**: sensitivity + specificity − 1; used to pick the optimal classification cutoff.
- **CBCT (Cone Beam Computed Tomography)**: 3D imaging recommended when panoramic is inconclusive for VRF.
