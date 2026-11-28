---
title: "음주 × 발치·임플란트 — chairside 위험 도구"
type: agenda
date: 2026-11-19
status: done
owner: 원장
priority: P1
tags: [alcohol, ethanol, heavy-drinking, implant-failure, peri-implantitis, liver-cirrhosis, bleeding, alcohol-withdrawal, dry-socket, decision-tool]
source_wiki:
  - wiki/overviews/alcohol-extraction-implant-surgery-risk-overview.md
  - wiki/implants/survival/boroomand-2026-alcohol-consumption-dental-implant-failure-sr-ma.md
  - wiki/implants/peri-implantitis/galarraga-vinueza-2025-peri-implant-disease-risk-factors.md
  - wiki/implants/survival/bhatia-2024-alcohol-consumption-implant-success-retrospective.md
  - wiki/implants/survival/da-rocha-coelho-2021-evaluation-of-the-association.md
  - wiki/implants/survival/de-deco-2015-extended-alcohol-intake-osseointegration-rats.md
  - wiki/implants/survival/doring-2025-postoperative-abstinence-restores-osseointegration.md
  - wiki/oral-surgery/rech-2021-bleeding-oral-surgery-liver-cirrhosis-sr.md
  - wiki/oral-surgery/medina-2018-bleeding-dental-extractions-liver-cirrhosis.md
  - wiki/oral-surgery/fenelon-2023-osteomyelitis-jaw-major-complications-risk-factors.md
  - wiki/drug/systemic-disease/desai-2023-alcohol-withdrawal-syndrome-head-neck-cancer.md
output:
  - interactives/2026-11-19_alcohol-extraction-implant-decision-tool.html
---

# Goal

음주 환자의 발치·임플란트 수술에서 **무엇을 물어야 하고, 무엇을 말해도 되고, 무엇을 말하면 안 되는지**를 chairside에서 30초 안에 정리해 주는 도구. 대상은 원장·위생사. 근거는 2026-11-19 인제스트한 음주 10편(메타분석 3·후향 3·동물 2·SR 1·논평 1)이며, 이 도구의 1차 목적은 위험 계산이 아니라 **근거가 멈추는 지점을 눈에 보이게 하는 것**이다.

# Input

- wiki/overviews/alcohol-extraction-implant-surgery-risk-overview.md — 종합(질문·결론·결정 사다리·근거 공백)
- wiki/implants/survival/boroomand-2026-…-sr-ma.md — 용량 층별 실패 OR (0.40 / 0.87 / 2.78)
- wiki/implants/peri-implantitis/galarraga-vinueza-2025-peri-implant-disease-risk-factors.md — 주위염 OR 2.07 (1.49–2.85)
- wiki/implants/survival/bhatia-2024-…-retrospective.md — 11.5% vs 46.2% 절대 발생률
- wiki/implants/survival/da-rocha-coelho-2021-…md — 반대 신호(이진 변수, P ≥ .12)
- wiki/implants/survival/de-deco-2015-…rats.md — BIC vs 노출 기간
- wiki/implants/survival/doring-2025-…md — 수술 시점 금주 = 회복 (정형외과 모델)
- wiki/oral-surgery/rech-2021-…sr.md — 간경변 출혈 0–8.9%
- wiki/oral-surgery/medina-2018-…md — 190내원/333치아, 혈소판 P=0.026, R²=0.16
- wiki/oral-surgery/fenelon-2023-…md — 골수염 주요합병증 41.2% vs 10.8%
- wiki/drug/systemic-disease/desai-2023-…md — 금단 = 수술 위험

# Output

- interactives/2026-11-19_alcohol-extraction-implant-decision-tool.html
- wiki/overviews/alcohol-extraction-implant-surgery-risk-overview.md (§10 chairside tool 절 추가 + 도구 백링크)

# Done Criteria

- [x] 음주 패턴 5단계 입력 → 결과 카드 재구성 (골유착·주위염·출혈·감염·금단·건성발치와)
- [x] 용량-반응 막대(동일 outcome 3층: 0.40 / 0.87 / 2.78) + 기준선 1.0
- [x] 간경변 맥락에서 혈소판·INR 입력 → 보유 근거 범위 안/밖 판정 (수치 날조 없이 경계만)
- [x] "말할 수 있는 것 / 말할 수 없는 것" 2단 패널 (건성발치와 공백 포함)
- [x] 환자 상담 스크립트 자동 구성 (저용량 보호효과 금지 문구 고정)
- [x] 근거 표 10행 — 각 논문 설계·수치·한계
- [x] 라이트 고정(다크 블록 없음) + 캐시 버전 JS
- [x] frontmatter에 source_wiki + agenda 백링크
- [x] overview §10에서 도구 링크, 도구에서 overview 링크 (양방향)

# Notes / Decisions

- 2026-11-19: **계산기가 아니라 판독기로 설계.** 보유 근거에 g/day 문턱값이 없으므로(10편 모두 결측) 숫자 위험점수를 만들면 Rule #1 위반. 대신 "근거 범위 안/밖"만 표시.
- 2026-11-19: 음주 패턴 라벨은 논문의 층(light/moderate/heavy)을 그대로 옮기고, 단위·컷오프는 화면에 명시하지 않음 — 원 연구들도 서로 다른 정의를 쓴다.
- 2026-11-19: INR 3–4는 Rech SR 범위 안이지만 Medina 코호트 기준(INR<3) 밖 → "경계" 등급으로 분리.
- 2026-11-19: 색인 카테고리는 `systemic-disease` (형제 도구인 흡연 상담기와 동일 버킷, 인덱스 taxonomy 축).
- 2026-11-19: 같은 날 만들어진 `2026-11-19_smoking-tobacco-risk-counselor.html`이 agenda 백링크 없이 커밋되어 `operations-lint.py`가 error 1건을 낸다(본 작업과 무관, 별도 처리 필요).

# References

- [[overviews/alcohol-extraction-implant-surgery-risk-overview]]
- [[agenda/2026-11-05_uv-plasma-wavelength-comparison-interactives]]
