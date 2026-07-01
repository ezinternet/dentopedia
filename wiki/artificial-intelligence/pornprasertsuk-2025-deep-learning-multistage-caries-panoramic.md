---
title: "Clinical application of deep learning for enhanced multistage caries detection in panoramic radiographs"
authors: "Suchaya Pornprasertsuk-Damrongsri et al."
year: 2025
date: 2025-09-29
doi: "10.1038/s41598-025-16591-4"
source: pornprasertsuk-2025-deep-learning-multistage-caries-panoramic.md
category: [artificial-intelligence]
confidence: retrospective
source_collection: pubmed-text
full_text: true
pmid: "41022932"
pmcid: "PMC12480035"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12480035/
text_path: /Users/oracleneo/llm-wiki/papers/pornprasertsuk-2025-deep-learning-multistage-caries-panoramic.txt
text_filename: pornprasertsuk-2025-deep-learning-multistage-caries-panoramic.txt
tags: [artificial-intelligence, deep-learning, YOLOv5, attention-U-Net, caries-segmentation, panoramic-radiograph, multistage-caries]
relations:
  - type: applies-to
    target: albano-2024-artificial-intelligence-radiographic-caries-detection
---

## One-line Summary

Retrospective single-dataset deep-learning study (500 panoramic radiographs, 1,792 caries in 14,997 teeth, same-day bitewing gold standard) of a two-stage YOLOv5 + Attention U-Net pipeline that segments and stages caries (enamel/dentine/pulp) on panoramics — F1 0.85, accuracy 0.93, recall 0.96 in posterior teeth, with strong-to-almost-perfect agreement (weighted κ 0.907–0.981) with radiologists.

## 한줄요약

파노라마 500장(치아 14,997개 중 우식 1,792개, 당일 촬영 바이트윙 gold standard) 후향 데이터셋에서 YOLOv5(치아 검출)+Attention U-Net(우식 분할) 2단계 딥러닝으로 우식을 법랑질/상아질/치수 단계별로 분할한 진단모델 연구 — 구치부 F1 0.85·정확도 0.93·재현율 0.96, 방사선과 전문의와 강한~거의 완벽 일치(가중 κ 0.907–0.981).

## Summary

Caries is usually overlooked on panoramic radiographs because of lower resolution and superimposition, so bitewing remains the proximal-caries gold standard. This study asks whether deep learning can recover clinically useful, *depth-staged* caries detection from panoramics. The key methodological move is the ground truth: for each of 500 PANs, the same patient's same-day full posterior bitewings were used by an experienced oral-and-maxillofacial radiologist to confirm and annotate caries on the panoramic image, yielding 1,792 lesions across 14,997 teeth, staged as enamel (27.1%), dentine (60.7%), or pulp involvement (12.2%).

A two-model pipeline (YOLOv5s crops each tooth → Attention U-Net segments caries on the cropped tooth) achieved F1 0.85 / accuracy 0.93 / recall 0.96 for posterior teeth and strong agreement with radiologists across all stages (weighted κ: teeth-with-caries 0.943, enamel 0.907, dentine 0.948, pulp 0.981). The model is deliberately high-recall (few missed lesions) at the cost of over-predicting caries on healthy teeth (FP 519 > FN 67 in posterior teeth), so the authors position it as decision support, not a standalone diagnostic tool. It is a concrete primary-study instance of the AI-caries-detection trends aggregated in [[artificial-intelligence/albano-2024-artificial-intelligence-radiographic-caries-detection]] and [[artificial-intelligence/abbott-2024-ai-platforms-dental-caries-detection]], notable for grading depth on a modality that usually underperforms for caries.

## Key Contributions

- **Bitewing-confirmed ground truth on panoramics** — combines two modalities (BW gold standard + PAN) instead of single-modality annotation, giving more reliable labels for a hard modality.
- **Multistage (depth) segmentation** — enamel / dentine / pulp staging, not binary detection; the clinically actionable dimension.
- **Two-model (multistage) architecture** — tooth-crop first, then segment, which raises effective ROI resolution and mitigates class imbalance for tiny lesions.
- **Safety-biased high recall (0.96)** — prioritizes minimizing false negatives; frames AI as an aid dentists can correct, not a replacement.

## Methodology

- **Design**: retrospective, single-center (Mahidol Dental Hospital), single-dataset model development + internal validation. 500 PANs (Carestream CS9000C) each with same-day full posterior bitewings; 317 F / 183 M, mean age ~26 y.
- **Ground truth**: 1,792 caries in 14,997 teeth, annotated by a 27-year OMFR using paired bitewings, stored to the AIM (Annotation and Image Markup) standard; staged enamel 519 / dentine 1,163 / pulp 234 surfaces. Calibration on 100 PANs (reliability vs GT 0.832–0.864; intrarater ICC 0.734; interrater ICC 0.707).
- **Tooth detection**: YOLOv5s (~7.2 M params), pretrained on DENTEX Challenge 2023 → precision 99.6%, recall 98.9%, mAP50 99.5%.
- **Caries segmentation**: Attention U-Net, chosen empirically on a 100-image subset (mIoU 0.484, beating Nested U-Net 0.477, U-Net 0.417, TransU-Net 0.384, Swin U-Net 0.204, R2U-Net 0.027). 2,161 caries images train / 737 val-test; Adam, batch 8, BCE loss, 100 epochs, RTX 2080 SUPER.
- **Evaluation**: pixel-level IoU/DSC/precision/recall/specificity/accuracy + tooth-level confusion matrix; weighted kappa (Conger) and Bland–Altman for agreement.

## Results

**Segmentation metrics:**

| Metric | Posterior teeth | All teeth |
|---|---|---|
| IoU | 0.75 | 0.66 |
| DSC | 0.85 | 0.79 |
| Precision | 0.77 | 0.68 |
| Recall | 0.96 | 0.96 |
| F1-score | 0.85 | 0.79 |
| Specificity | 0.93 | 0.94 |
| Accuracy | 0.93 | 0.94 |

**Agreement (weighted κ):** teeth with caries 0.943 (CI 0.927–0.958); enamel 0.907; dentine 0.948; pulp involvement 0.981 — all strong to almost perfect, highest for pulp (distinct radiographic features).

**Bland–Altman:** mean difference 0.13 teeth/PAN (CI 0.098–0.170), LoA −0.66 to 0.93; per-stage mean difference enamel 0.10 > dentine 0.08 > pulp 0.01 (all < 1 surface).

**Confusion matrix (posterior):** TP 1,725, FN 67, FP 519 → over-predicts caries in healthy teeth (more sensitive than specific). FP sources include cervical burnout, buccal pits, pulpal horns, palatoglossal space, oropharynx — structures dentists can usually dismiss.

**Error profile:** systematic enamel-caries under-detection (small lesions; even dentists have low radiographic sensitivity here); bidirectional stage misclassification (dentine↔enamel; one pulp→dentine) but only in 5/500 cases.

**Benchmark:** F1 0.85 beats DCDNet (0.68–0.71), ASPP-U-Net (0.78), PaXNet (0.78) but trails CariesNet (0.93) and Lian nnU-Net/DenseNet121 (0.90) — attributed to a smaller caries sample. Recall 0.96 is the highest reported. Authors' bottom line: promising decision-support aid, not a standalone diagnostic tool; needs external multi-center validation.

## Related Papers

- [[artificial-intelligence/albano-2024-artificial-intelligence-radiographic-caries-detection]] — applies-to: a concrete primary DL study whose panoramic multistage results exemplify (and are aggregated by) this SR of AI radiographic caries detection.
- [[artificial-intelligence/abbott-2024-ai-platforms-dental-caries-detection]] — reinforces: independent single-model performance data point (F1 0.85, recall 0.96) consistent with this SR's synthesis of AI caries-detection platforms; both stress AI as adjunct, not standalone.
