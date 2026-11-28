---
title: "Effect of Preparation Design on the Trueness and Precision of Intraoral Scanners: A Comparative Analysis Across Two IOS Systems"
authors: "Sanioğlu ŞH, Karol FE, Harorlı OT"
year: 2026
doi: "10.1111/jerd.70263"
category: [digital-workflow]
pdf_path: N/A
pdf_filename: N/A
source_collection: pubmed-abstract
---

## Why Ingested
지대치 삭제 형태(preparation design)가 IOS 정확도에 미치는 영향을 9가지 준비 디자인으로 체계화한 연구 — [[digital-workflow/revilla-leon-2025-tooth-preparation-factors-ios-accuracy-sr]] SR을 개별 디자인별 수치로 보완하며, 프라임스캔의 삭제 형태 의존성을 임상 결정에 직접 연결한다.

## One-line Summary
In vitro study (9 crown preparation designs × 2 IOS): preparation geometry significantly affected IOS trueness (p < 0.001), with scanner type showing no main effect but a significant interaction.

## 한줄요약
9가지 크라운 준비 디자인 × 2 IOS in vitro 연구: 삭제 형태가 진도성에 유의한 영향(p<0.001), 스캐너 종류 단독 효과는 무의미(p=0.056)이나 디자인×스캐너 상호작용 유의.

## 1. Document Information
- Journal: Journal of Esthetic and Restorative Dentistry (online September 3, 2026)
- DOI: 10.1111/jerd.70263
- Institution: Akdeniz University, Faculty of Dentistry, Department of Restorative Dentistry (Turkey)
- Funding: Not stated
- Conflicts of interest: Not stated

## 2. Key Contributions
- Systematic comparison of 9 single-tooth preparation designs on IOS accuracy using Primescan and TRIOS 5
- Preparation design is the dominant factor for IOS trueness (p < 0.001); scanner type alone is not (p = 0.056)
- Significant scanner × preparation interaction means optimal scanner may vary by preparation type
- Anterior veneer (buccal + palatal) with Primescan yielded highest RMS (0.0623 mm) — worst combination
- Partial occlusal veneer (VE3) with TRIOS 5 yielded lowest RMS (0.0247 mm) — best combination
- Simpler, more optically accessible geometries generally showed lower RMS values

## 3. Methodology and Architecture
- **Design**: In vitro comparative
- **Model**: Maxillary phantom model, 9 preparation designs on single teeth + 1 unprepared control
- **Preparations**: anterior veneer (VE1: buccal only; VE2: buccal + palatal), partial occlusal veneer (VE3), posterior onlay variants, full crown designs (details from abstract)
- **IOS**: TRIOS 5 (3Shape) and Primescan (Dentsply Sirona); 5 scans per combination
- **Reference**: High-accuracy industrial scanner (ATOS Q) — ground truth
- **Trueness metric**: RMS after best-fit alignment
- **Precision**: IQR of repeated RMS values (descriptive)
- **Statistics**: Two-way ANOVA; preparation design and scanner type as factors

## 4. Key Results and Benchmarks
- RMS range overall: **0.0247–0.0623 mm** (24.7–62.3 µm)
- Best trueness: VE3 (partial occlusal veneer) + TRIOS 5 → 0.0247 mm
- Worst trueness: VE2 (anterior veneer buccal + palatal) + Primescan → 0.0623 mm
- **Preparation design**: F(9,80) = 9.26, p < 0.001 (significant)
- **Scanner type**: p = 0.056 (not significant as main effect)
- **Interaction** (design × scanner): F(9,80) = 4.84, p < 0.001 (significant)
- General pattern: simpler, optically accessible surfaces → lower RMS; complex multi-surface/palatal preparations → higher RMS with Primescan specifically

## 5. Limitations and Future Work
- In vitro phantom model; no clinical validation
- Precision assessed descriptively (IQR) only — not statistically tested
- Only two IOS compared; broader scanner panel needed
- Optical vs. confocal acquisition technology difference (Primescan: active triangulation; TRIOS 5: confocal) may explain interaction
- Marginal and internal fit of resulting restorations not tested

## 6. Related Work
- Revilla-León 2025 SR: systematic review of tooth preparation factors affecting IOS accuracy — this study adds specific design-level data
- Wildhagen 2026 (this cohort): IOS accuracy for post preparations — parallel principle

## 7. Glossary
- **RMS (root mean square) deviation**: overall trueness metric; smaller = better
- **IQR (interquartile range)**: spread of RMS values across repeated scans — proxy for precision
- **Active triangulation**: Primescan acquisition technology — projects light pattern and calculates depth from reflection angle
- **Confocal scanning**: TRIOS technology — uses depth of focus to build surface; better for undercuts/palatal surfaces
- **Anterior veneer (VE2, buccal + palatal)**: preparation requiring scan of both buccal and palatal surfaces — most complex IOS challenge for anterior teeth
