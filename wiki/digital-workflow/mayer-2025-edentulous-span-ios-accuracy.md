---
title: "Influence of edentulous span length on complete-arch intraoral scanner accuracy: a comparative in vitro study"
authors: "Mayer Y et al."
year: 2025
date: 2025-09-18
doi: "10.3290/j.qi.b639465"
source: mayer-2025-edentulous-span-ios-accuracy.md
category: [digital-workflow]
confidence: in-vitro
source_collection: pubmed-abstract
tags: [intraoral-scanner, ios, primescan, trios-3, complete-arch, edentulous-span, accuracy, trueness, span-length, rms, implant, partial-edentulous]
relations:
  - type: refines
    target: ender-2026-complete-arch-accuracy-six-ios
---

## Three-line Summary
In vitro study (12 edentulous span scenarios, Primescan vs TRIOS 3, n=240): TRIOS 3 achieved lower overall RMS (0.296 ± 0.043 mm) than Primescan (0.338 ± 0.049 mm), with significant differences in 9/12 scenarios. Primescan showed stronger span-length dependence (R²=0.892) than TRIOS 3 (R²=0.674), indicating its active-triangulation technique is more sensitive to missing occlusal reference points. Both devices were highly reliable but showed accuracy decline with increasing span.

## 한줄요약
무치악 경간 12단계(프라임스캔 vs TRIOS 3, n=240): TRIOS 3 전체 RMS 더 낮음(0.296 vs 0.338 mm), 9/12 시나리오 유의차; 프라임스캔 경간 길이 의존성 더 강함(R²=0.892 vs 0.674).

## Summary
Mayer et al. created twelve progressive edentulous span scenarios (FA1–FA12) on a maxillary complete-arch model with a central incisor implant by sequentially removing adjacent teeth, then scanned each scenario ten times each with Primescan and TRIOS 3. Against an Identica Blue laboratory scanner reference, TRIOS 3 demonstrated superior overall trueness (RMS 0.296 mm vs 0.338 mm), with statistically significant differences in 9 of 12 span conditions. Linear regression revealed that Primescan accuracy declines more steeply with increasing span length (R²=0.892) than TRIOS 3 (R²=0.674). The finding aligns mechanistically with active-triangulation limitations: as more occlusal surface is missing, the structured-light pattern has fewer reference landmarks, increasing cumulative drift. TRIOS 3's confocal scanning is relatively less affected by this geometry change. Both IOS showed high within-group reliability throughout.

## Key Contributions
- First systematic span-length dose-response study for Primescan vs TRIOS 3 in partially edentulous complete-arch scenarios
- TRIOS 3 outperforms Primescan when edentulous spans are present — a reversal of Primescan's advantage in dentate scenarios (ender-2026)
- Primescan's stronger span-length dependency (R²=0.892) is mechanistically consistent with active-triangulation limitations (fewer occlusal reference points = greater drift)
- Both devices are reliable (precise) throughout — the gap is in trueness, not repeatability
- Clinical implication: in cases with multiple missing teeth forming a long edentulous span, TRIOS-class confocal IOS is preferable to Primescan

## Methodology
In vitro comparative study. Maxillary complete-arch model with central incisor implant. 12 span-length scenarios (FA1–FA12) created by sequential removal of teeth flanking the edentulous region. IOS: CEREC Primescan (Dentsply Sirona) and TRIOS 3 (3Shape). Scans: n=10 per IOS per scenario (N=240 total). Reference: Identica Blue laboratory scanner (Medit). Alignment: automatic and local best-fit in Medit Design. Outcomes: trueness (RMS vs reference), precision (intra-group RMS). Statistics: two-way mixed ANOVA, repeated-measures ANOVA, linear regression; Bonferroni correction (α=0.004).

## Results
**Overall RMS (trueness, mean ± SD across 12 scenarios):**
- TRIOS 3: **0.296 ± 0.043 mm**
- Primescan: **0.338 ± 0.049 mm**
- Significant difference: 9/12 scenarios (p<0.001)

**Span-length sensitivity (linear regression R²):**
- Primescan: **R²=0.892** (strong span-length dependence)
- TRIOS 3: **R²=0.674** (moderate dependence)

**Reliability:** both IOS high reliability throughout all scenarios

**Note on scale:** RMS values are in mm — edentulous arch reconstruction is fundamentally more challenging than dentate scanning; these values are not directly comparable to µm-scale dentate-scenario benchmarks

## Related Papers
- [[digital-workflow/ender-2026-complete-arch-accuracy-six-ios]] — refines (Primescan best in dentate; this study shows the ranking reverses when edentulous spans are introduced)
- [[digital-workflow/vitai-2023-intraoral-scanner-complete-arch-sr-network-ma]] — refines (TRIOS 3 superiority emerges specifically in edentulous-span conditions not captured by SR+NMA of dentate studies)
- [[digital-workflow/borbola-2024-virtual-fit-complete-arch-ios-accuracy]] — reinforces (both confirm Primescan's acceptable dentate performance; together highlight the edentulous-span as the boundary condition)
- [[digital-workflow/primescan-clinical-performance-overview]] — refines (new Clinical Decision Point: edentulous span → prefer TRIOS 3)
