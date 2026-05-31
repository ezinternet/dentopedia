---
title: "ISQ-Loading Threshold Calculator (Obsidian wrapper)"
type: interactive
date: 2026-05-25
status: draft
agenda: agenda/2026-05-25_q2-clinic-sop-dbbm-isq.md
source_wiki:
  - wiki/implants/isq/bavetta-2024-isq-osstell-osseo-device-comparison.md
  - wiki/implants/isq/andersson-2019-rfa-factors-5year-neoss-survival.md
  - wiki/sinus-lift/lateral/allurkar-2025-implant-stability-residual-bone-macrodesign.md
tags: [isq, chairside-calculator, custom-frames-wrapper, 2026-q2]
---

# ISQ-Loading Calculator

Obsidian 안에서 chairside calculator를 직접 띄우는 wrapper. 본체는 같은 폴더의 [`2026-05-25_isq-loading-threshold-calculator.html`](2026-05-25_isq-loading-threshold-calculator.html).

## Calculator (embed)

```custom-frames
frame: ISQ Calculator
height: 900px
```

> Custom Frames plugin Settings에서 Frame name이 **ISQ Calculator** 와 정확히 일치해야 함.
> 안 보이면 vault reload (Cmd+R) 또는 plugin toggle off/on.

## 사용 가이드

1. **4방향 ISQ 입력** — 근·원·협·설. 1방향만 평균과 ≥10 차이 시 자동 재측정 권고.
2. **측정 기기 선택** — Osstell이 우리 클리닉 기본. 외부 의뢰 case에서 Osseo 사용 시 자동 +3 보정 ([[implants/isq/bavetta-2024-isq-osstell-osseo-device-comparison|Bavetta 2024]]).
3. **시점·술식·잔존골·bone type** 입력 — MSFA·즉시식립·GBR은 임계값 +2~3.
4. **결과** — green(부하 OK) / yellow(추가 healing) / red(원장 보고) 권고.

## 임계값 근거

| 시점 | 권고 ISQ | 출처 |
|---|---|---|
| 식립 직후 (즉시·조기 부하 후보) | ≥70 | Andersson 2019 |
| 식립 직후 (표준 healing OK) | 65–69 | 일반 가이드라인 |
| 식립 직후 (부하 보류) | <65 | Case 1 학습 (2026-05) |
| MSFA·GBR | +3 보정 | [claude해석] augmented bone safety margin |
| Bone type IV | +2 보정 | Allurkar 2025 macro-design 데이터 |

## 책임 한계

본 도구는 의사결정 보조용. 최종 부하 결정은 원장. ISQ 단일 지표가 아닌 PD·BoP·mobility·CBCT 결과와 함께 판단.

## 모바일 사용 (iPad)

[미검증] Custom Frames plugin은 데스크톱 우선 지원. iPad Obsidian에서 작동 여부 확인 필요. 만약 iPad에서 frame이 안 뜬다면:
- Safari 북마크로 file:// 또는 로컬 HTTP 서버 사용
- 또는 HTML 본문을 markdown 안에 inline `<iframe srcdoc="...">`로 embed (script 제한 주의)

## Related

- [[agenda/2026-05-25_q2-clinic-sop-dbbm-isq]] — Q2 SOP 갱신 hub agenda
- [[slides/2026-05-25_hygienist-training_isq-stability-and-dbbm]] — 위생사 교육 deck (Part 5 시나리오에서 본 calculator 참조)
- [[note-meeting/2026-05-25_clinical-team-case-conference]] — Case 1 ISQ 58 실패 학습이 본 SOP 임계값 65의 근거
