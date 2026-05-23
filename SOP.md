# LLM Wiki — 운영 SOP
**Standard Operating Procedure** — 표준작업절차서

논문 1편 추가부터 사이트 반영까지의 표준 작업 절차. 본인 참고용.

작성: 2026-05-21 · v1

---

## 0. 시스템 개요

```
PDF                                      GitHub
 ↓                                         ↑
papers/  →  sources/  →  wiki/    →    git push
            (영문 요약)   (영문 + 한줄요약)        ↓
                                       GitHub Actions
                                         ↓ (자동)
                                  ezinternet.github.io/llm-wiki/
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
python3 scripts/lint.py            # frontmatter 필수 9개 필드
python3 scripts/orphan-check.py    # PDF ↔ sources 1:1 매칭
python3 scripts/find-no-wiki.py    # 모든 paper에 wiki 페이지
```

3개 모두 ✅이면 GitHub Actions도 통과 확신.

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
- 사이트: https://ezinternet.github.io/llm-wiki/ — 새 페이지가 explorer + graph 노드에 반영

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

### Lint 4종 한 번에

```bash
cd ~/llm-wiki
python3 scripts/lint.py && \
python3 scripts/orphan-check.py && \
python3 scripts/find-no-wiki.py && \
python3 scripts/operations-lint.py
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
- 사이트: https://ezinternet.github.io/llm-wiki/
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

## 10. 다음 작업 후보 (선택 사항)

1. **자동 watcher 확장** — `.claude/scripts/ingest-watcher` 기능 검토, PDF만 떨어뜨려도 자동 ingest되게
2. **Graph 카테고리 색상** — 시각적 구분 추가 (quartz/components 수정)
3. **검색 한국어 형태소 분석** — 현재 substring만, 형태소 라이브러리 추가 가능
4. **모바일 PWA** — 휴대폰에 앱처럼 설치 가능하게
5. **Privacy 영역 분리** — 환자 메모·민감 자료는 wiki/ 밖 별도 폴더로 (이미 papers/ 는 gitignored)

---

마지막 업데이트: 2026-05-21
