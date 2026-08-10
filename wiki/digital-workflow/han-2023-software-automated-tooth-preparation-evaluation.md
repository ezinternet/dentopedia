---
title: "Feasibility of software-based assessment for automated evaluation of tooth preparation for dental crown by using a computational geometric algorithm"
authors: Han S, Yi Y, Revilla-León M, Yilmaz B, Yoon HI
year: 2023
date: 2023-07-21
doi: 10.1038/s41598-023-39089-3
source: han-2023-software-automated-tooth-preparation-evaluation.md
category: [digital-workflow]
evidence_level: in-vitro
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

## Three-line Summary

In-vitro feasibility study (Sci Rep 2023, 35 graduate-student mandibular first molars prepared for single-unit anatomic-contour crowns) validating software-based automated evaluation (SAE) using a computational geometric algorithm for crown tooth preparation quality assessment.

SAE achieved perfect intra-rater agreement on all criteria (vs moderate-to-good for human digitally assisted evaluation, DAE); SAE–DAE inter-rater agreement was almost-perfect to substantial, with no significant score difference (p>0.05); mean TOC was 26.44° (MD) and 18.60° (BL), occlusal reduction 1.39–1.88 mm per cusp.

SAE removes the human-assigned-metric bottleneck of existing digital preparation tools and offers reliable, reproducible objective quantification of TOC and occlusal reduction for dental education feedback and clinical skill assessment.

## 세줄요약

In-vitro 타당성 연구 (Sci Rep 2023, 대학원생이 형성한 하악 제1대구치 35개): computational geometric algorithm 기반 자동 평가(SAE)로 단일 관 형성치의 품질 평가 타당성 검증.

SAE는 모든 기준에서 완벽한 검사자 내 일치도(DAE의 moderate~good 대비); SAE–DAE 검사자 간 일치도는 거의 완벽~상당 수준이며 점수 차이 비유의(p>0.05); 평균 TOC 26.44°(MD)·18.60°(BL), 교합면 삭제량 큐스프당 1.39–1.88 mm.

SAE는 기존 디지털 형성 도구의 인간 의존적 측정 병목을 제거하고 TOC·교합면 삭제량의 신뢰성 있는 객관적 정량화를 치과 교육 피드백 및 임상 술기 평가에 제공한다.

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
