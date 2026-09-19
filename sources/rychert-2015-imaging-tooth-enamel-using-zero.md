---
title: "Imaging tooth enamel using zero echo time (ZTE) magnetic resonance imaging"
authors: Kevin M. Rychert, Gang Zhu, Maciej M. Kmiec, Venkata K. Nemani, Benjamin B. Williams, Ann Barry Flood, Harold M. Swartz, Barjor Gimi
year: 2015
doi: 10.1117/12.2083995
category: radiology/mri
pdf_path: /Users/oracleneo/llm-wiki/papers/rychert-2015-imaging-tooth-enamel-using-zero.pdf
pdf_filename: rychert-2015-imaging-tooth-enamel-using-zero.pdf
source_collection: external
---

## Why Ingested
First demonstration that dental enamel — a tissue with ultra-short T2 invisible to conventional MRI — can be volumetrically imaged with zero echo time (ZTE) sequences, matching micro-CT enamel volume to within 0.3 mm³. Seeds the radiology/mri category's non-artifact, hard-tissue-imaging capability alongside [[wiki/radiology/mri/grover-2015-mri-principles-techniques-lessons-clinicians]] and extends the [[wiki/radiology/willershausen-2025-low-field-mri-pediatric-dental]] program of radiation-free dental imaging.

## Three-line Summary
- Ex vivo imaging study (10 extracted human central incisors, plus 1 validation tooth): 11.75 T Bruker ZTE MRI (TR 2 ms, 256³ matrix) with region-growing segmentation, micro-CT as reference.
- ZTE enamel volume 81.19 mm³ vs micro-CT 81.47 mm³ (Δ 0.3 mm³, <0.4%); ZTE also revealed caries invisible on visual inspection; enamel volume correlated with simulated EPR dose signal (R=0.78, p<0.05).
- Clinical implication: radiation-free 3D enamel imaging is feasible with ZTE — a foundation for caries/erosion assessment and tooth biodosimetry, though 11.75 T preclinical field strength limits direct clinical translation.

## 세줄요약
- 체외 영상 연구(발치된 사람 중절치 10개 + 검증용 1개): 11.75 T Bruker ZTE 자기공명영상(MRI, TR 2 ms, 256³ 매트릭스) + 영역성장 분할, 대조는 미세CT.
- ZTE 법랑질 부피 81.19 mm³ vs 미세CT 81.47 mm³(차이 0.3 mm³, <0.4%); ZTE는 육안 검사에서 정상이던 우식도 발견; 법랑질 부피는 모의 EPR 선량 신호와 상관(R=0.78, p<0.05).
- 임상적 의미: ZTE로 방사선 없는 3차원 법랑질 영상이 가능 — 우식·침식 평가와 치아 생체선량측정의 기초가 되나, 11.75 T 전임상 자기장 강도는 임상 직접 적용의 한계.

## 1. Document Information
- **Journal**: Proc SPIE Int Soc Opt Eng. 2015;9417 (doi:10.1117/12.2083995)
- **DOI**: 10.1117/12.2083995
- **Institution**: Geisel School of Medicine at Dartmouth (Radiology) + Bruker BioSpin Corporation, USA

## 2. Key Contributions
- First demonstration of tooth enamel volumetric imaging with ZTE MRI — enamel's ultra-short T2 (unimageable with conventional MRI/UTE) is captured by applying spatial-encoding gradients during RF excitation.
- ZTE enamel volume agrees with micro-CT within ~0.3 mm³ (0.4%) while adding zero radiation — an alternative to micro-CT (which deposits dose) and crushing (destructive) for enamel quantification.
- ZTE revealed caries on teeth that appeared normal on visual inspection (caries bright on MRI, hypodense on micro-CT) — incidental diagnostic signal beyond dosimetry.
- Enabled personalized EPR tooth biodosimetry modeling: enamel volume meshes fed finite-element (HFSS) simulations of resonator sensitivity for radiation-disaster triage.

## 3. Methodology and Architecture
- **Design**: Ex vivo laboratory imaging study (extracted teeth), validation against micro-CT
- **n**: 10 extracted central incisors (5 donor-paired mouth models) + 1 separate incisor for modality validation
- **MRI**: 11.75 T Bruker Avance spectrometer, triple-axis gradients; 3D ZTE TR = 2 ms, FOV 25.6 mm³, matrix 256³, NEX 16; UTE comparison TR = 8 ms, TE = 20 µs
- **Segmentation**: thresholding + seeded region-growing (itk-SNAP), enamel depth maps, HFSS volumetric meshes
- **Micro-CT reference**: GE MicroCT-Locus SP, 90 kVp, 80 µA, 720 projections, 0.01 mm resolution
- **EPR context**: L-band (1.15 GHz) tooth dosimetry, doses 0/2/4/6/10 Gy, measured RIS (mRIS) vs simulated RIS (sRIS) correlations

## 4. Key Results and Benchmarks
- ZTE vs micro-CT enamel volume: 81.19 mm³ vs 81.47 mm³ (validation tooth)
- ZTE provided excellent enamel–dentin contrast, superior to UTE (which lost dentin signal)
- Caries detection: visible on ZTE (bright), hypodense on micro-CT, invisible on visual inspection
- Correlations (n=10 teeth, after 10 Gy): enamel volume ↔ labial-surface height R=0.72 (p<0.05); enamel volume ↔ sRIS R=0.78 (p<0.05); enamel volume ↔ mRIS R=−0.39 (n.s.); sRIS ↔ mRIS not correlated

## 5. Limitations and Future Work
- Preclinical 11.75 T scanner — clinical magnetic resonance systems (1.5–3 T) not yet demonstrated for enamel ZTE imaging
- Small sample (10 teeth); enamel-volume mesh resolution lower than micro-CT
- ZTE/enamel-imaging work is dosimetry-motivated; caries finding is incidental, not a formally evaluated diagnostic outcome

## 6. Related Work
- [[wiki/radiology/mri/grover-2015-mri-principles-techniques-lessons-clinicians]]: MRI physics primer — provides the relaxation (T1/T2) background explaining why enamel needs ZTE
- [[wiki/radiology/willershausen-2025-low-field-mri-pediatric-dental]]: radiation-free dental MRI program; ZTE extends it to hard-tissue (enamel) imaging
- [[wiki/caries/van-amerongen-2019-silver-diamine-fluoride-caries-arrest-amazonian]] and caries-diagnosis pages: ZTE's incidental caries detection is relevant to radiation-free caries imaging (relationship directional: this page shows capability, clinical validation pending)

## 7. Glossary
- **ZTE (Zero Echo Time)**: MRI sequence applying spatial-encoding gradients during RF excitation, acquiring signal almost immediately after excitation — captures tissues with ultra-short T2 (enamel, cortical bone)
- **UTE (Ultrashort Echo Time)**: sequence with very short TE (~20 µs); still loses short-T2 signal relative to ZTE
- **EPR (Electron Paramagnetic Resonance)**: measures radiation-induced free radicals in tooth enamel for biodosimetry (tooth dosimetry)
- **mRIS / sRIS**: measured vs simulated radiation-induced EPR signal amplitude
- **HFSS**: Ansys High Frequency Structure Simulator — finite-element electromagnetic simulation of the EPR resonator
- **Region-growing segmentation**: seeded image segmentation algorithm (itk-SNAP) used to isolate enamel from dentin/water