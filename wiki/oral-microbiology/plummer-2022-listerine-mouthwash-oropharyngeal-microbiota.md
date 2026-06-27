---
title: "The Impact of Mouthwash on the Oropharyngeal Microbiota: OMEGA Trial Substudy (Plummer 2022)"
authors: Plummer EL, Maddaford K, Murray GL, Fairley CK, Pasricha S, Mu A, Bradshaw CS, Williamson DA, Chow EPF
year: 2022
date: 2022-01-12
doi: 10.1128/spectrum.01757-21
pmid: "35019769"
pmcid: "PMC8754113"
source: plummer-2022-listerine-mouthwash-oropharyngeal-microbiota.md
category: [oral-microbiology]
confidence: rct
text_path: /Users/oracleneo/llm-wiki/papers/plummer-2022-listerine-mouthwash-oropharyngeal-microbiota.txt
text_filename: plummer-2022-listerine-mouthwash-oropharyngeal-microbiota.txt
source_collection: pubmed-text
tags: [mouthwash, listerine, microbiome, essential-oil, long-term-safety]
---

## One-line Summary

RCT substudy (n=153, 12 weeks), daily Listerine Zero use produced no significant shift in oropharyngeal microbiota composition; Biotène caused small significant decreases in Streptococcus and Rothia.

## 한줄요약

RCT 서브스터디 (n=153, 12주), 리스테린 제로 매일 사용은 구인두 마이크로바이오타 구성에 유의한 변화 없었으며; Biotène은 Streptococcus·Rothia 소폭 유의 감소.

## Summary

The OMEGA (Oral Mouthwash use to Eradicate GonorrhoeA) trial substudy examined whether 12 weeks of daily antiseptic mouthwash use alters the oropharyngeal microbiota in MSM. Participants (n=153) were randomized to **Listerine Zero** (alcohol-free essential oil: thymol/eucalyptol/menthol/methyl salicylate) vs. **Biotène** (salivary enzyme system: lactoperoxidase/lysozyme/glucose oxidase). Tonsillar fossae swabs were collected at week 0 and week 12 and characterized by 16S rRNA V4 amplicon sequencing.

**Key finding**: Listerine Zero showed no significant change in overall microbiota structure (PERMANOVA p=0.413) and no differentially abundant taxa after FDR correction. Biotène showed a small but significant decrease in Streptococcus (FDR-p=0.004) and Rothia (FDR-p=0.03) — though species-level identification was not possible (commensal vs. pathogenic indistinguishable). Both groups showed a marginal increase in Shannon diversity (clinically non-meaningful).

## Key Contributions

- Demonstrates **12-week microbiota safety** of Listerine Zero (alcohol-free EO formulation)
- Contrasts Listerine vs. Biotène: EO formulation microbiota-neutral; enzyme system causes small commensal reduction
- Contextualized against chlorhexidine (CHX): 7-day CHX causes significant diversity loss and nitrate-reducing bacteria reduction — not seen with Listerine
- Baseline prior mouthwash frequency had no effect on microbiota composition (daily users vs. never-users at baseline: identical structure)

## Methodology

- **Design**: RCT (double-blind, parallel, multicenter) substudy; Melbourne Sexual Health Centre 2017–2018
- **n**: 153 MSM; Listerine n=78, Biotène n=75
- **Intervention**: 20 mL rinse, ≥60 s, ≥1×/day × 12 weeks
- **16S rRNA**: V4 region, DADA2+Silva v138 (genus level)
- **Beta-diversity**: PERMANOVA on Bray-Curtis (999 permutations)
- **Differential abundance**: ALDEx2 (Dirichlet MC, FDR) + ANCOM (W≥0.8) for confirmation
- **Sensitivity**: excluding/including prior daily users — results unchanged

## Results

| Outcome | Listerine Zero | Biotène |
|---|---|---|
| Overall microbiota shift (PERMANOVA p) | **0.413** (NS) | **0.331** (NS) |
| Shannon diversity change | 3.5 → 3.6 (p=0.012) | 3.5 → 3.6 (p=0.002) |
| FDR-significant genera decreased | **None** | Streptococcus ↓, Rothia ↓ |
| Baseline microbiota (top genera) | Streptococcus 23%, Prevotella 11%, Veillonella 7% | (same population) |

Gonorrhea infection status: no effect on microbiota structure (PERMANOVA p=0.078). Smoking: explained only 1.2% variance (p=0.04), no FDR-significant genera.

## Clinical Relevance for Mouthwash Use

- **Listerine Zero** (alcohol-free EO) is microbiota-neutral over 12 weeks — supports long-term daily use safety from microbiome standpoint
- Limitations apply: (1) alcohol-containing original Listerine not tested; (2) immediate transient post-rinse changes unmeasured; (3) MSM population only; (4) 12 weeks — not 6 months or longer
- Biotène's small reduction in Streptococcus/Rothia is of unclear clinical significance — these genera include both commensals and pathogens; species-level harm cannot be ruled out or confirmed
- Contrasts sharply with CHX mouthwash: CHX causes diversity loss and reduces nitrate-reducing bacteria (cardiovascular relevance), which Listerine does not

## Related Papers

- [[oral-microbiology]] — oral microbiome ecology overview
