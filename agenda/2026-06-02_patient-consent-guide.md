---
title: "환자 설명 가이드 v1.2 — wiki 논문 근거 연결"
type: agenda
date: 2026-06-02
status: in-progress
owner: 원장
priority: P1
tags: [patient-communication, hygienist-tool, consent, evidence-grounding, chairside]
source_wiki:
  - wiki/bone-regeneration/couso-queiruga-2021-post-extraction-dimensional-changes-systematic.md
  - wiki/implants/fan-2024-smoking-early-implant-failure-sr-ma.md
  - wiki/drug/al-ansari-2022-diabetes-mellitus-dental-implants-sr-ma.md
  - wiki/oral-surgery/camps-font-2024-antibiotic-prophylaxis-dry-socket-nma.md
  - wiki/drug/feldman-2024-nonopioid-opioid-third-molar-rct.md
  - wiki/drug/gaballah-2025-ibuprofen-paracetamol-concurrent-alternate-rct.md
  - wiki/behavioral-dentistry/communication-relationship/elwyn-2025-shared-decision-making-primer-clinicians.md
output_wiki:
  - interactives/2026-06-02_patient-consent-guide.html
---

# Goal

기존 위생사·원장 협업형 환자 설명 가이드(v1.1, 6개 술식 탭)의 임상 데이터표·반론카드·확신도 태그를 wiki 실증 논문(저자·연도·DOI·[[wikilink]])으로 근거 연결하고, 각 탭에 wiki에만 있는 신규 정량 표·반론카드를 추가해 chairside 설득 자료의 추적성을 확보한다. THE FOUR RULES 준수 — 모든 근거는 wiki/sources 내부 논문에서만 인용(웹검색 금지).

# Input

- wiki/bone-regeneration/couso-queiruga-2021-... — 발치 후 치조제 흡수 SR+MA 정량 anchor (비구치 수평 2.73mm, 구치 3.61mm)
- wiki/bone-regeneration/araujo-2005-... — 2단계 흡수 기전(동물)
- wiki/immediate-implant/chappuis-2013-... — 심미부 박벽(≤1mm) 수직소실 7.5mm
- wiki/bone-regeneration/atieh-2015-... — ARP Cochrane(height MD -2.60, width -1.97)
- wiki/implants/fan-2024-smoking-early-implant-failure-sr-ma — 흡연 OR 2.59
- wiki/drug/al-ansari-2022-diabetes-mellitus-dental-implants-sr-ma — 당뇨 OR 1.78 (T1DM 4.48)
- wiki/drug/baghalipour-2025-mronj-... — MRONJ 4단계 예방
- wiki/oral-surgery/camps-font-2024-... — 발치 항생제 NMA(dry socket NNT 25)
- wiki/oral-surgery/guardieiro-2023-..., dinkova-2025-... — DAPT 지혈, TXA 함수
- wiki/oral-surgery/feldman-2024-..., gaballah-2025-..., costa-2015-... — 진통 RCT/메타
- wiki/oral-surgery/cervera-espert-2016-... — coronectomy IAN 보존
- wiki/oral-surgery/hajibagheri-2025-... — PRF alveolar osteitis 감소
- wiki/endodontics/duncan-2019-..., fasoulas-2023-..., di-spirito-2022-..., dogramaci-2023-...
- wiki/prosthetic-materials/aljomard-2022-..., almashaan-2023-..., gseibat-2025-..., ali-2023-..., habibzadeh-2024-...
- wiki/periodontics/farooqi-2015-..., caggiano-2022-..., arunyanak-2024-...
- wiki/drug/catella-lawson-2001-..., gomes-2025-..., becker-2012-..., colibasanu-2025-..., bazsefidpay-2023-...
- wiki/behavioral-dentistry/elwyn-2025-..., choi-2024-..., cartes-velasquez-2024-..., dawood-2025-...

# Output

- interactives/2026-06-02_patient-consent-guide.html — v1.2 본 가이드 (frontmatter에 agenda 백링크)

# Done Criteria

- [ ] 6개 탭 + 방법론 프레임에 wiki 논문 근거 연결 (저자·연도·DOI)
- [ ] 각 탭 신규 정량 표 또는 반론카드 ≥1개 (wiki 기반)
- [ ] 전역 References 섹션 (탭별 그룹, [[wikilink]] + DOI)
- [ ] 확신도 태그 재검토 — 직접 논문 없는 claim(예: 당뇨-치주 양방향, teach-back 효과)은 합의수준/claude해석으로 정직하게 하향
- [ ] frontmatter source_wiki / agenda 백링크 박힘
- [ ] operations-lint.py 통과, 인용 [[wikilink]] 실존 검증

# Notes / Decisions

- 2026-06-02: 깊이 = "근거 보강 + 신규 표/카드". 신규 술식 탭(상악동·즉시식립 등)은 이번 범위 제외(v2.0 후보).
- 2026-06-02: 당뇨-치주 양방향 직접 SR이 wiki에 없음 → [근거강함]→[합의수준] 하향, implant 측은 al-ansari-2022로 anchor.
- 2026-06-02: teach-back 전용 RCT가 wiki에 없음 → [근거강함]→[claude해석] 하향, SDM은 elwyn-2025로 anchor.
- 2026-06-02: 진통 핵심 정정 — gaballah-2025 RCT는 ibuprofen/APAP "번갈아(alternate)"가 "동시(concurrent)"보다 우월. 기존 가이드 "번갈아" 권고와 일치, 정량 근거 추가.
- 2026-06-02 (v1.3, 사용자 피드백): 화면 내 인용·출처·하단 References를 전부 제거 요청. 근거 추적은 frontmatter source_wiki(비가시)로만 유지. 대신 내용 보강 방향으로 전환 — '상담·설득' 탭 신설(라포·MI OARS·SDM 3-talk·저항·비용·기대관리·불안·노쇼). 기존 표는 '환자에게 어떻게 말하나' 중심으로 재구성. 교훈: 이 산출물의 1차 독자는 chairside 위생사이며, 학술 인용 노출은 비선호 — 향후 환자/위생사 배포물은 근거를 메타로 숨기고 본문은 행동지향.

# References

- [[agenda/2026-05-25_q2-clinic-sop-dbbm-isq]] — chairside 산출물 frontmatter 규약 선례
