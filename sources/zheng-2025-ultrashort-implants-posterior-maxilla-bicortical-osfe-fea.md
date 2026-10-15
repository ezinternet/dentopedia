---
title: "Application of Ultrashort Implants in Posterior Maxilla With Insufficient Bone Height: A Finite Element Analysis"
authors: "Zheng L, Luo L, Chang L, Ren M, Li F, Liu Y"
year: 2025
doi: 10.1016/j.identj.2024.12.026
pmid: "39779383"
pmcid: "PMC12142781"
category: sinus-lift/transcrestal
source_collection: pubmed-abstract
full_text: true
pdf_path: null
pdf_filename: null
---

## Why Ingested

First FEA study comparing ultrashort implants (3–6 mm) under three surgical approaches — 단겹질 고정 (unicortical fixation), 쌍겹질 고정 (bicortical fixation), and 치조정접근 상악동 거상 (OSFE) — across posterior maxillary bone heights of 3–5 mm. Directly extends [[wiki/sinus-lift/transcrestal/rues-2020-bone-quality-primary-stability-bicortical-sinus]] and [[wiki/sinus-lift/transcrestal/han-2016-primary-stability-bicortical-posterior-maxilla]] by including ultrashort implants and modelling new bone formation after OSFE.

## Three-line Summary

FEA, 14 models: 4 ultrashort implant lengths (3–6 mm) × 3 surgical approaches (unicortical / bicortical / OSFE) in posterior maxilla with RBH 3–5 mm; 150 N load at 30°; stress, strain, and displacement outcomes.
6 mm implants showed lowest stress and displacement across all bone heights and approaches; bicortical fixation reduced cancellous bone strain 3.3–3.4× vs unicortical for 3 mm implants at RBH=5 mm; OSFE with 6 mm implant achieved the best overall stress profile.
For RBH 3–5 mm, 6 mm ultrashort implant + OSFE is biomechanically optimal; bicortical fixation is superior to unicortical but OSFE with appropriate length further reduces peri-implant stress.

## 세줄요약

FEA 14모델: 초단기 임플란트 (3–6 mm) × 3술식 (단겹질/쌍겹질/OSFE) × 잔존골 3–5 mm; 150 N 30° 하중; 응력·변형률·변위.
6 mm 임플란트가 모든 조건에서 최저 응력·변위; 잔존골 5 mm에서 3 mm 임플란트 단겹질 vs 쌍겹질 취소골 변형률 3.3–3.4배 차이; 6 mm + OSFE가 최선.
RBH 3–5 mm에서 6 mm 초단기 + OSFE가 생역학적 최적; 쌍겹질은 단겹질보다 우수하지만 적절한 임플란트 길이의 OSFE가 더 유리.

## Document Information

- **Journal**: International Dental Journal, 2025; 75(3): 2122-2131
- **DOI**: [10.1016/j.identj.2024.12.026](https://doi.org/10.1016/j.identj.2024.12.026)
- **PMC**: PMC12142781
- **Institution**: Dalian University / Dalian University of Technology, China
- **Study type**: Finite element analysis (FEA)
- **Software**: ABAQUS 2020

## Key Contributions

- First FEA comparing unicortical / bicortical / OSFE for ultrashort implants (3–6 mm) in RBH 3–5 mm
- Bicortical fixation reduces cancellous bone strain 3.3–3.4× vs unicortical for 3 mm implants (RBH=5 mm)
- OSFE with 6 mm implant achieves superior stress profile over bicortical in severely atrophic (RBH=3–4 mm)
- Implant displacement proportional to length (6 mm < 5 < 4 < 3 mm); all < 150 μm threshold
- Sinus floor cortex stress highest with shortest implants; 3 mm H5L3 = 53.53 MPa von Mises (highest)

## Methodology

- **Models**: 12 ultrashort + 2 control (8 mm, 10 mm); implant 4.1 mm diameter
- **Bone heights**: RBH 3, 4, 5 mm (atrophic) + 10, 12 mm (control)
- **Surgical approaches**: unicortical (apex below sinus floor), bicortical (apex at/through sinus floor cortex), OSFE (apex inside sinus with new bone formation)
- **New bone formation**: 0.5 mm thick around implant and Schneider membrane after OSFE (3D osteogenesis model)
- **Load**: 150 N at 30° oblique, mesiodistal constraint
- **Outputs**: von Mises stress (implant, sinus floor cortex), principal stress (alveolar ridge), cancellous bone strain, implant displacement

## Key Results

| Condition | Best finding | Worst finding |
|---|---|---|
| Implant length | **6 mm = lowest stress+displacement** | 3 mm = highest (H5L3: 148.90 MPa, 97 μm) |
| Bicortical vs unicortical (RBH=5, 3 mm) | Bicortical: 3.3–3.4× less cancellous strain | Unicortical H5L3: strain 23,000 |
| OSFE 6 mm (H5L6) | Max principal stress 35.77 MPa, min 10.66 MPa | — |
| Sinus floor von Mises | H5L3 unicortical: 53.53 MPa | H5L6 OSFE: lowest |

Cortical bone stress within physiological limits (tensile 121 MPa, compressive 167 MPa) in all models.

## Limitations

- Simplified isotropic homogeneous FEA model; actual anisotropic bone stress 20–30% higher
- Static load only; no fatigue or dynamic chewing simulation
- Single implant diameter (4.1 mm); no variation
- New bone after OSFE modeled as same elastic modulus as native bone — may overestimate OSFE stability

## Related Work

- [[wiki/sinus-lift/transcrestal/rues-2020-bone-quality-primary-stability-bicortical-sinus]] — in vitro, pig scapula: BMD and cortical penetration as stability predictors
- [[wiki/sinus-lift/transcrestal/han-2016-primary-stability-bicortical-posterior-maxilla]] — in vitro polyurethane: ISQ vs RBH levels
- [[wiki/sinus-lift/transcrestal/ahn-2012-implant-stability-preparation-methods-bicortical-monocortical]] — in vitro: preparation × cortical interaction for ISQ
- [[wiki/sinus-lift/transcrestal/hsu-2016-bicortical-fixation-indirect-sinus-unicortical]] — RCT: bicortical vs ISE vs unicortical ISQ

## Glossary

- **Ultrashort implant**: ≤6 mm length (some sources ≤8 mm; this study uses ≤6 mm)
- **OSFE (Osteotome Sinus Floor Elevation)**: 치조정접근 상악동 거상 — transalveolar approach using osteotomes, greenstick fracture of sinus floor
- **Crown-to-implant ratio (CIR)**: Crown length / implant length; ultrashort implants have high CIR (2.33–5.67 in this study)
