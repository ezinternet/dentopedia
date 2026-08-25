---
title: "환자용 진통제 설명 도구 — 발치 후 통증 · 치통 잠정관리"
type: agenda
date: 2026-08-25
status: in-progress
owner: 원장
priority: P1
tags: [patient-education, analgesics, acute-dental-pain, consent, chairside, korean]
source_wiki:
  - wiki/drug/analgesics/ada-2024-respite-patient-guide-tooth-removed.md
  - wiki/drug/analgesics/ada-2024-respite-patient-guide-toothache.md
  - wiki/drug/analgesics/carrasco-labra-2024-pharmacologic-management-acute-dental-pain-guideline.md
  - wiki/drug/analgesics/miroshnychenko-2023-dental-extraction-pain-network-meta.md
  - wiki/drug/analgesics/miroshnychenko-2023-corticosteroids-third-molar-acute-pain-sr-ma.md
---

# Goal

발치 후 통증·치통 환자에게 **체어사이드에서 즉시 열어 같이 보고, 필요하면 인쇄해 손에 쥐여 줄 수 있는** 한국어 진통제 설명 도구를 만든다. 근거는 ADA 2024 급성치통 지침, 표현 방식은 같은 프로젝트의 환자용 RESPITE 유인물에서 가져오되, 국내 맥락으로 현지화한다.

기존 도구 2개는 모두 **술자용**이고 환자용은 비어 있었다 — `2026-07-22_prescription-master-reference.html`(처방 마스터), `2026-08-24_ada-acute-dental-pain-chairside-guide.html`(ADA 결정 도구).

# Input

- `wiki/drug/analgesics/ada-2024-respite-patient-guide-tooth-removed.md` — 환자용 표현 설계의 출처: 0–10 통증척도, 회복일 타임라인, 진통 지속시간 막대, 그림 부작용
- `wiki/drug/analgesics/ada-2024-respite-patient-guide-toothache.md` — 치통 판본: "확정치료 전까지" 프레이밍, 벤조카인 도포
- `wiki/drug/analgesics/carrasco-labra-2024-pharmacologic-management-acute-dental-pain-guideline.md` — 모(母)지침. **모든 임상 수치의 인용처는 여기**
- `wiki/drug/analgesics/miroshnychenko-2023-dental-extraction-pain-network-meta.md` — NMA(82 RCT, n=9,095): 이부프로펜+아세트아미노펜 최상위, 오피오이드는 위약 수준
- `wiki/drug/analgesics/miroshnychenko-2023-corticosteroids-third-molar-acute-pain-sr-ma.md` — 스테로이드가 이 사다리에 없는 이유
- `interactives/2026-07-22_prescription-master-reference.html` — 이 진료실의 기존 입장: "Opioid(Oxycodone·Codeine·Tramadol)는 Network MA에서 위약과 동등 — 처방 정당화 어려움"

# Output

- `interactives/2026-08-25_patient-analgesic-explanation-guide.html` — 단일 파일, 한국어, 환자 대면용

# Done Criteria

- [ ] 시나리오 2종(발치 후 / 치통) 분기, 환자가 자기 상황을 고르게
- [ ] 0–10 통증 자가보고 입력 → 해당 구간의 약 조합 제시
- [ ] 약 카드에 1회 용량·1일 최대·예상 지속시간·주의 표기 (지침 수치 그대로)
- [ ] **아세트아미노펜 1일 총량 경고를 독립 배치** — 복합제 중복 복용이 실제 위해 경로
- [ ] NSAID 금기 분기 (위장관·신장·항응고제 등) → 아세트아미노펜 단독 경로
- [ ] 회복일 타임라인 (발치 후) / "확정치료 전까지" 프레이밍 (치통)
- [ ] **바로 연락해야 하는 신호** 목록
- [ ] 인쇄용 레이아웃 (`@media print`) — 화면 조작 요소 숨기고 환자가 가져갈 요약만 출력
- [ ] 라이트 배경 고정, 큰 글씨 — 고령 환자 가독성
- [ ] frontmatter에 `agenda:` 백링크 + `source_wiki:`

# Notes / Decisions

- 2026-08-25: **오피오이드 단계를 환자 화면에 넣지 않기로 결정.** RESPITE 원본에는 옥시코돈·하이드로코돈 분할정 단계가 있으나 (a) 미국 시장 맥락이고 (b) 이 진료실의 처방 마스터가 이미 "위약과 동등 — 처방 정당화 어려움"을 근거와 함께 못박았다. 환자용 화면에 실으면 환자가 요구할 근거를 우리가 만들어주는 셈이다. 대신 "1차 요법으로 조절이 안 되면 **약을 더 올리지 말고 연락**" 경로로 대체한다.
- 2026-08-25: **국내 OTC 제품명·규격은 쓰지 않는다.** 위키에 국내 시판 규격·허가사항 근거가 없다 (Rule #4). 지침 용량(이부프로펜 400mg 등)만 제시하고, 실제 조제품은 술자가 채우는 칸으로 남긴다.
- 2026-08-25: 코르티코스테로이드는 환자 화면에서 **아예 뺀다.** 권고 1.5가 진통 목적 추가에 반대이고, 환자에게 선택지로 보이면 안 된다. 근거·논쟁은 술자용 도구(`2026-08-24_ada-acute-dental-pain-chairside-guide.html`)의 전용 탭에 있다.
- 2026-08-25: 통증 점수는 **약을 자동 결정하지 않는다.** 0–10은 환자 자가보고를 여는 장치이고, 지침 사다리는 통증 점수가 아니라 시술 유형·금기로 갈린다. 점수는 "지금 어디쯤인지 같이 보기" 용도로 쓰고 그렇게 명시한다.

# References

- `INGEST.md` — RESPITE 2종 인제스트 (no-DOI, 제목 기반 dedup)
- `OPERATIONS.md` §1 routing, §3 frontmatter cross-link
- [[agenda/2026-08-24_ada-acute-dental-pain-guideline-interactive]] — 술자용 짝
