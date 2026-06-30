---
title: "A fully digital approach to replicate peri-implant soft tissue contours and emergence profile in the esthetic zone"
authors: Carlo Monaco, Edoardo Evangelisti, Roberto Scotti, Giuseppe Mignani, Giovanni Zucchelli
year: 2016
doi: 10.1111/clr.12599
category: [digital-workflow]
pdf_path: /Users/oracleneo/llm-wiki/papers/monaco-2016-fully-digital-peri-implant-emergence.pdf
pdf_filename: monaco-2016-fully-digital-peri-implant-emergence.pdf
source_collection: external
---

## Why Ingested

디지털 워크플로우를 통한 임플란트 주위 연조직 형태 복제 기술을 문서화하기 위해 인제스트. 기존 [[immediate-implant/esthetic-soft-tissue]] 및 [[digital-workflow]] 영역의 임시 수복물 활용 디지털 인상 프로토콜을 확장하는 단기 임상 보고서로, STL 중첩 기반 FDT(Fully Digital Technique)의 선도적 기술 기술(記述).

## One-line Summary

Short communication introducing the Fully Digital Technique (FDT) — a two-scan STL superimposition method using an intraoral scanner to capture peri-implant soft tissue contours and emergence profile directly from the provisional restoration, enabling fully digital CAD/CAM abutment design without conventional impressions.

## 한줄요약

임시 수복물의 두 번의 구강 내 디지털 인상을 STL 중첩하여 임플란트 주위 점막 형태와 출현 프로파일을 완전 디지털 방식으로 복제하는 FDT(완전 디지털 기법)를 소개한 단기 임상 보고.

## 1. Document Information

- **Journal**: Clinical Oral Implants Research
- **Volume/Issue**: Vol. 27, Issue 12, December 2016, pp. 1511–1514
- **Type**: Short Communication (technique report)
- **Published online**: 22 April 2015
- **DOI**: 10.1111/clr.12599
- **Authors**: Carlo Monaco DDS MS PhD, Edoardo Evangelisti, Roberto Scotti, Giuseppe Mignani, Giovanni Zucchelli (University of Bologna)

## 2. Key Contributions

1. **Fully Digital Technique (FDT)**: Novel two-scan protocol using an intraoral scanner — eliminating the need for conventional or open-tray implant impressions for soft tissue capture.
2. **STL superimposition workflow**: STL1 (scanbody/implant position) + STL2 (provisional in situ + subgingival scan) → merged STL3 containing 3D implant position AND full peri-implant mucosal architecture.
3. **CAD/CAM abutment design**: Merged file used directly to design customized CAD/CAM abutment and fabricate a stereolithographic (SLA) cast via 3D printing.
4. First description of scanning the provisional restoration subgingival portion *out of the mouth* immediately after removal to capture subgingival emergence shape.

## 3. Methodology and Architecture

**Step 1 — STL1**: Standard implant scanbody placed; intraoral scanner (IOS) captures the implant platform 3D position → STL1.

**Step 2 — STL2 (two-part scan)**:
- Part A: Full scan of vestibular and palatal aspects of the provisional retained restoration in situ + adjacent teeth.
- Part B: Provisional unscrewed and immediately scanned *outside the mouth* to capture the subgingival contour before soft tissue collapses.

**Step 3 — Superimposition**: STL1 and STL2 imported into imaging software; "best fit" algorithm merges them into STL3 encoding (a) implant platform position, (b) peri-implant mucosal architecture, and (c) emergence profile.

**Step 4 — Output**: STL3 drives CAD/CAM abutment design; stereolithographic model printed for prosthetic workflow.

- Study design: Technical report / case description (no controlled comparison)
- Implant location: Anterior maxilla (esthetic zone)
- No quantitative accuracy data reported; concept-proof communication

## 4. Key Results and Benchmarks

- FDT successfully generated a merged STL3 file capturing the complete peri-implant mucosal shape from the provisional restoration.
- The customized CAD/CAM abutment designed from STL3 allowed replication of the conditioned emergence profile in the definitive restoration.
- A stereolithographic model fabricated from STL3 served as a physical working model, enabling conventional laboratory steps when needed.
- Authors concluded FDT is a "rapid digital approach" replacing conventional polyvinylsiloxane or open-tray implant impressions for soft tissue capture.

## 5. Limitations and Future Work

- **Case series limitation**: Short communication with no controlled accuracy study, no quantitative comparison vs conventional impression, no RCT or prospective cohort.
- **Soft tissue rebound**: Brief window between provisional removal and subgingival scan; if soft tissue collapses before scan completion, emergence profile accuracy is compromised.
- **Software dependency**: Requires imaging software capable of STL superimposition and "best fit" algorithms.
- **Single-unit case**: Applicability to multi-unit or posterior implants not addressed.
- Future work needed: RCT comparing FDT accuracy vs conventional and digital workflows; clinical outcome data (pink esthetic score, marginal bone level, patient satisfaction).

## 6. Related Work

- Joda T, Wittneben JG, Brägger U (2014) "Individualized Scanbody Technique" for emergence profile support — precursor digital approach cited by authors.
- Wittneben JG et al. (2013) Peri-implant soft tissue conditioning with provisional restorations — "dynamic compression technique" context.
- Lin WS, Harris BT, Morton D (2013) Implant-supported interim restorations to transfer peri-implant soft tissue profiles — conventional analog comparison.
- Chen ST & Buser D (2014) Esthetic outcomes after immediate/early implant placement SR — clinical context.

## 7. Glossary

| Term | Definition |
|---|---|
| FDT (Fully Digital Technique) | Two-scan IOS protocol introduced in this paper to capture peri-implant soft tissue in digital form |
| STL (Standard Triangulation Language) | 3D mesh file format output by intraoral scanners |
| STL1 | First scan with scanbody — captures implant platform position |
| STL2 | Second scan with provisional restoration (in situ + out-of-mouth subgingival) |
| STL3 | Merged/superimposed file combining implant position and peri-implant mucosal architecture |
| Scanbody | Scan reference body placed on the implant to record implant platform position and angulation for IOS |
| Best-fit algorithm | Software method that aligns two STL meshes by minimizing point-cloud deviation |
| Emergence profile | Subgingival 3D shape of the restoration as it exits the peri-implant soft tissue |
| CAD/CAM abutment | Computer-aided-design / computer-aided-manufacturing customized implant abutment |
| SLA model | Stereolithography 3D-printed working cast |
