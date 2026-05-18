---
title: "Acute Postoperative Pain Due to Dental Extraction in the Adult Population: A Systematic Review and Network Meta-analysis"
authors: Miroshnychenko A, Ibrahim S, Azab M, Roldan Y, Martinez JPD, Tamilselvan D, He L, Little JW, Urquhart O, Tampi M, Polk DE, Moore PA, Hersh EV, Claytor B, Carrasco-Labra A, Brignardello-Petersen R
year: 2023
doi: 10.1177/00220345221139230
category: [drug]
pdf_path: /Users/oracleneo/llm-wiki/papers/miroshnychenko-2023-dental-extraction-pain-network-meta.pdf
pdf_filename: miroshnychenko-2023-dental-extraction-pain-network-meta.pdf
source_collection: external
---

## One-line Summary
Network MA (82 RCTs, n=9,095): ibuprofen 200–400mg+APAP 500–1,000mg is the most effective intervention for post-extraction pain; oxycodone 5mg, codeine 60mg, and tramadol 37.5mg+APAP were no better than placebo.

## 1. Document Information
- Journal: J Dent Res 2023;102(4):391–401
- DOI: 10.1177/00220345221139230
- Design: Systematic review + frequentist network meta-analysis (NMA)
- Conducted to inform 2022 ADA clinical practice guidelines on acute dental pain
- n = 82 RCTs; 9,095 participants (56 RCTs contributed to primary network)
- Search: Medline, EMBASE, CENTRAL, US ClinicalTrials.gov (through Nov 21, 2020)

## 2. Key Contributions
- Most comprehensive NMA on dental extraction pain pharmacotherapy to date
- Directly informs ADA 2022 CPG: first-line = ibuprofen ± APAP (moderate–high certainty)
- Establishes APAP 650mg + oxycodone 10mg as the only opioid-containing regimen with moderate-high certainty of effectiveness
- Codeine 60mg, oxycodone 5mg, tramadol 37.5mg+APAP: no better than placebo (moderate certainty)
- GRADE framework applied; most interventions not more harmful than placebo for adverse effects

## 3. Methodology and Architecture
- 10 interventions compared: APAP, ibuprofen 200–400mg, naproxen, APAP+ibuprofen, APAP+codeine, APAP+oxycodone (5mg and 10mg), codeine alone, oxycodone 5mg, tramadol+APAP
- Outcomes at 6h: pain relief (PR), TOTPAR6, SPID, global efficacy, rescue analgesia, adverse effects
- Risk of bias: modified Cochrane RoB 2.0; certainty: GRADE
- Analysis: RStudio v3.5.3, frequentist NMA
- Interventions ranked from most to least effective

## 4. Key Results
| Intervention | MDp vs placebo (PR, 0–4 scale) | 95% CI | Certainty |
|---|---|---|---|
| Ibuprofen 200–400mg + APAP 500–1,000mg | 1.68 | 1.06–2.31 | Moderate–high |
| Naproxen 400–440mg | 1.44 | 1.07–1.80 | Moderate–high |
| Ibuprofen 400mg | 1.31 | 1.17–1.45 | High |
| APAP 650mg + oxycodone 10mg | 1.19 | 0.85–1.54 | Moderate–high |
| Oxycodone 5mg | ~0 | — | No better than placebo |
| Codeine 60mg | ~0 | — | No better than placebo |
| Tramadol 37.5mg + APAP 325mg | ~0 | — | No better than placebo |

## 5. Limitations and Future Work
- Search cutoff Nov 2020 (pre-Feldman 2024 trial)
- 6h primary endpoint; longer outcomes not systematically addressed
- High heterogeneity in some networks
- Most RCTs used impaction surgery model (may not fully generalize)

## 6. Related Work
- Feldman 2024 (largest RCT confirming NMA's top finding)
- Watson 2022 (focused SR+MA on 3rd molar ibuprofen vs A/C)
- ADA 2022 CPG on acute dental pain

## 7. Glossary
- NMA: Network meta-analysis
- TOTPAR6: Total pain relief summed over 6 hours
- SPID: Summed pain intensity difference
- MDp: Mean difference vs placebo
- GRADE: Grading of Recommendations Assessment Development and Evaluation
- CPG: Clinical practice guideline
