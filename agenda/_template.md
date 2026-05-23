---
title: "<짧고 구체적인 작업명>"
type: agenda
date: YYYY-MM-DD
status: draft          # draft | in-progress | review | done | archived
owner: 원장             # 또는 위생사 팀장, 외부 협업자명
priority:               # P0 | P1 | P2 (선택)
deadline:               # YYYY-MM-DD (선택)
tags: []
---

# Goal

한 문장으로. "무엇을 / 왜 / 누구에게."

예) ISQ 기반 즉시·조기·지연 부하 결정 임계값을 위생사·원장이 chairside에서 즉시 참조할 수 있도록 종합 페이지 + 계산기로 정리.

# Input

근거가 될 wiki 페이지·문서·데이터. 경로 + 한 줄 역할 설명.

- wiki/implants/isq/<stem>.md — <역할>
- wiki/overviews/<related-overview>.md — <역할>
- 외부 자료: <출처> — <역할>

# Output

구체 산출물 파일 경로(들). 만들 위치까지 명시.

- wiki/overviews/<topic>.md
- slides/<date>_<event>_<topic>.md
- interactives/<date>_<topic>.html

각 산출물의 frontmatter에 `agenda: agenda/<this-file>.md` 백링크 박을 것.

# Done Criteria

객관적으로 "완료"라고 판정할 수 있는 조건. 체크박스로.

- [ ] 핵심 임계값·수치 표 1장 (출처 inline citation)
- [ ] 임상 시나리오 walk-through N개
- [ ] 확신도 등급(sr+ma / rct / 합의수준 / claude해석 등) 명시
- [ ] 위생사용 체크리스트 1장 (해당 시)
- [ ] 모든 산출물의 frontmatter에 source_wiki / agenda 백링크 박힘
- [ ] index.md 또는 해당 카테고리 index에 entry 추가

# Notes / Decisions

작업 중 결정 사항·트레이드오프·미해결 질문. 여기서 재사용 가능한 지식이 발견되면 wiki로 승격 후보 표시.

- 2026-MM-DD: <결정 내용 / 변경 근거>

# References

작업 종료 후 backfill. 인용한 외부 자료, 관련 agenda·meeting·overview 링크.

- [[agenda/<related>]]
- [[note-meeting/<related>]]
