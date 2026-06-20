---
title: "Control of alveolar bone development, homeostasis, and socket healing by salt-inducible kinases"
authors: Nicha Tokavanich, Byron Chan, Katelyn Strauss, Christian D. Castro Andrade, Yuki Arai, Mizuki Nagata, Marc Foretz, Daniel J. Brooks, Noriaki Ono, Wanida Ono, Marc N. Wein
year: 2025
doi: 10.1093/jbmr/zjaf038
journal: Journal of Bone and Mineral Research 2025;40(5):656–670
category: [bone-biology]
pdf_path: /Users/oracleneo/llm-wiki/papers/tokavanich-2025-control-alveolar-bone-development.pdf
pdf_filename: tokavanich-2025-control-alveolar-bone-development.pdf
source_collection: external
---

## One-line Summary
Mouse model study showing that salt-inducible kinases SIK2/SIK3 (downstream of PTH/PTHrP signaling) control alveolar bone osteoblast maturation, BV/TV, and post-extraction socket healing — conditional SIK2/3 deletion (Ubiquitin-CreERt2) impairs alveolar bone development and slows socket repair, opening a path to PTH-pathway-targeted regenerative therapeutics distinct from long-bone biology.

## 1. Document Information
- **Journal**: Journal of Bone and Mineral Research 2025;40(5):656–670 (Advance access March 9, 2025)
- **Lead institution**: Endocrine Unit, Massachusetts General Hospital, Harvard Medical School (Wein lab); collaborators at UT Houston Dentistry (N. Ono lab) and Institut Cochin (Foretz).
- **Type**: In vivo mouse experiment with microCT, histology, scRNA-seq integration
- **Funding**: NIH (implied), Broad Institute, Harvard Stem Cell Institute

## 2. Key Contributions
- First demonstration that **SIK2/SIK3 control alveolar bone specifically** — prior SIK work focused on appendicular skeleton.
- Conditional SIK2/SIK3 deletion → reduced alveolar BV/TV, impaired socket healing after maxillary first molar extraction.
- Single-cell RNA-seq comparison (P21 femur vs P25 alveolar bone) identifies osteoblast cluster differences relevant to SIK function.
- Builds mechanistic bridge between systemic PTH/PTHrP biology and craniofacial regenerative medicine.
- Provides preclinical rationale for SIK inhibitors (e.g., YKL-05-099) as adjuncts to ARP / socket healing.

## 3. Methodology
- Mouse model: Ubiquitin-CreERt2 driven conditional SIK2/SIK3 deletion (tamoxifen-induced global).
- Tooth extraction: first maxillary molar removed bilaterally under isoflurane; sacrificed 3–4 weeks post-op.
- Histology: H&E, DAPI, TRAP (osteoclast), alkaline phosphatase (osteoblast).
- RNAscope in situ hybridization for spatial gene expression.
- MicroCT: alveolar BV/TV (%), alveolar BMD, fixed threshold 550 mg HA/cm³.
- Single-cell RNA-seq integration: GEO datasets GSM5623768 (P21 femur) and GSM5140554 (P25 alveolar bone); Seurat + Harmony pipeline; non-parametric Wilcoxon for DEGs.

## 4. Key Results and Benchmarks
- SIK2/SIK3 deletion → impaired alveolar bone osteoblast maturation; reduced BV/TV.
- Post-extraction socket healing slower in SIK2/3 mutants.
- scRNA-seq: distinct osteoblast subpopulations between long bone and alveolar bone; SIK target genes differentially regulated.
- Tooth phenotype absent — alveolar bone defect not secondary to tooth development.
- Authors discuss that global deletion (Ubi-CreERt2) cannot fully exclude systemic mineral metabolism (mild hypercalcemia, elevated 1,25-vitD) as confounder; cell-type-specific Cre drivers (e.g., Six2-Cre) proposed for future work.

## 5. Limitations and Future Work
- Global conditional deletion → cell-intrinsic vs systemic effects not fully separable.
- Mouse → human translation pending.
- SIK inhibitor pharmacology in alveolar context untested.
- Long-term socket outcomes (>4 weeks) not assessed.

## 6. Related Work
- [[bone-biology/kondo-2022-current-perspectives-residual-ridge]] — complementary mechanistic angle on alveolar bone biology (oral barrier osteoclasts).
- [[bone-regeneration/ridge-preservation/cardaropoli-2003-bone-tissue-formation-extraction]] — classical histological timeline that SIK genetic studies seek to mechanistically explain.
- [[bone-regeneration/ridge-preservation/araujo-2005-dimensional-ridge-alterations-tooth-extraction]] — phenotype Tokavanich's mouse model recapitulates.

## 7. Glossary
- **SIK (Salt-Inducible Kinase)**: AMPK-family serine/threonine kinase; SIK2/SIK3 are key downstream regulators of PTH/PTHrP signaling.
- **PTH/PTHrP**: Parathyroid Hormone / Parathyroid Hormone-related Protein — major regulators of bone remodeling via PTH1R.
- **BV/TV**: Bone Volume / Total Volume — microCT measure of bone density in a region of interest.
- **Ubiquitin-CreERt2**: Tamoxifen-inducible Cre driven by the ubiquitin promoter — globally expressed, conditional gene deletion tool.
- **scRNA-seq**: single-cell RNA sequencing.
- **PTH1R**: PTH/PTHrP receptor (GPCR).
