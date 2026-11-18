# Gothic Arch Literature Surveillance — 2026-11-18

## 검색 방법
- PubMed E-utilities (이 세션에 PubMed MCP 리소스 없음 → 리포 기존 스크립트와 동일한 NCBI 경로 사용)
- Query: `("gothic arch"[Title/Abstract] OR "gothic arch tracing"[Title/Abstract] OR "arrow-point tracing"[Title/Abstract] OR "arrow-point tracing"[Title/Abstract] OR "gothic arch"[Mesh])`, sort by pub_date, retmax=120
- 총 170건 검색 → 비치과 주제(대동맥아치 coarctation/Aortic arch morphology, 고관절 Gothic Arch Angle/hip dysplasia, 대퇴 fovea 등) 제외 → 치과 CR/악간관계 논문만 추출
- 중복 게이트: `scripts/dedup-check.py --doi` 전 후보 Tier 1 rc=0 (보유분과 비중복 확인)

## 보유 베이스라인 (오버뷰 11편, 갱신 후 18편)
de Moraes Melo Neto 2021 · de Sousa Ervolino 2023 · Bhagat 2025 · Singh 2026 · Jász 2024 · Potdukhe 2023 · Zhou 2023 · Li 2022 · Li 2021 · Ribeiro 2024 · Kwak(2024 index) — +本次 7편(Huang·Abbad·Utz·Kattadiyil·Thakur·Keshvad·Rahman) 추가.

## 인제스트 실행 (선택 1·2 — 상위 3편, 병렬 팬아웃 후 직렬 finalize)
| 논문 | PMID / DOI | 설계 | 전문 | 비고 |
|---|---|---|---|---|
| Huang 2026 · J Dent Sci 21(3):1347-62 | 42688654 / 10.1016/j.jds.2025.07.3465 | sr+ma | PMC13536312 ✓ | MIP-anchored CR 과두변위 풀링 · refines Jász 2024 + overview |
| Abbad 2019 · JIPS 19(2):159-65 | 31040550 / 10.4103/jips.jips_269_18 | in-vivo (n=24) | PMC6482625 ✓ | 디지털 구내 트레이서 체위 비교 · extends Bhagat 2025 / Zhou 2023 |
| Utz 2023 · Int J Prosthodont 36(3):262-72 | 36484682 / 10.11607/ijp.7786 | cross-sectional (n=81) | abstract-only | 6종 CR 기록 비교 · reinforces Jász 2024, refines overview |

- 2026-11-18 인제스트 완료: sources/ + wiki/complete-denture/ 3쌍 작성, lint 0 errors, 1:1 orphan match, 커밋·푸시·qmd 임베딩 완료.
- 오버뷰 `wiki/overviews/gothic-arch-jaw-relation-recording-overview.md` 갱신: 한국어 핵심요약 3항목 추가, Axis 7 신설, Clinical Decision Threads 3항목, 체크리스트 3항목, spine 3줄, 11→14편, thesis-reviewed 2026-11-18.

## 인제스트 실행 (선택 4~7 — 고전 1차 근거 백필, 전부 abstract-only, 병렬 팬아웃 후 직렬 finalize)
| 논문 | PMID / DOI | 설계 | 전문 | 비고 |
|---|---|---|---|---|
| Kattadiyil 2021 · J Prosthodont 30(S1):34-42 | 33783085 / 10.1111/jopr.13321 | consensus | abstract-only | CR 술식 6종 정밀도 유사·술자 숙련도 핵심, PVS·폴리에터 우수 · extends de Moraes 2021 / Singh 2026 |
| Thakur 2012 · JIPS 12(3):175-81 | 23997468 / 10.1007/s13191-012-0154-5 | cross-sectional (n=28) | abstract-only (PMCID 있으나 JATS body 無) | 정적 왁스 vs 구외 고딕 CR 일치 7.14%, Woelfel 주관평가 무차이 · extends Singh 2026; Potdukhe SR 구성 원천이라 reinforces는 순환으로 보류 |
| Keshvad 2003 · J Prosthodont 12(2):90-101 | 12964681 / 10.1016/S1059-941X(03)00036-6 | in-vivo (n=14) | abstract-only | 3way 재현성 0.03~1.6mm, 양수 최고·고딕 최저 — de Moraes 2021 SR 원천 · extends de Moraes 2021 |
| Rahman 2004 · J Oral Rehabil 31(6):546-53 | 15189311 / 10.1111/j.1365-2842.2004.01190.x | in-vivo (n=5) | abstract-only | 추적판 반경사가 탭핑점을 MIP에 최근접, 탭핑점은 고딕 정점보다 전방(장치 기하 기전) · extends Singh 2026 |

- 2026-11-18 인제스트 완료: 4쌍 sources/wiki 작성, lint 4271 OK 0 errors, 1:1 orphan match(3841 PDFs / 4162 sources), index.md 4줄 추가, `--finish` 4편 커밋·푸시·qmd 임베딩 완료.
- 오버뷰 추가 갱신: Axis 7에 고전 1차 근거 백필 4 bullet(consensus framework / static-vs-functional head-to-head / 3way 재현성 원천 / 장치 기하 기전), spine 4줄, 14→18편. thesis-reviewed 2026-11-18 유지(동일일).
- 주의: 4편 전부 초록 기반이라 정밀 수치·p값은 과장 금지 — Thakur의 F-test/p pairing, Keshvad의 추론 통계 내부 불일치, Rahman의 n=5·효과크기 부재는 오버뷰에 명시.

## 미인제스트 후보 (보류 — 근거 가치 낮거나 중복 위험)
| 논문 | PMID | 판단 |
|---|---|---|
| Yang 2020 3-method 정확도 (중국어) | 32865359 | 초록만·중국어, 보류 |
| Orgev 2024 Digital GAT open-source (IJD) | 36484672 | Zhou 2023과 유사 device technique, 보류 |
| Potdukhe 2018/2018 clinico-radiographic GAT vs OPG | 30602631 / 29430137 | 이미 Potdukhe 2023 SR+MA가 흡수, 개별 인제스트 불필요 |

## 세션 확신도
- 검색·중복게이트·인제스트·lint·오버뷰 갱신: [확인] (이 세션 도구 출력 근거)
- 후보 보류 판단: [미검증] (해석)
