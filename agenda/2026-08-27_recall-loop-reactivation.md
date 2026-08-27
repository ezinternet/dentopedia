---
title: "리콜 루프 재가동 — 스케줄러는 도는데 채점이 안 남는다"
type: agenda
date: 2026-08-27
status: in-progress
owner: 원장
priority: P1
tags: [meta, recall, srs, retention, knowledge-compounding, operations]
source_wiki:
  - wiki/overviews/dbbm-bone-substitute-overview.md
  - wiki/overviews/implant-loading-protocol-prosthesis-type-overview.md
  - wiki/overviews/unopposed-tooth-overeruption-overview.md
  - wiki/overviews/implant-failure-mbl-risk-factors-overview.md
  - wiki/overviews/professional-biofilm-management-gbt-air-polishing-overview.md
---

# Goal

세 축(입력→종합 / 종합→산출물 / 종합→기억) 중 **기억 축만 죽어 있다.** 문항을 더 만드는 게 아니라, **이미 있는 144문항이 채점까지 도달하도록 전달 경로를 고친다.** `[[2026-08-25_wiki-midterm-review]]`가 2순위로 남긴 retention 항목의 실행 단계.

# 진단 — 왜 안 도는가 (2026-08-27 실측)

병목은 콘텐츠도 도구도 아니다. **스케줄러는 정상 작동 중이며, 채점만 상태에 안 남는다.**

| 확인 대상 | 실측 |
|---|---|
| `weekly-recall` 스케줄 | **존재·enabled·정상 발화** — `lastRunAt` 2026-08-24, `nextRunAt` 2026-08-30 |
| `scripts/recall-session.py` | 정상 — `--stats` = 문항 144 · 오늘 due **144** |
| `recall/_state.json` 마지막 채점 | **2026-08-08** (19일 전), 그마저 7문항뿐 |
| 한 번도 열리지 않은 문항 | **137 / 144** |
| 박스 분포 | box1: 138 · box2: 4 · box4: 2 — 사실상 전량 미착수 |
| 리콜 스펙 마지막 저작 | **2026-07-23** (35일 전, 47편 일괄) |
| recall-coverage | 48/279 (17.2%) — 2일 전 48/277에서 **변동 0** |

**근본 원인은 스케줄 태스크 명세 자체에 박혀 있다.** `~/.claude/scheduled-tasks/weekly-recall/SKILL.md` 마지막 제약:

> 세션이 백그라운드로 완전 자동 실행되어 사용자 응답을 받을 수 없는 경우(사용자가 비활성 상태) 문항만 제시하고 채점은 건너뛴 채 "다음 접속 시 이어서 답해주세요"로 마무리한다

억지 자동채점을 막는 건 옳은 설계다. 문제는 **그 "다음 접속"을 이어받는 장치가 없다는 것** — 일요일 20시에 사용자가 자리에 없으면 문항은 채팅 로그로 증발하고, 상태 파일은 그대로다. 8/24에도 발화했지만 상태는 8/08에 멈춰 있는 게 그 증거다. 주 1회 발화 × 부재 = 영구 미착수.

두 번째 원인은 **투여량**. `--due 7`인데 현재 due가 144다. 자리에 앉아도 첫 화면이 7문항이면 진료 사이에 낼 시간이 아니다.

# Input

- `logs/2026-08-27_recall-coverage.log` — 48/279, 미커버 231편 허브순 우선순위
- `recall/_state.json` · `scripts/recall-session.py --stats` — 박스 분포·due 실측
- `~/.claude/scheduled-tasks/weekly-recall/SKILL.md` — 발화 명세 + 무인 fallback 조항 (근본 원인)
- `[[agenda/2026-07-08_recall-loop-srs]]` — 루프 최초 설계 (Leitner 간격 1→3→7→16→35, forward-only 원칙)
- `[[agenda/2026-08-25_wiki-midterm-review]]` — 3축 비대칭 진단, 우선순위 "활용률 > 도메인 균형 > 노후화"
- `scripts/recall-coverage-lint.py` — 백로그 신호 (daily-audit 편입분)

# Output

- `scripts/recall-session.py` — pending 큐 플래그(`--write-pending`/`--read-pending`/`--clear-pending`) + `--grade`의 자동 pending 정리
- `~/.claude/scheduled-tasks/weekly-recall/SKILL.md` — read-pending-먼저 흐름으로 재작성
- `.gitignore` — `recall/_pending.json` 추가

## D1. 전달 경로 결정 (이 agenda의 핵심 — 나머지는 여기 종속)

무인 발화가 증발하지 않도록 **큐를 남기는 방식**으로 바꾼다. 후보 3안:

| 안 | 방식 | 장점 | 단점 |
|---|---|---|---|
| **A (권장)** | 스케줄 태스크가 due 문항을 `recall/_pending.json`으로 **파일에 적어두고**, 다음 대화형 세션 시작 시 그 파일을 집어 이어서 채점 | 부재해도 유실 0 · 저장소 안에서 완결 · 습관 불필요 | `_pending.json` 스키마 + 픽업 지점 신설 필요 |
| B | 발화 시각을 실제로 자리에 있는 시간대로 이동 (일 20:00 → 평일 아침 진료 전) | 변경 1줄 | 그날 부재하면 같은 문제 재발 |
| C | 아침 브리핑(`dentweb` Track A)에 리콜 3문항을 얹어 기존 습관에 기생 | 이미 도는 루틴 · 별도 습관 0 | 브리핑 스킬과 결합 → 둘 중 하나 깨지면 같이 깸 |

**권장: A + B 병행.** A가 유실을 막고, B가 애초에 부재할 확률을 낮춘다. C는 A가 안정된 뒤 얹는다.

- [x] A/B/C 중 채택안 확정 (원장 결정, **2026-08-27: A안 채택**. B·C는 기각이 아니라 **보류** — A가 안정된 뒤 재검토)
- [x] `~/.claude/scheduled-tasks/weekly-recall/SKILL.md` 무인 fallback 조항을 채택안에 맞게 개정

### D1 구현 (2026-08-27, A안)

`scripts/recall-session.py`에 pending 큐 3개 플래그 추가:

- `--due N --write-pending` — due 문항을 뽑아 제시하면서 동시에 `recall/_pending.json`에 고정 (`{created, items}`)
- `--read-pending` — pending 파일이 있으면 그 배치를 그대로 반환(**새 `--due`를 절대 뽑지 않음**), 없으면 빈 결과
- `--grade` — 채점된 key를 pending에서 자동 제거(부분 채점 시 나머지는 유지); 배치가 다 채점되면 파일째 삭제
- `--clear-pending` — 수동 폐기(사용자가 명시적으로 스킵을 요청한 경우만)

`weekly-recall` SKILL.md 흐름을 `read-pending 먼저 → 없으면 due+write-pending`으로 재작성. 무인 fallback 조항에서 "다음 접속 시 이어서"라고만 하던 것을, 실제로 **다음 발화가 정확히 그 배치를 다시 제시하도록** 만들었다 — 습관이나 사람의 기억에 의존하지 않는다.

`.gitignore`에 `recall/_pending.json` 추가 — 전이성 큐 파일이라 `_state.json`(추적 대상)과 달리 커밋 대상 아님.

**검증 (CLI 시뮬레이션, `recall/_state.json` 스냅샷 백업 후 원복)**:
1. `--due 3 --write-pending` → 3문항 제시 + pending 파일 생성 확인
2. (무인 가정, grade 미호출) `--read-pending` → **동일 3문항 재현**(diff 0) — 유실 없음 확인
3. 1문항만 `--grade` → pending에 나머지 2문항만 남는 것 확인(부분 채점 정상)
4. 나머지 2문항 채점 → pending 파일 자동 삭제 확인
5. 그 다음 `--due 3 --write-pending` → **다른(새) 3문항**이 나오는 것 확인 — 배치 재사용이 아니라 정상 진행임을 확인

전부 통과. 다만 이건 CLI 직접 호출 시뮬레이션이고, **실제 스케줄 발화(다음: 2026-08-30 일 20시)를 통과시켜 검증한 것은 아직 아니다** — Done Criteria 참조.

## D2. 투여량 조정 (2026-08-27 승인·완료)

- [x] `--due 7` → **`--due 3`** (진료 사이 1분 분량). 간격반복은 세션 크기가 아니라 **빈도**가 효과를 낸다.
      `~/.claude/scheduled-tasks/weekly-recall/SKILL.md`는 D1 구현 시점에 이미 `--due 3`로 작성돼 있었다(별도 변경 불필요, 확인만). `scripts/recall-session.py`의 CLI 기본값(`--due` 옵션을 인자 없이 호출할 때 쓰는 `const`)과 usage 예시·help 텍스트를 오늘 7→3으로 맞춰 실제 운영값과 문서를 일치시켰다.
- [x] due 144 적체 해소 방침 결정: **한 번에 밀지 않는다.** 회당 3문항으로 자연 소진 — box1 138편은 Leitner 간격상 3일 뒤 다시 due로 돌아오므로 별도 배치 작업(대량 채점 세션 등)을 만들지 않고 매주 회당 3문항이 자연히 갉아먹게 둔다. 상태 변경 없음(정책 결정이지 스크립트 변경 아님).

## D3. 스펙 백필 — 허브 우선 (D1·D2 안정화 **후**)

미커버 231편 전량이 아니라 **허브 상위만.** inbound 기준 top 5 (오늘 로그):

| inbound | overview |
|---|---|
| 15 | `dbbm-bone-substitute-overview` |
| 15 | `implant-loading-protocol-prosthesis-type-overview` |
| 15 | `unopposed-tooth-overeruption-overview` |
| 14 | `implant-failure-mbl-risk-factors-overview` |
| 14 | `professional-biofilm-management-gbt-air-polishing-overview` |

- [x] 위 5편 × 3문항 = 15문항 저작 완료 (2026-08-27; 뱅크 144→159문항; 5개 JSON 퍼파일 커밋·푸시)
- [x] 2026-07-08 agenda의 **forward-only 원칙 재확인** — 231편 소급 백필은 하지 않는다. 신규 overview 저작 시 3문항 동반이 정상 경로이며, 이번 5편은 "허브인데 비어 있음"에 한한 예외

## D4. 신호 보정

- [x] `recall-coverage-lint.py`에 `_state.json` 기반 인출 활성도 신호 추가 완료 (2026-08-27)
      추가 지표: `last_graded`/`days_since`(14일 초과→WARN·stdout·log 모두), `graded_30d`, `never_graded`(한 번도 안 풂), `box≥2 비율`.
      현재값: 루프 19일 정지 WARN · never_graded 152/159 · box≥2 6/159

# Done Criteria

- [x] D1 채택안 확정 + SKILL.md 개정 반영 (2026-08-27, A안. CLI 시뮬레이션 4단계 통과 — 위 D1 구현 참조)
- [ ] 무인 발화 1회를 **실제 스케줄 발화로** 통과시켜, 사용자 부재 상태에서도 **문항이 유실되지 않고 다음 세션에서 채점까지 도달**하는 것을 `_state.json`·`recall/_pending.json` 전후 비교로 확인 (다음 발화: 2026-08-30 일 20시 — CLI 시뮬레이션과 별개로 실측 필요)
- [ ] 연속 2주 세션에서 `_state.json`의 `last`가 갱신됨 (= 루프가 실제로 돈다는 유일한 증거)
- [ ] box2 이상 문항 수가 6 → **30 이상** (인출이 축적되기 시작한 지표)
- [x] D3 허브 5편 × 3문항 저작 완료, 모든 수치는 해당 overview 본문 대조 (2026-08-27)

# Notes / Decisions

- 2026-08-27: **"스펙을 231편으로 늘린다"를 이번 국면 목표에서 제외.** 스펙 48편·문항 144개가 이미 미착수인 상태에서 문항을 더 만드는 건 백로그를 키울 뿐이다. 병목은 저작이 아니라 **채점 도달률**.
- 2026-08-27: 리콜은 *signal, not gate* 원칙 아래 있다 — 미착수 문항 수를 gate로 쓰지 않는다. 다만 D4는 **신호가 실패를 볼 수 있게** 만드는 일이라 원칙과 충돌하지 않는다.
- 2026-08-27: 산출물 축(종합→산출물 14.8% → 18.3%)은 8/26 인터랙티브 11종으로 스스로 돌고 있으므로 이번 agenda 범위 밖.
- 2026-08-27: **D1 A안 채택 + 구현 완료.** B(발화 시각 이동)·C(아침 브리핑 결합)는 기각이 아니라 보류 — 다음 실제 무인 발화(8/30)에서 A만으로 유실이 안 잡히면 그때 B를 얹는다.
- 2026-08-27: **D2 승인 + 완료.** `--due 7`→`3` 확정. SKILL.md는 D1 구현 시점에 이미 3으로 작성돼 있었음(확인만 필요했음) — `recall-session.py`의 CLI 기본값·문서만 오늘 맞췄다. due 144 적체는 별도 소진 작업 없이 회당 3문항 자연 소진 방침으로 결정(상태 변경 없는 정책 결정).

# References

- `[[agenda/2026-07-08_recall-loop-srs]]` — 루프 원설계 (Leitner 간격·forward-only)
- `[[agenda/2026-08-25_wiki-midterm-review]]` — 3축 비대칭 진단
- `AUDITS.md` — recall-coverage 감사 정의
- `OPERATIONS.md` §4 agenda workflow
