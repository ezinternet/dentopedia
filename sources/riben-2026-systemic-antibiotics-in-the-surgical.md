---
title: "Systemic Antibiotics in the Surgical Treatment of Peri-Implantitis: Impact on the Salivary Microbiome"
authors: Riben Grundström C, Lund B, Bostanci N, Silbereisen A, Pennhag A, Koistinen IS, Zha Y, Damdimopoulos A, Belibasakis GN, Hultin M
year: 2026
doi: 10.1111/jcpe.70143
category: [implants/peri-implantitis]
source_collection: pubmed-text
full_text: true
pmid: "42184963"
pmcid: "PMC13371835"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13371835/
text_path: /Users/oracleneo/llm-wiki/papers/riben-2026-systemic-antibiotics-in-the-surgical.txt
text_filename: riben-2026-systemic-antibiotics-in-the-surgical.txt
---

## Why Ingested

외과적 임플란트주위염 치료에서 전신 항생제의 단기 임상 이득과 장기 무이득을 정량화한 [[wiki/implants/peri-implantitis/antonoglou-2025-do-systemic-antibiotics-offer-benefits]]은 항생제의 "효과" 축만 다뤘고, 항생제가 구강 미생물총에 남기는 "생태학적 비용" 축은 비어 있었다. 이 논문은 Antonoglou 2025 SR+MA가 통합한 Riben Grundström 2024 RCT의 하위 코호트(27명)에서 침(saliva) 미생물총을 전장 유전체 시퀀싱(whole genome sequencing, WGS)으로 12개월 추적해, 광범위(amoxicillin) 대 협범위(phenoxymethylpenicillin) 레짐의 교란 크기를 비교한다. EFP S3 지침 [[wiki/implants/peri-implantitis/herrera-2023-prevention-treatment-peri-implant-efp]]이 전신 항생제를 비권고한 근거 중 하나인 "미생물총 교란·내성" 논리에 실측 데이터를 더한다.

## Three-line Summary
Exploratory, blinded, single-centre two-arm analysis (a randomised subset of the NCT02185209 RCT) of 27 patients receiving resective surgery for peri-implantitis plus 7 days of systemic amoxicillin + metronidazole (group A, n = 14) or phenoxymethylpenicillin + metronidazole (group B, n = 13); unstimulated saliva at baseline, 8 d, 14 d, 6 mo and 12 mo analysed by whole genome shotgun sequencing.
Species richness fell significantly at Day 8 versus baseline in both groups, with recovery signs by Day 14 and recovery by 6 months; alpha and beta diversity did not differ between regimens at any timepoint (richness ANOVA q intervention = 0.762), although species-level differences existed (78 species lower and 38 higher in A vs B at Day 8); 12-month treatment success was 83% (A) vs 69% (B), p = 0.645.
The narrow-spectrum penicillin V regimen did not disturb the salivary microbiome less in a measurable community-level way, so the data give no microbiological or clinical basis to prefer one regimen; limitations are small n, no placebo arm and concurrent chlorhexidine rinsing.

## 세줄요약
임플란트주위염 외과수술(resective surgery) + 7일 전신 항생제를 받은 27명(A군 amoxicillin+metronidazole 14명, B군 phenoxymethylpenicillin+metronidazole 13명)의 탐색적·눈가림 단일기관 2군 하위분석(NCT02185209 RCT의 무작위 하위집단); 침을 수술 전·8일·14일·6개월·12개월에 채취해 WGS 분석.
두 군 모두 8일째 종 풍부도(richness)가 기저 대비 유의하게 감소하고 14일째 회복 조짐, 6개월째 회복; 알파·베타 다양성은 어느 시점에서도 군 간 차이 없음(richness ANOVA q intervention = 0.762), 다만 종 수준 차이는 존재(8일째 A군이 B군보다 78종 낮고 38종 높음); 12개월 치료 성공률 A 83% vs B 69%, p = 0.645.
협범위 penicillin V 레짐이 군집 수준에서 침 미생물총 교란을 더 줄인다는 근거는 없어 어느 쪽을 선호할 미생물학적·임상적 근거가 없으며, 한계는 소규모 n·위약군 부재·병용 클로르헥시딘 가글.

## 1. Document Information
- **Journal**: J Clin Periodontol 2026;53(8):1265-1277 (published 2026-05-25)
- **DOI**: 10.1111/jcpe.70143
- **Institution**: Specialist Clinic Kaniken (Public Dental Health Service, Uppsala) and Department of Dental Medicine, Karolinska Institutet, Sweden
- **Registration**: ClinicalTrials.gov NCT02185209; sequence data PRJEB102458

## 2. Key Contributions
- First study to evaluate amoxicillin + metronidazole versus phenoxymethylpenicillin + metronidazole effects on the salivary microbiome after peri-implant surgery using WGS (authors' claim).
- Shows a transient, comparable loss of species richness at Day 8 in both regimens with recovery by 6 months.
- Reports no community-level (alpha/beta diversity) difference between a broad-spectrum and a narrow-spectrum penicillin partner, while flagging species-level differences that may reflect small-sample noise.
- Frames the narrow-spectrum option as worth considering from an antimicrobial-stewardship standpoint without recommending a regimen.

## 3. Methodology and Architecture
- **Design**: Blinded, single-centre, two-armed exploratory study nested in a three-armed placebo-controlled RCT (84 patients in the parent trial); subset of 27 patients from the two antibiotic arms.
- **Intervention**: Group A amoxicillin 500 mg + metronidazole 400 mg three times daily; Group B phenoxymethylpenicillin 800 mg x 2 + metronidazole 400 mg three times daily; both 7 days. Resective surgery with titanium curettes, ultrasound, 3% hydrogen peroxide and saline; pre-operative 1 min CHX rinse and 0.12% CHX rinses twice daily for 14 days post-operatively.
- **n**: 27 patients (A 14, B 13), 40 implants (A 21, B 19); 126 samples collected, 23 patients complete at all five timepoints (115 samples).
- **Sampling**: Unstimulated saliva, minimum 5 mL, before surgery and at 8 days, 14 days, 6 months, 12 months. DNA extracted on bead-beating/ZymoBIOMICS protocol; 150 bp paired-end sequencing on DNBSEQ G400; MetaPhlAn4 profiling; samples under 100 k non-human reads excluded.
- **Statistics**: GLMM (negative binomial) for richness; LMM/ANOVA for Shannon and evenness; Bray-Curtis PCoA with PERMANOVA (99,999 permutations); edgeR differential abundance with Benjamini-Hochberg FDR q < 0.05.
- **Outcomes**: Primary - qualitative and quantitative salivary microbial change over 12 months. Secondary - treatment success at 12 months (PPD <= 5 mm, BOP in <= 1 site, no SOP, no additional bone loss > 0.5).

## 4. Key Results and Benchmarks
- Baseline: age 62.3 years overall (A 59.9, B 64.8; p = 0.499); current smokers 9 (33.3%) - A 7 (50.0%) vs B 2 (15.4%), p = 0.057; type II diabetes 3 (11.1%) - all in A; modified-surface implants A 18 vs B 10 of 28 (surface distribution p = 0.023).
- Sequencing: mean 35.7 million (+/- 8.2 million) counts; 498 species, 194 genera, 16 phyla; Firmicutes and Actinobacteria most abundant.
- Alpha diversity: richness significantly reduced at Day 8 vs baseline in both groups; richness rose by Day 14 vs Day 8 (A q < 0.05; B q > 0.05); recovery evident at 6 months. Richness ANOVA: q time = 0.00002, q time-intervention = 0.557, q intervention = 0.762.
- Beta diversity: composition changed across timepoints (PERMANOVA q = 0.00004) but not between interventions.
- Within-group differential species: 21 species in A and 37 in B across timepoints, 11 shared; mostly early (baseline vs Day 8/14) contrasts.
- Between-group differential species: Day 8 - 78 species lower and 38 higher in A vs B; Day 14 - 80 higher and 50 lower in A vs B. Seven species differed at >= 3 timepoints; Alloprevotella tannerae was lower in A at all timepoints; Streptococcus sp. F0442, Capnocytophaga granulosa, Actinomyces graevenitzii and Lautropia dentalis lower from 8 days to 6 months; Neisseria sicca and Actinomyces SGB17154 higher up to 6 months.
- Evenness: more marked decrease in group A at Day 14 (authors suggest more dominance in A and a more resilient community in B).
- Serratia liquefaciens appeared in high proportion in four patients (A n = 1 at Day 8; B n = 2 at Day 8, n = 1 at Day 14), interpreted as possible contamination, transient passage or a genuine signal.
- 12-month treatment success: A 10 (83%) vs B 9 (69%); total 19 (76%) of 25; p = 0.645.
- Attrition: one A patient lost by Day 8; in B one patient died by 6 months and another missed the 6- and 12-month samples.

## 5. Limitations and Future Work
- Small sample size; post hoc subset selection from a larger trial, with imbalances in smoking (A 50.0% vs B 15.4%) and implant surface.
- No placebo/no-antibiotic comparator, so the antibiotic effect cannot be separated from surgery and chlorhexidine (CHX) rinses; CHX may itself reduce alpha diversity.
- Saliva reflects peri-implant site-specific pathogens only imperfectly; site-level sampling was not done and health-versus-disease richness was not evaluated.
- Species-level differences may be technical or individual rather than antibiotic effects; WGS also detects non-viable DNA and contaminants.
- Descriptive study; no antibiotic resistance gene (resistome) analysis - authors call for long-term salivary resistome work.

## 6. Related Work
- Antonoglou 2025 SR+MA: parent RCT (Riben Grundström 2024) was one of its included trials; supplies the clinical-benefit axis that this paper complements with an ecological-cost axis.
- Herrera 2023 EFP S3 guideline: non-recommendation of systemic antibiotics, with metronidazole as a single adjunct supported only for specific peri-implant cases.
- Belstrom 2018 and Yamanaka 2012 (cited by authors): salivary versus subgingival/supragingival microbiota response to periodontal therapy.
- Bartsch 2025 (cited by authors): 0.2% CHX twice daily for 4 weeks after periodontal surgery decreased alpha diversity and raised tetracycline resistance genes.

## 7. Glossary
- **WGS (whole genome shotgun sequencing)**: sequencing all DNA in a sample, allowing species-level and functional profiling.
- **Alpha diversity**: within-sample diversity (richness, evenness, Shannon index).
- **Beta diversity**: between-sample compositional dissimilarity (Bray-Curtis, tested by PERMANOVA).
- **Phenoxymethylpenicillin (penicillin V)**: narrow-spectrum penicillin acting mainly on Gram-positive bacteria.
- **Resistome**: the collection of antibiotic resistance genes in a microbial community.
