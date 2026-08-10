---
title: "relations 타입 정합성 정비 + 논쟁 레이더 전량 판정 + RFA/ISQ 기전 오버뷰 신설"
type: agenda
date: 2026-07-18
status: done
owner: 원장
priority: P1
tags: [relations, audit, circular-reinforces, contradiction-radar, isq, rfa, mechanism, overview]
source_wiki:
  - wiki/overviews/rfa-isq-measurement-mechanism.md
  - wiki/overviews/implants-isq-stability-ladder.md
output_wiki:
  - wiki/overviews/rfa-isq-measurement-mechanism.md
  - wiki/overviews/caries-biomimetic-remineralization-orthodontic-pediatric-crown-overview.md
agenda: null
---

# Goal

임상질문 하나(오스텔 ISQ에서 강성↑ → 공진주파수↑ → ISQ↑가 맞는가, 그리고 공진주파수가 높다는 게 더 빠르게 떠는 것이지 더 크게 흔들리는 게 아닌가)에서 출발해, ① 위키에 비어 있던 **RFA/ISQ 기전 축**을 오버뷰로 채우고 ② 그 과정에서 드러난 `relations:` 타입 오라벨(circular reinforces 152건)을 **탐지기 교정 + 전량 재라벨링**으로 정리한다.

事後 성격의 agenda다 — 작업이 먼저 진행되고 명세를 뒤에 남긴다(세션 기록 요청).

# Input

- `wiki/implants/isq/meredith-1996-quantitative-stability-implant-tissue-rfa.md` — RFA 원조, 노출 고정체 높이↔공진주파수 r=0.94
- `wiki/implants/isq/sennerby-2008-implant-stability-resonance-frequency-analysis.md` — RFA 발명자(Meredith) 공저 종설, ISQ 결정 3대 인자
- `wiki/implants/isq/bhandarkar-2023-rfa-mathematical-modeling-implant-stability.md` — 2자유도 공학 모델, 강성↑ → 주파수↑ ∧ 미세변위↓
- `wiki/implants/isq/debruyne-2017-isq-laser-vibrometry-resonance-frequency.md` — LDV 독립 포착 r=0.990, 강성 3분해, RF 5.0–8.6 kHz
- `wiki/implants/isq/chatvaratthana-2017-cortical-bone-crestal-buccolingual-isq.md` — 치조정 피질골 r=0.885, 6·9mm·해면골 무상관
- `wiki/implants/isq/nedir-2004-predicting-osseointegration-primary-stability-rfa.md` — RFA 동요 검출 실패, ISQ ≥47 하한
- `scripts/relations-audit.py` — circular reinforces 신호 산출
- `logs/2026-07-18_relations.log` — 작업 큐

# Output

- `wiki/overviews/rfa-isq-measurement-mechanism.md` — **신규** 기전 오버뷰 (커밋 `6a0caef`)
- `scripts/relations-audit.py` — 시간순 필터 추가 (커밋 `917c683`)
- `wiki/overviews/caries-biomimetic-remineralization-orthodontic-pediatric-crown-overview.md` — Zn-CHA 오붙임 수정 (커밋 `72a6841`)
- 65개 wiki 페이지 relations 재라벨링 (커밋 `49d8189`)
- 11개 wiki 페이지 postdated 재라벨링 (커밋 `aceb8db`)
- `sources/alabdulkareem-2026-...md`, `sources/li-2026-...md` — Why Ingested 보강 (커밋 `828afa9`, `77adcb4`)

**후반부 (Tier 1·Tier 2 판정, 위 초안 작성 이후 진행)**

- Tier 1 거짓음성 4건 — 피에조 `contradicts` 외 (커밋 `968a442` `4e50ad0` `a79e1bf` `b0645f5`)
- `wiki/tmj/zhang-2024-tmj-morphology-ipilffdp-cbct.md` — Wang/Zhang 산문 상호링크 (typed 엣지는 의도적 미부여)
- `scripts/find-contradiction-candidates.py` — 억제 누수 버그 + 부정문 필터 + 회귀 테스트 (커밋 위 + `5946da4`)
- `scripts/log-relation-negative.py` — **신규** 부정-판정 대장 로거 (커밋 `ec08061`)
- `logs/relation-negatives.md` — **신규** 대장, 409건 초기 적재 (커밋 `2d13e88`)
- 23개 wiki 페이지 — Tier 2 전량 판정 결과 엣지 24건 (커밋 `bfd4b56`)

# Done Criteria

- [x] RFA 기전 오버뷰 신설 — spine 4편, Rule #4 경계(종합 추론 vs 인용 가능 사실) 페이지 내 명시
- [x] circular reinforces **152 → 0**
- [x] 감사 탐지기 오탐 교정 (시간순 필터, git 1회 호출로 성능 회귀 없음)
- [x] postdated 36건 판정 완료 (KEEP 18 · RETYPE 18)
- [x] `ingest-rationale-lint` blocking 실패 **2 → 0**
- [x] Tier 1 논쟁후보 12건 판정 (ADD 4 · NONE 8) — 진짜 `contradicts` 1건 발굴
- [x] 논쟁 레이더 억제 누수 버그 수정 + 부정문 필터 (Tier 2 629 → 412)
- [x] 부정-판정 대장 장치 구축 (판정 노동이 매일 증발하던 구조 해소)
- [x] **Tier 2 412건 전량 판정** (ADD 24 · NONE 388) → Tier 2 **412 → 1**
- [x] YAML 손상 사고 발견·되돌림·재작업·재검증 (아래 Notes 참조)
- [x] **Tier 1 잔여 8건 처리** (신규 판정 3 · 기판정 5 대장 기록) → Tier 1 **0** · Tier 2 **0**
- [x] daily-audit 19종 blocking 전부 통과
- [x] 변경 전 페이지 YAML 재파싱 무결, link-integrity 0 broken
- [x] qmd 재색인 완료 마커(`All content hashes already have embeddings`) 도달
- [x] 전 커밋 push 완료

# Notes / Decisions

## 2026-07-18: 기전 오버뷰 — Rule #4 경계를 페이지 안에 박았다

`f = (1/2π)√(k/m)`와 빔/지렛대 언어는 **일반 진동·빔 역학이지 보유 논문의 주장이 아니다**. "What the Mechanism Explains" 표의 우측 열(기전→관찰 연결)은 좌측 각 논문이 독립 보고한 사실 위에 얹은 **종합 추론**이며, 연결 자체를 검증한 연구는 보유하지 않았다. 인용은 좌측 논문으로 하라고 페이지에 적었다. 이 구분이 없으면 그럴듯한 물리 설명이 논문 근거인 척 빠져나간다.

## 2026-07-18: 감사 탐지기가 먼저 틀렸다 — 페이지가 아니라 탐지기를 고쳤다

14건 표본을 블라인드 판정했더니 정당(KEEP) 2건이 **둘 다 같은 서명**이었다: 논문이 오버뷰보다 **나중에** 리포에 진입. 원인은 탐지 조건이 `target in 본문_wikilinks(source)` 하나뿐이라 **구성 재료**와 **나중에 덧붙인 관련 논문**을 구분하지 못한 것.

- `date:` 필드로는 판정 불가 — 논문은 *출판일*, 오버뷰는 *작성일*이라 축이 다르다. **파일이 리포에 추가된 날**을 써야 한다.
- per-file git 호출 금지 — `f10ecfc`가 캐시로 제거한 그 느림의 원인이다. 전 wiki **1회** traversal(~4s)로 뽑았다.
- 걸러낸 36건은 버리지 않고 **POSTDATED 버킷으로 별도 보고**(무성 절삭 금지).
- 남는 한계도 docstring에 명시: 오버뷰보다 먼저 인제스트됐지만 재료로 안 쓰이고 나중에 Related Papers로만 링크된 논문은 여전히 오탐(시간순으로 구분 불가). `source_papers:`는 오버뷰 239장 중 80장에만 있어 기준이 못 된다.

## 2026-07-18: 재라벨링 91건 중 65건이 `refines`였다 — 이게 이번 작업의 실질 발견

오버뷰들이 앵무새처럼 되풀이하고 있던 게 아니라, **교차 독해로 원 논문의 결론을 실제로 한정**하고 있었는데 라벨만 `reinforces`였다.

- `huang-2016`의 "길이·골질 모두 무의"라는 무조건적 null을 Barikani와 맞붙여 **"연질골에서만 유의"** 조건부로 전환 (Huang은 골밀도 층화 미실시)
- Mello↔García-Sánchez 생존율 충돌을 **"포함기준 artifact"** 로 판정해 양쪽 헤드라인을 동시에 한정
- `abdar-esfahani`는 애초에 그 클러스터의 **반증 null** — `reinforces`가 방향부터 틀렸던 경우

DROP 25건은 반대로 아무 주장도 안 하던 엣지(Lim 2011 축 = 원 논문 Results 재서술). 멤버십은 본문 wikilink가 이미 보유.

## 2026-07-18: postdated KEEP 50%가 필터의 사후 검증이다

순환 버킷 116건은 KEEP **0건**, postdated 36건은 KEEP **18건(50%)**. 두 버킷이 실제로 다른 모집단이라는 뜻이고, 필터가 그은 경계가 옳았다는 증거다. 필터 없이 152건을 한 덩어리로 밀었다면 **멀쩡한 라벨 18개를 지웠을 것**이다.

재라벨링 쪽 지배 패턴은 **retrofit** — 논문이 도착해서 오버뷰의 그 입장을 *만든* 경우엔 확인할 선행 테제가 없으므로 `extends`. 판정단이 git으로 오버뷰 최초 커밋 상태를 복원해 판별했다(`czumbel-2019`는 오버뷰의 "부족한 논문" 목록에조차 없었고, `wang-2023`은 오버뷰 최초 버전에 "흡연" 0회, `podaropoulos-2016`은 오버뷰에 논문 도착일이 박힌 축 제목이 있었다).

## 2026-07-18: 커밋 단위 — 65파일 1커밋은 규칙의 의도적 예외

CLAUDE.md는 파일당 1커밋이고 최근 100커밋 최대가 4파일이다. 65파일 기계적 재라벨링은 감사 1건에서 나온 **단일 논리 단위**라 통째 revert가 맞고, 65개 커밋은 히스토리를 덮어 "깔끔한 히스토리"라는 규칙의 취지 자체를 해친다 — 사용자 확인 후 1커밋. 반면 sources 2건 Why Ingested는 서로 독립적 판단이라 파일당 1커밋 그대로 적용.

## 2026-07-18: 부수 발견 (별건)

- `caries-biomimetic-...-overview.md:105` — 지르코니아 경도 수치에 **Zn-CHA가 오붙임**. 같은 페이지 28행 한국어 요약은 올바르게 적혀 있어 두 줄이 같은 수치를 다르게 말하고 있었다. 재광화 소재 물성을 정반대로 전달하는 오류라 즉시 수정.
- `huang-2016`이 `superseded_by: huang-2017`(partial)인데 macrogeometry 오버뷰가 언급 없이 인용 중. 방향은 유리(직경은 2017에서도 생존)라 결론 불변 — 미조치.
- `fu-2023 ↔ implants-isq-stability-ladder`는 양방향 엣지가 다르게 판정됐다(overview→paper `extends`, paper→overview `KEEP`). 모순이 아니라 Fu가 발견을 둘 갖고 있어서 — MBL 축은 오버뷰에 없던 것이고 골밀도 구배는 기존 테제를 확인한다.
- `debrier-2020`은 `endodontics/`가 아니라 `dental-trauma/`에 있었다 — qmd로 후보를 찾은 뒤 파일 존재를 확인하는 절차(INGEST.md 규약)에서 걸렀다.

## 2026-07-18: 병행 세션 주의

다른 Claude 세션이 같은 트리에서 동시 작업 중이었다. 세션 초반 `index.md`에 넣은 내 줄이 **그 세션의 커밋 `cb75e10`에 끌려 들어갔다**(내용은 온전). 히스토리 재작성은 하지 않았다 — 공유 main을 되감는 쪽이 훨씬 위험하다. 오늘 sources 2건의 `## Why Ingested` 누락도 그 세션 산출물이었고, 그 세션의 작업이 커밋된 뒤 내가 보강했다.

## 2026-07-18: relations 타입 중 **답변을 바꾸는 건 2종뿐**이다 — 일반 훑기를 기각한 근거

"타입 정확도 일반 문제도 훑어달라"는 요청을 받고 먼저 **무엇이 relations를 실제로 읽는지** 조사했다. 결과가 요청의 전제를 바꿨다:

- `logs/{date}_relations-graph.json`은 **아무도 소비하지 않는다** — 자기를 쓰는 스크립트와 INGEST.md 문서뿐. "Quartz/커스텀 렌더링용 typed 그래프"는 아직 소비자가 없다.
- 답변 경로에서 타입으로 분기하는 곳은 `.claude/skills/clinical-consult/SKILL.md` **한 곳**이고, 쓰는 타입은 **`contradicts`/`refines` 둘뿐**이다("인용 페이지의 relations에 contradicts/refines가 있으면 반드시 회색지대로 노출… 반대 근거가 있으면 ⚪ 또는 강등").

그래서 2,361개 엣지가 갈린다 — **349개(contradicts+refines)만 답변에 영향**, 나머지 2,012개는 읽는 코드가 없다. `extends`인지 `applies-to`인지 구분하는 작업은 답변을 한 글자도 바꾸지 않는다.

**정확도에 걸린 건 방향이 다른 두 오류다**: 거짓 음성(진짜 충돌인데 라벨이 없음 → 답변이 확신을 과대표시, 임상적으로 위험) vs 거짓 양성(충돌이 아닌데 라벨이 있음 → 멀쩡한 권고를 강등, 위키가 늑대야 소리를 함). 그래서 일반 2,012건 훑기를 기각하고 **거짓 음성 사냥**(논쟁 레이더 Tier 1/2)으로 방향을 틀었다.

## 2026-07-18: 회색지대는 **드물어야** 값을 가진다 (사용자 판단 → 측정으로 확인)

사용자가 "회색지대에 대해 긍정적으로 본다, 진료는 흑백논리가 아니다"라고 방향을 정했다. 이건 위키 설계와 일치한다(`evidence_level` 4등급, Rule #4가 모두 같은 이유로 있다).

다만 **회색지대를 귀하게 볼수록 그 정확도 기준은 낮아지는 게 아니라 높아진다** — 모든 페이지에 뜨면 "진짜 논쟁 중"과 "정리된 사안"을 구분하는 힘을 잃는다. 그래서 재봤다: 전체 2,945장 중 **282장(9.6%)**, 오버뷰 243장 중 **61장(25.1%)**. 10페이지에 1장꼴이면 신호로 읽힌다 — **더 늘릴 여유가 있다**는 뜻이고, 이것이 전량 판정을 택한 근거다.

## 2026-07-18: 장치를 먼저 만들고 판정했다 — 순서를 바꾸면 헛일이 된다

Tier 2 412건을 판정하면 ~388건이 NONE으로 나오는데, **NONE을 기록할 방법이 없었다.** 감사의 억제 조건이 "typed 엣지가 있으면 제외"뿐이라 엣지가 안 생기는 NONE은 **다음날 그대로 재방출**된다. `find-contradiction-candidates.py` 주석이 경고한 "끌 수 없는 신호는 노이즈가 된다"의 나머지 절반이 이것이다.

그래서 판정 **전에** `scripts/log-relation-negative.py` + `logs/relation-negatives.md`를 만들었다. `logs/ingest-deviations.md` 패턴을 그대로 따랐다(logs/에 날짜 없는 지속 대장, 작은 로거가 append, 감사가 읽어 억제).

**키는 `(source, target, 문장해시)`다.** `(source, target)`만으로 잡으면 페이지가 개정돼 진짜 충돌이 새로 생겨도 영원히 억제된다. 검증: 공백만 바꾸면 같은 해시(재검토 안 함), 수치 `5min→10min`을 바꾸면 다른 해시(재검토 대상). **부정 판정은 "지금 이 문장일 때"라는 조건부 판단이지 영구 면제가 아니다.**

효과: Tier 2 **412 → 1**(대장 억제 397).

## 2026-07-18: 부정 필터를 한 번 잘못 만들어 진짜 충돌을 죽였다 — 회귀 테스트가 잡았다

논쟁 레이더 수정에서 부정문 필터를 넣었는데, 초안이 앞 60자 창에서 맨 `not`/`no`를 찾는 방식이었다. 회귀 테스트에서 이 문장을 억제했다:

> "Song found **no** pain difference …, **whereas** this RCT detects a penalty"

여기서 `no`는 *연구 결과*("no pain difference")의 일부이지 `whereas`의 부정이 아니다. 연구 산문에서 "no significant difference"는 극도로 흔해 맨 `no`를 넣으면 **진짜 신호를 대량으로 잃는다 — 거짓 음성은 임상적으로 위험한 방향이다.**

→ 맨 `no` 제거, 창 60→30자, 뒤쪽 창은 한국어 전용(한국어는 부정이 키워드 뒤에 온다). 그 사고 때문에 **12건 회귀 테스트를 스크립트에 박았다**(`--selftest`, 진짜 5·거짓 7). 과하게 자른 초안은 364까지 줄었으나 되돌려 **412가 안전한 값**이다 — 덜 줄이는 쪽이 옳다.

## 2026-07-18: ★ YAML 손상 사고 — **감사가 통과했다고 안전한 게 아니다**

Tier 2 판정 결과 24건을 정규식으로 `relations:` 블록에 끼워넣었는데, 삽입 위치가 어긋나 **9개 파일이 깨졌다**: `- type: contradicts`가 target을 잃고, 다른 항목에 `target:`이 2개 붙었다.

**그런데 `lint.py`도 `relations-audit.py`도 그대로 통과했다.** YAML 문법상 유효하고(중복 키는 뒤가 이김), 감사의 `parse_relations`가 `type`/`target` 둘 다 없는 항목을 조용히 건너뛰기 때문이다. 그 결과 **그날 아침 추가한 피에조 `contradicts` 엣지가 소리 없이 `refines`로 바뀌어 있었다.**

대응: `git checkout`으로 22개 전부 되돌리고 **줄 단위 삽입**으로 재작업(들여쓰기 줄을 끝까지 스캔해 블록 *끝*에 삽입). 재검증은 도구 통과가 아니라 **의도한 결과가 실제로 있는지**로 했다 — YAML 파서 + `target:` 개수 계수로 22파일 0문제, 의도한 24엣지 중 23 확인(나머지 1건은 retype이라 별도 처리).

교훈: **구조를 바꿨으면 린터의 OK가 아니라 결과물을 세어서 확인해야 한다.** 첫 점검기 자체에도 버그가 있었다(`^\s*type:`이 `- type:`을 매칭 못 해 전부 `type×0`으로 오보) — 검증기도 검증 대상이다.

## 2026-07-18: `pgrep -f`가 자기 자신을 매칭해 6시간을 헛돌았다

qmd embed 완료를 기다리려고 `until ! pgrep -f "qmd.js embed"; do sleep 10; done`을 백그라운드로 띄웠다. **이 스크립트 자신의 명령줄에 `qmd.js embed` 문자열이 들어 있어 pgrep이 자기를 찾아냈고**, 루프가 영원히 안 끝났다. 뒤에 오게 돼 있던 `qmd embed`는 실행조차 안 됐다.

더 나쁜 건 **그 가짜 프로세스를 "embed RUNNING"으로 읽어 사용자에게 여러 번 잘못 보고**한 것이다("2–4분 남았습니다"의 근거가 가짜였다). 같은 방식의 대기 4개가 전부 갇혀 있었다.

→ 앞으로 `pgrep -f "[q]md.js embed"`로 자기매칭을 깨거나 `ps aux | grep -v grep`으로 확인한다. **프로세스 존재 확인은 그 자체가 오탐원이다.**

## 2026-07-18: Wang/Zhang — typed 엣지를 **달지 않기로** 한 판단

Tier 2 표본에서 "위키가 보유한 정면 대립 쌍인데 typed 그래프에 없다"고 올라왔으나, 두 페이지를 읽으니 대립이 아니었다. **측정이 겹치지 않는다** — Wang은 랫 과두 *연골*을 조직학으로, Zhang은 사람 TMJ *골 형태*를 CBCT로 본다. **CBCT는 연골을 아예 영상화하지 못하므로** Zhang의 무변화가 Wang의 연골 손상을 반증할 수 없다.

INGEST.md가 이 형태를 이미 규정해뒀다 — "같은 결정의 직교 축(non-overlapping measurement, neither extends the other)은 산문 `## Related Papers`에 두라". 6번째 타입(`complements`)은 2026-07-17에 평가 후 기각됐고 재제안 금지다. 억지로 `contradicts`를 달면 clinical-consult가 **없는 논쟁으로 회색지대를 띄운다.**

→ Wang→Zhang 산문 링크는 이미 있었고 Zhang→Wang만 없어서 그 방향만 채우되, **왜 대립이 아닌지**를 함께 적었다(다음 사람이 같은 판단을 반복하지 않도록).

## 2026-07-18: Tier 2 판정에서 나온 임상적 수확

`contradicts` 98→112. 특히:

- **무봉합 발치** — kumar-2022·sen-2024·pachipulusu-2018 → takadoum-2022. 단일기관 3편이 검정력 있는 다기관 null과 정면 충돌하는데 엣지가 하나도 없었다.
- **접착 3건** — tennert→josic-2023, hong→doshi-2023, alghauli→josic-2022. **전부 SR+MA끼리의 결론 충돌**이었다.
- **craddock-2007 → livas-2016은 retype**: 기존 `reinforces`가 Livas를 오독하고 있었다(대조군이 거의 안 움직였는데 "둘 다 잔존접촉이 정출을 못 막는다"로 요약). 산문 설명도 함께 고쳤다.

**NONE 388건의 분포가 감사 설계에 주는 정보**: 문헌 내부 이질성, 오버뷰가 자기 구성 논문들의 불일치를 서술하는 문장, 통설·마케팅 반박, 그리고 **이미 엣지가 있는데 산문이 재서술**하는 경우. 마지막이 특히 많았다 — 감사가 본문만 보고 frontmatter를 안 보기 때문.

## 2026-07-19: Tier 1 잔여 처리 — 5건은 새 판정이 아니라 **빚 갚기**였다

Tier 1에 남은 6건을 열어보니 **5건이 오늘 오전에 이미 NONE으로 판정한 건**이었다. 그때는 대장이 없어서 기록할 곳이 없었고, 그래서 판정하고도 매일 다시 뜨고 있었다. 대장을 만든 이유가 정확히 이것이고 그 첫 청구서를 갚은 셈이다 — **재판정하지 않고 당시 근거를 그대로 옮겼다.**

이 순서가 뒤집혔으면(대장 없이 판정부터) 오전 12건 판정 중 8건이 통째로 증발했을 것이다. "장치 먼저"라는 결정의 실효가 하루 만에 확인됐다.

새로 판정한 3건은 전부 NONE이고, 각각이 서로 다른 오탐 유형이었다:

- `tmd-management-evidence-ladder → tenorio-2026` — "뒤집힘"이 성인 RA와 소아 JIA라는 **다른 인구집단** 사이였고 tenorio 자신의 소견이며, 이미 `tenorio extends chana-2026`으로 encoded돼 있었다.
- `nonaka-2023 → poudel-2026` — 침의 *분자 진단 매체* vs *타액분비·구강건조 결과*라는 다른 축. 페이지가 스스로 complementary라 적어놨다.
- `lopez-silva-2025 → NOTARGET` — 다른 세션이 방금 인제스트한 신규 논문. "in contrast to"가 주사용 헤파린의 프로토콜 **공백을 채운다**는 서술이지 충돌이 아니고, 기존 경구 항응고제 지속 합의와 정렬한다.

## 2026-07-19: 마지막 1건이 문장해시 키가 옳다는 증거였다

전부 처리한 줄 알았는데 Tier 1에 1건이 남았다 — 같은 쌍(`arp-critique → araujo-2009`)인데 **다른 문장**이었다. 표 행(`| ... | animal (dog, split-mouth) | "Flapless = ridge 보존" myth 반박 ...`)은 기록했고, `## Related Papers`의 짧은 줄(`— flapless myth 반박`)이 남아 있었다.

이건 버그가 아니라 **설계대로**다. 키가 `(source, target, 문장해시)`라 한 페이지가 같은 대상에 대해 여러 문장을 갖고 있으면 각각 따로 판정된다 — 같은 페이지의 다른 주장은 따로 봐야 하기 때문이다. 판정은 동일했다(반박 대상이 통설이고 Araujo가 그걸 반박하는 쪽).

## 2026-07-19: **0은 종착점이 아니라 "따라잡은 상태"다**

Tier 1 0 · Tier 2 0을 달성했지만 이 상태는 유지되지 않는다. 오늘 하루에도 다른 세션의 `lopez-silva` 인제스트로 새 후보가 1건 생겼고(위키 2688 → 2696장), 페이지를 고치면 그 문장의 해시가 바뀌어 재검토 대상이 된다.

**내일 아침 감사가 0이 아니라고 해서 뭔가 잘못된 게 아니다 — 그 사이 위키가 자란 것이다.** 이 구분을 기록해두지 않으면 다음 세션이 0을 기준선으로 오해하고 정상적인 증가를 회귀로 읽는다.

# 미해결 / 다음 후보

- **POSTDATED 잔여 18건** — 검증된 정당 `reinforces`라 조치 불필요. 다만 이후 인제스트로 버킷이 다시 늘 수 있다.
- **`relations:` 타입 정확도 일반 문제 — 의도적으로 기각했다.** INGEST.md에 "무작위 30건 표본에서 47%만 올바른 타입"이라는 실측이 있으나, 위 조사에서 **`extends`/`applies-to`/`reinforces` 2,012건은 답변에 영향이 없음**이 확인됐다(읽는 코드가 없다). 나중에 typed 그래프 렌더링을 실제로 만들 계획이 서면 그때 다시 볼 것 — 그 전까지는 메타데이터 위생 작업일 뿐이다.
- ~~**Tier 1 잔여 6건**~~ — 2026-07-19 해소. Tier 1 · Tier 2 모두 **0**(따라잡은 상태이지 고정값이 아님 — 위 Notes 참조).
- **감사가 여전히 frontmatter를 안 본다** — Tier 2 NONE 388건의 큰 부류가 "이미 엣지가 있는데 산문이 재서술"이었다. 대상이 특정된 후보는 억제되지만, 대상 미지정 후보는 문장만 보므로 계속 올라온다. 대장이 그걸 흡수하고 있으나 근본 해법은 아니다.
- **launchd `embed-until-done`은 다음번에 자동으로 안 돈다** — plist가 `KeepAlive={SuccessfulExit:false}`라 done 마커에서 잠든다. 대량 편집 뒤엔 매번 `launchctl kickstart` 필요.
- **대장이 커지면 억제가 과해질 수 있다** — 현재 417건. 문장해시 키라 페이지 개정 시 자동 해제되지만, 대장 자체의 건강성을 보는 감사는 없다(예: 대장에만 있고 원 문장이 사라진 고아 항목). 규모가 더 커지면 필요.

# References

- 커밋(전반): `6a0caef` `72a6841` `917c683` `49d8189` `aceb8db` `828afa9` `77adcb4`
- 커밋(후반): `968a442` `4e50ad0` `a79e1bf` `b0645f5` `ec08061` `5946da4` `bfd4b56` `2d13e88`
- 커밋(2026-07-19): `1d504ec`(agenda 후반부) · Tier 1 잔여 처리 · 본 갱신
- [[logs/relation-negatives]] — 부정-판정 대장 (이 세션의 핵심 산출물 중 하나)
- [[overviews/rfa-isq-measurement-mechanism]] — 이 작업의 주 산출물
- [[overviews/implants-isq-stability-ladder]] — 기전 축이 비어 있던 대상 오버뷰
- [[agenda/2026-07-15_audit-to-briefing-bridge]] — 감사 신호를 사람에게 표면화하는 인접 작업
