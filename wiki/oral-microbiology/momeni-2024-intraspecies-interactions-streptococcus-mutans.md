---
title: "Intraspecies interactions of Streptococcus mutans impact biofilm architecture and virulence determinants in childhood dental caries"
authors: "Momeni SS, Cao X, Xie B, Rainey K, Childers NK, Wu H"
year: 2024
date: 2024-07-11
doi: "10.1128/msphere.00778-23"
source: momeni-2024-intraspecies-interactions-streptococcus-mutans.md
category: [oral-microbiology]
confidence: in-vitro
source_collection: pubmed-text
full_text: true
pmid: "38990043"
pmcid: "PMC11288028"
text_path: /Users/oracleneo/llm-wiki/papers/momeni-2024-intraspecies-interactions-streptococcus-mutans.txt
text_filename: momeni-2024-intraspecies-interactions-streptococcus-mutans.txt
tags: [streptococcus-mutans, biofilm, dental-caries, intraspecies, ecc, clsm]
relations:
  - type: extends
    target: bowen-2011-streptococcus-mutans-glucosyltransferases
  - type: reinforces
    target: koo-2013-exopolysaccharides-matrix-biofilm-virulence
---

## One-line Summary

In vitro biofilm + in vivo Drosophila study of two clinical S. mutans genotypes (G09, G18) from one high-caries-risk child, showing that co-culture significantly lowers biofilm pH, roughly doubles cell density and biofilm thickness, and enhances colonization versus mono-culture — with each strain occupying a distinct, non-overlapping spatial domain (division of labor: G18 drives acidity, G09 drives architecture).

## 한줄요약

임상 S. mutans 두 유전형(G09·G18)의 in vitro 바이오필름 + in vivo 초파리 실험 — 함께 배양하면 단독 배양보다 바이오필름 pH가 유의하게 낮아지고(산도↑) 세포밀도·두께가 약 2배로 늘며 집락화가 강화되고, 각 균주는 서로 겹치지 않는 공간 영역을 차지한다(G18은 산도, G09는 구조 담당).

## Summary

Epidemiology consistently links **multiple S. mutans genotypes** in a child's mouth to greater early-childhood-caries (ECC) risk, but the mechanism was unexplored. Using clinical isolates from a longitudinal high-caries-risk cohort, Momeni et al. show that co-culturing two genotypes (G09, G18) from the same child produces a **mutualistic**, more cariogenic biofilm than either strain alone: significantly lower pH, ~doubled cell density and thickness by CLSM, and enhanced colonization in a Drosophila model. Time-lapse and confocal imaging reveal a **division of labor** — G18 drives biofilm acidity (higher intracellular polysaccharide, aciduricity) while G09 drives biofilm thickness/architecture (tall aggregates forming "volcano-like" structures) — with the two strains occupying distinct, non-overlapping spatial domains. A nested association analysis (n=78) found that acquiring multiple genotypes **within the first year of detection** was significantly associated with ECC (p=0.019), tying the mechanistic phenotype back to clinical risk.

## Key Contributions

- First CLSM + time-lapse dissection of **intraspecies** S. mutans biofilm interactions using clinical, patient-matched isolates rather than the reference strain UA159.
- Establishes that mixing two genotypes is **mutually beneficial** (lower pH, doubled biomass/thickness, greater colonization) — a mechanistic basis for the "multiple genotypes → higher caries" epidemiology.
- Documents **strain division of labor**: acidity (G18) vs architecture/thickness (G09), with distinct spatial domains.
- Ties an in vitro/in vivo phenotype to a clinical signal: multiple genotypes within the first year of detection significantly associated with ECC.
- Surfaces a reusable methods caveat: mCherry can artifactually induce aggregation in some clinical S. mutans strains → control with an alternate fluorophore.

## Methodology

- **Design**: laboratory in vitro biofilm assays + in vivo Drosophila melanogaster colonization + retrospective cross-sectional association (n=78), nested in a prior 8-year longitudinal cohort (African-American, non-fluoridated, high-caries-risk).
- **Strains**: >14,000 isolates → 34 rep-PCR/WGS genotypes; Child C-232 (G09 + G18, two most prevalent) selected for depth study; UA159 control.
- **Biofilm** (THB + 1% sucrose, 16 h): biomass (crystal violet), IPS (iodine), pH (pHrodo red), glucan (cascade blue), density (Syto9); ImageJ.
- **CLSM**: G09-mCherry / G18-GFP, Zeiss LSM 880/980, Imaris; differential antibiotic-selective CFU plating confirmed 50/50 inoculum.
- **Time-lapse**: Zeiss CD7, hourly 24-30 h (brightfield + GFP + pHrodo).
- **Statistics**: Fisher's exact test (association); Student's t-test / one-way ANOVA + Tukey; p<0.05.

## Results

- **Association**: multiple genotypes within first year of detection → ECC caries 52.6% vs 29.5% single genotype, **p=0.019**; at initial detection not significant (p=0.327). 86% of caries-free children failed to persistently colonize S. mutans.
- **pH**: co-culture significantly more acidic than mono-culture in 9/10 children and pooled population; G18 drives acidity independent of glucan.
- **CLSM**: total S. mutans fluorescence ~**doubled** in co-culture despite equal inoculum; G09 thickness significantly greater in mix; volume/area significantly doubled vs mono/UA159.
- **Architecture**: G09 = large aggregates ("volcano" structures over glucan); G18 = confluent "lawn"/"fish-net" chains; distinct non-overlapping domains. Bi-phasic acidification (~10-11 h, ~24-26 h).
- **In vivo**: G09 colonization consistently greater when G18 present (mutualistic).

## Related Papers

- [[oral-microbiology/bowen-2011-streptococcus-mutans-glucosyltransferases]] — extends: Gtf/EPS glucan biology underlying the glucan matrix imaged here.
- [[oral-microbiology/koo-2013-exopolysaccharides-matrix-biofilm-virulence]] — reinforces: EPS matrix as the scaffold organizing 3D biofilm microenvironments and acidity.
- [[oral-microbiology/klein-2012-mutans-protein-synthesis-mixed-species-biofilm]] — related: mixed-biofilm S. mutans behavior (interspecies counterpart to this intraspecies study).
- [[oral-microbiology/lueyar-2023-dynamic-interactions-between-candida-albicans]] — contrast: cross-kingdom (S. mutans × Candida) interaction vs the intraspecies axis studied here.
- [[oral-microbiology/koo-2013-exopolysaccharides-matrix-biofilm-virulence]] — spatial microcolony architecture framework.
