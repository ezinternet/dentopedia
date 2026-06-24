---
title: "치과 예약 미내원(no-show) 위험 플래그 도구"
type: agenda
date: 2026-06-25
status: done
owner: 원장
priority: P2
tags: [practice-management, no-show, interactive]
source_wiki:
  - wiki/practice-management/alkhurayji-2024-factors-patient-failure-attend-dental.md
  - wiki/practice-management/khries-2024-identifying-barriers-pediatric-dental-appointments.md
output_wiki:
  - interactives/2026-06-25_dental-no-show-risk-flag-tool.html
---

# Goal

치과 예약 미내원(no-show) 위험 요인을 chairside에서 빠르게 점검하는 **위험 플래그 체크리스트** 인터랙티브를 만든다. 보유 두 논문(alkhurayji-2024 성인·khries-2024 소아)이 **검증된 위험점수·OR·기저율을 제공하지 않으므로**, 확률/점수 계산기가 아니라 "해당 위험 플래그 개수"만 보여주는 정직한 도구로 설계한다.

# Input

- wiki/practice-management/alkhurayji-2024-factors-patient-failure-attend-dental.md — 성인 미내원 1,364건의 인구학적 프로파일(미혼·여성·≤35세·신환·오전). **연관검정 전부 비유의·비교군 없음 → 기저율/RR 산출 불가**
- wiki/practice-management/khries-2024-identifying-barriers-pediatric-dental-appointments.md — 소아 미내원율 44%(85% 보험가입에도); 유의 상관: 연령 P=0.0041, 대중교통 P=0.002; 장벽 빈도(망각 11.2%, 직원 소통오류 10.3% 등)
- wiki/overviews/korean-dental-practice-management-overview.md — 한국 개원 환경 맥락

# Output

- interactives/2026-06-25_dental-no-show-risk-flag-tool.html

frontmatter에 `agenda: agenda/2026-06-25_dental-no-show-risk-flag-tool.md` 백링크 + source_wiki 박을 것.

# Done Criteria

- [x] 성인(alkhurayji)·소아(khries) 위험 플래그를 **시각적으로 분리** (단일 모델로 오인 방지)
- [x] 출력은 "N개 중 M개 플래그 해당" 카운트만 — 확률/0–100 점수 금지
- [x] 각 플래그에 verbatim 통계 + 출처 stem 표기
- [x] 상단 고정 disclaimer: "검증된 위험점수 아님, 2024년 단일기관 2편 기반 descriptive flag"
- [x] 수정 가능 장벽(망각→리마인더, 소통오류→확인콜, 긴 간격→내원주기 단축)에 개입 프롬프트
