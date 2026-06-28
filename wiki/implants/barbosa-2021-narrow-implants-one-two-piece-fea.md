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

## One-line Summary

FEA study (3 implant models, 150 N axial/30° angled load) finds the 2.5 mm extra-narrow one-piece implant exceeds titanium yield strength by 93.6% under angled loading, while 3.0 mm one-piece and 3.5 mm two-piece Morse taper implants remain within safe stress limits.

## 한줄요약

FEA 연구: 2.5 mm 초소경 one-piece 임플란트는 경사하중(30°) 시 티타늄 항복강도를 93.6% 초과(2188 MPa vs. 1130 MPa)해 파절 위험이 있으며, 3.0 mm one-piece 및 3.5 mm Morse taper two-piece 임플란트는 축·경사 하중 모두에서 안전한 응력 범위를 유지함.

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
