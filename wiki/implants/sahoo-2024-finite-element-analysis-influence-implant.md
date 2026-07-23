---
title: "Finite Element Analysis of the Influence of Implant Tilting and the Direction of Loading on the Displacement and Micromotion of Immediately Loaded Implants"
authors: Nihar Ranjan Sahoo, Subrat Kumar Sahany, Vijayendra Pandey, Abhaya Chandra Das, Purobi Choudhury, Saurav Panda, Rashmita Sahoo
year: 2024
date: 2024-02-29
doi: 10.4103/jpbs.jpbs_1103_23
source: sahoo-2024-finite-element-analysis-influence-implant.md
category: [implants]
evidence_level: in-vitro
pdf_path: /Users/oracleneo/llm-wiki/papers/sahoo-2024-finite-element-analysis-influence-implant.pdf
pdf_filename: sahoo-2024-finite-element-analysis-influence-implant.pdf
source_collection: external
tags: [FEA, implant-tilting, micromotion, abutment-displacement, immediate-loading, primary-stability, loading-direction]
relations:
  - type: extends
    target: murat-2025-all-on-4-implant-angulation-load-direction-fea
---

## Three-line Summary

In vitro + FEA comparative study (8 synthetic polyurethane bone blocks, 8 NobelReplace Tapered Groovy implants — 4 axial, 4 distally tilted 30°, 11 mm × 4.5 mm) simulating immediately loaded implants under 180 N vertical and 45° mesiodistal oblique loading.

Oblique loading produced 2.6–3.9× greater maximum micromotion than vertical loading regardless of angulation; under vertical loading axial and tilted implants had nearly identical peak micromotion (19 vs 17 µm), but under oblique loading the tilted implant showed 19% lower peak micromotion than the axial implant (56 vs 75 µm), while abutment displacement was consistently larger for tilted than axial implants under both loading directions.

Loading direction, not implant angulation, is the dominant determinant of micromotion magnitude, and abutment displacement does not track with maximum micromotion — a single-implant, small-sample (n=4/group) bench study without a physiologic bone-density range, so findings support rather than conclusively confirm clinical immediate-loading protocols.

## 세줄요약

인공 골블록(폴리우레탄 폼) 8개·NobelReplace Tapered Groovy 임플란트 8개(축방향 4개, 원위 30° 경사 4개, 11×4.5mm)를 이용한 즉시부하 (immediate loading) 임플란트 in vitro + 유한요소분석 (Finite Element Analysis, FEA) 비교연구 — 180N 수직하중 vs 45° 근원심 사선하중.

사선하중은 각도와 무관하게 수직하중보다 2.6~3.9배 큰 최대 미세운동 (micromotion)을 유발했으며, 수직하중에서는 축방향·경사 임플란트의 최대 미세운동이 거의 동일(19 vs 17µm)했으나 사선하중에서는 경사 임플란트가 축방향보다 19% 낮은 최대 미세운동(56 vs 75µm)을 보였고, 지대주 변위 (abutment displacement)는 하중방향과 무관하게 경사 임플란트가 축방향보다 항상 컸다.

미세운동의 크기는 임플란트 각도보다 하중 방향이 더 크게 좌우하며 지대주 변위와 최대 미세운동은 서로 비례하지 않는다 — 단일 임플란트 디자인·소표본(군당 n=4) 벤치 연구로 임상 즉시부하 프로토콜에 대한 결론적 근거보다는 가설 지지 수준으로 해석해야 한다.

## Summary

Sahoo et al. (2024) combined a physical in vitro bench experiment with nonlinear finite element analysis (FEA) to compare axial versus 30° distally tilted implants under simulated immediate-loading conditions. Eight NobelReplace Tapered Groovy implants (4 axial, 4 distally tilted) were placed in synthetic polyurethane-foam bone blocks with a fiber-reinforced epoxy cortical shell, then loaded with 180 N either vertically or at a 45° mesiodistal oblique angle. Abutment displacement and micromotion (relative implant-bone displacement) were measured experimentally and predicted by FEA, with the two datasets cross-validated. The central finding runs counter to the intuitive assumption that tilting always worsens biomechanics: under oblique loading — the loading direction that produced by far the largest micromotion values overall — the tilted implant showed 19% lower peak micromotion than the axial implant, while under vertical loading the two designs were nearly indistinguishable. Abutment displacement, in contrast, was consistently larger for the tilted implant regardless of loading direction, showing that displacement and micromotion are not interchangeable proxies for implant stability.

## Key Contributions
- Head-to-head axial vs 30°-tilted comparison of BOTH abutment displacement and micromotion under two loading directions, in a design that pairs physical bench testing with FEA validation.
- Counter-intuitive result: tilted implants can show LOWER peak micromotion than axial implants under oblique loading (19% lower), consistent with prior work by Sugiura et al. (2017, not yet in this wiki) that the authors cite as validating precedent.
- Demonstrates that loading direction (oblique vs vertical) is a larger driver of micromotion magnitude (2.6–3.9× difference) than implant angulation itself.
- Locates maximum micromotion near the implant apex.

## Methodology
In vitro experimental bench study (8 polyurethane-foam bone blocks, density 0.32 g/cm³, with epoxy-fiber cortical shell) cross-validated against nonlinear FEA. 8 NobelReplace Tapered Groovy implants (Nobel Biocare), 11 mm × 4.5 mm — 4 axial, 4 distally tilted 30° — loaded with 180 N vertically and at 45° mesiodistal oblique angle. Abutment displacement and micromotion measured in both the physical experiment and the FEA simulation; reliability assessed by relative error between the two.

## Results

| Metric | Axial (vertical) | Tilted (vertical) | Axial (oblique) | Tilted (oblique) |
|---|---|---|---|---|
| Max micromotion (µm) | 19 | 17 | 75 | 56 |
| Abutment displacement, in vitro (µm) | 346.6 | 414.5 | 548.0 | 668.0 |
| Abutment displacement, FEA (µm) | 281.4 | 312.4 | 558.2 | ~602.6* |

(*Source Table 2 prints "6026" for this cell — almost certainly a typesetting artifact; see [[implants/sahoo-2024-finite-element-analysis-influence-implant]] for the flagged discrepancy.)

- Oblique-load micromotion was 2.6–3.9× greater than vertical-load micromotion in both groups.
- Tilted-implant micromotion was 19% lower than axial under oblique load; nearly identical under vertical load.
- Abutment displacement was always larger for tilted than axial implants, independent of loading direction — displacement and micromotion diverged as outcome measures.

## Related Papers
- [[implants/murat-2025-all-on-4-implant-angulation-load-direction-fea]] — companion FEA angulation × load-direction study; Murat 2025 quantifies cortical bone von Mises stress (BL load direction > implant angle as stress driver), while Sahoo 2024 quantifies micromotion/displacement (oblique load direction dominates micromotion; tilt lowers oblique micromotion) — same load-direction-matters theme, different outcome metric.
- [[overviews/tilted-axial-implant-angled-abutment-overview]] — existing synthesis of tilted-vs-axial implant biomechanics (stress, MBL, survival); this paper adds a micromotion/primary-stability lens specific to immediate loading that the overview does not yet cover.
- [[implants/eskan-2020-tapered-implants-full-arch-immediate-function]] — clinical full-arch immediate-loading outcomes with tilted implants (MBL, survival); this paper provides the underlying bench-level biomechanical rationale (micromotion) for why tilted implants can perform clinically comparably under immediate loading.
