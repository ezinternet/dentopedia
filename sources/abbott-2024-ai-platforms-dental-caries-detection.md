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

## Three-line Summary

Systematic review + meta-analysis (8 databases, Jan 2000–Mar 2024; 2,538 identified → 45 included, 21 AI platforms; QUADAS-2 + CLAIM quality appraisal; 7 studies poolable) evaluating AI diagnostic accuracy for dental caries on radiographs and clinical images — abstract-only ingest.

Pooled sensitivity 76% (95% CI 65–85%), specificity 91% (86–95%), AUC 92% (89–94%); accuracy ranged 41.5–98.6% across 21 platforms; AI on clinical images showed superior sensitivity and equal specificity vs bitewing radiography; high between-study heterogeneity throughout.

Only 7/45 studies were poolable, limiting the meta-analytic precision; standardized datasets and CLAIM-compliant reporting are needed before these pooled estimates can guide platform selection in practice.

## 세줄요약

체계적 문헌고찰+메타분석 (8개 데이터베이스, 2000년 1월–2024년 3월; 2,538편 확인 → 45편 포함, AI 플랫폼 21종; QUADAS-2+CLAIM 평가; 풀링 7편) — 방사선·임상 이미지 기반 치아우식 AI 진단 정확도 평가 (초록만 수집).

통합 민감도 76%(95% CI 65–85%), 특이도 91%(86–95%), AUC 92%(89–94%); 21종 플랫폼 간 정확도 41.5–98.6%로 편차 큼; 임상 이미지의 AI가 방사선 대비 민감도 우수; 모든 분석에서 높은 이질성.

풀링 가능 연구 7/45편으로 메타분석 정밀도 제한 — 플랫폼 선택에 활용하려면 표준화 데이터셋과 CLAIM 준수 보고가 선결 과제.

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
