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
- [x] **git push** — pilot 3-tier+SOP는 이미 원격 동기(`origin/main`=로컬 HEAD `114105e`, ahead/behind 0/0, 2026-06-19 확인). 이번 세션 agenda 갱신 커밋만 로컬 ahead → **데스크톱에서 push 1회 필요**(이 샌드박스는 SSH 키 없어 push 차단, HTTPS read만 가능).
- [ ] skill 3파일 로컬 설치 — **BLOCKED(데스크톱 작업)**: skill 파일이 이 세션 환경(repo·uploads)에 없고, Claude Desktop 사용자 skill 폴더는 샌드박스에서 비접근. Settings > Capabilities 또는 폴더 직접 복사로 본체에서.
- [ ] `python3 scripts/sweep_state.py init` → `.surveillance/` 생성 — **BLOCKED**: 스크립트 로컬 부재(위 설치 선행).
- [x] 첫 sweep 기능 검증 — 정식(state.json) 절차는 설치 후. 대신 **수동 sweep 1회로 메커니즘 검증 완료**(아래 Notes 2026-06-19 sweep): 4세분 [tiab]+edat 쿼리 동작, IUD 노이즈 1건 정상 차단, dedup 9건 전부 신규, OA 태깅 완료.
- [x] OA 보류 2건 처리 결정 — **둘 다 폐기/보류 확정**. Unpaywall 재확인 결과 41456794·40553084 모두 `oa_status: closed`, repository copy 없음, PMC 없음 → 합법 OA 전문 경로 부재(아래 Notes).

# Notes / Decisions

- 2026-06-19: IIP 쿼리 풀어쓰면 노이즈 유입(32건 중 12건 osseodensification·ridge mesh 등 무관). `[tiab]` phrase 필수 → topic-queries.md 반영.
- 2026-06-19: implant 4세분 확정 — iip/loading/soft-tissue/grafting, 연 물량 실측 20/25/18/36 (grafting은 sinus 분할 여지).
- 2026-06-19: PubMed가 IIP를 `Immediate Dental Implant Loading[MeSH]`로 색인 → 식립/즉시부하 섞임, abstract에서 재분리 필요.
- 2026-06-19: PDF OA 경로 우선순위 — 출판사 직접(BMC counter/pdf) > EuropePMC `?pdf=render` 미러 > PMC. PMC 직접은 JS 인터스티셜, Wiley는 봇 차단(둘 다 curl 실패), EuropePMC 미러로 우회 성공.
- 보류: 41456794·40553084는 PMC 없음 → Unpaywall/self-archive 미탐색 상태로 큐 보류. 불법 경로 금지.
- skill은 자동 cron 아님 — 정기 자동화 원하면 launchd 별도(미구현).

## OA 보류 2건 결정 (2026-06-19, Cowork 세션)

Unpaywall API 재조회로 합법 OA 경로 부재 확정. 둘 다 PMC ID 없음(convert_article_ids 미반환).

- **41456794** Wang 2025, *J Stomatol Oral Maxillofac Surg* (Elsevier), DOI 10.1016/j.jormas.2025.102697 — IIP vs delayed under periodontitis 9-RCT MA. Unpaywall `oa_status: closed`, `oa_locations: []`, `has_repository_copy: false`. → **결정: 보류(abstract-only 승격 가능)**. MA라 근거등급 높고 abstract에 효과크기 다수 포함(PD MD 0.32 / mSBI 0.29 / mPLI 0.61 / success RR 1.74). 합법 전문 미확보라 정식 ingest 불가, 단 [[immediate-implant/...]] 보강용으로 Step 1-T `full_text:false` abstract-only 페이지 후보로 보존.
- **40553084** Khalifah 2026, *Int J Oral Maxillofac Implants*(JOMI/Quintessence), DOI 10.11607/jomi.11388 — DET vs ridge-splitting, narrow-ridge IIP, RCT n=40 단일저자. Unpaywall `closed`, repository copy 없음. abstract에 정량 수치(MBL 값 등) 미기재. → **결정: 폐기(drop)**. 단일저자 신규 술식·niche·closed·정량 부족으로 위키 증분가치 낮음. 큐에서 제거.
- 출처: PubMed / Unpaywall (2026-06-19 조회). 불법 경로 미사용.

## 수동 sweep 1회 결과 (2026-06-19, skill 미설치 → MCP 직접)

implant 4세분 `[tiab]` phrase + `datetype=edat`(2026/06/01–06/19) PubMed sweep. state.json 없어 last-run은 pilot 기준 임시 창. dedup: 기존 sources DOI grep — 9건 전부 신규. **정식 큐(.surveillance/queue.md)는 skill 설치 후 enqueue.** 아래는 다음 ingest 후보(OA 태깅 포함):

| PMID | 토픽 | 유형 | 핵심 | OA | 우선순위 |
|---|---|---|---|---|---|
| 42312454 | soft-tissue | SR+MA(10 RCT) | abutment 형상이 peri-implant MBL/PD/PES에 유의차 없음(GRADE moderate) | none(Wiley) | ★ 高(근거강) |
| 42298522 | grafting | RCT n=14/28site | prebent Ti mesh vs custom PEEK mesh 수평증대 동등, 부피차는 graft 조성 영향 | PMC13270747 | ★ 高(OA·즉시) |
| 42223759 | grafting | SR(7편) | resorbable scaffold(PLA/PCL/PLGA/β-TCP) ridge aug 대안 가능, 근거 약 | PMC13226745 | 中(OA) |
| 42310175 | surface/soft-tissue | SR(34편) | UV photofunctionalization—biofilm 억제+연조직 부착, 임상은 안정성↑ 신호 | BMC born-OA(추정) | 中 |
| 42226346 | loading | RCT n=72 | 즉시부하 미니임플란트×4 OD가 지연부하 정규×2와 dPRO 동등, 초기 만족↑ | none(Wiley) | 中 |
| 42247033 | grafting | RCT n=24 | bovine block inlay vs onlay—onlay가 수평증대 유의우세, 수직 동등 | none(Springer) | 低 |
| 42242697 | grafting | SR(53편) | alloplastic vs auto/allo/xeno graft—우월 결론 불가, BCP 최다연구 | none(JOI) | 低 |
| 42255765 | (tissue-level) | 증례+SR | smooth-collar zygo/pterygoid 무이식 full-arch 100% 단기생존 | PMC13235772 | 低(증례) |
| 42291880 | grafting | narrative | NovaBone bioactive glass 기전·임상—제품 narrative | PMC13262605 | 低(narrative) |

- 노이즈 차단 검증: iip 쿼리 1건(42266170)이 산부인과 IUD "immediate placement" — 정상적으로 비치과로 식별·제외. `[tiab]`+abstract 재선별 동작 확인.
- 다음 ingest 권장 순서: 42312454(SR+MA) → 42298522(OA RCT) → 42223759/42310175(OA SR). OA:none 4건은 PDF 확보 후.

# References

- SOP.md §1-bis Literature Surveillance
- [[overviews/immediate-implant-conditions]]
- [[overviews/robotic-vs-navigation-implant-accuracy]]
