---
title: "Overview: Osteotomy Cooling Is a Delivery Problem — Irrigation Route, Dry Cooling, and Quantified Risk Hierarchy Once Cooling Is Present"
type: synthesis
category: overviews
date: 2026-10-19
evidence_level: synthesis
source_papers:
  - wiki/implants/osteotomy-thermal/paessens-2025-irrigation-bur-size-speed-thermographic-heat-osteotomy.md
  - wiki/implants/osteotomy-thermal/shobair-2026-heat-generation-guided-osteotomy-irrigation-route.md
  - wiki/implants/osteotomy-thermal/tur-2026-guided-conventional-pilot-drill-thermal-evaluation.md
  - wiki/implants/osteotomy-thermal/baris-2025-dry-cooling-peltier-osteotomy-heat.md
  - wiki/implants/osteotomy-thermal/balkanlioglu-2026-osteotomy-depth-diameter-d1-cadcam-temperature.md
  - wiki/implants/osseodensification/komu-2026-osseodensification-conventional-drilling-d3-heat-stability.md
  - wiki/implants/osteotomy-thermal/tur-2025-scais-cip-guided-conventional-drill-diameter-heat.md
  - wiki/implants/osteotomy-thermal/markovic-2016-effect-surgical-drill-guide-irrigans.md
  - wiki/implants/osteotomy-thermal/kapse-2022-thermal-effect-operatory-room-temperature-surgical.md
  - wiki/implants/osteotomy-thermal/sener-2009-effects-irrigation-temperature-heat-control.md
  - wiki/implants/osteotomy-thermal/gokce-uckun-2025-guided-surgery-cold-irrigation-temperature.md
tags: [osteotomy, irrigation-route, internal-irrigation, dry-cooling, peltier, guided-surgery, pilot-drill, odds-ratio, effect-size, osteotomy-depth, thermal-osteonecrosis, measurement-method]
relations:
  - type: refines
    target: osteotomy-drilling-heat-determinants-irrigation-overview
  - type: extends
    target: markovic-2016-effect-surgical-drill-guide-irrigans
  - type: contradicts
    target: kapse-2022-thermal-effect-operatory-room-temperature-surgical
---

> [!summary] 한국어 핵심요약
> - **핵심 질문**: 선행 overview는 "차가운 관주(irrigation)가 1순위"까지 정했다. 이 페이지는 그 다음을 묻는다 — 냉각을 *어떤 경로로, 얼마나* 전달해야 하고, 냉각이 이미 있을 때 남은 변수(깊이·직경·확장 단계·rpm)는 서로 얼마나 센가.
> - **관주 유무는 이분법이 아니라 최대 효과 크기**: 소 늑골 피질골 확장 골삭제 120편(Paeßens 2025, 열화상 계면 측정)에서 **관주 없음의 OR 177.5**(임계온도 ≥47°C), 확장 단계 Δ1.4 vs Δ0.8 mm는 OR 9.9, 속도 +400 rpm당 OR 4.9. 200 rpm 무관주도 시편의 80~100%가 47°C 초과 → "저속이면 무관주도 안전"은 다시 반박됨(Gökçe-Uçkun 2025와 같은 방향).
> - **관주 *경로*가 새 변수**: 가이드 수술 모델에서 3D 프린팅 가이드의 내부 채널 관주(internal)가 ΔT 3.50°C, 외부 관주 9.48°C, 무관주 31.41°C(고형 레진, Shobair 2026). 이중층 모델은 0.84 / 2.45 / 13.31°C. Markovic 2016이 지목한 "슬리브가 관주를 막는다"는 문제의 **공학적 해법 후보**지만 in vitro 레진 1편이다.
> - **가이드 수술의 열 불이익은 상수가 아니다**: 파일럿 드릴 단계(Tur 2026, 로봇 160회)에서 2.0 mm 슬리브 가이드는 일반 드릴링보다 *더 낮은* 온도(12 mm: 12.1 vs 22.1°C, p=0.0005), 2.8 mm 부분 가이드(슬리브 없는 handle cylinder)는 *더 높은* 온도(10 mm: 8.2 vs 5.6°C, p=0.0256). 선행 overview의 "가이드 = 입구 발열↑"은 슬리브 형태·관주 접근성·직경에 따라 방향이 바뀐다.
> - **건식 냉각(펠티어) 등장**: 소 늑골 RCT형 in vitro(n=120, Baris 2025)에서 DC 저압 ΔT 2.00°C vs 식염수 고압 5.45°C, 자가골 입자 28.5 vs 10.4 mg(2.75배). 단 시작 온도가 ~21°C라 "47°C보다 한참 아래"는 상온 출발의 산물이기도 하다 — 상대 비교로만 읽을 것.
> - **깊이 vs 직경(관주 하)**: D1형 소 피질골 3×3 요인설계(n=90, Balkanlioğlu 2026)에서 깊이 η²=0.82, 직경 η²=0.17, 깊이 1 mm당 +0.63°C(R²=0.785), 전 군 41.7°C 이하. **선행 overview가 인용한 Kapse 2022(직경·깊이 NS)와 충돌** — 아래 "미해결 충돌" 참조.
> - **깊이 효과의 방향은 관주 유무로 뒤집힌다 (본 페이지 해석, 가설)**: 무관주에서는 얕은 피질에서 최고(Sener: 3 mm 50.9°C vs 12 mm 38.1°C), 관주가 있으면 최고점이 깊은 쪽(Tur 2026: 무냉각 3–4.5 mm → 관주 시 6–9 mm)으로 이동. 관주가 피질 입구는 식히지만 깊은 와위까지는 덜 닿는다는 설명과 부합하나, 이를 직접 검증한 논문은 없다.
> - **측정법이 결론을 바꾼다**: 무관주 OD(골밀도화) D3 시험(Kömü 2026, 적외선 열화상, 단계별 Tmax)은 최고 45.45°C로 47°C 미만인 반면, 계면 열화상(Paeßens)은 무관주 시편이 대부분 47°C 초과·최고 116.4°C. 측정 위치·시점이 다르므로 같은 "무관주 안전성" 질문에 상반된 답이 나온다 — Kömü는 초록만 보유(full text 없음).
> - **교차 비교 금지**: OR(이분 결과)과 η²(Tmax 분산 설명률)는 단위가 다르다. "깊이 > 직경 > …" 같은 단일 서열은 만들 수 없고, 한 연구 *안*의 상대 크기만 읽는다.
> - **임상 takeaway**: ① 관주는 기본이되 *전달 경로*를 점검(가이드 슬리브·partial guide는 접근성 확인), ② 깊고 치밀한 와위에서는 관주 하에서도 깊이를 열 변수로 간주, ③ 확장 단계를 줄일 때는 저속(200 rpm대)+관주 조합에서만, ④ 건식 냉각·내부 채널은 임상 근거 전 단계 — 도입 판단 근거로 쓰지 말 것.

## Three-line Summary

This page extends the drilling-heat overview from "cool irrigant is the dominant lever" to **how the cooling is delivered and what still matters once it is present**, using six papers added after the prior synthesis. Irrigation absence carries by far the largest effect (OR 177.5 for ≥47°C in a 120-specimen thermographic expansion study; Paeßens 2025), irrigation *route* is a new variable (internal guide channels ΔT 3.50°C vs external 9.48°C vs none 31.41°C in solid resin; Shobair 2026), and a Peltier dry-cooling device beat saline in bovine rib (ΔT 2.00 vs 5.45°C at matched pressure extremes; Baris 2025) while preserving 2.75× more autogenous bone particles.

Three held findings **qualify the earlier overview**: guided-surgery heat penalty reverses sign with pilot diameter and sleeve design (2.0 mm sleeve cooler than conventional, 2.8 mm partial guide hotter; Tur 2026), osteotomy depth dominates temperature variance under irrigation in dense cortical bone (η² 0.82 vs diameter 0.17; Balkanlioğlu 2026) against the earlier "depth/diameter not worth optimizing" reading (Kapse 2022 NS) — an **unresolved conflict** between studies with different models and ranges — and non-irrigated safety verdicts depend on where and when temperature is measured (Kömü 2026 OD D3 Tmax ≤45.45°C vs Paeßens 2025 interface peaks to 116.4°C).

All six are in vitro or ex vivo on bovine bone or resin; two (Balkanlioğlu, Kömü) are held at abstract level only. Treat the effect *directions* and within-study magnitudes as usable, absolute temperatures and cross-study comparisons as not.

## 세줄요약

선행 overview의 "차가운 관주가 1순위"를 넘어 **냉각을 어떻게 전달하는가, 냉각이 있을 때 무엇이 남는가**를 그 이후 추가된 6편으로 정리한다. 관주 부재의 효과가 압도적(열화상 확장 골삭제 120편, ≥47°C OR 177.5; Paeßens 2025)이고, 관주 *경로*가 새 변수(가이드 내부 채널 3.50 vs 외부 9.48 vs 무관주 31.41°C, 고형 레진; Shobair 2026)이며, 펠티어 건식 냉각이 소 늑골에서 식염수보다 낮은 ΔT(2.00 vs 5.45°C)와 2.75배 많은 자가골 입자를 보였다(Baris 2025).

세 발견은 **선행 overview를 수정**한다: 가이드 수술의 발열 불이익은 파일럿 직경·슬리브 설계에 따라 부호가 바뀌고(2.0 mm 슬리브는 일반 드릴링보다 저온, 2.8 mm 부분 가이드는 고온; Tur 2026), 치밀 피질골 관주 하에서는 깊이가 Tmax 분산을 지배(η² 0.82 vs 직경 0.17; Balkanlioğlu 2026)해 "깊이·직경은 후순위"(Kapse 2022 NS)와 **미해결 충돌**하며, 무관주 안전성 판정은 측정 위치·시점에 좌우된다(Kömü 2026 OD D3 Tmax ≤45.45°C vs Paeßens 2025 계면 최고 116.4°C).

여섯 편 모두 소 뼈 또는 레진 대상 in vitro/ex vivo이고 둘(Balkanlioğlu, Kömü)은 초록 수준 보유다. 효과의 *방향*과 연구 내 상대 크기는 쓸 수 있으나 절대 온도와 연구 간 직접 비교는 쓸 수 없다.

## Thesis

**Clinical question:** The prior overview ([[overviews/osteotomy-drilling-heat-determinants-irrigation-overview]]) ranked chilled irrigant first and ruled depth, diameter, and room temperature out of contention. Given that, (a) does the *route* by which cooling reaches the bone matter, (b) can the cooling be delivered without saline, and (c) once cooling is present, which remaining variables still carry weight?

**Irrigation is a threshold-like effect, not a gradient.** Paeßens ([[implants/osteotomy-thermal/paessens-2025-irrigation-bur-size-speed-thermographic-heat-osteotomy]]) expanded 2.4 mm pilot cavities to 3.2 or 3.8 mm in 3.5 mm bovine rib cortex (120 specimens, 200/600/1000 rpm, ± 56 mL/min saline) and read the **drill–bone interface** with a thermographic camera at the moment of lamella perforation. Logistic regression gave OR 177.53 for no irrigation (p=0.00092), 9.94 for the larger expansion step, and 4.94 per +400 rpm. All 60 non-irrigated specimens ran hot enough to matter: at 200 rpm without irrigation 80–100% still exceeded 47°C, so slow speed does not substitute for cooling — the same conclusion Gökçe-Uçkun reached in sheep ilium ([[implants/osteotomy-thermal/gokce-uckun-2025-guided-surgery-cold-irrigation-temperature]]) and Rugova in the extreme synthetic-bone case. With irrigation at 200 rpm, both expansion steps stayed under threshold (mean 38.08 and 38.81°C), which is the study's basis for shortening step sequences. The page records no wear effect in this design (drills reused 6×, p=0.88), so it says nothing about the Tier-2 wear driver.

**Route matters once the case is guided.** The earlier overview explained the guided-surgery penalty through sleeve obstruction of external irrigation ([[implants/osteotomy-thermal/markovic-2016-effect-surgical-drill-guide-irrigans]]). Shobair ([[implants/osteotomy-thermal/shobair-2026-heat-generation-guided-osteotomy-irrigation-route]]) tests the obvious engineering answer — channels printed into the guide that deliver saline inside the sleeve — against external and no irrigation, drilling 2.0–4.2 mm sequentially to 18 mm at 1200 rpm in solid and bilayered (cortical + trabecular analogue) resin mandibles. Internal < external < none in both substrates (solid 3.50 / 9.48 / 31.41°C; bilayered 0.84 / 2.45 / 13.31°C). The wiki page states the ordering but does not record a pairwise test for internal vs external, so "internal beats external" is directional here. The bilayered model read lower than solid by infrared (p=0.009) and inconsistently by thermistor — a reminder that resin substrate and sensor choice shift the result as much as some clinical variables.

**The guided-surgery penalty is not a constant.** Tur 2026 ([[implants/osteotomy-thermal/tur-2026-guided-conventional-pilot-drill-thermal-evaluation]], robotic drilling, 160 preparations, 800 rpm, 50 mL/min, BoneSim bone substitute) splits the pilot phase by guide design. Under external irrigation the 2.0 mm **sleeve** guide was *cooler* than conventional drilling (10 mm: 9.44 vs 13.40°C, p=0.0107; 12 mm: 12.09 vs 22.10°C, p=0.0005), whereas the 2.8 mm **partially guided** protocol (drill-handle cylinder, no sleeve) was *hotter* at 10 mm (8.16 vs 5.62°C, p=0.0256; 12 mm NS, p=0.0655). Without irrigation, conventional drilling was hotter than guided in every diameter/depth cell (p=0.0016–0.0162). Combined with Tur 2025 (3.5 mm the critical diameter; [[implants/osteotomy-thermal/tur-2025-scais-cip-guided-conventional-drill-diameter-heat]]) and Saxena's SR, the defensible reading is that **sleeve geometry and irrigation access, not "guided vs freehand", set the thermal outcome** — which revises the earlier Tier-3 statement that guides add cortical-entrance heat. The wiki page does not record the baseline temperature for these ΔT values, so the absolute-versus-47°C claims cannot be rechecked from the held text.

**Cooling without saline is now a tested concept, with a caveat.** Baris ([[implants/osteotomy-thermal/baris-2025-dry-cooling-peltier-osteotomy-heat]], n=120, 30/group, bovine rib cortex 1.5–2 mm, 800 rpm, sequential to 4.1 mm at 10 mm depth) compared a closed-loop Peltier tip (~9.5°C, −11.5°C from ambient, no fluid) with 21°C external saline at 10 N and 20 N. ΔT: DC-low 2.00 ± 0.84°C, SC-low 3.45, SC-high 5.45 ± 0.90°C; DC-high had a final temperature of 24.00°C (ΔT not recorded in the page) and was statistically equivalent to SC-low. DC groups also recovered 28.53 vs 10.35 mg of bone particles (p<0.001). Two cautions: starting temperature was ~21°C, so every group ending at 23–26°C says little about margin to 47°C; and the cortex was thin. Read it as evidence that **delivered cold, not delivered fluid, is what lowers ΔT** — consistent with the earlier "colder beats copious" reading ([[implants/osteotomy-thermal/einafshar-2024-importance-precision-cortical-bone-drilling]] on pre-cooled drills points the same way) — not as a clinical alternative.

**With cooling present, depth appears — and conflicts with the earlier ranking.** Balkanlioğlu ([[implants/osteotomy-thermal/balkanlioglu-2026-osteotomy-depth-diameter-d1-cadcam-temperature]], fresh bovine femoral cortex as D1 analogue, 3.5/4.0/4.5 mm × 6.5/11/15 mm, n=90, CAD/CAM-guided thermocouples 1 mm from the wall, continuous external irrigation) found depth η²=0.82 and diameter η²=0.17, a significant interaction (p<0.001), and +0.63°C per mm (r=0.886, R²=0.785); every osteotomy peaked at ≤41.7°C. The earlier overview, citing Kapse 2022 ([[implants/osteotomy-thermal/kapse-2022-thermal-effect-operatory-room-temperature-surgical]]), treated drill diameter and depth as non-significant "within tested ranges". Both can be true only if the models or ranges differ in ways the held pages do not let me resolve — Balkanlioğlu is homogeneous dense cortex without a cancellous layer and is held at abstract level; I did not re-read Kapse's methods for this page. **This conflict is flagged, not resolved**, and the earlier Tier 4 wording on depth should be read as "not a lever *in the Kapse design*".

A candidate reconciliation, offered as a hypothesis and not a finding: without irrigation, heat peaks superficially (Sener 2009: 3 mm 50.9°C vs 12 mm 38.1°C; [[implants/osteotomy-thermal/sener-2009-effects-irrigation-temperature-heat-control]]), while with irrigation the peak migrates deeper (Tur 2026: superficial without cooling → 6–9 mm with irrigation). If external cooling reaches the entrance but not the depth of a long osteotomy, depth would *emerge* as the residual variable once irrigation is present — which is exactly Balkanlioğlu's design. No held paper tests this directly.

**Non-irrigated verdicts depend on the thermometer.** Kömü ([[implants/osseodensification/komu-2026-osseodensification-conventional-drilling-d3-heat-stability]], 60 implants in D3 bovine rib, no irrigation, IR thermography per step) reports OD Tmax 42.73 ± 5.14°C vs conventional 37.43 ± 4.22°C (p<0.001), the 2.3 mm Densah bur peaking at 45.45°C, and higher ISQ for OD (77.30 vs 74.68, p<0.05) — and concludes both stay under 47°C. Paeßens' interface method found most non-irrigated specimens above threshold with single peaks to 116.4°C. These are not contradictory data so much as **different measurement loci** (step-wise surface/field reading vs interface at perforation), the same heterogeneity Jung flagged ([[implants/osteotomy-thermal/jung-2021-heat-development-medical-drilling-influencing]]). For OD, the earlier overview's wear/rpm rule (Soldatos; [[implants/osseodensification/soldatos-2024-temperature-changes-osseodensification-cadaver-tibiae-cw-ccw]]) is unchanged; Kömü adds that the smallest bur is the hottest step and leaves a ~1.5°C margin in the worst-case dry condition. Abstract-level evidence only.

## Evidence Table

| Question | Paper | Design | Key result | Reading |
|---|---|---|---|---|
| Irrigation effect size | [[implants/osteotomy-thermal/paessens-2025-irrigation-bur-size-speed-thermographic-heat-osteotomy]] | Bovine rib, n=120, interface thermography | No irrigation OR 177.5; step Δ1.4 OR 9.9; +400 rpm OR 4.9 | Irrigation dominates; 200 rpm + irrigation safe for both steps |
| Irrigation route | [[implants/osteotomy-thermal/shobair-2026-heat-generation-guided-osteotomy-irrigation-route]] | Resin mandible, solid vs bilayered, IR + thermistor | Internal 3.50 / external 9.48 / none 31.41°C (solid) | Route is a variable; one substrate-limited study |
| Guide design | [[implants/osteotomy-thermal/tur-2026-guided-conventional-pilot-drill-thermal-evaluation]] | BoneSim, robotic, n=160 | 2.0 mm sleeve < conventional; 2.8 mm partial > conventional (10 mm) | Penalty depends on sleeve and irrigation access |
| Dry cooling | [[implants/osteotomy-thermal/baris-2025-dry-cooling-peltier-osteotomy-heat]] | Bovine rib, n=120, 4 arms | DC-low ΔT 2.00 vs SC-high 5.45°C; bone 28.5 vs 10.4 mg | Cold delivery matters; room-temperature start limits margin claims |
| Depth vs diameter | [[implants/osteotomy-thermal/balkanlioglu-2026-osteotomy-depth-diameter-d1-cadcam-temperature]] | Bovine cortex D1, 3×3, n=90 | Depth η² 0.82, diameter 0.17, +0.63°C/mm | **Conflicts with Kapse 2022**; abstract-level |
| Dry OD, D3 | [[implants/osseodensification/komu-2026-osseodensification-conventional-drilling-d3-heat-stability]] | Bovine rib D3, n=60, no irrigation | OD 42.73 vs CD 37.43°C; 2.3 mm bur 45.45°C; ISQ 77.30 vs 74.68 | Measurement-locus dependent; abstract-only |

## Open Conflicts and Gaps

- **Depth/diameter: Kapse 2022 (NS) vs Balkanlioğlu 2026 (η² 0.82 / 0.17).** Unresolved; needs a methods-level comparison of model, range, sensor distance, and irrigation set-up.
- **Guide penalty direction.** Markovic/Saxena (guide ↑ entrance heat) vs Tur 2026 2.0 mm sleeve (guide ↓). Candidate moderators: sleeve vs partial guide, pilot vs final diameter, irrigation access. Not yet separated in a single experiment.
- **Absolute safety margins.** Baris (21°C start) and Tur 2026 (baseline not recorded in the page) report ΔT or final values that cannot be read against 47°C without the baseline.
- **No in vivo or clinical data** in this set. The biological payoff of route or dry cooling (cf. Heuzeroth, [[implants/osteotomy-thermal/heuzeroth-2021-thermal-exposure-osteotomy-osseointegration]]) is untested.

## Clinical Bottom Line

1. **Irrigation stays non-negotiable and speed is no substitute** (Paeßens OR 177.5; 200 rpm dry still failed in 80–100%). This reinforces rather than changes the earlier Tier 1.
2. **In guided cases, check whether the saline actually reaches the bur.** The thermal question is sleeve geometry and irrigation access (Tur 2026, Markovic); internal guide channels (Shobair) are a promising but resin-only idea.
3. **Treat depth as a heat variable in dense cortical bone even under irrigation** (Balkanlioğlu, with the Kapse conflict noted), and favour slower speed with irrigation when collapsing expansion steps (Paeßens).
4. **Do not adopt dry cooling or internal-channel guides on this evidence.** Both are single in vitro studies; they inform the mechanism (cold delivery), not practice.
5. **Do not accept "dry OD is safe" from a single-method reading** (Kömü); the smallest Densah bur is the hottest step and the measured margin is thin.

## Related Overviews & Adjacent Threads

- [[overviews/osteotomy-drilling-heat-determinants-irrigation-overview]] — the parent synthesis; this page refines its Tier 3 (guided surgery) and Tier 4 (depth/diameter) statements.
- [[overviews/dense-bone-osteotomy-heat-reimplantation-overview]] — the D1 dense-bone scenario where the Balkanlioğlu depth finding is most applicable.
- [[overviews/osseodensification-clinical-applications]] — OD-side reading of Kömü and Soldatos.
- [[overviews/implants-clinical-decision-ladder]] — where drilling-heat control sits in the implant decision sequence.
