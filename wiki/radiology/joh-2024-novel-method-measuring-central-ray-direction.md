---
title: "A novel method for measuring the direction and angle of central ray and predicting rotation centre via panorama phantom"
authors: Joh BJ, Lee SS, Yeom HG, Jo GD, Kim JE, Huh KH, Yi WJ, Heo MS
year: 2024
date: 2024-10-18
doi: 10.1093/dmfr/twae050
source: joh-2024-novel-method-measuring-central-ray-direction.md
category: [radiology]
evidence_level: in-vitro
pdf_path: /Users/oracleneo/llm-wiki/papers/joh-2024-novel-method-measuring-central-ray-direction.pdf
pdf_filename: joh-2024-novel-method-measuring-central-ray-direction.pdf
source_collection: external
tags: [panoramic radiography, central ray, rotation centre, phantom, technical report]
relations:
  - type: extends
    target: martins-2022-multilayer-panoramic-radiography-device-mapping
  - type: extends
    target: devlin-2013-object-position-magnification-panoramic-radiography
---

## Three-line Summary

In-vitro technical-report study (3 repeated panoramic acquisitions on an OP-100 unit, ball-type panorama phantom, drawing-data coordinates to 0.001 mm) presenting the first quantitative, image-based method for measuring the central-ray direction and predicting the rotation-centre path of a panoramic device.

The central-ray angle to the midline decreased progressively from 179.8° (lower-incisor midpoint) to 82.2° (TMJ), the angle to the arch form peaked at ~120.9° in the lower-second-premolar cusp region, and the predicted rotation centre ran curved from the distolateral coronoid aspect to the midline between the mandibular notch and coronoid process.

The method provides a standardised phantom-based tool for comparing unit geometry (information manufacturers do not disclose), though single-device scope and manual-repositioning reproducibility limit it.

## 세줄요약

OP-100 파노라마 장비(73 kVp, 10 mA, 17.6 s)와 볼형 파노라마 팬텀(Panorama Phantom: 치아 중심선 금속구 2 mm·4 mm 간격, 2 mm 협설 간격 22개 평행 아치형 라인)으로 3회 반복 촬영해, 중심선 주사선(Central Ray)의 방향·각도 측정과 회전중심(Rotation Centre) 예측을 제안한 체외(In-vitro) 기술 보고.

중심선-정중선(Midline) 각도는 하악 절치 중점 179.8°→측두하악관절(TMJ) 82.2°로 전방→후방 점감; 중심선-아치형(Arch Form) 각도는 하악 제2소구치 교두부(약 120.9°)에서 최고치 후 감소; 회전중심은 관상돌기 원심측에서 하악절흔-관상돌기 사이를 지나 곡선으로 정중선까지 전내방 이동.

제조사 미공개 장비 기하학을 팬텀으로 정량 비교할 수 있는 표준화 도구를 제공하나, 단일 장비·수동 재위치 재현성·장비 간 일반화 검증이 한계.

## Summary

Panoramic radiography is the most prescribed dental screening examination, yet manufacturers do not disclose the central-ray direction or rotation-centre path that determine which structures superimpose on the 2D image. This in-vitro technical report proposes a novel method using a ball-type panorama phantom: two metal balls sharing the same x-coordinate define each central ray, from which the angle to the midline and to the arch form are computed at 46 ball positions and 8 major anatomical reference points. The midline angle fell monotonically from 179.8° anteriorly to 82.2° at the TMJ, the arch-form angle peaked near the lower second premolar cusp, and the intersections of adjacent central rays (Bézier-fitted) traced a rotation centre running from the distolateral coronoid process to the midline. The method gives manufacturers and clinicians a standardised, quantifiable way to characterise and compare panoramic unit geometry, with single-device scope and manual reproducibility as its main limitations.

## Key Contributions

- First quantitative, image-based method to measure central-ray direction (angle to the midline and to the arch form) from panoramic phantom images — no film remnants or subject exposure required.
- Rotation-centre path predicted from adjacent central-ray intersections and visualised with a Bézier curve on the phantom axial view.
- Continuous central-ray function allows prediction of the ray direction at any arch point (8 reference points from lower incisors to TMJ tabulated).
- Phantom-based standardised comparative-anatomical tool applicable in principle to any arch-form phantom — geometry is arch-form independent.

## Methodology

**Design**: in-vitro phantom technical study; 3 repeated acquisitions with phantom repositioning to assess positioning error (results reported as mean ± SD).
**Phantom**: panorama phantom — arch-shaped acrylic model from average lower dental arch of Korean adult men; 2 mm metal balls along the centre line at 4 mm mesiodistal intervals; 22 additional arch-parallel lines at 2 mm buccolingual intervals; ball height spaced 2.5 mm (balls appear oblique laterally).
**Equipment**: OP-100 (Instrumentarium Dental, Tuusula, Finland), 73 kVp, 10 mA, 17.6 s; phantom on a purpose-built tripod, incisor midpoint aligned to the incisive notch, levelled with a digital inclinometer.
**Measurement**: outermost reference point = centre of the outermost ball; innermost reference point derived from a perpendicular drop and ratio of distances between the two lowest adjacent balls; x-coordinates pixel-measured in Paint, proportional coordinates computed in Python at 0.001 mm drawing precision; balls B1–B34 plus even-numbered B36–B46 as starting points.
**Analysis**: slope of each central ray → midline angle via arctangent; arch-form angle via the central-ray function; rotation centre = intersection points of adjacent central rays, smoothed as a Bézier curve.

## Results

Central-ray angles at the 8 major reference points (mean of 3 measurements ± SD):

| Measurement point | Midline–central ray (°) | Arch-form–central ray (°) |
|---|---|---|
| Midpoint of lower incisors | 179.8 ± 0.76 | 89.73 ± 0.73 |
| Lower canine centre | 156.2 ± 0.88 | 101.90 ± 0.87 |
| Lower first premolar cusp | 146.1 ± 0.77 | 117.81 ± 0.64 |
| Lower second premolar cusp | 138.2 ± 0.84 | 119.87 ± 0.88 |
| Lower first molar (mesiobuccal cusp) | 132.4 ± 1.02 | 114.69 ± 1.00 |
| Lower second molar (mesiobuccal cusp) | 121.5 ± 0.59 | 101.81 ± 0.59 |
| Lower second molar (distobuccal cusp) | 116.1 ± 0.61 | 94.90 ± 0.61 |
| Temporomandibular joint | 82.22 ± 0.21 | 45.65 ± 0.21 |

Ball-by-ball trends (B1–B46):
- **Midline angle**: progressive decrease — 179.76 ± 0.76° (B1) → 75.89 ± 0.28° (B46), anterior to posterior.
- **Arch-form angle**: rise to a peak of 120.89 ± 0.97° (~121°, ball B9), then consistent decrease to a minimum of 33.24 ± 0.29° (B46); ~90° at ball B19 (90.16 ± 0.38°).
- **Precision**: SDs small across all points (≤ ~1.45°); three-repeated repositioning difference judged clinically negligible.

**Rotation centre**: predicted locus started approximately from the distolateral aspect of the coronoid process, then moved anteromedially in a curved line passing between the mandibular notch and coronoid process to reach the midline.

## Related Papers

- [[radiology/martins-2022-multilayer-panoramic-radiography-device-mapping]] — both are phantom-based geometric characterisations of panoramic units (focal-trough mapping vs central-ray/rotation-centre); this paper extends the device-geometry inventory to the beam-ray axis.
- [[radiology/devlin-2013-object-position-magnification-panoramic-radiography]] — theoretical magnification/object-position geometry; this paper supplies the complementary empirical ray trajectory that theory assumes.
- [[radiology/farman-2010-panoramic-ccd-storage-phosphor-film]] — detector/focal-trough comparison background; device geometry determines trough and ray behaviour alike.
- [[radiology/kim-2024-real-ghost-pseudo-ghost-images-panoramic]] — ghost-image formation is governed by object position relative to the rotation centre this paper measures quantitatively.