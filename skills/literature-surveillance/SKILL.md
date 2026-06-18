---
name: literature-surveillance
description: 치과 임상 관심 토픽(임플란트·근관·치주 등)을 PubMed에서 주기적으로 훑어 직전 sweep 이후 새로 등재된 RCT·SR·메타분석만 추려내고, 중복을 제거하고 PMC open-access 여부를 미리 태깅해 llm-wiki 인제스트 큐에 적립하는 문헌 감시(literature surveillance) skill. 사용자가 "감시 돌려", "새 논문 떴는지 확인", "PubMed 훑어", "신규 RCT/SR 찾아", "문헌 모니터링", "surveillance", "ingest 큐 채워", "이번 주 새 논문" 등을 언급하거나, 특정 임상 토픽의 최신 문헌을 정기적으로 따라잡으려 하면 트리거. llm-wiki-ingest의 *앞단* 으로, 논문을 손에 넣은 뒤가 아니라 "무엇을 넣을지 고르는" 단계를 담당하는 독립 skill — dental-wiki-entry(위키 항목 작성)·llm-wiki-ingest(PDF→위키 적재)와 기능이 다름. 명시적으로 "surveillance"라 말하지 않아도, 관심 토픽의 신규 문헌을 자동으로 따라잡는 작업이면 적극 적용.
---

# Literature Surveillance

치과 임상 관심 토픽의 PubMed 신규 문헌을 한 번에 훑어(one sweep) 인제스트 후보 큐를 채운다. 이 skill은 **자동으로 도는 cron이 아니다** — 호출될 때 1회전을 실행할 뿐이다. 정기 자동 실행은 launchd 같은 외부 스케줄러가 이 skill을 깨워주는 별도 레이어가 맡는다(현재 범위 밖).

## 실행 환경 / 사전조건

- macOS, Claude Desktop.
- **PubMed MCP** 연결 (검색·OA판정에 사용).
- **Desktop Commander**, allowedDirectory: `/Users/oracleneo/llm-wiki` (상태·큐 파일 I/O, 스크립트 실행).
- 상태·큐 루트: `/Users/oracleneo/llm-wiki/.surveillance/`

## 역할 분담 (중요 — 어기면 동작 안 함)

PubMed MCP는 **Claude가** 호출한다. 파이썬 스크립트는 Desktop Commander로 도는데 **MCP를 직접 부를 수 없다.** 따라서:

- **Claude(MCP) 담당**: `search_articles` 검색, `get_copyright_status`/PMC 링크로 OA 판정.
- **스크립트(`sweep_state.py`) 담당**: 토픽셋·last-run 로드, seen-pmids 중복 제거, 큐 append, 상태 갱신, 리포트 집계.

즉 Claude가 검색 결과 PMID를 스크립트에 넘겨 신규만 돌려받고, OA까지 태깅한 후보 객체를 다시 스크립트에 넘겨 큐에 적립한다.

## 워크플로우 (1 sweep)

### 1. 상태 로드
```bash
python3 scripts/sweep_state.py load
```
출력: 활성 토픽 목록(토픽명 + PubMed 쿼리식), 각 토픽의 `last_run_edat`, 전역 seen 개수.
`.surveillance/`가 없으면 먼저 `init` 실행:
```bash
python3 scripts/sweep_state.py init
```

### 2. 토픽별 검색 (Claude / MCP)
각 토픽마다 `search_articles` 호출:
- `query`: 토픽 쿼리식 + ptyp 필터.
  예: `osseointegration AND (Randomized Controlled Trial[Publication Type] OR Systematic Review[Publication Type] OR Meta-Analysis[Publication Type])`
- `date_from`: 해당 토픽의 `last_run_edat` (없으면 합리적 시작일, 예: 직전 3개월).
- `datetype`: **`edat`** (게재일 pdat 아님 — 신규 등재 누락 방지).
- `sort`: `pub_date`, `max_results`: 50 권장.

ptyp 필터는 토픽별로 조정 가능(가이드라인·코호트 포함 여부 등). 카탈로그는 `references/topic-queries.md` 참조.

### 3. 중복 제거 (스크립트)
검색으로 모은 PMID를 토픽별로 넘긴다:
```bash
python3 scripts/sweep_state.py dedup --topic "implant" --pmids 38123456,38234567,...
```
출력: seen-pmids·기존 큐에 없는 **신규 PMID만** (JSON).

### 4. OA 사전 판정 (Claude / MCP)
신규 PMID에 대해 `get_copyright_status` (배치) 또는 `find_related_articles(link_type='pubmed_pmc')`로 PMC 풀텍스트·라이선스 확인. 각 후보를 다음 형태로 구성:
```json
{"pmid":"38123456","title":"...","journal":"...","ptyp":"RCT","edat":"2026/06/10",
 "oa":"PMC","pmcid":"PMC1234567","license":"CC BY 4.0","topic":"implant"}
```
- `oa`: `PMC` | `unpaywall` | `none` 중 하나. PMC에 풀텍스트가 있으면 `PMC`로 태깅하고 `pmcid` 기입.
- PMC가 없으면 OA 여부 미상으로 두고 `oa":"none"` — 실제 접근경로 탐색은 ingest 단계로 미룬다(이 skill은 *사전* 태깅만).

### 5. 큐 적립 + 상태 갱신 (스크립트)
```bash
python3 scripts/sweep_state.py enqueue --json /tmp/candidates.json
```
- `.surveillance/queue.md`에 후보를 append (llm-wiki-ingest가 읽는 포맷).
- 적립된 PMID를 seen-pmids에 추가.
- 각 토픽의 `last_run_edat`를 이번 sweep 시각으로 갱신.

### 6. 리포트
```bash
python3 scripts/sweep_state.py status
```
화면에 토픽별 신규 N건, OA/유료 분포, 큐 총량 요약. Claude는 이를 산문 1~2문단으로 정리해 보고(신규 핵심 논문 제목 몇 개 강조).

## 큐 포맷과 ingest 체이닝

`queue.md`는 llm-wiki-ingest가 바로 집어먹을 수 있게 PMID·제목·저널·ptyp·OA·PMC ID·적립일을 한 항목씩 적는다. ingest는 이 큐의 `[OA:PMC]` 항목부터 우선 처리하면 접근경로 재탐색 비용이 준다. 처리 완료 항목은 ingest 쪽에서 `[x]`로 마킹하거나 큐에서 제거(운영 규칙은 ingest skill과 합의).

## 상태 스키마

`.surveillance/state.json`:
```json
{
  "topics": {
    "implant": {"query": "...", "ptyp": ["RCT","SR","MA"], "last_run_edat": "2026/06/01"},
    "endo": {"query": "...", "last_run_edat": null}
  },
  "seen_pmids": ["38123456", "..."]
}
```
seen-pmids가 수천 단위로 커져도 set 조회라 부담 없음. 큐(`queue.md`)와 상태(`state.json`)는 분리 — 큐는 사람이 읽고 ingest가 소비, state는 기계 상태.

## Reference / Scripts

- `references/topic-queries.md` — 토픽별 PubMed 쿼리식 카탈로그. 새 토픽 추가·쿼리 튜닝은 여기서. (skill 본문이 아니라 이 파일을 고치게 유도)
- `scripts/sweep_state.py` — 상태·중복·큐 I/O. 서브커맨드: `init` / `load` / `dedup` / `enqueue` / `status`. 사용법은 `--help`.

## 경계

- 이 skill은 **무엇을 ingest할지 고르는** 단계까지만. PDF 다운로드·위키 항목 작성은 llm-wiki-ingest / dental-wiki-entry 소관.
- OA 접근경로 전체 탐색(Unpaywall→preprint→author request→RISS 등)은 ingest 단계. 여기선 PMC 유무만 빠르게 태깅.
- 임상적 가치 판단(이 논문이 정말 중요한가)은 큐 적립 후 사람이 한다. skill은 ptyp·신규성으로만 1차 필터.
