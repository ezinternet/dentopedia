---
title: "Feasibility of software-based assessment for automated evaluation of tooth preparation for dental crown by using a computational geometric algorithm"
authors: Han S, Yi Y, Revilla-León M, Yilmaz B, Yoon HI
year: 2023
date: 2023-07-21
doi: 10.1038/s41598-023-39089-3
source: han-2023-software-automated-tooth-preparation-evaluation.md
category: [digital-workflow]
confidence: in-vitro
pdf_path: /Users/oracleneo/llm-wiki/papers/han-2023-software-automated-tooth-preparation-evaluation.pdf
pdf_filename: han-2023-software-automated-tooth-preparation-evaluation.pdf
source_collection: external
tags: [cad-cam, tooth-preparation, total-occlusal-convergence, automated-evaluation, dental-education]
relations:
  - type: extends
    target: revilla-leon-2025-tooth-preparation-factors-ios-accuracy-sr
  - type: reinforces
    target: sadid-zadeh-2020-teeth-prepared-students-cadcam
---

## One-line Summary

In-vitro feasibility study (35 graduate-prepared mandibular first molars) showing software-based automated evaluation (SAE) of crown tooth preparation via a computational geometric algorithm achieves perfect intra-rater agreement (vs moderate-to-good for human digitally assisted evaluation, DAE) with almost-perfect SAE–DAE agreement.

## 한줄요약

In-vitro 타당성 연구(대학원생 형성 하악 제1대구치 35개): computational geometric algorithm 기반 자동 평가(SAE)는 crown 형성치의 교합면 삭제량·TOC를 완벽한 재현성으로 평가했고, 인간의 디지털 보조 평가(DAE, moderate~good)보다 일관됐으며 SAE–DAE 간 일치도도 거의 완벽했다.

## Summary

This study proposes and validates **software-based automated evaluation (SAE)** of tooth preparation quality. A computational geometric algorithm auto-locates the measurement region and computes prepared-tooth dimensions (occlusal reduction per cusp, TOC in MD/BL planes, margin width) in a mathematically optimized model — removing the human-assigned-metric bottleneck of existing digital tools (E4D Compare, CEREC PrepCheck, Prepassistant).

On 35 scanned graduate-student crown preparations, SAE produced **identical scores across three rounds (perfect intra-rater agreement)**, whereas human DAE was only moderate-to-good. SAE–DAE inter-rater agreement was almost-perfect to substantial (moderate only for MD TOC), with no significant score difference (p>0.05). SAE thus offers a reliable, reproducible objective measurement of exactly the geometry parameters (TOC, occlusal reduction) that [[digital-workflow/revilla-leon-2025-tooth-preparation-factors-ios-accuracy-sr]] flags as IOS-accuracy determinants, and addresses the rater-inconsistency problem implicit in human assessment like [[digital-workflow/sadid-zadeh-2020-teeth-prepared-students-cadcam]].

## Key Contributions

- Introduces an automated, algorithm-driven preparation-quality evaluator (SAE).
- Demonstrates perfect intra-rater consistency vs moderate-to-good for human DAE.
- Provides objective quantification of TOC and occlusal reduction usable for dental education and clinical skill feedback.

## Methodology

- Design: In-vitro feasibility / methods validation.
- Sample: 35 mandibular first molars prepared for single-unit anatomic-contour crowns by graduate students; each digitized.
- Criteria: occlusal reduction (MB/DB/ML/DL cusps), TOC (MD, BL planes), margin width.
- Analysis: intra-rater (SAE, DAE) and inter-rater (SAE vs DAE) agreement; weighted Cohen's kappa; α=0.05.

## Results

- SAE: robust on all preparations; perfect intra-rater agreement on every criterion.
- DAE: moderate-to-good intra-rater reliability (none excellent).
- SAE vs DAE: almost-perfect (ML/DL reduction), substantial (MB/DB reduction, BL TOC), moderate (MD TOC); no significant score difference (p>0.05).
- Mean SAE values: occlusal reduction 1.39/1.60/1.88/1.59 mm (MB/DB/ML/DL); TOC 26.44° (MD), 18.60° (BL); margin width 0.36 mm.

## Related Papers

- [[digital-workflow/revilla-leon-2025-tooth-preparation-factors-ios-accuracy-sr]] — extends; objectively measures the TOC/occlusal-reduction geometry parameters that SR ties to IOS accuracy
- [[digital-workflow/sadid-zadeh-2020-teeth-prepared-students-cadcam]] — reinforces; automates the preparation-quality scoring that study did with a manual faculty rubric, solving rater inconsistency
- [[digital-workflow/alkadi-2023-intraoral-scanner-accuracy-factors]] — related; preparation geometry as a digital-workflow accuracy factor
- [[digital-workflow/singh-2025-intraoral-scanners-accuracy-umbrella-review]] — related; broad IOS accuracy context
