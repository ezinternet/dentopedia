---
title: "Defining Porphyromonas gingivalis strains associated with periodontal disease"
authors: Murugaiyan V, Utreja S, Hovey KM, Sun Y, LaMonte MJ, Wactawski-Wende J, Diaz PI, Buck MJ
year: 2024
date: 2024-03-14
doi: 10.1038/s41598-024-56849-x
source: murugaiyan-2024-porphyromonas-gingivalis-strains-periodontal.md
category: [periodontics]
evidence_level: cross-sectional
source_collection: pubmed-text
full_text: true
pmid: "38485747"
pmcid: "PMC10940620"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10940620/
text_path: /Users/oracleneo/llm-wiki/papers/murugaiyan-2024-porphyromonas-gingivalis-strains-periodontal.txt
text_filename: murugaiyan-2024-porphyromonas-gingivalis-strains-periodontal.txt
tags: [P-gingivalis, strain-typing, ISR-sequencing, W83, ATCC33277, keystone-pathogen, oral-microbiome, dysbiosis]
relations:
  - type: refines
    target: hajishengallis-2014-porphyromonas-gingivalis-host-manipulation
  - type: refines
    target: hajishengallis-2012-psd-model-periodontal-disease
---

## Three-line Summary

Cross-sectional strain-identification study (n=153 postmenopausal women, OsteoPerio/WHI ancillary cohort) validated a novel P. gingivalis intergenic spacer region (ISR) amplicon-sequencing method able to resolve strain identity, something 16S/shotgun microbiome methods cannot do.

The W83/W50 strain was the only one of 18 analyzed strains significantly enriched in Moderate/Severe periodontitis (present in 13% of that group, absent from None/Mild; p = 0.0003, q = 0.005), while the avirulent ATCC33277/381 strain was the single most abundant strain across all disease states.

Strains sharing identical ISR sequence (e.g., W83 and W50) remain indistinguishable by this assay, and CLR-strain-abundance did not correlate significantly with continuous pocket-depth/attachment-level measures — the association is currently demonstrated only as a categorical disease-severity enrichment.

## 세줄요약

단면 연구(cross-sectional), 폐경 후 여성 n=153(OsteoPerio/WHI 코호트) 대상, 16S/shotgun 분석법이 하지 못하는 P. gingivalis 균주 수준 식별을 가능케 하는 신규 intergenic spacer region (ISR, 유전자간 스페이서 부위) 시퀀싱법 검증.

분석한 18개 균주 중 W83/W50 균주만 중등도/중증 치주염군에서 유의하게 증가(해당 군의 13%에서 검출, 경도/무병군에서는 미검출; p=0.0003, q=0.005), 반면 무독성 ATCC33277/381 균주는 질환 단계와 무관하게 가장 우세한 단일 균주로 확인.

ISR 서열이 동일한 균주(W83·W50 등)는 여전히 구분 불가하며, CLR 변환 균주 존재비는 연속변수인 치주낭깊이(PD)·부착소실(CAL)과 유의한 상관을 보이지 않아 — 현재까지는 범주형(중등도/중증 vs 경도/무병) 질환중증도 연관성만 입증된 상태.

## Summary

Standard oral microbiome methods (16S rRNA amplicon or shotgun metagenomics) cannot resolve Porphyromonas gingivalis at the strain level, despite decades of evidence that different P. gingivalis strains carry markedly different virulence profiles (e.g., W83 causing spreading ulcerative lesions in animal models vs. other strains producing only localized abscesses). This study developed and validated a targeted PCR + Illumina sequencing assay against the P. gingivalis-specific 16S/23S intergenic spacer region (ISR) — a region far more sequence-variable between strains than 16S itself — and applied it to subgingival plaque from 153 postmenopausal women in the Buffalo OsteoPerio cohort (an ancillary study of the Women's Health Initiative Observational Study) with clinically graded periodontal disease status (none/mild/moderate/severe by CDC/AAP criteria). The assay was specific (no amplification of non-target/negative controls), sensitive (detected spiked DNA at 1 ng in complex background), and reproducible (concordant technical replicates). Of 18 strains analyzed after filtering, only the W83/W50 strain — previously flagged by heteroduplex typing and multiple prior virulence studies as more pathogenic — was significantly and exclusively enriched in the Moderate/Severe group (13% prevalence there, p=0.0003, q=0.005), while the reference avirulent strain ATCC33277/381 was the most abundant strain overall regardless of disease state.

## Key Contributions

- First cost-effective, strain-resolving amplicon sequencing assay specific to P. gingivalis, targeting the ISR rather than 16S rRNA, addressing the dual problem of (1) P. gingivalis being a minor fraction (0.1-5%) of total subgingival DNA and (2) 16S/shotgun methods missing strain-level variation entirely.
- Built and validated a custom reference database of 139 unique ISR sequences mapped against 67 published P. gingivalis genomes, with some sequences assigned provisional novel strain names ("PG-Strain #") when unmatched.
- Demonstrated in a real clinical cohort (n=153) that a single specific strain (W83/W50) — not overall P. gingivalis abundance — is the feature significantly associated with categorical periodontal disease severity.
- Confirmed ATCC33277/381 as the dominant strain in the sampled population overall, consistent with its long-standing characterization as a lower-virulence reference strain.

## Methodology

Cross-sectional strain-association analysis nested within the OsteoPerio cohort (prospective, postmenopausal women, complete periodontal exams for PD/CAL graded none/mild/moderate/severe). Two-step PCR generated dual-indexed ISR amplicon libraries (P. gingivalis-specific primers around a ~200-250 bp discriminating region), sequenced on Illumina MiSeq (2×300) multiplexed with shotgun libraries to offset low amplicon complexity. DADA2 pipeline (Cutadapt trimming, Q30 filtering, ASV inference, chimera removal) generated amplicon sequence variants mapped to the custom ISR reference database. Abundance data were CLR-transformed for compositional-data-appropriate statistics; strains were filtered to remove low-abundance/singleton detections, leaving 18 strains for None/Mild vs Moderate/Severe comparison with FDR-corrected significance testing; Pearson correlations assessed CLR-abundance vs. continuous PD/CAL.

## Results

- 139 unique ISR sequences identified across 153 participants; positive controls mapped 99.99-100% correctly to ATCC33277; 5 split-sample technical replicates were highly concordant.
- Most participants' P. gingivalis population was dominated (>90% of reads) by 1-2 strains.
- ISR library DNA concentration and P. gingivalis read depth were both significantly higher in moderate/severe vs. none/mild disease groups.
- Only W83_W50 reached significance after multiple-testing correction (p=0.0003, q=0.005) — detected exclusively in Moderate/Severe (13% prevalence there); 15 of 18 filtered strains trended toward higher abundance in Moderate/Severe but were not individually significant.
- ATCC33277_381 was the single most abundant strain overall (CLR 6.38 none/mild vs 5.34 moderate/severe, nonsignificant trend toward the healthier group).
- CLR-strain-abundance vs. whole-mouth mean PD (range -0.134 to 0.142) and CAL (range -0.095 to 0.152) showed no significant correlations after correction.

## Related Papers

- [[oral-microbiology/hajishengallis-2014-porphyromonas-gingivalis-host-manipulation]] — mechanistic account of how P. gingivalis subverts host immunity (C5aR-TLR2 crosstalk, gingipain-mediated complement evasion); this paper adds strain-level resolution showing not all P. gingivalis strains carry equal clinical weight, refining the largely species-level treatment in that review.
- [[oral-microbiology/hajishengallis-2012-psd-model-periodontal-disease]] — the polymicrobial synergy and dysbiosis (PSD) keystone-pathogen model that frames P. gingivalis as a low-abundance keystone driver of community-wide dysbiosis; this paper's strain-level data suggests keystone potency itself may vary by strain (W83/W50 vs. ATCC33277/381), a refinement not captured in the original PSD model.
