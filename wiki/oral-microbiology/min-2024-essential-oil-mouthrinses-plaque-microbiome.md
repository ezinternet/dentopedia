---
title: "Quantitative analysis of the effects of essential oil mouthrinses on clinical plaque microbiome: a parallel-group, randomized trial"
authors: Min K, Glowacki AJ, Bosma ML, McGuire JA, Tian S, McAdoo K, DelSasso A, Fourre T, Gambogi RJ, Milleman J, Milleman KR
year: 2024
date: 2024-05-18
doi: 10.1186/s12903-024-04365-9
source: min-2024-essential-oil-mouthrinses-plaque-microbiome.md
category: [oral-microbiology]
confidence: rct
source_collection: pubmed-text
text_path: /Users/oracleneo/llm-wiki/papers/min-2024-essential-oil-mouthrinses-plaque-microbiome.txt
text_filename: min-2024-essential-oil-mouthrinses-plaque-microbiome.txt
tags: [listerine, essential-oil, mouthwash, oral-microbiome, gingivitis, dysbiosis, metagenome, quantitative-microbiome, spike-in]
relations:
  - type: reinforces
    target: lamont-2018-oral-microbiota-dynamic-communities-host
  - type: applies-to
    target: hajishengallis-2012-psd-model-periodontal-disease
---

## One-line Summary

Parallel-group RCT (n=153, 6 weeks); alcohol-containing EO mouthrinses (LCM and ACPM) reduced gingivitis ≥37% vs hydroalcohol control and, uniquely shown via spike-in quantitative metagenomics, shifted the dysbiotic plaque microbiome toward healthy composition after 4 weeks.

## 한줄요약

병렬군 무작위대조시험 (Randomized Controlled Trial, RCT) (n=153, 6주); 알코올 함유 에센셜 오일 가글 (Essential Oil Mouthwash, EOMW) (LCM·ACPM)이 치은염 (Gingivitis) ≥37% 감소 및 이상증식 (Dysbiosis) 치태 (Plaque) 미생물군집을 4주 만에 건강 상태로 전환함을 spike-in 절대 정량 메타게놈 분석으로 최초 입증 (Johnson & Johnson 후원 연구).

## Summary

This industry-sponsored parallel-group RCT (funded by Johnson & Johnson, manufacturer of LISTERINE) compared three essential-oil-containing mouthrinses — LCM (LISTERINE Cool Mint Antiseptic, alcohol-containing), ACPM (alcohol-containing prototype), AFPM (alcohol-free prototype) — against a 5% hydroalcohol (HA) negative control in 153 adults with moderate gingivitis over 6 weeks of twice-daily use. The study's primary methodological contribution is the first application of a spike-in absolute quantification approach combined with shallow shotgun metagenomics to an oral care RCT, enabling detection of absolute bacterial cell numbers rather than the relative abundances provided by conventional 16S rRNA sequencing. Clinically, all three EO mouthrinses reduced gingivitis (MGI) by at least 37.4% vs HA at week 6; LCM and ACPM also significantly reduced plaque (TPI, ≥26%) and shifted the dysbiotic microbiome toward the composition observed in naturally healthy subjects, a phenomenon described as a microbiome "reset." The alcohol-free AFPM achieved comparable gingivitis reduction (−40.6%) despite weaker microbiological effects, suggesting a non-plaque mechanism for some of its benefit. Results should be interpreted in light of strong industry conflict of interest.

## Key Contributions

- **Novel quantitative microbiome method**: First RCT application of spike-in DNA + shotgun metagenomics to yield absolute bacterial cell numbers (Calculated Microbial Units, CMU) per sample — avoids compositional bias inherent to relative abundance methods
- **Dysbiosis reversal**: LCM and ACPM twice-daily use for 4 weeks shifted beta-diversity (weighted UniFrac PCoA) of gingivitis subjects' microbiomes toward healthy reference composition; HA control subjects returned to baseline dysbiosis
- **Mechanism clarification**: EO mouthrinses reset plaque via non-selective broad-spectrum bactericidal action (reducing all bacteria indiscriminately), not by selectively targeting pathogens; early-colonizing health-associated commensals repopulate preferentially after repeated use
- **Alcohol-free paradox**: AFPM showed reduced total microbial load and alpha-diversity effects vs alcohol-containing formulas, yet achieved comparable gingivitis reduction, implying additional mechanisms beyond direct antibacterial plaque suppression
- **Comprehensive species mapping**: 856 taxa identified; 213 classified as human oral bacteria and subdivided into commensals, gingivitis-, periodontitis-, malodor-, and caries-associated categories using HOMD + literature

## Methodology

**Design**: Randomized, controlled, examiner-blind, single-center, parallel-group trial. Oct–Dec 2019, Salus Research Inc., Fort Wayne, IN. Examiner-blinded; dispensing personnel excluded from examinations.

**Groups** (n per completers):
| Group | Formula | n |
|---|---|---|
| LCM | LISTERINE Cool Mint (0.092% eucalyptol, 0.042% menthol, 0.060% methyl salicylate, 0.064% thymol, 21.6% alcohol) | 31 |
| ACPM | Same EOs + new sensorial flavor, 21.6% alcohol | 29 |
| AFPM | Same EOs + new sensorial flavor, alcohol-free | 30 |
| HA | 5% hydroalcohol, no EOs (negative control) | 31 |
| Healthy reference | No intervention; baseline assessment only | 32 |

**Protocol**: Twice-daily brushing + 30 s rinse with 20 mL of assigned mouthrinse for 6 weeks. Fluoridated toothpaste and soft toothbrush provided to all.

**Clinical assessments** at weeks 4 and 6: Modified Gingival Index (MGI), Turesky Plaque Index (TPI), Expanded Bleeding Index (EBI, 168 sites).

**Microbiome collection**: Supragingival plaque from 4 teeth at weeks 1, 4, and 6. Plaque collected 4–6 h post-first brushing/rinsing. Stored at −80°C.

**Quantitative microbiome analysis**:
- Shallow shotgun metagenomics (SMS) at CosmosID Inc.; 3–4M paired-end 2×150 bp reads (HiSeq)
- Pre-extraction spike-in with ZymoBIOMICS Spike-in Control II (non-human reference bacteria)
- Linear regression of spike-in input vs. output abundance → absolute CMU per taxon per sample
- 856 species-level taxa identified; 213 human oral bacteria mapped to health/disease categories
- Alpha diversity: Shannon-Weaver + observed richness; Beta diversity: weighted UniFrac PCoA + PERMANOVA

**Statistical analysis**: Repeated measures mixed model (treatment, visit, baseline covariate, treatment×visit interaction) for clinical and microbiome endpoints; Wilcoxon rank sum for species-level differential abundance.

## Results

**Clinical outcomes at week 6 vs. HA control**:

| Index | LCM | ACPM | AFPM |
|---|---|---|---|
| MGI reduction | −44.4%*** | −37.4%*** | −40.6%*** |
| TPI reduction | −26.2%*** | −27.3%*** | −14.0%*** |
| EBI reduction | −38.0%*** | −36.3%*** | −40.0%*** |

(*** p<0.001; all comparisons vs. HA)

**Microbiome outcomes**:
- **Total microbial load (TML)**: LCM and ACPM — significant reductions at weeks 1, 4, 6; AFPM — only at week 1; HA — no significant change
- **Alpha diversity (Shannon-Weaver)**: LCM and ACPM significantly reduced at weeks 4 and 6; AFPM and HA unchanged
- **Observed species richness**: LCM and ACPM significantly reduced at week 6; AFPM and HA unchanged
- **Category-specific reductions** (LCM and ACPM vs. HA at weeks 1, 4, 6): significant reductions in commensals, gingivitis-associated species, and malodor/halitosis-associated species; no significant effect on acidogenic (caries) species
- **Beta diversity (PCoA)**: LCM and ACPM microbiomes at weeks 4 and 6 shifted toward healthy reference cohort cluster; AFPM and HA remained in gingivitis cluster — first demonstration of LCM-induced microbiome reset to health-associated state
- **Key species elevated in gingivitis vs. healthy** (selected, absolute logCMU values): *Fusobacterium nucleatum* (2.968 healthy vs. 4.472 gingivitis, p=0.001); *Prevotella veroralis* (1.876 vs. 3.339, p=0.002); *Candidatus Saccharibacteria* TM7x (3.929 vs. 5.055, p=0.002); *Leptotrichia buccalis* (3.365 vs. 4.515, p=0.002) — most of these were significantly reduced by LCM and ACPM to levels comparable with or below healthy cohort

**Methodology validation**: SMS spike-in CMU values for total anaerobes, Fusobacteria, Streptococci, and Actinomyces fell within published colony-count ranges; 16S rRNA qPCR values were ~1 log unit higher due to non-specific amplification of aerobic/transient extraoral species.

## Related Papers

- [[oral-microbiology/lamont-2018-oral-microbiota-dynamic-communities-host]] — ecological framework for oral microbiome stability and dysbiosis; this RCT provides direct clinical evidence that dysbiosis is reversible with EOMW
- [[oral-microbiology/hajishengallis-2012-psd-model-periodontal-disease]] — polymicrobial synergy and dysbiosis (PSD) model; the EO reset mechanism is consistent with disrupting polymicrobial dysbiosis at the supragingival level
- [[oral-microbiology/jakubovics-2021-dental-plaque-biofilm-matrix]] — dental plaque biofilm matrix composition; the species affected by EO mouthrinses are major matrix-contributing organisms
- [[oral-microbiology/sedghi-2021-oral-microbiome-key-organisms-networks]] — key organisms and interaction networks in oral microbiome; several species highlighted here (Fusobacterium nucleatum, Prevotella spp.) are discussed as keystone species
