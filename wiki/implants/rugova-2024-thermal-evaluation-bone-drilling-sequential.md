---
title: "Thermal Evaluation of Bone Drilling: Assessing Drill Bits and Sequential Drilling"
authors: Sihana Rugova, Marcus Abboud
year: 2024
date: 2024-09-16
doi: 10.3390/bioengineering11090928
source: rugova-2024-thermal-evaluation-bone-drilling-sequential.md
category: [implants]
confidence: in-vitro
pdf_path: /Users/oracleneo/llm-wiki/papers/rugova-2024-thermal-evaluation-bone-drilling-sequential.pdf
pdf_filename: rugova-2024-thermal-evaluation-bone-drilling-sequential.pdf
source_collection: external
tags: [sequential-drilling, pilot-drill, heat-generation, peck-drilling, IR-thermography, thermal-damage-zone, in-vitro]
---

## 한줄요약
인비트로(Bioengineering 2024, 5 drill, IR 카메라, **irrigation 없음**): sequential drilling이 thermal damage zone을 제거하지 못함 — pilot drill >100°C, 70°C 발열이 osteotomy로부터 측방 10mm까지 확산; **후속 enlarging drill(~4.2mm)이 절제하는 반경(~2mm)을 넘는 범위라 thermal-damaged 측방 골은 남음**. RPM·load 감소 + peck drilling이 완화책. ※ **본 결과는 irrigation 없는 합성골 극단치 — 정상 임상(saline irrigation + sharp drill + vital bone 혈류 cooling)에서는 후속 drilling이 thermal-damaged 영역 대부분 절제 가능; 적용 한정 시나리오는 D1 dense bone + irrigation 부족(full-guide 슬리브 차단 등) + 마모 drill의 3중 조건.**

## Summary
A custom-press in vitro study tested 5 drill bits in sequential drilling protocols with infrared thermography. The principal finding overturns a long-standing assumption: sequential drilling does not eliminate thermal trauma. The first (pilot) drill produces peak temperatures over 100°C, creating a thermal damage zone that spreads up to 10 mm from the osteotomy. Subsequent enlarging drills cannot remove this damage and instead add their own heat. Reducing RPM, reducing load, and using peck drilling lowered heat generation by reducing friction. The study was performed without irrigation.

## Key Contributions
Directly refutes the implicit clinical belief that "sequential drilling protects from heat." Identifies the pilot drill as the dominant thermal event and the peri-osteotomy zone (up to 10 mm) as the affected region.

## Methodology
- Custom drill press, artificial bone models.
- 5 drill bits, multiple protocols (load, RPM, peck on/off).
- IR thermography at multiple depths.
- **No irrigation in this protocol** — variable isolation.

## Results
| Variable | Finding |
|---|---|
| Pilot drill peak T | >100°C |
| Thermal damage zone | Spreads up to 10 mm from osteotomy |
| Sequential drilling | Does NOT remove thermal damage |
| Subsequent drills | Add heat, not remove it |
| Reduced RPM | ↓ heat |
| Reduced load | ↓ heat |
| Peck drilling | ↓ heat |

## Clinical Implications
- **본 결과의 임상 적용 한정 시나리오** — D1 dense cortical bone(열전도↓·마찰열↑) + irrigation 부족(full-guide 슬리브 차단, 술자 실수) + 마모된 pilot drill의 3중 조건이 겹칠 때. 정상 임상에선 다음과 같이 완화됨:
  - **Vital bone의 혈류 perfusion**이 능동적으로 열 소산 — in vitro 합성골의 10mm 확산은 임상에서 훨씬 축소
  - **Saline irrigation**이 표면 cooling, 핵심 열원 제거
  - **후속 enlarging drill**(2.0→2.8→3.5→4.2mm)이 osteotomy 직경을 키우면서 벽면 측방 ~2mm thermal-damaged 영역을 절제 — 정상 조건에선 thermal injury 범위가 이 안에 들어옴
- 즉 사용자 직관("후속 drill이 손상 골 절제")은 정상 임상에서 성립. rugova의 "후속 drill이 trauma 추가" claim은 in vitro 극단치 → vital bone·irrigation 가정 시 약화.
- 실용 take-away: pilot drill 단계는 thermal 위험 잠재 — irrigation 집중·sharp drill·간헐(peck) drilling으로 마진 확보. 그러나 정상 protocol에선 catastrophic failure 시나리오 아님.
- [claude해석] rugova의 진짜 가치는 "**irrigation·drill sharpness 관리가 무너졌을 때 sequential drilling이 자동 안전장치가 아니다**"라는 경고 — 기본을 못 갖춘 상태의 위험 폭로.
- bernabeu-mira-2020("initial/pilot > progressive/final")과 발열 분포 신호는 일치.

## Related Papers
- [[implants/bernabeu-mira-2020-bone-heating-drilling-implant]] — initial/pilot drill 발열 > progressive/final (같은 신호)
- [[implants/sorgato-2025-drill-bit-wear-temperature]] — irrigation 없는 조건에서 wear-온도 정량
- [[implants/heuzeroth-2021-thermal-exposure-osteotomy-osseointegration]] — 짧은 sequence + 신형 drill이 peak T 감소 in vivo
- [[implants/chauhan-2018-biomechanical-factors-heat-generation-osteotomy]] — multifactorial framework
- [[implants/jung-2021-heat-development-medical-drilling-influencing]] — internal·external factor 분류
- [[implants/aquilanti-2023-heat-generation-initial-osteotomy]] — 초기 osteotomy 발열
- [[implants/timon-2019-thermal-osteonecrosis-bone-drilling-orthopedic]] — orthopedic thermal osteonecrosis
