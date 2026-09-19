---
title: "MRI basics for radiation oncologists"
authors: van der Heide UA, Frantzen-Steneker M, Astreinidou E, Nowee ME, van Houdt PJ
year: 2019
date: 2019-04-13
doi: 10.1016/j.ctro.2019.04.008
source: van-der-heide-2019-mri-basics-for-radiation-oncologists.md
category: radiology/mri
evidence_level: narrative-review
pdf_path: /Users/oracleneo/llm-wiki/papers/van-der-heide-2019-mri-basics-for-radiation-oncologists.pdf
pdf_filename: van-der-heide-2019-mri-basics-for-radiation-oncologists.pdf
source_collection: external
tags: [radiology, mri, geometric-fidelity, radiotherapy-planning, image-contrast, t1, t2, water-fat-shift, artifact, safety]
---

## Three-line Summary
(Line 1: Narrative review (Clin Transl Radiat Oncol 18:74–79, 2019), Netherlands Cancer Institute — a didactic primer on using MRI in radiotherapy planning, written for clinicians, not a data study.)
(Line 2: T1/T2-weighted contrast; gradient non-linearity distortions grow up to ~1 cm at scanner edges; RT-accurate sequences require geometric distortion <2 mm (stereotactic <1 mm); water-fat shift 3.4 ppm (0.5–2 pixels, pixel 0.5–1.0 mm); metal artifacts worse at 3 T vs 1.5 T; diagnostic images are generally not geometrically trustworthy for RT.)
(Line 3: MR images must be acquired with RT-dedicated protocols in treatment position using flexible coils around fixation masks; verify geometric fidelity before contouring — do not use diagnostic-department scans.)

## 세줄요약
(줄1: 서사적 리뷰(Clin Transl Radiat Oncol 18:74–79, 2019, 네덜란드암연구소) — 방사선치료계획에서 MRI 사용을 위한 임상가용 기본 교재. 데이터 연구 아님.)
(줄2: T1/T2 강조 대조도; 경사자계 비선형성 왜곡은 스캐너 가장자리에서 최대 약 1 cm; RT용 정확 시퀀스는 기하 왜곡 <2 mm(정위 <1 mm); water-fat shift 3.4 ppm(0.5–2 픽셀, 픽셀 0.5–1.0 mm); 금속 인공물은 1.5 T보다 3 T에서 악화; 진단용 영상은 일반적으로 RT용 기하 신뢰가 어려움.)
(줄3: 고정 마스크 주위 유연 코일로 치료 자세에서 RT 전용 프로토콜로 촬영하고 기하 충실도를 검증해야 하며, 진단과 획득 영상은 검증 전 윤곽묘사에 쓰면 안 됨.)

## Summary
This is a narrative review-primer, not a clinical study, that teaches the MRI physics and workflow issues a clinician needs when using MR images for radiotherapy (RT) planning. It explains how T1/T2 relaxation generates soft-tissue contrast, why superior contrast makes MRI increasingly central to target and organ-at-risk delineation (with CT or MR-only via pseudo-CT), and — critically — why geometrical fidelity is the defining constraint for RT-MRI. Gradient non-linearity can shift structures up to ~1 cm at the scanner periphery; accurate RT sequences must hold distortion below 2 mm (1 mm for stereotactic). The water-fat shift (3.4 ppm) also biases geometry by 0.5–2 pixels. Because diagnostic MRI maximizes contrast and tolerates these errors, diagnostic-department images should not be used for RT contouring without verification of the specific acquisition protocol. For dentistry, this page supplies the physical-language foundation and quantitative fidelity thresholds behind dental-MRI applications such as low-field imaging of children and periodontal-ligament T2 assessment.

## Key Contributions
- Quantifies and localizes geometric-fidelity limits: gradient non-linearity distortions up to ~1 cm at scanner edges; RT-threshold <2 mm, stereotactic <1 mm; water-fat shift 0.5–2 pixels (3.4 ppm).
- Explains why diagnostic MRI ≠ planning MRI: 2D multi-slice sequences get only 2D (in-plane) distortion correction, diagnostic protocols maximize water-fat shift (sacrificing geometry for SNR), and images carry no visible marker that correction was applied.
- Framework for sequence/artifact/safety choices in a treatment workflow: flexible coils over fixation masks, T2-TSE vs T1-GRE resilience to metal, EPI-based DWI fragility, breath-hold vs navigator-triggered vs 4D-MRI for motion.

## Methodology
Narrative review / clinician-directed primer by the Netherlands Cancer Institute and Leiden University Medical Center radiation-oncology physics group (2019). No cohort or database search; didactic content is supported by cited primary physics and opinion references, including the Paulson et al. 2016 MRI-simulation consensus that sets the 2 mm / 1 mm distortion criteria, with phantom/grid and healthy-volunteer illustration cases.

## Results
| Outcome | Result |
|---|---|
| Field strength (diagnostic) | 1.5 T or 3.0 T; metal distortion larger at 3 T than 1.5 T |
| Gradient non-linearity distortion | ~minimal at iso-center up to ~1 cm at scanner edges; 2D correction leaves off-center slice planes warped |
| Geometric-fidelity threshold (RT) | <2 mm; stereotactic <1 mm |
| Water-fat shift | 3.4 ppm → 0.5–2 pixel shift (pixel 0.5–1.0 mm); example: ~2 mm cranio-caudal ventricle shift at 2-pixel shift |
| Metal artifact resilience | T2-TSE < T1 gradient-echo; DWI (EPI) most sensitive, often unusable near implants |
| Air/tissue interface effect | Small for most sequences; severe for DWI (rectal gas, head-neck air) |
| Motion artifacts | Ghosting; navigator-triggering freezes max-exhale phase (may mismatch treatment phase); 4D-MRI maps phases for mid-ventilation |
| Safety liabilities | Ferromagnetic attraction, pacemaker/ICD (MRI-conditional with cardiology check), RF heating (SAR limits), loop currents, implant heating |

## Related Papers
- [[radiology/willershausen-2025-low-field-mri-pediatric-dental]] — dental application of MRI (0.55 T low-field vs ultra-low-dose CT in children); this primer supplies the physics and field-strength/artifact trade-offs behind that comparison.
- [[radiology/dewake-2023-mri-occlusal-trauma-pdl]] — T2-weighted MRI signal of the periodontal ligament as an occlusal-trauma measure; an applied example of the contrast/sequence principles reviewed here.
- [[radiology/mri/vassiliou-2018-mri-physics-basics-cardiologist]] — the cardiology-targeted twin of this primer; together they establish the physical-concepts foundation for the radiology/mri category.
- [[radiology/mri/grover-2015-mri-principles-techniques-lessons-clinicians]] — clinicians-oriented MRI principles/techniques primer extending the same fundamentals.
- [[radiology/mri/al-haj-husain-2025-magnetic-resonance-imaging-in-dental]] — MRI applications review in dentistry, converting these general MRI concepts to the dental domain.
- [[radiology/mri/liedke-2026-tmj-structures-dental-dedicated-mri]] — dental-dedicated MRI of TMJ structures using the sequence/contrast principles described here.