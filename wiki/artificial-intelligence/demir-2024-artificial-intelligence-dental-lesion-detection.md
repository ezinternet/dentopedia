---
title: "Comprehensive Insights into Artificial Intelligence for Dental Lesion Detection: A Systematic Review"
authors: "Kubra Demir et al."
year: 2024
date: 2024-12-09
doi: "10.3390/diagnostics14232768"
source: demir-2024-artificial-intelligence-dental-lesion-detection.md
category: [artificial-intelligence]
confidence: sr
source_collection: pubmed-text
full_text: true
pmid: "39682676"
pmcid: "PMC11640338"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11640338/
text_path: /Users/oracleneo/llm-wiki/papers/demir-2024-artificial-intelligence-dental-lesion-detection.txt
text_filename: demir-2024-artificial-intelligence-dental-lesion-detection.txt
tags: [artificial-intelligence, deep-learning, dental-lesion-detection, U-Net, YOLO, CBCT, panoramic, systematic-review, PRISMA]
relations:
  - type: extends
    target: sadr-2022-deep-learning-periapical-radiolucent-lesions
---

## Three-line Summary

PRISMA/Kitchenham systematic review (29 primary studies, 2019–2024, 350 records screened) mapping deep-learning dental lesion detection across 5 lesion types, 3 imaging modalities (periapical/panoramic/CBCT), and 14 architectures — a qualitative field map, not a pooled-accuracy meta-analysis.

U-Net dominated architecture use (27.59%), periapical lesions were the most-studied target (62.07%), representative per-study performance spanned accuracy 73%–99%, and 12 augmentation techniques were catalogued with flip/rotation most common.

Deep-learning lesion detection is promising but not yet generalizable due to small single-institution datasets; 6 identified challenges with 13 proposed solutions (data diversification, transfer learning, multi-model) guide future model design.

## 세줄요약

PRISMA/Kitchenham 방법론으로 딥러닝 치과 병소 검출을 다룬 29편 1차 연구(2019–2024)의 체계적 문헌고찰: 치근단 62.07%·치근단병변 34.48%·낭종 6.9%·우식 6.9%·악골 3.45%의 5개 병소 유형, 치근단/파노라마/Cone-Beam Computed Tomography(CBCT) 3개 영상 양식.

14개 딥러닝 아키텍처(U-Net 27.59% 최다 → AlexNet·YOLO 계열·GoogleNet·DentaVN 등)와 12개 데이터 증강 기법, 6개 난제+13개 해결책을 목록화; 성능 수치는 연구별 기술적 보고로 메타분석은 없음.

딥러닝 병소 검출은 유망하나 소규모·단일 기관 데이터·낮은 일반화가 한계 — 데이터 다양화·멀티모델·전이 학습 등 13개 해결책 제안, 다기관 외부 검증 필요.

## Summary

Demir et al. (2024) systematically review deep-learning (DL) methods for detecting dental lesions on panoramic radiographs, periapical radiographs, and cone-beam CT (CBCT). Following PRISMA (PROSPERO CRD42024607099) and Kitchenham SR methodology, 350 records were screened down to 29 primary studies (2019–2024). Using a Goal–Question–Metric frame, the review answers four questions: which lesion/object types are detected, which state-of-the-art DL architectures are used, which data-augmentation techniques help, and what challenges and solutions recur. The output is a structured landscape of the field — lesion-type prevalence, architecture usage counts, augmentation catalogue, and a challenge→solution mapping — rather than a quantitative meta-analysis (metrics are reported per study and are not pooled).

## Key Contributions

- A **cross-modality, multi-lesion map** of DL lesion detection (5 lesion types × 3 imaging modalities), broader than prior single-lesion / caries-only reviews.
- An **architecture usage ranking** across 14 DL models, identifying U-Net as dominant and characterizing the roles of YOLO variants, AlexNet, CNN, GoogleNet, and tool-based systems (Denti.AI, DentaVN).
- A **12-technique augmentation catalogue** with usage frequencies and a caution on anatomically unrealistic transforms.
- A **6-challenge / 13-solution** synthesis to guide future model design (generalization, data quality, overfitting).

## Methodology

- **Standards**: PRISMA (updated), Kitchenham et al. SR method, Wohlin, Basili GQM.
- **Databases**: IEEE Xplore, Web of Science, Springer, Google Scholar, ScienceDirect, PubMed (2018–2024 window; first two result pages).
- **Selection**: 350 records → 37 duplicates removed → 313 assessed → 284 excluded → **29 included**.
- **Quality**: Kitchenham 4-dimension scoring (reporting, rigor, credibility, relevance; yes=1/somewhat=0.5/no=0). All included studies scored ≥ 6.5; 7 studies scored 9.0–9.5; none ≤ 6.0.
- **Synthesis**: qualitative with counts/percentages per research question. **No meta-analysis** — heterogeneity of datasets, metrics, and modalities precludes pooling.

## Results

- **29 primary studies (2019–2024)**; publication activity peaked in 2022, mostly journal articles.
- **5 lesion types** (share of studies): periapical **62.07%**, apical **34.48%**, cyst **6.9%**, dental caries **6.9%**, jawbone/maxillary bone **3.45%**.
- **14 DL approaches** — **U-Net most used (27.59%)**, followed by AlexNet, YOLOv3/v5/v8, CNN, GoogleNet, Denti.AI, DentaVN, RetinaNet, SqueezeNet, SAM, ResNet50, DetectNet, MobileNetV2, VGG16/19. Representative per-study performance:
  - **U-Net** — S14 CBCT periapical accuracy 93% (Dice: lesion 52% / bone 78% / tooth 74% / background 95% / restorative 58%); S15 CBCT sens 86.7% / spec 84.3%; S10 apical F1 82.8/81.5/74.2% at IoU 0.3/0.4/0.5; S19 segmentation accuracy 98.1% (vs Mask-RCNN 46.7%); S18 accuracy 95.8% / F1 95.5% / sens 95.2%.
  - **AlexNet** — S8 92.5% (panoramic+periapical+CBCT); S9 96.21%; S27 98% (AlexNet features → SVM).
  - **YOLO** — S1 YOLOv3 accuracy 86.3% / sens 92.1% / F1 89%; S4 YOLOv5 mAP@0.5 0.61; S12 YOLOv3 F1 71% / sens 98%; S7 **YOLOv8 > YOLOv5** for lesion detection.
  - **CNN** — S13 accuracy 74.95% (18,618 periapical root areas across 713 panoramic images); S29 95.85%.
  - **Tools / others** — GoogleNet 89–97%; SqueezeNet S6 99.9% (caries); **DentaVN** (Faster R-CNN) accuracy 95.6% / sens 89.5% / spec 97.9%; **RetinaNet** best model in S17 (accuracy up to 81.2%, F1 up to 89.5%); **Denti.AI** +8.6% AFROC-AUC; ResNet50 86.65%; VGG16/19 70–87.94%; DetectNet cyst 75–77%; **SAM** only 60%; MobileNetV2 radicular-cyst sens 95% / spec 86%.
  - **Failure signal**: S24 (2902 panoramic, U-Net) reached sens 92% / spec 84% / F1 88% but **missed 49% of periapical radiolucencies** — a caution against over-reading headline accuracy.
- **12 augmentation techniques** — brightness/contrast, horizontal mirroring, trapezoid transform, resizing, cropping, translation, scaling, shifting, sharpening, positioning/zoom, grayscale, and flip+rotation/reflection. **Flip and rotation/reflection each 17.24%** (most common and most impactful).
- **6 challenges** — data scarcity, poor image quality, limited generalization, lesion ambiguity, model complexity, overfitting.
- **13 proposed solutions** — data augmentation, image pre-processing, model optimization, model training, additional loss functions, cross-validation, transfer learning, performance evaluation, model customization, data diversification, multi-model approaches, multi-scale CNNs, expert opinion.
- **Bottom line**: DL lesion detection is promising but not yet generalizable; solutions must hold "regardless of image type, data quantity, and data quality."

## Related Papers

- [[artificial-intelligence/sadr-2022-deep-learning-periapical-radiolucent-lesions]] — **extends**: Sadr 2022 is a diagnostic-test-accuracy SR+MA confined to periapical radiolucent lesions and gives a pooled estimate; Demir 2024 broadens scope to 5 lesion types × 3 modalities and provides an architecture/augmentation/challenge map instead of a pooled accuracy.
- [[artificial-intelligence/albano-2024-artificial-intelligence-radiographic-caries-detection]] — caries-only counterpart; Demir subsumes caries into the wider lesion-detection problem.
