---
title: "Diagnosis of in vivo vertical root fracture using deep learning on cone-beam CT images"
authors: Ziyang Hu, Dantong Cao, Yanni Hu, Baixin Wang, Yifan Zhang, Rong Tang, Jia Zhuang, Antian Gao, Ying Chen, Zitong Lin
year: 2022
date: 2022-09-05
doi: 10.1186/s12903-022-02422-9
source: hu-2022-diagnosis-of-in-vivo-vertical.md
category: artificial-intelligence
evidence_level: retrospective
source_collection: pubmed-text
full_text: true
pmid: "36064682"
pmcid: "PMC9446797"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9446797/
text_path: /Users/oracleneo/llm-wiki/papers/hu-2022-diagnosis-of-in-vivo-vertical.txt
text_filename: hu-2022-diagnosis-of-in-vivo-vertical.txt
tags: [vertical-root-fracture, deep-learning, CNN, ResNet50, CBCT, diagnostic-accuracy, non-endodontically-treated, automatic-tooth-selection, artificial-intelligence]
relations:
  - type: extends
    target: mun-2024-deep-learning-cracked-tooth-extraction-panoramic
---

## Three-line Summary

Retrospective single-center diagnostic study (216 patients; 276 non-endodontically treated teeth = 138 vertical root fracture [VRF] + 138 non-VRF controls; NewTom VG CBCT, 0.15 mm voxel) training three ImageNet-pretrained CNNs (ResNet50, VGG19, DenseNet169; 3:1 train/test, fivefold cross-validation) on cropped axial CBCT images, in two arms: manual ROI selection (552 images) and automatic tooth selection (1118 images); a radiologist with 2 years of experience read the 552 manual-arm images.

Manual-selection arm: ResNet50 accuracy 97.8%, sensitivity 97.0%, specificity 98.5%, PPV 98.5%, AUC 0.99 versus DenseNet169 96.3% / VGG19 94.9% and the radiologist 95.3% / 96.4% / 94.2%; automatic-selection arm: ResNet50 91.4% / 92.1% / 90.7% (AUC 0.96), DenseNet169 87.1%, VGG19 87.8% (no confidence intervals or significance tests for the model-versus-radiologist comparison).

A promising CBCT-based screening aid, but the reference standard was CBCT reading by radiologists (not surgical/extraction confirmation), controls were a balanced 1:1 convenience mix, only fractures visible to experienced radiologists were included, and the small dataset (two images per tooth, split probably at image level) is likely optimistic; automatic cropping cost about 6 accuracy points.

## 세줄요약

후향적 단일기관 진단 연구(환자 216명; 근관치료 안 된 치아 276개 = 수직치근파절 (Vertical Root Fracture, VRF) 138 + 비-VRF 대조 138; NewTom VG 콘빔 CT (Cone-Beam CT, CBCT), 복셀 0.15 mm): ImageNet 사전학습 합성곱신경망 (Convolutional Neural Network, CNN) 3종(ResNet50·VGG19·DenseNet169; 훈련:검증 3:1, 5겹 교차검증)을 잘라낸 축상면 CBCT 영상으로 학습 — 수동 관심영역 선택군(552장)과 자동 치아선택군(1118장) 두 군, 경력 2년 영상의학과 의사가 수동군 552장을 판독.

수동 선택군에서 ResNet50 정확도 97.8%·민감도 97.0%·특이도 98.5%·양성예측도 98.5%·곡선하면적 (Area Under the Curve, AUC) 0.99로 DenseNet169 96.3%·VGG19 94.9%·판독의(95.3%/96.4%/94.2%)보다 높았고, 자동 선택군에서는 ResNet50 91.4%/92.1%/90.7% (AUC 0.96), DenseNet169 87.1%, VGG19 87.8% (모델-판독의 비교에 신뢰구간·유의성 검정 없음).

CBCT 기반 VRF 선별 보조 도구로 유망하나, 기준표준이 수술·발치 확인이 아니라 영상의학과 의사의 CBCT 판독이고, 대조군이 1:1 균형 편의 표본이며, 숙련 판독의가 볼 수 있는 파절만 포함됐고, 소규모 자료(치아당 영상 2장, 분할은 아마 영상 단위)라 성능이 낙관적일 가능성이 크다; 자동 절단은 정확도를 약 6%p 낮췄다.

## Summary

Hu et al. (Nanjing, BMC Oral Health 2022) asked whether convolutional neural networks can diagnose in vivo vertical root fracture (VRF) on cone-beam CT, a modality whose human-read accuracy is unstable because fracture widths approach the voxel size. Using 276 non-endodontically treated teeth (138 VRF, 138 non-VRF controls drawn from apical periodontitis, healthy and bone-loss teeth), they trained ResNet50, VGG19 and DenseNet169 on cropped axial images under fivefold cross-validation. With manual ROI cropping ResNet50 reached 97.8% accuracy, 97.0% sensitivity, 98.5% specificity and AUC 0.99, slightly above a radiologist with 2 years of experience (95.3% / 96.4% / 94.2%). With algorithmic tooth selection the same network fell to 91.4% / 92.1% / 90.7% (AUC 0.96). The authors position CNNs as an auxiliary screening tool, but the reference standard was radiologist CBCT reading, the dataset was small and balanced, and no confidence intervals or significance tests were reported.

## Key Contributions

- First reported CNN diagnosis of in vivo VRF on CBCT (per the authors), restricted to non-endodontically treated teeth to avoid root-filling artefacts.
- ResNet50 outperformed VGG19, DenseNet169 and a radiologist with 2 years of experience in the manual-selection arm (point estimates only).
- Built and tested an automatic tooth-selection front end; end-to-end automation cost about 6 accuracy points (97.8% to 91.4%).
- Controls deliberately included look-alikes (apical periodontitis, periodontitis with horizontal bone loss), so the models were not just separating "bone loss" from "no bone loss".

## Methodology

Retrospective single-center diagnostic study of CBCT scans from 2019-2021 (NewTom VG, 0.15 mm voxel). 216 patients; 276 teeth (138 VRF, 138 non-VRF), labeled by two radiologists with more than 10 years of experience (kappa 1). Manual arm: 552 radiologist-cropped images (two axial images per tooth); automatic arm: 1118 images from a Gaussian blur / Otsu / K3M skeleton / sliding-box tooth-selection algorithm. Three ImageNet-pretrained CNNs, 75/25 train/test, fivefold cross-validation, augmentation by flips, rotation and photometric changes. A radiologist with 2 years of experience (blinded; intra-examiner kappa 0.711) read the 552 manual-arm images.

## Results

| Arm / reader | Accuracy % | Sensitivity % | Specificity % | PPV % | AUC |
|---|---|---|---|---|---|
| Manual: ResNet50 | 97.8 | 97.0 | 98.5 | 98.5 | 0.99 |
| Manual: DenseNet169 | 96.3 | 94.1 | 98.5 | 98.5 | 0.98 |
| Manual: VGG19 | 94.9 | 92.7 | 97.0 | 96.9 | 0.97 |
| Manual: radiologist (2 y) | 95.3 | 96.4 | 94.2 | 94.3 | n/r |
| Auto: ResNet50 | 91.4 | 92.1 | 90.7 | 90.8 | 0.96 |
| Auto: DenseNet169 | 87.1 | 80.6 | 93.5 | 92.6 | n/r |
| Auto: VGG19 | 87.8 | 89.2 | 86.3 | 86.7 | n/r |

n/r = not reported in the text.

## Clinical Insights

- **What the numbers do and do not mean.** The 97-98% figures come from a balanced dataset of CBCT-visible fractures in non-endodontically treated teeth, labeled by radiologists reading the same CBCT. They show the CNN can reproduce expert CBCT reading on clear cases; they do not show it finds fractures experts miss, nor how it performs on root-filled teeth (the majority of VRF in the wiki's other sources) with post or gutta-percha artefacts.
- **Human benchmark is weak, which flatters the model.** The comparator was one radiologist with 2 years of experience (sensitivity 96.4%), already far above the pooled human CBCT sensitivity in [[cracked-tooth/shokri-2024-is-cone-beam-computed-tomography]] (about 0.71), a sign that this dataset is easier than typical clinical VRF work-ups (selected visible fractures, artefact-free scans).
- **Modality matters for specificity.** Compared with the panoramic CNN in [[artificial-intelligence/mun-2024-deep-learning-cracked-tooth-extraction-panoramic]] (specificity 53-61%, AUC 0.82), the CBCT CNN here held specificity at 90-98%, consistent with the 3D modality carrying far more fracture information, though the datasets and control definitions differ and no head-to-head exists.
- **Full automation is not yet equivalent.** Off-center algorithmic crops cost roughly 6 accuracy points and 13.5 points of DenseNet169 sensitivity (94.1% to 80.6%), so a deployable screening workflow would need a better localizer.
- **Placement in practice.** Reasonable as a second reader or screening aid on CBCT already acquired for another reason; not a basis for ordering CBCT or for extraction decisions, which still rest on the clinical and surgical findings summarized in [[cracked-tooth/patel-2022-present-status-future-directions-vertical]].

## Related Papers

- [[artificial-intelligence/mun-2024-deep-learning-cracked-tooth-extraction-panoramic]] — extends: same task (VRF diagnosis with ResNet50-class CNNs) on 3D CBCT instead of 2D panoramic radiographs, with much higher specificity.
- [[artificial-intelligence/alshahrani-2026-use-of-artificial-intelligence-in]] — SR that tabulates this study as a CBCT AI example (manual ROI 97.8%, automatic ROI 91.4%); described in prose only, since a typed edge would be circular.
- [[cracked-tooth/de-2025-exploring-diagnostic-reliability-of-cbct]] — pooled in vitro human-read CBCT accuracy for VRF (very-low GRADE); the human-reader baseline this AI approach aims to stabilize.
- [[cracked-tooth/shokri-2024-is-cone-beam-computed-tomography]] — CBCT vs periapical meta-analysis; pooled CBCT sensitivity well below the radiologist and CNN figures here.
- [[cracked-tooth/liao-2021-vertical-root-fracture-non-endodontically-treated]] — background on VRF in non-endodontically treated teeth, the population studied here.
- [[cracked-tooth/alaugaily-2022-cbct-patterns-bone-loss-clinical]] — in vivo CBCT bone-loss patterns; the bone-loss controls in this study test whether a CNN can tell true VRF from bone-loss look-alikes.
- [[cracked-tooth/patel-2022-present-status-future-directions-vertical]] — clinical context: CBCT reveals bone-loss patterns more reliably than the fracture line itself.
