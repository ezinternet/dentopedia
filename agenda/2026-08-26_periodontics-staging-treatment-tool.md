---
title: "치주 Stage·Grade 판정 + 치료강도 결정 도구"
type: agenda
date: 2026-08-26
status: in-progress
owner: 원장
priority: P0
tags: [periodontics, staging, grading, srp, spt, decision-ladder, chairside]
source_wiki:
  - wiki/overviews/periodontics-treatment-ladder.md
  - wiki/periodontics/papapanou-2018-periodontitis-classification-consensus-2017.md
  - wiki/periodontics/kwon-2021-current-concepts-management-periodontitis.md
  - wiki/periodontics/sanz-2020-treatment-stage-i-iii-periodontitis-efp.md
  - wiki/periodontics/herrera-2022-treatment-stage-iv-periodontitis-efp.md
  - wiki/periodontics/non-surgical-instrumentation/smiley-2015-nonsurgical-periodontitis-srp-guideline.md
---

# Goal

`periodontics-treatment-ladder`(inbound 30, uncovered 3위)를 체어사이드 도구로 전환한다.

# 형태 판단 — 앞의 둘과 또 다르다

| | ISQ ladder | 즉시식립 ladder | **치주 ladder** |
|---|---|---|---|
| 성격 | spine·지도 | 실행 문서 | **실행 문서 (10축 + Thread 3)** |
| 기존 도구 | 5개 (조각 촘촘) | 2개 (좁음) | **10개 (일부 축 이미 커버)** |
| 결론 | 허브 | 5축 순차 도구 | **입구 + 미커버 축 실행** |

치주는 이미 임상 도구가 10개다. 대조하면 **축6(치주성형)·축6c(시멘트질 열개)·GBT/바이오필름은 이미 전용 도구가 있고**, 축7(peri-implantitis)은 오버뷰 스스로 `implants-clinical-decision-ladder`에 위임한다.

비어 있는 것은 **입구 자체** — 2017 Stage/Grade 판정과, 거기서 갈라지는 치료 강도·SPT 주기다. 치주의 모든 결정이 여기서 시작하는데 어떤 도구도 이걸 다루지 않는다.

# ⚠ 근거 공백 — 이 작업의 핵심 제약

위키가 보유한 것 [확인]:
- **Stage CAL 기준** — I: 1–2mm · II: 3–4mm · III/IV: ≥5mm + 복잡성 증가 (`kwon-2021`)
- **복잡성 차원** — 치근이개부·동요도·수직골소실·치조제 결손 (`papapanou-2018`)
- **Stage IV 판별** — 치주염 기인 발치로 인한 저작기능 장애 (`papapanou-2018`)
- **Grade 상향 인자** — 흡연 ≥10개비/일 또는 HbA1c ≥7.0% (`kwon-2021`)

위키가 **보유하지 않은 것**:
- 방사선 골소실 % 임계 (<15 / 15–33 / ≥33)
- 치아 상실 개수 임계 (≤4 / ≥5)
- Grade A/B/C 진행속도의 수치 정의 (%골소실/연령 등)

→ **지어내지 않는다.** 보유분으로 Stage/Grade를 *제안*하고, 미보유 축은 도구 안에서 명시적으로 "위키 미보유 — 술자 판정"으로 표시한다. 이 공백 자체가 인제스트 후보다.

# Output

- `interactives/2026-08-26_periodontics-staging-treatment-tool.html`

# Done Criteria

- [ ] **Stage 제안** — 최대 CAL + 복잡성 인자 + Stage IV 저작기능 기준
- [ ] **Grade 제안** — 흡연 ≥10개비/일 · HbA1c ≥7.0% 상향 인자
- [ ] **미보유 기준 명시** — RBL%·치아상실 개수·진행속도 수치는 "술자 판정" 표시
- [ ] **Stage×Grade → 치료 강도 + SPT 주기** (오버뷰 축1 임상적용)
- [ ] 축2 비외과 사다리 (Stage별 5단계) + SRP 효과크기 + 항생제 제한(EFP S3: stage III grade C/D)
- [ ] 축3 외과·재생 (잔존 PPD ≥6mm 분기, furcation class별, 치주염력 임플란트 4.8배)
- [ ] 축5 SPT 주기 6단계 (Cho 2018 1개월 재교육 포함)
- [ ] 축6b STA 침범 — "일률적 2mm 규칙 금지"
- [ ] Thread A(전신질환) · B(endo-perio 감별) · C(치주성형) 시나리오
- [ ] 기존 도구 라우팅 (치주성형·시멘트질 열개·GBT·GCF)

# Notes / Decisions

- 2026-08-26: **staging 계산기를 "판정기"가 아니라 "제안기"로 만든다.** 위키가 CAL 축만 보유하므로 Stage를 확정할 수 없다. 확정처럼 출력하면 없는 근거를 만들어내는 것이다.
- 2026-08-26: `smiley-2015`에 이미 **대체 배너**가 있다 — "2020 EFP S3가 전신 항생제를 stage III grade C/D로 제한". 도구는 옛 광범위 권고가 아니라 배너의 제한 기준을 따른다.
- 2026-08-26: 축7은 오버뷰가 implants ladder로 위임하므로 도구에서도 다루지 않고 그 사실만 표시한다.

# References

- [[agenda/2026-08-26_isq-stability-ladder-chairside-hub]] · [[agenda/2026-08-26_immediate-implant-decision-tool]] — 형태가 매번 갈리는 대조군
