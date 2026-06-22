---
title: "Artificial Intelligence Platforms in Dental Caries Detection: A Systematic Review and Meta-Analysis"
authors: Abbott LP, Saikia A, Anthonappa RP
year: 2024
date: 2024-12-12
doi: 10.1016/j.jebdp.2024.102077
source: abbott-2024-ai-platforms-dental-caries-detection.md
category: [artificial-intelligence]
confidence: sr+ma
source_collection: pubmed-text
full_text: false
pmid: "39947783"
source_url: https://doi.org/10.1016/j.jebdp.2024.102077
text_path: /Users/oracleneo/llm-wiki/papers/abbott-2024-ai-platforms-dental-caries-detection.txt
text_filename: abbott-2024-ai-platforms-dental-caries-detection.txt
tags: [ai, caries-detection, deep-learning, cnn, diagnostic-accuracy, quadas-2, claim, radiograph]
relations:
  - type: reinforces
    target: garg-2026-artificial-intelligence-pediatric-dentistry-umbrella-review
---

## One-line Summary

SR+MA (45 studies qualitative, 7 pooled; QUADAS-2 + CLAIM) of AI platforms for dental caries detection: pooled sensitivity 76% (95% CI 65–85%), specificity 91% (86–95%), AUC 92% (89–94%); accuracy ranged 41.5–98.6% across 21 platforms with high heterogeneity.

## 한줄요약

치아우식 검출 인공지능(Artificial Intelligence, AI) 플랫폼 체계적 문헌고찰+메타분석(정성 45편, 풀링 7편): 통합 민감도 76%, 특이도 91%, 곡선하면적(AUC) 92%이나 플랫폼 21종 간 정확도 41.5–98.6%로 이질성 큼. (Based on articles retrieved from PubMed; abstract-only)

## Summary

According to PubMed, Abbott et al. (2024) systematically reviewed AI for dental caries detection across 8 databases (2000–March 2024), identifying 45 studies (33 radiograph, 12 clinical-image datasets) using 21 distinct AI platforms. Quality was appraised with QUADAS-2 and the CLAIM checklist. A meta-analysis of 7 studies yielded pooled **sensitivity 76% (95% CI 65–85%)**, **specificity 91% (86–95%)**, and **AUC 92% (89–94%)**. The headline practical finding: AI applied to **clinical (photographic) images** showed superior sensitivity and equal specificity compared with bitewing radiography. Accuracy varied widely (41.5–98.6%) across platforms, with high heterogeneity. [DOI](https://doi.org/10.1016/j.jebdp.2024.102077)

This is the adult-population quantitative complement to the pediatric CNN figures in the wiki (Garg umbrella review: sens/spec 80–83%, AUC 0.87–0.91).

## Key Contributions

- First poolable quantitative accuracy estimate for dental caries AI in this evidence cluster.
- Dual appraisal (QUADAS-2 + CLAIM) — risk of bias plus AI-reporting completeness.
- Modality signal: clinical images ≥ bitewing for AI sensitivity.

## Methodology

- 8 databases; 2538 → 45 included; 21 AI platforms; 7 studies in meta-analysis.
- Architectures span SVM, ANN, CNN/DCNN; tasks: detection, segmentation, classification, prediction.

## Results

| Metric | Pooled (95% CI) |
|---|---|
| Sensitivity | 76% (65–85%) |
| Specificity | 91% (86–95%) |
| AUC | 92% (89–94%) |
| Accuracy range | 41.5–98.6% |

High heterogeneity; only 7/45 studies poolable — a recurring AI-evidence-quality caveat.

## Related Papers

- [[artificial-intelligence/khubrani-2025-periodontal-bone-loss-periodontitis-detection]] — sibling image-diagnosis SR+MA (periodontal bone loss; APPRAISE-AI).
- [[artificial-intelligence/garg-2026-artificial-intelligence-pediatric-dentistry-umbrella-review]] — pediatric caries CNN figures (reinforced here for adults).
- [[overviews/ai-dentistry-reviews-2024-2025-synthesis]] — image diagnosis as the most mature AI domain.
