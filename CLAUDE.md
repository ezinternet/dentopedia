# LLM Wiki — Dentistry (치과학)

A personal knowledge base of dental research papers, following [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/1dd0294ef9567971c1e4348a90d69285).

> **This file is agent behavior rules only, and is kept under 200 lines** — adherence degrades as it grows (per global CLAUDE.md). Reference material lives in sibling docs; each is the single source of truth for its domain. Never copy their content back here.

| Open this | When |
|---|---|
| `INGEST.md` | 논문을 위키에 추가 (`인제스트`, `Add this paper`, PDF 경로). Step 0–5, 필드 정의(`evidence_level:`/`superseded_by:`/`relations:`), 페이지 템플릿·세줄요약 규칙, 파일명 규칙, qmd 임베딩 드레인 |
| `OPERATIONS.md` | `agenda/`·`slides/`·`interactives/`·`peer-review/`·`note-meeting/`에 뭔가를 만들 때. 라우팅·파일명·frontmatter cross-link·agenda 워크플로·interactive 도구 freshness |
| `AUDITS.md` | 감사 추가/변경, `logs/` 해석. 22개 감사 표·compounding 지표 |
| `wiki/_meta/categories.md` | 카테고리 선택. 60여 개 목록·서브카테고리 분기 (**여기 이 파일은 목록을 의도적으로 복제하지 않는다** — 두 벌은 반드시 drift한다) |
| `SOP.md` | 사람이 읽는 운영 절차 |

질문에 답하는 것만이라면 위 문서들은 필요 없다.

**Canonical publish URL** (single source — every hard-coded absolute URL references THIS; if the deploy domain changes, change it here and grep for the old host):

```
PUBLISH_BASE = https://ezinternet.github.io/dentopedia
```

---

## THE FOUR RULES (do not violate)

These rules prevent hallucination and keep every claim traceable. They apply to **every** response, including overview pages.

1. **Answer only from ingested knowledge.** When *answering a question*, never use `WebSearch`/`WebFetch` to fill gaps — every claim must be grounded in papers we actually hold. This governs *answer generation*, not *acquiring* papers.
2. **Answer from the wiki first.** `sources/` and `wiki/` are the only sources of truth. Retrieve with QMD, never from the web.
3. **If the wiki is insufficient, re-read the PDF.** Go to `papers/{stem}.pdf`, extract more with `pypdf`, then update the wiki.
4. **If the wiki has no paper on the topic, say so.** *"I don't have a paper on this — please give me the PDF, or run an ingest sweep."* Do not improvise clinical claims from memory.

**Scope of Rule #4 — factual claims, not clinical reasoning.** Rule #4 governs *citable factual claims* (an efficacy number, a survival %, a threshold, "study X found Y"). It does NOT forbid **clinical reasoning synthesized from papers we hold**: weighing options for a case, explaining a mechanism, walking through a decision the held evidence supports. That reasoning is encouraged — it is the point of the wiki. The boundary: reasoning may combine and apply what our papers say, but must not smuggle in a specific factual claim that no held paper supports. When a case question needs a fact we don't hold, name the gap and reason around it from what we do hold — don't fabricate the number, and don't refuse the whole question.

**Ingest is not a Rule-#1 violation — it is a different path.** QMD and PubMed MCP are not exceptions carved out of "no web"; they operate on different axes. QMD is *local retrieval* (indexes only this repo). PubMed MCP / `literature-surveillance` is the *ingest entry point*: it may reach external sources, but only to **acquire** papers, which must then pass the full 3-tier pipeline (`papers/` → `sources/` → `wiki/`) before any claim from them is used in an answer. Never let PubMed text bypass the pipeline to answer a live question.

---

## Output rules (every response)

**세션 확신도 2태그 (mandatory — `[확인]` / `[미검증]`)**: 사실 주장(factual claim)을 하는 문장마다 이번 세션에 도구로 검증했는지 표시한다.

- `[확인]` — 이번 세션에서 도구로 직접 확인. Read/Bash/grep/qmd 출력에 근거가 있고, 어느 도구·어느 파일인지 즉答 가능.
- `[미검증]` — 그 외 **전부**. 기억·추론·훈련지식·확인 없이 인용한 메모리·그럴듯한 일반론.
- **붙이는 대상**: 수치·상태·파일 내용·시스템 동작 등 검증 가능한 단정. 특히 **메모리·문서를 인용할 때** (읽지 않고 인용하는 것이 최대 위험원).
- **안 붙이는 대상**: 질문·제안·의견·계획·방금 이 대화에서 오간 내용. 남용하면 신호가 죽는다.
- 확신이 안 서면 `[미검증]`. 태그 없이 단정하면 사용자가 지적하도록 되어 있다.

*Why*: 검증한 문장과 지어낸 문장이 **똑같은 확신의 톤**으로 나오는 것이 할루시네이션의 전달 경로다. 태그가 그 톤 차이를 강제한다 — `[미검증]`이 붙는 순간 문장이 스스로를 고발하고, 사용자는 "확실해?"(무의미) 대신 "그거 어디서?"(검증 강제)로 물을 수 있다. 2026-07-17에 메모리를 읽지도 않고 인용해 없는 사실을 만들어낸 사고가 근거. `evidence_level:`(논문 연구설계 강도, 위키 필드)과는 **다른 축**이다.

**Term notation rule**: 기술·의학 용어는 대화에서 ALWAYS **한국어 (English, 약어)** 형식. 예: 골-임플란트 접촉률 (Bone-to-Implant Contact, BIC), 골밀도화 (Osseodensification, OD), 임플란트 안정성 지수 (Implant Stability Quotient, ISQ). No exceptions.

**Language policy**: 위키 본문은 영어 (RAG-friendly, 용어 보존). 대화는 아무 언어나 (한국어 포함). 모든 wiki·source 페이지는 이중언어 세줄요약(`## Three-line Summary` + `## 세줄요약`) 필수 — 포맷 규칙은 `INGEST.md`.

**Overview Korean digest (mandatory for `wiki/overviews/`)**: 영어 본문은 한국어로 훑기엔 너무 빽빽하므로, 모든 overview/synthesis 페이지는 **`## 한국어 핵심요약` 블록을 최상단**(frontmatter 바로 아래, `## Three-line Summary` 위)에 싣는다. Obsidian callout `> [!summary] 한국어 핵심요약` 형식, **~10 bullets**(더 길어도 됨): 결론/thesis, 핵심 수치, 주요 분기·결정 지점, 대비·예외, 임상 takeaway. bullet 안에서도 term notation rule 적용. 영어 본문은 그대로 둔다 (RAG 정책 불변) — 이건 위에 얹는 한국어 독해 보조다.

---

## Repository Structure

**KNOWLEDGE** (substrate — reusable knowledge atoms) / **OPERATIONS** (knowledge → outputs). 모든 신규 artifact는 둘 중 하나로 라우팅한다 — ad-hoc 생성 금지.

```
KNOWLEDGE:  papers/{stem}.pdf  →  sources/{stem}.md  →  wiki/{category}/{stem}.md
                (원본, cp only)    (LLM 요약, 영어)      (최종 페이지) + wiki/overviews/ (종합)

OPERATIONS: agenda/ (작업 명세)  →  slides/ · interactives/ · peer-review/  →  logs/
            note-meeting/ 의 결정사항이 wiki/ 와 agenda/ 로 되먹임
            scripts/ (ingest watcher, lint, audits)
```

`wiki/_meta/categories.md` = 카테고리 라우팅의 단일 출처 — 목록·서브카테고리 분기 규칙뿐 아니라 **라우팅 원칙 5단계 자체**도 그 파일 하나에서 관리한다 (여기 복제 안 함 — 2026-07-15엔 카테고리 목록이, 2026-07-20엔 라우팅 원칙 4단계 예시가 두 파일에서 각각 갈라져 있었다). 신규 paper 분류·카테고리 신설 전엔 그 파일의 "라우팅 원칙"을 연다.

---

## Searching the Wiki (QMD)

이 repo 규모에서는 plain `grep`이 cross-category overview 매치를 놓치기 시작한다. **QMD** ([tobi/qmd](https://github.com/tobi/qmd)) — on-device 하이브리드 검색(BM25 + vector + LLM re-rank), 전부 로컬. 조회는 항상 qmd 우선, `grep`/`index.md`는 데몬이 죽었을 때의 fallback.

**QMD는 Rule #1 위반이 아니다.** local-first — 이 repo의 markdown만 인덱싱하며(`~/.cache/qmd/index.sqlite`) 웹은 절대 안 본다. 로컬 검색을 충분히 강하게 만들어 웹 검색이 아쉽지 않게 함으로써 Rule #1을 *강화*한다. QMD는 더 나은 `grep`이지 `WebSearch`가 아니다.

Collections: `wiki/`, `sources/`, `agenda/`, `note-meeting/` (markdown only; `papers/` PDF는 미인덱싱). Setup: `bash scripts/setup-qmd.sh`. 데몬은 `localhost:8181` HTTP MCP.

검색 우선순위: **`query`**(하이브리드) = 개념·종합 질문 → **`search`**(BM25) = 저자명·기기명·특정 수치 등 정확 매치 → `grep` fallback.

**손으로 `wiki/`·`sources/`·`agenda/`·`note-meeting/`의 `.md`를 고쳤으면 그날 안에 `qmd update && qmd embed`를 돌린다.** 이 경로엔 자동화가 **없다** — `embed-until-done` launchd 잡은 큰 백로그를 한 번 드레인하고 멈추는 것이지 주기 잡이 아니고, `qmd update`는 어디서도 자동 실행되지 않는다. 인제스트는 예외로 파이프라인이 알아서 한다(`ingest-one.py --finish`). 재색인은 파일별이 아니라 리포 전체라 그날 한 번이면 그날 편집분이 다 쓸려 들어간다.

*Why*: 고쳐도 색인이 옛것을 들고 있으면 **검색은 고치기 전 내용을 계속 내놓는다** — 페이지는 맞는데 답이 틀리는, 감사로 안 잡히는 실패다. 2026-07-17에 철회 논문 페이지를 고쳐놓고 이걸 빠뜨려 10시간 동안 철회 경고 없는 옛 청크가 검색됐다. 실측: 인덱스 대상을 고친 55일 중 23일(42%)이 그날 인제스트가 없어 이 창에 노출됐다.

**`qmd embed`는 exit 0을 내고도 미완료일 수 있다** — 완료 신호는 `All content hashes already have embeddings`뿐이고, 진짜 백로그는 `qmd status`의 `Pending:`이다 (`qmd update`가 찍는 숫자는 전체 파일 수라 거짓). 큰 백로그 드레인 절차는 `INGEST.md` Step 5.

**고아 벡터 청소는 주간 launchd 잡(`com.llmwiki.qmd-cleanup`, 월 10:00)이 한다 — ingest 절차에 넣지 마라.** `update`/`embed`는 고아 벡터를 안 치우고, 방치하면 검색이 **에러 없이** 산 문서를 놓친다 (감사로 안 잡히는 실패). 검색이 이상하면 재임베딩(`-f`, ~2.5h) 말고 `qmd cleanup`(수 초, 산 벡터 보존)부터 의심하라. 근거·실측은 `INGEST.md` Step 5.

---

## Daily Audit → see `AUDITS.md`

```bash
python3 scripts/daily-audit.py     # 24 audits → logs/
```

4 hard guard + 1 rationale은 error(block), 나머지 19는 **signal — 절대 block하지 않는다.** 감사는 거울이다: ingest 압력은 gate가 아니라 가시성으로 self-correct한다 (gate는 임상 워크플로에서 번아웃·회피를 유발). 개별 감사 설명·compounding 지표는 `AUDITS.md`.

## Model Routing (3축 원칙 — 표에 없는 작업도 이 원칙으로 판단)

| 축 | 모델 | 판단 기준 |
|---|---|---|
| **전사·정형** | **Haiku** | 답이 입력에 이미 있다 — 수치 옮기기, 링크 수정, 로그 읽기, 파일 복사, 스크립트 결과 해석 |
| **표현·품질** | **Sonnet** | 문장을 새로 써야 한다 — 위키 본문, 세줄요약, 카테고리 정리, 임상 insights |
| **추론·종합** | **Opus** | 여러 논문·페이지를 비교해 판단해야 한다 — supersession, 카테고리 경계, overview 종합 |

애매할 때는 한 축 위로 올린다 (Haiku→Sonnet, Sonnet→Opus). 세부 매핑은 `ingest-paper` SKILL.md Step 0 참조.

## Knowledge Compounding

가장 가치 있는 페이지는 논문을 가로질러 종합하는 `wiki/overviews/`다. 좋은 Q&A 세션 뒤엔: *"Save this as an overview page in wiki/overviews/"*.

생산적인 세션은 보통 여러 페이지를 낳지만 이건 **관찰이지 할당량이 아니다.** 위키의 철학은 *signal, not gate* — 세션당 페이지 수 같은 건 감사 설계가 의도적으로 피한 바로 그 gate다. 진짜 종합할 게 있을 때 쓰지, 숫자를 채우려고 쓰지 않는다.

---

## Design Principles

- **3-tier**: Raw PDF (immutable) → sources/*.md → wiki/**/*.md
- **English only** in wiki content (RAG-friendly; Korean conversation is fine)
- **Obsidian compatible**: `[[wikilinks]]`, plain markdown (Obsidian은 읽기만 — agent 편집과 충돌 없음)
- **No web search**: rule #1 above
- **Signal, not gate**: audits surface state; they never block. Quotas and hard gates cause avoidance.
- **Single source of truth**: categories → `wiki/_meta/categories.md`; ingest·page templates → `INGEST.md`; OPS routing → `OPERATIONS.md`; audits → `AUDITS.md`; publish URL → `PUBLISH_BASE` above. Never a second copy.

When in doubt, follow rule #1.
