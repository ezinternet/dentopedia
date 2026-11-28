---
title: "Influence of Experimental Lighting Conditions on Digital Shade Matching and Intraoral Scanning Accuracy: A Clinical Study"
authors: "Guo YQ, Lin KJ, Marfi MJ, Ni L, Lin HL, Yu H"
year: 2026
doi: "10.1111/jerd.70222"
category: [digital-workflow]
pdf_path: N/A
pdf_filename: N/A
source_collection: pubmed-abstract
---

## Why Ingested
유일한 조명 조건별 Primescan 임상 성능 연구 — 프라임스캔이 치과 진료실 조명(2500 lx)에서 최적으로 작동함을 실증하여 [[digital-workflow/digital-workflow.md]] 현장 운용 가이드에 직접 임상 팁을 제공한다.

## One-line Summary
Clinical study (10 volunteers, 4 illuminance levels): Primescan performed best at 2500 lx/4100 K (dental operatory light), while TRIOS 4 peaked at 1000 lx/5500 K (examination room light).

## 한줄요약
임상연구(10명, 4개 조도 조건): 프라임스캔은 2500 lx/4100 K(치과 조명)에서 최고 성능, TRIOS 4는 1000 lx/5500 K에서 최적 — 스캐너별 최적 조명 조건이 다름.

## 1. Document Information
- Journal: Journal of Esthetic and Restorative Dentistry (online June 25, 2026)
- DOI: 10.1111/jerd.70222
- Institution: Fujian Medical University, School and Hospital of Stomatology (China); Nagasaki University (Japan)
- Funding: Not stated
- Conflicts of interest: Not stated

## 2. Key Contributions
- First study to systematically vary illuminance AND color temperature matched to each IOS's recommended conditions
- Scanner-specific optimal lighting: Primescan (PR) at 2500 lx/4100 K; TRIOS 4 (TR) at 1000 lx/5500 K
- Ambient light significantly affects both scanning trueness and digital shade accuracy
- Zero-light condition (0 lx) significantly reduced TRIOS 4 reliability but not Primescan's
- Practical clinical guideline: match operatory lighting to the specific scanner in use

## 3. Methodology and Architecture
- **Design**: In vivo clinical study (randomized crossover)
- **Participants**: 10 volunteers, maxillary arches scanned
- **IOS**: Primescan (PR, Dentsply Sirona, 4100 K light); TRIOS 4 wireless (TR, 3Shape, 5500 K light)
- **Illuminance levels tested**: 0 lx (dark), 500 lx, 1000 lx, 2500 lx — matched to each scanner's color temperature
- **Shade matching**: digital shade selection at middle third of right central incisor vs. visual consensus; Vita Classical (VC) and 3D-Master (VM) guides
- **Trueness**: IOS scans superimposed on stone model digitized with InEos X5 reference scanner
- **Statistics**: One-way ANOVA (α = 0.05)

## 4. Key Results and Benchmarks
- **Scanning trueness** (µm, mean): PR optimal at 2500 lx: **100.78 ±19.36**; TR optimal at 1000 lx: 104.04 ±20.88
- Ambient lighting significantly affected trueness (p < 0.05) for both scanners
- **Shade accuracy** (VC): TR best at 1000 lx 93.3 ±14.1%; PR best at 2500 lx 96.7 ±10.5%
- TR reliability significantly lower at 0 lx (p < 0.05); PR showed no significant difference among groups
- Primescan more robust to darkness than TRIOS 4 for shade determination

## 5. Limitations and Future Work
- Small sample (n = 10); single arch per participant
- Manufacturer-specified color temperatures used — cross-testing at non-matched temperatures not evaluated
- Trueness reference was digitized stone model, not metrology standard
- Long-term clinical outcomes (prosthetic fit, shade acceptance by patients) not assessed
- In-mouth variation (saliva, blood, anatomical complexity) not controlled beyond routine clinical conditions

## 6. Related Work
- Ramos-Morro 2026: chairside time and patient comfort — complements by adding an environmental factor
- Revilla-León 2025 SR: tooth preparation factors affecting IOS accuracy — lighting as a parallel environmental factor

## 7. Glossary
- **Illuminance (lux, lx)**: measure of luminous flux per unit area; standard dental operatory ~2000–3000 lx
- **Color temperature (K)**: warm light < 3300 K, cool/daylight > 5000 K; matched to scanner's own light source
- **Digital shade matching**: automated tooth color determination using IOS color capture module
