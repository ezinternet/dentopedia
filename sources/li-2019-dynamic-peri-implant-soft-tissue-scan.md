---
title: "Dynamic changes of peri-implant soft tissue after interim restoration removal during a digital intraoral scan"
authors: Junying Li, Zhaozhao Chen, Meijie Wang, Hom-Lay Wang, Haiyang Yu
year: 2019
doi: 10.1016/j.prosdent.2018.10.023
category: [immediate-implant/esthetic-soft-tissue]
pdf_path: /Users/oracleneo/llm-wiki/papers/li-2019-dynamic-peri-implant-soft-tissue-scan.pdf
pdf_filename: li-2019-dynamic-peri-implant-soft-tissue-scan.pdf
source_collection: external
---

## Why Ingested

디지털 인상 채득 시 임시 보철물(IR) 제거 후 연조직 붕괴 속도를 정량화한 유일한 임상 연구로, 심미부 임플란트 디지털 워크플로우의 핵심 임상 근거. [[immediate-implant/esthetic-soft-tissue/monaco-2016-fully-digital-replicate-peri-implant-contours]]의 디지털 프로토콜이 실제 임상에서 타이밍 제약을 받는 이유를 설명하는 근거 논문으로 활용.

## One-line Summary

Clinical study (n=12 implant sites, 10 patients) quantifying peri-implant soft tissue collapse after interim restoration removal — significant emergence profile discrepancy (EPD) appears immediately and increases logarithmically over time, while papilla height changes are minimal (≤0.27 mm at 20 min).

## 한줄요약

임상연구(12개 임플란트, 환자 10명): 임시 보철물 제거 즉시 유의미한 출현 윤곽 불일치(EPD)가 발생하고 시간에 따라 대수적으로 증가하나, 유두 높이 변화는 미미함(20분 내 ≤0.27 mm).

## 1. Document Information

- **Journal**: The Journal of Prosthetic Dentistry
- **Volume/Issue**: Vol 122, Issue 3, pp 288–294
- **Publication date**: September 2019 (e-pub 2018)
- **DOI**: 10.1016/j.prosdent.2018.10.023
- **Study type**: Prospective clinical study
- **Funding**: Not specified in available text

## 2. Key Contributions

1. First study to quantify the **time-dependent collapse** of peri-implant soft tissue contour after IR removal using digital intraoral scanning.
2. Demonstrates that **emergence profile discrepancy (EPD) is immediate** — present at 0 seconds after removal — and continues to increase logarithmically with time.
3. Shows that **papilla height and gingival margin** are relatively stable (≤0.27 mm change at 20 minutes), suggesting the facial/palatal emergence zone is the critical dimension to capture.
4. Identifies **gingival thickness and implant depth** as positively correlated with EPD magnitude at some sites.
5. Provides clinical evidence supporting the need for **immediate capture** of soft tissue contour or use of a customized scan body / emergence profile replica during digital impression.

## 3. Methodology and Architecture

- **Design**: Prospective clinical study
- **Sample**: 10 participants, 12 single-implant sites in esthetic zone (maxillary anterior/premolar)
- **Protocol**:
  - Group 1: Optical scan with IR in place (baseline reference)
  - Group 2: Serial optical scans at multiple timepoints from **0 sec to 20 min** after IR removal
- **Measurements**:
  - Mesial papilla height, distal papilla height, gingival margin height
  - Facial soft tissue thickness, palatal soft tissue thickness
  - Emergence profile discrepancy (EPD) — deviation from IR-supported contour
- **Statistics**: Linear mixed model; natural logarithm of time as predictor for EPD; correlation with gingival thickness and implant depth

## 4. Key Results and Benchmarks

| Parameter | Finding |
|---|---|
| EPD at 0 sec | Significant discrepancy present immediately at all measurement sites |
| EPD over time | Significant positive correlation with ln(time) — grows logarithmically |
| Mesial papilla height change | ≤0.27 mm at 20 minutes (minimal) |
| Distal papilla height change | ≤0.27 mm at 20 minutes (minimal) |
| Gingival margin change | ≤0.27 mm at 20 minutes (minimal) |
| Palatal soft tissue thickness | Increased over time after IR removal |
| Gingival thickness & EPD | Significant positive correlation at some sites |
| Implant depth & EPD | Significant positive correlation at some sites |

**Clinical implication**: Papilla/marginal gingiva is stable enough not to affect proximal contact design, but the emergence profile cannot be captured accurately without the IR in place or an emergence-profile replica.

## 5. Limitations and Future Work

- Small sample (n=10/12 sites); single-center
- Only esthetic zone (anterior/premolar); molars not studied
- Abstract-level data (full text behind paywall) — specific EPD millimeter values not available from extracted text
- No comparison between different digital scanning techniques or scan body types
- Does not address optimal timing window for "acceptable" EPD error

## 6. Related Work

- Monaco et al. 2016 (Clin Oral Implants Res): Fully digital approach to replicate peri-implant contours using IR as scan body — precursor technique
- Duran et al. 2018 (Implant Dent): Pilot study on dimensional variations after removal of interim restorations (cited in this paper)
- Su et al. 2010: Critical and subcritical contour concepts for implant abutment design
- Joda & Brägger 2014: Individualized scanbody technique for emergence profile support during digital impression

## 7. Glossary

- **IR (Interim Restoration)**: Provisional crown placed on implant to shape peri-implant soft tissue contour and emergence profile
- **EPD (Emergence Profile Discrepancy)**: Dimensional difference between soft tissue contour with IR in place vs. after IR removal — the error introduced if scanning is delayed
- **Emergence profile**: The contour of a restoration from the crest of soft tissue to the clinical crown; dictates gingival health and esthetics
- **Scan body**: Device attached to implant for digital impression; customized versions can replicate the emergence profile to avoid soft tissue collapse during scanning
- **Linear mixed model**: Statistical model accounting for repeated measures within the same patient across multiple timepoints
