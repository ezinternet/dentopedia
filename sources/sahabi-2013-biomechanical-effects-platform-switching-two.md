---
title: "Biomechanical effects of platform switching in two different implant systems: a three-dimensional finite element analysis."
authors: Mahasti Sahabi, Mehdi Adibrad, Fatemeh Sadat Mirhashemi, Sareh Habibzadeh
year: 2013
doi: null
category: [implants/mbl]
source_collection: pubmed-text
full_text: true
pmid: "24396353"
pmcid: "PMC3875508"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3875508/
text_path: /Users/oracleneo/llm-wiki/papers/sahabi-2013-biomechanical-effects-platform-switching-two.txt
text_filename: sahabi-2013-biomechanical-effects-platform-switching-two.txt
---

## Why Ingested

이미 위키에 있는 [[wiki/implants/mbl/yadav-2025-finite-element-analysis-platform-switching]]가 본문에서 "Sahabi et al."로 직접 인용하는 원 논문 — 골(bone) 응력은 낮추고 임플란트-지대주 계면(implant-abutment interface) 응력은 높인다는 동일한 trade-off를 10여 년 앞서, 서로 다른 두 임플란트 시스템(XiVE, 3i)으로 보여준 원 데이터포인트라 인제스트.

## Three-line Summary

In vitro 3D finite element analysis (FEA) study comparing platform-switching (PS) vs conventional (matched-diameter) abutment configurations in two implant systems — XiVE S Plus (DENTSPLY Friadent) and 3i Certain (Biomet 3i) — under 100N axial and 100N/15° oblique loading in a mandibular first molar model.

In both implant systems, PS models showed lower maximum von Mises stress in crestal cortical and cancellous bone than matched (conventional) models, but higher stress concentration at the implant-abutment interface (IAI), with the high-stress zone shifting from the implant shoulder periphery toward the implant's center under PS.

PS reduced bone stress more than simply widening the implant platform did, but the paper notes the elevated IAI stress remained below titanium/Co-Cr yield strength, so it may not translate to immediate mechanical failure — though this was not tested directly.

## 세줄요약

XiVE S Plus(DENTSPLY Friadent)와 3i Certain(Biomet 3i) 두 임플란트 시스템을 대상으로, 플랫폼 스위칭(Platform Switching, PS) vs 매칭형 지대주(conventional, matched abutment) 구성을 하악 제1대구치 모델에서 100N 축방향(axial) 및 100N/15° 사방향(oblique) 하중으로 비교한 in vitro 3차원 유한요소분석(Finite Element Analysis, FEA) 연구.

두 임플란트 시스템 모두에서 PS 모델은 치조정 피질골(cortical bone)·해면골(cancellous bone)의 최대 von Mises 응력이 conventional 모델보다 낮았으나, 임플란트-지대주 계면(Implant-Abutment Interface, IAI)의 응력은 오히려 높았고, 고응력 부위가 임플란트 숄더 주변부에서 중심부 쪽으로 이동했다.

PS는 단순히 임플란트 직경을 넓히는 것(wide platform)보다도 골 응력 감소 효과가 컸으나, 상승한 IAI 응력은 티타늄·Co-Cr 합금의 항복강도보다 낮아 즉각적 기계적 파단으로 이어지지는 않을 것으로 저자들은 추정(직접 검증되지는 않음).

## 1. Document Information

- **Journal**: Journal of Dentistry (Tehran, Iran), 2013;10(4):338-50
- **PMID**: 24396353
- **PMCID**: PMC3875508
- **DOI**: not found in PubMed metadata

## 2. Key Contributions

- One of the earlier FEA studies to directly compare platform switching (PS) against conventional matched-abutment designs across **two different commercial implant systems** (XiVE S Plus, 3i Certain) in the same study, rather than a single system.
- Isolates PS's effect from implant-diameter effect by including a third "wide platform" conventional arm (matched abutment on the larger-diameter implant) alongside the regular-platform conventional arm and the PS arm — showing PS reduced stress more than diameter widening alone.
- Reports stress at the implant-abutment interface (IAI) specifically, not just the surrounding bone — documenting that the high-stress zone shifts from the implant shoulder periphery (conventional models) toward the implant's center (PS models).
- Provides an early, frequently-cited data point (per its citation in [[wiki/implants/mbl/yadav-2025-finite-element-analysis-platform-switching]]) for the now well-established "PS lowers bone stress but raises component-side stress" trade-off.

## 3. Methodology and Architecture

- **Design**: In vitro 3D FEA study, mandibular first molar site, edentulous mandible CT-derived geometry (2.0mm slice interval), mandible ~8.5mm buccolingual width × 24mm inferosuperior height.
- **Implant systems / six models**:
  - XiVE-a: 3.8×11mm implant + 3.8mm Esthetic Base abutment (conventional, regular platform)
  - XiVE-b: 4.5×11mm implant + 3.8mm Esthetic Base abutment (**platform-switching**)
  - XiVE-c: 4.5×11mm implant + 4.5mm Esthetic Base abutment (conventional, wide platform)
  - 3i-a: 4.0×11.5mm implant + 4.1mm Certain abutment (conventional, regular platform)
  - 3i-b: 5.0×11.5mm implant + 4.1mm Certain abutment (**platform-switching**)
  - 3i-c: 5.0×11.5mm implant + 5.0mm Certain abutment (conventional, wide platform)
- **Digitizing/modeling**: implants and abutments digitized with ATOS II optical digitizing system (GOM); solid models built in SolidWorks 2008; FE analysis run in ABAQUS V6.7-1 (Simulia).
- **Mesh**: four-node tetrahedral solid elements, 90,765–102,795 nodes and 457,151–519,456 contact elements across the six models.
- **Material properties**: implants and bone modeled as isotropic, homogeneous, linearly elastic (properties taken from prior literature; specific values not itemized in the extracted text).
- **Interface conditions**: 100% osseointegration assumed at bone-implant interface; abutment-implant interface fully bonded, no relative movement.
- **Boundary conditions**: mesial and distal surfaces of the mandibular bone block fixed in all directions.
- **Loading**: linear static analysis, 100N load applied to the top-center of the abutments, either **axial** or **oblique** (15° buccolingual inclination to the alveolar long axis).
- **Outcomes**: von Mises stress in crestal bone (cortical + cancellous) and at the implant-abutment interface; maximum/minimum principal stress (tensile/compressive) at crestal bone also reported.

## 4. Key Results and Benchmarks

- Stress distribution pattern was similar under axial and oblique loading in both implant systems, but **oblique loads produced consistently higher stress than axial loads**.
- In all six models under both loading conditions, **cortical bone stress exceeded cancellous bone stress**.
- Under 100N oblique load, maximum von Mises stress in cortical bone ranged from **15.06 MPa (XiVE-b, PS)** to **32.11 MPa (3i-a, conventional regular platform)**; maximum von Mises stress in cancellous bone ranged from **2.49 MPa (3i-b, PS)** to **6.28 MPa (XiVE-a, conventional regular platform)**.
- **Platform switching reduced von Mises stress at the crestal bone in both implant systems**, for both loading conditions, and for both principal-stress measures (tensile and compressive were both lower in PS models than conventional models).
- Wide-platform conventional models (XiVE-c, 3i-c) showed lower bone stress than regular-platform conventional models (XiVE-a, 3i-a) — but **PS models still showed lower bone stress than the wide-platform conventional models**, i.e., PS outperformed simple diameter-widening as a stress-reduction strategy.
- At the implant-abutment interface (IAI), the high-stress zone was located at the periphery of the implant's uppermost surface in conventional models, but **shifted toward the center of the implant in PS models**; **PS increased IAI stress values in both implant systems and both loading conditions**.
- Discussion notes the elevated IAI stress values remained below reported yield strengths of titanium alloy (620–725 MPa) and Co-Cr alloy (552–1,034 MPa), so PS-related stress increases may not cause immediate mechanical failure — though this was not directly tested (no fatigue/cyclic loading analysis).

## 5. Limitations and Future Work

- In vitro/computational FEA — isotropic, homogeneous, linearly elastic material assumptions; 100% bone-implant contact assumed (in vivo contact is typically 30–70%), so results represent an idealized average clinical scenario.
- Static loading only (single 100N axial or oblique load) — no fatigue, cyclic loading, or long-term analysis.
- Single anatomic site modeled (mandibular first molar); results may not generalize to other jaw regions or bone densities.
- Authors explicitly caution that FEA models "do not identically reproduce all clinical situations" and results should be interpreted "with sound clinical judgment."
- Extracted full text (PubMed/PMC) does not retain the paper's stress-value tables/figures for axial loading or the numeric material-property table — only oblique-load stress ranges and qualitative axial-vs-oblique comparisons survived text extraction; specific axial MPa values were not recoverable from this source and are not stated in this summary.

## 6. Related Work

- [[wiki/implants/mbl/yadav-2025-finite-element-analysis-platform-switching]] — cites this paper directly as "Sahabi et al."; replicates the same bone-stress-down/component-stress-up trade-off a decade later, in different bone density contexts (D2/D3) and implant system (Adin Internal-Hex), extending this paper's two-implant-system comparison to a bone-density/loading-direction factorial design.
- [[wiki/implants/mbl/schwarz-2013-implant-abutment-connection-platform-switching]] — same-year literature on implant-abutment connection and platform switching; complements this paper's IAI-stress findings.
- [[wiki/implants/mbl/salimi-2011-platform-switching-current-results]] — narrative review of platform-switching evidence current to the same period; useful for situating this FEA study's findings against contemporaneous clinical literature.

## 7. Glossary

- **Von Mises stress**: scalar stress measure combining all stress-tensor components, used in FEA to predict yielding/failure risk under complex 3D loading.
- **Platform Switching (PS)**: use of an abutment narrower than the implant's coronal platform diameter, moving the implant-abutment junction (IAJ) inward and away from the crestal bone.
- **Implant-Abutment Interface (IAI) / Junction (IAJ)**: the mechanical connection point between implant and abutment; a common site of stress concentration and, clinically, of the "microgap" implicated in crestal bone remodeling.
- **Principal stress (maximum/minimum)**: the maximum (most tensile) and minimum (most compressive) normal stresses at a point, used alongside von Mises stress to characterize tension vs. compression in bone.
- **Wide-platform implant**: an implant with a larger-diameter coronal platform, using a matched (non-switched) abutment of the same wide diameter — distinct from platform switching, which narrows the abutment relative to a given implant diameter.
