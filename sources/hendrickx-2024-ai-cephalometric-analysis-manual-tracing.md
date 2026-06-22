---
title: "Can artificial intelligence-driven cephalometric analysis replace manual tracing? A systematic review and meta-analysis"
authors: Hendrickx J, Gracea RS, Vanheers M, Winderickx N, Preda F, Shujaat S, Jacobs R
year: 2024
doi: 10.1093/ejo/cjae029
category: [artificial-intelligence]
source_collection: pubmed-text
full_text: true
pmid: "38895901"
pmcid: "PMC11185929"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11185929/
text_path: /Users/oracleneo/llm-wiki/papers/hendrickx-2024-ai-cephalometric-analysis-manual-tracing.txt
text_filename: hendrickx-2024-ai-cephalometric-analysis-manual-tracing.txt
---

## Why Ingested

Adds the orthodontics/treatment-planning arm to the `artificial-intelligence` category — an SR+MA showing AI cephalometric landmarking on 2D images meets the clinically accepted <2 mm threshold (1.39 mm) in seconds, the clearest "AI already clinically usable" datapoint among dental-AI tasks. Extends the image-diagnosis maturity claim in [[overviews/ai-dentistry-reviews-2024-2025-synthesis]] into orthodontics and complements [[overviews/digital-workflow-decision-ladder]].

## One-line Summary

SR+MA (34 studies; 27 on 2D cephalograms, 7 on 3D-CBCT; QUADAS-2) of AI automated cephalometric landmark detection: pooled 2D mean radial error 1.39 mm (95% CI 0.85–1.92), below the clinically accepted 2 mm threshold, in <1 min; 3D error 1.0–5.8 mm (not poolable); most studies high risk of bias in patient selection.

## 한줄요약

인공지능(AI) 자동 두부계측 계측점 검출의 체계적 문헌고찰+메타분석(34편; 2D 27편, 3D-CBCT 7편): 2D 평균 방사 오차 1.39 mm로 임상 허용 기준 2 mm 미만이며 1분 이내 처리, 다만 대부분 연구가 환자 선택 비뚤림 위험 높음.

## 1. Document Information

- **Type**: Systematic review + meta-analysis (FULL TEXT, PMC).
- **Journal**: European Journal of Orthodontics 2024;46(4):cjae029. PROSPERO CRD42022328800.
- **PMID**: 38895901 · **PMCID**: PMC11185929 · **DOI**: [10.1093/ejo/cjae029](https://doi.org/10.1093/ejo/cjae029)
- **Search**: PubMed, WoS, Embase, grey literature, up to Jan 2024.

## 2. Key Contributions

- Benchmarks AI landmarking against the clinically meaningful **2 mm success threshold**, not just abstract error.
- Separates 2D (poolable) from 3D-CBCT (too heterogeneous to pool) performance.
- Quantifies the time advantage: automated landmarking <1 min vs manual tracing.

## 3. Methodology and Architecture

- 34 studies (27 × 2D lateral cephalograms, 7 × 3D-CBCT).
- QUADAS-2 risk of bias; meta-analysis on 2D success-detection rate using mean radial error + standard error.
- Deep-learning landmark detectors (CNN-based).

## 4. Key Results and Benchmarks

| Outcome | Result |
|---|---|
| 2D pooled mean radial error | 1.39 mm (95% CI 0.85–1.92) — below 2 mm threshold |
| 3D-CBCT landmark error | 1.0–5.8 mm (qualitative; not poolable) |
| Processing time | <1 min (2D and 3D) |
| Risk of bias | High in patient selection (n=27) and reference standard (n=29) |

## 5. Limitations and Future Work

- High risk of bias in data selection and reference-standard domains.
- 3D-CBCT performance heterogeneous and weaker; cannot be pooled.
- Generalizability/robustness across populations needs validation.

## 6. Related Work

- [[artificial-intelligence/khubrani-2025-periodontal-bone-loss-periodontitis-detection]] — image-diagnosis SR+MA (periodontal).
- [[overviews/digital-workflow-decision-ladder]] — digital orthodontic/planning workflow.

## 7. Glossary

- **Mean radial error (MRE)**: average Euclidean distance between predicted and reference landmark.
- **2 mm threshold**: conventional clinical acceptability limit for cephalometric landmarking.
- **CBCT**: Cone-Beam Computed Tomography.
