# Zirconia Occlusal Adjustment (지르코니아 교합조정) — Surveillance 2026-11-12

토픽 키: `zirconia-occlusal-adjustment` (신규 토픽 · 전 기간 백필 + 2020+ 확장 stem)

---

## 도구 메모 (환경 차이 — 재현 시 주의)

- 이 세션에는 **PubMed MCP가 노출되지 않았다** (툴 카탈로그에 PubMed 검색 도구 없음). 대신 **NCBI E-utilities**(esearch · esummary · efetch)를 직접 호출했다 — PubMed MCP와 동일 백엔드·동일 쿼리 문법.
- **PMC OA service(`oa.fcgi`)는 404로 폐기** → 라이선스는 **Europe PMC REST API**(`resultType=core`)의 `license` 필드에서 조회.
- 신규 토픽이므로 **water-mark 미적용**(전 기간 백필). 주의: `enqueue`가 seen에 고PMID를 추가하면서 **water-mark가 42,964,982로 올라갔다** — 이후 이 토픽의 증분 sweep은 이 값 기준으로 컷된다.

---

## 쿼리 (stem 2개 + SR 보강 1개)

| stem | 내용 | hit | 비고 |
|---|---|---|---|
| **A — 조정 어휘 직접** | zirconia 계열 AND (`"occlusal adjustment"` · `"intraoral adjustment"` · `"intraoral grinding"` · `"selective grinding"` · `"occlusal correction"` · `"occlusal refinement"`) | **68** | 전 기간. `occlusal` 수식어가 붙은 것만 |
| **B — 조정×결과 축** | zirconia 계열 AND (grinding · ground · adjustment*) AND (polishing · glazing · phase transformation · flexural strength · surface roughness · wear · monoclinic · LTD) | **147** (2020–2026) | 126건이 A에 없음 |
| **SR 보강** | zirconia 계열 AND (grinding·polishing·surface treatment·adjustment) AND (SR·MA) | **42** | 축에 맞는 3건만 채택 |
| **합집합(중복 제거)** | | **197** | |

**왜 stem A만으로 부족한가**: 위키 기보유 코어(kosmac-1999, lawson-2014, sarabi-2024)는 제목에 "occlusal"이 없이 `after adjustment, polishing and glazing` 식으로 쓴다. stem A 단독은 이 계열을 통째로 놓친다. stem B는 2020년 이후로 창을 좁혀 노이즈를 억제했다(전 기간이면 305+).

**ptyp 필터 없음(`[]`)**: 이 축의 근거는 **in vitro 기계시험이 지배적**(큐 114건 중 89건). RCT/SR/MA 필터를 걸면 코어를 놓친다.

---

## 파이프라인

| 단계 | 건수 |
|---|---|
| 검색 합집합 | 197 |
| − 기보유(위키 DOI·제목 교차) | −6 |
| 스크리닝 대상 | **191** |
| include (큐 적립) | **114** |
| exclude (screened-out 적립) | **77** |

큐 114건 구성: **OA:PMC 44 / OA:none 70**, 유형 in-vitro 89 · clinical 12 · RCT 7 · SR+MA 2 · CCT 2 · SR 1 · narrative-review 1. 게재연도 2012–2026(2020년 이후 98건 · 2019년 이전 16건).

---

## 티어 (ingest 우선순위 — 큐에는 topic만 실리고 티어는 이 표가 정본)

| 티어 | 정의 | 건수 |
|---|---|---|
| **T1** | 조정 행위 자체와 재료 결과 — 삭제(grinding)·bur 종류·조정 깊이가 상전이(t→m)·굽힘강도·색·마모에 미치는 영향 | 61 |
| **T2** | 조정 후 마무리·연마 프로토콜 — 연마 기구·페이스트·glaze, 거칠기·광학·표면 미생물 | 34 |
| **T3** | 교합접촉 정확도 / 임상 조정량 — 워크플로·디자인이 조정 수요에 미치는 영향, 임상 마모 | 19 |

### 먼저 넣을 8건

| PMID | 유형 | OA | 왜 |
|---|---|---|---|
| 36634437 | SR+MA | — | **grinding 후 finishing/polishing/glazing이 필요한가** — 이 축의 유일한 정면 SR+MA |
| 40435897 | SR+MA | — | **bur 종류·건/습 조건 → 상전이 정도** SR+MA |
| 41257139 | in-vitro | PMC (cc by) | **조정량(extent)이 노화 지르코니아 BFS에 미치는 영향** — "얼마나 깎아도 되나"에 직결 |
| 35934577 | in-vitro | — | 지르코니아 종류별 **chairside adjustment 후 강도·상전이** |
| 31743822 | in-vitro | — | **음성 결과**: 교합면 grinding·polishing·glazing이 fatigue load-bearing·survival에 영향 없음 |
| 32763368 | in-vitro | — | **simulated clinical adjustment + 구내 연마** (translucent monolithic 2종) |
| 42068718 | in-vitro | — | **intaglio면 grinding 조정** → 내면/변연 적합 + load-bearing (4YSZ) |
| 42139519 | in-vitro | — | **chairside finishing/polishing ± glazing** 표면 특성 |

---

## 기보유 (위키에 이미 있음 — 큐 제외)

| PMID | 위키 페이지 |
|---|---|
| 31297175 | [[alfrisany-2019-occlusal-adjustments-zirconia-enamel-wear]] |
| 33456027 | [[tachibana-2021-polishing-zirconia-antagonist-wear]] |
| 39710626 | [[badawy-2025-enamel-wear-zirconia-endocrowns-2year]] |
| 28385438 | [[mohammadi-bassir-2017-grinding-overglazing-polishing-zirconia]] (DOI 필드 누락 → 제목 교차로 검출, 큐에서 수동 제거) |
| 38993795 | [[sarabi-2024-grinding-ltd-flexural-strength-zirconia]] |
| 41366762 | [[aboushelib-2026-translucent-zirconia-monolithic-mechanical-performance]] |

추가로 이 축의 **2019년 이전 코어**는 이미 위키에 있다: [[kosmac-1999-grinding-sandblasting-flexural-strength-zirconia]], [[ramos-2016-grinding-heat-treatment-zirconia-flexural]], [[janyavula-2013-wear-polished-glazed-zirconia-enamel]], [[lawson-2014-wear-enamel-zirconia-lithium-disilicate]], [[stawarczyk-2013-two-body-wear-monolithic-veneered-zirconia]], [[steiner-2024-zirconia-conditioning-glazing-enamel-wear]], [[aflatoonian-2025-deglazing-hydrothermal-aging-high-translucent-zirconia]].

**→ 즉 이번 큐의 본체는 2020년 이후 델타다.** 2012–2019 구간의 in vitro 다수는 위키 코어와 중복 개념이므로 ingest 우선순위가 낮다.

---

## 노이즈 (exclude 77건의 성격)

- **접착(bonding) 축이 최대 노이즈** — zirconia 표면처리(sandblasting·laser·primer·MDP) 논문이 "surface treatment" 어휘를 공유해 대량 유입. 위키가 이미 별도 축(`resin-bonding`)으로 보유.
- 기계가공(machining·grinding force·laser cutting·소결 온도), 착색·shade·translucency 단독, 브라켓 접착, biofilm·S. mutans 단독, 비치과(THA·TBC·PBT).
- `"adjustment"` 단독은 교정장치·보청기까지 잡는다 — stem B에서 polishing/glazing/phase/strength/wear로 AND 묶은 이유.

---

## 관찰 · 갭

1. **SR+MA 2건이 결정적 갭** — "grinding 후 반드시 연마/glaze해야 하나", "어떤 bur가 상전이를 덜 일으키나"는 chairside 의사결정의 두 축인데 위키에 SR이 없다.
2. **조정량(extent) 축이 비어 있다** — 위키 페이지들은 "조정하면 강도/색이 어떻게 되나"는 다루지만 "몇 μm까지/얼마나 깎아도 되나"(41257139)와 "조정 시간·접촉 오차를 줄이는 워크플로"(T3 19건)는 페이지가 없다.
3. **overview 부재** — [[zirconia-material-clinical-overview]]가 조정을 한 줄 언급(line 29·342)하지만 전용 종합은 없다. 후보: `wiki/overviews/zirconia-adjustment-finishing-overview` (T1 ingest 후).
4. T3(교합접촉 정확도)는 인접 페이지만 있다 — [[assoratgoon-2025-occlusal-contact-changes-implant-supported-prostheses]], [[zhou-2021-digital-occlusal-analysis-posterior-implant]]. 지르코니아 보철의 조정량을 정량한 페이지는 없음.

---

## 다음 단계

1. 위 8건 → `ingest-paper` (SR+MA 2건 먼저, 그다음 41257139·35934577).
2. ingest 후 `zirconia-adjustment-finishing-overview` 작성 — 축: ①조정→상전이/강도 ②조정 후 연마·glaze의 필요성 ③조정량 한계 ④임상 조정 수요(워크플로).
3. 큐의 나머지 T1/T2는 위키 코어와의 중복 판정 후 선별 ingest.
