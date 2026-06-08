---
title: "지르코니아 인레이 접착 SOP 인터랙티브 (원장·위생사 통합)"
type: agenda
date: 2026-05-25
status: done
owner: 원장
priority: P1
deadline: 2026-05-31
tags: [zirconia, inlay, bonding, sop, interactive]
source_wiki:
  - wiki/dental-materials/blatz-2018-resin-bonding-high-strength-ceramics-review.md
  - wiki/inlay/behera-2021-lithium-disilicate-vs-zirconia-inlays-1year.md
  - wiki/inlay/bomicke-2025-3ytzp-inlay-enamel-wear-5year.md
  - wiki/dental-materials/ban-2023-dental-zirconia-types-development-review.md
  - wiki/dental-materials/silva-2022-zirconia-saliva-cleaning-sr-ma.md
  - wiki/dental-materials/genc-2025-cleaning-protocols-zirconia-bond-strength.md
  - wiki/dental-materials/al-akhali-2025-zirconia-cleaning-bonding-duration.md
  - wiki/dental-materials/awad-2022-mdp-cleaner-contaminated-zirconia.md
  - wiki/dental-materials/comba-2021-chemical-bonding-cubic-zirconia.md
  - wiki/dental-materials/opatragoon-2024-primer-applications-zirconia-bond.md
  - wiki/dental-materials/shokry-2022-zirconia-crown-primer-cement-retention.md
  - wiki/dental-materials/kwon-2026-self-adhesive-resin-cement-zirconia.md
  - wiki/dental-materials/lopes-2023-universal-adhesives-zirconia-long-term.md
  - wiki/resin-bonding/samartzi-2021-immediate-dentin-sealing-review.md
---

# Goal

지르코니아 인레이 시멘테이션 단계별 의사결정을 원장의 chairside SOP와 위생사 어시스트 체크리스트를 한 화면에서 분기형으로 따라갈 수 있는 단일 HTML 인터랙티브로 정리. 시적 후 타액 오염·프라이머 선택·시멘트 선택 등 임상 분기점에서 근거 강도와 함께 즉시 다음 단계로 안내.

# Input

- wiki/dental-materials/blatz-2018-resin-bonding-high-strength-ceramics-review.md — APC 컨셉(Air-abrade, Prime, Cement) 원전, 표면처리 기본 원칙
- wiki/inlay/behera-2021-lithium-disilicate-vs-zirconia-inlays-1year.md — 지르코니아 인레이 1년 임상 prospective (n=30)
- wiki/inlay/bomicke-2025-3ytzp-inlay-enamel-wear-5year.md — 3Y-TZP RBFPD 5년 임상, 대합 법랑질 마모 77μm
- wiki/dental-materials/ban-2023-dental-zirconia-types-development-review.md — 3Y vs 5Y vs 6Y 분류
- wiki/dental-materials/silva-2022-zirconia-saliva-cleaning-sr-ma.md — 타액 오염 세정 SR+MA (Al₂O₃ blasting > Ivoclean > 물/알코올/인산)
- wiki/dental-materials/genc-2025-cleaning-protocols-zirconia-bond-strength.md — 6세정법 SBS 정량 (Sandblasting+Ivoclean 9.3 MPa, IPA 3.04 MPa)
- wiki/dental-materials/al-akhali-2025-zirconia-cleaning-bonding-duration.md — 150일 후 Ivoclean 내구성 우수, Katana Cleaner 금기
- wiki/dental-materials/awad-2022-mdp-cleaner-contaminated-zirconia.md — MDP 함유 세정제 (Clearfil Ceramic Primer Plus) 이중기능
- wiki/dental-materials/comba-2021-chemical-bonding-cubic-zirconia.md — 5Y-PSZ도 MDP 반응성 유지
- wiki/dental-materials/opatragoon-2024-primer-applications-zirconia-bond.md — 프라이머 1회 도포 충분
- wiki/dental-materials/shokry-2022-zirconia-crown-primer-cement-retention.md — Panavia V5+CCP Plus 매칭 최우수
- wiki/dental-materials/kwon-2026-self-adhesive-resin-cement-zirconia.md — SARC 비교 (TheraCem > Clearfil SA > RelyX U200)
- wiki/dental-materials/lopes-2023-universal-adhesives-zirconia-long-term.md — 12개월 65% bond 감소 경고
- wiki/resin-bonding/samartzi-2021-immediate-dentin-sealing-review.md — IDS 프로토콜, 인레이에 권장

# Output

- interactives/2026-05-25_zirconia-inlay-bonding.html — 분기형 의사결정 트리 (원장·위생사 듀얼 레인)

산출물 frontmatter(HTML 헤드 주석)에 `agenda: agenda/2026-05-25_zirconia-inlay-bonding-interactive.md` 백링크 박을 것.

# Done Criteria

- [x] 분기점 ≥6개 (재료 확인 → 상아질 처리 → 인레이 내면 처리 → 시적 오염 분기 → 프라이머/시멘트 선택 → 시멘테이션 → 마무리)
- [x] 각 결정에 wiki 출처 inline citation
- [x] 확신도 태그 부착 ([근거강함]/[합의수준]/[claude해석])
- [x] 원장 결정포인트(파란색) / 위생사 어시스트(초록색) 시각적 구분
- [x] 단일 HTML 파일, CDN 외부 의존만
- [x] 시멘트·프라이머 추천 매트릭스 표 1장
- [ ] index.md 또는 interactives 카테고리에 entry 추가 (수동, 추후)

# Notes / Decisions

- 2026-05-25: 사용자 의도 = 원장+위생사 통합 SOP, 분기형 트리, 지르코니아 인레이만(LDS 비교 제외) — AskUserQuestion 응답.
- 핵심 결정: 시적 후 오염 처리 분기를 가장 중요한 imperative한 노드로. silva-2022 SR/MA 근거강함.
- 미해결: 본 인터랙티브는 chairside 의사결정용. 환자 설명용·교육용은 별도 산출물 필요.
- 잠재적 wiki 승격 후보: "지르코니아 인레이 접착 APC 프로토콜 overview" — wiki/overviews/ 후보

# References

- [[wiki/dental-materials/blatz-2018-resin-bonding-high-strength-ceramics-review]]
- [[wiki/dental-materials/silva-2022-zirconia-saliva-cleaning-sr-ma]]
