---
title: "A network meta-analysis of interproximal oral hygiene methods in the reduction of clinical indices of inflammation"
authors: Kotsakis GA, Lian Q, Ioannou AL, Michalowicz BS, John MT, Chu H.
year: 2018
doi: 10.1002/JPER.17-0368
category: [interdental-cleaning]
source_collection: pubmed-text
full_text: true
pmid: "29520910"
pmcid: "PMC5984142"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC5984142/
text_path: /Users/oracleneo/llm-wiki/papers/kotsakis-2018-network-meta-analysis-interproximal.txt
text_filename: kotsakis-2018-network-meta-analysis-interproximal.txt
---

## Why Ingested

Found while mining the reference list of Wen et al. 2026 ("The effect of dental floss sequence on plaque removal efficacy and periodontal health," an RCT on pre-/mid-/post-brushing flossing sequence). Kotsakis 2018 is the seminal Bayesian network meta-analysis (22 RCTs, 10 interdental oral hygiene aids) that first quantitatively ranked interdental brushes and water-jets above floss and toothpicks for reducing gingival inflammation, and it underpins the "floss is not the universal gold standard — device choice should be individualized" thesis that recurs across the wiki's later interdental-cleaning literature (e.g. [[interdental-cleaning/mancinelli-lyle-2024-water-flosser-vs-interdental-brush-rct]], [[interdental-cleaning/badahdah-2025-dental-water-jet-plaque-gingivitis-sr]], [[interdental-cleaning/jung-2025-flossing-performance-plaque-removal]]). It is directly cited/echoed by [[overviews/interdental-cleaning-devices-synthesis]] and provides the earliest network-level evidence base (pre-2015 search) against which those newer head-to-head trials and reviews can be benchmarked.

## Three-line Summary

Bayesian network meta-analysis (BNMA) of 22 RCTs covering 10 interdental oral hygiene (IOH) aids used as toothbrushing adjuncts, comparing plaque, gingival inflammation (GI/BOP), and probing depth reduction.

Interdental brushes (IB) ranked best for gingival index reduction (0.23 [95% CI 0.09-0.37], 64.7% probability of being best) and plaque index, followed by water-jet (WJ, 0.19 [95% CI 0.14-0.24]); unsupervised flossing and toothpicks ranked lowest, with near-zero probability of being the "best" aid.

Clinical implication: no single IOH aid is a universal gold standard — interdental brushes and water-jets are supported as effective alternatives/first-line options over unsupervised flossing, but ranking varied by outcome and most included trials had unclear risk of bias and heterogeneous populations (periodontal status often unreported).

## 세줄요약

22편 RCT, 10종 치간 구강위생(IOH) 보조기구를 대상으로 한 베이지안 네트워크 메타분석(BNMA) — 칫솔질 보조수단으로서 치태·치은염증(GI/BOP)·치주낭깊이 감소 비교.

치간칫솔(IB)이 치은지수 감소에서 최고 순위(0.23 [95% CI 0.09-0.37], 최선일 확률 64.7%)이자 치태지수도 최고, 그다음이 물세정기(WJ, 0.19 [95% CI 0.14-0.24]); 비지도 치실질과 이쑤시개는 최하위(최선일 확률 거의 0).

임상적 의미: 단일 IOH 도구가 보편적 금표준은 아니며 치간칫솔·물세정기가 비지도 치실질보다 우선 고려될 근거가 있으나, 지표별 순위가 달랐고 포함 연구 대부분이 편향위험 불명확·인구집단 이질적(치주 상태 미보고 다수)이라는 한계가 있음.

## 1. Document Information

- **Title**: A Network Meta-analysis of Interproximal Oral Hygiene Methods in the Reduction of Clinical Indices of Inflammation
- **Authors**: Georgios A. Kotsakis, Qinshu Lian, Andreas L. Ioannou, Bryan S. Michalowicz, Mike T. John, Haitao Chu
- **Journal**: Journal of Periodontology, 2018;89(5):558-570
- **DOI**: [10.1002/JPER.17-0368](https://doi.org/10.1002/JPER.17-0368)
- **PMID**: 29520910 / **PMCID**: PMC5984142
- **Study type**: Systematic review + Bayesian network meta-analysis (NMA) of RCTs

## 2. Key Contributions

- First application of Bayesian network meta-analysis (BNMA) to interdental oral hygiene (IOH) aids, allowing indirect comparisons among 10 intervention groups despite sparse direct head-to-head data (most direct comparisons limited to 1-2 studies).
- Provides a quantitative overall efficacy ranking (posterior "best" probability + SUCRA) across floss, powered floss, toothpicks (± instruction), water-jet, interdental brushes, gum-massaging devices, and powered/manual toothbrush controls.
- Corroborates and quantitatively reinforces the 11th European Workshop in Periodontology consensus statement that flossing cannot be generally recommended over interdental brushes except where interdental space is too tight for a brush.

## 3. Methodology and Architecture

- PICO-driven systematic review (Ovid Medline, EMBASE, Web of Science; 1/1/1980-4/17/2015 + manual search), PRISMA-reported.
- Inclusion: RCTs, IOH performed by physically competent persons, ≥2 weeks follow-up, outcomes = gingival inflammation/plaque/probing depth. Exclusion: non-randomized/uncontrolled studies, <10 patients/arm.
- Dual independent screening and data extraction (G.K., A.I.), third-reviewer adjudication (M.J.); Cohen's kappa for agreement (0.85 title/abstract, 0.80 full-text).
- Cochrane Handbook risk-of-bias assessment across 5 domains.
- Statistics: random-effects arm-based (AB) Bayesian NMA per outcome; non-informative priors for fixed effects, weakly informative priors for covariance; JAGS/rjags in R; MCMC Gibbs sampling (4 chains x 100,000 samples, 50,000 burn-in); convergence via trace plots + Gelman-Rubin statistic. Ranking via posterior "probability of being best" and SUCRA.

## 4. Key Results and Benchmarks

- 615 records screened → 71 full-text assessed → 49 excluded → **22 RCTs** (18 distinct interventions/combinations) included, grouped into **10 IOH categories**.
- Risk of bias: 4 studies low risk, 1 high risk, remainder unclear. 9/22 (40.9%) industry-funded.
- **BOP reduction vs control**: toothpick + intensive OH instruction (TO) best (26.4% [95% CI 7.50-45.4], 70.4% probability best), water-jet (WJ) second (19.3% [95% CI 16.2-22.4], 12.6%); floss (FL) and powered floss (FL2) significant but small effect (FL 5.1-10.3%, FL2 2.0-11.2%).
- **GI reduction**: interdental brushes (IB) best (mean 0.23 [95% CI 0.09-0.37], 64.7% probability best), WJ second (mean 0.19 [95% CI 0.14-0.24], 27.4%).
- **PI reduction**: IB best (mean 0.34 [95% CI 0.12-0.56]; SUCRA 95.5%), followed by powered-control+water-jet (PW).
- **PD reduction**: IB ranked #1 (data sparse: only 3 pairwise comparisons, 2 direct + 1 indirect).
- Only 6/21 active-vs-active comparisons were statistically significant for BOP — most head-to-head differences among active aids were not significant.

## 5. Limitations and Future Work

- NMA models could only assess each outcome (GI, BOP, PI, PD) asynchronously/separately — no joint multi-outcome model, so rankings differ by outcome and cannot be reconciled into one aid.
- Small numbers of studies per intervention arm; substantial population and instruction-method heterogeneity.
- Periodontal status of participants (pristine vs reduced periodontium) largely unreported, precluding subgroup conclusions — cited Christou et al. finding floss gave 50% less plaque reduction than interdental brushes specifically in periodontitis patients (attributed to loss of papillary guidance).
- Gingival inflammation indices are physical/disease-oriented outcomes, not patient-reported outcomes (OHRQoL not captured) — patient-perceived benefit of IOH aids remains unclear.
- Authors call for further well-designed, adequately powered RCTs with joint outcome modeling and patient-reported outcomes.

## 6. Related Work

- 11th European Workshop in Periodontology consensus (cited as concordant): flossing not generally recommended over interdental brushes.
- Christou et al. (cited): floss vs interdental brush plaque reduction differential in periodontitis patients.
- Superseded/extended in the wiki by later head-to-head RCTs and reviews: [[interdental-cleaning/mancinelli-lyle-2024-water-flosser-vs-interdental-brush-rct]], [[interdental-cleaning/badahdah-2025-dental-water-jet-plaque-gingivitis-sr]], [[interdental-cleaning/mohapatra-2024-water-flosser-vs-floss-plaque-sr]], [[interdental-cleaning/jung-2025-flossing-performance-plaque-removal]].

## 7. Glossary

- **BNMA (Bayesian Network Meta-Analysis)**: statistical method combining direct and indirect treatment comparisons across a network of trials using a Bayesian framework (MCMC sampling).
- **SUCRA**: Surface Under the Cumulative RAnking curve — summarizes an intervention's overall rank across a distribution (1 = best, 0 = worst).
- **GI (Gingival Index)**: clinical index scoring gingival inflammation severity.
- **BOP (Bleeding on Probing)**: percentage of sites bleeding after periodontal probing, marker of gingival inflammation.
- **IOH (Interproximal/Interdental Oral Hygiene)**: hygiene aids/techniques targeting the interdental (between-teeth) space — floss, interdental brushes, water-jet/oral irrigators, toothpicks, etc.
- **AB (arm-based) NMA model**: NMA model formulation using each trial arm's absolute outcome rather than only relative (contrast-based) treatment effects, enabling inclusion of single-arm data in the network.
