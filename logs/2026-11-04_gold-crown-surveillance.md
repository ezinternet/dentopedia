# 골드크라운 (전금속관) 서베일런스 로그
**일시**: 2026-11-04  
**검색자**: Claude Sonnet (llm-wiki 세션)  
**검색 대상**: 골드크라운 / 주조금속관 / 전금속관 임상 성능·생존율

---

## 검색 전략

PubMed MCP 사용 (`search_articles`). 4회 순차 검색 수행.

| 검색 # | 쿼리 | 결과 수 |
|---|---|---|
| S1 | `gold crown survival systematic review clinical performance` | 8 |
| S2 | `gold alloy dental crown systematic review long-term 10 year` | 8 |
| S3 | `cast metal crown survival rate clinical performance` | 8 |
| S4 | `gold alloy dental crown 10 year survival failure rate` | 8 |
| S5 | `cast gold crown longevity survival posterior teeth clinical performance retrospective` | 2 |

총 평가 PMID: 38702521, 25692556, 24596914, 23522363, 22708959, 21287210, 19686283, 16750593, 10815600, 12743836

---

## 주요 발견 — 인제스트 후보

### ★ 1순위: Krug 2024 (PMID 38702521)
**제목**: "Long-term performance of ceramic in/-onlays vs. cast gold partial crowns - a retrospective clinical study"  
**저널**: Clinical Oral Investigations 2024;28(5):298  
**DOI**: [10.1007/s00784-024-05682-7](https://doi.org/10.1007/s00784-024-05682-7)  
**설계**: 후향 코호트, N=325 환자, 최대 24.8년 추적 (평균 13.9년)

**핵심 데이터 — Cast Gold Partial Crown (CGPC):**
- **15년 생존율**: 92.6%
- **23.5년 생존율**: 91.8%
- **연간 실패율**: 0.7%
- **주요 합병증**: 근관치료 필요 8.8%, 이차우식 4.8%, 탈락(decementation) 2.0%

**인제스트 추천 이유**: 전금속관(골드 부분크라운) 최장기 임상 추적 데이터. 세라믹 인레이/온레이와의 직접 비교. PMCID 없음 → `pubmed-abstract` 수집.

**예정 stem**: `krug-2024-ceramic-inlay-cast-gold-partial-crown-longterm`  
**예정 카테고리**: `inlay` (부분 피개 수복물 비교 연구)

---

## 비관련 결과 (제외)

| PMID | 제목 | 제외 이유 |
|---|---|---|
| 25692556 | Short implants 6mm vs 10mm (Rossi 2015) | 임플란트 길이 연구; 금크라운 아님 |
| 24596914 | PFM precious alloy single crowns (Behr 2014) | PFM 연구; 이미 위키 보유 가능성 |
| 23522363 | MC single crowns 10-yr prospective (Reitemeier 2013) | MC 크라운 연구 |
| 22708959 | All-ceramic vs MC implant crowns (Hosseini 2012) | 임플란트 보철 비교 |
| 21287210 | MC FPD chipping risk (Behr 2011) | MC FPD 치핑 연구 |
| 19686283 | CNC titanium vs gold alloy frameworks (Örtorp 2009) | 무치악 임플란트 프레임워크; 단관 아님 |
| 16750593 | Cast post and core survival (Balkenhol 2006) | 포스트앤코어 연구; 크라운 아님 |
| 10815600 | Brånemark implant single crowns (Scholander 1999) | 임플란트 단관; 순수 금크라운 아님 |

---

## 현황 평가

**골드크라운 전용 SR/MA 부재**: 현재 PubMed 색인 기준, 전금속관(풀캐스트 금크라운) 단독을 대상으로 한 최신 체계적 고찰은 확인 안 됨. 대부분의 PFM/세라믹 비교 연구에서 금합금이 대조군으로 등장.

**임상 의의**: 골드크라운의 임상 근거는 Krug 2024(CGPC 23.5년 91.8%)와 고전적 Schwartz·Walton 연구들(1990s-2000s)에 집중. 단, 1990s-2000s 연구 대부분은 PubMed에서 풀 텍스트 접근 제한.

---

## .ingest-queue 추가 대상

```
krug-2024-ceramic-inlay-cast-gold-partial-crown-longterm | pmid:38702521 | doi:10.1007/s00784-024-05682-7 | inlay | pubmed-abstract | priority:high
```

---

## 메모

- QMD 데몬 현재 세션에서 타임아웃 발생 → grep 폴백으로 운영
- 골드크라운 역사적 근거(1950-2000년대 Kern, Schwartz 등) PubMed 미검색 (접근 제한 예상); 위키 외부에서 추가 인제스트 고려 대상
