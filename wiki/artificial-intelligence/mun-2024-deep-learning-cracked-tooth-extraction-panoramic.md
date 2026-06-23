---
title: "Deep learning-based prediction of indication for cracked tooth extraction using panoramic radiography"
authors: Mun et al.
year: 2024
date: 2024-08-16
doi: 10.1186/s12903-024-04721-9
source: mun-2024-deep-learning-cracked-tooth-extraction-panoramic.md
category: artificial-intelligence
confidence: retrospective
pdf_path: /Users/oracleneo/llm-wiki/papers/mun-2024-deep-learning-cracked-tooth-extraction-panoramic.txt
pdf_filename: mun-2024-deep-learning-cracked-tooth-extraction-panoramic.txt
source_collection: pubmed-text
full_text: true
pmid: "39152384"
pmcid: "PMC11328441"
text_path: /Users/oracleneo/llm-wiki/papers/mun-2024-deep-learning-cracked-tooth-extraction-panoramic.txt
text_filename: mun-2024-deep-learning-cracked-tooth-extraction-panoramic.txt
relations:
  - type: applies-to
    target: raj-2025-cracked-tooth-syndrome-diagnostic-dilemma
tags: []
---

## One-line Summary

Retrospective single-center deep-learning study: three CNNs (InceptionV3, ResNet50, EfficientNetB0; ImageNet transfer learning) trained on 418 individual-tooth crops from panoramic radiographs (200 patients; 209 vertical-root-fracture [VRF] teeth needing extraction vs 209 normal, 1:1) predicted the cracked-tooth extraction indication with high sensitivity (90.43–94.26%) but low specificity (52.63–60.77%), accuracy 72.01–75.84%, F1 76.36–79.00, AUC 0.80–0.82 (ResNet50 best, AUC 0.82) under fivefold cross-validation.

## 한줄요약

단일기관 후향 딥러닝 연구: 파노라마에서 잘라낸 개별 치아 영상 418개(환자 200명; 발치가 필요한 수직치근파절(VRF) 209개 vs 정상 209개, 1:1)로 CNN 3종(InceptionV3·ResNet50·EfficientNetB0, ImageNet 전이학습)을 학습 → 균열치 발치 적응증을 민감도 90~94%로는 잘 잡지만 특이도는 53~61%로 낮음(정확도 72~76%, F1 76~79, AUC 0.80~0.82, ResNet50가 0.82로 최고; 5겹 교차검증).

## Summary

Diagnosing cracked teeth — especially vertical root fracture (VRF), the subset that mandates extraction — is hard even for experts because crack lines are often invisible on plain radiography (the X-ray beam may run parallel to the fracture), pushing clinicians toward CBCT. Mun et al. asked whether a single panoramic radiograph plus a CNN could flag the extraction indication. Using a 1:1-balanced retrospective dataset (VRF tooth vs the patient's own contralateral healthy tooth), three CNN architectures were trained on cropped individual-tooth images. All three behaved as **high-sensitivity, low-specificity screeners**: they rarely miss a VRF but over-call normal teeth as fractured. The authors position the model as a triage aid that complements existing diagnosis and can justify ordering CBCT — not a standalone diagnostic.

## Key Contributions

- Head-to-head comparison of three modern CNNs (InceptionV3, ResNet50, EfficientNetB0) for predicting the **extraction indication** of cracked teeth from panoramic radiographs, extending prior single-model VRF detection (Fukuda et al., DetectNet/DIGITS).
- Clinically framed binary endpoint ("needs extraction = VRF" vs normal) rather than crack-line detection alone.
- Shows a low-resolution 2D modality carries screening-grade signal, while explicitly bounding the use case to triage given the low specificity.

## Methodology

- **Data**: 200 patients (113 M / 87 F, 21–89 y), Jan 2019–Apr 2023; 418 teeth = 209 VRF (extraction) + 209 normal. 1:1 balance via same-patient contralateral healthy tooth.
- **Ground truth**: endodontist diagnosis (history, probing, pulp sensibility, bite test, radiographs, microscope, transillumination, CBCT in selected cases), re-confirmed by an OMFS surgeon at extraction. Teeth with caries/prosthesis/filling/prior endo (other than the VRF tooth) excluded.
- **Imaging**: two panoramic devices (Vatech PCH-2500, Planmeca Promax) deliberately mixed for cross-environment robustness; 12-bit DICOM.
- **Preprocessing**: manual tooth-polygon crops → zero-pad to square → resample 224×224 → normalize 0–1.
- **Models / training**: InceptionV3, ResNet50, EfficientNetB0 with ImageNet pre-trained weights (transfer learning); 400 epochs, LR 1e-5, batch 8, Adam, early stopping, MAE loss.
- **Validation**: fivefold cross-validation; split train:val:test = 3:1:1. Metrics: sensitivity, specificity, accuracy, F1, ROC/AUC; optimal cutoff by Youden's Index.

## Results

| Model | Sensitivity | Specificity | Accuracy | F1 | AUC |
|---|---|---|---|---|---|
| InceptionV3 | 94.26% | 52.63% | 73.44% | 78.02 | ~0.80–0.82 |
| ResNet50 | 90.91% | 60.77% | 75.84% | 79.00 | **0.82 (highest)** |
| EfficientNetB0 | 90.43% | 53.59% | 72.01% | 76.36 | ~0.80–0.82 |

- Ranges across models: sensitivity 90.43–94.26%, specificity 52.63–60.77%, accuracy 72.01–75.84%, F1 76.36–79.00, AUC 0.80–0.82.
- **ResNet50** selected as best (highest AUC 0.82, best accuracy and F1).
- Persistent **sensitivity >> specificity** pattern → strong VRF detection, but a high false-positive rate that, in practice, would trigger confirmatory CBCT.
- **Limitations**: low specificity; small single-center sample; 2D representation of a 3D fracture loses depth information; only technical performance assessed (no patient-care outcomes). Authors call for multi-center datasets and CBCT-based 3D models.

## Related Papers

- [[cracked-tooth/raj-2025-cracked-tooth-syndrome-diagnostic-dilemma]] — clinical framing of the cracked-tooth / VRF diagnostic dilemma this AI model attempts to assist (applies-to).
- [[artificial-intelligence/sadr-2022-deep-learning-periapical-radiolucent-lesions]] — companion radiographic-CNN page (deep learning on 2D dental images for a hard-to-see lesion), same methodological family.
