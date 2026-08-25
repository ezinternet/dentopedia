# Daily Audit — 21 audits

> Split out of `CLAUDE.md` on 2026-07-17 to keep that file lean. `CLAUDE.md` keeps only the invariant (*signal, not gate*) and the entry-point command; the per-audit reference lives here. Open this file when adding/changing an audit or interpreting a log in `logs/`.

A single entry-point runs all 21 audits and writes their logs to `logs/`:

```bash
python3 scripts/daily-audit.py
```

> Runtime note: it looks hung for ~15 min on `ingest-rationale-lint`. Needs Homebrew python3 (3.10+) on PATH or 4 scripts crash on PEP604 hints.

---

## The 21 audits — 3 classic + 1 rationale (errors block) + 17 signals

| Audit | Type | Purpose |
|---|---|---|
| `lint.py` | error | **두 범위를 돈다.** ①**빌드 안전성 — `wiki/` 전체, 예외 없음**: frontmatter 최상위 키 중복 + YAML 파싱. ②**논문 필드 — `SKIP_DIRS` 제외**: 필수 필드·근거등급 vocab·아티팩트 경로 쌍. 이 분리는 2026-08-25 사고의 산물이다 — `wiki/overviews/patient-safety-culture-dentistry-overview.md`에 `date:`가 두 번 들어가 GitHub Pages 배포가 하루 넘게 실패했는데, **키 중복 검사는 그때도 이미 있었고 `overviews`가 `SKIP_DIRS`에 있어 스캔되지 않았을 뿐이다.** 검사가 있어도 안 도는 곳에 있으면 없는 것과 같다: 로컬 감사 21개·CI Wiki Lint 전부 초록불인 채 공개 배포만 조용히 깨졌다. 범위를 배포와 일치시킨 근거는 워크플로가 `cp -r wiki/.`로 **`wiki/` 전부**를 Quartz content로 넣는다는 것 — 검사 범위 ≠ 빌드 범위이면 같은 사고가 반복된다. 실측 구멍 304개 파일(overviews 277·evidence-appraisal 15·_lint 9·_meta 1·wiki/index.md·category-map). 키 중복을 **문자열 파싱으로** 따로 보는 이유: PyYAML `safe_load`는 중복 키에서 마지막 값을 조용히 채택해 절대 안 잡고, Quartz의 js-yaml만 `duplicated mapping key`로 빌드를 exit 1로 죽인다 — 즉 로컬 YAML 검사로는 원리상 검출 불가능하다 |
| `operations-lint.py` | error | OPS files (agenda/slides/interactives) cross-link chain |
| `orphan-check.py` | error | PDFs ↔ sources 1:1 matching |
| `synthesis-backlog.py` | signal | sources/ not referenced by any overview, stale ≥30d |
| `ingest-rationale-lint.py` | error (post-cutoff only) | `## Why Ingested` on sources ingested ≥ 2026-05-27 |
| `category-overflow.py` | signal | wiki categories with ≥5 unsynthesized papers → overview candidates |
| `overview-thesis-staleness.py` | signal | overview의 git log를 wikilink-only vs thesis edit으로 분류해 진짜 stale overview 식별 (mtime은 wikilink-only ingest로 갱신돼 부정확) |
| `overview-coverage-lint.py` | signal | overview 본문 cov% (linked paper 중 본문 author·year로 인용된 비율) — 낮으면 thesis 분기·표·결정 트리에 paper 반영 안 됨 |
| `output-coverage-lint.py` | signal | synthesis-backlog의 **출력 방향 거울**: overview가 downstream 산출물(`slides/`·`interactives/`·lectures)로 꺼내 쓰였나 (Express leg) |
| `recall-coverage-lint.py` | signal | overview 중 `recall/{stem}.json` 리콜 스펙이 없는 것 = **기억 백로그** (retention 축, output-coverage와 짝). forward-only — 신규 overview 저작 시 3문항 동반, 소급 백필 없음 |
| `doi-duplicate-check.py` | signal | 동일 DOI·다른 stem 검출 + 제목 정규화 fallback(한쪽 DOI 비거나 불일치라 DOI로 못 잡는 동일논문) — orphan-check가 못 잡는 cross-stem 중복 가시화 |
| `supersession-audit.py` | signal | `superseded_by` 깨진 링크 + 필드↔본문 배너 sync + decay 후보(sr+ma/sr/rct 중 5년↑ 미대체, 카테고리·중심성 집계) — living-document 갱신을 신호화. **transitivity 검사(A→B, B→C면 A는 C를 가리켜야 한다)는 `full`에만 타당하다** — `partial`은 축(axis)별로 일어나 합성되지 않으므로, C가 B에게서 넘겨받은 축이 B가 A에게서 넘겨받은 축과 다르면 A의 포인터는 B에 남는 게 맞다. 그 판단을 내렸으면 A에 `supersession_chain: intentional`(필드 정의는 `INGEST.md`)을 달고 **이유는 배너에 적는다**; 감사는 그 행을 `chain stale`에서 빼되 `chain intentional (선언)`로 따로 세어 체인 tail까지 계속 출력한다(뮤트가 아니라 이동). 실사례: `avila-ortiz-2014`(2026-08-15) |
| `relations-audit.py` | signal | `relations:` typed edge target 실존·vocab 검증 + 타입 분포 + typed-edge JSON export(Quartz/custom 렌더용). **+ `CIRCULAR reinforces`**(별도 집계, issues에 미합산): 파생문서가 자기 원료를 "독립 확인"한다는 주장 — overview→구성논문(C1)·논문→자기를 재료로 쓴 overview(C2). `reinforces`의 정의가 *독립적* 확인이므로 순환이다. 2026-07-17 실측 152건(=전체 reinforces의 13.3%), 30건 표본의 독립 추정(~115건)과 수렴. 신호일 뿐 — overview가 교차 독해로 구성논문을 한정하면 진짜 `refines`이고, 단순 재서술이면 엣지를 빼도 멤버십은 안 사라진다(대상 227/227이 본문 wikilink로도 존재) |
| `link-integrity.py` | signal | 본문 `[[wikilink]]` 깨짐 + index.md 양방향 커버리지 (Astro-Han lint 개념 차용). `INDEX_EXEMPT_DIRS`(현재 `wiki/_meta/`)는 **등재 의무만** 면제 — 라우팅용 참조 문서라 독자용 카탈로그에 넣을 대상이 아니다. `SKIP_DIRS`가 아니라 별도 상수인 이유: `SKIP_DIRS`에 넣으면 link 대상 해석에서도 빠져 `[[_meta/categories]]`가 broken으로 잡히고, `pages` 자체에서 빼면 그 페이지의 **나가는** 링크가 깨짐 검사에서 누락된다 (2026-07-31) |
| `overview-catalogue-lint.py` | signal | 위 항목의 **좁은 짝**: 각 overview가 index.md에 자기 `- [[overviews/x]]` **카탈로그 목록 항목**을 갖는가 = 목록을 훑는 독자에게 보이는가. link-integrity는 index.md 안 어디든 wikilink 한 번이면 커버리지로 세므로, **다른 항목 설명문에만 언급된 페이지는 통과시킨다** — 그 사각지대만 본다. 2026-07-18 실측 근거: `patient-consultation-communication-protocol`이 2026-06-03 생성 후 약 6주간 blockquote 언급만 있고 카탈로그 항목이 없었는데 link-integrity 로그 42개 어디에도 안 나타났다(설계상 정상). 동시점 관례는 242개 중 239개가 bullet 항목·blockquote-only는 그 1건뿐이라 규칙이 분명하다. dangling(항목→실존X)도 함께 검사 |
| `interactive-staleness.py` | signal | 임상 interactive 도구의 `source_wiki` 근거가 도구보다 git상 최신이면 STALE(LLM 재작성 후보), 근거 경로 소실이면 BROKEN. meta/통계 도구는 제외(build-wiki-stats.py가 배포 때 재생성). 임상 수치 자동 재작성은 Rule #1 위배라 신호만 |
| `find-contradiction-candidates.py` | signal | 본문에 명시적 충돌 표현(contradict/counterpoint/반박 등)이 있으나 **그 쌍이 아직 판단되지 않은** 논쟁 레이더 백필 후보. "판단됨"의 정의는 아래 *논쟁 레이더 — 억제 조건* 참조 (억제가 이 감사의 설계 전부다). Tier1(키워드에 가장 가까운 wikilink로 대상 지목)·Tier2(대상 불명/너무 멂/동일 줄 비최근접/soft). 기계가 충돌을 확정하지 않고 신호만 — LLM이 두 페이지 읽고 판단해 엣지를 단다. **type_hint를 그대로 엣지로 옮기지 말 것** — 2026-07-17 전수 검토에서 contradicts 계열 지목 122건 중 실제 contradicts는 1건이었다 |
| `content-lint.py` | signal | frontmatter lint가 못 보는 **본문 내용 규칙**을 결정론으로 검사: (A) 이중언어 세줄요약 쌍 + overview 한국어 핵심요약 콜아웃, (B) heading 태그 일관성, (C) wiki↔source cross-tier 정합(`source:` 실존·pmid 일치), (D) 레거시 frontmatter 키 `confidence:`(2026-07-15에 `evidence_level:`로 개명) — 소비 측이 두 키를 다 읽어서 **다른 어느 감사에도 안 걸리는** 드리프트. 발견 시 `scripts/migrate-confidence-field.py --apply`로 일괄 수정 |
| `retraction-audit.py` | signal | `retraction_status: RETRACTED` 페이지가 **인용 사고를 실제로 막는 구조**인지 검사. 핵심은 **경고가 섹션 제목 안에 있는가** — QMD는 청크로 검색하므로 페이지 상단 콜아웃은 `## Results` 청크에 따라오지 않는다(사람이 페이지를 열 때만 작동하는 경고는 답변 생성 경로를 못 막는다). 그 외: 필수 3섹션(Why This Page Exists / What We Can NOT Use / What It Does Tell Us), typed 엣지 **양방향 0**(철회 논문이 overview 합성에 살아있는 관계로 조립되면 안 됨). 역방향으로 필드 누락 의심도 검출. `grep retracted`는 교정과 'canine retraction'(견인)에 걸려 못 쓰므로 기계 판독 고리는 `retraction_status:` 필드뿐 |
| `overview-volatility-audit.py` | signal | **채점 단위가 페이지가 아니라 overview**인 유일한 감사 — 논문이 뭐라고 했는지는 안 바뀌고, 바뀌는 건 그 논문들을 묶어 내린 결론이다. 새 신호를 수집하지 않고 기존 감사 신호를 종합 단위로 롤업해 "어느 결론이 먼저 뒤집힐까"로 정렬한다. 성분: ①마지막 thesis 편집 이후 유입 논문 수(신규 신호) ②thesis 노후 ③구성 논문 간 `contradicts`×2+`refines` ④고근거(sr+ma/sr/rct) 중 7년 경과+`superseded_by` 없는 비율 ⑤최신 논문 공백. 철회 논문 포함은 점수 성분이 아니라 **하드 플래그**(점수에 녹이면 묻힌다). 두 함정이 실측으로 확인돼 대응돼 있다 — (a) 구성 논문을 `source_papers` frontmatter로만 읽으면 안 된다(2026-08-02 실측 262편 중 90편만 보유, 나머지는 본문 wikilink뿐이라 ③④⑤가 통째로 죽었다), (b) 정비 커밋(overview 10편 이상 동시 수정)을 thesis 편집으로 세면 안 된다(229편 필드 마이그레이션 하나에 전편 나이가 15~19일로 붕괴했고 ①churn도 같이 오염됐다). ②의 정규화 상한은 리포 히스토리 창에 자동 연동 — 첫 커밋이 2026-05-18이라 고정 365일 상한에서는 성분이 죽는다. 가중치·티어 경계는 캘리브레이션 전 잠정값이므로 **절대점수가 아니라 티어와 성분 내역으로 읽을 것**. `interactives/volatility-index.html`은 `--html` 로만 생성 |
| `deviation-audit.py` | signal | `logs/ingest-deviations.md` 집계 — SOP 개정 후보 출력 (Rule-of-Three trigger). **억제가 이 감사의 설계 절반이다** — 원판은 누적 ≥3 기준이었고, 로그가 334건까지 자라자 **20종 중 16종이 후보**로 찍혀 신호가 죽었다 (2026-08-25 실측). 논쟁 레이더와 같은 교훈: *억제되지 않는 신호는 끌 수 없고, 끌 수 없는 신호는 노이즈가 된다.* 억제 3겹 — **①판단 기록형 6종 제외**(`relation`/`category`/`confidence`/`supersession`/`evidence-level`/`reporting-judgment`): SOP 위반이 아니라 **SOP가 시킨 대로 판단을 남긴 것**이라 개정 후보로 띄우는 게 범주 오류다(실측 100건, 전체의 30%). **②자기소멸형 제외**(`batch-relation-pending`): "배치라 relations를 나중에 달겠다"는 예고이고 2026-08-25 전수 확인에서 17건 **전부** relations 8~26개로 해소돼 있었는데 로그가 append-only라 영구히 카운트됐다. **③임계값을 누적수가 아닌 최근 30일 창으로**(`--window`로 조정): 누적수는 위키가 사는 한 단조증가라 임계값이 의미를 잃는다 — 판단 기준은 "지금 반복되고 있는가"다. 억제는 **뮤트가 아니라 이동**이다 — 제외된 유형도 하단 참고 블록에 누적/최근 수와 함께 계속 출력한다(supersession-audit의 `chain intentional`과 같은 처리). `EXTERNAL_CONSTRAINT_TYPES`(abstract-only·empty/partial-pmc-text·no-doi·date-fallback)는 후보에서 빼지 않되 근본원인이 페이월·PMC 추출이라 SOP 개정 폭이 좁다고 태그만 단다. 적용 후 후보 16종 → 5종(그중 실제 공정결함 3종) |

**Signals never block.** They're a mirror — the principle is that ingest pressure self-corrects via visibility, not via gates (which trigger burnout/avoidance in clinical workflows). This is a load-bearing design choice, not laziness; see *Design Principles* in `CLAUDE.md`.

## 논쟁 레이더 — 억제 조건

키워드 매칭은 오탐이 지배적이라(2026-07-17 전수 검토: contradicts 계열 122건 중 실제 1건) **무엇을 억제하느냐가 이 감사의 설계 전부**다. 억제되지 않는 신호는 끌 수 없고, 끌 수 없는 신호는 노이즈가 된다.

**① 이미 판단된 쌍 — typed 엣지·supersession (양방향)**

`relations:` 엣지는 **타입 무관**으로 억제한다. contradicts/refines만 인정하던 시절엔 extends·reinforces로 이미 연결된 쌍이 매일 재방출됐다(2026-07-17: Tier1 122건 중 96건이 이 오탐, 전수 검토 결과 96건 모두 기존 타입이 옳았다).

판단의 근거는 **네 방향 모두**에서 읽는다 — 어느 쪽에 기록됐든 저자가 그 쌍을 보고 판단했다는 사실은 같기 때문이다.

- 자기 `relations:` 엣지
- 자기 `superseded_by:` 포인터 *(2026-08-15 추가)* — 대체 관계는 `relations:`가 아니라 전용 필드에 산다. 레이더가 그걸 몰라서, **정상 처리를 마친** 대체 쌍이 매일 돌아왔다. 대체 배너 문구가 "뒤집음"·"overturn" 그 자체다.
- **자기가 대체한** 옛 페이지 (역방향 색인) *(2026-08-15 추가)* — `superseded_by:`는 옛 페이지에 있으므로, 새 논문이 자기가 뒤집은 옛 논문을 언급하는 (더 흔한) 방향은 위 항목으로 안 잡힌다. `canullo-2021 → avila-ortiz-2019`가 이 구멍으로 Tier 1에 재등장했다.
- **다른 페이지가 이쪽으로 단** 엣지 (incoming 색인) *(2026-08-15 추가)* — 엣지는 한쪽에만 단다. `farina-2026 extends → lamont-2018`이 있는데도 `lamont-2018 → farina-2026`이, `gehrke-2020`·`di-fiore-2018`이 osteotomy overview로 엣지를 갖고 있는데도 그 반대 방향이 후보로 떴다.

대체 배너는 여러 줄 Obsidian 콜아웃이고 링크는 헤더 줄에만 있는데 **충돌 키워드는 항상 둘째 줄에 있어**, 후속 `>` 줄이 헤더 target을 상속하게 했다. 상속은 **대체 배너로만** 한정한다 — 모든 blockquote로 넓히면 `[!summary] 한국어 핵심요약`에서 앞 bullet 링크가 뒤 bullet으로 새어 과억제된다. `--selftest`가 배너 4가지 표기와 **매치되면 안 되는** 콜아웃 2가지를 함께 고정한다.

**② 부정문 — 충돌의 *부인*** *(2026-07-18)*

"reinforcing rather than **overturning**", "이는 결론을 **뒤집는** 것이 아니라"처럼 키워드가 부정 안에 있으면 충돌이 아니다. 부정어는 키워드에 **통사적으로 붙어** 있어야 한다 — 초안은 앞 60자에서 맨 `no`를 찾다가 진짜 신호를 죽였다("found **no** pain difference …, **whereas** this RCT detects a penalty"에서 `no`는 연구 결과의 일부지 whereas의 부정이 아니다). 그래서 맨 `no`는 빼고, 창을 30자로 좁히고, 뒤쪽 창은 한국어 전용으로 뒀다(한국어는 부정이 키워드 뒤에 온다). 회귀 테스트 12케이스가 `--selftest`에 있다 — **필터를 손대면 먼저 돌릴 것.**

**③ 검토했고 엣지 불필요 — `logs/relation-negatives.md`**

판정 결과가 "엣지 없음"이면 엣지가 안 생기므로 다음날 같은 후보가 그대로 뜬다. 판정 노동이 통째로 증발하는 구조다. 이 대장이 그 빠진 반쪽이다 — **부정 판정도 지식이다.**

키는 `(source, target, 충돌문장 해시)`다. `(source, target)`만으로 잡으면 페이지가 개정돼 **진짜 충돌이 새로 생겨도** 영원히 억제된다. 문장이 바뀌면 해시가 달라져 자동으로 재검토 대상이 되는 것이 옳은 동작이다. 대상 미지정 후보는 target을 `NOTARGET`으로 적는다. 기록은 `scripts/log-relation-negative.py <source> <target|NOTARGET> "<문장>" "<사유>"`.

**억제가 도달할 수 없는 지점** — 2026-08-15에 Tier1/Tier2를 0/0으로 비우며 76건을 전수 판정한 결과, 최대 그룹(HIGH-no-target 46건)은 구조적으로 대장 행 말고는 답이 없었다: 이미 다른 곳에 typed된 충돌을 산문으로 서술하거나(줄에 링크가 없다), 논문 **자기 내부**의 불일치·결과 요약이거나, 같은 문장이 스스로 해소하는 겉보기 충돌이거나(투여경로·인구집단 차이), 페이지에 이미 "공식 엣지는 달지 않는다"고 적힌 판정이었다. 나머지 오탐의 최대 원인은 **최근접 링크 규칙의 대상 오지목** — 문장이 말하는 충돌 상대가 같은 줄의 다른 논문인데 키워드에 가까운 링크가 엉뚱하게 집히는 경우다.

## The three compounding metrics

Run daily (manual or cron). Watch these over time:

- **synthesis-backlog %**: should trend up (more sources getting linked from overviews).
- **category-overflow count**: should trend down as overviews get written.
- **thesis-staleness warn/info**: should stay low — overview 본문이 정기적으로 refresh되는지 보는 signal.

## Closing the loop — audit signals → morning briefing

Audits only compound if someone reads them; leaving that to memory is the weak link. The intended terminal is a one-line badge in the morning-briefing pipeline (STALE overview N건, category-overflow N건, BROKEN link N건) so the day's top signals surface without opening `logs/`. Design: `agenda/2026-07-15_audit-to-briefing-bridge.md`.

Design rationale (audit set): see `agenda/2026-05-26_synthesis-enforcement-setup.md`.
