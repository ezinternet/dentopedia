---
title: "편측저작 부하→치조골 밀도 기전 — 인터랙티브 HTML"
type: agenda
date: 2026-06-14
status: done
owner: 원장
priority: P2
tags: [interactive, unilateral-mastication, alveolar-bone, mechanobiology]
source_wiki:
  - wiki/overviews/unilateral-mastication-occlusal-load-alveolar-bone-density.md
  - wiki/implants/lee-2018-unilateral-mastication-bone-density-alveolus.md
  - wiki/bone-biology/chen-2023-occlusal-force-alveolar-bone-type-h-angiogenesis.md
  - wiki/bone-biology/xu-2016-sclerostin-wnt-occlusal-hypofunction-alveolar-bone.md
  - wiki/bone-biology/liu-2015-occlusal-hypofunction-recovery-mandibular-alveolar-bone-rats.md
  - wiki/occlusion/hayashi-2014-low-level-laser-periodontal-hypofunctional-teeth.md
agenda:
output_wiki:
---

# Goal

편측저작에서 "왜 작업측 치조골이 더 단단한가"의 조직학적 기전(PIEZO1 → sclerostin/Wnt → osteoblast/osteoclast 균형 → type H 혈관)을 **부하 ON/OFF 토글**로 직접 비교·애니메이션하는 교육용 인터랙티브 HTML. 강의·환자설명·전공의 교육용.

# Input

- wiki/overviews/unilateral-mastication-occlusal-load-alveolar-bone-density.md — 6편 종합 thesis (틀)
- wiki/implants/lee-2018-unilateral-mastication-bone-density-alveolus.md — 인체 CBCT 정량 데이터 (HU 표)
- wiki/bone-biology/chen-2023-occlusal-force-alveolar-bone-type-h-angiogenesis.md — type H 혈관·PIEZO1/SLIT3 기전
- wiki/bone-biology/xu-2016-sclerostin-wnt-occlusal-hypofunction-alveolar-bone.md — sclerostin/Wnt/RANKL 분자 서명
- wiki/bone-biology/liu-2015-occlusal-hypofunction-recovery-mandibular-alveolar-bone-rats.md — 가역성
- wiki/occlusion/hayashi-2014-low-level-laser-periodontal-hypofunctional-teeth.md — 회복(LLLT)

# Output

- interactives/2026-06-14_unilateral-mastication-bone-mechanism.html

# Done Criteria

- [x] 부하 ON(작업측) ↔ OFF(비작업측) 토글로 캐스케이드 상태 전환
- [x] sclerostin·Wnt·파골세포·type H 혈관 4경로가 토글에 따라 시각 변화 (배지 valence색 통일)
- [x] 골소주 밀도 시각화(촘촘 ↔ 성김) + HU 지표 변화 (513↔409, 게이지)
- [x] Lee 2018 좌우 HU 표 inline 포함 (★하악 대구치 최대차 강조)
- [x] 근거 논문 6편 출처 표기 (확신도: 동물·전임상 명시 + caveat)
- [x] HTML frontmatter에 agenda·source_wiki 백링크 박힘 (operations-lint 0 에러)
- [x] preview 검증 (ON/OFF 토글 작동 확인)
- [x] 커밋 + 푸시

# Notes / Decisions

- 2026-06-14: show_widget SVG 다이어그램을 standalone 인터랙티브로 확장. 핵심 메시지 = "같은 스위치가 부하 유무로 반대 작동" + "치조골(load-positive)과 과두는 별개 축". 한계(설치류·전임상, PDL 중심이라 임플란트 직접적용 주의) 명시.

# References

- [[agenda/_template.md]]
- [[wiki/overviews/unilateral-mastication-occlusal-load-alveolar-bone-density]]
