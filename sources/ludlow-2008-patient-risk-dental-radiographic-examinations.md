---
title: "Patient risk related to common dental radiographic examinations: the impact of 2007 International Commission on Radiological Protection recommendations regarding dose calculation"
authors: "Ludlow JB, Davies-Ludlow LE, White SC"
year: 2008
doi: 10.14219/jada.archive.2008.0339
pmid: "18762634"
category: [radiology]
source_collection: pubmed-text
full_text: false
text_path: ""
source_url: https://pubmed.ncbi.nlm.nih.gov/18762634/
---

## Why Ingested

치과 방사선 유효선량(유효선량, Effective Dose, ED)의 표준 기준 논문. [[radiology/stervik-2024-radiation-exposure-during-orthodontic-treatment]]과 [[radiology/lee-2021-dental-imaging-doses-web-dose-calculator]]에서 반복 인용하는 원천 데이터 제공. ICRP 2007 권고안 적용 후 계산 값이 32–422% 상승했음을 처음으로 정량화.

## One-line Summary

Phantom-based dosimetry study recalculating effective doses of common dental radiographs using 2007 ICRP recommendations: intraoral PSP+rect-collimation full-mouth 34.9 µSv, 4 bitewings 5.0 µSv, panoramic 14–24 µSv.

## 한줄요약

2007 ICRP 권고안 적용 재계산: 구내 전악(PSP+직사각조준) 34.9 µSv, 4매 bite-wing 5.0 µSv, 파노라마 14–24 µSv — 이전 값 대비 32–422% 상승.

## 1. Document Information

- **Type**: Phantom dosimetry / comparative study
- **Journal**: Journal of the American Dental Association, 2008 Sep; 139(9):1237–43
- **PMID**: 18762634
- **DOI**: [10.14219/jada.archive.2008.0339](https://doi.org/10.14219/jada.archive.2008.0339)
- **Note**: Abstract-only; no PMC full text available.

## 2. Key Contributions

- First major paper to recalculate dental X-ray effective doses under ICRP 2007 (vs 1990), which added salivary glands, extrathoracic region, and oral mucosa as newly weighted tissues.
- Benchmark effective dose table for all major dental radiographic modalities (JADA 2008 Table):
  - FMX + PSP or F-speed + rectangular collimation: **34.9 µSv**
  - 4-image posterior bitewings + PSP/F-speed + rectangular: **5.0 µSv**
  - FMX + PSP or F-speed + round collimation: **170.7 µSv**
  - FMX + D-speed + round collimation: **388 µSv**
  - Panoramic Orthophos XG (CCD): **14.2 µSv**
  - Panoramic ProMax (CCD): **24.3 µSv**
  - PA cephalogram (PSP): **5.1 µSv**
  - Lateral cephalogram (PSP): **5.6 µSv**
- Demonstrates that transitioning from D-speed film + round collimation to PSP/F-speed + rectangular collimation reduces FMX dose by ~91%.
- Provides the cancer-risk framework: at 34.9 µSv, risk of fatal cancer ≈ 1–2 per million (compared to background ~2400 µSv/year in the US).

## 3. Methodology and Architecture

- Tissue-equivalent head phantom (Alderson-Rando).
- Measurements: organ-absorbed doses at 28 radiosensitive sites using thermoluminescent dosimeters (TLDs).
- Effective dose calculated twice: E(1990) and E(2007) — the 2007 tissue-weighting coefficients newly include salivary glands (w=0.01 each), extrathoracic airways (w=0.01), oral mucosa (w=0.01 for residual tissues).
- Equipment: standard clinical units (Orthophos XG, ProMax), film and digital receptors.

## 4. Key Results and Benchmarks

| Exam | Receptor | Collimation | E(2007) µSv |
|---|---|---|---|
| FMX | PSP/F-speed | Rectangular | 34.9 |
| 4 BW | PSP/F-speed | Rectangular | 5.0 |
| FMX | PSP/F-speed | Round | 170.7 |
| FMX | D-speed | Round | 388 |
| Panoramic Orthophos XG | CCD | N/A | 14.2 |
| Panoramic ProMax | CCD | N/A | 24.3 |
| PA cephalogram | PSP | N/A | 5.1 |
| Lateral cephalogram | PSP | N/A | 5.6 |

- Values are 32–422% higher than E(1990) depending on modality (D-speed round collimation shows greatest increase).
- Natural background radiation (USA): ~3,000 µSv/year (~8.2 µSv/day).
- Single PA (part of FMX) approximately ~1.5–2 µSv estimated; full FMX 34.9 µSv ≈ 4.3 days of background radiation.

## 5. Limitations and Future Work

- No individual PA single-image dose explicitly tabulated (FMX aggregate reported); later studies (e.g., Johnson & Ludlow 2020) provide single-image breakdown.
- Phantom-based, not patient-based; actual patient organ positions vary.
- No digital sensor (CCD/CMOS) for intraoral compared directly in this study.

## 6. Related Work

- Preceded by Ludlow & Ivanovic (2008) on CBCT doses under the same ICRP 2007 framework.
- Followed by Johnson & Ludlow (2020) updating dose data with newer collimation systems.
- Stervik (2024) cites this paper for dose anchors in pediatric orthodontic imaging.

## 7. Glossary

- **E(2007)**: Effective dose calculated per ICRP 2007 tissue-weighting factors
- **FMX**: Full-mouth series (typically 18–20 periapical + bitewing images)
- **PSP**: Photostimulable phosphor storage plate (digital receptor)
- **Rectangular collimation**: Beam-limiting aperture matching the receptor size → reduces dose vs round collimation
- **µSv**: Microsievert — unit of effective dose (1 mSv = 1,000 µSv)
