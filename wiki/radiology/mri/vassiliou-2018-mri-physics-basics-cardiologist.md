---
title: "Magnetic resonance imaging: Physics basics for the cardiologist"
authors: Vassiliou VS, Cameron D, Prasad SK, Gatehouse PD
year: 2018
date: 2018-01-01
doi: 10.1177/2048004018772237
source: vassiliou-2018-mri-physics-basics-cardiologist.md
category: radiology/mri
evidence_level: narrative-review
pdf_path: /Users/oracleneo/llm-wiki/papers/vassiliou-2018-mri-physics-basics-cardiologist.pdf
pdf_filename: vassiliou-2018-mri-physics-basics-cardiologist.pdf
source_collection: external
tags: [radiology, mri, magnetic-resonance-physics, larmor-frequency, t1-relaxation, t2-relaxation, gradient-echo, spin-echo, lge, t1-mapping, foundation, narrative-review]
relations:
  - type: extends
    target: willershausen-2025-low-field-mri-pediatric-dental
  - type: extends
    target: dewake-2023-mri-occlusal-trauma-pdl
---

## Three-line Summary

Narrative review (~2018) of MRI physics aimed at clinical readers (cardiologist-oriented; physics is generic). Covers hardware, net magnetization/Larmor precession, radiofrequency (RF) excitation, T1 (spin-lattice) and T2 (spin-spin) relaxation, frequency/phase encoding, and sequences — spin echo, gradient echo/SSFP cine, late gadolinium enhancement (LGE), and quantitative T1 (MOLLI/ECV) and T2 mapping.

Key quantitative anchors: Larmor frequency f = γ·B0 with γ(H) = 42.6 MHz/T (1.5 T → 63.9 MHz); T1 = time to recover 63% of longitudinal magnetization; T2 = time for transverse (Mxy) signal to decay to 37%; T2* = combined T2 + T2′ dephasing; peak transmit RF power ~10,000 W; first human image 1977 (>4 h scan).

No clinical efficacy data — a didactic primer. Read as the physics foundation for the radiology/mri category and for MRI-based dental research pages (low-field MRI, T2-weighted PDL imaging).

## 세줄요약

줄1: 심장 영상 임상가를 대상으로 MRI 물리 기본을 정리한 내러티브 리뷰(2018) — 하드웨어, 순자화·라모르 세차운동(Larmor precession), 고주파(RF) 여기, 세로이완(T1)·가로이완(T2), 주파수·위상 부호화(encoding), 시퀀스(spin echo, 구배에코/SSFP, 지연가돌리늄증강(LGE), T1·T2 mapping)를 망라.

줄2: 핵심 수치 — 라모르 주파수(Larmor frequency) f = γ·B0, 수소 자기회전비율(gyromagnetic ratio, γ) 42.6 MHz/T (1.5 T에서 63.9 MHz); T1은 세로자화 63% 회복 시점, T2는 가로(Mxy) 신호 37% 감쇠 시점, T2* = T2 + T2′ 탈위상; 송신 RF 피크 출력 약 10,000 W; 최초 인체 영상 1977년(4시간 이상 촬영).

줄3: 임상 성적 근거가 아니라 교과서적 기본 물리 원리 — 치과 MRI를 방법으로 쓴 위키 페이지(저자기장 소아 MRI, T2 강조 치주인대(PDL)) 해석과 환자에게 "MRI는 전리방사선이 없다"를 설명할 근간.

## Summary

This is a narrative review from the cardiology literature that walks a clinical reader through MRI physics from first principles: how a hydrogen proton behaves as a spin, how the net magnetization M is created by B0, how Larmor precession sets the scanner operating frequency, and how RF excitation flips M into the transverse plane where T1 and T2 relaxation produce the received signal. It then explains image formation through frequency and phase encoding with a 2D Fourier transform, and surveys the main pulse sequences: spin echo, gradient echo/SSFP cine, LGE, and quantitative T1 (MOLLI, ECV) and T2 mapping. The didactic value for dentistry is as the foundation layer for the wiki's radiology/mri category — the physics behind the low-field MRI (T1-weighted FLASH, relaxation contrast) and T2-weighted PDL-edema studies the wiki already holds. Its cardiology frame and 2018 vintage limit it to physics fundamentals, not dental-specific protocols.

## Key Contributions

- Clinician-accessible chain of MRI fundamentals: spin → net magnetization → Larmor precession (f = γ·B0) → RF excitation → T1/T2/T2* relaxation.
- Image formation from first principles: frequency encoding under a gradient + phase encoding + 2D Fourier transform reconstruction.
- Sequence survey: spin echo (T1/T2 weighting by echo/repetition timing), GRE/SSFP cine, LGE for focal fibrosis, MOLLI T1 mapping with ECV, and T2 mapping for oedema.
- Safety framing: no ionizing radiation, with cautions on Gd contrast, implantable devices, and a theoretical neoplasia concern.

## Methodology

Narrative review (2018, JRSM Cardiovascular Disease). No systematic search or data synthesis: the authors revisit basic physics theories and describe established plus novel cardiac pulse sequences, to give non-physicist clinicians the vocabulary to read advanced MRI manuscripts. Physics itself is modality-generic and transfers to dental MRI.

## Results

| Concept | Parameter as stated |
|---|---|
| Larmor frequency | f = γ × B0; γ(H) = 42.6 MHz/T → 63.9 MHz at 1.5 T |
| T1 (longitudinal) | time for z-magnetization to recover to 63% of initial; tighter bonds → shorter T1 |
| T2 (transverse) | time for Mxy signal to decay to 37%; usually much faster than T1 |
| T2* | combined T2 + T2′ dephasing; T2′ usually but not always faster |
| Transmit RF power | ~10,000 W peak in short pulses |
| First human MRI | 1977, >4 h scan |
| MOLLI T1 mapping | 8 inversion-recovery images / 11 beats, 8–12 s breath-hold |
| ECV | (1 − haematocrit) × (Δ1/T1_myo) / (Δ1/T1_blood), pre/post Gd |
| Other nuclei | ¹³C, ¹⁷O, ¹⁹F, ³¹P (research spectroscopy only) |

Sequence contrast notes: spin echo 90°–180° rephases T2′ at the echo time to leave pure T2 decay; longer echo time → more T2 weighting; T1 weighting arises when the acquisition repeats before full T1 recovery. GRE uses a single <90° RF pulse for motion-tolerant cine; SSFP yields reliable blood–myocardium contrast because blood T2 is markedly longer than myocardium. LGE is T1-sensitive GRE 10–15 min post-Gd; fibrotic myocardium retains Gd (slower washout) and enhances, normal myocardium is nulled.

## Related Papers

- [[radiology/willershausen-2025-low-field-mri-pediatric-dental]] — 0.55 T MRI of pediatric teeth; this primer supplies the relaxation physics (T1-weighted FLASH) behind that method.
- [[radiology/dewake-2023-mri-occlusal-trauma-pdl]] — T2-weighted IDEAL MRI quantifying PDL edema; this primer explains the T2 relaxation that makes water (edema) conspicuous.
- [[complete-denture/yeung-2023-functional-neuroplasticity-denture-rehabilitation-fmri]] — fMRI of denture rehabilitation; BOLD contrast rests on the T2*/MR-signal physics introduced here.