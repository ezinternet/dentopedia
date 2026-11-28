---
title: "Directional Prosthesis–Implant Geometry as a Correlate of Eccentric Load Sensitivity Across Axial Inclination–Driven Access-Hole Positions: A Finite Element Analysis"
authors: Young K. Kim, Jermaine Eow, Dung Dinh Luong
year: 2026
date: 2026-01-01
doi: 10.32542/implantology.2026012
source: kim-2026-directional-prosthesis-implant-geometry-eccentric-load-fea.md
category: [implants]
evidence_level: in-vitro
pdf_path: /Users/oracleneo/llm-wiki/papers/kim-2026-directional-prosthesis-implant-geometry-eccentric-load-fea.pdf
pdf_filename: kim-2026-directional-prosthesis-implant-geometry-eccentric-load-fea.pdf
source_collection: external
tags: [finite-element-analysis, FEA, implant-biomechanics, eccentric-loading, oblique-loading, access-hole, axial-inclination, PIAAR, directional-geometry, von-mises, guided-planning]
relations:
  - type: extends
    target: leblebicioglu-kurtulus-2022-fea-implant-design-bone-density-stress
---

## Three-line Summary

3D finite element analysis (17 deterministic geometry layouts of an 8-mm × 3.3-mm posterior molar implant, 34 load solutions → 17 configuration-level observations) comparing centric axial with 30° oblique eccentric loading.

Despite a lower aggregate load, localized oblique loading raised bone–implant interface stress (center 487 MPa eccentric vs 108 MPa centric); weakest-direction PIAAR (Prosthesis–Implant Arch Area Ratio) correlated positively with eccentric amplification (Spearman ρ=0.63, p=0.007; R²=0.49) while directional spread correlated inversely (ρ=−0.61, p=0.009).

Access-hole centricity alone incompletely characterizes the modeled behavior and PIAAR is offered as a geometric index, but its clinical threshold validity is unestablished and sector-specific stress vulnerability was not quantified.

## 세줄요약

3D 유한요소분석(Finite Element Analysis, FEA) — 8 mm × 3.3 mm 후방 대구치 임플란트의 결정론적 기하 배치 17종(중심 1 + 경사 16), 하중해 34회 → 구성 단위 관찰 17건; 중심 하중과 30° 경사 편심 하중(eccentric loading) 비교.

총 하중은 더 작았는데도 국소 경사 하중에서 골-임플란트 계면 응력이 더 높았음(중심 487 MPa vs 108 MPa); 최취약방향 임플란트-보철체 면적비(Prosthesis–Implant Arch Area Ratio, PIAAR)는 편심 증폭과 양의 관련(스피어만 ρ=0.63, p=0.007; R²=0.49), 방향성 분산은 음의 관련(ρ=−0.61, p=0.009).

접근공 중심성(access-hole centricity)만으로는 모델링된 역학을 온전히 설명하지 못하며 PIAAR를 기하 지표로 제안하나, 임상 역치 타당도는 미확립이고 방향별 국소 응력 취약성은 정량화하지 않음.

## Summary

This finite element study asks whether the directionally resolved geometry between a prosthetic crown and its implant — rather than the centricity of the screw access hole alone — explains how sensitive a posterior implant restoration is to eccentric (non-axial) loading. Seventeen deterministic 3D configurations of an 8-mm × 3.3-mm implant were built with the platform center fixed and the axis rotated ~2°, 5°, 7° or 9° mesially, distally, buccally or lingually around a centered reference, and each was solved under centric and 30° oblique loading. Peak von Mises stress at the bone–implant interface was higher under the lower-magnitude localized oblique condition (center: 487 vs 108 MPa), confirming that load direction and contact location — not aggregate force — governed the modeled response. Across configurations, higher weakest-direction PIAAR was associated with greater eccentric amplification (ρ=0.63, p=0.007) and directional spread with less (ρ=−0.61, p=0.009); the authors present PIAAR as a proof-of-concept geometric descriptor for guided planning, while stressing that clinical threshold validity, sector-level stress vulnerability and physiologic loading were outside scope.

## Key Contributions

- Separates access-hole position from directional prosthesis–implant geometry: inclination-driven access-hole displacement is treated as a geometric consequence, not the causal biomechanical variable.
- Adapts PIAAR from full-arch to a single posterior unit by partitioning the occlusal projection into buccal/lingual/mesial/distal sectors; defines weakest-direction PIAAR and directional spread.
- Shows that non-axial load direction dominates nominal load magnitude for peak interface stress, and that increasing inclination does not produce a uniform biomechanical penalty across directions (distal dominates under centric load, mesial under eccentric load).
- Provides exploratory correlation/regression evidence that directional geometry captures eccentric-load sensitivity not accounted for by access-hole centricity.

## Methodology

- **Design**: Deterministic 3D finite element computational simulation; no human participants, no replicates; 17 geometry layouts × 2 loading conditions = 34 solutions, collapsed to 17 configuration-level observations.
- **Model**: Posterior molar restoration, 8 mm × 3.3 mm implant, standardized occlusal morphology/bone geometry/material properties/mesh; fixed implant platform center; monolithic one-piece abutment–implant complex to eliminate interface variability.
- **Configurations**: C0 reference plus M2/M5/M7/M9, D2/D5/D7/D9, B2/B5/B7/B9, L2/L5/L7/L9 (≈2°, 5°, 7°, 9°).
- **Loading**: F0 = 900 N reference; centric = 4 contact units; eccentric = 2 contact units at θ=30° with α=1.25 intensity factor (per-unit load F0/cos θ), applied obliquely on the inner incline of the buccal cusps.
- **Outcomes**: Maximum von Mises stress (MPa) at the bone–implant interface; relative eccentric amplification S_e/S_c and absolute difference ΔS = S_e − S_c.
- **Analysis**: Pearson/Spearman correlations and exploratory linear regression against weakest-direction PIAAR and directional spread (two-sided p-values).

## Results

| Outcome | Result |
|---|---|
| Center, centric / eccentric peak interface stress | 108 / 487 MPa — higher stress despite lower aggregate eccentric load |
| Distal inclination, centric stress change vs 0° | 5 MPa (2°) → 101 MPa (9°), progressive |
| Mesial inclination, eccentric stress change vs 0° | 184 MPa at 9° — dominant mesiodistal eccentric increase |
| Lingual eccentric change vs 0° | +40 (2°), +127 (5°), +27 (7°), −90 MPa (9°) — non-monotonic |
| Weakest-direction PIAAR ↔ eccentric amplification | ρ=0.63 (p=0.007); r=0.70 (p=0.002); slope 17.57; R²=0.49 |
| Directional spread ↔ eccentric amplification | ρ=−0.61 (p=0.009); r=−0.64 (p=0.005); slope −16.41; R²=0.42 |
| Weakest-direction PIAAR ↔ absolute ΔS | ρ=0.58 (p=0.015); r=0.48 (p=0.051); slope 861.2; R²=0.23 |
| Directional spread ↔ absolute ΔS | ρ=−0.60 (p=0.011); r=−0.46 (p=0.061); slope −841.7; R²=0.21 |

The inverse directional-spread association concerns global interface-level maximum stress only; sector-specific stress vulnerability was not independently quantified and cannot be assumed absent.

## Related Papers

- [[implants/leblebicioglu-kurtulus-2022-fea-implant-design-bone-density-stress]] — extends the 30° oblique-load FEA paradigm from abutment angulation and bone density to directional prosthesis–implant geometry.
- [[overviews/implant-design-bone-quality-stress-fea]] — FEA stress synthesis this proof-of-concept adds to; shares the caveat that FEA ranks/localizes stress but does not predict clinical survival.
- [[implants/chang-2024-optimization-implant-design-bone-quality-fea]] — FEA showing geometry effects on crestal stress are bone-quality dependent; a different geometric axis.
- [[implants/ceddia-2025-crestal-position-splinted-implant-fea]] — FEA of implant vertical alignment under oblique load; complementary spatial-geometry axis.
