---
title: "Microbial evaluation of zirconia and titanium implants in the anterior mandibula: a randomized controlled clinical trial"
authors: "Kniha K, et al."
year: 2026
doi: 10.1038/s41598-026-54915-0
category: [implants]
source_collection: pubmed-text
full_text: true
pmid: "42230722"
pmcid: "PMC13230837"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13230837/
text_path: /Users/oracleneo/llm-wiki/papers/kniha-2026-zirconia-titanium-microbial-anterior-rct.txt
text_filename: kniha-2026-zirconia-titanium-microbial-anterior-rct.txt
---

## Why Ingested

지르코니아 임플란트의 구강 미생물 환경 영향은 임플란트 재료 선택 시 근거가 되지만 임상 RCT 데이터가 부족했다. 본 split-mouth RCT는 12개월에 걸쳐 지르코니아 vs 티타늄 임플란트의 주위 미생물 군집을 16S rRNA 시퀀싱으로 직접 비교해 [[implants/peri-implantitis]] 위험 인자 맥락에서 재료 의존적 미생물 생태학에 기여한다.

## One-line Summary

Split-mouth RCT (n=20 edentulous patients, 12 months): zirconia implants harbored lower Actinobacteria at 12 months and higher microbial diversity vs titanium; beta diversity did not differ significantly between materials at any timepoint; findings are exploratory with no definitive clinical superiority of either material.

## 한줄요약

분할구 RCT (20명, 12개월): 지르코니아 임플란트는 12개월 시점 Actinobacteria 감소·미생물 다양성 우세 경향을 보였고 티타늄은 다양성 감소; 베타 다양성은 재료 간 차이 없으며, 어느 재료의 임상적 우위도 결론 짓기 어렵다.

## 1. Document Information

- **Type**: One-year prospective split-mouth RCT (microbiome focus)
- **Authors**: Kniha K, et al. (RWTH Aachen University, Germany)
- **Year**: 2026
- **Journal**: Scientific Reports (Nature)
- **DOI**: 10.1038/s41598-026-54915-0
- **PMID**: 42230722 / **PMCID**: PMC13230837
- **Ethics**: EK 180/19, RWTH Aachen
- **Sample**: 20 patients (18 completed 12 months), entirely edentulous lower jaw
- **Implants**: Straumann PURE Ceramic (zirconia) vs TL SLactive (titanium), both 4.1 mm diameter, 8–12 mm length, mandibular inter-foramina
- **Prosthetics**: Overdenture with clip attachments (PUREloc / Novaloc)

## 2. Key Contributions

1. First split-mouth RCT using 16S rRNA sequencing to compare peri-implant microbiome of zirconia vs titanium over 12 months in overdenture patients
2. Zirconia showed higher microbial diversity at 12 months than titanium (Shannon index)
3. Zirconia showed decreases in Fusobacteria and Proteobacteria (T0→T1); titanium showed Actinomyces israelii increase at 12 months
4. Beta diversity (community composition overall) did not differ significantly between materials — null hypothesis partially rejected for composition/diversity metrics but composition overlap is large
5. Red complex pathogens (P. gingivalis, T. forsythia, T. denticola) tended lower on zirconia
6. Comprehensive bioinformatics pipeline with best-test selection (MaAsLin2 from 14-test ROC evaluation) and bootstrapping sensitivity analysis

## 3. Methodology and Architecture

**Design**: Prospective split-mouth RCT, 12-month follow-up
**Randomization**: Balanced computerized (side allocation left/right for Ti vs Zr per patient)
**n**: 20 recruited, 18 completed (2 dropouts at 12 months)

**Implant materials**:
- Zirconia (Zi): Straumann PURE Ceramic Implant, 4.1 mm ø
- Titanium (Tn): Straumann TL SLactive, 4.1 mm ø
- Control (To): Natural teeth in upper jaw (supragingival plaque samples)

**Timepoints**: T0 (3 months, baseline after osseointegration), T1 (6 months), T2 (12 months)

**Microbiome pipeline**:
- DNA: DNeasy Blood and Tissue Kit (Qiagen)
- Sequencing: 16S rRNA V1-V3 amplicon, Eurofins Genomics
- Bioinformatics: QIIME2, DADA2 (forward 320 bp, reverse 242 bp truncation), SILVA 138
- Alpha diversity: Shannon-Wiener index, richness, Pielou's evenness (vegan package)
- Beta diversity: Bray-Curtis dissimilarity, NMDS, pairwise PERMANOVA (999 permutations)
- Differential abundance: MaAsLin2 (selected from 14 tests by ROC + synthetic dataset evaluation), BH correction, 10% prevalence threshold, AST transformation
- Sensitivity: bootstrapping 200 repetitions; taxa significant only if bootstrap 95% CI excludes zero

**Sample size**: G*Power, matched pairs t-test, effect size 0.71, 80% power → 18 → 20 patients

## 4. Key Results and Benchmarks

**Alpha diversity (Shannon index)**:
- Zi and Tn: both increased significantly at T2 vs T0 and T1
- At T2: Ti significantly LOWER diversity than Zi (p < 0.05)
- Natural teeth: no significant change (stable high diversity)

**Beta diversity**: No significant inter-material differences (PERMANOVA NS at all time points); no systematic temporal clustering

**Phyla (top 5 pooled)**: Firmicutes 39.02%, Actinobacteria 24.03%, Bacteroidetes 17.71%, Proteobacteria 11.87%, Fusobacteria 5.06%

**Within-material phylum changes**:
| Phylum | Material | Change | p |
|---|---|---|---|
| Fusobacteria | Zirconia | ↓ T0→T1 | 0.03 |
| Proteobacteria | Zirconia | ↓ T0→T1 | 0.03 |
| Firmicutes | Zirconia | ↑ T0→T1 | 0.03 |
| Actinobacteria | Titanium | No change | NS |

**Inter-material phylum comparison (T2)**: Actinobacteria less abundant on Zi than Tn (p=0.04)

**Key species/genus changes (MaAsLin2, BH-corrected)**:
| Taxon | Material | Change | p-adj |
|---|---|---|---|
| Actinomyces israelii | Titanium | ↑ at T2 vs T0 | 0.009 |
| Leptotrichia (genus) | Zirconia | ↓ at T1 vs T0 | 0.022 |

**Red complex**: Lower relative abundance on zirconia vs titanium (not statistically quantified in main text — descriptive observation)

## 5. Limitations and Future Work

- Supragingival sampling only — peri-implantitis is predominantly subgingival; results may not reflect disease-relevant dysbiosis
- Clinical outcomes (probing depth, BOP, plaque index) reported separately — cannot correlate microbiome differences to clinical status in this paper
- 16S rRNA limited species-level resolution; no functional/metabolic data
- Split-mouth design: intraoral cross-contamination between sites cannot be excluded
- Overdenture clip design may create specific plaque-accumulation niches
- Natural teeth vs implants comparison limited by fundamental biological differences (periodontal ligament, different soft tissue attachment)
- 12-month follow-up — insufficient for long-term peri-implant disease outcome assessment
- Authors caution: findings are descriptive/exploratory, not evidence of clinical superiority
- Future needs: next-generation sequencing, subgingival sampling, longitudinal clinical + microbiome integration

## 6. Related Work

- Prior studies: ZrO2 implants show reduced bacterial adhesion vs Ti (referenced but not fully cited in text); lower surface free energy / smoother topography proposed mechanism
- Red complex literature: P. gingivalis, T. forsythia, T. denticola as key peri-implantitis pathogens; their lower abundance on zirconia is biologically plausible
- Titanium corrosion / ion release: potential contributor to local inflammation and biofilm dysbiosis
- Peri-implant biofilm maturation: early colonizers (Streptococcus spp.) → complex communities; Fusobacteria and certain Treponema linked to inflammatory progression
- Clinical peri-implantitis literature: titanium associated with higher peri-implantitis incidence in some systems — microbiome data here provides mechanistic context

## 7. Glossary

- **16S rRNA sequencing**: Bacterial identification via highly conserved ribosomal RNA gene; V1-V3 region used here
- **Alpha diversity (알파 다양성)**: Within-sample species richness and evenness; Shannon index = species richness + abundance; Pielou = evenness
- **Beta diversity (베타 다양성)**: Between-sample microbial community dissimilarity; Bray-Curtis distance + NMDS visualization
- **PERMANOVA**: Permutational multivariate ANOVA for beta diversity group differences
- **MaAsLin2**: Multivariable association discovery in microbial community studies; mixed-effects model for differential abundance
- **Red complex (레드 컴플렉스)**: Highly pathogenic triad — Porphyromonas gingivalis, Tannerella forsythia, Treponema denticola; classic peri-implant/periodontal pathogens
- **QIIME2**: Quantitative Insights Into Microbial Ecology — bioinformatics framework for microbiome analysis
- **DADA2**: Amplicon sequence variant (ASV) denoising algorithm for 16S data
- **SILVA 138**: Comprehensive ribosomal RNA database for taxonomic classification
- **Benjamini-Hochberg correction (BH)**: Multiple-comparison correction controlling false discovery rate (FDR)
- **AST (Arcsin Square root Transformation)**: Data transformation for compositional microbiome data before MaAsLin2
- **Leptotrichia**: Anaerobic gram-negative rod; associated with oral biofilm; decreased on zirconia at 6 months
- **Actinomyces israelii**: Gram-positive anaerobic bacterium; increased on titanium at 12 months; associated with opportunistic infection
