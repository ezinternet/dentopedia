---
title: "Overview: Robotic vs Dynamic Navigation vs Static Guide — Implant Placement Accuracy"
type: synthesis
category: overviews
date: 2026-06-07
confidence: synthesis
source_papers:
  - wiki/digital-workflow/yu-2025-autonomous-robotic-versus-dynamic-navigation.md
  - wiki/digital-workflow/wei-2025-autonomous-robotic-surgery-dynamic-navigation.md
  - wiki/digital-workflow/chen-2025-robot-assisted-dynamic-navigation-accuracy.md
  - wiki/digital-workflow/wu-2024-autonomous-dental-implant-robotic-accuracy.md
  - wiki/digital-workflow/schiavon-2025-computer-assisted-immediate-implant-accuracy-nma.md
tags: [robotic-surgery, dynamic-navigation, CAIS, implant-accuracy, synthesis]
---

## 한국어 핵심요약

> [!summary] 한국어 핵심요약
> - 임플란트 식립 정확도 비교 종합 — 자율 로봇(robotic, r-CAIS) vs 동적 내비게이션(dynamic navigation, d-CAIS) vs 정적 가이드(static guide), 5편.
> - 핵심 질문 전환: "로봇이 더 정확한가?"가 아니라 "정확도의 *어느 성분*이 개선되며, 그것이 로봇 덕인가 추적 파이프라인 덕인가?"
> - 결론 한 줄: 로봇은 각도 편차(angular deviation)를 일관되게 줄이나, 동일 추적장치로 통제하면 선형(플랫폼·첨부) 편차 우위는 비유의해지고 시술시간만 길어짐.
> - 비통제 비교(Yu 2025, prospective n=135): 로봇이 세 편차 지표를 모두 약 절반으로(각도 1.62° vs 3.61°, p<0.001).
> - 추적장치를 양 군에 동일화한 유일한 RCT(Wei 2025, n=40): 로봇의 재현 가능한 이점은 각도 통제뿐(1.01° vs 1.78°, p<0.01), 관상·첨부 선형 편차는 통계적으로 동등(NS).
> - 반자율 로봇(Chen 2025, retrospective n=57): 반대 양상 — 선형 이득은 있으나(p<0.001) 각도 이득은 없음(NS) → 술자가 부분적으로 loop에 남으면 각도 이득을 잃음.
> - 해석[claude해석]: 로봇은 손떨림·drift(각도)를 제거하나 내비게이션과 동일한 registration·tracking 오차 예산(선형)을 물려받음.
> - 임상 결정점: ①각도가 critical한 케이스(다수 임플란트 평행성·좁은 치근간·보철 주도 각도)→로봇이 가장 명확·재현 가능한 이점[합의수준] ②단순 단일 부위→동적 내비가 선형 정확도 동등하면서 더 빠름 ③벤더 정확도 주장은 동일 추적장치 비교를 요구[근거강함, Wei RCT] ④로봇 자율 수준을 필요한 정확도 성분에 맞출 것.
> - Gap: 편차 차이를 골유착·MBL·보철 적합·생존 등 hard outcome에 연결한 데이터 없음, RCT n 작음·단일치 중심·학습곡선 미분리·비용효과 분석 없음, 복잡/full-arch·즉시식립 로봇 정확도 미연구.

## One-line Summary
Across current clinical evidence, autonomous implant robots reliably reduce angular deviation vs dynamic navigation, but their advantage in linear (platform/apex) deviation shrinks to non-significant once the optical tracking system is held constant — at the cost of longer chair time.

## 한줄요약
현재 임상근거 종합: 자율 임플란트 로봇은 동적내비게이션 대비 각도 편차를 일관되게 줄이나, 동일 추적장치로 통제하면 선형(플랫폼·첨부) 편차 우위는 비유의해지고 시술시간만 길어진다.

## Thesis
The clinical question is not "is the robot more accurate?" but "*which* component of accuracy improves, and is the improvement attributable to the robot or to its tracking pipeline?" Non-randomized comparisons (Yu 2025) show the robot roughly halving all three deviation metrics. But the one RCT that equalises the optical tracker across arms (Wei 2025) finds the robot's reliable, reproducible benefit is **angular control** — coronal and apical deviations become statistically equivalent to dynamic navigation. A semi-autonomous robot (Chen 2025) shows the opposite emphasis (linear gain, no angular gain), consistent with the operator remaining partly in the loop. Robots also impose longer surgical time. Net: robots are an angular-stability tool, not a blanket accuracy upgrade, and much of the apparent linear advantage in uncontrolled studies reflects tracking/operator confounding.

[claude해석] The most defensible reading is that the robot removes hand tremor/drift (angular) but inherits the same registration and tracking error budget as navigation (linear). Where pre-existing static-guide accuracy already suffices, robotic angular gain may not change clinical outcomes.

## Evidence Map

| Paper | Design | n (implants) | Comparison | Angular (robot vs nav) | Linear |
|---|---|---|---|---|---|
| Yu 2025 | prospective | 135 | r-CAIS vs d-CAIS | 1.62° vs 3.61° (p<0.001) | platform 0.50 vs 1.12; apex 0.58 vs 1.36 mm (both p<0.001) |
| Wei 2025 | RCT | 40 | AR vs DN, same tracker | 1.01° vs 1.78° (p<0.01) | coronal & apical NS |
| Chen 2025 | retrospective | 57 | sa-RASS vs DNS | 3.07° vs 3.71° (NS) | platform 0.91 vs 1.26; apex 1.06 vs 1.51 mm (p<0.001) |
| Wu 2024 | prospective single-arm | 86 | robot only | 2.56° (no comparator) | coronal 0.61; apical 0.79 mm |
| Schiavon 2025 | SR+NMA | 338 | static/dynamic CAIS vs freehand | CAIS ≫ freehand | accuracy ranked, immediate placement |

## Clinical Decision Points
- **Angular-critical cases** (parallelism in multi-implant, tight inter-radicular, prosthetically driven angulation): autonomous robot offers the clearest, most reproducible benefit. [합의수준]
- **Single straightforward sites**: dynamic navigation matches the robot on linear accuracy and is faster; robot's marginal angular gain may not justify added time/cost. [claude해석]
- **Interpreting vendor accuracy claims**: demand same-tracker comparisons. Cross-system deviation gaps overstate the robot effect. [근거강함, Wei RCT]
- **Semi-autonomous vs fully autonomous**: keeping the operator in the loop trades away angular gain — match robot autonomy level to the accuracy component you need.

## Gaps & Future Research
- No data linking deviation differences to hard outcomes (osseointegration, MBL, prosthetic fit, survival).
- Small RCT n; single-tooth focus; learning-curve not isolated; no cost-effectiveness.
- Complex/full-arch and immediate-placement robotic accuracy under-studied.

## Related Papers
- [[digital-workflow/yu-2025-autonomous-robotic-versus-dynamic-navigation]] — robot vs nav, largest deviation gap
- [[digital-workflow/wei-2025-autonomous-robotic-surgery-dynamic-navigation]] — RCT, same-tracker control narrows benefit to angular
- [[digital-workflow/chen-2025-robot-assisted-dynamic-navigation-accuracy]] — semi-autonomous robot, linear gain only
- [[digital-workflow/wu-2024-autonomous-dental-implant-robotic-accuracy]] — robot absolute accuracy benchmark
- [[digital-workflow/schiavon-2025-computer-assisted-immediate-implant-accuracy-nma]] — CAIS-vs-freehand NMA backbone
- [[overviews/digital-workflow-decision-ladder]] — broader digital workflow framework
