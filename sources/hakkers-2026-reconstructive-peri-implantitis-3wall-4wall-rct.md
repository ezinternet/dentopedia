---
title: "Surgical Reconstructive Peri-Implantitis Treatment for 3- and 4-Wall Bone Defects: A Single-Blind Randomised Controlled Trial With a 1-Year Follow-Up"
authors: Hakkers J, Meijer HJA, Glas B, de Waal YCM, Raghoebar GM
year: 2026
doi: 10.1111/jcpe.70123
category: [implants/peri-implantitis]
source_collection: pubmed-text
full_text: true
pmid: "41992493"
pmcid: "PMC13167631"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13167631/
text_path: /Users/oracleneo/llm-wiki/papers/hakkers-2026-reconstructive-peri-implantitis-3wall-4wall-rct.txt
text_filename: hakkers-2026-reconstructive-peri-implantitis-3wall-4wall-rct.txt
---

## Why Ingested

Fills the gap in head-to-head RCT evidence for reconstructive vs access-flap surgery specifically stratified by 3-wall vs 4-wall defect morphology in peri-implantitis — the key clinical decision split that existing NMA data from [[implants/peri-implantitis/ramanauskaite-2023-guided-bone-regeneration-periimplantitis-defects-nma]] does not resolve at defect-type level. This trial (Groningen, 2020–2025) adds defect-morphology subgroup data confirming radiographic MBL benefit of reconstruction while finding no difference in composite disease resolution.

## One-line Summary

Single-blind RCT (n=52 patients, 63 implants, 1-year follow-up) found reconstructive peri-implantitis surgery (autogenous bone + Bio-Oss + Bio-Gide) vs open-flap debridement improved radiographic marginal bone levels (β = −1.65 mm at T12; p<0.001) and reduced mid-buccal recession (β = −1.68 mm; p<0.001), but showed no difference in PPD, BoP, SoP, or composite disease resolution.

## 한줄요약

단일맹검 무작위대조시험 (n=52명, 63개 임플란트, 1년 추적): 재건적 임플란트주위염 수술 (자가골 + Bio-Oss + Bio-Gide)은 개방소파술 대비 방사선학적 변연골 수준 (Marginal Bone Level, MBL) 개선 (β = −1.65 mm; p<0.001) 및 협측 퇴축 감소 (β = −1.68 mm; p<0.001)에서 유의한 이점을 보였으나, 치주낭 깊이 (Probing Pocket Depth, PPD), 탐침 시 출혈 (Bleeding on Probing, BoP), 화농 (Suppuration on Probing, SoP), 복합 질환 해소율에는 유의한 차이가 없었다.

## 1. Document Information

- **Journal**: Journal of Clinical Periodontology (JCPE)
- **Publication year**: 2026
- **DOI**: [10.1111/jcpe.70123](https://doi.org/10.1111/jcpe.70123)
- **Study type**: Single-blind, parallel-group RCT (1:1 allocation)
- **Study period**: January 2020 – January 2025 (enrollment Jan 2020–Aug 2023; last follow-up Jan 2025)
- **Institution**: Department of Oral and Maxillofacial Surgery, University Medical Center Groningen, Netherlands
- **Ethics**: METc UMCG 2019/625 (approved 20 Feb 2020); registered NL-OMON27505
- **Funding**: Department of Oral and Maxillofacial Surgery, UMCG (institutional — no industry)
- **Conflicts of interest**: None declared

## 2. Key Contributions

1. First RCT to explicitly stratify 3-wall vs 4-wall peri-implant defects in a surgical reconstruction trial, with post hoc subgroup analyses by defect morphology.
2. Confirms radiographic MBL benefit of reconstruction (−1.65 mm at 1 year) and soft-tissue recession reduction (−1.68 mm) — consistent with Renvert et al. findings.
3. Demonstrates the paradox: radiographic improvement without improvement in composite disease resolution, PPD, or BoP — challenges whether radiographic fill reflects true re-osseointegration.
4. Reports significantly higher adverse events in reconstruction group (pain, dryness, metal taste, headache), informing the benefit-burden trade-off.
5. Uses multilevel mixed-effects models appropriate for clustered hierarchical data (implants within patients).

## 3. Methodology and Architecture

**Design**: Two-arm, parallel RCT (1:1), single-blind (assessor-blinded — investigator J.H. blinded to allocation).

**Sample**: 123 screened → 52 enrolled (27 test, 25 control). ITT analysis. One patient per group discontinued (implant removed).

**Inclusion criteria**:
- Peri-implantitis per 2017 World Workshop criteria (BoP/SoP + increased PPD + bone loss > crestal remodeling; or PPD ≥ 6 mm + bone ≥ 3 mm apical to implant shoulder if no baseline data)
- Failed to resolve with non-surgical submarginal instrumentation (NSI)
- 3- or 4-wall bone defect confirmed intraoperatively

**Exclusion criteria (pre-NSI)**: Medical contraindications, head/neck radiotherapy, pregnancy, uncontrolled diabetes (HbA1c threshold), IV bisphosphonates, chlorhexidine/amoxicillin/metronidazole allergy, long-term anti-inflammatory use, bone loss >2/3 implant length, prior surgical peri-implantitis treatment, chronic respiratory disease.

**Interventions**:
- Pre-op: Single NSI session — air-polishing (Airflow Master Piezon, EMS) + erythritol powder with 0.3% CHX
- Surgery: Intra-sulcular incision, full-thickness flap elevation, granulation tissue removal (titanium curettes), air-polisher decontamination, 35% phosphoric acid gel (1 min), rinse
- Test: Autogenous bone (SafeScraper TWIST, Geistlich) + Bio-Oss (1:1 mix) + Bio-Gide membrane (Geistlich)
- Control: Open-flap debridement only (protocol deviation: changed from registered resective procedure)
- Post-op: CHX + CPC mouthwash ×2 wks; amoxicillin 500 mg TID ×1 wk

**Randomisation**: Fixed block size of 4; sealed coded envelopes opened intraoperatively by assistant.

**Primary outcomes**: Mean PPD (mm), MBL (mm) — note: BoP was original primary, changed post-initiation.

**Secondary outcomes**: BoP (%), disease resolution (composite: PPD ≤5 mm + BoP ≤1/6 sites + no SoP), SoP (%), plaque score, mid-buccal recession, mid-buccal KM width, full-mouth periodontal parameters.

**Statistics**: Linear and logistic mixed-effects models (lme4, R 4.4.3); random intercepts for patients (implants nested); LOCF for missing data; post hoc defect-type subgroup analyses (exploratory).

## 4. Key Results and Benchmarks

### Radiographic MBL (primary — between-group, mixed-effects model)

| Timepoint | β (95% CI) | p |
|-----------|------------|---|
| T3 (3 mo) | −0.85 mm (−1.66 to −0.05) | 0.04 |
| T6 (6 mo) | −1.12 mm (−1.93 to −0.31) | 0.01 |
| T9 (9 mo) | −1.39 mm (−2.23 to −0.55) | <0.001 |
| T12 (12 mo) | −1.65 mm (−2.54 to −0.77) | <0.001 |

*Negative β = test group had higher (better) MBL than control.*

### Mid-buccal Recession (secondary)

| Timepoint | β (95% CI) | p |
|-----------|------------|---|
| T3 | −1.06 mm (−1.87 to −0.24) | 0.01 |
| T6 | −1.26 mm (−2.08 to −0.45) | <0.001 |
| T9 | −1.47 mm (−2.31 to −0.64) | <0.001 |
| T12 | −1.68 mm (−2.57 to −0.80) | <0.001 |

*Negative β = less recession in test group.*

### No Significant Between-Group Differences

| Parameter | β | p |
|-----------|---|---|
| PPD | −0.27 mm | 0.32 (all timepoints) |
| BoP | −7.49% | 0.21 (all timepoints) |
| Disease resolution | OR −0.14 | 0.96 |
| SoP | −4.16% | 0.15 |
| Midbuc KM | −0.55 mm | 0.27 |

### Disease Resolution at T12

- Test: 43.8% patients meeting composite criterion
- Control: 44.4% patients meeting composite criterion

### Subgroup Findings — 3-wall vs 4-wall defects (exploratory, post hoc)

**3-walled defects**:
- Test MBL significantly higher vs control at T3 (2.2 vs 4.6 mm; p=0.03) and T6 (2.4 vs 4.3 mm; p=0.01)
- Treatment success at T6: test 58.3% vs control 16.7% (p=0.045)

**4-walled defects**:
- MBL significantly higher in test at T12 (2.5 vs 3.0 mm; p=0.04)

### Adverse Events

Reconstruction group had significantly more: pain (p=0.03), mouth dryness (p=0.01), metal taste (p=0.03), headache (p=0.04).

### Descriptive Outcomes at T12

| Parameter | Test T0 → T12 | Control T0 → T12 |
|-----------|---------------|-----------------|
| PPD (mm) | 5.7 → 3.3 | 6.0 → 3.5 |
| MBL (mm from reference) | −4.3 → −2.3 | −4.0 → −3.2 |
| BoP implant-level (%) | 100% → 87.9% | 96.6% → 88.9% |
| SoP implant-level (%) | 58.8% → 15.2% | 72.4% → 18.5% |

## 5. Limitations and Future Work

1. **Mixed dentate/edentulous population** — different oral microbiota may confound outcomes
2. **1-year follow-up too short** — ≥3 years recommended for long-term stability/recurrence assessment
3. **Intraoperative randomisation** — defect configuration confirmed intraoperatively; prior to this, patients could not know their assignment, but this limits pre-surgical planning equality
4. **Protocol deviation**: Control changed from resective to open-flap debridement (changes comparability with registered protocol)
5. **Detection bias risk**: Radiopaque xenograft visible on radiographs may bias radiographic assessor despite blinding procedures
6. **No validated PRO instruments** (OHIP-14 not used) — patient-centered outcomes unknown
7. **Decontamination protocol**: Air-polisher + phosphoric acid not fully aligned with current EFP guidelines
8. **Early T3 reassessment** may miss complete tissue maturation

**Future directions**: 3-year follow-up to assess long-term stability; histological analysis to confirm re-osseointegration; validated PRO measures; standardized decontamination protocols.

## 6. Related Work

- **Renvert et al.**: RCT showing greater radiographic defect fill with reconstruction at 1 year and higher disease resolution at 3 years — consistent with present findings on radiographic outcomes
- **Heitz-Mayfield et al.**: RCT (xenograft + membrane + systemic antimicrobials vs access flap) — found no between-group difference — partial conflict
- **Derks et al.**: Multi-center RCT (n=138 patients, 147 implants) — disease resolution 16.4% (test) vs 13.5% (control) — much lower rates than present study (43–44%)
- **Monje et al.**: Disease resolution 75.1% (augmentation + membrane) vs 79.2% (augmentation alone) — different composite definition
- **Tomasi et al.**: SR finding weighted mean difference of 0.7 mm recession favoring reconstruction — supports present recession data
- **Ramanauskaite et al.**: NMA of GBR for peri-implantitis defects — provides evidence ranking context

## 7. Glossary

- **PPD (Probing Pocket Depth, 탐침 깊이)**: Distance from gingival margin to pocket base
- **MBL (Marginal Bone Level, 변연골 수준)**: Radiographic distance from implant reference to bone crest
- **BoP (Bleeding on Probing, 탐침 시 출혈)**: Bleeding elicited by gentle probing — marker of active inflammation
- **SoP (Suppuration on Probing, 탐침 시 화농)**: Pus on probing — marker of severe inflammation
- **KM (Keratinized Mucosa, 각화점막)**: Width of attached/keratinized tissue around implant
- **Midbuc REC (Mid-buccal Recession, 협측 퇴축)**: Distance from reference point to gingival margin at mid-buccal site
- **Bio-Oss (탈단백 우골 무기질, DBBM)**: Deproteinised bovine bone mineral; most documented xenograft
- **Bio-Gide (콜라겐 차폐막)**: Resorbable bilayer collagen membrane by Geistlich
- **NSI (Non-Surgical Instrumentation, 비수술적 기구조작)**: Mechanical debridement without flap surgery
- **ITT (Intention-To-Treat, 치료의향 분석)**: Includes all randomized patients regardless of protocol adherence
- **LOCF (Last Observation Carried Forward, 마지막 관측값 이입)**: Missing data imputation method
- **3-wall defect (3면 골결손)**: Peri-implant defect bounded by 3 bony walls — generally more favorable for regeneration
- **4-wall defect (4면 골결손 / 분화구형 결손)**: Circumferential defect bounded by 4 bony walls — "crater" morphology
