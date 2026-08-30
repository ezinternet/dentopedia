---
title: "AI-Assisted 3D Histological Reconstruction for Trabecular Microarchitecture Assessment"
authors: "Báskay et al."
year: 2024
date: 2024-02-15
doi: "10.3390/jcm13041106"
source: baskay-2024-ai-histological-reconstruction-trabecular.md
category: [bone-biology]
confidence: in-vitro
pdf_path: /Users/oracleneo/llm-wiki/papers/baskay-2024-ai-histological-reconstruction-trabecular.pdf
pdf_filename: baskay-2024-ai-histological-reconstruction-trabecular.pdf
source_collection: external
tags: [AI, histology, microCT, trabecular-bone, bone-microarchitecture, sinus-augmentation, U-Net, BV-TV]
---

## One-line Summary
In vitro methodology study (1 sinus augmentation biopsy): AI (U-Net)-assisted 3D histological reconstruction achieves strong correlation with microCT for trabecular microarchitecture (BV/TV r=0.777, Tb.Th r=0.666) — simultaneous histological + architectural information.

## 한줄요약
방법론 연구 (상악동 거상 골생검 1개): AI (U-Net) 3D 조직 재구성이 microCT 골소주 파라미터와 강한 상관관계 (BV/TV r=0.777, Tb.Th r=0.666) — 조직학적 정보와 구조 정보 동시 획득.

## Summary
Báskay et al. at Semmelweis University developed a pipeline for three-dimensional histological reconstruction of bone biopsy samples using AI-based tissue classification and transformer-based section alignment. A single bone core biopsy from a sinus augmentation re-entry was processed: serial H&E sections (~5μm) were classified by a modified U-Net, then aligned using detector-free local feature matching. The resulting 3D histological reconstruction was compared to microCT reconstruction of the same sample using five trabecular microarchitecture parameters. Correlation coefficients ranged from 0.666 (Tb.Th) to 0.777 (BV/TV), and Bland-Altman analysis confirmed good agreement for BV/TV. This method uniquely provides both structural (architectural) and biological (tissue type) information simultaneously — a capability microCT alone cannot offer. The study is a proof-of-concept with n=1, requiring larger validation cohorts before clinical application.

## Key Contributions
- First application of AI (U-Net + transformer alignment) for 3D histological reconstruction in dental bone research
- Validates reconstruction vs microCT for all 5 standard trabecular parameters
- Strongest agreement for BV/TV (r=0.777) — the most clinically relevant parameter
- Simultaneous histological tissue classification + microarchitecture — unique advantage over microCT alone
- Applicable to re-entry bone biopsies from augmentation sites — clinically actionable timing

## Methodology
- 1 bone core biopsy: sinus floor augmentation re-entry
- MicroCT: SkyScan 1272, 11μm voxel, Bruker CTAn
- Histology: FFPE, 5μm serial sections, H&E, 3Dhistech Panoramic 1000 scanner
- AI: Modified U-Net for tissue segmentation; detector-free local feature matching (transformers) for section alignment
- Parameters: BV/TV, BS/TV, Tb.Pf, Tb.Th, Tb.Sp
- Analysis: Pearson correlation coefficients + Bland-Altman plots + mountain plots

## Results
- Correlation (histological reconstruction vs microCT):
  - BV/TV: r=0.777 (strongest)
  - BS/TV: r=0.717
  - Tb.Pf: r=0.705
  - Tb.Sp: r=0.687
  - Tb.Th: r=0.666
- Bland-Altman: good BV/TV agreement between methods
- Proof-of-concept level — n=1 sample

## Related Papers
- [[bone-biology/shemtovyona-2021-jawbone-quality-quantitative-meta-analysis]] — bone quality classification from CBCT; this study offers histological ground truth methodology
- [[bone-biology/palominozorrilla-2024-jawbone-quality-classification-scoping]] — scoping review calling for validated bone quality assessment methods; this paper advances histomorphometry methodology
- [[bone-biology/chen-2023-occlusal-force-alveolar-bone-type-h-angiogenesis]] — bone biology and vascularity in implant sites (complementary biology)
