---
title: "Magnetic resonance imaging: Physics basics for the cardiologist"
authors: Vassiliou VS, Cameron D, Prasad SK, Gatehouse PD
year: 2018
doi: 10.1177/2048004018772237
category: radiology/mri
pdf_path: /Users/oracleneo/llm-wiki/papers/vassiliou-2018-mri-physics-basics-cardiologist.pdf
pdf_filename: vassiliou-2018-mri-physics-basics-cardiologist.pdf
source_collection: external
---

## Why Ingested

Seeds the new `radiology/mri` category with a foundation physics primer. The wiki already holds MRI-as-method dental papers whose interpretation depends on the physics this review explains: [[radiology/willershausen-2025-low-field-mri-pediatric-dental]] (0.55 T low-field MRI of pediatric teeth — needs T1/T2 relaxation, spin-echo vs gradient-echo contrast) and [[radiology/dewake-2023-mri-occlusal-trauma-pdl]] (T2-weighted IDEAL MRI of PDL edema — needs T2 relaxation and T2-weighting). This page gives a dentist/clinician the mechanism behind image formation so those pages and future dental-MRI work are read with correct physics, not as black boxes.

## Three-line Summary

Narrative review (~2018) of MRI physics aimed at clinical readers (cardiologist-oriented; physics is generic). Covers hardware, net magnetization/Larmor precession, radiofrequency (RF) excitation, T1 (spin-lattice) and T2 (spin-spin) relaxation, frequency/phase encoding, and sequences — spin echo, gradient echo/SSFP cine, late gadolinium enhancement (LGE), and quantitative T1 (MOLLI/ECV) and T2 mapping.

Key quantitative anchors: Larmor frequency f = γ·B0 with γ(H) = 42.6 MHz/T (1.5 T → 63.9 MHz); T1 = time to recover 63% of longitudinal magnetization; T2 = time for transverse (Mxy) signal to decay to 37%; T2* = combined T2 + T2′ dephasing; peak transmit RF power ~10,000 W; first human image 1977 (>4 h scan).

No clinical efficacy data — a didactic primer. Read as the physics foundation for MRI-based dental research pages (low-field MRI, T2-weighted PDL imaging) and for explaining to patients why MRI carries no ionizing radiation.

## 세줄요약

줄1: 심장 영상 임상가를 대상으로 MRI 물리 기본을 정리한 내러티브 리뷰(2018) — 하드웨어, 순자화·라모르 세차운동(Larmor precession), 고주파(RF) 여기, 세로이완(T1)·가로이완(T2), 주파수·위상 부호화(encoding), 시퀀스(spin echo, 구배에코/SSFP, 지연가돌리늄증강(LGE), T1·T2 mapping)를 망라.

줄2: 핵심 수치 — 라모르 주파수(Larmor frequency) f = γ·B0, 수소 자기회전비율(gyromagnetic ratio, γ) 42.6 MHz/T (1.5 T에서 63.9 MHz); T1은 세로자화 63% 회복 시점, T2는 가로(Mxy) 신호 37% 감쇠 시점, T2* = T2 + T2′ 탈위상; 송신 RF 피크 출력 약 10,000 W; 최초 인체 영상 1977년(4시간 이상 촬영).

줄3: 임상 성적 근거가 아니라 교과서적 기본 물리 원리 — 치과 MRI를 방법으로 쓴 위키 페이지(저자기장 소아 MRI, T2 강조 치주인대(PDL)) 해석과 환자에게 "MRI는 전리방사선이 없다"를 설명할 근간.

## 1. Document Information

- **Journal**: JRSM Cardiovascular Disease, 2018;7:1–9
- **DOI**: 10.1177/2048004018772237
- **Institution**: Royal Brompton Hospital and Imperial College London, CMR Unit, London, UK; Norwich Medical School, University of East Anglia, Norwich, UK (CC BY-NC 4.0 review article)

## 2. Key Contributions

- Clinician-accessible explanation of the physics chain: hydrogen proton as a spin, net magnetization M along B0, Larmor precession, resonance/excitation, T1 and T2 relaxation, and T2* as combined T2 + T2′.
- Image formation explained from first principles: frequency encoding (position → Fourier spectrum under a gradient), repeated phase-encoding steps, and 2D Fourier-transform reconstruction.
- Sequence-level survey: spin echo (90°/180°, T1 vs T2 weighting via repetition/echo timing), gradient echo / steady-state free precession (SSFP) cine, late gadolinium enhancement (LGE) for focal fibrosis, and quantitative T1 mapping (MOLLI, ECV) and T2 mapping as tissue-characterization biomarkers.
- Safety framing: MRI has no ionizing radiation, with cautions on paramagnetic contrast agents (Gd), implantable devices, and a theoretical neoplasia concern.

## 3. Methodology and Architecture

- **Design**: Narrative review (primarily for cardiologists; the physics is modality-generic).
- **Scope**: Fundamentals — hardware (magnet, RF chain, shim/gradient coils, computer), magnetization and Larmor frequency, excitation, T1/T2/T2* relaxation, image encoding; then established and novel pulse sequences (spin echo, GRE/SSFP, LGE, MOLLI/ECV, T2 mapping); safety considerations.
- **n**: Not applicable (no systematic search, no data synthesis); ~30 cited references plus supplementary material.

## 4. Key Results and Benchmarks

Didactic content (values exactly as stated in the paper):

| Concept | Parameter as stated |
|---|---|
| Larmor frequency | f = γ × B0; γ(hydrogen) = 42.6 MHz/T; 1.5 T → 63.9 MHz |
| T1 (spin-lattice / longitudinal) | time for z-magnetization to recover to 63% of initial value; tighter-bonded protons → shorter T1 |
| T2 (spin-spin / transverse) | time for total transverse (Mxy) signal to decay to 37%; usually much faster than T1 |
| T2* (T2 star) | combined dephasing of T2 + T2′; T2′ usually but not always faster than T2 |
| Transmit RF power | ~10,000 W peak in short pulses (safety-motivated coil distance) |
| First human MRI image | 1977, requiring >4 h scanning |
| MOLLI (T1 mapping) | newer variant 8 inversion-recovery images over 11 heart beats, single breath-hold of 8–12 s |
| ECV formula | ECV = (1 − haematocrit) × (1/T1_myo_post − 1/T1_myo_pre) / (1/T1_blood_post − 1/T1_blood_pre) |
| Other MRI-active nuclei | ¹³C, ¹⁷O, ¹⁹F, ³¹P (research/CMR spectroscopy only) |

Sequence notes: spin echo recovers T2′ inhomogeneity at the echo time to leave pure T2 decay (T2 weighting increases with longer echo time; T1 weighting occurs when the 90°–180° acquisition repeats before complete T1 recovery). GRE uses a single RF pulse (typically <90°) for faster/motion-tolerant imaging, repeated continuously for cine function; SSFP gives more reliable blood–myocardium contrast because of the markedly longer T2 of blood. LGE: T1-sensitive gradient echo 10–15 min post-gadolinium; fibrotic regions show slower washout and appear enhanced; normal myocardium is nulled dark.

## 5. Limitations and Future Work

- Cardiology-oriented: no dental-specific coils, sequences, or small-FOV maxillofacial applications (the reviewer must transfer physics to the dental setting).
- A primer, not evidence synthesis — no quantitative validation or grading of the diagnostic claims cited (e.g., LGE-outcome associations).
- 2018 vintage: predates current low-field dental MRI literature (e.g., 0.55 T studies) and modern acceleration/AI reconstruction; treat sequence details as of its time.

## 6. Related Work

- Willershausen 2025 (low-field MRI, pediatric dentistry): applies the same physics at 0.55 T for dental imaging — this primer supplies the mechanism (T1-weighted FLASH / relaxation contrast) behind that method.
- Dewake 2023 (T2-weighted IDEAL MRI of PDL in occlusal trauma): this primer explains the T2 relaxation and T2-weighting that make PDL edema (water) conspicuous.
- Yeung 2023 (fMRI in complete/implant denture rehabilitation): the blood-oxygen-level-dependent (BOLD) contrast relies on the MR signal physics and T2* effects this primer introduces.

## 7. Glossary

- **Larmor frequency**: the precession frequency of net magnetization, f = γ × B0; it sets the operating (RF) frequency of the scanner — 42.6 MHz × 1.5 T = 63.9 MHz.
- **Gyromagnetic ratio (γ)**: ratio of a nucleus's magnetic dipole moment to its angular momentum (42.6 MHz/T for hydrogen); hydrogen wins on abundance and highest ratio in the body.
- **T1 (spin-lattice / longitudinal relaxation)**: recovery of z-axis magnetization after RF excitation — the time to reach 63% of equilibrium; energy released to the molecular environment.
- **T2 (spin-spin / transverse relaxation)**: decay of in-plane (Mxy) signal from spin-spin interaction — the time to drop to 37% of the original value; usually much faster than T1.
- **T2***: the combined dephasing of genuine T2 plus T2′ (macroscopic-to-subvoxel field inhomogeneity, e.g., iron deposition).
- **Frequency/phase encoding**: applying a gradient so signal frequency encodes position (read-out via Fourier transform), with repeated phase twists along the perpendicular in-plane direction to assemble a 2D image.