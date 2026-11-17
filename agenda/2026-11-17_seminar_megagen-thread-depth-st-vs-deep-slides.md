---
title: "메가젠 ST(기본형) vs Deep Thread 슬라이드"
type: agenda
date: 2026-11-17
status: done
owner: 원장
priority: P1
tags: [thread-depth, megagen, standard-thread, deep-thread, insertion-torque, ISQ, primary-stability, slides, education]
source_wiki:
  - wiki/overviews/megagen-thread-depth-standard-vs-deep-overview.md
  - wiki/implants/isq/kwon-2026-thread-depth-guided-immediate-implant-isq-rct.md
  - wiki/implants/isq/baldi-2018-insertion-torque-isq-tapered-knife-edge.md
  - wiki/implants/khaohoen-2023-biomaterials-dental-implants-bone-density-narrative-review.md
output:
  - slides/2026-11-17_seminar_megagen-thread-depth-st-vs-deep.md
---

# Goal

메가젠 계열 ST(Standard Thread, 기본형) vs Deep Thread 임플란트의 장단점을 근거기반 교육 슬라이드로 정리해 동료 임상의 세미나에서 사용할 수 있게 한다. "토크가 높으면 좋은가?"라는 흔한 오해를 ISQ·각도 정확도·골질 맥락과 함께 바로잡는 것이 핵심 메시지.

# Input

- wiki/overviews/megagen-thread-depth-standard-vs-deep-overview.md — 종합 가이드(선택 트리·근거 한계)
- wiki/implants/isq/kwon-2026-thread-depth-guided-immediate-implant-isq-rct.md — 직접 비교 RCT(n=54, ST vs Deep, 12개월), 토크·ISQ·MBL·각도편차 수치
- wiki/implants/isq/baldi-2018-insertion-torque-isq-tapered-knife-edge.md — 메가젠 AnyRidge >50 Ncm 토크 상한, 실패 분포
- wiki/implants/khaohoen-2023-biomaterials-dental-implants-bone-density-narrative-review.md — 저밀도골(D3/D4) deep thread 권고 지침

# Output

- slides/2026-11-17_seminar_megagen-thread-depth-st-vs-deep.md (Marp, dentopedia theme, 한국어)
- lectures/2026-11-17_seminar_megagen-thread-depth-st-vs-deep.html (export 산출물)
- lectures/2026-11-17_seminar_megagen-thread-depth-st-vs-deep-quiz.html (동반 자가테스트)

# Done Criteria

- [x] 직접 비교표(Kwon 2026): 삽입토크·≥40Ncm·ISQ·MBL·각도편차 수치 인용
- [x] Deep 장점(토크) / 대가(각도) / 무위(ISQ·MBL) 3축 명시
- [x] ~50 Ncm 토크 상한(Baldi 2018) 경고 슬라이드
- [x] 골질 맥락(D3/D4 저밀도)에 따른 방향 역전 슬라이드
- [x] 임상 선택 의사결정 트리(토크 임계 vs 각도 정밀도)
- [x] 근거 한계(메가젠 구체 모델명 미명시, 자금 출처) 명시
- [x] 동반 자가테스트 4문항(정답·해설·근거 링크)
- [x] export → lectures/ → 색인 갱신, lint 0 errors
- [x] 산출물 frontmatter에 source_wiki / agenda 백링크 박힘

# Notes / Decisions

- 2026-11-17: 슬라이드는 Promise/교육용이므로 환자 식별정보 없음. 논문 수치는 위키 확인분만 사용(Rule #1). Kwon 2026의 MST/MDT를 메가젠 특정 SKU로 단정하지 않고 '스레드 깊이 설계'로 서술.
- 2026-11-17: 기존 커밋 미반영 작업이 여러 개 있어, 이번 커밋은 이 agenda·슬라이드·export·quiz·색인 + overview 1개만 명시적으로 stage.

# References

- [[overviews/megagen-thread-depth-standard-vs-deep]]
