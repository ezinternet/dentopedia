---
title: "The salivary microbiome as a diagnostic biomarker of periodontitis: a 16S multi-batch study"
stem: "regueira-iglesias-2024-salivary-microbiome-periodontitis-diagnostic"
source: "sources/regueira-iglesias-2024-salivary-microbiome-periodontitis-diagnostic.md"
source_collection: pubmed-abstract
category: oral-microbiology
year: 2024
authors: "Regueira-Iglesias A, Suárez-Rodríguez B, Blanco-Pintos T, Relvas M, Alonso-Sampedro M, Balsa-Castro C, Tomás I"
doi: "10.3389/fcimb.2024.1405699"
pmid: "39071165"
pmcid: "PMC11272481"
evidence_level: cross-sectional
tags: [oral-microbiology, salivary-microbiome, diagnostic-biomarker, periodontitis, 16s-rrna, machine-learning, auc, batch-effect, asv, precision-diagnostics]
relations:
  - type: complements
    target: wiki/oral-microbiology/teles-2024-salivary-biomarkers-periodontitis-progression
  - type: complements
    target: wiki/oral-microbiology/li-2025-subgingival-microbiome-nspt-antiplaque
---

## Three-line Summary

Multi-batch 16S (V3-V4/Illumina MiSeq) study pooling 796 participants (50 healthy + 74 periodontitis from own cohort; 672 from 4 external datasets); before batch-effect removal, a 16-ASV random forest classifier achieved AUC=0.944, sensitivity=90.73%, specificity=87.16% — good/excellent diagnostic accuracy for periodontitis from saliva.

After batch-effect removal, specificity improved slightly (91.51%) but required 200 ASVs (vs 16 before) to achieve AUC=0.935 with lower sensitivity (81.79%) — batch correction reduces false positives but produces less parsimonious models that may be harder to implement clinically.

The salivary microbiome demonstrates AUC 0.935–0.955 for periodontitis diagnosis; multi-site implementation requires rigorous batch effect control as a prerequisite.

## 세줄요약

다중 배치(multi-batch) 16S(V3-V4, Illumina) 연구; 796명 풀링; 배치 효과 제거 전 16-ASV 분류기 AUC=0.944, 민감도=90.73%, 특이도=87.16%.

배치 효과 제거 후 특이도 소폭 개선(91.51%)이나 200 ASV 필요(vs 16), AUC=0.935, 민감도=81.79% — 배치 보정 → 위양성 감소, 모델 복잡도 3배 증가.

타액 마이크로바이옴 치주염 진단 AUC 0.935–0.955 — 우수; 다기관 구현 시 배치 효과 필수 통제.

## Background

Salivary microbiome profiling is an appealing non-invasive approach to periodontitis diagnosis — saliva contains microorganisms from all oral surfaces and can be collected without clinician contact. Prior studies were methodologically fragmented (different technologies, gene regions, databases), making cross-study comparison unreliable. This 2024 study is the **first 16S multi-batch investigation at ASV level** (the highest resolution, using exact sequence variants rather than 97%-similarity OTU clusters), specifically quantifying the impact of batch-effect removal on both diagnostic performance and model complexity.

## Methods

- **Own cohort**: 124 participants (50 healthy, 74 periodontitis); Illumina MiSeq, V3-V4 16S
- **External datasets**: 4 databases from systematic search (V3-V4 Illumina studies)
- **Total pooled**: 796 participants
- **Bioinformatics**: ASV-level with DADA2 denoising; R-Bioconductor
- **Machine learning**: Random forest; 10-fold cross-validation; AUC/sensitivity/specificity
- **Batch-effect removal**: ComBat or equivalent; pre/post comparison
- **Models tested**: All-samples (n=796) and train/test split (531/265)

## Results

### Diagnostic Performance Before Batch-Effect Removal

| Model | n ASVs (%) | AUC | Sensitivity | Specificity |
|-------|-----------|-----|-------------|-------------|
| All samples (n=796) | 16 (0.16%) | 0.944 | 90.73% | 87.16% |
| Train/test (531/265) | 35 (0.36%) | 0.955 | 86.54% | 90.06% |

### Diagnostic Performance After Batch-Effect Removal

| Model | n ASVs (%) | AUC | Sensitivity | Specificity |
|-------|-----------|-----|-------------|-------------|
| All samples (n=796) | 200 (2.03%) | 0.935 | 81.79% | 91.51% |
| Train/test (531/265) | 100 (1.01%) | 0.947 | 78.85% | 90.68% |

### Differential Abundance
- Before batch removal: 265 differentially abundant ASVs
- After batch removal: 190 ASVs (batch correction removed ~28% of differentially abundant ASVs — these were likely technical artifacts)

### Interpretation
- **Batch correction trade-off**: Improves specificity (fewer false positives) but requires 6–12x more ASVs, reduces sensitivity, and creates more complex models
- **Overall conclusion**: AUC 0.935–0.955 = good-to-excellent diagnostic accuracy regardless of batch-correction approach

## Clinical Takeaway

The salivary microbiome can detect periodontitis with excellent accuracy (AUC ~0.944) using as few as 16 ASVs — a potentially practical panel for a future point-of-care diagnostic. The key challenge for multi-site implementation is batch effect control: different sequencing runs introduce technical variation that degrades model transferability. Before any clinical deployment of salivary microbiome diagnostics, a standardized library preparation and bioinformatics pipeline is essential. This paper should be read alongside [[oral-microbiology/teles-2024-salivary-biomarkers-periodontitis-progression]] (which provides cytokine, not microbiome, salivary biomarker data for progression monitoring).

## Evidence Map

| Claim | Source |
|-------|--------|
| Pre-batch-removal: 16 ASVs → AUC=0.944 for periodontitis detection | Multi-batch study, n=796, random forest |
| Post-batch-removal: 200 ASVs → AUC=0.935 | Same study, ComBat correction |
| Batch removal reduced differentially abundant ASVs from 265→190 | Differential abundance analysis |
| Best AUC achieved: 0.955 (train/test, pre-correction) | Validation model |
