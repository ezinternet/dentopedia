---
title: "Imaging tooth enamel using zero echo time (ZTE) magnetic resonance imaging"
authors: Kevin M. Rychert, Gang Zhu, Maciej M. Kmiec, Venkata K. Nemani, Benjamin B. Williams, Ann Barry Flood, Harold M. Swartz, Barjor Gimi
year: 2015
date: 2015-03-19
doi: 10.1117/12.2083995
source: rychert-2015-imaging-tooth-enamel-using-zero.md
category: radiology/mri
evidence_level: in-vitro
pdf_path: /Users/oracleneo/llm-wiki/papers/rychert-2015-imaging-tooth-enamel-using-zero.pdf
pdf_filename: rychert-2015-imaging-tooth-enamel-using-zero.pdf
source_collection: external
tags: [mri, zte, enamel-imaging, tooth-imaging, zero-echo-time, radiation-free, biodosimetry]
---

## Three-line Summary
- Ex vivo imaging study (10 extracted human central incisors + 1 validation tooth): 11.75 T Bruker ZTE MRI (TR 2 ms, 256³ matrix), region-growing segmentation, micro-CT reference.
- ZTE enamel volume 81.19 mm³ vs micro-CT 81.47 mm³ (<0.4% difference); ZTE also revealed caries invisible to visual inspection; enamel volume correlated with simulated EPR dose signal (R=0.78, p<0.05).
- Clinical implication: radiation-free 3D enamel imaging is feasible with ZTE — a foundation for caries/erosion imaging and tooth biodosimetry, limited by the 11.75 T preclinical field strength.

## 세줄요약
- 체외 영상 연구(발치 중절치 10개 + 검증 1개): 11.75 T Bruker ZTE 자기공명영상(MRI, TR 2 ms, 256³ 매트릭스) + 영역성장 분할, 미세CT 대조.
- ZTE 법랑질 부피 81.19 mm³ vs 미세CT 81.47 mm³(차이 <0.4%); 육안 정상 치아의 우식도 발견; 법랑질 부피 ↔ 모의 EPR 신호 상관 R=0.78 (p<0.05).
- 임상적 의미: ZTE로 방사선 없는 법랑질 3차원 영상 가능 — 우식·침식 영상과 치아 생체선량측정의 기초, 단 11.75 T 전임상 장비가 한계.

## Summary
This ex vivo study demonstrates that tooth enamel — a tissue whose ultra-short T2 relaxation makes it invisible to conventional MRI — can be imaged volumetrically with zero echo time (ZTE) sequences at 11.75 T. Ten extracted central incisors were scanned (TR 2 ms, 256³ matrix) and enamel segmented by region-growing; on a validation tooth, ZTE enamel volume (81.19 mm³) matched micro-CT (81.47 mm³) within 0.4% while adding no radiation. ZTE also revealed caries on teeth that appeared visually normal, and enamel-volume meshes enabled finite-element (HFSS) simulation of EPR tooth-dosimetry signals (volume ↔ simulated RIS R=0.78, p<0.05). The clinical significance is that radiation-free, quantitative enamel imaging is technically feasible, opening a path to caries/erosion assessment and individualized biodosimetry, though the preclinical field strength used here is far above clinical systems.

## Key Contributions
- First demonstration of enamel volumetric imaging with ZTE MRI, enabled by spatial-encoding during RF excitation (captures ultra-short-T2 signal lost by conventional MRI and UTE).
- Radiation-free enamel quantification matching micro-CT (81.19 vs 81.47 mm³), an alternative to dose-depositing micro-CT and destructive crushing.
- Incidental caries detection: lesions bright on ZTE, hypodense on micro-CT, invisible on visual inspection.
- Enamel geometry meshed for HFSS EPR-resonator simulation — individualizes radiation-disaster tooth dosimetry.

## Methodology
- **Design**: Ex vivo laboratory imaging study, micro-CT validation
- **n**: 10 extracted central incisors (5 donor-paired mouth models) + 1 separate validation tooth
- **MRI**: 11.75 T Bruker Avance (triple-axis gradients); 3D ZTE TR = 2 ms, FOV 25.6 mm³, matrix 256³, NEX 16; UTE comparison TR = 8 ms, TE = 20 µs
- **Segmentation**: threshold + seeded region-growing (itk-SNAP) → enamel depth maps → HFSS meshes
- **Micro-CT**: GE MicroCT-Locus SP, 90 kVp, 80 µA, 720 projections, 0.01 mm resolution
- **EPR**: L-band 1.15 GHz, serial doses 0–10 Gy (6 MV linac), measured (mRIS) vs simulated (sRIS) signal correlations

## Results

| Outcome | Value |
|---|---|
| ZTE enamel volume (validation tooth) | 81.19 mm³ |
| Micro-CT enamel volume (same tooth) | 81.47 mm³ |
| Enamel volume ↔ labial height (n=10) | R = 0.72, p<0.05 |
| Enamel volume ↔ simulated EPR signal (sRIS) | R = 0.78, p<0.05 |
| Enamel volume ↔ measured EPR signal (mRIS) | R = −0.39, n.s. |
| sRIS ↔ mRIS | not correlated (unexpected) |
| Caries on visually-normal teeth | detected (bright on ZTE, hypodense on micro-CT) |
| Enamel–dentin contrast vs UTE | ZTE superior (UTE lost dentin signal) |

## Related Papers
- [[radiology/mri/grover-2015-mri-principles-techniques-lessons-clinicians]] — the physics primer behind this page: ultra-short T2 in hard tissues is exactly why enamel needs ZTE rather than conventional sequences.
- [[radiology/mri/vassiliou-2018-mri-physics-basics-cardiologist]] — companion primer on relaxation physics (T1/T2 fundamentals) framing why enamel is invisible to standard MRI.
- [[radiology/willershausen-2025-low-field-mri-pediatric-dental]] — radiation-free dental MRI direction; ZTE enamel imaging is the hard-tissue extension of this program (noted in the page's own context).
- [[radiology/dewake-2023-mri-occlusal-trauma-pdl]] — fellow dental-MRI application page; ZTE adds a hard-tissue imaging capability not covered by soft-tissue/PDL MRI.
- caries imaging relevance: ZTE's incidental caries detection motivates radiation-free caries diagnosis, though clinical validation at lower field strengths is pending.