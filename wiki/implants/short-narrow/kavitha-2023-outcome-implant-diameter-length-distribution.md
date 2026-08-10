---
title: "Outcome of Implant Diameter and Length on the Distribution of Stress with Immediate Loaded Implants: A 3D Finite Element Analysis"
authors: Kavitha G, Subhash Sonkesriya, Anil Kumar K, Faris Jaser Almutairi, Pravin M Parmar, Anuj Singh Parihar, Tanu Priya Sonkar
year: 2023
date: 2023-07-11
doi: 10.4103/jpbs.jpbs_100_23
source: kavitha-2023-outcome-implant-diameter-length-distribution.md
category: [implants/short-narrow]
evidence_level: in-vitro
pdf_path: /Users/oracleneo/llm-wiki/papers/kavitha-2023-outcome-implant-diameter-length-distribution.pdf
pdf_filename: kavitha-2023-outcome-implant-diameter-length-distribution.pdf
source_collection: external
tags: [finite-element-analysis, implant-length, implant-diameter, immediate-loading, von-mises, one-piece-implant]
relations:
  - type: contradicts
    target: singh-2024-influence-implant-design-length-stress
---

## Three-line Summary

3D finite element analysis (ANSYS v12) of a one-piece LEADER/ITALIA-Fix immediate-loading implant embedded in a 25×15×15 mm bone block, comparing two lengths (10 mm, 12 mm) and two diameters (3.75 mm, 4.25 mm) under a 2.0 MPa axial occlusal load.

Implant neck was the highest-stress zone in all configurations; increasing length from 10 mm to 12 mm slightly raised interface von Mises stress (1.32→1.76 MPa max), while increasing diameter from 3.75 mm to 4.25 mm had no appreciable effect on stress (1.77→1.79 MPa max).

Single in-silico model with idealized homogeneous/isotropic materials and one implant system — the length-increases-stress direction is opposite to some other FEA studies and should not be generalized without design/bone-density context.

## 세줄요약

일체형(one-piece) LEADER/ITALIA-Fix 즉시하중 임플란트를 25×15×15 mm 골블록에 매립한 3D 유한요소해석(Finite Element Analysis, FEA, ANSYS v12)으로, 길이 2종(10, 12 mm)·직경 2종(3.75, 4.25 mm)을 2.0 MPa 축방향 교합하중 하에서 비교.

전 조건에서 임플란트 넥(neck)이 최고 응력 부위였고, 길이를 10→12 mm로 늘리면 계면 von Mises 응력이 소폭 증가(최대 1.32→1.76 MPa)했으며, 직경을 3.75→4.25 mm로 늘려도 응력에 뚜렷한 영향은 없었다(최대 1.77→1.79 MPa).

단일 임플란트 시스템의 in-silico 모델(균질·등방성 재료 가정)이며, 길이 증가가 응력을 높이는 방향은 일부 다른 FEA 연구와 반대이므로 디자인·골밀도 맥락 없이 일반화하면 안 된다.

## Summary

This 3D finite element study models a one-piece LEADER/ITALIA-Fix implant designed specifically for immediate loading, embedded in a homogeneous bone block, to isolate the effect of implant **length** (10 mm vs 12 mm) and **diameter** (3.75 mm vs 4.25 mm) on peri-implant von Mises stress under a fixed 2.0 MPa axial load. Across all four configurations the implant neck/cervical region carried the maximum stress. Counter to the common assumption that longer implants reduce interface stress, this model found the opposite: going from 10 mm to 12 mm slightly **increased** maximum stress (1.32 → 1.76 MPa). Diameter increase (3.75 → 4.25 mm), by contrast, had essentially no effect on stress magnitude (1.77 → 1.79 MPa). As a single-system, idealized-material in-silico model, the length finding should be read as design-specific rather than a general biomechanical rule.

## Key Contributions

- Isolates length and diameter independently in a one-piece immediate-loading implant, holding the other dimension fixed for each comparison.
- Confirms the implant neck as the consistent maximum-stress location, replicating a repeated finding across the FEA literature this paper cites (Dundar 2016, Geng 2004).
- Reports a **length-increases-stress** direction (10→12 mm) that runs counter to some other FEA studies in this wiki (see Related Papers), highlighting that the length-stress relationship is not universal across implant macrogeometries and length ranges.
- Reports a **diameter-null** finding (3.75→4.25 mm) that also contrasts with cited studies (Eazhil 2016, de Moraes 2018) reporting diameter benefits.

## Methodology

- 3D FEA using ANSYS V.12; LEADER/ITALIA-Fix one-piece (fixture + abutment) implant, immediate-loading design.
- Bone block: 25 mm tall × 15 mm wide × 15 mm long, homogeneous/isotropic.
- Element types: SOLID95 (titanium implant, 3D 20-node tetrahedral) and SOLID191 (bone, 3D 20-node layered solid, up to 100 material layers).
- Variables: length 10 mm vs 12 mm (diameter fixed); diameter 3.75 mm vs 4.25 mm (length fixed at 12 mm).
- Load: 2.0 MPa axial force applied to the top of the abutment, simulating axial occlusal loading (no oblique loading tested).
- Outcome: von Mises stress magnitude and distribution at the implant-bone interface.

## Results

| Comparison | Configuration | Max stress (MPa) | Min stress (MPa) | Peak location |
|---|---|---|---|---|
| Length | 10 mm | 1.32 | 0.145 | Cervical/neck |
| Length | 12 mm | 1.76 | 0.373 | Neck |
| Diameter | 3.75 mm (length 12 mm) | 1.77 | 0.345 | Neck |
| Diameter | 4.25 mm (length 12 mm) | 1.79 | 0.367 | Cervical |

- Length increase (10→12 mm): small but consistent stress **increase**.
- Diameter increase (3.75→4.25 mm): negligible effect on stress magnitude.
- Implant neck/cervical zone is the highest-stress region in every tested configuration.

## Related Papers

- [[implants/singh-2024-influence-implant-design-length-stress]] — contradicts on direction: Singh 2024 (2D FEA, D4 bone, tapered/step designs, 6 mm vs 10 mm) found longer fixtures **consistently lowered** interface stress (vertical 188→35.44 MPa for step design); Kavitha 2023 (3D FEA, one-piece immediate-loading design, 10 mm vs 12 mm) found the **opposite direction** — a small stress increase with longer length. Different implant macrogeometry, length range, and bone model likely explain the divergence; together they show the length-stress relationship is design/context-dependent, not a fixed rule.
- [[implants/leblebicioglu-kurtulus-2022-fea-implant-design-bone-density-stress]] — reinforces the implant-neck/crestal-cortical-layer as the consistent peak-stress location across bone densities and thread designs; this paper adds a one-piece immediate-loading system to that pattern.
- [[implants/short-narrow/barbosa-2021-narrow-implants-one-two-piece-fea]] — related FEA comparing one-piece vs two-piece implants and diameter effects; useful cross-reference for interpreting this paper's diameter-null finding against a different one-piece/two-piece design contrast.
