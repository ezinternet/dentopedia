---
title: "Are arch width measurements from Invisalign arch width tables reliable?"
authors: Cristina de-la-Rosa-Gay, Sofia Valmaseda-de-la-Rosa, Andrea Hernández-Mangas, Octavi Camps-Font, Eduard Valmaseda-Castellón, Rui Figueiredo
year: 2026
date: 2026-05-13
doi: 10.1007/s00784-026-06904-w
source: de-la-rosa-gay-2026-arch-width-measurements-invisalign-tables.md
category: [orthodontics/clear-aligner]
evidence_level: retrospective
source_collection: pubmed-text
full_text: true
pmid: "42126458"
pmcid: "PMC13171758"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13171758/
text_path: /Users/oracleneo/llm-wiki/papers/de-la-rosa-gay-2026-arch-width-measurements-invisalign-tables.txt
text_filename: de-la-rosa-gay-2026-arch-width-measurements-invisalign-tables.txt
tags: [clear-aligner, invisalign, clincheck, arch-width, bland-altman, metrology, geomagic, measurement-validation]
relations:
  - type: refines
    target: de-la-rosa-gay-2025-expansion-predictability-clear-aligner
---

## Three-line Summary

Retrospective method-agreement study (35 adults treated with Invisalign SmartTrack, single orthodontist, Barcelona metropolitan area, Nov 2017–Sep 2025; 126 screened, 35 analyzed) — digital models measured with Geomagic Control X at canines, first/second premolars, and first molars across three ClinCheck timepoints (pretreatment, predicted, pre-first-refinement), yielding 840 paired arch-width measurements.

Mixed-effects Bland–Altman analysis (patient random intercepts, accounting for within-patient clustering, ICC 0.37–0.46) showed narrow bias across reference points: occlusal 0.03 mm (95% LoA −0.78 to +0.84 mm, total variance), cusp +0.21 mm (~−1.0 to +1.5 mm), gingival −0.30 to −0.48 mm (up to ±1.8 mm); the discrepancy variable (observed minus predicted expansion) showed the most stable results with bias closest to zero across all three reference-point sets.

Clinical implication: ClinCheck arch-width table values are metrologically consistent with independent measurement — most reliably at occlusal and cusp references, least at gingival — but this validates the measurement tool, not the aligner's ability to achieve the clinically planned expansion.

## 세줄요약

후향적 측정법-일치도(Method-Agreement) 연구(Invisalign SmartTrack 치료 성인 35명, 단일 교정의, 바르셀로나, 2017.11–2025.9; 126명 선별 중 35명 분석) — 치료 전·ClinCheck 예측·첫 리파인먼트 전 3개 시점의 디지털 모델을 Geomagic Control X로 견치·제1/2소구치·제1대구치에서 측정, 치아궁 폭(Arch Width) 쌍 840개 확보.

혼합효과 일치도 분석(Mixed-Effects Bland-Altman Analysis, 환자별 무작위 절편으로 환자 내 군집 보정, 급내상관계수(Intraclass Correlation Coefficient, ICC) 0.37–0.46)에서 기준점별 편향(bias)이 좁게 나타남: 교합면(Occlusal) 기준 0.03 mm(95% 일치한계(Limits of Agreement, LoA) −0.78~+0.84 mm), 교두(Cusp) 기준 +0.21 mm(약 −1.0~+1.5 mm), 치은(Gingival) 기준 −0.30~−0.48 mm(±1.8 mm까지); 실제확장-예측확장 불일치(Discrepancy) 변수가 세 기준점 모두에서 편향 0에 가장 근접하고 가장 안정적.

임상적 의미: ClinCheck 치아궁 폭 표 수치는 독립 계측과 대체로 일치하며(교합면·교두 기준이 가장 신뢰도 높고 치은 기준이 가장 낮음) — 다만 이는 "측정도구"의 신뢰성 검증이지, 얼라이너가 계획한 확장을 실제로 "달성"한다는 증거는 아니다.

## Summary

This retrospective method-agreement study asks whether the arch-width numbers reported in Invisalign's ClinCheck arch-width tables can be trusted, independent of whether the aligner achieves the planned tooth movement. Digital models from 35 adults treated with Invisalign SmartTrack (single orthodontist, Barcelona metropolitan area, Nov 2017–Sep 2025) were measured with Geomagic Control X metrology software at canines, first/second premolars, and first molars, across three ClinCheck timepoints (pretreatment, predicted, and pre-first-refinement), yielding 840 paired arch-width measurements. Because ClinCheck's internal reference points and centers of rotation cannot be reproduced in external software, the authors compared derived variables instead of raw widths: predicted expansion, observed expansion, and their discrepancy. Non-parametric and mixed-effects Bland–Altman analyses (the latter accounting for within-patient clustering via patient random intercepts, ICC 0.37–0.46) showed narrow bias across all three reference-point sets, with occlusal references — reportedly the point Align Technology uses internally — showing the tightest agreement (bias 0.03 mm; 95% LoA −0.78 to +0.84 mm) and gingival references the widest (LoA up to ±1.8 mm). The authors conclude ClinCheck arch-width tables are metrologically consistent with independent measurement and can be used in research/clinical decision-making without re-measuring STL models by hand, but explicitly caution that this agreement is not proof the aligner achieves the clinically planned expansion, nor validation of Align's proprietary algorithm.

## Key Contributions

- First independent metrology validation of ClinCheck **transverse (arch-width)** table values — prior validation work covered only overjet/overbite.
- Compared three anatomical reference levels (occlusal, cusp, gingival) and ranked their reliability: occlusal ≈ cusp (tight agreement) >> gingival (widest limits of agreement, up to ±1.8 mm).
- Used mixed-effects Bland–Altman modeling with patient-level random intercepts to correctly account for 24 non-independent repeated measurements per patient (ICC 0.37–0.46; design effect 9.6–11.7; effective independent n ≈ 72–88).
- Validated across two separate ClinCheck records (pretreatment→predicted, and pretreatment→pre-refinement/observed), broader in scope than a prior single-timepoint overjet/overbite validation study.
- Isolated a "discrepancy" metric (observed minus predicted expansion) that was the most stable and least biased across all reference points — proposed as a practical benchmark for future digital-planning-tool validation studies.

## Methodology

- **Design**: retrospective cohort / method-agreement (metrology validation) study; STROBE-reported; single orthodontist, single private clinic (Barcelona).
- **Population**: adults ≥18 y, Invisalign SmartTrack, no extractions, both arches treated, first refinement phase present; 126 screened → 35 analyzed (91 excluded).
- **Measurement**: STL digital models (pretreatment, ClinCheck-predicted, pre-first-refinement) imported into Geomagic Control X v2023.3.0; horizontal reference plane through the palatal interproximal papilla between maxillary 1st/2nd molars and the incisive papilla midpoint; arch width measured at canines, 1st/2nd premolars, and 1st molars using three reference points (occlusal, cusp, gingival) per tooth pair; blinded measurer.
- **n**: 840 paired arch-width measurements (35 patients × 8 tooth-pair widths [4 maxillary + 4 mandibular] × 3 timepoints = 24 repeated measurements per patient).
- **Statistics**: Shapiro–Wilk normality testing → non-parametric Bland–Altman (median bias, 2.5th/97.5th percentile limits of agreement, bootstrap 95% CI, 2000 iterations) plus mixed-effects Bland–Altman models with patient-specific random intercepts to partition between- and within-patient variance; test–retest reliability re-check in 10 randomly selected cases after ≥15 days (ICC 0.989–0.997).

## Results

| Reference point | Outcome variable | Bias (mixed-effects BA) | 95% Limits of Agreement |
|---|---|---|---|
| Occlusal | pooled (predicted/observed expansion, discrepancy) | 0.03 mm | −0.78 to +0.84 mm (total variance); −0.74 to +0.81 mm (within-patient variance) |
| Cusp | predicted & observed expansion | +0.21 mm | approximately −1.0 to +1.5 mm |
| Gingival | predicted expansion | −0.30 mm | up to ±1.8 mm |
| Gingival | observed expansion | −0.48 mm | up to ±1.8 mm |
| Gingival | discrepancy | −0.18 mm | up to ±1.8 mm |

Non-parametric Bland–Altman analysis (individual-measurement level, not clustering-adjusted) showed the same ordering: occlusal and cusp LoA within approximately ±1 mm, gingival LoA up to ±1.8 mm; the discrepancy variable produced the narrowest ranges and bias closest to zero across all three reference-point sets, supporting its use as the most stable metric for future digital-planning validation work.

## Related Papers

- [[orthodontics/clear-aligner/de-la-rosa-gay-2025-expansion-predictability-clear-aligner]] — same first author/clinic; that retrospective GLMM study quantified clinical arch-expansion predictability (0.92 mm mean absolute planned-vs-achieved discrepancy, worse in the maxilla/posterior teeth/crossbite) using arch-width values read directly off the ClinCheck arch-width table. This paper validates the measurement instrument behind those numbers rather than the aligner's clinical performance; because the mixed-effects LoA reported here (up to ±0.84 mm at occlusal, wider at cusp/gingival) is of comparable magnitude to the 0.92 mm discrepancy reported in 2025, part of that clinical discrepancy could plausibly reflect measurement-tool variability rather than pure biological/mechanical under-expansion — a qualification (`refines`) of how tightly the 2025 discrepancy estimate should be read, not a contradiction of it.
- [[orthodontics/clear-aligner/fonseca-planells-2026-clear-aligner-maxillary-expansion-growing]] — different population (growing/mixed-dentition) and different question (aligner vs. conventional-expander efficacy via SR+MA); included here only as adjacent clear-aligner transverse-expansion literature, not a direct methodological match to this measurement-validation study.
