---
title: "ISQ 안정성 사다리 체어사이드 허브 — 측정→보정→부하결정 + 전문도구 라우팅"
type: agenda
date: 2026-08-26
status: in-progress
owner: 원장
priority: P0
tags: [isq, rfa, implant-stability, loading-protocol, decision-ladder, chairside, hub]
source_wiki:
  - wiki/overviews/implants-isq-stability-ladder.md
  - wiki/overviews/isq-loading-threshold.md
  - wiki/overviews/rfa-isq-measurement-mechanism.md
  - wiki/implants/isq/chatvaratthana-2017-cortical-bone-crestal-buccolingual-isq.md
  - wiki/implants/isq/huang-2017-multivariate-regression-isq-prediction.md
  - wiki/implants/isq/kim-2013-implant-stability-retrospective-rfa-isq.md
  - wiki/implants/isq/balshi-2005-rfa-immediately-loaded-maxillary-mandibular.md
  - wiki/implants/isq/tisci-2026-isq-it-mbl-survival-sr-ma.md
  - wiki/implants/isq/kastel-2019-smartpeg-torque-isq-rfa.md
  - wiki/implants/isq/lee-2024-primary-implant-stability-isq-devices-invitro.md
  - wiki/implants/isq/won-2008-smartpeg-sterilization-rfa-implant-stability.md
  - wiki/implants/isq/nedir-2004-predicting-osseointegration-primary-stability-rfa.md
---

# Goal

`implants-isq-stability-ladder` overview(31편 spine, inbound 39로 위키 최대 허브)를 체어사이드 도구로 전환한다. 중간평가가 지목한 **최우선 항목** — 위키에서 가장 많이 참조되는 결론이 어떤 임상 산출물로도 안 꺼내져 있었다.

# Input

- `wiki/overviews/implants-isq-stability-ladder.md` — 전환 대상. 3축(측정도구·임계값·영향변수) spine + 각 축의 임상 ladder
- 위 frontmatter의 spine paper 9편 — 도구에 들어가는 모든 수치의 인용처

# 왜 6번째 계산기가 아닌가 (설계 판단)

ISQ 인터랙티브는 **이미 5개** 있다:

| 기존 도구 | 다루는 것 | 인용 overview |
|---|---|---|
| `2026-06-02_isq-rfa-loading-simulator-v1` | 측정→치유궤적→부하결정 | (개별 논문만) |
| `2026-08-18_ist-vs-isq-device-selector` | Osstell vs Anycheck 기기 선택 | (개별 논문만) |
| `2026-08-18_under-milling-itv-isq-calculator` | under-milling ITV·ISQ 예측 | isq-loading-threshold |
| `isq-flex-constant-explorer` | ISQ ↔ 측방변위 | rfa-isq-measurement-mechanism |
| `rfa-2dof-frequency-simulator` | 강성·공진주파수·미세변위 | rfa-isq-measurement-mechanism |

**어느 것도 `implants-isq-stability-ladder`를 인용하지 않는다** (인용 2건은 둘 다 `category: meta` 자동생성 도구). 즉 5개가 각자 한 조각씩 다루고 **입구가 없다**. 그리고 ladder 본문 스스로 "자세한 ladder는 isq-loading-threshold, chairside 도구는 시뮬레이터 참조"라고 위임하고 있다 — 이 페이지의 역할은 **spine이자 지도**다.

따라서 산출물은 계산기가 아니라 **허브**여야 한다: ladder의 임상 사다리를 실행 가능하게 만들고, 각 결정 지점에서 5개 전문 도구로 보낸다.

# Output

- `interactives/2026-08-26_isq-stability-ladder-hub.html`

# Done Criteria

- [ ] **입력**: 부위(상/하악 × 전치/구치), 골질 Type I–IV, 동반술식(없음/상악동거상/GBR), 발치와(신선/치유), ISQ 4방향, 삽입토크(Ncm)
- [ ] **보정 임계값 자동 계산** — 기준 70에 상악동거상·GBR +3, Type IV +2 (ladder 축2 규칙)
- [ ] **4방향 편차 검사** — 1방향만 평균과 ≥10 차이 시 재측정 경고
- [ ] **부하 결정 3분기** — 즉시(ISQ≥임계 + IT≥35) / 조기·재측정(60–69) / 통상(<60)
- [ ] **신선 발치와 예외** — ISQ 인위적 저하(~57 vs 치유골 ~72) → IT 우선 기준으로 전환
- [ ] **ISQ↔IT 불일치 경고** — 상관 r=0.44·I²>90%라 둘이 갈릴 수 있고, 갈리는 것 자체가 정보
- [ ] **30일 stability dip 궤적** — 즉시부하 선택 시 Balshi 2005 곡선(70.35→66.38→68.01→68.82)과 "60일 이전 프로토콜 변경 금지"
- [ ] **축3 예측 패널** — 피질골 두께·직경·악궁 위치로 식립 전 ISQ 기대치
- [ ] **5개 전문 도구 라우팅** — 각 결정 지점에서 해당 도구로
- [ ] 모든 수치에 인용 표기, 라이트 배경 고정, frontmatter는 HTML 주석
- [ ] `operations-lint` 통과 · `interactive-staleness` OK

# Notes / Decisions

- 2026-08-26: **허브로 만들되 계산은 진짜로 한다.** 단순 링크 모음이면 output-coverage 숫자만 올리고 실제로는 안 쓰인다 — 중간평가가 경계한 "지표 채우기"가 된다. ladder 축2의 보정 규칙(+3/+2)과 4방향 편차 검사는 손으로 하면 실수하는 계산이라 도구가 값을 한다.
- 2026-08-26: **통증 도구와 달리 여기서는 논쟁을 전면에 두지 않는다.** ISQ 임계값은 ADA 코르티코스테로이드 건과 달리 spine 내부에서 수렴해 있다(Andersson 2019 + Bavetta 2024). 다만 ISQ↔IT 상관 r=0.44는 명시한다 — 둘을 같은 것으로 쓰는 오용이 실제 위험이다.
- 2026-08-26: Nedir 2004의 낮은 임계(지연 ≥49 / 즉시 ≥54)는 **역사적 하한**으로만 표시하고 결정 로직에는 안 넣는다. 현행 ladder는 70/65이고, 두 기준을 섞으면 도구가 관대해진다.

# References

- [[agenda/2026-08-25_wiki-midterm-review]] — 이 작업을 최우선으로 지목한 중간평가
- `OPERATIONS.md` §1 routing, §3 frontmatter cross-link
