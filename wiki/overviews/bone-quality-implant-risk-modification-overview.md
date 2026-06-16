---
title: "Bone Quality → Implant Risk & Modification Overview (골질·골밀도별 임플란트 위험·수정전략)"
authors: synthesis (llm-wiki)
year: 2026
date: 2026-06-09
doi: N/A
source: synthesis
category: [overviews]
confidence: synthesis
pdf_path: N/A
pdf_filename: N/A
source_collection: synthesis
tags: [bone-quality, bone-density, lekholm-zarb, misch-d1-d4, type-iv-bone, primary-stability, osteoporosis, osteosclerosis, low-density-bone, overview]
source_papers:
  - wiki/implants/rosa-2024-do-dental-implants-bone-types.md
  - wiki/implants/raghavan-2025-bone-density-implant-dentistry-review.md
  - wiki/implants/di-stefano-2021-stability-dental-implants-cortical-bone.md
  - wiki/implants/premnath-2012-stress-distribution-bone-density-fea.md
  - wiki/implants/isq/stoilov-2023-macrodesign-length-diameter-bone-quality-isq.md
  - wiki/implants/isq/chatvaratthana-2017-cortical-bone-thickness-isq-cbct.md
  - wiki/implants/isq/canullo-2024-bioactive-surface-poor-bone-isq-stability.md
  - wiki/implants/mello-machado-2021-osseodensification-low-quality-bone-rct.md
  - wiki/implants/munjal-2015-implants-low-density-bone-d3d4.md
  - wiki/implants/kim-2026-dental-implant-osteoporosis-osteosclerosis.md
relations:
  - type: extends
    target: rosa-2024-do-dental-implants-bone-types
  - type: reinforces
    target: raghavan-2025-bone-density-implant-dentistry-review
---

## 한국어 핵심요약

> [!summary] 한국어 핵심요약
> - 핵심 명제: 골질(Bone Quality)을 하나의 술식이 아니라 "위험 축"으로 묶어, "이 골질이면 실패 위험이 얼마이고 무엇을 수정할 것인가"에 답하는 종합 페이지.
> - 국소 골밀도(Lekholm-Zarb I~IV / Misch D1~D4)가 초기 안정성과 실패 위험을 결정 — type IV(저밀도·얇은 피질·상악 구치부)는 ~1.5~1.9배 더 실패(Rosa 2024 SR+MA, 49편·29,905 임플란트).
> - ISQ 밴드: type IV 58~65 vs type I 72~80; type I=II 동등, type III는 중간.
> - 안정성은 피질골 맞물림 현상 — 치조정 피질골 두께(Crestal Cortical Thickness)가 가장 강한 ISQ 예측인자이며, 깊은 해면골(6~9mm)은 얇은 피질을 대체하지 못함(Chatvaratthana 2017, Di Stefano 2021).
> - 연질골 수정 레버(stackable): 언더드릴링/골밀도화(Osseodensification, OD), 테이퍼 매크로디자인, 길이보다 직경(Diameter > Length), 생체활성·친수성 표면, 지연 부하 — 연질골일수록 매크로디자인 차이는 줄고 드릴링 프로토콜이 더 중요(Stoilov 2023).
> - OD는 삽입 토크(Insertion Torque, IT)를 올리지만(39 vs 32 Ncm) ISQ·6개월 생존은 동등 — 생존 업그레이드가 아닌 안정성 보존 옵션(Mello-Machado 2021 RCT, n=16).
> - 표면 레버: 연질골에서 생체활성 표면이 T30/T45 ISQ dip을 제거해 45일 부하 가능(Canullo 2024).
> - 부하 결정: 얇은 치조정 피질·낮은 ISQ → 지연 부하 기본; ISQ < ~65에서 조기 부하 강행 금지.
> - 전신·병적 골은 같은 축의 시간·생물학적 확장: 골다공증(Osteoporosis)은 단기 생존은 건강군과 유사하나 장기 82.6~94.1%(5~10년)로 감소; 골경화성 병변은 과열·병변내 실패 위험 추가(Kim 2026).
> - 주의 충돌: FEA(응력)는 D3/D4에서 실린더형을 선호하나 임상(초기 안정성)은 테이퍼형 선호 — 미해결 쟁점.
> - 임상 정리: 골다공증 = 높은 임플란트 실패라는 통념은 틀림; 위험은 장기·골질 기반이며 약물(MRONJ) 위험과 분리해서 봐야 함.

## One-line Summary

Synthesis organizing bone quality as the *risk axis* (not a procedure): local density (Lekholm-Zarb I–IV / Misch D1–D4) sets primary-stability and failure risk — type IV bone fails ~1.5–1.9× more (ISQ 58–65 vs 72–80 for type I) — and crestal cortical thickness, not cancellous volume, is the dominant stability driver; the modification levers are drilling protocol, implant macro-design, surface, and loading timing, while systemic/pathologic bone (osteoporosis, osteosclerotic lesions) extends the same axis with long-term and lesion-specific caveats.

## 한줄요약

골질을 "위험 축"으로 묶은 종합. 국소 골밀도(Lekholm-Zarb I–IV / Misch D1–D4)가 초기 안정성·실패 위험을 결정하고(type IV는 ~1.5–1.9배 실패, ISQ 58–65 vs type I 72–80), 해면골 양보다 **치조정 피질골 두께**가 안정성의 핵심이다. 수정 레버는 드릴링 프로토콜·매크로디자인·표면·부하 시기이며, 전신/병적 골(골다공증·골경화성 병변)은 같은 축의 장기·병변별 단서로 확장된다.

## Thesis

The clinical question this page answers: **"Given this bone quality, what is the failure risk and what should I modify?"** Three companion overviews touch bone but answer different questions — [[overviews/osseodensification-clinical-applications]] is one *solution* (a drilling technique), [[overviews/implants-isq-stability-ladder]] is the *measurement* layer, and [[overviews/drug-mronj-antiresorptive-overview]] is the *drug* layer. None synthesizes bone quality itself as the problem axis. This page does, then connects each tier to its modification levers.

Best-evidence bottom line:

1. **Type IV (low-density, thin cortical, posterior maxilla) is an independent failure risk factor; types I/II are equivalent and type III intermediate.** — Rosa 2024 SR+MA (49 studies, 29,905 implants). [근거강함]
2. **Stability is a cortical-engagement phenomenon: crestal cortical thickness is the strongest ISQ predictor; deep cancellous bone does not substitute.** — Chatvaratthana 2017 (CBCT prospective), Di Stefano 2021 SR (13 studies). [합의수준]
3. **In soft bone the modification levers (under-drilling, tapered macro-design, diameter > length, osseodensification, bioactive surface, delayed loading) converge toward preserving/creating primary stability** — and macro-design differences attenuate in soft foam, so drilling protocol matters *more*, not less. — Stoilov 2023, Premnath 2012, Mello-Machado 2021, Canullo 2024. [합의수준~claude해석]
4. **Systemic and pathologic bone is the same axis extended in time and biology**: osteoporosis is healthy-comparable short-term but declines long-term (82.6–94.1% at 5–10y); osteosclerotic lesions add overheating/intralesional-failure risk. — Kim 2026 narrative review. [합의수준]

## Evidence Map

| Paper | Design | Bone-quality role | Key finding | Confidence |
|---|---|---|---|---|
| [[implants/rosa-2024-do-dental-implants-bone-types]] | sr+ma (49 studies, 29,905 impl) | Risk stratification (Lekholm-Zarb) | Type IV ↓ survival (~1.5–1.9× failure); I=II; ISQ IV 58–65 vs I 72–80 | [근거강함] |
| [[implants/di-stefano-2021-stability-dental-implants-cortical-bone]] | sr (13 studies) | Cortical thickness → stability | Thicker cortex → ↑ISQ/IT; bicortical = highest; MBL link inconclusive | [합의수준] |
| [[implants/isq/chatvaratthana-2017-cortical-bone-thickness-isq-cbct]] | prospective | Pre-op predictor | Crestal cortical thickness = strongest ISQ predictor; thin cortex → plan delayed loading | [합의수준] |
| [[implants/raghavan-2025-bone-density-implant-dentistry-review]] | narrative | Classification + protocol map | Misch D1–D4, CBCT HU; under-drill D3/D4, modify healing, design selection | [합의수준] |
| [[implants/isq/stoilov-2023-macrodesign-length-diameter-bone-quality-isq]] | in-vitro | Macro-design × density | Diameter > length for ISQ; tapered superior; soft bone → drilling protocol critical | [claude해석] |
| [[implants/premnath-2012-stress-distribution-bone-density-fea]] | in-vitro (FEA) | Stress × density | Peak stress at crestal neck; D3/D4 favors cylindrical; threaded > cylindrical stress | [claude해석] |
| [[implants/mello-machado-2021-osseodensification-low-quality-bone-rct]] | rct (16 pts/55 impl) | Soft-bone drilling lever | OD vs conventional: IT 39 vs 32 Ncm (p<.001), ISQ equivalent, survival equal at 6mo | [근거강함(소표본)] |
| [[implants/isq/canullo-2024-bioactive-surface-poor-bone-isq-stability]] | prospective | Soft-bone surface lever | In poor bone, bioactive surface avoids the T30/T45 ISQ dip → enables 45-day loading | [합의수준] |
| [[implants/munjal-2015-implants-low-density-bone-d3d4]] | prospective (n=14) | D3/D4 outcome | 92.3% survival at 12mo, MBL not significant | [claude해석(소표본)] |
| [[implants/kim-2026-dental-implant-osteoporosis-osteosclerosis]] | narrative-review (30 studies) | Systemic/pathologic extension | Osteoporosis short 97.9–100% → long 82.6–94.1%; sclerotic lesion-dependent | [합의수준] |

## Reference — two classifications in use

| Misch | Lekholm-Zarb | Description | Typical ISQ | Typical site |
|---|---|---|---|---|
| D1 | (I) | Dense homogeneous cortical | 72–80 | Anterior mandible |
| D2 | II | Thick cortical + dense trabecular | 72–75 | Anterior jaw / posterior mandible |
| D3 | III | Thin cortical + fine trabecular | 70–75 | Anterior maxilla / posterior mandible |
| D4 | IV | Thin cortical + sparse trabecular | 58–65 | **Posterior maxilla** |

ISQ bands from Rosa 2024; the two systems are not a perfect 1:1 map (Misch is density/HU-oriented, Lekholm-Zarb is cortical/trabecular morphology) — use whichever the source uses and do not over-convert. [claude해석]

## Clinical Decision Points — modification ladder by tier

**Dense bone (D1 / type I–II)**
- Risk: overheating during osteotomy, stress-shielding, low vascularity. Premnath FEA: highest crestal stress with threaded design.
- Modify: full (or slightly under-) drilling is *not* needed — avoid over-compression; copious irrigation, sharp drills, consider two-stage to manage heat. Survival is the reference standard (I = II). [합의수준]

**Intermediate (D3 / type III)**
- Risk: moderate primary-stability shortfall.
- Modify: tapered design, slight under-preparation, ISQ check before deciding loading timing. [합의수준]

**Soft bone (D4 / type IV — posterior maxilla)** — the high-risk tier
- Risk: low primary stability, ~1.5–1.9× failure (Rosa 2024); thin crestal cortex predicts low ISQ (Chatvaratthana 2017).
- Modify (stackable levers):
  - *Drilling*: under-preparation / osseodensification — Mello-Machado RCT shows OD raises IT (39 vs 32 Ncm) with equivalent ISQ and 6-mo survival; macro-design differences attenuate in soft bone, so protocol dominates (Stoilov 2023).
  - *Macro-design*: tapered, prioritize **diameter over length** (Stoilov 2023). FEA favors cylindrical for stress in D3/D4 (Premnath 2012) — note this conflicts with the clinical primary-stability preference for tapered; FEA optimizes stress distribution, clinical data optimizes initial fixation. [claude해석/미검증]
  - *Surface*: bioactive/hydrophilic surface avoids the early ISQ dip and can permit 45-day loading (Canullo 2024).
  - *Loading*: thin crestal cortex / low ISQ → default to delayed loading; do not force early loading on ISQ < ~65 (cross-ref [[overviews/implants-isq-stability-ladder]]).

**Systemic / pathologic bone (extends the axis)**
- *Osteoporosis* (systemic low turnover/density): short-term survival healthy-comparable but long-term decline to 82.6–94.1% (5–10y) with greater MBL → long-term follow-up is the lever; oral bisphosphonates not a contraindication, drug holiday only high-risk (see [[overviews/drug-mronj-antiresorptive-overview]]). [합의수준]
- *Osteosclerotic lesions* (focal high density): overheating + intralesional-placement failure; florid COD 66.7% vs localized 100%; condensing osteitis / idiopathic osteosclerosis OK when stable; cementoblastoma needs resection first; hypercementosis fails on residual tissue (Kim 2026). Two-stage placement + careful drilling. [합의수준]

## Misconception patterns

- "More cancellous bone depth compensates for thin cortex." — No: 6–9 mm deep cancellous bone does not substitute for crestal cortical engagement (Chatvaratthana 2017). [합의수준]
- "Longer implant fixes soft bone." — Diameter beats length for ISQ in soft bone (Stoilov 2023). [claude해석]
- "Osseodensification guarantees better outcomes in D4." — It raises insertion torque, but ISQ (more correlated with osseointegration) was equal to conventional; survival equal at 6 mo on a 16-patient RCT (Mello-Machado 2021). Treat as a stability-preservation option, not a survival upgrade. [근거강함(소표본)]
- "Osteoporosis = high implant failure." — Short-term comparable to healthy; the risk is long-term and bone-quality-driven, separate from drug/MRONJ risk (Kim 2026). [합의수준]

## Gaps & Future Research

- Most soft-bone modification evidence is short-term (6–12 mo) and small-n (Mello-Machado n=16, Munjal n=14) — no long-term MBL/survival RCT isolating bone quality.
- FEA (stress) vs clinical (primary stability) give divergent macro-design recommendations in D3/D4 — unresolved.
- No prospective data on implant outcomes *within* osteosclerotic lesions (case reports only).
- HU→ISQ→loading-timing thresholds are not standardized across density systems (Misch vs Lekholm-Zarb vs CBCT HU).

## Related overviews

- [[overviews/osseodensification-clinical-applications]] — the soft-bone drilling *solution* this page references as one lever
- [[overviews/implants-isq-stability-ladder]] — the *measurement* layer feeding loading-timing decisions
- [[overviews/drug-mronj-antiresorptive-overview]] — the *drug* layer for osteoporosis/antiresorptive patients
- [[overviews/implant-loading-protocol-prosthesis-type-overview]] — loading timing downstream of primary stability
- [[overviews/implant-design-bone-quality-stress-fea]] — the FEA *mechanism* layer: why low-density bone concentrates crestal stress and how macro-design redistributes it

## Related Papers

(see Evidence Map above for the 10 spine papers and their typed roles)

Supporting papers added 2026-06-10 (determinant evidence across the four modification levers):

- [[implants/isq/al-juboori-2024-cortical-thickness-implant-stability-sr]] — SR: thicker cortical bone → higher IT/ISQ (primary + secondary stability); confirms cortical-thickness-dominance thesis.
- [[implants/isq/nkenke-2003-implant-stability-histomorphometry-cadaver-correlation]] — cadaver: primary stability correlates with CT bone mineral density + histomorphometry (mechanistic anchor).
- [[implants/heimes-2023-macrogeometry-primary-stability-implants-narrative-review]] — narrative review: macro-design (diameter/taper/thread/surface) as the design lever.
- [[implants/di-stefano-2018-undersizing-tapping-bic-primary-stability-bovine-histomorphometric]] — bench: torque-depth integral quantifies undersizing → primary stability (the drilling lever).
- [[implants/el-kholey-2019-drilling-technique-low-density-bone-sr]] — SR: undersized/osteotome/Piezo/OD all raise primary stability but long-term superiority weak (caution on the drilling lever).
- [[implants/tabassum-2021-undersized-axial-compression-primary-stability]] — animal: lateral + axial compression raise IT/%BIC in low-density bone.
- [[implants/gehrke-2021-healing-chambers-macrogeometry-low-density-drilling]] — in-vitro: undersizing helps only above a density floor; macrogeometry complements.
