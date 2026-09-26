---
title: "HbA1c 임플란트 5년 위험 계산기"
type: agenda
date: 2026-09-22
status: done
owner: 원장
priority: P2
tags: [HbA1c, diabetes, implant-failure, peri-implantitis, risk-calculator, dose-response]
source_wiki:
  - wiki/implants/survival/abichandani-2026-time-varying-glycemic-control-long.md
  - wiki/drug/systemic-disease/ahmad-2025-glucagon-like-peptide-1-receptor.md
  - wiki/implants/peri-implantitis/li-2025-inflammatory-response-dental-implant-surgery.md
output_wiki:
  - interactives/2026-09-22_hba1c-implant-risk-calculator.html
---

# Goal

HbA1c 수치별 5년 임플란트 실패·합병증 절대 위험도를 chairside에서 즉시 참조할 수 있도록 계산기로 정리 — 당뇨 환자 임플란트 상담 시 근거 기반 수치 제시.

# Input

- wiki/implants/survival/abichandani-2026-time-varying-glycemic-control-long.md — HbA1c band별 5년 절대 위험도 원자료 (후향적 코호트, n=782, 1312 임플란트, 5.6년)
- wiki/drug/systemic-disease/ahmad-2025-glucagon-like-peptide-1-receptor.md — 혈당강하제 계열과 임플란트 예후 맥락
- wiki/implants/peri-implantitis/li-2025-inflammatory-response-dental-implant-surgery.md — 염증반응 기전 배경

# Output

- interactives/2026-09-22_hba1c-implant-risk-calculator.html

각 산출물 frontmatter에 `agenda: agenda/2026-09-22_hba1c-implant-risk-calculator.md` 백링크 박음.

# Done Criteria

- [x] HbA1c band별 5년 절대 위험도 시각화
- [x] 복수 임플란트 누적 위험 계산
- [x] 비의료기기·교육/의사결정 보조 도구 명시
- [x] source_wiki 백링크

# Notes / Decisions

- 2026-09-22: 산출물이 agenda 없이 먼저 저작됨 — 2026-09-23 daily-audit(`operations-lint.py` MISSING agenda 오류)에서 발견되어 이 agenda 파일을 소급 작성하고 상호 백링크를 채움.

# References

- [[interactives/2026-09-22_hba1c-implant-risk-calculator]]
