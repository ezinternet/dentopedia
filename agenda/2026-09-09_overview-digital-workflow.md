---
title: "digital-workflow 카테고리 unsynthesized 논문 종합 (주간 overview 제안 → go)"
type: agenda
date: 2026-09-09
status: review
owner: 원장
priority: P2
deadline:
tags: [digital-workflow, intraoral-scanner, overview-synthesis, weekly-review]
source_wiki:
  - wiki/digital-workflow/lee-2019-full-mouth-rehabilitation-reduced.md
  - wiki/digital-workflow/oguz-2026-trueness-precision-intraoral-scanners-3d-printed.md
  - wiki/digital-workflow/ramos-morro-2026-patient-perception-reliability-reproducibility-chairside.md
  - wiki/digital-workflow/schlenz-2022-transfer-accuracy-digital-conventional-full-arch.md
output_wiki:
  - wiki/overviews/digital-workflow-decision-ladder.md
---

# Goal

`digital-workflow` 카테고리의 unsynthesized 논문(2026-09-05 스크립트 스냅샷 기준 5편, nav-index 제외 실 4편)을
기존 `wiki/overviews/digital-workflow-decision-ladder.md` 축1(IOS 정확도)에 종합해 category-overflow 신호를 해소.

# Input

- wiki/digital-workflow/lee-2019-full-mouth-rehabilitation-reduced.md — 전악 디지털 워크플로우 증례보고
- wiki/digital-workflow/oguz-2026-trueness-precision-intraoral-scanners-3d-printed.md — 클리어얼라이너 부착물 3D프린팅 모형 IOS 5종 trueness/precision in-vitro
- wiki/digital-workflow/ramos-morro-2026-patient-perception-reliability-reproducibility-chairside.md — IOS vs 전통인상 정확도·chairside time·환자편의 SR (10편)
- wiki/digital-workflow/schlenz-2022-transfer-accuracy-digital-conventional-full-arch.md — 고정성 교정장치 유무별 전악 전이정확도 in-vitro (IOS 5종 vs 알지네이트)
- wiki/overviews/digital-workflow-decision-ladder.md — 종합 대상 기존 overview (축1 IOS 정확도)

# Output

- wiki/overviews/digital-workflow-decision-ladder.md (수정 — 신규 파일 생성 안 함, 아래 Notes 참조)

# Done Criteria

- [x] 4편 모두 `[[wikilink]]`로 wiki/overviews/ 어딘가에 연결됨 (category-overflow.py 재실행으로 확인)
- [x] 축1 IOS 정확도 표에 schlenz-2022·oguz-2026 반영
- [x] ramos-morro-2026(환자경험·chairside time SR)의 "정확도 혼재하지만 시간·편의는 일관 우위" 축을 본문에 반영
- [x] 확신도 태그([확인]/[미검증]) 적용
- [x] Related Papers "신규 추가 (2026-09)" 섹션에 3편 백링크 추가 (lee-2019은 기존 추가분)
- [ ] qmd update && qmd embed 재인덱싱 (사람 확인 대기 — 사용자 세션에서만 실행 가능한 도구일 경우 스킵하고 표기)

# Notes / Decisions

- 2026-09-09: **스냅샷 stale 발견.** 초기 제안(2026-09-05 로그)은 digital-workflow unsynth=5(nav-index 포함, 실 4편)로 1위 보고했으나, "go" 실행 시점 재확인 결과 `lee-2019-full-mouth-rehabilitation-reduced`가 이미 다른 세션에서 decision-ladder에 링크되어 있었음(파일 내 "신규 추가 (2026-09)" 섹션, 정확한 날짜 미기재). 재실행 결과 전체 121개 카테고리 중 ≥5 후보 0개 — living document 특성상 스냅샷과 실행 시점 사이 상태가 이미 갱신됨. **판단**: 남은 실제 unsynthesized 3편(oguz-2026·ramos-morro-2026·schlenz-2022)을 종합하는 원래 목표는 여전히 유효(사용자가 이미 go 승인)하므로 스코프를 3편으로 축소해 계속 진행.
- 2026-09-09: **신규 overview 대신 기존 페이지 확장.** research 결과 `wiki/overviews/digital-workflow-decision-ladder.md`가 이미 IOS 정확도(축1)를 28편 기준으로 종합 중인 living 문서. 신규 freestanding overview를 만들면 repo의 "Single source of truth — Never a second copy" 원칙(CLAUDE.md) 위반 및 축1과의 내용 중복/drift 위험. 3편을 기존 축1에 합류시키는 방식으로 진행.

# References

- logs/2026-09-05_category-overflow.log — 원 스냅샷 (stale)
- logs/2026-09-09_category-overflow.log — go 실행 시점 재확인 (0/121 candidates)
- [[overviews/digital-workflow-decision-ladder]]
