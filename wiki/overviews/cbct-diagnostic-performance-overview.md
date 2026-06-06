---
title: "CBCT 진단 성능 및 임상 적용 지침 종합"
authors: Synthesis (Damian Lee)
year: 2026
date: 2026-06-06
doi: N/A
source: N/A
category: overviews
confidence: synthesis
pdf_path: N/A
pdf_filename: N/A
source_collection: internal
tags: [CBCT, diagnostic-performance, sensitivity, specificity, endodontics, implant, treatment-planning, FOV, voxel, dose, radiology, clinical-indication]
---

## One-line Summary
Synthesis of 25 radiology papers: CBCT changes endodontic treatment plans in 24–56% of cases, achieves 78% sensitivity/79% specificity for root resorption, effective dose spans 2–200× panoramic equivalents — indication-specific FOV/voxel selection is the critical optimization lever.

## 한줄요약
방사선학 25편 종합: CBCT가 근관치료 계획을 24–56% 변경, 외흡수 민감도 78%·특이도 79%, 유효선량 파노라마 2–200배 — 적응증별 FOV·복셀 선택이 핵심 최적화 레버.

## Summary

CBCT (cone-beam computed tomography, 콘빔 전산화단층촬영) is the dominant 3D imaging modality in dentistry. The core clinical tension is between diagnostic gain and radiation burden. This overview synthesizes the diagnostic performance evidence (what CBCT actually detects and changes), the clinical indication framework (when CBCT is justified), and the critical technical parameters (FOV, voxel size, kVp/mA selection) that determine both dose and image quality.

Radiation dose optimization is covered separately in [[overviews/dental-imaging-radiation-dose-optimization-overview]]. This overview focuses on diagnostic utility and clinical indication.

---

## Diagnostic Performance by Application

### 1. External Root Resorption (ERR) — Baena 2022 (SR+MA, 17 studies)

| Metric | Pooled value | Range |
|---|---|---|
| Sensitivity | 78.1% | 42–98% |
| Specificity | 79.3% | 49–96% |
| Effective dose | 34–1073 µSv | — |

Interpretation: CBCT reliably detects most ERR cases but false negatives occur (~22%) particularly in early/small lesions. The wide dose range (34–1073 µSv) across units means device choice matters as much as FOV selection. [근거강함]

### 2. Endodontic Treatment Planning — Tay 2022 (SR, 16 studies)

- **CBCT changed treatment plans in 24–56% of cases** vs periapical radiography
- Direction of change: predominantly prescribing additional intervention (endodontic treatment, extractions)
- Greatest impact: high-difficulty cases (retreatment, suspected vertical root fracture, complex anatomy)

Clinical implication: CBCT is not a routine diagnostic for every endodontic case; highest yield in high-difficulty and retreatment cases. [합의수준]

### 3. Endodontic Treatment Outcome Assessment — Brochado-Martins 2025 (SR+MA, 19 studies)

- CBCT-assessed periapical healing: **87% (loose criteria) vs 36% (strict criteria)**
- Under strict CBCT criteria, success rates appear substantially lower than periapical radiograph assessment
- Conclusion: **routine CBCT for treatment outcome follow-up may be unnecessary** and overcounts apparent failures due to strict criteria [합의수준]

This has two clinical implications:
1. Do not use CBCT routinely to evaluate endodontic healing — periapical radiograph sufficient for most follow-up
2. If CBCT is used for outcome, interpret with awareness of the strict-criteria underestimation

### 4. Implant Dentistry — Jacobs 2018 (narrative review)

Justified CBCT applications in oral implantology:
- Presurgical diagnosis (bone volume, density, anatomical limits)
- Preoperative planning (virtual implant placement)
- Peroperative transfer (surgical guides, navigation, 3D printing)

Dose quantification: effective dose = approximately **2–200× panoramic radiograph equivalents** even for similar indications, depending on unit and protocol. Segmentation/linear accuracy: ~200 µm achievable but up to 5× worse with motion or metal artefacts. [합의수준]

---

## Specialty-Specific Indication Framework

**Fontenele 2025 (87 CBCT units, 34 manufacturers, 11 countries):**

Decision-support charts by specialty (FOV and voxel selection):

| Specialty | Recommended FOV | Voxel priority |
|---|---|---|
| Implant/prosthodontics | Large (full arch) | 0.2–0.4 mm |
| Periodontology | Medium (jaw segment) | 0.2–0.3 mm |
| OMFS | Large | 0.2–0.4 mm |
| Endodontics | Small (single tooth) | 0.076–0.2 mm |
| Paediatric/orthodontics | Medium–large | 0.2–0.4 mm |

Device parameter spread (11 countries, 87 units): tube voltage 50–120 kV, current 1–17 mA, DAP 10–5600 mGy·cm², effective dose ~3–500 µSv. This spread underscores that unit and protocol selection — not just anatomical indication — determines actual patient dose. [합의수준]

---

## Eye Lens and Scattered Dose

**Khafaji 2023 (SR, 5 phantom studies):**
- Scattered dose to eye lens from dental CBCT: **0.103–8.3 mSv**
- Varies with FOV size, exposure parameters, dosimeter type, and scanner model
- Threshold for lens opacity: ~0.5 Gy (cumulative); single dental CBCT exposures are below threshold but occupational/repeated exposure warrants awareness
- Recommendation: dose reference levels and optimization protocols needed for eye dose [합의수준]

---

## Emerging Alternative: Low-Field MRI

**Willershausen 2025 (prospective, 16 children, 0.55 T MRI):**
- Radiation-free 0.55 T MRI matched ultra-low-dose CT (ULD-CT) image quality for: tooth axis, root morphology, root resorption assessment, cyst detection
- Did NOT match CT for all structures (bone cortical details, calcified structures)
- Potential role: pediatric patients where radiation concern is highest [in-vivo, small n]

Clinical note: MRI for dental use is not yet standard practice; 0.55 T findings are early-stage evidence. Useful for cases where radiation is contraindicated or in children with multiple imaging needs.

---

## Panoramic Ghost Image Artifacts

**Kim 2024 (case report):**
Earrings produced three overlapping image types: real image, typical ghost image, AND pseudo-ghost image (ghost-like real image created when rotation center extends beyond the jaw). Understanding this trifecta prevents misidentification of metallic artifacts as pathology. [case-report]

---

## CBCT Justification Principle

The ALADA**I**P (As Low As Diagnostically Acceptable, being Indicative to Preference) principle applies:
1. Is 2D imaging sufficient for the clinical question? If yes → use 2D
2. If 3D is necessary → select the smallest FOV and largest voxel size that answer the diagnostic question
3. Document clinical justification before acquisition

---

## Summary Decision Map

```
Clinical question → CBCT justified?

Periapical pathosis, routine follow-up → No (periapical radiograph sufficient)
Suspected ERR, unclear on 2D → Yes (sensitivity 78%, specificity 79%)
Endodontic treatment planning, high-difficulty/retreatment → Yes (changes plans 24–56%)
Endodontic outcome assessment → Preferably No (strict criteria underestimates healing)
Implant planning (bone volume/density) → Yes (presurgical)
Implant intraoperative guide transfer → Yes (peroperative)
Pediatric, multiple imaging needs, radiation concern → Consider 0.55T MRI (emerging)
```

---

## Related Pages

- [[overviews/dental-imaging-radiation-dose-optimization-overview]] — radiation dose, ALARA/ALADAIP, panoramic dose, shielding
- [[radiology/baena-2022-cbct-diagnostic-performance-root-resorption]] — ERR diagnostic accuracy SR+MA
- [[radiology/tay-2022-influence-cbct-endodontic-treatment-planning]] — treatment plan change SR
- [[radiology/brochado-martins-2025-cbct-outcomes-endodontic-treatment-retreatment]] — outcome assessment SR+MA
- [[radiology/jacobs-2018-cbct-implant-dentistry-recommendations-clinical]] — implant CBCT justification
- [[radiology/fontenele-2025-cbct-dentistry-clinical-recommendations-indication]] — specialty FOV/voxel charts
- [[radiology/khafaji-2023-scattered-dose-eye-dentistry-cbct]] — eye lens dose
- [[radiology/willershausen-2025-low-field-mri-pediatric-dental]] — MRI alternative
- [[radiology/kim-2024-real-ghost-pseudo-ghost-images-panoramic]] — panoramic artifacts
