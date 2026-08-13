---
title: "Effective dose estimation in cone-beam computed tomography for dental use by Monte-Carlo simulation optimizing calculation numbers using a step-and-shoot method"
authors: Ozaki Y, Watanabe H, Kurabayashi T
year: 2021
date: 2021-01-01
doi: 10.1259/dmfr.20210084
source: ozaki-2021-cbct-effective-dose-monte-carlo-simulation.md
category: [radiology]
evidence_level: in-vitro
pdf_path: /Users/oracleneo/llm-wiki/papers/ozaki-2021-cbct-effective-dose-monte-carlo-simulation.pdf
pdf_filename: ozaki-2021-cbct-effective-dose-monte-carlo-simulation.pdf
source_collection: external
tags: []
relations:
  - type: refines
    target: lee-2019-cbct-dose-osl-monte-carlo-comparison
---

## Three-line Summary

In-vitro Monte Carlo study (PHITS code) using a step-and-shoot method with a virtual Rando phantom to estimate effective dose for large and small FOV CBCT scans on a 3DX Accuitomo FPD8, validated against TLD measurements.

Angular step intervals of 5° (large FOV) and 10° (small FOV) reproduced 1°-step accuracy at reduced computational cost; tiling six small FOVs yielded ~1.2× the effective dose of one equivalent large FOV scan.

This method provides a compute-efficient MC recipe for CBCT dose estimation and demonstrates that multiple small-FOV scans are not necessarily dose-sparing compared to a single large-FOV acquisition.

## 세줄요약

가상 Rando 팬텀과 PHITS 코드를 이용한 step-and-shoot 몬테카를로 방법으로 3DX Accuitomo FPD8의 대형·소형 FOV CBCT 유효선량을 추정하고 TLD 측정값으로 검증한 체외 연구.

대형 FOV 5°·소형 FOV 10° 각도 간격이 1° 간격 수준의 정확도를 재현하면서 계산 비용 절감; 소형 FOV 6회 촬영 ≈ 대형 FOV 1회의 약 1.2배 유효선량.

효율적인 MC 선량 추정 레시피를 제공하고, 소형 FOV 반복 촬영이 대형 FOV 1회보다 선량을 줄인다고 볼 수 없음을 실증.

## Summary

Provides a compute-efficient MC recipe and the practical insight that tiling small FOVs is not necessarily dose-sparing vs one large FOV.

## Key Contributions

- Step-and-shoot MC (PHITS) validated against TLD for 3DX Accuitomo FPD8.
- Step intervals of 5° (large FOV) and 10° (small FOV) reproduce 1°-step accuracy at lower compute cost.
- Six small FOVs ≈ 1.2× the effective dose of one equivalent large FOV → multiple small scans favored only when justified.

## Methodology

PHITS MC of large vs small FOV against virtual Rando phantom; confirmed vs TLD; tested coarsened angular sampling.

## Results

Provides a compute-efficient MC recipe and the practical insight that tiling small FOVs is not necessarily dose-sparing vs one large FOV.

## Related Papers

- [[radiology/lee-2019-cbct-dose-osl-monte-carlo-comparison]] — 측정 vs MC dosimetry 비교
- [[radiology/kaasalainen-2021-dental-cone-beam-ct-updated-review]] — CBCT dosimetry 리뷰
