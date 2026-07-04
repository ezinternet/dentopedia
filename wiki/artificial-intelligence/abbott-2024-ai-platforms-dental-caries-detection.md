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

## Three-line Summary

SR+MA (45 studies qualitative, 7 pooled; QUADAS-2 + CLAIM) of AI platforms for dental caries detection across 8 databases (2000–March 2024), spanning 21 distinct AI platforms and 33 radiograph + 12 clinical-image datasets.

Pooled sensitivity 76% (95% CI 65–85%), specificity 91% (86–95%), AUC 92% (89–94%); accuracy ranged 41.5–98.6% across platforms with high heterogeneity; AI on clinical photographs showed superior sensitivity to bitewing radiography.

Only 7 of 45 studies were poolable — high heterogeneity and varying platform architectures limit generalizability, and standardized reporting (CLAIM) compliance was inconsistent.

## 세줄요약

8개 데이터베이스(2000–2024년 3월), 21종 AI 플랫폼, 방사선 33편+임상사진 12편 포함 치아우식 검출 인공지능(Artificial Intelligence, AI) 플랫폼 체계적 문헌고찰+메타분석(정성 45편, 풀링 7편).

통합 민감도 76%(95% CI 65–85%), 특이도 91%(86–95%), 곡선하면적(AUC) 92%(89–94%); 플랫폼 간 정확도 41.5–98.6%로 이질성 높으며, 임상 사진 AI가 교익 방사선보다 민감도 우수.

45편 중 풀링 가능한 연구는 7편뿐 — 높은 이질성과 플랫폼 아키텍처 다양성으로 일반화가 제한되며 CLAIM 보고 준수도 불균등.

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
