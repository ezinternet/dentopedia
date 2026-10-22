# Bone Graft Biological Properties (골형성 · 골유도 · 골전도) — Surveillance 2026-10-22

토픽 키: `bone-graft-properties` (신규 토픽 · 전 기간 백필)

---

## 도구 메모 (환경 차이 — 재현 시 주의)

- 이 세션에는 **PubMed MCP가 노출되지 않았다** (MCP 리소스 0건, 코드모드 툴 카탈로그에 PubMed 검색 도구 없음).
- 대신 **NCBI E-utilities**(esearch · esummary · efetch)를 직접 호출했다. PubMed MCP가 래핑하는 것과 **동일한 백엔드이며 쿼리 문법도 동일**하므로 스위프 결과는 MCP 경로와 동일하다.
- OA 판정용 **NCBI PMC OA service(`oa.fcgi`)는 404로 폐기됨** → 라이선스는 **Europe PMC REST API**(`resultType=core`)에서 조회했다. Europe PMC의 `license` 필드를 대문자 표기로 정규화(CC BY / CC BY-NC / CC BY-NC-ND / unknown).
- 신규 토픽이므로 **water-mark 미적용 전 기간 백필**로 돌렸다.

---

## 쿼리 (4 stems · ptyp = RCT + SR + MA)

`state.json`의 `bone-graft-properties.query`에 고정(4 stem을 OR로 묶은 단일 문자열). stem별 실측 카운트:

| stem | 축 | hit |
|---|---|---|
| `P-osteoinduction` | osteoinduct* · BMP · DBM | 210 |
| `P-osteoconduction` | osteoconduct* · bone conduction | 63 |
| `P-osteogenesis` | osteogenic* · osteogenesis · bone forming | 274 |
| `P-material-properties` | 이식재 종류 × 특성 표현 동시 등장 | 122 |
| **합집합(중복 제거)** | | **515** |

**노이즈**: `"bone graft"`/`"bone substitute"`가 맥락 항목으로 들어 있어 **정형외학(척추·장골·발목·종양)·뼈 대사·전신골** 논문이 대량으로 섞인다(제외 255건 중 124건이 그쪽). `alveolar`는 "inferior alveolar nerve"도 잡는다. `osteoinduct*` + BMP는 치과 맥락 없는 세포실험을 끌어온다.

---

## 파이프라인

| 단계 | 건수 |
|---|---|
| 검색 합집합 | 515 |
| − 기보유(PMID·DOI·제목 교차) | −15 → 500 |
| − seen / screened_out(상태 버킷) | −17 → **483 스크리닝 대상** |
| 스크리너 판정 (4배치 병렬, 3-way) | include 217 / borderline 94 / exclude 172 |
| 상위 모델 직접 판정 (borderline 94건 초록 확인) | include 11 / exclude 83 |
| **최종** | **include 228 / exclude 255** |
| 큐 적립 (`.surveillance/queue.md`) | 228건 (OA:PMC 50, OA:none 178) |
| screened-out 버킷 | 255건 (`.surveillance/screened-out.md` + `state.json`) |

**큐 ptyp 분포**: SR / SR+MA / MA / RCT 혼재. **OA 라이선스**: CC BY 33 · CC BY-NC 6 · CC BY-NC-ND 8 · unknown 3.

---

## 티어 정의 (큐 안에서의 우선순위 — 사람이 ingest 순서 결정)

| 티어 | 정의 | 건수 |
|---|---|---|
| **A** | 이식재·골대체재의 **생물학적 특성 자체**를 다루는 논문(골전도/골유도/골형성、组织계측·신생골 비율·잔존 이식재·입자 크기·bioactive glass·P-15·치아유래 이식재) | 122 |
| **B** | **골유도 보조**(BMP-2, PRF/PRP, 멜라토닌·호르몬, MSC/exosome, 스캐폴드) | 50 |
| **C** | **임플란트 표면·골유착** 축(osseointegration, 코팅, PEEK/TiO2) | 6 |
| **D** | 주변 맥락(교정·DO·치주 일반 등) — 낮은 우선순위 | 50 |

---

## 우선 ingest 후보 (Tier A · 축 연결 확인된 것만 추림)

| PMID | 제목 | 저널 | 연 | ptyp | OA |
|---|---|---|---|---|---|
| 39901815 | Clinical efficacy and safety of P-15 peptide enhanced bone graft substitute in surgical bone regenerative procedures in adult maxillofacial, spine, and trauma patients : a systematic literature review | Bone & joint research | 2025 | SR | OA:PMC11795317 (CC BY-NC-ND) |
| 36645164 | Osteoinductive calcium phosphate with submicron topography as bone graft substitute for maxillary sinus floor augmentation: A translational study | Clinical oral implants research | 2023 | RCT | OA:none |
| 41526568 | Clinical efficacy of bioactive glass in periodontal regeneration: a systematic review and meta-analysis | Odontology | 2026 | SR+MA | OA:none |
| 37047413 | Osteogenic Potential of Autologous Dentin Graft Compared with Bovine Xenograft Mixed with Autologous Bone in the Esthetic Zone: Radiographic, Histologic and Immunohistochemical Evaluation | International journal of molecular sciences | 2023 | RCT | OA:PMC10094989 (CC BY) |
| 38905116 | Maxillary Sinus Augmentation with Anorganic Bovine Bone Mineral of Different Particle Sizes: A Split-Mouth Study with Histomorphometric, Radiographic, and Clinical Analyses | Int J Oral Maxillofac Implants | 2024 | RCT | OA:none |
| 35511290 | Histomorphometric evaluation of different graft associations for maxillary sinus elevation in wide antral cavities: a randomized controlled clinical trial | Clinical oral investigations | 2022 | RCT | OA:none |
| 39946741 | Vertical Guided Bone Regeneration: Leukocyte and PRF Bone Block vs a Mixture of Autogenous Bone with DBBM: A Split-Mouth RCT with up to 1 Year of Follow-up After Implant Loading | Int J Periodontics Restorative Dent | 2026 | RCT | OA:none |
| 40459982 | Local Delivery of Melatonin Along With Bone Grafts to Improve Osteogenesis | J Craniofac Surg | 2025 | SR | OA:none |
| 40214305 | Local Delivery of Various Hormonal Drugs Along With Bone Grafts to Improve Osteogenesis: A Systematic Review | J Craniofac Surg | 2025 | SR | OA:none |
| 41699617 | Evaluation of osteogenic effects following alveolar bone augmentation with corticotomy | BMC oral health | 2026 | RCT | OA:PMC13014984 (CC BY-NC-ND) |
| 38922797 | Randomized split-mouth clinical trial comparing osteoblastic activity and osteogenic potential of autogenous particle harvesting during implant surgery without irrigation and with irrigation | Clin Implant Dent Relat Res | 2024 | RCT | OA:none |
| 36751833 | Efficacy of rh-PDGF-BB and Emdogain with or without DFDBA using M-MIST in the treatment of intrabony defects | Nigerian J Clin Pract | 2023 | RCT | OA:none |
| 42740456 | Use of cells and/or biologics combined with scaffolds in alveolar bone augmentation for implant site development | Journal of periodontology | 2026 | SR | OA:PMC13575443 (CC BY) |
| 39478364 | The Clinical Efficacy and Safety of ErhBMP-2/BioCaP/β-TCP as a Novel Bone Substitute Using the Tooth-Extraction-Socket-Healing Model: A Proof-of-Concept RCT | J Clin Periodontol | 2025 | RCT | OA:PMC11743062 (CC BY-NC-ND) |
| 35224778 | Maxillary sinus floor augmentation comparing bovine versus porcine bone xenografts mixed with autogenous bone graft. A split-mouth RCT | Clin Oral Implants Res | 2022 | RCT | OA:PMC9313845 (CC BY-NC-ND) |
| 36305933 | Comparative Assessment of Bovine Versus Porcine Xenograft for Augmentation: A Randomized Prospective Cohort Study | Int J Periodontics Restorative Dent | 2022 | RCT | OA:none |
| 39849313 | Histomorphometric and Immunohistochemical Evaluation of Bone Healing Around Implants Placed Using Piezosurgery vs Conventional Drills: A Split-Mouth Pilot Study | J Oral Implantol | 2025 | RCT | OA:none |
| 39273529 | Revolutionizing Bone Regeneration with Grinder-Based Dentin Biomaterial: A Systematic Review | Int J Mol Sci | 2024 | SR | OA:PMC11394881 (CC BY) |

Tier B(골유도 보조) 상위: 42471687(BMP-2 구강·악안면 골증강 SR+MA, OA), 42382924(rhBMP-2 치조 cleft MA, OA). Tier A 안에도 BMP·MSC 계열이 섞여 있다 — 41944755(rhBMP-2 대 자가골 SR), 41289609(buccal fat pad MSC 상악동 SR, OA), 41052564(광생물조调控 MSC 골형성 SR).

---

## 이미 보유(중복 제외 15건)

| PMID | 연 | 제목(요약) |
|---|---|---|
| 42562852 | 2026 | Natural bovine bone + HA의 즉시임플란트 골유착 평가 |
| 42556907 | 2026 | Melatonin 보조 비수술 치주치료 SR+MA |
| 42310175 | 2026 | UV 광기능화 임플란트 표면 |
| 42174333 | 2026 | 탈민 치아기질(autogenous DDM) 대 이종골 histology |
| 42168967 | 2026 | 치아유래 막 대 e-PRF GBR 2년 |
| 41715114 | 2026 | Schneiderian membrane의 osteogenic potential 조직계측 |
| 39755940 | 2025 | Gelatin/PLA 막 비교 |
| 39392473 | 2024 | Bioactive surface modification SR+MA(osseointegration) |
| 39317600 | 2024 | Socket preservation regeneratve graft SR+MA |
| 38050282 | 2023 | 자가골 치아기질 이식 ARP SR+MA |
| 36225604 | 2022 | Biomolecule bioactive surface SR |
| 35841608 | 2022 | Biologics for ARP/ISD (AAE position) |
| 35048503 | 2022 | Vertical GBR healing complications SR |
| 19821311 | 2009 | Cochrane 수평·수직 증대술 SR |
| 12519332 | 2002 | 원신 Ossix 막 vs 표준막 histology |

→ **프레임워크 논문 3종(골형성/골유도/골전도 정의)은 이미 기보유**: `wiki/bone-regeneration/misch-1993-bone-grafting-materials-implant-dentistry.md`, `wiki/bone-regeneration/zhao-2021-bone-grafts-substitutes-dentistry-review.md`, `wiki/bone-regeneration/haugen-2026-bone-grafts-everything-you-need.md`. 이번 스위프는 **프레임워크를 뒤집는 실증 근거(신생골 비율·잔존 이식재·입자 크기·생물활성)**를 채운다.

---

## 제외 사유 분포 (255건)

| 카테고리 | 건수 |
|---|---|
| 비치과(척추·장골·발목·종양 재건·전신골 대사) | 124 |
| 치주·약물·기타(_STATIN·alendronate·GLP-1·두부·미세출혈 등) | 53 |
| 치과 맥락이나 축 약함(교정·DO·치수·PAOO 중심) | 39 |
| 교정·수술기법만(DO·PAOO·안면접근술식) | 27 |
| 임플란트 표면·골유착 축(티타늄·PEEK 코팅) | 12 |

→ 전부 `screened_out` 버킷에 기록됨(`restore-screened`로 복구 가능, `seen_pmids`에는 들어가지 않음).

---

## 커버리지 평가

| 축 | 현재 위키 커버리지 | 이번 스위프가 채우는 공백 |
|---|---|---|
| 4대 특성(골형성/골유도/골전도/골유착) 정의 | misch-1993, zhao-2021, haugen-2026 | — (완료) |
| 이식재 잔존 비율·전환(turnover) | rao-2026, benic-2014, thomas-2026 | 다중 재료 비교 RCT (35511290, 35224778, 36305933, 38905116) |
| 생물활성(bioactive)·골유도성 첨가제 | **부족** | 36645164(골유도성 CaP), 39901815(P-15), 41526568(bioactive glass SR+MA), 39478364(ErhBMP-2/BioCaP) |
| 이식재 크기·형태가 골형성에 미치는 영향 | **부족** | 38905116(입자 크기 split-mouth) |
| 호르몬·성장인자 보조의 골형성 효과 | **부족** | 40459982·40214305(멜라토닌·호르몬), 42471687(BMP-2) |
| 치아유래 이식재의 골형성 잠재력 | 부분(42174333 기보유) | 37047413, 39273529( grinder dentin) |

**커버리지 판단**: 특성 *정의*는 이미 두텁고, **초록에서 명시하는 특성 정량(신생골 %, 잔존 이식재 %, 흡수 속도)** 이 약하다. 이번 228건이 그 구간을 채운다.

---

## 다음 단계

1. Tier A 122건 중 **OA:PMC 26편**부터 ingest 우선(오픈액세스 = PDF 확보 비용 0). 티어별 PMC: A 26 · B 14 · C 1 · D 9.
2. `bone-graft-material` 토픽(2026-10-21) 큐 49건 중 **6건이 이번 검색 합집합과 겹쳤다** — 이미 `seen`이므로 이번 큐에는 재적립되지 않았다(실제 중복 적립 0건). ingest 시 두 토픽의 실질적 중복만 확인할 것.
3. `restore-screened --topic bone-graft-properties`로 제외분 재심 가능(특히 Tier D 39건).
4. 동일 축의 **후속 스위프는 water-mark 모드**(PMID > 42867553)로 전환 — 지금 상태에선 `last_run_edat = 2026/10/22` 기준.
