---
title: "Assessment of the Impact of Bone Quality and Abutment Configuration on the Fatigue Performance of Dental Implant Systems Using Finite Element Analysis (FEA)"
authors: Erdoğdu M, Demirel MG, Mohammadi R, Güntekin N
year: 2024
date: 2024-09-28
doi: 10.3390/jpm14101040
pmid: "39452546"
pmcid: "PMC11508474"
source: erdogdu-2024-abutment-angle-bone-quality-fatigue-fea.md
category: [implants]
evidence_level: in-vitro
source_collection: pubmed-text
text_path: /Users/oracleneo/llm-wiki/papers/erdogdu-2024-abutment-angle-bone-quality-fatigue-fea.txt
text_filename: erdogdu-2024-abutment-angle-bone-quality-fatigue-fea.txt
full_text: true
tags: [abutment-angle, fatigue, stress-distribution, FEA, multiunit-abutment, cemented-abutment, bone-quality]
relations:
  - type: reinforces
    target: chi-2024-customized-angled-abutment-tooth-inclination-fea
  - type: reinforces
    target: murat-2025-all-on-4-implant-angulation-load-direction-fea
---

## Three-line Summary

FEA study (maxillary 3-unit bridge, 150 N oblique load, 6 groups: multiunit vs cemented abutments at 0°/15°/25–30°, healthy vs resorbed bone) jointly analyzing stress distribution and fatigue performance.

Increasing abutment angle raised von Mises stress and reduced fatigue life in all groups; multiunit abutments produced lower stress and higher fatigue resistance than cemented abutments at every comparable angle; resorbed bone amplified both adverse findings.

Minimize abutment angulation and prefer multiunit (screw-retained) over cemented design — especially in resorbed bone patients who already face higher biomechanical risk.

## 세줄요약

FEA 연구 (상악 3단 브릿지, 150 N 경사 하중, 6군: 멀티유닛 vs 시멘트형 지대주 각 0°/15°/25–30°, 건강골 vs 흡수골) — 응력 분포와 피로 강도를 동시 분석.

지대주 각도 증가 → von Mises 응력 증가 + 피로 강도 감소; 멀티유닛 지대주가 모든 비교 각도에서 시멘트형보다 낮은 응력·높은 피로 강도; 흡수골에서 두 불리한 경향 모두 심화.

지대주 각도는 최소화하고 특히 흡수골 환자에서 시멘트형보다 멀티유닛(나사 유지형)을 선호해야 하며, 경사 부위에서는 최소 각도로 수직 보정 후 멀티유닛 설계를 우선 선택.

## Summary

This FEA study is one of the few to jointly analyze stress distribution AND fatigue performance across abutment angle configurations, providing a more complete biomechanical picture than stress-only analyses.

**Bottom line**: Abutment angle increase worsens two independent outcomes — stress AND fatigue — and resorbed bone amplifies both. Multiunit abutments consistently outperform cemented abutments. The implication is clear: when you cannot place the implant axially and must use an angled abutment, choose the minimum angle needed and prefer multiunit (screw-retained) over cemented design.

## Key Contributions

- Quantified abutment angle effect on fatigue performance (cycles-to-failure) — not just static stress
- Demonstrated consistent superiority of multiunit over cemented abutments across 0°, 15°, and 25–30° angles
- Showed resorbed bone significantly amplifies both adverse findings (higher vMS, lower fatigue)
- Clinically relevant angle groupings matched to real commercial abutment options

## Methodology

- 3D maxillary bone model (SolidWorks + Abaqus): cortical + trabecular + mucosa
- 2 implants: 1st premolar + 1st molar (Bil Implant, Ø3.7 mm × 10 mm); 2nd premolar pontic
- 6 groups: Multiunit 0°/15°/30° (Mu0/Mu15/Mu30); Cemented 0°/15°/25° (C0/C15/C25)
- 2 bone types: Healthy bone (Hb) vs Resorbed bone (Rb)
- Load: 150 N oblique, palatal→buccal, 30°; screw preload 781 N (25 N·cm)
- Fatigue: critical-plane criterion + Coffin-Manson + Basquin laws; 1000 direct cyclic steps
- Restoration: monolithic zirconia; 40 µm resin cement (cemented groups)

## Results

| Group | Bone stress (vMS) | Implant fatigue |
|---|---|---|
| Mu0 | Lowest | Highest |
| Mu15 | Low-moderate | High |
| Mu30 | Moderate | Moderate |
| C0 | Moderate | Moderate |
| C15 | High | Lower |
| C25 | HIGHEST | LOWEST |

- vMS increases proportionally with abutment angle in ALL groups
- Multiunit < Cemented vMS at every comparable angle
- Fatigue performance decreases inversely with angle increase
- Resorbed bone → numerically higher vMS AND lower fatigue vs healthy bone in all groups
- Molar region → higher stress + lower fatigue than premolar (thinner cortical bone)

**Mechanism**: Higher abutment angle → bending moment at IAJ → stress concentration at implant neck / crestal cortical bone → reduced fatigue life. Resorbed bone: lower elastic modulus → less effective load distribution → magnified stress.

## Clinical Implication

1. **Minimize abutment angulation** — each degree added costs fatigue life
2. **Prefer multiunit (screw-retained) over cemented** abutments — especially when angled
3. **Resorbed bone patients** are at higher biomechanical risk → consider bone augmentation or flat-angle solutions first
4. When adjacent tooth is tilted: place implant perpendicular to occlusal plane → correct crown direction with minimum-angle abutment → prefer multiunit design

## Related Papers

- [[implants/chi-2024-customized-angled-abutment-tooth-inclination-fea]] — customized abutments designed for tooth inclination; axial vs oblique loading determines winner
- [[implants/murat-2025-all-on-4-implant-angulation-load-direction-fea]] — load direction × implant angle interaction; frontal BL load is more detrimental than implant angle alone
