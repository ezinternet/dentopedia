---
title: "즉시식립 5축 결정 도구 — timing·site·술식·연조직·부하"
type: agenda
date: 2026-08-26
status: in-progress
owner: 원장
priority: P0
tags: [immediate-implant, iip, decision-ladder, chairside, timing, loading]
source_wiki:
  - wiki/overviews/immediate-implant-decision-ladder.md
  - wiki/immediate-implant/anatomic-assessment/najm-2024-immediate-implant-premolar-perforation-cbct.md
  - wiki/immediate-implant/aung-2024-tapered-sla-immediate-implant-survival.md
  - wiki/immediate-implant/gap-grafting/meijer-2024-immediate-implant-bony-defect-10year-rct.md
  - wiki/immediate-implant/gap-grafting/sanz-2017-bone-graft-gap-immediate-implant-rct.md
  - wiki/immediate-implant/esthetic-soft-tissue/staas-2026-fiipp-palatal-position-cbct-3year.md
  - wiki/immediate-implant/molar-septum/mustakim-2023-immediate-implant-maxillary-molar-guidelines.md
  - wiki/immediate-implant/infected-socket/pranckeviciene-2024-immediate-implant-periapical-pathology-sr-ma.md
  - wiki/immediate-implant/loading-protocol/esposito-2015-immediate-loading-vs-delayed-anterior-rct.md
  - wiki/immediate-implant/loading-protocol/botros-2025-early-conventional-loading-immediate-molar.md
  - wiki/immediate-implant/socket-shield/ogawa-2022-socket-shield-technique-systematic-review.md
---

# Goal

`immediate-implant-decision-ladder`(inbound 32, uncovered 2위)를 체어사이드 결정 도구로 전환한다.

# 형태 판단 — ISQ와 왜 다른가

ISQ ladder는 **spine이자 지도**였다(상세를 다른 overview·도구에 명시적으로 위임). 그래서 허브가 답이었다.

이 페이지는 **실행 문서**다. 383줄, 5축이 순차 의사결정으로 이어지고, 각 축에 구체적 임계값(협측 plate 1mm/2mm/5mm, jumping gap 2mm, palatal ≥2mm, IT 35/25 Ncm)과 5~6단계 사다리가 박혀 있으며 위임 문구가 없다. 게다가 **오판 패턴 5개**와 한국 환경 조정까지 자체 보유한다.

기존 도구는 2개뿐이고 각각 좁다:

| 기존 도구 | 다루는 것 | ladder 5축 대비 |
|---|---|---|
| `2026-08-17_iip-complexity-calculator` (792줄) | Liu 2025 분류 기반 케이스 복잡도 점수 | 축 전반의 *난이도*만 |
| `2026-08-17_socket-shield-iip-selector` (640줄) | SST vs 통상 IIP | 축4의 socket shield 조각만 |

→ 축1(timing)·축2(site)·축3(술식)·축5(부하)가 **비어 있다.** 따라서 산출물은 허브가 아니라 **5축을 순서대로 통과시키는 결정 도구**이고, 복잡도·SST는 해당 지점에서 기존 도구로 넘긴다.

# Output

- `interactives/2026-08-26_immediate-implant-decision-tool.html`

# Done Criteria

- [ ] **입력**: 부위(6구획) · 협측 plate 5단계 · socket 벽 · 치근단 병소 · 상악동 병변 · 삽입토크 · 술자 숙련 · 심미요구
- [ ] **축1 timing** — Type 1/2/3/4 권고 + 근거
- [ ] **축2 site** — Ideal/Acceptable/Marginal/Challenging/Expert 5등급 + **부위별 5년 생존**(상악전치 85.4% 최저, 하악·소구치 100%) + **상악동 병변 flag**(실패 3건 전부) + **소구치 천공 경고**(보철주도 84.1%, 골주도 40.5%, 18.3° 순측경사 필요 → CBCT 필수·각형 보철 전제)
- [ ] **축3 술식** — flap/flapless, palatal ≥2mm, jumping gap ≥2mm 이식, GBR+dPTFE, 구치부 **ABH×septum 3×3**(Mustakim 2023)
- [ ] **축4 연조직** — CTG 1차, immediate provisional 조건(IT ≥35 + plate intact + 협조), CHA/SSA 대안, **SST는 숙련 게이트 + 합병증 9.5% 동의**
- [ ] **축5 부하** — immediate(≥35 Ncm, 비기능 교합) / early(25–35 + 4–6주 ISQ ≥70) / conventional(<25)
- [ ] **오판 패턴 5개** 별도 섹션 — 이 도구의 교육적 핵심
- [ ] 한국 환경 조정 — 비용은 원문대로 **[미검증]** 표기 유지
- [ ] 기존 도구 2종 라우팅
- [ ] frontmatter는 HTML 주석, 라이트 배경 고정

# Notes / Decisions

- 2026-08-26: **오판 패턴을 접어두지 않고 전면 섹션으로 뺀다.** 5개 중 4개가 "금기라고 알려진 것이 사실은 조건부 가능"이고, 이건 케이스를 놓치는 방향의 오류다 — 도구가 보수적 기본값만 주면 오히려 그 오류를 굳힌다.
- 2026-08-26: **비용은 [미검증] 태그를 그대로 달고 옮긴다.** 오버슈의 확신도 등급이 "한국 가용성·비용 = [미검증]"이라고 명시했다. 도구로 옮기면서 태그를 떼면 미검증 정보가 검증된 것처럼 승격된다.
- 2026-08-26: 후속 후보 — overview의 원장 체크리스트가 **"환자 안내: 즉시식립 가능/불가 평어 설명서 + Type 1-4 시각화"** 를 스스로 요청하고 있다. 술자용을 먼저 만들고, 환자용은 별건으로.

# References

- [[agenda/2026-08-26_isq-stability-ladder-chairside-hub]] — 바로 앞 전환. 형태가 왜 달라지는지의 대조군
- [[agenda/2026-08-25_wiki-midterm-review]]
