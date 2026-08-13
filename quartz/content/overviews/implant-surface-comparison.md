---
title: "임플란트 표면처리 비교 — SLA·CA·UV 광기능화·골밀도화 매트릭스"
authors: synthesis (llm-wiki)
year: 2026
date: 2026-08-07
type: overview
category: [overviews]
tags: [implant-surface, SLA, SLActive, CA, UV-photofunctionalization, hydroxyapatite, hydrophilic, biological-aging, osseointegration, bone-to-implant-contact, BIC, surface-topography, magnesium-coating, silver-coating, tricalcium-phosphate, implant-neck-topography, peri-implantitis-risk, adventitious-carbon, organic-acid, native-oxide, wavelength-dependent]
source_papers: 
evidence_level: synthesis
source: synthesis
relations:
  - type: extends
    target: bonfante-2012-calcium-phosphate-coatings-plasma-spray
  - type: extends
    target: witek-2020-boronized-surface-osseointegration
  - type: refines
    target: lang-2022-photofunctionalization-implant-stability-marginal-bone-loss-sr-ma
  - type: reinforces
    target: vilchez-2025-sla-slactive-split-mouth-rct
  - type: extends
    target: komatsu-2026-uv-photofunctionalization-surface-agnostic-biofilm-soft-tissue-sr
  - type: extends
    target: czumbel-2019-sandblasting-implant-failure-rate-sr-ma
  - type: refines
    target: implants/surface/damerau-2021-inorganic-surface-coatings-tcp-ha-periimplant
    note: "major correction — pooled large-animal meta-analysis (15 studies) finds NO significant BIC advantage of TCP/HA coating over uncoated rough Ti, HA significantly lower at 14 days (p=.001); this overview's favorable CaP/HA framing (built on single-study bonfante-2012/yamada-2012) required an explicit caveat as a result"
  - type: refines
    target: implants/surface/dipalma-2026-implant-surface-characteristics-peri-implant-outcomes
    note: "fills the long-standing 'peri-implantitis 장기 발생률' coverage gap; tempers surface-optimistic framing with long-term evidence that patient/site risk factors outweigh surface type"
  - type: refines
    target: implants/surface/saini-2024-bone-apposition-surface-modified-titanium-animal
    note: "nuances the sandblasting-as-minimum-roughness-threshold claim — sandblasted-alone (without acid-etch) does not separate from machined on BIC/RTV in animal histomorphometry"
  - type: refines
    target: implants/surface/serbanescu-2025-nanofeatured-titanium-surfaces-dental-implants
    note: "adds a durability caveat to the hierarchical-roughness/nanofeature enthusiasm in §4 — early gains converge with microrough controls by 8-12 weeks"
  - type: extends
    target: implants/surface/huraib-2023-micro-threaded-laser-textured-implant-neck-peri-implant
    note: "adds a new axis — implant-NECK micro-topography (distinct from body/thread surface technology) — to the surface-comparison framework"
  - type: extends
    target: implants/surface/wagstaffe-2019-rgd-tripeptide-adsorption-titania-surfaces
    note: "adds the chemical identity of the hydrocarbon contamination layer (small organic acids, carboxylate-cation bridging) that sits ON TOP of the permanent TiO2 oxide layer — clarifies that 'aging' is contamination accumulation, not oxide-state change"
  - type: extends
    target: implants/surface/houshmand-2023-uv-photofunctionalization-sla-titanium-disks
    note: "shows decontamination is wavelength-dependent (UVC works, UVB does not) — wettability improvement alone does not confirm the contamination layer was removed"
  - type: reinforces
    target: implants/surface/trisi-2003-bone-implant-contact-machined-dual-acid-etched
    note: "early human split-surface histomorphometry (2003, n=11) — dual acid-etched BIC 47.81% vs machined 19.00% at just 2 months, gap widening in low-density bone; the historical human-data anchor for the roughened-vs-machined direction this overview and czumbel-2019 (failure-rate RCT SR+MA) already establish"
---

## 한국어 핵심요약

> [!summary] 한국어 핵심요약
> - 핵심: 임플란트 표면처리 15편 + 횡단 인용 5편 종합 — SLA·CA·UV 광기능화·골밀도화를 매트릭스로 비교.
> - SLA/SA = 임상 표준 — 8년 생존 94.8%(Kim 2020 retrospective, n=96).
> - CA(초친수성, Osstem) = 더 안정적 — 5.2년 생존 97.3%, MBL 0.074mm(Kim 2022 retrospective, n=258); 한국에서 가장 검증된 초친수성 옵션.
> - UV 광기능화(Photofunctionalization, UV-PF) = 위축골·복잡증례 1순위 — 복잡증례 ISQ +21.9, 7년 100% 성공(Hirota 2020 prospective).
> - 표면처리의 진짜 기전은 친수성(접촉각)이 아니라 탄화수소(Hydrocarbon) 제거를 통한 양전하(Electropositivity) 회복 = 생물학적 노화(Biological Aging) 역전(Hayashi 2014, Minamikawa 2016 in-vitro).
> - 탄소/티타늄(C/Ti) 비율↑ → 골아세포 부착·증식·분화 농도 의존적 감소(C/Ti=1.0에서 ALP·칼슘 무기화 >40% 감소).
> - **근거 갱신(2026-08) — 산화막과 오염막은 다른 층**: 티타늄은 가공 직후 즉시·영구적으로 산화막(TiO₂)이 생기고 이는 사라지지 않는다 — "노화"란 그 산화막 위에 별도로 쌓이는 부착탄소오염 (Adventitious Carbon)층 얘기다. Wagstaffe 2019(XPS/STM)가 그 정체를 처음 특정: 기름·유분이 아니라 폼산·아세트산 같은 소형 유기산이 카르복실기-Ti 결합으로 화학흡착된 것. UV/플라즈마가 벗겨내는 건 산화막이 아니라 이 카르복실기-Ti 결합이며, Houshmand 2023(EDS)은 이게 파장 의존적임을 보임 — UVC는 실제로 벗겨내나 UVB는 접촉각만 개선하고 탄소는 그대로.
> - 친수성 표면은 ISQ 절대값을 올리는 게 아니라 D3/D4 골에서 stability dip을 제거해 조기 부하 시기를 앞당김(Canullo 2024 prospective: 친수성 T45 74.97 vs SLA 73.44, p<0.05).
> - 생물학적 노화는 4주가 아닌 6개월까지 지속 — 포장 후 6개월 이상 보관 임플란트는 골유착 손실 가능, UV-PF로 역전.
> - 샌드블라스팅(Sandblasting) vs 머신드(Machined) 직접 비교 RCT SR+MA(Czumbel 2019, 7 RCT, 722임플란트): 샌드블라스팅이 실패율을 1년 80%(RR=0.20, I²=0%), 5년 74%(RR=0.26, I²=0%) 감소. 단 변연골소실(MBL)은 두 표면 간 유의차 없음 — **표면 거칠기는 실패율을 낮추지만 변연골 유지에는 영향을 주지 않는다**는 핵심 분리(Dissociation).
> - 거칠기 최적: 메조+마이크로+나노 계층형(Hierarchical) 표면이 이론적 최적(Hasegawa 2020 in-vivo).
> - 골밀도화(Osseodensification, OD)는 표면처리가 아니라 osteotomy 기법 — Densah burs로 측방 골 압축, 표면처리와 보완 관계; TSFE에서 ISQ 우위(Starch-Jensen 2025 SR+MA).
> - 근거 갱신(2026-06): UV-PF 임상 SR+MA가 등장(Lang 2022, 임상 7편/734임플란트) — 골유착 속도지수(OSI, MD=2.13)·2개월 안정성은 유의 상승하나 다른 시점·MBL은 비유의(I²≤99%, high RoB); SLA vs SLActive 직접 비교 split-mouth RCT도 등장(Vílchez 2025, n=68) — ISQ 궤적·12개월 MBL 동등.
> - **근거 갱신(2026-08) — 중요 정정**: TCP/HA 코팅이 골전도(Osteoconduction)를 개선한다는 이 오버뷰의 기존 우호적 서술은 **대형동물 15편 메타분석(Damerau 2021)으로 뒤집힘** — 이미 거친(rough) 비코팅 티타늄 대비 TCP/HA 코팅은 BIC 유의 우위 없음, HA는 오히려 14일차에 유의하게 낮음(−6.94%p, p=.001). 기존에 인용한 yamada-2012(단일 쥐 연구)와 정면 상충(contradicts) — **작은 표본 단일 연구가 큰 표본 메타분석에 뒤집힌 사례**.
> - 코팅 화학(Coating Chemistry) 확장 — 금속 코팅 중 마그네슘(Mg)은 BIC 유의 향상(Alenezi 2026, Z=4.38, p<0.001, 전임상 11편), 은(Ag)은 BIC 유의하나 더 약함(Alenezi 2025, Z=2.01, p=0.04, 동물 16편, 골 부피 무해). 생체분자(BMP·콜라겐·펩타이드) 코팅은 **두 SR+MA가 상반**: Alshayeb 2024(동물 9편)는 BIC MD=7.29 유의, López-Valverde 2022(전임상 26편, 더 큰 표본)는 이질성 I²=99%로 유의차 없음 — 생체분자 코팅의 BIC 이점은 아직 결론 나지 않음.
> - 지르코니아(Zirconia) CaP 코팅(Matys 2025, SR 27편): 티타늄과 다른 패턴 — 티타늄은 이미 반응성 표면이라 CaP 코팅 유형차가 BIC에 안 드러나지만(Bonfante 2012), 생체불활성 지르코니아는 코팅 유무 자체가 BIC를 좌우; 단 장기 인체 RCT 없이 "연구단계".
> - 샌드블라스팅 재정정(Saini 2024, 동물 37편 SR+MA): **단독 모래분사만으로는 BIC·RTV 모두 머신드 대비 유의차 없음**(SMD 9.44, p=0.65) — SLA(산부식 결합)·레이저·양극산화는 전부 유의(p<0.01). 즉 "샌드블라스팅=거칠기 최소 기준"이라는 §2.2 결론은 **모래분사 단독이 아니라 SLA 이상의 복합처리에만 성립**.
> - 나노구조 표면(Șerbănescu 2025, SR 25편): 초기(2-4주) 골유착 가속은 21/25편에서 확인되나 **8-12주면 마이크로거칠기 대조군과 수렴** — 계층형(메조+마이크로+나노)이 "이론적 최적"이라는 §4 서술에 지속성 단서 추가, GRADE 확신도 낮음~매우낮음.
> - Peri-implantitis 장기 연관(Dipalma 2026, SR 13편, 인체 비교연구): 단기 RCT는 표면 간 MBL 차이 미미하나 **장기 후향적 코호트는 거친 표면이 peri-implantitis 오즈 증가와 연관**(Ferrantino OR 4.877; Raes 5년 12/42 vs 3/41, p<0.01) — 단, 환자·부위 위험요인(흡연·치주염력·유지관리)이 표면 효과보다 우세. **단기 골유착 이점과 장기 peri-implantitis 위험이 같은 거칠기 축에서 트레이드오프**할 수 있음을 시사.
> - 임플란트 넥(Neck) 미세지형은 몸체 표면과 별개 축(Huraib 2023, SR 15편): 거친 미세나사산/레이저 넥이 매끄러운 넥보다 MBL·PD 유의하게 낮음, 단 1편은 매끄러운 넥에서 peri-implantitis 빈도가 오히려 낮음(2.92% vs 14.41%) — MBL과 감염위험이 같은 방향으로 안 움직인 사례.
> - 한계: 직접 비교 RCT는 등장했으나 SLA-SLActive-CA 3자 동시 비교·다기관 RCT는 여전히 부재; 암절제·방사선 환자는 UV-PF로도 7년 22.2%로 불충분(병태생리적 손상 보상 불가); TCP/HA·Mg·Ag 코팅은 전부 동물 데이터뿐 인체 RCT 부재.
> - 골질별 알고리듬: D1/D2 → SLA/SA, D3 → CA/친수성, D4 → CA/SLActive + OD 또는 UV-PF, 노화 임플란트 → UV-PF 역전 후 사용. (CaP/HA 코팅은 이제 골질 알고리듬에서 근거 등급 하향 — §2.4 참조)

## Three-line Summary

Synthesis matrix of 15 `implants/surface/` papers + 5 cross-cited across SLA/SA, hydrophilic CA/SLActive, UV photofunctionalization (UV-PF), and osseodensification (OD): SLA/SA remains the clinical standard (8y survival 94.8%, Kim 2020 retrospective n=96); hydrophilic CA/SLActive surfaces remove the D3/D4 stability dip without raising absolute ISQ (CA 5.2y 97.3% survival, MBL 0.074 mm, Kim 2022 n=258); UV-PF is first-line for atrophic/complex cases (ISQ +21.9 in complex sites, 7y 100% success, Hirota 2020 prospective).

The dominant surface-efficacy mechanism is hydrocarbon removal reversing biological aging (C/Ti ratio rise depresses osteoblast ALP and mineralization >40%), not hydrophilicity per se (Hayashi 2014, Minamikawa 2016 in-vitro); biological aging continues up to 6 months post-packaging, making UV-PF a validated rescue for aged implants.

OD is an osteotomy technique (not a surface) complementary to surface choice — it provides ISQ advantage over conventional drilling in maxillary sinus floor elevation (TSFE) cases (Starch-Jensen 2025 SR+MA) and general placement in D3/D4 bone; sandblasting vs machined surfaces: roughened implants reduce 1y failure rate by 80% (RR=0.20) and 5y failure rate by 74% (RR=0.26), but have no effect on marginal bone loss (Czumbel 2019 SR+MA, 7 RCTs, 722 implants).

## 세줄요약

임플란트 표면처리 15편 + 5편 횡단인용 종합 매트릭스: SLA/SA = 임상 표준(8년 생존 94.8%, Kim 2020 n=96); 친수성(CA/SLActive) = D3/D4 골에서 stability dip 제거, 절대 ISQ 상승은 아님(CA 5.2년 97.3%, MBL 0.074 mm, Kim 2022 n=258); UV 광기능화(UV-PF) = 위축골·복잡증례 1순위(ISQ +21.9, 7년 100% 성공, Hirota 2020 전향적).

표면처리의 핵심 기전은 친수성이 아니라 탄화수소(Hydrocarbon) 제거를 통한 생물학적 노화(Biological Aging) 역전 — C/Ti 비율↑ 시 골아세포 ALP·무기화 >40% 감소(Hayashi 2014·Minamikawa 2016 in-vitro); 생물학적 노화는 포장 후 6개월까지 지속되므로 노화 임플란트는 UV-PF로 역전 후 사용.

골밀도화(Osseodensification, OD)는 표면처리가 아닌 술기 — 상악동거상 동시식립(TSFE)에서 일반 드릴링 대비 ISQ 우위(Starch-Jensen 2025 SR+MA); 거칠기 비교: 샌드블라스팅은 1년 실패율 80%·5년 실패율 74% 감소하나(RR=0.20·0.26), 변연골소실에는 영향 없음(Czumbel 2019 SR+MA, 7 RCT, 722개).

---

## Summary

LLM-Wiki `implants/surface/` 35편+ (2026-06까지 15편+횡단인용 3편; 2026-08-07 갱신에서 12편 추가 — 코팅화학 확장 6편, 넥디자인 1편, 장기 peri-implantitis 연관 1편, 기존결론 정밀화 2편, 오염 화학기전 확장 2편(횡단인용 3→5)).

근거 등급(2026-08 기준): sr+ma 다수(Czumbel·Lang·Damerau·Saini·Alshayeb·López-Valverde·Alenezi×2) · sr 다수(Komatsu·Serbanescu·Dipalma·Matys·Huraib) · RCT 다수(Vílchez·Krishna·Farsiani) · Prospective(Hirota UV-PF 7년) · Retrospective 2편(Kim 2020 SA·Kim 2022 CA) · narrative-review·in-vitro·animal 다수. **장기 임상 결과는 retrospective 2편이 핵심**이며 (Kim 2020 SA 94.8% 8년, Kim 2022 CA 97.3% 5.2년), SLA→SLActive→CA→UV-PF 진화에서 각 단계의 임상 근거 차이가 크다. 2026-08 갱신으로 **CaP/HA 코팅 효능 하나가 정정**됐고(Damerau 2021), **금속/생체분자 코팅·넥디자인·장기 peri-implantitis 연관**이라는 3개 신규 축이 더해졌다.

핵심 질문 6개 (2026-08, 4→6):
1. **표면처리의 핵심 기전은 무엇인가** — 거칠기 vs 친수성 vs 탄화수소 vs 노화 역전
2. **표면별 임상 성과는** — 생존·MBL·ISQ
3. **어떤 환자·골질에 어떤 표면을 선택하나** — 임상 적용
4. **UV 광기능화의 위치** — 차세대 표준 vs 보조 기술
5. **코팅 화학(Mg·Ag·CaP·HA·생체분자)이 실제로 BIC를 개선하는가** — 개별 메타분석 근거로 재평가 (§2.4, 2026-08 신규)
6. **표면 거칠기의 단기 이점과 장기 peri-implantitis 위험이 트레이드오프하는가** — §10 (2026-08 신규)

---

## 1. 표면처리 기전의 3차원 이론 (D1·D2·D3)

[확인 — Ogawa 2025 narrative-review의 3D 이론 채택]

| 차원 | 의미 | 임상 의미 |
|---|---|---|
| **D1: 재료 (Material)** | Ti, TiO2, HA, Zr | Ti 표준; HA·Zr는 보조 |
| **D2: 표면 형상 (Topography)** | 마이크로·나노·계층 | 마이크로 단독 → 마이크로+나노 진화 |
| **D3: 시간·노화 (Time/Aging)** | 탄화수소 오염 → 생물학적 노화 | **UV-PF로 역전** 가능 |

**핵심 발견** [확인]: 표면처리 효능의 진짜 driver는 친수성(접촉각)이 아니라 **탄화수소 제거 → 양전하 (Electropositivity) 회복**.

| Confidence | 출처 | 결론 |
|---|---|---|
| **in-vitro** | [[implants/surface/hayashi-2014-hydrocarbon-attenuates-osteoblast-titanium]] | **탄소/티타늄 (C/Ti) 비율↑ → 골아세포 부착·증식·분화 농도 의존적 감소**; C/Ti=1.0에서 ALP·칼슘 무기화 >40% 감소 — BIC 정체의 직접 원인 |
| **in-vitro** | [[implants/surface/minamikawa-2016-long-term-degradation-titanium-biological]] | **티타늄 생물학적 노화는 4주가 아닌 6개월까지 지속**; 친수성보다 탄화수소 오염이 주된 노화 구동자 |
| **in-vitro** | [[implants/surface/iwasa-2011-tio2-micro-nano-hybrid-biological-aging]] | TiO2 나노결절 (300 nm) + 마이크로피트 → UV-PF 후 7일까지 생체활성 유지; **기전은 친수성이 아닌 양전하 지속** |
| **in-vitro** | [[implants/surface/wagstaffe-2019-rgd-tripeptide-adsorption-titania-surfaces]] | **2026-08 신규**: XPS/STM으로 "탄화수소"의 화학적 정체를 처음 특정 — 기름·유분이 아니라 폼산·아세트산 같은 소형 유기산이 카르복실기-양이온 브리징으로 화학흡착된 층; SLActive는 이 층이 SLA보다 얇아 RGD 펩타이드 흡수↑ |
| **in-vitro** | [[implants/surface/houshmand-2023-uv-photofunctionalization-sla-titanium-disks]] | **2026-08 신규**: UVC(210nm)는 탄소·질소 유의 감소, UVB(310nm)는 접촉각만 개선(129.9°→58.9°)하고 탄소·질소는 무변화 — **습윤성 개선이 곧 탈오염 증명이 아님** |

**산화막 vs 오염막 — 두 개의 다른 층 (2026-08 명확화)** [확인]: "산화됐다"는 사실 자체와 "활성화 상태"를 혼동하기 쉽다. 실제로는 층이 두 개다.

1. **산화막 (TiO₂, native oxide)** — 티타늄이 가공 직후 공기에 닿는 순간 거의 즉시·영구적으로 형성. 이 층은 시간이 지나도 사라지거나 되돌아가지 않는다(Wagstaffe 2019: "inert and biocompatible protective titanium dioxide layer").
2. **오염막 (adventitious carbon, 부착탄소)** — 그 산화막 **위에** 대기 노출 시간에 따라 쌓이는 별개의 층. 폼산·아세트산 같은 소형 유기산이 산화막 표면의 카르복실기-Ti 결합으로 붙는다(Wagstaffe 2019). 이게 4주~6개월에 걸쳐 진행되는 진짜 "노화"다(Minamikawa 2016).

즉 "활성화 상태"란 **산화막은 있고 오염막은 아직 없는** 초기 상태(접촉각≈0°)를 말하는 것이지, 산화 여부 자체가 활성/비활성을 가르지 않는다. UV/플라즈마가 벗겨내는 것도 산화막이 아니라 그 위의 오염막(카르복실기-Ti 결합)이다 — UV 광자가 이 결합을 직접 해리시키거나(Roy et al 모델, Houshmand 2023 인용), 플라즈마의 반응성 산소/질소종이 같은 결합을 화학적으로 공격한다.

[미검증] 임상 의미: **포장 후 6개월 이상 보관된 임플란트는 노화로 골유착 손실 가능**. UV-PF는 이를 역전.

---

## 2. 표면처리 진화 — 임상 결과 매트릭스

### 2.1 표면 종류 정의

| 약어 | 풀네임 | 처리 방식 | 친수성 |
|---|---|---|---|
| **Machined** | Turned/Polished | 미처리 | 저 |
| **SLA** | Sandblasted, Large-grit, Acid-etched | 알루미나 분사 + 산부식 | 중 |
| **SA / SLA-like** | 산부식 알루미나 | 산업 표준 변형 | 중 |
| **SLActive** | SLA + 질소 보관 + 식염수 | 친수성 유지 보관 | 고 |
| **CA / Super-hydrophilic** | Calcium / Hydrophilic SA | Ca 처리 초친수 | 초고 |
| **HA-coated (PSHA/ACP)** | Plasma-sprayed HA / Amorphous CaP | 플라즈마 스프레이 결정질·비결정질 CaP | 화학적 결합 |
| **Boronized** | TiB/TiB₂ surface (pack boriding) | 고온 고체확산 — 마모·부식 저항성 우수 | N/A (osseointegration-impaired) |
| **UV-PF** | UV Photofunctionalization | 표면 UV 조사 (12–15분) | 초고 + 양전하 |

### 2.2 임상 결과 비교

| Confidence | 출처 | 표면 | 결과 | 추적 |
|---|---|---|---|---|
| **sr+ma** | [[implants/surface/czumbel-2019-sandblasting-implant-failure-rate-sr-ma]] | **Sandblasted vs Machined (직접 비교)** | 실패율 1년 **RR=0.20** (80%↓, I²=0%), 5년 **RR=0.26** (74%↓, I²=0%); MBL 1년 WMD=−0.10mm(NS), 5년 WMD=−0.01mm(NS) — **생존에서 분리된 MBL 동등성** | 7 RCT, 722임플란트 |
| **sr+ma** | [[implants/surface/lang-2022-photofunctionalization-implant-stability-marginal-bone-loss-sr-ma]] | **UV-PF (임상 SR+MA)** | **첫 임상 SR+MA** — 골유착 속도지수(OSI) **MD=+2.13 (p=0.007)**, 2개월 안정성 MD=+3.48 (p=0.04); 다른 시점·MBL은 비유의 (I²≤99%, high RoB) | 임상 7편(5 RCT) / 430명·734임플란트 |
| **sr (2026)** | [[implants/surface/komatsu-2026-uv-photofunctionalization-surface-agnostic-biofilm-soft-tissue-sr]] | **UV-PF (표면 비의존)** | 최신·최광 UV-PF SR — UV-PF = **표면형태 보존 "포지티브섬" 재활성화**; 초기 세균부착·바이오필름↓ + 연조직 봉쇄↑(Ti 일관, Zr 신흥); 임상 일관 신호 = 안정성 가속 | 34편(질적 종합) |
| **prospective(7yr)** | [[implants/surface/hirota-2020-uv-photofunctionalization-dental-implant-7year]] | **UV-PF** | 일반·복잡증례 **100% 성공**; 암절제 22.2%; 복잡증례 **ISQ +21.9** | 7년, n=70 |
| **rct (split-mouth, 당뇨)** | [[implants/surface/krishna-2025-uv-photofunctionalization-diabetic-implant-stability-rct]] | **UV-PF** | 조절 당뇨 환자에서 3개월 ISQ 상승폭 4.40 vs 2.60, OSI 1.42 vs 0.84, 9개월 원심 골소실 0.35 vs 0.64mm (모두 유의) — UV-PF 효과를 **대사적 손상 host로 확장** | split-mouth |
| **rct (split-mouth, 프랙탈)** | [[implants/surface/farsiani-2025-photofunctionalized-implants-fractal-bone-analysis-rct]] | **UV-PF** | 임플란트 주위 해면골 프랙탈 차원(FD) 식립 전→후 유의 상승(1.075→1.103, p=0.044), 대조군 무변화; 양군 조기 생존 100% (ISQ 미측정) | 21명·42임플란트, 12–16주 |
| **rct (n=68, split-mouth)** | [[implants/isq/vilchez-2025-sla-slactive-split-mouth-rct]] | **SLA vs SLActive 직접비교** | **첫 직접 비교 RCT** — 변형 SLActive vs 기존 SLA(BLT Roxolid): ISQ 궤적·1차결과(부하→12개월 MBL 0.04 vs 0.07mm, p=0.658) **동등**, 양군 생존 100% | 136임플란트, 12개월 |
| **rct (n=40, 즉시식립)** | [[implants/surface/ko-2024-hydroxyapatite-nano-coated-sla-immediate-implants]] | **HA 나노코팅 SLA vs SLA** | 상악 구치부 즉시식립(가이드): HA 나노코팅이 ISQ 회복·volumetric 안정성 우위 경향(abstract 수준) | SNU, 다시점 ISQ |
| **rct (n=30)** | [[implants/surface/kim-2016-hydrophilic-tapered-implant-6week-12week-loading]] | 친수성 테이퍼 | 6주/12주 부하 모두 97.56% 성공 | 1년 |
| **retrospective(n=258, 5.2yr)** | [[implants/surface/kim-2022-ca-implant-superhydrophilic-surface-long-term]] | **Osstem CA** | 생존 97.3%, 성공 94.2%, MBL 0.074mm | 평균 62개월 |
| **retrospective(n=96, 8yr)** | [[implants/surface/kim-2020-sa-implant-acid-etched-alumina-long-term]] | **Osstem SA** | 생존 94.8%; 합병증·1년 MBL>1mm = 실패 예측 | ≥8년 |
| **prospective(early-loading)** | [[implants/surface/cochran-2002-reduced-healing-iti-sla-surface]] | **ITI SLA** | 4.1 mm SLA 솔리드스크류를 ~6주(class IV는 ~12주)에 보철 — abutment 35 Ncm 성공 99.3%, 1·2년 생명표 성공 99.1% | 1–2년, n=110/326 |
| **prospective (D3/D4)** | [[implants/isq/canullo-2024-bioactive-surface-poor-bone-isq-stability]] | 나노 생체활성 | **Stability dip 제거** (T0=74.57 → T45=74.97 vs SLA T0=77.12 → T45=73.44, p<0.05) | 45일 |
| **case-report** | [[implants/isq/seol-2017-uv-implant-resonance-frequency-early-loading]] | UV-PF | 1–4주 조기부하 가능 | — |
| **animal** | [[implants/surface/yamada-2012-nanopolymorphic-hydroxyapatite-titanium-implant]] | 나노 HA 코팅 | BIC·강도 조기·후기 모두 향상; 효과 표면 50 µm 이내 (**단일 쥐 연구 — 아래 damerau-2021 대형동물 메타분석과 contradicts, §2.4 참조**) | 쥐 |
| **animal** | [[implants/surface/bonfante-2012-calcium-phosphate-coatings-plasma-spray]] | PSHA vs ACP (플라즈마 스프레이) | 결정성(71% HA vs <1%) 및 거칠기(Sa 3.22 vs 5.18 µm) 차이에도 불구하고 BIC·BAFO 6주·12주 동등 (P>0.86 / P>0.75) — 임플란트 매크로 형태(plateau root form)가 CaP 코팅 유형보다 골전도에 우선할 수 있음 | 비글 6마리, 36개, 6+12주 |
| **animal** | [[implants/surface/witek-2020-boronized-surface-osseointegration]] | Boronized (BM·BAA) vs acid-etched control | BIC·BAFO 보론화군에서 시간이 지날수록 감소 (BAA BIC: 21.73%→5.93%, p<0.01; BAFO 3→6주 significant decline p<0.03), 대조군은 증가 — TiB/TiB₂ 표면에서 골 탈회(osteoid foci) 관찰, 기계적 특성 우수에도 골유착 저해 | 양 5마리, 40개, 3+6주 |
| **sr+ma (2021)** | [[implants/surface/damerau-2021-inorganic-surface-coatings-tcp-ha-periimplant]] | **TCP·HA 코팅 vs 비코팅 거친 Ti (직접 비교)** | 40편 SR + 15편 MA — TCP·HA 코팅 모두 **비코팅 거친 티타늄 대비 통계적으로 견고한 BIC 우위 없음**; HA는 14일에 오히려 유의하게 낮음(−6.94%p, p=.001); 42–84일엔 TCP가 비유의하게 우세(+13.79%p, p=.08) | 대형동물(개·염소·양·돼지) 40편 |
| **sr+ma (2024)** | [[implants/surface/saini-2024-bone-apposition-surface-modified-titanium-animal]] | 표면처리 종류별(SLA·레이저·산부식·양극산화·**단독 모래분사**) | SLA·레이저·산부식·양극산화는 BIC 유의 우수(p<0.01)하나 **단독 모래분사는 BIC·RTV 모두 비유의**(SMD 9.44, p=0.65) — 샌드블라스팅 단독은 산부식 등 추가처리 없이는 불충분 | 동물 37편(1891임플란트) |

**합성 결론** [확인]:

- **샌드블라스팅 단독 vs SLA — 2026-08 정정** [확인]: Czumbel 2019(인체 RCT, 실패율 outcome)는 샌드블라스팅이 머신드 대비 실패율을 80%/74% 낮춘다고 확정했으나, Saini 2024(동물 BIC/RTV 기전 outcome)는 **단독 모래분사만으로는 BIC·RTV가 머신드와 유의차 없음**(p=0.65/0.51) — 실패율(임상 outcome)과 골접촉 기전(histomorphometric outcome)이 반드시 같이 움직이지 않음을 시사. **임상 실무 함의**: "샌드블라스팅=최소 기준"이라는 표현은 정확히는 "SLA(산부식 결합) 이상의 복합처리=최소 기준"으로 좁혀 읽어야 함.
- **SLA/SA = 임상 표준** — 8년 94.8% 생존 (Kim 2020 retrospective); 그 표준의 출발점인 **SLA 단축 치유(~6주 부하)**의 최초 다기관 임상 근거는 Cochran 2002 (n=110/326 prospective, abutment 35 Ncm 성공 99.3%, 1·2년 성공 99.1%)로, 친수성·UV-PF 가속 부하 프로토콜이 비교되는 역사적 baseline
- **CA (초친수성) = 더 안정적** — 5.2년 97.3% 생존, MBL 거의 무 (Kim 2022 retrospective)
- **UV-PF = 가장 강한 7년 임상 근거** — 복잡증례에서 ISQ +21.9 (Hirota 2020 prospective); **임상 SR+MA(Lang 2022)도 등장** — OSI(골유착 속도) MD=+2.13으로 "안정성 도달 속도" 가속은 확증, 단 절대 안정성·MBL pooled 효과는 비유의(high heterogeneity·RoB)
- **SLA vs SLActive 직접 비교 RCT 등장** — Vílchez 2025(split-mouth, n=68): 변형 SLActive와 기존 SLA가 ISQ 궤적·12개월 MBL **동등** → 친수성의 임상 우위는 "절대값"이 아니라 D3/D4·가속 부하 같은 **특정 시나리오에 한정**된다는 본 overview의 thesis를 직접 보강 [미검증]
- **CaP/HA 코팅 = 2026-08 근거 하향** [확인]: 이 overview는 2026-06까지 bonfante-2012(동등성)·yamada-2012(HA 우위)를 근거로 CaP/HA 코팅에 우호적이었으나, **Damerau 2021(15편 pooled MA)이 이를 뒤집음** — 이미 거친 티타늄 대비 TCP·HA 코팅은 견고한 BIC 우위가 없고, HA는 14일차에 오히려 유의하게 낮다. 저자 해석: 기준 표면 자체의 조도가 CaP 코팅 화학의 골전도 이점을 가릴 가능성 — **"코팅"보다 "거칠기"가 더 지배적인 변수**라는 이 overview 전체의 핵심 thesis(§1 탄화수소·§4 거칠기)와 오히려 정합적. 상세는 §2.4.
- **여전히 부재** — SLA·SLActive·CA 3자 동시 비교·다기관 RCT; TCP/HA·Mg·Ag 코팅의 인체 RCT [미검증]

### 2.3 친수성 표면이 무엇을 바꾸나 — Stability Dip

[확인 — Canullo 2024 prospective, D3/D4 골]

| 시점 | 친수성 나노 표면 ISQ | 전통 SLA ISQ |
|---|---|---|
| T0 (식립) | 74.57 ± 7.85 | 77.12 ± 5.83 |
| T30 (30일) | 74.78 ± 7.31 | **73.33 ± 6.13** (p<0.05 vs T0) |
| T45 (45일) | 74.97 ± 6.34 | **73.44 ± 7.89** (p<0.05 vs T0) |

**핵심**: 친수성 표면이 ISQ 절대값을 올리는 게 아니라 **dip을 제거**해서 조기 부하 가능 시기를 앞당김.

### 2.4 코팅 화학(Coating Chemistry) 확장 — Mg·Ag·생체분자·Zr-CaP (2026-08 갱신)

[확인 — Alenezi 2026/2025, Alshayeb 2024, López-Valverde 2022, Matys 2025, 전부 동물/전임상 SR·SR+MA]

기존 §2.1–2.2는 표면 **형태(topography)**(SLA/CA/UV-PF) 축이었다. 2026-08 서베일런스는 표면 **코팅 화학(coating chemistry)** 축을 동물/전임상 SR·SR+MA 6편으로 보강한다 — 어떤 첨가 원소·분자가 BIC에 유의한 효과를 내는지 메타분석 수준에서 재평가.

| Confidence | 출처 | 코팅 | BIC 효과 | 비고 |
|---|---|---|---|---|
| **sr+ma** | [[implants/surface/alenezi-2026-magnesium-modified-titanium-implants-osseointegration]] | 마그네슘(Mg) | **유의 향상** (Z=4.38, p<0.001) | BA는 비유의(Z=0.93); 전임상 11편 |
| **sr+ma** | [[implants/surface/alenezi-2025-implant-silver-coatings-bone-formation]] | 은(Ag) | **유의 향상, 더 약함** (Z=2.01, p=0.04) | BA·BV/TV 무영향(골형성 악영향 없음); 동물 16편 |
| **sr+ma** | [[implants/surface/alshayeb-2024-bioactive-surface-modifications-dental-implants]] | 생체분자(콜라겐·BMP-2, 9편) | **유의 향상** (MD=7.29, I²=50%) | 콜라겐=초기촉진, BMP-2+HA=최다효과 |
| **sr+ma** | [[implants/surface/lopez-valverde-2022-biomolecule-based-bioactive-surfaces-osseointegration]] | 생체분자(펩타이드·BMP·콜라겐, 26편) | **비유의** (I²=99%, 출판편향 소견) | Alshayeb 2024와 정반대 결론 — 표본 3배 크나 이질성이 압도 |
| **sr+ma** | [[implants/surface/damerau-2021-inorganic-surface-coatings-tcp-ha-periimplant]] | TCP·HA (15편) | **비유의, HA는 14일 유의 열세** | §2.2 참조 — yamada-2012와 contradicts |
| **sr** | [[implants/surface/matys-2025-osseointegration-zirconia-implants-calcium-phosphate]] | CaP on 지르코니아 (27편) | 초기(1-4주) 우위, 시간 지날수록 격차 축소 | 메타분석 불가(이질성); 장기 인체 RCT 없음 |

**해석** [미검증]:
- **금속 이온 코팅(Mg·Ag)이 오히려 유기 생체분자 코팅보다 더 견고한 메타분석 신호를 낸다** — Mg/Ag는 각 1편의 최신 SR+MA로 유의(p<0.05)했지만, 생체분자 코팅은 두 SR+MA가 정반대 결론(Alshayeb 유의 vs López-Valverde 비유의)이라 아직 결론 낼 수 없음. 표본 크기(9편 vs 26편)와 포함 기준 차이가 원인으로 보이나, 임상 권고 단계는 아님.
- **"코팅하면 다 좋다"는 성립하지 않는다** — TCP/HA(전통적으로 가장 오래·널리 쓰인 코팅)가 가장 약한 근거(비유의~유의하게 열세)를 보인 반면, 신흥 코팅(Mg)이 가장 강한 근거(p<0.001)를 보임. 코팅의 "역사"나 "친숙도"가 아니라 개별 메타분석 근거로 판단해야 함.
- **전부 동물/전임상 데이터** — 인체 RCT는 이 6편 중 0편. 골질별 알고리듬(§7)에 코팅 화학 축을 아직 추가하지 않는 이유.

---

## 3. UV 광기능화 (Photofunctionalization)

### 3.1 기전과 효과

[확인 — Park 2025 narrative, Ogawa 2025 narrative, Hirota 2020 prospective]

| 효과 | 결과 | 출처 |
|---|---|---|
| 탄화수소 제거 | C/Ti 비율 정상화 → 양전하 회복 | Hayashi 2014 in-vitro |
| 친수성 | 초친수성 (접촉각 ~0°) | Park 2025 |
| 골유착 (Osseointegration) | BIC 유의 향상 | Yamada 2012 animal |
| 임상 ISQ | 복잡증례 +21.9 상승 | Hirota 2020 prospective |
| 세균 부착 | 생물막 형성 감소 (살균 효과는 없음) | Dorigatti 2015 in-vitro |
| 연조직 | 부착·치유 향상 | Park 2025 |

### 3.2 적응증 [확인]

- **위축골·복잡증례** — Hirota 2020에서 100% 7년 생존
- **D3/D4 골** — 친수성 표면군과 유사한 dip 제거
- **재근관치료 후 임플란트** — 치유 잠재력 보조
- **노화 임플란트 (보관 6개월 이상)** — 노화 역전

### 3.3 한계 [확인]

- **암절제 (Cancer Resection) 환자: 7년 22.2%** — UV-PF는 해부학적 손상만 보상, 병태생리적 손상 (방사선·항암) 불가
- VUV(진공자외선, 1분) 차세대 방법 등장 — 임상 근거 미성숙 (Park 2025)
- **임상 SR+MA는 등장(Lang 2022)했으나** 신뢰성 제한적 — pooled 효과는 OSI·2개월 안정성에서만 유의, 다른 시점·MBL은 비유의이며 I²≤99%·high RoB. 효과 방향은 일관되게 UV-PF 우세이나 정량적 확신은 아직 약함 → 표준화된 다기관 RCT 여전히 필요

---

## 4. 표면 거칠기 — 마이크로 vs 나노 vs 계층

| Confidence | 출처 | 결론 |
|---|---|---|
| **in-vivo** | [[implants/surface/hasegawa-2020-meso-micro-nano-rough-titanium-surface]] | **메조+마이크로+나노 계층형 표면 → 골유착 강도 마이크로 단독 대비 최대 향상**; 부착 손상 없음 |
| **in-vitro** | [[implants/surface/iwasa-2011-tio2-micro-nano-hybrid-biological-aging]] | TiO2 나노 + 마이크로 → 생체활성 7일 유지 (마이크로 단독 30–50% 감소 방지) |
| **animal** | [[implants/surface/yamada-2012-nanopolymorphic-hydroxyapatite-titanium-implant]] | 나노 HA → BIC·강도 향상, 효과 표면 50 µm 이내 |
| **sr (2025)** | [[implants/surface/serbanescu-2025-nanofeatured-titanium-surfaces-dental-implants]] | 나노구조 표면 25편 종합 SR — 21/25편이 초기(2-4주) 우위이나 **8-12주면 마이크로거칠기 대조군과 수렴**; GRADE 확신도 MBL/생존은 낮음~매우낮음 |

[확인] **계층형 (메조+마이크로+나노) 표면이 이론적 최적**. 임상 product (CA·SLActive·UltraGrip 등) 다수가 이 방향.

**지속성 단서 (2026-08 갱신)** [미검증]: Hasegawa 2020·Iwasa 2011·Yamada 2012는 전부 단일 연구(in-vivo/in-vitro/animal) 수준이라 장기 추적이 없다. Șerbănescu 2025(25편 종합 SR)는 나노구조의 **초기 가속 효과는 신뢰할 만하나 8-12주 이후 장기 우위는 미입증**이라는 첫 종합적 caveat을 제공한다. 즉 "계층형 표면이 이론적 최적"이라는 문장은 **초기 골유착 속도**에 대한 것이지, 장기 생존·MBL에 대한 우위 주장은 아직 아니다.

---

## 5. 골밀도화 (Osseodensification, OD) — 표면 아닌 술기

[확인]

| Confidence | 출처 | 결론 |
|---|---|---|
| **sr** | [[implants/osseodensification/fontes-pereira-2023-osseodensification-osteotomy-alternative-sr]] | OD: IT 일관 상승, ISQ 가변 우위, **D3/D4 골에서 효과 최대** |
| **sr+ma (TSFE)** | [[sinus-lift/transcrestal/starch-jensen-2025-transcrestal-sinus-osseodensification-meta-analysis]] | TSFE에서 OD ISQ 식립시·지대주연결시 유의 우위 |

**구분 주의** [미검증]: OD는 **표면 처리가 아니라 osteotomy 기법**. Densah burs로 시상 절삭 없이 골을 측방 압축. 표면처리와 보완 관계. 상세는 [[overviews/sinus-lift-technique-selection]] 참조.

---

## 6. Confidence 등급별 합성 매트릭스

| 임상 결정 | 강한 결론 (rct·prospective·retrospective) | 보조 (narrative·in-vitro·animal) | 미해결 |
|---|---|---|---|
| 거칠기 vs 머신드 (기초 비교) | **샌드블라스팅 실패율 1년 80%↓·5년 74%↓ (Czumbel 2019 SR+MA, 7RCT, I²=0%)** MBL은 동등 | 단독 모래분사는 BIC/RTV 비유의(Saini 2024 동물 SR+MA) — SLA/레이저/산부식/양극산화만 유의 | 샌드블라스팅+산부식(SLA) vs 샌드블라스팅 단독 직접 비교 인체 SR+MA |
| 표준 표면 선택 | SLA/SA: 8년 94.8% (Kim 2020); CA: 5.2년 97.3% (Kim 2022); **SLA≈SLActive 12개월 동등 (Vílchez 2025 RCT)** | SLActive·CA 임상 RCT 부족 | SLA·SLActive·CA 3자 동시 비교 SR+MA |
| D3/D4 골 표면 | **친수성·생체활성이 dip 제거** (Canullo 2024 prospective) | UV-PF가 ISQ +21.9 (Hirota 2020 prospective) | D3/D4 표면 비교 RCT |
| UV-PF 적응증 | 복잡증례 7년 100% (Hirota 2020); **OSI MD=+2.13 (Lang 2022 SR+MA)**; 당뇨 host RCT (Krishna 2025) | 노화 역전 기전 (Iwasa 2011 in-vitro); 표면 비의존 biofilm/연조직 SR (Komatsu 2026) | 표준화 다기관 RCT (절대 안정성·MBL pooled 비유의) |
| 표면 기전 핵심 | **탄화수소 제거 = 양전하 회복** (Hayashi 2014, Minamikawa 2016) | 친수성은 부차적 | 임상 효능 정량화 |
| 거칠기 최적 | 메조+마이크로+나노 계층 (Hasegawa 2020 in-vivo) | 나노 HA (Yamada 2012 animal); **나노는 8-12주면 수렴 (Șerbănescu 2025 SR)** | 인체 BIC 직접 측정, 장기 나노-대-마이크로 RCT |
| **TCP/HA 코팅 효능 (2026-08 정정)** | — | **비유의, HA는 14일 유의 열세 (Damerau 2021 SR+MA 15편)** — yamada-2012와 contradicts | 코팅 vs 거칠기 상대 기여도 분리 RCT |
| **Mg/Ag 코팅 효능 (2026-08 신규)** | — | Mg BIC 유의(Alenezi 2026, Z=4.38); Ag BIC 유의·약함(Alenezi 2025, Z=2.01) — 전부 동물 | 인체 RCT 전무 |
| 6주 부하 가능성 | 친수성 테이퍼 97.56% (Kim 2016 RCT) | 골질만 ISQ 예측 (RCT 결과) | D3/D4 부하 protocol |
| 세균 부착 감소 | UV-PF (Dorigatti 2015 in-vitro) | 임상 peri-implantitis 감소 효과 미확정 | 임상 RCT |
| **거칠기 vs 장기 peri-implantitis (2026-08 신규)** | 후향적 코호트: 거친 표면 peri-implantitis 오즈↑ (Ferrantino OR 4.877; Raes 5yr 12/42 vs 3/41, p<0.01, Dipalma 2026 SR 인용) | 환자·부위 위험요인이 표면 효과보다 우세 (Dipalma 2026) | 표면-vs-숙주요인 상대기여도 다기관 전향적 |
| **넥(Neck) 미세지형 (2026-08 신규)** | 거친 미세나사산/LMS 넥 → MBL·PD 유의 감소 (Huraib 2023 SR, 15편) | 1편은 매끄러운 넥에서 peri-implantitis 빈도 오히려 낮음(2.92% vs 14.41%) | 넥 디자인-peri-implantitis 장기 RCT |

---

## 7. 환자·골질별 표면 선택 알고리듬

```
환자 평가 → 골질 + 부위 + 위축도 + 전신상태
├─ D1/D2 골, 정상 부위, 건강
│   └─ SLA/SA 표준 — 8년 94% 충분
├─ D3 골 (상악 후방, 중등도 위축)
│   └─ CA / 친수성 → stability dip 제거, 6–8주 부하 가능
├─ D4 골 (상악 후방, 심한 위축)
│   ├─ CA / SLActive → 친수성 표면 우선
│   ├─ + OD (Densah) → 식립시 ISQ ~5–10 추가 상승
│   └─ 또는 + UV-PF → ISQ +21.9 가능, 위축골 100% 성공
├─ 암절제·방사선 환자
│   └─ UV-PF로도 불충분 (22.2%); 다학제 의사결정
└─ 노화 임플란트 (포장 6개월 이상)
    └─ UV-PF로 노화 역전 후 사용
```

[미검증] 한국 임상에서 Osstem CA는 5.2년 97.3% 근거 (n=258)로 가장 검증된 초친수성 옵션. UV-PF는 별도 장비 (Therabyte 등) 필요 — 비용·workflow 검토.

**2026-08 추가 고려사항** [미검증]: 위 알고리듬은 단기~중기(≤5년) 골유착·안정성 근거 기준이다. Dipalma 2026(§10)에 따르면 **장기(≥5년)에서는 거친 표면이 peri-implantitis 오즈를 높일 수 있어**, D3/D4에서 거친/친수성 표면을 선택할 때도 유지관리 프로토콜을 강화하는 것이 근거에 부합한다 — "거친 표면=초기 유리"와 "거친 표면=장기 위험 요인 중 하나"가 동시에 성립할 수 있음.

---

## 8. 임상 적용 한 페이지 요약

**표면처리 10대 원칙** (2026-08 갱신, 7→9→10) [확인]:

1. **SLA/SA가 기본 표준** — 8년 94% 생존 (Kim 2020)
2. **D3/D4 골은 친수성 표면** — Stability dip 제거 (Canullo 2024)
3. **친수성의 진짜 기전은 탄화수소 제거** — 노화 역전 (Hayashi 2014, Minamikawa 2016)
4. **UV-PF = 위축골 1순위** — 7년 100% (Hirota 2020); 단 SR+MA 부재
5. **OD는 표면 아닌 술기** — 친수성 표면과 보완 사용
6. **노화 임플란트 주의** — 보관 6개월 이상은 골유착 감소 가능, UV-PF로 회복
7. **암절제·방사선 환자** — 표면처리만으로 불충분
8. **CaP/HA 코팅은 "코팅했다고 좋아진다"가 아님 (2026-08 정정)** — 이미 거친 티타늄 대비 TCP/HA 코팅의 견고한 BIC 우위는 입증되지 않았고(Damerau 2021 SR+MA), Mg/Ag 등 신흥 금속 코팅이 오히려 더 강한 근거(p<0.05~<0.001)를 보임(§2.4) — 코팅 종류가 아니라 개별 메타분석 근거로 판단
9. **거친 표면의 장기 peri-implantitis 위험 고려** — 단기 골유착 이점과 장기(≥5년) peri-implantitis 오즈 증가가 같은 거칠기 축에서 공존할 수 있음(Dipalma 2026); 단 환자·부위 위험요인이 표면 효과보다 우세하므로 표면 선택보다 유지관리가 우선
10. **산화막과 오염막을 혼동하지 말 것 (2026-08 신규)** — 산화막(TiO₂)은 가공 즉시·영구적으로 형성되고 사라지지 않음; "노화"는 그 위에 쌓이는 별개의 오염막(소형 유기산, Wagstaffe 2019) 얘기임. UV/플라즈마가 벗겨내는 대상도 오염막뿐이며, **접촉각(습윤성) 개선만으로 탈오염이 됐다고 단정하면 안 됨** — 같은 SLA 배치에서 UVB는 접촉각만 낮추고 탄소는 그대로였다(Houshmand 2023). 기기 파장/스펙트럼을 확인하지 않은 "UV 처리했다"는 보고는 실제 탈오염 여부가 불확실할 수 있음

---

## 9. 임플란트 넥(Neck) 미세지형 — 몸체 표면과 별개 축 (2026-08 신규)

[확인 — Huraib 2023 SR, 15편 인체 대조연구]

지금까지 §2–§4는 임플란트 **몸체/나사산(body/thread) 표면** 기술이었다. [[implants/surface/huraib-2023-micro-threaded-laser-textured-implant-neck-peri-implant]]은 **넥(Neck, 치조정 부위 collar)**의 미세지형이라는 별개 축을 다룬다 — 이는 SLA/CA/UV-PF와 독립적으로 선택되는 디자인 변수다.

| 비교 | 결과 |
|---|---|
| 거친 미세나사산 넥 vs 매끄러운 머신드 넥 | 부하 후 MBL 0.12–3.25mm vs 0.38–3.75mm — **미세나사산 넥이 유의하게 낮음** |
| 레이저 미세조직화(LMS) 넥 vs 머신드 넥 | 3년 탐침깊이(PD) 2.3±0.7mm vs 3.8±0.8mm — LMS가 낮음; 치은퇴축은 양군 유사 |
| **내부 모순** [미검증] | 포함된 1편에서 **매끄러운 넥의 peri-implantitis 빈도가 오히려 낮음**(2.92% vs 14.41%, p<0.001) — MBL 개선과 감염 위험 감소가 항상 같이 가지 않음을 시사 |

**해석**: 넥 디자인은 몸체 표면 선택(§2 알고리듬)과 **별개로** 판단해야 한다. 미세나사산/LMS 넥은 MBL·PD 지표에서는 유리하나, 이것이 peri-implantitis 발생률 감소를 보장하지는 않는다 — §10의 "거칠기-감염위험 트레이드오프"와 같은 축의 문제. 메타분석은 이질성으로 시행되지 못했고(SR only), 추적기간은 대부분 12–24개월로 짧다(5년 이상 RCT 부재).

---

## 10. 표면 거칠기와 장기 Peri-Implantitis 위험 — 새로운 긴장 (2026-08 신규)

[확인 — Dipalma 2026 SR, 인체 비교연구 13편, PROSPERO #1301140]

이 overview는 §2–§4에서 **거칠기가 초기 골유착에 유리하다**는 근거를 반복 확인했다. [[implants/surface/dipalma-2026-implant-surface-characteristics-peri-implant-outcomes]]는 이 그림에 **장기 시간축**을 더한다 — 초기 골유착 이점이 장기 peri-implantitis 위험과 반드시 무관하지 않을 수 있다는 것이다.

- **단기~중기 RCT**: 표면 유형 간 MBL 차이는 미미함(Ko 2019, Vílchez 2025 1년; Guarnieri 2019 3년까지) — §2.2의 "SLA≈SLActive 동등" 결론과 일치.
- **장기 후향적 코호트**: 거친 표면이 peri-implantitis 오즈 증가와 연관 — Ferrantino 2022(630임플란트, ~13년): OR 4.877 (95% CI 1.701–13.980); Raes 2018(split-mouth RCT, 5년): 중등도 거친 TiUnite 12/42 vs 최소거친 turned 3/41 (p<0.01), 단 누적 생존율은 100% vs 97.6%로 turned가 오히려 낮음(생존과 peri-implantitis가 반대로 움직임).
- **결정적 조절변수**: 환자·부위 위험요인(흡연, 치주염력, 유지관리 순응도)이 표면 효과보다 우세(Hussain 2024, Gnanajothi 2024 인용) — 즉 "거친 표면이 원인"이 아니라 "거친 표면 + 위험요인 조합"이 문제.

**본 overview thesis에 대한 함의** [미검증]: §1–§4는 "거칠기·탄화수소제거·계층형 나노구조가 골유착에 유리하다"는 것을 확립했다. Dipalma 2026은 이를 **반박하지 않는다** — 초기 골유착과 장기 peri-implantitis 위험은 다른 시간축·다른 outcome이기 때문이다. 다만 임상 알고리듬(§7)에서 거친/친수성 표면을 선택할 때, 특히 흡연·치주염력이 있는 환자에서는 **유지관리 강화**가 표면 선택 자체보다 중요하다는 균형추를 더한다.

---

## Related Overviews

- [[overviews/isq-loading-threshold]] — 표면별 stability dip과 부하 결정
- [[overviews/sinus-lift-technique-selection]] — OD 술기 (표면처리 보완)
- [[overviews/immediate-implant-conditions]] — 즉시식립에서 표면 선택

## Wiki Coverage Caveat

추가 PDF 사냥 권장:
- ~~샌드블라스팅 vs 머신드 RCT SR+MA~~ → **확보됨 (Czumbel 2019, 7 RCT, I²=0%)**; ~~단독 모래분사 vs SLA 복합처리 동물 SR+MA~~ → **확보됨 (Saini 2024, 단독 모래분사는 BIC/RTV 비유의)**; 다음은 **동일 질문의 인체 SR+MA**
- ~~SLA vs SLActive 직접 비교 RCT~~ → **확보됨 (Vílchez 2025, 12개월 동등)**; 다음은 **SLA·SLActive·CA 3자 동시 비교 + 5년 이상** RCT
- ~~UV-PF 임상 SR+MA~~ → **확보됨 (Lang 2022)**; 다음은 표준화된 ISQ·MBL 측정의 **다기관 prospective RCT** (현 SR+MA는 I²≤99%·high RoB)
- ~~표면처리와 peri-implantitis 장기 발생률 연관 prospective~~ → **부분 확보됨 (Dipalma 2026 SR, 13편 인체 비교연구 — 후향적 코호트에서 거친 표면 오즈↑, 단 환자/부위 요인이 더 우세)**; 다음은 **표면-vs-숙주요인 상대기여도를 분리하는 다기관 전향적 코호트**
- **신규 갭 (2026-08)**: TCP/HA·Mg·Ag 코팅 전부 동물/전임상뿐 — **인체 RCT 전무**. 특히 Damerau 2021(TCP/HA 비유의~열세)과 yamada-2012(HA 우위)의 정면 상충을 해소할 **인체 데이터**가 가장 시급한 갭.
- **신규 갭 (2026-08)**: 생체분자(BMP·콜라겐) 코팅의 두 SR+MA(Alshayeb 2024 유의 vs López-Valverde 2022 비유의) 상충 해소 — 더 큰 표본·표준화된 후속 메타분석 필요.
- **신규 갭 (2026-08)**: 임플란트 넥(Huraib 2023) — MBL·PD 이점은 SR 수준 확보되었으나, 넥 미세지형과 peri-implantitis 발생률의 직접 관계 RCT는 여전히 부재.
- D3/D4 골 표면별 5년 이상 prospective
- 임플란트 노화 (저장 기간)와 임상 결과 RCT

## Related Papers

### 신규 추가 (2026-06)

- [[implants/surface/cochran-2002-reduced-healing-iti-sla-surface]] — reinforces: landmark prospective multicenter trial (n=110/326) establishing SLA reduced healing time (~6wk; class IV ~12wk) with 99.3% abutment-placement success and 99.1% 1–2yr life-table success — historical early-loading baseline for the SLA→SLActive→CA→UV-PF accelerated-loading timeline (prospective, 2002)
- [[implants/surface/bonfante-2012-calcium-phosphate-coatings-plasma-spray]] — reinforces: plasma-spray PSHA (71% crystalline HA) vs ACP (<1% HA) — BIC/BAFO statistically equivalent at 6+12 weeks despite large physicochemical differences; macrogeometry may dominate over CaP coating type (animal, 2012)
- [[implants/surface/witek-2020-boronized-surface-osseointegration]] — extends: boronized CP-Ti (BM, BAA) implants showed declining BIC/BAFO over 3→6 weeks vs increasing controls; osteoid demineralization adjacent to TiB/TiB₂ surface — cautionary evidence that superior mechanical properties do not guarantee osseointegration (animal, 2020)
- [[implants/surface/zhang-2025-dual-biofunctional-implant-coatings-in-vivo-sr]] — SR (English, Medline/Scopus/WoS, up to Dec 2024): 16편 in vivo (1 clinical 15 animal … (sr, 2025)
- [[implants/surface/jadhav-2026-dental-implant-surface-review]] — Narrative review of surface-modification methods (physical/chemical/mechanical), bio-functionalized surfaces, and emerging responsive coatings / 'omics / AI-guided directions (narrative-review, 2026)
- [[implants/surface/rehner-2025-dental-implants-nanoparticle-coatings-review]] — Narrative review: metal/metal-oxide, polymer, and bioceramic nanoparticle coatings enhance osseointegration + add antibacterial/anti-peri-implantitis action across in vitro/in vivo (narrative-review, 2025)

**갱신 메모 (2026-06-07)**: jadhav-2026·rehner-2025 두 narrative review는 본 overview의 표면처리 진화 축(SLA→SLActive→CA→UV-PF)에 **차세대 지평(나노입자 항균 코팅·responsive coating·AI 설계)**을 덧붙인다. 단 둘 다 narrative-review·전임상 중심이라 현 임상 권장(SLA 표준, 친수성 D3/D4, UV-PF 위축골)을 바꾸지 않음. [미검증] 나노입자 항균 코팅은 peri-implantitis 예방 맥락에서 추적 가치 있으나 임상 RCT 부재.

### 신규 추가 (2026-06-26) — 임상 근거 갭 충전

- [[implants/surface/lang-2022-photofunctionalization-implant-stability-marginal-bone-loss-sr-ma]] — reinforces: **첫 UV-PF 임상 SR+MA** (7편/734임플란트). OSI(골유착 속도) MD=+2.13(p=0.007)·2개월 안정성 MD=+3.48(p=0.04) 유의; 다른 시점·MBL pooled 비유의(I²≤99%, high RoB). 본 overview가 §3.3·§6·caveat에서 반복 명시한 "UV-PF SR+MA 부재"를 충전 (sr+ma, 2022)
- [[implants/isq/vilchez-2025-sla-slactive-split-mouth-rct]] — reinforces: **첫 SLA vs SLActive 직접 비교 split-mouth RCT** (n=68/136임플란트). ISQ 궤적·12개월 MBL(0.04 vs 0.07mm) 동등, 양군 생존 100%. "직접 비교 RCT 부재" 갭 충전 — 친수성의 임상 우위가 절대값이 아닌 D3/D4·가속부하 한정이라는 thesis 보강 (rct, 2025)
- [[implants/surface/komatsu-2026-uv-photofunctionalization-surface-agnostic-biofilm-soft-tissue-sr]] — extends: 최신·최광 UV-PF SR(34편). UV-PF = 표면형태 보존 "surface-agnostic positive-sum" 재활성화 — biofilm 억제 + 연조직 봉쇄(Ti 일관, Zr 신흥). zone별 토포그래피 선택 후 UV-PF로 각 구역 생물학 극대화 개념 (sr, 2026)
- [[implants/surface/krishna-2025-uv-photofunctionalization-diabetic-implant-stability-rct]] — extends: UV-PF 효과를 **조절 당뇨(대사적 손상 host)**로 확장한 split-mouth RCT — 3개월 ISQ·OSI·9개월 골소실 모두 유의 우위 (rct, 2025)
- [[implants/surface/farsiani-2025-photofunctionalized-implants-fractal-bone-analysis-rct]] — reinforces: UV-PF 처리부 임플란트 주위 해면골 프랙탈 차원 유의 상승(대조군 무변화) — 프랙탈 분석으로 PF 골 효과를 본 최초 인체 RCT (rct, 2025)
- [[implants/surface/ko-2024-hydroxyapatite-nano-coated-sla-immediate-implants]] — reinforces: 상악 구치부 즉시식립에서 HA 나노코팅 SLA가 무코팅 SLA 대비 ISQ 회복·volumetric 안정성 우위 경향 (rct, 2024)

### 신규 추가 (2026-06-28)

- [[implants/surface/czumbel-2019-sandblasting-implant-failure-rate-sr-ma]] — reinforces: **RCT 한정 첫 SR+MA** (7 RCT, 722임플란트, I²=0%) — 샌드블라스팅 표면이 머신드 대비 임플란트 실패율을 1년 RR=0.20(80%↓), 5년 RR=0.26(74%↓)로 감소; MBL은 동등. 본 overview의 "샌드블라스팅=거칠기 최소 기준" 포지션에 RCT-only 근거를 추가하며, **실패율과 MBL의 독립적 거동**이라는 핵심 인사이트를 확정 (sr+ma, 2019)

**갱신 메모 (2026-06-26)**: 이번 갱신의 핵심은 **본 overview가 명시했던 두 가지 "부재" 갭이 충전**된 것 — (1) UV-PF 임상 SR+MA(Lang 2022), (2) SLA vs SLActive 직접 비교 RCT(Vílchez 2025). 임상 권장 자체는 불변(SLA 표준·친수성 D3/D4·UV-PF 위축골)이나, **근거의 질이 한 단계 상승**했고 두 신규 근거 모두 thesis를 반박이 아닌 보강 방향으로 정렬한다: UV-PF는 "절대 안정성"이 아니라 "안정성 도달 속도(OSI)"를 높이고(Lang), SLActive는 SLA 대비 절대 우위가 아니라 특정 시나리오 한정(Vílchez). 남은 갭은 SLA·SLActive·CA **3자 동시 비교** 다기관 RCT.

### 신규 추가 (2026-08-07) — PMC 서베일런스, 코팅 화학·넥 디자인·장기 peri-implantitis 축 확장 + 오염 화학기전 (12편)

- [[implants/surface/damerau-2021-inorganic-surface-coatings-tcp-ha-periimplant]] — **refines (overview 정정)**: 대형동물 40편 SR + 15편 pooled MA — TCP/HA 코팅이 이미 거친 비코팅 티타늄 대비 견고한 BIC 우위 없음, HA는 14일에 오히려 유의하게 열세(−6.94%p, p=.001). 본 overview가 2026-06까지 bonfante-2012·yamada-2012에 기반해 유지해온 CaP/HA 코팅 우호적 서술을 **직접 정정**(yamada-2012와 `contradicts`) — §2.2·§2.4 신설 (sr+ma, 2021)
- [[implants/surface/dipalma-2026-implant-surface-characteristics-peri-implant-outcomes]] — **refines (갭 충전)**: 인체 비교연구 13편 SR — 단기 MBL은 표면 간 동등하나 장기 후향적 코호트는 거친 표면 peri-implantitis 오즈 증가와 연관(Ferrantino OR 4.877, Raes p<0.01), 단 환자·부위 위험요인이 표면보다 우세. 본 overview Wiki Coverage Caveat의 "peri-implantitis 장기 연관" 갭을 부분 충전 — §10 신설 (sr, 2026)
- [[implants/surface/saini-2024-bone-apposition-surface-modified-titanium-animal]] — **refines**: 동물 37편 SR+MA — SLA/레이저/산부식/양극산화는 BIC 유의 우수하나 **단독 모래분사는 BIC·RTV 모두 비유의**(SMD 9.44, p=0.65). 본 overview의 "샌드블라스팅=거칠기 최소 기준" 서술을 "SLA 이상 복합처리=최소 기준"으로 정밀화 (sr+ma, 2024)
- [[implants/surface/serbanescu-2025-nanofeatured-titanium-surfaces-dental-implants]] — **refines**: 나노구조 표면 종합 SR(25편) — 초기(2-4주) 우위는 21/25편에서 확인되나 8-12주면 마이크로거칠기와 수렴. §4 "계층형 표면 이론적 최적" 서술에 지속성 단서 추가 (sr, 2025)
- [[implants/surface/huraib-2023-micro-threaded-laser-textured-implant-neck-peri-implant]] — **extends (신규 축)**: 인체 대조연구 15편 SR — 거친 미세나사산/레이저 넥이 매끄러운 넥보다 MBL·PD 유의하게 낮음, 단 1편은 매끄러운 넥에서 peri-implantitis 빈도가 오히려 낮음(2.92% vs 14.41%). 몸체 표면(§2-4)과 별개인 **넥 미세지형** 축을 신설 — §9 신설 (sr, 2023)
- [[implants/surface/alshayeb-2024-bioactive-surface-modifications-dental-implants]] — 동물 9편 SR+MA — 생체활성(콜라겐·BMP-2) 코팅 BIC MD=7.29 유의 향상 (sr+ma, 2024)
- [[implants/surface/lopez-valverde-2022-biomolecule-based-bioactive-surfaces-osseointegration]] — 전임상 26편 SR+MA — 생체분자 코팅 BIC 비유의(I²=99%, 출판편향 소견) — alshayeb-2024와 상반 결론, §2.4 표에 병기 (sr+ma, 2022)
- [[implants/surface/alenezi-2026-magnesium-modified-titanium-implants-osseointegration]] — 전임상 11편 SR+MA — 마그네슘 코팅 BIC 유의 향상(Z=4.38, p<0.001), 코팅 화학 중 가장 강한 신호 (sr+ma, 2026)
- [[implants/surface/alenezi-2025-implant-silver-coatings-bone-formation]] — 동물 16편 SR+MA — 은 코팅 BIC 유의 향상(Z=2.01, p=0.04), 골 부피 무해 (sr+ma, 2025)
- [[implants/surface/matys-2025-osseointegration-zirconia-implants-calcium-phosphate]] — 27편 SR — 지르코니아 임플란트 CaP 코팅, bonfante-2012(티타늄)과 대비되는 기질-의존적 코팅 효과 패턴; `extends → bonfante-2012` (sr, 2025)
- [[implants/surface/wagstaffe-2019-rgd-tripeptide-adsorption-titania-surfaces]] — **extends (기전 확장)**: XPS/STM — §1의 "탄화수소"가 화학적으로 무엇인지 처음 특정(폼산·아세트산 등 소형 유기산, 카르복실기-양이온 브리징); 산화막(TiO₂, 영구)과 오염막(부착탄소, 시간의존)이 별개 층임을 명확히 함; SLActive의 얇은 오염막 → 전 pH RGD 흡수↑ (in-vitro, 2019)
- [[implants/surface/houshmand-2023-uv-photofunctionalization-sla-titanium-disks]] — **extends (기전 확장)**: EDS, 같은 SLA 배치 UVC/UVB 직접비교 — UVC는 탄소·질소 유의 감소(p<0.001), UVB는 접촉각만 개선하고 탄소·질소 무변화(p=0.171/0.785) — **습윤성 개선 ≠ 탈오염 증명**, 파장 의존적 (in-vitro, 2023)

### 신규 추가 (2026-08-09)

- [[implants/surface/trisi-2003-bone-implant-contact-machined-dual-acid-etched]] — reinforces: 인체 split-surface 조직계측학(n=11, 후상악) — 이중 산부식 BIC 47.81% vs 기계가공 19.00%, 2개월만에 유의차(P<0.001), 저밀도골에서 격차 더 확대. czumbel-2019(실패율 SR+MA)보다 앞선 초기 인체 BIC 데이터 — 거친 표면 우위 방향의 역사적 앵커; abstract-only ingest (prospective, 2003)

**갱신 메모 (2026-08-07)**: 이번 갱신은 이전 두 갱신(UV-PF·SLA-SLActive 갭 충전)과 성격이 다르다 — **처음으로 본 overview의 기존 결론 하나(CaP/HA 코팅의 BIC 이점)를 정정**했다(Damerau 2021). 나머지 11편은 (a) 코팅 화학 축 확장(Mg·Ag·생체분자, §2.4 신설), (b) 넥 디자인이라는 신규 독립 축(§9 신설), (c) 장기 peri-implantitis-거칠기 트레이드오프(§10 신설), (d) 기존 결론의 정밀화(샌드블라스팅 단독 vs SLA, 나노구조 지속성), (e) §1 기전의 화학적 심화(Wagstaffe·Houshmand — 산화막/오염막 구분, 파장 의존성)로 분류된다. 핵심 thesis(탄화수소 제거=기전, 거칠기가 코팅 화학보다 지배적)는 오히려 **강화**됐다 — Damerau의 "코팅보다 기준 표면 거칠기가 우선"이라는 결론이 §1의 탄화수소/양전하 기전론과 정합적이기 때문. 남은 최대 갭: TCP/HA·Mg·Ag 코팅 전부 **인체 RCT 부재**.
