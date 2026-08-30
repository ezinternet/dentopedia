---
title: "Effects of dental implant diameter and tapered body design on stress distribution in rigid polyurethane foam during insertion"
authors: "Baixuan Yang, Ainara Irastorza Landa, Peter Heuberger, Heidi-Lynn Ploeg"
year: 2024
doi: "10.1016/j.medengphy.2024.104181"
category: [implants]
pdf_path: /Users/oracleneo/llm-wiki/papers/yang-2024-implant-diameter-tapered-stress-insertion.pdf
pdf_filename: yang-2024-implant-diameter-tapered-stress-insertion.pdf
source_collection: external
---

## Why Ingested
FEA + in-vitro 연구로 임플란트 직경과 테이퍼 설계가 삽입 중 삽입 토크 (Insertion Torque, IT)와 골 응력 분포에 미치는 영향을 정량화함 — [[implants/isq/baldi-2018-insertion-torque-isq-tapered-knife-edge]] 및 [[overviews/high-insertion-torque-primary-stability-crestal-bone-overview]]에서 다루는 "테이퍼가 IT를 높이는 기전"의 기계적 설명을 제공.

## One-line Summary
In vitro FEA + experiment study: tapered body design dominates normalized IT (β₂=0.93) while implant diameter dominates raw IT (β₁=0.78), and tapered design distributes compressive stress further from the thread compared to parallel-walled implants.

## 한줄요약
PU 폼 삽입 실험 + FEA: 테이퍼 바디 설계가 정규화 삽입 토크를 주로 결정(β₂=0.93)하며, 병렬 벽 대비 나사산에서 더 멀리 압축 응력을 분산시킴.

## 1. Document Information
- Journal: Medical Engineering and Physics, vol. 129, article 104181, 2024
- Available online 18 May 2024
- Affiliation: Queen's University Kingston (Canada), Nobel Biocare Services AG (Zürich)
- Funding: Nobel Biocare (P. Heuberger, A. Irastorza Landa are Nobel Biocare employees)

## 2. Key Contributions
- Quantifies separate contributions of implant diameter vs. taper body design to IT during insertion using analytical model + explicit FEA
- Shows that normalized IT (IT / radial interference δ) is dominated by taper design (β₂=0.93, p<0.001), not diameter (β₁=0.20, p=0.020)
- Demonstrates that tapered body creates a compression zone in PU foam distal to the threads — distinct stress distribution from parallel-walled
- Validates FEA insertion model against 2D-DIC surface strain measurements
- Provides pre-clinical mechanical data to guide implant design development

## 3. Methodology and Architecture
- Study design: In vitro + FEA, parallel-walled (P1 Ø3.5mm, P2 Ø4.3mm) vs tapered (T1 Ø3.5mm, T2 Ø4.3mm) Nobel Biocare implants
- Substrate: Single-density rigid polyurethane (PU) foam without cortical layer (ASTM F1839-08)
- Insertion: MACH-1 tester, 12 rpm, 5 repeats per implant, straight drill protocol
- Measurement: IT + insertion depth at 100 Hz; 2D-DIC for surface strain
- FEA: 3D explicit Abaqus 2017; modeled threaded implant into PU foam
- Analytical model: IT fitted to radial interference δ (R²=0.88–1.0)
- Regression: standardized coefficients β for diameter vs. taper on IT, normalized IT, effective force, effective pressure

## 4. Key Results and Benchmarks
- Raw IT: diameter (β₁=0.78, p<0.001) + taper (β₂=0.41, p=0.0024), R²=0.77
- Normalized IT: diameter (β₁=0.20, p=0.020) + taper (β₂=0.93, p<0.001), R²=0.90 — taper dominates when press-fit is normalized
- Effective pressure p′: taper β₂=0.97 (p<0.001) — taper body creates higher unit pressure on PU foam
- Tapered implants: compression stress zone extends further from thread; parallel-walled: stress concentrated near thread
- FEA contact ratio consistent with IT trends; DIC validated FEA surface strain patterns

## 5. Limitations and Future Work
- PU foam without cortical layer — does not represent D1-D4 bone heterogeneity
- Room temperature + dry conditions — no irrigation, no bone biology
- 4 implant designs only; one drill protocol each — limited generalizability
- Explicit FEA is computationally intensive; model not validated in vivo
- No biological outcome (ISQ, osseointegration) measured

## 6. Related Work
- Atieh et al. meta-analysis: tapered implants had higher IT and ISQ at placement vs parallel-walled (cited as motivation)
- Coyac et al. 2019 (rat maxilla, misfit): tapered compression can cause osteocyte death — biological consequence of this mechanical model
- Baldi et al. 2018: IT vs ISQ correlation in tapered knife-edge implants (clinical counterpart)

## 7. Glossary
- **Radial interference (δ)**: difference between implant major radius and pilot hole radius at entrance
- **Tip clearance (Δ)**: difference between implant tip radius and pilot hole radius
- **Normalized IT**: IT/δ — removes press-fit magnitude effect to isolate design contribution
- **2D-DIC**: two-dimensional digital image correlation — full-field surface strain measurement
- **PU foam**: rigid polyurethane foam ASTM F1839-08 — standardized bone surrogate
- **Explicit FEA**: time-domain FEA for dynamic/contact problems (Abaqus explicit)
