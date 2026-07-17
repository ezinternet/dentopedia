# Daily Audit — 19 audits

> Split out of `CLAUDE.md` on 2026-07-17 to keep that file lean. `CLAUDE.md` keeps only the invariant (*signal, not gate*) and the entry-point command; the per-audit reference lives here. Open this file when adding/changing an audit or interpreting a log in `logs/`.

A single entry-point runs all 19 audits and writes their logs to `logs/`:

```bash
python3 scripts/daily-audit.py
```

> Runtime note: it looks hung for ~15 min on `ingest-rationale-lint`. Needs Homebrew python3 (3.10+) on PATH or 4 scripts crash on PEP604 hints.

---

## The 19 audits — 3 classic + 1 rationale (errors block) + 15 signals

| Audit | Type | Purpose |
|---|---|---|
| `lint.py` | error | wiki frontmatter required fields |
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
| `supersession-audit.py` | signal | `superseded_by` 깨진 링크 + 필드↔본문 배너 sync + decay 후보(sr+ma/sr/rct 중 5년↑ 미대체, 카테고리·중심성 집계) — living-document 갱신을 신호화 |
| `relations-audit.py` | signal | `relations:` typed edge target 실존·vocab 검증 + 타입 분포 + typed-edge JSON export(Quartz/custom 렌더용) |
| `link-integrity.py` | signal | 본문 `[[wikilink]]` 깨짐 + index.md 양방향 커버리지 (Astro-Han lint 개념 차용) |
| `interactive-staleness.py` | signal | 임상 interactive 도구의 `source_wiki` 근거가 도구보다 git상 최신이면 STALE(LLM 재작성 후보), 근거 경로 소실이면 BROKEN. meta/통계 도구는 제외(build-wiki-stats.py가 배포 때 재생성). 임상 수치 자동 재작성은 Rule #1 위배라 신호만 |
| `find-contradiction-candidates.py` | signal | 본문에 명시적 충돌 표현(contradict/counterpoint/반박 등)이 있으나 그 쌍에 `relations:` 타입 엣지가 **(어떤 타입이든)** 없는 논쟁 레이더 백필 후보. Tier1(키워드에 가장 가까운 wikilink로 대상 지목)·Tier2(대상 불명/너무 멂/동일 줄 비최근접/soft). 기계가 충돌을 확정하지 않고 신호만 — LLM이 두 페이지 읽고 판단해 엣지를 단다. **type_hint를 그대로 엣지로 옮기지 말 것** — 2026-07-17 전수 검토에서 contradicts 계열 지목 122건 중 실제 contradicts는 1건이었다 |
| `content-lint.py` | signal | frontmatter lint가 못 보는 **본문 내용 규칙**을 결정론으로 검사: (A) 이중언어 세줄요약 쌍 + overview 한국어 핵심요약 콜아웃, (B) heading 태그 일관성, (C) wiki↔source cross-tier 정합(`source:` 실존·pmid 일치) |
| `retraction-audit.py` | signal | `retraction_status: RETRACTED` 페이지가 **인용 사고를 실제로 막는 구조**인지 검사. 핵심은 **경고가 섹션 제목 안에 있는가** — QMD는 청크로 검색하므로 페이지 상단 콜아웃은 `## Results` 청크에 따라오지 않는다(사람이 페이지를 열 때만 작동하는 경고는 답변 생성 경로를 못 막는다). 그 외: 필수 3섹션(Why This Page Exists / What We Can NOT Use / What It Does Tell Us), typed 엣지 **양방향 0**(철회 논문이 overview 합성에 살아있는 관계로 조립되면 안 됨). 역방향으로 필드 누락 의심도 검출. `grep retracted`는 교정과 'canine retraction'(견인)에 걸려 못 쓰므로 기계 판독 고리는 `retraction_status:` 필드뿐 |
| `deviation-audit.py` | signal | `logs/ingest-deviations.md` 집계 — 동일 유형 3회 이상이면 SOP 개정 후보 출력 (Rule-of-Three trigger) |

**Signals never block.** They're a mirror — the principle is that ingest pressure self-corrects via visibility, not via gates (which trigger burnout/avoidance in clinical workflows). This is a load-bearing design choice, not laziness; see *Design Principles* in `CLAUDE.md`.

## The three compounding metrics

Run daily (manual or cron). Watch these over time:

- **synthesis-backlog %**: should trend up (more sources getting linked from overviews).
- **category-overflow count**: should trend down as overviews get written.
- **thesis-staleness warn/info**: should stay low — overview 본문이 정기적으로 refresh되는지 보는 signal.

## Closing the loop — audit signals → morning briefing

Audits only compound if someone reads them; leaving that to memory is the weak link. The intended terminal is a one-line badge in the morning-briefing pipeline (STALE overview N건, category-overflow N건, BROKEN link N건) so the day's top signals surface without opening `logs/`. Design: `agenda/2026-07-15_audit-to-briefing-bridge.md`.

Design rationale (audit set): see `agenda/2026-05-26_synthesis-enforcement-setup.md`.
