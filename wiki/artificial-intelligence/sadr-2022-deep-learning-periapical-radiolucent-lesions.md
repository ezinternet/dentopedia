---
title: "Deep Learning for Detection of Periapical Radiolucent Lesions: A Systematic Review and Meta-analysis of Diagnostic Test Accuracy"
authors: Sadr S, Mohammad-Rahimi H, Motamedian SR, Zahedrozegar S, Motie P, Vinayahalingam S, Dianat O, Nosrat A
year: 2023
date: 2023-03-01
doi: 10.1016/j.joen.2022.12.007
source: sadr-2022-deep-learning-periapical-radiolucent-lesions.md
category: [artificial-intelligence]
confidence: sr+ma
source_collection: pubmed-text
full_text: false
pmid: "36563779"
source_url: https://doi.org/10.1016/j.joen.2022.12.007
text_path: /Users/oracleneo/llm-wiki/papers/sadr-2022-deep-learning-periapical-radiolucent-lesions.txt
text_filename: sadr-2022-deep-learning-periapical-radiolucent-lesions.txt
tags: [ai, deep-learning, periapical-lesion, endodontics, diagnostic-accuracy, quadas-2, grade, cbct]
relations:
  - type: reinforces
    target: abbott-2024-ai-platforms-dental-caries-detection
---

## One-line Summary

SR+MA of diagnostic test accuracy (18 SR, 6 pooled; QUADAS-2 + GRADE) of deep learning vs expert clinicians for periapical radiolucent lesion detection: pooled sensitivity 0.925 (95% CI 0.862–0.960), specificity 0.852 (0.810–0.885), diagnostic OR 71.7, GRADE certainty "high" — the only dental-AI review in this cluster reaching high certainty.

## 한줄요약

치근단 방사선투과 병소 검출 딥러닝 vs 전문의 진단정확도 체계적 문헌고찰+메타분석(SR 18편, 풀링 6편): 통합 민감도 0.925, 특이도 0.852, 진단 오즈비 71.7, GRADE 근거수준 "높음" — 다만 대부분 연구가 비뚤림 위험. (Based on articles retrieved from PubMed; abstract-only)

## Summary

According to PubMed, Sadr et al. (2023, Journal of Endodontics) meta-analyzed deep-learning detection of periapical (PA) radiolucent lesions on dental radiographs versus expert clinicians. From 932 screened, 18 studies entered the SR and 6 the meta-analysis (hierarchical logistic regression). Pooled **sensitivity 0.925 (95% CI 0.862–0.960)**, **specificity 0.852 (0.810–0.885)**, positive LR 6.26, negative LR 0.087, **diagnostic odds ratio 71.7**. No publication bias (Egger P=.82). Notably, the GRADE certainty of evidence was **"high"** — the strongest evidence grade among the dental-AI reviews in this wiki. Caveats: most studies had risk of bias and there was a lack of prospective studies. Subgroups covered PA, panoramic, and CBCT modalities and classification/segmentation/detection tasks. [DOI](https://doi.org/10.1016/j.joen.2022.12.007)

## Key Contributions

- High pooled sensitivity (0.925) with GRADE "high" certainty — unusual robustness for dental AI.
- Methodologically sound bivariate (hierarchical logistic regression) diagnostic-accuracy meta-analysis.
- Modality and task subgroup analyses.

## Methodology

- 932 → 18 SR → 6 meta-analysis; QUADAS-2; GRADE; Egger's test.
- DL benchmarked against expert clinicians.

## Results

| Metric | Pooled (95% CI) |
|---|---|
| Sensitivity | 0.925 (0.862–0.960) |
| Specificity | 0.852 (0.810–0.885) |
| Diagnostic OR | 71.692 |

GRADE: high. 6/18 low risk of bias.

## Related Papers

- [[artificial-intelligence/abbott-2024-ai-platforms-dental-caries-detection]] — sibling caries SR+MA (reinforced).
- [[artificial-intelligence/khubrani-2025-periodontal-bone-loss-periodontitis-detection]] — periodontal-bone SR+MA.
- [[endodontics/diagnosis/dumitrescu-2021-cbct-periapical-lesions-maxillary-sinus]] — periapical lesion CBCT diagnosis context.
- [[overviews/ai-dentistry-reviews-2024-2025-synthesis]] — image diagnosis as the mature AI domain.
