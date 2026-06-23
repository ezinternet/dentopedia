---
title: "Adverse events of oral analgesics after third molar extraction: A network meta-analysis of randomized controlled trials"
authors: Magesty R-A, de-Souza G-M, Fernandes I-A, de-Almeida R-S, Meireles M-R, Al-Moraissi E-A, Galvão E-L, Falci S-G
year: 2026
doi: 10.4317/medoral.27956
category: drug/analgesics
source_collection: pubmed-text
full_text: true
pmid: "41578906"
pmcid: "PMC13135298"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13135298/
text_path: /Users/oracleneo/llm-wiki/papers/magesty-2026-adverse-events-oral-analgesics-third-molar-nma.txt
text_filename: magesty-2026-adverse-events-oral-analgesics-third-molar-nma.txt
---

## Why Ingested

Existing analgesics pages emphasize NSAID *efficacy* and serious long-term safety (GI/CV/renal) but lack a structured safety ranking for the acute single-dose third-molar model. This NMA (28 RCTs, 5306 patients) directly ranks adverse-event safety across single-dose oral regimens and contextualizes the NSAID risk as mostly minor/nocebo-driven, complementing the efficacy-focused [[drug/analgesics/watson-2022-acetaminophen-codeine-ibuprofen-third-molar-sr-ma]] and the broad [[drug/analgesics/moore-2015-single-dose-oral-analgesics-cochrane-overview]]. It also pairs with [[drug/analgesics/feldman-2024-nonopioid-opioid-third-molar-rct]] (nonopioid vs opioid in the same model).

## One-line Summary

Frequentist network meta-analysis of 28 RCTs (5306 third-molar patients): single-dose NSAID monotherapy ranked least safe by SUCRA (86.5%), but very low–low certainty and a high placebo adverse-event rate point to a predominant nocebo effect rather than true NSAID harm.

## 한줄요약

28개 RCT(5306명, 하악 제3대구치 발치)의 빈도주의 네트워크 메타분석: 단회 경구 NSAID 단독요법이 SUCRA 안전성 순위에서 가장 위험(86.5%)했으나 근거 확실성은 매우 낮음~낮음이고 위약군 이상반응 빈도도 높아, 실제 NSAID 위해보다 노세보(nocebo) 효과가 주된 기전으로 해석됨.

## 1. Document Information

- **Title**: Adverse events of oral analgesics after third molar extraction: A network meta-analysis of randomized controlled trials
- **Authors**: Magesty R-A, de-Souza G-M, Fernandes I-A, de-Almeida R-S, Meireles M-R, Al-Moraissi E-A, Galvão E-L, Falci S-G
- **Journal**: Medicina Oral, Patología Oral y Cirugía Bucal 2026;31(3):e431-e445
- **DOI**: 10.4317/medoral.27956 · **PMID**: 41578906 · **PMCID**: PMC13135298
- **Source**: PubMed Central full text (PMC13135298)
- **Type**: Systematic review + network meta-analysis (frequentist, random-effects), CINeMA certainty
- **Registration**: PROSPERO CRD420251045775

## 2. Key Contributions

- First NMA focused specifically on the **safety** (adverse-event) profile of single-dose oral analgesics in the third molar surgery model (prior NMAs in this model focused on efficacy).
- Ranks seven analgesic-class regimens + placebo by SUCRA-based probabilistic safety, with CINeMA certainty grading.
- Reframes the apparently "unsafe" NSAID ranking as a likely **nocebo-dominated** phenomenon, given the high adverse-event rate in placebo arms and very low–low certainty.

## 3. Methodology and Architecture

- **Design**: PRISMA-NMA + Cochrane Handbook; frequentist random-effects NMA in R (`netmeta`).
- **Databases (to June 2024)**: MEDLINE/PubMed, CENTRAL, VHL, Embase, Web of Science + ClinicalTrials.gov + Google Scholar + handsearch.
- **PICOS**: lower third molar extraction under local anesthesia; single-dose oral anti-inflammatory/analgesic; vs placebo or other oral drug/dose; AEs related to medication up to discharge; parallel/cross-over/split-mouth RCTs.
- **Exclusions**: herbal/homeopathic/enzymatic, non-oral routes, nitrous oxide/fentanyl/benzodiazepines, experimental/withdrawn drugs, non-RCTs, observational.
- **Class-based nodes** (not individual molecules, to keep network connected): monotherapies (Non-opioid analgesic; NSAIDs; Opioid analgesic) and combinations (Non-opioid+Opioid; NSAID+Non-opioid; NSAID+Non-opioid+Opioid; Opioid+NSAID); Placebo as common comparator.
- **Outcome**: composite "any AE related to medication use" (no event-type sub-analysis — would fragment network).
- **Risk of bias**: Cochrane RoB 2.0. **Certainty**: CINeMA (6 domains).

## 4. Key Results and Benchmarks

- **Yield**: 6677 records → 40 in SR → **28 RCTs, 5306 surgeries** in NMA. Placebo arm n=1078 across 23 RCTs. RoB in NMA: 7 low, 13 some concerns, 8 high.
- **Significant pairwise comparisons (RR, 95% CI):**
  - Non-opioid analgesic + Opioid vs Placebo: **RR 1.71 (1.05–2.77)** — only active regimen significantly worse than placebo (low certainty).
  - NSAID alone vs other non-opioid analgesic: **RR 1.82 (1.24–2.68)** — NSAID higher risk (low certainty).
  - NSAID alone vs (Non-opioid + Opioid): **RR 1.42 (1.03–1.96)** — NSAID higher risk (low certainty).
  - Opioid alone vs NSAID alone: **RR 0.61 (0.41–0.89)** — opioid monotherapy LOWER AE risk than NSAID monotherapy (very low certainty).
- **SUCRA safety ranking** (higher % = higher probability of being the LEAST safe / most adverse events):
  - **NSAIDs 86.5% → highest AE probability (least safe)**
  - **Placebo 81.7% → second-least safe**
  - **NSAID + non-opioid analgesic + opioid (triple combination) 15.5% → SAFEST / fewest adverse events**
- **Consistency**: significant global inconsistency (Q=47.27, df=31, p=0.0309), driven by between-design divergence (Q=32.01, p=0.0150) not within-design heterogeneity. No significant local inconsistency by SIDE.
- **Certainty**: very low to low across the network.

## 5. Limitations and Future Work

- Composite AE outcome only (could not separate GI vs CNS events without disconnecting the network).
- **Class-level aggregation** masks molecule-level differences (e.g., selective COX-2 inhibitors vs non-selective ibuprofen).
- Immediate postoperative window only (delayed AEs like alveolar osteitis / surgical-site infection not captured).
- Heterogeneous/under-reported local anesthetics, third-molar difficulty classification, and baseline pain intensity (severe pain itself triggers autonomic nausea/vomiting).
- Serious-risk NSAID evidence (CNT Collaboration 2013) comes from long-term use and should not be extrapolated to acute single-dose use in young healthy patients.
- Future: standardized outcome definitions, baseline-pain stratification, pharmacovigilance to detect rare events, and nocebo-mitigation (positive framing during informed consent).

## 6. Related Work

- Efficacy-focused third-molar combination evidence: Watson 2022 (acetaminophen/codeine/ibuprofen SR-MA), Moore 2015 Cochrane overviews.
- Same-model nonopioid vs opioid RCT: Feldman 2024.
- NSAID serious-safety context (long-term): zingel-2025 (CV), gomes-2025 (renal).
- Methodologically analogous dental NMAs: Miroshnychenko 2023 (extraction pain NMA), Samani 2025 (endodontic NSAID NMA).

## 7. Glossary

- **NMA (Network Meta-Analysis)**: combines direct + indirect comparisons to simultaneously rank multiple treatments.
- **SUCRA (Surface Under the Cumulative Ranking curve)**: 0–100% summary of a treatment's ranking; here higher % = higher probability of being the *least safe* (most adverse events).
- **CINeMA (Confidence in Network Meta-Analysis)**: framework grading certainty across six domains.
- **RR (Relative Risk)**: ratio of adverse-event risk between two regimens; CI excluding 1 = statistically significant.
- **Nocebo effect**: adverse symptoms arising from negative expectations rather than pharmacology — invoked here to explain the high placebo adverse-event rate.
- **SIDE (Separate Indirect from Direct Evidence)**: method to detect local inconsistency between direct and indirect estimates.

*According to PubMed; full text from PMC13135298. DOI: [10.4317/medoral.27956](https://doi.org/10.4317/medoral.27956)*
