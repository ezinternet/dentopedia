---
title: "Clinical application of deep learning for enhanced multistage caries detection in panoramic radiographs"
authors: "Suchaya Pornprasertsuk-Damrongsri, Sirawich Vachmanus, Dhanaporn Papasratorn, Jira Kitisubkanchana, Sarunya Chaikantha, Raweewan Arayasantiparb, Pattanasak Mongkolwat"
year: 2025
doi: "10.1038/s41598-025-16591-4"
category: [artificial-intelligence]
source_collection: pubmed-text
full_text: true
pmid: "41022932"
pmcid: "PMC12480035"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12480035/
text_path: /Users/oracleneo/llm-wiki/papers/pornprasertsuk-2025-deep-learning-multistage-caries-panoramic.txt
text_filename: pornprasertsuk-2025-deep-learning-multistage-caries-panoramic.txt
---

## Why Ingested

Recent (2025) primary deep-learning study performing multistage caries segmentation (enamel / dentine / pulp) on panoramic radiographs — a modality usually considered weaker for caries — with bitewing-confirmed ground truth. It provides a concrete, well-validated primary exemplar of the trends aggregated in the sibling SRs [[artificial-intelligence/albano-2024-artificial-intelligence-radiographic-caries-detection]] and [[artificial-intelligence/abbott-2024-ai-platforms-dental-caries-detection]], and is notable for grading caries *depth* on panoramics (F1 0.85, recall 0.96) rather than binary detection.

## One-line Summary

Retrospective diagnostic model development/validation (500 panoramic radiographs, 1,792 caries in 14,997 teeth, bitewing gold standard) of a two-stage YOLOv5 + Attention U-Net pipeline that segments and stages caries (enamel/dentine/pulp) on panoramics with F1 0.85, accuracy 0.93, recall 0.96 in posterior teeth and strong agreement (κ ≥ 0.9) with radiologists.

## 한줄요약

파노라마 방사선사진 500장(치아 14,997개 중 우식 1,792개, 바이트윙 gold standard)에서 YOLOv5(치아 검출) + Attention U-Net(우식 분할) 2단계 파이프라인으로 우식을 단계별(법랑질/상아질/치수)로 분할·분류한 후향적 진단모델 연구 — 구치부 F1 0.85·정확도 0.93·재현율 0.96, 방사선과 전문의와 강한 일치(κ ≥ 0.9).

## 1. Document Information

- **Title**: Clinical application of deep learning for enhanced multistage caries detection in panoramic radiographs
- **Authors**: Suchaya Pornprasertsuk-Damrongsri, Sirawich Vachmanus, Dhanaporn Papasratorn, Jira Kitisubkanchana, Sarunya Chaikantha, Raweewan Arayasantiparb, Pattanasak Mongkolwat (Faculty of Dentistry / Faculty of ICT, Mahidol University, Thailand)
- **Journal**: Scientific Reports 2025;15(1):33491
- **DOI**: 10.1038/s41598-025-16591-4 · **PMID**: 41022932 · **PMCID**: PMC12480035
- **Study type**: Retrospective single-dataset diagnostic deep-learning model development and internal validation
- **Ethics**: Mahidol University Multi-Faculty Cooperative IRB (MU-MOU CoA.2022/060.1511), approved 15 Nov 2022

## 2. Key Contributions

1. **Bitewing-confirmed ground truth on panoramics.** Departs from prior single-modality work: a 27-year OMFR annotated caries on panoramic radiographs *using the paired same-day bitewing radiographs* (the proximal-caries gold standard) as confirmation, producing a more robust ground truth (1,792 caries across 14,997 teeth from 500 PANs). Annotations stored to the Annotation and Image Markup (AIM) standard for consistency.
2. **Multistage (depth) segmentation, not binary detection.** The system classifies caries into enamel / dentine / pulp involvement — clinically actionable staging rarely combined with clinical validation in prior work.
3. **Two-model architecture.** YOLOv5s tooth detection (crops each tooth to remove class-imbalance / large irrelevant areas) → Attention U-Net caries segmentation on the cropped tooth. This multistage design lets the segmenter operate on higher-resolution ROIs, improving capture of tiny carious lesions.
4. **High-recall (safety-biased) clinical framing.** The model deliberately prioritizes minimizing false negatives (missed lesions) → recall 0.96, positioning it as a decision-support aid (not standalone), with false positives that dentists can usually dismiss.

## 3. Methodology and Architecture

- **Dataset**: 500 panoramic radiographs (Carestream CS9000C; 68–72 kV, 8–10 mA, 15.1 s), each patient with same-day full posterior bitewings (Planmeca ProX / Belmont PHOT-XIIS 505 + VistaScan Mini Plus, 20 lp/mm), Jan–Aug 2022, Mahidol Dental Hospital. Anonymized DICOM.
  - **Inclusion**: age > 13 y; overlapping enamel < outer half of proximal enamel; ≥ 1 caries on bitewing.
  - **Exclusion**: jawbone pathology, distortion/noise, teeth rotated > 90°, AI/DI (amelogenesis/dentinogenesis imperfecta), full-mouth crowns, brackets, ≥ 2 implants per quadrant.
- **Demographics**: 317 F (mean 25.7 y), 183 M (mean 26.2 y). 1,792/9,053 posterior teeth carious.
- **Caries staging (ground truth)**: enamel (radiolucency confined to enamel) 519 surfaces (27.1%); dentine (extends past DEJ into dentine) 1,163 surfaces (60.7%); pulp involvement (large radiolucency reaching pulp chamber ± apical PDL widening / lamina dura thickening) 234 surfaces (12.2%).
- **Calibration / reliability**: 100/500 PANs used. Two OMFRs (21 y, others) independently scored; disagreements resolved by consensus, escalated to a 25-y OMFR if needed. Reliability vs ground truth 0.832 and 0.864; intrarater ICC 0.734; interrater ICC 0.707 (27-y OMFR repeated 100 PANs / 469 caries 2 months later).
- **Tooth detection**: YOLOv5s (~7.2 M params), trained on the public DENTEX Challenge 2023 dataset. On this study's teeth: precision 99.6%, recall 98.9%, mAP50 99.5%, mAP50-95 79.9%.
- **Caries segmentation**: Attention U-Net (Attention Gates on a U-Net backbone). Model selection was empirical on a 100-image subset by mIoU: Attention U-Net 0.484 > Nested U-Net 0.477 > U-Net 0.417 > TransU-Net 0.384 > Swin U-Net 0.204 > R2U-Net 0.027.
- **Training**: 14,997 tooth images extracted; 2,161 caries-annotated images for training, 737 for validation/testing, remainder for expert system evaluation. Binary (caries / non-caries) pixel classification. Intensity normalization. Ubuntu 22.0, AMD Ryzen 9 3950X, RTX 2080 SUPER; Adam, batch size 8, binary cross-entropy, 100 epochs.
- **Evaluation**: pixel-level TP/TN/FP/FN → IoU, DSC, precision, recall, specificity, accuracy; plus a tooth-level confusion matrix (binary label per tooth). Agreement via linear weighted kappa (Conger) and Bland–Altman. Stats in MedCalc v22.023.

## 4. Key Results and Benchmarks

**Quantitative segmentation performance (Table 6):**

| Metric | Posterior teeth | All teeth |
|---|---|---|
| IoU | 0.75 | 0.66 |
| DSC | 0.85 | 0.79 |
| Precision | 0.77 | 0.68 |
| Recall | 0.96 | 0.96 |
| F1-score | 0.85 | 0.79 |
| Specificity | 0.93 | 0.94 |
| Accuracy | 0.93 | 0.94 |

**Agreement with radiologists (weighted kappa, all "strong"/"almost perfect"):**
- Number of teeth with caries: κ = 0.943 (95% CI 0.927–0.958); disagreement in 56/500 cases (11.2%), mostly the radiologist finding one more tooth than AI.
- Enamel caries surfaces: κ = 0.907 (0.871–0.943); AI under-detected in 24/249 surfaces (9.64%).
- Dentine caries surfaces: κ = 0.948 (0.930–0.966); discrepancies 33/436 (7.57%).
- Pulp involvement: κ = 0.981 (0.956–1.000) — highest agreement, only 2/168 (1.19%) discrepancies.

**Bland–Altman**: mean difference 0.13 teeth/radiograph (95% CI 0.098–0.170), limits of agreement −0.66 to 0.93. By stage, mean difference highest for enamel (0.10 surfaces), then dentine (0.08), lowest for pulp (0.01) — all < 1 tooth/surface.

**Confusion matrix (posterior teeth)**: TP 1,725, FN 67; FP (519) > FN, i.e. the model over-predicts caries in healthy teeth (more sensitive than specific). FP sources: palatoglossal space, pulp chamber, corner of mouth opening, cervical burnout, buccal pits, oropharynx, inter-radicular bone, pulpal horns.

**Benchmark vs prior panoramic-caries segmentation (Table 7)**: F1 0.85 exceeds Dayi et al. DCDNet (0.68–0.71), Chen et al. ASPP-U-Net (0.78), Haghanifar et al. PaXNet (F0.5 0.78); below Zhu et al. CariesNet (0.93) and Lian et al. nnU-Net/DenseNet121 (0.90). DSC 0.85 exceeds Dayi (0.68–0.71), Lian (0.66), Alharbi U-Net3+ (0.60); below Zhu (0.94). Authors' recall (0.96) is the highest reported — the study's distinguishing strength. Lower F1/DSC vs Zhu attributed to smaller caries sample (~2/3 of Zhu's).

## 5. Limitations and Future Work

- **Enamel-caries underestimation**: AI systematically under-detects small enamel lesions (a known low-sensitivity zone even for dentists on radiographs); bidirectional stage misclassifications observed (dentine↔enamel; one pulp→dentine), though only in 5/500 cases with no specific trend.
- **False-positive bias**: FP > FN → moderate precision (0.77); over-prediction on anatomical structures. Confirmatory clinical exam / bitewing still needed → **not a standalone diagnostic tool**.
- **Anterior teeth not confirmed**: bitewing confirms only posterior teeth, so anterior caries were unlabeled (AI still detected some, suggesting extensibility).
- **Single-center, single device / internal validation only**; smaller caries sample than top comparators. No external multi-center / multi-device validation.
- **Panoramic-inherent difficulties**: unequal exposure, density/thickness variation, superimposition, geometric distortion (overlapping premolars) add noise.
- **Future**: dentist/student reading with-vs-without AI studies; harder PANs with more overlap; external multi-center data; real-world clinician–AI interaction / workflow-integration studies.

## 6. Related Work

- Prior panoramic caries-segmentation models cited/benchmarked: Zhu et al. CariesNet (2023, DSC 0.94), Lian et al. nnU-Net/DenseNet121 (2021), Dayi et al. DCDNet (2023), Chen et al. ASPP-U-Net (2023), Haghanifar et al. PaXNet (2023), Alharbi et al. U-Net3+ (2023).
- Reported AI caries-detection accuracies across modalities: intraoral photos 0.92, smartphone photos 0.92, bitewing 0.87, panoramic 0.86; MobileNet V2 classification on cropped third molars 0.87; Ying et al. periapical segmentation DSC 0.75.
- Within this wiki: aggregated by SRs [[artificial-intelligence/albano-2024-artificial-intelligence-radiographic-caries-detection]] and [[artificial-intelligence/abbott-2024-ai-platforms-dental-caries-detection]].

## 7. Glossary

- **YOLOv5 (You Only Look Once v5)**: single-stage object-detection CNN; here YOLOv5s (~7.2 M params) crops each tooth.
- **Attention U-Net**: U-Net segmentation network augmented with Attention Gates that focus on salient features.
- **AIM (Annotation and Image Markup)**: standard for storing consistent, structured image annotations.
- **IoU (Intersection-over-Union)**: overlap ÷ union of predicted and ground-truth regions.
- **DSC (Dice Similarity Coefficient)**: 2·overlap ÷ (sum of both areas); F1-equivalent for segmentation.
- **Weighted kappa (Conger)**: chance-corrected agreement; 0.81–1.00 = strong.
- **Bland–Altman**: agreement plot of mean-difference vs mean of two methods.
- **DEJ (dentoenamel junction)**: enamel–dentine boundary; caries crossing it = dentine caries.
- **Cervical burnout**: radiolucent artifact near the cervical tooth region mimicking caries (an FP source).
- **DENTEX Challenge 2023**: public dental panoramic dataset used to pre-train the tooth detector.
