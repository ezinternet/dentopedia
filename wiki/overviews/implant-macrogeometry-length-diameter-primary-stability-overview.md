---
title: "Implant Macrogeometry (Length · Diameter · Insertion Torque) → Primary Stability / ISQ — Determinant Synthesis"
authors: Synthesis (Damian Lee)
year: 2026
date: 2026-10-20
doi: N/A
source: N/A
category: overviews
evidence_level: synthesis
pdf_path: N/A
pdf_filename: N/A
source_collection: synthesis
tags: [isq, primary-stability, implant-diameter, implant-length, insertion-torque, macrogeometry, rfa, fea, bone-quality, overview]
source_wiki:
  - wiki/implants/isq/barikani-2013-implant-length-diameter-primary-stability.md
  - wiki/implants/isq/gomez-polo-2016-length-diameter-bone-quality-stability.md
  - wiki/implants/isq/huang-2016-influencing-factors-implant-stability-quotient.md
  - wiki/implants/isq/quesada-garcia-2012-implant-diameter-localization-prgf-stability.md
  - wiki/implants/isq/de-elio-2023-insertion-torque-resonance-frequency-tapered-parallel-implants.md
  - wiki/implants/short-narrow/kavitha-2023-outcome-implant-diameter-length-distribution.md
  - wiki/implants/sahoo-2024-finite-element-analysis-influence-implant.md
  - wiki/implants/singh-2024-influence-implant-design-length-stress.md
relations:
  - type: extends
    target: implants-isq-stability-ladder
  - type: refines
    target: huang-2016-influencing-factors-implant-stability-quotient
  - type: refines
    target: gomez-polo-2016-length-diameter-bone-quality-stability
  - type: refines
    target: barikani-2013-implant-length-diameter-primary-stability
---

## 한국어 핵심요약

> [!summary] 한국어 핵심요약
> - 이 페이지는 "임플란트 길이와 직경 중 무엇이 1차 안정성(primary stability)·임플란트 안정성 지수(Implant Stability Quotient, ISQ)를 더 좌우하는가"를 8편(임상 RFA 4 + 체외/유한요소분석 FEA 4)으로 종합한 determinant 페이지다.
> - **핵심 결론**: 임상 근거는 **직경 > 길이**로 수렴한다. 직경은 이를 검증한 모든 임상연구에서 유의(좁을수록 나쁨)했고, 길이는 반복적으로 무의(non-significant)이거나 저밀도골에서만 유의했다.
> - **직경**: Gómez-Polo 2016 — 3.75mm 대비 4.25mm에서 삽입토크(Insertion Torque, IT) 26.5→33.8 N/cm (p=.002); Huang 2016 다변량 회귀에서 직경이 T2(2차) ISQ의 최강 예측인자 (β=0.414); Quesah-García 2012 — 좁은 직경일수록 12주 ISQ 유의하게 낮음 (P<.001).
> - **길이**: Gómez-Polo·Huang에서 길이는 ISQ에 유의한 영향 없음. Barikani 2013 — 길이 효과는 **연질골(D3)에서만** 발현(예: D3에서 13 vs 10mm p=.005), 치밀골(D1)에서는 무의(p=.785).
> - **골질(bone quality)이 1차 안정성의 1차 인자**: 치밀골이 훨씬 높은 ISQ/IT 산출 (Barikani D1≫D3 p≤0.001; Gómez-Polo type 1+2 IT 34.9 vs type 4 20.6 N/cm). 단 이 효과는 2차(골유착) 시점엔 소멸 (Gómez-Polo 2차 ISQ 골질 무의; Huang 골질 양 시점 모두 무의).
> - **임상 vs FEA 충돌**: FEA는 갈린다 — Singh 2024는 저밀도(D4) 골에서 10mm 긴 임플란트가 계면 응력을 크게 낮춤(step design 188→35 MPa)을 보이나, Kavitha 2023은 one-piece 즉시부하 모델에서 12mm가 오히려 경부 응력을 소폭 증가시킴을 보임. 길이–응력 관계는 **디자인·골밀도·길이 범위에 따라 방향이 뒤집힌다.**
> - **삽입토크·기기 caveat**: de-Elío 2023 — 겉보기 macro-design/IT 차이가 실은 최종 드릴 직경 차이의 artifact일 수 있고, **Osstell vs Penguin RFA 값은 상호 호환 불가**(P<.001). 서로 다른 RFA 기기 수치를 직접 비교 금지.
> - **IT ≠ 2차 안정성**: Gómez-Polo — IT는 1차 ISQ와 상관(r=0.56)하나 2차 ISQ와는 무상관(r=0.14, NS). IT를 골유착 예측 지표로 오용 금지.
> - **임상 함의**: 저밀도골·상악에서는 (a) 좁은 직경 회피, (b) 필요 시 길이 확보(연질골 한정 효과), (c) tapered/피질골 고정으로 1차 안정성 보강. 치밀골에서는 길이 증가로 얻는 이득 거의 없음.
> - 이 페이지는 [[overviews/implants-isq-stability-ladder]]의 "영향 변수" 축을 macrogeometry 관점에서 심화한 것 — 측정 도구·부하 임계값 결정은 ladder 및 [[overviews/isq-loading-threshold]] 참조.
> - 근거등급: 임상 RFA 4편(전향/후향/체외) + FEA 4편 (+2026-10-20 보강 4편) — 결론(직경>길이)은 임상 [확인], 절대 응력 수치는 FEA 모델 상대값이라 임상 임계값 아님.
> - 2026-10-20 보강: 체계적 문헌고찰 (Systematic Review, SR; 유한요소해석 40편, Qiu 2024) — 직경이 피질골 응력·치조정 과부하를 좌우하고 길이는 해면골 응력 (D3/D4에서 길이 효과 증가); 테이퍼가 정규화 식립 토크 (Insertion Torque, IT)를 지배, 직경은 원시 IT에 더 기여 (Yang 2024, in vitro); 50 Ncm 초과 토크는 ISQ 이득 없이 실패·나사풀림만 집중 (Baldi 2018, 테이퍼 칼날나사); 골수준 vs 조직수준 임플란트는 1차 안정성 차이 없음 (Elkattan 2026, 파일럿 RCT). [확인]

## Three-line Summary

Determinant synthesis of 8 core papers (4 clinical/RFA + 4 in-vitro/FEA; plus 4 added 2026-10-20: Qiu SR, Yang, Baldi, Elkattan) on whether implant diameter or length governs primary stability/ISQ: across every clinical study that tested it, **diameter is the significant driver (narrower = worse) while length is repeatedly non-significant** or significant only in soft bone — Gómez-Polo 2016 (n=88 implants) IT 26.5→33.8 N/cm for 3.75→4.25 mm (p=.002); Huang 2016 (n=329) diameter the strongest secondary-ISQ predictor (β=0.414); Quesada-García 2012 (n=235) narrow diameter → lower 12-week ISQ (P<.001); Barikani 2013 length effect present only in D3 bone.

Bone quality is the first-order determinant of primary/mechanical stability (dense bone yields much higher ISQ/IT: Barikani D1≫D3 p≤0.001; Gómez-Polo type 1+2 IT 34.9 vs type 4 20.6 N/cm) but its influence fades by the osseointegrated timepoint (Gómez-Polo secondary-ISQ bone effect NS; Huang bone type NS at both times); insertion torque correlates with primary ISQ (r=0.56) but not secondary ISQ (r=0.14, NS) — IT is not a proxy for osseointegration.

The clinical "diameter-dominant, length-minor" pattern conflicts with FEA, which itself splits — Singh 2024 finds longer 10 mm implants markedly reduce interface stress in D4 bone (step design 188→35 MPa) whereas Kavitha 2023 finds longer 12 mm implants slightly *increase* neck stress in a one-piece immediate-load model — so the length↔stress relationship inverts with design, bone density, and length range; de-Elío 2023 further warns apparent macrogeometry/IT gaps can be a drill-diameter artifact and that Osstell vs Penguin RFA readings are not interchangeable (P<.001).

## 세줄요약

임플란트 직경 vs 길이가 1차 안정성/ISQ를 좌우하는지 종합한 8편(임상 RFA 4 + 체외/FEA 4): 이를 검증한 모든 임상연구에서 **직경이 유의한 결정인자(좁을수록 나쁨), 길이는 반복적으로 무의**이거나 연질골에서만 유의 — Gómez-Polo 2016(n=88) IT 26.5→33.8 N/cm(3.75→4.25mm, p=.002); Huang 2016(n=329) 직경이 2차 ISQ 최강 예측인자(β=0.414); Quesada-García 2012(n=235) 좁은 직경→12주 ISQ 저하(P<.001); Barikani 2013 길이 효과는 D3 연질골 한정.

골질이 1차 안정성의 1차 결정인자(치밀골이 훨씬 높은 ISQ/IT)이나 골유착 시점엔 소멸; 삽입토크(IT)는 1차 ISQ와 상관(r=0.56)하나 2차 ISQ와는 무상관(r=0.14, NS) — IT는 골유착 예측 지표가 아님.

임상의 "직경 우세·길이 미미" 패턴은 FEA와 충돌하며 FEA끼리도 갈림 — Singh 2024는 D4골에서 10mm가 응력을 크게 낮추나(188→35 MPa) Kavitha 2023은 12mm가 경부 응력을 소폭 증가시킴; 길이–응력 관계는 디자인·골밀도에 따라 방향이 뒤집힘. de-Elío 2023은 겉보기 macro-design/IT 차이가 드릴 직경 artifact일 수 있고 Osstell·Penguin RFA 값은 호환 불가(P<.001)임을 경고.

## Summary

This page answers one recurring chairside question: **when you can adjust implant length or diameter, which move buys more primary stability?** It synthesizes 8 unsynthesized papers — four clinical/RFA studies that measured ISQ or insertion torque (IT) directly, and four in-vitro/finite-element (FEA) studies that modelled stress and micromotion. It is a *determinant* deep-dive that extends the "influencing variables" axis of [[overviews/implants-isq-stability-ladder]]; it does not restate device selection or loading thresholds (see the ladder and [[overviews/isq-loading-threshold]] for those).

The bottom line: in the clinical evidence **diameter dominates length**, and **bone quality dominates both for the *primary* (mechanical) stability that ISQ captures at placement** — but that bone-quality edge disappears by the secondary (osseointegrated) timepoint. FEA muddies the length story rather than settling it, because the length↔stress relationship reverses depending on implant design, bone density, and the length range tested.

## Key Contributions

### 1. Diameter is the consistent driver; length usually is not

| Study | Design / n | Diameter effect | Length effect |
|---|---|---|---|
| Gómez-Polo 2016 | Prospective, 88 implants / 63 pts | IT 26.5 (3.75) → 33.8 N/cm (4.25 mm), **p=.002**; primary ISQ 75.0→77.0 (p=.043) | **NS** (28.3 vs 30.5 N/cm, p=.361; ISQ NS) over 10–11.5 mm |
| Huang 2016 | Retrospective regression, 329 implants / 177 pts | Significant at both timepoints; **strongest secondary-ISQ predictor β=0.414** | **NS at both T1 and T2** |
| Quesada-García 2012 | Prospective, 235 implants / 93 pts | Narrow diameter → lower 12-wk ISQ (**P<.001**) | Not a significant predictor (abstract-only) |
| Barikani 2013 | In-vitro RFA, 60 implants (D1/D3 blocks) | Narrow platform (3.4 mm) < RP/WP (**p≤.007**); no RP-vs-WP difference | **D3 (soft) bone only** (13 vs 10 mm p=.005–.011); NS in D1 dense bone |

Diameter and insertion torque were the *only* two factors significant at both placement and pre-restoration in Huang's 11-factor model. The diameter benefit at the primary timepoint partly inverts by the secondary timepoint in Gómez-Polo (77.4 vs 75.5, p=.029) — a regression-to-the-mean effect the paper explicitly documents (high primary ISQ drifts down, low drifts up during healing).

### 2. Bone quality is first-order for primary stability — then fades

Dense bone produces markedly higher primary ISQ/IT: Barikani D1 ≫ D3 (p≤.001; e.g. RP-10 mm ISQ 75.2 vs 51.4); Gómez-Polo IT 34.9 (type 1+2) / 27.1 (type 3) / 20.6 N/cm (type 4), P<.001. But this is a *placement-time mechanical* phenomenon: Gómez-Polo's **secondary** (8-week) ISQ shows no bone-type effect (P=.529), and Huang finds Lekholm-Zarb bone type non-significant at both timepoints. Barikani additionally shows bone quality *interacts* with length (length only helps in soft bone) rather than acting as an independent lever.

### 3. Insertion torque is not a proxy for secondary stability

Gómez-Polo: IT ↔ primary ISQ r=0.56 (P<.01, R²≈32%) but IT ↔ secondary ISQ r=0.14 (P=.097, **NS**). High placement torque buys mechanical primary stability, not osseointegration — do not read a high IT as a guarantee of the biological outcome. (This complements the wider ISQ↔IT decoupling documented in the ladder overview.)

The upper end of torque is not benign either: in a multicenter prospective series of tapered knife-edge implants (n=75), the high-torque group (>50 Ncm, mean 68.2) gained no extra ISQ over the moderate group (78.0 vs 75.6), contained both implant failures (IT 77–80 Ncm) and most screw-loosening events, and the IT–ISQ correlation was significant only in the 30–50 Ncm band (ρ=0.481) (Baldi 2018) — a design-specific ceiling, not a universal "more torque is better" rule.

### 4. FEA does not settle the length question — it inverts

The four modelling papers show the length↔stress relationship is design- and bone-dependent, not monotonic:

- **Singh 2024** (2D FEA, D4 posterior maxilla, immediate load): 10 mm implants consistently *lower* interface stress than 6 mm — step design von Mises 188 → 35 MPa (vertical); micromovement 36% lower. Longer is better in soft bone with adequate height.
- **Kavitha 2023** (3D FEA, one-piece immediate-load, homogeneous bone): 12 mm *raised* peak neck stress vs 10 mm (1.76 vs 1.32 MPa); diameter 3.75→4.25 mm negligible (1.77 vs 1.79 MPa). A direct counterexample to "longer/wider = less stress."
- **Sahoo 2024** (in-vitro + FEA): orthogonal — finds **loading direction** (oblique 2.6–3.9× vertical micromotion), not geometry or tilt, dominates micromotion; abutment displacement ≠ micromotion.
- **Qiu 2024** (SR of 40 FEA/in-vitro studies, 2003–2023): diameter governs cortical-bone stress and crestal overloading, length governs cancellous-bone stress; overall diameter dominates, and short wide implants produced lower stress than long narrow ones; length gains more relevance in D3/D4 bone. This is the pooled direction behind items 1–2 of the Results hierarchy and makes Kavitha's "diameter negligible" look like a single-model outlier (homogeneous bone, one-piece design) rather than the rule [미검증: 필자 해석] — but it is a qualitative SR of heterogeneous FEA, so the same model-relative caveat applies.
- **Yang 2024** (3D explicit FEA + in-vitro insertion, polyurethane foam, Ø3.5/4.3 mm, parallel vs tapered): *normalized* insertion torque is dominated by taper (β₂=0.93) while *raw* insertion torque is driven more by diameter (β₁=0.78); taper also extends the compressive stress field further from the thread. This gives a mechanical reason for Results item 3 (tapered bodies raise placement torque) and separates the "diameter" and "taper" levers that clinical series conflate. In vitro, foam model only.
- Absolute MPa in FEA are model-relative (homogeneous, isotropic, linear-elastic assumptions) and are **not** clinical stress thresholds.

### 5. Device and drill-diameter confounds (de-Elío 2023)

In a split-mouth study, parallel implants showed higher IT than tapered (P<.05) — but the design built in a final-drill-diameter difference (3.25 mm parallel vs 3.4 mm tapered), so the apparent "macrogeometry" effect is plausibly a drilling artifact. Between-group ISQ did not differ (P>.05). Critically, **Osstell and Penguin RFA values differed significantly from each other (P<.001) — the two devices are not interchangeable**, reinforcing the ladder's "pick one device and stay on it" rule.

A pilot parallel-group RCT (21 patients, 90 implants) found bone-level vs tissue-level implants of one system had no ITV difference (36.0 vs 38.0 Ncm, p=0.381) or baseline ISQ difference; 90-day horizontal ISQ was marginally higher for tissue-level (66.5 vs 57.1, p=0.029), and ITV correlated with baseline ISQ (r=0.493) but not 90-day ISQ (Elkattan 2026). Platform design therefore does not appear to govern primary stability, and the ITV→secondary-ISQ decoupling in section 3 is reproduced — but the study had no a priori power calculation, so treat it as feasibility-level.

## Methodology

Narrative determinant synthesis (no pooled meta-analysis; heterogeneous designs). Evidence base (original 2026-07 synthesis; 2026-10-20 additions: Qiu 2024 SR, Yang 2024 in vitro/FEA, Baldi 2018 prospective, Elkattan 2026 pilot RCT): 4 clinical (1 in-vitro RFA bench, 2 prospective, 1 retrospective regression) + 4 modelling (2D/3D FEA ± in-vitro). Two clinical sources (de-Elío, Quesada-García) are abstract-only, so directionality is captured but not effect sizes. Numbers are quoted verbatim from each source page; FEA stress magnitudes are reported as within-model relative values only.

## Results

**Practical hierarchy for maximizing primary stability (ISQ at placement):**

1. **Bone quality** — the dominant lever, but you usually cannot change it; you assess it (CBCT / tactile Lekholm-Zarb) and adapt.
2. **Diameter** — the strongest *modifiable* lever: avoid narrow diameters in soft bone / esthetic-zone secondary-stability-critical sites; wider gives higher IT and primary ISQ.
3. **Macro-design / cortical anchorage** — tapered bodies and cortical engagement raise placement torque (see ladder overview).
4. **Length** — a *secondary* lever that mainly helps in **soft (D3/D4) bone**; in dense bone extra length adds little primary stability and, per one FEA model, can even raise neck stress.
5. **Insertion torque** — useful primary-stability readout, but **not** a secondary-stability / osseointegration predictor.

**Do-not:** compare ISQ numbers across different RFA devices; treat FEA MPa values as clinical thresholds; assume "longer = safer" as a universal rule.

## Related Papers

- [[implants/isq/barikani-2013-implant-length-diameter-primary-stability]] — in-vitro RFA; length helps only in soft bone, narrow diameter worst
- [[implants/isq/gomez-polo-2016-length-diameter-bone-quality-stability]] — prospective; diameter+bone drive primary stability, length NS, IT≠secondary stability
- [[implants/isq/huang-2016-influencing-factors-implant-stability-quotient]] — retrospective regression; diameter strongest secondary-ISQ predictor (β=0.414), length/bone NS
- [[implants/isq/quesada-garcia-2012-implant-diameter-localization-prgf-stability]] — prospective; narrow diameter & maxilla → lower 12-wk ISQ
- [[implants/isq/de-elio-2023-insertion-torque-resonance-frequency-tapered-parallel-implants]] — split-mouth; drill-diameter confound, RFA devices not interchangeable
- [[implants/short-narrow/kavitha-2023-outcome-implant-diameter-length-distribution]] — FEA; longer implant slightly raised neck stress, diameter negligible
- [[implants/sahoo-2024-finite-element-analysis-influence-implant]] — FEA; loading direction dominates micromotion, not geometry
- [[implants/singh-2024-influence-implant-design-length-stress]] — FEA; longer implants lower interface stress in D4 bone
- [[implants/qiu-2024-comprehensive-biomechanical-evaluation-length-diameter]] — SR of 40 FEA studies; diameter dominates stress, length matters more in D3/D4 (sr, 2024)
- [[implants/yang-2024-implant-diameter-tapered-stress-insertion]] — in vitro + FEA; taper dominates normalized IT, diameter dominates raw IT (in-vitro, 2024)
- [[implants/isq/baldi-2018-insertion-torque-isq-tapered-knife-edge]] — prospective n=75; >50 Ncm adds no ISQ, all failures in high-torque group (prospective, 2018)
- [[implants/isq/elkattan-2026-insertion-torque-isq-bone-level]] — pilot RCT; bone- vs tissue-level no ITV/baseline-ISQ difference (rct, 2026)

## Related Overviews

- [[overviews/implants-isq-stability-ladder]] — parent: ISQ/RFA measurement · threshold · influencing-variable ladder (this page deepens the macrogeometry variable)
- [[overviews/isq-loading-threshold]] — loading-decision thresholds built on ISQ
- [[overviews/implant-primary-stability-arp-macrogeometry-low-density-overview]] — macrogeometry & low-density-bone primary stability (ARP context)
- [[overviews/implant-length-selection-why-not-always-short]] — length-selection decision (short vs standard)
- [[overviews/narrow-diameter-implants-clinical-outcomes-overview]] — narrow-diameter clinical outcomes
