---
title: "감사 커버리지 갭 — Gemini 파이프라인 건전성 프레임워크 대조"
type: agenda
date: 2026-11-15
status: in-progress
owner: 원장
priority: P2
tags: [audit, quality-assurance, pipeline-health]
source_wiki: []
---

# Goal

Gemini가 제안한 논문 위키 파이프라인 건전성 9항목 프레임워크를 현재 26개 감사 체계와 대조해, 커버됨·갭·자동화 가능 여부를 분류하고 신규 감사 스크립트 2개의 명세를 작성한다.

# Input

- `AUDITS.md` — 현재 26개 감사 목록 및 설계 근거
- `scripts/daily-audit.py` — 감사 실행 목록 (정본)
- Gemini 9항목 프레임워크 (2026-11-15 붙여넣기, 아래 §원문 첨부)

# Output

- [x] `AUDITS.md` §커버리지 갭 섹션 추가 (2026-11-15)
- [ ] `scripts/parse-gap-flag-audit.py` — 항목 2 커버 (파싱 결측 플래그)
- [ ] `scripts/source-provenance-lint.py` — 항목 3+5 커버 (Provenance + Limitations)

# Done Criteria

- [ ] 9항목 전체가 "커버됨 / 자동화불가 / 신규스크립트" 중 하나로 분류됨
- [ ] 신규 스크립트 2개 명세 완성 (입력·출력·억제 조건)
- [ ] `AUDITS.md`에 갭 섹션 반영
- [ ] `daily-audit.py` AUDITS 리스트에 신규 스크립트 추가 (스크립트 구현 후)

# 갭 분석 요약

현재 26개 감사는 9항목 중 5개를 커버, 4개가 갭이다.

| # | 항목 | 상태 | 담당/제안 |
|---|---|---|---|
| 1 | 수치 원문 일치율 100% | ❌ 자동화 불가 | 수동 샘플링 SOP |
| 2 | 파싱 결측 플래그 | ❌ 신규 가능 | `parse-gap-flag-audit.py` |
| 3 | 출처 위치 Provenance | ❌ 신규 가능 | `source-provenance-lint.py` |
| 4 | 연구 설계 메타데이터 | ✅ 커버됨 | `lint.py` |
| 5 | 한계점 보존 | ❌ 신규 가능 | `source-provenance-lint.py` |
| 6 | 고아 노트 + 깨진 링크 | ✅ 커버됨 | `orphan-check` + `link-integrity` + `synthesis-backlog` |
| 7a | 중복 인제스트 | ✅ 커버됨 | `doi-duplicate-check` |
| 7b | 용어 파편화 | ⚠️ 부분 | 수동 태그 감사 |
| 8 | 상충 근거 병렬 제시 | ⚠️ 부분 | `find-contradiction-candidates` (갭 탐지만) |
| 9 | 코퍼스 외 지식 혼입 | ✅ 커버됨 | `golden-question-check` + `[확인]/[미검증]` |

# 신규 스크립트 명세

## parse-gap-flag-audit.py (항목 2)

**목적**: 최근 N일(기본 30일) 인제스트된 `sources/*.md` 중 `[원문 표 대조 필요]` 플래그가 없는 파일 비율을 보고. 다단 레이아웃·이미지 테이블이 많은 논문(`source_collection: pubmed-abstract` 또는 `pmc-empty-fulltext` 계열)에서 플래그 의무화 여부를 확인.

**입력**: `sources/*.md` frontmatter (`date:`, `source_collection:`)  
**출력**: 최근 N일 인제스트 중 플래그 없는 파일 목록 + 비율  
**억제**: `source_collection: pubmed-text`이고 본문 길이 ≥ 2000자 → 추출이 충분했을 가능성이 높으므로 INFO로만  
**타입**: signal (non-blocking)

## source-provenance-lint.py (항목 3+5)

**목적**: `sources/*.md`에 (A) `## Limitations` 섹션이 존재하는가, (B) 주요 결론 문장에 `(Results §...)` 또는 `(Table X)` 형태의 출처 주석 비율. 둘 다 없으면 WARN.

**입력**: `sources/*.md` 본문  
**출력**: Limitations 섹션 없는 파일 목록 + 출처 주석 미달 파일 목록  
**억제**: `evidence_level: in-vitro` / `animal` / `narrative-review` — 임상 결과 테이블이 없는 연구 유형은 Limitations 체크만  
**타입**: signal (non-blocking)  
**주의**: False positive 가능성 높음 — 오래된 인제스트(2026-05-27 이전)는 별도 집계

# 수동 샘플링 SOP (항목 1 — 자동화 불가)

**빈도**: 주간 신규 인제스트의 10% 무작위 추출 (약 1~3편/주)  
**절차**:
1. `git log --since="1 week ago" sources/ --name-only | grep ".md" | shuf -n 3`으로 대상 추출
2. `papers/{stem}.pdf` Results 섹션을 직접 열어 $n$, $p$-value, 주요 수치를 `sources/{stem}.md`와 대조
3. 불일치 발견 시 `python3 scripts/log-deviation.py data-integrity "{stem}" "수치 불일치: sources에 X, PDF에 Y"`
4. `deviation-audit.py`가 `data-integrity` 유형 ≥3건 시 Rule-of-Three trigger → SOP 개정 후보

# Notes / Decisions

- 2026-11-15: Gemini 프레임워크는 "[합의수준]" / "[근거강함]" / "[gemini해석]" 태그로 출처를 구분함. "[gemini해석]"은 추론이므로 위키 의사결정에 직접 반영하지 않고 SOP 개선 아이디어로만 활용.
- 2026-11-15: `source-provenance-lint.py` 구현 시 오래된 인제스트 소급 적용은 하지 않음 — signal-not-gate 원칙, 소급하면 한꺼번에 300건+ 경고 발생.
- 2026-11-15: 항목 7b(용어 파편화)는 현재 코퍼스 규모(≈1,300편)에서 false positive가 많아 자동화 ROI가 낮음. 태그 감사는 카테고리 신설·인제스트 서베일런스 시점에 수동으로.

# 원문 — Gemini 프레임워크 (2026-11-15)

> 아래는 붙여넣기 원문 그대로 보존. 이 프레임워크 자체는 "[gemini해석]" 태그 항목을 포함하므로 사실 주장으로 직접 인용하지 않는다.

논문 정리 및 문답 파이프라인의 건전성은 개별 요약문의 유창함이 아니라, **수치 보존 무결성·근거 위계 구분·코퍼스 참조 일관성·검색 정밀도**라는 4가지 영역의 정량적 통과 기준으로 검증해야 합니다.

**9항목 (축약):**

1. 핵심 수치의 원문 일치율 100% — 표본 10~20편, $n$/$p$/CI/결과 대조, 군 뒤섞임 0건
2. 파싱 결측 시 `[원문 표 대조 필요]` 명시적 플래그
3. 출처 위치(Provenance) 즉각 추적 — 섹션명·표 번호 병기
4. 연구 설계 메타데이터 분리 — SR/RCT/코호트/증례/in vitro 명확 분류
5. 조건부 결론 및 한계점 보존 — Discussion 단서 조항 별도 항목
6. 고아 노트 5% 미만 + 깨진 링크 0건
7. 중복 인제스트 없음 + 용어 파편화 통제
8. 상충 근거 병렬 제시 — 한쪽만 단정하지 않음
9. 코퍼스 외 지식 혼입 차단 — 근거 부재 선언

# References

- [[agenda/2026-05-26_synthesis-enforcement-setup]]
