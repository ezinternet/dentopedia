---
title: "Comparative efficacy of electric toothbrush technologies in plaque and gingivitis reduction: a network meta-analysis"
authors: Chenchen Luo et al.
year: 2026
doi: 10.1007/s00784-026-06955-z
category: [periodontics]
source_collection: pubmed-text
full_text: true
pmid: "42234020"
pmcid: "PMC13233912"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13233912/
text_path: /Users/oracleneo/llm-wiki/papers/luo-2026-electric-toothbrush-technologies-plaque-gingivitis-nma.txt
text_filename: luo-2026-electric-toothbrush-technologies-plaque-gingivitis-nma.txt
---

## Why Ingested

Prior pairwise reviews established only "electric > manual" for plaque control; they could not rank among electric subtypes. This 2026 frequentist NMA (19 RCTs) is the first to produce a SUCRA hierarchy — oscillating-rotating > sonic > ultrasonic > other electric > manual — for both plaque and gingivitis, converting the patient/clinician question from "whether electric" to "which electric." It extends the plaque-biofilm management literature in [[periodontics/jo-2008-management-of-dental-biofilm-through]] (professional care improving patient plaque-control ability) by quantifying the home-care tool axis, and provides a mechanical-disruption complement to the matrix biology in [[oral-microbiology/jakubovics-2021-dental-plaque-biofilm-matrix]].

## One-line Summary

Frequentist network meta-analysis (19 RCTs, 1996–2025) ranking electric toothbrush technologies: oscillating-rotating ranks first for both plaque (SUCRA 89.2%) and gingivitis (86.5%), followed by sonic > ultrasonic > other electric > manual; all electric types beat manual, with largest benefits in orthodontic patients and children and a non-significant effect in the elderly.

## 한줄요약

빈도주의 네트워크 메타분석 (19개 RCT, 1996–2025): 전동칫솔 기술 순위 — 진동회전형(oscillating-rotating)이 치면세균막(SUCRA 89.2%)·치은염(86.5%) 모두 1위, 이어 음파(sonic) > 초음파(ultrasonic) > 기타 전동 > 수동 순. 모든 전동칫솔이 수동보다 우수하며 교정 환자·소아에서 효과 최대, 노인에서는 유의하지 않음.

## 1. Document Information

- **Title**: Comparative efficacy of electric toothbrush technologies in plaque and gingivitis reduction: a network meta-analysis
- **First author**: Chenchen Luo (Southwest Medical University, China)
- **Journal**: Clinical Oral Investigations (2026)
- **DOI**: [10.1007/s00784-026-06955-z](https://doi.org/10.1007/s00784-026-06955-z) · PMID 42234020 · PMCID PMC13233912
- **Registration**: PROSPERO CRD420251273484
- **Study type**: Systematic review + frequentist network meta-analysis (PRISMA-NMA)
- **Source**: PubMed Central open-access full text (pubmed-text artifact)

## 2. Key Contributions

- First NMA to produce a **direct quantitative ranking among electric toothbrush subtypes** (oscillating-rotating, sonic, ultrasonic, other electric), not merely electric-vs-manual.
- Integrates direct head-to-head electric-vs-electric evidence with indirect evidence via the manual common comparator in a connected 5-node network.
- Stratified NMA (short-term single-use vs longer-term home-use) confirms ranking robustness.
- Translates SMDs into absolute, clinically interpretable effects (RMNPI / MGI).

## 3. Methodology and Architecture

- **Search**: PubMed, Embase, Cochrane CENTRAL, Web of Science, ClinicalTrials.gov; inception → June 2025; English.
- **PICOS**: children/adults (permanent or mixed dentition); electric (O-R / sonic / ultrasonic / other); vs manual; outcomes = validated Plaque Index (PI) and/or Gingivitis Index (GI); RCTs (parallel + crossover).
- **Index hierarchy**: author-designated primary → RMNPI (plaque) / MGI (gingivitis) → whole-mouth over site-specific.
- **RoB**: Cochrane RoB 2.0 (5 domains).
- **Analysis**: frequentist random-effects NMA in R 4.5.0 (netmeta); SMD with 95% CI; longest follow-up per study; node-splitting for global/local inconsistency; SUCRA ranking.
- **Nodes**: Manual, Oscillating-Rotating (O-R), Sonic (S), Ultrasonic (U), Other Electric (OE).
- **Prespecified**: subgroups (children/adults/elderly, orthodontic, follow-up); stratified NMA by duration; transitivity check via effect modifiers (baseline plaque, supervision, follow-up).
- **Publication bias**: comparison-adjusted funnel plots, Egger's regression (O-R vs manual), p-curve, precision-weighted regression, sensitivity excluding <50 studies (power limited, k<10 most comparisons).

## 4. Key Results and Benchmarks

- **Included**: 1,852 records → 124 full text → **19 RCTs** (1996–2025); sample sizes 23–150. RoB: 12 low, 5 some concerns, 2 high.
- **Plaque SUCRA**: O-R **89.2%** > Sonic 72.4% > Ultrasonic 54.1% > Other Electric 45.3% > Manual 18.3%.
  - O-R vs manual SMD **-1.24** (95% CI -1.56 to -0.92); sonic vs manual SMD -0.87 (-1.15 to -0.59).
  - Absolute (RMNPI 0–1): O-R vs manual difference **-0.18** (95% CI -0.24 to -0.12) ≈ 18% greater plaque reduction.
- **Gingivitis SUCRA**: O-R **86.5%** > Sonic 70.1% > Ultrasonic 52.8% > Other Electric 43.9% > Manual 16.7%.
  - Absolute (MGI 0–4): O-R vs manual difference **-0.32** (95% CI -0.45 to -0.19).
  - Overall electric vs manual gingivitis: SMD **0.82** (95% CI 0.65 to 0.98, p<0.001).
- **Stratified**: short-term single-use (k=7) O-R SUCRA 91.5%, O-R vs manual SMD -1.52 (-1.98 to -1.06); longer-term home-use (k=12) O-R SUCRA 86.7%, SMD -0.96 (-1.35 to -0.57). Ranking consistent across strata.
- **Subgroups**: largest effects in **orthodontic patients and children**; **elderly subgroup non-significant**; adult gingivitis subgroup CI crosses null (NS).
- **Direct electric-vs-electric**: only 2 O-R-vs-sonic RCTs (Van der Weijden 1996; Erbe 2019); Erbe 2019 O-R-with-ortho-head superior to sonic (p=0.017).
- **Publication bias**: no significant evidence; p-curve right-skewed (χ²=43.0, p=0.03); sensitivity excluding <50 → max ΔSUCRA 3.2%.
- **Mechanism**: O-R 3D oscillation+rotation → focused shear forces disrupting biofilm on concave surfaces / fissures / gingival margin; sonic (lateral sweep) and ultrasonic (microstreaming) less efficient on firmly adherent plaque.

## 5. Limitations and Future Work

- "Other electric" rests on only **k=2** small studies; NS vs manual in the longer-term stratum — interpret SUCRA with extreme caution.
- Only **2 direct O-R-vs-sonic RCTs** → imprecise electric-vs-electric estimates; ranking is **provisional**.
- SUCRA = probability of top rank, NOT magnitude of clinical benefit.
- Clinical heterogeneity (populations, varied indices, follow-up 4 weeks–12 months); no standardized core outcome set; no meta-regression on follow-up length.
- Publication-bias tests underpowered (k<10).
- **Industry sponsorship**: majority of trials funded by electric toothbrush manufacturers (potential bias favoring sponsor product).
- Future: standardized core outcomes; long-term real-world adherence/cost-effectiveness; AI-feedback brushes; special-needs/elderly-targeted designs.

## 6. Related Work

- Pairwise predecessors (Yaacob 2014; Elkerbout 2020; de Jager 2017): electric > manual but no inter-electric ranking — this NMA extends them.
- [[periodontics/jo-2008-management-of-dental-biofilm-through]] — professional care raising patient plaque-control capability (home-care tool axis complement).
- [[oral-microbiology/jakubovics-2021-dental-plaque-biofilm-matrix]] — biofilm matrix biology underlying the mechanical-disruption rationale.

## 7. Glossary

- **NMA (Network Meta-Analysis)**: synthesis combining direct + indirect evidence to rank multiple interventions in one framework.
- **SUCRA (Surface Under the Cumulative Ranking)**: 0–100% summary of an intervention's probability of being the best; higher = more likely optimal.
- **SMD (Standardized Mean Difference)**: effect measure standardizing across studies using different indices.
- **O-R (Oscillating-Rotating)**: powered brush head moving by simultaneous oscillation + rotation (3D action).
- **RMNPI (Rustogi Modified Navy Plaque Index)**: 0–1 plaque index, the most commonly reported plaque metric here.
- **MGI (Modified Gingival Index)**: 0–4 gingival inflammation index, the prioritized gingivitis metric.
- **Transitivity**: NMA assumption that studies across comparisons are similar enough for valid indirect comparison.
