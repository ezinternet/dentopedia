# LLM Wiki — 운영 SOP
**Standard Operating Procedure** — 표준작업절차서

논문 1편 추가부터 사이트 반영까지의 표준 작업 절차. 본인 참고용.

작성: 2026-05-21 · v1 / 개정: 2026-06-23 · v2

---

## 0. 시스템 개요

```
PDF                                      GitHub
 ↓                                         ↑
papers/  →  sources/  →  wiki/    →    git push
            (영문 요약)   (영문 + 한줄요약)        ↓
                                       GitHub Actions
                                         ↓ (자동)
                                  ezinternet.github.io/dentopedia/
```

- **3-tier 구조**: 원본 PDF → 영문 summary → wiki page
- **자동 deploy**: wiki/, index.md, quartz/ 변경 시 GitHub Actions가 Quartz 빌드 + GitHub Pages 게시
- **Lint workflow**: frontmatter / 1:1 매칭 / no-wiki 검사 자동 실행

---

## 1. 새 논문 추가 — 표준 5단계

### Step 1 — PDF를 papers/ 폴더로 cp

```bash
cp /path/to/new-paper.pdf ~/llm-wiki/papers/
```

파일명은 임의로 둬도 됨 (Claude가 ingest 시 표준 stem으로 rename).

### Step 2 — Claude 세션에서 ingest 요청

Cowork 세션 열고 한 줄:

```
새 논문 추가해줘: ~/llm-wiki/papers/<파일명>.pdf
```

여러 편 일괄:

```
papers/ 폴더에 새로 들어온 PDF들 다 ingest해줘
```

Claude가 자동 수행 (CLAUDE.md Step 1~4):

1. PDF 텍스트 추출 (pypdf, 15페이지)
2. 표준 stem으로 rename (`{author}-{year}-{title-5-words}.pdf`)
3. `sources/{stem}.md` 작성 (영문 요약, 7섹션)
4. `wiki/{category}/{stem}.md` 작성 (영문 wiki + 한줄요약 + frontmatter)
5. `index.md`의 해당 카테고리에 한 줄 entry 추가

### Step 3 — 로컬 lint 점검 (선택, 권장)

```bash
cd ~/llm-wiki
python3 scripts/lint.py                          # frontmatter 필수 9개 필드
python3 scripts/orphan-check.py                  # PDF ↔ sources 1:1 매칭
python3 scripts/find-no-wiki.py                  # 모든 paper에 wiki 페이지
python3 scripts/supersession-audit.py --ci       # 깨진 링크·배너 desync → exit 1
```

4개 모두 ✅이면 GitHub Actions도 통과 확신. `--ci`는 decay 후보는 무시하고 hard error(dangling / desync / transitivity chain)만 잡는다.

### Step 4 — git commit + push

```bash
cd ~/llm-wiki
git add -A
git commit -m "Add: {paper title or category summary}"
git push origin main
```

한 줄 압축:

```bash
cd ~/llm-wiki && git add -A && git commit -m "Add new paper(s)" && git push
```

### Step 5 — 자동 deploy 확인

push 후 1~2분, 다음 확인:

- Actions: https://github.com/ezinternet/llm-wiki/actions — 두 workflow 모두 ✅
- 사이트: https://ezinternet.github.io/dentopedia/ — 새 페이지가 explorer + graph 노드에 반영

---

## 1-bis. Literature Surveillance — ingest 앞단 (2026-06-19 추가)

섹션 1 ingest가 "손에 든 PDF를 위키로" 넣는 거라면, surveillance는 그 *앞단* — "무엇을 넣을지" PubMed에서 골라 큐를 채운다.

### skill 구성

- `literature-surveillance/` : `SKILL.md` + `scripts/sweep_state.py` + `references/topic-queries.md`
- 상태·큐: `.surveillance/state.json` (토픽·seen-pmids), `.surveillance/queue.md` (인제스트 대기 목록)
- skill은 자동 cron이 아님 — 호출 시 1 sweep만 돈다. 정기 자동 실행은 launchd로 깨워야 함 (선택).

### 1 sweep 절차 (Cowork 한 줄: "○○ 토픽 감시 돌려줘")

1. **load** — `python3 scripts/sweep_state.py load` : 토픽셋 + 토픽별 last-run 출력.
2. **검색** — 토픽별 PubMed `search_articles`. 신규성은 `datetype=edat`(등재일) 기준, 노이즈는 `[tiab]` phrase로 차단.
3. **dedup** — `sweep_state.py dedup` : seen-pmids·큐에 있는 건 제외하고 신규만.
4. **OA 판정** — `get_copyright_status`/PMC 링크로 `OA:PMC` / `OA:none` 태깅.
5. **enqueue** — `sweep_state.py enqueue` : `queue.md` 적립 + seen·last-run 갱신.
6. 채워진 큐를 섹션 1 ingest 5단계로 넘긴다.

### 토픽 쿼리 (references/topic-queries.md에서 관리)

- phrase(`[tiab]`) 필수. 풀어 쓰면 노이즈 유입 — 실측: IIP를 풀어 쓰면 32건 중 12건이 osseodensification·ridge mesh 등 무관 논문.
- implant은 4세분(iip / loading / soft-tissue / grafting), ptyp는 state.json에서 RCT+SR+MA로 관리.
- PubMed가 IIP를 `Immediate Dental Implant Loading[MeSH]`로 색인 → 식립(IIP)/즉시부하(IIL) 섞임, abstract에서 한 번 더 분리.

### 내 손 vs Claude

- **너**: 트리거 한마디 → 시범 1건 포맷 확인 → **git push** (게시는 항상 수동).
- **Claude**: 검색·dedup·OA판정·큐 적립 + (ingest 단계) 풀텍스트·sources/wiki 작성·PDF 다운로드·index·lint.

### OA 미확보 처리

PMC 없는 건(Elsevier·JOMI 등)은 Unpaywall·self-archive를 더 탐색 → 안 되면 보류. 불법 경로(Sci-Hub 등) 금지.

---

## 1-ter. Supersession 판단 — ingest 시 결론 충돌 처리 (2026-06-23 추가)

> **이 위키의 핵심 가치.** 논문은 누구나 쌓는다. "옛 결론과 새 결론이 충돌할 때 어느 쪽이 현재 정설인가"의 지도(`superseded_by`)만이 이 위키 고유의 자산이다. 이게 없으면 검색 시 2018년·2024년 논문이 동등한 무게로 튀어나와 모순 더미가 된다. CLAUDE.md `superseded_by:` 스펙(영어)을 임상 판단 순서로 풀어쓴 것.

**새 논문 인제스트마다 한 번 묻는다: "이게 기존 어느 페이지의 결론을 흔드나?"** forward-only — 과거 전수조사는 안 함, 들어올 때 한 번만 판단.

### 판단 4단계 (위에서부터 순서대로)

**0단계 — 충돌 후보를 찾는다**
- `## Why Ingested`에 거는 `[[wikilink]]` 대상 페이지가 1차 후보.
- QMD 의미검색으로 "같은 임상 질문을 다루는 기존 페이지"를 끌어온다.
- 여기서 안 걸리면 supersession 대상 없음 → 새 지식 추가로 끝.

**1단계 — 같은 질문에 *반대 답*인가?**
| 관계 | 처리 |
|---|---|
| 같은 질문 + 같은 결론 | `reinforces` (보강). 대체 아님 |
| 같은 질문 + **반대 결론** | → 2단계로 (supersession 검토 시작) |
| 범위만 넓힘 | `extends`. 대체 아님 |
| 조건 좁힘("이 하위집단에선") | `refines`. 대체 아님 |
| 다른 질문 | 무관 |

⚠️ "더 많은 걸 말한다" ≠ 대체. *범위 확장*은 `extends`다.

**2단계 — 근거 무게(evidence weight)를 비교 ← 가장 중요**

결론이 충돌해도 **새 논문이 더 강한 근거일 때만** 대체. "최신 ≠ 우월."

```
sr+ma > sr > rct > prospective > retrospective
      > cross-sectional > case-report > ... > narrative-review
```
- 새 논문이 사다리 **위** → 대체 강력 후보 (예: 옛 RCT 1건 ↔ 새 48-study SR+MA)
- 같은 등급인데 새 논문이 **더 큼/최신** (12-study SR → 48-study SR) → 대체 후보
- 새 논문이 사다리 **아래** → **대체 안 함** (2026 narrative-review는 2022 SR+MA 못 이김)
- 약한 근거가 강한 옛 결론에 반대 → **무시**(본문에 "한 in-vitro는 반대했으나" 정도만)

**3단계 — `full`이냐 `partial`이냐**
- `full` — 옛 페이지 결론이 통째로 교체. "현재 결정은 새 페이지를 따르라."
- `partial` — 일부만 낡음, 또는 옛 페이지가 고유 가치 유지(최초 종합·역사적 기준점·특정 하위집단). 애매하면 과장 말고 `partial`.

**4단계 — 표식은 *옛(older)* 페이지에 박는다**

frontmatter:
```yaml
superseded_by: tisci-2026-isq-it-mbl-survival-sr-ma   # 새 stem, >1이면 콤마
superseded_scope: full                                 # full | partial
```
본문 최상단(frontmatter 직후, `## One-line Summary` 앞) 배너 — **왜 대체됐는지 수치를 적어** 나중에 1초 검증 가능하게:
```markdown
> [!warning] Superseded (full) → [[tisci-2026-isq-it-mbl-survival-sr-ma]]
> 48-study SR+MA (r=0.44, p<0.001) overturns this 12-study NS result. (set 2026-06-23)
```
`partial`은 `> [!note] Partially superseded → [[...]]` + 옛 페이지가 아직 주는 게 뭔지 명시.

### 검증
- `python3 scripts/supersession-audit.py` — 깨진 링크 + 필드↔배너 sync + decay 후보(5년↑ 미대체 SR/RCT).
- 현재 상태(2026-06-23): 9 superseded, sync 이슈 0, decay 후보 200(2026-06-21 ib≥7 전수검증 완료 → ~2027 전 재검토 불필요).

### 한 줄 규칙
> **"같은 질문에 반대 답인가" → "새 쪽이 근거가 더 무거운가" → 둘 다 yes일 때만, 옛 페이지에 표식.** 이 두 관문이 "최신이 무조건 이기는" 실수를 막아 모순이 애초에 안 쌓이게 한다.

---

## 2. 자동화 수준별 옵션

| 옵션 | 사용자 작업 | Trade-off |
|---|---|---|
| **A. 수동 (현재 표준)** | PDF 떨어뜨림 → Claude 요청 → git push | 모든 단계 확인 가능, 안전. 매번 두 번 작업 |
| **B. Claude가 git push까지** | PDF 떨어뜨림 → Claude 요청만 | 단계 감소. git config 권한 필요, push 시점 통제력↓ |
| **C. ingest-watcher 활용** | PDF 떨어뜨림만 | 가장 자동화. watcher 기능 범위 사전 확인 필요 |

`.claude/scripts/ingest-watcher.log` 존재 — watcher가 셋업되어 있음. 기능 범위 확인 필요.

---

## 2-bis. OPERATIONS 폴더 사용법 (2026-05-23 추가)

KNOWLEDGE(papers/sources/wiki)는 지식 substrate, OPERATIONS는 그 지식을 산출물로 회수하는 7폴더.

### 폴더 역할 한 줄씩

| 폴더 | 무엇을 넣나 |
|---|---|
| `agenda/` | 모든 작업의 명세 (Goal·Input·Output·Done). 새 작업은 여기서 시작. |
| `interactives/` | HTML 계산기·시각화·의사결정 트리 |
| `slides/` | 강의·발표 자료 (위키가 1차 입력) |
| `peer-review/` | 외부 paper 리뷰 (저널 reviewer 의뢰) |
| `note-meeting/` | 미팅 기록 (1 미팅 = 1 파일) |
| `scripts/` | 자동화 코드 |
| `logs/` | audit 산출 |

### 새 작업 시작 — agenda 파일 1개

```bash
cd ~/llm-wiki
cp agenda/_template.md agenda/$(date +%Y-%m-%d)_<topic>.md
```

agenda 채우고 Cowork 세션 열어서 "이 agenda 진행해줘"라고 하면 Claude가 frontmatter cross-link 다 박아서 산출물 만든다.

### Hard rule: slides/interactives/peer-review는 agenda 선행

agenda 없이 슬라이드부터 만들지 말 것. 출처 추적이 끊긴다. Lint(`operations-lint.py`)가 잡아낸다.

### Lint 5종 한 번에

```bash
cd ~/llm-wiki
python3 scripts/lint.py && \
python3 scripts/orphan-check.py && \
python3 scripts/find-no-wiki.py && \
python3 scripts/operations-lint.py && \
python3 scripts/supersession-audit.py --ci
```

`operations-lint.py`가 검사하는 것:
- OPERATIONS 파일 frontmatter `type` / `date` / `status` 필수
- `source_wiki` / `agenda` / `output_wiki` 셋 다 비면 **orphan** (경고)
- slides·interactives·peer-review에 `agenda:` 없으면 **MISSING agenda** (hard rule 위반)

### 환자정보·민감정보 마스킹 — OPERATIONS 폴더 정책

**원칙**: 사이트(GitHub Pages)로 노출되는 건 `wiki/` 디렉토리만이다. deploy workflow가 `wiki/` → `quartz/content/`만 복사한다. OPERATIONS 폴더(agenda·note-meeting·peer-review 등)는 GitHub repo엔 올라가지만 **사이트엔 안 올라간다**.

그럼에도 마스킹 원칙:

1. **환자 식별정보**(이름·연락처·차트번호·생년월일)는 OPERATIONS 폴더 어디에도 평문으로 쓰지 않는다. `환자 A`, `case_001` 같은 익명 식별자만.
2. **직원 개인정보** 동일 기준.
3. **note-meeting**에 진료 사례 토론 들어가면 익명화 후 작성.
4. 외부 공유용 산출물(slides·peer-review)은 git push 전 한 번 더 확인.

**3중 방어**:
- 1차: deploy workflow trigger paths가 `wiki/**`로 한정 — agenda 수정해도 사이트 빌드 안 됨
- 2차: deploy workflow가 `wiki/`만 복사 — OPERATIONS 폴더는 content/에 안 들어감
- 3차: `quartz/quartz.config.ts` `ignorePatterns`에 OPERATIONS 폴더 이름 등록 — 실수로 wiki/agenda/ 같이 옮겨도 빌드 제외

그래도 git repo는 public이라면 OPERATIONS 폴더 내용이 GitHub에 보인다. 진짜 민감한 건 별도 `private/` 폴더(이미 `.gitignore`·`quartz` ignore 모두 등록됨) 또는 wiki/ 밖 별도 vault로.

---

## 3. 실패 시 대처

### Lint workflow 실패

원인: 새 wiki/{category}/{stem}.md frontmatter에 필수 필드 누락 또는 잘못된 값.

필수 9개 필드:

```yaml
---
title: "Paper Title"
authors: Author list
year: YYYY
doi: 10.xxxx/xxxx
source: {stem}.md
category: [category-folder]
confidence: sr+ma           # 또는 rct/prospective/retrospective/...
pdf_path: /Users/oracleneo/llm-wiki/papers/{stem}.pdf
pdf_filename: {stem}.pdf
---
```

`confidence` 값은 12개 중 하나 (sr+ma, sr, rct, prospective, retrospective, cross-sectional, case-report, in-vivo, animal, in-vitro, narrative-review, consensus).

### Quartz Build 실패

99% YAML frontmatter의 quote 안 된 특수문자.

문제 패턴:

```yaml
authors: Smith et al. (correspondence: Jane Doe)   # ✗ unquoted colon
title: Effects of A: A Comprehensive Review        # ✗ unquoted colon
```

수정:

```yaml
authors: "Smith et al. (correspondence: Jane Doe)" # ✓
title: "Effects of A: A Comprehensive Review"      # ✓
```

YAML 특수문자: `:` `[` `]` `{` `}` `&` `*` `#` `?` `|` `-` `<` `>` `=` `!` `%` `@`

이런 문자가 값에 포함되면 전체 값을 `"..."` 로 감싸기.

### 사이트 안 보임 (404 / RSS XML)

순서:

1. `~/llm-wiki/` 에서 `git log origin/main --oneline -2` — push 됐는지 확인
2. Actions 페이지에서 가장 최신 Deploy run의 commit hash 확인
3. 둘 다 ✓이면 시크릿 모드에서 사이트 접속 (RSS 확장 우회)
4. 그래도 안 보이면 build job 로그에서 "Found 0 input files" 또는 YAML error 검색

### "Found 0 input files" — wiki는 있는데 빌드 결과 비어있음

원인: 누군가 `.gitignore`에 `quartz/content` 같은 패턴 다시 넣었을 가능성. Quartz는 globby의 `gitignore: true` 옵션으로 .gitignore 자동 참조.

수정: `.gitignore`에서 해당 줄 제거.

---

## 4. 일괄 처리 — 여러 편 동시

### 시나리오: 한꺼번에 10~50편 추가

1. PDF 다 받아서 `~/llm-wiki/papers/` 에 떨어뜨림 (또는 임시 폴더에)
2. Cowork 세션:
   ```
   papers/ 폴더 전체 ingest해줘. 카테고리별로 분류해서.
   ```
3. Claude가 일괄 처리 후 결과 보고
4. 로컬 lint 3개 돌려서 확인
5. 한 commit으로 push:
   ```bash
   git add -A
   git commit -m "Bulk ingest: {N papers} — {category overview}"
   git push
   ```

### 카테고리 분류 가이드

Claude가 자동 판단하지만, 모호하면 method/procedure 기준 우선:

- "임플란트 SLA 표면 + ISQ" → `implants/surface/`
- "측방 sinus lift PRF" → `sinus-lift/lateral/`
- "근관 세정 PUI" → `endodontics/irrigation/`

질병이나 해부 부위 아니라 시술·기법으로 분류.

---

## 5. Graph View / 사이트 활용 팁

### 검색

좌측 검색창 또는 `Ctrl+K` — 페이지 제목·본문 substring 매칭. 한국어 substring도 검색됨.

### Graph View

- 우측 상단 미니 그래프: 현재 페이지 + 1-hop 이웃
- 클릭하면 전체 그래프로 확장 (Local Graph → Global Graph)
- 노드 색상은 기본 단색 (카테고리별 색상은 향후 quartz/quartz.layout.ts 수정으로 추가 가능)

### 백링크

우측 하단: 이 페이지를 인용하는 다른 wiki 페이지 자동 목록. `[[wikilinks]]` 추가하면 자동 반영.

### 모바일

URL 그대로 휴대폰 브라우저에서 접속. Quartz가 모바일 반응형 — 좌측 explorer는 햄버거 메뉴로.

---

## 6. 사이트 외관 조정 (선택)

수정 후 push하면 자동 반영.

### 색상 / 폰트

`quartz/quartz.config.ts`:
- `theme.typography.header` / `body` / `code`
- `theme.colors.lightMode` / `darkMode`

### Layout / Component

`quartz/quartz.layout.ts`:
- 좌측·우측 사이드바 컴포넌트 추가·제거
- Graph 위치
- Footer 링크

### Ignore 패턴

`quartz/quartz.config.ts`의 `ignorePatterns` — 빌드에서 제외할 폴더·파일 글로브.

---

## 7. 주요 파일 위치

| 파일 | 용도 |
|---|---|
| `CLAUDE.md` | Claude 에이전트 행동 규약 (글로벌 + 프로젝트) |
| `SOP.md` (이 파일) | 본인 참고용 운영 절차 |
| `index.md` | 카테고리별 페이지 목록 (legacy, lint trigger 대상) |
| `wiki/index.md` | Quartz 홈페이지 (frontmatter 필수, 자동 deploy 대상) |
| `papers/` | 원본 PDF (gitignore — GitHub에 안 올라감) |
| `sources/` | 영문 요약 markdown |
| `wiki/` | 최종 wiki 페이지 (Quartz가 빌드) |
| `quartz/` | Quartz 정적 사이트 생성기 + config |
| `.github/workflows/lint.yml` | frontmatter / 1:1 / no-wiki 검사 |
| `.github/workflows/deploy-pages.yml` | Quartz 빌드 + GitHub Pages 게시 |
| `scripts/lint.py` | frontmatter 9 필드 검사 (wiki/) |
| `scripts/orphan-check.py` | PDF ↔ sources 1:1 매칭 |
| `scripts/find-no-wiki.py` | paper마다 wiki 페이지 존재 검사 |
| `scripts/operations-lint.py` | OPERATIONS frontmatter cross-link 검사 |
| `agenda/` | 작업 명세서 (Goal·Input·Output·Done) |
| `interactives/` | HTML 시각화·계산기 |
| `slides/` | 강의·발표 자료 |
| `peer-review/` | 외부 paper 리뷰 |
| `note-meeting/` | 미팅 기록 |
| `logs/` | audit 산출 로그 |

---

## 8. 환경 정보 — 최초 셋업 (참고)

- GitHub repo: https://github.com/ezinternet/llm-wiki
- 사이트: https://ezinternet.github.io/dentopedia/
- Quartz 버전: v4.5.2
- Node.js: 22 (GitHub Actions에서)
- 호스팅: GitHub Pages (Source: GitHub Actions)
- 가시성: Public (Pages 활성화 조건)

---

## 9. 자주 쓰는 명령어 모음

```bash
# wiki 폴더로 이동
cd ~/llm-wiki

# lint 4종 한 번에
python3 scripts/lint.py && python3 scripts/orphan-check.py && python3 scripts/find-no-wiki.py && python3 scripts/operations-lint.py

# 변경 확인
git status -s

# 압축 commit + push
git add -A && git commit -m "Add new paper(s)" && git push

# 미푸시 commit 확인
git log origin/main..HEAD --oneline

# 최근 commit 5개
git log --oneline -5

# 마지막 Quartz deploy 상태
gh run list --workflow=deploy-pages.yml --limit 3   # gh CLI 설치 시
```

---

## 2-ter. Supersession CI 편입 (v2 추가)

`supersession-audit.py --ci`가 GitHub Actions lint workflow의 5번째 step으로 편입됐다.

| 검사 유형 | --ci 동작 | 일반 실행 |
|---|---|---|
| Dangling link (target stem 없음) | **exit 1** (CI fail) | 로그만 |
| Banner desync (필드↔배너 불일치) | **exit 1** (CI fail) | 로그만 |
| Transitivity chain stale (A→B, B→C인데 A가 B 가리킴) | **exit 1** (CI fail) | 로그만 |
| Decay 후보 (5년↑ 고근거, 미대체) | exit 0 (pass) | 로그만 |

fix 절차: 로컬에서 `python3 scripts/supersession-audit.py --stdout` 실행 → ⚠ 항목 수정 → 재커밋.

---

## 2-quater. OPERATIONS 폴더 민감도 정책 (v2 추가)

현재 `agenda/`·`note-meeting/`·`peer-review/` 등 OPERATIONS 폴더는 public repo에 올라가지만 사이트에는 노출 안 된다(deploy workflow가 `wiki/`만 복사). 진짜 민감 자료(환자 식별 가능 정보, 법적 분쟁 자료)는 별도 처리:

**단기**: `private/` 폴더 사용 (이미 `.gitignore` + `quartz ignorePatterns` 등록).

**장기(선택)**: OPERATIONS 폴더를 private repo로 분리.
1. `git subtree split --prefix=agenda/ -b split-agenda` 등으로 폴더별 히스토리 분리
2. private repo `llm-wiki-ops` 생성 후 push
3. `llm-wiki` 에서 OPERATIONS 폴더 제거 + `.gitignore` 갱신
4. Claude 세션에서는 두 repo 모두 접근 (별도 작업 디렉토리)

이 마이그레이션은 수동 작업이며 SOP에서 완료 시 이 항목을 갱신한다.

---

## 2-quinquies. 근거 등급 단일 참조 (v2 추가)

등급 정의·supersession 규칙은 **`references/evidence-ladder.md`** 가 유일한 출처다. `confidence:` 값 선택, supersession 판단 기준, `rob:` 보조 필드 모두 이 파일 참조. CLAUDE.md·SOP.md 내 인라인 설명은 요약이고, 충돌 시 `evidence-ladder.md` 우선.

RoB 필드 (옵션, rct 이상 논문에서 동등 등급 충돌 시 판단 보조):
```yaml
rob: low         # low | some-concerns | high
```

---

## 6-bis. Quartz 버전 drift 관리 (v2 추가)

Quartz는 `npm` 패키지로 관리된다. 커스텀 수정(`quartz/` 하위 직접 편집)이 있으면 upstream 업그레이드 시 충돌이 날 수 있다.

### 주기적 점검 (분기 1회)

```bash
cd ~/llm-wiki
npm outdated          # 현재 버전 vs latest 확인
```

Quartz 패치 버전(4.5.x → 4.5.y) → 직접 `npm update` 후 로컬 빌드 확인 후 push.  
Quartz 마이너(4.5 → 4.6) → 변경 노트 먼저 확인, 커스텀 파일과 충돌 검토 후 적용.

### 커스텀 파일 격리 패턴

Quartz 원본 파일을 직접 수정하지 말고, 커스텀 파일을 별도 경로로 유지:

```
quartz/
  quartz.config.ts       ← upstream 원본 (minimal edit만)
  quartz.layout.ts       ← upstream 원본 (minimal edit만)
  custom/                ← 우리 커스텀만 (새 컴포넌트, 테마 오버라이드)
    CustomFooter.tsx
    custom.scss
```

업그레이드 후 `quartz/custom/`만 다시 연결하면 충돌 최소화.

현재 버전: Quartz v4.5.2 (2026-05-21 기준). 다음 점검: 2026-09.

---

## 10. 다음 작업 후보 (선택 사항)

1. **자동 watcher 확장** — `.claude/scripts/ingest-watcher` 기능 검토, PDF만 떨어뜨려도 자동 ingest되게
2. **Graph 카테고리 색상** — 시각적 구분 추가 (quartz/components 수정)
3. **검색 한국어 형태소 분석** — 현재 substring만, 형태소 라이브러리 추가 가능
4. **모바일 PWA** — 휴대폰에 앱처럼 설치 가능하게
5. **Privacy 영역 분리** — 환자 메모·민감 자료는 wiki/ 밖 별도 폴더로 (이미 papers/ 는 gitignored)

---

마지막 업데이트: 2026-06-23 · v2 (6개 개선 반영: supersession CI·OPERATIONS 정책·근거사다리 통합·transitivity chain·버전 drift)
