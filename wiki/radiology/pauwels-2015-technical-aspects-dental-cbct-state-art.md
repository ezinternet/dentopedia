---
title: "Technical aspects of dental CBCT: state of the art"
authors: Pauwels R, Araki K, Siewerdsen JH, Thongvigitmanee SS
year: 2015
date: 2015-01-01
doi: 10.1259/dmfr.20140224
source: pauwels-2015-technical-aspects-dental-cbct-state-art.md
category: [radiology]
evidence_level: narrative-review
pdf_path: /Users/oracleneo/llm-wiki/papers/pauwels-2015-technical-aspects-dental-cbct-state-art.pdf
pdf_filename: pauwels-2015-technical-aspects-dental-cbct-state-art.pdf
source_collection: external
tags: [cbct, cone-beam-ct, radiation-physics, image-quality, reconstruction, artifacts, mtu, focal-spot, fov, grey-values]
relations:
  - type: extends
    target: radiology/kaasalainen-2021-dental-cone-beam-ct-updated-review
  - type: extends
    target: radiology/suomalainen-2015-dentomaxillofacial-imaging-panoramic-views-cone
---

## Three-line Summary

Narrative state-of-the-art review (Dentomaxillofac Radiol 2015, CBCT Special Issue) covering the entire dental CBCT imaging chain — X-ray tube (spectrum, 0.5 mm focal spot, 2.5–10 mm Al-Eq filtration), gantry, flat-panel detector (indirect CsI/a-Si vs direct a-Se), FOV/collimation, scout-based mA modulation, FDK/ART/statistical reconstruction, stitching, grey-value calibration, and task-based image-quality assessment (MTF, contrast, noise, artifacts).

Key physics: mAs alone is linearly proportional to dose; FDK filtered backprojection runs on almost all dental CBCT machines; CBCT noise is generally higher than diagnostic CT; grey values are semiquantitative (HU-like use requires calibration); systematic geometric-calibration errors produce double images (360°) or crescent-moon artifacts (short orbits), random jitter produces streaks.

For users and referring dentists: understanding the imaging chain is the prerequisite for justification and optimization — smaller FOV, appropriate exposure factors, and recognizing that smoothing-reconstruction filters trade spatial resolution for noise.

## 세줄요약

치과용 CBCT 전 영상사슬을 다루는 state-of-the-art 리뷰(Dentomaxillofac Radiol 2015, CBCT 특집호) — X선관(스펙트럼·0.5 mm 포컬스팟·2.5–10 mm Al 환산 여과), 게트리, 평판검출기(간접 CsI/a-Si vs 직접 a-Se), FOV·콜리메이션, scout 기반 mA 변조, FDK/ART/통계적 재구성, 스티칭, 회색값 보정, 과제 기반 화질 평가(MTF·대조도·노이즈·인공물).

핵심 물리: 선량에 선형 비례하는 것은 mAs뿐, 거의 모든 치과 CBCT는 FDK(필터 보정 역투영) 재구성, CBCT 노이즈는 일반 진단 CT보다 높고, 회색값은 반정량적(HU 유사 사용엔 보정 필요), 기하보정의 계통 오류는 이중상(360°)/초승달 모양 인공물(짧은 궤도), 무작위 지터는 줄무늬(스트릭) 유발.

사용자·의뢰 치과의사에게: 영상사슬 이해가 정당화·최적화(작은 FOV, 적절 노출, 재구성 평활필터의 공간해상도-노이즈 trade-off 인지)의 전제.

## Summary

This state-of-the-art review walks through the physical and engineering basis of every stage of dental cone-beam computed tomography (CBCT). It opens with the X-ray tube — Bremsstrahlung/characteristic spectra, aluminium-equivalent filtration of 2.5–10 mm, and a typical 0.5 mm focal spot that is a key determinant of sharpness — then covers C-arm gantry types (seated, standing, supine), flat-panel detectors (indirect CsI/a-Si versus direct a-Se), FOV/collimation options, and scout-image-based exposure control. Reconstruction is dominated by the Feldkamp–Davis–Kress (FDK) filtered backprojection, with iterative (ART) and statistical methods acknowledged as higher quality but computationally too heavy for routine dental use. The page also covers image stitching, grey-value calibration (CBCT values are only semiquantitative), geometric-calibration failure modes, and the four fundamental image-quality parameters — spatial resolution (MTF), contrast, noise, and artifacts — emphasizing that image quality must be judged relative to the imaging task. The clinical takeaway is optimization literacy: FOV size, exposure factors, and reconstruction filters are the levers that balance dose, resolution, and noise.

## Key Contributions

- Complete imaging-chain exposition: hardware → acquisition → reconstruction → visualization (MPR, oblique, synthetic panoramic, 3D).
- X-ray spectrum/filtration physics specific to CBCT: kVp sets maximum photon energy (90 kV → 90 keV), mean energy ≈60% of maximum; mAs is linearly dose-proportional.
- FOV taxonomy: predefined rectangular collimator openings vs free z-collimation; small-FOV vs large-FOV dose logic.
- Detector comparison: indirect (CsI scintillator + a-Si TFT) vs direct (a-Se) flat panels — fill factor, DQE, ghosting/afterglow trade-offs.
- Reconstruction algorithm landscape: FDK (almost universal), ART, statistical IR (OSEM, penalized likelihood) — noise-model advantage at low dose, computational barrier to routine use.
- Grey-value semiquantitative nature + geometric-calibration failure signatures (systematic shift → double image/crescent-moon; jitter → streaks).
- Task-based image-quality framework: spatial resolution (MTF), contrast (large-area), noise (quantum + electronic), artifacts (scatter, metal, beam hardening).

## Methodology

Narrative state-of-the-art review (20 pp) written for the DMFR CBCT Special Issue. No systematic search protocol — expert synthesis grounded in classic references (Birch & Marshall spectrum data; Feldkamp, Davis & Kress 1984; Daly et al. calibration-artifact studies; Bushberg et al. imaging-physics textbook).

## Results

| Topic | Key technical content |
|---|---|
| X-ray tube | Bremsstrahlung continuous spectrum + characteristic peaks; mAs ∝ dose; kVp sets max/mean energy |
| Filtration | Al or Cu, 2.5–10 mm Al-Eq; thicker → higher mean energy, less beam hardening, lower entrance dose |
| Focal spot | Typical 0.5 mm; smaller → sharper (penumbra reduces), tube-loading limited |
| Gantry | Fixed C-arm seated/standing or supine; limited translation + up–down for FOV positioning |
| Detector | Indirect CsI/a-Si vs direct a-Se flat panels; electronic noise notable → CBCT noise > diagnostic CT |
| FOV | Multiple predefined vs free z-collimation; small FOV preferred for dose |
| Exposure control | Scout-based mAs; real-time patient-specific mA modulation not yet available (2015) |
| Reconstruction | FDK FBP in almost all systems; ART/statistical better at low dose but slow |
| Grey values | n-bit → 2^n values; semiquantitative, HU-like use requires calibration |
| Geometric calibration | Systematic centre-of-rotation shift → double image (360°)/crescent-moon (short orbit); jitter → streaks |
| Artifacts | Scatter (Compton) → shading/streaks/darkening; antiscatter grid reduces but may raise dose; metal + beam hardening |
| Visualization | MPR, oblique reformation, synthetic curved panoramic, 3D; window/level controls perceived contrast |

## Related Papers

- [[radiology/kaasalainen-2021-dental-cone-beam-ct-updated-review]] — 2021 medical-physics update of CBCT technology/dose/DRLs; this 2015 review is its predecessor providing the full imaging-chain foundation.
- [[radiology/suomalainen-2015-dentomaxillofacial-imaging-panoramic-views-cone]] — companion teaching review: same dose ladder + artifact discussion at clinical level; this page adds the engineering depth.
- [[radiology/jacobs-2018-cbct-implant-dentistry-recommendations-clinical]] — implant CBCT justification/optimization built on the physics principles (FOV, dose) explained here.
- [[radiology/dioguardi-2025-radiographic-artifacts-caries-diagnosis-sr-ma]] — empirical artifact taxonomy for caries diagnosis; operational counterpart to this page's artifact mechanism physics.
- [[radiology/charuakkra-2023-low-dose-cbct-image-dose-comparison]] — low-dose CBCT protocol benchmarks; practical demonstration of the exposure-optimization levers described here.