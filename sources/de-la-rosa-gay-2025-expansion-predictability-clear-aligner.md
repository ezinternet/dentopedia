---
title: "Factors affecting expansion predictability of clear aligner treatment"
authors: "de la Rosa-Gay ..., et al."
year: 2025
doi: "10.1007/s00784-025-06328-y"
category: [orthodontics/clear-aligner]
source_collection: pubmed-text
full_text: true
pmid: "40257582"
pmcid: "PMC12011961"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12011961/
text_path: /Users/oracleneo/llm-wiki/papers/de-la-rosa-gay-2025-expansion-predictability-clear-aligner.txt
text_filename: de-la-rosa-gay-2025-expansion-predictability-clear-aligner.txt
---

## Why Ingested

[[orthodontics/clear-aligner/fonseca-planells-2026-clear-aligner-maxillary-expansion-growing]] covers aligner maxillary expansion in *growing* patients (orthopedic potential). This adult-only retrospective cohort complements it by quantifying *which clinical factors* drive expansion underachievement in adults (where movement is purely dental tipping), and is the first study to use a multilevel (patient/arch/tooth) GLMM to adjust for confounding — supplying the adjusted effect sizes (arch, crossbite, tooth type, predicted-expansion magnitude) that single-landmark studies could not isolate.

## Three-line Summary

Retrospective cohort (98 adults, 720 tooth pairs, Invisalign SmartTrack, Barcelona) with multilevel generalized linear mixed model (GLMM) analysis of factors affecting clear-aligner expansion predictability.

Mean planned-vs-achieved expansion discrepancy was 0.92 mm (72.2% underexpansion); multivariate GLMM identified four independent predictors of worse predictability: maxillary arch (+0.47 mm vs mandible), bilateral crossbite (+0.55 mm), more posterior tooth position (1st molar +0.45 mm vs canine), and larger planned expansion (+0.14 mm per mm planned).

Clinicians should anticipate systematic underexpansion — especially in the posterior maxilla and in crossbite cases — and build overcorrection into aligner prescriptions; mandibular and canine expansion is the most reliable.

## 세줄요약

후향 코호트(성인 98명·치아쌍 720개, 인비절라인 SmartTrack, 바르셀로나): 다수준 일반화선형혼합모델(Generalized Linear Mixed Model, GLMM)로 투명교정장치(Clear Aligner Therapy, CAT) 치열궁 확장 예측성 결정 인자 분석.

계획 대비 실제 확장의 평균 절대 오차 0.92 mm(72.2% 과소확장); 다변량 GLMM에서 예측성 저하의 독립 예측 인자: 상악(+0.47 mm vs 하악), 양측성 교차교합(+0.55 mm), 구치부(제1대구치 +0.45 mm vs 견치), 계획 확장량 클수록(1 mm당 +0.14 mm).

상악 구치부 및 교차교합에서 과소확장을 예상하고 교정 처방에 과교정(Overcorrection)을 미리 반영해야 함; 하악과 견치 확장이 가장 예측 신뢰성이 높음.

## 1. Document Information

- **Title**: Factors affecting expansion predictability of clear aligner treatment
- **Authors**: de la Rosa-Gay et al. (single treating orthodontist CRG, University of Barcelona / private clinic, Barcelona, Spain)
- **Year**: 2025 (published 2025-04-21)
- **Journal**: Clinical Oral Investigations
- **DOI**: 10.1007/s00784-025-06328-y
- **PMID**: 40257582 / **PMCID**: PMC12011961
- **Study design**: Retrospective cohort study (STROBE-reported; multilevel GLMM)
- **Source**: According to PubMed, retrieved via PMC full text — [DOI](https://doi.org/10.1007/s00784-025-06328-y)

## 2. Key Contributions

1. **First multilevel (patient → arch → tooth) GLMM** of aligner expansion predictability — corrects the statistical flaw of prior single-landmark, tooth-as-independent analyses.
2. **Adjusted effect sizes** for the four factors that independently degrade predictability: maxillary arch, posterior crossbite, posterior tooth position, and larger planned expansion.
3. **Less-restrictive inclusion criteria** than prior reports (Tien, Houle) — improving external validity to the real adult Invisalign population (allowed missing teeth, implants, IPR, class II/III elastics).
4. Quantifies the overall accuracy gap (0.92 mm) and the directionality (72.2% underexpansion; overcorrections concentrated in the mandible).

## 3. Methodology and Architecture

- **Sample**: 102 screened → 98 analyzed (4 excluded for poor compliance), 720 tooth pairs. Adults >18 y, both arches treated, no extractions, first refinement present.
- **Aligner**: Invisalign SmartTrack, Lite/Moderate/Comprehensive, treated Nov 2017–Dec 2023 by one orthodontist.
- **Outcome**: absolute difference (mm) between ClinCheck-predicted and achieved arch-width expansion at canines, 1st/2nd premolars, 1st molars (from the ClinCheck arch-width table).
- **Covariates**: age, sex, posterior crossbite (none/uni/bilateral), modality, planned aligners, treatment time, compliance, predicted expansion, IPR, attachment count, implants, missing teeth, wear interval (7 vs 10 days by modality).
- **Statistics**: sample size adjusted for 3-level clustering (final n=98). Univariate GLMM per covariate; multivariate GLMM (forced entry, covariates with univariate p<0.30 + arch×tooth interaction). Attachment count dropped from the multivariate model for co-linearity with crossbite.

## 4. Key Results and Benchmarks

- **Overall accuracy**: absolute difference 0.92 mm (95%CI 0.86–0.99). 72.2% underexpansion; 22.78% overcorrection (95%CI 19.86–25.98), of which the large majority occurred in the mandible (130/164; text also states 79.3% of overcorrections were mandibular).
- **Arch-level discrepancy**: Maxilla 1.24 mm vs Mandible 0.61 mm.
- **Tooth-level absolute discrepancy (max / mand)**: canine 0.90 / 0.36; 1st premolar 1.29 / 0.69; 2nd premolar 1.44 / 0.67; 1st molar 1.37 / 0.78 mm.
- **Multivariate GLMM (adjusted coefficients, mm)**:
  - Maxilla vs mandible: +0.47 (0.35–0.59), p<0.001
  - Posterior crossbite: unilateral +0.26 (0.08–0.45), bilateral +0.55 (0.20–0.90), p<0.001
  - Tooth type vs canine: 1st premolar +0.22, 2nd premolar +0.29, 1st molar +0.45, p<0.001
  - Predicted expansion: +0.14 per mm (0.10–0.19), p<0.001
  - Arch×tooth interaction NOT significant (F[3,709]=1.43, p=0.233)
- **Not associated** with predictability: age, sex (in multivariate), treatment modality, compliance, implants, missing teeth, IPR/stripping, treatment duration.

## 5. Limitations and Future Work

- Retrospective design (some variable reliability), though outcomes were objective software measurements.
- Single experienced orthodontist + single manufacturer → limits generalization across operators/aligner systems.
- Did not assess malocclusion type/complexity, tipping vs bodily movement, periodontal support, or simultaneous movements.
- Reported mean age inconsistency in the paper (abstract 48.7 y vs Table/body ~42.3 y).
- Future work: compare commercially available aligner systems; analyze growing patients separately; model tipping and periodontal support.

## 6. Related Work

- Tien et al. and Houle et al. — prior predictability studies (maxilla ~73–76%, mandible ~87%) with restrictive inclusion criteria; this study confirms the maxilla<mandible pattern with adjusted models.
- Solano-Mendoza et al. — ClinCheck arch-width table validity vs digital casts.
- Adult transverse-deficiency adjuncts when >7 mm needed: SARPE, mini-implant assisted maxillary expansion (MARPE), segmental osteotomies.
- [[orthodontics/clear-aligner/fonseca-planells-2026-clear-aligner-maxillary-expansion-growing]] — aligner maxillary expansion in growing patients (orthopedic vs dental).

## 7. Glossary

- **ClinCheck**: Align Technology's treatment-planning software; its arch-width table is the source of predicted/achieved measurements.
- **GLMM (generalized linear mixed model)**: regression handling clustered/multilevel data (here patient → arch → tooth).
- **Underexpansion**: achieved arch width less than planned (the common error mode).
- **Overcorrection / overexpansion**: achieved expansion exceeds planned (here concentrated in the mandible).
- **IPR / stripping**: interproximal reduction of enamel to create space.
- **SARPE / MARPE**: surgically-assisted / mini-implant-assisted rapid palatal expansion for adult skeletal transverse deficiency.
