---
title: "Finite Element Analysis of Platform Switching Effects on Stress Distribution in Posterior Implants Placed in Different Bone Types Under Axial and Oblique Loading Conditions"
authors: Kanika Yadav, Sandeep Kumar, Rajnish Aggarwal, Iqbal Kaur, Ankit Goyal, Rahul Sharma, Satyendra Banjara
year: 2025
date: 2025-06-26
doi: 10.7759/cureus.86821
source: yadav-2025-finite-element-analysis-platform-switching.md
category: [implants/mbl]
evidence_level: in-vitro
source_collection: pubmed-text
full_text: true
pmid: "40718348"
pmcid: "PMC12296853"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12296853/
text_path: /Users/oracleneo/llm-wiki/papers/yadav-2025-finite-element-analysis-platform-switching.txt
text_filename: yadav-2025-finite-element-analysis-platform-switching.txt
tags: [platform-switching, finite-element-analysis, biomechanics, stress-distribution, von-mises-stress]
relations:
  - type: reinforces
    target: juan-montesinos-2022-platform-switching-conventional-sr-ma
---

## Three-line Summary

In vitro finite element analysis (FEA) study using CBCT-derived 3D models of posterior maxilla (D3 bone) and mandible (D2 bone), comparing platform-switched (PS, 3.2mm abutment on 4.2mm implant) vs non-platform-switched (NPS, matched 4.2mm abutment) configurations under 200N axial and 200N/30° oblique loading.

PS consistently reduced peak von Mises stress in cortical and cancellous bone compared to NPS, especially near the crestal region and under oblique loading, but shifted higher stress onto the implant, abutment, and abutment screw components — most pronounced in the maxilla under axial loading and in the mandible under oblique loading.

PS provides a biomechanical rationale for the clinically observed crestal-bone-preservation effect, but the higher internal stress on prosthetic components under PS suggests a need for more durable abutment materials/designs, particularly under oblique (non-axial) functional loading.

## 세줄요약

유한요소분석(Finite Element Analysis, FEA) in vitro 연구 — CBCT 기반 상악 구치부(D3골) · 하악 구치부(D2골) 3차원 모델에서 플랫폼 스위칭(Platform Switching, PS, 4.2mm 임플란트+3.2mm 지대주) vs 비-플랫폼 스위칭(Non-Platform-Switching, NPS, 4.2mm 지대주 매칭) 비교, 200N 축방향(axial) 및 200N/30° 사방향(oblique) 하중 적용.

PS는 NPS 대비 피질골·해면골, 특히 치조정 부위의 최대 von Mises 응력을 일관되게 낮췄고 이는 사방향 하중에서 더 뚜렷했으나, 임플란트·지대주·지대주나사에는 오히려 응력이 증가(상악에서는 축방향, 하악에서는 사방향 하중 시 최대).

PS의 임상적 치조정골 보존 효과에 생체역학적 근거를 제공하나, 보철 구성요소(특히 지대주)의 응력 증가는 사방향 하중 하에서 더 견고한 지대주 소재·설계가 필요함을 시사.

## Summary

This FEA study fills a mechanistic gap in the wiki's platform-switching evidence: while multiple clinical RCTs and SR+MAs already established that PS reduces marginal bone loss, none of them explain *why* in biomechanical terms. Using CBCT-derived 3D models of posterior maxilla (D3, lower-density bone) and mandible (D2, denser bone), the authors compared platform-switched (3.2mm abutment on a 4.2mm implant) against non-platform-switched (matched 4.2mm abutment) configurations under both axial and 30° oblique 200N loads. The consistent finding across both jaws and both loading directions: PS lowers peak von Mises stress in the crestal cortical and cancellous bone — supporting the clinical bone-preservation effect — but this comes at the cost of elevated stress on the implant, abutment, and abutment screw, since the narrower abutment acts as a longer lever arm under off-axis loading. The effect was most dramatic under oblique loading, where abutment stress roughly doubled with PS in both jaws (maxilla 47.8→96.6 MPa; mandible 46.7→106.1 MPa).

## Key Contributions

- Directly compares PS vs NPS across a 2×2 factorial design (D3 maxilla / D2 mandible × axial / oblique loading) — more comprehensive than most single-condition FEA studies in this space.
- Quantifies the PS trade-off explicitly: bone-side stress reduction vs prosthetic-component stress increase, with component-level (cortical, cancellous, implant, abutment, screw) von Mises stress tables.
- Oblique loading — a more clinically realistic simulation of masticatory forces than axial-only studies — shows the largest PS-related shift of stress from bone to prosthetic components.

## Methodology

- In vitro FEA, CBCT-derived 3D models (CATIA V5), ANSYS Workbench meshing with <5% convergence tolerance.
- Implant: titanium, modeled on Adin Internal-Hex Touareg-S, 11.5mm × 4.2mm. NPS = 4.2mm abutment; PS = 3.2mm abutment. PFM crown on first molar.
- Perfect-bonding interfaces (complete osseointegration assumed); isotropic homogeneous linear-elastic material properties (cortical bone E=13.7GPa; cancellous bone E=1.6GPa maxilla/5.5GPa mandible; titanium E=110GPa).
- Loads: 200N axial, 200N at 30° oblique — both representative of literature-standard molar occlusal forces.
- Outcome: von Mises stress/strain on cortical bone, cancellous bone, implant, abutment, abutment screw.

## Results

| Structure | Axial: NPS→PS (Maxilla, MPa) | Axial: NPS→PS (Mandible, MPa) | Oblique: NPS→PS (Maxilla, MPa) | Oblique: NPS→PS (Mandible, MPa) |
|---|---|---|---|---|
| Cortical bone | 9.259→8.082 | 5.432→4.817 | 19.293→16.924 | 16.374→11.201 |
| Cancellous bone | 5.357→3.658 | 1.287→0.933 | 4.406→3.271 | 1.247→1.139 |
| Implant | 18.679→19.138 | 12.712→13.919 | 47.091→61.108 | 39.704→64.646 |
| Abutment | 22.310→23.699 | 21.628→22.892 | 47.811→96.632 | 46.678→106.072 |
| Abutment screw | 6.720→9.599 | 9.075→6.500 | 6.720→9.599 | 6.500→9.075 |

- PS reduced peak bone stress in all 4 jaw×loading combinations, largest relative drop in mandibular cortical bone under oblique loading (~32% reduction).
- PS raised peak implant/abutment stress in nearly all combinations, most dramatically under oblique loading (abutment stress roughly doubled in both jaws).
- Oblique loading produced markedly higher stress than axial loading across all structures and both designs.
- Authors note observed peak stresses remained below titanium (620–725 MPa) and Ni-Cr (415–620 MPa) yield strengths, so the elevated PS-side stress may not immediately translate to mechanical failure — but this was not fatigue-tested.

## Related Papers

- [[implants/mbl/juan-montesinos-2022-platform-switching-conventional-sr-ma]] — clinical SR+MA (PS MD 0.255mm less MBL). This FEA study supplies the biomechanical mechanism (reduced crestal bone stress) underlying that pooled clinical effect.
- [[implants/mbl/strietzel-2015-platform-switching-mbl-sr-ma]] / [[implants/mbl/di-girolamo-2016-platform-switching-matching-sr-ma]] — clinical SR+MAs on PS bone preservation; this paper's stress-distribution data offers a mechanistic complement to their pooled effect sizes.
- [[implants/mbl/bhatt-2025-effect-platform-switching-peri-implant]] — contemporary (2025) clinical RCT showing PS lowers 12-month CBL; this FEA study's crestal-stress-reduction finding is a plausible mechanism for that RCT's result.
