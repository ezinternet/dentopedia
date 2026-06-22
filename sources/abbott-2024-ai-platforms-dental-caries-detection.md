---
title: "Artificial Intelligence Platforms in Dental Caries Detection: A Systematic Review and Meta-Analysis"
authors: Abbott LP, Saikia A, Anthonappa RP
year: 2024
doi: 10.1016/j.jebdp.2024.102077
category: [artificial-intelligence]
source_collection: pubmed-text
full_text: false
pmid: "39947783"
source_url: https://doi.org/10.1016/j.jebdp.2024.102077
text_path: /Users/oracleneo/llm-wiki/papers/abbott-2024-ai-platforms-dental-caries-detection.txt
text_filename: abbott-2024-ai-platforms-dental-caries-detection.txt
---

## Why Ingested

The `artificial-intelligence` category held only pediatric pages; this is the strongest quantitative anchor for the most mature dental-AI task — caries detection on radiographs/clinical images — providing a pooled meta-analysis (sens 76%, spec 91%, AUC 92%) that the [[overviews/ai-dentistry-reviews-2024-2025-synthesis]] flagged as the image-diagnosis domain but lacked a dedicated page for. Extends [[artificial-intelligence/garg-2026-artificial-intelligence-pediatric-dentistry-umbrella-review]] (pediatric caries CNN) to the general adult evidence base.

## One-line Summary

Systematic review + meta-analysis (45 studies qualitative, 7 pooled; QUADAS-2 + CLAIM) of AI platforms for dental caries detection: pooled sensitivity 76% (95% CI 65–85%), specificity 91% (86–95%), AUC 92% (89–94%), with high heterogeneity and accuracy ranging 41.5–98.6% across 21 platforms.

## 한줄요약

치아우식 검출 인공지능(AI) 플랫폼의 체계적 문헌고찰+메타분석(정성 45편, 풀링 7편): 통합 민감도 76%, 특이도 91%, 곡선하면적(AUC) 92%이나 플랫폼 21종 간 정확도 41.5–98.6%로 이질성이 큼.

## 1. Document Information

- **Type**: Systematic review + meta-analysis (diagnostic accuracy). [ABSTRACT-ONLY — full text not retrieved]
- **Journal**: Journal of Evidence-Based Dental Practice 2024;25(1):102077
- **PMID**: 39947783 · **DOI**: [10.1016/j.jebdp.2024.102077](https://doi.org/10.1016/j.jebdp.2024.102077)
- **Search window**: January 2000 – March 2024, 8 databases.

## 2. Key Contributions

- Quantitative pooled estimate of AI caries-detection accuracy (most prior dental-AI caries reviews were narrative/umbrella).
- Dual quality appraisal: QUADAS-2 (risk of bias) **and** the CLAIM checklist (AI-reporting completeness).
- Head-to-head signal: AI on **clinical images** had superior sensitivity and equal specificity vs bitewing radiography.

## 3. Methodology and Architecture

- 8 databases (Scopus, WoS, MEDLINE, ERIC, IEEE Xplore, ScienceDirect, DOAJ, JSTOR).
- 2538 identified → 45 included (33 radiograph datasets, 12 clinical-image datasets); 21 distinct AI platforms.
- Meta-analysis on 7 studies with extractable contingency data.

## 4. Key Results and Benchmarks

| Metric | Pooled estimate (95% CI) |
|---|---|
| Sensitivity | 76% (65–85%) |
| Specificity | 91% (86–95%) |
| AUC | 92% (89–94%) |
| Accuracy range (all platforms) | 41.5–98.6% |

High between-study heterogeneity throughout.

## 5. Limitations and Future Work

- Only 7/45 studies poolable → meta-analysis is a thin slice.
- High heterogeneity (platform, dataset, imaging modality) limits a single generalizable number.
- Need standardized datasets/reporting (CLAIM adherence) for fair platform comparison.

## 6. Related Work

- [[artificial-intelligence/khubrani-2025-periodontal-bone-loss-periodontitis-detection]] — sibling image-diagnosis SR+MA (periodontal bone loss).
- [[overviews/ai-dentistry-reviews-2024-2025-synthesis]] — image diagnosis is the most mature AI domain.

## 7. Glossary

- **QUADAS-2**: Quality Assessment of Diagnostic Accuracy Studies tool.
- **CLAIM**: Checklist for Artificial Intelligence in Medical imaging (reporting standard).
- **AUC**: Area Under the (ROC) Curve.
- **CNN**: Convolutional Neural Network.
