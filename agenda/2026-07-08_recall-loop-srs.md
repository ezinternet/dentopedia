---
title: "리콜 루프 (SRS) — 검색되는 지식을 인출되는 지식으로"
type: agenda
date: 2026-07-08
status: in-progress
source_wiki:
  - wiki/overviews/sinus-lift-technique-selection.md
---

# Goal
제안 C. 위키는 2,645편을 *찾을* 수 있지만(QMD retrieval) 진료 중 *떠올리는*(retention) 루프가 없다 = Anki 격차. overview마다 3문항 리콜 스펙을 만들고, Leitner 간격반복으로 주 1회 인출 세션을 돌려 지식을 챗사이드 인출 가능 상태로 굳힌다.

# 왜 별도 레이어인가
기존 `interactives/quiz-specs/`(환자 자가테스트)·`lectures/quiz-specs/`(강의 확인)와 다르다: 저건 *남을* 교육하는 일회성 퀴즈, 이건 *원장 본인*의 간격반복 기억. 그래서 `recall/` 뱅크 + 박스 상태를 분리한다.

# 구조 (Rule #1 준수 — 문항 저작은 LLM-in-the-loop, 스케줄·선별은 스크립트)
```
recall/{overview-stem}.json      # overview당 3문항 (q/opts/ans/rat/cite) — LLM이 overview 근거로 저작
recall/_state.json               # Leitner 박스 상태 {stem::qid: {box, due, last}}
scripts/recall-session.py        # --due N (오늘 볼 문항) / --grade (정오답→박스 이동) / --stats
scripts/recall-coverage-lint.py  # recall 스펙 없는 overview = 기억 백로그 신호 (daily-audit 편입)
```
Leitner 간격: box 1→3→7→16→35일. 정답=박스+1(상한), 오답=box 1로 리셋.

# Output
- agenda/2026-07-08_recall-loop-srs.md (이 파일)
- recall/sinus-lift-technique-selection.json (첫 스펙 — dogfood)
- scripts/recall-session.py, scripts/recall-coverage-lint.py
- daily-audit.py에 recall-coverage 편입
- 주간 스케줄 task `weekly-recall`

# Done 기준
- [x] recall-session.py --due / --grade / --stats 동작 확인 (Leitner 박스 이동 검증: 정답→box+1, 오답→box1)
- [x] recall-coverage-lint.py 실행 + daily-audit 편입 (신호: 1/213 리콜화, 212 백로그)
- [x] 첫 리콜 스펙(sinus-lift) 3문항, 모든 수치 overview 대조
- [x] weekly-recall 스케줄 생성 — 일요일 20:00 (2026-07-08)

# 운영 원칙
- 문항은 overview가 새로 만들어질 때 3개씩 저작(ingest의 Why-Ingested처럼 forward-only, 소급 백필 없음).
- 주간 세션은 위생사 교육과 겸용 가능하나 난이도는 원장용(수치·임계값 직행).
- 백로그 신호는 gate 아님 — 신호만(위키 철학).
