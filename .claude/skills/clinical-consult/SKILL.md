---
name: clinical-consult
description: Chairside 임상 자문 — 케이스/임상질문을 던지면 위키(QMD)에서 근거를 retrieve → overview로 synthesize → 근거등급(🟢🟡🟠⚪)을 붙인 권고 + 인용을 돌려준다. 사용자가 "컨설트", "consult", "이 케이스", "이 환자", "어떻게 할까", "근거 알려줘", "~해도 되나", 환자 인자(나이·전신질환·치아번호·타이밍)를 곁들인 임상 결정 질문을 하면 트리거. 논문 ingest(ingest-paper)나 환자 민원 응대(claim-coach)와는 다른 독립 스킬 — 근거기반 임상 결정 질문이면 명시적으로 "스킬"이라 말 안 해도 적용.
argument-hint: [클리니컬 케이스 또는 임상 질문]
allowed-tools: Bash, Read, Grep
---

# Chairside 임상 컨설트 (Clinical Consult)

임상 케이스/질문에 대해 **이 위키에 실제로 있는 논문만** 근거로, 근거등급을 붙인
권고를 chairside 속도로 돌려준다. 자문의(board consultant)처럼 — 정답 하나가 아니라
**근거 + 강도 + 회색지대**를 같이 준다.

## ⛔ THE FOUR RULES (CLAUDE.md — 절대 위반 금지)

1. **웹검색 금지.** `WebSearch`/`WebFetch` 절대 사용 안 함. (PubMed MCP·PMID 조회는 별개로 허용되나, 컨설트 답변 근거는 오직 위키.)
2. **위키에서 먼저 답한다.** `sources/`·`wiki/`가 유일한 진실원천.
3. **위키가 부족하면 PDF 재독.** `papers/{stem}.pdf`를 pypdf로 더 파고, 위키를 갱신.
4. **논문이 없으면 없다고 말한다.** "이 주제 논문이 위키에 없습니다 — PDF를 주세요." 지어내지 말 것.

이 4규칙은 컨설트 **모든 답변**에 적용된다. 훈련지식으로 임상 권고를 만들지 않는다.

## 언제 이 스킬이 아닌가 (경계)

- 논문을 위키에 **넣는** 작업 → `ingest-paper`
- 화난 환자 **민원·클레임 응대 작문** → `claim-coach`
- 이 스킬은 **근거기반 임상 결정 질문**에만.

---

## Step 1 — 케이스 파싱

케이스에서 두 가지를 분리해 명시한다:

- **핵심 임상 질문** (1문장). 결정 대상이 무엇인가?
- **환자/상황 인자**: 나이, 전신질환(HbA1c·항응고·골다공증약 등), 치아번호·부위,
  타이밍, 재료, 술식 변수. 답을 바꾸는 modifier들.

질문이 모호하면 **가정을 명시하고 진행**하거나, 답을 가르는 결정적 인자 1개만 되묻는다.
(chairside이므로 되묻기는 최소화 — 웬만하면 가정 명시 후 진행.)

## Step 2 — 근거 검색 (QMD, 위키 한정)

여러 각도로 검색한다. **overview를 먼저** 노린다(이미 종합돼 있어 warm start).

```bash
export PATH="/opt/homebrew/bin:$PATH"   # brew node 강제 (구 node ABI 회피)
cd /Users/oracleneo/llm-wiki
qmd search  "<정확 용어·저자·기기·수치>"   # BM25 — 빠르고 안정적. 1차 경로.
qmd vsearch "<임상 개념 문장>"              # 벡터 유사도 — 개념/의미 검색. LLM 없음, 빠름.
qmd get "wiki/<category>/<stem>.md"        # 히트 페이지 열람(줄번호)
```

- **1차 경로 = `qmd search`(BM25) + `qmd vsearch`(벡터).** 둘 다 LLM을 안 써서 빠르고,
  헤드리스/에이전트 실행에서도 안 멈춘다.
- `qmd query`(하이브리드+LLM 리랭킹)는 품질은 최상이나 **비대화형(백그라운드/subagent)
  실행에서 리랭커가 멈출 수 있다** — 대화형 세션에서 즉답할 때만 쓰고, 안 돌아오면
  `search`/`vsearch`로 즉시 전환한다. (macOS엔 `timeout` 없음 → `gtimeout` 또는 백그라운드.)
- **여러 각도로 2~3번** 검색한다: exact term 1회(search) + 개념 1회(vsearch) + 한국어 1회.
- 히트 중 **`wiki/overviews/`를 우선** 읽는다 (이미 cross-paper 종합됨).
- 상위 후보를 `qmd get` 또는 `Read`로 실제로 읽는다. 각 페이지의
  **One-line Summary + Results 표 + `confidence:` + `relations:`**를 최소한 확인. 목표 3~8편.
- MCP `qmd` 서버가 붙어 있으면 그 `search`/`query`를 써도 됨(동일 인덱스). CLI가 fallback.

## Step 3 — Rule #4 게이트 (STOP 조건)

검색이 **주제상 관련 페이지를 못 내놓으면** 여기서 멈춘다.

> "이 주제 논문이 위키에 없습니다 — PDF를 주시면 ingest 후 근거로 답하겠습니다."

훈련지식으로 임상 권고를 지어내지 **않는다**. (인접 주제만 있으면 "직접 논문은 없고,
인접 근거는 X뿐"이라고 정확히 경계를 긋는다.)

## Step 4 — 근거 등급화

각 인용 페이지의 `confidence:` 필드를 증거 가중치로 삼아, 아래로 **종합 등급**을 매긴다:

| 종합 등급 | 기준 |
|---|---|
| 🟢 **Strong** | `sr+ma` 또는 일관된 다수 `rct` |
| 🟡 **Moderate** | 단일 `rct` / `prospective`, 또는 caveat 있는 `sr` |
| 🟠 **Weak** | `retrospective` / `cross-sectional` / `case-report` / `in-vitro` / `animal` / `narrative-review` |
| ⚪ **Insufficient·Conflicting** | 직접 근거 없음, 또는 근거끼리 충돌 |

**충돌 체크(중요):** 인용한 페이지의 frontmatter `relations:`에 `contradicts`/`refines`
엣지가 있으면 반드시 회색지대로 노출한다. (전체 논쟁 지도는 `interactives/contradiction-radar.html`
— 논쟁 레이더와 짝을 이룸.) 등급을 과대평가하지 말 것 — 반대 근거가 있으면 ⚪ 또는 강등.

## Step 5 — 답변 포맷 (chairside)

한국어 + **한국어 (English, 약어)** 용어표기 규칙. 아래 구조로:

```
⚡ Bottom line  [🟢/🟡/🟠/⚪]
  1~2문장 권고. 등급 배지 포함.

📊 근거
  • <주장> — [[category/stem]] (confidence 배지) · 핵심수치
  • <주장> — [[category/stem]] (confidence 배지) · 핵심수치
  (모든 임상 주장은 실제로 읽은 페이지로의 [[wikilink]]를 달 것)

🧑‍⚕️ 이 환자 보정
  환자 인자가 권고를 어떻게 바꾸는지.

⚠️ 회색지대 · 반대근거
  contradicts/refines, 불확실성, "아직 논쟁 중".

한 줄 요약: <한 문장>
```

**인용 규율(엄수):**
- 모든 임상 주장은 **실제로 읽은 페이지**로의 `[[wikilink]]`를 단다. 인용을 지어내지 않는다.
- 수치는 페이지에서 **그대로 인용**. 기억으로 수치를 만들지 않는다.
- 페이지를 안 읽었으면 인용하지 않는다.

**면책 한 줄(항상):** *의사결정 지원용 — 최종 임상 판단·책임은 술자에게 있습니다.*

## Step 6 — 지식 복리 (optional, 답변 뒤에 한 줄)

- 컨설트 중 **논문 공백**이 드러나면: "이 부분은 위키에 논문이 없어요 — PDF 주시면 ingest."
- 좋은 종합이 나왔으면: "이 답변을 `wiki/overviews/`에 종합 페이지로 저장할까요?"

---

## Worked example (형식 참고용)

**입력:** "68세, 조절 안 되는 당뇨(HbA1c 8.2), #26 발치와 즉시식립 고민 중. 해도 되나?"

**Step 1** — 질문: 조절불량 당뇨 환자에서 상악 구치부 즉시식립 가부.
인자: 고령·HbA1c 8.2(조절불량)·상악 구치부·즉시식립(type 1).

**Step 2** — `qmd search "immediate implant diabetes survival"` →
`andrade-2021-survival-rate-peri-implant-evaluation` (SR+MA) 히트. `qmd get`으로 열람.

**Step 5 출력 (실제 검색·독해로 만든 답 — 직관을 근거로 검증한 예):**

> ⚡ **Bottom line** [🟡 Moderate]
> HbA1c 8.2는 즉시식립·즉시부하의 금기가 **아니다.** 위키 근거는 조절불량 당뇨에서도
> 즉시부하 생존율이 비당뇨와 **차이 없음**을 보인다 — 프로토콜 준수·구강위생 하에 진행 가능.
>
> 📊 **근거**
> • 제2형 당뇨 즉시부하 생존율, 비당뇨 대비 차이 없음 — [[drug/systemic-disease/andrade-2021-survival-rate-peri-implant-evaluation]] (sr+ma) · RR 1.00 (0.96–1.04, I²=0%)
> • **조절불량**(high HbA1c) 당뇨에서도 생존율 차이 없음 — 같은 SR+MA · RR 1.08 (0.87–1.33)
> • 즉시 vs 전통부하 12개월 변연골소실 차이 없음 — 같은 SR+MA · MD −0.08 mm
>
> 🧑‍⚕️ **이 환자 보정** — 상악 구치부 저골질이 1차 안정성을 낮춤 → OD/undersized drilling으로
> 삽입토크 확보. HbA1c는 생존보다 **변연골·BOP/PD 등 주위염 지표**와 상관 → SPT 강화.
>
> ⚠️ **회색지대** — 근거 얕음(pooled당 ≤3편, 대개 ≤24개월), 조절불량·MBL 분석 이질성 큼
> (I² 70~83%). 관련 SR+MA [[drug/systemic-disease/al-ansari-2022-diabetes-mellitus-dental-implants-sr-ma]]와 교차확인 권장.
>
> 한 줄 요약: 금기 아님 — 즉시부하 생존율은 당뇨와 무관, 단 주위염 지표·SPT를 집중 관리.
>
> *의사결정 지원용 — 최종 판단은 술자.*

**교훈:** 초기 직관("혈당 조절 선행 후 지연부하")은 **위키의 SR+MA로 뒤집혔다.** 컨설트는
반드시 검색·독해한 실 페이지·실 수치로 답을 만들고, prior로 임상 권고를 만들지 않는다.
