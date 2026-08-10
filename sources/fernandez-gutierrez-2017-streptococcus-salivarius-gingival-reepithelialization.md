---
title: "Streptococcus salivarius MS-oral-D6 promotes gingival re-epithelialization in vitro through a secreted serine protease"
authors: Marcela M. Fernandez-Gutierrez, Peter P.J. Roosjen, Eveline Ultee, Maarten Agelink, Jacques J.M. Vervoort, Bart Keijser, Jerry M. Wells, Michiel Kleerebezem
year: 2017
doi: 10.1038/s41598-017-11446-z
category: [periodontics/host-modulation]
pdf_path: /Users/oracleneo/llm-wiki/papers/fernandez-gutierrez-2017-streptococcus-salivarius-gingival-reepithelialization.pdf
pdf_filename: fernandez-gutierrez-2017-streptococcus-salivarius-gingival-reepithelialization.pdf
source_collection: external
---

## Why Ingested
Existing wiki coverage of probiotics in periodontics is entirely clinical-outcome level (RCTs/SR-MA on BOP, PPD, CAL — see [[wiki/overviews/periodontal-adjunctive-therapy-probiotics-pdt-overview]]); this paper supplies the missing mechanistic layer — a specific bacterial strain and secreted molecule shown to accelerate gingival epithelial wound closure in vitro, offering a candidate explanation for why probiotic adjuncts might improve inflammatory indices clinically.

## Three-line Summary
In-vitro high-throughput scratch-assay screen of 39 lactic acid bacteria (LAB) strains on the Ca9-22 gingival epithelial cell line, using automated fluorescence microscopy and a modified Gompertz kinetic model to quantify re-epithelialization.
Streptococcus salivarius MS-oral-D6 was the strongest stimulator (~2.5-fold vs untreated control), and its effect was traced to a secreted >180 kDa serine protease (not lactic/acetic acid) whose activity was abolished by the protease inhibitor PMSF; P. gingivalis W83 significantly inhibited re-epithelialization and served as a negative-control benchmark.
Purely in-vitro mechanistic evidence (no animal or human data) — clinical translation requires confirming the effector protein's mechanism and testing purified protein or high-producing strains in vivo.

## 세줄요약
잇몸상피세포주(Ca9-22)를 이용한 고처리량 스크래치 분석(scratch assay)으로 유산균(Lactic Acid Bacteria, LAB) 39종을 스크리닝한 시험관내(in-vitro) 연구, 자동형광현미경과 변형 곰페르츠(Gompertz) 모델로 재상피화(re-epithelialization) 동역학을 정량화했다.
살리바리우스연쇄상구균(Streptococcus salivarius) MS-oral-D6 균주가 가장 강력한 촉진 효과(무처치 대비 약 2.5배)를 보였고, 그 효과는 유산·초산이 아닌 분비형 세린단백분해효소(secreted serine protease, >180 kDa)에 기인했으며 단백분해효소 억제제(PMSF)로 효과가 소실됐다; 치은포르피로모나스균(P. gingivalis) W83은 대조적으로 재상피화를 유의하게 억제했다.
순수 시험관내(in-vitro) 기전 연구로 동물·인체 데이터가 없어, 임상 적용 전 정제 단백질 또는 고생산 균주의 생체내(in-vivo) 검증이 필요하다.

## 1. Document Information
- **Journal**: Scientific Reports 2017;7:11100
- **DOI**: 10.1038/s41598-017-11446-z
- **Institution**: TI Food and Nutrition / Wageningen University & Research, The Netherlands (Department of Preventive Dentistry, ACTA Amsterdam co-author affiliation)

## 2. Key Contributions
- Developed a high-throughput (96-well), automated scratch-assay platform (HTSScratcher + CellProfiler image segmentation) for quantifying gingival epithelial re-epithelialization kinetics, improving on low-throughput manual 24-well scratch assays
- Modified Gompertz function fit of cell-infiltration curves yields three biologically interpretable parameters (repair rate μm, plateau cell number A, lag time λ) with excellent fit (R² close to 1)
- Identified S. salivarius MS-oral-D6 as the strongest LAB stimulator of gingival re-epithelialization among 39 strains screened, and identified a secreted serine protease as the likely effector molecule via desalting, proteinase K sensitivity, SDS-PAGE/silver staining, and LC-MS/MS peptide mapping

## 3. Methodology and Architecture
- **Design**: In-vitro experimental study (cell-based high-throughput screening + mechanistic follow-up)
- **Cell line**: Ca9-22 (JCRB0625) gingival epithelial cells
- **n**: 39 LAB strains screened (duplicate primary screen); 6 strains selected for dose-response (MOI 10/50/250, n=3 replicates, ≥2 independent experiments); positive control hTGFα, negative control p38+MEK1/2 inhibitors; P. gingivalis W83 and L. rhamnosus GG as literature-benchmark reference strains
- **Outcomes**: Re-epithelialization kinetic parameters (μm, A, μm*A performance value) via tissue-recognition and cell-recognition image-analysis pipelines; lactic/acetic acid concentration (fermentation end products); IL-8 (pro-inflammatory cytokine); protein identification via LC-MS/MS

## 4. Key Results and Benchmarks
- hTGFα (positive control) increased re-epithelialization >5-fold; p38/MEK1/2 inhibitors (negative control) suppressed it ~2-fold vs untreated
- S. salivarius MS-oral-D6 and L. paracasei NIZO2936 were top stimulators in initial screen (~2.5-fold and ~2-fold, respectively); S. salivarius strains (MS-oral-D6, MS-ileo-F1, HSISS3) showed dose-dependent stimulation at MOI 50/250 (P values from 0.039 to <0.0001)
- P. gingivalis W83 significantly inhibited re-epithelialization (P=0.037) at high dosage, causing monolayer deterioration
- Lactic acid concentration correlated positively with repair rate (r=0.378, P=0.004) and plateau cell number (r=0.354, P=0.008), but S. salivarius MS-oral-D6 (strongest stimulator) produced negligible lactic/acetic acid — ruling out fermentation acids as its mechanism
- Conditioned medium of MS-oral-D6 retained activity after 7 kDa desalting but lost it after proteinase K treatment; silver-stain SDS-PAGE showed a >180 kDa band unique to MS-oral-D6, identified by LC-MS/MS as most consistent with a secreted serine protease (241 kDa predicted, gene present in only 12/37 sequenced S. salivarius genomes — consistent with strain-specific effect); PMSF (serine-protease inhibitor) pretreatment abolished the stimulatory effect

## 5. Limitations and Future Work
- Entirely in-vitro (Ca9-22 cell line only); no animal or human wound-healing data, so clinical relevance to periodontal/gingival therapy is inferential
- Molecular mechanism by which the serine protease accelerates epithelial migration/proliferation was not determined; contribution of other co-identified secreted proteins (peptidoglycan hydrolase, peptidase M26, surface antigen) could not be excluded
- Bacterial dosage (MOI) was capped by acidification of culture medium affecting cell viability at higher doses, limiting direct comparison to very-high-dose lysate studies in the literature
- Single epithelial cell line; authors note the model is applicable to other cell lines but this was not shown in the paper (data not shown)

## 6. Related Work
- benavides-reyes-2025-probiotics-periodontitis-ma: clinical SR/MA of probiotic adjunct effects on gingivitis/periodontitis (PI, BOP, PPD) — this paper supplies mechanistic rationale at the bacterial-effector level
- mendonca-2024-effects-probiotic-therapy-periodontal: umbrella review of probiotic therapy in periodontal/peri-implant treatment — clinical-outcome counterpart to this in-vitro mechanism study
- jeon-2026-probioticcmu-gingivitis-rct: RCT showing oral probiotic tablets improve gingival index/BOP — clinical evidence this paper's mechanism could help explain

## 7. Glossary
- **Re-epithelialization**: the wound-healing phase in which epithelial cells proliferate and migrate to re-cover a denuded wound surface, restoring barrier integrity
- **Scratch assay**: an in-vitro wound-healing model in which a mechanical scratch is introduced into a confluent cell monolayer and closure is tracked over time
- **Modified Gompertz function**: a sigmoidal growth-curve model (originally for bacterial growth) adapted here to fit re-epithelialization kinetics, yielding repair rate (μm), plateau (A), and lag time (λ)
- **MOI (Multiplicity of Infection)**: ratio of bacterial cells to host (epithelial) cells used in an exposure experiment
- **Serine protease**: an enzyme that cleaves peptide bonds using a catalytic serine residue (here, part of a subtilase-family catalytic triad Asp/Ser/His), inhibited by PMSF
- **LC-MS/MS**: liquid chromatography-tandem mass spectrometry, used here for peptide mapping/protein identification from an in-gel trypsin digest
