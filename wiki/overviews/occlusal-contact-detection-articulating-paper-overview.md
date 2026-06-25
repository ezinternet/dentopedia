---
title: "Overview: Occlusal Contact Detection — Articulating Paper Accuracy & Indicator Selection"
type: synthesis
category: overviews
date: 2026-06-26
confidence: synthesis
source_papers:
  - wiki/occlusion/rovira-lastra-2026-articulating-paper-accuracy-occlusal-points.md
  - wiki/occlusion/bozhkova-2021-occlusal-indicators-dental-practice-survey.md
  - wiki/occlusion/didier-2026-occlusal-contacts-ios-vs-carbon-paper-concordance.md
  - wiki/occlusion/velasquez-2022-occlusal-analysis-natural-dentition-sr.md
  - wiki/occlusion/gozen-2025-occlusal-force-distribution-digital-analysis-implant-in-vivo.md
tags: [occlusal-indicator, articulating-paper, shim-stock, t-scan, occlusense, intraoral-scanner, occlusal-adjustment, accuracy]
---

> [!summary] 한국어 핵심요약
> - **결론(bottom line)**: 교합지(Articulating Paper, AP)는 여전히 가장 많이 쓰이는 교합 지시재지만 정확도는 "중간" 수준 — 접촉의 ~81%만 검출하고 ~15%는 위양성(False Positive, FP)이며, 교합력·접촉 순서는 전혀 측정 못 한다. 정확도는 *재료가 아니라 술식*으로 끌어올린다.
> - **실사용 1위 압도(usage)**: 치과의사 228명 설문에서 교합지 52.4% ≫ 교합박(foil) 26.2% > 실크(silk) 16.8% ≫ 심스탁(shim stock) 2.45% · T-Scan 1.4% · OccluSense 0.7%. 디지털 도입 의향은 58.7%로 사용률(~2%)과 큰 격차.
> - **두께(thickness) — 직관과 반대**: 200 µm 교합지가 100 µm보다 *더* 정확(위양성 9.4% vs 20.6%, 교두정 위양성 0.61 vs 1.75/hemiarch). 얇다고 정밀한 게 아니다.
> - **악궁(arch) 선택**: 하악궁(mandibular) 검사가 상악궁보다 진양성 ~5%p 높고(잉크 보존·직접 시야), 임상적으로도 보기 쉽다.
> - **읽는 법(interpretation) 핵심 규칙**: ① 교두정(cusp tip) 마크가 대합치에 짝이 없으면 위양성으로 간주 — FP의 약 2/3가 교두정 마찰 자국. ② **양악 일치(both-arch coincidence)** 기준 적용 시 위양성이 15% → 2%로 급감.
> - **색 강도 ≠ 교합력**: 진한 파란색이 강한 접촉이라는 통념은 근거 약함(이론적 light-blue/dark halo 패턴이 실제론 거의 안 나타남). 힘은 정량 도구로만.
> - **심스탁(shim stock)의 역할**: 표면에 자국을 남기지 않고 *대합치 접촉 유무(presence/absence)*만 8~12 µm foil로 확인 — 그래서 사용률 최하위지만, "이 치아가 닿는가?"를 yes/no로 판정할 땐 유일하게 깔끔한 도구.
> - **디지털 ≠ 교합지 대체(not interchangeable)**: iTero IOS 교합도 vs 8 µm 카본지 일치도 매우 낮음(카파 0.07–0.20). IOS red+orange는 접촉 ~70% 과대평가, red-only는 과소평가. 디지털과 카본지는 *교환이 아니라 병용*.
> - **디지털끼리는 잘 맞음**: Medit i700 IOS(접촉 위치)와 OccluSense(접촉면적+교합력)는 강한 상관(p<0.001) — IOS=위치, OccluSense=힘으로 상호 보완.
> - **객관성(objectivity)**: SR은 디지털 교합분석이 교합지(주관적)보다 객관적이라고 정리; 교합외상-치아민감-악관절장애(TMD) 연관, 최대 접촉력은 비기능교두 48%.
> - **임상 권고 요약**: 정성 판정엔 200 µm 교합지 + 하악궁 + 양악일치 규칙, 닿음 yes/no엔 shim stock, 교합력·타이밍 정량엔 T-Scan/OccluSense, IOS는 위치 매핑 보조(카본지 대체 금지).

## One-line Summary

Synthesis of 5 papers on how clinicians detect and verify occlusal contacts: articulating paper dominates practice yet is only moderately valid (~81% true positives, ~15% false positives) and cannot quantify force or timing — accuracy is best improved by technique (200 µm paper, mandibular arch, both-arch coincidence, distrusting cusp-tip marks), while digital systems (T-Scan, OccluSense, IOS) add objectivity but are complementary to, not interchangeable with, paper.

## 한줄요약

교합접촉 검출·검증법을 다룬 5편 종합: 교합지는 실사용 1위지만 정확도는 중간(진양성 ~81%, 위양성 ~15%)이고 교합력·순서는 측정 못 함 — 정확도는 술식(200 µm·하악궁·양악일치·교두정 마크 불신)으로 올리고, 디지털 도구(T-Scan/OccluSense/IOS)는 교합지의 대체가 아닌 보완으로 쓴다.

## Thesis

The clinical question "how do I know where (and how hard) the teeth contact?" has two layers, and the held evidence answers each:

1. **Qualitative location** — *where* contacts are. Articulating paper is the near-universal tool (Bozhkova: 52.4% usage). Its validity is moderate, not high: Rovira-Lastra's reference-standard study puts it at 81% true positives and 15% false positives for posterior contact *points*. Crucially, this accuracy is **operator-controllable**: thicker (200 µm) paper, examining the mandibular arch, and only accepting marks that coincide on both arches collapse false positives to ~2%.

2. **Quantitative force & timing** — *how hard* and *in what sequence*. Paper cannot do this (color intensity is an unreliable proxy). Quantitative systems (T-Scan, OccluSense) can, and SR-level synthesis (Velásquez) judges digital analysis more objective. But adoption lags far behind intent (Bozhkova: ~2% use vs 58.7% willing).

The bridge between layers is **non-interchangeability**: digital occlusal maps do not agree with carbon paper (Didier: κ 0.07–0.20), each erring in a known direction, so digital and conventional methods are *complementary*. Among digital tools themselves, location (IOS) and force (OccluSense) correlate strongly and pair well (Gözen). The net clinical rule: **match the indicator to the question**, and optimize paper technique rather than assuming the mark equals the truth.

## Evidence Map

| Paper | Design | n | Key Finding | Confidence |
|---|---|---|---|---|
| [[occlusion/rovira-lastra-2026-articulating-paper-accuracy-occlusal-points]] | cross-sectional, test–retest vs silicone reference | 32 natural dentitions | AP 81% true-pos / 15% false-pos; 200 µm FP 9.4% < 100 µm 20.6%; mandibular > maxillary (+5%); both-arch coincidence → FP 2%; ~66% of FP on cusp tips; pulling no effect | cross-sectional |
| [[occlusion/bozhkova-2021-occlusal-indicators-dental-practice-survey]] | survey | 228 dentists | Usage: AP 52.4% ≫ foil 26.2% > silk 16.8% ≫ shim stock 2.45% · T-Scan 1.4% · OccluSense 0.7%; 58.7% willing to go digital; shim stock = presence/absence only | cross-sectional |
| [[occlusion/didier-2026-occlusal-contacts-ios-vs-carbon-paper-concordance]] | retrospective method-agreement | 35 pts / 840 teeth | iTero occlusogram vs 8 µm carbon: κ 0.07–0.20 (poor); red+orange +70% overestimate, red-only underestimate; 48.1% of red contacts clinically ideal; not interchangeable | cross-sectional |
| [[occlusion/velasquez-2022-occlusal-analysis-natural-dentition-sr]] | systematic review | 10 studies | Digital occlusal analysis more objective than (subjective) articulating paper; occlusal trauma ↔ tooth sensitivity & TMD; max force on non-functional cusps (48%) | sr |
| [[occlusion/gozen-2025-occlusal-force-distribution-digital-analysis-implant-in-vivo]] | prospective in-vivo | 18 analyzed | Medit i700 IOS (area) vs OccluSense (area + force) correlate strongly (p<0.001); IOS = location, OccluSense = force; single implant crown redistributes arch-wide force | in-vivo |

## Clinical Decision Points

**1. Which indicator for which question?**

| Question | Best tool (held evidence) |
|---|---|
| *Where* are the contacts? (mark location) | Articulating paper / foil / silk — qualitative |
| *Does* this tooth contact at all? (yes/no) | Shim stock foil (8–12 µm) — presence/absence only |
| *How hard* / *in what order*? (force, timing) | T-Scan or OccluSense — quantitative |
| Localize contacts in a digital workflow | IOS occlusogram — but **pair with paper**, never replace |

**2. Articulating-paper technique (to reach the ~2% false-positive floor):**
- Prefer **200 µm** over 100 µm paper (fewer false positives, fewer cusp-tip artifacts).
- Examine the **mandibular arch** preferentially (higher true-positive %, ink better preserved, easier direct view).
- Apply the **both-arch coincidence rule**: count a contact only when the mark appears on *both* opposing surfaces at the same site.
- Treat a **cusp-tip mark with no matching antagonist mark as an artifact** (incidental rubbing) — ~2/3 of false positives live here.
- The "**pulling**" forceps technique gives no accuracy benefit; basics matter more (dry surfaces, saliva control, verified intercuspal closure, fresh non-fragmented paper, don't drag the strip).

**3. Reading the marks — what NOT to infer:**
- Do **not** read occlusal *force* from color/mark intensity (the theoretical light-blue-with-dark-halo pattern is largely absent in practice; subjective force ranking is unreliable).
- Do **not** treat digital "red" contacts as automatically excessive — ~48% of intense red contacts were clinically ideal; over-removing them risks overcorrection / posterior open bite.

**4. Digital ↔ conventional:**
- Digital maps and carbon paper **disagree** (κ 0.07–0.20) — use them as complements, knowing IOS red+orange overestimates and red-only underestimates.
- Within digital, **IOS = position, OccluSense = force** — they pair, not compete.

## Gaps & Future Research

- **Thin films (8–40 µm) untested for validity** — Rovira-Lastra's accuracy data cover only 100–200 µm; the thinner papers/foils many clinicians prefer lack reference-standard validation.
- **Anterior teeth & restored/prosthetic dentitions** — current accuracy figures are posterior, natural-dentition only; not generalizable to crowns, RPD/implant prostheses, or occlusal disorders.
- **Adoption gap** — ~2% digital usage vs 58.7% stated willingness (Bozhkova); barriers (cost, learning curve, workflow) and whether quantitative tools change patient outcomes remain open.
- **Outcome relevance of "objectivity"** — SR shows digital is more objective, but RCT evidence that objective measurement improves clinical results is thin (cf. T-Scan-guided post-orthodontic adjustment showing no measurable advantage at 6 months).
- **AI-assisted mark interpretation** — deep-learning detection of true vs false-positive marks and chromatic force estimation proposed but unproven.

## Related Papers

- [[occlusion/rovira-lastra-2026-articulating-paper-accuracy-occlusal-points]] — accuracy/technique backbone of the paper-optimization recommendations.
- [[occlusion/bozhkova-2021-occlusal-indicators-dental-practice-survey]] — real-world indicator usage and the qualitative/quantitative dichotomy.
- [[occlusion/didier-2026-occlusal-contacts-ios-vs-carbon-paper-concordance]] — digital-vs-conventional non-interchangeability.
- [[occlusion/velasquez-2022-occlusal-analysis-natural-dentition-sr]] — SR establishing digital objectivity and trauma/TMD links.
- [[occlusion/gozen-2025-occlusal-force-distribution-digital-analysis-implant-in-vivo]] — digital-vs-digital agreement (IOS location vs OccluSense force).
- [[occlusion/jahanbin-2026-occlusal-adjustment-post-orthodontic-tscan-rct]] — T-Scan-measured RCT: objective monitoring did not translate to a measurable adjustment advantage at 6 months (outcome-relevance caveat).
