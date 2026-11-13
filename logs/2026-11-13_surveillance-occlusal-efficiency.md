# Occlusal Efficiency / 교합저작 효율 — Surveillance 2026-11-13

토픽 키: `occlusal-efficiency` (신규 토픽 · 전 기간 백필)

발단: "글레이징이 교합저작 효율에 영향을 주나" 질문 → 위키에 그 축의 논문이 **0건**임을 확인 → 주제 자체를 토픽으로 등록하고 백필.

---

## 도구 메모 (환경 차이 — 재현 시 주의)

- 이 세션에 **PubMed MCP가 노출되지 않았다**(툴 카탈로그에 PubMed 도구 없음). **NCBI E-utilities**(esearch · esummary · efetch)를 직접 호출 — 동일 백엔드·동일 쿼리 문법.
- **PMC OA 판정**: `oa.fcgi`는 404(폐기). `esummary`의 `articleids[idtype=pmc]`로 대체(배치 150건). 라이선스 필드는 이번엔 미조회(ingest 단계로 이연).
- 신규 토픽이므로 **water-mark 미적용**(`dedup`에 `--watermark` 없이 호출 = 전 기간 백필). 주의: `enqueue`가 seen에 고PMID를 넣어 **water-mark가 다시 올라간다** — 이 토픽의 다음 증분 sweep은 이 값 기준으로 컷된다.

---

## 쿼리 (stem 2개)

| stem | 내용 | hit | 비고 |
|---|---|---|---|
| **A — 효율 어휘 직접** | (`"masticatory efficiency"` · `"masticatory performance"` · `"masticatory ability"` · `"chewing efficiency"` · `"chewing performance"` · `"chewing ability"` · `"food comminution"` · `Masticatory Performance[MeSH]`) AND 치과 문맥 AND **2020–2026[edat]** AND (RCT · SR · MA) | **152** | 창을 좁혀 근거등급 위주 |
| **B — 교합 인자 축** | (`"occlusal contact area"` · `"occlusal contacts"` · `"occlusal scheme"` · `"occlusal design"` · `"food comminution"` · `comminution` · `"chewing cycles"`) AND (masticat* · chew*) AND 치과 문맥, **2005–2026[edat]** | **619** (상위 400 수집) | 도재·치과 문맥 필터 없으면 779 → 식품공학 노이즈 |
| **합집합(중복 제거)** | | **539** | |

**왜 stem A만으로 부족한가**: 효율을 *결과변수*로 쓰지 않고 *교합접촉·교합양식* 쪽에서 접근하는 논문(대부분 치과보철)이 제목에 "masticatory"를 안 쓴다. 반대로 stem B만 쓰면 식품 텍스처·동물 저작 연구가 대량 유입된다 → 치과 문맥 절이 필수.

**ptyp 필터 없음(토픽 `ptyp: []`)**: 이 축은 **관찰·단면·기기검증 연구가 본체**(큐 191건 중 obs 135). RCT/SR/MA만 걸면 계측법·결정인자 논문을 통째로 놓친다. 대신 stem A에만 ptyp를 걸어 근거등급 상층을 확보.

---

## 파이프라인

| 단계 | 건수 |
|---|---|
| 검색 합집합 | 539 |
| − 기보유(위키 제목 교차) | −13 |
| − seen/screened 중복(`dedup`) | −8 |
| 스크리닝 대상 | **530** (efetch 1건 누락) |
| include (큐 적립) | **191** |
| exclude (screened-out 적립, 복구가능) | **326** |

큐 191건 구성: **OA:PMC 62 / OA:none 129**, 유형 obs 135 · RCT 35 · MA 12 · SR 11 · CCT 1. 게재연도 2015–2026(**2020년 이후 145건**).

screened-out 326건 사유 분포: `off-topic (biomechanics/other field)` 176 · `adjacent: no masticatory-efficiency outcome` 130 · `case-report/off-topic subject` 17.

---

## 티어 (ingest 우선순위 — 큐에는 topic만 실리고 티어는 이 표가 정본)

| 티어 | 정의 | 건수 |
|---|---|---|
| **T1** | 저작효율이 **결과변수 또는 주제 자체** — 효율 측정·결정인자·중재(보철·훈련·교합) | **154** |
| **T2** | 교합 인자(접촉면적·교합양식·교합력)에서 효율을 종속변수로 다룸 | **37** |
| **T3** | 인접 축(영양·허약·QoL·인지)에서 효율이 부수 지표 — screened-out에 적립, `review-screened`로 복구 가능 | 130 |

---

## 이번 sweep의 핵심 관찰

1. **"글레이징 × 저작효율" 논문은 존재하지 않는다** — 후보 530건 중 glaze 언급 4건(26313248, 30142040, 36718695, 38071838)은 **전부 마모·조도 실험**이고 저작효율을 측정하지 않는다. 즉 앞선 답변("글레이즈 유무를 저작효율과 연결한 근거는 위키에 없다")은 위키 부재가 아니라 **문헌 자체의 부재**다. 글레이즈는 마모 축(zirconia-occlusal-adjustment 토픽)에서만 다뤄진다.
2. **위키의 실제 공백은 계측·중재 축**이다 — 위키는 저작효율을 *배경변수*로만 인용했고(총의치·RPD·교합접촉 상실), **효율을 어떻게 재는가**(chewing gum 2-color, gummy jelly, glucose, mixing ability, digital texture analysis)와 **어떻게 올리는가**(구강운동, gum training, 교합양식, 보철 설계)에 대한 페이지가 없다.
3. **2026년 SR이 계측법을 정리했다**(41793788, "Assessment of Masticatory Performance: SR of current assessment methods and measurement properties") — 이 토픽의 앵커 페이지 후보. overview 후보: `masticatory-efficiency-assessment-overview`.
4. 축이 4갈래로 갈린다: ① 계측·검증 ② 보철 결정인자(교합양식·어태치먼트·잔존악 형태) ③ 훈련·재활 중재(구강운동·껌저작·biofeedback) ④ 인구집단 연결(허약·영양·인지·뇌혈류). ④는 T3로 밀어냈다.

---

## 먼저 넣을 11건 (T1 상위 · SR/MA 우선)

| PMID | 연도 | 제목(축약) | 왜 |
|---|---|---|---|
| 41793788 | 2026 | Assessment of Masticatory Performance: SR of assessment methods | 계측법 정본 후보 |
| 34836460 | 2022 | SR+MA: Effect of Oral Exercises on Masticatory Function (JDR) | 유일한 중재 SR+MA |
| 36563840 | 2023 | SR+MA: MP and oral conditions in adults | 결정인자 총괄 |
| 41966910 | 2026 | SR+MA: Masticatory function indicators and frailty risk | 인구집단 연결 |
| 34814903 | 2021 | SR: PROMs for masticatory function | 주관적 지표 정리 |
| 37729477 | 2024 | SR: RPD impact on masticatory performance | 보철 축 |
| 36920311 | 2023 | SR+MA: MP after orthognathic surgery | 술식 축 |
| 36004768 | 2023 | SR+MA: Masticatory function of stroke patients | 신경학 축 |
| 33279156 | 2022 | SR: Denture adhesives and MP | 즉효 중재 |
| 40346735 | 2025 | SR+MA: Prevalence of self-assessed masticatory disorders | 역학 기준선 |
| 38151428 | 2025 | SR+MA: Maxillectomy surgical vs prosthetic rehab | 결손 축 |

차선(계측 검증 클러스터 — overview 작성 시 한 번에): 29356092 · 30024031 · 33956854 · 38379391 · 26111925 · 26371787 · 34888906.

---

## 변경 파일

- `.surveillance/queue.md` — 191건 적립
- `.surveillance/state.json` — 토픽 `occlusal-efficiency` 등록 + seen/screened 갱신
- `.surveillance/screened-out.md` — 326건 (복구가능)
- `references/topic-queries.md` — `occlusal-efficiency` 쿼리 카탈로그 추가
- `logs/2026-11-13_surveillance-occlusal-efficiency.md` — 이 파일

## 다음 단계

- 상위 SR 11건 ingest → `wiki/overviews/masticatory-efficiency-assessment-overview` 후보
- T2 37건(교합양식·접촉면적)은 보철 결정 축으로 별도 배치 ingest 권장
- screened-out 130건(인접 축)은 90일 후 `review-screened`로 재심
