---
title: "Complete-arch accuracy of seven intraoral scanners measured by the virtual-fit method"
authors: "Borbola D et al."
year: 2024
doi: "10.1016/j.jdent.2024.105281"
category: [digital-workflow]
source_collection: pubmed-abstract
---

## Why Ingested
7개 IOS 가상적합(virtual-fit) 방법으로 완전궁 정확도 직접 비교 — 프라임스캔 변연 간격 42 µm 2위 확인.
→ [[digital-workflow/primescan-clinical-performance-overview]]
→ [[digital-workflow/ender-2026-complete-arch-accuracy-six-ios]]

## One-line Summary
In vitro study (4 maxillary arches, 7 IOS, virtual-fit method): EmeraldS, Mediti700, Primescan, and Trios5 all meet marginal/internal fit criteria; Primescan marginal gap 42 µm (second-best), MAE precision second subset.

## 한줄요약
타이포돈트 완전궁 7개 IOS 가상적합: 프라임스캔 변연 간격 42 µm(2위); 정밀도(MAE)는 EmeraldS·Mediti700·Trios5 다음 2그룹.

## 1. Document Information
- Journal: Journal of Dentistry, vol. 149, article 105281, October 2024 (epub 2024-07-31)
- Authors: Borbola D, Mikolicz A, Romanszky L, Sersli G, DeFee M, Renne W, Vag J
- Affiliation: Semmelweis University (Budapest); Artifex Dentis Kft.; Modern Optimized Dentistry Institute (Charleston, SC)
- Funding/COI: Research support, non-U.S. gov't (stated in article types)

## 2. Key Contributions
- First study applying the virtual-fit method to compare 7 contemporary IOS (including newer devices: Helios600, Lumina, Mediti700)
- Primescan ranks 2nd for marginal gap trueness (42 µm, same subset as Mediti700 at 43 µm) and 2nd group for precision (MAE)
- EmeraldS achieves top-tier performance in both marginal gap subset and MAE subset despite being a newer/less-studied scanner
- Trios5 performs notably better in precision (MAE) than trueness ranking — highlighting metric-dependence of IOS rankings
- Increasing cement space (group 70+20) significantly improves marginal fit for Lumina and Aoralscan3 — design compensation strategy for lower-accuracy scanners

## 3. Methodology and Architecture
- 4 maxillary arch models with tooth abutments scanned by industrial reference scanner (n=1 reference per model)
- 7 IOS: Aoralscan3, EmeraldS, Helios600, Lumina, Mediti700, Primescan, Trios5; each IOS n=12 scans per model
- Two complete-arch fixed frameworks designed on each IOS scan: Group 70 (70 µm cement space) and Group 70+20 (70+20 µm, additional 20 µm at margin)
- Virtual-fit method: framework designs superimposed onto reference scan using non-penetrating algorithm simulating clinical try-in
- Outcomes: marginal gap, internal gap (µm); precision = MAE
- Statistical: ANOVA-based homogenous subsets; pairwise comparisons

## 4. Key Results and Benchmarks

**Marginal gap — Group 70 (homogenous subsets):**
- Subset 1 (best): Mediti700 (43 µm), **Primescan (42 µm)**, EmeraldS
- Subset 2: Lumina (67 µm), Aoralscan3 (70 µm), Trios5 (70 µm)
- Subset 3: Helios600 (118 µm)

**MAE at margin — Group 70 (precision, homogenous subsets):**
- Subset 1 (best): Mediti700, Trios5, EmeraldS
- Subset 2: **Primescan**
- Subset 3: Lumina, Helios600
- Subset 4: Aoralscan3

**Group 70+20 effect:**
- Lumina and Aoralscan3: marginal gap significantly decreased
- EmeraldS and Aoralscan3: MAE significantly decreased
- Primescan, Trios5, Mediti700: minimal change — these already perform optimally at 70 µm

**Internal gap:** Similar ranking pattern to marginal gap across all IOS

## 5. Limitations and Future Work
- In vitro only (typodont arches) — clinical conditions (saliva, patient movement) not modeled
- Single cement-space increments tested — optimal spacing per IOS not explored
- Virtual-fit method has not been fully validated against direct clinical fit measurements
- 4 arch models may not capture all clinical geometry variability

## 6. Related Work
- Ender 2026 (in vivo, 6 IOS): Primescan ranked 1st — different IOS cohort, different method (direct scan vs virtual fit)
- Vitai 2023 SR+NMA: Primescan and TRIOS 3 top cluster — consistent with this study's findings
- Buhl 2025 in vitro: similar complete-arch accuracy range (50–100 µm)

## 7. Glossary
- **Virtual-fit method**: CAD framework is designed on the IOS scan, then digitally superimposed onto the reference scan to measure gaps without physical manufacturing
- **MAE (Mean Absolute Error)**: precision metric — lower = more repeatable scans
- **Group 70 / Group 70+20**: cement space of 70 µm (standard) vs 70+20 µm (20 µm additional at the margin)
