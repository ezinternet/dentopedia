---
title: "MRI basics for radiation oncologists"
authors: van der Heide UA, Frantzen-Steneker M, Astreinidou E, Nowee ME, van Houdt PJ
year: 2019
doi: 10.1016/j.ctro.2019.04.008
category: radiology/mri
pdf_path: /Users/oracleneo/llm-wiki/papers/van-der-heide-2019-mri-basics-for-radiation-oncologists.pdf
pdf_filename: van-der-heide-2019-mri-basics-for-radiation-oncologists.pdf
source_collection: external
---

## Why Ingested
Foundation primer for the new dental-MRI category (`radiology/mri`): it supplies the physics/vocabulary (T1/T2 contrast, gradient non-linearity, water-fat shift, artifact classes, safety) that the wiki's other dental-MRI pages assume without explaining. Defines the quantitative geometric-fidelity thresholds (<2 mm, <1 mm stereotactic) that any clinical MRI-use decision — including dental/head-and-neck — should be checked against, and extends [[wiki/radiology/willershausen-2025-low-field-mri-pediatric-dental]] and [[wiki/radiology/dewake-2023-mri-occlusal-trauma-pdl]] by giving the physical basis behind why sequence choice and scanner fidelity matter.

## Three-line Summary
(Line 1: Narrative review (Clin Transl Radiat Oncol 18:74–79, 2019), Netherlands Cancer Institute — a didactic primer on using MRI in radiotherapy planning, written for clinicians, not a data study.)
(Line 2: Core didactic content: T1/T2-weighted contrast theory; gradient non-linearity distortions grow up to ~1 cm toward scanner edges; accurate RT sequences require geometric distortion <2 mm (stereotactic <1 mm); water-fat shift is 3.4 ppm (0.5–2 pixels, pixel 0.5–1.0 mm); metal artifacts worsen at 3 T vs 1.5 T; diagnostic images are generally not geometrically trustworthy for RT.)
(Line 3: Implication: MR images must be acquired with RT-dedicated protocols in treatment position (flexible coils around masks), verified for geometric fidelity; diagnostic-department scans should not be used for contouring without verification.)

## 세줄요약
(줄1: 서사적 리뷰(Clin Transl Radiat Oncol 18:74–79, 2019, 네덜란드암연구소) — 방사선종양 치료계획에서 MRI 사용을 위한 임상가용 기본 교재. 데이터 연구는 아님.)
(줄2: 핵심 교재 내용: T1/T2 강조 대조도 이론; 경사자계 비선형성 왜곡은 스캐너 가장자리에서 최대 약 1 cm; 방사선치료용 정확 시퀀스는 기하 왜곡 <2 mm(정위 <1 mm) 요구; 지방-물 화학적 이동(water-fat shift) 3.4 ppm(0.5–2 픽셀, 픽셀 0.5–1.0 mm); 금속 인공물은 1.5 T보다 3 T에서 악화; 진단용 영상은 일반적으로 RT용 기하학적으로 신뢰 불가.)
(줄3: 임상적 함의: MR 영상은 치료 자세(마스크 주위 유연 코일)에서 RT 전용 프로토콜로 획득하고 기하 충실도를 검증해야 하며, 진단과 획득 영상은 검증 전에 윤곽묘사(contouring)에 쓰면 안 됨.)

## 1. Document Information
- **Journal**: Clinical and Translational Radiation Oncology 2019;18:74–79
- **DOI**: 10.1016/j.ctro.2019.04.008
- **Institution**: Department of Radiation Oncology, The Netherlands Cancer Institute (Amsterdam) & Leiden University Medical Center, the Netherlands
- **Access**: Open access, CC BY-NC-ND, published by Elsevier on behalf of ESTRO. Received 22 March 2019, accepted 9 April 2019, available online 13 April 2019.

## 2. Key Contributions
- Identifies, for clinical readers, which aspects of MRI matter when MR images are interpreted for radiotherapy — contrast selection, geometrical fidelity, artifacts, safety — and why diagnostic MR scans are generally unsuitable for RT contouring without dedicated protocol verification.
- Quantifies geometric-fidelity requirements: gradient non-linearity distortions reach ~1 cm at scanner edges; RT-accurate sequences need distortion <2 mm (stereotactic <1 mm); water-fat shift is ~0.5–2 pixels (0.5–1.0 mm pixels).
- Reviews the workflow implications: MRI+CT registration vs MR-only (pseudo-CT), treatment-position scanning with flexible coils around fixation masks, and MRI for brachytherapy (cervix, prostate focal boost).

## 3. Methodology and Architecture
- **Design**: Narrative review / didactic primer (not a systematic review, no data cohort).
- **Databases**: n/a — references primary physics (e.g. Doran et al. gradient warp correction), consensus (Paulson et al., ESTRO/ISMRM), and tumor-site sequence reviews.
- **n**: n/a (review; illustrated with phantom/healthy-volunteer grid figures and one head-neck patient MRI example).
- **Outcomes**: Texture-level didactic outcomes — contrast physics, distortion sources/limits, artifact classes, safety liabilities.

## 4. Key Results and Benchmarks
- **Field strength**: diagnostic scanners use 1.5 T or 3.0 T; metal-induced distortion is larger at 3 T than 1.5 T.
- **Gradient non-linearity distortion**: minimal at iso-center; grows up to **~1 cm** toward the scanner edges (grid phantom, Fig. 2). Vendors offer software correction; most T2-weighted sequences are multi-slice 2D where only a **2D** (in-plane) correction is applied, leaving the slice plane warped off-center; 3D sequences allow full 3D correction but T2-weighted 3D contrast differs from 2D.
- **Geometric-fidelity thresholds**: accurate RT sequences require distortion **<2 mm**; stereotactic/radiosurgery applications **<1 mm** (per Paulson et al. consensus).
- **Water-fat shift**: water vs fat hydrogen resonance differs by **3.4 ppm**, shifting water/fat positions by typically **0.5–2 image pixels** (pixel size 0.5–1.0 mm). Reducing water-fat shift during sequence optimization lowers distortion but costs signal-to-noise — diagnostic images are often acquired with maximum water-fat shift, compromising RT usability. Worked example: diagnostic 3D T1 brain with 2-pixel (~1 mm²/voxel) water-fat shift showed a ~2 mm cranio-caudal shift of the ventricles relative to bone-marrow fat after registration to planning CT (Fig. 4).
- **Artifacts**: metal implants leave dark voids + surrounding warping (sequence- and susceptibility-dependent); T2-TSE is less affected than T1 gradient echo; DWI (EPI-based) is most sensitive — often unusable around metal implants. Tissue/air interfaces (rectal gas, head-neck air cavities) also distort field, strongly affecting DWI. Periodic motion → ghosting; navigator-triggered sequences freeze motion in the max-exhale phase (which may mismatch deep-inspiration breath-hold or free-breathing treatment); 4D-MRI maps multiple phases for mid-ventilation contouring.
- **Safety**: ferromagnetic attraction, pacemaker/ICD malfunction (may be MRI-conditional — cardiology verification needed), RF heating under specific absorption rate (SAR) limits, loop currents (avoid crossed limbs), implant/wire local heating, and mandating MRI-compatible fixation (glass fiber) plus screening of every patient/operator (mrisafety.com database).

## 5. Limitations and Future Work
- Targeted at radiotherapy use; does not address dental/head-and-neck intraoral or maxillofacial imaging specifics (coil design for jaws, dental-material artifacts beyond prostheses).
- Primer-level physics — refers readers to Seminars in Radiation Oncology special issues and ESTRO/ISMRM courses for complete MRI physics.
- Implicit, not tested, in a dental setting: the 2 mm / 1 mm geometric-fidelity thresholds derive from RT target delineation, not implant/endodontic measurement contexts.
- 2019 publication predates the current generation of low-field (0.55 T) dental MRI systems, whose distortion/artifact characteristics differ.

## 6. Related Work
- [[wiki/radiology/willershausen-2025-low-field-mri-pediatric-dental]]: dental application of MRI (0.55 T low-field vs ultra-low-dose CT in children) — provides the clinical contrast and the practical setting this primer's physics underpins; note 3 T vs lower-field trade-offs also recur.
- [[wiki/radiology/dewake-2023-mri-occlusal-trauma-pdl]]: dental T2-weighted MRI signal of periodontal ligament for occlusal-trauma severity — an example of the T2-contrast and sequence-choice principles this review explains.
- [[wiki/radiology/mri/vassiliou-2018-mri-physics-basics-cardiologist]] and [[wiki/radiology/mri/grover-2015-mri-principles-techniques-lessons-clinicians]]: parallel clinician-oriented MRI physics primers in the same category.
- [[wiki/radiology/mri/al-haj-husain-2025-magnetic-resonance-imaging-in-dental]]: dental MRI applications review — the dental-domain application of these fundamentals.
- Paulson et al. 2016 consensus (MRI simulation) — source of the <2 mm / <1 mm geometric-fidelity criteria quoted here.
- Nyholm & Jonsson 2014 — MR-only workflow and pseudo-CT generation review, cited for the CT-registration-free workflow.

## 7. Glossary
- **T1 / T2 relaxation**: longitudinal vs transversal decay of the MRI radio signal after an RF pulse; tissue-specific values in water vs fat determine image contrast (long-T1 water dark on T1-weighted, bright on T2-weighted).
- **Geometric fidelity**: the accuracy with which image geometry represents true anatomy; compromised by magnetic-field-gradient non-linearities, water-fat shift, and susceptibility effects.
- **Water-fat shift (chemical shift)**: the ~3.4 ppm resonance frequency difference between water and fat hydrogens that translates into a positional shift of typically 0.5–2 pixels; small shifts are desired for RT but cost signal-to-noise.
- **Gradient non-linearity correction**: vendor software correction of the imperfectly linear field gradients; can be 2D (in-plane only, standard for multi-slice 2D sequences) or 3D.
- **Echo planar imaging (EPI)**: the ultrafast acquisition underlying diffusion-weighted MRI; highly sensitive to magnetic-field (susceptibility) distortions.
- **Navigator-triggered sequence**: a fast 1D acquisition (typically across the liver dome in cranio-caudal direction) that detects the max-exhale breathing phase to gate a motion-artifact-free (but treatment-mismatched) acquisition.