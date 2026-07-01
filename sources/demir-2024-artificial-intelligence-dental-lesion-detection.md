---
title: "Comprehensive Insights into Artificial Intelligence for Dental Lesion Detection: A Systematic Review"
authors: "Kubra Demir, Ozlem Sokmen, Isil Karabey Aksakalli, Kubra Torenek-Agirman"
year: 2024
doi: "10.3390/diagnostics14232768"
category: [artificial-intelligence]
source_collection: pubmed-text
full_text: true
pmid: "39682676"
pmcid: "PMC11640338"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11640338/
text_path: /Users/oracleneo/llm-wiki/papers/demir-2024-artificial-intelligence-dental-lesion-detection.txt
text_filename: demir-2024-artificial-intelligence-dental-lesion-detection.txt
---

## Why Ingested

Extends the wiki's AI lesion-detection coverage beyond the single-lesion DTA focus of [[artificial-intelligence/sadr-2022-deep-learning-periapical-radiolucent-lesions]] (periapical radiolucency only): this PRISMA SR maps deep-learning lesion detection across FIVE lesion types (periapical, apical, cyst, jawbone, dental caries) and THREE imaging modalities (panoramic, periapical, CBCT), giving a model/architecture landscape (U-Net, AlexNet, YOLOv8) rather than a pooled-accuracy estimate. It also broadens the caries-only scope of the sibling review by Albano 2024 (artificial-intelligence, radiographic caries detection) to the wider lesion-detection problem.

## One-line Summary

PRISMA systematic review (n=29 primary studies, 2019–2024, PROSPERO CRD42024607099) mapping deep-learning dental lesion detection across 5 lesion types, 3 imaging modalities, 14 DL architectures (U-Net most used at 27.59%), 12 augmentation techniques, and 6 recurring challenges with 13 proposed solutions.

## 한줄요약

PRISMA 체계적 문헌고찰(1차 연구 29편, 2019–2024): 치과 병소 탐지용 딥러닝을 5개 병소유형·3개 영상양식(파노라마·치근단·CBCT)·14개 아키텍처(U-Net 27.59%로 최다)·12개 데이터증강 기법·6개 공통 난제(+13개 해결책)로 정리한 지도(map)형 리뷰. 성능 pooling(메타분석)은 없음.

## 1. Document Information

- **Title**: Comprehensive Insights into Artificial Intelligence for Dental Lesion Detection: A Systematic Review
- **Authors**: Kubra Demir, Ozlem Sokmen, Isil Karabey Aksakalli, Kubra Torenek-Agirman
- **Journal**: Diagnostics (Basel) 2024;14(23):2768
- **Year / Date**: 2024 / 2024-12-09
- **DOI**: 10.3390/diagnostics14232768
- **PMID**: 39682676 · **PMCID**: PMC11640338
- **Registration**: PROSPERO CRD42024607099
- **Type**: Systematic review (PRISMA; qualitative synthesis, NO meta-analysis)
- **Design**: 29 primary studies (2019–2024) from IEEE Xplore, Web of Science, Springer, Google Scholar, ScienceDirect, PubMed. 350 records screened → 37 duplicates removed → 313 assessed → 284 excluded → 29 included. Quality-assessed via Kitchenham criteria (reporting/rigor/credibility/relevance, 0–10; all included studies scored ≥ 6.5).

## 2. Key Contributions

1. **Structured GQM/PRISMA map of the field** answering 4 research questions: (RQ1) object/lesion types, (RQ2) state-of-the-art DL approaches, (RQ3) data-augmentation methods, (RQ4) challenges + solutions.
2. **Lesion-type taxonomy** across modalities — periapical (62.07% of studies), apical (34.48%), cyst (6.9%), dental caries (6.9%), jawbone/maxillary bone (3.45%).
3. **Architecture landscape** — 14 DL models catalogued; U-Net dominant (27.59%), with AlexNet, YOLOv3/v5/v8, CNN, GoogleNet, Denti.AI, DentaVN, RetinaNet, SqueezeNet, SAM, ResNet50, DetectNet, MobileNetV2, VGG16/19.
4. **Augmentation catalogue** — 12 techniques; flip and rotation/reflection most impactful (each 17.24%).
5. **Challenge–solution mapping** — 6 recurring challenges (data scarcity, poor image quality, limited generalization, lesion ambiguity, model complexity, overfitting) linked to 13 proposed solutions.

## 3. Methodology and Architecture

- **Guidelines**: PRISMA (updated), Kitchenham et al. SR methodology, Wohlin, Basili Goal–Question–Metric (GQM).
- **Search queries**: e.g. "lesion detection OR object types AND dental images"; "lesion detection AND deep learning methods"; "state-of-the-art solutions AND dental images"; "application areas AND lesion detection". First two database pages considered (2018–2024 window), 350 records.
- **Quality assessment**: Kitchenham scoring yes=1 / somewhat=0.5 / no=0 across four dimensions (reporting, rigor, credibility, relevance). Cutoff avg > 5; all 29 passed (7 studies scored 9.0–9.5; none ≤ 6.0). Data extraction via Google-Sheet form (study ID, title, authors, year, publication type, publisher, per-RQ findings).
- **Not a meta-analysis**: findings synthesized qualitatively with counts/percentages; no pooled diagnostic accuracy.

## 4. Key Results and Benchmarks

**Lesion types (RQ1)** — periapical 62.07%; apical 34.48%; cyst 6.9%; dental caries 6.9%; jawbone/maxillary 3.45% (studies may use multiple modalities).

**Representative per-study metrics from the DL-approach synthesis (RQ2):**
- **U-Net**: S14 CBCT periapical detection accuracy 93% (Dice per class: lesion 52%, bone 78%, tooth 74%, background 95%, restorative 58%); S15 CBCT sensitivity 86.7% / specificity 84.3%; S10 panoramic apical F1 82.8/81.5/74.2% at IoU 0.3/0.4/0.5; S19 segmentation accuracy 98.1% (vs Mask-RCNN 46.7%); S18 accuracy 95.8% / F1 95.5% / sensitivity 95.2%.
- **AlexNet**: S8 92.5% (panoramic+periapical+CBCT); S9 96.21% periapical; S27 98% (AlexNet feature extraction → SVM).
- **YOLO**: S1 YOLOv3 accuracy 86.3%, sensitivity 92.1%, F1 89%; S4 YOLOv5 mAP@0.5 0.61; S12 YOLOv3 F1 71% / sensitivity 98%; S7 YOLOv8 > YOLOv5 for lesion detection.
- **CNN**: S13 accuracy 74.95% (18,618 periapical root areas / 713 panoramic); S29 95.85%.
- **Others**: GoogleNet S6 97.10%, S8 89.36%; SqueezeNet S6 99.9% (caries); DentaVN (Faster R-CNN) S28 accuracy 95.6% / sens 89.5% / spec 97.9%; RetinaNet S17 best model (accuracy up to 81.2%, F1 up to 89.5%); Denti.AI S11 +8.6% AFROC-AUC; ResNet50 S8 86.65%; VGG16/19 S8 87.94%, S26 70% (Siamese+DenseNet-121); DetectNet S2 cyst 75–77%; SAM S7 60%; MobileNetV2 S25 radicular-cyst classification sens 95% / spec 86%.
- Notable failure signal: S24 (2902 panoramic, U-Net) sens 92% / spec 84% / F1 88% but **49% of periapical radiolucencies missed**.

**Augmentation (RQ3)** — 12 techniques: brightness/contrast, horizontal mirroring, trapezoid transform, resizing, cropping, translation, scaling, shifting, sharpening, positioning/zoom, grayscale, and flip+rotation/reflection. Flip and rotation/reflection each 17.24% (most common).

**Challenges + solutions (RQ4)** — 6 challenges: data scarcity, poor image quality, limited generalization, lesion ambiguity, model complexity, overfitting. 13 solutions: data augmentation, image pre-processing, model optimization, model training, additional loss functions, cross-validation, transfer learning, performance evaluation, model customization, data diversification, multi-model approaches, multi-scale CNNs, expert opinion.

## 5. Limitations and Future Work

- **No meta-analysis / no pooled accuracy** — heterogeneous datasets, metrics, and modalities preclude quantitative synthesis; reported metrics are per-study and non-comparable.
- **Small, non-standardized primary datasets** and inconsistent labeling; augmentation can introduce anatomical misinterpretation (e.g. X-ray flips distort maxilla–mandible alignment) if applied unrealistically.
- **Search scope** limited to first two database pages (2018–2024), risking selection bias; grey literature and non-English work under-covered.
- Authors call for larger integrated datasets, model optimization, and diversified data sources; solutions must generalize "regardless of image type, data quantity, and data quality."

## 6. Related Work

- [[artificial-intelligence/sadr-2022-deep-learning-periapical-radiolucent-lesions]] — DTA SR+MA restricted to periapical radiolucency; Demir extends the scope to 5 lesion types and gives an architecture map instead of a pooled estimate.
- Albano 2024 (SR of AI for radiographic **caries** detection; artificial-intelligence source stub) — caries-only counterpart; Demir subsumes caries into a broader lesion-detection landscape.

## 7. Glossary

- **U-Net** — encoder–decoder CNN for semantic segmentation; dominant architecture here (27.59%).
- **YOLO (v3/v5/v8)** — one-stage real-time object detectors; v8 = optimized successor of v5 (PyTorch).
- **AlexNet / VGG16-19 / GoogleNet (InceptionV1) / ResNet50** — classic CNN classification backbones, often used via transfer learning.
- **RetinaNet** — one-stage detector using focal loss to counter class imbalance (ResNet/ResNeXt backbone).
- **SAM (Segment Anything Model)** — Meta FAIR instance-segmentation foundation model.
- **Faster R-CNN** — two-stage region-proposal detector (backbone of the DentaVN tool).
- **CBCT** — cone-beam computed tomography; 3D, non-superposed dental imaging.
- **mAP / IoU / Dice / AFROC-AUC** — detection/segmentation metrics (mean average precision; intersection-over-union; Dice overlap; alternative FROC area-under-curve).
- **PRISMA / PROSPERO / GQM** — SR reporting standard / prospective SR registry / Goal–Question–Metric scoping method.
