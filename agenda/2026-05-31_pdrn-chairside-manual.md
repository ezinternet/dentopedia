---
title: "PDRN chairside 의사결정 매뉴얼 (원장용, 인쇄 가능 HTML)"
type: agenda
date: 2026-05-31
status: in-progress
owner: 원장
priority: P1
tags: [pdrn, chairside, decision-support, interactive]
source_wiki:
  - wiki/overviews/pdrn-dentistry-evidence-synthesis.md
output_wiki:
  - interactives/2026-05-31_pdrn-chairside-manual.html
---

# Goal

PDRN(Polydeoxyribonucleotide, 폴리뉴클레오티드)을 chairside에서 적응증별로 "쓸지/말지·어떻게·한계는 무엇인지" 원장이 즉시 판단할 수 있도록, 위키 10편 근거를 근거등급과 함께 단일 인쇄 가능 HTML로 정리. 핵심 제약: human RCT 1편 외 전부 동물/in vitro이므로 "프로토콜 처방"이 아니라 "근거 경계 + 시도 조건 명시" 구조.

# Input

- wiki/pdrn/ku-2025-polydeoxyribonucleotide-pdrn-dentistry-narrative-review.md — 기전(A2A + salvage), 적응증 카탈로그, RCT gap 프레임
- wiki/pdrn/manfredini-2023-polydeoxyribonucleotides-pre-clinical-findings-bone-healing.md — preclinical 골치유 scoping review, dose/vehicle 이질성
- wiki/pdrn/bitto-2013-adenosine-receptor-polynucleotides-pdrn-periodontitis.md — A2A 기전 원전(rat 치주염, DMPX 소거)
- wiki/pdrn/kim-2026-efficacy-submucosal-polydeoxyribonucleotide-injection-impacted.md — 유일 human RCT(제3대구치 발치 후 통증, POD3·7)
- wiki/pdrn/lee-2023-impact-polydeoxyribonucleotide-lateral-sinus-elevation.md — lateral sinus, apical zone 한정 효과(BIC_a 76.7 vs 55.6%)
- wiki/pdrn/lee-2023-effect-polydeoxyribonucleotide-early-bone-formation.md — IIP dehiscence, new bone↑ but BIC/BAFO 무효
- wiki/pdrn/lee-2024-impact-polydeoxyribonucleotides-morphology-viability-osteogenic.md — GMSC spheroid in vitro, marker별 최적농도 상이
- wiki/pdrn/lim-2023-xenogeneic-collagen-matrix-polydeoxyribonucleotide-gingival-phenotype.md — box defect, XCM+PDRN ≈ SCTG
- wiki/pdrn/lee-2024-soft-tissue-augmentation-immediate-implant-pdrn.md — IIP 연조직, volume gain 무효·KT만 우위·dehiscence>50%
- wiki/pdrn/kim-2025-preclinical-investigation-collagen-matrix-polydeoxyribonucleotide.md — buccal implant KT, dose 비선형(2≈4 mg/mL)

# Output

- interactives/2026-05-31_pdrn-chairside-manual.html — 인쇄 가능 단일 HTML (원장 임상 의사결정용)

산출물 frontmatter에 `agenda: agenda/2026-05-31_pdrn-chairside-manual.md` 백링크 박음.

# Done Criteria

- [x] 기전 섹션 (A2A receptor + salvage pathway, PDRN vs PN 경계)
- [x] 근거등급 범례 (RCT / SR / animal / in-vitro / narrative)
- [x] 4개 적응증 카드: 근거등급·말할수있는것/없는것·시도조건·trade-off·대안·출처
- [x] dose/vehicle/timing 종합표 (미명시 항목 '미검증' 표기)
- [x] 원장 메모 체크리스트
- [x] 레퍼런스 10편 (study type inline)
- [x] 검증: 정량 수치 wiki 원본 대조
- [ ] index.md / 본 agenda Output 백링크 확정

# Notes / Decisions

- 2026-05-31: 근거 한계상 "처방 프로토콜" 금지, "근거 경계 + 조건부 시도" 톤으로 확정. human injection 농도는 wiki 페이지에 미기재 → '미검증, 원 PDF 재확인 필요'로 표기, 임의 수치 생성 금지(Rule #4).
- 연조직 적응증의 상충(IIP volume 무효 vs box defect comparable)은 카드 내 명시 — 단일 결론 회피.

# References

- [[wiki/pdrn/ku-2025-polydeoxyribonucleotide-pdrn-dentistry-narrative-review]]
- [[wiki/pdrn/manfredini-2023-polydeoxyribonucleotides-pre-clinical-findings-bone-healing]]
