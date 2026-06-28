---
title: "Relationship between Sponsorship and Failure Rate of Dental Implants: A Systematic Approach"
authors: Antoine Popelut, Fabien Valet, Olivier Fromentin, Aurélie Thomas, Philippe Bouchard
year: 2010
doi: 10.1371/journal.pone.0010274
category: [implants]
pdf_path: /Users/oracleneo/llm-wiki/papers/popelut-2010-sponsorship-implant-failure-rate-sr.pdf
pdf_filename: popelut-2010-sponsorship-implant-failure-rate-sr.pdf
source_collection: external
---

## Why Ingested

임플란트 생존율 데이터의 신뢰성을 평가하는 맥락에서, 연구 후원자(industry vs. non-industry)가 결과 보고에 영향을 미치는지 검토하기 위해 수집. 기존 [[wiki/implants/benic-2014-loading-protocols-single-implant-crowns-sr-ma]] 같은 SR/MA가 인용하는 임플란트 생존율 수치가 어느 정도 출판 편향에 노출되어 있는지 파악하는 근거로 활용.

## One-line Summary

Systematic review of 41 implant trials (5 SRs, 1993–2008): industry-sponsored trials reported ~5× lower annual failure rates (OR 0.21) than non-industry-sponsored trials after controlling for publication age.

## 한줄요약

체계적 고찰(41개 임상시험): 업계 후원 임플란트 연구는 비후원 연구 대비 연간 실패율이 약 5배 낮게 보고되어(OR 0.21), 후원 편향(sponsorship bias)이 임플란트 연구 결과에 유의한 영향을 미침.

## 1. Document Information

- **Journal**: PLoS ONE 5(4): e10274
- **Published**: April 21, 2010
- **Study design**: Systematic review with secondary statistical analysis (quasi-Poisson regression)
- **Funding**: University Paris Diderot (non-industry)
- **Conflict of interest**: None declared by authors

## 2. Key Contributions

- First systematic examination of sponsorship bias specifically in dental implant clinical trials
- Demonstrated that industry-associated funding correlates with significantly lower reported annual implant failure rates (OR = 0.21 after multivariate adjustment)
- Showed that 63% of trials did not report funding source, and those trials also had lower failure rates (OR = 0.33) than non-industry trials
- Only 2 of 41 trials disclosed a conflict of interest statement
- Raised implications for tooth preservation decisions driven by apparently high implant success rates

## 3. Methodology and Architecture

**Search strategy**: MEDLINE and Cochrane searched (January 1993 – December 2008) with MeSH terms "Dental Implants" and "Denture, Partial, Fixed" combined with survival/success/complications. Hand searching in 13 dental journals.

**Inclusion**: Systematic reviews reporting ≥5-year mean follow-up implant survival for IS-SC, IS-FPD, or ITS-FPD. Primary articles extracted from included SRs. Excluded: fully edentulous patients, immediate/early-loading, sinus-lift cases.

**Sponsorship classification**:
1. Industry — grant exclusively from implant company
2. Industry-associated — company had role in study design or provided free implants
3. Non-industry — universities, government, foundations
4. Unknown — no sponsorship information

**Quality assessment**: 3 criteria (inclusion/exclusion criteria, blinding, dropout reporting); ≥2 criteria met = low risk of bias.

**Statistical approach**: Failure rate = implant losses / total implant-years. Quasi-Poisson regression (univariate then multivariate) to identify variables associated with failure rate. Interrater kappa = 0.90 for sponsorship coding.

**Sample**: 5 SRs identified → 38 primary articles → 41 analyzable trials (3 articles covered 2 prosthetic designs each).

## 4. Key Results and Benchmarks

| Metric | Value |
|---|---|
| Analyzable trials | 41 (from 5 SRs) |
| Mean annual failure rate (all) | 1.09% (95% CI 0.84–1.42%) |
| Mean annual failure rate, non-industry | 2.73% (95% CI 1.14–6.55%) |
| Funding not reported | 63% of trials (26/41) |
| High risk of bias | 66% of trials (27/41) |
| No statistical advisor | 73% (30/41) |
| Periodontal status not reported | 83% (34/41) |
| COI statement disclosed | 2/41 trials |

**Multivariate quasi-Poisson model** (final variables: publication age + funding source):
- Industry-associated vs. non-industry: OR = 0.21 (95% CI 0.12–0.38)
- Unknown funding vs. non-industry: OR = 0.33 (95% CI 0.21–0.51)
- Annual failure rate increased 1.12× per year of publication age (older studies → higher failure rates, possibly reflecting improvement over time)

**Univariate findings**: Prosthetic design (p = 0.023) and funding source (p = 0.005) were significant predictors; Impact Factor, sample size, quality assessment, and periodontal reporting were not.

## 5. Limitations and Future Work

- Cannot definitively determine causality (genuine product improvements vs. selective reporting)
- Study age confounds: newer industry studies may use better implant designs
- Relatively small sample (41 trials); limited statistical power for subgroup analyses
- Unknown category (63%) is interpretively ambiguous — deliberate non-disclosure vs. journal policy
- Only English-language papers included
- Authors call for mandatory conflict-of-interest and funding disclosure in dental implant journals

## 6. Related Work

- Bekelman et al. (2003) and Als-Nielsen et al. (2003): prior meta-analyses showing pharmaceutical industry sponsorship → pro-industry results
- Five systematic reviews serving as the source database: Pjetursson et al. (2004, 2007), Berglundh et al. (2002), Jung et al. (2008), Aglietta et al. (2009)
- Subsequent discussion in evidence-based dentistry regarding outcome reporting bias in implant literature

## 7. Glossary

- **Annual failure rate (AFR)**: implant losses divided by total implant-years of observation; enables comparison across studies with different follow-up durations
- **Quasi-Poisson regression**: Poisson regression with variance–mean ratio estimated from data (handles overdispersion); appropriate for count outcomes (implant failures)
- **Sponsorship bias**: systematic distortion of study results in favor of the sponsor's product
- **Industry-associated**: sponsor had substantive role in study design, data collection/analysis, or provided materials free of charge
- **Kappa = 0.90**: almost perfect interrater agreement for funding source classification
