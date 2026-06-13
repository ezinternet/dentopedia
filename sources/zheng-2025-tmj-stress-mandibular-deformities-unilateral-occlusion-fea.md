---
title: "Temporomandibular joint stress analysis of patients with different mandibular deformities during unilateral molar occlusion"
authors: Chongke Zheng, Jingheng Shu, Bingmei Shao, Zhan Liu
year: 2025
doi: 10.1080/10255842.2024.2361778
category: [tmj]
pdf_path: /Users/oracleneo/llm-wiki/papers/zheng-2025-tmj-stress-mandibular-deformities-unilateral-occlusion-fea.pdf
pdf_filename: zheng-2025-tmj-stress-mandibular-deformities-unilateral-occlusion-fea.pdf
source_collection: external
---

## Why Ingested

기존 [[wiki/tmj/zheng-2023-unilateral-chewing-tmj-structure-tmd-review]] (편측저작이 TMJ·TMD에 미치는 영향, narrative review)와 [[wiki/tmj/decarli-2023-mandibular-condyle-unilateral-masticatory-function]] (rat unilateral mastication condyle change)이 제기한 "편측저작·비대칭 부하가 TMJ 위험을 높인다"는 가설을, 본 유한요소해석(FEA) 논문은 실제 환자 기반 모델로 정량화한다. 하악 기형 유형(전돌·후퇴·편위)별 단일 대구치 교합 시 TMJ 응력을 직접 비교해, 어느 기형이 TMD 위험이 가장 큰지 biomechanical 근거를 제공.

> NOTE: This source is extracted from the Taylor & Francis abstract/landing page only (full text behind paywall). Methodology specifics (mesh, material properties, exact stress values in MPa) are NOT recoverable — only the structured Abstract, keywords, sample composition, and qualitative conclusions are captured. Quantitative stress magnitudes are absent.

## One-line Summary

Finite-element analysis of 35 patient-derived models (11 asymptomatic, 10 mandibular prognathism, 5 retrusion, 9 deviation) under unilateral molar occlusion: mandibular deformity raises condyle and articular-disc stress, with facial asymmetry (deviation) producing the highest TMJ stress and therefore the highest TMD risk; chewing on the non-deviated side worsens it.

## 한줄요약

유한요소해석(FEA) 연구 (환자 기반 모델 35개: 무증상 11, 하악전돌 10, 하악후퇴 5, 하악편위 9). 단일 대구치 교합 시 하악 기형이 과두·관절원판 응력을 높이며, 특히 안면 비대칭(편위)이 TMJ 응력을 가장 크게 증가시켜 TMD 위험이 가장 높다. 편위 환자가 비편위측으로 씹으면 응력이 더 커진다.

## 1. Document Information

- **Title**: Temporomandibular joint stress analysis of patients with different mandibular deformities during unilateral molar occlusion
- **Authors**: Chongke Zheng, Jingheng Shu, Bingmei Shao, Zhan Liu
- **Journal**: Computer Methods in Biomechanics and Biomedical Engineering, 2025;28(14):2162–2169
- **DOI**: 10.1080/10255842.2024.2361778
- **Received** 22 Feb 2024; **Accepted** 26 May 2024; **Published online** 04 Jun 2024
- **Study type**: Finite-element analysis (FEA), patient-derived models
- **Funding**: National Natural Science Foundation of China (12202298, 31670963); Sichuan University–Yibin cooperation projects
- **Extraction note**: Abstract/landing page only — quantitative results not available.

## 2. Key Contributions

- Compares TMJ stress across the three common mandibular deformities — prognathism (전돌), retrusion (후퇴), and deviation (편위/facial asymmetry) — within a single FEA framework using patient-derived models, plus an asymptomatic control group.
- Isolates the clinically common loading scenario of **unilateral molar occlusion** (rather than symmetric/bilateral occlusion) as the condition of interest for masticatory function.
- Ranks TMD risk by deformity type: facial asymmetry (deviation) > prognathism/retrusion, identifying the deviation patient as the highest-risk phenotype.
- Yields an actionable chewing-side recommendation: deviation patients should chew **bilaterally or on the deviated side**, because chewing on the **non-deviated side** elevates TMJ stress further.

## 3. Methodology and Architecture

- **Subjects**: 35 individuals total — 11 asymptomatic controls, 10 mandibular prognathism, 5 mandibular retrusion, 9 mandibular deviation.
- **Models**: Finite-element (FE) models corresponding to unilateral molar occlusion were constructed for each subject (patient-specific geometry).
- **Loading condition**: Unilateral molar occlusion (single posterior occlusal contact scenario representative of mastication).
- **Outcomes assessed**: Stress on the mandibular condyle and the articular disc of the TMJ; comparison between non-deviated-side vs deviated-side chewing in the deviation group.
- Mesh details, material property assignment, boundary conditions, and numerical stress magnitudes are not recoverable from the abstract.

## 4. Key Results and Benchmarks

Qualitative (no numeric stress values available in abstract):

- Mandibular deformity **increases** pressure on the condyle and articular disc during unilateral molar occlusion (vs asymptomatic).
- **Facial asymmetry (deviation) significantly increases TMJ stress** compared with mandibular protrusion (prognathism) or retraction (retrusion).
- In deviation patients, chewing on the **non-deviated side** leads to **higher** TMJ stress than chewing on the deviated side.
- **Conclusion**: Patients with mandibular deviation have the **highest risk of TMD**; recommendation is to chew bilaterally or on the deviated side.

## 5. Limitations and Future Work

- Small and unequal subgroup sizes (retrusion n=5, deviation n=9, prognathism n=10) limit statistical power and generalizability.
- FEA is a computational idealization: results depend on material assumptions and boundary conditions that are unverified against in-vivo measurement.
- Abstract reports only directional/qualitative findings; without numeric stress values, effect magnitudes cannot be appraised.
- No clinical TMD outcome correlation — stress is a surrogate, not a measured pain/dysfunction endpoint.
- Full-text methodology (mesh convergence, validation) could not be extracted.

## 6. Related Work

- [[wiki/tmj/zheng-2023-unilateral-chewing-tmj-structure-tmd-review]] — narrative review of chewing-side preference effects on TMJ/TMD; this FEA quantifies that hypothesis.
- [[wiki/tmj/decarli-2023-mandibular-condyle-unilateral-masticatory-function]] — animal model of unilateral mastication condylar remodeling; converging biological evidence.
- [[wiki/tmj/radej-2023-condylar-displacement-malocclusion-cr-mip-sr]] — malocclusion and condylar displacement; deformity–TMJ loading link.

## 7. Glossary

- **FEA (Finite-element analysis / 유한요소해석)**: Numerical method partitioning a structure into small elements to compute stress/strain under load.
- **Mandibular prognathism (하악전돌)**: Forward protrusion of the mandible.
- **Mandibular retrusion (하악후퇴)**: Posterior/backward position of the mandible.
- **Mandibular deviation (하악편위)**: Lateral asymmetry of the mandible (facial asymmetry).
- **Unilateral molar occlusion (편측 대구치 교합)**: Occlusal loading on posterior teeth of one side only.
- **Articular disc (관절원판)**: Fibrocartilaginous disc between condyle and temporal bone in the TMJ.
- **TMD (Temporomandibular disorder, 턱관절장애)**: Disorders of the TMJ and masticatory muscles.
