---
title: "Effective dose estimation in cone-beam computed tomography for dental use by Monte-Carlo simulation optimizing calculation numbers using a step-and-shoot method"
authors: Ozaki Y, Watanabe H, Kurabayashi T
year: 2021
doi: 10.1259/dmfr.20210084
category: [radiology]
pdf_path: /Users/oracleneo/llm-wiki/papers/ozaki-2021-cbct-effective-dose-monte-carlo-simulation.pdf
pdf_filename: ozaki-2021-cbct-effective-dose-monte-carlo-simulation.pdf
source_collection: external
---

## Why Ingested

radiology 카테고리 CBCT MC 선량추정의 계산효율·FOV 전략 근거. [[radiology/lee-2019-cbct-dose-osl-monte-carlo-comparison]]의 측정-MC 비교와 방법 보완, '큰 FOV 1회 vs 작은 FOV 다회'의 방호적 함의를 정량.

## One-line Summary

Step-and-shoot Monte Carlo CBCT dose (PHITS, Accuitomo): 5° (large FOV)/10° (small FOV) steps suffice; six small FOVs ≈1.2× one large FOV.

## 한줄요약

step-and-shoot 몬테카를로 CBCT 선량(PHITS, Accuitomo): 대형 FOV 5°·소형 10° 간격이면 충분. 소형 6회 ≈ 대형 1회의 1.2배.

## 1. Document Information

- Title: Effective dose estimation in cone-beam computed tomography for dental use by Monte-Carlo simulation optimizing calculation numbers using a step-and-shoot method
- Authors: Ozaki Y, Watanabe H, Kurabayashi T
- Year: 2021 | Journal: Dentomaxillofacial Radiology | DOI: 10.1259/dmfr.20210084
- Study type: in-vitro

## 2. Key Contributions

- Step-and-shoot MC (PHITS) validated against TLD for 3DX Accuitomo FPD8.
- Step intervals of 5° (large FOV) and 10° (small FOV) reproduce 1°-step accuracy at lower compute cost.
- Six small FOVs ≈ 1.2× the effective dose of one equivalent large FOV → multiple small scans favored only when justified.

## 3. Methodology and Architecture

PHITS MC of large vs small FOV against virtual Rando phantom; confirmed vs TLD; tested coarsened angular sampling.

## 4. Key Results and Benchmarks

Provides a compute-efficient MC recipe and the practical insight that tiling small FOVs is not necessarily dose-sparing vs one large FOV.

## 5. Limitations and Future Work

Single CBCT model; phantom; effective dose only.

## 6. Related Work

- [[radiology/lee-2019-cbct-dose-osl-monte-carlo-comparison]] — 측정 vs MC dosimetry 비교
- [[radiology/kaasalainen-2021-dental-cone-beam-ct-updated-review]] — CBCT dosimetry 리뷰

## 7. Glossary

- Step-and-shoot: 단계별 정지 후 조사 방식
- PHITS: 입자·중이온 수송 MC 코드
- FOV: 촬영 용적
