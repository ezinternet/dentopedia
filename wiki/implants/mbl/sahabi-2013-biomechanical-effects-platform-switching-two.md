---
title: "Biomechanical effects of platform switching in two different implant systems: a three-dimensional finite element analysis."
authors: Mahasti Sahabi, Mehdi Adibrad, Fatemeh Sadat Mirhashemi, Sareh Habibzadeh
year: 2013
date: 2013-05-31
doi: null
source: sahabi-2013-biomechanical-effects-platform-switching-two.md
category: [implants/mbl]
evidence_level: in-vitro
source_collection: pubmed-text
full_text: true
pmid: "24396353"
pmcid: "PMC3875508"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3875508/
text_path: /Users/oracleneo/llm-wiki/papers/sahabi-2013-biomechanical-effects-platform-switching-two.txt
text_filename: sahabi-2013-biomechanical-effects-platform-switching-two.txt
tags: [platform-switching, finite-element-analysis, biomechanics, von-mises-stress]
relations:
  - type: reinforces
    target: yadav-2025-finite-element-analysis-platform-switching
---

## Three-line Summary

In vitro 3D finite element analysis (FEA) study comparing platform-switching (PS) vs conventional (matched-diameter) abutment configurations in two implant systems — XiVE S Plus (DENTSPLY Friadent) and 3i Certain (Biomet 3i) — under 100N axial and 100N/15° oblique loading in a mandibular first molar model.

In both implant systems, PS models showed lower maximum von Mises stress in crestal cortical and cancellous bone than matched (conventional) models, but higher stress concentration at the implant-abutment interface (IAI), with the high-stress zone shifting from the implant shoulder periphery toward the implant's center under PS.

PS reduced bone stress more than simply widening the implant platform did, but the paper notes the elevated IAI stress remained below titanium/Co-Cr yield strength, so it may not translate to immediate mechanical failure — though this was not tested directly.

## 세줄요약

XiVE S Plus(DENTSPLY Friadent)와 3i Certain(Biomet 3i) 두 임플란트 시스템을 대상으로, 플랫폼 스위칭(Platform Switching, PS) vs 매칭형 지대주(conventional, matched abutment) 구성을 하악 제1대구치 모델에서 100N 축방향(axial) 및 100N/15° 사방향(oblique) 하중으로 비교한 in vitro 3차원 유한요소분석(Finite Element Analysis, FEA) 연구.

두 임플란트 시스템 모두에서 PS 모델은 치조정 피질골(cortical bone)·해면골(cancellous bone)의 최대 von Mises 응력이 conventional 모델보다 낮았으나, 임플란트-지대주 계면(Implant-Abutment Interface, IAI)의 응력은 오히려 높았고, 고응력 부위가 임플란트 숄더 주변부에서 중심부 쪽으로 이동했다.

PS는 단순히 임플란트 직경을 넓히는 것(wide platform)보다도 골 응력 감소 효과가 컸으나, 상승한 IAI 응력은 티타늄·Co-Cr 합금의 항복강도보다 낮아 즉각적 기계적 파단으로 이어지지는 않을 것으로 저자들은 추정(직접 검증되지는 않음).

## Summary

This early (2013) FEA study compares platform switching (PS) against conventional, matched-diameter abutment configurations in **two different commercial implant systems** — XiVE S Plus (DENTSPLY Friadent) and 3i Certain (Biomet 3i) — modeled on a CT-derived edentulous mandibular first molar site. Six models were built: for each system, a regular-platform conventional model, a platform-switched model, and a wide-platform conventional model (matched abutment on the larger implant diameter), loaded with 100N either axially or obliquely (15° buccolingual). The central finding, consistent across both implant systems and both loading directions, is the now-familiar PS trade-off: **lower von Mises stress in the crestal cortical and cancellous bone**, but **higher stress concentration at the implant-abutment interface (IAI)**, with the IAI stress zone shifting inward from the implant shoulder periphery toward the implant's center. Notably, PS reduced bone stress more effectively than simply widening the implant platform (matched wide-diameter abutment) did — isolating the PS mechanism from a pure diameter effect. This paper is directly cited as "Sahabi et al." in [[implants/mbl/yadav-2025-finite-element-analysis-platform-switching]], a 2025 FEA study that reproduces the same bone-vs-component stress trade-off with different bone densities, implant system, and oblique-loading angle a decade later.

## Key Contributions

- Compares PS across **two different implant systems** (XiVE, 3i) in one study, rather than a single system — an early cross-system replication of the PS stress-reduction effect.
- Includes a "wide platform" conventional arm (matched abutment on the wider implant) to isolate PS's effect from a simple implant-diameter effect — shows PS still reduces bone stress more than diameter widening alone does.
- Explicitly localizes the shift in implant-abutment interface (IAI) stress concentration: from the implant shoulder periphery (conventional) to the implant's center (PS) — a mechanistic detail not always reported in later PS FEA studies.
- Serves as one of the earlier documented instances of the "bone stress down / component stress up" PS trade-off later replicated by [[implants/mbl/yadav-2025-finite-element-analysis-platform-switching]].

## Methodology

- In vitro 3D FEA, mandibular first molar site, CT-derived edentulous mandible geometry (2.0mm slice interval, ~8.5mm buccolingual × 24mm inferosuperior).
- Six models across two implant systems:
  - **XiVE S Plus**: XiVE-a (3.8×11mm implant + 3.8mm abutment, conventional regular platform), XiVE-b (4.5×11mm implant + 3.8mm abutment, **platform-switched**), XiVE-c (4.5×11mm implant + 4.5mm abutment, conventional wide platform)
  - **3i Certain**: 3i-a (4.0×11.5mm implant + 4.1mm abutment, conventional regular platform), 3i-b (5.0×11.5mm implant + 4.1mm abutment, **platform-switched**), 3i-c (5.0×11.5mm implant + 5.0mm abutment, conventional wide platform)
- Implants/abutments digitized (ATOS II), solid models in SolidWorks 2008, FE analysis in ABAQUS V6.7-1; tetrahedral mesh, 90,765–102,795 nodes per model.
- Isotropic, homogeneous, linearly elastic material properties; 100% osseointegration assumed at bone-implant interface; abutment-implant interface fully bonded.
- Mesial/distal mandibular bone surfaces fixed; linear static analysis; 100N load applied to abutment top-center, either axial or oblique (15° buccolingual inclination).
- Outcomes: von Mises stress in crestal cortical and cancellous bone and at the implant-abutment interface; maximum/minimum principal (tensile/compressive) stress at crestal bone.

## Results

- Stress patterns were similar under axial vs. oblique loading in both systems, but **oblique loading produced higher stress than axial loading** throughout.
- **Cortical bone stress exceeded cancellous bone stress** in all six models, under both loading conditions.
- Under 100N **oblique** load, maximum von Mises stress in cortical bone: **15.06 MPa (XiVE-b, PS, lowest)** to **32.11 MPa (3i-a, conventional regular platform, highest)**. Maximum von Mises stress in cancellous bone: **2.49 MPa (3i-b, PS, lowest)** to **6.28 MPa (XiVE-a, conventional regular platform, highest)**.
- **PS reduced von Mises stress at the crestal bone in both implant systems**, under both loading conditions, and for both tensile and compressive principal stress.
- **PS outperformed simple diameter-widening**: wide-platform conventional models (XiVE-c, 3i-c) had lower bone stress than regular-platform conventional models (XiVE-a, 3i-a), but PS models (XiVE-b, 3i-b) still showed **lower** bone stress than the wide-platform conventional models.
- At the implant-abutment interface, the high-stress zone sat at the implant-shoulder periphery in conventional models but **shifted toward the implant's center under PS**; **PS increased IAI stress in both systems and both loading directions**.
- Observed IAI stress values remained below reported yield strengths of titanium alloy (620–725 MPa) and Co-Cr alloy (552–1,034 MPa), so the authors suggest PS-related stress increases may not cause immediate mechanical failure — not directly tested (no fatigue/cyclic loading modeled).
- Axial-loading-specific MPa values and the material-property table were not recoverable from the extracted full text (figures/tables not preserved by PubMed text extraction); only oblique-load ranges and qualitative axial-vs-oblique comparisons are quoted above.

## Related Papers

- [[implants/mbl/yadav-2025-finite-element-analysis-platform-switching]] — directly cites this paper ("Sahabi et al.") and reproduces the same bone-stress-down/component-stress-up PS trade-off over a decade later, across D2/D3 bone densities and a different implant system (Adin Internal-Hex) under axial and 30° oblique loading. This 2013 paper is the earlier, cross-implant-system data point that [[implants/mbl/yadav-2025-finite-element-analysis-platform-switching]] extends and reinforces.
- [[implants/mbl/schwarz-2013-implant-abutment-connection-platform-switching]] — same-year (2013) literature specifically on implant-abutment connection design and platform switching; complements this paper's implant-abutment-interface stress findings.
- [[implants/mbl/salimi-2011-platform-switching-current-results]] — narrative review of PS evidence contemporaneous with this study; situates its FEA findings within the broader clinical/biomechanical literature of the period.
- [[implants/mbl/juan-montesinos-2022-platform-switching-conventional-sr-ma]] — clinical SR+MA confirming PS's marginal bone loss (MBL) benefit; this paper's crestal-bone-stress reduction is an early biomechanical rationale consistent with that pooled clinical effect.
