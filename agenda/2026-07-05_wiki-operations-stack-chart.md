---
title: "5-레이어 운영 스택 차트 (\"오늘은 어제 위에 쌓인다\") 제작"
type: agenda
date: 2026-07-05
status: done
source_wiki:
  - index.md
output_wiki: []
---

# Goal

사용자가 보여준 참고 이미지("오늘은 어제 위에 쌓인다" — 5개 운영 레이어 누적 stacked-area 차트, 04-08~05-08 예시)를 llm-wiki 실제 저장소 구조·git 히스토리에 맞게 재구성해 `interactives/`에 추가. 다른 저장소의 레이어 이름(AGENTS.md 룰, 분석 스펙·TSV)을 그대로 베끼지 않고 llm-wiki에 실제로 존재하는 5개 레이어로 매핑.

# Input

- `git log --diff-filter=A --name-only --date=short` — papers/sources, wiki/overviews, scripts, agenda, logs 각 경로의 최초-추가일 (실측, 2026-05-18 repo init ~ 2026-07-05 현재)
- `git log --format=%ad -- CLAUDE.md` — CLAUDE.md 수정 커밋 누적 (운영 규칙 개정 횟수 proxy)
- 기존 `interactives/2026-06-22_wiki-evolution-v4.html` — CSS 변수·tooltip·legend·frontmatter 컨벤션 재사용

# Output

- `interactives/2026-07-05_wiki-operations-stack.html`

# 레이어 매핑 (사용자 확인 완료)

| 레이어 | 실측 소스 | 2026-07-05 누적 |
|---|---|---|
| Papers · sources | `sources/*.md` 최초 추가일 | 2,385 |
| 구조 · overviews | `wiki/overviews/*.md` 최초 추가일 | 194 |
| 운영 규칙 (CLAUDE.md) | `CLAUDE.md` 수정 커밋 누적 | 37 |
| 일일 운영 루프 (scripts) | `scripts/*.py` 최초 추가일 | 37 |
| 작업 스펙 (agenda+logs) | `agenda/*.md` + `logs/*.md` 최초 추가일 | 62 |

스케일 차이(2,385 vs 37, ~65배)로 절대값 그대로 쌓으면 4개 레이어가 안 보여서, 사용자 확인 하에 **레이어별 정규화(0~100%, 자기 최종값 대비) 후 스택**하는 방식 채택. 절대 누적 수치는 hover 툴팁에 그대로 노출.

# Done Criteria

- [x] 5개 레이어 실측 데이터로 생성 (하드코딩 추정치 없음)
- [x] 정규화 스택 방식 + 절대값 tooltip 병기
- [x] 기존 wiki-evolution 시리즈와 동일한 frontmatter/CSS 컨벤션
- [x] `interactives/index.html`은 build-interactives-index.py가 자동 반영 (수기 편집 불필요)

# Notes / Decisions

- 2026-07-05: 원본 참고 이미지의 날짜 범위(04-08~05-08)·레이어 이름(AGENTS.md 룰, 분석 스펙·TSV)은 다른 저장소/예시 목업으로 판단, llm-wiki 실제 git 히스토리(2026-05-18 repo init ~ 07-05, 48일, 5,520 커밋)로 대체.
