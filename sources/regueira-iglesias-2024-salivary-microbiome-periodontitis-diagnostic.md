---
title: "The salivary microbiome as a diagnostic biomarker of periodontitis: a 16S multi-batch study before and after the removal of batch effects"
authors: "Regueira-Iglesias A, Suárez-Rodríguez B, Blanco-Pintos T, Relvas M, Alonso-Sampedro M, Balsa-Castro C, Tomás I"
year: 2024
doi: "10.3389/fcimb.2024.1405699"
pmid: "39071165"
pmcid: "PMC11272481"
category: [oral-microbiology]
source_collection: pubmed-text
full_text: true
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11272481/
text_path: /Users/oracleneo/llm-wiki/papers/regueira-iglesias-2024-salivary-microbiome-periodontitis-diagnostic.txt
text_filename: regueira-iglesias-2024-salivary-microbiome-periodontitis-diagnostic.txt
---

## Why Ingested

First rigorous 16S multi-batch study on the salivary microbiome as a periodontitis diagnostic tool at ASV level — addresses the methodological fragmentation of prior studies (different technologies, gene regions, databases) and directly quantifies the impact of batch-effect removal on diagnostic model performance, providing a translational roadmap for precision periodontitis diagnostics.

## Three-line Summary

Multi-batch 16S (V3-V4/Illumina MiSeq) study pooling 796 participants (50 healthy, 74 periodontitis — own cohort; 672 from 4 external datasets); before batch-effect removal, a 16-ASV classifier achieved AUC=0.944, sensitivity=90.73%, specificity=87.16%.

After batch-effect removal, diagnostic accuracy improved slightly for specificity (91.51%) but required 200 ASVs (vs 16) to achieve AUC=0.935 — more variables needed for slightly lower sensitivity (81.79%), indicating batch correction reduces false positives but creates less parsimonious models.

The salivary microbiome demonstrates good/excellent diagnostic potential for periodontitis (AUC 0.935–0.955) and shows clinical applicability as a precision diagnostic tool, though batch effects must be rigorously controlled in any multi-site implementation.

## 세줄요약

다중 배치(multi-batch) 16S(V3-V4/Illumina) 연구; 796명(자체 50+74명, 외부 672명) 풀링; 배치 효과 제거 전 16 ASV 분류기 AUC=0.944, 민감도=90.73%, 특이도=87.16%.

배치 효과 제거 후 특이도 소폭 개선(91.51%)이나 200 ASV 필요(vs 16), AUC=0.935·민감도=81.79% — 배치 보정 → 위양성 감소하지만 모델 복잡도 증가.

타액 마이크로바이옴은 치주염 진단에 우수한 AUC(0.935–0.955)를 달성, 정밀 진단 도구로서 임상 활용 가능성 있으나 다기관 구현 시 배치 효과 관리 필수.

## 1. Document Information

- **Title**: The salivary microbiome as a diagnostic biomarker of periodontitis: a 16S multi-batch study before and after the removal of batch effects
- **Authors**: Regueira-Iglesias A et al. (Universidade de Santiago de Compostela)
- **Journal**: Frontiers in Cellular and Infection Microbiology. 2024;14:1405699
- **PMID**: 39071165 | **PMCID**: PMC11272481 | **DOI**: 10.3389/fcimb.2024.1405699
- **Study type**: Observational, multi-batch bioinformatics study; ASV-level analysis
- **Full text**: PMC open access

## 2. Key Contributions

- First 16S multi-batch study at ASV level for salivary microbiome periodontitis diagnosis.
- Quantifies impact of batch-effect removal on model parsimony vs. accuracy trade-off.
- Demonstrates that batch-effect removal triples the number of ASVs needed while providing only minor accuracy gains.
- Provides validated models with external cohort validation.

## 3. Methodology

- **Own cohort**: 124 patients (50 healthy, 74 periodontitis); Illumina MiSeq, V3-V4 16S
- **External datasets**: 4 databases identified via systematic search; V3-V4 Illumina studies
- **Total pooled**: 796 participants
- **Bioinformatics**: ASV-level (vs OTU); DADA2 or similar denoising; R-Bioconductor
- **Batch-effect removal**: Applied to combined dataset; re-ran models before/after
- **Machine learning**: Random forest models; AUC, sensitivity, specificity

## 4. Key Results

**Before batch-effect removal:**
- All samples model (n=796): 16 ASVs (0.16%), AUC=0.944, sensitivity=90.73%, specificity=87.16%
- Training/test split (531/265): 35 ASVs (0.36%), AUC=0.955, sensitivity=86.54%, specificity=90.06%

**After batch-effect removal:**
- All samples: 200 ASVs (2.03%), AUC=0.935, sensitivity=81.79%, specificity=91.51%
- Training/test: 100 ASVs (1.01%), AUC=0.947, sensitivity=78.85%, specificity=90.68%

**Differential abundance**: Before: 265 ASVs; After: 190 ASVs (batch correction reduced ~1/3 of differentially abundant ASVs)

## 5. Limitations

- Cross-sectional; no longitudinal validation
- Limited external dataset diversity (4 databases, V3-V4 only)
- Machine learning models — black box interpretability
- Clinical applicability requires point-of-care implementation not yet available

## 6. Glossary

- **ASV**: Amplicon sequence variant — exact sequences (vs OTU clustering at 97%)
- **Batch effect (BE)**: Technical variation between studies/labs distorting biological signals
- **AUC**: Area under the ROC curve (0.5=random, 1.0=perfect)
- **V3-V4**: Hypervariable regions of 16S rRNA gene amplified by Illumina
- **OTU**: Operational taxonomic unit (97% similarity clustering — less precise than ASV)
