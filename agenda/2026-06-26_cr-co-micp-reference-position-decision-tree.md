---
title: "CR vs CO/MIP 기준위 선택 결정 트리 인터랙티브"
type: agenda
date: 2026-06-26
status: done
owner: 원장
priority: P2
tags: [occlusion, centric-relation, reference-position, decision-tree]
source_wiki:
  - wiki/overviews/cr-co-micp-reference-position-debate.md
output_wiki:
  - wiki/overviews/cr-co-micp-reference-position-debate.md
---

# Goal

교합 재건 시 기준위(중심위 CR / 중심교합 CO vs 최대교두감합위 MIP/ICP)를 chairside에서 즉시 판단할 수 있도록, CR/CO/MICP 논쟁 종합 overview의 4-노드 결정 경로를 인터랙티브 결정 트리로 구현.

# Input

근거 wiki 페이지:

- wiki/overviews/cr-co-micp-reference-position-debate.md — 4-노드 decision path + Evidence Map (1차 입력)
- wiki/occlusion/kattadiyil-2021-relationship-centric-occlusion-maximal-intercuspal.md — 전악수복 CO 권고
- wiki/occlusion/zonnenberg-2021-centric-relation-critically-revisited-clinical.md — 건강 유치악 MIP 수용
- wiki/occlusion/goldstein-2022-centric-relation-needed-reference-position.md — CR 유지 근거
- wiki/occlusion/fornai-2022-centric-relation-matter-form-substance.md — 과두 모니터링 / Reference Position, 활주 2mm 컷오프
- wiki/occlusion/fukushima-2016-controversy-with-respect-occlusion.md — 불안정 과두 → 근육 유도 ICP
- wiki/tmj/radej-2023-condylar-displacement-malocclusion-cr-mip-sr.md — hyperdivergent 위험인자

# Output

- interactives/2026-06-26_cr-co-micp-reference-position-decision-tree.html

산출물 frontmatter 동등 메타에 `agenda:` 백링크 포함.

# Done Criteria

- [x] 4-노드 결정 경로(전악수복 여부 → 과두 안정성 → 활주<2mm/무증상 → 측정 표준화)를 단계별 인터랙티브로 구현
- [x] 각 결과(권고 기준위)에 근거 논문 inline 표기 + DOI
- [x] Quartz 다크/라이트 호환 (CSS 변수, 인라인 스타일)
- [x] 시작으로 리셋 가능
