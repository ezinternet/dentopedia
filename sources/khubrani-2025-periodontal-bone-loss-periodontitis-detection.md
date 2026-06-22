---
title: "Detection of periodontal bone loss and periodontitis from 2D dental radiographs via machine learning and deep learning: systematic review employing APPRAISE-AI and meta-analysis"
authors: Khubrani YH, Thomas D, Slator PJ, White RD, Farnell DJJ
year: 2025
doi: 10.1093/dmfr/twae070
category: [artificial-intelligence]
source_collection: pubmed-text
full_text: true
pmid: "39656957"
pmcid: "PMC11979759"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11979759/
text_path: /Users/oracleneo/llm-wiki/papers/khubrani-2025-periodontal-bone-loss-periodontitis-detection.txt
text_filename: khubrani-2025-periodontal-bone-loss-periodontitis-detection.txt
---

## Why Ingested

Fills the periodontal-AI gap in the `artificial-intelligence` category — a 30-study SR with a 10-study meta-analysis using the dedicated APPRAISE-AI critical-appraisal tool, giving both performance (sens 87%, spec 76%) and a rigorous evidence-quality verdict (no study reached "very high" quality). Reinforces the "image diagnosis mature, but reporting weak" thesis of [[overviews/ai-dentistry-reviews-2024-2025-synthesis]] and pairs with the caries SR+MA [[artificial-intelligence/abbott-2024-ai-platforms-dental-caries-detection]].

## One-line Summary

SR (30 studies) + meta-analysis (10 studies) of ML/DL for detecting periodontal bone loss/periodontitis on 2D panoramic and periapical radiographs, appraised with APPRAISE-AI: pooled sensitivity 87% (95% CI 80–93%), specificity 76% (69–81%), accuracy 84% (75–91%); 0 studies reached "very high" quality (only 7/30 "high").

## 한줄요약

2D 파노라마·치근단 방사선에서 치주 골소실/치주염을 검출하는 머신러닝·딥러닝의 체계적 문헌고찰(30편)+메타분석(10편), APPRAISE-AI 평가: 통합 민감도 87%, 특이도 76%, 정확도 84%이나 "매우 높은 품질" 연구는 0편(고품질 7/30).

## 1. Document Information

- **Type**: Systematic review + meta-analysis (FULL TEXT, PMC).
- **Journal**: Dentomaxillofacial Radiology 2025;54(2):89–108. PROSPERO CRD42023480552.
- **PMID**: 39656957 · **PMCID**: PMC11979759 · **DOI**: [10.1093/dmfr/twae070](https://doi.org/10.1093/dmfr/twae070)
- **Search**: 5 databases (Medline, Embase, Scopus, WoS, Cochrane), Jan 1990 – Jan 2024.

## 2. Key Contributions

- Uses **APPRAISE-AI**, a quantitative AI-study appraisal tool, instead of the generic QUADAS-2 — sharper read of clinical-decision-support quality.
- Pooled diagnostic performance for periodontal-bone AI via `metaprop` (R).
- Explicit quality stratification: 1 very-low, 3 low, 19 intermediate, 7 high, **0 very-high**.

## 3. Methodology and Architecture

- 30 articles in qualitative synthesis; 10 eligible for meta-analysis (proportion meta-analysis, `metaprop`).
- Models span CNN/R-CNN, SVM, and other ML on panoramic + periapical radiographs.
- Outcomes: sensitivity, specificity, precision/PPV, NPV, F1, AUC; segmentation via IoU/Dice.

## 4. Key Results and Benchmarks

| Metric | Pooled (95% CI) |
|---|---|
| Sensitivity | 87% (80–93%) |
| Specificity | 76% (69–81%) |
| Accuracy | 84% (75–91%) |

APPRAISE-AI quality: very-low 1 (3.3%), low 3 (10.0%), intermediate 19 (63.3%), high 7 (23.3%), very-high 0.

## 5. Limitations and Future Work

- Performance varies; specificity (76%) notably lower than sensitivity.
- AI studies lack transparency; reporting standards need improvement (no very-high-quality study).
- Heterogeneity in datasets and metrics limits comparability.

## 6. Related Work

- [[artificial-intelligence/abbott-2024-ai-platforms-dental-caries-detection]] — sibling caries SR+MA.
- [[overviews/ai-dentistry-reviews-2024-2025-synthesis]] — mature image diagnosis, weak reporting.

## 7. Glossary

- **APPRAISE-AI**: Appraisal tool for quantitative evaluation of AI studies for clinical decision support.
- **metaprop**: R command for proportion meta-analysis.
- **IoU / Dice**: segmentation overlap metrics.
