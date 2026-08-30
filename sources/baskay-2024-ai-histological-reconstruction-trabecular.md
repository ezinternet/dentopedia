---
title: "Are Artificial Intelligence-Assisted Three-Dimensional Histological Reconstructions Reliable for the Assessment of Trabecular Microarchitecture?"
authors: "János Báskay, Dorottya Pénzes, Endre Kontsek, Adrián Pesti, András Kiss, Bruna Katherine Guimarães Carvalho, Miklós Szócska, Bence Tamás Szabó, Csaba Dobó-Nagy, Dániel Csete, Attila Mócsai, Orsolya Németh, Péter Pollner, Eitan Mijiritsky, Márton Kivovics"
year: 2024
doi: "10.3390/jcm13041106"
category: [bone-biology]
pdf_path: /Users/oracleneo/llm-wiki/papers/baskay-2024-ai-histological-reconstruction-trabecular.pdf
pdf_filename: baskay-2024-ai-histological-reconstruction-trabecular.pdf
source_collection: external
---

## Why Ingested
AI(U-Net) 기반 연속 조직 절편 3D 재구성으로 골소주 미세구조를 microCT와 비교 검증 — [[bone-biology/bone-biology]] 및 [[wiki/overviews/bone-quality-implant-risk-modification-overview]]에서 다루는 골질 평가 방법론의 디지털화 방향에 해당하는 기술 논문.

## One-line Summary
In vitro methodology study: AI-assisted (U-Net) 3D histological reconstruction of sinus augmentation bone biopsy shows strong correlation with microCT for trabecular microarchitecture parameters (r=0.666–0.777).

## 한줄요약
방법론 연구: AI (U-Net) 기반 상악동 거상 골생검 3D 조직 재구성이 microCT 골소주 미세구조 파라미터와 강한 상관관계 달성 (r=0.666–0.777).

## 1. Document Information
- Journal: Journal of Clinical Medicine, vol. 13, article 1106, 2024
- DOI: 10.3390/jcm13041106
- Received: 8 Jan 2024; Revised: 4 Feb 2024; Accepted: 12 Feb 2024; Published: 15 Feb 2024
- Affiliation: Semmelweis University (Budapest), Eötvös Loránd University, Tel Aviv University / Tel-Aviv Sourasky Medical Center
- Corresponding: Márton Kivovics (kivovics.marton@semmelweis.hu)

## 2. Key Contributions
- First 3D histological reconstruction using AI (U-Net) tissue classification + detector-free local feature matching (transformers) for dental bone biopsy
- Validates reconstruction against microCT for 5 trabecular microarchitecture parameters
- Strong linear correlation r=0.777 for BV/TV (bone volume/tissue volume) — key osseointegration parameter
- Good Bland-Altman agreement for BV/TV between methods
- Provides simultaneous histological tissue information + microarchitectural data — a capability microCT alone cannot offer
- Method applicable to re-entry bone biopsies from augmentation sites

## 3. Methodology and Architecture
- Sample: 1 bone core biopsy from re-entry sinus floor augmentation
- MicroCT: SkyScan 1272, 11μm voxel, 60 kV, 66 mA; Bruker CTAn software
- Histology: FFPE, ~5μm sections, H&E stain; 3Dhistech Panoramic 1000 scanner
- AI: Modified U-Net architecture trained for tissue classification on H&E sections
- Alignment: Detector-free local feature matching with transformers (stepwise affine transformation)
- Pre-processing: OpenSlide + OpenCV; ROI detection at lowest resolution then scaled
- Parameters: BV/TV, BS/TV, Tb.Pf, Tb.Th, Tb.Sp — standard histomorphometry metrics
- Comparison: correlation coefficients + Bland-Altman plots + mountain plots

## 4. Key Results and Benchmarks
- Correlation microCT vs histological reconstruction:
  - BV/TV: r=0.777 (strongest)
  - BS/TV: r=0.717
  - Tb.Pf (trabecular pattern factor): r=0.705
  - Tb.Th (trabecular thickness): r=0.666
  - Tb.Sp (trabecular separation): r=0.687
- Bland-Altman: good agreement for BV/TV between methods
- Mountain plots: agreement confirmed
- Single biopsy — proof-of-concept; not population statistics

## 5. Limitations and Future Work
- n=1 biopsy sample — proof-of-concept study; not powered for clinical validation
- Decalcification and FFPE processing may alter dimensions (shrinkage artifact)
- Damaged/torn slides excluded — limits completeness
- Computational intensity high (MIRAX 100,000×200,000 pixel images)
- Manual validation of AI tissue classification not described in detail
- Requires specialized AI infrastructure — not clinic-ready

## 6. Related Work
- MicroCT as gold standard for trabecular microarchitecture (Bruker CTAn widely validated)
- SkyScan platform used in multiple sinus augmentation histomorphometry studies
- BV/TV as primary osseointegration quality parameter (Albrektsson standards)
- Histomorphometry for bone augmentation biopsy evaluation (standard of care)

## 7. Glossary
- **U-Net**: deep learning architecture for image segmentation — originally developed for biomedical imaging
- **BV/TV**: bone volume fraction (%) — key measure of trabecular bone density
- **BS/TV**: bone surface density
- **Tb.Pf**: trabecular pattern factor — measures trabecular convexity/concavity (connectivity)
- **Tb.Th**: mean trabecular thickness (μm)
- **Tb.Sp**: mean trabecular separation/spacing (μm)
- **Bland-Altman plot**: graphical method for agreement between two measurement methods
- **FFPE**: formalin-fixed paraffin-embedded tissue block (standard histology preparation)
- **Detector-free local feature matching**: transformer-based image alignment without explicit feature detectors
