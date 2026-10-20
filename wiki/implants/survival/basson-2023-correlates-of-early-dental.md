---
title: "Correlates of Early Dental Implant Failure: A Retrospective Study"
authors: Basson Ayelet Aviva, Mann Jonathan, Findler Mordechai, Chodick Gabriel
year: 2023
date: 2023-01-01
doi: 10.11607/jomi.10199
source: basson-2023-correlates-of-early-dental.md
category: implants/survival
evidence_level: retrospective
source_collection: pubmed-text
full_text: false
pmid: "37847831"
source_url: https://pubmed.ncbi.nlm.nih.gov/37847831/
text_path: /Users/oracleneo/llm-wiki/papers/basson-2023-correlates-of-early-dental.txt
text_filename: basson-2023-correlates-of-early-dental.txt
tags: [early-implant-failure, risk-factors, smoking, implant-number, maxilla, PPI, nested-case-control, EMR]
relations:
  - type: reinforces
    target: fan-2024-smoking-early-implant-failure-sr-ma
  - type: reinforces
    target: chrcanovic-2016-factors-influencing-early-dental-implant
  - type: extends
    target: manzano-2016-risk-factors-in-early-implant
---

abstract-only — full text not retrieved

## Three-line Summary

Historical nested case-control study using national electronic medical records (Israel, 2015–2020; 585 individuals with implant failure within 6 months of placement, matched 1:1 to controls, from 29,378 eligible patients) examining patient-level disease, drug, and dental clinical correlates of early implant failure.

The significant correlates were all clinical/dental — number of implants per person (two implants OR 1.53; ≥4 implants OR 3.33; P<.01), maxillary location (OR 1.59, 95% CI 1.2–2.04), and lifetime smoking (OR 1.57, 95% CI 1.09–2.26); Crohn's disease, myocardial infarction, and osteoporosis were only borderline, and most medication exposures did not reach significance.

Clinical implication: implant count, maxillary site, and smoking are the actionable early-failure correlates in this cohort — but the patient-level unit of analysis (585 failing individuals, not implants), the 6-month case window, and abstract-only retrieval limit how directly these ORs transfer to chairside implant-level risk.

## 세줄요약

이스라엘 전자의무기록 기반 역사적 내포 환자대조연구 (2015–2020; 식립 후 6개월 내 임플란트 실패 환자 585명, 대조군 1:1 매칭, 적격 환자 29,378명) — 조기 임플란트 실패의 환자 단위 질환·약물·치과 임상 상관인자 분석.

유의한 상관인자는 모두 치과 임상 인자였다 — 1인당 임플란트 개수 (2개 OR 1.53, 4개 이상 OR 3.33, P<.01), 상악 위치 (OR 1.59, 95% CI 1.2–2.04), 평생 흡연력 (OR 1.57, 95% CI 1.09–2.26); 크론병·심근경색·골다공증은 경계성에 그쳤고 대부분의 약물 노출은 유의하지 않았다.

임상적 의미: 임플란트 개수·상악 부위·흡연이 이 코호트의 실행 가능한 조기 실패 상관인자 — 다만 환자 단위 분석 (실패 임플란트가 아닌 585명), 6개월 사례 정의, 초록만 수집이라는 점이 이 OR들을 임플란트 단위 임상 위험으로 직접 옮기는 데 한계.

## Summary

This historical nested case-control study mined the electronic medical records of Clalit, a large state-mandated Israeli health provider, to test whether patient-level diagnoses, drug purchases, and dental clinical factors correlate with early implant failure. Among 29,378 eligible patients treated 2015–2020, 585 individuals experienced implant extraction within 6 months of placement and were matched 1:1 to controls (mean age 53 years; 51.3% female). Univariate comparisons flagged lifetime smoking (18% vs 11.5%, P=.009), inflammatory bowel disease (1.5% vs 0.02%, P=.059), and proton pump inhibitor purchase within 6 months (40.0% vs 32.5%, P=.028); adjusted multivariate conditional logistic regression left the **clinical** factors significant — number of implants per person (two: OR 1.53; ≥4: OR 3.33; P<.01), maxillary location (OR 1.59, 95% CI 1.2–2.04), and smoking (OR 1.57, 95% CI 1.09–2.26) — while Crohn's disease, myocardial infarction, and osteoporosis stayed borderline. The authors conclude systemic correlates were weaker than dental clinical ones in this population and call for larger patient-level studies of combined effects.

## Key Contributions

- One of the largest patient-level early-failure datasets in the wiki (585 failure cases from a 29,378-patient pool), built on routable national EMR rather than single-clinic charts.
- Adds an **implant-count exposure axis** with a clear dose-response (2 implants OR 1.53 → ≥4 implants OR 3.33, P<.01) — a correlate that anatomy- and protocol-focused cohorts do not report.
- Reproduces the smoking → early-failure signal independently (OR 1.57) at roughly half the pooled SR+MA magnitude (OR 2.59, [[implants/survival/fan-2024-smoking-early-implant-failure-sr-ma]]).
- Provides a **negative/weak** result set for systemic disease and medication exposures (Crohn's, MI, osteoporosis borderline; PPI and IBD significant only in univariate prevalence terms) — useful as a counterweight to smaller positive-signal cohorts.

## Methodology

- **Design**: Historical, nested case-control study from electronic medical records.
- **Setting**: Clalit Health Services (large, state-mandated Israeli health provider), implants placed 2015–2020.
- **n**: 29,378 eligible adult patients → 585 individuals with implant failure (extraction ≤6 months after implantation); controls matched 1:1.
- **Exposures**: demographics; number/location/complicated status of implants; osteoporosis, diabetes, hypertension, IBD, MI; drug purchases — chemotherapy, bisphosphonates, selective serotonin inhibitors, antihypertensives, PPIs, DMARDs, corticosteroids, NSAIDs.
- **Outcome**: Early implant failure, defined as implant extraction up to 6 months after implantation.
- **Statistics**: univariate and adjusted multivariate conditional logistic regression (ORs).

## Results

| Outcome | Result |
|---|---|
| Cases / eligible pool | 585 / 29,378 |
| Case demographics | Mean age 53 [42,62]; 51.3% female, 49.7% male |
| Lifetime smoking | 18% vs 11.5% controls, P = .009; adjusted OR 1.57 (95% CI 1.09–2.26) |
| PPI use within 6 months | 40.0% vs 32.5%, P = .028 (univariate) |
| IBD | 1.5% vs 0.02%, P = .059 (borderline) |
| Number of implants — 2 | OR 1.53 (P < .01) |
| Number of implants — ≥4 | OR 3.33 (P < .01) |
| Implant location — maxilla | OR 1.59 (95% CI 1.2–2.04) |
| Crohn's disease / MI / osteoporosis | Borderline significant correlates |

Only the values above appear in the retrieved abstract (abstract-only — no adjusted model table, covariate list, or medication ORs are available). **Any number not in this table was not present in the source text.**

## Related Papers

- [[implants/survival/fan-2024-smoking-early-implant-failure-sr-ma]] — reinforces (pooled smoking → early failure OR 2.59; this cohort's adjusted OR 1.57 is directionally consistent but smaller)
- [[implants/survival/chrcanovic-2016-factors-influencing-early-dental-implant]] — reinforces (Swedish specialist-clinic patient-level smoking OR 3.27; independent confirmation of the smoking axis, larger effect)
- [[implants/survival/manzano-2016-risk-factors-in-early-implant]] — extends (earlier early-failure risk-factor cohort; Basson adds a national EMR patient-level denominator and an implant-count dose-response)
- [[implants/survival/yari-2023-risk-factors-early-implant-failure]] — complementary multivariable cohort (posterior maxilla OR 2.96, type IV bone, immediate provisional OR 3.42); Basson's maxilla signal (OR 1.59) is weaker and lacks the protocol/anatomy covariates Yari modelled
- [[implants/survival/borba-2017-risk-factors-for-implant-failure]] — earlier risk-factor reference for the same outcome
- [[implants/survival/grigoras-2024-early-implant-failure-a-meta]] — meta-analytic framing of early-failure risk against which this single cohort's effect sizes can be read
- [[drug/systemic-disease/masri-2024-early-implant-failure-antihypertensive-medications]] — same EMR drug-purchase logic (antihypertensives protective); Basson found no significant medication correlate, a useful contrast
- [[overviews/early-implant-failure-risk-prevention-overview]] — synthesis of early-failure risk factors into which this page feeds
