# Decay 후보 112건 — 우선순위 Triage (2026-05-31)

`supersession-audit.py` decay 신호(고근거 sr+ma·sr·rct 중 5년↑·미대체) 112건을 **중심성(inbound wikilink) × 카테고리 velocity × age**로 tier 분류. 기계는 후보만 띄우고, tier는 임상 판단. [claude해석]

원칙: decay = "갱신 대상"이 아니라 "**여전히 current인지 검증 대상**". 고전 anchor(약물 기전 RCT 등)는 5년↑여도 갱신 불필요할 수 있다.

## 카테고리 분포

| 건수 | 카테고리 | median age | maxInbound | velocity 판단 |
|---|---|---|---|---|
| 19 | implants | 6.4y | 12 | 빠름 |
| 18 | bone-regeneration | 8.5y | 17 | 빠름 (ARP 집중) |
| 11 | drug | 10.7y | 9 | 느림 (기전 안정) |
| 9 | immediate-implant | 7.1y | 14 | 빠름 |
| 7 | periodontics | 10.4y | 5 | 중간 |
| 6 | sinus-lift | 6.2y | 14 | 빠름 |
| 6 | resin | 8.3y | 8 | 중간 |
| 5 | endodontics | 8.6y | 5 | 중간 |
| 나머지 | oral-surgery·inlay·prosthetic·tmj·resin-bonding 등 | — | — | 혼재 |

## P0 — 지금 검증 (중심성↑ AND 빠른 분야)

가장 ROI 높은 단일 동작은 **ARP(치조제 보존, Alveolar Ridge Preservation) 근거 갱신 패스**다. bone-regeneration decay 18건 중 7편이 ARP/발치와 치수변화 한 주제에 몰려 있고, 전부 고중심성이다. 2024~2026 ARP SR+MA 한 편을 ingest하면 여러 편을 동시에 supersede + 기존 bone-regeneration overview를 refresh할 수 있다. [claude해석]

ARP 클러스터:
- `bone-regeneration/avila-ortiz-2014-alveolar-ridge-preservation-systematic-review` (ib17, 12.0y) — decay 최다 피인용. 최우선.
- `bone-regeneration/atieh-2015-alveolar-ridge-preservation-cochrane-review` (ib12, 11.1y)
- `bone-regeneration/bassir-2018-alveolar-ridge-preservation-meta-analysis` (ib12, 7.7y)
- `bone-regeneration/tan-2012-post-extractional-alveolar-dimensional-changes` (ib8, 14.4y)
- `bone-regeneration/couso-queiruga-2021-post-extraction-dimensional-changes-systematic` (ib8, 5.6y)
- `bone-regeneration/troiano-2018-bone-graft-membrane-ridge-preservation` (ib7, 8.4y)
- `bone-regeneration/atieh-2021-interventions-replacing-missing-teeth` (ib7, 5.1y)

기타 P0 (개별):
- `sinus-lift/anitua-2021-mucous-cysts-pseudocysts-implants-sr` (ib14, 5.1y) — pseudocyst overview의 근거축. 검증 우선.
- `immediate-implant/ogawa-2022-socket-shield-technique-systematic-review` (ib14, 5.2y) — socket shield는 빠르게 진화. atef-2021 RCT(ib7)와 묶어 검증.
- `digital-workflow/revilla-leon-2021-artificial-intelligence-implant-dentistry-sr` (ib9, 5.1y) — **AI는 최고속 분야, 5년이면 사실상 구식.** 단독 P0.
- `implants/inchingolo-2021-osseodensification-implant-site-osteotomy-sr-ma` (ib12, 5.3y) — OD 분야 활발. (padhye를 supersede한 당사자 — 자신도 곧 검증 대상.)

## P1 — 일정 잡아 검증 (중심성 중간 or 비교적 안정)

- `implants/derks-2015-peri-implant-health-disease-epidemiology` (ib11, 11.4y) — 역학이라 비교적 안정하나 11년·고중심성.
- `sinus-lift/diaz-olivares-2021-schneiderian-membrane-perforation` (ib11, 5.4y)
- `immediate-implant/seyssens-2021-immediate-implant-connective-tissue-graft-sr-ma` (ib9, 5.6y)
- `implants/di-stefano-2021`, `implants/mortazavi-2021`, `implants/mello-machado-2021-rct`(ib8), `resin/boaro-2019-bulk-fill`(ib8), `prosthetic-materials/tiu-2015`(ib8), `implants/rocha-2016-platform-switching-3year-rct`(ib7), `sinus-lift/el-ghobashy-osseodensification-vs-osteotome`(ib7).

## P2 — anchor 추정, 기회 될 때만 (기전 안정 / 교육용 고전)

검증 불필요할 가능성 높음 — 갱신보다 "anchor" 표기가 맞을 수 있다:
- `drug/catella-lawson-2001-cyclooxygenase-inhibitors-aspirin-nejm` (24.4y, RCT) — aspirin-NSAID 상호작용 기전, NEJM 고전. anchor.
- `drug/renda-2006`, `drug/wells-2011-ibuprofen-acetaminophen-rct`, `drug/moore-2015-single-dose-oral-analgesics-cochrane-overview` (ib9) — 진통 기전 안정.
- `behavioral-dentistry/lundahl-2013-motivational-interviewing` (12.6y) — MI 방법론, 안정.

→ P2는 검증 대신 `superseded_scope` 개념의 역(逆)인 "anchor" 주석을 본문에 한 줄 다는 것으로 충분. decay 신호에서 반복 노출되는 잡음을 줄이려면 향후 `anchor: true` 같은 opt-out 플래그를 고려할 수 있으나, 지금은 과설계라 보류. [claude해석]

## 실행 제안

1. ARP SR+MA(2024~2026) 1편 확보 → ingest → ARP 클러스터 다중 supersede + bone-regeneration overview refresh. (단일 최고 ROI)
2. revilla-leon-2021(AI) → 최신 AI-in-implant SR 확인. AI는 분야 특성상 별도 우선.
3. socket-shield(ogawa-2022 + atef-2021) 묶음 검증.
4. P2는 검증 제외, 필요 시 anchor 주석만.

관련: `agenda/2026-05-31_supersession-decay-setup.md`. 매 `daily-audit.py` 실행 시 카테고리·중심성 분포가 `logs/{date}_supersession.log`에 재계산된다.
