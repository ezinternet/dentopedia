---
title: "The Impact of Mouthwash on the Oropharyngeal Microbiota of Men Who Have Sex with Men: a Substudy of the OMEGA Trial"
authors: Plummer EL, Maddaford K, Murray GL, Fairley CK, Pasricha S, Mu A, Bradshaw CS, Williamson DA, Chow EPF
year: 2022
doi: 10.1128/spectrum.01757-21
pmid: "35019769"
pmcid: "PMC8754113"
category: [oral-microbiology]
source_collection: pubmed-text
full_text: true
text_path: /Users/oracleneo/llm-wiki/papers/plummer-2022-listerine-mouthwash-oropharyngeal-microbiota.txt
text_filename: plummer-2022-listerine-mouthwash-oropharyngeal-microbiota.txt
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8754113/
---

## Why Ingested

리스테린 장기 매일 사용 시 구강 마이크로바이옴 변화 여부를 직접 검증한 유일한 PMC 풀텍스트 RCT 서브스터디. 가글액 장기사용 안전성 질문에 대한 핵심 근거이며 [[wiki/oral-microbiology]] 분야의 마이크로바이옴 안정성 데이터를 보강한다.

## One-line Summary

RCT substudy (n=153, 12 weeks), Listerine Zero daily use caused no significant change in oropharyngeal microbiota composition; Biotène caused small but significant decreases in Streptococcus and Rothia.

## 한줄요약

RCT 서브스터디 (n=153, 12주), 리스테린 제로 매일 사용은 구인두 마이크로바이오타 구성에 유의한 변화 없음; Biotène은 Streptococcus·Rothia 소폭 감소.

## 1. Document Information

- **Journal**: Microbiology Spectrum 10(1): e0175721
- **Study type**: RCT substudy (OMEGA trial, ACTRN12616000247471)
- **Setting**: Melbourne Sexual Health Centre, 2017–2018
- **Participants**: 153 MSM; 78 Listerine Zero, 75 Biotène
- **Intervention**: 20 mL rinse/gargle 60 s, ≥once daily × 12 weeks

## 2. Key Contributions

1. First 16S rRNA sequencing study of 12-week daily Listerine impact on oropharyngeal microbiota
2. PERMANOVA showed no global microbiota shift with Listerine (p=0.413) or Biotène (p=0.331)
3. ALDEx2 + ANCOM: Listerine → zero FDR-significant taxa; Biotène → Streptococcus ↓ (FDR-p=0.004), Rothia ↓ (FDR-p=0.03)
4. Shannon diversity marginally increased in both groups (clinically non-meaningful)
5. Gonorrhea infection status and smoking had no significant impact on microbiota structure

## 3. Methodology and Architecture

- **Microbiota**: 16S rRNA V4 amplicon (515F/806R), Illumina MiSeq 2×150bp
- **Taxonomy**: DADA2 + Silva v138 (genus level; Streptococcus species by BLAST)
- **Beta-diversity**: PERMANOVA on Bray-Curtis distance (999 permutations)
- **Differential abundance**: ALDEx2 (Dirichlet MC, Wilcoxon, Benjamini-Hochberg FDR); confirmed by ANCOM
- **Sensitivity**: results stable across exclusion of prior daily mouthwash users and inclusion of only mouthwash-naive participants

## 4. Key Results and Benchmarks

| Parameter | Listerine (n=78) | Biotène (n=75) |
|---|---|---|
| PERMANOVA p (beta-div) | 0.413 (NS) | 0.331 (NS) |
| Shannon diversity change | 3.5→3.6 (p=0.012) | 3.5→3.6 (p=0.002) |
| FDR-significant taxa | None | Streptococcus ↓, Rothia ↓ |
| Clinical implication | Microbiota-safe | Small commensal shift |

Top 5 genera at baseline: Streptococcus (23%), Prevotella (11%), Veillonella (7%), Fusobacterium (6%), Porphyromonas (5%)

## 5. Limitations and Future Work

- 12-week interval: immediate post-rinse transient effects could not be captured
- 16S V4 region: insufficient species-level resolution for Streptococcus spp. (commensal vs. cariogenic indistinguishable)
- MSM cohort only: generalizability to general population uncertain
- Mouthwash: Listerine Zero tested (alcohol-free); original alcohol-containing Listerine not studied directly
- Only 4 gonorrhea acquisition events — insufficient for infection-microbiota analysis

## 6. Related Work

- OMEGA trial main paper: Chow EPF et al. 2020 (Listerine vs Biotène for gonorrhea prevention — no difference in efficacy)
- CHX mouthwash microbiome studies: 7-day use reduces nitrate-reducing bacteria and diversity (contrasts with Listerine findings)
- Cortelli 2013 (PMID 23986962): Listerine Zero 6-month plaque/gingivitis RCT — 31.6% plaque ↓, 24.0% gingivitis ↓ vs. negative control

## 7. Glossary

- **PERMANOVA**: Permutational MANOVA — tests if group centroids differ in multivariate space (beta-diversity)
- **ALDEx2**: ANOVA-like Differential abundance, accounts for compositional data nature via Dirichlet Monte Carlo
- **ANCOM**: Analysis of Composition of Microbiomes — confirmatory differential abundance method
- **ASV**: Amplicon Sequence Variant — exact 16S sequence, higher resolution than OTU
- **Shannon index**: Alpha-diversity measure combining richness and evenness
- **FDR**: False discovery rate correction (Benjamini-Hochberg) to control multiple testing
- **Listerine Zero**: Alcohol-free essential oil mouthwash (thymol, eucalyptol, menthol, methyl salicylate)
- **Biotène**: Alcohol-free salivary enzyme system mouthwash (lactoperoxidase, lysozyme, glucose oxidase)
