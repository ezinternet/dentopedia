---
title: "Adverse events of oral analgesics after third molar extraction: A network meta-analysis of randomized controlled trials"
authors: Magesty R-A, de-Souza G-M, Fernandes I-A, de-Almeida R-S, Meireles M-R, Al-Moraissi E-A, Galvão E-L, Falci S-G
year: 2026
date: 2026-05-01
doi: 10.4317/medoral.27956
source: magesty-2026-adverse-events-oral-analgesics-third-molar-nma.md
category: drug/analgesics
confidence: sr+ma
source_collection: pubmed-text
full_text: true
pmid: "41578906"
pmcid: "PMC13135298"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13135298/
pdf_path: /Users/oracleneo/llm-wiki/papers/magesty-2026-adverse-events-oral-analgesics-third-molar-nma.txt
pdf_filename: magesty-2026-adverse-events-oral-analgesics-third-molar-nma.txt
text_path: /Users/oracleneo/llm-wiki/papers/magesty-2026-adverse-events-oral-analgesics-third-molar-nma.txt
text_filename: magesty-2026-adverse-events-oral-analgesics-third-molar-nma.txt
tags: [nsaid, opioid, acetaminophen, third-molar, adverse-events, network-meta-analysis, nocebo, sucra]
relations:
  - type: extends
    target: watson-2022-acetaminophen-codeine-ibuprofen-third-molar-sr-ma
  - type: reinforces
    target: moore-2015-single-dose-oral-analgesics-cochrane-overview
---

## Three-line Summary

Frequentist NMA of 28 RCTs (5,306 third-molar extraction patients) comparing 7 analgesic-class regimens + placebo on medication-related adverse events.

NSAID monotherapy ranked least safe by SUCRA (86.5%) and placebo ranked second (81.7%); the NSAID+non-opioid+opioid triple combination ranked safest (15.5%).

Very low–low certainty and the high placebo adverse-event rate indicate a predominant nocebo effect rather than true drug harm, so NSAIDs should remain first-line for post-extraction pain.

## 세줄요약

28개 RCT(5,306명, 하악 제3대구치 발치) 네트워크 메타분석 — 7개 진통제 약물군+위약의 이상반응을 비교한 SUCRA 분석.

NSAID 단독군이 SUCRA 안전성 최하위(86.5%)였고 위약이 2위(81.7%)였으며, NSAID+비마약성+마약성 3제 병용군이 최상위(15.5%)로 가장 안전했다.

근거 확실성이 매우 낮음~낮음이고 위약군 이상반응도 높아 NSAID의 겉보기 위험은 실제 약물 독성이 아닌 노세보 효과로 해석되며, NSAIDs는 계속 1차 선택약으로 유지되어야 한다.

## Summary

This is the first network meta-analysis (NMA) focused on the **safety** (adverse-event, AE) profile of single-dose oral analgesics in the standardized third molar surgery model — prior NMAs in this model addressed efficacy. Twenty-eight RCTs (5306 surgeries) were analyzed in a frequentist random-effects framework, with CINeMA certainty grading. Treatments were nodes by pharmacological *class* (not individual molecule) to keep the network connected.

The headline ranking is counterintuitive: **NSAID monotherapy** had the highest probability of being least safe (SUCRA 86.5%), but **placebo was second-least safe (81.7%)**. Because a pharmacologically inert placebo cannot cause true drug AEs, the authors attribute the pattern to the **nocebo effect** — negative patient expectations (amplified by the informed-consent risk disclosure) plus surgery-related prostaglandin-driven nausea being misattributed to medication. Combined with very low–low certainty evidence and few significant active-vs-placebo differences, the conclusion is that NSAIDs' apparent "safety cost" is mostly mild, transient symptoms (nausea/vomiting), and that NSAIDs should remain first-line given their established superior analgesic efficacy (NNT as low as 1.5–3 in prior Cochrane NMAs).

## Key Contributions

- First safety-focused NMA of single-dose oral analgesics after third molar extraction.
- SUCRA probabilistic safety ranking of 7 analgesic-class regimens + placebo, graded by CINeMA.
- Identifies the **nocebo response** as the dominant driver of reported AEs in this acute single-dose setting (high placebo event rate).
- Clarifies that NSAID monotherapy's unfavorable AE ranking reflects minor transient events, not the serious GI/CV/renal harms seen with chronic use.

## Methodology

- **Design**: PRISMA-NMA + Cochrane Handbook; R `netmeta`, frequentist random-effects; PROSPERO CRD420251045775.
- **Search (to June 2024)**: MEDLINE, CENTRAL, VHL, Embase, Web of Science + ClinicalTrials.gov + Google Scholar + handsearch.
- **PICOS**: lower third molar extraction under local anesthesia; single-dose oral anti-inflammatory/analgesic; vs placebo or other oral drug/dose; medication-related AEs to discharge; parallel/cross-over/split-mouth RCTs.
- **Nodes (class effect)**: Non-opioid analgesic; NSAIDs; Opioid analgesic; Non-opioid+Opioid; NSAID+Non-opioid; NSAID+Non-opioid+Opioid; Opioid+NSAID; + Placebo.
- **Outcome**: composite "any AE related to medication" (no event-type sub-analysis — would disconnect the network).
- **RoB**: Cochrane RoB 2.0. **Certainty**: CINeMA (6 domains).
- **Yield**: 6677 → 40 in SR → **28 RCTs / 5306 surgeries** in NMA (7 low RoB, 13 some concerns, 8 high).

## Results

**Significant pairwise comparisons (RR, 95% CI):**

| Comparison | RR (95% CI) | Direction | Certainty |
|---|---|---|---|
| Non-opioid + Opioid vs Placebo | 1.71 (1.05–2.77) | combination worse than placebo (only such regimen) | low |
| NSAID alone vs other non-opioid analgesic | 1.82 (1.24–2.68) | NSAID higher AE risk | low |
| NSAID alone vs (Non-opioid + Opioid) | 1.42 (1.03–1.96) | NSAID higher AE risk | low |
| Opioid alone vs NSAID alone | 0.61 (0.41–0.89) | opioid monotherapy LOWER risk than NSAID | very low |

**SUCRA safety ranking** (higher % = higher probability of being the LEAST safe / most adverse events):

| Rank | Regimen | SUCRA | Interpretation |
|---|---|---|---|
| Most adverse events | **NSAIDs (monotherapy)** | 86.5% | highest AE probability — *least* safe |
| 2nd | **Placebo** | 81.7% | counterintuitive → nocebo |
| Fewest adverse events | **NSAID + non-opioid analgesic + opioid (triple)** | 15.5% | *safest* protocol |

- **Most adverse events**: NSAID monotherapy (and, counterintuitively, placebo).
- **Fewest adverse events / safest**: NSAID + non-opioid + opioid triple combination; opioid monotherapy also lower than NSAID monotherapy.
- **Consistency**: significant global inconsistency (Q=47.27, df=31, p=0.0309), driven by between-design divergence; no significant local inconsistency by SIDE.
- **Certainty**: very low to low across the network.

**Clinical bottom line**: Do not down-rank NSAIDs on these probabilistic safety figures. The "harm" is mild/transient (nausea), the certainty is low, and the placebo arm's high event rate shows nocebo dominates AE perception. NSAIDs remain first-line for acute post-extraction pain on efficacy grounds; the safest *combination* by this ranking is the NSAID-containing triple regimen.

## Related Papers

- [[drug/analgesics/watson-2022-acetaminophen-codeine-ibuprofen-third-molar-sr-ma]] — extends: efficacy-focused third-molar SR-MA on the same acetaminophen/opioid/ibuprofen comparators; this NMA adds the safety/AE ranking.
- [[drug/analgesics/moore-2015-single-dose-oral-analgesics-cochrane-overview]] — reinforces: Cochrane single-dose analgesic NNT data underpinning the "NSAID efficacy outweighs minor AE" conclusion.
- [[drug/analgesics/feldman-2024-nonopioid-opioid-third-molar-rct]] — same model nonopioid-vs-opioid RCT; consistent with opioid AE burden being driven by the opioid component.
- [[drug/analgesics/miroshnychenko-2023-dental-extraction-pain-network-meta]] — companion extraction-pain NMA (efficacy side).
- [[drug/analgesics/zingel-2025-nsaids-cardiovascular-risk-inflammatory-arthritis]] — long-term NSAID serious-risk context the authors caution against extrapolating to single-dose use.
- [[drug/analgesics/gomes-2025-nsaids-kidney-toxicity-icu-retrospective]] — NSAID renal-toxicity context (chronic/critically-ill, not single-dose).

*According to PubMed; full text from PMC13135298. DOI: [10.4317/medoral.27956](https://doi.org/10.4317/medoral.27956)*
