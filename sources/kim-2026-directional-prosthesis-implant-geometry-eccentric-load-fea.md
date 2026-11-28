---
title: "Directional Prosthesis–Implant Geometry as a Correlate of Eccentric Load Sensitivity Across Axial Inclination–Driven Access-Hole Positions: A Finite Element Analysis"
authors: Young K. Kim, Jermaine Eow, Dung Dinh Luong
year: 2026
doi: 10.32542/implantology.2026012
category: [implants]
pdf_path: /Users/oracleneo/llm-wiki/papers/kim-2026-directional-prosthesis-implant-geometry-eccentric-load-fea.pdf
pdf_filename: kim-2026-directional-prosthesis-implant-geometry-eccentric-load-fea.pdf
source_collection: external
---

## Why Ingested

The wiki's FEA-stress cluster — e.g. [[wiki/implants/leblebicioglu-kurtulus-2022-fea-implant-design-bone-density-stress]] (abutment angulation × bone density under 30° oblique load) and the synthesis in [[wiki/overviews/implant-design-bone-quality-stress-fea]] — treats implant geometry mainly through design, dimension, bone density and static load magnitude, and relies on access-hole centricity as a planning surrogate for biomechanical favorability. This study adds a different axis: it uses access-hole *position* only as a geometric read-out of implant axial inclination, and asks whether directional prosthesis–implant geometry (PIAAR) tracks eccentric-load sensitivity beyond centricity — a proof-of-concept extension to the same oblique-loading paradigm with an explicitly unvalidated clinical threshold.

## Three-line Summary

3D finite element analysis (17 deterministic geometry layouts of an 8-mm × 3.3-mm posterior molar implant, 34 load solutions → 17 configuration-level observations) comparing centric axial with 30° oblique eccentric loading.

Despite a lower aggregate load, localized oblique loading raised bone–implant interface stress (center 487 MPa eccentric vs 108 MPa centric); weakest-direction PIAAR (Prosthesis–Implant Arch Area Ratio) correlated positively with eccentric amplification (Spearman ρ=0.63, p=0.007; R²=0.49) while directional spread correlated inversely (ρ=−0.61, p=0.009).

Access-hole centricity alone incompletely characterizes the modeled behavior and PIAAR is offered as a geometric index, but its clinical threshold validity is unestablished and sector-specific stress vulnerability was not quantified.

## 세줄요약

3D 유한요소분석(Finite Element Analysis, FEA) — 8 mm × 3.3 mm 후방 대구치 임플란트의 결정론적 기하 배치 17종(중심 1 + 경사 16), 하중해 34회 → 구성 단위 관찰 17건; 중심 하중과 30° 경사 편심 하중(eccentric loading) 비교.

총 하중은 더 작았는데도 국소 경사 하중에서 골-임플란트 계면 응력이 더 높았음(중심 487 MPa vs 108 MPa); 최취약방향 임플란트-보철체 면적비(Prosthesis–Implant Arch Area Ratio, PIAAR)는 편심 증폭과 양의 관련(스피어만 ρ=0.63, p=0.007; R²=0.49), 방향성 분산은 음의 관련(ρ=−0.61, p=0.009).

접근공 중심성(access-hole centricity)만으로는 모델링된 역학을 온전히 설명하지 못하며 PIAAR를 기하 지표로 제안하나, 임상 역치 타당도는 미확립이고 방향별 국소 응력 취약성은 정량화하지 않음.

## 1. Document Information

- **Journal**: Journal of Implantology and Applied Sciences 2026;30(3):139-156 (Original Article; OPEN ACCESS)
- **DOI**: 10.32542/implantology.2026012
- **Institution**: Department of Prosthodontics, New York University College of Dentistry, NY, USA; Department of Mechanical and Aerospace Engineering, New York University Tandon School of Engineering, NY, USA
- **Study type**: Finite element computational simulation (no human participants; de-identified CBCT/prosthetic datasets used only to build the model; ethical approval exempt)

## 2. Key Contributions

- Reframes guided-planning "access-hole centricity" as an incomplete surrogate: axial inclination shifts the prosthesis–implant directional relationship, and that shift — not the access-hole position per se — tracks eccentric-load sensitivity.
- Adapts PIAAR (previously a full-arch area-based index) into four directional sectors (buccal/lingual/mesial/distal) for a single posterior unit: sectional PIAAR = projected prosthetic area per sector normalized to a constant implant arch area; minimum = weakest-direction PIAAR, max−min = directional spread.
- Demonstrates load *directionality* dominates nominal load magnitude: lower-magnitude localized oblique loading produced higher peak interface von Mises stress than centric loading, with direction-dependent (not monotonic) response to increasing inclination.
- Reports exploratory association statistics (Spearman/Pearson correlations, regression slopes, R²) linking weakest-direction PIAAR and directional spread to eccentric amplification and absolute stress difference.

## 3. Methodology and Architecture

- **Design**: Deterministic 3D finite element computational simulation; no human participants, no biological or technical replicates (random allocation / sample-size calculation not applicable).
- **Model**: Posterior molar implant restoration, 8-mm-long × 3.3-mm-diameter implant; occlusal morphology, prosthetic/implant dimensions, CBCT-derived bone geometry, material properties, interfaces and mesh standardized across all models. Implant platform center fixed at the prosthetic crown geometric center; abutment–implant complex modeled as a monolithic one-piece structure to remove interface variability.
- **Configurations**: 17 layouts — centered reference C0 plus 16 allocated to mesial/distal/buccal/lingual groups at ~2°, 5°, 7°, 9° (M2/M5/M7/M9, D2/D5/D7/D9, B2/B5/B7/B9, L2/L5/L7/L9). Each analyzed under centric and eccentric loading → 34 FE solutions; amplification and absolute difference computed once per geometry → 17 configuration-level observations.
- **Loading**: Reference axial scale F0 = 900 N; centric = 4 contact units (n_c), eccentric = 2 contact units (n_e) at θ=30° with contact-intensity scaling α=1.25; effective oblique per-unit load F0/cos θ; aggregate terms F_c = n_c·F0 and F_e = n_e·α·(F0/cos θ). Eccentric force applied obliquely on the inner incline of the buccal cusps.
- **Outcomes**: Maximum von Mises stress (MPa) at the bone–implant interface under each condition; relative eccentric amplification = S_e/S_c; absolute eccentric stress difference ΔS = S_e − S_c (Eqs. 9–10).
- **Analysis**: Exploratory linear regression (Y = β0 + β1·PIAAR_min + ε and Y = β0 + β1·spread + ε; Eqs. 11–12) plus Pearson and Spearman correlation coefficients with two-sided p-values.

## 4. Key Results and Benchmarks

Maximum von Mises stress at the bone–implant interface (MPa), selected configurations (Table 2):

| Configuration | Centric | Eccentric |
|---|---|---|
| Center (C0) | 108 | 487 |
| Mesial 2° / 7° / 9° | 130 / 94 / 107 | 481 / 568 / 671 |
| Distal 2° / 5° / 9° | 113 / 149 / 209 | 524 / 478 / 497 |
| Buccal 2° / 9° | 116 / 111 | 480 / 434 |
| Lingual 2° / 5° / 9° | 104 / 110 / 114 | 527 / 614 / 397 |

- Peak interface response did not track aggregate load: the eccentric condition used fewer contact units (lower total load) yet produced higher stress than centric loading.
- Relative to the 0° reference, centric stress stayed compact while distal inclination rose progressively from 5 MPa at 2° to 101 MPa at 9°; under eccentric loading the dominant mesiodistal increase shifted to the mesial direction (184 MPa at 9°).
- Buccolingual eccentric response was heterogeneous: lingual +40 MPa (2°), +127 MPa (5°), +27 MPa (7°), −90 MPa (9°); buccal inclination predominantly negative relative to the eccentric reference.
- Weakest-direction PIAAR vs relative eccentric amplification: Spearman ρ=0.63, p=0.007; Pearson r=0.70, p=0.002; slope 17.57, R²=0.49.
- Directional spread vs relative eccentric amplification: Spearman ρ=−0.61, p=0.009; Pearson r=−0.64, p=0.005; slope −16.41, R²=0.42.
- Weakest-direction PIAAR vs absolute eccentric stress difference: Spearman ρ=0.58, p=0.015; Pearson r=0.48, p=0.051; slope 861.2, R²=0.23.
- Directional spread vs absolute eccentric stress difference: Spearman ρ=−0.60, p=0.011; Pearson r=−0.46, p=0.061; slope −841.7, R²=0.21.

All values read directly from the PDF (Tables/Results, pp. 148–151). The global inverse spread–stress association does **not** establish that sector-specific stress vulnerability was reduced or absent.

## 5. Limitations and Future Work

- Fully in silico: isotropic, linearly elastic material properties do not capture anisotropic/viscoelastic biological tissue behavior; static standardized loading with no cyclic or fatigue simulation — not a physiologic force reproduction.
- Load scale (900 N) and contact-intensity factor (α=1.25) are comparative constructs, not estimates of physiologic force partitioning among individual occlusal contacts.
- PIAAR is a proof-of-concept geometric descriptor; threshold-level clinical validity unestablished, requiring evaluation against patient-level biomechanical and peri-implant outcomes.
- Maximum von Mises stress measured globally at the bone–implant interface; sector-specific stress distribution not independently quantified, so localized directional vulnerability cannot be excluded.
- Implant/abutment design and additional restorative configurations, occlusal variables and clinical conditions not modeled; other eccentric contact directions (working/nonworking/protrusive) not simulated.

## 6. Related Work

- [[wiki/implants/leblebicioglu-kurtulus-2022-fea-implant-design-bone-density-stress]] — also a 3D FEA under 30° oblique loading examining angulation effects on peri-implant stress; this paper extends the angulation axis from abutment angle/density to directional prosthesis–implant geometry.
- [[wiki/overviews/implant-design-bone-quality-stress-fea]] — synthesis of the FEA stress cluster this paper extends; shares the in-silico-only caveat that FEA ranks/localizes stress but does not predict survival.
- [[wiki/implants/chang-2024-optimization-implant-design-bone-quality-fea]] — FEA showing geometry effects on crestal stress are bone-quality dependent; different geometric axis.
- [[wiki/implants/ceddia-2025-crestal-position-splinted-implant-fea]] — FEA of implant position/alignment under oblique load; complementary spatial-geometry axis.

## 7. Glossary

- **PIAAR (Prosthesis–Implant Arch Area Ratio)**: area-based geometric index of prosthetic support relative to implant platform; here computed per directional sector from occlusal projections (weakest-direction = minimum sector value; directional spread = max − min).
- **Access-hole centricity**: conventional guided-planning surrogate assuming a centered screw access hole reflects axial implant placement and reduced bending moments.
- **Eccentric amplification**: ratio of maximum von Mises stress under eccentric (oblique) loading to that under centric axial loading (S_e/S_c).
- **von Mises stress**: equivalent stress scalar used here to report peak interface stress (MPa) in the linear-elastic FE models.
- **Directional spread**: anisotropy measure across the four sectorial PIAAR values (maximum minus minimum); lower values indicate more balanced directional prosthetic support.
