---
title: "Deep Learning for Detection of Periapical Radiolucent Lesions: A Systematic Review and Meta-analysis of Diagnostic Test Accuracy"
authors: Sadr S, Mohammad-Rahimi H, Motamedian SR, Zahedrozegar S, Motie P, Vinayahalingam S, Dianat O, Nosrat A
year: 2023
doi: 10.1016/j.joen.2022.12.007
category: [artificial-intelligence]
source_collection: pubmed-text
full_text: false
pmid: "36563779"
source_url: https://doi.org/10.1016/j.joen.2022.12.007
text_path: /Users/oracleneo/llm-wiki/papers/sadr-2022-deep-learning-periapical-radiolucent-lesions.txt
text_filename: sadr-2022-deep-learning-periapical-radiolucent-lesions.txt
---

## Why Ingested

Adds the endodontic arm to the `artificial-intelligence` category — the strongest periapical-lesion DL meta-analysis available, notable for being the only dental-AI SR in this cluster to reach **GRADE "high" certainty** (pooled sensitivity 0.925). Anchors the diagnostic-AI maturity claim of [[overviews/ai-dentistry-reviews-2024-2025-synthesis]] in endodontics and complements [[artificial-intelligence/abbott-2024-ai-platforms-dental-caries-detection]].

## One-line Summary

SR+MA of diagnostic test accuracy (18 studies SR, 6 pooled; QUADAS-2 + GRADE) of deep learning vs expert clinicians for detecting periapical radiolucent lesions: pooled sensitivity 0.925 (95% CI 0.862–0.960), specificity 0.852 (0.810–0.885), diagnostic OR 71.7; GRADE certainty "high"; most studies had risk of bias.

## 한줄요약

치근단 방사선투과 병소를 검출하는 딥러닝 vs 전문의의 진단정확도 체계적 문헌고찰+메타분석(SR 18편, 풀링 6편; QUADAS-2+GRADE): 통합 민감도 0.925, 특이도 0.852, 진단 오즈비 71.7, GRADE 근거수준 "높음"(이 클러스터 중 유일).

## 1. Document Information

- **Type**: SR + meta-analysis of diagnostic test accuracy. [ABSTRACT-ONLY — full text not retrieved]
- **Journal**: Journal of Endodontics 2023;49(3):248–261.e3 (e-pub Dec 2022).
- **PMID**: 36563779 · **DOI**: [10.1016/j.joen.2022.12.007](https://doi.org/10.1016/j.joen.2022.12.007)
- **Search**: Medline, Embase, Scopus, Google Scholar, arXiv.

## 2. Key Contributions

- Only dental-AI review in this wiki cluster reaching **GRADE "high"** certainty for its pooled estimate.
- Hierarchical-logistic-regression meta-analysis (bivariate) — methodologically sound for diagnostic accuracy.
- Subgroup analyses by image modality (PA, panoramic, CBCT) and DL task (classification/segmentation/detection).

## 3. Methodology and Architecture

- 932 screened → 18 SR → 6 meta-analysis; QUADAS-2; hierarchical logistic regression.
- DL models compared against expert clinicians; Egger's test for publication bias (P=.82, none).

## 4. Key Results and Benchmarks

| Metric | Pooled (95% CI) |
|---|---|
| Sensitivity | 0.925 (0.862–0.960) |
| Specificity | 0.852 (0.810–0.885) |
| Positive LR | 6.261 |
| Negative LR | 0.087 |
| Diagnostic OR | 71.692 |

GRADE certainty: high. Risk of bias: 6/18 low, 12/18 with risk.

## 5. Limitations and Future Work

- Most studies had risk of bias; lack of prospective studies.
- Only 6/18 poolable.

## 6. Related Work

- [[artificial-intelligence/abbott-2024-ai-platforms-dental-caries-detection]] — caries detection SR+MA.
- [[artificial-intelligence/khubrani-2025-periodontal-bone-loss-periodontitis-detection]] — periodontal-bone SR+MA.
- [[endodontics/diagnosis/dumitrescu-2021-cbct-periapical-lesions-maxillary-sinus]] — periapical lesion CBCT diagnosis context.

## 7. Glossary

- **Diagnostic OR**: ratio of odds of positivity in diseased vs non-diseased.
- **GRADE**: Grading of Recommendations Assessment, Development and Evaluation.
- **Hierarchical logistic regression**: bivariate model for diagnostic-accuracy meta-analysis.
