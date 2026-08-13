---
title: "Deep Learning for Detection of Periapical Radiolucent Lesions: A Systematic Review and Meta-analysis of Diagnostic Test Accuracy"
authors: Sadr S, Mohammad-Rahimi H, Motamedian SR, Zahedrozegar S, Motie P, Vinayahalingam S, Dianat O, Nosrat A
year: 2023
date: 2023-03-01
doi: 10.1016/j.joen.2022.12.007
source: sadr-2022-deep-learning-periapical-radiolucent-lesions.md
category: [artificial-intelligence]
evidence_level: sr+ma
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

## Three-line Summary

SR+MA of diagnostic test accuracy (18 SRs, 6 pooled; QUADAS-2 + GRADE) testing deep learning vs expert clinicians for periapical radiolucent lesion detection on dental radiographs (PA, panoramic, CBCT).

Pooled sensitivity 0.925 (95% CI 0.862–0.960), specificity 0.852 (0.810–0.885), diagnostic OR 71.7; GRADE certainty "high" — the only dental-AI SR in this wiki reaching high certainty.

Clinically, DL performs comparably to expert clinicians for PA lesion detection; most primary studies had high risk of bias and the SR was limited to 6/18 studies for meta-analysis, so caution in individual-model adoption is warranted.

## 세줄요약

치근단 방사선투과 병소 검출 딥러닝 vs 전문의 진단정확도 SR+MA (18편 SR, 6편 풀링; QUADAS-2 + GRADE); 파노라마·치근단·CBCT 다양식 포함.

통합 민감도 0.925(95% CI 0.862–0.960), 특이도 0.852(0.810–0.885), 진단 오즈비(diagnostic Odds Ratio, dOR) 71.7; GRADE 근거수준 "높음" — 이 wiki 치과 AI SR 중 유일한 high 등급.

딥러닝은 전문의와 유사한 수준으로 치근단 병소를 검출할 수 있으나, 대부분 연구가 비뚤림 위험이 높고 풀링 가능 연구가 6편에 불과해 개별 모델 임상 도입 시 신중이 필요하다.

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
