---
title: "Different surface treatments and adhesive monomers for zirconia-resin bonds: A systematic review and network meta-analysis"
authors: Li X, Liang S, Inokoshi M, Zhao S, Hong G, Yao C, Huang C
year: 2024
doi: 10.1016/j.jdsr.2024.05.004
category: [resin-bonding]
source_collection: pubmed-text
full_text: true
pmid: "38938474"
pmcid: "PMC11208804"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11208804/
text_path: /Users/oracleneo/llm-wiki/papers/li-2024-zirconia-surface-treatments-monomers-nma.txt
text_filename: li-2024-zirconia-surface-treatments-monomers-nma.txt
---

## Why Ingested

This Bayesian network meta-analysis (Li 2024, 77 in-vitro studies) directly ranks both mechanical surface treatments AND chemical adhesive monomers for zirconia-resin bonding in one model, establishing that 10-MDP-based formulations are superior to all other acidic monomers and that non-MDP formulations are essentially ineffective. It extends the chemical-interaction evidence in [[wiki/resin-bonding/nagaoka-2017-mdp-zirconia-chemical-interaction-nmr]] (NMR mechanism of the MDP–Zr bond) from molecular mechanism into a quantitative cross-treatment ranking, and complements the clinical-durability synthesis in [[wiki/prosthetic-materials/alammar-2022-zirconia-bonding-durability-clinical-outcomes-sr]] and the MDP-cleaner contamination work in [[wiki/dental-materials/zirconia/awad-2022-mdp-cleaner-contaminated-zirconia]].

## One-line Summary

Bayesian network meta-analysis (77 in-vitro studies): for zirconia-resin bonding, SIE/hot-etching rank highest by SUCRA but air abrasion remains the practical standard; fine air-abrasion particles (25–53 µm) beat coarse (110–150 µm) immediately, Rocatec > CoJet, and 10-MDP-containing primers/cements are significantly superior to all other acidic monomers (MD 12.15 MPa), while silane/HEMA alone and gas plasma confer no benefit.

## 한줄요약

베이지안 네트워크 메타분석(in-vitro 77편): 지르코니아-레진 접착에서 SIE/hot-etching이 SUCRA 1·2위지만 임상 표준은 여전히 표면처리(air abrasion), 미세 입자(25–53 µm)가 즉시접착에서 굵은 입자(110–150 µm)보다 우수, Rocatec > CoJet, 10-MDP 함유 프라이머/시멘트가 다른 모든 산성 모노머보다 유의하게 우수(MD 12.15 MPa)인 반면 실란/HEMA 단독·가스 플라즈마는 효과 없음.

## 1. Document Information

- **Title**: Different surface treatments and adhesive monomers for zirconia-resin bonds: A systematic review and network meta-analysis
- **Authors**: Li X, Liang S, Inokoshi M, Zhao S, Hong G, Yao C, Huang C
- **Journal**: Japanese Dental Science Review 2024;60:175–189
- **Year**: 2024 (e-pub 2024-06-07)
- **DOI**: 10.1016/j.jdsr.2024.05.004
- **PMID**: 38938474 | **PMCID**: PMC11208804
- **Study type**: Systematic review + Bayesian network meta-analysis (NMA) of in-vitro studies
- **Source**: PMC open-access full text (pubmed-text)

## 2. Key Contributions

- **First NMA** to simultaneously juxtapose multiple mechanical surface treatments AND adhesive-monomer combinations for zirconia-resin bonding, rather than the prior descriptive/pairwise approach.
- Ranks 7 surface treatments (control, air abrasion, silica coating, SIE, laser, hot etching, gas plasma) and 12 primer/cement component combinations by SUCRA in both immediate and aged conditions.
- Establishes 10-MDP as the dominant chemical determinant: any formulation lacking 10-MDP is ineffective; the four 10-MDP-containing formulations do not differ significantly from each other.
- Quantifies practical sub-questions via standard pairwise meta-analysis (SPMA): air-abrasion particle size, silica-coating system (CoJet vs Rocatec), and 10-MDP vs other acidic monomers.
- Characterizes bond durability: 91.2% of bonds weaken after aging, but air abrasion and silica coating significantly mitigate the decline.

## 3. Methodology and Architecture

- **Reporting/guidelines**: PRISMA Extension for NMA + Cochrane Handbook. Research question: "which surface treatment method and adhesive monomer are most advantageous for bonding to zirconia?"
- **Databases**: PubMed (MEDLINE), Embase, Web of Science, Scopus, Cochrane Library; Jan 2000 – May 30, 2023; two independent reviewers.
- **Screening yield**: 8878 records → 4518 after de-duplication screened on title/abstract → 181 full-text (+2 manual) → **77 in-vitro studies included** (104 excluded).
- **Bias tool**: modified CONSORT (15 items; 0–5 high, 6–10 medium, 11–15 low risk).
- **Statistics**:
  - **NMA**: Four Bayesian NMAs (R packages gemtc 0.9–8 and BUGSNET 1.0.3 in MetaInsight V4.0.0) — two on surface methods, two on bonding-agent components, each split into immediate and aged samples. League tables via MCMC (5000 burn-in, 20,000 iterations, 4 chains, thinning 1). SUCRA ranks treatments; network plots in Stata 17.0; convergence via Brooks–Gelman–Rubin trace plots; inconsistency via split-node method.
  - **SPMA**: Review Manager 5.4, random-effects model, 95% CI, p<0.05; heterogeneity via Cochran Q and I². Targeted air-abrasion particle size, silica-coating system, and 10-MDP.
- **Bond-strength tests** in the corpus: macroshear 61.0%, microshear 19.5%, microtensile 11.7%, macrotensile 7.8%.
- **Surface treatment usage** (n studies): air abrasion 54, silica coating 25, laser 16, SIE 8, gas plasma 5, hot etching 4.
- **Aging**: protocol based on ISO 10477–2020; minimum 5000 thermocycles.

## 4. Key Results and Benchmarks

- **Surface SUCRA (immediate)**: SIE 91.30% > hot etching 86.76% > silica coating 68.77% > air abrasion 49.68% > laser 33.90% > gas plasma 17.98%.
- **Surface SUCRA (aged)**: SIE 90.49% > hot etching 85.16% > laser 56.93% > silica coating 53.65% > air abrasion 46.84% > gas plasma 9.44%.
- **vs air abrasion (MD)**: SIE statistically superior (immediate 5.73, 95% CI 0.93–10.53; aged 6.15, 95% CI 0.72–11.54). No significant difference for other treatments vs air abrasion, except gas plasma was significantly worse in aged conditions (−9.78, 95% CI −16.74 to −2.76).
- **Gas plasma** was the only surface treatment NOT significantly better than control (immediate ES 2.82, 95% CI −1.47 to 7.16; aged ES 0.440, 95% CI −6.27 to 7.16).
- **Air-abrasion particle size (SPMA)**: small (25–53 µm) > large (110–150 µm) for immediate bond strength (p<0.00001); no significant difference long-term (p=0.52).
- **Silica coating (SPMA)**: Rocatec Soft and Rocatec Plus both > CoJet; Rocatec Soft vs Rocatec Plus not different (immediate p=0.64, aged p=0.14).
- **10-MDP vs other acidic monomers (SPMA)**: 10-MDP superior, MD 12.15 MPa (95% CI 8.91–15.39, p<0.00001); consistent across aging (interaction p=0.80).
- **Adhesive-monomer NMA** (27 studies; 24 immediate, 24 aged): only 10-MDP-containing formulations (10-MDP; silane+10-MDP; HEMA+10-MDP; silane+HEMA+10-MDP) were effective vs control; silane+HEMA+10-MDP showed highest bonding potential, HEMA-only the lowest. The four 10-MDP formulations did not differ significantly. HEMA and silane addition diminished/did not augment the 10-MDP benefit.
- **Durability** (204 data points; 102 matched immediate/aged pairs): 91.2% of bonds decreased after aging. Fitted slopes — air abrasion m=0.78±0.10 and silica coating m=0.72±0.13 significantly mitigate decline vs control m=0.27±0.11.
- **Risk of bias**: 94.8% medium, 5.2% (4 studies) high; only 3.9% reported randomization or sample-size calculation; limitations reported in 48.1%, funding in 51.9%.

## 5. Limitations and Future Work

- Substantial heterogeneity among included studies may reduce precision of pooled estimates.
- Exclusively in-vitro evidence — direct extrapolation to clinical practice is limited; no oral-environment factors (pH, saliva/blood contamination, occlusal load).
- SIE ranked highest but the evidence base is small (8 studies) and the technique is multi-step and sensitive; hot etching uses corrosive chemicals — both need clinical refinement.
- No standardized aging protocol for zirconia-resin bonds.
- Calls for in-vivo experiments / better oral-environment-simulating in-vitro methods and long-term clinical trials.

## 6. Related Work

- Builds on prior pairwise/descriptive meta-analyses that established the value of combining mechanical + chemical treatment but could not rank specific options.
- Mechanistic basis of the 10-MDP–zirconia bond detailed by NMR work (Nagaoka 2017).
- Clinical durability of zirconia bonding reviewed by Alammar 2022.
- Contamination/cleaning of 10-MDP-treated zirconia addressed by Awad 2022.

## 7. Glossary

- **Y-TZP**: yttria-stabilized tetragonal zirconia polycrystalline ceramic.
- **10-MDP**: 10-methacryloyloxydecyl dihydrogen phosphate; acidic functional monomer that bonds chemically to zirconia via Zr–O–P interactions.
- **NMA**: network meta-analysis — combines direct and indirect comparisons to rank multiple treatments simultaneously.
- **SUCRA**: surface under the cumulative ranking curve; higher (→100%) = more likely the best treatment.
- **SIE**: selective infiltration etching — glass conditioning + heating + acid rinse to create a retentive zirconia surface.
- **TSC**: tribochemical silica coating (e.g., CoJet, Rocatec) — silica-coated alumina particles deposit silica + roughen the surface for silane bonding.
- **HEMA**: 2-hydroxyethyl methacrylate; low-molecular wetting monomer.
- **MPS**: 3-methacryloxypropyltrimethoxysilane; common silane coupling agent.
- **SPMA**: standard pairwise meta-analysis.
