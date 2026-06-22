---
title: "Detection of periodontal bone loss and periodontitis from 2D dental radiographs via machine learning and deep learning: systematic review employing APPRAISE-AI and meta-analysis"
authors: Khubrani YH, Thomas D, Slator PJ, White RD, Farnell DJJ
year: 2025
date: 2025-02-01
doi: 10.1093/dmfr/twae070
source: khubrani-2025-periodontal-bone-loss-periodontitis-detection.md
category: [artificial-intelligence]
confidence: sr+ma
source_collection: pubmed-text
full_text: true
pmid: "39656957"
pmcid: "PMC11979759"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11979759/
text_path: /Users/oracleneo/llm-wiki/papers/khubrani-2025-periodontal-bone-loss-periodontitis-detection.txt
text_filename: khubrani-2025-periodontal-bone-loss-periodontitis-detection.txt
tags: [ai, deep-learning, machine-learning, periodontitis, alveolar-bone-loss, appraise-ai, diagnostic-accuracy, panoramic, periapical]
relations:
  - type: reinforces
    target: abbott-2024-ai-platforms-dental-caries-detection
---

## One-line Summary

SR (30 studies) + meta-analysis (10 studies) of ML/DL for periodontal bone loss/periodontitis detection on 2D panoramic + periapical radiographs, appraised with APPRAISE-AI: pooled sensitivity 87% (95% CI 80–93%), specificity 76% (69–81%), accuracy 84% (75–91%); only 7/30 studies "high" quality, none "very high".

## 한줄요약

2D 방사선에서 치주 골소실·치주염을 검출하는 머신러닝·딥러닝 체계적 문헌고찰(30편)+메타분석(10편), APPRAISE-AI 평가: 통합 민감도 87%, 특이도 76%, 정확도 84%이나 고품질 연구 7/30·최고품질 0편 — 성능은 유망, 보고 투명성은 미흡. (Based on articles retrieved from PubMed)

## Summary

According to PubMed, Khubrani et al. (2025, Dentomaxillofacial Radiology) reviewed AI for assessing alveolar bone loss/periodontitis on dental panoramic and periapical radiographs, searching 5 databases (1990–Jan 2024). Thirty articles entered the systematic review; 10 were poolable. Using the **APPRAISE-AI** tool (purpose-built for AI clinical-decision-support studies), they graded 1 study very-low, 3 low, 19 intermediate, 7 high, and **none very-high** quality. The proportion meta-analysis (R `metaprop`) gave **sensitivity 87% (95% CI 80–93%)**, **specificity 76% (69–81%)**, and **accuracy 84% (75–91%)**. Deep learning "shows much promise" for evaluating periodontal bone levels, but performance varied and reporting standards need improvement. [DOI](https://doi.org/10.1093/dmfr/twae070)

The lower specificity (76%) vs sensitivity (87%) means more false positives — clinically, AI here is better as a screening/triage flag than a confirmatory read.

## Key Contributions

- Adopts APPRAISE-AI rather than generic QUADAS-2 for sharper AI-quality grading.
- Quantitative pooled performance for periodontal-bone AI.
- Documents the transparency/reporting gap (zero very-high-quality studies).

## Methodology

- 5 databases; 30 in qualitative synthesis, 10 in meta-analysis.
- Panoramic + periapical 2D radiographs; CNN/R-CNN, SVM, other ML.
- Proportion meta-analysis via `metaprop`; sensitivity analyses for outliers.

## Results

| Metric | Pooled (95% CI) |
|---|---|
| Sensitivity | 87% (80–93%) |
| Specificity | 76% (69–81%) |
| Accuracy | 84% (75–91%) |

APPRAISE-AI quality: 7/30 high, 19/30 intermediate, 0 very-high.

## Related Papers

- [[artificial-intelligence/abbott-2024-ai-platforms-dental-caries-detection]] — sibling caries SR+MA (reinforced pairing).
- [[artificial-intelligence/hendrickx-2024-ai-cephalometric-analysis-manual-tracing]] — image-diagnosis SR+MA in orthodontics.
- [[overviews/ai-dentistry-reviews-2024-2025-synthesis]] — image diagnosis mature, reporting weak.
- [[periodontics/caton-2018-classification-scheme-periodontal-periimplant-diseases]] — clinical periodontitis staging/classification context.
