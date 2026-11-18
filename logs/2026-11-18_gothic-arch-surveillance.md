# Gothic Arch Literature Surveillance — 2026-11-18

## 검색 방법
- PubMed E-utilities (이 세션에 PubMed MCP 리소스 없음 → 리포 기존 스크립트와 동일한 NCBI 경로 사용)
- Query: `("gothic arch"[Title/Abstract] OR "gothic arch tracing"[Title/Abstract] OR "arrow-point tracing"[Title/Abstract] OR "arrow-point tracing"[Title/Abstract] OR "gothic arch"[Mesh])`, sort by pub_date, retmax=120
- 총 170건 검색 → 비치과 주제(대동맥아치 coarctation/Aortic arch morphology, 고관절 Gothic Arch Angle/hip dysplasia, 대퇴 fovea 등) 제외 → 치과 CR/악간관계 논문만 추출
- 중복 게이트: `scripts/dedup-check.py --doi` 전 후보 Tier 1 rc=0 (보유분과 비중복 확인)

## 보유 베이스라인 (오버뷰 11편, 갱신 후 14편)
de Moraes Melo Neto 2021 · de Sousa Ervolino 2023 · Bhagat 2025 · Singh 2026 · Jász 2024 · Potdukhe 2023 · Zhou 2023 · Li 2022 · Li 2021 · Ribeiro 2024 · Kwak(2024 index) — +本次 3편(Huang·Abbad·Utz) 추가.

## 인제스트 실행 (선택 1·2 — 상위 3편, 병렬 팬아웃 후 직렬 finalize)
| 논문 | PMID / DOI | 설계 | 전문 | 비고 |
|---|---|---|---|---|
| Huang 2026 · J Dent Sci 21(3):1347-62 | 42688654 / 10.1016/j.jds.2025.07.3465 | sr+ma | PMC13536312 ✓ | MIP-anchored CR 과두변위 풀링 · refines Jász 2024 + overview |
| Abbad 2019 · JIPS 19(2):159-65 | 31040550 / 10.4103/jips.jips_269_18 | in-vivo (n=24) | PMC6482625 ✓ | 디지털 구내 트레이서 체위 비교 · extends Bhagat 2025 / Zhou 2023 |
| Utz 2023 · Int J Prosthodont 36(3):262-72 | 36484682 / 10.11607/ijp.7786 | cross-sectional (n=81) | abstract-only | 6종 CR 기록 비교 · reinforces Jász 2024, refines overview |

- 2026-11-18 인제스트 완료: sources/ + wiki/complete-denture/ 3쌍 작성, lint 0 errors, 1:1 orphan match, 커밋·푸시·qmd 임베딩 완료.
- 오버뷰 `wiki/overviews/gothic-arch-jaw-relation-recording-overview.md` 갱신: 한국어 핵심요약 3항목 추가, Axis 7 신설, Clinical Decision Threads 3항목, 체크리스트 3항목, spine 3줄, 11→14편, thesis-reviewed 2026-11-18.

## 미인제스트 후보 (보류 — 근거 가치 낮거나 중복 위험)
| 논문 | PMID | 판단 |
|---|---|---|
| Kattadiyil 2021 Best Evidence Consensus (JPR) | 33783085 | CR 기록 재료·재현성 합의문 — 가치 있으나 consensus라 후보 보류 (초록만) |
| Thakur 2012 static vs functional CR (JIPS) | 23997468 | PMC 전문 있음 — Singh 2026·Potdukhe의 선행, 보류 |
| Keshvad 2003 (J Prosthodont) | 12964681 | 양손/턱끝/GAT 3-way — de Moraes Melo Neto SR 원천일 수 있어 중복 확인 후 결정 |
| Rahman 2004 추적판 경사각 (J Oral Rehabil) | 15189311 | 구내 오차증폭 기전 — 가치 있으나 소표본(n=5), 보류 |
| Yang 2020 3-method 정확도 (중국어) | 32865359 | 초록만·중국어, 보류 |
| Orgev 2024 Digital GAT open-source (IJD) | 36484672 | Zhou 2023과 유사 device technique, 보류 |
| Potdukhe 2018/2018 clinico-radiographic GAT vs OPG | 30602631 / 29430137 | 이미 Potdukhe 2023 SR+MA가 흡수, 개별 인제스트 불필요 |

## 세션 확신도
- 검색·중복게이트·인제스트·lint·오버뷰 갱신: [확인] (이 세션 도구 출력 근거)
- 후보 보류 판단: [미검증] (해석)
