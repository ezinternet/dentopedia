---
title: "골질 양극단(골다공증·골경화성 병변) 임플란트 전략 매트릭스 인터랙티브"
type: agenda
date: 2026-06-09
status: done
owner: 원장
priority: P2
tags: [implant, osteoporosis, osteosclerosis, bone-quality, mronj, decision-matrix, interactive]
source_wiki:
  - wiki/implants/kim-2026-dental-implant-osteoporosis-osteosclerosis.md
  - wiki/overviews/drug-mronj-antiresorptive-overview.md
output:
  - interactives/2026-06-09_bone-quality-extremes-implant-matrix.html
---

# Goal

골다공증(저밀도)과 5종 골경화성 병변(고밀도/병적 골)에서 임플란트 식립 가부·술기·추적 프로토콜을 한 화면에서 비교하는 단일 HTML 결정 매트릭스. 병태를 선택하면 성공률·핵심 리스크·수술 술기·추적 권고를 카드로 표시.

# Input

- wiki/implants/kim-2026-dental-implant-osteoporosis-osteosclerosis.md — 주 데이터(병변별 성공률, 골다공증 단기/장기 생존율, 비스포스포네이트 drug holiday)
- wiki/overviews/drug-mronj-antiresorptive-overview.md — MRONJ·항흡수제 맥락

# Output

- interactives/2026-06-09_bone-quality-extremes-implant-matrix.html

# Done Criteria

- [x] 7개 병태(골다공증 + COD·condensing osteitis·idiopathic osteosclerosis·cementoblastoma·hypercementosis) 카드
- [x] 각 카드: 성공률 수치·핵심 리스크·술기 포인트·추적 권고
- [x] 저밀도 vs 고밀도 축 시각 구분
- [x] 출처 inline + 확신도 태그(narrative-review, 근거 약함 caveat)
- [x] 단일 파일·CDN 없음·한글 sans-serif
- [x] frontmatter agenda/source_wiki 백링크

# Notes / Decisions

- 종설 기반이라 성공률 수치는 선택 바이어스 가능 — 의사결정 보조용이며 환자별 영상·병력 우선 명시.
