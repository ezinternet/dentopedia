---
title: "Finite Element Analysis of the Influence of Implant Tilting and the Direction of Loading on the Displacement and Micromotion of Immediately Loaded Implants"
authors: Nihar Ranjan Sahoo, Subrat Kumar Sahany, Vijayendra Pandey, Abhaya Chandra Das, Purobi Choudhury, Saurav Panda, Rashmita Sahoo
year: 2024
doi: 10.4103/jpbs.jpbs_1103_23
category: [implants]
pdf_path: /Users/oracleneo/llm-wiki/papers/sahoo-2024-finite-element-analysis-influence-implant.pdf
pdf_filename: sahoo-2024-finite-element-analysis-influence-implant.pdf
source_collection: external
---

## Why Ingested

기존 [[wiki/overviews/tilted-axial-implant-angled-abutment-overview]]은 경사식립 (tilted implant)의 von Mises 응력(stress)과 임상 MBL/생존율을 종합했지만, 미세운동 (micromotion) — 즉시부하 (immediate loading) 골유착 성패를 좌우하는 별개 변수 — 는 다루지 않았다. 본 논문(Sahoo 2024)은 in vitro 실험 + FEA를 결합해 축방향(axial) vs 30° 원위경사(tilted) 임플란트의 하중방향별(수직/사선) 지대주 변위·미세운동을 직접 측정·비교했고, 사선하중 시 경사 임플란트가 축방향보다 오히려 낮은 최대 미세운동(19% 감소)을 보였다는, 응력 중심 문헌과는 다른 각도의 근거를 추가한다.

## Three-line Summary

In vitro + FEA comparative study (8 synthetic polyurethane bone blocks, 8 NobelReplace Tapered Groovy implants — 4 axial, 4 distally tilted 30°, 11 mm × 4.5 mm) simulating immediately loaded implants under 180 N vertical and 45° mesiodistal oblique loading.

Oblique loading produced 2.6–3.9× greater maximum micromotion than vertical loading regardless of angulation; under vertical loading axial and tilted implants had nearly identical peak micromotion (19 vs 17 µm), but under oblique loading the tilted implant showed 19% lower peak micromotion than the axial implant (56 vs 75 µm), while abutment displacement was consistently larger for tilted than axial implants under both loading directions.

Loading direction, not implant angulation, is the dominant determinant of micromotion magnitude, and abutment displacement does not track with maximum micromotion — a single-implant, small-sample (n=4/group) bench study without a physiologic bone-density range, so findings should be read as hypothesis-supporting rather than conclusive for clinical immediate-loading protocols.

## 세줄요약

인공 골블록(폴리우레탄 폼) 8개·NobelReplace Tapered Groovy 임플란트 8개(축방향 4개, 원위 30° 경사 4개, 11×4.5mm)를 이용한 즉시부하 임플란트 in vitro + 유한요소분석 (Finite Element Analysis, FEA) 비교연구 — 180N 수직하중 vs 45° 근원심 사선하중.

사선하중은 각도와 무관하게 수직하중보다 2.6~3.9배 큰 최대 미세운동 (micromotion)을 유발했으며, 수직하중에서는 축방향·경사 임플란트의 최대 미세운동이 거의 동일(19 vs 17µm)했으나 사선하중에서는 경사 임플란트가 축방향보다 19% 낮은 최대 미세운동(56 vs 75µm)을 보였고, 지대주 변위는 하중방향과 무관하게 경사 임플란트가 축방향보다 항상 컸다.

미세운동의 크기는 임플란트 각도보다 하중 방향이 더 크게 좌우하며 지대주 변위와 최대 미세운동은 서로 비례하지 않는다 — 단일 임플란트 디자인·소표본(군당 n=4)·단일 골밀도 벤치 연구로 임상 즉시부하 프로토콜에 대한 결론적 근거보다는 가설 지지 수준으로 해석해야 한다.

## 1. Document Information
- **Journal**: Journal of Pharmacy and Bioallied Sciences 2024;16(Suppl 1):S924-S926
- **DOI**: 10.4103/jpbs.jpbs_1103_23
- **Institution**: Institute of Dental Sciences, Siksha 'O' Anusandhan (Deemed to be University), Bhubaneswar, Odisha, India; Department of Mechanical Engineering, ITER, Bhubaneswar

## 2. Key Contributions
- Directly compares axial vs 30° distally tilted implants under both vertical and mesiodistal oblique loading, measuring both abutment displacement and micromotion (two related but non-equivalent biomechanical outcomes) in the same experiment.
- Validates FEA micromotion predictions against physical in vitro bench testing (synthetic bone blocks + epoxy cortical shell), reporting relative error between in vitro and FEA displacement values (Table 1).
- Finds that under oblique loading, tilted implants show LOWER peak micromotion than axial implants (19% reduction) — consistent with Sugiura et al. 2017 (J Periodontal Implant Sci), which the authors cite as validating precedent.
- Identifies maximum micromotion location near the implant apex.

## 3. Methodology and Architecture
- **Design**: in vitro experimental bench study + nonlinear FEA validation (bench-vs-simulation comparative study)
- **Materials**: 8 solid rigid polyurethane foam blocks (Sawbones, density 0.32 g/cm³, mimicking low-to-medium density cancellous bone) with fiber-packed epoxy sheets as a cortical-bone analog
- **Implants**: 8 NobelReplace Tapered Groovy screw-type implants (Nobel Biocare AB), 11 mm length × 4.5 mm diameter; 4 placed axially, 4 placed with 30° distal tilt
- **Loading**: 180 N applied at the abutment top, tested both vertically and at 45° mesiodistal oblique angle
- **Outcomes**: abutment displacement (µm) and micromotion (µm, relative implant-bone displacement), measured experimentally and predicted by nonlinear FEA; reliability assessed by comparing in vitro vs FEA values
- **n**: 4 implants per group (axial, tilted) — no stated in vitro replicate count beyond the 8 total blocks/implants

## 4. Key Results and Benchmarks
**Table 1 — Abutment displacement (µm), in vitro vs FEA, with relative error:**

| Condition | In vitro (axial) | In vitro (tilted) | FEA (axial) | FEA (tilted) | Relative error |
|---|---|---|---|---|---|
| Vertical loading | 346.6 | 414.5 | 281.4 | 312.4 | −17.1% (axial), −25.1% (tilted) |
| Oblique loading | 548.0 | 668.0 | 558.2 | 602.6* | +2.1% (axial), −9.2% (tilted) |

(*Table 2 in the source PDF prints "6026" for oblique/tilted FEA displacement, almost certainly a typesetting artifact for 602.6 µm — flagged here for transparency rather than silently corrected.)

**Table 2 — Highest micromotion (µm):**

| Condition | Axial implant | Tilted implant |
|---|---|---|
| Vertical load | 19 | 17 |
| Oblique load | 75 | 56 |

- Oblique-load micromotion was 2.6–3.9× greater than vertical-load micromotion in both groups.
- Under oblique loading, tilted-implant micromotion was 19% lower than axial-implant micromotion.
- Under vertical loading, axial and tilted micromotion were "extremely near" (19 vs 17 µm).
- Abutment displacement values did not track with maximum micromotion values — the two metrics diverged by loading condition and angulation.

## 5. Limitations and Future Work
- Single implant system (NobelReplace Tapered Groovy) and single implant geometry (11 × 4.5 mm) — findings may not generalize to other macro-designs.
- Small sample (n=4 per group), single-implant models — no splinted/multi-implant or full-arch configuration tested.
- Single bone-density surrogate (0.32 g/cm³ polyurethane foam) — does not span the clinical D1–D4 bone-quality range.
- Static, single-load-magnitude testing (180 N) — no cyclic/fatigue loading to represent chronic function.
- Authors explicitly state "further studies are needed with larger sample size to validate the results."
- Apparent numeric inconsistency in Table 2 (oblique/tilted FEA displacement printed as "6026" rather than an expected ~602.6 µm) suggests a transcription/typesetting error in the original publication; treat that specific cell with caution.

## 6. Related Work
- Sugiura T, Yamamoto K, Horita S, Murakami K, Tsutsumi S, Kirita T (2017), *J Periodontal Implant Sci* 47:251-62 — cited by the authors as the original in vitro + FEA study on implant tilting/loading direction and micromotion in immediately loaded implants; the present paper explicitly reports its tilted-implant-lower-oblique-micromotion finding as consistent with Sugiura 2017. Not currently held in this wiki.
- Satyanarayana TSV et al. (2019), *J Clin Exp Dent* — cited as prior FEA work showing implant surface coating had no significant role in stress distribution.
- Huang SC, Tsai CF (2003) — cited as prior FEA work showing implant length does not reduce stress distribution, while increasing implant diameter does reduce stress.
- [[wiki/overviews/tilted-axial-implant-angled-abutment-overview]] — existing wiki synthesis on tilted vs axial implant biomechanics (von Mises stress, MBL, survival); this paper adds a micromotion/primary-stability angle not covered there.
- [[wiki/implants/murat-2025-all-on-4-implant-angulation-load-direction-fea]] — closest existing wiki FEA paper on implant angulation × occlusal load direction interaction (cortical stress outcome, not micromotion).

## 7. Glossary
- **Micromotion**: relative displacement between the implant surface and surrounding bone under load; excessive micromotion during the healing phase is a recognized risk factor for fibrous encapsulation instead of osseointegration.
- **Abutment displacement**: the total movement of the abutment top under an applied load, driven by both implant-bone micromotion and elastic deformation of the implant/bone-block system — not interchangeable with micromotion.
- **Distally tilted implant**: an implant intentionally angled (here 30°) relative to the long axis of the alveolar ridge/occlusal plane, commonly used to avoid anatomical structures or improve AP spread in full-arch/immediate-loading protocols.
- **Nonlinear FEA**: finite element analysis accounting for non-linear material behavior and/or contact conditions (e.g., implant-bone interface friction/slip), used here to more realistically simulate micromotion at the bone-implant interface.
- **Primary stability**: the mechanical stability of an implant immediately after placement, before biological osseointegration has occurred; micromotion is a proxy measure for the risk to primary stability under function.
