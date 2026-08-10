---
title: "Rehabilitation in Cases of Maxillary Lateral Incisor Agenesis Using Zirconia Implant and Abutment: Finite Element Analysis and Systematic Review"
authors: Leonardo Folmer Rodrigues da Silva, Ivan Onone Gialain, Marina Guimarães Roscoe, Omar Melendres Ugarte, Paolo Maria Cattaneo, Josete Barbosa Cruz Meira
year: 2026
doi: 10.1111/jerd.70080
category: [prosthetic-materials]
pdf_path: /Users/oracleneo/llm-wiki/papers/dasilva-2026-maxillary-lateral-incisor-agenesis-zirconia.pdf
pdf_filename: dasilva-2026-maxillary-lateral-incisor-agenesis-zirconia.pdf
source_collection: external
---

## Why Ingested

Fills a gap noted by both [[dental-materials/zirconia/talmazov-2020-fea-one-piece-zirconia-implant-anterior]] (single-material FEA of one-piece zirconia vs titanium in the anterior maxilla) and [[prosthetic-materials/abutment-screw/sterzenbach-2025-hybrid-abutment-crowns-zirconia-titanium-implants]] (hybrid-abutment-crown material comparison): this paper is the first in the wiki to combine FEA with a matched systematic review specifically for maxillary lateral incisor agenesis (MLIA), directly comparing titanium/titanium (TT), titanium/hybrid (TH), and zirconia/zirconia (ZZ) implant-abutment configurations across narrow (3.0 mm) and standard (3.5 mm) diameters in both control and atrophic anterior maxilla geometries. It also confirms, via a 25-study systematic review, that no clinical study to date has used zirconia implants for MLIA — a gap the FEA component is designed to address in silico.

## Three-line Summary

Mixed-methods study: 3D finite element analysis (FEA) of 10 simulated implant-abutment models (control vs atrophic anterior maxilla; TT/TH/ZZ material combinations; 3.0/3.5 mm diameters) paired with a PRISMA systematic review (SR) of 25 clinical studies (2011–Dec 2024) on implant-supported crowns for maxillary lateral incisor agenesis (MLIA).

FEA: all implant/abutment configurations showed failure risk below 0.7 (below critical stress); narrower diameter and atrophic bone increased peri-implant bone strain energy density (SED), with all models except the ZZ/control combination exceeding the pathological SED threshold (109.6 μJ/mm³); SR: 19/25 studies (case reports, cohorts, RCTs) reported successful outcomes, but zero used zirconia implants clinically.

Regular-diameter (3.5 mm) titanium implants with hybrid (zirconia-over-titanium-base) abutments offered the best combined biomechanical/esthetic profile; zirconia implants, despite numerically lower FEA failure risk, remain clinically unvalidated (no long-term survival data) due to lower fracture toughness (~8 MPa·m^1/2 vs titanium's 60–86 MPa·m^1/2) and risk of subcritical crack propagation.

## 세줄요약

혼합연구방법 논문: 상악측절치 결손(MLIA) 재건을 위한 임플란트-어버트먼트 재료 조합(티타늄/티타늄, 티타늄/하이브리드, 지르코니아/지르코니아) 10개 시뮬레이션 모델을 이용한 3차원 유한요소분석(FEA)과, 2011~2024년 12월까지 25편의 임상연구를 분석한 체계적 문헌고찰(SR)을 결합.

FEA 결과 모든 임플란트-어버트먼트 조합의 파괴위험도는 0.7 미만으로 낮았으나, 좁은 직경(3.0mm)과 위축된 골에서 변형에너지밀도(SED)가 병리적 역치(109.6 μJ/mm³)를 초과; SR 결과 25편 중 19편이 성공적 결과를 보고했지만 임상에서 지르코니아 임플란트를 사용한 연구는 전무.

표준 직경(3.5mm) 티타늄 임플란트 + 하이브리드(지르코니아-티타늄베이스) 어버트먼트 조합이 생체역학적·심미적으로 가장 균형잡힌 선택지이며, 지르코니아 임플란트는 낮은 파괴인성(약 8 MPa·m^1/2, 티타늄 60–86 MPa·m^1/2)으로 인한 미세균열 전파 위험 때문에 장기 임상 데이터 부재로 아직 검증되지 않음.

## 1. Document Information

- **Title**: Rehabilitation in Cases of Maxillary Lateral Incisor Agenesis Using Zirconia Implant and Abutment: Finite Element Analysis and Systematic Review
- **Authors**: Leonardo Folmer Rodrigues da Silva, Ivan Onone Gialain, Marina Guimarães Roscoe, Omar Melendres Ugarte, Paolo Maria Cattaneo, Josete Barbosa Cruz Meira
- **Journal**: Journal of Esthetic and Restorative Dentistry, 2026; 38:855–873
- **DOI**: 10.1111/jerd.70080
- **Received**: 15 June 2025 | Revised: 26 September 2025 | Accepted: 9 December 2025
- **Study type**: Mixed methods — finite element analysis (in-vitro/computational) + systematic review (clinical studies)
- **Open access**: Yes (Creative Commons Attribution License)

## 2. Key Contributions

- First study to combine FEA and a matched systematic review to specifically evaluate the biomechanical AND clinical viability of zirconia (as well as titanium and hybrid) implant-abutment systems for MLIA rehabilitation.
- Directly compares three implant-abutment material configurations (TT, TH, ZZ) across two implant diameters (3.0/3.5 mm, except ZZ only at 3.5 mm — the narrowest commercially available screw-retained zirconia implant) and two bone conditions (control vs atrophic maxilla modeled after MLIA anatomy).
- Introduces/uses the Peri-Implant Bone Resorption Risk Index (PIBRri), converting Frost's Mechanostat pathological strain threshold (4000 μstrain) into an SED-based risk classification (low <0.8, medium 0.8–1.0, high >1.0).
- Systematic review (PRISMA, PICOS framework, Cochrane methodology) of 25 clinical studies published 2011–Dec 2024, confirming no clinical MLIA study to date has used zirconia implants — establishing the evidence gap the FEA addresses in silico.
- Explicitly tests the consistency between FEA predictions and clinical SR findings, a methodological pairing rarely done together in dental implant biomechanics literature.

## 3. Methodology and Architecture

**FEA component:**
- Two 3D anterior-maxilla models: Control (C, patient-derived CT, IRB-approved, normal bone dimensions) and Atrophic (A, modified to MLIA-characteristic reduced buccal bone thickness based on literature values).
- Software: Blue Sky Plan (segmentation) → MeshMixer → Rhinoceros 7 (geometry) → MSC.Apex (mesh/material assignment) → MSC.MarcMentat (loading/boundary conditions).
- Mesh: 730,456–757,892 elements (convergence-tested); materials modeled as linear, elastic, homogeneous, isotropic.
- Implant/abutment groups: TT (titanium implant + titanium abutment), TH (titanium implant + hybrid zirconia-over-Ti-base abutment), ZZ (zirconia implant + zirconia abutment); diameters 3.0 and 3.5 mm (ZZ only 3.5 mm); standardized 13 mm length; lithium disilicate crowns throughout. Total 10 FEA models.
- Loading: 100 N oblique load at 45°, split 50 N at two points (mesial/distal palatal margins), simulating a 2 mm overbite occlusal contact pattern per Nelson.
- Boundary conditions: proximal and superior (sinus floor) surfaces fully constrained (6 DOF); all interfaces bonded (assumes complete osseointegration).
- Failure risk formula: component maximum stress ÷ material critical stress (von Mises/yield strength for ductile titanium; maximum principal stress/ultimate tensile strength for brittle zirconia).
- Bone resorption risk formula (PIBRri): mean of 10 highest peri-implant SED values ÷ pathological SED threshold (109.6 μJ/mm³, derived from Frost's Mechanostat 4000 μstrain).

**Systematic review component:**
- Conducted per Cochrane Oral Health Group Handbook, PICOS framework (P: MLIA implant-supported crown patients; I: dental implants; C: implant/abutment materials; O: treatment success/esthetics/satisfaction; S: clinical studies).
- Databases: PubMed, Scopus, Web of Science; publications from 2011 onward; last search December 2024.
- Two independent reviewers (title/abstract screening), full-text eligibility assessment against predefined inclusion/exclusion criteria.
- PRISMA flow: 1096 records → 521 duplicates removed → 575 screened → 481 excluded (title/abstract) → 94 full-text assessed → 25 included.

## 4. Key Results and Benchmarks

**FEA results:**
- Atrophic maxilla models showed higher SED than control models; increasing implant diameter reduced SED in all groups; TT groups had higher SED than TH and ZZ groups.
- All models exceeded the pathological SED threshold (109.6 μJ/mm³) except the ZZ group in the control (non-atrophic) maxilla.
- All implant/abutment configurations had failure risk below 0.7 (well below 1.0 critical threshold) — indicating overall low mechanical failure risk under the simulated 100 N oblique load.
- ZZ group showed slightly lower numerical failure risk than TT group, but zirconia's brittle failure mode (fracture toughness ~8 MPa·m^1/2) is fundamentally more catastrophic/unpredictable than titanium's ductile yielding (fracture toughness 60.4–85.8 MPa·m^1/2).
- Zirconia abutments (TH, ZZ) concentrated stress on the palatal side only; titanium abutments (TT) concentrated stress on both buccal and palatal sides.
- At 3.5 mm diameter, zirconia abutments showed lower stress than titanium abutments; in the atrophic maxilla, zirconia implants showed higher stress than titanium implants at the same diameter.

**SR results:**
- 25 studies included: case reports (16), cohorts, RCTs/nonrandomized trials; implant diameters ranged 1.8–4.8 mm across studies.
- 19/25 studies reported successful (+) outcomes; several reported mixed (+/−) or negative (−) outcomes (e.g., abutment/component fracture, aggressive buccal bone resorption, bluish discoloration from titanium show-through).
- 20/25 studies used prior orthodontic space opening; 8/25 used bone or soft-tissue augmentation.
- Zero of the 25 clinical studies used zirconia implants (only zirconia abutments on titanium implants, or titanium implants/abutments) — confirming an evidence gap for zirconia implant survival data in MLIA.
- One study (Martinez-Rus et al. 2014) reported zirconia abutment fracture 6 weeks post-placement due to excessive angulation/thin wall thickness, successfully managed by replacement with a less-angulated design.

## 5. Limitations and Future Work

- FEA assumes fully bonded (100% osseointegrated), linear-elastic, isotropic materials and a single static oblique loading condition — does not capture cyclic/fatigue loading, osseointegration variability, or the "already-monoclinic-phase" scenario where zirconia's tetragonal-to-monoclinic tenacification mechanism becomes ineffective.
- Zero clinical (SR) data exist on zirconia implant survival in MLIA specifically, so the FEA's favorable ZZ failure-risk numbers cannot yet be clinically validated; available zirconia implant survival evidence generally is limited to ≤5-year follow-up.
- SR studies are heterogeneous in design (case reports dominate: 16/25), follow-up duration, and implant dimensions (1.8–4.8 mm), limiting quantitative pooling/meta-analysis.
- Authors explicitly call for long-term clinical studies to validate zirconia implant longevity/performance in MLIA before recommending it over titanium.
- Angled abutment considerations (increased stress, screw loosening, reliance on cement retention/peri-implantitis risk) are discussed but not directly simulated in this FEA (all simulations used straight abutments).

## 6. Related Work

- [[dental-materials/zirconia/talmazov-2020-fea-one-piece-zirconia-implant-anterior]] — earlier FEA comparing one-piece zirconia vs titanium implants in the anterior maxilla across three bone-loss geometries; this paper extends that single-material comparison into a three-way (TT/TH/ZZ) matched design with a companion systematic review.
- [[prosthetic-materials/abutment-screw/sterzenbach-2025-hybrid-abutment-crowns-zirconia-titanium-implants]] — direct clinical/prosthetic comparison of hybrid abutment crowns on zirconia vs titanium implants; complements this paper's FEA-level hybrid-abutment (TH) findings with clinical technical/esthetic/osseointegration-failure data.
- [[overviews/zirconia-implant-clinical-outcomes]] — cross-paper synthesis of zirconia implant survival/MBL trends; this SR's zero-zirconia-implant-in-MLIA finding is a notable gap relative to that broader survival literature.
- [[implants/barbosa-2021-narrow-implants-one-two-piece-fea]] — FEA of narrow/extra-narrow one- vs two-piece implants; relevant to this paper's narrow-diameter (3.0 mm) stress-distribution findings.

## 7. Glossary

- **MLIA**: Maxillary Lateral Incisor Agenesis — congenital absence of the maxillary lateral incisor, one of the most common dental agenesis conditions after third molars and mandibular second premolars.
- **FEA**: Finite Element Analysis — computational method simulating stress/strain distribution in a physical structure (here, implant-bone-abutment-crown complex) under load.
- **SED**: Strain Energy Density — a measure of mechanical energy stored per unit volume of bone under load; used as a surrogate for bone remodeling/resorption risk.
- **PIBRri**: Peri-Implant Bone Resorption Risk Index — ratio of maximum observed SED to a pathological SED threshold (109.6 μJ/mm³), classifying resorption risk as low/medium/high.
- **TT / TH / ZZ groups**: Titanium implant + titanium abutment / Titanium implant + hybrid (zirconia-over-Ti-base) abutment / Zirconia implant + zirconia abutment.
- **NDI**: Narrow-Diameter Implant.
- **YS / UTS**: Yield Strength (ductile failure criterion, used for titanium) / Ultimate Tensile Strength (brittle failure criterion, used for zirconia).
- **Ti-base**: Titanium base component onto which a custom zirconia abutment portion is bonded/milled, forming a "hybrid abutment."
