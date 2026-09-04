---
title: "Acquisition of a Digital Intraoral Scanning Device: An Examination of Practice Volume Changes and the Economic Impact via an Interrupted Time Series Analysis"
authors: Michael M Mackay, Mohammad Fallah, Tiffany Danyal
year: 2017
doi: null
category: [practice-management]
pdf_path: /Users/oracleneo/llm-wiki/papers/mackay-2017-acquisition-digital-intraoral-scanning-device.pdf
pdf_filename: mackay-2017-acquisition-digital-intraoral-scanning-device.pdf
source_collection: external
full_text: false
pmid: "29272086"
---

## Why Ingested

위키의 practice-management 카테고리에는 치과 경제학 이론(health economics framework, [[practice-management/listl-2019-what-is-health-economics-oral-health]])과 비용분담·이용률 실증 연구는 있지만, **자본 장비(구강스캐너) 도입이 진료 매출/볼륨에 미치는 경제적 임팩트**를 직접 측정한 연구가 없다 — digital-workflow 클러스터의 IOS 연구는 전부 정확도(accuracy)·정밀도(trueness/precision) 축이지 경제적 성과 축이 아니다. 이 논문은 그 공백을 메우지만, Align Technology의 자체 Invisalign 매출 데이터를 이용한 산업 후원 분석이라는 점을 반드시 병기해야 한다.

## Three-line Summary

Interrupted time series (ITS) analysis of 48 months (24 pre-/24 post-scanner) of Invisalign receipt data from 1,871 GP and orthodontic practices worldwide, examining the impact of iTero intraoral scanner acquisition on Invisalign treatment starts; a subset of 319 North American low-volume GP practices (≤5 receipts in the prior 12 months) was analyzed separately.

Scanner introduction produced a significant abrupt increase in Invisalign receipts for the full sample (b = 0.49; p < 0.001), from a predicted 2.38 to an observed 2.88 in month 25 (+20.71% vs. counterfactual), and a significant abrupt increase for the low-volume North American subset (b = 0.28; p < 0.001) that persisted 24 months post-introduction; projected 12-month gains were +5.92 receipts (full sample) and +3.41 receipts (low-volume subset).

The outcome is Align's own Invisalign receipt data with no non-Invisalign comparator and no cost-side accounting (scanner capital + per-scan cost not netted against gains), and an ITS built on manufacturer-supplied receipt data cannot separate a scanner effect from concurrent marketing or organic practice growth — the finding should be read as association, not an isolated causal scanner effect, and not as net economic benefit.

## 세줄요약

제조사 데이터 기반 단절적 시계열(Interrupted Time Series, ITS) 분석 — 전세계 GP·교정 치과 1,871곳의 48개월(스캐너 도입 전 24개월/후 24개월) Invisalign 매출 데이터, iTero 구강스캐너(Intraoral Scanner) 도입이 Invisalign 치료 시작 건수에 미치는 영향을 측정; 북미 저볼륨 GP 진료소 319곳(직전 12개월 ≤5건) 하위분석 포함.

스캐너 도입 시점(25개월차)에 전체 표본에서 유의한 급격한 매출 증가(b=0.49, p<0.001), 예측값 2.38 대비 실측 2.88로 +20.71%; 북미 저볼륨 GP 하위군에서도 유의한 증가(b=0.28, p<0.001)가 도입 후 24개월간 유지; 12개월 투사 시 전체 표본 +5.92건, 저볼륨군 +3.41건.

측정 지표가 제조사(Align Technology) 자체 Invisalign 매출뿐이라 비-Invisalign 대조군·비용 측(스캐너 자본비·스캔당 비용) 상계가 전혀 없고, 제조사 제공 매출 데이터 기반 ITS로는 마케팅·자연성장 등 동시 요인과 스캐너 단독 효과를 분리할 수 없다 — 연관성으로만 읽어야 하며 순경제이익(net economic benefit)으로 확대해석 금지.

## 1. Document Information
- **Journal**: J Clin Dent. 2017 Nov;28(Suppl):S1-5.
- **DOI**: none in PubMed (PMID 29272086)
- **Institution**: not specified in abstract; analysis built on proprietary receipt data from Align Technology (maker of Invisalign/iTero); funding and sponsorship are not stated in the abstract or PubMed record

## 2. Key Contributions

- First (to this wiki's holdings) quantitative ITS estimate of a specific capital-equipment acquisition's (iTero scanner) association with Invisalign practice revenue/volume, at large scale (1,871 practices, 48 months).
- Separately quantifies the effect in a **low-volume North American GP subset** (n=319), showing the abrupt increase persisted at least 24 months post-acquisition — relevant to a GP deciding whether an IOS purchase "pays for itself" via Invisalign starts specifically.
- Reports both an abrupt level-change effect (month 25) and a projected 12-month receipt gain, giving practices a rough order-of-magnitude figure (+5.92 or +3.41 receipts/year depending on segment) rather than only a p-value.

## 3. Methodology and Architecture

- **Design**: Interrupted time series (ITS) analysis, industry (Align Technology) receipt data.
- **Data**: Invisalign gross-receipt records for 1,871 GP and orthodontic practices worldwide, 24 months pre- and 24 months post-iTero scanner introduction (48 months total); low-volume North American GP subset n=319 (≤5 Invisalign receipts in the 12 months prior to scanner acquisition).
- **n**: 1,871 practices (full sample); 319 practices (low-volume North American GP subset).
- **Outcomes**: monthly Invisalign gross receipts / treatment-start counts; abrupt level change at scanner-introduction month (month 25) vs. counterfactual (no-scanner) regression prediction; slope-change (longer-term trend shift) also explored.

## 4. Key Results and Benchmarks

- Full sample: abrupt increase at month 25, b = 0.49, p < 0.001; predicted (no-scanner counterfactual) 2.38 → observed 2.88 receipts, **+20.71%**.
- Low-volume North American GP subset (n=319): abrupt increase at month 25, b = 0.28, p < 0.001; effect still evident 24 months after scanner introduction.
- Projected 12-month gain: **+5.92 receipts** for the full worldwide sample (1,871 practices); **+3.41 receipts** for the 319 low-volume North American GPs.

## 5. Limitations and Future Work

- **No non-Invisalign comparator.** The only outcome measured is Invisalign gross receipts — the paper cannot say whether total practice revenue, total case starts (including non-Invisalign clear aligners or fixed appliances), or patient volume changed; it is possible the scanner shifted case mix toward Invisalign without net practice growth.
- **No cost-side accounting.** Scanner capital cost and ongoing per-scan/subscription cost are not netted against the receipt increase — the paper reports a top-line association, not a net economic benefit or ROI.
- **Sponsor/data-source conflict of interest.** The receipt data, the scanner (iTero), and the outcome (Invisalign) are all Align Technology products; this is manufacturer data about the manufacturer's own ecosystem, published in a J Clin Dent supplement (a manufacturer-supplement-friendly venue). Independent replication with non-Align data does not appear to exist in this wiki.
- **Causal attribution problem inherent to ITS on receipt data.** An abrupt increase coincident with scanner acquisition cannot be cleanly separated from concurrent practice-level events — marketing pushes that often accompany a new-technology purchase, general practice growth, seasonal effects, or a Hawthorne-like effect of investing in new technology — since the analysis has no untreated comparison practices matched on timing.
- **External validity of the low-volume subset.** The 319-practice North American low-volume GP subset was selected post hoc as practices with ≤5 receipts in the prior year; conclusions may not generalize to high-volume GPs or non-North-American markets.

## 6. Related Work

- listl-2019 ([[practice-management/listl-2019-what-is-health-economics-oral-health]]): health-economics framework (demand, market incentives, provider behavior under new capability) into which this paper's finding fits as an empirical (but sponsor-affiliated) instance.
- singh-2025 ([[digital-workflow/singh-2025-intraoral-scanners-accuracy-umbrella-review]]): the accuracy/clinical-performance rationale (why a practice would clinically justify an IOS purchase) that this paper's economic-impact finding is a companion, non-overlapping axis to.

## 7. Glossary

- **Interrupted Time Series (ITS) analysis**: a quasi-experimental design that models an outcome's trend before and after a defined intervention point, testing for an abrupt level change and/or slope change at that point.
- **iTero**: Align Technology's intraoral scanner (IOS) product line, marketed as a digital-impression precursor to Invisalign treatment.
- **Invisalign receipts**: gross billing records for Invisalign clear-aligner treatment starts, used here as the practice-revenue proxy.
