---
title: "relations 타입 정합성 정비 + RFA/ISQ 기전 오버뷰 신설"
type: agenda
date: 2026-07-18
status: done
owner: 원장
priority: P1
tags: [relations, audit, circular-reinforces, isq, rfa, mechanism, overview]
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

# Done Criteria

- [x] RFA 기전 오버뷰 신설 — spine 4편, Rule #4 경계(종합 추론 vs 인용 가능 사실) 페이지 내 명시
- [x] circular reinforces **152 → 0**
- [x] 감사 탐지기 오탐 교정 (시간순 필터, git 1회 호출로 성능 회귀 없음)
- [x] postdated 36건 판정 완료 (KEEP 18 · RETYPE 18)
- [x] `ingest-rationale-lint` blocking 실패 **2 → 0**
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

# 미해결 / 다음 후보

- **POSTDATED 잔여 18건** — 검증된 정당 `reinforces`라 조치 불필요. 다만 이후 인제스트로 버킷이 다시 늘 수 있다.
- **`relations:` 타입 정확도 일반 문제** — 이번엔 circular/postdated 152건만 봤다. INGEST.md에 "무작위 30건 표본에서 47%만 올바른 타입"이라는 실측이 있어, 나머지 ~2200 엣지에도 같은 종류의 오라벨이 남아 있을 것이다. 감사가 잡아주지 않는 영역이라 별도 설계 필요.
- **launchd `embed-until-done`은 다음번에 자동으로 안 돈다** — plist가 `KeepAlive={SuccessfulExit:false}`라 done 마커에서 잠든다. 대량 편집 뒤엔 매번 `launchctl kickstart` 필요(이번에도 그렇게 드레인했다).

# References

- 커밋: `6a0caef` `72a6841` `917c683` `49d8189` `aceb8db` `828afa9` `77adcb4`
- [[overviews/rfa-isq-measurement-mechanism]] — 이 작업의 주 산출물
- [[overviews/implants-isq-stability-ladder]] — 기전 축이 비어 있던 대상 오버뷰
- [[agenda/2026-07-15_audit-to-briefing-bridge]] — 감사 신호를 사람에게 표면화하는 인접 작업
