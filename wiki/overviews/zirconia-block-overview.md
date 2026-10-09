---
title: "지르코니아 블록 — 제조·결함·소결·선택 종합 (CAD/CAM Blank)"
authors: Synthesis (Damian Lee)
year: 2026
date: 2026-10-09
doi: N/A
source: N/A
category: overviews
evidence_level: synthesis
pdf_path: N/A
pdf_filename: N/A
source_collection: synthesis
tags: [dental-materials, zirconia, cad-cam, blank, block, multilayer, sintering, shrinkage, milling-defects, manufacturing, overview]
---

## 한국어 핵심요약

> [!summary] 한국어 핵심요약
> - 결론: 지르코니아 블록(CAD/CAM pre-sintered blank/disc)을 **제조 → 화학 설계 → 멀티레이어 → 결함 → 소결 → 임상 선택**의 6축으로 분해한 sub-overview. 기존 두 자매 오버뷰([[overviews/zirconia-material-clinical-overview]] = 재료과학·수명, [[overviews/zirconia-types-clinical-selection]] = grade 선택)가 비워둔 **"블록 단위" 시점**을 채운다.
> - 블록은 반제품이다: 부분소결(pre-sintered) 상태로 밀링하고 최종 소결(≈1500°C)에서 완제품이 된다. 소결 선형 수축 20–25%(용적 49–57%) → CAM 확대계수(예 1.23×) 입력이 적합도의 관문 [미검증 — 일반 공정 지식·웹 출처].
> - 화학 설계가 성능을 결정: 이트리아(Y₂O₃)↑ → 입방상(cubic)↑ → 투명도↑·강도↓. 3Y-TZP 900–1200 → 4Y-PSZ 700–900 → 5Y-PSZ 600–700 → 6Y/UHTZ 500–600 MPa (Cesar 2024 spine, Ban 2023 정합). [확인]
> - 현재 시장 표준은 조성경사형 멀티레이어 블록: 3Y(치경부·구조) + 5Y(절연부) gradient. 구세대 층간 결함은 신규 분말 압축 기술로 해결(Cesar 2024). [확인]
> - **블록 위치(네스팅)가 강도를 좌우**: 3Y/5Y 멀티레이어는 디스크 중심부 네스팅 > 상단부(Waldecker 2026 in-vitro, RBFPD 하중 지지능). 5Y 단독 블록은 RBFPD에 하중 안전역 부족. [확인 — in-vitro]
> - **임상 파절의 상당 기원은 밀링 결함**: as-sintered는 외재적(밀링 gouge·에지 칩), 고연마 시 내재적(기공·결정군집·이물질)으로 전환 — 평균강도↑ but Weibull 계수(신뢰도)↓의 "연마 역설". 제조사별 블랭크 품질(EDS Al·Si·Ca·Fe 오염)이 임상적으로 중요하나 불투명한 변수(Kwon 2024). [확인 — in-vitro]
> - 소결: 표준 ~8h/≈1500°C, 고속 소결(30–90분)은 임상 신뢰성 미성숙, HIP는 신뢰성↑이나 아직 표준 아님(Cesar 2024). 교합 조정 후 grinding mark 재도입 = 새 응력집중 → 반드시 재연마. [확인]
> - 임상 선택: 후방 고하중 → 3Y-TZP monolithic, 전치 심미 → 5Y/멀티레이어, 전치 단교 → 4Y/멀티레이어. 어느 블록이든 **최소 교합면 1.5mm**(Ali 2023)와 APC 접착(air-abrasion + MDP)은 불변. [확인]
> - 확신도: 축 2–5 = 재료과학 narrative + in-vitro 중심(근거강함~중간), 축 6 = SR+MA 파생(근거강함). 소결 수축 수치·제조사 스펙·한국 가용성 = [미검증].

## Three-line Summary

Sub-overview synthesizing dental zirconia **CAD/CAM blanks (blocks/discs)** — the manufacturing unit behind every milled zirconia restoration — across six axes: block fabrication workflow, yttria-driven chemistry (strength–translucency trade-off), composition-gradient multilayer blocks, blank/milling defects as fracture origins, sintering (shrinkage, programs, HIP), and chairside block selection.

A block is a semi-finished pre-sintered puck: it is milled roughly 20–25% oversized and only becomes a restoration after final sintering (~1500°C), so block chemistry (3Y→5Y yttria), internal quality (pores, grain clusters, EDS-detectable contaminants), and nesting position inside the disc all become hidden clinical variables; CAD/CAM milling defects — not intrinsic blank flaws — dominate fracture initiation in as-sintered restorations (Kwon 2024), and composition-gradient multilayer (3Y base + 5Y incisal) is the current clinical standard (Cesar 2024).

Clinical translation: choose block grade by indication (posterior high-load → 3Y-TZP, anterior esthetic → 5Y-PSZ/multilayer, anterior short-span FPD → 4Y-PSZ/multilayer), keep ≥1.5 mm occlusal thickness for every grade (Ali 2023), use the same APC bonding protocol regardless of grade, and re-polish after any chairside adjustment — sintering and blank-quality factors stay lab-side and opaque, so clinician leverage is grade choice, thickness, and finish.

## 세줄요약

지르코니아 **CAD/CAM 블록(blank/disc)**을 제조 → 이트리아 화학 → 멀티레이어 → 결함 → 소결 → 임상 선택의 6축으로 합성한 sub-overview. 기존 재료 오버뷰가 "어떤 grade"를 다뤘다면, 본 페이지는 "그 grade가 어떤 블록으로 만들어지고 왜 파절하는가"를 다룬다.

블록은 부분소결 반제품 — 약 20–25% 확대 밀링 후 1500°C 소결에서 완성되므로, 이트리아 함량(3Y→5Y)·내부 결함(기공·결정군집·EDS 검출 오염)·디스크 내 네스팅 위치가 모두 숨은 임상 변수다. as-sintered 파절은 밀링 결함이 지배하고(Kwon 2024), 조성경사 멀티레이어(3Y 코어 + 5Y 절연)가 현 표준(Cesar 2024).

임상 번역: 적응증별 grade 선택(후방 고하중 3Y, 전치 심미 5Y/멀티, 전치 단교 4Y), 전 grade 공통 최소 교합면 1.5mm(Ali 2023), 접착 SOP는 grade 무관 APC 동일, 조정 후 재연마. 소결·블랭크 품질은 lab-side 불투명 변수이므로 임상가의 레버는 grade·두께·마감이다.

## Summary

[[overviews/zirconia-material-clinical-overview]]가 재료과학·LTD·생존율을, [[overviews/zirconia-types-clinical-selection]]가 grade × 적응증을 담당한다. 본 페이지는 그 사이의 **블록 제조 단위**를 spine으로 다시 합성한다 — 제조 공정·멀티레이어 설계·블랭크 결함·소결 파라미터가 임상 결과로 이어지는 chain.

핵심 명제 7개:

1. **블록은 반제품이다 — 부분소결 상태로 밀링, 최종 소결에서 완제품** — 소결 선형 수축 20–25%이므로 CAM 확대계수(제조사 라벨, 예 1.23×) 입력이 적합도(fit)를 결정. 블록 교체 시 확대계수 갱신 필수. [미검증 — 일반 공정 지식·웹 출처]
2. **이트리아 함량이 성능을 결정** — Y₂O₃↑ → cubic↑ → 투명도↑·강도↓; 3Y-TZP 900–1200 → 4Y-PSZ 700–900 → 5Y-PSZ 600–700 → 6Y/UHTZ 500–600 MPa (Cesar 2024). [확인]
3. **조성경사형 멀티레이어가 현 시장 표준** — 3Y(치경부/구조) + 5Y(절연/교합) gradient; 구세대 층간 결함은 신규 분말 압축 기술로 해결 (Cesar 2024). [확인]
4. **네스팅 위치가 강도를 좌우** — 3Y/5Y 멀티레이어는 디스크 중심부 > 상단부; 5Y 단독은 RBFPD 하중 안전역 부족 (Waldecker 2026 in-vitro). [확인 — in-vitro]
5. **as-sintered 파절 기원은 밀링 결함** — 외재적(밀링 gouge·에지 칩) → 고연마 시 내재적(기공·결정군집·EDS 오염) 전환; 평균강도↑·Weibull 계수↓의 연마 역설 (Kwon 2024). [확인 — in-vitro]
6. **소결 프로토콜이 곧 신뢰성** — 표준 ≈8h/1500°C; 고속 소결(30–90분)은 일관성 미확립, HIP는 reliability↑이나 비표준 (Cesar 2024). [확인]
7. **임상가의 레버는 grade·두께·마감** — 블록 화학은 선택으로, 파절은 두께(≥1.5mm)와 마감(재연마)으로 통제; 접착은 grade 무관 APC. [확인]

## Results

### 축 1 — 블록 제조 워크플로

**핵심**: 블록은 "분말 → 성형 → 부분소결 → 밀링 → 최종소결"의 중간 산물이며, 각 단계가 최종 강도·적합도의 품질 관문이다.

| 단계 | 공정 | 임상적 함의 |
|---|---|---|
| 분말 제조 | 공침법(co-precipitation)으로 Y₂O₃ 균일 분포 (Tosoh·Noritake·Metoxit 등) | 분말 균질성 → 결정립·소결밀도 (Cesar 2024) [확인] |
| 성형 | 고압 압축(냉간 등방압, CIP) | 밀도 균일성 → 층간·내부 결함 좌우 |
| 부분소결 | ≈900–1000°C pre-sintering | 여기서 "블랭크(disk/puck)" 완성 — 밀링 가능하게 |
| CAD/CAM 밀링 | 카바이드 버, 5축, 20–25% 확대 | 밀링 결함(gouge·에지 칩)이 파절 기원 후보 (Kwon 2024) [확인] |
| 최종소결 | ≈1500°C, ≈2h | 수축·결정립 성장·완성 |
| 마감 (선택) | HIP / 연마·유약 | HIP는 reliability↑, 유약은 LTD 보호 못 함 |

- **확대 밀링(oversize milling)**: 블록은 소결 수축을 예상해 크게 깎는다. CAM이 확대계수(예 1.23×)를 적용하며, **배치별 편차가 있어 라벨 확인·소프트웨어 갱신이 remake 원인 통제의 핵심**이다. [미검증 — 웹 출처, 실무 공정 지식]
- **블록 두께/직경 규격**: 통상 Ø98.5mm 디스크, 높이 12–25mm(예: ZirCAD Prime 16mm). 디스크 높이와 레스토레이션 배치가 네스팅 가능 범위를 제한. [미검증 — 제조사 데이터]
- **chairside vs labside**: 1회 내원 chairside CAD/CAM(고속 소결 전제)과 labside(표준 소결)는 소결 프로토콜이 달라 신뢰성 논쟁의 중심(축 5).

**제조사 블록 라인업 비교 (참고)** — 아래는 웹·제조사 자료 수준으로 **전부 [미검증]**, 임상 결정 전 제조사 IFU·lab 검증 필요:

| 제조사 / 라인 | 멀티레이어 방식 | 대표 grade | 비고 |
|---|---|---|---|
| Ivoclar IPS e.max ZirCAD Prime | 3Y(치경부) + 전이층 + 5Y(절연) 이종 조성층 | 3Y/5Y 복합 | 디스크 16mm·절연층 18% 높이, 제조사 주장 ~1100–1200 MPa [미검증] |
| Ivoclar ZirCAD MT Multi / LT / MO | 조성·색조 gradient | MT Multi >6.5–8.0 Y₂O₃; LT/MO 4.5–6.0 Y₂O₃ | 라인별 이트리아 대역 상이 [미검증] |
| Kuraray Noritake KATANA | STML/HTML/UTML (HTML은 5Y 중심 층) | 4Y/5Y 계열 | "멀티레이어"라도 층 구성 기술이 ZirCAD와 다름 [미검증] |
| Glidewell BruxZir | monolithic 중심 | 3Y/4Y | 한국 수입, 비용 합리 [미검증] |
| 국산(DDS·HASS 등) | monolithic 3Y 중심 | 3Y-TZP | 후방부 합리적 옵션, 5Y 가용성 lab 의존 [미검증] |

- **핵심 함의**: 같은 "멀티레이어"라도 ①이종 조성층+전이층(Prime형) vs ②단일 5Y 소재 층(HTML형)으로 물성 분포가 다르다 — 블록 라인을 바꾸면 네스팅·색조·강도 가정을 다시 세워야 한다. [미검증 — 웹/in-vitro PMC]

### 축 2 — 화학 설계: 이트리아 → 결정상 → 강도/투명도

**핵심**: 블록의 grade는 곧 이트리아 몰%이고, 이것이 cubic 비율·투명도·강도·파괴인성을 한 줄로 결정한다.

| Generation | 이트리아/조성 | cubic | 굴곡강도 | 투명도 | 블록 용도 |
|---|---|---|---|---|---|
| 1세대 3Y-TZP(고알루미나 ~0.25wt%) | 3 mol% | <5% | 900–1200 MPa | 낮음 | 코어 전용(베니어) |
| 2세대 저알루미나 3Y-TZP | 3 mol% | <5% | 900–1100 MPa | 향상 | monolithic 후방 |
| 3세대 4Y-PSZ | 4 mol% | >30% | 700–900 MPa | 높음 | monolithic 전후방 |
| 4세대 5Y-PSZ | 5 mol% | >50% | 600–700 MPa | 매우 높음 | monolithic 심미 |
| UHTZ | >5 mol% | ~60% | 500–600 MPa | 최대 | 심미·저하중 |
| 멀티레이어 | gradient | 층별 | 3Y base + 5Y top | gradient | full contour |

- Spine: [[dental-materials/zirconia/cesar-2024-dental-zirconia-15years-material-processing]] (5,102편 서술적 고찰, 15년 taxonomy) — [[dental-materials/zirconia/ban-2023-dental-zirconia-types-development-review]]가 발전사·결정학으로 정합. [확인]
- **알루미나 트레이드오프**: 1세대의 소량 알루미나(~0.25wt%)는 소결성·입계강도를 올리지만 광투과를 낮춘다; 알루미나를 줄이고 이트리아를 늘리면 투명해지나 변태강화를 잃는다(Cesar 2024). [확인]
- **블록 선택의 함의**: "지르코니아 = 단일 재료" 사고가 블록 단위에서 깨진다 — 같은 제조사 블록 세트 안에서도 grade마다 적응증·두께·접착 민감도가 다르다. [확인]

### 축 3 — 멀티레이어 블록 (조성경사형)

**핵심**: 한 블록 안에 강한 3Y와 투명한 5Y를 층으로 넣어 심미와 강도를 동시에 얻는다 — 현재 표준.

- **구조**: 치경부/구조부 3Y-TZP + 절연부 5Y-PSZ, 사이에 전이층(transition layer). 예: IPS e.max ZirCAD Prime — 디스크 16mm, 절연층이 전체 높이의 18%, 3Y dentin + 전이 + 5Y incisal, 제조사 주장 굴곡강도 1100–1200 MPa. [미검증 — 제조사 데이터]
- **층 구성 기술은 제조사마다 다름**: ZirCAD Prime형(3Y/5Y 이종 층 + 전이층) vs KATANA Multilayered(5Y 단일 소재 층) — 같은 "멀티레이어"라도 물성 분포가 다르다. [미검증 — 웹/in-vitro PMC 출처]
- **층간 결함 해결**: 구세대는 전이부 밀도차 → 층간 결함 → 조기 파절; 신규 분말 압축 기술로 해결(Cesar 2024). [확인]
- **네스팅이 강도를 좌우**: [[prosthetic-materials/waldecker-2026-multilayer-zirconia-rbfpd-load-bearing]] — WR 1,025–1,617N > IR 684–1,216N; 3Y/5Y 멀티레이어 **중심 네스팅 > 상단**; **5Y 단독은 IR 최저(~684N)로 안전역 부족**; 인공 노화 영향 없음. [확인 — in-vitro]
- **실무 규칙**: 멀티레이어를 쓸 때 밀링 네스팅을 디스크 중심에 두고, 고하중 RBFPD·커넥터 부위에는 5Y 단독 배치를 피한다. [확인 — in-vitro]

### 축 4 — 블랭크 결함과 파절 기원

**핵심**: 파절의 상당 부분은 환자가 아니라 블록/밀링에서 시작한다 — 원인은 표면 상태에 따라 두 집단으로 나뉜다.

| 상태 | 지배적 파절 기원 | 평균 강도 | Weibull 계수(신뢰도) |
|---|---|---|---|
| As-sintered(임상 유사) | 외재적: 밀링 gouge·스크래치·에지 칩 | 낮음 | 높음(일관적) |
| 고연마 | 내재적: 기공·결정군집·EDS 이물질·corner flaw | 높음 | 낮음(불일관) |

- Spine: [[dental-materials/zirconia/kwon-2024-strength-limiting-defects-zirconia-cad-cam]] — 7종 blank, n=168, 4점 굽힘 + FE-SEM/EDS. [확인 — in-vitro]
- **연마 역설(polishing paradox)**: 연마는 표면 밀링 결함을 제거해 평균강도를 올리지만, 무작위 내재 결함을 드러내 신뢰도를 떨어뜨린다 — 어느 표면 상태도 명확히 우월하지 않다(Kwon 2024). [확인]
- **EDS 검출 오염물(Al·Si·Ca·Fe)**: 파절기원에서 확인 — 분말 오염 또는 bur 마모 파편 추정. **제조사별 블랭크 품질 차이는 임상적으로 중요하나 불투명한 위험 인자.** [확인 — in-vitro]
- **5Y 이질성**: 5Y 3종 중 2종은 연마해도 유의 변화 없음(소결 중 self-heal 추정), 1종은 강도↑·신뢰도↓ — 제조사 편차가 grade 편차보다 클 수 있다(Kwon 2024). [확인]
- **임상 함의**: 유약/경량 연마로 납품된 full-contour 보철은 밀링 결함을 활성 기원으로 유지한다. 교합 조정 등으로 새 grinding mark를 도입하면 즉시 재연마한다([[overviews/zirconia-material-clinical-overview]] Thread 3). [확인]
- **마감 관련 블록**: [[dental-materials/zirconia/ramos-2016-grinding-heat-treatment-zirconia-flexural]](연삭 손상의 열처리 회복), [[dental-materials/zirconia/mohammadi-bassir-2017-grinding-overglazing-polishing-zirconia]](과유약 > 연마의 강도 회복) — 단 유약은 LTD 보호가 아니다. [확인 — in-vitro]

### 축 5 — 소결: 수축률·프로그램·고속소결·HIP

**핵심**: 소결은 블록이 완제품이 되는 단계이며, 온도·시간이 결정립 크기와 상 안정성을 좌우한다.

- **표준 프로그램**: 예 — 900°C 예열 유지 30분 → 1500°C 승온·유지 12분 → 냉각; 총 ≈8시간 규모(제조사 3상 프로토콜). [미검증 — 제조사 IFU]
- **소결 프로토콜 비교**: 온도·유지시간·승온 속도가 결정립 성장과 상 안정성을 좌우하므로, 고속 프로그램은 강도·적합도를 재검증해야 한다. [미검증]

| 프로토콜 | 시간 | 온도 | 근거 상태 | 임상 함의 |
|---|---|---|---|---|
| 표준 labside | ≈6–8h | ≈1500°C, 유지 ~12분 | 확립 | 기본값, 적합도·강도 예측 가능 |
| 고속(express) | 30–90분 | 제조사별 상이 | 미성숙(Cesar 2024) | chairside 1회 내원용 — 일관성·강도 패널티 우려 [확인, 다만 정량은 미검증] |
| HIP(후처리) | — | 소결 −100–200°C, 등압 | 효과 인정·비표준 | 기공·연마 결함 치유 → reliability↑ [확인] |

- **수축률**: 부분소결 블록은 선형 20–25%(용적 49–57%) 수축 → 적합도는 확대계수 정확도에 직결. [미검증 — 일반 공정 지식·웹 출처]
- **고속 소결(30–90분)**: Cesar 2024가 **"일관된 임상 신뢰성 위해 추가 개발 필요"로 미성숙 판정**. [확인]
- **적합도와 급속 소결의 상호작용**: "급속 소결이 3Y 적합도는 개선하나 4Y 적합도는 저하"라는 최근 JPD 보도가 있으나 소셜 미디어 요약만 확보 — **원문 확인 전 인용 금지, [미검증]으로만 취급**. [미검증]
- **HIP(열간등방압)**: 소결 온도보다 100–200°C 낮은 온·압에서 기공·연마 결함을 치유해 신뢰성↑ — 그러나 아직 임상 표준 아님(Cesar 2024). [확인]
- **3D 프린팅 지르코니아**: 유망하나 아직 임상 사용 불가 수준(Cesar 2024). [확인]
- **결정립-상 안정성**: 결정립이 커지면 정방상이 불안정해져 LTD 취약↑ — 3Y-TZP가 가장 취약하고 5Y는 cubic 비율이 높아 덜하다([[dental-materials/zirconia/chopra-2024-mechanical-characteristics-zirconia-dentistry]], [[dental-materials/zirconia/koenig-2021-ltd-monolithic-zirconia-prospective]], [[dental-materials/zirconia/koenig-2024-ltd-monolithic-zirconia-5year-prospective]]). [확인]

### 축 6 — 임상 선택 매트릭스 (블록 관점)

**1차 권고**: grade로 강도/심미를 고르고, 멀티레이어로 층간 설계를 고르고, 제조사 라벨로 적합도를 지킨다. 무엇을 고르든 두께와 접착은 불변.

| 임상 시나리오 | 추천 블록 | 피할 블록 | 근거 |
|---|---|---|---|
| 후방부 단관(고하중, 비이갈이) | 3Y-TZP monolithic | UHTZ(500–600 MPa 부족) | Cesar 2024, Warreth 2020 |
| 전치부 단관(심미) | 5Y-PSZ 또는 3Y/5Y 멀티레이어 | — | Cesar 2024 |
| 전치부 short-span FPD | 4Y-PSZ 또는 멀티레이어 | 5Y 단독 | Waldecker 2026 |
| 후방 장경간 FPD(4 unit+) | 3Y 코어 + 베니어 또는 monolithic 3Y | 5Y 계열 | Saravi 2021 SR+MA |
| RBFPD/IRFPD | 3Y/5Y 멀티레이어(중심 네스팅) | 5Y 단독 | Waldecker 2026 |
| 이갈이 환자 | grade 무관 monolithic + 교합 보호 | 베니어(칩핑) | Leitão 2022 |

- **두께가 grade보다 앞선다**: 모든 grade 공통 최소 교합면 1.5mm, <1mm 시 파절 급증([[dental-materials/ali-2023-cadcam-restoration-failure-reasons-sr-ma]]). "지르코니아는 강하니 최소삭제 OK"는 오판. [확인]
- **접착은 grade 불변**: 50µm Al₂O₃ 분사 + MDP 프라이머 + 레진 시멘트(APC). 5Y(cubic)도 MDP 반응성 유지([[dental-materials/zirconia/comba-2021-chemical-bonding-cubic-zirconia]]). SOP 상세는 [[overviews/dental-materials-decision-ladder]] 위임. [확인]
- **박형 부분피개**: 초박형 0.5mm 멀티레이어는 크라운보다 부분피개가 유리하나 크라운은 ≥1.0mm 필요([[inlay/spitznagel-2025-multilayer-zirconia-partial-coverage-fatigue]]). [확인 — in-vitro]

### 근거 한계 · 미검증

- **소결 수축 수치·확대계수 운용·제조사 IFU 스펙**: 본 페이지의 웹 출처·일반 공정 지식 수준으로, 위키 논문 근거 아님 — clinical decision에 쓰려면 제조사 문서·lab 검증 필요. [미검증]
- **제조사 주장 물성**(예: Prime 1100–1200 MPa)은 마케팅 데이터로 독립 시험치와 다를 수 있음. [미검증]
- **층 경계부 장기 임상 데이터 부족**: 멀티레이어는 in-vitro·단기만; 층별 강도 편차의 장기 영향 미확립. [미검증]
- **급속 소결 적합도 연구**: 단일·약한 출처(소셜 요약). [미검증]
- **한국 블록 가용성**(Katana STML/UTML·ZirCAD·BruxZir·국산 DDS/HASS): 자매 오버뷰가 [미검증]으로 표기 — 본 페이지도 승계. [미검증]

## Phase 2 확장 후보 (Stub)

- [ ] `wiki/overviews/multilayer-zirconia-color-zone-matching.md` — 멀티레이어 gradient 색조·네스팅 SOP (자매 오버뷰 stub 승계).
- [ ] `wiki/overviews/zirconia-sintering-protocol-fit-overview.md` — 표준 vs 고속 소결 × 적합도·강도 정량 (축 5에 개요만 부분 반영).
- [ ] `wiki/overviews/zirconia-blank-quality-manufacturer-comparison.md` — 제조사·배치별 기공·오염·Weibull 비교 (축 1에 라인업 표로 부분 반영, Kwon 2024 후속).
- [ ] `wiki/overviews/zirconia-aging-ltd-hydrothermal.md` — LTD hydrothermal aging (자매 오버뷰 stub 승계).

## 한국 임상 환경 조정 사항

- **Katana (Kuraray)** — STML/HTML/UTML 계열. HTML은 5Y 중심 멀티레이어로 층 구성 기술이 ZirCAD와 다름 [미검증]. 전치부 1순위 관행 [[overviews/zirconia-types-clinical-selection]].
- **IPS e.max ZirCAD (Ivoclar)** — Prime(3Y/5Y+전이층), MT Multi/LT 등; 멀티레이어 매칭 우수 [미검증 — 제조사].
- **BruxZir·국산(DDS·HASS 등)** — 가용성·grade 편차 [미검증].
- **Lab 협의 항목**: ①블록 grade·제조사 ②확대계수/소결 프로그램 ③네스팅 위치(중심) ④고속 소결 사용 여부. 네 가지를 케이스마다 확인하는 것이 블록 리스크 통제의 실무.
- Preparation·접착 protocol은 [[overviews/zirconia-types-clinical-selection]]·[[overviews/dental-materials-decision-ladder]] 위임.

## Related Papers

### spine (본문 인용)

- [[dental-materials/zirconia/cesar-2024-dental-zirconia-15years-material-processing]] — 15년 세대분류·분말·소결·멀티레이어 spine
- [[dental-materials/zirconia/ban-2023-dental-zirconia-types-development-review]] — 타입 발전사·결정학 정합
- [[dental-materials/zirconia/kwon-2024-strength-limiting-defects-zirconia-cad-cam]] — 블랭크 결함·연마 역설·EDS 오염 spine
- [[dental-materials/zirconia/chopra-2024-mechanical-characteristics-zirconia-dentistry]] — 변태강화·LTD·피로 기전
- [[prosthetic-materials/waldecker-2026-multilayer-zirconia-rbfpd-load-bearing]] — 멀티레이어 네스팅·하중 지지능
- [[dental-materials/ali-2023-cadcam-restoration-failure-reasons-sr-ma]] — 두께 <1mm 파절 위험
- [[dental-materials/zirconia/comba-2021-chemical-bonding-cubic-zirconia]] — 5Y MDP 결합
- [[inlay/spitznagel-2025-multilayer-zirconia-partial-coverage-fatigue]] — 박형 멀티레이어 두께×피로

### Related overviews

- [[overviews/zirconia-material-clinical-overview]] — 자매: 재료과학·세대·생존율·LTD·파절수리 (본 페이지 = 블록 제조·결함·소결)
- [[overviews/zirconia-types-clinical-selection]] — 자매: grade × 적응증 5축 (본 페이지 = 그 grade를 만드는 블록)
- [[overviews/dental-materials-decision-ladder]] — 부모: 재료 4축 (접착·CAD/CAM vs PFM·아말감·시멘트)
- [[dental-materials/ceramic/warreth-2020-all-ceramic-restorations-narrative-review]] — 세라믹 강도 위계 배경
- [[dental-materials/zirconia/miyazaki-2013-current-status-zirconia-restoration-review]] — CAD/CAM 지르코니아 개발사·총론

### 마감·가공 관련 블록

- [[dental-materials/zirconia/ramos-2016-grinding-heat-treatment-zirconia-flexural]]
- [[dental-materials/zirconia/mohammadi-bassir-2017-grinding-overglazing-polishing-zirconia]]
- [[dental-materials/zirconia/kosmac-1999-grinding-sandblasting-flexural-strength-zirconia]]
- [[dental-materials/zirconia/oh-2016-zirconia-core-fitness-four-bur-types]]
- [[dental-materials/zirconia/steiner-2024-zirconia-conditioning-glazing-enamel-wear]]
- [[dental-materials/zirconia/aljomard-2022-enamel-wear-monolithic-zirconia-sr-ma]]

## 원장 메모 체크리스트

- [ ] Lab 블록 목록화 — 사용 중인 제조사·grade·확대계수·소결 프로그램 문서화.
- [ ] 네스팅 SOP — 멀티레이어·고하중 케이스는 중심 네스팅 요청을 lab에 명시.
- [ ] 두께 protocol — 전 grade 최소 교합면 1.5mm prep 가이드 환자·lab 공유.
- [ ] chairside 마감 — 교합 조정 후 재연마(연마 kit) 루틴화, 유약 재처리 금지(LTD 비보호).
- [ ] 고속 소결 여부 확인 — chairside 사용 시 근거 약함 인지, 제조사 프로그램 준수.
- [ ] 환자 안내 — "블록 grade에 따라 강도·심미 다름" 평어 설명서.

확신도 등급 글로벌:
- 축 1 제조 워크플로 = [확인] (narrative) + 수축 수치 [미검증].
- 축 2 화학·세대 = [확인] (narrative 정량).
- 축 3 멀티레이어 = [확인] (narrative + in-vitro), 제조사 층구조 [미검증].
- 축 4 블랭크 결함 = [확인] (in-vitro fractography).
- 축 5 소결 = [확인] (narrative), 고속소결 적합도 [미검증].
- 축 6 임상 선택 = [확인] (SR+MA + in-vitro 파생).
- 한국 가용성 = [미검증].
