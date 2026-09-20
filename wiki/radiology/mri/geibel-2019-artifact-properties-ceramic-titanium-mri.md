---
title: "Artifact Properties of Dental Ceramic and Titanium Implants in MRI"
authors: Margit-Ann Geibel, Benjamin Gelißen, Anna-Katinka Bracher, Volker Rasche
year: 2019
date: 2018-11-12
doi: 10.1055/a-0755-2374
source: geibel-2019-artifact-properties-ceramic-titanium-mri.md
category: radiology/mri
evidence_level: in-vitro
pdf_path: /Users/oracleneo/llm-wiki/papers/geibel-2019-artifact-properties-ceramic-titanium-mri.pdf
pdf_filename: geibel-2019-artifact-properties-ceramic-titanium-mri.pdf
source_collection: external
tags: [mri, artifacts, titanium implant, zirconia implant, implant imaging, in-vitro]
relations:
  - type: extends
    target: overviews/zirconia-implant-clinical-outcomes
  - type: extends
    target: implants/surface/shetty-2026-titanium-vs-zirconia-implants-umbrella
  - type: provides-context
    target: radiology/wamasing-2018-imaging-bifid-mandibular-canal
---

## Three-line Summary
- In-vitro study: 21 dental implants (7 ceramic/zirconia, 14 titanium) embedded in agarose, scanned at 3 T with three isotropic 3D sequences (FFE, SE, UTE); implant volumes segmented and compared to manufacturer theoretical volumes (relative error).
- Ceramic implants were artifact-free with mean relative volume errors of 5.4 ± 2.3% (UTE) to 6.5 ± 4.3% (FFE) and no significant sequence difference; titanium implants gave mean errors of 1314 ± 350% (FFE), 1398 ± 562% (UTE), 2157 ± 810% (SE) with non-evaluable periphery in every case.
- MRI is a viable radiation-free option for ceramic-implant imaging (peri-implantitis, healing monitoring) but unsuitable for titanium implants; UTE gave no significant artifact advantage over FFE.

## 세줄요약
- 체외 실험: 아가로오스에 매립한 임플란트 21개(세라믹/지르코니아 7, 티타늄 14)를 3T 등방성 3D 시퀀스 3종(FFE·SE·UTE)으로 스캔, 분할 부피로 이론 부피 대비 상대오차를 측정했다.
- 세라믹은 무아티팩트로 평균 부피 오차 FFE 6.5±4.3% ~ UTE 5.4±2.3%(시퀀스 간 유의차 없음)였지만, 티타늄은 FFE 1314±350%·UTE 1398±562%·SE 2157±810%로 전례에서 주변부 평가 불가였다.
- MRI는 세라믹 임플란트의 방사선 없는 평가 수단이 될 수 있으나 티타늄엔 부적합하고, UTE는 FFE 대비 아티팩트 개선의 유의한 이점이 없었다.

## Summary
An in-vitro study at Ulm University scanned 21 dental implants — 7 ceramic (zirconia: Ziterion ZI510H, BreDent white sky SKY4512C) and 14 titanium (BreDent bSKY series) — embedded in agarose on a clinical 3 T scanner (Philips Achieva) using three spatially isotropic 3D sequences: TSE (SE), steady-state FFE, and UTE (0.5 mm³ voxels). Artifact severity was quantified as the relative error between semiautomatically segmented MR implant volume and the manufacturer's theoretical volume. Ceramic implants were artifact-free in all cases with mean relative volume errors of only ~5–6.5% and showed no significant differences between sequences, allowing full evaluation of the implant–tissue transition. Titanium implants produced mean errors over 1000% (1314 ± 350% FFE to 2157 ± 810% SE) with the implant periphery unreadable in every case, although artifacts were localized rather than the long-range streak artifacts typical of CBCT. The authors conclude MRI is a radiation-free alternative for ceramic-implant follow-up (including peri-implantitis diagnosis) but currently unsuitable for titanium implants.

## Key Contributions
- Quantitative volume-error comparison (not just visual scoring) of MRI artifacts for ceramic vs titanium implants across three 3D sequences.
- Ceramic implant MRI volumes are position/orientation-independent (small SD), while titanium artifacts show strong orientation dependence.
- Artifacts for both materials were confined to the immediate implant vicinity — MRI artifacts are localized, unlike CBCT streak artifacts.
- UTE showed no significant artifact advantage over standard FFE for either material.

## Methodology
In-vitro agarose-phantom study; 3 T Philips Achieva; 21 implants (7 ceramic, 14 titanium), embedded in agarose and positioned in random orientation on a 2×2-channel carotid coil. Three spatially isotropic 3D sequences at 0.5 mm³ voxel size: T1-weighted TSE (TR/TE 419/11 ms, 4 echoes, BW 444.6 Hz, 25 min 8 s), FFE (5.5/2.0 ms, BW 1883.2 Hz, 2 min 38 s), UTE (12/0.14 ms, 3× oversampled, BW 656.5 Hz, 31 min 41 s). Volumes segmented with ITK-Snap region growing (manual seeds); primary outcome = relative volume error vs manufacturer theoretical volume; two-sided paired Student's t-test (p < 0.05 significant).

## Results

| Implant group (n) | Mean relative volume error FFE | Mean relative volume error SE | Mean relative volume error UTE | Periphery evaluation |
|---|---|---|---|---|
| Ceramic / zirconia (7) | 6.5 ± 4.3% | 6.4 ± 2% | 5.4 ± 2.3% | readable in all cases, no artifacts |
| Titanium (14) | 1314 ± 350% | 2157 ± 810% | 1398 ± 562% | non-evaluable in all cases |

- Ceramic: no significant difference between sequences; measured vs theoretical volume significant for FFE (p < 0.05) and SE (p < 0.05), not UTE (p = 0.06).
- Titanium: significant differences FFE vs SE (p < 0.001) and UTE vs SE (p < 0.01); FFE vs UTE not significant (p = 0.47); measured vs theoretical significant for all sequences (p < 0.001).
- Greatest titanium variability in SE, smallest in FFE (e.g., #6C: SE 3513.4% vs #6A: SE 1607.3% — orientation dependence).
- Replicate implant series (Table 7): titanium error FFE 1265–1825%, SE 2183–2853%, UTE 1487–1750%; ceramic error 5.1–6.0% across all sequences.

## Related Papers
- [[overviews/zirconia-implant-clinical-outcomes]] — zirconia implant survival/MBL/PROs; this paper adds the MR-imaging (artifact) axis to zirconia-implant properties.
- [[implants/surface/shetty-2026-titanium-vs-zirconia-implants-umbrella]] — titanium vs zirconia clinical-outcomes umbrella; consistent with zirconia being comparable or preferable, here on the imaging axis.
- [[radiology/wamasing-2018-imaging-bifid-mandibular-canal]] — diagnostic head/neck MRI imaging; this page supplies the implant-artifact counterpoint for MRI use around dental implants.
- [[radiology/dewake-2023-mri-occlusal-trauma-pdl]] — dental MRI application; ceramic-implant MRI compatibility extends MRI's dental diagnostic reach.