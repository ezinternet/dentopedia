---
title: "Risk of Adverse Reactions to Oral Antibiotics Prescribed by Dentists"
authors: M.H. Thornhill, M.J. Dayer, M.J. Durkin, P.B. Lockhart, L.M. Baddour
year: 2019
doi: 10.1177/0022034519863645
category: [drug/antibiotics]
pdf_path: /Users/oracleneo/llm-wiki/papers/thornhill-2019-adverse-reactions-oral-antibiotics-dentists.pdf
pdf_filename: thornhill-2019-adverse-reactions-oral-antibiotics-dentists.pdf
source_collection: external
---

## One-line Summary
NHS England prescription cost analysis (2010–2017) cross-referenced with Yellow Card MHRA adverse drug reaction (ADR) reports to quantify ADR rates per million prescriptions for the antibiotics dentists prescribe most: **amoxicillin safest (21.5/million overall, 0.1/million fatal)**, clindamycin most dangerous (highest fatal rate 2.9/million, mostly C. difficile), penicillin V highest anaphylaxis, macrolides associated with QT/cardiac death.

## 1. Document Information
- **Journal**: Journal of Dental Research 2019;98(10):1081–1087.
- **Study type**: Retrospective national pharmacoepidemiologic analysis (NHS prescription data + national pharmacovigilance reports).
- **Setting**: England, 2010–2017; mean 23,624 actively practicing dentists/year.

## 2. Key Contributions
- Provides per-million-prescription ADR rates (overall, serious, fatal) for the antibiotic classes dentists actually prescribe — a number clinicians can quote for informed consent.
- Demonstrates that amoxicillin is by a wide margin the safest first-line dental antibiotic.
- Identifies clindamycin's disproportionately high fatal ADR rate (mostly C. difficile colitis) — undermines "amoxicillin allergy → switch to clindamycin" reflex.
- Quantifies penicillin V's relatively high anaphylaxis rate and macrolide cardiac arrhythmia mortality (QT prolongation → torsades de pointes).
- Real-world denominators (prescriptions issued) avoid the bias of relying on RCT safety data.

## 3. Methodology and Architecture
- Prescription Cost Analysis (NHS Digital): all oral antibiotic prescriptions in England primary care 2010–2017, separately extractable for general dental practitioners.
- Yellow Card MHRA Interactive Drug Analysis Profiles: spontaneous ADR reports for those antibiotics.
- ADR rate = Yellow Card reports / total NHS primary-care prescriptions per million.
- Categorization via MedDRA (Medical Dictionary for Regulatory Activities); 27 system organ classes reduced to 14 + "other" for clarity.
- Limitation: spontaneous reporting underestimates absolute ADR rates but allows valid relative comparisons.

## 4. Key Results and Benchmarks
- **Amoxicillin**: 64.8% of all dental antibiotic prescribing; overall ADR 21.5/million; fatal 0.1/million — lowest among commonly prescribed dental antibiotics.
- **Metronidazole** (2nd most prescribed): overall 70.6/million, serious 51.4/million, fatal 0.7/million — ~3× amoxicillin.
- **Clindamycin**: highest fatal rate 2.9/million — almost all due to C. difficile infection/colitis; also highest GI ADR rate.
- **Penicillin V**: highest immune system ADR rate; >20% of immune ADRs were anaphylaxis/anaphylactoid including 0.15 deaths/million.
- **Macrolides (erythromycin, clarithromycin, azithromycin)**: cardiac arrhythmia (QT prolongation, torsades) dominant cause of death; nervous system + psychiatric ADRs.
- **Amoxicillin + clavulanic acid**: only antibiotic associated with hepatobiliary ADRs (cholestatic jaundice).

## 5. Limitations and Future Work
- Yellow Card spontaneous reporting underestimates true incidence (estimated 1–10% report rate).
- Numerator (ADRs) and denominator (prescriptions) come from different systems — attribution to dental prescribing specifically not always direct.
- England only; prescribing patterns vary internationally.
- Cannot adjust for patient-level confounders (comorbidity, drug-drug interactions, dose).
- Trends over 8 years not separately analyzed in this paper.

## 6. Related Work
- Bazsefidpay 2023 — Dental antibiotic prescribing adherence to restrictive recommendations.
- Colibasanu 2025 — Drug-drug interaction prevalence in dental patients (Romania).
- Pyo 2026 — Geriatric dentistry drug interaction review (Korea).
- Hancox 2013 — Macrolide QT prolongation mechanism.

## 7. Glossary
- **ADR (Adverse Drug Reaction)**: Noxious response to a medication at normal therapeutic doses; subdivided into nonserious / serious / fatal by reporter.
- **Yellow Card scheme**: UK MHRA spontaneous ADR reporting system, in place >50 years, open to patients and healthcare professionals.
- **MedDRA**: International standardized medical terminology hierarchy with 27 system organ class categories; used for ADR coding.
- **C. difficile colitis**: Toxin-mediated pseudomembranous colitis triggered by antibiotic disruption of normal gut flora; clindamycin classically highest risk.
- **Torsades de pointes**: Polymorphic ventricular tachycardia precipitated by QT prolongation; can degenerate to ventricular fibrillation and sudden cardiac death.
