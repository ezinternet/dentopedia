---
title: "All-on-Four vs All-on-Six Framework Materials: FEA Biomechanical Comparison"
authors: "Lala Cabbarova, Ali Rıza Tunçdemir, Reza Mohammadi"
year: 2026
date: 2026-01-01
doi: 10.1002/cre2.70277
source: cabbarova-2026-all-on-four-six-framework-fea.md
category: [implants]
confidence: in-vitro
pmcid: PMC12834504
source_collection: pubmed-text
text_path: /Users/oracleneo/llm-wiki/papers/cabbarova-2026-all-on-four-six-framework-fea.txt
text_filename: cabbarova-2026-all-on-four-six-framework-fea.txt
tags: [all-on-four, all-on-six, framework-material, FEA, PEEK, zirconia, titanium, full-arch, biomechanics]
---

## Three-line Summary

FEA study comparing All-on-Four vs All-on-Six mandibular full-arch configurations across 6 framework materials (titanium, zirconia, PEEK, PEKK, Trilor, Trinia) with 150 N bilateral vertical loading on a CBCT-based mandible model (12 models total).

All-on-Six produced more homogeneous, lower stress in peri-implant bone and screws across all materials vs All-on-Four; PEEK/PEKK frameworks transmitted the highest stress to implants and bone (low elastic modulus = more deformation = more load transfer); titanium/zirconia distributed stress most favorably; FRC composites (Trilor/Trinia) showed intermediate clinically acceptable performance.

All-on-Six + rigid frameworks (Ti/Zr) is the biomechanically optimal combination; PEEK/PEKK are contraindicated for full-arch frameworks; FRC materials are viable alternatives if aesthetic or weight constraints exist; All-on-Four's distal cantilever amplifies stress concentration regardless of material.

## 세줄요약

하악 All-on-4 vs All-on-6, 6가지 프레임워크 소재 FEA 비교(12모델; 150 N 양측 수직 교합력).

All-on-6가 전 소재에서 하중 분산 우수 — 원심 임플란트·골·나사 응력 감소; PEEK·PEKK(낮은 탄성계수)는 임플란트·골에 응력 최대 집중; Ti·Zr는 최소 응력; FRC(Trilor·Trinia) 중간값으로 임상 허용 수준.

All-on-6 + Ti/Zr = 최적 생역학 조합; PEEK/PEKK 풀아치 프레임워크 금기; FRC는 PEEK보다 우수하나 Ti/Zr 대비 열등; All-on-4 선택 시 강성 프레임워크 필수이며 캔틸레버 최소화 필수.

## Summary

According to PubMed, this Turkish FEA study (Necmettin Erbakan University) is the first to systematically compare both implant number (4 vs 6) and framework material (6 types) simultaneously for full-arch mandibular prostheses. The null hypothesis — that neither variable affects stress distribution — was rejected.

**Implant number effect**: All-on-Four's 10 mm distal cantilever concentrates stress at the posterior implants. All-on-Six eliminates the cantilever by extending implants to the molar region, distributing forces more evenly. Framework stress reductions of 80–87% were seen when switching from All-on-4 to All-on-6.

**Framework material paradox**: materials with low elastic modulus (PEEK E=4,200 MPa, PEKK E=5,100 MPa) seem "shock-absorbing" but actually deform more under load — transferring higher stress to implants, screws, and peri-implant bone. High-modulus materials (Ti E=110,000 MPa, Zr E=210,000 MPa) deform less and distribute load through the stiff framework rather than concentrating it at bone interfaces.

**FRC composites (Trilor, Trinia)**: Trilor E=26,000 MPa, Trinia E=18,500 MPa — intermediate stiffness. Stress values within clinically acceptable limits; their shock-absorbing properties may reduce chipping/fractures at the crown level but this study did not include fatigue modeling.

All values in cortical bone were below the critical thresholds for bone resorption (compressive 170–190 MPa; tensile 100–130 MPa).

## Key Contributions

- Quantifies the elastic modulus-to-stress transfer relationship across clinically used materials
- Demonstrates that All-on-Six's biomechanical superiority holds regardless of framework material
- First comparative FEA including newer FRC CAD-CAM materials (Trilor, Trinia) alongside traditional options
- Provides clinical guidance: avoid PEEK/PEKK for full-arch frameworks; prefer Ti/Zr or FRC

## Methodology

- 3D FEA; CBCT-based mandible model; Abaqus 2020 software
- All-on-4: anterior axial + 2 posterior at 30°; 10 mm cantilever; 3.7×10 mm implants
- All-on-6: anterior axial + 2 at 15° + 2 at 30°; no cantilever; same implant dimensions
- Load: 150 N bilateral vertical; encastre boundary; fully osseointegrated (tie constraint)
- Screw preload: 25 Ncm tightening → 781 N preload

## Results — Framework Stress (vMS) Comparison

| Material | E (MPa) | All-on-4 (MPa) | All-on-6 (MPa) |
|----------|---------|----------------|----------------|
| Titanium | 110,000 | 1117 | 207 |
| Zirconia | 210,000 | 1372 | 227 |
| Trilor | 26,000 | 818 | 146 |
| Trinia | 18,500 | 795 | 135 |
| PEKK | 5,100 | 692 | 100 |
| PEEK | 4,200 | 806 | 102 |

*Note: higher framework vMS ≠ worse — it means the framework absorbs stress, protecting bone. The concern is when LOW-E materials produce HIGH bone/implant stress despite low framework stress.*

- Cortical bone stress: All-on-4 PEEK/PEKK highest; All-on-6 Ti/Zr lowest
- Abutment stress: All-on-4 posterior region highest regardless of material
- Screw stress: All-on-4 PEEK/PEKK highest (flexible frame → more screw loading)

## Related Papers

- [[overviews/tilted-axial-implant-angled-abutment-overview]] — extends: adds framework material variable to tilted implant biomechanics picture
- [[implants/erdogdu-2024-abutment-angle-bone-quality-fatigue-fea]] — reinforces: FEA biomechanics of full-arch implant configurations; abutment stress patterns
- [[implants/szabo-2022-all-on-four-tilted-distal-implants-mbl]] — applies-to: FEA explains clinical MBL data; All-on-4 distal stress concentration matches Szabó's finding of tilted MBL premium
- [[implants/coskunses-2021-narrow-diameter-implants-full-arch-fixed]] — reinforces: 6-implant clinical MBL advantage is now explained by FEA stress distribution
