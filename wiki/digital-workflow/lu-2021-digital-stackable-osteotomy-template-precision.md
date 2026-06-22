---
title: "Immediate Precision of the Digital Osteotomy Template in the Digital Stackable Template: A Clinical Study"
authors: Lu Jiayi et al.
year: 2021
date: 2021-01-01
doi: 10.7518/hxkq.2021.06.018
source: lu-2021-digital-stackable-osteotomy-template-precision.md
category: [digital-workflow]
confidence: case-report
pdf_path: /Users/oracleneo/llm-wiki/papers/lu-2021-digital-stackable-osteotomy-template-precision.pdf
pdf_filename: lu-2021-digital-stackable-osteotomy-template-precision.pdf
source_collection: external
tags: [digital-workflow, stackable-template, osteotomy-guide, immediate-implant, accuracy, CBCT, 3D-printing, chinese-paper]
---

## One-line Summary
Case report (Chinese paper, n=4 edentulous patients): accuracy assessment of the osteotomy layer of a 3D-printed digital stackable guide (osteotomy + implant guide + provisional restoration integrated) — mean volumetric deviation 492.94 mm³ (21.21% of planned volume), mean displacement 0.0248 mm (sign-cancellation artifact), mean angular deviation 6.03° (range 1.39°–10.52°); n=4 with one large outlier distorting the mean.

## 한줄요약
증례 보고 (case report, 중국어 논문), n=4 무치악 환자 — 절골 가이드 + 식립 가이드 + 임시수복물 일체형 3D 프린팅 디지털 스택형 가이드 (digital stackable template)의 절골층 정확도 평가: 평균 체적 편차 492.94 mm³ (예정 체적의 21.21%)·평균 변위 0.0248 mm (실은 부호 상쇄로 인한 평균, 개별 ±0.5 mm)·평균 각도 편차 6.03° (범위 1.39°~10.52°). n=4·1건 큰 outlier (MU 1419.54 mm³)로 평균이 왜곡됨.

## Summary
Lu et al. report a 4-patient clinical case series evaluating the **osteotomy layer** accuracy of a three-tier digital stackable template (osteotomy guide → implant guide → provisional restoration), an integrated workflow for immediate implant + immediate provisional in edentulous patients with insufficient vertical restorative space. The osteotomy layer is the reference plane that locates the rest of the stack, so its accuracy is the upper bound on the entire system's accuracy.

After CBCT + intraoral scan + digital wax-up + B-VTRS (bone-level vertical height of target restorative space)-driven planning, three-layer guides (in resin or metal) were 3D printed and used intraoperatively. Pre and post-op CBCT were superimposed to compute volumetric, displacement, and angular deviations of the actual osteotomy vs the preset osteotomy.

Mean values: volume deviation 492.94 mm³ (21.21% of preset volume), displacement 0.0248 mm, angle 6.03°. However, with n=4 and one clear outlier (case MU — maxillary metal-printed guide, 1419.54 mm³ volume deviation and 8.07° angle deviation), these means are not robust. The displacement "mean" of 0.0248 mm is especially misleading — individual cases range from −0.5394 mm to +0.5033 mm; the small mean is sign cancellation, not small absolute error.

This paper should be read as a **technique-feasibility case series**, not as an accuracy benchmark.

## Key Contributions
- Documents a three-tier stackable digital guide concept with the osteotomy layer as the system reference.
- First reported accuracy figures for the osteotomy guide layer specifically (prior literature focused on implant guides).
- Provides B-VTRS-driven prosthetic-material decision thresholds (>15 mm metal-acrylic, 13–15 mm PFM, 11–13 mm monolithic zirconia).
- Per-case data table comparing resin vs metal-printed guides on upper and lower arches.

## Methodology
4 edentulous patients (2 max, 2 mand, age 43–57, mean 50), all suitable for immediate implant + immediate provisional and requiring intraoperative osteotomy due to insufficient vertical restorative space. Workflow: CBCT → intraoral scan (3Shape Trios) → ExoCAD wax-up → BlueSky registration → Geomagic Studio guide assembly → 3D print (resin or metal) → guided osteotomy → guided implant placement → immediate provisional. Pre/post CBCT superimposition for accuracy metrics.

## Results
Per-case (Table 1):

| Case | Print material | Site | Volume dev (mm³) | Displacement (mm) | Angle (°) |
|---|---|---|---|---|---|
| RU | resin | maxilla | 254.72 | 0.5033 | 4.12 |
| RL | resin | mandible | 84.51 | −0.0733 | 1.39 |
| MU | metal | maxilla | 1419.54 | −0.5394 | 8.07 |
| ML | metal | mandible | 213.00 | 0.0104 | 10.52 |
| **Mean** | | | **492.94** | **−0.0248** | **6.03** |

- Volume deviation ≈ 21.21% of preset volume.
- Angle deviation range 1.39° to 10.52° (wide).
- Case MU is a clear outlier — drives the mean volume deviation up; without it, mean drops to ~184 mm³.

## Limitations
- **n = 4** — sub-pilot scale; no inference about accuracy distribution.
- Mean displacement of 0.0248 mm is a sign-cancellation artifact; absolute deviations are up to ±0.5 mm.
- One large outlier (MU) inflates volume deviation mean to 492.94 mm³.
- Angle deviations up to 10.52° are clinically meaningful — could mis-place subsequent implants.
- No control (freehand osteotomy or single-purpose guide) — accuracy claimed in isolation.
- Single center, single team, single workflow.
- Chinese-language paper; full discussion content not surfaceable from English abstract — body sections (esp. detailed registration and superimposition methods) not extractable from available text.

## Living Document Notes
- Cite as **technique feasibility** for stackable guides, not as accuracy benchmark.
- Always report the **per-case table**, not just means — with n=4 and one outlier, the means hide more than they reveal.
- The 6.03° mean angle deviation is on the high end of what literature considers acceptable for fully-guided implant surgery — flag this whenever discussing stackable workflows.
- Update this page when a prospective multi-center accuracy study of stackable guides appears.

## Related Papers
- [[overviews/digital-workflow-decision-ladder]] — broader category for guided surgery accuracy literature
- (Add links to specific implant-guide accuracy studies as they enter the wiki)
