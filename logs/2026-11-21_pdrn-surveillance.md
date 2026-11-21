# PDRN (폴리데옥시리보뉴클레오티드) 치과 문헌 서베일런스 — 2026-11-21

## 검색 방법
- PubMed E-utilities (이 세션에 PubMed MCP 리소스 없음 → 리포 기존 서베일런스 로그와 동일한 NCBI 경로). E-utilities에서는 `datetype=edat` 필터가 정상 동작하므로 water-mark 대신 **edat 창을 신규성의 기준**으로 사용.
- Query: `(PDRN[tiab] OR polydeoxyribonucleotide[tiab] OR "poly deoxyribonucleotide"[tiab] OR "polynucleotide"[tiab]) AND (dental[tiab] OR dentistry[tiab] OR implant[tiab] OR periodontal[tiab] OR endodontic[tiab] OR oral[tiab] OR osseointegration[tiab] OR "bone regeneration"[tiab] OR osteoblast[tiab] OR osteoclast[tiab] OR TMJ[tiab] OR "temporomandibular"[tiab])`
- 창: `edat 2026/09/21 – 2026/11/21` (pdrn 토픽 `last_run_edat` 기준). ptyp 필터(RCT/SR/MA) 적용 1건, 미적용 3건. ptyp 미적용 pass를 추가한 이유: 이 위키의 PDRN 코퍼스는 동물·in vitro 논문이 다수라 ptyp 필터만 쓰면 놓침.
- 중복 게이트: `sweep_state.py dedup --topic pdrn --pmids ...` → seen·screened 0건, PMID/DOI/제목 기준 `sources/`·`wiki/`·`index.md`·`queue.md` 중복 0건.

## water-mark 주의 (이번 스윕에서 실제 발생)
- 전역 water-mark `42964982`로 dedup 시 PMID `42883322`(edat 2026/10/07)가 **below-watermark로 잘못 제외**됨. pdrn last_run(2026/09/21)보다 edat가 뒤이므로 진짜 신규. MCP의 죽은 edat 필터를 보완하기 위한 water-mark 프록시가 edat 직접 필터보다 오히려 false-negative를 만든 사례. → edat 필터가 살아 있는 E-utilities 경로에서는 water-mark를 신규성 기준으로 쓰지 않음.

## 신규 후보 3건 (큐 적립 완료 — `[ ]` 미인제스트)
| 논문 | PMID / DOI | 설계 | edat | 전문 | 스크리닝 |
|---|---|---|---|---|---|
| Lee SH 2026 · Front Pharmacol | 43017077 / 10.3389/fphar.2026.1965494 | SR (38편: clinical 28 + preclinical 10) | 2026/10/28 | PMC13752129 (CC BY) ✓ | **include** — 비치과 근골격계 SR이나 TMJ·최대개구(MMO) 결과 포함 → [[pdrn/ku-2025-prolotherapy-temporomandibular-joint-disorders]]·[[pdrn/kim-2019-efficacy-safety-polydeoxyribonucleotide-knee]]의 cross-domain 축 연장 |
| Lee D 2026 · J Periodontal Implant Sci | 43059186 / 10.5051/jpis.2602540127 | animal (NZW rabbit n=16, calvarial 6mm × 4) | 2026/11/20 | none (JPIS publisher OA — ingest 단계 확인) | **include** — 치과 저널·직접 골재생 축. PDRN-A/B/C 제형 비교 + graft浸泡, 2/6주 BV·T·조직계측. 위키의 **제형·용량 표준화 공백**을 정면으로 다룸. PDRN-A 2주 22.85% vs control 18.24%, 6주 25.33% vs 19.33% |
| Jeong KM 2026 · Molecules | 42883322 / 10.3390/molecules31193558 | in vitro + in vivo (mechanism) | 2026/10/07 | PMC13666977 (CC BY) ✓ | **borderline → include** (false-negative 회피 원칙) — 전신 성장판·간 IGF-1 축으로 **치과 적응증 아님**. 그러나 A2A 길항제 ZM241385로 수용체 매개 확인 + 파골세포/조골세포 marker 변조 → 위키 PDRN 기전 축과 연결. 인제스트 우선순위 낮음, 인제스트 시 cross-domain 명시 필요 |

- 큐 적립: 3건 (`added: 3, skipped: 0`), `pdrn.last_run_edat` `2026/09/21 → 2026/11/21` 갱신.

## 인제스트 결과 (완료 — 2026-11-21)
세 건 모두 인제스트 완료·커밋·푸시·qmd 재색인 완료. 최종 인제스트 순서는 아래 권장안과 달리 SR → 제형비교 → 기전 순으로 진행(모두 동일 결과).
- 43017077 → `wiki/pdrn/lee-2026-polydeoxyribonucleotide-and-polynucleotide-effects-in` (PMC full text, sr)
- 43059186 → `wiki/pdrn/lee-2026-early-bone-regeneration-with-different` (JPIS publisher OA PDF via `xmlink_gate=v1` cookie, animal — PMCID 없음)
- 42883322 → `wiki/pdrn/jeong-2026-polydeoxyribonucleotide-promotes-longitudinal-bone-growth` (PMC full text, in-vivo, cross-domain 명시)
검증: lint 0 errors · orphan 1:1 · rationale-lint 0 errors · pii-guard 위반 0 · qmd 3편 검색 확인 · push 성공.

## 인제스트 권장 순서 (당시 안 — 실행 완료)
1. **43059186** — 치과 골재생 직접 근거 + 제형 비교(위키 공백). OA 경로 JPIS publisher 확인 필요.
2. **43017077** — PMC OA 즉시 가능. TMJ cross-domain SR로 기존 prolotherapy 노드 보강; 13,267건 중 38건 선별 기준·비교군별 유의성 이질성 주의(과장 금지).
3. **42883322** — PMC OA이나cross-domain 기전. 인제스트 시 `cross-domain` 라벨 + 전신 성장판 효과와 치과 재생 효과를 동일선상에 두지 않도록 명시.

## 세션 확신도
- 검색·dedup·OA 태깅·큐 적립·상태 갱신: [확인] (이 세션 E-utilities/esummary/efetch + `sweep_state.py` 출력 근거)
- 스크리닝 include/borderline 판정: [확인] (초록 직접 판독, 위 근거 문장 근거)
- 43059186의 JPIS publisher OA 가능성: [미검증] (Europe PMC 기준 `isOpenAccess N`·PMCID 없음 — publisher 사이트 미확인, ingest 단계에서 확인 필요)
