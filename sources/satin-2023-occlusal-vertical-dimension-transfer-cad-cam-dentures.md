---
title: "Comparing the accuracy of occlusal vertical dimension transfer in CAD-CAM dentures"
authors: "Satin SR, Goodacre BJ, Masri R"
year: 2023
doi: "10.1111/jopr.13669"
pmid: "36815435"
category: complete-denture
full_text: false
source_collection: pubmed-abstract
---

## Why Ingested
기존 [[wiki/complete-denture/fayad-2025-vertical-dimension-determination-prosthodontics-review]]와 [[wiki/complete-denture/alhajj-2017-occlusal-vertical-dimension-complete-denture-review]]는 수직고경(Occlusal Vertical Dimension, OVD)을 "어떻게 최초 결정하는가"를 다뤘다면, 이 in-vitro 연구는 그 다음 단계 — 이미 결정된 OVD를 디지털(CAD-CAM) 의치 제작 워크플로로 어떻게 "정확히 전달(transfer)"하는가를 duplicate denture(DD) vs occlusion rim(OR) 두 방식으로 정량 비교한다. 두 워크플로 모두 오차가 OVD를 증가시키는 방향(양성 편향, 98.9%)으로 체계적으로 발생한다는 점이 임상적으로 중요한 발견.

## Three-line Summary
In-vitro simulation study comparing two OVD-transfer workflows for digital complete dentures — duplicate dentures (DD, n=15) versus occlusion rims (OR, n=15) — using mounted edentulous casts and STL superimposition against a control cast scan.

OR produced significantly larger overall deviation than DD at all three measured locations (0.72 ± 0.13 mm vs 0.45 ± 0.23 mm; F = 46.00, p < 0.0001); 98.9% of deviations were positive, meaning both workflows systematically increased OVD rather than scattering randomly.

The authors conclude DD is more accurate for OVD transfer than OR, but explicitly flag that the magnitude of difference (~0.3 mm) may not be clinically significant — a live, unresolved question rather than a settled one.

## 세줄요약
디지털(CAD-CAM) 완전틀니 제작 시 수직고경(Occlusal Vertical Dimension, OVD) 전달 정확도를 duplicate denture(DD, n=15) 워크플로와 occlusion rim(OR, n=15) 워크플로로 비교한 in-vitro 모형 실험.

OR이 세 측정 위치 모두에서 DD보다 유의하게 큰 편차를 보였다(전체 0.72 ± 0.13 mm vs 0.45 ± 0.23 mm; F = 46.00, p < 0.0001); 편차의 98.9%가 양성(positive) — 즉 두 워크플로 모두 OVD를 증가시키는 방향으로 체계적 편향을 보임.

저자들은 DD가 OR보다 정확하다고 결론짓지만, 그 차이(~0.3 mm)가 임상적으로 유의미한지는 스스로 단정하지 않고 열린 질문으로 남김.

## 1. Document Information
- **Title**: Comparing the accuracy of occlusal vertical dimension transfer in CAD-CAM dentures
- **Authors**: Satin SR, Goodacre BJ, Masri R
- **Journal**: Journal of Prosthodontics 2023;33(3):239-245
- **Year / date**: 2023 (2023-03-14)
- **DOI**: [10.1111/jopr.13669](https://doi.org/10.1111/jopr.13669)
- **PMID**: 36815435
- **Institutions**: Division of Prosthodontics, University of Maryland, Baltimore; Division of General Dentistry, Loma Linda University, California
- **Source**: PubMed abstract only — paywalled, no open-access full text (verified via `scripts/fetch-oa.py`)
- **Study type**: In-vitro simulation study (mounted edentulous casts standing in for a patient; NOT a clinical/patient study)

## 2. Key Contributions
- Directly compares OVD-**transfer** accuracy between two commonly used digital-denture workflows (duplicate denture vs occlusion rim), a step distinct from OVD *determination* covered by other wiki pages.
- Reports overall deviation as a directional bias, not just magnitude: 98.9% of measurements were positive (OVD increased in both workflows), which is a predictable, compensable systematic error rather than random scatter.
- Provides comparative quantitative benchmarks (DD 0.45 ± 0.23 mm vs OR 0.72 ± 0.13 mm) for evaluating digital OVD-transfer fidelity.
- Explicitly hedges clinical significance of the ~0.27 mm difference between workflows, rather than overclaiming.

## 3. Methodology
- **Design**: In-vitro simulation; mounted edentulous casts used to simulate a completely edentulous patient (not patient data).
- **Groups**: (1) DD workflow — complete dentures fabricated and relined (n = 15); (2) OR workflow — final impressions and occlusion rims constructed (n = 15).
- **Digitization**: Relined dentures and occlusion rims (with fiduciary markers) scanned and virtually articulated, exported as STL. A separate scan of the articulated control casts (with embedded fiduciary markers) exported as STL served as the control/reference.
- **Analysis**: STL files for each workflow superimposed over the control in 3D inspection software (Geomagic Control X, 3D Systems, NC); deviations (mm) measured at three locations.
- **Statistics**: Two-way ANOVA (α = 0.05) comparing average 3D deviation among groups.
- **Scope note**: DD requires an existing, well-fitting denture to duplicate — the workflow is therefore unavailable for a first-time edentulous patient with no prior denture.

## 4. Key Results and Benchmarks
| Measure | DD workflow (n=15) | OR workflow (n=15) | Statistic |
|---|---|---|---|
| Overall mean deviation from control | 0.45 ± 0.23 mm | 0.72 ± 0.13 mm | F = 46.00, p < 0.0001 |
| Deviation direction | — | 98.9% of measurements positive (increased OVD) | — |
| Location × method interaction | — | — | F = 0.02, p < 0.98 (no interaction; no difference between measurement points) |

- OR deviation significantly larger than DD at **all three** measurement locations.
- No significant difference in deviation between the different measurement points, and no interaction between location and method — the DD-vs-OR gap is consistent across sites.
- Authors' own conclusion: DD shows less OVD-transfer deviation than OR, "but the deviation was small and may not be clinically significant."

## 5. Limitations and Future Work
- **In-vitro only** — mounted casts, not human patients; n=15 refers to fabricated specimens per workflow, not patients. No clinical/functional outcome data.
- DD workflow structurally requires a pre-existing well-fitting denture to duplicate, limiting applicability to patients being relined/replaced, not first-time edentulous patients.
- Abstract does not report whether the ~0.27 mm DD-vs-OR gap, or the systematic positive bias itself, was tested against a pre-defined clinical-significance threshold.
- No comparison to non-digital/conventional OVD-transfer benchmarks in the retrieved abstract.

## 6. Related Work
- Precedes/complements OVD-**determination** literature ([[wiki/complete-denture/fayad-2025-vertical-dimension-determination-prosthodontics-review]], [[wiki/complete-denture/alhajj-2017-occlusal-vertical-dimension-complete-denture-review]]) — this paper assumes OVD is already decided and measures how faithfully it survives the digital fabrication workflow.
- Relevant to digital complete-denture procedure selection ([[wiki/complete-denture/thu-2024-digital-complete-denture-clinical-laboratory]]).
- Useful cross-dimension comparison point against [[wiki/complete-denture/singh-2026-nick-notch-intraoral-gothic-arch-jaw-relation]], which found extraoral Gothic arch (horizontal-plane) error of 0.74-0.86 mm to be potentially clinically perceptible — a vertical-plane error of similar magnitude (~0.72 mm, OR group here) is not automatically equivalent, since vertical error is partly absorbed by freeway/interocclusal rest space in a way horizontal error is not.

## 7. Glossary
- **OVD (Occlusal Vertical Dimension, 수직고경)**: vertical distance between two facial reference points when teeth/occlusion rims are in contact.
- **Duplicate denture (DD) workflow**: fabricating a new denture by duplicating/relining an existing well-fitting denture, preserving its established OVD.
- **Occlusion rim (OR) workflow**: constructing wax/record-base rims from a fresh final impression to newly establish OVD.
- **Fiduciary marker**: fixed reference point embedded in a cast/appliance used to align scans for superimposition.
- **STL superimposition**: digital overlay of two 3D scans (here, workflow output vs control) to measure positional/dimensional deviation.
