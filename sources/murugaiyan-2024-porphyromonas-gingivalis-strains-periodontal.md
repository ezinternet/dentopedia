---
title: "Defining Porphyromonas gingivalis strains associated with periodontal disease"
authors: Murugaiyan V, Utreja S, Hovey KM, et al.
year: 2024
doi: 10.1038/s41598-024-56849-x
category: [periodontics]
source_collection: pubmed-text
full_text: true
pmid: "38485747"
pmcid: "PMC10940620"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10940620/
text_path: /Users/oracleneo/llm-wiki/papers/murugaiyan-2024-porphyromonas-gingivalis-strains-periodontal.txt
text_filename: murugaiyan-2024-porphyromonas-gingivalis-strains-periodontal.txt
---

## Why Ingested

Found while mining the reference list of a paper on dental floss sequence and plaque removal efficacy, which frames dental plaque biofilm as the etiological driver of periodontal disease. That framing stays at the community/biofilm level; this paper adds strain-level resolution to the single most-cited keystone pathogen within that biofilm, P. gingivalis, and shows that not all colonizing strains carry equal clinical weight — the W83/W50 strain is significantly enriched in moderate/severe periodontitis (13% of that group, p = 0.0003) while the avirulent ATCC33277/381 strain dominates across all disease states. This directly extends the mechanistic host-manipulation account in [[wiki/oral-microbiology/hajishengallis-2014-porphyromonas-gingivalis-host-manipulation]], which treats P. gingivalis largely as a single keystone actor — this paper is a reminder that strain identity, not just presence/abundance, may modulate the pathogen's clinical impact, with implications for future 16S/shotgun-based dysbiosis models like [[wiki/oral-microbiology/hajishengallis-2012-psd-model-periodontal-disease]].

## Three-line Summary

Cross-sectional strain-identification study (n=153 postmenopausal women, OsteoPerio/WHI ancillary cohort) validating a novel P. gingivalis intergenic spacer region (ISR) amplicon-sequencing method against clinical periodontal disease status.

The W83/W50 strain was the only one of 18 analyzed strains significantly enriched in Moderate/Severe periodontitis (13% of that group harbored it; p = 0.0003, q = 0.005), while the avirulent ATCC33277/381 strain was the most abundant strain across all disease states.

Standard 16S/shotgun microbiome methods cannot resolve P. gingivalis at the strain level; this ISR-targeted two-step PCR + Illumina approach is cost-effective and reproducible, but strains sharing identical ISR sequences (e.g., W83 and W50) remain indistinguishable and correlations with continuous PD/CAL measures were not significant.

## 세줄요약

단면 연구(cross-sectional), 폐경 후 여성 n=153(OsteoPerio/WHI 코호트) 대상 신규 P. gingivalis 균주 식별법(intergenic spacer region, ISR 시퀀싱) 검증 연구.

분석된 18개 균주 중 W83/W50 균주만 중등도/중증 치주염군에서 유의하게 증가(해당 군의 13%가 보유; p=0.0003, q=0.005), 반면 무독성 ATCC33277/381 균주는 모든 질환 단계에서 가장 우세한 균주로 확인.

기존 16S/shotgun 미생물체 분석법은 P. gingivalis를 균주 수준까지 구분 못하는데, 본 ISR 표적 two-step PCR + Illumina 시퀀싱법은 비용효율적·재현성 있으나 ISR 서열이 동일한 균주(W83·W50 등)는 여전히 구분 불가하며 연속변수(PD/CAL)와의 상관관계는 유의하지 않았음.

## 1. Document Information

- **Title**: Defining Porphyromonas gingivalis strains associated with periodontal disease
- **Authors**: Murugaiyan V, Utreja S, Hovey KM, Sun Y, LaMonte MJ, Wactawski-Wende J, Diaz PI, Buck MJ
- **Journal**: Scientific Reports, 2024;14(1):6222
- **DOI**: 10.1038/s41598-024-56849-x
- **PMID**: 38485747 / **PMCID**: PMC10940620
- **Publication date**: 2024-03-14
- **Institution**: Jacobs School of Medicine and Biomedical Sciences, University at Buffalo (Departments of Biochemistry, Epidemiology & Environmental Health, Microbiology & Immunology, Biomedical Informatics) and UB School of Dental Medicine (Department of Oral Biology / UB Microbiome Center)

## 2. Key Contributions

- Developed a novel, cost-effective PCR + Illumina sequencing assay targeting the P. gingivalis-specific 16S/23S intergenic spacer region (ISR) to resolve strain identity — something standard 16S rRNA and shotgun metagenomic approaches cannot do.
- Validated the assay's specificity (no amplification of non-P. gingivalis/negative controls), sensitivity (detects spiked-in DNA down to 1 ng in a complex background), and reproducibility (highly concordant technical replicates split before DNA extraction).
- Applied the assay to a well-characterized clinical cohort (OsteoPerio/WHI, n=153) and identified 139 unique ISR sequences, mapping to a custom reference database built from 67 published P. gingivalis genomes.
- Demonstrated a specific clinically meaningful association: the W83/W50 strain is significantly and exclusively enriched in Moderate/Severe periodontitis, while ATCC33277/381 (a strain long characterized as avirulent) dominates the overall sample regardless of disease state.

## 3. Methodology and Architecture

- **Design**: Cross-sectional strain-association analysis nested within a prospective cohort (Buffalo Osteoporosis and Periodontal Disease [OsteoPerio] Study, an ancillary study of the Women's Health Initiative Observational Study), in postmenopausal women with complete clinical periodontal exams (PD, CAL scored to CDC/AAP none/mild/moderate/severe categories).
- **Assay**: Two-step PCR amplicon library prep targeting a ~200-250 bp information-rich region within the P. gingivalis ISR flanked by conserved primer sites; dual-indexed and sequenced on Illumina MiSeq (2×300), multiplexed 1:5 with shotgun microbiome libraries to offset low amplicon complexity.
- **Bioinformatics**: DADA2 pipeline (Cutadapt primer trimming, Q30 quality filtering, error-rate learning, dereplication, ASV inference, chimera removal) mapped amplicon sequence variants (ASVs) to a custom ISR reference database built from all available P. gingivalis genomes via BLASTN; unmatched novel sequences assigned provisional "PG-Strain #" names.
- **Statistics**: Centered log-ratio (CLR) transformation of strain abundance (compositional-data-appropriate); discrete FDR correction for multiple testing across 18 filtered strains; Pearson correlation of CLR abundance vs. whole-mouth mean PD/CAL; alpha diversity (Shannon, Chao1) and enrichment testing via MicrobiomeAnalyst.
- **Controls**: Positive controls (ATCC33277 strain, pooled subgingival plaque), negative controls (Zymo mock DNA, microbial-DNA-free water), and 5 split-sample technical replicates.

## 4. Key Results and Benchmarks

- 139 unique P. gingivalis ISR sequences detected across 153 participants (161 samples total including pools/controls).
- Positive controls: 99.99-100% of reads correctly mapped to ATCC33277.
- Most participants' P. gingivalis population was dominated (>90% of reads) by a single top strain, typically among 1-2 strains total per participant.
- After filtering, 18 strains analyzed for None/Mild vs Moderate/Severe association: only W83_W50 reached significance (p=0.0003, q=0.005), detected in 13% of the Moderate/Severe group and absent from None/Mild.
- ATCC33277_381 (avirulent reference strain) was the most abundant strain overall (CLR 6.38 none/mild vs 5.34 moderate/severe — nonsignificant trend toward the healthier group).
- CLR-strain-abundance correlations with continuous PD (range -0.134 to 0.142) and CAL (range -0.095 to 0.152) were not significant after multiple-testing correction.
- ISR-library DNA concentration and P. gingivalis read counts were both significantly higher in moderate/severe vs. none/mild groups, consistent with known abundance-disease severity relationships.

## 5. Limitations and Future Work

- A meaningful subset of characterized P. gingivalis strains share identical sequence in the targeted ISR region (e.g., W83 and W50 cannot be separated); resolving these would require additional primer sets in virulence-associated genes.
- Strain assignment is limited by the completeness of the reference database (67 genomes at time of study); accuracy should improve as more P. gingivalis strains are sequenced.
- Low-complexity amplicon libraries on Illumina platforms require spike-in dephasing strategies or multiplexing with high-complexity libraries — a technical overhead specific to single-target strain assays.
- Sample size (153 participants, all postmenopausal women from one cohort) and cross-sectional design limit generalizability and preclude causal inference; correlations with continuous clinical measures (PD, CAL) were not significant, so the strain-disease association is currently only demonstrated as a categorical (none/mild vs moderate/severe) enrichment.

## 6. Related Work

- Builds on prior strain-typing methods (multilocus enzyme electrophoresis, RAPD fingerprinting, MLST) that separated P. gingivalis into 41-73 strains, and prior heteroduplex-typing studies associating W83 with periodontitis severity and virulence.
- Complements 16S rRNA-based subgingival microbiome characterization of the same OsteoPerio cohort (cited as a prior analysis of this cohort).
- Directly relevant to the P. gingivalis host-manipulation mechanistic literature (e.g., [[wiki/oral-microbiology/hajishengallis-2014-porphyromonas-gingivalis-host-manipulation]]) and the polymicrobial synergy and dysbiosis (PSD) keystone-pathogen model ([[wiki/oral-microbiology/hajishengallis-2012-psd-model-periodontal-disease]]), both of which treat P. gingivalis largely at the species level rather than the strain level.

## 7. Glossary

- **ISR (Intergenic Spacer Region)**: The variable-length, sequence-variable DNA segment between the 16S and 23S ribosomal RNA genes in bacteria; used here as a strain-discriminating marker because it is far more variable between P. gingivalis strains than the 16S gene itself.
- **ASV (Amplicon Sequence Variant)**: A unique sequence inferred from amplicon sequencing data by denoising algorithms (e.g., DADA2), distinguishing sequences differing by as little as one nucleotide, used in place of traditional OTU clustering.
- **CLR (Centered Log-Ratio) transformation**: A compositional-data-appropriate normalization method that log-transforms each feature relative to the geometric mean of all features in a sample, reducing spurious correlation risk inherent to relative-abundance (compositional) microbiome data.
- **Red-complex bacteria**: The Socransky microbial-complex classification's most disease-associated subgingival bacterial cluster (P. gingivalis, Tannerella forsythia, Treponema denticola).
- **W83/W50, ATCC33277**: Reference P. gingivalis strains; W83 is a well-characterized highly virulent strain (used in animal abscess models), ATCC33277 is a commonly used lower-virulence/avirulent reference strain.
