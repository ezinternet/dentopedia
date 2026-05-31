---
title: "Unveiling Drug-Drug Interactions in Dental Patients: A Retrospective Real-World Study"
authors: Daiana Colibăsanu, Sebastian Mihai Ardelean, Florina-Diana Goldiș, Maria-Medana Drăgoi, Sabina-Oana Vasii, Tamara Maksimović, Șerban Colibăsanu, Codruța Șoica, Lucreția Udrescu
year: 2025
doi: 10.3390/dj13060255
category: drug
pdf_path: /Users/oracleneo/llm-wiki/papers/colibasanu-2025-drug-drug-interactions-dental-patients-retrospective.pdf
pdf_filename: colibasanu-2025-drug-drug-interactions-dental-patients-retrospective.pdf
source_collection: external
---

## One-line Summary
Retrospective real-world study (n=105 dental patients, Timișoara private practice, Nov–Dec 2024): DrugBank Drug Interaction Checker analysis of 1,332 drug pairs found 542 DDIs — 2.3% major / 25.0% moderate / 13.4% minor; major DDI burden concentrated in age 31–60 (61.3%) and patients with cardiovascular disease (epinephrine + beta-blocker as flagship example).

## 1. Document Information
- **Journal**: Dentistry Journal 2025, 13, 255 (received Mar, accepted Jun, published 9 Jun 2025).
- **Study type**: Retrospective single-center real-world cohort study with computational DDI analysis.
- **Setting**: Private dental practice, Timișoara, Romania (Nov–Dec 2024); Victor Babeș University of Medicine and Pharmacy.

## 2. Key Contributions
- First Romanian DDI prevalence and severity quantification in a real-world dental cohort.
- Uses DrugBank Drug Interaction Checker — open, versioned, API-accessible database — as the assessment tool, demonstrating a reproducible computational workflow.
- Stratifies DDI severity by age and cardiovascular comorbidity, identifying high-risk subgroups.
- Provides concrete high-risk example pairs (epinephrine + beta-blockers) for chairside risk mitigation.

## 3. Methodology and Architecture
- 105 consecutive eligible patients of a single private dental practice over 2 months.
- Variables: demographics, preexisting diseases, dental procedures, prescribed medications (including dentistry-specific and chronic comorbidity medications).
- DDI assessment: DrugBank Drug Interaction Checker → severity classification (major / moderate / minor / none).
- Statistics: descriptive; Chi-square (major DDI prevalence across age groups 0–30 / 31–60 / ≥61); Kruskal-Wallis (total DDIs across age groups); Mann-Whitney U (total DDIs by CVD status).
- Post-hoc power analysis; no a priori sample size calculation (exploratory design).

## 4. Key Results and Benchmarks
- **Preexisting disease**: 45.7% of patients; cardiovascular disease most prevalent (19.0%).
- **Common dental diagnoses/procedures**: apical lesions 47.6%, tooth extractions 53.3%.
- **DDI totals**: 542 DDIs out of 1,332 drug pairs.
  - Major: 2.3%
  - Moderate: 25.0%
  - Minor: 13.4%
  - None: 59.3%
- **Major DDI age distribution**: 31–60 yr group 61.3%; ≥61 yr 38.7%; 0–30 yr 0.
- **Key high-risk pair**: epinephrine (local anesthetic vasoconstrictor) + beta-blockers — risk of paradoxical hypertensive crisis.
- Authors interpret higher 31–60 burden as possibly reflecting better drug recall/reporting in mid-age vs elderly.

## 5. Limitations and Future Work
- Small single-center sample (n=105).
- Computational DDI flagging only — clinical confirmation/outcome not captured.
- DrugBank "no interaction found" does not exclude unknown interactions.
- Romanian private practice — generalizability to other systems limited.
- Cross-sectional snapshot of chronic + dental meds at one timepoint.
- Authors note possible under-reporting in elderly (recall bias) as caveat to age stratification.

## 6. Related Work
- Thornhill 2019 — Dental antibiotic ADR rates (NHS England real-world).
- Pyo 2026 — Geriatric dentistry DDI narrative review (cites 40.7% DDI prevalence as benchmark).
- Bazsefidpay 2023 — Adherence to restrictive antibiotic prescribing.

## 7. Glossary
- **DDI (Drug-Drug Interaction)**: Pharmacokinetic or pharmacodynamic interaction between two co-administered drugs altering efficacy or safety.
- **DrugBank**: Open-source pharmaceutical knowledge base with API-accessible Drug Interaction Checker; versioned for reproducibility.
- **Major / moderate / minor DDI**: DrugBank severity tier — major = clinically significant, often warrants regimen change; moderate = monitor; minor = usually no action.
- **Polypharmacy**: Concurrent use of multiple medications (commonly ≥5); primary driver of DDI risk.
- **Real-world data (RWD)**: Patient health data collected outside controlled trials (EHR, claims, registries) — complements RCT evidence on actual practice patterns.
