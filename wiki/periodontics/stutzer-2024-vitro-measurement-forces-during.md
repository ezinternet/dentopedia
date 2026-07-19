---
title: "In-Vitro Measurement of Forces During Debridement with a Piezoelectric Ultrasonic Periodontal Scaler."
authors: Stutzer D, et al.
year: 2024
date: 2024-06-12
doi: 10.3290/j.ohpd.b5458595
source: stutzer-2024-vitro-measurement-forces-during.md
category: periodontics
evidence_level: in-vitro
source_collection: pubmed-text
full_text: true
pmid: "38864381"
pmcid: "PMC11619864"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11619864/
text_path: /Users/oracleneo/llm-wiki/papers/stutzer-2024-vitro-measurement-forces-during.txt
text_filename: stutzer-2024-vitro-measurement-forces-during.txt
tags: [ultrasonic-scaling, piezoelectric-scaler, debridement-force, dental-hygienist, in-vitro-biomechanics, periodontal-instrumentation]
relations:
  - type: extends
    target: dvorska-2026-mechanical-instrumentation-hard-tissue-sr
  - type: refines
    target: lodigkeit-2026-periodontal-instrumentation-enamel-cementum-review
---

## Three-line Summary

In-vitro biomechanical study: 10 dental hygienists and 6 dentists debrided soft (Model A, ~4.6 HV) and hard (Model B, ~24 HV) artificial dental calculus using a piezoelectric ultrasonic scaler (EMS PIEZON EN-060), with applied force recorded via a custom 3-axis force-sensor rig.

Mean total force was 0.34 N (hygienists) / 0.28 N (dentists) on soft calculus and 0.63 N / 0.57 N on hard calculus (hard vs soft: 1.85x, p=0.04 for hygienists; 2.04x, p=0.06 for dentists); force did not differ significantly between professions, was predominantly perpendicular to the surface (2.7–13.7x the parallel component), and exceeded the 0.5 N literature-recommended limit 14–56% of debridement time depending on calculus hardness.

Even trained, experienced professionals frequently exceed the recommended lateral-force ceiling, especially on hard calculus, suggesting force-feedback training aids could reduce iatrogenic root-surface damage risk; findings are limited by a small sample (one institution withdrew consent) and an in-vitro rig likely underestimating true in-vivo forces.

## 세줄요약

인비트로(In-Vitro) 생체역학 연구 — 치위생사 10명·치과의사 6명이 3축 힘센서(Three-axis Force Sensor) 실험대에서 압전형 초음파 스케일러(Piezoelectric Ultrasonic Scaler, EMS PIEZON EN-060)로 연질(Model A, 약 4.6 HV)·경질(Model B, 약 24 HV) 인공치석(Artificial Calculus)을 제거하며 가해진 힘을 기록.

평균 총력(Total Force)은 연질치석에서 치위생사 0.34 N·치과의사 0.28 N, 경질치석에서 0.63 N·0.57 N(경질/연질 비 1.85배 p=0.04[치위생사], 2.04배 p=0.06[치과의사]); 직종 간 유의차 없음, 힘은 표면 수직 방향이 압도적(평행 성분 대비 2.7~13.7배), 문헌 권장 상한 0.5 N을 치석 경도에 따라 전체 시간의 14~56% 초과.

숙련된 술자도 특히 경질 치석에서 권장 측방력(Lateral Force) 상한을 자주 초과 — 힘 피드백(Force Feedback) 훈련 보조기구가 의원성(Iatrogenic) 치근면 손상 위험을 줄일 수 있음을 시사; 표본이 작고(기관 1곳 참여 철회) in-vitro 실험대가 실제 임상보다 힘을 과소평가할 가능성이 한계.

## Summary

This in-vitro biomechanical study quantified the magnitude, direction, and temporal dynamics of force applied during periodontal debridement with a contemporary piezoelectric ultrasonic scaler (EMS PIEZON EN-060). Ten dental hygienists and six dentists, all experienced with the device, debrided artificial dental calculus of two hardness levels (soft ~4.6 HV, hard ~24 HV) mounted on a custom three-axis force-sensor rig. Mean applied force nearly doubled on hard versus soft calculus (0.63 N vs 0.34 N for hygienists; 0.57 N vs 0.28 N for dentists) with no significant difference between the two professions, and force was applied predominantly perpendicular rather than lateral to the surface. Critically, even these trained operators exceeded the literature-recommended 0.5 N force limit 14–56% of the time depending on calculus hardness, indicating that force awareness/control during ultrasonic scaling is difficult to achieve by training and experience alone, and supporting a case for instrumented force-feedback aids in both clinical practice and hygienist education.

## Key Contributions

- First force data for a contemporary **piezoelectric** ultrasonic scaler (prior data — Ruppert et al. — covered only magnetostrictive scalers), including direction and rate-of-change, not just magnitude.
- Shows force is predominantly perpendicular to the treated surface (2.7–13.7x the parallel component), reframing the common "lateral force ≤0.5 N" guidance.
- Calculus hardness, not clinician role, drives applied force: hygienists and dentists apply statistically indistinguishable forces, but force roughly doubles on hard vs soft calculus.
- Quantifies how often trained professionals exceed the 0.5 N recommended threshold — up to 56% of debridement time on hard calculus — showing training/experience alone does not guarantee force compliance.

## Methodology

- Custom 3-axis force-sensor rig (ZM3DW-AL 10N sensor + amplifier + NI USB-6366 DAQ), spring-scale-validated; video recorded scaler position.
- Two artificial-calculus models bonded to glass substrates: Model A soft (~4.6 HV), Model B hard (~24 HV).
- 10 dental hygienists + 6 dentists (all experienced with the device) each debrided a defined area on both models with a piezoelectric scaler (EMS PIEZON EN-060), self-selecting vibration intensity/irrigation.
- Force decomposed in MATLAB into 3 axes (Fx, Fy=perpendicular-to-surface, Fz) and total force F=√(Fx²+Fy²+Fz²); Wilcoxon rank-sum tests compared professions and calculus models.

## Results

| Outcome | Result |
|---|---|
| Mean total force — soft calculus (Model A) | Hygienists 0.34 N (SD 0.18); Dentists 0.28 N (SD 0.33) |
| Mean total force — hard calculus (Model B) | Hygienists 0.63 N (SD 0.40); Dentists 0.57 N (SD 0.17) |
| Hard vs soft force ratio | 1.85x hygienists (p=0.04); 2.04x dentists (p=0.06) |
| Hygienist vs dentist force | No significant difference (soft p=0.26; hard p=1.00) |
| Perpendicular : parallel force ratio | 12.6–13.7x (Model A, soft); 2.7–3.3x (Model B, hard) |
| % of debridement time force >0.5 N | Model A: 23%/14% (hygienists/dentists); Model B: 54%/56% |
| Max rate of force change recorded | Up to 61.8 N/s (mean max 11.9–39.5 N/s across groups/models) |

## Related Papers

- [[periodontics/dvorska-2026-mechanical-instrumentation-hard-tissue-sr]] — extends: that in-vitro SR quantifies ultrasonic-scaler-associated hard-tissue substance loss and surface roughness (the outcome side of instrumentation damage); this study supplies the upstream mechanistic driver — actual force magnitude, direction, and temporal dynamics applied by trained operators.
- [[periodontics/lodigkeit-2026-periodontal-instrumentation-enamel-cementum-review]] — refines: that narrative review names force as one of several unquantified operator-dependent variables behind ultrasonic-scaling cementum loss; this study provides exactly that force-magnitude quantification for a contemporary piezoelectric device.
