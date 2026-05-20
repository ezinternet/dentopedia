---
title: "3D-evaluation of the maxillary sinus in cone-beam computed tomography"
authors: Julia Luz, Dominique Greutmann, Daniel Wiedemeier, Claudio Rostetter, Martin Rücker, Bernd Stadlinger
year: 2018
doi: 10.1186/s40729-018-0128-4
category: digital-workflow
pdf_path: /Users/oracleneo/llm-wiki/papers/luz-2018-maxillary-sinus-3d-cbct-evaluation.pdf
pdf_filename: luz-2018-maxillary-sinus-3d-cbct-evaluation.pdf
source_collection: external
---

## One-line Summary
Retrospective CBCT study of 128 maxillary sinuses (64 patients) using the SMOP implant-planning software to quantify osseous and mucosal-bordered (pneumatized) sinus volumes; mean osseous surface area 39.7 cm², volume 17.1 cm³; 42.2% of sinuses showed obliteration, with mean obliterated volume 5.1 cm³; obliteration volume associated with pathologies; males had significantly larger osseous volume.

## 1. Document Information
- **Journal**: International Journal of Implant Dentistry, 2018; 4:17
- **Affiliation**: Clinic of Cranio-Maxillofacial and Oral Surgery, University of Zurich, Switzerland
- **Study type**: Retrospective cross-sectional CBCT analysis
- **Software**: SMOP (Swissmeda AG, Baar, Switzerland)

## 2. Key Contributions
- Demonstrates that CBCT, paired with an implant-planning software (SMOP) that allows interpolated closed-curve volumetric reconstruction, can produce **3D quantification of both osseous and mucosal-bordered (residual pneumatized) maxillary sinus volumes**.
- Establishes population-level **reference ranges** for sinus surface area and volume in a Swiss cohort.
- Introduces a method for quantifying **obliteration volume** as the arithmetic difference between osseous-bounded and mucosa-bounded volumes.
- Tests associations between sinus volumetric parameters and patient/site variables: age, sex, dentition state, apical lesions, sinus pathology, and root-sinus communication.

## 3. Methodology and Architecture
- 64 patients, 128 sinuses analyzed; CBCT scans acquired 2013 at the Department of Cranio-Maxillofacial and Oral Surgery, University of Zurich.
- Device: KaVo 3D eXam CBCT (120 kV, 5.0 mA; voxel sizes 0.125–0.4 mm; FOV 16 cm diameter, 10–13.3 cm height).
- DICOM imported into SMOP; volumes (mm³) and surfaces (mm²) computed by interpolation of parallel closed curves spaced every 2 mm in the coronal plane (15–25 curves per sinus).
- Two parallel measurements per sinus: (a) osseous-bordered volume; (b) mucosal-bordered (remaining pneumatized) volume; difference = obliteration volume.
- Recorded patient covariates: age, sex, dentition state, sinus pathologies, periapical lesions, number of teeth/roots communicating with the sinus, CBCT season (autumn-winter vs spring-summer).

## 4. Key Results and Benchmarks
- **Osseous-bordered sinus**: mean surface area 39.7 cm², mean volume 17.1 cm³.
- **Mucosal-bordered (residual pneumatized) sinus**: mean surface 36.4 cm², mean volume 15 cm³.
- **Obliteration prevalence**: 42.2% of sinuses; mean obliterated volume 5.1 cm³.
- **Pathology association**: obliterated volume associated with presence of pathologies.
- **Sex effect**: males had significantly higher mean osseous sinus volume than females.
- **No association** detected between age or dentition state and sinus volume; no association between communicating tooth roots and sinus pathologies or unilateral opacity / apical radiolucency; no significant seasonality (autumn/winter vs spring/summer) for bilateral obliteration.

## 5. Limitations and Future Work
- Single-center, single-vendor CBCT cohort; generalizability to other populations and devices unproven.
- Cross-sectional design — cannot infer trajectory of obliteration over time.
- The 2 mm coronal slice spacing for curve interpolation is a tradeoff between operator time and resolution.
- Obliteration is operationalized as radiographic mucosal swelling; histological correlation absent.
- Implant-planning software (SMOP) is proprietary; reproducibility across other DICOM viewers / segmentation engines not tested.

## 6. Related Work
- Lee 2020 — CBCT 3D evaluation of inferior maxillary sinus.
- Munakata 2021 — Factors influencing sinus membrane thickness on CBCT.
- Schriber 2019 — Sinus pneumatization after tooth loss.
- Padhye 2020 — Quantitative CBCT of edentulous posterior maxilla.

## 7. Glossary
- **CBCT (Cone-Beam Computed Tomography)**: Volumetric dental imaging modality using a cone-shaped X-ray beam; provides 3D reconstruction with limited radiation compared to medical CT.
- **DICOM**: Digital Imaging and Communications in Medicine — standard file format for radiologic image data.
- **SMOP**: Swissmeda Online Planning — proprietary implant planning software used here for 3D volumetric reconstruction of the sinus.
- **Sinus obliteration**: Radiographic reduction of the air-filled (pneumatized) sinus cavity due to mucosal swelling or pathology.
- **FOV (Field of View)**: Volume captured by the CBCT scanner; affects radiation dose and anatomical coverage.
- **Voxel**: Volumetric pixel; smaller voxel size → higher spatial resolution but higher dose / file size.
