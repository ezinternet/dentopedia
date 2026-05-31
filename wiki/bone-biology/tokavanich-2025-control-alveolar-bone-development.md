---
title: "Control of alveolar bone development, homeostasis, and socket healing by salt-inducible kinases"
authors: Nicha Tokavanich, Byron Chan, Katelyn Strauss, Christian D. Castro Andrade, Yuki Arai, Mizuki Nagata, Marc Foretz, Daniel J. Brooks, Noriaki Ono, Wanida Ono, Marc N. Wein
year: 2025
date: 2025-03-09
doi: 10.1093/jbmr/zjaf038
source: tokavanich-2025-control-alveolar-bone-development.md
category: [bone-biology]
confidence: animal
pdf_path: /Users/oracleneo/llm-wiki/papers/tokavanich-2025-control-alveolar-bone-development.pdf
pdf_filename: tokavanich-2025-control-alveolar-bone-development.pdf
source_collection: external
tags: [animal-study, mouse, SIK, PTH-PTHrP, alveolar-bone, socket-healing, scRNA-seq]
---

## One-line Summary
J Bone Miner Res mouse study showing conditional deletion of SIK2/SIK3 — kinases downstream of PTH/PTHrP signaling — impairs alveolar bone osteoblast maturation, BV/TV, and post-extraction socket healing, suggesting SIK inhibitors as candidate pharmacological adjuncts for alveolar bone regeneration.

## 한줄요약
J Bone Miner Res 마우스 연구 — PTH/PTHrP 신호 하류 kinase인 SIK2/SIK3을 조건 결손시키면 치조골 osteoblast 성숙·BV/TV·발치와 치유가 모두 저하; SIK 억제제가 치조골 재생의 새 표적이 될 가능성을 제시.

## Summary
Wein lab(MGH/Harvard)이 long bone에서 정립한 PTH–SIK 축을 처음으로 치조골 맥락에 적용한 in vivo 연구. Ubiquitin-CreERt2로 SIK2/SIK3을 조건 결손한 마우스에서 (1) 치조골 발달 결함, (2) 상악 제1대구치 발치 후 socket healing 지연, (3) microCT로 BV/TV 감소가 모두 확인됨. scRNA-seq로 P21 femur와 P25 alveolar bone의 osteoblast cluster를 비교, 두 부위가 동일하지 않은 osteoblast 아형으로 구성됨을 보임. 임상 의미는 직접적이지 않으나, **SIK 억제제(YKL-05-099 등) 또는 PTH 유도체가 ARP/socket 치유의 약리적 보조요법 후보**가 될 수 있다는 preclinical rationale 제공.

## Key Contributions
- 치조골 특이적 SIK 기능 입증 — 기존 SIK 연구는 사지골 중심.
- 발치 후 socket healing이 SIK 결손으로 지연됨을 in vivo로 시연.
- scRNA-seq로 alveolar bone osteoblast가 long bone osteoblast와 다른 cluster임을 정량.
- 치아 발달은 정상 → 치조골 결함이 치아 secondary 효과가 아님 (cell-intrinsic alveolar bone biology).

## Methodology
- 마우스 모델: Ubiquitin-CreERt2 × SIK2/SIK3 floxed (tamoxifen 유도).
- 발치: 양측 상악 제1대구치, isoflurane 마취, 3–4주 후 희생.
- 조직학: H&E, DAPI, TRAP(파골세포), ALP(조골세포).
- RNAscope in situ hybridization.
- MicroCT: 알베올라 BV/TV(%), BMD, threshold 550 mg HA/cm³.
- scRNA-seq integration: GEO GSM5623768(P21 femur) + GSM5140554(P25 alveolar) Seurat+Harmony; Wilcoxon DEG.

## Results
- SIK2/SIK3 결손 → osteoblast 성숙 저하, BV/TV 감소.
- 발치 후 socket healing 지연.
- 치아 표현형 정상 (alveolar bone 결함이 치아 secondary 아님).
- scRNA-seq: alveolar bone osteoblast cluster가 long bone과 구별되는 marker 발현.
- 저자 인정: 전신 mineral metabolism(경도 hypercalcemia, 1,25-vitD 상승)이 confounder일 가능성 — cell-type-specific Cre(Six2-Cre 등) 후속 연구 제안.

## Clinical Implications (preclinical)
- 직접 임상 적용 단계 아님.
- SIK 억제제 또는 intermittent PTH 유도체가 ARP/socket healing 가속제로 개발될 가능성 — 임플란트 식립 timeline 단축 시나리오.
- 치조골 osteoblast가 long bone osteoblast와 다른 cluster라는 점은, **장골 대상 골다공증 약물(bisphosphonate, denosumab)의 치조골 반응이 다를 수 있음**을 시사 — 이미 알려진 MRONJ 병태생리와 결이 맞음.
- Kondo 2022의 oral-barrier osteoclast 가설과 Tokavanich의 alveolar-specific osteoblast biology를 합치면 "치조골은 별개의 골생물학 단위"라는 통합적 framing이 가능.

## Limitations (Living-document note)
- 전신 conditional deletion → cell-intrinsic vs systemic 분리 불완전.
- 마우스 → 인간 translation 미검증.
- SIK 억제제의 치조골 약리학 미시험.
- Long-term(>4주) socket outcome 미평가.
- 임상 결정에 직접 반영 불가, 그러나 약리적 ARP 보조요법 개발 흐름의 기초 데이터 (claude해석).

## Related Papers
- [[bone-biology/kondo-2022-current-perspectives-residual-ridge]] — 같은 시기 치조골 외측면 osteoclast 기전.
- [[bone-regeneration/cardaropoli-2003-bone-tissue-formation-extraction]] — 본 연구가 분자수준으로 설명하려는 socket healing 시간표.
- [[bone-regeneration/araujo-2005-dimensional-ridge-alterations-tooth-extraction]] — 마우스 모델이 재현하는 phenotype.
- [[drug/]] — MRONJ 관련 페이지(향후 cross-link).
