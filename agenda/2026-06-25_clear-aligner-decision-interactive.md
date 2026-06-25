---
title: "투명교정 적응증 결정 게이트 + 상악확장 over-correction 계산기"
type: agenda
date: 2026-06-25
status: done
owner: 원장
priority: P2
tags: [clear-aligner, orthodontics, interactive, decision-aid]
source_wiki:
  - wiki/overviews/clear-aligner-indications-limitations.md
  - wiki/orthodontics/clear-aligner/de-la-rosa-gay-2025-expansion-predictability-clear-aligner.md
  - wiki/orthodontics/clear-aligner/marinelli-2025-temporary-anchorage-devices-clear-aligner-sr.md
  - wiki/orthodontics/clear-aligner/cao-2025-clear-aligner-biomechanics-finite-element-analysis-sr.md
---

# Goal

투명교정(Clear Aligner Therapy, CAT) 26편 종합 오버뷰의 "적응증 gradient"를 chairside에서 즉시 참조 가능한 단일 HTML 의사결정 도구로 변환. 두 탭: (1) 적응증 결정 게이트 — 부정교합 복잡도·이동유형·발치·골격성 플래그를 입력하면 CA 단독 / CA+보조(attachment·TAD·IPR) / FA 고려 3-tier 권고, (2) 상악확장 over-correction 계산기 — de la Rosa-Gay 0.92mm 평균오차·72% 과소확장 데이터로 계획 확장량 보정 제안.

# Input

- wiki/overviews/clear-aligner-indications-limitations.md — 적응증 gradient 9→10축 종합 (게이트 로직의 근간)
- wiki/orthodontics/clear-aligner/de-la-rosa-gay-2025-expansion-predictability-clear-aligner.md — 확장 0.92mm 오차·72.2% 과소확장 (계산기 정량 앵커)
- wiki/orthodontics/clear-aligner/marinelli-2025-temporary-anchorage-devices-clear-aligner-sr.md — CA+TAD 적응증 (게이트 보조-tier 근거)
- wiki/orthodontics/clear-aligner/cao-2025-clear-aligner-biomechanics-finite-element-analysis-sr.md — auxiliaries가 tipping→translation 전환 (보조-tier 메커니즘)

# Output

- interactives/2026-06-25_clear-aligner-decision-tools.html

산출물 frontmatter(HTML 주석)에 `agenda: agenda/2026-06-25_clear-aligner-decision-interactive.md` 백링크 + source_wiki 박음.

# Done Criteria

- [x] 탭 1: 적응증 게이트 — 가중 플래그 입력 → 3-tier 권고 pill + 근거 inline citation
- [x] 탭 2: 상악확장 계산기 — 계획 확장량 입력 → 추정 달성량·over-correction 권고 (정량 앵커 0.92mm/72%는 paper, 수정계수는 claude해석 명시)
- [x] 두 도구 모두 근거 paper author-year 표기 + 면책(개인 임상 참고용) 명시
- [x] 무근거 수치 fabrication 없음 — paper 미보유 magnitude는 claude해석 태그로 분리
