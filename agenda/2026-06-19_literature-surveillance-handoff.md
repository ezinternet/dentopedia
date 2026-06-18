---
title: "Literature Surveillance skill 정식 운영 + IIP 2026 파일럿 마무리"
type: agenda
date: 2026-06-19
status: in-progress
owner: 원장
priority: P1
tags: [literature-surveillance, ingest, immediate-implant, skill, handoff]
output_wiki:
  - wiki/immediate-implant/ebrahim-2026-vestibular-socket-therapy-immediate-implant-rct.md
  - wiki/immediate-implant/abdelsameaa-2026-dentine-membrane-eprf-gbr-immediate-implant-rct.md
  - wiki/digital-workflow/nava-2026-guided-surgery-immediate-implant-accuracy-nma.md
---

# Goal

literature-surveillance skill을 정식 운영 체계로 올리고(로컬 설치 → init → 첫 sweep 검증), 이번 IIP 2026 파일럿(3건 ingest)을 git push로 마무리한다. 다음 세션(Cowork 포함)이 이 노트만 읽고 이어갈 수 있게 하는 핸드오프.

# Input

- literature-surveillance skill 3파일 (`SKILL.md` + `scripts/sweep_state.py` + `references/topic-queries.md`) — 현재 다운로드 산출물, **로컬 미설치**
- SOP.md 1-bis 섹션 (surveillance 절차)
- 이번 ingest 3건: ebrahim-2026 / abdelsameaa-2026 (wiki/immediate-implant), nava-2026 (wiki/digital-workflow)

# Output

- Claude Desktop skill 폴더에 `literature-surveillance/` 설치
- `.surveillance/state.json` + `queue.md` (init으로 생성)
- (완료) wiki/sources/papers 3-tier 3건 + index.md 엔트리 + SOP 1-bis

# Done Criteria

- [x] IIP 2026 sweep: 32건 검색 → 진짜 IIP 5건 선별 → PMC OA 3건 ingest
- [x] lint 3종 통과 (frontmatter 0 error / PDF↔sources 1:1 / no-wiki 0)
- [x] SOP.md 1-bis Literature Surveillance 섹션 추가
- [ ] **git push** (이번 wiki/sources/index/SOP 변경분 — papers는 gitignore)
- [ ] skill 3파일 로컬 설치
- [ ] `python3 scripts/sweep_state.py init` → `.surveillance/` 생성
- [ ] 첫 정식 sweep 1회 (`datetype=edat`, 직전 sweep 이후) 검증
- [ ] OA 보류 2건 처리 결정 (41456794 Elsevier MA, 40553084 JOMI RCT)

# Notes / Decisions

- 2026-06-19: IIP 쿼리 풀어쓰면 노이즈 유입(32건 중 12건 osseodensification·ridge mesh 등 무관). `[tiab]` phrase 필수 → topic-queries.md 반영.
- 2026-06-19: implant 4세분 확정 — iip/loading/soft-tissue/grafting, 연 물량 실측 20/25/18/36 (grafting은 sinus 분할 여지).
- 2026-06-19: PubMed가 IIP를 `Immediate Dental Implant Loading[MeSH]`로 색인 → 식립/즉시부하 섞임, abstract에서 재분리 필요.
- 2026-06-19: PDF OA 경로 우선순위 — 출판사 직접(BMC counter/pdf) > EuropePMC `?pdf=render` 미러 > PMC. PMC 직접은 JS 인터스티셜, Wiley는 봇 차단(둘 다 curl 실패), EuropePMC 미러로 우회 성공.
- 보류: 41456794·40553084는 PMC 없음 → Unpaywall/self-archive 미탐색 상태로 큐 보류. 불법 경로 금지.
- skill은 자동 cron 아님 — 정기 자동화 원하면 launchd 별도(미구현).

# References

- SOP.md §1-bis Literature Surveillance
- [[overviews/immediate-implant-conditions]]
- [[overviews/robotic-vs-navigation-implant-accuracy]]
