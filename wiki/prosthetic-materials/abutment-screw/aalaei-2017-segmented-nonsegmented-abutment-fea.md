---
title: "Stress distribution pattern of screw-retained restorations with segmented vs. non-segmented abutments: A finite element analysis"
authors: Shima Aalaei, Zahra Rajabi Naraki, Fatemeh Nematollahi, Elaheh Beyabanaki, Afsaneh Shahrokhi Rad
year: 2017
date: 2017-07-04
doi: 10.15171/joddd.2017.027
source: aalaei-2017-segmented-nonsegmented-abutment-fea.md
category: [prosthetic-materials/abutment-screw]
evidence_level: in-vitro
pdf_path: /Users/oracleneo/llm-wiki/papers/aalaei-2017-segmented-nonsegmented-abutment-fea.pdf
pdf_filename: aalaei-2017-segmented-nonsegmented-abutment-fea.pdf
source_collection: external
tags: []
relations:
  - type: extends
    target: velez-2020-implant-connection-abutment-design-screw
---

## Three-line Summary

3D finite element analysis (CT-based mandibular first molar, Straumann tissue-level 4.1×10 mm, ANSYS Workbench; n=2 abutment designs: segmented RNSynocta vs non-segmented RNSynocta Gold; 100 N vertical and 100 N 45° angular loading).

Under angular loading, the segmented abutment reduced peri-implant bone von Mises stress dramatically (31 vs 126 MPa, 4× lower) and micro-strain (2400 vs 9400 μɛ, well below vs far above the 3000 μɛ overload threshold), at the cost of slightly higher abutment screw stress (430 vs 375 MPa); vertical loading showed similar bone stress between designs (21 vs 24 MPa).

The segmented abutment's two-piece micro-motion junction absorbs lateral force, providing meaningful bone protection under the angular loading dominant in clinical occlusion — a favorable stress trade-off for bone preservation at modest screw-stress cost.

## 세줄요약

3D 유한요소분석(CT 기반 하악 제1대구치, Straumann 조직 수준 임플란트 4.1×10 mm, ANSYS Workbench; 세그먼트형 RNSynocta vs 비분리형 RNSynocta Gold; 100 N 수직·45° 각도 하중 2조건).

각도 하중에서 세그먼트형 어버트먼트는 골 응력을 4배 낮추고(31 vs 126 MPa), 미세변형률도 과부하 역치(3000 μɛ) 이하로 유지(2400 vs 9400 μɛ); 나사 응력은 약간 증가(430 vs 375 MPa); 수직 하중은 두 설계 유사(21 vs 24 MPa).

세그먼트형 어버트먼트의 2단 미세운동 접합부가 측방력을 흡수하여 임상 교합에서 지배적인 각도 하중 시 골 보호 효과를 제공함 — 약간의 나사 응력 증가를 감수하더라도 골 보존 면에서 유리한 응력 절충안이다.

## Summary

FEA study comparing two screw-retained abutment designs on stress distribution. The key finding is a trade-off: segmented abutment markedly protects crestal bone under angular (non-axial) loading — clinically the more physiological scenario — but concentrates slightly more stress in the abutment screw itself. The non-segmented design sacrifices bone protection for screw protection.

The dramatic angular bone stress difference (31 vs 126 MPa, i.e., non-segmented = 4× higher) is the clinically actionable finding. Both types show similar bone stress under purely vertical loading (21 vs 24 MPa). Micro-strain data amplifies the same message: angular load in non-segmented = 9400 μɛ vs 2400 μɛ in segmented (nearly 4× higher, well into overload zone).

## Key Contributions

- Quantified the bone-protection advantage of segmented abutment under realistic angular loading (clinically the predominant occlusal vector)
- Established the stress trade-off: lower bone stress (segmented) at cost of modestly higher screw stress — overall a favorable exchange for bone preservation
- Micro-strain data (non-segmented angular: 9400 μɛ, far above 3000 μɛ overload threshold) supports clinical preference for segmented design in areas with off-axis loading

## Methodology

- **Model**: CT-based 3D mandibular first molar; Straumann tissue-level implant 4.1 mm × 10 mm; 1 mm cortical bone buccal/lingual
- **Abutments**: Segmented (RNSynocta 1.5 + Synocta Gold coping) vs Non-segmented (RNSynocta Gold Abutment)
- **Crown**: PFM symmetric, 12×9 mm (mesiodistal × buccolingual)
- **Loading**: 100 N vertical; 100 N at 45° oblique — applied at central fossa
- **Software**: ANSYS Workbench v12.0.1; von Mises stress; parabolic tetrahedral mesh
- **Assumption**: complete osseointegration; homogeneous isotropic linear elastic materials

## Results

**Peri-implant bone — von Mises stress:**

| Load | Segmented | Non-segmented |
|---|---|---|
| Vertical (100 N) | 21 MPa | 24 MPa |
| Angular 45° (100 N) | **31 MPa** | **126 MPa** |

**Abutment screw — von Mises stress:**

| Load | Segmented | Non-segmented |
|---|---|---|
| Vertical (100 N) | 100 MPa | 87 MPa |
| Angular 45° (100 N) | 430 MPa | 375 MPa |

**Micro-strain in peri-implant bone:**

| Load | Segmented | Non-segmented |
|---|---|---|
| Vertical | 2200 μɛ | 4400 μɛ |
| Angular | 2400 μɛ | **9400 μɛ** |

Maximum stress always at implant neck; diminished with distance from implant. Angular loading produced substantially higher stresses in all components vs vertical loading.

**Mechanism**: The two-piece junction of segmented abutment permits micro-motion at the component interface, absorbing/dissipating lateral force before it reaches crestal bone (consistent with Rangert et al. flexibility principle).

## Related Papers

- [[prosthetic-materials/abutment-screw/velez-2020-implant-connection-abutment-design-screw]] — abutment design and implant connection effects on screw mechanics (extends context)
- [[prosthetic-materials/abutment-screw/bulaqi-2015-dynamic-nature-abutment-screw-retightening]] — abutment screw dynamics and preload; relevant to the screw-stress trade-off found here
- [[prosthetic-materials/abutment-screw/angermair-2024-microgap-abutment-displacement-implant-connection]] — microgap and micro-motion at implant-abutment connection, mechanistically related
