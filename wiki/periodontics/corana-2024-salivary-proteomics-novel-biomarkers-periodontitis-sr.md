---
title: "Salivary Proteomics for Detecting Novel Biomarkers of Periodontitis: A Systematic Review"
authors: "Matteo Corana, Giacomo Baima, Giovanni Iaderosa, Francesco Franco, Jianjian Zhang, Giovanni Nicolao Berta, Federica Romano, Mario Aimetti"
year: 2024
date: 2024-12-02
doi: "10.1111/jre.13357"
source: corana-2024-salivary-proteomics-novel-biomarkers-periodontitis-sr.md
category: [periodontics]
evidence_level: sr
source_collection: pubmed-text
full_text: true
pmid: "39620241"
pmcid: "PMC12371805"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12371805/
text_path: /Users/oracleneo/llm-wiki/papers/corana-2024-salivary-proteomics-novel-biomarkers-periodontitis-sr.txt
text_filename: corana-2024-salivary-proteomics-novel-biomarkers-periodontitis-sr.txt
tags: [salivary-biomarkers, proteomics, periodontitis, diagnosis, S100A8, complement-C3, cystatin-SN]
relations:
  - type: extends
    target: cosin-villanueva-2024-micrornas-gingival-crevicular-fluid-periodontal
  - type: reinforces
    target: li-2024-salivary-diagnostics-opportunities-challenges
---

## Three-line Summary

Systematic review (PRISMA; PROSPERO CRD42022299826) of 13 untargeted salivary-proteomics studies (11 cross-sectional, 2 longitudinal; n=20–141) comparing periodontitis with health or gingivitis.

Complement C3, profilin-1, S100A8, and fibrinogen were consistently up-regulated in periodontitis (≥3 studies); cystatin-SN and leukocyte elastase inhibitor were down-regulated; only S100A8 was poolable, yielding a modest AUC of 0.71 (95% CI 0.66–0.75, I²=2.4%).

No single salivary protein is yet clinic-ready as a periodontal diagnostic; within-study multi-protein ML panels reach AUC ~0.97, but standardized protocols and independent validation are lacking.

## 세줄요약

치주염 vs 건강/치은염을 비교한 미표적 타액 프로테오믹스 연구 13편 체계적 고찰(PRISMA; PROSPERO CRD42022299826, 11편 단면·2편 종단; n=20–141).

치주염에서 C3·profilin-1·S100A8·fibrinogen 일관 상승(≥3편), cystatin-SN·leukocyte elastase inhibitor 하락; 메타분석 가능한 마커는 S100A8뿐으로 진단정확도 AUC 0.71(95% CI 0.66–0.75, I²=2.4%)에 그침.

단일 타액 마커로는 아직 임상 적용 불가; 단일기관 내 다단백질 기계학습 패널은 AUC ~0.97이나 외부 검증·표준화 프로토콜이 부재.

## Summary

Diagnosis of periodontitis still rests on probing and radiographs, which record *past* destruction rather than *current* disease activity, motivating a search for molecular biomarkers. Saliva is an attractive non-invasive whole-mouth medium (>5000 human/microbial proteins, ~73% saliva-unique), whereas gingival crevicular fluid (GCF) offers site-specificity at the cost of collection burden. This PRISMA systematic review (PROSPERO CRD42022299826) synthesizes **untargeted** salivary proteomics — hypothesis-free discovery rather than pre-selected cytokines — across 13 studies (11 cross-sectional, 2 treatment-longitudinal; n 20–141), using a consistency rule that a protein counts only when ≥3 independent studies agree on its direction. The reproducible signature is complement C3, profilin-1, S100A8, and fibrinogen elevated in periodontitis, with cystatin-SN and leukocyte elastase inhibitor higher in health; these map to complement activation, humoral immune response, and endopeptidase regulation. Diagnostic accuracy, however, was rarely reported and poolable for only one marker (S100A8, AUC 0.71), while multi-protein panels reached AUC ~0.97 within single studies but without external replication. The clinical bottom line: salivary proteomics can distinguish periodontitis from health, but heterogeneous methods, scarce diagnostic-accuracy data, and thin independent validation mean no salivary marker or panel is yet a deployable chairside screen.

## Key Contributions

- Defines a **reproducible untargeted salivary signature** for periodontitis (C3, profilin-1, S100A8, fibrinogen ↑; cystatin-SN, leukocyte elastase inhibitor ↓) using a ≥3-study consistency filter that discards discovery noise (17 of 52 twice-reported proteins had conflicting direction).
- Provides the **only poolable diagnostic estimate** in the field: S100A8 meta-analytic AUC 0.71 (95% CI 0.66–0.75, I²=2.4%) — quantifying how modest single-marker performance currently is.
- Contrasts single markers (weak) with **within-study multi-protein panels** (Bostanci ML 5-protein AUC >0.97; Grant α-1-acid glycoprotein+MMP-9+pyruvate kinase+S100A8+age AUC 0.970), signposting that panels + machine learning outperform any lone protein.
- Exposes a **validation gap** via modified QUADOMICS appraisal (2 high / 9 moderate / 1 low / 1 very-low quality): only 4/13 studies validated in an independent cohort, only 2/13 justified sample size — a roadmap for standardized future protocols.

## Methodology

- **Question (PECO)**: systemically healthy adults; exposure = clinical periodontitis; comparison = periodontal health or gingivitis; outcome = salivary protein-expression differences and diagnostic accuracy.
- **Search**: Medline/PubMed, Scopus, Embase, Cochrane through Oct 2023; duplicate calibrated screening (κ 0.86 abstract, 0.91 full text); 461 records → 13 studies.
- **Included studies**: 11 cross-sectional + 2 longitudinal treatment; Europe 6 / Asia 4 / South America 3; saliva unstimulated whole (9) or stimulated whole (4); detection LC–MS/MS (8) or MALDI-TOF MS (5).
- **Synthesis**: broad meta-analysis **not feasible** (proteins counted 2–4161/study; units from Da peaks to μg/μL to fold-change) → qualitative consistency analysis; targeted secondary search + fixed-effect meta-analysis only where ≥2 studies gave accuracy for the same marker; Flame pathway enrichment (GO-BP/GO-CC); modified QUADOMICS quality tool (15 items).

## Results

- **Consistent (≥3 studies)** — up in periodontitis: complement C3, profilin-1, **S100A8**, fibrinogen; up in health: **cystatin-SN**, leukocyte elastase inhibitor.
- **Pooled diagnostic accuracy**: S100A8 **AUC 0.71 (95% CI 0.66–0.75)**, low heterogeneity (I²=2.4%) — the only marker meta-analyzable.
- **Within-study panels**: Bostanci 5-protein ML panel AUC >0.97; Grant 5-feature panel AUC 0.970 (health/gingivitis vs. periodontitis) and 0.789 (mild-moderate vs. advanced); Antezack 6-peak decision tree sensitivity 70.3% / specificity 77.8%; Tang peptide-peak AUCs 0.688–0.860.
- **Pathways**: complement activation, humoral immune response, negative regulation of endopeptidase activity, response to external stimulus; extracellular/secretory-vesicle localization.
- **Quality caveats**: no sample-size justification in 11/13; unclear index-test↔reference-standard timing in most; independent-cohort validation in only 4/13; frequent case–control age imbalance (control means as low as 24–27 vs. cases 45–60).

## Related Papers

- [[periodontics/cosin-villanueva-2024-micrornas-gingival-crevicular-fluid-periodontal]] — extends: GCF miRNA biomarkers to the whole-saliva protein layer of the same diagnostic question.
- [[periodontics/fadli-2024-oral-gingival-crevicular-fluid-jawbone-turnover]] — reinforces: GCF molecular markers of periodontal bone turnover; complementary compartment to saliva.
- [[periodontics/donertas-2026-gbt-subgingival-debridement-gcf-biomarkers]] — reinforces: treatment-responsive GCF biomarkers (Corana notes only 2/13 salivary studies tracked pre/post-therapy change).
- [[overviews/gingival-crevicular-fluid-biomarker-diagnostics-overview]] — reinforces: GCF-side synthesis; saliva is the whole-mouth counterpart medium.
- [[overviews/saliva-diagnostics-and-salivary-gland-dysfunction-overview]] — extends: fills the periodontal-diagnosis branch of the saliva-diagnostics overview.
- [[oral-medicine/li-2024-salivary-diagnostics-opportunities-challenges]] — reinforces: general salivary-diagnostics opportunities/challenges framing, here made concrete for periodontitis.
- [[oral-medicine/nonaka-2023-saliva-diagnostics-salivaomics-exosomics-liquid-biopsy]] — reinforces: salivaomics/liquid-biopsy paradigm underlying proteomic discovery.
