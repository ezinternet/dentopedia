---
title: "Efficacy of the Monte Carlo method and dose reduction strategies in paediatric panoramic radiography"
authors: Lee C, Park B, Lee SS, Kim JE, Han SS, Huh KH, Yi WJ, Heo MS, Choi SC
year: 2019
doi: 10.1038/s41598-019-46157-0
category: [radiology]
pdf_path: /Users/oracleneo/llm-wiki/papers/lee-2019-monte-carlo-paediatric-panoramic-dose-reduction.pdf
pdf_filename: lee-2019-monte-carlo-paediatric-panoramic-dose-reduction.pdf
source_collection: external
---

## Why Ingested

radiology 카테고리 파노라마 선량 저감의 인자별 정량근거. [[radiology/benchimol-2018-collimation-panoramic-effective-dose-reduction]]의 collimation 선량저감과 동일 기전(조사야 축소)을 인자분석으로 보강하고, MC 방법론을 [[radiology/lee-2019-cbct-dose-osl-monte-carlo-comparison]]와 공유.

## One-line Summary

Monte Carlo vs TLD for paediatric panoramic dose (MC 3.474 vs TLD 3.850 µSv); beam height is the dominant dose-reduction lever.

## 한줄요약

소아 파노라마 선량 MC vs TLD(MC 3.474 vs TLD 3.850 µSv). 빔 높이(beam height)가 선량 결정 최대 인자.

## 1. Document Information

- Title: Efficacy of the Monte Carlo method and dose reduction strategies in paediatric panoramic radiography
- Authors: Lee C, Park B, Lee SS, Kim JE, Han SS, Huh KH, Yi WJ, Heo MS, Choi SC
- Year: 2019 | Journal: Scientific Reports | DOI: 10.1038/s41598-019-46157-0
- Study type: in-vitro

## 2. Key Contributions

- Validated Monte Carlo against TLD for paediatric panoramic effective dose (MC 3.474 µSv vs TLD 3.850 µSv).
- Among 7 factors (36 simulations), beam height most strongly drives effective dose; rotation angle and focus-to-patient distance least influential.
- Short beam height = practical paediatric dose-reduction strategy.

## 3. Methodology and Architecture

MC simulation (validated vs TLD) of paediatric panoramic; 7 dose-determining factors each at 6 levels (36 runs); linear regression of each factor vs effective dose.

## 4. Key Results and Benchmarks

MC is a simpler, reliable alternative to TLD; collimating beam height (vertical field) is the highest-yield lever for cutting paediatric panoramic dose.

## 5. Limitations and Future Work

Phantom/simulation; single geometry family; effective dose not diagnostic-task outcome.

## 6. Related Work

- [[radiology/benchimol-2018-collimation-panoramic-effective-dose-reduction]] — 파노라마 collimation 선량저감
- [[radiology/lee-2019-cbct-dose-osl-monte-carlo-comparison]] — MC dosimetry 방법 (동일 1저자)

## 7. Glossary

- TLD (Thermoluminescent Dosimetry): 열형광선량계
- Beam height: 빔(수직 조사야) 높이
- Monte Carlo: 확률론적 선량 시뮬레이션
