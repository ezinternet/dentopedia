---
title: "Decomposing Organic Molecules on Titanium with Vacuum Ultraviolet Light for Effective and Rapid Photofunctionalization"
authors: "Toshikatsu Suzumura, Takanori Matsuura, Keiji Komatsu, Takahiro Ogawa"
year: 2023
doi: "10.3390/jfb14010011"
category: [implants/surface]
text_path: /Users/oracleneo/llm-wiki/papers/suzumura-2023-vacuum-uv-organic-decomposition-titanium.txt
text_filename: suzumura-2023-vacuum-uv-organic-decomposition-titanium.txt
source_collection: pubmed-text
pmid: "36662058"
pmcid: "PMC9861116"
---

## Why Ingested

Houshmand 2023([[implants/surface/houshmand-2023-uv-photofunctionalization-sla-titanium-disks]])이 UVC가 카르복실기-Ti 결합을 해리시키는 광자 에너지 임계를 넘는다고 보였는데, 이 논문은 더 짧은 파장인 진공자외선 (Vacuum Ultraviolet, VUV, 172 nm)이 UVC(254 nm) 대비 1분 처리로도 훨씬 빠른 유기물 분해를 달성함을 보여 파장-에너지-탄소제거 계단의 최상단을 완성한다. 위키의 [[overviews/uv-photofunctionalization-dental-implants]] 오버뷰의 임상적용 한계(처리시간 문제) 절을 직접 보완.

## One-line Summary

In vitro study (grade 4 cp-Ti + grade 5 Ti-6Al-4V + PMMA; methylene blue as model organic molecule): VUV (172 nm xenon excimer) decomposed 57% of coated methylene blue in 1 minute vs. 2% (UVC), 36% (HUVC), 42% (PUV), with TiO₂ photocatalysis accounting for only ~20–25% of decomposition.

## 한줄요약

In vitro 연구 (상업용 티타늄, 메틸렌블루 모델 유기분자): 진공자외선 (VUV, 172 nm 크세논 엑시머 램프)이 1분 처리로 UVC(2%)·고에너지UVC(36%)·전용UV장비(42%) 대비 57% 유기물 분해 달성; 이산화티타늄 광촉매 기여도는 ~20–25%에 불과.

## 1. Document Information

- Journal: Journal of Functional Biomaterials, 14(1), art. 11 (January 2023)
- Institution: Weintraub Center for Reconstructive Biotechnology, UCLA School of Dentistry
- Funding: not stated; all authors at UCLA Ogawa lab

## 2. Key Contributions

- Establishes VUV (172 nm) as the most effective UV source for organic decomposition on titanium at 1 minute — sets a new benchmark for rapid photofunctionalization.
- Quantifies the photocatalytic contribution of TiO₂: only 20–25% of decomposition — meaning the dominant mechanism is direct photolysis by UV photons, not surface chemistry.
- Demonstrates quartz ampoules do not significantly reduce VUV efficacy — enabling sealed sterile packaging during treatment (solves the "recontamination after unpacking" problem).
- Load-testing (variable methylene blue density): VUV maintains ~40–52% decomposition across all load densities, whereas UVC/HUVC/PUV show near-zero efficacy at thin-coating loads and plateau at thick loads — VUV is robust, others are sensitive to contamination density.
- Provides the photon-energy mechanism for why shorter wavelength = faster decomposition, linking to the hydrocarbon-Ti bond dissociation model.

## 3. Methodology and Architecture

- **Specimens**: grade 4 cp-Ti (14 mm × 6 mm × 2 mm, machine-milled); grade 5 Ti-6Al-4V; PMMA acrylic
- **Model organic**: methylene blue (0.07% stock, 5 µL/specimen, air-dried 12 h)
- **UV sources**: (i) UVC — commercial low-pressure mercury lamp, 254 nm, 1.2 mW/cm²; (ii) HUVC — TheraBeam Affiny (Ushio); (iii) PUV — SuperOsseo (Ushio); (iv) VUV — xenon excimer, 172 nm, ~60 mW/cm² (DIO, Busan, Korea)
- **Containers**: quartz ampoules (10 mm × 25 mm synthetic quartz) vs. plastic tubes (open/closed)
- **Measurement**: residual methylene blue dissolved in 800 µL ddH₂O, absorbance at 650 nm (microplate reader)
- **Statistics**: n=3 specimens/group; one-way ANOVA + Bonferroni post hoc; regression for dose-dependency

## 4. Key Results and Benchmarks

| UV source | Residual MB @ 1 min | Wavelength |
|---|---|---|
| VUV | 43% (decomposed 57%) | 172 nm |
| PUV | 58% (decomposed 42%) | proprietary |
| HUVC | 64% (decomposed 36%) | high-energy UVC |
| UVC | 98% (decomposed 2%) | 254 nm |

- VUV dose-dependency: maximal decomposition at 60 s; negative exponential fit (R² = 0.93); no additional benefit at 80 s
- TiO₂ photocatalysis: PMMA showed 20–25% less decomposition than Ti for all sources → photocatalysis is minor contributor
- Quartz ampoule: no significant reduction in VUV efficacy vs. open/uncontained (closed plastic tubes completely blocked all UV)
- Load-test: VUV robustly 40–52% across all methylene blue densities; UVC near-zero at thin loads, PUV/HUVC plateau at high loads

## 5. Limitations and Future Work

- Methylene blue is a model molecule — does not perfectly represent the mixture of carboxylate/amine hydrocarbon contaminants on aged titanium (Roy model)
- No direct surface carbon quantification (XPS/EDS) — decomposition is inferred from colorimetric residual, not directly measured as C% reduction
- No biological outcomes (cell attachment, osseointegration) — purely physicochemical
- VUV device (DIO, Busan) used is a prototype/research-grade xenon excimer; commercial chairside availability not established at time of publication
- VUV at 172 nm is absorbed by atmospheric oxygen (requires nitrogen purge or quartz containment) — adds handling complexity

## 6. Related Work

- Houshmand 2023 — UVC vs UVB on SLA disks; VUV would fit as a third step on the energy ladder
- Park 2025 (park-2025-uv-photofunctionalization-osseointegration-soft-tissue) — includes VUV section in narrative review; this paper is the foundational VUV data
- Ogawa group: Hirota 2020, Komatsu 2026 — clinical outcomes of UV-PF; this paper solves the treatment-time bottleneck

## 7. Glossary

- VUV (Vacuum Ultraviolet): UV light < 200 nm; absorbed by atmospheric oxygen, requiring quartz or sealed containers
- HUVC: High-energy UVC (commercial dental implant UV device, TheraBeam Affiny, Ushio)
- PUV: Proprietary UV (SuperOsseo, Ushio)
- Methylene blue: model organic chromophore used as surrogate for hydrocarbon contamination
- Xenon excimer lamp: lamp producing monochromatic 172 nm VUV via xenon excimer emission
- Photolysis: direct UV photon-mediated decomposition (wavelength-dependent)
- Photocatalysis: TiO₂-mediated UV decomposition (surface-dependent)
