---
title: "Can artificial intelligence-driven cephalometric analysis replace manual tracing? A systematic review and meta-analysis"
authors: Hendrickx J, Gracea RS, Vanheers M, Winderickx N, Preda F, Shujaat S, Jacobs R
year: 2024
date: 2024-08-01
doi: 10.1093/ejo/cjae029
source: hendrickx-2024-ai-cephalometric-analysis-manual-tracing.md
category: [artificial-intelligence]
confidence: sr+ma
source_collection: pubmed-text
full_text: true
pmid: "38895901"
pmcid: "PMC11185929"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11185929/
text_path: /Users/oracleneo/llm-wiki/papers/hendrickx-2024-ai-cephalometric-analysis-manual-tracing.txt
text_filename: hendrickx-2024-ai-cephalometric-analysis-manual-tracing.txt
tags: [ai, deep-learning, cephalometric, landmark-detection, orthodontics, cbct, quadas-2, diagnostic-accuracy]
relations:
  - type: reinforces
    target: khubrani-2025-periodontal-bone-loss-periodontitis-detection
  - type: applies-to
    target: digital-workflow-decision-ladder
---

## One-line Summary

SR+MA (34 studies; 27 on 2D cephalograms, 7 on 3D-CBCT; QUADAS-2) of AI cephalometric landmark detection: pooled 2D mean radial error 1.39 mm (95% CI 0.85–1.92), below the clinically accepted 2 mm threshold, in <1 min; 3D error 1.0–5.8 mm (not poolable); most studies high risk of bias.

## 한줄요약

인공지능(Artificial Intelligence, AI) 두부계측 계측점 자동검출 체계적 문헌고찰+메타분석(34편; 2D 27편, 3D-CBCT 7편): 2D 평균 방사 오차 1.39 mm로 임상 허용 2 mm 미만·1분 이내, 3D는 1.0–5.8 mm로 더 부정확하고 풀링 불가, 대부분 비뚤림 위험 높음. (Based on articles retrieved from PubMed)

## Summary

According to PubMed, Hendrickx et al. (2024, European Journal of Orthodontics) asked whether AI-driven cephalometric landmarking can replace manual tracing. Searching to Jan 2024, they included 34 studies (27 on 2D lateral cephalograms, 7 on 3D-CBCT), appraised with QUADAS-2. Meta-analysis of 2D success-detection rate gave a **pooled mean radial error of 1.39 mm (95% CI 0.85–1.92)** — comfortably below the **2 mm clinical acceptability threshold** — with automated landmarking completing in **under one minute**. 3D-CBCT could not be meta-analyzed (heterogeneity); qualitatively its error ranged **1.0–5.8 mm**, i.e. weaker and more variable than 2D. Most studies carried a **high risk of bias** in patient selection (27) and reference standard (29). [DOI](https://doi.org/10.1093/ejo/cjae029)

This is arguably the clearest "AI is already clinically usable" datapoint in the dental-AI literature: 2D cephalometric landmarking meets the accepted accuracy bar and is dramatically faster than manual tracing — though 3D and bias concerns temper a full "replace manual tracing" verdict.

## Key Contributions

- Benchmarks against the clinically meaningful 2 mm threshold (not just raw error).
- Cleanly separates poolable 2D from non-poolable 3D-CBCT performance.
- Quantifies the time advantage (<1 min vs manual tracing).

## Methodology

- 34 studies (27 × 2D, 7 × 3D-CBCT); CNN-based landmark detectors.
- QUADAS-2 risk of bias; 2D meta-analysis on mean radial error + standard error.

## Results

| Outcome | Result |
|---|---|
| 2D pooled mean radial error | 1.39 mm (0.85–1.92) — below 2 mm |
| 3D-CBCT error | 1.0–5.8 mm (qualitative) |
| Time | <1 min |
| Risk of bias | High in selection (27/34) and reference (29/34) |

## Related Papers

- [[artificial-intelligence/khubrani-2025-periodontal-bone-loss-periodontitis-detection]] — sibling image-diagnosis SR+MA.
- [[artificial-intelligence/abbott-2024-ai-platforms-dental-caries-detection]] — caries detection SR+MA.
- [[overviews/digital-workflow-decision-ladder]] — digital orthodontic/planning workflow this applies to.
- [[overviews/ai-dentistry-reviews-2024-2025-synthesis]] — image diagnosis as the mature AI domain.
