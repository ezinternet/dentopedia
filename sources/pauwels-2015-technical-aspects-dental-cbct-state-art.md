---
title: "Technical aspects of dental CBCT: state of the art"
authors: Pauwels R, Araki K, Siewerdsen JH, Thongvigitmanee SS
year: 2015
doi: 10.1259/dmfr.20140224
category: [radiology]
pdf_path: /Users/oracleneo/llm-wiki/papers/pauwels-2015-technical-aspects-dental-cbct-state-art.pdf
pdf_filename: pauwels-2015-technical-aspects-dental-cbct-state-art.pdf
source_collection: external
---

## Why Ingested

CBCT 기기의 하드웨어·획득·재구성·화질·시각화 전 사슬을 한 권으로 설명하는 기술 총론 — 위키의 임상 적응증/선량 위주 CBCT 페이지들이 전제하는 물리·기술 근거를 보강한다. [[radiology/kaasalainen-2021-dental-cone-beam-ct-updated-review]]는 2021 의학물리 업데이트로, 이 페이지는 그 원형이 되는 2015 state-of-the-art 리뷰다.

## Three-line Summary

Narrative state-of-the-art review (Dentomaxillofac Radiol 2015) covering the entire dental CBCT imaging chain — X-ray tube/spectrum parameters, gantry types, flat-panel detector (indirect CsI/a-Si vs direct a-Se), FOV/collimation, scout-based mA modulation, FDK/ART/statistical reconstruction, stitching, grey-value calibration, geometric calibration, and image-quality metrics (spatial resolution/MTF, contrast, noise, artifacts).

Focal-spot size is a key determinant of image sharpness; CBCT noise generally exceeds diagnostic CT (higher detector electronic noise), and grey values are only semiquantitative — HU-like calibration demands care; metal artifacts and beam hardening remain major limitations.

Designed to give users and referring dentists the physical grounding to justify and optimize CBCT exposures — smaller FOV, appropriate exposure factors, and understanding of when reconstruction settings (e.g. smoothing filters) trade resolution for noise.

## 세줄요약

치과용 CBCT 전 영상사슬을 다루는 state-of-the-art 내러티브 리뷰(Dentomaxillofac Radiol 2015) — X선관·스펙트럼 파라미터, C-arm 게트리 유형, 평판검출기(간접 CsI/a-Si vs 직접 a-Se), FOV·콜리메이션, scout 기반 mA 변조, FDK/ART/통계적 재구성, 스티칭, 회색값 보정, 기하 보정, 화질 지표(공간해상도/MTF, 대조도, 노이즈, 인공물).

포컬스팟 크기가 선예도 결정 인자이고, CBCT 노이즈는 일반 진단 CT보다 높으며(검출기 전자노이즈), 회색값은 반정량적 — HU 유사 보정에 주의 필요, 금속 인공물·빔하드닝이 여전히 주요 한계.

사용자와 의뢰 치과의사가 CBCT 피폭을 정당화·최적화(작은 FOV, 적절한 노출 조건, 재구성 필터의 해상도-노이즈 trade-off 이해)할 수 있는 물리 기초를 제공.

## 1. Document Information
- **Journal**: Dentomaxillofacial Radiology 2015;44:20140224 (CBCT Special Issue)
- **DOI**: 10.1259/dmfr.20140224
- **Institution**: Chulalongkorn University (Bangkok), Showa University (Tokyo), Johns Hopkins University (Baltimore), NSTDA (Pathumthani) — international collaborative review

## 2. Key Contributions
- End-to-end description of the dental CBCT imaging chain: hardware (tube, gantry, detector) → acquisition (geometry, exposure control) → reconstruction (FDK/ART/statistical) → visualization (MPR, oblique, curved/synthetic panoramic, 3D).
- X-ray physics primer specific to CBCT: Bremsstrahlung vs characteristic spectrum, filtration (aluminium-equivalent 2.5–10 mm), kVp↔spectrum vs mAs↔photon-count/dose proportionality.
- FOV/collimation taxonomy: multiple predefined rectangular collimator openings vs free z-collimation; small-FOV vs large-FOV dose implications.
- Detector comparison: indirect (CsI scintillator + a-Si TFT) vs direct (a-Se + TFT) flat-panel detectors — fill factor, DQE, ghosting/afterglow implications.
- Reconstruction algorithm comparison: FDK (most widespread), iterative ART, statistical/statistical-IR (OSEM, penalized likelihood) — noise modelling advantage of statistical methods at low dose, not yet routine in dental CBCT.
- Grey-value semiquantitative nature + geometric calibration failure modes (systematic rotation-centre shift → double image; jitter → streaks).
- Image-quality framework: spatial resolution (MTF), contrast (large-area), noise (quantum vs electronic), artifacts (scatter, metal, beam hardening) — task-based assessment principle.

## 3. Methodology and Architecture
- **Design**: Narrative state-of-the-art review (20 pp, CBCT special issue of DMFR).
- **Scope**: X-ray tube (spectrum, filtration, focal spot), gantry (C-arm seated/standing, supine), detector, scout/auto-exposure, reconstruction (FDK/ART/statistical), stitching, grey-value calibration, geometric calibration, image quality (resolution/contrast/noise/artifacts), visualization (MPR/oblique/synthetic panoramic/3D).
- **n**: Not applicable (review; references include Birch & Marshall spectral data, Feldkamp/Davis/Kress 1984, Daly et al. calibration-artifact studies).

## 4. Key Results and Benchmarks
- Focal spot: typical CBCT ~0.5 mm; smaller focal spot → sharper images (but tube-loading limits).
- Filtration: aluminium or copper, aluminium-equivalent 2.5–10 mm; thicker filter → higher mean/effective energy, less beam hardening, lower entrance dose.
- mAs is linearly proportional to dose; kVp determines maximum photon energy (90 kV → 90 keV max) and mean energy (~60% of max).
- FDK (Feldkamp–Davis–Kress) FBP used in almost all CBCT machines — simple, fast; ART/statistical iterative methods better quality/low-dose, but large computation time → not common in dental CBCT.
- Noise in CBCT generally higher than diagnostic CT; quantum noise + electronic noise (detector signal conversion/transmission); noise-resolution trade-off managed via smoothing filter cut-off (fraction of Nyquist) — Ram-Lak (sharpest) → Hann (smoothest).
- Grey values: n-bit → 2^n possible values; CBCT values not absolute — HU-like use demands calibration (semiquantitative, task-dependent validity).
- Geometric calibration errors: systematic centre-of-rotation/piercing-ray shift → double image (360°) / crescent-moon (short orbits); random jitter → streaks hard to distinguish from noise.
- Artifacts: scatter (Compton) → shading/streaks, darkening; antiscatter grids reduce scatter but may raise dose; scatter-correction algorithms (parametrized background or Monte Carlo). Metal artifacts from high-density objects; beam hardening from low-energy photon absorption (mean energy ~60% of max kVp).
- Visualization: MPR (axial/sagittal/coronal), oblique reformation (rotated planes), synthetic curved panoramic along user-defined curve in axial plane, 3D rendering; window/level controls perceived contrast.

## 5. Limitations and Future Work
- Narrative review — no systematic literature protocol or meta-analytic synthesis.
- 2015 technology snapshot: statistical/iterative reconstruction not yet common in dental CBCT (now increasingly implemented), real-time patient-specific mA modulation not yet introduced (later partially realized).
- Quantitative imaging (HU-like values, MTF-based resolution) discussed conceptually, not measured across devices.

## 6. Related Work
- [[radiology/kaasalainen-2021-dental-cone-beam-ct-updated-review]]: 2021 Helsinki update restricted to CBCT technology/dose/DRLs — extends this 2015 state-of-the-art review along the medical-physics axis.
- [[radiology/suomalainen-2015-dentomaxillofacial-imaging-panoramic-views-cone]]: teaching-oriented companion review covering panoramic + CBCT with the same dose-ladder and artifact discussion — this page supplies the deeper physics/engineering detail.
- [[radiology/jacobs-2018-cbct-implant-dentistry-recommendations-clinical]]: clinical implant CBCT justification/optimization built on the physical principles explained here.
- [[radiology/dioguardi-2025-radiographic-artifacts-caries-diagnosis-sr-ma]]: artifact taxonomy applied to caries diagnosis — empirical counterpart to this page's artifact physics.
- [[radiology/charuakkra-2023-low-dose-cbct-image-dose-comparison]]: low-dose CBCT protocol benchmarking — practical instance of the exposure-optimization concepts (mA modulation, FOV) described here.

## 7. Glossary
- **CBCT (Cone-Beam Computed Tomography)**: 3D imaging reconstructing a voxel matrix from 2D cone-beam projections over a single gantry rotation.
- **Bremsstrahlung**: "braking radiation" — continuous X-ray spectrum produced when electrons decelerate in the anode; most photons in a diagnostic beam.
- **FOV (Field of View)**: scanned volume height/diameter defined by collimator openings; smaller FOV → lower dose.
- **FDK (Feldkamp–Davis–Kress)**: the 3D filtered-backprojection algorithm used in almost all dental CBCT systems.
- **MTF (Modulation Transfer Function)**: system's ability to transfer signal at a given spatial frequency — the standard characterization of spatial resolution.
- **DQE (Detective Quantum Efficiency)**: detector efficiency in converting X-ray photons into signal relative to noise.
- **Beam hardening**: preferential absorption of low-energy photons, shifting the beam spectrum harder — a CBCT artifact source alongside scatter and metal.