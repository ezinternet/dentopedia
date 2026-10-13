---
title: "Diagnosis of in vivo vertical root fracture using deep learning on cone-beam CT images"
authors: Ziyang Hu, Dantong Cao, Yanni Hu, Baixin Wang, Yifan Zhang, Rong Tang, Jia Zhuang, Antian Gao, Ying Chen, Zitong Lin
year: 2022
doi: 10.1186/s12903-022-02422-9
category: artificial-intelligence
source_collection: pubmed-text
full_text: true
pmid: "36064682"
pmcid: "PMC9446797"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9446797/
text_path: /Users/oracleneo/llm-wiki/papers/hu-2022-diagnosis-of-in-vivo-vertical.txt
text_filename: hu-2022-diagnosis-of-in-vivo-vertical.txt
---

## Why Ingested

[[artificial-intelligence/mun-2024-deep-learning-cracked-tooth-extraction-panoramic]]이 파노라마(2D)에서 수직치근파절(VRF) 발치 적응증을 AUC 0.82·특이도 53-61%로만 예측한 것과 대비되는 CBCT(3D) 기반 in vivo CNN 연구로, 같은 진단 과제에서 영상 모달리티에 따라 성능이 어떻게 달라지는지 확인하기 위해 인제스트. 동시에 [[cracked-tooth/de-2025-exploring-diagnostic-reliability-of-cbct]]·[[cracked-tooth/shokri-2024-is-cone-beam-computed-tomography]]가 정리한 사람 판독 CBCT의 불안정한 정확도에 AI가 무엇을 더하는지의 1차 자료이며, 이 연구를 포함한 AI-VRF 체계적 문헌고찰 [[artificial-intelligence/alshahrani-2026-use-of-artificial-intelligence-in]]의 원자료 중 하나다.

## Three-line Summary

Retrospective single-center diagnostic study (216 patients; 276 non-endodontically treated teeth = 138 vertical root fracture [VRF] + 138 non-VRF controls; NewTom VG CBCT, 0.15 mm voxel) training three ImageNet-pretrained CNNs (ResNet50, VGG19, DenseNet169; 3:1 train/test, fivefold cross-validation) on cropped axial CBCT images, in two arms: manual ROI selection (552 images) and automatic tooth selection (1118 images); a radiologist with 2 years of experience read the 552 manual-arm images.

Manual-selection arm: ResNet50 accuracy 97.8%, sensitivity 97.0%, specificity 98.5%, PPV 98.5%, AUC 0.99 versus DenseNet169 96.3% / VGG19 94.9% and the radiologist 95.3% / 96.4% / 94.2%; automatic-selection arm: ResNet50 91.4% / 92.1% / 90.7% (AUC 0.96), DenseNet169 87.1%, VGG19 87.8% (no confidence intervals or significance tests for the model-versus-radiologist comparison).

A promising CBCT-based screening aid, but the reference standard was CBCT reading by radiologists (not surgical/extraction confirmation), controls were a balanced 1:1 convenience mix, only fractures visible to experienced radiologists were included, and the small dataset (two images per tooth, split probably at image level) is likely optimistic; automatic cropping cost about 6 accuracy points.

## 세줄요약

후향적 단일기관 진단 연구(환자 216명; 근관치료 안 된 치아 276개 = 수직치근파절 (Vertical Root Fracture, VRF) 138 + 비-VRF 대조 138; NewTom VG 콘빔 CT (Cone-Beam CT, CBCT), 복셀 0.15 mm): ImageNet 사전학습 합성곱신경망 (Convolutional Neural Network, CNN) 3종(ResNet50·VGG19·DenseNet169; 훈련:검증 3:1, 5겹 교차검증)을 잘라낸 축상면 CBCT 영상으로 학습 — 수동 관심영역 선택군(552장)과 자동 치아선택군(1118장) 두 군, 경력 2년 영상의학과 의사가 수동군 552장을 판독.

수동 선택군에서 ResNet50 정확도 97.8%·민감도 97.0%·특이도 98.5%·양성예측도 98.5%·곡선하면적 (Area Under the Curve, AUC) 0.99로 DenseNet169 96.3%·VGG19 94.9%·판독의(95.3%/96.4%/94.2%)보다 높았고, 자동 선택군에서는 ResNet50 91.4%/92.1%/90.7% (AUC 0.96), DenseNet169 87.1%, VGG19 87.8% (모델-판독의 비교에 신뢰구간·유의성 검정 없음).

CBCT 기반 VRF 선별 보조 도구로 유망하나, 기준표준이 수술·발치 확인이 아니라 영상의학과 의사의 CBCT 판독이고, 대조군이 1:1 균형 편의 표본이며, 숙련 판독의가 볼 수 있는 파절만 포함됐고, 소규모 자료(치아당 영상 2장, 분할은 아마 영상 단위)라 성능이 낙관적일 가능성이 크다; 자동 절단은 정확도를 약 6%p 낮췄다.

## 1. Document Information

- **Journal**: BMC Oral Health 2022;22(1):382 (published 2022-09-05; open access)
- **DOI**: 10.1186/s12903-022-02422-9
- **PMID / PMCID**: 36064682 / PMC9446797
- **Institution**: Nanjing Stomatological Hospital, Medical School of Nanjing University (Dentomaxillofacial Radiology), and School of Electronic Science and Engineering, Nanjing University, China
- **Ethics**: retrospective study approved by the hospital ethics committee; written informed consent waived

## 2. Key Contributions

- Stated first attempt to diagnose **in vivo** VRF on CBCT with CNNs (prior CNN work cited: Fukuda et al. on panoramic radiographs; Johari et al. probabilistic neural network on CBCT ex vivo with artificially generated fractures).
- Head-to-head comparison of three ImageNet-pretrained CNNs plus a human reader (radiologist with 2 years of experience) on identical CBCT images.
- Adds an **automatic tooth-selection pipeline** (Gaussian blur, modified Otsu binarization, K3M skeleton, 170 x 170 px sliding boxes every 60-80 px) in front of the CNNs, and quantifies the accuracy lost relative to manual ROI cropping.
- Restricts the VRF set to **non-endodontically treated teeth**, deliberately avoiding gutta-percha/metal-post beam-hardening artefacts.

## 3. Methodology and Architecture

- **Design**: retrospective diagnostic-accuracy study with a case-control-style balanced dataset; single center; PACS search of CBCT scans from 2019-2021.
- **Patients/teeth**: 216 patients (126 M / 90 F; mean age 52.03 +/- 14.29 y, range 19-86); 276 teeth = 138 VRF + 138 non-VRF.
- **VRF inclusion**: non-endodontically treated; good image quality without motion/beam-hardening artefacts; fracture recorded when a hypodense line appeared on at least two consecutive axial images. **Non-VRF controls** (random mix of three types): apical periodontitis from caries, healthy teeth, periodontitis teeth with horizontal bone loss.
- **Reference standard**: confirmation by two radiologists with more than 10 years of experience, repeated after 3 months (kappa 1 inter- and intra-examiner). No surgical, extraction or direct-visualization confirmation is described.
- **Imaging**: NewTom VG, voxel 0.15 mm, 110 kV, 3.6-3.7 mA, FOV 12 x 8 cm, 5.4 s.
- **Datasets**: manual-selection group = 552 cropped images (276 VRF + 276 non-VRF; two axial dentition images per tooth) cropped by a radiologist with 5 years of experience; auto-selection group = 1118 images (555 VRF + 563 non-VRF) cropped by the tooth-selection algorithm (one or two crops per tooth because boxes overlap neighboring teeth). Sharpening (gray-level transformation) applied to both; augmentation by random flips, rotation within 90 degrees, brightness/contrast/saturation.
- **Models**: VGG19, DenseNet169, ResNet50 (ImageNet-pretrained); PyTorch 1.11; NVIDIA Tesla V100; batch 16; learning rate 5e-3 with reduction on plateau; 75% training / 25% testing; fivefold cross-validation, reported as the mean of the validation folds.
- **Human comparator**: radiologist C (2 years of experience), blinded to patient identity, clinical and imaging findings and final diagnosis, read the 552 manual-arm images; repeated after 3 months (intra-examiner kappa 0.711).
- **Statistics**: accuracy, sensitivity, specificity, PPV, ROC/AUC (Python pandas), kappa (SPSS 23).

## 4. Key Results and Benchmarks

Manual-selection group (Table 1):

| Reader | Accuracy % | Sensitivity % | Specificity % | PPV % | AUC |
|---|---|---|---|---|---|
| ResNet50 | 97.8 | 97.0 | 98.5 | 98.5 | 0.99 |
| DenseNet169 | 96.3 | 94.1 | 98.5 | 98.5 | 0.98 |
| VGG19 | 94.9 | 92.7 | 97.0 | 96.9 | 0.97 |
| Radiologist (2 y) | 95.3 | 96.4 | 94.2 | 94.3 | not reported |

Auto-selection group (Table 2): ResNet50 91.4 / 92.1 / 90.7 / 90.8 (AUC 0.96); DenseNet169 87.1 / 80.6 / 93.5 / 92.6; VGG19 87.8 / 89.2 / 86.3 / 86.7 (accuracy / sensitivity / specificity / PPV, %).

- Agreement (Table 3): radiologists A and B kappa 1.0 (inter- and intra-examiner); radiologist C intra-examiner kappa 0.711 (substantial).
- ResNet50 was described as stable on difficult cases (non-VRF teeth with large bone loss, VRF with little or no bone loss, subtle fractures; Fig. 4 shows examples).
- No confidence intervals, p-values or formal tests are reported for model-versus-model or model-versus-radiologist differences.

## 5. Limitations and Future Work

Author-stated:
- VRF sample is small and should be expanded for stable results.
- Only non-endodontically treated teeth; performance on root-filled teeth with post/gutta-percha artefacts is untested.
- Auto-selection was less accurate than manual selection (off-center crops); the algorithm needs optimization.
- Only VRF teeth observable by an experienced radiologist were included; hidden fractures invisible on CBCT would need to be included before clinical use.

Inferred (not stated by the authors):
- The reference standard is the same modality (CBCT) read by radiologists, so the CNNs learn to reproduce radiologist labels (incorporation bias); the method cannot be shown to detect fractures radiologists miss.
- Two images per tooth (manual arm) or one to two crops per tooth (auto arm) are described, but the text does not say the 3:1 split / fivefold folds were made at the tooth or patient level; if made at the image level, near-duplicate images of one tooth could appear in both training and test sets and inflate performance.
- Balanced 1:1 sampling and a single scanner/center limit generalization; PPV and accuracy would differ at real-world VRF prevalence.
- The comparator was one radiologist with 2 years of experience; no experienced-radiologist or CBCT-reading benchmark is given.

## 6. Related Work

- [[artificial-intelligence/mun-2024-deep-learning-cracked-tooth-extraction-panoramic]]: panoramic CNN (ResNet50 AUC 0.82, specificity 53-61%) for the same VRF task; Hu 2022 shows far higher specificity on 3D CBCT.
- [[artificial-intelligence/alshahrani-2026-use-of-artificial-intelligence-in]]: SR of AI for VRF that tabulates this study as a CBCT AI example (manual ROI 97.8%, automatic ROI 91.4%).
- [[cracked-tooth/de-2025-exploring-diagnostic-reliability-of-cbct]] and [[cracked-tooth/shokri-2024-is-cone-beam-computed-tomography]]: pooled human-read CBCT accuracy for VRF, mostly ex vivo/in vitro.
- [[cracked-tooth/liao-2021-vertical-root-fracture-non-endodontically-treated]]: background on VRF in non-endodontically treated teeth, the population studied here.
- [[cracked-tooth/alaugaily-2022-cbct-patterns-bone-loss-clinical]]: in vivo CBCT bone-loss patterns, the confounder (bone loss in controls) the CNNs had to separate from true VRF.

## 7. Glossary

- **VRF (vertical root fracture)**: complete or incomplete longitudinal root fracture, usually buccolingual, that may start at any root level.
- **CBCT (cone-beam CT)**: 3D dental imaging; voxel size (here 0.15 mm) is of the same order as many VRF widths (reported 60-770 um), which blurs fracture lines.
- **ROI (region of interest)**: the cropped tooth image fed to the CNN; manual vs algorithmic selection is the study's main experimental contrast.
- **ResNet50 / VGG19 / DenseNet169**: ImageNet-pretrained convolutional networks (residual, plain deep, and densely connected architectures).
- **Auto-selection (tooth selection model)**: classical image-processing pipeline (Gaussian blur, Otsu, K3M skeleton, sliding boxes) that crops candidate teeth without human input.
- **Fivefold cross-validation**: training/validation repeated over five data partitions, with results averaged.
