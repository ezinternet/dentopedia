# 논쟁 레이더 백필 후보 — 2026-08-17

명시적 충돌 표현이 있으나 그 쌍에 `relations:` 타입 엣지(어떤 타입이든)도 `superseded_by:` 포인터도 없는 후보. **이 목록은 신호일 뿐 — 두 페이지를 읽고 판단해 엣지를 단다.**

**카드 읽는 법**: 각 카드는 `출발페이지 —[충돌유형·한글뜻]→ 대상페이지` 형태다. 아래에 (1) **근거 문장**(위키 본문에서 충돌 표현이 나온 실제 문장), (2) **양쪽 페이지의 `## 세줄요약`**(한국어)을 붙여, 페이지를 열지 않고도 두 논문이 각각 무엇을 주장하는지·정말 충돌하는지 한글로 판단할 수 있게 했다. 충돌 유형 한글뜻은 표현 매칭 기반 근사치이며, **최종 판단은 사람/LLM 몫**이다. (reinforces가 맞는 경우도 있으니 키워드를 그대로 엣지로 옮기지 말 것 — 2026-07-17 전수 검토에서 contradicts 계열로 지목된 122건 중 실제 contradicts는 1건이었다.)

**대상은 키워드에 가장 가까운 링크로 특정한다.** 같은 줄의 나머지 링크는 충돌 표현의 대상이라는 근거가 없어 Tier 2(`AMBIG→`)로 강등된다 — 버리지 않으니 진짜 대상이 강등됐다면 Tier 2에서 찾을 수 있다.

- Tier 1 (대상 지목됨, actionable): **1**
- Tier 2 (대상 불명/soft, review): **6**
- (억제됨) 이미 typed 엣지·supersession 포인터가 있어 제외: **273** · 부정문 제외: **101** · 검토·불필요 대장: **461** · 동일 줄 비최근접으로 Tier 2 강등: **0**

## Tier 1 — 판단 후 엣지 달 후보 (page → 지목된 target)

### oral-microbiology

- `pignatelli-2020-periodontal-disease-nitric-oxide-blood-pressure`  —[counterpoint · 반대 논점]→  **`elzein-2021-chlorhexidine-povidone-iodine-mouthwash-salivary-sars-cov-2-rct`**
  - **근거 문장**: This narrative review introduces a clinically important paradox: chlorhexidine mouthwash—widely recommended for preprocedural rinsing and ICU oral hygiene—may raise systemic blood pressure by 2–3.5 mmHg through disruption of oral nitrate-reducing bacteria essential to the nitric oxide vasodilatory pathway. This systemic risk is especially relevant for hypertensive patients and provides a critical 
  - ▸ 출발(`pignatelli-2020-periodontal-disease-nitric-oxide-blood-pressure`) 세줄: 이 내러티브 리뷰는 산화질소(NO) 경로를 통해 구강 미생물, 특히 질산염 환원 박테리아 및 치주 질환과 전신 혈압(BP) 간의 연관성을 탐구합니다. 내인성 NO는 주요 혈관 확장제이며, 식이 질산염(예: 채소)이 구강 내 공생 박테리아에 의해 아질산염으로 환원되고 위와 순환계에서 NO로 전환되는 "질산염-아질산염-NO 경로"에 의해 보충됩니다. 항균 구강 세정액(예: 클로르헥시딘) 또는 혀 세척에 의한 이 경로의 교란은 타액 아질산염 생성을 감소시켜 혈압 상승을 초래할 수 있습니다. 반대로, 병
  - ▸ 대상(`elzein-2021-chlorhexidine-povidone-iodine-mouthwash-salivary-sars-cov-2-rct`) 세줄: 본 연구는 COVID-19 양성 환자 61명(평균 연령 45.3 ± 16.7세)을 대상으로 0.2% 클로르헥시딘과 1% 포비돈-아이오딘 구강 세정액의 타액 내 SARS-CoV-2 불활성화 효과를 평가한 평행군, 이중맹검, 무작위배정, 위약대조 임상시험으로, 2020년 6월부터 9월까지 레바논 라피크 하리리 대학병원에서 수행되었다. 시술 전후(세정 30초, 5분 후) 타액을 채취하여 rRT-PCR로 주기 역치(CT) 변화를 측정하였다. 0.2% 클로르헥시딘과 1% 포비돈-아이오딘 모두 증류수 대비 


## Tier 2 — 대상 식별 필요 / soft signal (review only)

- `greenstein-2018-need-replace-missing-second-molar` [occlusion] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: - Synthesizes the paradox that super-eruption is common but occlusal interference is not a predictable downstream consequence, refuting reflexive replacement.
  - ▸ 출발(`greenstein-2018-need-replace-missing-second-molar`) 세줄: 제2대구치 (Second Molar) 결손 후 임플란트 (Implant) 수복 여부를 평가한 서술적 문헌고찰 — 저작효율 (Masticatory Efficiency)·과맹출·교합간섭 (Occlusal Interference) 데이터 종합. 제1대구치 교합만으로 저작효율 약 90% 달성; 대합치 없는 구치의 약 20%가 ≥2 mm 정출 (Supraeruption)하나, 정출 정도와 교합간섭 발생은 강한 상관이 없음. 수복 여부는 환자 선호 (Patient Preference)에 따름 — 저작 불편감

- `namuangchan-2023-iodine-mouthwash-oral-mucositis-ccrt-rct` [oral-medicine/mucositis] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: The study failed to demonstrate statistically significant superiority of IS mouthwash over NSS for preventing CCRT-induced OM, likely due to small sample size and possibly insufficient iodine concentration. Larger-scale studies are warranted to confirm or refute any potential benefit.
  - ▸ 출발(`namuangchan-2023-iodine-mouthwash-oral-mucositis-ccrt-rct`) 세줄: 본 연구는 태국 콘켄 대학에서 2019년 1월부터 12월까지 수행된, 단일기관, 전향적, 이중맹검, 무작위대조 임상시험으로, 동시항암방사선치료(CCRT)를 받는 두경부암 환자 20명(1:1 배정)을 대상으로 자체 제조한 요오드 용액(IS) 가글의 구강점막염(OM) 예방 효과를 정상 생리식염수(NSS)와 비교 평가하였다. 1차 평가변수는 주간 구강점막염 평가 척도(OMAS) 점수로, CCRT 시작 전부터 치료 종료 4주 후까지 측정되었다. IS군과 NSS군 간 주간 평균 OMAS 점수(전체 평균 차

- `immediate-implant-evidence-survival-timing-infected-loading-overview` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: 즉시 vs 지연 생존 갈등은 해소: Mello 2017(관찰포함 30편 ~3%p 열세)은 **García-Sánchez 2022에 의해 완전 superseded**(2026-08) — RCT만 보면 생존 무차이이고 설계 편향이 원인. 동일한 트레이드오프(골·PES 우세, 실패율 비유의 증가)가 **하나의 210명 3군 RCT 내부**(Felice 2016/Esposito 2017)에서도 재현 — 즉시·즉시지연이 골·PES는 유의 우위이나 실패율은 비유의하게 더 높은 경향(4개월→1년 안정). 부위·직경이 방향을 뒤집기도 함 — Checchi 2017(구치·광경직경)은 지연군이 PES·변연골 모두 우위(전치부 Puisys 2022와 정반대).
  - ▸ 출발(`immediate-implant-evidence-survival-timing-infected-loading-overview`) 세줄: 즉시식립(Type 1)의 5개 결정축(생존·타이밍·감염소켓·부하/보철·환자체감)을 19편으로 종합한 허브: 생존율의 새 기준은 Gallucci 2026(PROSPERO 갱신 SR, 140편·10,456임플란트) — 9조합 가중생존율에서 Type 1A(즉시+즉시부하) 98.0%(검증됨) 대비 **Type 1B(즉시+조기부하) 91.6%(미검증)**로 손실률 약 4배 차이. 즉시 vs 지연 생존 갈등은 해소: Mello 2017(관찰포함 30편 ~3%p 열세)은 **García-Sánchez 2022

- `mandibular-third-molar-management-overview` [overviews] (HIGH-far→canellas-2020-intrasocket-ao-third-molar-sr-nma, '상충' · 상충)
  - **근거 문장**: - [[oral-surgery/third-molar/canellas-2020-intrasocket-ao-third-molar-sr-nma]] — SR+NMA (37 RCTs): 발치와 내 소독재와 치조골염(Alveolar Osteitis, AO) 예방 — 혈소판 풍부 피브린(Platelet-Rich Fibrin, PRF) OR 0.28, 0.2% CHX 젤 OR 0.52로 최상위; iodoform 거즈·SurgicelⓇ 劣; PRF+CHX 병용 효과 상충. 적응증: 고위험 발치(흡연·여성·고령·매복) 시 PRF 우선 고려. (sr+nma, 2020)
  - ▸ 출발(`mandibular-third-molar-management-overview`) 세줄: 하악 사랑니 관리 4편 종합: 매복은 측정 가능한 병리 부담(치관주위염 82.4%, M2M 원심 우식 18.8%, 치주병변 14.8%; Ye 2021, n=432)을 만들고 매복 형태가 병리 종류를 예측하며, 전문가 합의(Sun 2026)가 3단계 적응증(확정적 병리·치료적·예방적)을 제시한다. 치관주위염의 1차 치료는 국소 세척·NSAIDs이며 항생제는 감염 확산·전신 증상 시에만 한정해야 하나 실제로 치과의사 약 75%가 처방(Schmidt 2021 SR); 발치 후 morbidity는 CGF

- `nccl-etiology-diagnosis-management-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Synthesis of 17 papers on noncarious cervical lesions (NCCL) — etiology, diagnosis, and monitor-vs-restore decision: NCCLs are multifactorial (stress/abfraction + friction/abrasion + biocorrosion/erosion as a case-specific combination), the "abfraction as sole cause" hypothesis is clinically unproven with SR evidence directly contradicting across three systematic reviews (Senna 2012 — association 
  - ▸ 출발(`nccl-etiology-diagnosis-management-overview`) 세줄: 비우식성 치경부 병소(Noncarious Cervical Lesion, NCCL) 17편 종합 — 병인은 stress(abfraction)·friction(abrasion)·biocorrosion(erosion)의 case-specific 다인성 조합이고, "교합응력(abfraction) 단독원인설"은 임상적으로 미입증이며 3편의 SR이 충돌(Senna 2012 결론 불가, Duangthip 2017 81% 연관 단 lab 가중, Dioguardi 2024 scoping 6편으로 확정·반박 모두 

- `nccl-etiology-diagnosis-management-overview` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: 비우식성 치경부 병소(Noncarious Cervical Lesion, NCCL) 17편 종합 — 병인은 stress(abfraction)·friction(abrasion)·biocorrosion(erosion)의 case-specific 다인성 조합이고, "교합응력(abfraction) 단독원인설"은 임상적으로 미입증이며 3편의 SR이 충돌(Senna 2012 결론 불가, Duangthip 2017 81% 연관 단 lab 가중, Dioguardi 2024 scoping 6편으로 확정·반박 모두 불가).
  - ▸ 출발(`nccl-etiology-diagnosis-management-overview`) 세줄: 비우식성 치경부 병소(Noncarious Cervical Lesion, NCCL) 17편 종합 — 병인은 stress(abfraction)·friction(abrasion)·biocorrosion(erosion)의 case-specific 다인성 조합이고, "교합응력(abfraction) 단독원인설"은 임상적으로 미입증이며 3편의 SR이 충돌(Senna 2012 결론 불가, Duangthip 2017 81% 연관 단 lab 가중, Dioguardi 2024 scoping 6편으로 확정·반박 모두 
