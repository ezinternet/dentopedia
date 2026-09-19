---
title: "A novel method for measuring the direction and angle of central ray and predicting rotation centre via panorama phantom"
authors: Joh BJ, Lee SS, Yeom HG, Jo GD, Kim JE, Huh KH, Yi WJ, Heo MS
year: 2024
doi: 10.1093/dmfr/twae050
category: [radiology]
pdf_path: /Users/oracleneo/llm-wiki/papers/joh-2024-novel-method-measuring-central-ray-direction.pdf
pdf_filename: joh-2024-novel-method-measuring-central-ray-direction.pdf
source_collection: external
---

## Why Ingested

User-requested ingest into the panoramic-quality cluster: this is the first quantitative, phantom-based method to measure the central-ray direction and predict the rotation-centre path of a panoramic unit, directly extending the device-geometry characterisation held in [[wiki/radiology/martins-2022-multilayer-panoramic-radiography-device-mapping]] (focal-trough mapping) and the projection theory of [[wiki/radiology/devlin-2013-object-position-magnification-panoramic-radiography]].

## Three-line Summary

In-vitro technical-report study (3 repeated panoramic exposures with the OP-100 device, ball-type panorama phantom, drawing coordinates measured to 0.001 mm) proposing a novel method to quantify the central-ray direction and predict the rotation centre from panoramic phantom images.

The angle between the central ray and the midline decreased progressively from 179.8° (lower-incisor midpoint) to 82.2° (TMJ), while the angle to the arch form peaked at 119.9° at the lower-second-premolar cusp region, and the predicted rotation centre ran from the distolateral coronoid aspect anteromedially to the midline between the mandibular notch and coronoid process.

Clinically, the method gives manufacturers and clinicians a standardised, non-radioactive-phantom tool to compare panoramic equipment geometry — knowledge no manufacturer discloses — though reproducibility and equipment generality remain untested.

## 세줄요약

OP-100 파노라마 장비와 볼형 파노라마 팬텀(Panorama Phantom, 치경부 중심선 금속구 2 mm, 4 mm 간격)으로 3회 반복 촬영(73 kVp, 10 mA, 17.6 s)해 중심선 주사선(Central Ray)의 방향·각도, 회전중심(Rotation Centre)을 예측하는 새 측정법을 제안한 체외(In-vitro) 기술 보고.

정중선(Midline)과 중심선의 각도는 하악 절치 중점 179.8°에서 측두하악관절(TMJ) 82.2°까지 전방→후방으로 점감, 아치형(Arch Form)에 대한 각도는 하악 제2소구치 교두부(119.9°)에서 최대였고, 회전중심은 관상돌기 원심측에서 하악절흔과 관상돌기 사이를 지나 정중선으로 전내방 이동하는 예측 결과를 얻음.

제조사가 공개하지 않는 장비별 중심선·회전중심 기하학을 팬텀 하나로 정량 비교할 수 있는 표준화 도구를 제공하지만, 단일 장비·반복 재현성·장비 간 일반화 검증은 남은 과제.

## 1. Document Information

- **Journal**: Dentomaxillofacial Radiology 2024;53(8):573-579 (Technical Report)
- **DOI**: 10.1093/dmfr/twae050
- **Institution**: Department of Oral and Maxillofacial Radiology, School of Dentistry and Dental Research Institute, Seoul National University; Department of Oral and Maxillofacial Radiology, Wonkwang University College of Dentistry, Korea

## 2. Key Contributions

- First quantitative, image-based method to measure the central-ray direction (angle to midline and to arch form) of a panoramic device using a ball-type panorama phantom — no film, no ionizing exposure of a subject.
- Rotation-centre path predicted from intersections of adjacent central rays, fitted with a Bézier curve; visualised on the phantom axial view.
- Central-ray function derived from intermittent measurements predicts the ray direction at any point in the arch (8 major reference points: incisors to TMJ).
- Standardised comparative-analysis tool for equipment manufacturers and clinicians, applicable in principle to any arch-form phantom (coordinates are arch-form independent).

## 3. Methodology and Architecture

- **Design**: In-vitro phantom technical study; 3 repeated acquisitions with phantom repositioning to assess positioning error
- **Phantom**: Panorama phantom — acrylic, arch-shaped from average lower dental arch of Korean adult men; 2 mm diameter metal balls along the centre line at 4 mm mesiodistal intervals; 22 additional arch-shaped parallel lines at 2 mm buccolingual intervals; ball height spaced 2.5 mm in the horizontal plane (oblique appearance from the side)
- **Equipment**: OP-100 (Instrumentarium Dental, Tuusula, Finland), 73 kVp, 10 mA, 17.6 s; phantom on specialised tripod mount, incisor midpoint matched to incisive-notch centre, levelled with a digital inclinometer
- **Measurement**: outermost + innermost reference points on the same x-coordinate define the central ray; x-coordinates measured in Paint (pixel measurement), proportional coordinates computed in Python up to a drawing precision of 0.001 mm; balls B1–B34 plus even-numbered B36–B46 used as starting points
- **Analysis**: slopes → midline angle via arctangent; arch-form angle via central-ray function + arctangent; rotation centre via intersection of adjacent central rays smoothed with a Bézier curve

## 4. Key Results and Benchmarks

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

(Values are mean of 3 measurements ± SD.)

- Midline–central-ray angle: continuous decrease anterior→posterior, B1 179.76 ± 0.76° → B46 75.89 ± 0.28°.
- Arch-form–central-ray angle: increase to a peak of 120.89 ± 0.97° (≈121°) at ball B9, then consistent decrease to a minimum of 33.24 ± 0.29° at B46; ≈90° at ball B19 (90.16 ± 0.38°).
- Standard deviations across repeats were small (≤≈1.45° for arch-form angles); repositioning error judged clinically negligible.
- Rotation centre: started from approximately the distolateral aspect of the coronoid process, then moved anteromedially in a curved line passing between the mandibular notch and coronoid process to reach the midline.

## 5. Limitations and Future Work

- Single panoramic device type (OP-100) — no cross-unit generalisation tested.
- Reproducibility limited by manual phantom placement; a phantom–equipment adapter would improve it (difference across the 3 repeats was not significant).
- Potential errors from metal-ball centre measurement, interconnection of the 2 innermost balls, and axial-view visualisation; mitigated by using outermost/innermost reference points + linear-regression ratio distance between the 2 innermost balls.
- Method based on phantom drawing data — small errors from drawing-vs-actual-phantom discrepancy.
- Future: automate the principle in software; comparative analysis across many panoramic units; clinical studies of the method's benefit.

## 6. Related Work

- Martins 2022: multilayer device focal-trough mapping (phantom-based geometry) — Joh extends device-geometry characterisation to central-ray direction and rotation centre
- Devlin 2013: theoretical magnification/object-position analysis — Joh provides the complementary empirical ray geometry
- Scarfe 1993 (cited): projection-beam angulation vs average tangent of tooth contact points — limited to specific locations; Joh measures continuously across the arch
- Kaeppler 2008 (cited): rotation-centre shape via film fixed to an Alderson Rando phantom — approximate shape only, no quantitative measurement; Joh's method is digital and quantitative
- Yeom 2018 (cited): original ball-type panorama phantom development — the phantom this paper reuses

## 7. Glossary

- **Central ray**: the trajectory along the axial view through which the X-ray beam passes at each instant during panoramic acquisition; its direction determines which structures overlap on the 2D image
- **Rotation centre**: the pivot point around which the X-ray source and image receptor rotate during panoramic imaging; directly related to the central-ray direction
- **Panorama phantom**: ball-type acrylic phantom in an arch shape built from average lower-dental-arch data of Korean adult males, with 2 mm metal balls at defined intervals
- **Bézier curve**: a parametric curve used here to smooth the locus of central-ray intersection points into a continuous predicted rotation-centre path