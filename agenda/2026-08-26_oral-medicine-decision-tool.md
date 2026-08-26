---
title: "구강점막질환 감별·처치 도구 — OLK·OLP·BMS·RAS·OMS·수포궤양"
type: agenda
date: 2026-08-26
status: in-progress
owner: 원장
priority: P0
tags: [oral-medicine, opmd, leukoplakia, lichen-planus, bms, ras, sinusitis, chairside]
source_wiki:
  - wiki/overviews/oral-medicine-decision-ladder.md
  - wiki/oral-medicine/opmd/pimenta-barros-2025-leukoplakia-malignant-transformation-sr-ma.md
  - wiki/oral-medicine/opmd/sapkota-2024-oral-leukoplakia-recurrence-malignant.md
---

# Goal

`oral-medicine-decision-ladder`(inbound 28)를 체어사이드 도구로 전환한다.

# 형태 판단 — 도메인 전체가 비어 있다

앞의 넷과 완전히 다르다. **구강내과 도메인에 임상 인터랙티브가 0개다.** 7축(OPMD·OLK·OLP·BMS·RAS·OMS·수포궤양) 전부가 미커버이고, 각 축이 독립적인 감별·처치 사다리를 갖는다.

→ 산출물은 **주소(chief presentation) 기반 라우터 + 축별 사다리**. 환자가 무엇을 호소하는지 고르면 그 축의 처치 사다리 전체가 열린다.

# 계산 가능한 지점 — OLK 위험 층화

축2가 상대위험을 전부 보유해 **실제 층화가 가능하다** [확인]:

| 인자 | RR | 출처 |
|---|---|---|
| 비균질형(NHOL) | **4.23** (95% CI 3.31–5.39) — 가장 강력한 단일 임상 예측인자 | Pimenta-Barros 2025 |
| 설측연 부위 | 2.09 (1.48–2.95) · 절대 MT **12.71%** | Pimenta-Barros 2025 |
| 이형성(OED) 존재 | 2.75 (2.26–3.35) | Pimenta-Barros 2025 |
| 재발 OL | **7.39** | Sapkota 2024 |

**주의**: 이 RR들을 곱해 단일 점수를 만들지 않는다. 서로 독립이라는 근거가 없고, 곱셈은 위키에 없는 주장이다. 각 인자를 <b>나란히 표시</b>하고 최고 위험 인자로 조치를 결정한다.

# Output

- `interactives/2026-08-26_oral-medicine-decision-tool.html`

# Done Criteria

- [ ] 주소 6종 라우터 (백색병소·망상미란·작열감·재발궤양·단측부비동·수포궤양)
- [ ] OLK 위험 층화 — 4개 RR 나란히 + 최고 위험 기반 조치
- [ ] OLP — 형태별 처치 + **악성전환 0.5–1.4% 과대인식 경고** + 전신 동반질환 OR
- [ ] BMS — 2차 원인 배제 체크리스트 우선 + 단계별 약물
- [ ] RAS — minor/major/herpetiform + thalidomide 안전 게이트(임신 절대금기·25mg sweet spot·VAS 개선 없음)
- [ ] OMS — 단측 의심 → CBCT → 원인치아 → ENT
- [ ] 수포궤양 — PHGS·herpes labialis·EM·cGVHD 분기 + SJS/TEN 응급 감별
- [ ] 근거 강도 표기 (OLP 스테로이드는 Cochrane이지만 certainty 낮음)

# Notes / Decisions

- 2026-08-26: **RR을 곱하지 않는다.** 독립성 근거가 없고 곱셈 결과는 위키에 없는 수치다. 나란히 보여주고 판단은 술자에게 남긴다.
- 2026-08-26: OLP 악성전환은 **과대 인식 경고를 명시**한다 — 오버뷰가 "진정한 위험 0.5–1.4%, 과대 위험 인식 회피"라고 못박았다. 도구가 위험을 부풀리면 불필요한 생검·불안을 만든다.
- 2026-08-26: thalidomide는 **임신·가임기 여성 절대 금기**를 게이트로 건다. 효능이 좋아도(완전반응 RR 6.95) 이 게이트 없이 제시할 수 없는 약이다.
