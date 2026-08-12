---
title: "Automated quality evaluation of dental panoramic radiographs using deep learning"
authors: Ameli N, Miri Moghaddam M, Lai H, Pacheco-Pereira C
year: 2025
doi: 10.5624/isd.20240232
category: [radiology]
source_collection: pubmed-text
full_text: true
pmid: "40607073"
pmcid: "PMC12210116"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12210116/
text_path: /Users/oracleneo/llm-wiki/papers/ameli-2025-automated-quality-evaluation-dental-panoramic.txt
text_filename: ameli-2025-automated-quality-evaluation-dental-panoramic.txt
---

## Why Ingested

User-requested ingest on panoramic radiograph distortion phenomena; this 2025 paper is the first to apply YOLOv8 for automated quality assessment of OPGs across four distortion/error criteria, directly extending manual audit work already held in [[wiki/radiology/lingam-2023-common-errors-subjective-quality-panoramic]].

## Three-line Summary

Retrospective secondary-data study (n=1,000 OPGs, University of Alberta, 2018–2023) training five YOLOv8 classification models to automate panoramic radiograph quality assessment across artifacts, coverage area, patient positioning, and contrast/density criteria.

YOLOv8 achieved validation accuracies of 87.2% (artifacts), 74.1% (coverage), 77.3% (patient positioning), 97.9% (contrast/density), and 79.3% overall quality; average clinical-acceptability accuracy 81.4%.

Automating panoramic IQA with YOLOv8 is feasible for clinical workflow integration and dental education, though dataset heterogeneity and pixel-level annotation limitations constrain generalizability.

## 세줄요약

캐나다 앨버타 대학 치과대학 데이터베이스(2018–2023)의 파노라마 방사선 사진(Panoramic Radiograph, OPG) 1,000장을 대상으로, 인공물(Artifact)·촬영범위(Coverage)·환자 자세(Patient Positioning)·대조도/농도(Contrast/Density) 4가지 화질 기준에 맞춰 YOLOv8 분류 모델 5개를 훈련한 후향적 이차자료 연구.

검증 정확도: 인공물 87.2%, 촬영범위 74.1%, 환자 자세 77.3%, 대조도/농도 97.9%, 전체 화질 79.3%; 임상적 수용 가능 여부 평균 정확도 81.4%.

파노라마 화상 품질 자동평가(Image Quality Assessment, IQA)에 YOLOv8 적용이 실현 가능하며, 향후 임상 워크플로 통합 및 방사선 교육 도구로 활용 가능하나 데이터셋 다양성 부족과 픽셀 단위 주석 부재가 일반화를 제한한다.

## 1. Document Information
- **Journal**: Imaging Science in Dentistry 2025;55(2):175-188
- **DOI**: 10.5624/isd.20240232
- **PMID**: 40607073 / PMCID: PMC12210116
- **Institution**: Mike Petryk School of Dentistry, University of Alberta, Edmonton, Canada

## 2. Key Contributions

- **First YOLOv8 application** to panoramic radiograph IQA — full-image single-stage classification vs. patch-based CNN predecessors
- **Four-criteria quality framework** with operationalized definitions: artifacts, coverage area, patient positioning (4 error subtypes), contrast/density
- **Clinical acceptability binary classifier** (retake/no-retake decision) achieving 81.4% average accuracy
- **Positioning error taxonomy** with mechanism-linked descriptors: chin height → occlusal plane curvature; midline shift → asymmetric distortion; rotation/tilt → side-differential magnification; A-P error → anterior sharpness/magnification

## 3. Methodology and Architecture

- **Design**: Retrospective secondary data study; ethics-board approved
- **Images**: 1,000 digital OPGs (OrthoPhos XG Series, Dentsply Sirona) from 2018–2023
- **Raters**: 2 trained dentists supervised by board-certified OMFR; inter-rater reliability Kappa 0.74–0.93 ("very good")
- **Model**: YOLOv8 classification (141 layers); Adam-W optimizer; 30 epochs; batch 16; AMP
- **Augmentation**: Scaling, translation, flipping, mosaic (post-split to prevent leakage)
- **Criteria details**:
  - Artifacts: binary (present/absent); n=279 images used
  - Coverage: 3-class (poor/moderate/good); n=409 images
  - Positioning: binary (poor/good); n=391 images
  - Contrast/density: binary (poor/good); n=188 images + proprietary augmented set
  - Overall quality: binary (unacceptable/acceptable); n=396 images

## 4. Key Results and Benchmarks

| Quality Criterion | Validation Accuracy | Note |
|---|---|---|
| Contrast/density | 97.9% | Strongest performance; clear pixel-intensity signal |
| Artifacts | 87.2% | Better at identifying artifact presence than absence |
| Overall quality (clinical acceptability) | 81.4% avg | Retake/no-retake binary decision |
| Patient positioning | 77.3% | Poor positioning detected more accurately (0.77 vs 0.69) |
| Coverage area | 74.1% | Lowest; moderate class most ambiguous |

Inter-rater reliability (Kappa): 0.93 artifacts / 0.89 coverage / 0.87 contrast / 0.74 positioning

Background statistic: up to 22% of panoramic radiographs require retakes clinically (cited literature).

## 5. Limitations and Future Work

- Dataset from single institution/device — limited demographic and equipment diversity
- Image-level labels only; no pixel-wise (bounding-box/segmentation) annotation → misses fine-grained errors
- Imbalanced raw classes required augmentation to compensate; may introduce distributional bias
- Coverage area: boundary between moderate and good inherently subjective; spatial/anatomical landmark cues not exploited
- Real-world clinical integration not validated (latency, EHR linkage, radiographer acceptance)
- **Future**: multi-task learning (all criteria simultaneously), extension to periapical/CBCT, transformer-based (ViT) comparisons, larger multi-center datasets

## 6. Related Work

- Lingam 2023 — manual 10-category audit of 2,629 OPGs (Riyadh); established positioning-error prevalence benchmark (15% unacceptable); this paper automates that assessment
- Choi et al. — criteria framework this paper adopted for scoring
- Delamare et al. — systematic review categorizing panoramic image quality errors (distortion, blur, artifacts, brightness, mispositioning)

## 7. Glossary

- **IQA (Image Quality Assessment)**: systematic evaluation of radiographic image quality for clinical suitability; can be subjective (human expert) or objective (algorithmic/DL model)
- **YOLOv8**: latest generation of the You Only Look Once single-stage real-time object detection/classification CNN; 141-layer architecture with full-image processing (no patch segmentation)
- **Occlusal plane distortion**: geometric deformation of the bite-plane image caused by chin positioning errors — chin too high → excessive curvature; chin too low → flattening
- **Ghost image**: secondary panoramic artifact formed when a radiopaque object lies between the X-ray source and the machine's center of rotation, producing a magnified, blurred, contralateral shadow
- **OMFR (Oral and Maxillofacial Radiologist)**: specialist radiologist serving as ground-truth arbiter for inter-rater discordance
