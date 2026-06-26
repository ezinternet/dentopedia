---
title: "치과 방사선 조사량 비교 인터랙티브"
type: agenda
date: 2026-06-26
status: in-progress
source_wiki:
  - wiki/overviews/dental-imaging-effective-dose-background-equivalent-overview.md
  - wiki/radiology/lee-2021-dental-imaging-doses-web-dose-calculator.md
  - wiki/radiology/benchimol-2018-collimation-panoramic-effective-dose-reduction.md
  - wiki/radiology/stervik-2024-radiation-exposure-during-orthodontic-treatment.md
  - wiki/radiology/yeh-2018-estimated-radiation-risk-cancer-dental.md
output_wiki: []
---

## Goal

치과 방사선 기기별 유효선량(µSv)을 흉부 PA X선과 비교하는 인터랙티브 HTML 제작.
환자 설명용이 아닌 임상 레퍼런스 / wiki OPERATIONS 산출물.

## Input

- `wiki/overviews/dental-imaging-effective-dose-background-equivalent-overview.md` (primary)
- `wiki/radiology/lee-2021-dental-imaging-doses-web-dose-calculator.md` — 구내 1.32 / 파노라마 17.93 / CBCT 121.09 µSv, 배경 3110 µSv/yr
- `wiki/radiology/benchimol-2018-collimation-panoramic-effective-dose-reduction.md` — 파노라마 17.6 µSv
- `wiki/radiology/stervik-2024-radiation-exposure-during-orthodontic-treatment.md` — 측방두부 환산, 5-10일 보정
- `wiki/radiology/yeh-2018-estimated-radiation-risk-cancer-dental.md` — CBCT 소형 FOV ~31 µSv
- 흉부 X선 50 µSv: NRPB/IAEA 외부 참조값 (corpus 외, 비교 맥락용)

## Output

- `interactives/2026-06-26_dental-radiation-dose-comparison.html`

## Done criteria

- [x] 로그 스케일 바 차트 (8개 모달리티 + 흉부 X선 기준선)
- [x] 단위 토글: µSv / 자연방사선 일수 / 흉부 X선 배수
- [x] 클릭-상세 카드 (선량범위, 자연방사선 환산, 흉부 배수, 출처)
- [x] corpus 외 참조값 명시
- [x] git push → Quartz 배포
