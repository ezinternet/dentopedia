---
title: "Removable partial dentures and mortality among partially edentulous adults"
authors: Nasir Zeeshan Bashir, Eduardo Bernabé
year: 2022
doi: 10.1016/j.jdent.2022.104304
category: [removable-partial-denture]
source_collection: pubmed-text
full_text: false
pmid: "36152952"
source_url: https://pubmed.ncbi.nlm.nih.gov/36152952/
text_path: /Users/oracleneo/llm-wiki/papers/bashir-2022-rpd-mortality-partially-edentulous.txt
text_filename: bashir-2022-rpd-mortality-partially-edentulous.txt
---

abstract-only — full text not retrieved

## Why Ingested

선택 결정 축의 **가장 먼 종점**이라 넣었다. 나머지 논문들이 보철 생존([[wiki/removable-partial-denture/drummond-2024-rpd-long-term-periodontal-health-sr-ma]])·치주([[wiki/removable-partial-denture/gotfredsen-2021-removable-partial-prosthesis-periodontitis-sr]])·삶의 질([[wiki/removable-partial-denture/choong-2022-ohrqol-after-rpd-rehabilitation-sr-ma]])에서 멈추는 데 반해, 이 코호트는 **전체 사망률**까지 간다. 결과가 놀랍고(중앙 생존기간 3.1년 차이) 바로 그래서 위험하다 — 인과로 오독되기 쉬운 관찰연구이므로, 위키가 이 논문을 *들고 있으면서 동시에 인과 주장을 막는* 형태로 보유해야 한다. 저자들 스스로 검증이 더 필요하다고 닫는다.

## Three-line Summary

Cohort analysis of NHANES III (US national survey, clinical dental examination) linked to public-use mortality files through 2019, restricted to partially edentulous adults with fewer than 20 teeth, propensity-score weighted to balance 27 covariates spanning sociodemographics, health behaviours, insurance, laboratory markers and general health status.

Across 1,246 participants and 22,557 person-years, RPD wearers showed an all-cause mortality rate difference of −6.5 (95% CI −11.6 to −1.4), a median survival time 3.1 years longer (20.3 vs 17.2 years), an event time ratio of 1.26 (95% CI 1.17–1.37) corresponding to a 26% increase in survival time, and a number-needed-to-treat of 7.5 for one death prevented over ten years.

The association is large and survives extensive covariate balancing, but this is observational: wearing a partial denture is entangled with care-seeking, dexterity, cognition and social support, and the authors themselves call for validation and for identification of the mediating factors before any causal reading.

## 세줄요약

NHANES III (미국 국민건강영양조사, 임상 구강검진 포함)를 2019년까지의 공개 사망 자료와 연계한 코호트 분석: 잔존치 20개 미만의 부분무치악 성인으로 한정하고, 사회인구·건강행태·보험·검사수치·전반적 건강상태에 걸친 **27개 공변량**을 성향점수 (propensity score) 가중으로 균형화했다.

1,246명·22,557 인년 (person-years) 자료에서 가철성 국소의치 (Removable Partial Denture, RPD) 착용자는 전체 사망률 차이 −6.5 (95% CI −11.6 ~ −1.4), 중앙 생존기간 **3.1년 김** (20.3년 vs 17.2년), 사건시간비 (Event Time Ratio, ETR) 1.26 (95% CI 1.17~1.37, 생존기간 26% 증가), 10년간 **7.5명 치료 시 1명의 사망 예방** (Number Needed to Treat, NNT)을 보였다.

연관성은 크고 광범위한 공변량 균형화에서도 살아남지만 이것은 **관찰연구**다 — 의치 착용은 의료이용 성향·손기술·인지기능·사회적 지지와 얽혀 있고, 저자들 스스로 인과 해석 전에 검증과 매개인자 규명이 필요하다고 닫는다.

## 1. Document Information

- **Journal**: Journal of Dentistry 2022;126:104304
- **DOI**: 10.1016/j.jdent.2022.104304 · **PMID**: 36152952
- **Type**: Cohort study (secondary analysis of NHANES III with mortality linkage), propensity-score weighted
- **Source**: PubMed structured abstract — **abstract-only, full text not retrieved** (no PMC record). The covariate list, propensity model specification, balance diagnostics, sensitivity analyses and any E-value for unmeasured confounding are not recoverable from the abstract.

## 2. Key Contributions

- Extends the RPD outcome literature to **all-cause mortality**, the furthest endpoint in this category.
- Uses **clinical examination** rather than self-report for both exposure (RPD use) and dentition status.
- Applies **propensity-score weighting across 27 covariates**, a stronger confounding-control strategy than the usual regression adjustment.
- Reports both absolute (rate difference, median survival, NNT) and relative (ETR) measures.

## 3. Methodology and Architecture

Data from the Third National Health and Nutrition Examination Survey linked to public-use mortality files through 2019. Inclusion: partially edentulous adults with fewer than 20 teeth. RPD use and dentition status determined by clinical examination. Propensity-score weighting to balance 27 covariates (sociodemographics, health behaviours and insurance, laboratory markers, general health status). Survival analysis computing absolute measures (mortality rate, median survival time) and a relative measure (event time ratio).

## 4. Key Results and Benchmarks

| Measure | Value | 95% CI |
|---|---|---|
| Analysed cohort | 1,246 participants · 22,557 person-years | — |
| All-cause mortality rate difference (wearers − non-wearers) | −6.5 | −11.6 to −1.4 |
| Median survival, RPD wearers | 20.3 years | — |
| Median survival, non-wearers | 17.2 years | — |
| Difference in median survival | **+3.1 years** | — |
| Event time ratio (survival time) | **1.26** (26% increase) | 1.17 to 1.37 |
| NNT for one death prevented at 10 years | **7.5** | — |

## 5. Limitations and Future Work

- **Observational — no causal claim is supported.** RPD use is not randomly assigned; it tracks care-seeking behaviour, manual dexterity, cognition, social support and financial access, all of which independently predict mortality. Propensity weighting balances *measured* covariates only.
- The effect size is implausibly large for a dental prosthesis acting through nutrition alone (NNT 7.5 over ten years would make an RPD comparable to major cardiovascular interventions), which is itself a signal of **residual confounding by indication** rather than a discovery.
- Ingested **abstract-only**: no covariate list, balance diagnostics, sensitivity analyses or E-value for unmeasured confounding.
- NHANES III baseline is 1988–1994; both dentures and background mortality have changed since.
- US population with US insurance structure; transfer to Korean practice is unexamined.
- The authors explicitly state that further research is needed to validate the findings and to identify mediating factors.

**How this page should be used**: as a reason to take a non-functional dentition seriously as a general-health signal, and as an argument against therapeutic nihilism in older partially edentulous patients — **not** as a claim that fitting a denture extends life.

## 6. Related Work

- [[wiki/removable-partial-denture/drummond-2024-rpd-long-term-periodontal-health-sr-ma]] — prosthesis-level and abutment-level outcomes; this paper takes the same exposure to a systemic endpoint.
- [[wiki/removable-partial-denture/campbell-2017-rpd-clinical-need-for-innovation]] — ~40% discontinuation; wearers and non-wearers differ in ways that matter for the present comparison.
- [[wiki/removable-partial-denture/mckenna-2020-functionally-orientated-tooth-replacement-older]] — the older-patient population where this question is most live.

## 7. Glossary

- **NHANES III (미국 국민건강영양조사 3차)**: US national survey combining interview, examination and laboratory data, linkable to national death records.
- **Propensity score weighting (성향점수 가중)**: reweighting a cohort so that measured covariates are balanced between exposed and unexposed, approximating randomisation for *measured* variables only.
- **ETR (사건시간비, Event Time Ratio)**: ratio of survival times between groups; 1.26 means 26% longer.
- **NNT (치료필요수, Number Needed to Treat)**: number of people who must receive the intervention for one additional beneficial outcome.
- **Confounding by indication (적응증에 의한 교란)**: the reason a treatment was given also predicts the outcome, biasing observational comparisons.
