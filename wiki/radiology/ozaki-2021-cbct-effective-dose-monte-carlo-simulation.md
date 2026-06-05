---
title: "Effective dose estimation in cone-beam computed tomography for dental use by Monte-Carlo simulation optimizing calculation numbers using a step-and-shoot method"
authors: Ozaki Y, Watanabe H, Kurabayashi T
year: 2021
date: 2021-01-01
doi: 10.1259/dmfr.20210084
source: ozaki-2021-cbct-effective-dose-monte-carlo-simulation.md
category: [radiology]
confidence: in-vitro
pdf_path: /Users/oracleneo/llm-wiki/papers/ozaki-2021-cbct-effective-dose-monte-carlo-simulation.pdf
pdf_filename: ozaki-2021-cbct-effective-dose-monte-carlo-simulation.pdf
source_collection: external
tags: []
relations:
  - type: refines
    target: lee-2019-cbct-dose-osl-monte-carlo-comparison
---

## One-line Summary

Step-and-shoot Monte Carlo CBCT dose (PHITS, Accuitomo): 5° (large FOV)/10° (small FOV) steps suffice; six small FOVs ≈1.2× one large FOV.

## 한줄요약

step-and-shoot 몬테카를로 CBCT 선량(PHITS, Accuitomo): 대형 FOV 5°·소형 10° 간격이면 충분. 소형 6회 ≈ 대형 1회의 1.2배.

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
