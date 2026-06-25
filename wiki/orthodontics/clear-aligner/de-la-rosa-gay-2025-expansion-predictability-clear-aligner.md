---
title: "Factors affecting expansion predictability of clear aligner treatment"
authors: "de la Rosa-Gay ..., et al."
year: 2025
date: 2025-04-21
doi: "10.1007/s00784-025-06328-y"
source: de-la-rosa-gay-2025-expansion-predictability-clear-aligner.md
category: [orthodontics/clear-aligner]
confidence: retrospective
source_collection: pubmed-text
full_text: true
pmid: "40257582"
pmcid: "PMC12011961"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12011961/
text_path: /Users/oracleneo/llm-wiki/papers/de-la-rosa-gay-2025-expansion-predictability-clear-aligner.txt
text_filename: de-la-rosa-gay-2025-expansion-predictability-clear-aligner.txt
tags: []
relations:
  - type: extends
    target: fonseca-planells-2026-clear-aligner-maxillary-expansion-growing
---

## One-line Summary

Retrospective cohort (98 adults, 720 tooth pairs, Invisalign SmartTrack) with a first-of-kind multilevel GLMM: mean planned-vs-achieved expansion discrepancy 0.92 mm (72.2% underexpansion); predictability is independently worse in the maxilla (+0.47 mm), in posterior teeth (1st molar +0.45 mm vs canine), with posterior crossbite (bilateral +0.55 mm), and with larger planned expansion (+0.14 mm/mm) — best in the mandible and canine region.

## 한줄요약

후향 코호트(성인 98명·치아쌍 720개, 인비절라인 SmartTrack)에서 다수준 GLMM 분석 결과, 계획 대비 실제 확장의 절대 오차는 평균 0.92 mm(72.2%가 과소확장)였고, 상악(+0.47 mm)·구치부(제1대구치 견치 대비 +0.45 mm)·후방 교차교합(양측 +0.55 mm)·계획확장량이 클수록(+0.14 mm/mm) 예측성이 독립적으로 떨어졌으며, 하악과 견치부에서 가장 신뢰도가 높았다.

## Summary

This adult-only retrospective cohort study quantifies how clinical variables degrade the predictability of arch expansion with Invisalign SmartTrack aligners, and is the first to model the discrepancy with a multilevel (patient → arch → tooth) generalized linear mixed model (GLMM) rather than treating teeth as independent units. Across 98 patients and 720 tooth pairs, ClinCheck-planned expansion was achieved with a mean absolute error of 0.92 mm, and the dominant error mode was underexpansion (72.2% of measurements). Four factors independently worsened predictability: the maxillary arch, posterior crossbite, posterior tooth position, and the magnitude of planned expansion. Because adults have no orthopedic expansion potential, aligners expand by tooth tipping rather than bodily translation — which the authors use to explain why the lower arch (where compression is usually accompanied by lingual tipping, easy to correct) and the canine region are the most reliable, while the constricted maxilla and molar region are the least.

## Key Contributions

- **First multilevel GLMM** of aligner expansion predictability, correcting the tooth-as-independent statistical flaw of prior single-landmark studies.
- **Adjusted (confounding-controlled) effect sizes** for the four independent predictors of discrepancy.
- **Less-restrictive inclusion criteria** (missing teeth, implants, IPR, class II/III elastics all allowed) improve external validity to the real adult Invisalign population.
- Clinical bottom line: greatest risk of not achieving planned expansion is in the maxilla, in posterior teeth, and when crossbite is present.

## Methodology

- **Design**: retrospective cohort, single orthodontist, single private clinic (Barcelona), Nov 2017–Dec 2023; STROBE-reported.
- **Sample**: 102 screened → 98 analyzed (4 excluded for poor compliance), 720 tooth pairs. Adults >18 y, both arches, no extractions, first refinement present. Sample size adjusted for 3-level clustering (target n=98).
- **Aligner**: Invisalign SmartTrack (Lite/Moderate/Comprehensive); wear 10 days (Lite/Moderate) or 7 days (Comprehensive).
- **Outcome**: absolute difference (mm) between ClinCheck-predicted and achieved arch width at canines, 1st/2nd premolars, 1st molars, from the ClinCheck arch-width table.
- **Analysis**: univariate GLMM per covariate; multivariate GLMM (forced entry; covariates with univariate p<0.30 + arch×tooth interaction). Attachment count excluded from the multivariate model for co-linearity with crossbite.

## Results

- **Overall accuracy**: absolute difference 0.92 mm (95%CI 0.86–0.99). Underexpansion in 72.2%; overcorrection in 22.78% (95%CI 19.86–25.98), concentrated in the mandible (130/164 overcorrections; ~79% mandibular).
- **Arch-level absolute discrepancy**: Maxilla 1.24 mm vs Mandible 0.61 mm.
- **Tooth-level absolute discrepancy (maxilla / mandible, mm)**: canine 0.90 / 0.36; 1st premolar 1.29 / 0.69; 2nd premolar 1.44 / 0.67; 1st molar 1.37 / 0.78.
- **Multivariate GLMM — adjusted coefficients (mm of added discrepancy)**:

| Predictor | Coefficient (95%CI) | p |
|---|---|---|
| Maxilla (vs mandible) | +0.47 (0.35–0.59) | <0.001 |
| Crossbite, unilateral | +0.26 (0.08–0.45) | <0.001 |
| Crossbite, bilateral | +0.55 (0.20–0.90) | <0.001 |
| 1st premolar (vs canine) | +0.22 (0.10–0.35) | <0.001 |
| 2nd premolar (vs canine) | +0.29 (0.20–0.39) | <0.001 |
| 1st molar (vs canine) | +0.45 (0.32–0.57) | <0.001 |
| Predicted expansion (per mm) | +0.14 (0.10–0.19) | <0.001 |

- Arch × tooth-type interaction NOT significant (F[3,709]=1.43, p=0.233).
- **No significant association** with predictability: age, treatment modality, compliance (good vs excellent), number of implants, number of missing teeth, IPR/stripping, treatment duration. (Sex and attachment count were univariate-significant but not in the final adjusted model — attachments via co-linearity with crossbite.)
- **Clinical translation**: each aligner delivers ~0.25–0.33 mm of movement, so larger planned expansions require more aligners and accumulate larger discrepancies. In adults needing >7 mm of expansion, the authors point to SARPE, mini-implant-assisted maxillary expansion (MARPE), or segmental osteotomies rather than relying on aligner overexpansion.

## Related Papers

- [[orthodontics/clear-aligner/fonseca-planells-2026-clear-aligner-maxillary-expansion-growing]] — aligner maxillary expansion in growing patients (orthopedic potential); this adult-only cohort extends it by isolating the clinical factors that degrade expansion in adults (purely dental tipping).
- [[orthodontics/clear-aligner/yassir-2022-cat-vs-fat-overview-systematic-reviews]] — overview of clear-aligner vs fixed-appliance evidence; contextualizes aligners' known weakness at transverse/bodily movements.
- [[orthodontics/clear-aligner/nucera-2022-composite-attachments-clear-aligners-sr]] — attachments and force control, relevant to the attachment-count/crossbite co-linearity noted here.
- [[orthodontics/clear-aligner/inchingolo-2023-clear-aligner-distalization-predictability-sr]] — predictability of a different aligner movement (distalization), parallel methodology theme.
