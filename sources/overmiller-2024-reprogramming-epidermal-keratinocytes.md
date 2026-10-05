---
title: "Reprogramming of epidermal keratinocytes by PITX1 transforms the cutaneous cellular landscape and promotes wound healing"
authors: "Overmiller AM, Ursich A, Hanna EDG, Ortega CG, Howard K, Narechania F, Deng S, Braunstein SR, Jiang K, Chen YW, Meijer MIM"
year: 2024
date: 2024-11-01
doi: "10.1172/jci.insight.182844"
pmid: "39480496"
pmcid: "PMC11665584"
category: [oral-surgery]
source_collection: pubmed-text
full_text: true
source_url: https://pubmed.ncbi.nlm.nih.gov/39480496/
---

## Why Ingested

Ingested to support the training-knowledge-seeded [[overviews/oral-mucosal-epithelial-turnover-overview]] page, which lists PITX1 as a key molecular driver of the faster oral keratinocyte proliferation and migration that underlies site-specific turnover rate differences. This paper provides the first in-depth mechanistic characterization of PITX1 as a transcriptional determinant of oral keratinocyte identity, directly underpinning the clinical claim that oral mucosa heals faster than skin.

## One-line Summary

Transgenic mouse scRNA-Seq + Xenium spatial transcriptomics study (n=8+8 mice) showing that ectopic PITX1 expression in skin keratinocytes drives an oral-like gene-expression state, increases proliferation and migration, and accelerates full-thickness wound closure via neutrophil-mediated inflammatory priming.

## 한줄요약

형질전환 마우스 단세포 RNA-Seq + Xenium 공간전사체학(n=8+8): 표피 케라티노사이트 (Epidermal Keratinocyte) 에 PITX1 이소발현 시 구강 유사 전사 상태로 전환·증식·이동 증가·전층 창상 치유가 가속화됨 — 중성구 (Neutrophil) 매개 염증성 프라이밍이 핵심 기전.

## 1. Document Information

- **Journal**: JCI Insight, Vol. 9, No. 21, November 2024
- **DOI**: [10.1172/jci.insight.182844](https://doi.org/10.1172/jci.insight.182844)
- **PMID**: 39480496 | **PMCID**: PMC11665584
- **Funding**: NIH (details in supplemental)
- **Conflicts**: none declared

## 2. Key Contributions

- Identifies PITX1 as a master transcriptional regulator of **oral keratinocyte (KC) identity** — highly expressed in oral epithelium, absent in skin epidermis.
- Demonstrates that ectopic PITX1 in skin KCs drives expression of canonical **activated/oral KC genes** (KRT6A, KRT16, S100A8/A9, ALDH1A3) directly bound by PITX1 (CUT&Tag-Seq).
- Shows PITX1 skin heals full-thickness wounds significantly faster (days 2–8 post-injury) via increased KC migration, granulation tissue formation, and neutrophil influx.
- Uses scRNA-Seq + Xenium to map how PITX1 reshapes not only keratinocytes but fibroblasts, immune cells, and intercellular signaling toward a buccal-mucosa-like state.
- PITX1-driven oral-like KC state is transferable without co-expression of other oral signature genes (SOX2, TP63, KLF4), confirming PITX1 as a **necessary and sufficient oral identity driver**.

## 3. Methodology and Architecture

- **Model**: Tet-On TRE-/-rtTA inducible transgenic mice expressing PITX1 in epidermis (doxycycline-fed for 6 weeks starting telogen phase); n=8 control + 8 PITX1 for scRNA-Seq; n=7 pools buccal mucosa for comparison
- **Sequencing**: scRNA-Seq (Seurat pipeline) + Xenium in situ spatial transcriptomics (328-probe custom panel); total 331,572 Xenium cells analyzed
- **CUT&Tag-Seq**: PITX1 genomic binding sites + H3K4me3 occupancy in isolated epidermal cells
- **Wound healing**: 6 mm full-thickness excisional wounds on dorsum; wound area measured days 0–12; histology day 4 + day 35
- **In vitro**: KC migration (scratch assay), proliferation (PCNA IF) in primary KCs with PITX1 knockdown/overexpression
- No human subjects; no statistical methods for sex-based differences (both sexes included)

## 4. Key Results and Benchmarks

- **Proliferation**: PITX1 skin and buccal mucosa both show significantly increased PCNA+ cells vs control skin
- **Migration**: PITX1 expression drives significantly increased KC migration in vitro
- **Wound healing**: PITX1 mice heal faster at days 2–8 (proliferative phase); both groups fully closed by day 14; no increase in fibrosis at day 35
- **Wound day 4**: granulation tissue area and IFE migration distance significantly greater in PITX1
- **scRNA-Seq**: PITX1 skin keratinocytes show higher oral pseudotime gene expression scores, increasing with differentiation
- **Neutrophils**: significant expansion of neutrophil populations in PITX1 skin; Ly-6G IHC confirms recruitment; neutrophils cluster around hair follicles
- **Alopecia**: irreversible alopecia in PITX1 mice due to HF stem cell loss + terminal differentiation arrest

## 5. Limitations and Future Work

- All experiments in murine model; murine skin differs from human skin in hair follicle density and wound healing kinetics
- Alopecia phenotype is an off-target effect limiting the clinical translation of constitutive PITX1 overexpression
- Persistent neutrophil influx in PITX1 skin — whether this causes damaging NETosis was not assessed
- PITX1 × RA signaling interaction (ALDH1A3 upregulation) is described but not mechanistically resolved
- Temporal/inducible or topical PITX1 delivery strategies for wound treatment not tested

## 6. Related Work

- Xu et al. (multiple, cited) — established oral KC priming at transcriptome level, identified SOX2/PITX1 as oral signatures in acute wound healing study
- Overmiller et al. (prior) — SOX2 overexpression in skin KC promotes healing via EGFR ligand secretion; PITX1 study follows same paradigm
- RORA/PITX1 in corneal stem cell differentiation (cited) — converging evidence for PITX1 as tissue-specific epithelial identity factor

## 7. Glossary

- **PITX1** (Paired-like homeodomain 1): homeodomain TF; oral signature gene
- **Activated KC**: wound-responding KC expressing KRT6A/KRT16/S100A8; primed state in oral mucosa at baseline
- **CUT&Tag-Seq**: epigenomic technique mapping TF genomic binding with fewer input cells than ChIP-Seq
- **Xenium**: 10x Genomics in situ spatial transcriptomics platform (subcellular transcript localization)
- **NETosis**: neutrophil extracellular trap formation; associated with chronic non-healing wounds
- **IFE**: interfollicular epidermis
- **HF**: hair follicle
