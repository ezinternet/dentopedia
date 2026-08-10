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

## 실행 모드 — 루틴 vs 심층 (먼저 고를 것)

sweep마다 두 모드 중 하나를 고른다. **잘못 고르면 과설계 또는 비용폭발**이므로 첫 단계에서 판단한다.

| | **루틴 증분 sweep** (기본) | **심층 백필 sweep** |
|---|---|---|
| 언제 | edat 최근 2~4주, 토픽당 신규 0~10건 예상 | 넓게 캐스팅(토픽당 수백 hit), 신규 토픽 최초 백필, ptyp 완화 |
| 관련성 스크리닝 | 상위 모델(이 세션)이 인라인으로 초록 훑음 | **Haiku 토픽 분대**가 병렬 스크리닝, 상위는 통과분만 종합 |
| 병렬화 | 안 함 | 토픽 fan-out (concurrency 캡 필수) |
| screened_out | 거의 안 씀 | **필수** — 탈락분을 복구가능 버킷에 적립 |

**판단 규칙**: 아래 워크플로우(Step 1~6)는 **루틴 모드**다. `load` 출력에서 특정 토픽의 예상 hit이 수십~수백이거나(넓은 쿼리·긴 공백·신규 토픽) 상위 모델이 초록 수백 개를 읽어야 하는 상황이면 그 토픽만 **심층 모드**(아래 별도 섹션)로 돌린다. 한 sweep 안에서 토픽별로 모드를 섞어도 된다. 애매하면 루틴이 기본값 — 심층은 초록 부하가 실제로 클 때만.

## 워크플로우 (1 sweep, 루틴 모드)

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
- `date_from`: 해당 토픽의 `last_run_edat` (없으면 합리적 시작일, 예: 직전 3개월). **주의: 현재 MCP가 이 파라미터를 무시한다 → Step 3의 water-mark로 신규 판별한다.**
- `datetype`: **`edat`** 지정은 하되 실제로는 무시됨(위 결함). 신규 컷은 water-mark가 담당.
- `sort`: `pub_date`, `max_results`: 50 권장.

ptyp 필터는 토픽별로 조정 가능(가이드라인·코호트 포함 여부 등). 카탈로그는 저장소 루트의 `references/topic-queries.md` 참조 (이 스킬 폴더 내 동명 파일이 아님 — 과거 두 파일로 갈라졌다가 2026-07-05 병합됨).

### 3. 중복 제거 + water-mark (스크립트)

> [!warning] 알려진 결함 — edat 날짜 필터가 죽어 있음 (2026-07-14 확인)
> PubMed MCP `search_articles`는 `date_from`/`datetype=edat`를 **완전히 무시**한다(날짜 유무와 무관하게 `total_count`·top PMID 동일). 그래서 Step 2의 edat 증분 필터는 **no-op**이고, `dedup`이 seen만 빼면 "top-N 최신순 중 아직 위키에 없는 옛 논문"까지 대량 유입된다.
> **대체책 = water-mark.** PMID는 등재순으로 단조증가하므로 `max(seen)`를 edat 프록시로 삼아 그 초과분만 진짜 신규로 본다. `dedup --watermark`(또는 스냅샷 `--watermark-value`)로 적용한다.

**권장 절차** — sweep 시작 시 water-mark를 한 번 스냅샷하고 모든 토픽 dedup에 같은 값을 넘긴다(중간 enqueue로 seen이 커져도 기준이 안 흔들림):

```bash
# 0) sweep 시작 — water-mark 스냅샷
WM=$(python3 scripts/sweep_state.py load | python3 -c "import json,sys;print(json.load(sys.stdin)['watermark'])")

# 1) 토픽별 dedup (스냅샷 고정)
python3 scripts/sweep_state.py dedup --topic "implant" --pmids 42500000,42000000,... --watermark-value "$WM"
```

출력: seen·screened·큐에 없고 **PMID > water-mark 인 신규만** (JSON) + `watermark`, `excluded_below_watermark`. water-mark 없이 seen만으로 거르려면 플래그 생략(옛 동작).

**한계**: 정렬이 `pub_date`뿐이라(edat 정렬 옵션 없음) 게재일은 옛날인데 최근 등재된 논문은 top-N 밖으로 밀려 놓칠 수 있다 — 넓은 토픽은 `max_results`를 키우거나 심층 모드로 보완.

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

## 심층 sweep 모드 (Haiku 토픽 분대 + 스크리닝)

토픽당 hit이 수백에 이르면 상위 모델이 초록을 전부 읽는 건 낭비다("비싼 모델은 판단 자리에만"). 이때만 다음 fan-out을 쓴다.

### 원칙 (어기면 지식 유실 또는 차단)

1. **Haiku는 관련성만, 근거등급은 안 본다.** ptyp는 이미 PubMed 쿼리(`[Publication Type]`)에서 걸러졌다. 분대원의 임무는 오직 "이 논문이 이 토픽에 topical하게 맞는가"뿐.
2. **판정은 3분법 — include / exclude / borderline. 불확실하면 무조건 borderline, 절대 exclude 금지.** 서베일런스에서 false-negative는 "영원히 놓침"이라 일반 검색보다 훨씬 비싸다. borderline 쪽으로 편향시킨다.
3. **concurrency 캡 ≤ 4.** PubMed MCP는 결국 NCBI eutils(키 없이 3 req/s, 키 있어도 10 req/s)를 때린다. 23개 분대원 동시 발사는 throttle/차단. 한 번에 최대 4개 토픽만 병렬로 돌리고 나머지는 큐잉. eutils API 키가 있으면 캡을 8까지 올려도 된다.

### 프로토콜

**Step D1 — 토픽 분대 fan-out (상위 모델이 Agent 호출).** 심층 대상 토픽마다 Haiku 서브에이전트 1개. 동시 실행은 ≤4개씩 배치.

```
Agent(subagent_type="general-purpose", model="haiku",
      description="<topic> 관련성 스크리닝",
      prompt=<아래 임무명세서>)
```

**임무명세서(각 분대원 프롬프트에 반드시 박을 것):**
- 입력: 토픽명 + 이 토픽의 PubMed 검색 결과(PMID·제목·초록 리스트). *검색은 상위 모델이 미리 `search_articles`로 돌려 결과를 프롬프트에 넣어준다* — 분대원이 MCP를 직접 부르면 concurrency 캡이 깨지므로, 검색은 상위가 캡을 지키며 순차/소량병렬로 수행하고 분대원은 텍스트 판정만 한다.
- 작업: 각 논문을 topical 관련성으로만 판정.
- 출력(JSON 배열): `[{"pmid","verdict":"include|exclude|borderline","reason":"한 줄 근거"}]`
- **철칙: 이 토픽에 맞는지 확신 없으면 borderline. exclude는 "명백히 다른 주제"일 때만**(예: 정형외과 임플란트, 수의학, 완전 무관 분야). 근거·표본크기·연구질은 판단하지 말 것(그건 상위·사람 몫).

**Step D2 — 상위 모델이 판정 취합.**
- `include` → 기존 루틴 Step 4(OA 태깅)→Step 5(enqueue)로.
- `borderline` → **상위 모델이 직접 초록을 읽고** include/exclude 결정. 어느 버킷에도 자동 안 넣는다.
- `exclude` → `screen-out`으로 복구가능 버킷에 적립:
  ```bash
  python3 scripts/sweep_state.py screen-out --json /tmp/screened.json
  ```
  형식: `[{"pmid","topic","edat","reason","verdict":"exclude"}]`. **seen_pmids에는 안 들어간다** — 이게 false-negative 영구소실 방지의 핵심.

**Step D3 — dedup은 screened도 자동 제외.** 다음 루틴 sweep에서 탈락분이 매번 재부상해 재스크리닝 비용을 반복하지 않도록, `dedup`이 `screened_out`을 이미 제외한다(코드 반영됨). 재부상시키려면 명시적으로 `restore-screened`.

### 복구 루프 (false-negative 되돌리기 — 정기)

Haiku 오탈락은 되돌릴 수 있어야 감시 시스템이다. 월 1회 정도:

```bash
python3 scripts/sweep_state.py review-screened --older-than 90   # 90일+ 묵은 탈락분
```

상위 모델이 이 목록을 읽고, 잘못 버린 게 있으면:

```bash
python3 scripts/sweep_state.py restore-screened --pmids 38123456,38234567
```

→ screened_out에서 빠지고 seen에도 없으므로 다음 sweep 때 재부상한다. `status`의 `screened_by_topic`으로 특정 토픽 탈락률이 비정상적으로 높으면(=쿼리나 Haiku 룹이 과잉 배제) 쿼리식을 조인다.

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
  "seen_pmids": ["38123456", "..."],
  "screened_out": {
    "38999999": {"topic":"implant","edat":"2026/06/10","reason":"off-topic: orthopedic implant",
                 "verdict":"exclude","screened_by":"haiku","screened_on":"2026/07/14"}
  }
}
```
- **`seen_pmids`** = 이미 ingest 결정(영구 재부상 금지). set 조회라 수천 단위여도 부담 없음.
- **`screened_out`** = Haiku 탈락 버킷. seen과 **분리** — 루틴 재부상은 막되 `review-screened`/`restore-screened`로 복구 가능. 이 분리가 false-negative 영구소실을 막는 스키마적 장치다(프롬프트 룰만으론 불충분).
- 큐(`queue.md`)와 상태(`state.json`)도 분리 — 큐는 사람이 읽고 ingest가 소비, state는 기계 상태. `screened-out.md`는 탈락 사람이 읽는 로그(append-only).
- 하위호환: 기존 state.json에 `screened_out` 키가 없어도 모든 커맨드가 `.get(...,{})`로 안전; 키는 첫 `screen-out` 때 생긴다.

## Reference / Scripts

- 저장소 루트 `references/topic-queries.md` — 토픽별 PubMed 쿼리식 카탈로그(canonical). 새 토픽 추가·쿼리 튜닝은 여기서 (skill 본문이 아니라 이 파일을 고치게 유도). `skills/literature-surveillance/references/topic-queries.md`는 스텁이니 편집하지 말 것.
- `scripts/sweep_state.py` — 상태·중복·큐 I/O. 서브커맨드: `init` / `load` / `dedup` / `enqueue` / `screen-out` / `review-screened` / `restore-screened` / `status`. 사용법은 `--help`. (심층 sweep 3종 — `screen-out`/`review-screened`/`restore-screened` — 은 위 "심층 sweep 모드" 섹션 참조.)

## 경계

- 이 skill은 **무엇을 ingest할지 고르는** 단계까지만. PDF 다운로드·위키 항목 작성은 llm-wiki-ingest / dental-wiki-entry 소관.
- OA 접근경로 전체 탐색(Unpaywall→preprint→author request→RISS 등)은 ingest 단계. 여기선 PMC 유무만 빠르게 태깅.
- 필터 계층: ptyp·신규성(쿼리/dedup) → [심층 모드 한정] Haiku **topical 관련성** → 상위 모델(borderline·include 종합). **임상적 가치 판단(이 논문이 정말 중요한가)은 여전히 큐 적립 후 사람 몫** — Haiku도 상위도 "주제 적합성"까지만 본다.
