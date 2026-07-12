---
title: "Harnessing AI in prosthodontics and implant dentistry: An umbrella review of systematic evidence"
authors: Alfaraj A, Limones Á, Ahmad S, Aljubairah F, Albalawi S, Albesher M, Alghamdei B, Lin WS
year: 2026
date: 2026-01-01
doi: 10.1111/jopr.70091
source: alfaraj-2026-harnessing-ai-prosthodontics-implant-dentistry.md
category: [artificial-intelligence]
confidence: sr
pdf_path: /Users/oracleneo/llm-wiki/papers/alfaraj-2026-harnessing-ai-prosthodontics-implant-dentistry.pdf
pdf_filename: alfaraj-2026-harnessing-ai-prosthodontics-implant-dentistry.pdf
source_collection: external
tags: [artificial-intelligence, deep-learning, convolutional-neural-network, implant-identification, prosthodontics, umbrella-review, AMSTAR-2]
relations:
  - type: extends
    target: revilla-leon-2021-artificial-intelligence-implant-dentistry-sr
  - type: reinforces
    target: garg-2026-artificial-intelligence-pediatric-dentistry-umbrella-review
---

## Three-line Summary

Umbrella review (PROSPERO CRD420251067048; 11 systematic reviews, 261 unique primary studies, 5 databases 2018–2025) synthesizing AI applications in prosthodontics and implant dentistry, quality-appraised with AMSTAR-2 and overlap-quantified via CCA (overall 0.77%).

AI achieved ~95.6% pooled accuracy for implant-type identification on radiographs and 90.6–97.4% for preparation-margin detection, but only 62.4–80.5% for multivariable implant-prognosis prediction; caries/fracture detection reached ~82–89%.

Only 4/11 (36%) contributing SRs were AMSTAR-2 "high" quality (55% critically low), so image-recognition/segmentation tasks are the most clinically mature AI use case while outcome-prediction and routine adoption still need prospective, multi-center validation.

## 세줄요약

엄브렐러 리뷰(PROSPERO CRD420251067048; 11편 체계적 문헌고찰(SR), 고유 1차 연구 261편, 5개 데이터베이스 2018–2025)로 보철·임플란트 치의학 인공지능(Artificial Intelligence, AI) 적용을 종합; AMSTAR-2 질 평가 + 중복보정면적(Corrected Covered Area, CCA) 전체 0.77%.

방사선 사진 임플란트 종류 식별 풀링 정확도 ~95.6%, 지대치 변연 탐지 90.6–97.4%이나, 다변량 임플란트 예후 예측은 정확도 62.4–80.5%에 그침; 우식·파절 탐지는 ~82–89%.

11편 중 4편(36%)만 AMSTAR-2 "높음" 등급(55% critically low)이므로 영상인식·분할 과제가 가장 임상 성숙도가 높고, 예후 예측·일상 진료 도입은 추가 전향적·다기관 검증이 필요함.

## Summary

This umbrella review (PRIOR 2022-guided, PROSPERO CRD420251067048) synthesized 11 systematic reviews (261 unique primary studies) on artificial intelligence (AI) in prosthodontics and implant dentistry, searched across PubMed, Scopus, Web of Science, Embase, and Cochrane (2018–2025). Because outcome metrics were too heterogeneous for cross-review meta-analysis, findings were synthesized descriptively and organized by clinical task, with a 3-level clinical-readiness rating (high/moderate/emerging) assigned per task. AI performed best on well-defined image-recognition and segmentation tasks — implant-type identification on radiographs (~92.6–95.6% pooled accuracy, up to 99–100% sensitivity for top CNN models), CBCT-based anatomic segmentation of mandibular canal/maxillary sinus, and mandibular edentulous-site detection (96% accuracy) — and more modestly on prosthodontic preparation-margin detection (90.6–97.4%) and caries/fracture detection (~82–89%). Performance was weaker and more variable for multivariable implant-prognosis prediction from patient/biomechanical data (62.4–80.5% accuracy) and maxillary edentulous-site detection (83%). Methodological quality of the 11 contributing SRs was mixed: only 36% (4/11) were AMSTAR-2 "high," while 55% were "critically low," predominantly due to missing protocol pre-registration (only 36% registered) and absent excluded-study lists (91% lacked one). The authors conclude AI is a promising adjunct for radiographic diagnostics and CBCT-based planning but caution that most evidence derives from retrospective, idealized, single-center datasets, so routine clinical adoption should await prospective, standardized, multi-center validation.

## Key Contributions
- Joint umbrella synthesis spanning both general prosthodontics and implant dentistry (previously covered only by separate, narrower SRs).
- 3-level clinical-readiness scale (high/moderate/emerging) mapping best-reported performance + evidence maturity onto a clinically interpretable judgment per AI task (Table 4).
- AMSTAR-2 quality profile across the field: 36% high / 9% low / 55% critically low, with universal (100%) failure to report primary-study funding and near-universal (91%) failure to list excluded studies — a field-level red flag for evidence trustworthiness.
- Corrected covered area (CCA) analysis shows minimal primary-study duplication across the 11 SRs (overall CCA = 0.77%), meaning the convergent accuracy findings for implant identification reflect independent replication rather than the same studies being re-counted.

## Methodology
- **Design**: Umbrella review (overview of systematic reviews), PRIOR 2022 reporting, PROSPERO CRD420251067048.
- **Databases**: PubMed, Scopus, Web of Science, Embase, Cochrane Library; search April 2025; SRs published 2018–2025, English only.
- **Selection**: 207 records → 186 after dedup → 21 full-text reviewed → 11 SRs included (193 studies in main analyses; 281 primary-study citations; 261 unique primary studies).
- **Quality appraisal**: AMSTAR-2, two independent raters + third-reviewer arbitration.
- **Overlap**: Corrected covered area (CCA), overall and task-level.
- **Synthesis**: Descriptive/narrative by review (Table 3) and by clinical task (Table 4); no cross-review meta-analysis performed.

## Results

| Clinical task | Best-reported performance | Clinical readiness |
|---|---|---|
| Implant-type identification (radiograph, CNN) | 92.56–95.6% pooled accuracy; top models 99.08–100% sensitivity | High |
| Edentulous-site detection, mandible | 96% accuracy | High |
| Edentulous-site detection, maxilla | 83% accuracy | Moderate |
| CBCT anatomic segmentation (mandibular canal, maxillary sinus) | ~77% accuracy to ~99% precision; up to 116× faster than manual | High |
| Preparation-margin (finish-line) detection | 90.6–97.4% accuracy | High |
| Caries/fracture detection (general prosthodontics) | ~82–89% accuracy | Moderate |
| Peri-implant radiolucency detection | ≥78.6% accuracy | Moderate |
| Implant failure/peri-implantitis prediction (radiographic) | Up to 99.8% accuracy; sens 67–95%, spec 78–100% | Moderate |
| Implant prognosis prediction (patient/biomechanical data) | 62.4–80.5% accuracy | Emerging |
| Implant design optimization (AI + FEA) | Up to 36.6% stress reduction at bone–implant interface | Emerging |
| AMSTAR-2 quality of 11 contributing SRs | 36% high, 9% low, 55% critically low | — |

## Related Papers
- [[digital-workflow/revilla-leon-2021-artificial-intelligence-implant-dentistry-sr]] — one of the 11 primary systematic reviews synthesized here (implant type recognition/success prediction/design optimization); this umbrella review *extends* it by contextualizing its findings within the broader AI-in-prosthodontics evidence base and AMSTAR-2 quality landscape.
- [[artificial-intelligence/garg-2026-artificial-intelligence-pediatric-dentistry-umbrella-review]] — sibling AMSTAR-2 + CCA umbrella review applied to pediatric dentistry; *reinforces* this paper's headline pattern (strong image-task performance, weak underlying SR quality) in an independent population.
- [[overviews/ai-dentistry-reviews-2024-2025-synthesis]] — cross-paper AI-in-dentistry synthesis this page can be woven into (implant/prosthodontics cluster).
