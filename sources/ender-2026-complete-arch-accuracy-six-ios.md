---
title: "Complete arch accuracy of six intraoral scanning devices: A clinical study"
authors: "Ender A, Buhl J, Mehl A"
year: 2026
doi: "10.1016/j.prosdent.2025.12.016"
category: [digital-workflow]
pdf_path: N/A
pdf_filename: N/A
source_collection: pubmed-abstract
---

## Why Ingested
유일한 환자 대상(in vivo) 임상연구로 Primescan의 전악 임상 정확도를 직접 측정 — 기존 위키의 모든 Primescan 비교 근거가 in vitro임을 보완하며 [[digital-workflow/singh-2025-intraoral-scanners-accuracy-umbrella-review]] SR에 임상 근거를 추가한다. 또한 차세대 **Primescan 2**가 처음 등장하는 비교 연구다.

## One-line Summary
Clinical study (10 participants, 6 IOS): Primescan achieved the highest complete-arch trueness (41 µm) among all tested scanners; Primescan 2 performed comparably.

## 한줄요약
임상연구(10명, 6 구강내스캐너(IOS)): 프라임스캔(Primescan)이 전악 진도성(trueness) 41 µm로 가장 우수, 프라임스캔 2(Primescan 2)도 동등 수준.

## 1. Document Information
- Journal: The Journal of Prosthetic Dentistry, Vol. 136, Issue 1, pp. 136–143 (July 2026)
- Electronic publication: January 7, 2026
- Institution: University of Zurich, Center for Dental Medicine, Division of Computerized Restorative Dentistry
- Funding: Not stated
- Conflicts of interest: Not stated

## 2. Key Contributions
- First clinical study comparing Primescan and its successor Primescan 2 head-to-head in patients
- Primescan showed the best trueness (41 µm) of all six IOS tested; conventional impression still superior in precision
- No significant difference between Primescan and Primescan 2, or between Primescan and MEDIT i900
- Trueness values for all tested IOS remained below 100 µm, within clinically acceptable range
- Precision of conventional impressions (21 µm) significantly exceeded all IOS (best IOS ~40 µm)

## 3. Methodology and Architecture
- **Design**: Clinical study (in vivo, single-operator, prospective cross-sectional)
- **Participants**: 10 adults, maxillary and mandibular complete arches scanned
- **IOS tested**: Emerald S (EME), MEDIT i900 (MED), Primescan (PRI), Primescan 2 (PS2), Aoralscan 3 (SHI), TRIOS 5 (TRI); 3 complete arch scans per IOS per participant
- **Control**: Conventional high-precision impression (polyether) → stone model → laboratory scan
- **Trueness**: Each IOS scan vs. corresponding conventional impression (90th–10th percentile method)
- **Precision**: Intragroup pairwise comparison
- **Statistics**: Welch ANOVA, Games-Howell post-hoc, linear mixed-effects model (α = 0.05)

## 4. Key Results and Benchmarks
- **Precision** (µm): CONV 21 ±4 < PRI/PS2/MED group ≈ SHI/TRI group < EME 82 ±38 (CONV significantly better than all IOS)
- **Trueness** (µm): PRI **41 ±10** < PS2 ≈ MED < SHI ≈ TRI < EME 96 ±29
- No significant difference: PRI vs PS2, PRI vs MED, PS2 vs MED, SHI vs TRI (p > 0.05)
- EME significantly worse than all others (p < 0.001)
- All trueness values < 100 µm (clinically acceptable threshold)

## 5. Limitations and Future Work
- Small sample (n = 10); single operator; single session
- Conventional impression used as reference rather than a metrology-grade standard — not an absolute ground truth
- Maxillary and mandibular arches pooled in analysis; arch-specific differences not reported
- Long-term clinical implications (marginal fit, prosthetic outcome) not studied

## 6. Related Work
- Buhl 2025 (in vitro, same group): IOS complete arch accuracy in vitro — this study adds in vivo confirmation
- Singh 2025 umbrella review: covers IOS accuracy SRs including earlier scanner generations
- Vitai 2023 SR+NMA: IOS complete arch accuracy meta-analysis

## 7. Glossary
- **Primescan 2**: second-generation CEREC Primescan released ~2025 (Dentsply Sirona), updated optical/software system
- **Trueness**: deviation from a reference standard (systematic error)
- **Precision**: repeatability of repeated measurements (random error)
- **(90–10)/2 percentile method**: trueness metric that excludes outliers, used by Zurich group
