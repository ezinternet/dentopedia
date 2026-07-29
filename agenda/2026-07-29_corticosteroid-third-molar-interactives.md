---
title: "사랑니 발치 코르티코스테로이드 — 비교 매트릭스 + 처방 결정 트리 인터랙티브"
type: agenda
date: 2026-07-29
status: done
source_wiki:
  - wiki/drug/analgesics/buyukkurt-2006-prednisolone-diclofenac-third-molar-rct.md
  - wiki/drug/analgesics/ibikunle-2016-prednisolone-qol-third-molar-rct.md
  - wiki/drug/analgesics/gholami-2021-methylprednisolone-masseter-gluteal-third-molar-rct.md
  - wiki/drug/analgesics/larsen-2021-methylprednisolone-doses-split-mouth-rct.md
  - wiki/drug/analgesics/singh-2023-dexamethasone-vs-methylprednisolone-third-molar-sr-ma.md
  - wiki/drug/analgesics/liborio-2025-methylprednisolone-third-molar-sr-ma.md
  - wiki/drug/analgesics/tamgadge-2025-preoperative-dexamethasone-third-molar-pain-swelling-trismus.md
  - wiki/drug/analgesics/costa-2015-preemptive-nsaids-third-molar-pain-meta.md
  - wiki/overviews/drug-analgesics-postop-pain-overview.md
tags: [corticosteroid, third-molar, dexamethasone, methylprednisolone, prednisolone, interactive, chairside]
---

# Agenda: 사랑니 발치 코르티코스테로이드 인터랙티브 2종

> **소급 작성 (retroactive)**: 두 인터랙티브는 2026-07-29 코르티코스테로이드 M3 인제스트(커밋 `785aca5`)와 함께 먼저 만들어졌고, agenda 명세가 누락돼 `operations-lint`에서 frontmatter 없음으로 걸렸다. 이 파일은 그 산출물을 규정된 cross-link 구조에 소급 편입하기 위한 명세다. 아래 Goal·Output은 실제로 만들어진 결과물을 기술한다.

## Goal

사랑니(제3대구치) 발치 시 코르티코스테로이드 처방 결정을, 위키가 보유한 RCT·SR/MA 근거만으로 체어사이드에서 즉시 참조 가능한 형태로 만든다. 두 개의 서로 다른 질문에 답한다:

1. **"어느 약을, 얼마나?"** — 약물·용량·경로 간 비교 (비교 매트릭스)
2. **"이 환자에게 쓸 것인가?"** — 증례 조건에 따른 분기 (결정 트리)

## Input

`wiki/drug/analgesics/` 의 코르티코스테로이드 M3 근거 — 개별 RCT(Buyukkurt 2006, Ibikunle 2016, Gholami 2021, Larsen 2021)와 종합(Singh 2023 SR+MA, Libório 2025 SR+MA, Tamgadge 2025), 그리고 선제 진통 비교축으로 Costa 2015.

## Output

- `interactives/corticosteroid-third-molar-comparison.html` — 약물 비교 매트릭스 (덱사메타손·메틸프레드니솔론·프레드니솔론 × 용량·경로·시점 × 통증/부종/개구제한 결과)
- `interactives/third-molar-drug-protocol-decision-tree.html` — 처방 프로토콜 결정 트리

## Done 기준

- 두 HTML이 `interactives/`에 존재하고 `agenda:` 백링크를 가진다
- 인터랙티브가 인용하는 모든 저자-연도가 `source_wiki`의 실존 위키 페이지로 추적된다
- `operations-lint` 통과
