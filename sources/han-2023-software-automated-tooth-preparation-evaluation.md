---
title: "Feasibility of software-based assessment for automated evaluation of tooth preparation for dental crown by using a computational geometric algorithm"
authors: Han S, Yi Y, Revilla-León M, Yilmaz B, Yoon HI
year: 2023
doi: 10.1038/s41598-023-39089-3
category: [digital-workflow]
pdf_path: /Users/oracleneo/llm-wiki/papers/han-2023-software-automated-tooth-preparation-evaluation.pdf
pdf_filename: han-2023-software-automated-tooth-preparation-evaluation.pdf
source_collection: external
---

## Why Ingested

[[wiki/digital-workflow/sadid-zadeh-2020-teeth-prepared-students-cadcam]]가 인간(faculty) 평가의 빈번한 형성 오류·rater 불일치를 보여줬다면, 본 in-vitro 연구는 **computational geometric algorithm으로 형성치(TOC·교합면 삭제량)를 자동·재현성 있게 평가**하는 software-based automated evaluation(SAE)의 타당성을 입증해 그 평가 일관성 문제의 해법을 제시한다. 또한 [[wiki/digital-workflow/revilla-leon-2025-tooth-preparation-factors-ios-accuracy-sr]]가 정의한 형성 geometry 파라미터(TOC, occlusal reduction)를 객관적으로 측정하는 방법론을 제공한다.

## One-line Summary

In-vitro feasibility study (35 mandibular first molars prepared by graduate students) proposing software-based automated evaluation (SAE) of crown tooth preparation via a computational geometric algorithm; SAE showed perfect intra-rater agreement (vs moderate-to-good for human digitally assisted evaluation) and almost-perfect SAE–DAE inter-rater agreement.

## 한줄요약

In-vitro 타당성 연구(대학원생이 형성한 하악 제1대구치 35개): computational geometric algorithm 기반 자동 평가(SAE)로 crown 형성치의 교합면 삭제량·축면 경사(TOC)를 평가했더니, 인간의 디지털 보조 평가(DAE)는 moderate~good 내적 일치였던 반면 SAE는 완벽한 내적 일치를 보였고 SAE–DAE 간 일치도도 거의 완벽했다.

## 1. Document Information

- **Title**: Feasibility of software-based assessment for automated evaluation of tooth preparation for dental crown by using a computational geometric algorithm
- **Authors**: Sangjun Han, Yuseung Yi, Marta Revilla-León, Burak Yilmaz, Hyung-In Yoon
- **Journal**: Scientific Reports 2023;13:11847
- **DOI**: 10.1038/s41598-023-39089-3
- **Type**: In-vitro feasibility / methods-validation study

## 2. Key Contributions

- Proposes **software-based automated evaluation (SAE)** of tooth preparation quality using a computational geometric algorithm that auto-defines the measurement region and computes prepared-tooth dimensions in a mathematically optimized model.
- Benchmarks SAE against **human-based digitally assisted evaluation (DAE)** by trained evaluators for reliability.

## 3. Methodology and Architecture

- 35 mandibular first molars prepared for single-unit anatomic-contour crowns by graduate students; each digitized (scanned).
- Evaluation criteria: occlusal reduction (per cusp: MB/DB/ML/DL) and total occlusal convergence (TOC) in MD and BL planes; margin width also reported.
- Intra-rater agreement (SAE and DAE) and inter-rater agreement (SAE vs DAE) analyzed (weighted Cohen's kappa; α = 0.05). Two null hypotheses: no difference in intra-rater agreement, and no difference in scores.

## 4. Key Results and Benchmarks

- SAE operated robustly on all 35 preparations; identical scores across 3 rounds (perfect intra-rater agreement on every criterion).
- DAE showed moderate-to-good intra-rater reliability (moderate for MB/DB cusp reduction and BL TOC; good for ML/DL cusp reduction and MD TOC; none excellent).
- Inter-rater (SAE vs DAE): almost-perfect for ML/DL cusp reduction; substantial for MB/DB cusp reduction and BL TOC; moderate for MD TOC. No significant SAE–DAE score difference (p>0.05).
- Mean measured values (SAE): occlusal reduction ≈1.39 mm (MB), 1.60 mm (DB), 1.88 mm (ML), 1.59 mm (DL); TOC 26.44° (MD) and 18.60° (BL); margin width ≈0.36 mm.
- First null hypothesis (intra-rater) rejected (SAE more consistent); second (scores) not rejected.

## 5. Limitations and Future Work

- In-vitro, single-institution graduate cohort; limited criteria (occlusal reduction, TOC, margin) — minimum reduction and other parameters not yet validated (true minimum reduction not always in central fossa).
- Generalizability to clinical preparations and broader criteria requires further study.

## 6. Related Work

- Extends prior digital-assessment tools (E4D Compare, CEREC PrepCheck, Prepassistant) that improved consistency over visual inspection but still depend on human-assigned metrics.

## 7. Glossary

- **SAE**: Software-based automated evaluation using a computational geometric algorithm.
- **DAE**: (Human-based) digitally assisted evaluation by trained raters with metrology software.
- **TOC (Total Occlusal Convergence)**: Combined angle of opposing axial walls.
- **Occlusal reduction**: Amount of tooth removed at cusp tips for restorative thickness.
- **Cohen's kappa (weighted)**: Agreement statistic correcting for chance.
