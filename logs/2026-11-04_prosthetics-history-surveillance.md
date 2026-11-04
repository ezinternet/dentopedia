# 치과보철재료 역사·발전 서베일런스 로그
**일시**: 2026-11-04  
**검색자**: Claude Sonnet (llm-wiki 세션)  
**검색 대상**: 치과보철재료 역사·발전·생존율 비교 — 근거 갱신

---

## 검색 전략

PubMed MCP 사용. 2회 검색 수행 (컨텍스트 복구 후).

| 검색 # | 쿼리 | 결과 수 |
|---|---|---|
| S1 | `dental ceramic crown clinical performance survival systematic review 2024 2025` | 4 |
| S2 | `monolithic zirconia crown clinical study survival complication 2023 2024 2025` | 0 |

---

## 평가 결과

### ⛔ 이미 인제스트됨 (신규 아님)

| PMID | Stem | 상태 |
|---|---|---|
| 40750081 | `laumacher-2025-lithium-disilicate-single-crowns-overview-sr` | 기존 인제스트 완료 |
| 40186393 | `alghauli-2025-clinical-complications-survival-rate-resin` | 기존 인제스트 완료 |

### ★ 신규 후보 — 인제스트 큐 추가

#### Prott 2024 (PMID 39558793) — **1순위**
**제목**: "Survival and Complications of Partial Coverage Restorations on Posterior Teeth—A Systematic Review and Meta-Analysis"  
**저널**: J Esthet Restor Dent 2024;37(3):620–641  
**DOI**: [10.1111/jerd.13353](https://doi.org/10.1111/jerd.13353)  
**설계**: SR+MA, 6 RCTs  
**핵심**: 구치부 부분피개 수복물(PCR) — RMC vs LD vs LRGC 3년 비교
- LDS 3년 생존율: 93.7% (95% CI 83.7–97.7)
- RMC 3년 생존율: 89.3% (95% CI 76.4–95.3)
- LRGC: 96.1–98.3% (대조군 대비)
- 결론: LDS > RMC (경미하게), 단기–중기 데이터 한계

**인제스트 추천 이유**: 부분피개(PCR) 세라믹 비교 SR+MA — 인레이·온레이 카테고리의 핵심 근거. 현재 `inlay/` 카테고리에 비교 SR+MA 부재.

**예정 stem**: `prott-2024-partial-coverage-restorations-posterior-sr-ma`  
**예정 카테고리**: `inlay`  
**source_collection**: PMC12076112 → `pubmed-text`

#### Morimoto 2024 (PMID 39384464) — 선택 후보
**제목**: "One-piece endodontic crowns in posterior teeth: An overview of systematic reviews"  
**저널**: J Prosthet Dent 2024;134(6):2103–2116  
**설계**: 9 SRs 포함된 overview  
**적합도**: 엔도크라운 특화 — prosthetics history보다 `endodontics/` 더 적합  
**권고**: 보철역사 overview보다 endodontics 카테고리 ingest 검토 (별도 서베일런스)

---

## 현황 평가

**보철역사 overview 갱신**: Krug 2024 인제스트 완료 → overview에 Era 0(전금속관 시대) 섹션 추가 완료.

**Laumacher 2025 (LD 단관 overview-of-SR)**: 이미 인제스트되어 overview source_papers에 포함. 추가 갱신 불필요.

**신규 증거 갭**: 부분피개 수복물 SR+MA (Prott 2024) 인제스트 대기 중 — `inlay/` 카테고리 보강.

---

## .ingest-queue 추가

```
prott-2024-partial-coverage-restorations-posterior-sr-ma | pmid:39558793 | pmc:PMC12076112 | doi:10.1111/jerd.13353 | inlay | pubmed-text | priority:medium
```
