---
title: "A systematic review of biomechanics of clear aligners by finite element analysis"
authors: "Cao H, Hu X, Yang L, Li D, et al."
year: 2025
date: 2025-07-02
doi: "10.1186/s12903-025-06295-6"
source: cao-2025-clear-aligner-biomechanics-finite-element-analysis-sr.md
category: [orthodontics/clear-aligner]
evidence_level: sr
source_collection: pubmed-text
full_text: true
pmid: "40604856"
pmcid: "PMC12224713"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12224713/
text_path: /Users/oracleneo/llm-wiki/papers/cao-2025-clear-aligner-biomechanics-finite-element-analysis-sr.txt
text_filename: cao-2025-clear-aligner-biomechanics-finite-element-analysis-sr.txt
tags: []
relations:
  - type: extends
    target: nakornnoi-2024-aligner-trimline-biomechanics-tooth-movement-sr
  - type: reinforces
    target: nucera-2022-composite-attachments-clear-aligners-sr
---

## Three-line Summary

PROSPERO-registered systematic review (186→29 FEA studies; ABAQUS/Ansys 13/13; all graded B-moderate; organized by mesiodistal, buccolingual, and occlusal movement direction) — first SR spanning all movement directions and auxiliary classes for clear-aligner biomechanics.

All clear aligner side effects (roller-coaster effect, anchorage loss, tipping, rotation) stem from uneven crown-vs-root stress distribution; every auxiliary device (attachments, power ridges, divots, intermaxillary elastics, membrane thickness) exists to rebalance that stress; extraction-space closing can exert 8–11× PDL pressure on anchorage teeth vs fixed appliances.

This FEA atlas maps side-effect-to-auxiliary relationships as a treatment-planning reference — understanding that CA delivers force only to crowns explains tipping-dominant movement and guides which auxiliary counterbalances each unwanted effect.

## 세줄요약

PROSPERO 등록 체계적 문헌고찰(186→FEA 29편; ABAQUS/Ansys 각 13편; 전체 B등급 중간; 근원심·협설·교합 방향별 분류) — 투명교정장치(Clear Aligner, CA) 생역학 전 이동 방향 및 보조장치 클래스를 포괄하는 최초 SR.

CA의 모든 부작용(롤러코스터 효과(Roller-Coaster Effect), 고정원 손실, 경사이동, 회전)은 치관-치근 간 불균등 응력 분포에서 기원; 모든 보조장치(어태치먼트·파워릿지·디봇·악간고무·멤브레인 두께)는 이 응력 재균형 목적; 발치 공간 폐쇄 시 치주인대(PDL) 압력 고정성 장치 대비 최대 8~11배.

이 FEA 아틀라스는 부작용↔보조장치 대응표를 치료계획 참조자료로 제공 — CA가 치관에만 힘을 전달한다는 점이 경사이동 우세의 근본 설명.

## Summary

This systematic review (PROSPERO 425621) collects every finite-element-analysis (FEA) study of clear-aligner (CA) biomechanics it could find on Web of Science and PubMed and organizes the **29 included studies** by the three orthodontic movement directions: mesiodistal (diastema), buccolingual (alignment), and occlusal/vertical (extrusion/intrusion). No meta-analysis was possible because the studies share no standard FEA protocol, parameter set, or data-presentation format.

Its central thesis is mechanistic. Because a CA shape-memory membrane delivers force only to **tooth crowns**, it inherently produces **unbalanced stress between crown and root** — more stress and displacement on the crown — which manifests as torque and the characteristic CA side effects: tipping, rotation, anchorage loss, and the **roller-coaster effect (RCE)** (lingual/distal tipping + extrusion of anteriors, mesial tipping + intrusion of posteriors during extraction-space closure). Every auxiliary device the review catalogs — attachments (shape/position), power ridges, divots, intermaxillary/intramaxillary elastic systems, and CA membrane thickness/layering — exists to **rebalance that stress distribution** so tipping converts into translation, or to deliberately generate a *controlled* torque where one is wanted.

All 29 articles were graded "B" (moderate reliability) under an SBU/CRD risk-of-bias scheme; FEA was run in ABAQUS (13/29) or Ansys (13/29).

## Key Contributions

- **A full FEA biomechanics atlas** of CA, the first SR to span all movement directions and auxiliary classes (prior reviews, e.g. trimline-focused, addressed single variables).
- A unifying **uneven-crown-vs-root-stress → torque → side-effect → auxiliary-counterbalance** framework.
- A side-effect-to-auxiliary mapping (which device offsets which problem) usable as a treatment-planning reference.
- Quantified periodontal cost (8-11× PDL pressure on anchorage teeth vs FA in extraction closure; max PDL stress proportional to CA thickness).

## Methodology

- **Design**: systematic review, PROSPERO 425621; PICO (P malocclusion, I CA, C CA/auxiliary designs, O FEA biomechanics).
- **Search**: Web of Science + PubMed, "clear aligner" AND "finite element" with synonyms.
- **Selection**: 186 records → 35 duplicates removed → exclusions → 45 full-text → **29 included** (13 excluded no FEA data, 3 FEA-vs-experimental only).
- **Two independent reviewers** (H.C., X.H.); verification by L.Y., D.L.
- **Risk of bias**: SBU + CRD grading — all 29 graded "B".
- **Included-study split**: 18 mesiodistal, 13 buccolingual, 8 occlusal; 20/29 modeled PDL (all linear elastic).

## Results

- **Extraction-space closing (9 studies)**: RCE is the dominant side effect; typical attachments on 3/5/6/7. **Indirect strong anchorage** (posterior teeth fixed/ligated) preserves anchorage and root control better than direct strong anchorage (elastics) or CA-alone moderate anchorage. Moving a molar button from mesiobuccal to mesiolingual reduces posterior mesial tipping. Multi-layer CA with >50% soft layer reduces lingual inclination of anteriors and mesial tipping of posteriors.
- **Non-extraction space opening / molar distalization (6 studies)**: incisal buccal flaring and posterior distal tipping persist; Class II elastics, AMS springs, and patient-specific attachments mitigate but do not eliminate them; guideline attachments even stress for bodily translation.
- **Scattered diastema (3 studies)**: root-control attachments (asymmetrical labial, overhanging) achieve bodily translation only after sufficient time (≈500 iterations).
- **Buccolingual torque (8 studies)**: power-ridge height shifts the center of rotation (root apex = controlled tipping; further = bodily retraction) without altering Von Mises stress; optimal ridge height is relative to CA thickness. Divots transfer higher load than attachments but are less precise (manually placed). 0.75 mm CA gives less incisal tipping and more even PDL stress than 0.5 mm.
- **Rotation (5 studies)**: CA alone can rotate anteriors; force/Crot scale with CA thickness; posterior rotation activation should stay ≤1.2°, and is more efficient with an attachment on the single target tooth than on target + proximal teeth.
- **Extrusion (4 studies)**: horizontal rectangular attachments concentrate stress on the incisal edge (highest efficiency); rectangular palatal attachments beat buccal; mandibular incisor extrusion is more efficient than maxillary.
- **Intrusion (5 studies)**: CA alone concentrates stress on the incisor cervix and causes lingual tipping/extrusion side effects; intermaxillary elastics (mini-screw) add palatal root torque, with linguoincisal (not labial) elastics relieving root resorption.
- **Periodontal**: worse PDL condition → higher stress → smaller planned movements; CA's instantaneous force exceeds FA's and reaches 8-11× PDL pressure on anchorage teeth in extraction closure, yet CA still shows lower periodontitis/gingivitis indices than FA.
- **Limitations**: no protocol/parameter/presentation standardization (no pooling), only instantaneous effects modeled, no biological (crown/root length) variables, linear-elastic PDL only, material fatigue/thermal aging under-studied.

## Related Papers

- [[orthodontics/clear-aligner/nakornnoi-2024-aligner-trimline-biomechanics-tooth-movement-sr]] — extends: companion FEA biomechanics SR focused on the single design variable of trimline/gingival-margin extension; Cao 2025 generalizes to the full auxiliary set.
- [[orthodontics/clear-aligner/nucera-2022-composite-attachments-clear-aligners-sr]] — reinforces: clinical attachment evidence base; Cao 2025 supplies the FEA mechanism by which attachment shape/position retunes torque and stress.
- [[orthodontics/clear-aligner/bhate-2025-cat-maxillary-molar-distalization-class-ii-sr]] — clinical molar-distalization outcomes underpinned here by the FEA biomechanics of incisal buccal flaring, distal tipping, and Class II elastics.
- [[orthodontics/clear-aligner/butsabul-2024-clear-aligner-root-resorption-cbct-sr-ma]] — root resorption clinical signal; Cao 2025 explains the root-apex PDL stress (thickness-dependent) that drives it.
- [[orthodontics/clear-aligner/yassir-2022-cat-vs-fat-overview-systematic-reviews]] — umbrella CAT-vs-FAT comparison; Cao 2025 adds the biomechanical why behind CAT's narrower indications and lower efficiency in bodily movement.
