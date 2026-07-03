---
title: "YYYY년 M월 <미팅 제목 — 예: 케이스 컨퍼런스 / 직원회의 / 분기 SOP 리뷰>"
type: meeting
date: YYYY-MM-DD
status: draft            # draft → in-progress → done → archived
attendees: [원장, 위생사 팀장, 임상위생사, 코디]   # 개인 실명 대신 역할/이니셜만
duration_min: 60
# ─── cross-link (아래 3개 중 최소 하나는 채운다) ───
source_wiki:             # 이 미팅의 결정 근거가 된 위키 페이지
  - wiki/<category>/<stem>.md
output_wiki:             # 이 미팅이 갱신·생성할 위키 페이지 (SOP 등, 예정 포함)
  - # wiki/overviews/<stem>.md   # 필요 없으면 줄째로 삭제
followup_agenda:         # 후속 작업 명세서 (실제로 agenda 파일도 신설할 것)
  # agenda/YYYY-MM-DD_<topic>.md
tags: [meeting, <topic>, YYYY-MM]
---

<!--
작성 규칙 (지우고 써도 됨)
1) 환자·직원 식별정보(이름·연락처·차트번호·생년월일) 평문 금지 → "환자 A", "59세 여", "위생사 L" 등 익명만.
2) 결정에는 근거를 [[category/stem]] 위키링크로 건다. 근거 못 찾으면 "이 결정 근거 위키에서 찾아줘"라고 요청.
3) 근거 확신도 표기: [근거강함] / [합의수준] / [claude해석] 등으로 판단 출처를 구분.
4) Action items는 반드시 [담당자] + 마감일 + (연결 산출물) 형태로.
-->

# Agenda (의제)

1. <의제 1> (___min)
2. <의제 2> (___min)
3. Decision — <결정 안건> (___min)

---

# Case 1 — <제목>

## 환자
- <나이·성별·ASA·주요 전신질환>, <흡연/구강위생 등>
- <치식·시술 이력·재료·수치(ISQ/IT/MBL 등)>

## 논의
- [근거강함] <위키 근거 기반 판단> ([[category/stem|저자 연도]])
- [claude해석] <해석·추론 (근거 약할 때 명시)>

## 결정
- <이 케이스에서 내린 결정 / 프로토콜 트리거>

---

# Decision — <운영·SOP 결정 안건>

## 논의 근거 (요약)
- <핵심 근거 논문 요약> ([[category/stem|저자 연도]])

## 결정
1. <결정 1>
2. <결정 2>

---

# Action items
- [ ] [<담당자>] <할 일> (마감 __/__) → <연결 산출물: slides/interactives/wiki 경로>
- [ ] [<담당자>] <할 일> (마감 __/__)

# Followup
- [[agenda/YYYY-MM-DD_<topic>]] — <후속 작업 hub>
- <다음 미팅에서 재검토할 항목>
