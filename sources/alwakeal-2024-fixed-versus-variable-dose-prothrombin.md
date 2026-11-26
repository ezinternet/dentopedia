---
source_collection: pubmed-text
full_text: true
pmid: "38353592"
pmcid: "PMC11008445"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11008445/
text_path: /Users/oracleneo/llm-wiki/papers/alwakeal-2024-fixed-versus-variable-dose-prothrombin.txt
text_filename: alwakeal-2024-fixed-versus-variable-dose-prothrombin.txt
---

## Why Ingested

Fixed- vs variable-dose 4-PCC for emergent VKA reversal is directly relevant to dental hemostasis/anticoagulant management; complements [[drug/anticoagulants/choudhary-2025-bleeding-thrombosis-noac-dental-management]].

→ [[drug/anticoagulants/alwakeal-2024-fixed-versus-variable-dose-prothrombin]]

## Three-line Summary

This systematic review and meta-analysis of 3 RCTs and 16 cohort studies (2235 total patients) compared fixed-dose vs variable-dose 4-PCC for emergent VKA reversal. Fixed-dose regimens were associated with lower 4-PCC doses, shorter administration time, improved clinical hemostasis, and reduced mortality and thromboembolic events, but were less likely to achieve INR <1.5. Authors suggest a fixed dose of at least 2000 IU may be optimal, with additional variable dosing for ICH, high INR, or heavy patients.

## 세줄요약

본 연구는 비타민 K 길항제 (Vitamin K Antagonist, VKA) 응급 역전을 위한 4-factor 프로트롬빈 복합체 농축물 (4-Factor Prothrombin Complex Concentrate, 4-PCC)의 고정 용량 vs 가변 용량을 비교한 체계적 문헌고찰 및 메타분석이다. 고정 용량은 용량·투여 시간·임상 지혈·사망률·혈전색전증에서 이득이 있었으나 INR <1.5 달성률은 낮았다. 최소 2000 IU 고정 용량이 최적일 수 있으며, ICH·고INR·고체중 환자에는 추가 가변 용량이 필요할 수 있다.

## 1. Document Information

- **Title**: Fixed- Versus Variable-Dose Prothrombin Complex Concentrate for the Emergent Reversal of Vitamin K Antagonists: A Systematic Review and Meta-Analysis
- **Authors**: Alwakeal Amr, Maas Matthew B., Naidech Andrew M., Jahromi Babak S., Potts Matthew B.
- **Journal**: Critical Care Medicine
- **Year**: 2024
- **DOI**: 10.1097/CCM.0000000000006212
- **PMID**: 38353592
- **PMCID**: PMC11008445

## 2. Key Contributions

- Comprehensive meta-analysis (3 RCTs + 16 cohort studies, 2235 patients) of fixed- vs variable-dose 4-PCC for emergent VKA reversal.
- Fixed-dose associated with lower 4-PCC dose (1537.3 vs 2222.2 IU), shorter order-to-needle time (39 vs 72 min), and improved clinical hemostasis (74.1% vs 61.6%).
- High-certainty evidence: fixed-dose reduces mortality and thromboembolic events.
- Fixed-dose less likely to achieve INR <1.5 (64.6% vs 74.3% cohorts; 66.7% vs 88.6% RCTs).
- Exploratory subgroup: fixed dose ≥2000 IU may be optimal.

## 3. Methodology and Architecture

- Systematic review per Cochrane and PRISMA; searched PubMed, Embase, Ovid MEDLINE Jan 2000–Aug 2023.
- Inclusion: English, VKA patients, fixed-dose 4-PCC intervention vs variable-dose comparator, clinical outcome.
- Quality: NOS for cohorts, ROBINS-I for RCTs; GRADE certainty.
- Random-effects meta-analysis (DerSimonian-Laird) in R `meta`; SMD for continuous, OR for binary.
- Subgroups: study type, indication (ICH/non-ICH/all), baseline INR (≥4 vs <4), weight (≥80 vs <80 kg), 4-PCC dose (1000–1500/1500–2000/2000–2500 IU).

## 4. Key Results and Benchmarks

- Total: 323 RCT (161 fixed/162 variable) + 1912 cohort (858 fixed/1054 variable).
- 4-PCC dose: 1537.3 vs 2222.2 IU (SMD −1.02; 95% CI −1.3 to −0.8; low certainty).
- Dose/kg: 22.1 vs 27.7 IU/kg (SMD −0.5; 95% CI −1.03 to 0.0002; low).
- Order-to-needle: 39 vs 72 min (SMD −0.4; high certainty).
- PCC-to-INR: 147.4 vs 192.5 min (SMD −0.3; high).
- Clinical hemostasis: 74.1% vs 61.6% (OR 1.7; 95% CI 1.05–2.8; moderate).
- INR <2: 88.8% vs 92.4% (OR 0.7; 95% CI 0.4–1.2; moderate) — no clear difference.
- INR <1.5: cohorts 64.6% vs 74.3% (OR 0.6; 95% CI 0.5–0.8; moderate); RCTs 66.7% vs 88.6% (OR 0.3; 95% CI 0.09–0.8; high).
- Mortality: cohorts 15.6% vs 18.8% (OR 0.8; 95% CI 0.6–1.03; high); RCTs 4.7% vs 7.2% (OR 0.6; 95% CI 0.1–1.9; high).
- TEEs: cohorts 2.4% vs 4.4% (OR 0.5; 95% CI 0.3–1; high); RCTs 1.2% vs 1.8% (OR 0.7; 95% CI 0.1–3.8; moderate).
- Additional 4-PCC: cohorts 5.2% vs 3.1% (OR 1.5); RCTs 17.4% vs 2.5% (OR 8.6).
- FFP: cohorts 16.3% vs 17.8% (OR 0.8); RCTs 5.5% vs 0.8% (OR 4.7).
- ICU/hospital LOS: uncertain.
- ICH subgroup: fixed-dose reduces order-to-needle time; equivalent INR<2 and clinical hemostasis; lower TEE (moderate); uncertain mortality; lower INR<1.5 achievement (80% vs 89%; low).

## 5. Limitations and Future Work

- Few RCTs; majority retrospective.
- Heterogeneous primary outcomes (goal INRs, clinical hemostasis definition).
- Small patient numbers in some subgroups.
- Moderate–high heterogeneity (10/19 meta-analyses I²>50%).
- Optimal fixed-dose regimen not directly compared; future studies needed.

## 6. Related Work

- Mohammadi et al (2020): 1000–1500 IU fixed dose safe/effective/timesaving.
- PROPER-3 trial: 1000 IU fixed vs variable in non-ICH patients, similar outcomes.
- Stoecker et al: 1500 IU fixed → 61.8% INR<1.5 within 15 min.
- Klein et al: 1500 IU fixed → INR<2 in 92%, ≤1.5 in 72%, no TEEs.
- Choudhary 2025 (dental NOAC management) — reversal agent mapping context.

## 7. Glossary

- **4-PCC (Four-Factor Prothrombin Complex Concentrate)**: concentrate of factors II, VII, IX, X for VKA reversal.
- **VKA (Vitamin K Antagonist)**: e.g., warfarin; reversed by PCC/vitamin K.
- **INR (International Normalized Ratio)**: coagulation measure; targets <2 or <1.5.
- **TEE (Thromboembolic Event)**: clotting complication of reversal.
- **Clinical hemostasis**: absence of major bleeding per ISTH criteria.
- **Order-to-needle time**: time from order entry to PCC administration.