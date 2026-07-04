---
title: "Comparative analysis of stress distribution in one-piece and two-piece implants with narrow and extra-narrow diameters: A finite element study"
authors: Fabricia Teixeira Barbosa, Luiz Carlos Silveira Zanatta, Edelcio de Souza Rendohl, Sergio Alexandre Gehrke
year: 2021
date: 2021-02-04
doi: 10.1371/journal.pone.0245800
source: barbosa-2021-narrow-implants-one-two-piece-fea.md
category: [implants]
confidence: in-vitro
pdf_path: /Users/oracleneo/llm-wiki/papers/barbosa-2021-narrow-implants-one-two-piece-fea.pdf
pdf_filename: barbosa-2021-narrow-implants-one-two-piece-fea.pdf
source_collection: external
tags: []
---

## Three-line Summary

In vitro FEA study (Ansys Workbench) comparing 3 narrow/extra-narrow implant designs — G1: 2.5 mm extra-narrow one-piece; G2: 3.0 mm narrow one-piece; G3: 3.5 mm narrow two-piece Morse taper — under 150 N axial and 30° angled loading in a simulated maxillary lateral incisor site (cortical 1 mm, cancellous bone, porcelain crown).

G1 generated 2188 MPa under angled loading, exceeding titanium yield strength (1130 MPa) by 93.6%; G2 and G3 remained within safe limits; the Morse taper G3 reduced cortical bone stress 321% versus G1 under axial load, though under angled loading G3 cortical stress was 391.8% higher than G1/G2 (still within 50 MPa bone limit); no bone failure was predicted for any group by Mohr-Coulomb analysis.

Extra-narrow one-piece implants ≤2.5 mm are biomechanically risky under off-axis occlusal forces and should be used with great caution in anterior sites; 3.0 mm one-piece and 3.5 mm Morse taper two-piece designs show adequate structural behavior under both loading conditions.

## 세줄요약

FEA 연구(Ansys Workbench): 3가지 소경·초소경 임플란트 모델 — G1 2.5 mm 초소경 one-piece, G2 3.0 mm 소경 one-piece, G3 3.5 mm Morse taper two-piece — 상악 측절치 부위 모델에서 150 N 축하중·30° 경사하중 비교.

G1은 경사하중 시 2188 MPa 발생으로 티타늄 항복강도(1130 MPa)를 93.6% 초과; G2·G3는 임플란트 응력 허용 범위 이내; G3 Morse taper는 축하중에서 G1 대비 피질골 응력을 321% 감소시키나 경사하중에서는 G1·G2 대비 391.8% 증가(단, 50 MPa 골 허용치 이내); Mohr-Coulomb 분석에서 모든 군 골 파절 예측 없음.

2.5 mm 이하 초소경 one-piece 임플란트는 비축방향 교합력이 예상되는 전치부 식립 시 파절 위험이 크므로 신중한 적응증 선택 필요; 3.0 mm one-piece 및 3.5 mm Morse taper two-piece는 두 하중 조건 모두에서 안전한 생역학적 거동을 보임.

## Summary

This PLoS ONE FEA study compared stress distribution across three narrow/extra-narrow implant designs (G1: 2.5 mm extra-narrow one-piece; G2: 3.0 mm narrow one-piece; G3: 3.5 mm narrow two-piece Morse taper). Three-dimensional models including cortical bone (1 mm), cancellous bone, cement, and feldspathic porcelain crown (maxillary lateral incisor) were built in Rhinoceros 5.4.1 and analyzed in Ansys Workbench 19.0 under 150 N axial and 30° angled loads.

The critical finding: G1 generated 2188 MPa under angled loading — 93.6% above the titanium yield limit of 1130 MPa — indicating fracture risk with off-axis loading. In contrast, G2 and G3 remained within structural limits. G3 (Morse taper) concentrated implant stress at the internal cone under axial load (1593.3 MPa but within limit) while dramatically reducing cortical bone stress (321% lower than G1 under axial load). Under angled loading, G3 showed 391.8% higher cortical bone stress than G1/G2, though still within the 50 MPa bone limit. Cancellous bone stress was low across all groups (3–12 MPa). Mohr-Coulomb analysis confirmed no bone failure risk for any group.

The authors conclude that extra-narrow one-piece implants (≤2.5 mm) should be used with great caution, especially where off-axis occlusal forces are expected, while narrow one-piece (3.0 mm) and two-piece Morse taper (3.5 mm) implants show adequate biomechanical behavior.

## Key Contributions

- Demonstrated that the 2.5 mm one-piece design exceeds titanium yield limits under angled (30°) loading — a clinically relevant finding for anterior sites with non-axial forces
- Quantified the stress-shielding benefit of Morse taper connections: G3 showed 321% lower cortical bone stress than G1 under axial load
- Applied dual stress criteria (von Mises for titanium + Mohr-Coulomb for bone) for more rigorous structural analysis
- Provided concrete stress thresholds (MPa values) for each implant component and bone compartment

## Methodology

- **Models**: 3 groups (G1: 2.5 mm one-piece; G2: 3.0 mm one-piece; G3: 3.5 mm two-piece Morse taper, 9 mm length each)
- **Software**: Rhinoceros 5.4.1 (geometry) + Ansys Workbench 19.0 (FEA)
- **Bone model**: Cortical bone 1.0 mm thick; cancellous bone below; all contacts bonded except G3 Morse cone (frictional, μ=0.8)
- **Load**: 150 N axial (0°) and angled (30°)
- **Criteria**: von Mises (implant + bone); Mohr-Coulomb (bone, distinguishing tension/compression)
- **Yield limits**: Titanium 1130 MPa; cortical bone 114 MPa (axial) / 50 MPa (angled)
- **Mesh**: 432,020–887,245 elements; 753,005–1,398,103 nodes

## Results

| Group | Diameter | Type | Axial stress (implant) | Angled stress (implant) | Cortical bone (axial) |
|---|---|---|---|---|---|
| G1 | 2.5 mm | One-piece | 224.26 MPa | **2188 MPa** (93.6% over limit) | Highest |
| G2 | 3.0 mm | One-piece | 169.2 MPa | Within limit | 22.35% less than G1 |
| G3 | 3.5 mm | Two-piece (Morse) | 1593.3 MPa (cone, within limit) | Within limit | 321.23% less than G1 |

- All groups: cancellous bone 3–12 MPa (safe)
- G3 under angled load: cortical bone 391.8% higher than G1/G2 but still within 50 MPa limit
- Mohr-Coulomb: no bone failure predicted for any group

**Clinical implication**: Extra-narrow one-piece implants (≤2.5 mm) are biomechanically risky under off-axis loading; narrow one-piece (3.0 mm) and Morse taper two-piece (3.5 mm) are safe choices.

## Related Papers

- [[implants/cao-2023-titanium-zirconium-narrow-diameter-single-crown]] — clinical outcomes of narrow-diameter titanium/zirconia implants (complements this biomechanical FEA data)
- [[implants/baki-2025-all-on-4-trefoil-five-implant-fea]] — FEA for full-arch implant designs, same Ansys methodology
- [[implants/bilgi-ozyetim-2025-biomechanical-comparison-implant-inclinations]] — FEA of implant inclination effects on stress distribution
- [[implants/leblebicioglu-kurtulus-2022-fea-implant-design-bone-density-stress]] — FEA implant design and bone density stress interactions
