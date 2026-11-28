---
title: "Influence of edentulous span length on complete-arch intraoral scanner accuracy: a comparative in vitro study"
authors: "Mayer Y et al."
year: 2025
doi: "10.3290/j.qi.b639465"
category: [digital-workflow]
source_collection: pubmed-abstract
---

## Why Ingested
무치악 경간 길이와 IOS 정확도 관계 — 프라임스캔이 TRIOS 3보다 경간 길이에 더 민감함을 처음 정량화.
→ [[digital-workflow/primescan-clinical-performance-overview]]
→ [[digital-workflow/ender-2026-complete-arch-accuracy-six-ios]]

## One-line Summary
In vitro (12 edentulous span scenarios, Primescan vs TRIOS 3, n=240): TRIOS 3 overall RMS 0.296 mm vs Primescan 0.338 mm; Primescan span-length sensitivity R²=0.892 vs TRIOS 3 R²=0.674.

## 한줄요약
무치악 경간 12단계(프라임스캔 vs TRIOS 3, n=240): TRIOS 3 전체 RMS 더 낮음(0.296 vs 0.338 mm); 프라임스캔이 경간 길이에 더 민감(R²=0.892 vs 0.674).

## 1. Document Information
- Journal: Quintessence International, vol. 56, issue 8, pp. 618–625, September 18, 2025
- Authors: Mayer Y, Berg Y, Kfir O, Triestino A, Gutmacher Z, Canullo L
- DOI: 10.3290/j.qi.b639465

## 2. Key Contributions
- First study to systematically vary edentulous span length (12 scenarios) and measure its independent effect on IOS accuracy for Primescan and TRIOS 3
- Primescan is significantly worse in 9/12 span scenarios — challenges Primescan's superiority narrative in dentate scenarios
- Primescan span-length dependence (R²=0.892) is markedly stronger than TRIOS 3 (R²=0.674) — active triangulation more vulnerable to missing occlusal reference
- Both devices maintain high reliability (repeatable scans) despite accuracy differences
- Practical implication: for cases with large edentulous spans, TRIOS-class confocal technology may be preferred

## 3. Methodology and Architecture
- In vitro maxillary complete-arch model with central incisor implant
- 12 span-length scenarios (FA1–FA12): created by sequentially removing adjacent teeth from either side of the edentulous region
- Each scenario scanned 10× per IOS: Primescan (Dentsply Sirona) and TRIOS 3 (3Shape) → n=240 scans total
- Reference scanner: Identica Blue (Medit) laboratory scanner
- Alignment: automatic and local best-fit in Medit Design
- Outcomes: trueness (RMS vs reference), precision (intra-group RMS)
- Statistics: two-way mixed ANOVA, repeated-measures ANOVA, linear regression with Bonferroni correction (α=0.004)

## 4. Key Results and Benchmarks

**Overall RMS (trueness):**
- TRIOS 3: **0.296 ± 0.043 mm**
- Primescan: **0.338 ± 0.049 mm**
- Significant difference in 9/12 scenarios (p<0.001)

**Span-length correlation (linear regression, R²):**
- Primescan: **R²=0.892** — strong linear increase with span length
- TRIOS 3: **R²=0.674** — moderate correlation, more plateau at longer spans

**Reliability:** Both devices showed high within-group reliability (precise scans)

**Clinical threshold note:** RMS values in mm (not µm as in dentate studies) — the larger magnitude reflects the challenge of unsupported arch reconstruction; direct comparison to dentate-scenario benchmarks requires caution

## 5. Limitations and Future Work
- In vitro only (no soft tissue, no saliva, no patient movement)
- Only 2 IOS compared — broader multi-scanner comparison would be informative
- Single arch model and implant position — generalizability to other arch geometries unclear
- No prosthetic fit validation — RMS accuracy not linked to marginal/internal gap outcomes
- Short follow-up: scan sessions only, no restorative outcomes

## 6. Related Work
- Ender 2026 (in vivo, full-arch, 6 IOS, dentate): Primescan best; this study shows the advantage reverses in edentulous spans
- Vitai 2023 SR+NMA (full-arch accuracy): Primescan/TRIOS 3 comparable in dentate; this study reveals divergence with missing teeth
- Singh 2025 umbrella review: acknowledges span length as accuracy factor

## 7. Glossary
- **FA1–FA12**: the 12 edentulous span scenarios (FA = Full-Arch span condition, increasing span from FA1 to FA12)
- **RMS (Root Mean Square)**: 3D deviation measure — smaller = more accurate
- **Span-length sensitivity (R²)**: how much of the accuracy variance is explained by the number of missing teeth/span extent
