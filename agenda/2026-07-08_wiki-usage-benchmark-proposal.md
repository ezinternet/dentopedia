---
title: "위키 활용법 벤치마킹 & 통합 활용 제안"
type: agenda
date: 2026-07-08
status: draft
# 메타 아젠다 — 특정 paper가 아니라 시스템 전체 운영을 대상으로 함.
# 근거 grounding: 아래 '실측 현황'의 daily-audit 로그 + repo 상태.
source_wiki:
  - wiki/index.md
output_wiki:
  - wiki/overviews/  # 제안 D·E가 생성/갱신 대상
---

## 한 줄 진단

**입력 엔진(ingest → source → wiki → overview → QMD → 15종 audit)은 완전 포화 상태로 외부 어떤 개인 지식관리 사례보다 앞서 있다. 반대로 출력(Express)·기억(retention)·임상 역류(clinic feedback) 세 레그가 비어 있어, 2,446편의 지식이 진료·강의·환자설명·기억으로 전환되는 비율이 극단적으로 낮다.** 활용법 제안의 핵심은 "더 많이 넣기"가 아니라 "쌓인 걸 꺼내 쓰는 세 개의 파이프라인을 새로 놓기"다.

이 요청이 제대로 처리되었다면 → ① 외부 사례 대비 내 시스템의 앞선 점·빈 곳이 명시되고, ② 죽은 자산이 이름으로 지목되고, ③ 실제 진료 루틴에 꽂을 수 있는 통합 시나리오가 우선순위와 함께 나와 있어야 한다.

---

## 1. 실측 현황 (2026-07-08 기준, repo 직접 스캔)

| 레이어 | 규모 | 상태 신호 |
|---|---|---|
| papers (PDF 1,730 + txt 716) | 2,446편 | 최근 7일 신규 204편 — 주간 ingest 폭 매우 큼 |
| sources | 2,419편 | synthesis-backlog: **100% linked, unsynthesized 0, stale 0** |
| wiki 페이지 | 2,645편 | lint/orphan/coverage 전부 green |
| overviews | 213편 | overview-coverage: WARN 0, healthy(cov≥60%) 174 |
| category-overflow | 86개 카테고리 | 후보 **0개** (≥5 미합성 카테고리 없음) |
| **interactives** | 53개 | 살아있음 (Class A 자동갱신 + Class B staleness 신호) |
| **slides** | **5개** | ← 지식 대비 극빈 |
| **peer-review** | **1개** | ← 사실상 미가동 |
| **note-meeting** | **1개 + 템플릿** | ← 임상 역류 체인 설계돼 있으나 미사용 |

핵심 비대칭: KNOWLEDGE 레이어는 5,000편 규모까지 무리 없이 굴러가는 반면, OPERATIONS의 산출(slides·peer-review·meeting)은 지식량의 0.2% 수준만 전환되고 있다.

두 번째 신호: **모든 입력 audit가 0/green으로 포화됐다.** 이건 좋은 소식이지만 동시에 audit가 더 이상 압력을 만들지 못한다는 뜻 — 신호 재조준이 필요하다 (제안 E).

---

## 2. 외부 사례 벤치마킹 — 앞선 점 / 빈 곳

내 시스템을 5개 표준 프레임에 대보면:

**① Karpathy LLM-wiki (원형)** — 원형은 `PDF → summary → page` 단일 계층이 전부다. 내 시스템은 여기에 overview 합성 계층, typed-relations, supersession(living-document), 로컬 하이브리드 검색(QMD), 15종 audit를 얹어 **원형을 한참 초과**했다. 벤치마킹 대상이라기보다 이미 그 위에 있다.

**② Zettelkasten (Luhmann)** — 원자 노트 + 링크에서 구조가 창발. 고전 Zettelkasten은 링크에 의미를 안 붙이지만, 내 시스템은 `extends/reinforces/contradicts/refines/applies-to` **타입드 엣지로 한 단계 더 구조화**돼 있다. overview = Luhmann의 structure note에 정확히 대응. → **앞서 있음.**

**③ Second Brain / CODE (Tiago Forte)** — Capture·Organize·Distill·**Express** 4단계. 앞 3개(C·O·D)는 만점인데 **Express(꺼내 쓰기)만 비어 있다.** 이 프레임이 1번의 비대칭을 그대로 설명한다. 내 시스템의 유일하고 명확한 구조적 결손.

**④ Anki / Spaced Repetition** — 검색으로 *찾을* 수는 있지만(retrieval) 챗사이드에서 *떠올리는*(retention) 루프가 없다. quiz interactive 몇 개(halitosis·listerine·zirconia quiz)와 `quiz-specs`가 씨앗은 있으나 체계적 SRS는 부재. → **명확한 빈 곳.**

**⑤ Evergreen notes / Digital garden (Andy Matuschak)** — "노트는 계속 갱신되는 상록수"라는 원칙을 supersession + 배너 + decay-audit로 **기계검증까지 구현** — 대부분의 디지털 가든보다 앞서 있다. 다만 evergreen의 다른 축인 "노트를 남에게 보여주며 사고를 다듬는다(public thinking)"는 Quartz 사이트가 있음에도 미활용.

**요약**: 구조·검색·갱신은 세계 최고 개인 사례 수준. 빈 곳은 딱 세 군데 — **Express(출력), Retention(기억), Public/Clinic feedback(역류)**.

---

## 3. 활용도 진단 — 살아있는 자산 vs 죽은 자산

**살아있는 것**: ingest 파이프라인, QMD 검색, daily/weekly audit, interactives(chairside 계산기·결정트리), overview 합성. 이 루프는 매주 스스로 돈다.

**죽어 있거나 미활용**:
- `note-meeting/` — 케이스 컨퍼런스 1건 후 정지. **임상 케이스 → output_wiki → overview 역류 체인이 설계만 되고 안 돎.** 진료실에서 나온 실제 판단이 위키로 안 올라온다.
- `peer-review/` — 1건. 저널 리뷰 의뢰가 오면 위키가 최강 무기인데 폴더가 비어 있음.
- `slides/` 대 overview = 5 : 213. 강의 자산화율 2.3%.
- **입력 audit 포화** — synthesis-backlog·category-overflow가 0에 붙어 더 이상 할 일을 알려주지 않음. 신호가 침묵.
- **retention 부재** — 2,645편을 "안다"가 아니라 "찾을 수 있다". 진료 중 즉시 인출은 별개 문제.

---

## 4. 워크플로우 통합 제안 (진료 루틴에 꽂는 6개 시나리오)

### A. 예약 연동 아침 브리핑 ★킬러
매일 아침 `dentweb appointmentList`로 오늘 진료를 당겨 → 각 술식 키워드로 QMD 질의 → 해당 overview + 이번 주 뒤집힌/충돌 페이지(weekly-digest·contradiction-radar)를 3줄로 요약. "오늘 상악동 케이스 2건 → 최근 감염소켓 즉시식립 SR+MA 2편이 판도 바뀜" 식. `schedule` 스킬 + dentweb + QMD 결합. **입력 엔진을 진료 시점에 붙이는 유일한 다리.**

### B. Express 레그 상설화 (overview → 산출물)
overview 1편이 완성되면 자동으로 파생 후보를 띄운다: 위생사 매뉴얼(번호 체크리스트) / 환자 설명 카드(산문+괄호 평어) / 세미나 슬라이드. 213편 중 강의·교육 수요 높은 상위 20편부터 월 4편 페이스로 전환. agenda 체인 그대로 사용.

### C. 챗사이드 기억 루프 (Anki 격차 메우기)
신규 overview마다 `quiz-specs` 포맷으로 3문항 자동 생성 → 주 1회 리콜 세션(위생사 교육과 겸용 가능). 검색되는 지식을 인출되는 지식으로. 이미 quiz interactive 인프라 있음 → SRS 스케줄만 추가.

### D. 임상 역류 체인 부활 (note-meeting)
케이스 컨퍼런스 1회 = note 1개 → `output_wiki:`에 갱신할 페이지 → 필요시 `followup_agenda:` → 신규 overview. 진료실 판단이 위키 근거를 *반박·한정*하는 순간을 `relations: contradicts/refines` 엣지로 남기면, 내 임상경험이 문헌과 같은 층위에 축적된다. **이게 남들이 절대 못 만드는 자산.**

### E. Signal 재조준 — 출력 커버리지 audit 신설
입력 신호가 포화됐으니 거울을 출력으로 돌린다. `synthesis-backlog`(source→overview 미연결)의 출력판: **overview 중 downstream 산출물(slide/interactive/patient-card)이 0인 페이지**를 신호로. 이러면 daily-audit가 다시 "이번 주 꺼내 쓸 것"을 알려준다.

### F. Public thinking — Quartz 사이트 활용
`ezinternet.github.io/dentopedia` 가 이미 배포 중. overview를 블로그/스터디 공유용으로 노출하면 evergreen의 마지막 축(공개 사고)까지 닫힌다. 우선순위는 낮음(사생활·환자정보 마스킹 재확인 필요).

---

## 5. 우선순위

**Now (2주 내)** — A(예약 연동 브리핑, 효용 최대·구현 작음) + E(출력 커버리지 신호, 스크립트 1개).
**Next (1~2개월)** — B(Express 상설화 월 4편) + C(리콜 루프, 위생사 교육 겸용).
**Later** — D(역류 체인은 케이스 컨퍼런스 재개 의존) + F(공개).

가장 큰 레버는 A와 B다: A는 쌓인 지식을 *매일 진료에* 꽂고, B는 *강의·교육 자산*으로 복리를 만든다. 나머지는 이 둘을 보강한다.

---

## Done 기준
- [x] A: 아침 브리핑 스케줄 태스크 가동 — `morning-clinic-brief`, 평일 07:55 (2026-07-08)
- [x] E: 출력 커버리지 audit — `scripts/output-coverage-lint.py` 작성 + daily-audit 편입 (2026-07-08). 첫 실행: overview 213편 중 31편(14.6%)만 산출물화, 182편 uncovered.
- [x] B: 전환 상위 리스트 산출 — E 로그 `logs/2026-07-08_output-coverage.log` 허브순 상위(sinus-lift-technique-selection 30, immediate-implant-decision-ladder 28, implants-isq-stability-ladder 26 …). 월 4편 전환은 진행형.
- [ ] C: 신규 overview 3문항 quiz 자동생성 + 주간 리콜 세션 정례화
- [ ] D: 케이스 컨퍼런스 재개 시 note-meeting→output_wiki 체인 1회 완주

## F. 배포 사이트(ezinternet.github.io/dentopedia) 활용 — 확인·제안
- 배포 범위 확인: `deploy-pages.yml`이 **wiki/ + interactives/ + lectures/만** 서빙. note-meeting/agenda/sources/dentweb은 배포 제외(+ quartz ignorePatterns 이중방어) → 환자정보 유출 경로 구조적으로 차단됨.
- 1급 가치 = **맥 밖 인출 경로**. Obsidian·QMD는 맥 전용이라, 진료실 아이패드·폰·Boox에서 2,645편 + chairside 계산기에 접근하는 유일한 길. 상위 decision-ladder·계산기를 모바일 홈화면 북마크.
- interactives는 이미 `/interactives/`로 verbatim 배포 → 환자 앞 화면공유(consent-guide·방사선 선량 비교)·QR 상담실 비치.
- B가 만든 slide는 `/lectures/`로 자동 공개 → 세미나·위생사 교육 배포 URL이 공짜로 생김.
- 역할 분담: 정밀 합성검색은 맥 QMD, 빠른 체어사이드 인출은 사이트. 재확인: 사이트 public 유지 의도가 맞는지(동료 유입 원치 않으면 noindex).

## 재확인 포인트
- A의 dentweb 자동 조회는 환자 식별정보 마스킹(userPreferences) 하에서만. 브리핑은 술식·카테고리 레벨로만 집계.
- B·C·D 각각은 별도 agenda로 분기해 실행 (이 파일은 상위 명세).
