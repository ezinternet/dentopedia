---
title: "Evaluation of the Influence of Location of Osseointegrated Implants Associated with Mandibular Removable Partial Dentures"
authors: Ligia Del'Arco Pignatta Cunha, Eduardo Piza Pellizzer, Fellippo Ramos Verri, João Antonio Pereira
year: 2008
date: 2008-01-01
doi: null
source: cunha-2008-implant-location-mandibular-rpd-fea.md
category: [implants]
evidence_level: in-vitro
pdf_path: /Users/oracleneo/llm-wiki/papers/cunha-2008-implant-location-mandibular-rpd-fea.pdf
pdf_filename: cunha-2008-implant-location-mandibular-rpd-fea.pdf
source_collection: external
tags: [FEA, RPD, mandible, implant-location, stress-distribution, Kennedy-Class-I]
relations:
  - target: implants/hussein-2019-thread-depth-implant-shape-stress-mandible-fea
    type: extends
    note: "Both use FEA on mandibular implants; hussein-2019 focuses on thread design while cunha-2008 focuses on implant location in RPD context"
---

## Three-line Summary

2D finite element analysis (ANSYS 8.0; 5 models) evaluated how implant location in the distal-extension ridge affects stress distribution and displacement in a mandibular Kennedy Class I RPD associated with an osseointegrated implant.

Mesial implant placement (second premolar, Model E) produced the best stress relief at the abutment tooth; central placement (first molar, Model D) yielded the lowest overall RPD displacement; all implant models reduced RPD intrusion compared to implant-free RPD.

Implant location matters for biomechanical outcomes: mesial placement favors abutment protection, central placement favors prosthetic stability — but 2D static FEA without clinical validation limits direct clinical translation.

## 세줄요약

줄1: 2차원 유한요소법 (FEA, Finite Element Analysis, ANSYS 8.0)으로 5개 모델을 이용해 하악 Kennedy Class I 원심연장 가철성 국소의치 (RPD, Removable Partial Denture)에서 임플란트 위치가 응력 분포와 변위에 미치는 영향을 평가했다.

줄2: 근심 위치(제2소구치, Model E)에서 지대치 응력 분포가 가장 양호했고, 중심 위치(제1대구치, Model D)에서 의치 변위가 가장 적었으며, 임플란트가 있는 모든 모델에서 임플란트 없는 RPD보다 의치 함입이 감소했다.

줄3: 임플란트 위치는 생역학적 결과에 영향을 미치므로 임상 목표(지대치 보호 vs 의치 안정성)에 따라 위치를 선택해야 하나, 2D 정적 FEA 한계로 직접적 임상 적용에는 검증이 필요하다.

## Summary

This 2D FEA study from UNESP (Brazil) investigated whether the location of an osseointegrated implant along the mandibular posterior ridge influences the biomechanical behavior of a Kennedy Class I removable partial denture (RPD). Five models were compared: (A) natural dentition control, (B) RPD without implant, (C) RPD + implant at distal site (#37), (D) RPD + implant at central site (#36), (E) RPD + implant at mesial site (#35). A 50 N vertical load was applied to premolar cusp tips, and von Mises stress and displacement were assessed across the implant, abutment tooth, alveolar bone, prosthetic framework, and mucosa.

**Key finding:** Moving the implant mesially (toward the abutment tooth) progressively improved abutment tooth stress distribution, while central positioning minimized overall prosthetic displacement. All implant-supported models reduced RPD intrusion tendency relative to Model B (RPD only). Stress concentration consistently occurred at the implant's internal thread region across all implant models.

## Key Contributions

1. **Location-specific biomechanical trade-off:** Mesial position (near abutment) → better abutment stress; central position → better displacement control. No single position simultaneously optimizes both outcomes.
2. **Implant reduces intrusion universally:** Regardless of position, an implant supporting a distal-extension RPD reduces tissue-ward movement compared to conventional RPD design.
3. **Internal thread is the stress riser:** Stress concentration at the implant internal thread is location-independent — a consistent structural vulnerability across all tested positions.
4. **Methodological baseline:** One of the early 2D FEA studies establishing the RPD-implant interaction framework, later extended by 3D analyses with more realistic geometry.

## Methodology

- **Study type:** In vitro — 2D finite element analysis
- **Software:** ANSYS 8.0
- **Models:** 5 (A: control; B: RPD only; C: distal implant; D: central implant; E: mesial implant)
- **Geometry:** Sagittal cross-section of mandibular left hemi-arch (Kennedy Class I defect)
- **Loading:** 50 N vertical force on cusp tips of first and second premolars
- **Material properties:** Simplified isotropic, homogeneous bone; linear elastic analysis
- **Outputs:** Von Mises stress maps, displacement maps

## Results

| Model | Implant Site | Abutment Tooth Stress | RPD Displacement |
|---|---|---|---|
| A | Control (no RPD/implant) | Lowest baseline | Lowest baseline |
| B | RPD only | Elevated | Elevated |
| C | #37 (distal) | Moderate reduction | Moderate |
| D | #36 (central, 1st molar) | Moderate reduction | **Lowest** |
| E | #35 (mesial, 2nd premolar) | **Best relief** | Moderate |

- Models C, D, E all showed reduced RPD intrusion vs Model B
- Internal thread stress concentration present in all implant models (C, D, E)
- The closer the implant to the abutment tooth, the more favorable the abutment stress pattern

## Related Papers

- [[implants/hussein-2019-thread-depth-implant-shape-stress-mandible-fea]] — extends FEA mandibular implant analysis with thread depth and implant shape as variables (ANSYS, 2019)
- [[implants/premnath-2012-stress-distribution-bone-density-fea]] — parallel FEA study examining how bone density (Misch D1–D4) affects mandibular implant stress distribution
