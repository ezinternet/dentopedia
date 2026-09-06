# 논쟁 레이더 백필 후보 — 2026-09-05

명시적 충돌 표현이 있으나 그 쌍에 `relations:` 타입 엣지(어떤 타입이든)도 `superseded_by:` 포인터도 없는 후보. **이 목록은 신호일 뿐 — 두 페이지를 읽고 판단해 엣지를 단다.**

**카드 읽는 법**: 각 카드는 `출발페이지 —[충돌유형·한글뜻]→ 대상페이지` 형태다. 아래에 (1) **근거 문장**(위키 본문에서 충돌 표현이 나온 실제 문장), (2) **양쪽 페이지의 `## 세줄요약`**(한국어)을 붙여, 페이지를 열지 않고도 두 논문이 각각 무엇을 주장하는지·정말 충돌하는지 한글로 판단할 수 있게 했다. 충돌 유형 한글뜻은 표현 매칭 기반 근사치이며, **최종 판단은 사람/LLM 몫**이다. (reinforces가 맞는 경우도 있으니 키워드를 그대로 엣지로 옮기지 말 것 — 2026-07-17 전수 검토에서 contradicts 계열로 지목된 122건 중 실제 contradicts는 1건이었다.)

**대상은 키워드에 가장 가까운 링크로 특정한다.** 같은 줄의 나머지 링크는 충돌 표현의 대상이라는 근거가 없어 Tier 2(`AMBIG→`)로 강등된다 — 버리지 않으니 진짜 대상이 강등됐다면 Tier 2에서 찾을 수 있다.

- Tier 1 (대상 지목됨, actionable): **1**
- Tier 2 (대상 불명/soft, review): **60**
- (억제됨) 이미 typed 엣지·supersession 포인터가 있어 제외: **294** · 부정문 제외: **111** · 검토·불필요 대장: **451** · 동일 줄 비최근접으로 Tier 2 강등: **0**

## Tier 1 — 판단 후 엣지 달 후보 (page → 지목된 target)

### orthodontics/clear-aligner

- `pham-2026-clear-aligner-deep-bite-rct`  —[대비되는 · 대비]→  **`charoenrat-2025-clear-aligner-anterior-open-bite-molar-intrusion-sr-ma`**
  - **근거 문장**: 심부교합(deep bite)에 대한 투명교정의 임상 효능과 환자 만족도를 비교한 RCT로, [[orthodontics/clear-aligner/charoenrat-2025-clear-aligner-anterior-open-bite-molar-intrusion-sr-ma]]가 다룬 개방교합과 대비되는 수직부조화(심부교합) 쪽 투명교정 적용 근거를 제공한다.
  - ▸ 출발(`pham-2026-clear-aligner-deep-bite-rct`) 세줄: 심부교합 환자에서 투명교정(CAT) 대 고정교정의 임상 효능과 환자 만족도를 비교한 베트남 국립병원 RCT. CAT는 유의하게 짧은 치료 기간(20.77±6.43개월 대 27.47±4.81개월, P<.001)을 보였으며, 심부교합 개선(P=.461)과 양악 겹침 감소(P=.603)는 두 그룹 간 유의한 차이 없음. 환자 만족도는 모든 범주에서 CAT 그룹이 유의하게 높았음(P<.001). 고정교정은 수직 안면 치수에 더 큰 영향을 미쳤음.
  - ▸ 대상(`charoenrat-2025-clear-aligner-anterior-open-bite-molar-intrusion-sr-ma`) 세줄: SR+MA (PRISMA/PROSPERO, 10편 — non-RCT 4편·전후비교 6편): 전치부 개방교합 교정에서 투명교정(Clear Aligner Treatment, CAT)과 TAD 병용 고정식 장치(FATADs)를 비교. CAT는 절치 정출(상악 +0.87 mm, 하악 +1.06 mm)로 overbite를 +2.77 mm 증가시키나 구치 압하는 유의하지 않았고, FATADs는 구치 압하(상악 +1.88 mm, 하악 +0.45 mm)를 통해 CAT보다 +1.64 mm 더 큰 overbite 


## Tier 2 — 대상 식별 필요 / soft signal (review only)

- `christopoulou-2022-intraoral-scanners-orthodontics-critical-review` [digital-workflow] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Accuracy and duration results across the included studies were contradictory — some found IOS as accurate as alginate, others found conventional impressions significantly more precise, with no consistent time advantage either way; patients generally preferred digital scanning and reported reduced gag reflex (two studies found 100% patient preference for IOS), but operator experience/learning curve
  - ▸ 출발(`christopoulou-2022-intraoral-scanners-orthodontics-critical-review`) 세줄: 서술적 critical review(7개 DB, inception–2020.10 전수검색 + 회색문헌 손검색; PRISMA·PROSPERO 없음, 비뚤림위험 평가 없음): 교정과(orthodontics) 임상시험을 대상으로 구강스캐너(Intraoral Scanner, IOS)의 정확도·재현성·소요시간·환자 편의/선호·술자 경험을 재래식(알지네이트/PVS) 인상과 비교 종합. 포함 연구 간 정확도·소요시간 결과가 상충 — 일부는 IOS가 알지네이트만큼 정확하다 했고, 다른 연구는 재래식 인상이 유의

- `christopoulou-2022-intraoral-scanners-orthodontics-critical-review` [digital-workflow] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 포함 연구 간 정확도·소요시간 결과가 상충 — 일부는 IOS가 알지네이트만큼 정확하다 했고, 다른 연구는 재래식 인상이 유의하게 더 정밀하다 했으며, 시간 면에서도 일관된 우위가 없었음; 환자는 대체로 디지털 스캔을 선호하고 구역반사 감소를 보고했음(두 연구에서 환자 선호도 100%), 다만 술자 경험·학습곡선이 결과에 영향을 미치는 주요하지만 충분히 규명되지 않은 교란변수로 반복 확인됨.
  - ▸ 출발(`christopoulou-2022-intraoral-scanners-orthodontics-critical-review`) 세줄: 서술적 critical review(7개 DB, inception–2020.10 전수검색 + 회색문헌 손검색; PRISMA·PROSPERO 없음, 비뚤림위험 평가 없음): 교정과(orthodontics) 임상시험을 대상으로 구강스캐너(Intraoral Scanner, IOS)의 정확도·재현성·소요시간·환자 편의/선호·술자 경험을 재래식(알지네이트/PVS) 인상과 비교 종합. 포함 연구 간 정확도·소요시간 결과가 상충 — 일부는 IOS가 알지네이트만큼 정확하다 했고, 다른 연구는 재래식 인상이 유의

- `christopoulou-2022-intraoral-scanners-orthodontics-critical-review` [digital-workflow] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: This is a self-labeled "critical review" (not a formal systematic review) that searched seven databases (PubMed, CENTRAL, Cochrane Reviews, Scopus, Web of Science, Clinical Trials, Proquest) from inception to October 2020, plus hand-searched gray literature, to synthesize orthodontic clinical trials on intraoral scanner (IOS) performance. It covers accuracy, reproducibility, duration, patients' ti
  - ▸ 출발(`christopoulou-2022-intraoral-scanners-orthodontics-critical-review`) 세줄: 서술적 critical review(7개 DB, inception–2020.10 전수검색 + 회색문헌 손검색; PRISMA·PROSPERO 없음, 비뚤림위험 평가 없음): 교정과(orthodontics) 임상시험을 대상으로 구강스캐너(Intraoral Scanner, IOS)의 정확도·재현성·소요시간·환자 편의/선호·술자 경험을 재래식(알지네이트/PVS) 인상과 비교 종합. 포함 연구 간 정확도·소요시간 결과가 상충 — 일부는 IOS가 알지네이트만큼 정확하다 했고, 다른 연구는 재래식 인상이 유의

- `christopoulou-2022-intraoral-scanners-orthodontics-critical-review` [digital-workflow] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Documents genuinely contradictory accuracy findings: e.g., Lythos digital models were reported as accurate as conventional impressions for occlusal/linear measurements, while other trials found conventional materials significantly more precise than digital; maxillary scans were reported less accurate than mandibular scans.
  - ▸ 출발(`christopoulou-2022-intraoral-scanners-orthodontics-critical-review`) 세줄: 서술적 critical review(7개 DB, inception–2020.10 전수검색 + 회색문헌 손검색; PRISMA·PROSPERO 없음, 비뚤림위험 평가 없음): 교정과(orthodontics) 임상시험을 대상으로 구강스캐너(Intraoral Scanner, IOS)의 정확도·재현성·소요시간·환자 편의/선호·술자 경험을 재래식(알지네이트/PVS) 인상과 비교 종합. 포함 연구 간 정확도·소요시간 결과가 상충 — 일부는 IOS가 알지네이트만큼 정확하다 했고, 다른 연구는 재래식 인상이 유의

- `christopoulou-2022-intraoral-scanners-orthodontics-critical-review` [digital-workflow] (HIGH-no-target, 'Contradict' · 반박·충돌)
  - **근거 문장**: | Accuracy | Contradictory across studies — some show IOS as accurate as alginate; others show conventional impressions significantly more precise. Maxillary scans less accurate than mandibular. |
  - ▸ 출발(`christopoulou-2022-intraoral-scanners-orthodontics-critical-review`) 세줄: 서술적 critical review(7개 DB, inception–2020.10 전수검색 + 회색문헌 손검색; PRISMA·PROSPERO 없음, 비뚤림위험 평가 없음): 교정과(orthodontics) 임상시험을 대상으로 구강스캐너(Intraoral Scanner, IOS)의 정확도·재현성·소요시간·환자 편의/선호·술자 경험을 재래식(알지네이트/PVS) 인상과 비교 종합. 포함 연구 간 정확도·소요시간 결과가 상충 — 일부는 IOS가 알지네이트만큼 정확하다 했고, 다른 연구는 재래식 인상이 유의

- `christopoulou-2022-intraoral-scanners-orthodontics-critical-review` [digital-workflow] (HIGH-no-target, 'Contradict' · 반박·충돌)
  - **근거 문장**: | Duration | Contradictory overall; alginate chairside time typically shorter than digital in most studies; powder-free next-gen scanners reduce both chairside and processing time. |
  - ▸ 출발(`christopoulou-2022-intraoral-scanners-orthodontics-critical-review`) 세줄: 서술적 critical review(7개 DB, inception–2020.10 전수검색 + 회색문헌 손검색; PRISMA·PROSPERO 없음, 비뚤림위험 평가 없음): 교정과(orthodontics) 임상시험을 대상으로 구강스캐너(Intraoral Scanner, IOS)의 정확도·재현성·소요시간·환자 편의/선호·술자 경험을 재래식(알지네이트/PVS) 인상과 비교 종합. 포함 연구 간 정확도·소요시간 결과가 상충 — 일부는 IOS가 알지네이트만큼 정확하다 했고, 다른 연구는 재래식 인상이 유의

- `christopoulou-2022-intraoral-scanners-orthodontics-critical-review` [digital-workflow] (HIGH-far→singh-2025-intraoral-scanners-accuracy-umbrella-review, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[digital-workflow/singh-2025-intraoral-scanners-accuracy-umbrella-review]] — later umbrella review (10 SRs, sr+ma) reaching more decisive conclusions on device ranking (TRIOS 3/Primescan highest full-arch accuracy) and time/comfort advantages than this 2022 review's "contradictory, more research needed" stance on the same questions; adjudicated 2026-09-04 as **not** a supersession — different q
  - ▸ 출발(`christopoulou-2022-intraoral-scanners-orthodontics-critical-review`) 세줄: 서술적 critical review(7개 DB, inception–2020.10 전수검색 + 회색문헌 손검색; PRISMA·PROSPERO 없음, 비뚤림위험 평가 없음): 교정과(orthodontics) 임상시험을 대상으로 구강스캐너(Intraoral Scanner, IOS)의 정확도·재현성·소요시간·환자 편의/선호·술자 경험을 재래식(알지네이트/PVS) 인상과 비교 종합. 포함 연구 간 정확도·소요시간 결과가 상충 — 일부는 IOS가 알지네이트만큼 정확하다 했고, 다른 연구는 재래식 인상이 유의

- `christopoulou-2022-intraoral-scanners-orthodontics-critical-review` [digital-workflow] (HIGH-far→vitai-2023-intraoral-scanner-complete-arch-sr-network-ma, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[digital-workflow/vitai-2023-intraoral-scanner-complete-arch-sr-network-ma]] — SR + network meta-analysis giving a device-ranked, quantified account of complete-arch accuracy and arch-extension error accumulation, where this 2022 review only reports individual-study-level contradictions without a pooled ranking.
  - ▸ 출발(`christopoulou-2022-intraoral-scanners-orthodontics-critical-review`) 세줄: 서술적 critical review(7개 DB, inception–2020.10 전수검색 + 회색문헌 손검색; PRISMA·PROSPERO 없음, 비뚤림위험 평가 없음): 교정과(orthodontics) 임상시험을 대상으로 구강스캐너(Intraoral Scanner, IOS)의 정확도·재현성·소요시간·환자 편의/선호·술자 경험을 재래식(알지네이트/PVS) 인상과 비교 종합. 포함 연구 간 정확도·소요시간 결과가 상충 — 일부는 IOS가 알지네이트만큼 정확하다 했고, 다른 연구는 재래식 인상이 유의

- `herbert-2016-aggregatibacter-actinomycetemcomitans-immunoregulator-periodontal` [oral-microbiology] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: > - 지식 공백: 비조혈계 세포(특히 조골세포) 대상 기전 연구 부족, 혈청형·균주별 이질성으로 인한 상충 결과 다수
  - ▸ 출발(`herbert-2016-aggregatibacter-actinomycetemcomitans-immunoregulator-periodontal`) 세줄: 응집간균 (Aggregatibacter actinomycetemcomitans, Aa)은 백혈구독소 (LtxA), 세포독성팽창독소 (CDT), LPS를 이용해 비조혈계(치은 상피·섬유아세포)와 조혈계(골수계·림프계) 세포 구획 전반에서 숙주 면역을 회피하고 치주 미세환경의 병적 염증을 유발한다. Aa는 여러 세포 유형에서 MAPK/NF-κB, NLRP3 인플라마좀, RANKL/OPG 신호 축을 활성화해 TNF-α·IL-1β·IL-6·IL-17 등 전염증성 사이토카인을 급증시키고, 파골세포 (Ost

- `greenstein-2018-need-replace-missing-second-molar` [occlusion] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: - Synthesizes the paradox that super-eruption is common but occlusal interference is not a predictable downstream consequence, refuting reflexive replacement.
  - ▸ 출발(`greenstein-2018-need-replace-missing-second-molar`) 세줄: 제2대구치 (Second Molar) 결손 후 임플란트 (Implant) 수복 여부를 평가한 서술적 문헌고찰 — 저작효율 (Masticatory Efficiency)·과맹출·교합간섭 (Occlusal Interference) 데이터 종합. 제1대구치 교합만으로 저작효율 약 90% 달성; 대합치 없는 구치의 약 20%가 ≥2 mm 정출 (Supraeruption)하나, 정출 정도와 교합간섭 발생은 강한 상관이 없음. 수복 여부는 환자 선호 (Patient Preference)에 따름 — 저작 불편감

- `open-healing-arp-technique-variables-overview` [overviews] (HIGH-no-target, '대비되는' · 대비)
  - **근거 문장**: 같은 맥락에서 Friedmann 2026(전향 증례시리즈, 49명 62부위)은 완전 흡수형 재료(SCLC/HA: 당 가교 콜라겐/수산화인회석 스펀지)로 개방치유(봉합만, 막·판막 없음)를 수행해 전 부위 합병증 없이 치유, 72% 추가 증대 불필요, 6개월 이후 재진입에서 이종골 완전 개조(잔여 이종골 0)를 확인했다. 협측골 ≥50% 잔존이 적응증이며, 대조군 없는 증례시리즈로 비교 결론은 불가하나, Benekou의 pooled 잔존 20.49%와 대비되는 **완전흡수 재료의 open-healing 적용 가능성**을 처음 제시한다. [미검증 — 증례시리즈]
  - ▸ 출발(`open-healing-arp-technique-variables-overview`) 세줄: Open-healing(개방치유) 치조제 보존술(Alveolar Ridge Preservation, ARP) 술기 변수 종합: 판막거상 vs 무판막은 골 폭·높이가 동등(Lee 2018 SR+MA, NS)하나 각화치은폭(Keratinized Gingiva Width, KGW)은 판막거상에서 −3.21 mm 더 소실(p<0.00001) → 무판막/개방치유 우선; hidden X suture가 기존 X suture보다 협측 KT 보존 우수(+0.25 vs −1.56 mm, Park 2016 RCT),

- `apical-patency-endodontic-outcome-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: > - **술후 통증과의 관계**: "개통성이 통증을 악화시킨다"는 전통적 우려는 최신 메타분석에서 지지되지 않음 — 오히려 통증 완화 가능성이 시사되나 개별 연구 간 상충.
  - ▸ 출발(`apical-patency-endodontic-outcome-overview`) 세줄: 두 전용 연구가 근단 개통성 (Apical Patency, AP) 임상 근거를 종합한다: Kuzhanchinathan 2024 SR(5편 임상연구, 4370근관; PROSPERO CRD42022374966)에서 AP 유지가 장기 치유율 **2배** 증가와 연관됐고, Ishizaki 2026 종합 리뷰는 "해부학적 개통성 vs 시술적 개통성" 개념 구분을 제시하며 AP와 술후 통증·해부학과의 관계를 종합했다. Ishizaki 2026이 인용한 최신 메타분석들은 AP가 술후 통증을 악화보다 오히려 완

- `apical-patency-endodontic-outcome-overview` [overviews] (HIGH-no-target, 'contrary to' · 상반된 결과)
  - **근거 문장**: Recent meta-analyses cited by Ishizaki 2026 suggest AP may *alleviate* rather than exacerbate postoperative pain — contrary to decades of clinical anxiety — but the evidence across individual studies remains conflicting; the evidence base for AP and healing is thin (only 1 RCT among 5 studies) and heterogeneous, precluding meta-analysis.
  - ▸ 출발(`apical-patency-endodontic-outcome-overview`) 세줄: 두 전용 연구가 근단 개통성 (Apical Patency, AP) 임상 근거를 종합한다: Kuzhanchinathan 2024 SR(5편 임상연구, 4370근관; PROSPERO CRD42022374966)에서 AP 유지가 장기 치유율 **2배** 증가와 연관됐고, Ishizaki 2026 종합 리뷰는 "해부학적 개통성 vs 시술적 개통성" 개념 구분을 제시하며 AP와 술후 통증·해부학과의 관계를 종합했다. Ishizaki 2026이 인용한 최신 메타분석들은 AP가 술후 통증을 악화보다 오히려 완

- `apical-patency-endodontic-outcome-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: Ishizaki 2026이 인용한 최신 메타분석들은 AP가 술후 통증을 악화보다 오히려 완화할 수 있다고 시사하지만 개별 연구 간 상충이 지속되며, 치유 근거 기반도 취약하다(RCT 1편·전향 임상연구 4편, 이질적 설계 → 메타분석 불가).
  - ▸ 출발(`apical-patency-endodontic-outcome-overview`) 세줄: 두 전용 연구가 근단 개통성 (Apical Patency, AP) 임상 근거를 종합한다: Kuzhanchinathan 2024 SR(5편 임상연구, 4370근관; PROSPERO CRD42022374966)에서 AP 유지가 장기 치유율 **2배** 증가와 연관됐고, Ishizaki 2026 종합 리뷰는 "해부학적 개통성 vs 시술적 개통성" 개념 구분을 제시하며 AP와 술후 통증·해부학과의 관계를 종합했다. Ishizaki 2026이 인용한 최신 메타분석들은 AP가 술후 통증을 악화보다 오히려 완

- `interdental-cleaning-devices-synthesis` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: > **모범답안**: IDB 1순위 근거: ① Carrouel 2026 RCT(임신 치은염 n=323): 보정교차비 OR 3.14로 출혈 소실의 최강 독립 예측인자, BOP 56%→12%(−79.6%) ② Kotsakis 2018 베이지안 NMA(RCT 22편, 도구 10종): IDB가 최선일 확률 64.7%, 치은지수·치태지수 감소 1위. 치실 한정 이유: Jung 2025(n=37 전향)에서 치실 술식(Flossing Performance Score) 교육으로 향상시켜도 치태 제거는 개선되지 않고 술식과 무관(p=.112) — "기술만 가르치면 된다"는 통념 반박. 치실은 IDB가 들어가지 않는 **좁은/정상 접촉**에만 한정 적용.
  - ▸ 출발(`interdental-cleaning-devices-synthesis`) 세줄: 치간 청소도구 21편 종합(+토스픽법 overview), Cochrane 우산 SR(Worthington 2019, RCT 35편·n=3929: 치실/치간칫솔+칫솔질이 칫솔질 단독보다 나을 가능성은 있으나 low~very low certainty, 치간 우식 평가 연구 0편)이 전체 틀을 제공: 보편적 우승 도구 없음 — **순응도가 도구보다 중요**(Yilmaz 2025 RCT n=54: 고무 치간 픽 12.61주 vs 치실 4.96주 규칙적 사용, p=0.003; Jung 2025 n=37: 

- `complete-denture-ovd-determination-overview` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: 10편 종합(Fayad 2025 종합리뷰, Alhajj 2017 방법 분류, Goyal 2026 안면계측 SR+MA, Khan 2023 검지 RCT, Matsuda 2014 EEG 결과, Sheppard 1975 두부계측 안정위, Satin 2023 OVD 전달 정확도): 총의치 OVD를 정확히 잡는 단일 신뢰 기법 없음 — 안정위는 불안정(연조직이 골격 변화를 가리고, 의치 장착 시 이동, Sheppard 1975); 안면계측은 보조지표(엄지 길이 r≈0.63 최강, I²=99%, Goyal 2026)이며, 검지법을 의치 제작까지 밀고 간 RCT(Khan 2023, 여성 r=0.966·1주 만족 97%)도 이 판정을 **뒤집지 못한다**(상관≠개별환자 정확도, 1주는 너무 짧음).
  - ▸ 출발(`complete-denture-ovd-determination-overview`) 세줄: 10편 종합(Fayad 2025 종합리뷰, Alhajj 2017 방법 분류, Goyal 2026 안면계측 SR+MA, Khan 2023 검지 RCT, Matsuda 2014 EEG 결과, Sheppard 1975 두부계측 안정위, Satin 2023 OVD 전달 정확도): 총의치 OVD를 정확히 잡는 단일 신뢰 기법 없음 — 안정위는 불안정(연조직이 골격 변화를 가리고, 의치 장착 시 이동, Sheppard 1975); 안면계측은 보조지표(엄지 길이 r≈0.63 최강, I²=99%, Goyal 2

- `non-surgical-periodontal-therapy-overview` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: > - **CHX 대안·착색 완화**: 칫솔질 병행 상황에서 CPC는 CHX와 동등(Windhorst 2025 SR+MA, 14 RCT), 착색 유의 적음; CHX+ADS는 효능 비손상으로 착색 유의 감소(Van Swaaij 2019 SR+MA) — "착색 없으면 효과 없다" 통념 반박; 착색 우려 환자엔 CPC(칫솔질) 또는 CHX+ADS(비칫솔질) 선택. [확인]
  - ▸ 출발(`non-surgical-periodontal-therapy-overview`) 세줄: 치주 비수술 치료 31편 종합: SRP는 만성 치주염 1차 치료로 강력 권고(Smiley 2015 ADA), PPD 1-2mm 감소·CAL 0.5-1mm 획득; 전신 항생제 보조는 매우 낮은 확실성·임상 이득 미미로 routine 금지(Cochrane 2020, 45 RCT). NSPT는 구강 밖 선택적 항염증 효과가 있음 — CRP·IL-6·수축기혈압 감소하나 지질 프로필은 변화 없음(Meng 2024 SR+MA, 21 RCT); GBT는 환자 편의성 우수하나 임상 결과는 전통 SRD와 동등(Y

- `non-surgical-periodontal-therapy-overview` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: **결론**: CHX+ADS는 수술 후 창상 보호 기간에 효능을 유지하면서 착색을 유의하게 줄임 — "착색이 없으면 효과도 없다"는 통념 반박. 착색 우려로 CHX 순응도가 낮을 환자에게 CHX+ADS 복합 제제 우선 권고.
  - ▸ 출발(`non-surgical-periodontal-therapy-overview`) 세줄: 치주 비수술 치료 31편 종합: SRP는 만성 치주염 1차 치료로 강력 권고(Smiley 2015 ADA), PPD 1-2mm 감소·CAL 0.5-1mm 획득; 전신 항생제 보조는 매우 낮은 확실성·임상 이득 미미로 routine 금지(Cochrane 2020, 45 RCT). NSPT는 구강 밖 선택적 항염증 효과가 있음 — CRP·IL-6·수축기혈압 감소하나 지질 프로필은 변화 없음(Meng 2024 SR+MA, 21 RCT); GBT는 환자 편의성 우수하나 임상 결과는 전통 SRD와 동등(Y

- `gbr-barrier-membrane-exposure-axis` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: > - 축2(막 구성): 콜라겐 막 이중층은 단일층 대비 이득 없음(Choi 2017); 골이식 + 흡수성 막은 자연치유 대비 수평 −2.19mm·수직 −1.72mm 흡수 감소(Troiano 2018 SR+MA+TSA — **단, 이 논문은 위키에서 Canullo 2021 네트워크 메타분석 (Network Meta-Analysis, NMA)에 의해 supersede 표시됨**; 방향은 뒤집히지 않고 재료 순위가 추가된 것).
  - ▸ 출발(`gbr-barrier-membrane-exposure-axis`) 세줄: GBR 차폐막 17편을 "막노출(membrane exposure)"이라는 공통 실패 모드 중심으로 4축(재료·가교, 막 구성, 판막·절개, 티타늄메쉬 맞춤화)으로 통합 — 노출은 막 브랜드보다 연조직·판막 관리가 좌우한다. 화학가교막은 비가교막 대비 노출 ~30% 더 많고 골이득은 없으며(Wessing 2018 SR+MA), 판막 절개 위치·각화치은 폭이 노출을 예측하고(Park 2007 전향), 판막 거상 자체가 각화치은 3.21 mm 손실을 초래하며(Lee 2018 SR+MA), 노출 시 e-

- `penicillin-allergy-dental-antibiotic-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: 5. **The sinus-lift allergy recommendation is internally contradictory in the wiki** (ciprofloxacin per SEI 2022 vs clindamycin per Díaz 2025), and neither rests on outcome data in penicillin-allergic sinus-lift patients. A paper measuring infection outcomes by agent in this subgroup would resolve a real chairside question.
  - ▸ 출발(`penicillin-allergy-dental-antibiotic-overview`) 세줄: 위키 17편(합의문 2·체계적문헌고찰+메타분석 3·체계적문헌고찰 3·내러티브리뷰 3·후향/단면 미생물·약물역학 자료 4)을 종합: 치과에서 페니실린 알레르기 환자의 실제 1차 문제는 알레르기가 아니라 **알레르기 라벨**이다 — 인구의 약 10%가 보유하나 자가보고 라벨의 80–99%는 검사에서 부정되며, 그 라벨이 촉발하는 반사적 대체 처방이 더 큰 위해가 되었다. 오래 가르쳐온 두 수치가 바뀌었다: 페니실린–세팔로스포린 교차반응은 전체 0.7%·확진 페니실린 알레르기에서 3%로 과거 8–10%

- `implant-surface-comparison` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: > **모범답안**: **수정해야 한다.** 이 오버뷰는 2026-08 근거 갱신으로 HA/TCP 코팅에 대한 우호적 서술을 **뒤집었다**: Damerau 2021(대형동물 15편 SR+MA)에서 이미 거친(rough) 비코팅 티타늄 대비 TCP/HA 코팅은 BIC 유의 우위 없음이 확인됐고, HA는 오히려 14일차에 BIC가 유의하게 낮았다(−6.94%p, p=0.001). "작은 표본 단일 연구가 큰 표본 메타분석에 뒤집힌 사례"로 명시돼 있다. 단, Mg 코팅(Alenezi 2026, BIC 유의 향상)과 Ag 코팅은 전임상에서 여전히 가능성이 있으나 인체 RCT 없음.
  - ▸ 출발(`implant-surface-comparison`) 세줄: 임플란트 표면처리 15편 + 5편 횡단인용 종합 매트릭스: SLA/SA = 임상 표준(8년 생존 94.8%, Kim 2020 n=96); 친수성(CA/SLActive) = D3/D4 골에서 stability dip 제거, 절대 ISQ 상승은 아님(CA 5.2년 97.3%, MBL 0.074 mm, Kim 2022 n=258); UV 광기능화(UV-PF) = 위축골·복잡증례 1순위(ISQ +21.9, 7년 100% 성공, Hirota 2020 전향적). 표면처리의 핵심 기전은 친수성이 아니라 탄화수

- `patient-recall-retention-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: The wiki holds two findings that look contradictory and are not:
  - ▸ 출발(`patient-recall-retention-overview`) 세줄: 19편 종합(치주·임플란트주위 유지관리 + 예약 내원 + 행동변화) — "구환 리콜"을 3층 운영 시스템으로 재정의: ① 누구를 언제 부를지 ② 예약된 방문이 실제로 일어나게 하는 법 ③ 애초에 왜 다시 오는지. 층별 근거 강도가 급격히 다르다: ②는 내원 RCT 2편 + 196,018건 머신러닝 모델(SMS vs 무 79.2% vs 35.5%, Prasad 2012; 음성>SMS 보정 OR 2.12, Nelson 2011; 리드타임이 최강 예측인자, Alabdulkarim 2022)로 가장 단단

- `direct-resin-restoration-adhesion-placement-overview` [overviews] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: Bulk-fill and incremental placement are clinically equivalent through ≥24 months (9-RCT MA RR 0.82 NS; 12-RCT NMA no significant difference; umbrella review; Zailai 2025, Chaple-Gil 2026) — conditional on a conventional occlusal cover layer, since uncovered bulk-fills wear 2–4× a nanohybrid (Osiewicz 2022) — and the claim "low-shrinkage = clinically superior" is refuted by 21-RCT MA (Kruly 2018).
  - ▸ 출발(`direct-resin-restoration-adhesion-placement-overview`) 세줄: Cochrane SR·우산형 리뷰·SR+MA/NMA·대규모 RCT·독일 S3 가이드라인을 아우르는 직접 복합레진 수복의 두 축 종합; 갈림길은 EAR이냐 SE냐가 아니라 **법랑질에 인산을 대느냐**다(Hong 2021 SR+MA; Oza 2022 SE 단독 24개월 부적합; Peumans 2023 3년 RCT E&R≈SEE 동등; Omoto 2025 4년 RCT 무산부식군만 기저치 이하). 벌크필과 적층충전은 ≥24개월 임상 동등(9-RCT MA RR 0.82 NS·12-RCT NMA 차이 없음

- `immediate-implant-evidence-survival-timing-infected-loading-overview` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: 즉시 vs 지연 생존 갈등은 해소: Mello 2017(관찰포함 30편 ~3%p 열세)은 **García-Sánchez 2022에 의해 완전 superseded**(2026-08) — RCT만 보면 생존 무차이이고 설계 편향이 원인이며, 독립 SR+MA인 Patel 2023(비교연구 10편, 위험비 0.99, I²=0%, 97.4% vs 97.5%)이 이질성 0%로 같은 결론을 재확인한다. 동일한 트레이드오프(골·PES 우세, 실패율 비유의 증가)가 **하나의 210명 3군 RCT 내부**(Felice 2016/Esposito 2017)에서도 재현 — 즉시·즉시지연이 골·PES는 유의 우위이나 실패율은 비유의하게 더 높은 경향(4개월→1년 안정). 부위·직경이 방향을 뒤집기도 함 — Checchi 2017(
  - ▸ 출발(`immediate-implant-evidence-survival-timing-infected-loading-overview`) 세줄: 즉시식립(Type 1)의 5개 결정축(생존·타이밍·감염소켓·부하/보철·환자체감)을 20편으로 종합한 허브: 생존율의 새 기준은 Gallucci 2026(PROSPERO 갱신 SR, 140편·10,456임플란트) — 9조합 가중생존율에서 Type 1A(즉시+즉시부하) 98.0%(검증됨) 대비 **Type 1B(즉시+조기부하) 91.6%(미검증)**로 손실률 약 4배 차이. 즉시 vs 지연 생존 갈등은 해소: Mello 2017(관찰포함 30편 ~3%p 열세)은 **García-Sánchez 2022

- `tmj-retrodiscal-tissue-disc-displacement-overview` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: 이 논문들은 교과서의 배역을 뒤집는다 — 주인공이던 관절원판 (articular disc)이 오히려 불활성 구획(무신경·무혈관·치밀 콜라겐·최고 글리코사미노글리칸 (GAG)·T2 최저 반응)이고, 후방조직은 변위를 저지하기엔 너무 무르지만(생리적 변형에서 영률 <1 MPa) 변위 후 하중 견디는 섬유연골로 재형성되고(FB2 전구 섬유아세포 + 혈관주위세포 유래 MC4 벽세포의 FGF2·BMP5 신호), 관절에서 유일하게 다양한 통각수용기 집단(비펩타이드성 ~20% + CGRP+ 75%)을 가지며, 환자에서 가장 먼저 정량 영상 변화를 보이는(후방조직 T2 34.4 → 반대측 37.8 → 환측 41.6 ms) 활성 구획이다.
  - ▸ 출발(`tmj-retrodiscal-tissue-disc-displacement-overview`) 세줄: 후방조직 (retrodiscal tissue, 이중판대 (bilaminar zone))을 인장 역학·부위별 생화학·단일세포 생물학·감각신경 분포·생체 정량 MRI의 5개 독립 축에서 다룬 논문 5편 종합으로, 기존 TMD/TMJ 오버뷰들이 관리 사다리 중심이라 비어 있던 **조직 축**을 채운다. 이 논문들은 교과서의 배역을 뒤집는다 — 주인공이던 관절원판 (articular disc)이 오히려 불활성 구획(무신경·무혈관·치밀 콜라겐·최고 글리코사미노글리칸 (GAG)·T2 최저 반응)이고, 후방조

- `healing-abutment-reuse-single-use-controversy-overview` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: > - **청결도 축 — 효과적 보조법**: 세 논문이 "특정 프로토콜이면 거의 미사용 표면"을 보인다 — ①**1% 차아염소산나트륨 (Sodium Hypochlorite, NaOCl)+초음파**로 성숙 바이오필름 **99.7%** 제거, SEM/EDX상 신품과 동등(Çetinsoy 2026); ②**3% NaOCl 또는 글리신 분말 에어폴리싱 (Glycine Air Polishing)** 추가 시 body 표면 오염 최저(에어폴리싱 1.7±1.1%·3% NaOCl 2.4±1.1% vs 대조 6.1%·12% 클로르헥시딘 (Chlorhexidine, CHX) 5.4%·3% 과산화수소 (Hydrogen Peroxide, H2O2) 4.6%, p<0.001; Naghsh 2024) — 뒤집어 말하면 **CHX·H
  - ▸ 출발(`healing-abutment-reuse-single-use-controversy-overview`) 세줄: 힐링 어버트먼트 재사용 논쟁을 청결도 축(미사용 표면 복원 가능?)과 생물학적 반응 축(깨끗해도 염증 안 내나?)으로 분리한 재사용 논문 8편 + 인접 임상결과 1편 종합: 2편 SR은 어떤 통상 프로토콜도 100% 미사용 표면을 복원 못 하고, 멸균 후 잔류 단백질이 나사산·드라이버홀 요철부에 집중됨을 일치시킨다. 1% NaOCl + 초음파(바이오필름 99.7% 제거, Çetinsoy 2026), 글리신 에어폴리싱·3% NaOCl(CHX·H2O2는 대조군 대비 이득 없음; Naghsh 2024)

- `healing-abutment-reuse-single-use-controversy-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: > - **축 간 충돌(contradiction)**: Kyaw(청결도 축, in vitro) "엄격 프로토콜이면 다회 재사용 OK" ↔ Abreu(생물학 축, in vitro) "깨끗해도 염증 유발 → 재사용 불가". 둘 다 옳을 수 있다 — 서로 **다른 종말점(endpoint)** 을 측정하기 때문. 이 충돌이 논쟁의 미해결 핵심.
  - ▸ 출발(`healing-abutment-reuse-single-use-controversy-overview`) 세줄: 힐링 어버트먼트 재사용 논쟁을 청결도 축(미사용 표면 복원 가능?)과 생물학적 반응 축(깨끗해도 염증 안 내나?)으로 분리한 재사용 논문 8편 + 인접 임상결과 1편 종합: 2편 SR은 어떤 통상 프로토콜도 100% 미사용 표면을 복원 못 하고, 멸균 후 잔류 단백질이 나사산·드라이버홀 요철부에 집중됨을 일치시킨다. 1% NaOCl + 초음파(바이오필름 99.7% 제거, Çetinsoy 2026), 글리신 에어폴리싱·3% NaOCl(CHX·H2O2는 대조군 대비 이득 없음; Naghsh 2024)

- `healing-abutment-reuse-single-use-controversy-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Manufacturers label HAs single-use yet 98.1% of implantologists reuse them (cost the primary driver, 71.2%) without informing patients (94.5%); crucially, zero clinical-outcome studies link reuse to peri-implant infection, bone loss, or failure — the nearest clinical-endpoint evidence the wiki holds (Canullo 2020 SR+MA on titanium HA *surface* differences) is null short-term and contradictory long
  - ▸ 출발(`healing-abutment-reuse-single-use-controversy-overview`) 세줄: 힐링 어버트먼트 재사용 논쟁을 청결도 축(미사용 표면 복원 가능?)과 생물학적 반응 축(깨끗해도 염증 안 내나?)으로 분리한 재사용 논문 8편 + 인접 임상결과 1편 종합: 2편 SR은 어떤 통상 프로토콜도 100% 미사용 표면을 복원 못 하고, 멸균 후 잔류 단백질이 나사산·드라이버홀 요철부에 집중됨을 일치시킨다. 1% NaOCl + 초음파(바이오필름 99.7% 제거, Çetinsoy 2026), 글리신 에어폴리싱·3% NaOCl(CHX·H2O2는 대조군 대비 이득 없음; Naghsh 2024)

- `healing-abutment-reuse-single-use-controversy-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - **The core unresolved contradiction:** Kyaw (cleanliness axis, in vitro) concludes reuse is acceptable with a rigorous protocol; Abreu (biologic axis, in vitro) concludes reuse is not acceptable because cleanliness ≠ inertness. Both can be internally valid because they measure different endpoints. Neither is a clinical outcome.
  - ▸ 출발(`healing-abutment-reuse-single-use-controversy-overview`) 세줄: 힐링 어버트먼트 재사용 논쟁을 청결도 축(미사용 표면 복원 가능?)과 생물학적 반응 축(깨끗해도 염증 안 내나?)으로 분리한 재사용 논문 8편 + 인접 임상결과 1편 종합: 2편 SR은 어떤 통상 프로토콜도 100% 미사용 표면을 복원 못 하고, 멸균 후 잔류 단백질이 나사산·드라이버홀 요철부에 집중됨을 일치시킨다. 1% NaOCl + 초음파(바이오필름 99.7% 제거, Çetinsoy 2026), 글리신 에어폴리싱·3% NaOCl(CHX·H2O2는 대조군 대비 이득 없음; Naghsh 2024)

- `healing-abutment-reuse-single-use-controversy-overview` [overviews] (HIGH-far→canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma, 'contradict' · 반박·충돌)
  - **근거 문장**: - **The mechanistic chain has an untested middle link (adjacent evidence).** The single-use rationale runs: repeated reprocessing oxidizes/roughens the titanium surface → the altered surface retains biofilm and degrades the mucosal seal → peri-implant disease. Only the *first* link is documented here (Kyaw's micro-gap worsening under repeated NaOCl-only cleaning; Paganotto's cited oxidation mechan
  - ▸ 출발(`healing-abutment-reuse-single-use-controversy-overview`) 세줄: 힐링 어버트먼트 재사용 논쟁을 청결도 축(미사용 표면 복원 가능?)과 생물학적 반응 축(깨끗해도 염증 안 내나?)으로 분리한 재사용 논문 8편 + 인접 임상결과 1편 종합: 2편 SR은 어떤 통상 프로토콜도 100% 미사용 표면을 복원 못 하고, 멸균 후 잔류 단백질이 나사산·드라이버홀 요철부에 집중됨을 일치시킨다. 1% NaOCl + 초음파(바이오필름 99.7% 제거, Çetinsoy 2026), 글리신 에어폴리싱·3% NaOCl(CHX·H2O2는 대조군 대비 이득 없음; Naghsh 2024)

- `healing-abutment-reuse-single-use-controversy-overview` [overviews] (HIGH-far→canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma, 'contradict' · 반박·충돌)
  - **근거 문장**: | [[implants/soft-tissue/canullo-2020-titanium-abutment-surface-peri-implant-tissue-ma]] | SR+MA (4 RCT, 2 CCT) | 118 patients / 182 implants | **Adjacent — clinical-endpoint bound** | Titanium HA *surface* differences → no short-term difference in plaque (P=0.091), BoP (P=0.099), PD (P=0.488); 5–6 y studies contradictory. Tests deliberate surface modification, NOT reprocessing damage — bounds the
  - ▸ 출발(`healing-abutment-reuse-single-use-controversy-overview`) 세줄: 힐링 어버트먼트 재사용 논쟁을 청결도 축(미사용 표면 복원 가능?)과 생물학적 반응 축(깨끗해도 염증 안 내나?)으로 분리한 재사용 논문 8편 + 인접 임상결과 1편 종합: 2편 SR은 어떤 통상 프로토콜도 100% 미사용 표면을 복원 못 하고, 멸균 후 잔류 단백질이 나사산·드라이버홀 요철부에 집중됨을 일치시킨다. 1% NaOCl + 초음파(바이오필름 99.7% 제거, Çetinsoy 2026), 글리신 에어폴리싱·3% NaOCl(CHX·H2O2는 대조군 대비 이득 없음; Naghsh 2024)

- `vertical-ridge-augmentation-overview` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: > - **합병증 자체는 드물다(≈11%)는 점이 예방 논리를 뒤집지 않는다**: 수직 골유도재생술(Guided Bone Regeneration, GBR) 전체 치유합병증은 부위 11.0%·환자 10.8%로 낮지만(Tay 2022), 발생 시 손실이 35%로 크기 때문에 **저빈도·고손실 구조 → 예방이 지배 전략**이다. 단 Ti-mesh의 노출률(16–35%)은 다른 차폐 방식의 수직 증대 합병증(11–17%)보다 높아, **메시는 상대적으로 술기민감한 선택지**다(Ng 2025). [확인]
  - ▸ 출발(`vertical-ridge-augmentation-overview`) 세줄: 26편 종합, 5축: 술식별 장기 임플란트주위 골소실(Peri-implant Bone Loss, PBL) 순위 SBB 0.66 < GBR 1.06 < Onlay 1.31 < Inlay 1.72 < 골신장술 1.81 mm(Cucchi 2024 SR+MA, 41개월); CAD/CAM Ti-mesh가 Ti강화 d-PTFE에 합병증·PROMs·통증·비용에서 비열등(Cucchi 2017/2024/2025 다수 RCT), pooled 수직 획득 3.36 mm(Sabri 2024)~4.05 mm(Ng 2025

- `oral-microbiome-biofilm-dysbiosis-synthesis` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: 구강 미생물·바이오필름 review 24편 통합(Socransky 1998 complex paradigm + Costerton 1999 biofilm paradigm 2개 historical foundation 포함): 3축 — ①매트릭스(EPS/matrixome): glucan이 caries 바이오필름 핵심 virulence, 국소 산성 미세환경(pH 4.5–5.5) 2시간 이상 지속; ②생태(microbiome): ~1,000종·부위당 ~50종, 건강=generalist·질환=specialist(Baker 2024가 종수준 biogeography로 정밀화); ③병인(dysbiosis): 치주염은 keystone pathogen P. gingivalis(<0.01%)가 주도하는 PSD 모델·균주특이적(Mu
  - ▸ 출발(`oral-microbiome-biofilm-dysbiosis-synthesis`) 세줄: 구강 미생물·바이오필름 review 24편 통합(Socransky 1998 complex paradigm + Costerton 1999 biofilm paradigm 2개 historical foundation 포함): 3축 — ①매트릭스(EPS/matrixome): glucan이 caries 바이오필름 핵심 virulence, 국소 산성 미세환경(pH 4.5–5.5) 2시간 이상 지속; ②생태(microbiome): ~1,000종·부위당 ~50종, 건강=generalist·질환=specialis

- `nsaid-osseointegration-impairment-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: > - 핵심 명제: 비스테로이드소염제(Non-Steroidal Anti-Inflammatory Drug, NSAID)의 임플란트 골유착(Osseointegration) 저해는 **근거 층위마다 신호 강도가 다르다** — 세포·동물에선 뚜렷하나 인체 임상에선 약하고 상충한다. 8편(SR+메타분석 1·SR 3(우산고찰 1 포함)·서술적 고찰 1·RCT 1·대규모 후향코호트 1·동물 1)을 근거 사다리로 재배열.
  - ▸ 출발(`nsaid-osseointegration-impairment-overview`) 세줄: 8편(SR+메타분석 1·SR 3(우산고찰 1 포함)·서술적 고찰 1·파일럿 RCT 1·대규모 후향코호트 1·동물 1) 종합: NSAID의 골유착 저해 신호는 in vitro·동물에선 강하나 인체 임상에선 약하고 상충한다 — 근거 사다리로 재배열. 기전상 COX-2 억제가 초기 임플란트 주위 골형성에 필요한 PGE2를 낮추며, 범인은 COX-2(COX-1 억제는 무해), 효과는 용량·기간·선택성 의존(동물서 장기·고용량 COX-2만 저해); 인체 층위는 갈린다 — 49,997 임플란트 코호트는 ib

- `nsaid-osseointegration-impairment-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: > - **치과 술후 진통제 결정**: ①아세트아미노펜(Acetaminophen)을 기본 축으로(경로 무관·무저해) → ②NSAID는 **선제 1회분 + 단기(3–7일)·최저용량**까지는 통증 근거가 지지하고 저해 근거는 없다 → ③경계선은 **만성·장기 상용**과 **선택적 COX-2 억제제**이지 술후 단기 코스가 아니다 → ④위험군(고령·당뇨·골다공증·골질 불량·즉시부하)일수록 보수적. 근거강도: 기전·용량축 = 강, 인체 인과 = 약(상충).
  - ▸ 출발(`nsaid-osseointegration-impairment-overview`) 세줄: 8편(SR+메타분석 1·SR 3(우산고찰 1 포함)·서술적 고찰 1·파일럿 RCT 1·대규모 후향코호트 1·동물 1) 종합: NSAID의 골유착 저해 신호는 in vitro·동물에선 강하나 인체 임상에선 약하고 상충한다 — 근거 사다리로 재배열. 기전상 COX-2 억제가 초기 임플란트 주위 골형성에 필요한 PGE2를 낮추며, 범인은 COX-2(COX-1 억제는 무해), 효과는 용량·기간·선택성 의존(동물서 장기·고용량 COX-2만 저해); 인체 층위는 갈린다 — 49,997 임플란트 코호트는 ib

- `nsaid-osseointegration-impairment-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 8편(SR+메타분석 1·SR 3(우산고찰 1 포함)·서술적 고찰 1·파일럿 RCT 1·대규모 후향코호트 1·동물 1) 종합: NSAID의 골유착 저해 신호는 in vitro·동물에선 강하나 인체 임상에선 약하고 상충한다 — 근거 사다리로 재배열.
  - ▸ 출발(`nsaid-osseointegration-impairment-overview`) 세줄: 8편(SR+메타분석 1·SR 3(우산고찰 1 포함)·서술적 고찰 1·파일럿 RCT 1·대규모 후향코호트 1·동물 1) 종합: NSAID의 골유착 저해 신호는 in vitro·동물에선 강하나 인체 임상에선 약하고 상충한다 — 근거 사다리로 재배열. 기전상 COX-2 억제가 초기 임플란트 주위 골형성에 필요한 PGE2를 낮추며, 범인은 COX-2(COX-1 억제는 무해), 효과는 용량·기간·선택성 의존(동물서 장기·고용량 COX-2만 저해); 인체 층위는 갈린다 — 49,997 임플란트 코호트는 ib

- `nsaid-osseointegration-impairment-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 4. **인체 임상은 약·상충**: ibuprofen 7일 RCT 2편·naproxen 파일럿 RCT는 골유착 지표 비유의(단 과소검정, 점추정 저해 방향) — Kumchai 2025, Luo 2018(Alissa·Sakka). SR 8편 우산고찰도 NSAID에 대해 골유착·실패 변화의 일관된 근거 없음 — D'Ambrosio 2023. 그러나 대규모 후향코호트는 ibuprofen 조기실패 OR 2.29–2.87 — Chatzopoulos 2025. [상충: RCT·우산고찰 무영향 vs 코호트 위험신호]
  - ▸ 출발(`nsaid-osseointegration-impairment-overview`) 세줄: 8편(SR+메타분석 1·SR 3(우산고찰 1 포함)·서술적 고찰 1·파일럿 RCT 1·대규모 후향코호트 1·동물 1) 종합: NSAID의 골유착 저해 신호는 in vitro·동물에선 강하나 인체 임상에선 약하고 상충한다 — 근거 사다리로 재배열. 기전상 COX-2 억제가 초기 임플란트 주위 골형성에 필요한 PGE2를 낮추며, 범인은 COX-2(COX-1 억제는 무해), 효과는 용량·기간·선택성 의존(동물서 장기·고용량 COX-2만 저해); 인체 층위는 갈린다 — 49,997 임플란트 코호트는 ib

- `nsaid-osseointegration-impairment-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 5. **노출 축이 층위 상충을 설명한다**: 위험 신호를 낸 코호트의 노출은 **용량·기간·식립 대비 타이밍이 보고되지 않은 상용 NSAID 사용**이고(Chatzopoulos 2025, abstract-only), 저해가 관찰된 동물 실험은 **장기(6주·60일)**였다. **단기 노출을 직접 본 층위(동물 2주·인체 7일 RCT·7일 파일럿)는 예외 없이 무영향**이다. 한편 임플란트·치주 수술 특화 SR+MA는 선제진통의 통증 감소 효과를 지지한다 — Gousias 2025. 즉 두 축은 "단기"에서 충돌하지 않는다. [해석 명제 — 노출 미보고에 근거한 귀속 불가 논증이며, 단기 안전을 입증한 것은 아님]
  - ▸ 출발(`nsaid-osseointegration-impairment-overview`) 세줄: 8편(SR+메타분석 1·SR 3(우산고찰 1 포함)·서술적 고찰 1·파일럿 RCT 1·대규모 후향코호트 1·동물 1) 종합: NSAID의 골유착 저해 신호는 in vitro·동물에선 강하나 인체 임상에선 약하고 상충한다 — 근거 사다리로 재배열. 기전상 COX-2 억제가 초기 임플란트 주위 골형성에 필요한 PGE2를 낮추며, 범인은 COX-2(COX-1 억제는 무해), 효과는 용량·기간·선택성 의존(동물서 장기·고용량 COX-2만 저해); 인체 층위는 갈린다 — 49,997 임플란트 코호트는 ib

- `antibiotics-comprehensive-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: [확인] Torof 2023 SR+MA: 단일 술전 Amoxicillin 2g이 조기 실패 유의 감소(Momand과 상충 → 방법론 차이).
  - ▸ 출발(`antibiotics-comprehensive-overview`) 세줄: 근관치료·치주치료·구강외과·임플란트를 아우르는 21편 종합: 항생제는 전신 증상 동반 감염에만 적응, 염증성 치수염(SIP)에는 금지 (Lockhart 2019 ADA CPG, Tampi 2019 SR+MA). 치주치료 보조 전신 항생제는 CAL 0.3-0.4mm 개선이나 근거 질 "약함" (Botelho 2025 우산형 고찰); 술전 단일 Amoxicillin 2g이 구강외과 표준, 24시간 초과 연장은 AMR만 증가. 약물 선택: Amoxicillin 1차(치명 0.1/million), Cli

- `conservative-access-cavity-biomechanics-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Synthesis of 12 papers resolving an apparent contradiction in conservative access cavity (CEC) biomechanics: pooled analyses report a significant fracture-resistance advantage for CEC over traditional endodontic cavities (TEC) — SUCRA 51.4% vs 15.3%, ~562 N difference (Motiwala 2022, 10 molar studies, n=456); SMD 2.61, 95% CI 1.47–3.74, p<0.001 (Mrinalini 2024, 14 studies) — while the three best-c
  - ▸ 출발(`conservative-access-cavity-biomechanics-overview`) 세줄: 논문 12편(네트워크 메타분석 1·쌍대 메타분석 2·체계적 고찰 3·통제 체외연구 3) 종합 — 보존적 접근와동 (Conservative Endodontic Cavity, CEC) 생역학의 겉보기 모순을 해소: 풀링 분석은 CEC가 전통 접근와동 (Traditional Endodontic Cavity, TEC)보다 파절저항이 유의하게 높다고 보고하는 반면(Motiwala 2022 — 누적순위곡선하면적 (Surface Under the Cumulative Ranking, SUCRA) 51.4% vs

- `nsaid-hypersensitivity-analgesic-selection-overview` [overviews] (SOFT→nsaid-aspirin-antiplatelet-interaction-overview, 'unlike' · 다름)
  - **근거 문장**: - **Aspirin antiplatelet** — [[overviews/nsaid-aspirin-antiplatelet-interaction-overview]] already flags celecoxib as **not** interfering with low-dose aspirin's cardioprotection (unlike ibuprofen/naproxen). So for a **cardiac patient on low-dose aspirin who is NSAID-hypersensitive**, celecoxib is consistent on both axes — provided the aspirin hypersensitivity itself has been phenotyped (a true as
  - ▸ 출발(`nsaid-hypersensitivity-analgesic-selection-overview`) 세줄: 보고된 "NSAID 알러지"·"아스피린 알러지"는 하나의 진단이 아니라 표현형(phenotype) 질문이다 — 병력 3문항과, 애매하면 경구 아스피린 유발검사로 표현형을 정하고, 그 표현형이 다른 NSAID·선택적 COX-2 억제제·아세트아미노펜 중 무엇이 치과 진통에 안전한지를 결정한다. 결정적 갈림길은 교차반응형(화학적으로 무관한 NSAID 2종 이상 반응, 또는 천식·비용종·만성두드러기 환자의 반응 — COX-1 억제·비IgE 기전으로 모든 강력 COX-1 억제제 금기)과 약물특이형(한 가지
  - ▸ 대상(`nsaid-aspirin-antiplatelet-interaction-overview`) 세줄: 5편(건강인 약력학 RCT 1편, OA+IHD 환자 RCT 1편, 9종 NSAID 인비트로 스크린 1편, 피라졸리논 인비트로 1편, 아스피린 State-of-the-Art 종설 1편) 종합: 특정 NSAID는 혈소판 COX-1 소수성 통로를 경쟁적으로 점유해 아스피린의 비가역적 Ser-529/530 아세틸화를 차단함으로써 항혈소판 효과를 소실시킨다. 이 상호작용은 복용 순서 의존적 — 아스피린 먼저(NSAID 2시간 전)면 완전 보존, NSAID 먼저면 차단; 이부프로펜이 최대 방해자(인비트로 4

- `mandibular-third-molar-management-overview` [overviews] (HIGH-far→canellas-2020-intrasocket-ao-third-molar-sr-nma, '상충' · 상충)
  - **근거 문장**: - [[oral-surgery/third-molar/canellas-2020-intrasocket-ao-third-molar-sr-nma]] — SR+NMA (37 RCTs): 발치와 내 소독재와 치조골염(Alveolar Osteitis, AO) 예방 — 혈소판 풍부 피브린(Platelet-Rich Fibrin, PRF) OR 0.28, 0.2% CHX 젤 OR 0.52로 최상위; iodoform 거즈·SurgicelⓇ 劣; PRF+CHX 병용 효과 상충. 적응증: 고위험 발치(흡연·여성·고령·매복) 시 PRF 우선 고려. (sr+nma, 2020)
  - ▸ 출발(`mandibular-third-molar-management-overview`) 세줄: 하악 사랑니 관리 9편 종합: 매복은 측정 가능한 병리 부담(치관주위염 82.4%, M2M 원심 우식 18.8%, 치주병변 14.8%; Ye 2021, n=432)을 만들고 매복 형태가 병리 종류를 예측하며, 전문가 합의(Sun 2026)가 3단계 적응증(확정적 병리·치료적·예방적)을 제시한다. 치관주위염의 1차 치료는 국소 세척·NSAIDs이며 항생제는 감염 확산·전신 증상 시에만 한정해야 하나 실제로 치과의사 약 75%가 처방(Schmidt 2021 SR); 발치 후 morbidity는 CGF

- `unopposed-tooth-overeruption-overview` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: > - 흔한 오판: "엔도한 치아라 더/덜 정출한다"(근거 없음·기전상 무관), "크라운 씌우면 정출 안 한다"(전체 치아가 이동), "대합치 없으면 무조건 빨리 보철"(저위험치는 과한 개입), "정출은 수직만"(경사·회전 동반), "인접 치아가 공간 채우면 정출 해결"(Smith 1996 반박).
  - ▸ 출발(`unopposed-tooth-overeruption-overview`) 세줄: 17편 종합: 대합치 없는 후방 치아의 ~83%가 정출(단기 ~9개월 평균 0.43 mm / 최대 0.75 mm; CBCT 5년 기준 근심교두 1.37 mm [Hong 2023]; ~72%는 1 mm 미만; 초기 최대 속도; 수직+협측경사+회전 3D); ~18%는 전혀 안 움직임; 정출은 PDL·치조골 매개라 치수 생활력 무관. 고정 retention도 부분접촉 대비 효과 없어(Livas 2016); 5년 후 인접 하악 제2대구치 근심 경사 (Mesial Tipping) 57.47°·협측 CEJ 

- `unopposed-tooth-overeruption-overview` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: > - **연령 효과의 경계 (중요 — 이번 개정에서 조정)**: "젊을수록 많이 정출"의 강한 근거는 **랫드 실험**(Fujita 2009, Denes 2020)이다. 사람 데이터로 연령을 조절인자로 검정한 유일한 풀링 분석인 Fan 2026 메타회귀에서는 **연령이 유의하지 않았다**. 뒤집혔다기보다 **측정 대상이 다르다** — 랫드는 어린 개체 vs 성체의 정출 *속도·크기*, Fan은 성인 코호트 안에서의 교합 *재확립 성공 여부*. 임상 함의: 성인 환자에서 "나이가 어리니 훨씬 빠를 것"이라는 추정은 동물 근거에 기대고 있으며 성인 연령대 안에서는 검증되지 않았다.
  - ▸ 출발(`unopposed-tooth-overeruption-overview`) 세줄: 17편 종합: 대합치 없는 후방 치아의 ~83%가 정출(단기 ~9개월 평균 0.43 mm / 최대 0.75 mm; CBCT 5년 기준 근심교두 1.37 mm [Hong 2023]; ~72%는 1 mm 미만; 초기 최대 속도; 수직+협측경사+회전 3D); ~18%는 전혀 안 움직임; 정출은 PDL·치조골 매개라 치수 생활력 무관. 고정 retention도 부분접촉 대비 효과 없어(Livas 2016); 5년 후 인접 하악 제2대구치 근심 경사 (Mesial Tipping) 57.47°·협측 CEJ 

- `vitamin-d-osseointegration-implant-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Vitamin D is biologically tied to bone metabolism (calcium homeostasis, osteoblast differentiation, immunomodulation), so a pro-osseointegration role is mechanistically plausible. The wiki holds 9 papers spanning the full evidence ladder, and they do **not** all agree. This page resolves the apparent contradiction.
  - ▸ 출발(`vitamin-d-osseointegration-implant-overview`) 세줄: 비타민 D[25(OH)D]와 임플란트 골유착(Osseointegration) 9편(우산형 1·SR 3·RCT 1·전향 2·후향 1·서사적 종설 1) 종합 — 기전/동물·SR/MA·사람 임상 근거 사다리 전반; Tallon 2024 우산형 고찰은 메타분석 부재·기준치·용량·결과지표 불일치를 명시. 동물·기전 근거는 일관되게 양성; 사람 근거는 결핍 중증도에 따라 갈림 — 양성 신호가 중증 결핍(<10~20 ng/mL)+동반위험에 몰림(Mohsen 2024: 실패율 <10 ng/mL 46.2% vs 

- `nccl-etiology-diagnosis-management-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Synthesis of 19 papers on noncarious cervical lesions (NCCL) — etiology, diagnosis, and monitor-vs-restore decision: NCCLs are multifactorial (stress/abfraction + friction/abrasion + biocorrosion/erosion as a case-specific combination), the "abfraction as sole cause" hypothesis is clinically unproven with SR evidence directly contradicting across three systematic reviews (Senna 2012 — association 
  - ▸ 출발(`nccl-etiology-diagnosis-management-overview`) 세줄: 비우식성 치경부 병소(Noncarious Cervical Lesion, NCCL) 19편 종합 — 병인은 stress(abfraction)·friction(abrasion)·biocorrosion(erosion)의 case-specific 다인성 조합이고, "교합응력(abfraction) 단독원인설"은 임상적으로 미입증이며 3편의 SR이 충돌(Senna 2012 결론 불가, Duangthip 2017 81% 연관 단 lab 가중, Dioguardi 2024 scoping 6편으로 확정·반박 모두 

- `nccl-etiology-diagnosis-management-overview` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: 비우식성 치경부 병소(Noncarious Cervical Lesion, NCCL) 19편 종합 — 병인은 stress(abfraction)·friction(abrasion)·biocorrosion(erosion)의 case-specific 다인성 조합이고, "교합응력(abfraction) 단독원인설"은 임상적으로 미입증이며 3편의 SR이 충돌(Senna 2012 결론 불가, Duangthip 2017 81% 연관 단 lab 가중, Dioguardi 2024 scoping 6편으로 확정·반박 모두 불가).
  - ▸ 출발(`nccl-etiology-diagnosis-management-overview`) 세줄: 비우식성 치경부 병소(Noncarious Cervical Lesion, NCCL) 19편 종합 — 병인은 stress(abfraction)·friction(abrasion)·biocorrosion(erosion)의 case-specific 다인성 조합이고, "교합응력(abfraction) 단독원인설"은 임상적으로 미입증이며 3편의 SR이 충돌(Senna 2012 결론 불가, Duangthip 2017 81% 연관 단 lab 가중, Dioguardi 2024 scoping 6편으로 확정·반박 모두 

- `nccl-etiology-diagnosis-management-overview` [overviews] (HIGH-no-target, '대비되는' · 대비)
  - **근거 문장**: - Universal adhesive — 산부식 전략은 **상위 근거가 갈린다**: 개별 RCT는 E&R과 SEE 모드 3년 성능 동등(Peumans 2023)이지만, NCCL 특이 SR+MA 2편이 서로 충돌한다 — Assis 2023(RCT 20편, PROSPERO 등록, 최대 규모)은 E&R이 중기(12–36개월) 유지·변연적합·변연착색·이차우식에서 우위이고 SE는 술후 과민증만 낮다고 보고, Doshi 2023(RCT 13편 메타분석)은 5개 지표 전부 무차이(p>0.05, I²=0%)라고 보고한다. 두 SR+MA는 서로를 "대비되는 결과"로 명시 인용하며, 어느 쪽도 아직 철회·대체되지 않았다.
  - ▸ 출발(`nccl-etiology-diagnosis-management-overview`) 세줄: 비우식성 치경부 병소(Noncarious Cervical Lesion, NCCL) 19편 종합 — 병인은 stress(abfraction)·friction(abrasion)·biocorrosion(erosion)의 case-specific 다인성 조합이고, "교합응력(abfraction) 단독원인설"은 임상적으로 미입증이며 3편의 SR이 충돌(Senna 2012 결론 불가, Duangthip 2017 81% 연관 단 lab 가중, Dioguardi 2024 scoping 6편으로 확정·반박 모두 

- `implant-failure-mbl-risk-factors-overview` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: > **모범답안**: 이 오버뷰는 **경사 임플란트의 MBL 패널티는 시간 의존적**임을 보여준다. malak-2024(메타분석): 단기 NS → 3년 +0.08mm(유의) → 장기 +0.18mm(유의)로 시간이 지날수록 차이가 커진다. del-fabbro 연구진 자체 데이터도 2014년(≥3년, P=.30, NS) → 2022년(3–18년, P<.0001, 축방향 MBL 적음)으로 뒤집혔다. 따라서 "단기에 차이 없다"는 2017년 SR은 **추적기간이 짧은 연구 종합**이라는 한계를 갖는다. 경사 vs 축방향의 **실패 위험은 동일(RR=1.02)**이지만 장기 MBL 관리를 위해서는 이 시간 의존성을 고려해야 한다.
  - ▸ 출발(`implant-failure-mbl-risk-factors-overview`) 세줄: 후기(정착 후) 임플란트 실패·변연골소실(MBL) 관련 논문 **24편** 종합 — 로딩 전 조기실패는 [[overviews/early-implant-failure-risk-prevention-overview]]와 상호보완. 우산리뷰 10편을 축으로 삼되, **우산리뷰는 등급만 매기고 효과크기를 안 주므로** 그 아래 1차 SR+MA·코호트 층을 함께 싣고, 여기에 위험인자 차이값을 읽을 **기준선**(kumar-2021, 1년 pooled MBL 0.56 mm)을 더한다. 가장 광범위한 우산리뷰

- `topical-anesthetic-injection-pain-overview` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: > - 명제5 (2026 갱신): 치주기구조작 맹검 RCT(Cabral 2026, n=76)는 명제2를 **부분적으로 뒤집는다** — 감온성 겔(Oraqix)과 컴퓨터제어 주사 간 **통증강도는 동등**(NRS-11 중앙값 0 vs 1, P>0.05)이나 **보충마취 필요율은 100% vs 24%(P<0.001)**. 즉 Wambier의 결론 중 재현되는 축은 통증강도가 아니라 **rescue·신뢰도**다. [확인]
  - ▸ 출발(`topical-anesthetic-injection-pain-overview`) 세줄: 6편 종합: 표면마취제는 위약 대비 needle·주사 통증을 줄이나(농도 의존, 5%→20%; Khongkhunthian 2018) 그 위약 대비 우위의 확실성은 GRADE low이고 표준 농도 위로의 증량은 trivial(20% vs 10% benzocaine RR 0.93, moderate; Miroshnychenko 2023 SR+MA), 제제 간 비교는 비일관적 — 소규모 RCT(Subramanian 2023)는 benzocaine 우위, 더 엄격한 triple-blind RCT(Karko

- `yang-2024-implant-diameter-tapered-stress-insertion` [implants] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 테이퍼 임플란트가 높은 IT를 내는 임상 관찰에 기계적 설명 제공 — 방사형 간섭이 응력장을 확대한다는 기전으로, 임상 문헌의 IT-1차 안정성-골 응력 상충관계와 거시형태를 연결.
  - ▸ 출발(`yang-2024-implant-diameter-tapered-stress-insertion`) 세줄: In vitro 삽입 실험 + 3D 명시적 FEA(Nobel Biocare 병렬벽 2종·테이퍼 2종, Ø3.5·4.3mm, PU 폼): 정규화 삽입 토크는 테이퍼 설계가 지배(β₂=0.93), 원시 삽입 토크는 직경이 더 크게 기여(β₁=0.78). 테이퍼가 유효 접촉압도 지배(β₂=0.97); 테이퍼 임플란트는 병렬벽 대비 나사산에서 더 멀리 압축 응력을 분산; FEA는 2D-DIC로 검증, 전 회귀모델 R²≥0.77. 테이퍼 임플란트가 높은 IT를 내는 임상 관찰에 기계적 설명 제공 — 방사형

- `miroshnychenko-2023-analgesics-acute-dental-pain` [drug/analgesics] (SOFT→di-spirito-2022-endodontic-pain-management-overview, 'unlike' · 다름)
  - **근거 문장**: - [[drug/analgesics/di-spirito-2022-endodontic-pain-management-overview]] — endodontic pain pharmacologic management overview; complementary adult context where pulpitis pain IS covered, unlike this pediatric review's extraction-only evidence.
  - ▸ 출발(`miroshnychenko-2023-analgesics-acute-dental-pain`) 세줄: - 소아(≤ 12세) 발치 후 급성 치통의 경구 진통제에 관한 체계적 문헌고찰 및 메타분석 (Systematic Review and Meta-Analysis, SRMA): 무작위대조시험 (Randomized Controlled Trial, RCT) 6편(연구당 45–201명, 평균 연령 5.5–9.3세), 2022년 ADA(미국치과협회) 소아 급성 치통 임상지침의 근거. - 이부프로펜과 아세트아미노펜은 위약보다 낫지만 서로 간 차이는 사소했고, 이부프로펜(5 mg/kg)+아세트아미노펜(15 mg/
  - ▸ 대상(`di-spirito-2022-endodontic-pain-management-overview`) 세줄: 체계적 고찰 개요(Healthcare 2022)와 기술적 요인 서술 고찰 통합: 근관 술후통증(환자의 2.5–60%, 6–12시간 최고조) 약물·비약물 관리 포괄. NSAIDs(ibuprofen ± APAP) 1차 약물치료; 코르티코스테로이드(dexamethasone)는 NSAID 보조제로 추가 이득; 술전 예방투여가 술후 반응투여보다 우월. 기구의 근첨 외 이탈·세정액 농도/용량·단일 vs 다회 방문 등 기술적 요인도 통증에 영향; 진통 목적 항생제 사용은 근거 없음.

- `einafshar-2024-importance-precision-cortical-bone-drilling` [implants/osteotomy-thermal] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Resolved contradictory literature on spindle speed: higher speed consistently raises MT while reducing MTF in this validated model framework.
  - ▸ 출발(`einafshar-2024-importance-precision-cortical-bone-drilling`) 세줄: 소 피질골 시편 + DEFORM-3D V6.02 3D 유한요소해석 (Finite Element Analysis, FEA) 통합 연구: 드릴 초기온도 (Initial Temperature, IT)·직경·끝각 (Point Angle)·스핀들 속도 (225–2700 rpm)·이송속도 (0.5–3 mm/s) 4개 변수가 최대 온도 (Maximum Temperature, MT)·최대 추력 (Maximum Thrust Force, MTF)에 미치는 영향 예측. IT 25 → 5°C 강하 시 MT −26.14

- `ceddia-2025-finite-element-analysis-of-implant` [implants/isq] (HIGH-no-target, 'counter to' · 반대)
  - **근거 문장**: - Demonstrates that ISQ increases slightly with inclination under horizontal load — counter to intuitive concern about instability
  - ▸ 출발(`ceddia-2025-finite-element-analysis-of-implant`) 세줄: Cyroth 임플란트(4 mm×15 mm)를 D2·D3 폴리우레탄 블록에 0°·15°·20° 경사 식립 후, 유한요소분석(FEA) 미세운동→ISQ 방정식 결과를 Osstell RFA 실측치와 비교한 in vitro 연구. FEA ISQ 오차 D3 1.27%, D2 2.86%; 경사 증가 시 ISQ 소폭 상승(D2 60.96→61.10); 피질골 응력 55.4→68.4 MPa(20°), 피크 임플란트 응력 220.2 MPa — 소성변형 한계(130 MPa) 미만. FEA로 다양한 경사 조건 ISQ 

- `naughton-2023-safemount-osstell-transducer-torque-isq` [implants/isq] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Demonstrated hand tightening yields significantly lower ISQ than 6 Ncm calibrated torque (p<.001), contradicting Kästel 2019
  - ▸ 출발(`naughton-2023-safemount-osstell-transducer-torque-isq`) 세줄: 체외 폴리우레탄 뼈 블록 연구 (임플란트 7종, 56개, D1–D4 골질): 스마트팩 조임 방법 4종 비교 — 수동, 플라스틱 마운트, SafeMount, 정확한 토크 렌치 6 Ncm. 수동 조임이 정확한 토크 렌치 대비 유의하게 낮은 임플란트 안정성 지수 (Implant Stability Quotient, ISQ) 산출 (계수 −2.05, p<.001); SafeMount와 표준 플라스틱 마운트는 대조군과 유의차 없음. 골밀도가 ISQ 변이의 36%를 차지해 가장 큰 영향 인자였고, 술자는 6%

- `namuangchan-2023-iodine-mouthwash-oral-mucositis-ccrt-rct` [oral-medicine/mucositis] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: The study failed to demonstrate statistically significant superiority of IS mouthwash over NSS for preventing CCRT-induced OM, likely due to small sample size and possibly insufficient iodine concentration. Larger-scale studies are warranted to confirm or refute any potential benefit.
  - ▸ 출발(`namuangchan-2023-iodine-mouthwash-oral-mucositis-ccrt-rct`) 세줄: 본 연구는 태국 콘켄 대학에서 2019년 1월부터 12월까지 수행된, 단일기관, 전향적, 이중맹검, 무작위대조 임상시험으로, 동시항암방사선치료(CCRT)를 받는 두경부암 환자 20명(1:1 배정)을 대상으로 자체 제조한 요오드 용액(IS) 가글의 구강점막염(OM) 예방 효과를 정상 생리식염수(NSS)와 비교 평가하였다. 1차 평가변수는 주간 구강점막염 평가 척도(OMAS) 점수로, CCRT 시작 전부터 치료 종료 4주 후까지 측정되었다. IS군과 NSS군 간 주간 평균 OMAS 점수(전체 평균 차

- `ishizaki-2026-clinical-significance-anatomical-considerations-apical-patency` [endodontics/shaping] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: > - 최신 메타분석에 따르면 개통성은 술후 통증을 오히려 완화할 수 있으나, 개별 연구 간 증거는 여전히 상충된다.
  - ▸ 출발(`ishizaki-2026-clinical-significance-anatomical-considerations-apical-patency`) 세줄: 종합 리뷰(Comprehensive Review, 비체계적) — 근단 개통성(Apical Patency)의 임상적 의의, 술후 통증(Postoperative Pain)과의 상관관계, 해부학적 고려사항, 협상(Negotiation) 기구·모터 키네마틱스(Motor Kinematics)를 기존 메타분석·임상연구 근거로 종합 검토. 최신 메타분석에 따르면 개통성은 술후 통증을 오히려 완화할 수 있으나(Apical Patency가 통증 악화가 아닌 감소), 개별 연구 간 증거는 여전히 상충 — 사전 CB

- `ishizaki-2026-clinical-significance-anatomical-considerations-apical-patency` [endodontics/shaping] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 최신 메타분석에 따르면 개통성은 술후 통증을 오히려 완화할 수 있으나(Apical Patency가 통증 악화가 아닌 감소), 개별 연구 간 증거는 여전히 상충 — 사전 CBCT는 MB2 근관 등 복잡 해부학 확인에 필수, 특수 NiTi 파일과 왕복형(Reciprocating) 모터 키네마틱스가 활주로(Glide Path) 형성 예측가능성을 높인다.
  - ▸ 출발(`ishizaki-2026-clinical-significance-anatomical-considerations-apical-patency`) 세줄: 종합 리뷰(Comprehensive Review, 비체계적) — 근단 개통성(Apical Patency)의 임상적 의의, 술후 통증(Postoperative Pain)과의 상관관계, 해부학적 고려사항, 협상(Negotiation) 기구·모터 키네마틱스(Motor Kinematics)를 기존 메타분석·임상연구 근거로 종합 검토. 최신 메타분석에 따르면 개통성은 술후 통증을 오히려 완화할 수 있으나(Apical Patency가 통증 악화가 아닌 감소), 개별 연구 간 증거는 여전히 상충 — 사전 CB

- `ishizaki-2026-clinical-significance-anatomical-considerations-apical-patency` [endodontics/shaping] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Regarding the contentious relationship between patency and postoperative pain, the review notes that recent meta-analyses suggest patency may actually alleviate discomfort intensity — a finding that contradicts longstanding clinical anxiety about patency maneuvers causing flare-ups. However, the evidence across individual studies remains conflicting, and the authors call for further RCTs with stan
  - ▸ 출발(`ishizaki-2026-clinical-significance-anatomical-considerations-apical-patency`) 세줄: 종합 리뷰(Comprehensive Review, 비체계적) — 근단 개통성(Apical Patency)의 임상적 의의, 술후 통증(Postoperative Pain)과의 상관관계, 해부학적 고려사항, 협상(Negotiation) 기구·모터 키네마틱스(Motor Kinematics)를 기존 메타분석·임상연구 근거로 종합 검토. 최신 메타분석에 따르면 개통성은 술후 통증을 오히려 완화할 수 있으나(Apical Patency가 통증 악화가 아닌 감소), 개별 연구 간 증거는 여전히 상충 — 사전 CB

- `ishizaki-2026-clinical-significance-anatomical-considerations-apical-patency` [endodontics/shaping] (HIGH-no-target, 'conflicting evidence' · 상충 결과)
  - **근거 문장**: 3. **Pain–patency relationship**: Synthesizes conflicting evidence from recent meta-analyses, showing the relationship is more nuanced than the traditional fear that patency increases postoperative pain.
  - ▸ 출발(`ishizaki-2026-clinical-significance-anatomical-considerations-apical-patency`) 세줄: 종합 리뷰(Comprehensive Review, 비체계적) — 근단 개통성(Apical Patency)의 임상적 의의, 술후 통증(Postoperative Pain)과의 상관관계, 해부학적 고려사항, 협상(Negotiation) 기구·모터 키네마틱스(Motor Kinematics)를 기존 메타분석·임상연구 근거로 종합 검토. 최신 메타분석에 따르면 개통성은 술후 통증을 오히려 완화할 수 있으나(Apical Patency가 통증 악화가 아닌 감소), 개별 연구 간 증거는 여전히 상충 — 사전 CB
