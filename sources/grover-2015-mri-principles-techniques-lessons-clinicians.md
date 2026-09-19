---
title: "Magnetic Resonance Imaging: Principles and Techniques: Lessons for Clinicians"
authors: Vijay P.B. Grover, Joshua M. Tognarelli, Mary M.E. Crossey, I. Jane Cox, Simon D. Taylor-Robinson, Mark J.W. McPhail et al.
year: 2015
doi: 10.1016/j.jceh.2015.08.001
category: [radiology/mri]
pdf_path: /Users/oracleneo/llm-wiki/papers/grover-2015-mri-principles-techniques-lessons-clinicians.pdf
pdf_filename: grover-2015-mri-principles-techniques-lessons-clinicians.pdf
source_collection: external
---

## Why Ingested
Seeds the brand-new `radiology/mri` subcategory with the underlying physics primer — nuclear spin, T1/T2 relaxation, sequences, and artifact sources — that underpins interpretation of the clinical dental-MRI pages [[radiology/willershausen-2025-low-field-mri-pediatric-dental]] (field-strength/SNR trade-offs in low-field 0.55 T dental imaging) and [[radiology/dewake-2023-mri-occlusal-trauma-pdl]] (T2-weighted signal-intensity interpretation).

## Three-line Summary
Narrative review by an Imperial College London hepatology team written for clinical readers: NMR/MRI fundamentals (nuclear spin, precession, Larmor equation), RF excitation and FID, gradients and coils, parallel imaging (SENSE), T1/T2 relaxation, magnetization transfer, diffusion-weighted/diffusion tensor imaging (ADC, FA), and MR spectroscopy.

Quantitative didactic anchors: water/CSF T1 = 3000–5000 ms vs fat 260 ms; DWI at 3 T vs 1.5 T improves SNR 30–50% and contrast-to-noise up to 96%; SENSE factor 2 cuts imaging time up to 50%; typical diffusion weighting b-value 1000 s/mm²; MRS TR ≥ 1500–2000 ms, TE 30–35 ms; PRESS signal ~2× STEAM.

For clinicians: the physical basis for why tissue appears bright/dark, how field strength and parallel imaging trade off speed vs artifact, and the limitations to weigh when requesting or reading MRI — setup for the wiki's dental-MRI interpretation pages rather than clinical evidence on any dental outcome.

## 세줄요약
줄1: Imperial College London 간담도 연구진이 임상 독자를 위해 쓴 내러티브 리뷰 — 핵스핀·세차운동·Larmor 방정식, RF 여기와 FID, 경사자장·코일, 병렬영상(SENSE), T1/T2 이완, 자화전이(MT), 확산강조영상(DWI/DTI, ADC·FA), 자기공명분광(MRS).
줄2: 정량 값: 물·뇌척수액(CSF) T1 3000–5000 ms vs 지방 260 ms; 3 T 확산강조영상(DWI)이 1.5 T 대비 신호대잡음비(SNR) 30–50%, 대조도대잡음비 최대 96% 개선; SENSE 인자 2는 촬영시간 최대 50% 단축; b값 1000 s/mm²; MRS TR≥1500–2000 ms, TE 30–35 ms; PRESS 신호가 STEAM의 약 2배.
줄3: 조직이 왜 밝고 어두운지, 자장세기·병렬영상이 속도와 인공물(자기민감도·와전류) 사이에서 어떻게 절충되는지를 이해하게 하는 기초 — 치과 MRI 판독을 뒷받침하는 물리 원리이지 임상 결과 증거는 아니다.

## 1. Document Information
- **Journal**: Journal of Clinical and Experimental Hepatology 2015;5(3):246–255 (© INASL)
- **DOI**: 10.1016/j.jceh.2015.08.001
- **Institution**: Imperial College London (Liver Unit, Division of Diabetes, Endocrinology and Metabolism, Department of Medicine) & Institute of Hepatology, University of London, United Kingdom
- Received 31 July 2015; accepted 10 August 2015; available online 20 August 2015.

## 2. Key Contributions
- Clinician-oriented primer mapping NMR physics (spin, B₀ alignment, Larmor precession, RF excitation, FID, Fourier transform) to how MR images are formed.
- Explains T1 (spin-lattice) vs T2 (spin-spin) relaxation with concrete tissue time constants and TR manipulation, so signal ordering on T1-/T2-weighted images is interpretable (e.g., fat bright on T1, water/CSF dark on T1).
- Positions parallel imaging (SENSE/SMASH), field strength (1.5 T vs 3 T) and their artifact trade-offs (magnetic susceptibility, eddy currents) in scanner terms the requesting clinician sees.
- Reviews magnetization transfer imaging (MTR formula), DWI/DTI (isotropic vs anisotropic diffusion, tensor, ADC, FA, b-value, minimum diffusion directions) as quantitative microstructural tools.
- Reviews clinical MRS: single-voxel vs CSI (chemical shift imaging), STEAM vs PRESS, quantification strategies, and the cerebral metabolite peaks (NAA 2.0, Cr 3.0, cho 3.2, mI 3.6, Glx 2.1–2.5, Lac ~1.3 ppm at TE 30 ms).

## 3. Methodology and Architecture
- **Design**: Narrative review article (no systematic search strategy, no PRISMA, no meta-analysis).
- **Scope**: Basic physics + clinical applications (DWI/DTI, MT, MRS) + future outlook; heavily hepatology/neurology-oriented in clinical examples.
- **n**: Not applicable (no pooled patient data; cited source studies only).

## 4. Key Results and Benchmarks
- Scanners: superconducting magnets 0.5–1.5 T typical (Earth's field 0.5 G = 0.00005 T comparison); 3 T research systems with better SNR, spectral/spatial/temporal resolution; susceptibility and eddy-current artifacts worse at 3 T.
- Spin dynamics: nucleus precesses at Larmor frequency ν₀ = γB₀ (γ = gyromagnetic ratio, fixed per nucleus; energy gap ΔE = γħB₀/2π).
- Relaxation: T1 = time to return 63% of longitudinal magnetization toward equilibrium; T2 = transverse/spin-spin dephasing in xy plane.
- Tissue T1 values: water and CSF 3000–5000 ms (dark on T1-weighted); fat 260 ms (bright on T1-weighted).
- 3 T vs 1.5 T DWI: SNR +30–50%, contrast-to-noise up to +96%, ADC/FA variability −34–52%; FA and ADC values field-strength-independent in principle.
- Diffusion: minimum 6 noncollinear directions for diffusion tensor; 20–30 directions for rotationally invariant isotropic voxel estimates; typical b-value 1000 s/mm²; two-point ADC (b0 + 1000) adequate for human brain.
- MRS parameters: TR should be ≥ 2000 ms, "certainly no less than 1500 ms"; TE as short as possible, usually 30–35 ms; PRESS (90°+two 180° pulses) yields ~2× the signal of STEAM.
- MRS reference: ¹H water reference at 4.7 ppm; absolute quantification hard (water >70% of brain tissue, >10,000× typical metabolite ~10 mmol/L), so ratios to creatine are used.
- Magnetization transfer: MTR = 100 × (SI_off − SI_on)/SI_off quantifies normally MR-invisible bound protons.

## 5. Limitations and Future Work
- Narrative review — no systematic search, inclusion criteria, or evidence grading; selection of topics/examples is author-led and liver/neuro-centric.
- 2015 hardware landscape (0.5–3 T) predates the 2020s spread of low-field (0.55 T) and ultra-high-field systems, though its physics framing generalizes.
- Does NOT cover patient safety, metal/artifact screening, or contrast-agent (gadolinium) handling in depth — clinician expertise must come from dedicated safety references rather than this primer.
- No dental content: every clinical example is liver/brain; transfer to dentomaxillofacial MRI requires the dental-application pages.

## 6. Related Work
- willershausen-2025-low-field-mri-pediatric-dental: clinical 0.55 T MRI study whose SNR/resolution and motion-artifact discussion sits on the field-strength physics this primer explains.
- dewake-2023-mri-occlusal-trauma-pdl: T2-weighted periodontal-ligament signal-intensity study; primer gives the T2-relaxation basis for that weighting.
- (No pre-existing sibling physics primer in the wiki — this page seeds `radiology/mri`.)

## 7. Glossary
- **Larmor frequency (ν₀)**: the precession rate of a nucleus in field B₀, ν₀ = γB₀, determined by the nucleus's gyromagnetic ratio γ.
- **Free induction decay (FID)**: the RF-induced voltage signal emitted by excited nuclei as they relax, averaged and Fourier-transformed into image or spectrum.
- **T1 / spin-lattice relaxation**: regrowth of longitudinal magnetization; time constant for return to 63% of equilibrium.
- **T2 / spin-spin relaxation**: dephasing of nuclear spins in the transverse (xy) plane after excitation.
- **Apparent diffusion coefficient (ADC)**: measured tissue water diffusivity mapped from differently weighted DWI images.
- **Fractional anisotropy (FA)**: scalar describing how directionally restricted (anisotropic) diffusion is within a voxel.
- **Chemical shift**: dependence of resonant frequency on the local electronic (chemical) environment, expressed in ppm.