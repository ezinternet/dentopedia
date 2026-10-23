# Vasovagal Syncope — Surveillance 2026-10-23

Mode: **루틴 백필** (신규 토픽 2개 시드). PubMed MCP 미연결 → NCBI E-utilities 직접 호출(`esearch`/`esummary`/`efetch`, OA 판정은 Europe PMC REST).

PubMed queries:
- `vasovagal-syncope` (치과 앵커): VVS 코어 phrase 7종 AND 치과 앵커 15종 — **78건** (전 기간)
- `vasovagal-guideline` (GUIDE 축): 코어만, `Guideline`/`Practice Guideline` — **10건**
- 합집합 **88건** (중복 0)

노이즈 실측:
- 느슨한 앵커(`dent* OR oral`) + ptyp(RCT/SR/MA/GUIDE) = 37건 → **실제 치과 문헌 2건**. `oral[tiab]`이 "oral midodrine"·"oral rehydration salts"를 끌어온 탓. 앵커를 완전형 phrase로 조이면 78건(전 ptyp)으로 정제.
- VVS 코어 단독(`vasovagal[tiab]`) = 4,774건 → 치과 앵커 없이는 감시 불가.
- ptyp를 켜면 치과 축이 78 → **6건**으로 붕괴(증례·서술 리뷰가 대부분) → 이 토픽만 ptyp 비움.

QMD·grep 커버리지 체크: `wiki/` 내 VVS 언급 9페이지 — `malave-2022`(기전·예방·처치 주력), `smereka-2019`(발생률 46.3%), `jevon-2020`(아나필락시스 감별), `bina-2018`·`becker-2012`·`zhou-2023`(LA 알레르기·약리), 오버뷰 2건(부분 언급). 2026-10-22 인터랙티브 `interactives/2026-10-22_vvs-vasovagal-syncope-mechanism.html`이 기전·감별·프로토콜을 이미 시각화.

---

## Already Ingested (skip)

| PMID | Stem | 근거 |
|---|---|---|
| 30843612 | smereka-2019-preparedness-and-attitudes-towards-medical | `wiki/drug/systemic-disease/` (PMID 필드 일치) |
| 29952645 | bina-2018-true-allergy-amide-local-anesthetics-case | `wiki/local-anesthesia/` (PMID 필드 없음 — 제목 교차 확인) |

`seen_pmids`·큐에 VVS PMID는 사전에 0건이었다(이 토픽이 첫 sweep). 따라서 dedup은 `seen`이 아니라 **wiki PMID/제목 교차**로 수행 — 위 2건이 그 결과다.

---

## Ingested This Session

없음 — 이번 세션은 **큐 적립까지**(surveillance 경계). 인제스트는 `ingest-paper` 5단계로 별도 실행.

---

## Enqueued (26, OA:PMC 15)

### Tier A — 감시의 목적 자체 (최우선 ingest)

| PMID | Stem suggestion | Journal / Year | OA | Key finding |
|---|---|---|---|---|
| 41640727 | li-2026-syncope-dentistry-risk-prevention-management | J Dent Anesth Pain Med 2026 | PMC12865304 (CC BY-NC) | 치과 실신 총론 최신 리뷰 — 위험인자·예방·처치를 한 편으로 갱신. **malave-2022(시술 통증 클리닉)의 치과판 대응물** |
| 41857549 | zouaghi-2026-recurrent-vasovagal-syncope-tooth-extraction | BMC Oral Health 2026 | PMC13126704 (CC BY) | 동일 세션 내 **재발** VVS 증례 — 1회 진정으로 끝나지 않는 케이스의 처리 |
| 37379085 | sanuki-2023-hypotension-without-skin-symptoms-anaphylaxis-vasovagal | Anesth Prog 2023 | PMC10328191 (OA 아님·PMC 열람) | LA 후 **피부증상 없는 저혈압** = 아나필락시스 vs VVS 감별 (jevon-2020의 ABCDE 감별을 좁히는 축) |
| 40729568 | mcallister-2025-local-anesthetic-systemic-toxicity-or-vasovagal-syncope | Am J Ther 2025 | none | LAST vs VVS 감별 — 아나필락시스 3자 감별축 완성 |
| 37589875 | hockin-2023-pain-intravascular-instrumentation-orthostatic-tolerance-rct | Clin Auton Res 2023 | none | **RCT** — 주사 통증 자체가 기립내성을 떨어뜨려 VVS를 유발(니들 공포증 없는 건강 성인). "통증 → 반사" 인과를 무작위로 지지. 이 축의 유일한 RCT |
| 39110332 | wang-2024-chinese-pediatric-neurally-mediated-syncope-guideline | World J Pediatr 2024 | PMC11502568 (CC BY) | 소아·청소년 NMAS 2024 개정 가이드라인(진단·치료) |
| 28280231 | shen-2017-acc-aha-hrs-syncope-guideline | Circulation 2017 | none | 실신 평가·관리의 표준 — **심장성 실신 감별**의 상위 규범. 동일 가이드라인 8개 재게재 중 canonical |

### Tier B — 치과 고유 기전·예방 술기

| PMID | Stem suggestion | Journal / Year | OA | Key finding |
|---|---|---|---|---|
| 24456612 | rashad-2013-extraction-bradycardia-case-crossover | Head Face Med 2013 | PMC3854007 (CC BY) | 발치 중 심박수 실측 case-crossover — 단순 발치에서도 유의한 서맥 |
| 36051807 | agarwal-2022-trigeminocardiac-reflex-maxillary-third-molar | Natl J Maxillofac Surg 2022 | PMC9426688 (CC BY-NC-SA) | 상악 제3대구치 발치 중 **삼차신경-심장반사(TCR)** — VVS와 기전이 다른 감별·처치 축 |
| 19815349 | arakeri-2010-trigeminocardiac-reflex-hypothesis-syncope-extraction | Med Hypotheses 2010 | none | "발치 중 실신 = TCR" 가설 원논문 |
| 36874341 | [author]-2023-leg-raise-leg-fold-syncope-extraction | Cureus 2023 | PMC9982758 (CC BY) | 발치 중 **leg raise / leg fold** 예방 pilot — 체위 중재를 치과에서 직접 시험 |
| 36995954 | shiraishi-2023-lidocaine-tape-venipuncture-vasovagal-syncope | Anesth Prog 2023 | PMC10069530 (PMC 열람) | 3시간 리도카인 테이프로 채혈 VVS 예방(증례군) — 치과마취과 세팅 |
| 30511415 | gebhardt-2019-anxiolytic-premedication-vasovagal-intrathecal | Acta Anaesthesiol Scand 2019 | none | 항불안 전처치가 VVS를 15%→7.5%로 낮춘 후향 — malave-2022가 인용한 Gebhardt 2018의 **원 데이터**에 해당 |
| 41523572 | kawauchi-2025-vasovagal-syncope-sinus-arrest-venipuncture | Cureus 2025 | PMC12790449 (CC BY) | 정신과 다약물 환자에서 채혈 유발 VVS + **동정지(sinus arrest)** — "양성"이라는 통념의 반례 |

### Tier C — 증례·발생률·소아 (맥락 보강)

| PMID | Journal / Year | OA | 한 줄 |
|---|---|---|---|
| 10397654 | Oral Surg Oral Med Oral Pathol 1999 | none | 심장이식 환자의 치과 시술 중 VVS — Bezold-Jarisch 탈신경 심장 논증 |
| 1437055 | Oral Surg Oral Med Oral Pathol 1992 | none | 발치 중 VVS 16례에서 **저혈당**이 유발인자 |
| 23635903 | Pediatr Dent 2013 | none | 7세 소아 신경심장성 실신 증례 |
| 19284194 | Gen Dent 2008 | none | 소아·청소년 VVS 리뷰(치과) |
| 16756240 | Dent Update 2006 | none | "malignant VVS" — 반복 실신으로 치료 연기·심장내과 의뢰 |
| 37244725 | Dent Clin North Am 2023 | none | 중증 불안 + 실신력 환자의 보철 치료 (case-based) |
| 33968415 | Acute Med Surg 2021 | PMC8088391 (CC BY-NC-ND) | 치과 관련 응급 발생률·특성 단일기관 후향 |
| 34178562 | Plast Reconstr Surg Glob Open 2021 | PMC8225362 (CC BY-NC-ND) | LA 주사 후 "adrenaline rush" vs VVS 발생률 |
| 39034210 | Int Dent J 2025 | PMC11806336 (CC BY-NC-ND) | 레바논 치과의사 응급 준비도 전국 설문(smereka-2019의 2025년 대응물) |
| 42056033 | Zhonghua Kou Qiang Yi Xue Za Zhi 2026 | none | 구강응급실 중증 케이스 후향(중국어) |
| 27688429 | Acta Stomatol Croat 2016 | PMC5017275 (PMC 열람) | 소아치과 응급 리뷰 |
| 34453905 | J Oral Maxillofac Surg 2021 | none | Brugada 증후군 구강외과 perioperative 관리 — **심장성 실신** 감별 |

---

## Screened Out — Not Enqueued (62)

복구 가능 버킷(`.surveillance/screened-out.md`, `restore-screened`로 되살림). 묶음별 사유:

| 묶음 | n | 사유 |
|---|---|---|
| 부인과·비뇨기과·유방·혈관·기타 시술 | 25 | office hysteroscopy·prostate/breast/thyroid biopsy·WALANT·endovenous laser·port implantation — 치과 VVS에 전이되는 고유 근거 없음 |
| 술자 준비도 설문·시뮬레이션 훈련 | 10 | VVS가 부수 항목. 발생률 축은 smereka-2019 + 39034210으로 대표됨 |
| 2017 ACC/AHA 가이드라인 중복 게재 | 5 | canonical 28280231만 유지 |
| 심장내과 치료·기전(비치과) | 8 | pacing·cardioneuroablation·etilefrine/atenolol trial·tilt test·ACR imaging |
| 기타 감별·인접 | 9 | LAST/알레르기 리뷰 중복(Baluga 2건), 편두통·척추마취 증례, 안검성형 VVS 심정지(비치과), 폐동맥고혈압 증례, IV 진정 회복기 심정지, atropine bronchoscopy |
| 이미 위키 보유 | 2 | 30843612(smereka-2019), 29952645(bina-2018) |

**주의**: "비치과" 사유로 버린 40385074(안검성형 중 VVS→심정지), 30883228(IV 진정 회복기 31초 심정지)는 치과 응급 프로토콜의 **반례 데이터**로 가치가 있다. 치과 VVS 오버뷰를 쓸 때 `restore-screened`로 되살릴 후보.

---

## Coverage Assessment

현재 위키의 VVS 커버리지(2026-10-23 기준):

| 축 | 커버 | 공백 |
|---|---|---|
| 기전(Bezold-Jarisch) | malave-2022 + 2026-10-22 인터랙티브 | **TCR(삼차신경-심장반사)** — 이번 큐의 36051807·19815349로 채워짐 |
| 발생률 | smereka-2019(46.3%) | 치과 시술 단위 발생률(발치·주사별) — 정량 데이터 여전히 없음 |
| 감별 | jevon-2020(아나필락시스), bina-2018(LA 알레르기) | **LAST**·**심장성 실신** — 40729568·37379085·28280231로 채워짐 |
| 예방 | malave-2022(진정·항무스카린·수액, 시술통증 맥락) | **체위 중재(leg raise/fold)** — 36874341 |
| 처치 프로토콜 | 인터랙티브 + malave-2022 | 치과 전용 알고리듬 문헌 — 41640727이 최신판 |
| 소아 | 없음 | 39110332·19284194·23635903 |

**판단**: 이 백필로 "VVS는 왜 생기고 어떻게 감별하며 무엇을 하나"의 축은 닫힌다. 남는 진짜 공백은 **치과 시술별 정량 발생률**과 **glycopyrrolate 예방의 치과 RCT** — 후자는 존재 자체가 확인되지 않았다(malave-2022도 "no study"로 명시). 백필로는 채울 수 없는 축이므로, 이후 sweep은 이 두 축의 신규 등재만 감시하면 된다.

## 검증 메모

- OA 라벨은 Europe PMC `license`/`isOpenAccess` 기준. PMC는 있는데 OA가 아닌 3건(10328191·10069530·5017275)은 `OA:none`으로 적립 — PMC 웹 열람은 가능하나 재배포 라이선스 없음.
- `https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi`는 2026-10-23 현재 **404**(폐기). OA 판정은 Europe PMC REST로 대체할 것.
- PMID 41640727은 2026-02 게재(JDAPM) — 이 위키의 VVS 지식 기준일을 2026년으로 끌어올리는 논문이므로 Tier A 최우선.

---

## Addendum (2026-10-23) — Tier B/C 처리 + 증분 sweep

| 구분 | 결과 |
|---|---|
| Tier B (7편) | **전량 인제스트 완료** — rashad-2013, agarwal-2022, arakeri-2010, bhagat-2023, shiraishi-2023, gebhardt-2019, kawauchi-2025 |
| Tier C 중 선별 2편 | **추가 인제스트** — 39034210(choufani-2025, 레바논 전국 설문, PMC 전문), 34453905(dellolio-2021, Brugada 구강외과, abstract-only) |
| Tier C 잔여 | 10편 `[ ]` 유지 (증례·발생률 보강 성격, 우선순위 낮음) |
| 오버뷰 | `wiki/overviews/dental-vasovagal-syncope-overview.md` — 18편 종합 (1차 13편 → 2차 18편) |
| 증분 sweep | `edat 2026-10-20~` 재검색: 치과 앵커 **0건**, 지침 축 **0건** → 반영할 신규 문헌 없음 |

**Tier C 선별 근거**: 39034210은 smereka-2019와 동일 도구 계보의 독립 전국 표본으로 "VVS 1위"를 재현했고(161명 중 56.5%), 34453905는 심장성 실신 감별축에 채널병증(Brugada)이라는 구체적 의뢰 경로를 추가한다. 나머지 Tier C는 개별 증례·발생률 맥락 보강이라 오버뷰의 결론을 바꾸지 않는다.

**남은 공백(변동 없음)**: ① 치과 시술별 정량 발생률, ② 예방적 글리코피롤레이트의 치과 RCT(존재 미확인).

---

## Addendum 2 (2026-10-23) — Tier C 종결 (잔여 10편 → 8 인제스트 / 2 스킵)

앞선 addendum에서 "우선순위 낮음, 결론을 바꾸지 않는다"고 남겨둔 Tier C 10편을 실제로 처리했다. 결과적으로 **결론이 바뀌었다** — 가장 큰 이유는 33968415 하나다.

| PMID | 페이지 | 판정 | 핵심 |
|---|---|---|---|
| 33968415 | obata-2021-medical-emergencies-dental-treatment-incidence | 인제스트(전문) | 치과 외래 **1,146,929방문 중 응급 42건(0.0037%)**, VVS 26건(61.9%), 발치 45.2%, 술전·술중·술후 17·12·13, 90.5% 당일 귀가 |
| 34178562 | greene-2021-adrenaline-rush-vasovagal-la-injection | 인제스트(전문) | 2% 리도카인+에피 1:100,000, n=387(비치과): 아드레날린 러시 2.2% vs 미주신경성 1.8% |
| 42056033 | liu-2026-oral-emergency-critical-cases-retrospective | 인제스트(초록) | 구강응급실 중증 92예: 출혈 38.0%·심혈관 23.9% > VVS 13예(14.1%), 구조 성공 91.3% |
| 10397654 | montebugnoli-1999-vasovagal-syncope-heart-transplant-dental | 인제스트(초록) | 탈신경 심장 3례: SBP 137→76 mmHg, HR 96.7→102.6/분 — **서맥 없는 혈관억제형** |
| 1437055 | salins-1992-hypoglycemia-vasovagal-syncope | 인제스트(초록) | 발치 중 실신 16명, 실신 시점 혈당 < 회복 후 — 역인과 가설 |
| 16756240 | sharma-2006-malignant-vasovagal-syncope | 인제스트(초록) | 21세 남 반복 실신 → 경사검사 무수축 = 악성 VVS → 디소피라미드+인공심박동기 |
| 19284194 | kapusta-2008-vasovagal-syncope-children-adolescents | 인제스트(초록) | 소아 VVS 고찰, **소아 발생률 자료 희박** 명시 |
| 27688429 | vranic-2016-medical-emergencies-pediatric-dentistry | 인제스트(초록) | 소아 응급 병인 분류(수치 없음) |
| 23635903 | ross-2013-neurocardiogenic-syncope-child-dental-case-review | **스킵** | 초록 2문장, 임상상·처치 기술 없음 → 패딩 방지 |
| 37244725 | mistry-2023-severe-anxiety-fainting-dental-restoration | **스킵** | 초록이 프레이밍만(불안척도·감시·진정 선택·결과 없음) → 기존 li-2026·zouaghi-2026과 중복 |

**오버뷰 영향(18 → 26편)**:
1. §1 역학이 "분모 없음"에서 **세 층의 분모**로 바뀌었다 — 방문 단위 0.0037%(obata, 하한) / 응급 삽화 중 비율 46.3–61.9% / 응급실 중증 14.1%(liu). 기존 공백 1번은 "시술 1건당 발생률"로 정밀화.
2. §2-1에 **탈신경 심장 자연실험**(montebugnoli)을 추가 — "VVS = 서맥" 등식이 깨지고, 혈관억제형에서는 아트로핀이 아니라 에페드린 갈래라는 처치 연결이 생겼다.
3. §3의 저혈당 행이 "위키에 없음" → 근거 있는 행으로 교체(salins), 아드레날린 러시 행 신설(greene).
4. §6·§7에 **의뢰 상한선**(sharma, 인공심박동기)과 반복 실신 규칙 추가.
5. 소아 축 신설(kapusta·vranic) — 결론은 "수치 없음", 즉 공백을 명시적으로 등재.

**정정**: 이전 addendum의 "Tier C 잔여는 결론을 바꾸지 않는다"는 판단은 **틀렸다**. 발생률 논문 1편이 역학 절의 구조를 바꿨으므로, 남은 큐도 "결론 무영향" 가정으로 미루지 않는다.
