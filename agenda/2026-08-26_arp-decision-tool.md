---
title: "발치와 보존(ARP) 결정 도구 — 할까 말까 · 얼마나 잃나 · 무엇으로"
type: agenda
date: 2026-08-26
status: in-progress
owner: 원장
priority: P0
tags: [bone-regeneration, arp, ridge-preservation, extraction, gbr, chairside]
source_wiki:
  - wiki/overviews/bone-regeneration-protocol-ladder.md
---

# Goal

`bone-regeneration-protocol-ladder`(inbound 28)를 체어사이드 도구로 전환한다.

# 형태 판단 — 상류가 비어 있다

골재생 도메인엔 이미 임상 도구가 7개다. 대조하면:

| 오버뷰 축 | 기존 도구 | 상태 |
|---|---|---|
| 축1 자연 치유 baseline | — | **비어 있음** |
| 축2 ARP 효과 크기 · 발치 시점 결정 | — | **비어 있음** |
| 축3 graft material 비교 | `2026-08-17_arp-material-histology-matrix` | 커버 |
| 축4 막·판막·연조직 seal | `2026-06-28_gbr-6panel-classification` | 부분 커버 |

기존 도구는 **"어떤 재료로"·"어떤 GBR 패턴으로"** 를 답한다. 그런데 그 앞 질문 — **"ARP를 할 것인가, 안 하면 얼마나 잃나"** — 이 비어 있다. 상류 결정이 없으니 하류 도구는 이미 ARP를 하기로 정한 사람만 쓸 수 있다.

→ 산출물은 **발치 시점의 상류 결정 도구**. 손실량을 나란히 놓고 결정하게 하고, 재료·막 세부는 기존 도구로 넘긴다.

# 계산 근거 (오버뷰 보유 수치)

- 자연 치유 6개월: **수평 −3.79mm**(가중평균), **수직 협측 −1.24~1.67mm**. 수평이 수직보다 훨씬 크다 [확인]
- ARP 시행 시: 자연 치유 대비 **수평 흡수 1.86~2.19mm 감소** [확인]
- 협측 얇음(BBT &lt;1mm) 부위는 손실 더 큼 [확인]

# Output

- `interactives/2026-08-26_arp-decision-tool.html`

# Done Criteria

- [ ] 자연 치유 vs ARP **예상 잔여 손실 비교** (수평/수직) — 위 수치로 계산
- [ ] 발치 시점 결정 사다리 4단계 (즉시식립 가능 / ARP / 선택적 / 결손+심미)
- [ ] 재료 사다리 5단계 (DBBM · β-TCP · 자가골 mix · 자가치아 · 동종골) + 국내 가용성
- [ ] 판막·막·seal 사다리 4단계 + 오판 패턴("막 노출=실패" ✗ — dPTFE는 노출 설계)
- [ ] 기존 도구 라우팅 (재료 매트릭스 · GBR 6패널 · 상악동 천공 · OD 내비게이터)
- [ ] 국내 비용은 시세 변동 명시

# Notes / Decisions

- 2026-08-26: 손실량을 **막대로 나란히** 보여주는 것이 이 도구의 핵심이다. "ARP 하면 좋다"는 이미 다 안다 — 결정을 바꾸는 건 *안 했을 때 3.79mm를 잃는다*는 크기 감각이다.
- 2026-08-26: 즉시식립 분기는 [[agenda/2026-08-26_immediate-implant-decision-tool]]로 넘긴다. 오버뷰도 그 축을 별도 페이지로 위임한다.
