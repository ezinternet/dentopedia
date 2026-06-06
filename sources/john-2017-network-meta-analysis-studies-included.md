---
title: "Network Meta-Analysis of Studies Included in the Clinical Practice Guideline on the Nonsurgical Treatment of Chronic Periodontitis"
authors: Mike T. John, Bryan S. Michalowicz, Georgios A. Kotsakis, Haitao Chu
year: 2017
doi: 10.1111/jcpe.12726
category: [periodontics]
pdf_path: /Users/oracleneo/llm-wiki/papers/john-2017-network-meta-analysis-studies-included.pdf
pdf_filename: john-2017-network-meta-analysis-studies-included.pdf
source_collection: external
---

## Why Ingested

기존 [[periodontics/smiley-2015-nonsurgical-periodontitis-srp-guideline]] ADA 가이드라인이 SRP 보조요법들을 서로 직접 비교하지 않은 공백을, 동일한 1차 연구를 사용한 네트워크 메타분석으로 보강·확장한다. 또한 [[evidence-appraisal/shin-wj-2015-systematic-review-meta-analysis-introduction]]의 NMA·SUCRA·출판편향 방법론을 실제 치주 임상 질문에 적용한 사례로 근거평가 측면에서도 유용하다.

## One-line Summary

Star-shaped network meta-analysis (61 RCTs, 74 comparisons, 9 adjuncts) found no adjunct to SRP statistically superior to another for CAL gain; all adjuncts add ~0.3-0.35 mm CAL over 6-12 months vs SRP alone, with publication bias inflating effects by ~20%.

## 한줄요약

별형 네트워크 메타분석(RCT 61편, 74개 비교, 보조요법 9종): SRP 단독 대비 어떤 보조요법도 임상부착수준(CAL) 이득에서 다른 보조요법보다 통계적으로 우월하지 않았고, 모든 보조요법은 6-12개월간 약 0.3-0.35 mm의 CAL 이득만 추가했으며 출판편향이 효과를 약 20% 부풀렸다.

## 1. Document Information

- Title: Network Meta-Analysis of Studies Included in the Clinical Practice Guideline on the Nonsurgical Treatment of Chronic Periodontitis
- Authors: Mike T. John (University of Minnesota), Bryan S. Michalowicz, Georgios A. Kotsakis (University of Washington), Haitao Chu (UMN Biostatistics)
- Journal: Journal of Clinical Periodontology, 2017;44(6):603-611
- DOI: 10.1111/jcpe.12726 (HHS Public Access author manuscript; PMC 2018-06-02)
- Type: Network meta-analysis (NMA) of RCTs
- Conflicts/funding: None declared.

## 2. Key Contributions

- First network meta-analysis to directly compare the SRP adjuncts that the 2015 ADA Clinical Practice Guideline (Smiley et al.) evaluated only against SRP alone, never head-to-head.
- Uses the Guideline's own curated RCT library, making the NMA results explicitly complementary to (not a re-search of) the Guideline.
- Provides comparative-efficacy ranking (probability of ranking first/second; SUCRA) across nine adjuncts.
- Quantifies and corrects for publication bias using a contour-enhanced funnel plot.
- Frames the clinical bottom line around patient relevance: CAL is a clinician-measured physical outcome, not a patient-reported one.

## 3. Methodology and Architecture

- Design: Star-shaped (common-comparator) frequentist NMA; each adjunct connected only through SRP-alone, yielding 9×8/2 = 36 indirect comparisons.
- Primary outcome: change in clinical attachment level (CAL) at ≥6 months after randomization.
- Inclusion: RCTs published 1960-July 2014, English, reporting CAL change ≥6 mo; parallel-arm and split-mouth allowed; aggressive periodontitis excluded; experimental/non-US/OTC adjuncts and adjuncts applied >1 week after SRP excluded.
- Sample: from 72 Guideline studies, excluded 11 SRP-vs-untreated-control trials → 61 RCTs with 74 SRP+adjunct vs SRP-alone pairwise comparisons.
- Nine adjuncts: sub-antimicrobial dose doxycycline (SDD, host modulation); systemic antimicrobials (ANTI); chlorhexidine chips (CHX); doxycycline hyclate gel (DH); minocycline microspheres (MM); photodynamic therapy with diode laser (PDT); diode laser non-PDT (DL); Nd:YAG laser (NDL); erbium laser (ERL).
- Progressive grouping strategy (5 schemes): 9 clinical groups → 4 mechanism groups → 3 broader groups → 2 groups (antimicrobials/host-modulators vs lasers) → all-combined non-specific adjunct effect.
- Statistics: frequentist NMA (White 2011; Lu & Ades; Salanti); parametric bootstrap 50,000 reps for parameter uncertainty; cumulative ranking bar chart; SUCRA (0-1, higher = better). Heterogeneity via I² (Cochrane thresholds). Publication bias via contour-enhanced funnel plot.

## 4. Key Results and Benchmarks

- No adjunct was statistically significantly superior to any other; all 36 pairwise differences had wide confidence intervals.
- Highest ranking probabilities: local doxycycline hyclate gel (DH) ranked first, photodynamic therapy with diode laser (PDT) ranked second.
- Overall, adjuncts improved CAL gain by roughly a third of a millimeter (~0.3-0.35 mm) over 6-12 months vs SRP alone.
- NMA treatment effects closely matched the original Guideline meta-analysis effects (as expected, differing mainly in variance estimators).
- Publication bias was evident — fewer-than-expected small-effect studies; their absence inflated the observed treatment effects by an estimated ~20%.

## 5. Limitations and Future Work

- Star-shaped network: all comparisons are indirect (through SRP), so no direct head-to-head loops to check consistency.
- CAL is a clinician-measured surrogate; patient-perceived benefit of a ~0.3 mm gain is unclear — calls for patient-reported outcomes.
- Confined to the Guideline's primary studies by design; other trials not included.
- Documented publication bias limits confidence in absolute effect magnitudes.
- Heterogeneity expected from variation in baseline disease severity, three decades of studies, and 20 countries across 5 continents.

## 6. Related Work

- Smiley et al. 2015a/2015b — the ADA Evidence-Based Clinical Practice Guideline whose RCT library underlies this NMA.
- Methodologic NMA references: White 2011a/b; Lu & Ades 2004; Salanti et al. 2008/2011 (SUCRA); White et al. 2012 (bootstrap); Palmer et al. 2008 (contour-enhanced funnel plot); Leucht et al. 2016 (NMA as highest evidence level).

## 7. Glossary

- SRP: scaling and root planing, the standard nonsurgical periodontal therapy.
- CAL: clinical attachment level; change in CAL is the primary periodontal efficacy outcome here.
- Adjunct: an additional nonsurgical treatment given with SRP (systemic/local antimicrobials, host modulation, lasers).
- NMA (network meta-analysis): meta-analytic method comparing >2 treatments simultaneously, including indirect comparisons.
- Star-shaped NMA: network where all interventions connect only through one common comparator (here SRP alone).
- SUCRA: Surface Under the Cumulative RAnking curve; 0-1 summary of how well a treatment ranks.
- SDD: sub-antimicrobial dose doxycycline (host-modulating agent).
- PDT: photodynamic therapy (here with a diode laser).
- Contour-enhanced funnel plot: funnel plot overlaid with significance contours to distinguish publication bias from other asymmetry.