---
title: "Magnetic Resonance Imaging: Principles and Techniques: Lessons for Clinicians"
authors: Vijay P.B. Grover, Joshua M. Tognarelli, Mary M.E. Crossey, I. Jane Cox, Simon D. Taylor-Robinson, Mark J.W. McPhail et al.
year: 2015
date: 2015-08-20
doi: 10.1016/j.jceh.2015.08.001
source: grover-2015-mri-principles-techniques-lessons-clinicians.md
category: [radiology/mri]
evidence_level: narrative-review
pdf_path: /Users/oracleneo/llm-wiki/papers/grover-2015-mri-principles-techniques-lessons-clinicians.pdf
pdf_filename: grover-2015-mri-principles-techniques-lessons-clinicians.pdf
source_collection: external
tags: [mri, physics, rf-safety, t1-t2-relaxation, diffusion-weighted-imaging, diffusion-tensor-imaging, mr-spectroscopy, magnetization-transfer, parallel-imaging, field-strength, radiology]
relations:
  - type: applies-to
    target: radiology/willershausen-2025-low-field-mri-pediatric-dental
  - type: applies-to
    target: radiology/dewake-2023-mri-occlusal-trauma-pdl
---

## Three-line Summary
Narrative review of MRI physics and techniques written for clinical readers: nuclear spin, Larmor precession, RF excitation and FID, gradients and coils, parallel imaging (SENSE), T1/T2 relaxation, magnetization transfer, diffusion-weighted/tensor imaging (ADC, FA), and MR spectroscopy.

Key numbers: water/CSF T1 3000–5000 ms vs fat 260 ms; 3 T DWI improves SNR 30–50% and contrast-to-noise up to 96% over 1.5 T; SENSE factor 2 cuts imaging time up to 50%; typical diffusion weighting b 1000 s/mm²; MRS TR ≥1500–2000 ms, TE 30–35 ms; PRESS ~2× STEAM signal.

For dental MRI readers this is the foundation layer: it explains why tissue contrast appears as it does and where artifacts come from — not a clinical-outcome study.

## 세줄요약
줄1: 임상 독자를 위한 MRI 물리·기법 내러티브 리뷰 — 핵스핀, Larmor 세차운동, RF 여기와 자유유도감쇠(FID), 경사자장·코일, 병렬영상(SENSE), T1/T2 이완, 자화전이(MT), 확산강조·확산텐서영상(DWI/DTI, ADC·FA), 자기공명분광(MRS).
줄2: 핵심 수치: 물·뇌척수액(CSF) T1 3000–5000 ms vs 지방 260 ms; 3 T 확산강조영상(DWI)이 1.5 T 대비 신호대잡음비(SNR) 30–50%, 대조도대잡음비 최대 96% 개선; SENSE 인자 2는 촬영시간 최대 50% 단축; 대표 b값 1000 s/mm²; MRS TR≥1500–2000 ms, TE 30–35 ms; PRESS 신호가 STEAM의 약 2배.
줄3: 조직 대비가 생기는 이유와 인공물의 원인을 이해하게 하는 기반 지식 — 치과 MRI 판독의 물리적 토대이지 특정 임상 결과를 평가한 연구는 아니다.

## Summary
This is a clinician-oriented review of magnetic resonance physics and techniques from an Imperial College London hepatology group. It walks from quantum/classical basics (nuclear spin, B₀ alignment, Larmor precession at ν₀ = γB₀) through signal generation (RF excitation, free induction decay, Fourier transform), spatial localization (gradients, RF/phase-array coils), and scan acceleration (parallel imaging, SENSE), and then surveys the imaging tools most relevant to interpretation: T1/T2 relaxation weighting, magnetization transfer, DWI/DTI with ADC and FA metrics, and MRS. Quantitative anchors are given throughout (tissue T1 values, field-strength SNR gains, sequence timings, metabolite chemical shifts). Its clinical value for this wiki is didactic rather than evidentiary: it provides the physics underpinning for interpreting the dental-MRI application pages, and it flags the limits (susceptibility and eddy-current artifacts, cryogenic magnet environment) that affect image quality and safety screening.

## Key Contributions
- Makes NMR physics legible to clinicians: spin, B₀ alignment, Larmor equation (ν₀ = γB₀), RF B₁ excitation, FID, Fourier transform to image or spectrum.
- Explains T1 (spin-lattice, 63% regrowth) vs T2 (spin-spin dephasing) relaxation and how TR weights the image — with tissue constants (water/CSF T1 3000–5000 ms dark on T1; fat 260 ms bright on T1).
- Quantifies field-strength trade-offs: 3 T DWI over 1.5 T gives SNR +30–50%, contrast-to-noise up to +96%, ADC/FA variability −34–52%, but worse susceptibility and eddy-current artifacts — attenuated by parallel imaging (SENSE).
- Covers magnetization transfer imaging and the MTR formula (100 × (SI_off − SI_on)/SI_off).
- Reviews DWI/DTI operational rules: ≥6 noncollinear directions for the tensor, 20–30 for rotationally invariant voxels, b 1000 s/mm² typical, two-point ADC adequate in brain.
- Reviews clinical MRS: single-voxel vs CSI, STEAM vs PRESS (~2× signal), TR/TE guidelines, quantification approaches, and the key cerebral metabolite resonances (NAA 2.0, cho 3.2, Cr 3.0, mI 3.6, Glx 2.1–2.5, Lac ~1.3 ppm at TE 30 ms).

## Methodology
Narrative review article in a hepatology journal (J Clin Exp Hepatol, © INASL), written for clinical readers; no systematic search, no pooled data, no meta-analysis. Timeframe context: received 31 July 2015, accepted 10 August 2015, online 20 August 2015 — reflects the 0.5–3 T scanner generation of its era.

## Results
| Topic | Key content / value |
|---|---|
| Nuclear spin & excitation | ¹H and ³¹P nuclei possess spin; B₀ aligns spins into low/high energy states; RF pulse at resonant frequency generates FID; signal averaged to improve SNR; Fourier transform → image or spectrum |
| Gradients & coils | Gx/Gy/Gz gradient coils localize signal spatially; phased-array coils → uncorrelated noise, higher SNR than single receiver |
| Parallel imaging | SENSE™ (Philips) under-samples k-space + multi-coil acquisition; SENSE factor 2 → up to 50% shorter scans; needs reference scan for coil sensitivities |
| Scanner / field strength | Cryogenic superconducting magnets 0.5–1.5 T typical (Earth's field ~0.5 G = 0.00005 T); 3 T systems widely available — better SNR/resolution/quantification but worse susceptibility, eddy current, field-instability artifacts |
| T1/T2 relaxation | T1 = 63% return to equilibrium; water/CSF 3000–5000 ms (dark on T1), fat 260 ms (bright on T1); T2 = spin-spin dephasing in xy plane |
| Magnetization transfer | Saturates MR-invisible bound proton pool via off-resonance RF; MTR = 100 × (SI_off − SI_on)/SI_off quantifies bound/free water compartments |
| DWI / DTI | Isotropic vs anisotropic diffusion; diffusion tensor needs ≥6 noncollinear directions; 20–30 directions for robust isotropic ADC/FA; tractography; ADC measures tissue water diffusivity |
| ADC / FA | ADC from differently weighted DWI; FA/RA describe degree of anisotropy; myelination not essential for anisotropy |
| 3 T vs 1.5 T DWI | SNR +30–50%, CNR up to +96%, ADC/FA variability −34–52%; FA/ADC values field-independent but measurement precision improves |
| MRS acquisition | Single-voxel (higher SNR) vs CSI/2D-single-slice (wider coverage); TR ≥2000 ms (≥1500 min), TE 30–35 ms short to maximize data; PRESS ~2× STEAM signal |
| MRS metabolites | ¹H: NAA 2.0 ppm (neuronal marker), cho 3.2 ppm (membrane), Cr 3.0 ppm (internal reference), mI 3.6 ppm (glial/osmolyte), Glx 2.1–2.5 ppm, Lac ~1.3 ppm (at TE 30 ms); ¹H water reference 4.7 ppm; absolute quantification difficult → ratios to creatine common |

## Related Papers
- [[radiology/willershausen-2025-low-field-mri-pediatric-dental]] — applies-to: field-strength physics (0.55 T SNR/resolution limits) here underpins the interpretation of that low-field pediatric dental MRI study.
- [[radiology/dewake-2023-mri-occlusal-trauma-pdl]] — applies-to: the T1/T2 relaxation content here is the basis for reading T2-weighted periodontal-ligament signal intensity.
- This page seeds the `radiology/mri` subcategory; no prior physics-primer sibling exists yet.