---
title: "Clinical Success Rates of Dental Implants with Bone Grafting in a Large-Scale National Dataset"
authors: Findler M, Doron H, Mann J, Chackartchi T, Tobias G, Taba M Jr, Kasaj A, Park CH
year: 2026
date: 2026-01-15
doi: 10.3390/jfb17010046
source: findler-2026-clinical-success-rates-of-dental.md
category: [immediate-implant]
evidence_level: retrospective
source_collection: pubmed-text
full_text: true
pmid: "41590814"
pmcid: "PMC12843187"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12843187/
text_path: /Users/oracleneo/llm-wiki/papers/findler-2026-clinical-success-rates-of-dental.txt
text_filename: findler-2026-clinical-success-rates-of-dental.txt
tags: [immediate-implant, bone-grafting, success-rate, risk-factors, national-cohort, socioeconomic-status, timing]
relations:
  - type: reinforces
    target: lang-2012-immediate-implant-survival-success-sr
  - type: refines
    target: tonetti-2017-immediate-vs-delayed-implant-timing-rct
---

## Three-line Summary

Retrospective cohort of 158,824 implants (53,874 patients, 2014–2022) from a nationwide Israeli dental network, 45,715 placed with simultaneous bone augmentation; GEE adjusted for within-patient clustering.

Augmented implants achieved 97.83% success (2.17% failure), comparable to the general implant population, but immediate placement was an independent risk indicator — 3.08% vs 2.07% failure (OR 1.487, p<0.000) — and 70% of failures occurred within the first year.

Supports the stabilization hypothesis (augmentation is not inherently detrimental) while flagging timing, male sex, maxillary location, and low SES as risk dimensions for personalized IIP case selection; administrative-coding design limits granular confounding control.

## 세줄요약

이스라엘 전국 치과 네트워크 후향적 코호트(임플란트 158,824개, 환자 53,874명, 2014–2022) — 동시 골이식 45,715개; GEE로 환자 내 상관 보정.

골이식 임플란트 성공률 97.83%(실패 2.17%)로 전체 집단과 유사하나, 즉시식립은 독립 위험인자(실패 3.08% vs 2.07%, OR 1.487, p<0.000); 실패 70%가 1년 이내 발생.

골이식 자체는 해롭지 않다는 "안정화 가설"을 지지하면서도 시기·남성·상악·낮은 사회경제적 지위를 즉시식립 증례선택의 위험 차원으로 제시; 행정 코딩 설계상 세부 교란 통제는 제한적.

## Summary

Large-scale real-world evidence on implants placed with **simultaneous bone augmentation** (DBGIs) from Maccabi Dent, a nationwide Israeli dental service. The study tests two hypotheses: augmentation does not raise failure relative to the general implant population, and failure risk is modulated by timing, anatomy, restoration type, and demographics — especially socioeconomic status (SES).

For the immediate-implant wiki, the load-bearing finding is that **immediate placement is an independent failure risk indicator** even within augmented sites (3.08% vs 2.07% for early/delayed, OR 1.487), with failures concentrated early (≤1 year). This is population-scale, hypothesis-consistent support for IIP being technique-sensitive.

> [!note] Evidence scope
> Retrospective administrative registry; no granular smoking/periodontitis/graft-material data. Absolute failure rates are low (~2%), so the IIP risk signal is a relative one.

## Key Contributions

- Population-scale success estimate for augmented implants: 97.83% (994 failures / 45,715).
- Immediate placement as an independent failure risk indicator after adjustment (OR 1.487, p<0.000).
- Temporal failure concentration: ~70% within the first year in both augmented and general cohorts.
- SES gradient (3.07% low vs 2.06% high) independent of clinical covariates.
- Explicit stabilization-vs-complexity hypothesis test favoring augmentation safety.

## Methodology

- Registry: all implant placements 2014-01-01 → 2022-12-31 with linked graft/prosthetic codes; IRB-approved, de-identified.
- DBGI = graft code on same day/site as placement (socket grafting, GBR, ridge expansion, block grafts, sinus elevation).
- Immediate = same date/site as extraction; all others early/delayed.
- Failure = removal or documented failure; early ≤1 y, late >1 y; pre/post restoration.
- Multivariable GEE (binary logistic, exchangeable correlation, robust SE): sex, SES, timing, six jaw zones, restoration type, grafting; OR + 95% CI; listwise exclusion, no imputation.

## Results

- 158,824 implants / 53,874 patients; mean age 55.54 ± 11.93 (18–88).
- Augmented: 45,715 implants / 17,600 patients; 11.4% (4,682) immediate, 88.6% (41,033) early/delayed.
- Augmented success 97.83%; immediate augmented failure 3.08% vs early/delayed 2.07% (p<0.001; OR 1.487, p<0.000).
- 696/994 augmented failures (70%) early; 324 (32.6%) post-restoration. All-implant: 3,507 failures, 2,476 (70%) early.
- Placement→failure 13.77 ± 17.31 mo; restoration at 6.19 ± 3.57 mo; loading→failure 22.9 ± 21.81 mo.
- Maxillary molar 3.36%, maxillary incisor 3.09% failure vs mandibular 1.61–1.69%; maxillary premolar 2.16% vs mandibular 1.16% (p<0.0056).
- Male 2.5% vs female 1.9% (p=0.0002); low SES 3.07% vs high 2.06%; removable overdenture 2.18% vs fixed crown 0.80% post-loading failure.

## Limitations

- Retrospective administrative coding; missing smoking, periodontitis, graft-material detail.
- Heterogeneous augmentation procedures prevented dedicated horizontal-augmentation subgroup analysis.
- Binary failure definition misses retained implants with marginal bone loss (underestimates peri-implantitis).
- Variable follow-up; no cohort-wide 10-year Kaplan–Meier.

## Related Papers

- [[immediate-implant/lang-2012-immediate-implant-survival-success-sr]] — high-survival bottom line confirmed at population scale.
- [[immediate-implant/tonetti-2017-immediate-vs-delayed-implant-timing-rct]] — immediate-vs-delayed timing comparison qualified by registry data.
- [[immediate-implant/liu-2025-iip-iipp-classification-surgical-restorative]] — case-selection framework that could absorb these risk modifiers.
- [[immediate-implant]] — general placement-timing category (ITI Type 1–4 classification referenced here).
