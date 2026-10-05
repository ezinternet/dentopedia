# 논쟁 레이더 백필 후보 — 2026-10-05

명시적 충돌 표현이 있으나 그 쌍에 `relations:` 타입 엣지(어떤 타입이든)도 `superseded_by:` 포인터도 없는 후보. **이 목록은 신호일 뿐 — 두 페이지를 읽고 판단해 엣지를 단다.**

**카드 읽는 법**: 각 카드는 `출발페이지 —[충돌유형·한글뜻]→ 대상페이지` 형태다. 아래에 (1) **근거 문장**(위키 본문에서 충돌 표현이 나온 실제 문장), (2) **양쪽 페이지의 `## 세줄요약`**(한국어)을 붙여, 페이지를 열지 않고도 두 논문이 각각 무엇을 주장하는지·정말 충돌하는지 한글로 판단할 수 있게 했다. 충돌 유형 한글뜻은 표현 매칭 기반 근사치이며, **최종 판단은 사람/LLM 몫**이다. (reinforces가 맞는 경우도 있으니 키워드를 그대로 엣지로 옮기지 말 것 — 2026-07-17 전수 검토에서 contradicts 계열로 지목된 122건 중 실제 contradicts는 1건이었다.)

**대상은 키워드에 가장 가까운 링크로 특정한다.** 같은 줄의 나머지 링크는 충돌 표현의 대상이라는 근거가 없어 Tier 2(`AMBIG→`)로 강등된다 — 버리지 않으니 진짜 대상이 강등됐다면 Tier 2에서 찾을 수 있다.

- Tier 1 (대상 지목됨, actionable): **7**
- Tier 2 (대상 불명/soft, review): **113**
- (억제됨) 이미 typed 엣지·supersession 포인터가 있어 제외: **332** · 부정문 제외: **159** · 검토·불필요 대장: **444** · 동일 줄 비최근접으로 Tier 2 강등: **2**

## Tier 1 — 판단 후 엣지 달 후보 (page → 지목된 target)

### drug/antibiotics

- `esposito-2026-antibiotics-implant-placement-cochrane-pub5`  —[contradict · 반박·충돌]→  **`momand-2024-antibiotic-prophylaxis-early-implant-failure`**
  - **근거 문장**: - [[drug/antibiotics/momand-2024-antibiotic-prophylaxis-early-implant-failure]] — contradicts; double-blind-only subgroup shows no benefit (RR 0.66)
  - ▸ 출발(`esposito-2026-antibiotics-implant-placement-cochrane-pub5`) 세줄: 코크란 SR+MA pub5 (2025년 11월까지): 15편 RCT, 2874명 — pub4(2013) 대비 RCT 약 3배, 참여자 약 2.5배 확대. 예방적 항생제(주로 술전 아목시실린 2g 단일 투여)가 임플란트 실패(RR 0.34; NNT=19)·보철물 실패·술후 감염을 아마 감소(전부 moderate certainty). 단일 투여 = 다중 투여; 술전 vs 술후, 아목시실린 vs 클린다마이신 간 유의차 없음 — 최적 요법 미확정.
  - ▸ 대상(`momand-2024-antibiotic-prophylaxis-early-implant-failure`) 세줄: 위약대조 이중맹검 RCT 7편만 포함한 SR+MA(환자 1859명/임플란트 3014개; PROSPERO CRD42021292610): 기존 SR+MA들이 비맹검·고위험-비뚤림 연구를 포함해 상충된 결론을 낸 한계를 방법론적으로 극복. 술전 항생제 예방이 조기 임플란트 실패를 유의하게 줄이지 못함(RR 0.66, 95% CI 0.30–1.47; 위험차 −0.007; NNT 143); GRADE 중간; 즉시 발치 후 임플란트 제외 분석에서 방향 역전(RR 1.10) → 항생제 효과는 발치 후 즉시 식


### drug/anticoagulants

- `kyyak-2023-platelet-rich-fibrin-ensures-hemostasis`  —[contradict · 반박·충돌]→  **`xiang-2026-continuous-interrupted-doac-minimal-bleeding-sr-ma`**
  - **근거 문장**: - [[drug/anticoagulants/xiang-2026-continuous-interrupted-doac-minimal-bleeding-sr-ma]] — SR+MA on continuing vs interrupting DOACs; consistent with the conclusion here. No supersession or contradiction: this small RCT neither overturns nor conflicts with existing pages.
  - ▸ 출발(`kyyak-2023-platelet-rich-fibrin-ensures-hemostasis`) 세줄: 전향적 이중맹검 무작위 분할구강 시험(마인츠, Xa 인자 억제제 복용 환자 21명, 발치와 42개)으로, 항응고제를 중단하지 않고 혈소판풍부피브린 (Platelet-Rich Fibrin, PRF)과 젤라틴 스펀지 (Gelatine Sponge, GS)를 비교했다. 42부위 중 28부위(67%)에서 경미한 스며나옴이 있었고 24건은 거즈 압박 30분 내, 최장 1.5시간 내 지혈되었으며, 출혈 합병증이나 지연 출혈은 없었고 PRF와 GS 간 차이도 없었다(모두 p>0.05). PRF와 GS 모두 봉
  - ▸ 대상(`xiang-2026-continuous-interrupted-doac-minimal-bleeding-sr-ma`) 세줄: PROSPERO 등록 SR+MA(24편, n=8,663; 심장 절제술 13·박동기 4·치과 4편; 대부분 심방세동으로 DOAC 복용): minimal bleeding-risk 시술에서 DOAC 지속 vs 중단 비교. 전체 풀에서 continuous DOAC이 대출혈(OR 0.57)·혈전(OR 0.54)을 줄였으나, RCT 8편만 분석하면 모든 차이 소실(대출혈 OR 0.82, 혈전 OR 0.53 — 모두 NS): 관찰 데이터의 selection bias 시사; GRADE very low~low. 


### immediate-implant/infected-socket

- `da-silva-2023-short-implant-and-heavy-smokers`  —[refut · 반증]→  **`de-oliveira-neto-2019-immediate-dental-implants-placed-into`**
  - **근거 문장**: **Reading against the rest of the wiki [미검증 — Claude 해석]:** the non-significant CAP effect is compatible with the held reports that chronic periapical lesions are not an absolute contraindication when the socket is debrided, but the 95% CI (0.70–7.97) is too wide to exclude a clinically important increase in failure, so it neither confirms nor refutes the higher-risk estimate in [[immediate-implan
  - ▸ 출발(`da-silva-2023-short-implant-and-heavy-smokers`) 세줄: 후향 코호트 (브라질 리우데자네이루 단일 개인치과, 2006–2018, 단일 술자): 환자 186명·즉시식립 임플란트 423개, 그중 215개는 만성 치근단 치주염 (Chronic Apical Periodontitis, CAP) 치아의 발치와, 208개는 CAP 없는 발치와에 식립; 평균 추적 39.4개월. 전체 임플란트 생존율 91% (385/423): CAP 발치와 88.8% (191/215) vs 비CAP 93.3% (194/208)로 유의차 없음 (이변량 p=0.111; GEE 보정 OR 
  - ▸ 대상(`de-oliveira-neto-2019-immediate-dental-implants-placed-into`) 세줄: SR+MA (PROSPERO CRD42018092156; 2018년 5월까지 7개 DB; 사람 임상연구 8편·임플란트 935개; Cochrane 비뚤림 위험 전반 불명확, 참여자·시술자 눈가림은 전 연구 high risk)로, 항생제 투여·추적 1년 이상·전신질환 없는 환자만 포함해 감염 vs 비감염 발치와 즉시식립을 비교. 감염 부위의 임플란트 실패 위험비 2.99 (95% CI 1.04–8.56, p=0.04, I²=0%), 연구별 생존율 90.8–100%; 변연골 소실(MD −0.03 mm)


### implants/survival

- `ramesh-2024-compression-necrosis-cause-concern-early`  —[counterpoint · 반대 논점]→  **`trisi-2011-high-low-implant-torque-histology-sheep`**
  - **근거 문장**: - [[implants/isq/trisi-2011-high-low-implant-torque-histology-sheep]] — the strongest counterpoint: 110 Ncm assigned by design in dense sheep mandibular cortex produced no osteocyte lacunar emptying and no avascular zone. Read together, torque alone is not the variable; the operative context (no pre-tapping into human D2 cortical bone, 3.2 mm osteotomy for a 3.5 mm implant) is what Trisi's design 
  - ▸ 출발(`ramesh-2024-compression-necrosis-cause-concern-early`) 세줄: 증례보고 (n=1) — 33세 비흡연·비당뇨 여성의 하악 좌측 구치부에 3.5 × 11.5 mm 임플란트 식립, 6주째 조기 실패. 재수술 시 실패 임플란트와 함께 채취한 골을 조직학적으로 검사함. 언더사이징 드릴링(3.5D 임플란트에 최종 드릴 3.2 mm) + 프리태핑 없음 + 35–50 Ncm 삽입토크를 D2-D3 골에 적용 → 6주 IOPAR에서 임플란트 길이의 절반까지 골소실(50%) 및 동요. 조직은 골성 소주 + **골아세포 테두리 부재** + 생존골 전무 + 골세포가 빠진 소공 → 
  - ▸ 대상(`trisi-2011-high-low-implant-torque-histology-sheep`) 세줄: 양 하악 분할-구강 동물실험(5마리, 임플란트 40개, 6주): 과삽입토크(HT=평균 110 Ncm) vs 저토크(LT=10 Ncm) 조직학·생체역학 비교. HT군에서 전 측정 시점 골형성↑·제거토크↑, 결정적으로 **압박괴사 없음** — 110 Ncm의 피질골 압박도 허혈성 골괴사를 유발하지 않음. HT군은 식립 7일째 1차 안정성 유의 감소(리모델링 딥)가 나타났으나 ISQ/공명주파수분석(Resonance Frequency Analysis, RFA)은 이를 감지하지 못함 — RFA의 초기 골유

- `ramesh-2024-compression-necrosis-cause-concern-early`  —[counterpoint · 반대 논점]→  **`khayat-2011-clinical-outcome-dental-implants-high`**
  - **근거 문장**: - [[implants/isq/khayat-2011-clinical-outcome-dental-implants-high]] — human counterpoint: up to 176 Ncm with all implants integrated at 1 year and no significant MBL difference. Bounded by control n = 9, post-hoc torque grouping and a 1-year horizon.
  - ▸ 출발(`ramesh-2024-compression-necrosis-cause-concern-early`) 세줄: 증례보고 (n=1) — 33세 비흡연·비당뇨 여성의 하악 좌측 구치부에 3.5 × 11.5 mm 임플란트 식립, 6주째 조기 실패. 재수술 시 실패 임플란트와 함께 채취한 골을 조직학적으로 검사함. 언더사이징 드릴링(3.5D 임플란트에 최종 드릴 3.2 mm) + 프리태핑 없음 + 35–50 Ncm 삽입토크를 D2-D3 골에 적용 → 6주 IOPAR에서 임플란트 길이의 절반까지 골소실(50%) 및 동요. 조직은 골성 소주 + **골아세포 테두리 부재** + 생존골 전무 + 골세포가 빠진 소공 → 
  - ▸ 대상(`khayat-2011-clinical-outcome-dental-implants-high`) 세줄: 전향적 임상연구 (환자 48명, Zimmer Tapered Screw-Vent 4.5 mm 임플란트 66개, 비매몰 치유): 최대 삽입 토크 (Maximum Insertion Torque, MIT) >70 Ncm군(42개; 평균 110.6, 범위 70.8–176 Ncm) vs 30–50 Ncm 대조군(9개; 평균 37.1 Ncm)의 변연골 수준 비교. 2–3개월 후 전 임플란트 임상적 안정; 변연골 흡수 (Marginal Bone Loss, MBL)는 부하 시 고토크 0.72 mm vs 대조 1.


### overviews

- `immediate-implant-infected-sites-decision`  —[contradict · 반박·충돌]→  **`de-oliveira-neto-2019-immediate-dental-implants-placed-into`**
  - **근거 문장**: - [[immediate-implant/infected-socket/de-oliveira-neto-2019-immediate-dental-implants-placed-into]] — MA with failure RR 2.99 (contradicting evidence; partially superseded)
  - ▸ 출발(`immediate-implant-infected-sites-decision`) 세줄: 21편(SR+MA 4·SR 1·MA 1·전향/비교 5·후향 5·증례/증례군 5; 2015–2026) 합성: 핵심 변수는 '감염 자체'가 아닌 **감염 유형** — 만성 치근단 병변(chronic periapical lesion)은 철저한 소파+항생제 예방 시 비감염 부위와 생존율 동등(RR=0.99, Saijeva 2020; Pranckeviciene 2024 SR+MA); 급성 화농성 농양(acute purulent abscess)은 8–12주 조기식립(Early placement)이 24개월 
  - ▸ 대상(`de-oliveira-neto-2019-immediate-dental-implants-placed-into`) 세줄: SR+MA (PROSPERO CRD42018092156; 2018년 5월까지 7개 DB; 사람 임상연구 8편·임플란트 935개; Cochrane 비뚤림 위험 전반 불명확, 참여자·시술자 눈가림은 전 연구 high risk)로, 항생제 투여·추적 1년 이상·전신질환 없는 환자만 포함해 감염 vs 비감염 발치와 즉시식립을 비교. 감염 부위의 임플란트 실패 위험비 2.99 (95% CI 1.04–8.56, p=0.04, I²=0%), 연구별 생존율 90.8–100%; 변연골 소실(MD −0.03 mm)


### resin-bonding

- `bourgi-2026-chx-pretreatment-clinical-adhesive-restorations-sr-ma`  —[refut · 반증]→  **`kiuru-2021-mmp-inhibitors-dentin-bonding-sr-ma`**
  - **근거 문장**: This SR+MA directly tests whether in vitro MMP-inhibition by CHX translates to clinical advantage in adhesive restorations — a question left open by earlier mechanistic reviews in the wiki. The null result (no benefit for retention, sensitivity, or secondary caries across 11 RCTs) challenges the rationale for routine CHX pretreatment and complements [[resin-bonding/kiuru-2021-mmp-inhibitors-dentin
  - ▸ 출발(`bourgi-2026-chx-pretreatment-clinical-adhesive-restorations-sr-ma`) 세줄: SR+MA (11편, 최대 4년): CHX 전처리는 유지율·술후 과민·2차 우식에서 대조군과 유의차 없음 (I²=0%). 실험실 MMP 억제 효과가 임상으로 전이 안 되는 이유 — 현대 접착제의 화학적·미세기계적 하이브리드층이 CHX 혜택을 상쇄. 임상 결론: 일상적 접착 프로토콜에서 CHX 불필요; 고위험 우식·항균 목적 시 여전히 선택 가능. ---
  - ▸ 대상(`kiuru-2021-mmp-inhibitors-dentin-bonding-sr-ma`) 세줄: SR+MA (J Dent Res 2021; 740편 → 43편; 클로르헥시딘(CHX) 21편 메타분석) — MMP 억제제가 레진-상아질 결합강도 내구성에 미치는 영향 평가. CHX(0.2–2%)는 즉시 결합강도에 유의한 영향이 없으나(p=0.308), 6·12·24개월 노화 후 결합강도를 유의하게 보존하며(모두 p<0.001), 24개월에서 I²=0%로 노화 기간이 길수록 이점이 커진다. CHX 상아질 전처리는 혼성층 콜라겐 분해를 억제해 수복물 수명을 연장하는 근거 있는 보조 술식이나, 포함된 


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

- `yildirim-2026-cbct-earr-clear-aligner-vs-fixed-sr-ma` [orthodontics/clear-aligner] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Contextualizes the apparent contradiction with Bespalez-Neto 2026 RCT (no CA-vs-FA difference): heterogeneous case selection, smaller RCT power, and different measurement methods (AI-3D volumetric surface vs. linear CBCT landmark) account for the discordance rather than true biological contradiction.
  - ▸ 출발(`yildirim-2026-cbct-earr-clear-aligner-vs-fixed-sr-ma`) 세줄: - SR+MA (PROSPERO CRD420261320269; CBCT 전용 비교연구 6편; 392명): 투명교정 (Clear Aligner) vs 고정식 교정장치 간 외부 치근단 흡수 (External Apical Root Resorption, EARR) — CBCT 선형 계측만 포함. - 메타분석 MD = −0.50 mm (95% CI −0.79~−0.21; p<0.001; I²=60.8%) CA 우위; 비발치/혼합 하위군 (k=5) MD = −0.41 mm; 민감도 분석 (Leave-one-

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

- `erridge-2008-green-dentistry` [practice-management] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: BDJ 독자편지 (2008, Erridge): 언론의 치과 수은 비판에 반박하며 "치과에 대한 환경 감사가 이루어진 적이 있나?"라고 질문 — 치과 수은은 화산 배출 대비 오염 기여가 작고 아말감 사용은 20년간 감소 추세라고 주장.
  - ▸ 출발(`erridge-2008-green-dentistry`) 세줄: BDJ 독자편지 (2008, Erridge): 언론의 치과 수은 비판에 반박하며 "치과에 대한 환경 감사가 이루어진 적이 있나?"라고 질문 — 치과 수은은 화산 배출 대비 오염 기여가 작고 아말감 사용은 20년간 감소 추세라고 주장. 제조→진료실 폐기물·추출 공기까지 폭넓은 환경 감사, 환경 고려 치료 계획·교육 반영, '그린'의 비용효과성, BDJ의 재생지/온라인 전환을 제안 — 치과 경영·공중보건 차원의 지속가능성 의제를 2008년 시점에 문서화. 편집자 답변: BDJ는 국제 인증 지속가능 산

- `herbert-2016-aggregatibacter-actinomycetemcomitans-immunoregulator-periodontal` [oral-microbiology] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: > - 지식 공백: 비조혈계 세포(특히 조골세포) 대상 기전 연구 부족, 혈청형·균주별 이질성으로 인한 상충 결과 다수
  - ▸ 출발(`herbert-2016-aggregatibacter-actinomycetemcomitans-immunoregulator-periodontal`) 세줄: 응집간균 (Aggregatibacter actinomycetemcomitans, Aa)은 백혈구독소 (LtxA), 세포독성팽창독소 (CDT), LPS를 이용해 비조혈계(치은 상피·섬유아세포)와 조혈계(골수계·림프계) 세포 구획 전반에서 숙주 면역을 회피하고 치주 미세환경의 병적 염증을 유발한다. Aa는 여러 세포 유형에서 MAPK/NF-κB, NLRP3 인플라마좀, RANKL/OPG 신호 축을 활성화해 TNF-α·IL-1β·IL-6·IL-17 등 전염증성 사이토카인을 급증시키고, 파골세포 (Ost

- `ne-2022-treatment-dental-erosion-systematic-review` [dental-erosion] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: 포함 연구가 4편이고 방법이 이질적이며 물만 쓴 음성대조군과 획득피막 (acquired pellicle)이 없어 CPP-ACP 신호는 가설 수준이고, '불소는 효과 없음'으로 일반화하면 안 된다. 스태너스불화물 치약을 우위로 본 상위 수준 우산 리뷰 (umbrella review)를 뒤집지 못한다.
  - ▸ 출발(`ne-2022-treatment-dental-erosion-systematic-review`) 세줄: 체계적 문헌고찰 (Systematic Review, SR; 메타분석 없음): 인간 영구치에 국소 항침식제를 적용하고 인공타액 (artificial saliva) 대조군과 비교한 실험실 연구 (in vitro) 4편만 포함 (표본 n = 35, 150, 40, 36; 522편 검색), 비뚤림 위험 (risk of bias) 3편 낮음·1편 높음. 불소 치약 2편은 인공타액 대비 뚜렷한 항침식 효과가 없었고 (브라질 연구에서 Sensodyne Pronamel과 Elmex Erosion Protecti

- `chatzidimitriou-2024-role-calcium-prevention-erosive-tooth` [dental-erosion] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Calcium added to juice drinks reduced enamel loss (blackcurrant vs orange juice: 2.6 times less enamel loss, p = 0.0001, I2 = 89%); chewing gum with vs without CPP-ACP showed no significant difference in surface microhardness (p = 0.31, I2 = 71%); results for milk and CPP-ACP pastes were contradictory.
  - ▸ 출발(`chatzidimitriou-2024-role-calcium-prevention-erosive-tooth`) 세줄: 치아 침식마모 (Erosive Tooth Wear, ETW) 예방에 대한 칼슘 제제를 평가한 in situ 무작위대조시험 체계적 고찰 및 메타분석 (PROSPERO CRD42021229819)으로, 869편 중 21편이 선정되었다. 주스에 칼슘을 첨가하면 법랑질 손실이 감소했고(블랙커런트 주스가 오렌지 주스 대비 2.6배 적은 손실, p = 0.0001, I2 = 89%), 카제인 포스포펩타이드-비정질 인산칼슘 (Casein Phosphopeptide-Amorphous Calcium Phospha

- `chatzidimitriou-2024-role-calcium-prevention-erosive-tooth` [dental-erosion] (HIGH-no-target, '상반되' · 상반)
  - **근거 문장**: 주스에 칼슘을 첨가하면 법랑질 손실이 감소했고(블랙커런트 주스가 오렌지 주스 대비 2.6배 적은 손실, p = 0.0001, I2 = 89%), 카제인 포스포펩타이드-비정질 인산칼슘 (Casein Phosphopeptide-Amorphous Calcium Phosphate, CPP-ACP) 함유 껌은 유무 간 표면 미세경도 차이가 없었으며(p = 0.31, I2 = 71%), 우유와 CPP-ACP 페이스트의 결과는 상반되었다.
  - ▸ 출발(`chatzidimitriou-2024-role-calcium-prevention-erosive-tooth`) 세줄: 치아 침식마모 (Erosive Tooth Wear, ETW) 예방에 대한 칼슘 제제를 평가한 in situ 무작위대조시험 체계적 고찰 및 메타분석 (PROSPERO CRD42021229819)으로, 869편 중 21편이 선정되었다. 주스에 칼슘을 첨가하면 법랑질 손실이 감소했고(블랙커런트 주스가 오렌지 주스 대비 2.6배 적은 손실, p = 0.0001, I2 = 89%), 카제인 포스포펩타이드-비정질 인산칼슘 (Casein Phosphopeptide-Amorphous Calcium Phospha

- `chatzidimitriou-2024-role-calcium-prevention-erosive-tooth` [dental-erosion] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Of 869 retrieved studies, 21 were eligible. Calcium-fortified acidic drinks showed the clearest benefit, whereas CPP-ACP chewing gum did not differ from control gum on microhardness and milk and CPP-ACP pastes gave contradictory results. Clinical weight is therefore limited: the signal supports calcium as a dietary-acid modifier, not a proven restorative or clinical ETW-arresting treatment.
  - ▸ 출발(`chatzidimitriou-2024-role-calcium-prevention-erosive-tooth`) 세줄: 치아 침식마모 (Erosive Tooth Wear, ETW) 예방에 대한 칼슘 제제를 평가한 in situ 무작위대조시험 체계적 고찰 및 메타분석 (PROSPERO CRD42021229819)으로, 869편 중 21편이 선정되었다. 주스에 칼슘을 첨가하면 법랑질 손실이 감소했고(블랙커런트 주스가 오렌지 주스 대비 2.6배 적은 손실, p = 0.0001, I2 = 89%), 카제인 포스포펩타이드-비정질 인산칼슘 (Casein Phosphopeptide-Amorphous Calcium Phospha

- `chatzidimitriou-2024-role-calcium-prevention-erosive-tooth` [dental-erosion] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Milk and CPP-ACP pastes: contradictory.
  - ▸ 출발(`chatzidimitriou-2024-role-calcium-prevention-erosive-tooth`) 세줄: 치아 침식마모 (Erosive Tooth Wear, ETW) 예방에 대한 칼슘 제제를 평가한 in situ 무작위대조시험 체계적 고찰 및 메타분석 (PROSPERO CRD42021229819)으로, 869편 중 21편이 선정되었다. 주스에 칼슘을 첨가하면 법랑질 손실이 감소했고(블랙커런트 주스가 오렌지 주스 대비 2.6배 적은 손실, p = 0.0001, I2 = 89%), 카제인 포스포펩타이드-비정질 인산칼슘 (Casein Phosphopeptide-Amorphous Calcium Phospha

- `greenstein-2018-need-replace-missing-second-molar` [occlusion] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: - Synthesizes the paradox that super-eruption is common but occlusal interference is not a predictable downstream consequence, refuting reflexive replacement.
  - ▸ 출발(`greenstein-2018-need-replace-missing-second-molar`) 세줄: 제2대구치 (Second Molar) 결손 후 임플란트 (Implant) 수복 여부를 평가한 서술적 문헌고찰 — 저작효율 (Masticatory Efficiency)·과맹출·교합간섭 (Occlusal Interference) 데이터 종합. 제1대구치 교합만으로 저작효율 약 90% 달성; 대합치 없는 구치의 약 20%가 ≥2 mm 정출 (Supraeruption)하나, 정출 정도와 교합간섭 발생은 강한 상관이 없음. 수복 여부는 환자 선호 (Patient Preference)에 따름 — 저작 불편감

- `jeong-2022-efficacy-of-tooth-brushing-via` [periodontics/oral-hygiene-instruction] (SOFT→zini-2026-electric-vs-manual-toothbrush-children-plaque-rct, 'whereas' · 반면(대조))
  - **근거 문장**: - [[periodontics/oral-hygiene-instruction/zini-2026-electric-vs-manual-toothbrush-children-plaque-rct]] — same age group and the same Turesky-modified Quigley-Hein index family, but tests the brush itself (electric vs manual, 4 weeks) whereas this paper tests the instruction method; Zini found a significant electric advantage, this trial found no difference between instruction methods.
  - ▸ 출발(`jeong-2022-efficacy-of-tooth-brushing-via`) 세줄: 병행군 무작위대조시험 (Randomized Controlled Trial, RCT; 6–12세 학령기 아동 42명, 군당 21명; 치은염 증상 및 기저 터레스키 변형 퀴글리-하인 치태지수 (Turesky-modified Quigley-Hein index) >1.5; 연세대학교 치과병원·서울 보건소 2곳): 3차원 동작 인식 실시간 음성 피드백 스마트 칫솔·스마트 거울 (Smart Toothbrush and Smart Mirror, STM) 시스템 칫솔질 교육 (Toothbrushing Instru
  - ▸ 대상(`zini-2026-electric-vs-manual-toothbrush-children-plaque-rct`) 세줄: 4주 검사자-맹검 병렬군 RCT (n=60, 6–10세; Hadassah–Hebrew University, 이스라엘; 2025년 1–2월): 첨단 회전-진동(OR) 전동칫솔(Oral-B iO2+Gentle Care) vs 수동칫솔(Paro Junior Soft), 1,450 ppm 불소 치약 1일 2회. 전동칫솔이 전악 치면세균막(TQHPI) 51% 더 감소(조정 변화 0.670 vs 0.444; p=0.003); 모든 하위부위 유의하게 더 큰 감소: 설면 +64.3%, 인접면 +52.4%, 구치

- `namuangchan-2023-iodine-mouthwash-oral-mucositis-ccrt-rct` [oral-medicine/mucositis] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: The study failed to demonstrate statistically significant superiority of IS mouthwash over NSS for preventing CCRT-induced OM, likely due to small sample size and possibly insufficient iodine concentration. Larger-scale studies are warranted to confirm or refute any potential benefit.
  - ▸ 출발(`namuangchan-2023-iodine-mouthwash-oral-mucositis-ccrt-rct`) 세줄: 본 연구는 태국 콘켄 대학에서 2019년 1월부터 12월까지 수행된, 단일기관, 전향적, 이중맹검, 무작위대조 임상시험으로, 동시항암방사선치료(CCRT)를 받는 두경부암 환자 20명(1:1 배정)을 대상으로 자체 제조한 요오드 용액(IS) 가글의 구강점막염(OM) 예방 효과를 정상 생리식염수(NSS)와 비교 평가하였다. 1차 평가변수는 주간 구강점막염 평가 척도(OMAS) 점수로, CCRT 시작 전부터 치료 종료 4주 후까지 측정되었다. IS군과 NSS군 간 주간 평균 OMAS 점수(전체 평균 차

- `ron-canelos-2026-immediate-versus-delayed-dental-implant` [immediate-implant] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 즉시식립 vs 지연식립 논쟁을 겨냥한 최초 등록 우산논문으로, 생존·성공·실패·합병증·환자보고결과(PROM)·수술시간을 서술적으로 종합해 위키가 보유한 상충적 SR 결과(생존 차이 없음 vs IIP 실패↑)를 한 층 위에서 맥락화할 계획.
  - ▸ 출발(`ron-canelos-2026-immediate-versus-delayed-dental-implant`) 세줄: 우산논문(umbrella review) **계획서** (PRISMA-P, OSF GZ3DR, BMJ Open 2026;16:e119635) — 발치 후 즉시식립(Immediate Implant Placement, IIP, Type I, ≤10일) vs 지연식립(Type IV, 4–6개월) 비교 체계적 문헌고찰(±메타분석)들을 통합해 재평가할 프로토콜. 결과 수치는 아직 없음: 2026년 9월 MEDLINE/Embase/Scopus/Web of Science/LILACS/Cochrane + 회색문헌

- `ron-canelos-2026-immediate-versus-delayed-dental-implant` [immediate-implant] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: This BMJ Open protocol (Ron Canelos/Magrin group, UFSC Brazil + UDLA Ecuador + University of Zurich) registers the first umbrella review dedicated to immediate versus delayed dental implant placement. It will include systematic reviews with or without meta-analysis comparing Type I (immediate, ≤10 days after extraction) with Type IV (delayed, 4–6 months) placement, excluding reviews where early ty
  - ▸ 출발(`ron-canelos-2026-immediate-versus-delayed-dental-implant`) 세줄: 우산논문(umbrella review) **계획서** (PRISMA-P, OSF GZ3DR, BMJ Open 2026;16:e119635) — 발치 후 즉시식립(Immediate Implant Placement, IIP, Type I, ≤10일) vs 지연식립(Type IV, 4–6개월) 비교 체계적 문헌고찰(±메타분석)들을 통합해 재평가할 프로토콜. 결과 수치는 아직 없음: 2026년 9월 MEDLINE/Embase/Scopus/Web of Science/LILACS/Cochrane + 회색문헌

- `de-oliveira-neto-2019-immediate-dental-implants-placed-into` [immediate-implant/infected-socket] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: The authors conclude infection is a real failure risk factor, but the CI lower bound is 1.04, all studies are non-randomized two-group designs at unclear-to-high risk of bias, and infected sites were pooled without acute/chronic or endodontic/periodontal stratification — which contradicts later, larger syntheses reporting no survival difference.
  - ▸ 출발(`de-oliveira-neto-2019-immediate-dental-implants-placed-into`) 세줄: SR+MA (PROSPERO CRD42018092156; 2018년 5월까지 7개 DB; 사람 임상연구 8편·임플란트 935개; Cochrane 비뚤림 위험 전반 불명확, 참여자·시술자 눈가림은 전 연구 high risk)로, 항생제 투여·추적 1년 이상·전신질환 없는 환자만 포함해 감염 vs 비감염 발치와 즉시식립을 비교. 감염 부위의 임플란트 실패 위험비 2.99 (95% CI 1.04–8.56, p=0.04, I²=0%), 연구별 생존율 90.8–100%; 변연골 소실(MD −0.03 mm)

- `de-oliveira-neto-2019-immediate-dental-implants-placed-into` [immediate-implant/infected-socket] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 저자는 감염을 실패 위험인자로 결론짓지만 신뢰구간 하한이 1.04이고, 전 연구가 비무작위 2군 설계(불명확~높은 비뚤림 위험)이며, 감염 부위를 급성/만성·근관성/치주성으로 나누지 않고 합산했다 — 이후 더 큰 종합 연구들의 "생존율 차이 없음"과 상충한다.
  - ▸ 출발(`de-oliveira-neto-2019-immediate-dental-implants-placed-into`) 세줄: SR+MA (PROSPERO CRD42018092156; 2018년 5월까지 7개 DB; 사람 임상연구 8편·임플란트 935개; Cochrane 비뚤림 위험 전반 불명확, 참여자·시술자 눈가림은 전 연구 high risk)로, 항생제 투여·추적 1년 이상·전신질환 없는 환자만 포함해 감염 vs 비감염 발치와 즉시식립을 비교. 감염 부위의 임플란트 실패 위험비 2.99 (95% CI 1.04–8.56, p=0.04, I²=0%), 연구별 생존율 90.8–100%; 변연골 소실(MD −0.03 mm)

- `de-oliveira-neto-2019-immediate-dental-implants-placed-into` [immediate-implant/infected-socket] (HIGH-far→lee-2018-comparison-immediate-implant-placement-infected, '상충' · 상충)
  - **근거 문장**: 감염 소켓 즉시식립에 대해 위키가 보유한 SR+MA들([[immediate-implant/infected-socket/saijeva-2020-immediate-implant-placement-non-infected-sockets]] RR=0.99, [[immediate-implant/infected-socket/lee-2018-comparison-immediate-implant-placement-infected]] 생존 차이 NS, [[immediate-implant/infected-socket/pranckeviciene-2024-immediate-implant-periapical-pathology-sr-ma]])는 모두 "감염 여부로 생존율 차이 없음"인데, 이 2019 MA는 유일하게 통계적으로 유의한 
  - ▸ 출발(`de-oliveira-neto-2019-immediate-dental-implants-placed-into`) 세줄: SR+MA (PROSPERO CRD42018092156; 2018년 5월까지 7개 DB; 사람 임상연구 8편·임플란트 935개; Cochrane 비뚤림 위험 전반 불명확, 참여자·시술자 눈가림은 전 연구 high risk)로, 항생제 투여·추적 1년 이상·전신질환 없는 환자만 포함해 감염 vs 비감염 발치와 즉시식립을 비교. 감염 부위의 임플란트 실패 위험비 2.99 (95% CI 1.04–8.56, p=0.04, I²=0%), 연구별 생존율 90.8–100%; 변연골 소실(MD −0.03 mm)

- `huynh-ba-2010-analysis-socket-bone-wall` [immediate-implant/anatomic-assessment] (HIGH-far→huynh-ba-2018-immediate-loading-vs-early-conventional, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[immediate-implant/loading-protocol/huynh-ba-2018-immediate-loading-vs-early-conventional]] — **Same first author, unrelated question.** Huynh-Ba's 2018 SR (PROSPERO #49604, 9 studies, no meta-analysis) asks a patient-reported-outcome question about *loading* timing for Type 1 single-tooth implants. It is a different study on a different axis, not a sibling report of the trial this page's measu
  - ▸ 출발(`huynh-ba-2010-analysis-socket-bone-wall`) 세줄: 횡단적 형태계측 연구 (n = 93 발치 부위, 상악 심미 영역 — 견치~견치 및 제2소수치; 진행 중인 전향적 무작위대조 다중임상시험 (Prospective Randomized-Controlled Multicenter Clinical Trial)의 일부, Clin Oral Implants Res 2010) — 발치 시점에 협측·구개측 치조 골벽 두께를 직접 계측. 협측 평균 1 mm vs 구개측 1.2 mm (P<0.05); 전방(견치~견치) 협측 평균 0.8 mm vs 구개부(제2소수치) 1.

- `smoking-tobacco-periodontal-implant-overview` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: > - **조기 실패에서는 결과가 갈린다 (갱신 2026-09-29)**: Zhang 2025(후향, 3,533개, 다변량 흡연 OR 2.148, 초록만)·Stiller 2024(서술적 SR 33편 중 25편 유의, 통합 추정치 없음)는 방향이 일치하지만, Wåhlberg 2025(스웨덴 다기관 후향, 환자 1,875명, 조기 실패 63명)는 흡연이 조기 **실패**에 비유의(다변량 OR 1.61, 95% CI 0.88–2.94)이고 조기 **합병증**에만 유의(OR 2.30)했다. Fan 2024의 OR 2.59를 뒤집지는 않으나 "흡연 = 조기 실패 확정 위험"이라는 단정은 피하고 합병증까지 함께 고지.
  - ▸ 출발(`smoking-tobacco-periodontal-implant-overview`) 세줄: 흡연·담배제품과 치주-임플란트 위험 14편 종합 — 기전(Apatzidou 2022) → 임플란트 생존/MBL 수렴 근거(Mustapha 2022·Fan 2024·**Calciolari 2026**) → 용량-반응(Naseri 2020) → 금연 효과(Caggiano 2022) → 수술 합병증(Wang 2023, 슈나이더막 천공) → 2026년 신규 노출경로(Ye 2026 비흡연자 간접흡연, La Rosa 2026 전자담배 미생물총, Calciolari 2026의 무연담배·전자담배 하위분석). 궐

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

- `immediate-implant-infected-sites-decision` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: > - **증거 구조**: Pranckeviciene 2024 SR+MA (22편, 앵커)·Saijeva 2020 SR+MA (9편, n=2,281)·AlMugeiren 2024 MA (RCT 10편, n=849)·Amato 2025 후향적 (n=143, 2–12년 추적) 포함 초기 10편에, 2026-09-29 갱신에서 Elaskary 2024를 포함해 총 21편이 되도록 10편(상충 MA 1·후향/비교 코호트 4·증례/증례군 5)을 추가.
  - ▸ 출발(`immediate-implant-infected-sites-decision`) 세줄: 21편(SR+MA 4·SR 1·MA 1·전향/비교 5·후향 5·증례/증례군 5; 2015–2026) 합성: 핵심 변수는 '감염 자체'가 아닌 **감염 유형** — 만성 치근단 병변(chronic periapical lesion)은 철저한 소파+항생제 예방 시 비감염 부위와 생존율 동등(RR=0.99, Saijeva 2020; Pranckeviciene 2024 SR+MA); 급성 화농성 농양(acute purulent abscess)은 8–12주 조기식립(Early placement)이 24개월 

- `immediate-implant-infected-sites-decision` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: > - **상충 근거 (갱신 2026-09-29)**: de Oliveira-Neto 2019 MA(8편·임플란트 935개)는 감염 부위 즉시식립의 **실패 RR 2.99**(95% CI 1.04–8.56, p=0.04)로 위 "차이 없음"과 반대다. 신뢰구간 하한이 1.04이고 전 연구가 비무작위 2군·비뚤림 위험 불명확~높음이며 감염 유형(급성/만성, 근관성/치주성)을 나누지 않아, 이 오버뷰의 핵심 명제(감염 **유형**이 변수)를 검증하지도 반박하지도 못한다 — 그 논문 저자도 유형별 층화를 향후 과제로 제시.
  - ▸ 출발(`immediate-implant-infected-sites-decision`) 세줄: 21편(SR+MA 4·SR 1·MA 1·전향/비교 5·후향 5·증례/증례군 5; 2015–2026) 합성: 핵심 변수는 '감염 자체'가 아닌 **감염 유형** — 만성 치근단 병변(chronic periapical lesion)은 철저한 소파+항생제 예방 시 비감염 부위와 생존율 동등(RR=0.99, Saijeva 2020; Pranckeviciene 2024 SR+MA); 급성 화농성 농양(acute purulent abscess)은 8–12주 조기식립(Early placement)이 24개월 

- `immediate-implant-infected-sites-decision` [overviews] (HIGH-no-target, 'Contradict' · 반박·충돌)
  - **근거 문장**: **Contradicting evidence — de Oliveira-Neto 2019 [확인].** This MA (8 non-randomized two-group studies, 935 implants, all with antibiotics) reports a failure RR of 2.99 (95% CI 1.04–8.56) for infected vs non-infected sites, the only held synthesis with a significant survival penalty; AlMugeiren 2024 (OR=2.08) leans the same way. Saijeva 2020 (9 cohorts, 2,281 sockets, RR=0.99) and Pranckeviciene 202
  - ▸ 출발(`immediate-implant-infected-sites-decision`) 세줄: 21편(SR+MA 4·SR 1·MA 1·전향/비교 5·후향 5·증례/증례군 5; 2015–2026) 합성: 핵심 변수는 '감염 자체'가 아닌 **감염 유형** — 만성 치근단 병변(chronic periapical lesion)은 철저한 소파+항생제 예방 시 비감염 부위와 생존율 동등(RR=0.99, Saijeva 2020; Pranckeviciene 2024 SR+MA); 급성 화농성 농양(acute purulent abscess)은 8–12주 조기식립(Early placement)이 24개월 

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

- `high-insertion-torque-primary-stability-crestal-bone-overview` [overviews] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: Lemos's pooled null is absence of evidence rather than evidence of absence — RR 0.51 (95% CI 0.06–4.06) and MBL MD 0.15 mm (95% CI −0.14–0.44) across only 6 studies, averaging populations whose effect sign is opposite; critically, **all human primary studies held — the three above plus Khayat 2011 (up to 176 Ncm, 1-y MBL null), added 2026-09-30 with Manfredini 2025 and Nascimento 2024 — classified
  - ▸ 출발(`high-insertion-torque-primary-stability-crestal-bone-overview`) 세줄: 고삽입토크(IT) 5편은 서로 어긋나 보이지만 — Trisi 2011(양 분할구강 조직학, 40개, 110 vs 10 Ncm), Marconcini 2018(RCT, 치유부위 단일 116개, 3년), Aldahlawi 2018(후향, NobelActive 113개), Faot 2019(전향, 위축 무치악 하악 세경 ø2.9mm 62개, 1년), Lemos 2020(SR+MA, 6편/651개) — IT를 *투여한 용량*이 아니라 *저항한 골을 읽은 값*으로 보면 정합적으로 풀린다. 2026-07-1

- `tmj-dislocation-reduction-recurrence-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Nothing in this chain is a contradiction of fact. The consensus did not find contrary data; it declined to recommend a technique its voters could not perform. That is a legitimate guideline decision — a recommendation to use an unfamiliar manoeuvre in an emergency is a recommendation to fail at it — but it has a clear corollary for the wiki: **the technique with the best randomized support is the 
  - ▸ 출발(`tmj-dislocation-reduction-recurrence-overview`) 세줄: 악관절 탈구 10편은 문헌이 뒤섞어 다루는 두 임상 문제로 깔끔히 갈린다 — 과두를 되돌리는 **복원 (reduction)** 과 다시 빠지지 않게 하는 **재발 방지 (recurrence prevention)**. 10편 중 메타분석은 0편이므로 이 근거 기반 어디에도 통합 추정치는 없다. 임상 부담이 큰 쪽은 두 번째다: 헬싱키 260명에서 평생 2회 이상 탈구가 **61.9%** 이고, 저자들은 재발성 탈구의 급성 복원을 "일시적 처치"로 규정한다. 술기 축에서 유일한 3군 무작위 비교는 *

- `tmj-dislocation-reduction-recurrence-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: ### 2.2 Dextrose prolotherapy — a real contradiction, resolved by comparator
  - ▸ 출발(`tmj-dislocation-reduction-recurrence-overview`) 세줄: 악관절 탈구 10편은 문헌이 뒤섞어 다루는 두 임상 문제로 깔끔히 갈린다 — 과두를 되돌리는 **복원 (reduction)** 과 다시 빠지지 않게 하는 **재발 방지 (recurrence prevention)**. 10편 중 메타분석은 0편이므로 이 근거 기반 어디에도 통합 추정치는 없다. 임상 부담이 큰 쪽은 두 번째다: 헬싱키 260명에서 평생 2회 이상 탈구가 **61.9%** 이고, 저자들은 재발성 탈구의 급성 복원을 "일시적 처치"로 규정한다. 술기 축에서 유일한 3군 무작위 비교는 *

- `penicillin-allergy-dental-antibiotic-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: 5. **The sinus-lift allergy recommendation is internally contradictory in the wiki** (ciprofloxacin per SEI 2022 vs clindamycin per Díaz 2025), and neither rests on outcome data in penicillin-allergic sinus-lift patients. A paper measuring infection outcomes by agent in this subgroup would resolve a real chairside question.
  - ▸ 출발(`penicillin-allergy-dental-antibiotic-overview`) 세줄: 위키 17편(합의문 2·체계적문헌고찰+메타분석 3·체계적문헌고찰 3·내러티브리뷰 3·후향/단면 미생물·약물역학 자료 4)을 종합: 치과에서 페니실린 알레르기 환자의 실제 1차 문제는 알레르기가 아니라 **알레르기 라벨**이다 — 인구의 약 10%가 보유하나 자가보고 라벨의 80–99%는 검사에서 부정되며, 그 라벨이 촉발하는 반사적 대체 처방이 더 큰 위해가 되었다. 오래 가르쳐온 두 수치가 바뀌었다: 페니실린–세팔로스포린 교차반응은 전체 0.7%·확진 페니실린 알레르기에서 3%로 과거 8–10%

- `clear-aligner-attachments-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: The held evidence answers two different questions, and conflating them produces an apparent contradiction.
  - ▸ 출발(`clear-aligner-attachments-overview`) 세줄: 투명교정 어태치먼트(Composite Attachment) 근거를 종합 — 어태치먼트 전용 6편(SR 2·SR+MA 1·단일모델 FEA 2·split-mouth RCT 1)에 정출·회전 정확도·레진/보철물 접착·FEA 기전·어태치먼트 주위 탈회·스캔 정확도 관련 보조 7편을 더했다. 일관된 신호는 어태치먼트의 **존재**가 이동 발현과 유지력을 높이고 정출의 전제조건이라는 것이며, **종류**(최적화형 vs 재래형)는 임상 정확도 우위가 없고 둘 다 계획 이동량에 못 미친다. 일반 vs 벌크필 플

- `implant-surface-comparison` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: > **모범답안**: **수정해야 한다.** 이 오버뷰는 2026-08 근거 갱신으로 HA/TCP 코팅에 대한 우호적 서술을 **뒤집었다**: Damerau 2021(대형동물 15편 SR+MA)에서 이미 거친(rough) 비코팅 티타늄 대비 TCP/HA 코팅은 BIC 유의 우위 없음이 확인됐고, HA는 오히려 14일차에 BIC가 유의하게 낮았다(−6.94%p, p=0.001). "작은 표본 단일 연구가 큰 표본 메타분석에 뒤집힌 사례"로 명시돼 있다. 단, Mg 코팅(Alenezi 2026, BIC 유의 향상)과 Ag 코팅은 전임상에서 여전히 가능성이 있으나 인체 RCT 없음.
  - ▸ 출발(`implant-surface-comparison`) 세줄: 임플란트 표면처리 15편 + 5편 횡단인용 종합 매트릭스: SLA/SA = 임상 표준(8년 생존 94.8%, Kim 2020 n=96); 친수성(CA/SLActive) = D3/D4 골에서 stability dip 제거, 절대 ISQ 상승은 아님(CA 5.2년 97.3%, MBL 0.074 mm, Kim 2022 n=258); UV 광기능화(UV-PF) = 위축골·복잡증례 1순위(ISQ +21.9, 7년 100% 성공, Hirota 2020 전향적). 표면처리의 핵심 기전은 친수성이 아니라 탄화수

- `socket-preservation-arp-overview` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: > - **PRGF ARP RCT — 심미부 신생골 + 조기 연조직 이득 (Anitua 2026, n=46)**: 전치부 ARP에서 혈소판 풍부 성장인자 (Plasma Rich in Growth Factors, PRGF) vs 자연치유 12주 비교 — 신생골 형성 48.7% vs 36.1%, p=0.024; 3일 통증·3/5/7일 연조직 치유 모두 PRGF 우월(p<0.05). PRGF 클래스(BTI 시스템)는 L-PRF와 제조 프로토콜 달라 직접 교환 불가; Alavi 2024 L-PRF null 결과와 상충되는 것처럼 보이나 **제조방식 차이와 관찰 시점(12주 vs 장기 차원) 차이**로 설명 가능.
  - ▸ 출발(`socket-preservation-arp-overview`) 세줄: 다편 종합 — 발치와 보존술(Alveolar Ridge Preservation, ARP)은 발치 후 치조제 손실을 줄이지만 없애지는 못함(무처치 시 수평 ~50%·수직 30–40% 손실; 다발골(bundle bone) 소실은 필연적이며 즉시식립 단독으로도 막지 못함). 소켓 해부(ST 분류·골오목 깊이/각도·소켓 무결성)가 이식재 선택보다 강한 예후 예측인자; 콜라겐 플러그 단독은 높이만 보존·폭경 불충분; 이종골(DBBM/Bio-Oss Collagen) ± PRF 추가로 폭경 개선(Kollati

- `patient-recall-retention-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: The wiki holds two findings that look contradictory and are not:
  - ▸ 출발(`patient-recall-retention-overview`) 세줄: 19편 종합(치주·임플란트주위 유지관리 + 예약 내원 + 행동변화) — "구환 리콜"을 3층 운영 시스템으로 재정의: ① 누구를 언제 부를지 ② 예약된 방문이 실제로 일어나게 하는 법 ③ 애초에 왜 다시 오는지. 층별 근거 강도가 급격히 다르다: ②는 내원 RCT 2편 + 196,018건 머신러닝 모델(SMS vs 무 79.2% vs 35.5%, Prasad 2012; 음성>SMS 보정 OR 2.12, Nelson 2011; 리드타임이 최강 예측인자, Alabdulkarim 2022)로 가장 단단

- `full-arch-fixed-four-vs-six-implants-overview` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: > - **반대 신호 (La Monaca 2022)**: 단일기관 후향·비무작위(술자 판단 배정), 28명·보철 32개·164 임플란트, 평균 6.5년, 가이드 무피판 즉시부하 — 임플란트 생존 **all-on-4 89.7% vs all-on-6 99.0%**, 생물학적 합병증 **10.3% vs 1.0% (p=0.014)**; MBL은 군간 차이 없음(p=0.104). 소규모·선택편향 가능성 때문에 RCT·대규모 코호트의 생존 동등성을 뒤집지는 못하지만, "4개의 대가"를 기술적 합병증에서 생물학적 합병증·임플란트 1개 상실의 여유 부족까지 넓히는 신호.
  - ▸ 출발(`full-arch-fixed-four-vs-six-implants-overview`) 세줄: 무치악 고정성 풀아치 임플란트 4개 vs 6개 결정을 임상 성적 축(RCT 2편+후향 코호트 2편)·생체역학 축(FEA 2편)·2026 글로벌 컨센서스 축(지침+그룹 3 보고서 2편)으로 종합한 8편. 생존은 강한 설계에서 대체로 개수 무관(Toia 3·5년 RCT 양군 ~100%; Caramés 2025 943명/5,989 임플란트 5년 98.4% vs 98.7%, 개수가 아니라 악궁·연령이 실패 예측)이나 소규모 비무작위 코호트는 all-on-4 생존 89.7% vs 99.0%·생물학적 합병증

- `direct-resin-restoration-adhesion-placement-overview` [overviews] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: Bulk-fill and incremental placement are clinically equivalent through ≥24 months (9-RCT MA RR 0.82 NS; 12-RCT NMA no significant difference; umbrella review; Zailai 2025, Chaple-Gil 2026) — conditional on a conventional occlusal cover layer, since uncovered bulk-fills wear 2–4× a nanohybrid (Osiewicz 2022) — and the claim "low-shrinkage = clinically superior" is refuted by 21-RCT MA (Kruly 2018).
  - ▸ 출발(`direct-resin-restoration-adhesion-placement-overview`) 세줄: Cochrane SR·우산형 리뷰·SR+MA/NMA·대규모 RCT·독일 S3 가이드라인을 아우르는 직접 복합레진 수복의 두 축 종합; 갈림길은 EAR이냐 SE냐가 아니라 **법랑질에 인산을 대느냐**다(Hong 2021 SR+MA; Oza 2022 SE 단독 24개월 부적합; Peumans 2023 3년 RCT E&R≈SEE 동등; Omoto 2025 4년 RCT 무산부식군만 기저치 이하). 벌크필과 적층충전은 ≥24개월 임상 동등(9-RCT MA RR 0.82 NS·12-RCT NMA 차이 없음

- `immediate-implant-evidence-survival-timing-infected-loading-overview` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: 즉시 vs 지연 생존 갈등은 해소: Mello 2017(관찰포함 30편 ~3%p 열세)은 **García-Sánchez 2022에 의해 완전 superseded**(2026-08) — RCT만 보면 생존 무차이이고 설계 편향이 원인이며, 독립 SR+MA인 Patel 2023(비교연구 10편, 위험비 0.99, I²=0%, 97.4% vs 97.5%)이 이질성 0%로 같은 결론을 재확인한다. 동일한 트레이드오프(골·PES 우세, 실패율 비유의 증가)가 **하나의 210명 3군 RCT 내부**(Felice 2016/Esposito 2017)에서도 재현 — 즉시·즉시지연이 골·PES는 유의 우위이나 실패율은 비유의하게 더 높은 경향(4개월→1년 안정). 부위·직경이 방향을 뒤집기도 함 — Checchi 2017(
  - ▸ 출발(`immediate-implant-evidence-survival-timing-infected-loading-overview`) 세줄: 즉시식립(Type 1)의 5개 결정축(생존·타이밍·감염소켓·부하/보철·환자체감)을 27편으로 종합한 허브: 생존율의 새 기준은 Gallucci 2026(PROSPERO 갱신 SR, 140편·10,456임플란트) — 9조합 가중생존율에서 Type 1A(즉시+즉시부하) 98.0%(검증됨) 대비 **Type 1B(즉시+조기부하) 91.6%(미검증)**로 손실률 약 4배 차이. 즉시 vs 지연 생존 갈등은 해소: Mello 2017(관찰포함 30편 ~3%p 열세)은 **García-Sánchez 2022

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

- `systemic-disease-ckd-ssc-diabetes-osteoporosis-dental-overview` [overviews] (HIGH-far→fernandes-2015-immunologic-glycemic-postextraction-t2dm, 'contradict' · 반박·충돌)
  - **근거 문장**: - [[oral-surgery/fernandes-2015-immunologic-glycemic-postextraction-t2dm]] — prospective case-control (T2DM n=53 vs controls n=29): even with impaired neutrophil function and poor glycemic control, NO increase in postextraction complications — contradicts intuitive expectation; JADA 2015 Vol 146 Issue 8
  - ▸ 출발(`systemic-disease-ckd-ssc-diabetes-osteoporosis-dental-overview`) 세줄: 소아 CKD·당뇨+골다공증(임플란트)·전신경화증 3종의 구강·치과적 영향을 세 편의 서술적 종설(Elhusseiny 2024, Guadarrama Bello 2026, Sharma 2024)로 종합한 합성 개요. 소아 CKD는 타액 완충으로 우식은 적으나 법랑질 형성저하(31–83%)·치은출혈(95.8%)이 두드러지고; 당뇨는 대사 이상(AGE-RAGE·M1 염증)으로 임플란트 통합을 저해하고 골다공증은 골 구조를 악화(BIC·BV/TV 감소)시키나 조절 양호 시 생존율 >90%; 전신경화증은 소

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

- `dental-erosion-epidemiology-risk-factors-management-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: **Calcium-enriched acidic beverages**: Chatzidimitriou's 2024 SR+MA (21 in situ RCTs) found calcium-enriched orange juice caused 2.6-fold less enamel surface loss than plain acidic equivalent. Calcium-enriched products effectively neutralize the proton-driven dissolution by saturating the oral fluid with calcium ions near the enamel surface. CPP-ACP chewing gum showed no statistically significant 
  - ▸ 출발(`dental-erosion-epidemiology-risk-factors-management-overview`) 세줄: 9편(SR+MA 5, SR 1, in situ SR+MA 1, 정책 1, GERD SR 1) 종합: ETW 유병률 유치열 35.6%~성인 80%; 고위험군은 섭식장애 65%, GERD 54.1%로 급격히 높아져 위험인자 계층화가 필수 — 치과 진료실이 섭식장애·역류 첫 발견 기회. 정량 위험인자: 성인에서 산성식품 OR 2.40·역류 OR 2.27·소화기 장애 OR 1.81; 유치열에서 산성음료 OR 6.90·GERD OR 1.98; 빨대 보호 OR 0.58; 취침 전 탄산음료 OR 7.8(단일 

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

- `masticatory-muscle-pain-evidence-synthesis-2026` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: > - **결론(thesis)**: 24편은 사다리 순서를 뒤집지 않는다 — 능동치료(도수치료(Manual Therapy, MT)·운동·심리행동) 우선, 장치·전기물리는 보조, 보툴리눔독소 A(Botulinum Toxin Type A, BoNT-A)는 불응 시. 바뀌는 것은 **확실성 수준과 개별 모달리티의 등급**이다.
  - ▸ 출발(`masticatory-muscle-pain-evidence-synthesis-2026`) 세줄: 새 사다리가 아닌 업데이트 층: 근육형 저작근 통증 SR/MA/NMA 24편(전문 6·초록만 18)을 기존 TMD overview 4편과 대조 — 능동치료 우선 순서는 확인(MT는 치료 NMA 3편 모두 상위 2위)되나, MFR 전용 GRADE는 낮음이고 스플린트·레이저·건침·BoNT-A는 하향 또는 단서 추가. 핵심 충돌은 진짜 모순이 아니라 비교군·대상군 차이: MT 1위(Al-Moraissi 2021, 위약 대조, ~2018) vs PBM 1위(Zhang 2026, 통상치료 대조, ~2025

- `implant-placement-drilling-torque-compression-overview` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: > - **치유챔버 거시형태 (Healing Chamber Macrogeometry)**: 동일 골절개에서 치유챔버 디자인이 IT를 29% 낮춤(5.70 vs 8.01 Ncm)에도 21일 후 중간·심부 골-임플란트 접촉률 (BIC)이 유의하게 높음 — C2 59.30% vs 40.30%, C3 42.10% vs 17.90% (Gehrke 2026 토끼 경골). **낮은 IT = 나쁜 결과'라는 직관을 반박** — IT와 BIC가 해리될 수 있음.
  - ▸ 출발(`implant-placement-drilling-torque-compression-overview`) 세줄: 7편(증례+문헌고찰 1·in vitro 2·전임상 in vivo 1·내러티브 리뷰 3) 종합: 골 압박 괴사는 35-50 Ncm에서도 D2 골+프리태핑 없음+언더사이즈 드릴링 조합에서 발생 가능하며 조직학적으로 확인(Ramesh 2024); 드릴링 프로토콜이 IT를 골밀도별로 고도 유의하게 변화시키나 D4에서는 효과 소진(Stoilov 2025); 치유챔버 거시형태는 IT 29% 낮추면서도 BIC 59.30% vs 40.30% 달성 — IT≠BIC 해리 중요 (Gehrke 2026). 토크 렌치는

- `clear-aligner-indications-limitations` [overviews] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: > - **상악확장**: 성장기서 CAT 확장은 가능하나 conventional expander 대비 유의 적음(Fonseca-Planells 2026), 확장은 주로 **치조성(dentoalveolar)**, 골격엔 conventional 우위. 성인 예측성 후향코호트(de la Rosa-Gay 2025, 98명·multilevel GLMM) — Invisalign 확장 **오차 0.92 mm·과소확장 72.2%**, 상악·구치·crossbite·대량 계획확장일수록 악화. 성인 SR+MA 최초(xianggang 2026, 6편·233명, GRADE 포함) — 부위별 예측성: **1소구치 80.73%(GRADE high·최고)** > 2소구치 78.74%(GRADE moderate) > 1대구치 71.57%
  - ▸ 출발(`clear-aligner-indications-limitations`) 세줄: 투명교정(Clear Aligner Therapy, CAT) 위키 78편을 효율(착용 프로토콜·개방교합 기전·제품라인별 예측성 포함)·이동특이 한계(발치 Roller Coaster Effect·스피 곡선 성형 실패·전치 3D 정확도·구치 근원심 SR·발치 공간폐쇄 SR+MA 포함)·Class II 전략·Class III camouflage/성장기 증례(수술 후 CAT SR 포함)·생체역학/설계(attachment 재료과학·실측 force/moment·브랜드 VTS 비교 포함)·확장(혼합치열 2년 안

- `clear-aligner-indications-limitations` [overviews] (SOFT→serafin-2026-invisalign-first-mixed-dentition-expansion-sr-ma, 'unlike' · 다름)
  - **근거 문장**: The first SR+MA specific to **Invisalign First mixed-dentition expansion** provides pooled predictability benchmarks: [[orthodontics/clear-aligner/serafin-2026-invisalign-first-mixed-dentition-expansion-sr-ma]] (9 studies; PROSPERO) found maxillary expansion predictability of **65%** and mandibular of **71%**, with notably **no dose-response between the amount of planned expansion and achieved pre
  - ▸ 출발(`clear-aligner-indications-limitations`) 세줄: 투명교정(Clear Aligner Therapy, CAT) 위키 78편을 효율(착용 프로토콜·개방교합 기전·제품라인별 예측성 포함)·이동특이 한계(발치 Roller Coaster Effect·스피 곡선 성형 실패·전치 3D 정확도·구치 근원심 SR·발치 공간폐쇄 SR+MA 포함)·Class II 전략·Class III camouflage/성장기 증례(수술 후 CAT SR 포함)·생체역학/설계(attachment 재료과학·실측 force/moment·브랜드 VTS 비교 포함)·확장(혼합치열 2년 안
  - ▸ 대상(`serafin-2026-invisalign-first-mixed-dentition-expansion-sr-ma`) 세줄: 혼합치열 Invisalign First 확장 SR+MA (PROSPERO 등록, 9편 포함/8편 메타분석); 상악·하악 따로 비율 메타분석(로짓 스케일 이항 모델); ROBINS-I·GRADE 평가. 상악 예측성(predictability) 65%(GRADE 낮음; 범위: 영구대구치 58%~유견치 70%), 하악 71%(GRADE 보통; 유견치 75% 최고); 예정확장량과 달성 예측성 간 상관·회귀 모두 유의하지 않음. Invisalign First는 혼합치열 확장에서 중등도 예측성 — 하악·전치

- `digital-workflow-decision-ladder` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: > - 축1 보강(2026-09): 고정성 교정장치(브라켓±와이어) 존재 시엔 자연치 원칙이 뒤집혀 IOS가 알지네이트보다 우수(28–141 vs 103–212µm, Schlenz 2022); 클리어얼라이너 부착물 모형에서도 Primescan·TRIOS 3가 최상위 재확인, 오차 목표 ~50µm(Oğuz 2026); 정확도가 혼재된 상황에서도 chairside time·환자 편의는 측정된 연구 전부에서 IOS 우위이나 근거는 10편 중 2편 한정(Ramos-Morro 2026). [확인]
  - ▸ 출발(`digital-workflow-decision-ladder`) 세줄: 28편 4축 결정 사다리(IOS 정확도 4 SR/우산형+2 in-vitro, CAIS SR+NMA, AI 진단 다수 SR/후향, LLM SR+MA+우산형): IOS는 단관·소악궁 임상 표준(trueness 50–100µm)이나 전악·무치악 오차 누적(50–200µm), 무치악은 기공실 스캐너·전통 인상 우선. CAIS: 즉시식립·심미·다중 임플란트에서 dynamic/full-static이 freehand 우위(Schiavon 2025 SR+NMA, 7 RCT, 338 임플란트); AI 진단은 우식

- `unopposed-tooth-overeruption-overview` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: > - 흔한 오판: "엔도한 치아라 더/덜 정출한다"(근거 없음·기전상 무관), "크라운 씌우면 정출 안 한다"(전체 치아가 이동), "대합치 없으면 무조건 빨리 보철"(저위험치는 과한 개입), "정출은 수직만"(경사·회전 동반), "인접 치아가 공간 채우면 정출 해결"(Smith 1996 반박).
  - ▸ 출발(`unopposed-tooth-overeruption-overview`) 세줄: 17편 종합: 대합치 없는 후방 치아의 ~83%가 정출(단기 ~9개월 평균 0.43 mm / 최대 0.75 mm; CBCT 5년 기준 근심교두 1.37 mm [Hong 2023]; ~72%는 1 mm 미만; 초기 최대 속도; 수직+협측경사+회전 3D); ~18%는 전혀 안 움직임; 정출은 PDL·치조골 매개라 치수 생활력 무관. 고정 retention도 부분접촉 대비 효과 없어(Livas 2016); 5년 후 인접 하악 제2대구치 근심 경사 (Mesial Tipping) 57.47°·협측 CEJ 

- `unopposed-tooth-overeruption-overview` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: > - **연령 효과의 경계 (중요 — 이번 개정에서 조정)**: "젊을수록 많이 정출"의 강한 근거는 **랫드 실험**(Fujita 2009, Denes 2020)이다. 사람 데이터로 연령을 조절인자로 검정한 유일한 풀링 분석인 Fan 2026 메타회귀에서는 **연령이 유의하지 않았다**. 뒤집혔다기보다 **측정 대상이 다르다** — 랫드는 어린 개체 vs 성체의 정출 *속도·크기*, Fan은 성인 코호트 안에서의 교합 *재확립 성공 여부*. 임상 함의: 성인 환자에서 "나이가 어리니 훨씬 빠를 것"이라는 추정은 동물 근거에 기대고 있으며 성인 연령대 안에서는 검증되지 않았다.
  - ▸ 출발(`unopposed-tooth-overeruption-overview`) 세줄: 17편 종합: 대합치 없는 후방 치아의 ~83%가 정출(단기 ~9개월 평균 0.43 mm / 최대 0.75 mm; CBCT 5년 기준 근심교두 1.37 mm [Hong 2023]; ~72%는 1 mm 미만; 초기 최대 속도; 수직+협측경사+회전 3D); ~18%는 전혀 안 움직임; 정출은 PDL·치조골 매개라 치수 생활력 무관. 고정 retention도 부분접촉 대비 효과 없어(Livas 2016); 5년 후 인접 하악 제2대구치 근심 경사 (Mesial Tipping) 57.47°·협측 CEJ 

- `osteotomy-drilling-heat-determinants-irrigation-overview` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: > - **상황 증폭인자 — 가이드수술(guided surgery)**: 금속 슬리브가 외부 관주를 차단해 **피질골 입구부에서만** 발열↑(Markovic: 입구 p<0.001, 중간·바닥 NS; 가이드온도↔골온도 rho=0.868). SR도 가이드>비가이드 발열 확인, 1500–2000 rpm에서 역치 돌파 사례(Saxena) → full-guided라면 냉각(~10°C) saline + 800–1200 rpm + peck drilling. **[2026-10-02 추가] Gökçe-Uçkun 2025 엑스비보 양 장골능(D3, n=40, 192 와위)이 이를 정량 확인**: 10°C 냉세척이 24°C 세척·저속무세척보다 유의하게 저온(p=0.001); 저속무세척(300–600rpm)은 안전하지 않으며 
  - ▸ 출발(`osteotomy-drilling-heat-determinants-irrigation-overview`) 세줄: 임플란트 골절제 드릴링 발열 36편을 "요인 나열"이 아니라 **무엇을 실제로 통제할지의 근거가중 순위**로 재구성: 47°C/1분 괴사 역치(Timon 2019 교차검증; 정형외과 ~50°C), 다인자 프레이밍(Chauhan 2018 SR 34편; Jung 2021 내부·외부 인자 분류), 생물학적 endpoint(Heuzeroth 2021 in vivo 미니피그 n=36; Kosior 2025 조직학적 골상 점수). 여러 결정인자를 맞대결시킨 연구에서 **관주 온도가 가장 재현성 높은 지렛대*

- `vitamin-d-osseointegration-implant-overview` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Vitamin D is biologically tied to bone metabolism (calcium homeostasis, osteoblast differentiation, immunomodulation), so a pro-osseointegration role is mechanistically plausible. The wiki holds 9 papers spanning the full evidence ladder, and they do **not** all agree. This page resolves the apparent contradiction.
  - ▸ 출발(`vitamin-d-osseointegration-implant-overview`) 세줄: 비타민 D[25(OH)D]와 임플란트 골유착(Osseointegration) 9편(우산형 1·SR 3·RCT 1·전향 2·후향 1·서사적 종설 1) 종합 — 기전/동물·SR/MA·사람 임상 근거 사다리 전반; Tallon 2024 우산형 고찰은 메타분석 부재·기준치·용량·결과지표 불일치를 명시. 동물·기전 근거는 일관되게 양성; 사람 근거는 결핍 중증도에 따라 갈림 — 양성 신호가 중증 결핍(<10~20 ng/mL)+동반위험에 몰림(Mohsen 2024: 실패율 <10 ng/mL 46.2% vs 

- `nccl-etiology-diagnosis-management-overview` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: > - 병인: stress(abfraction)·friction(abrasion)·biocorrosion(erosion)의 case-specific 다인성 조합. 교합응력 단독원인설은 임상적으로 미입증 — SR 3편이 충돌(Senna 2012·Silva 2013 연관 약함 / Duangthip 2017 81% 연관 but lab 가중 / Dioguardi 2024 scoping 확정·반박 불가).
  - ▸ 출발(`nccl-etiology-diagnosis-management-overview`) 세줄: 비우식성 치경부 병소(Noncarious Cervical Lesion, NCCL) 36편 종합 — 병인은 다인성이며 abfraction 단독원인설은 미입증: SR 3편이 충돌하고, 최초 16년 코호트(Giller 2024)는 교합 마모(Occlusal Wear, OW)–NCCL이 횡단면으로는 연관(OR 1.74)되나 종단으로는 진행을 예측하지 못함(OR 1.14, 비유의)을 보였다; 상아질 과민증(Dentin Hypersensitivity, DH)의 교정 가능한 연관인자는 식후 즉시 칫솔질·미백치

- `nccl-etiology-diagnosis-management-overview` [overviews] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: - "교합응력→abfraction"이 모든 NCCL의 주원인이라는 강한 주장은 임상적으로 미입증이다. SR 근거가 갈리고(Senna 2012·Silva 2013 연관 약함 / Duangthip 2017 81% 연관 but lab 가중 / Dioguardi 2024 확정·반박 불가), **최초의 장기 종단 코호트(Giller 2024)는 횡단면 연관(OR 1.74)을 재현하면서도 16년 종단 연관(OR 1.14, CI 0.99–1.30)은 유의하지 않았다** — 공존은 확실, 인과·진행 예측은 미입증. 단 종단 분석(226명·718치아)은 검정력이 부족할 수 있어 "약한 효과 없음"을 증명한 것은 아니다. [확인 — SR 충돌 + 코호트]
  - ▸ 출발(`nccl-etiology-diagnosis-management-overview`) 세줄: 비우식성 치경부 병소(Noncarious Cervical Lesion, NCCL) 36편 종합 — 병인은 다인성이며 abfraction 단독원인설은 미입증: SR 3편이 충돌하고, 최초 16년 코호트(Giller 2024)는 교합 마모(Occlusal Wear, OW)–NCCL이 횡단면으로는 연관(OR 1.74)되나 종단으로는 진행을 예측하지 못함(OR 1.14, 비유의)을 보였다; 상아질 과민증(Dentin Hypersensitivity, DH)의 교정 가능한 연관인자는 식후 즉시 칫솔질·미백치

- `implant-failure-mbl-risk-factors-overview` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: > **모범답안**: 이 오버뷰는 **경사 임플란트의 MBL 패널티는 시간 의존적**임을 보여준다. malak-2024(메타분석): 단기 NS → 3년 +0.08mm(유의) → 장기 +0.18mm(유의)로 시간이 지날수록 차이가 커진다. del-fabbro 연구진 자체 데이터도 2014년(≥3년, P=.30, NS) → 2022년(3–18년, P<.0001, 축방향 MBL 적음)으로 뒤집혔다. 따라서 "단기에 차이 없다"는 2017년 SR은 **추적기간이 짧은 연구 종합**이라는 한계를 갖는다. 경사 vs 축방향의 **실패 위험은 동일(RR=1.02)**이지만 장기 MBL 관리를 위해서는 이 시간 의존성을 고려해야 한다.
  - ▸ 출발(`implant-failure-mbl-risk-factors-overview`) 세줄: 후기(정착 후) 임플란트 실패·변연골소실(MBL) 관련 논문 **24편** 종합 — 로딩 전 조기실패는 [[overviews/early-implant-failure-risk-prevention-overview]]와 상호보완. 우산리뷰 10편을 축으로 삼되, **우산리뷰는 등급만 매기고 효과크기를 안 주므로** 그 아래 1차 SR+MA·코호트 층을 함께 싣고, 여기에 위험인자 차이값을 읽을 **기준선**(kumar-2021, 1년 pooled MBL 0.56 mm)을 더한다. 가장 광범위한 우산리뷰

- `topical-anesthetic-injection-pain-overview` [overviews] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: > - 명제5 (2026 갱신): 치주기구조작 맹검 RCT(Cabral 2026, n=76)는 명제2를 **부분적으로 뒤집는다** — 감온성 겔(Oraqix)과 컴퓨터제어 주사 간 **통증강도는 동등**(NRS-11 중앙값 0 vs 1, P>0.05)이나 **보충마취 필요율은 100% vs 24%(P<0.001)**. 즉 Wambier의 결론 중 재현되는 축은 통증강도가 아니라 **rescue·신뢰도**다. [확인]
  - ▸ 출발(`topical-anesthetic-injection-pain-overview`) 세줄: 6편 종합: 표면마취제는 위약 대비 needle·주사 통증을 줄이나(농도 의존, 5%→20%; Khongkhunthian 2018) 그 위약 대비 우위의 확실성은 GRADE low이고 표준 농도 위로의 증량은 trivial(20% vs 10% benzocaine RR 0.93, moderate; Miroshnychenko 2023 SR+MA), 제제 간 비교는 비일관적 — 소규모 RCT(Subramanian 2023)는 benzocaine 우위, 더 엄격한 triple-blind RCT(Karko

- `wu-2018-submerged-nonsubmerged-internal-hexagonal` [implants] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: - **Supersession check: no.** Nothing held in this wiki is overturned by this cohort; on this axis it is the *weaker* evidence. No `superseded_by` is set.
  - ▸ 출발(`wu-2018-submerged-nonsubmerged-internal-hexagonal`) 세줄: 5년 후향적 코호트(중산대학교 광화구강医学院·부속구강병원·샤먼시강구병원, 중국) — 즉시 식립한 골수준(Bone-Level) 내부 육각형 연결(Internal Hexagonal Connection) 임플란트 XiVE S plus 114개를 환자 72명에서 5년간 추적, 침습식(Submerged) 대 비침습식(Nonsubmerged) 치유를 비교하고 유도골재생술(Guided Bone Regeneration, GBR) 적용·식립 부위(Implant Site)·길이(Implant Length)·지름(I

- `wu-2018-submerged-nonsubmerged-internal-hexagonal` [implants] (SOFT→mortazavi-2021-bone-loss-tissue-bone-level-implants, 'disagree' · 불일치)
  - **근거 문장**: This is the primary-study anchor for a figure the wiki currently holds only second-hand: [[wiki/implants/mbl/mortazavi-2021-bone-loss-tissue-bone-level-implants]] tabulates "Wu 2018 | BL, 114 implants | 1.2mm (yr 1) + 0.78mm (yr 1–5) | 5 yr" as one of its 38 trials, yet no page in this wiki owns those numbers or reports the MBL-by-protocol breakdown the paper's title promises. More importantly, it
  - ▸ 출발(`wu-2018-submerged-nonsubmerged-internal-hexagonal`) 세줄: 5년 후향적 코호트(중산대학교 광화구강医学院·부속구강병원·샤먼시강구병원, 중국) — 즉시 식립한 골수준(Bone-Level) 내부 육각형 연결(Internal Hexagonal Connection) 임플란트 XiVE S plus 114개를 환자 72명에서 5년간 추적, 침습식(Submerged) 대 비침습식(Nonsubmerged) 치유를 비교하고 유도골재생술(Guided Bone Regeneration, GBR) 적용·식립 부위(Implant Site)·길이(Implant Length)·지름(I
  - ▸ 대상(`mortazavi-2021-bone-loss-tissue-bone-level-implants`) 세줄: 체계적 고찰 (SR, 38개 임상시험) — 골수준 (Bone-Level, BL) vs 조직수준 (Tissue-Level, TL) 임플란트의 변연골소실 (Marginal Bone Loss, MBL) 비교. 높은 이질성으로 BL-TL 직접 판정 불가; 플랫폼 스위칭 (Platform Switching)이 MBL을 0.7–2.5 mm → 0.12–0.29 mm로 감소; 모스 테이퍼 연결이 세균 침투 최소; SLActive 표면이 초기 골소실 최소; 전체 MBL의 대부분이 1년 내 발생. 플랫폼 스위칭·

- `wu-2018-submerged-nonsubmerged-internal-hexagonal` [implants] (AMBIG→al-amri-2016-crestal-bone-loss-submerged, 'disagree' · 불일치)
  - **근거 문장**: This is the primary-study anchor for a figure the wiki currently holds only second-hand: [[wiki/implants/mbl/mortazavi-2021-bone-loss-tissue-bone-level-implants]] tabulates "Wu 2018 | BL, 114 implants | 1.2mm (yr 1) + 0.78mm (yr 1–5) | 5 yr" as one of its 38 trials, yet no page in this wiki owns those numbers or reports the MBL-by-protocol breakdown the paper's title promises. More importantly, it
  - ▸ 출발(`wu-2018-submerged-nonsubmerged-internal-hexagonal`) 세줄: 5년 후향적 코호트(중산대학교 광화구강医学院·부속구강병원·샤먼시강구병원, 중국) — 즉시 식립한 골수준(Bone-Level) 내부 육각형 연결(Internal Hexagonal Connection) 임플란트 XiVE S plus 114개를 환자 72명에서 5년간 추적, 침습식(Submerged) 대 비침습식(Nonsubmerged) 치유를 비교하고 유도골재생술(Guided Bone Regeneration, GBR) 적용·식립 부위(Implant Site)·길이(Implant Length)·지름(I

- `esposito-2009-1-vs-2-stage-implant-placement-cochrane` [implants] (HIGH-far→verma-2024-comparison-bone-loss-submerged-nonsubmerged, 'Contradict' · 반박·충돌)
  - **근거 문장**: - [[implants/mbl/verma-2024-comparison-bone-loss-submerged-nonsubmerged]] — 2024 RCT (30 implants): submerged healing had significantly less MBL (0.18 mm) vs non-submerged anatomical healing abutment (0.34 mm) at 3 months. **Contradicts the "no difference" trend** of earlier SRs.
  - ▸ 출발(`esposito-2009-1-vs-2-stage-implant-placement-cochrane`) 세줄: 코크란 체계적 문헌고찰(2009년 1월까지 검색): 1단계(비매몰형/transmucosal) vs 2단계(매몰형/submerged) 임플란트 식립 비교. 적격 RCT 1편(Barber 1996, n=40)만 포함 — 2007년 원본은 0편이었으나 2009년 업데이트에서 포함. 1년 추시에서 임플란트 실패율 유의차 없음. 2018년 제5호로 **철회(withdrawn)** 됨: 내용이 구식이 되었고 현재 코크란 방법론/보고 표준 미충족, 저자 업데이트 불가. 2009년 출판 시점 결론만 유효.

- `yang-2024-implant-diameter-tapered-stress-insertion` [implants] (HIGH-no-target, '상충' · 상충)
  - **근거 문장**: 테이퍼 임플란트가 높은 IT를 내는 임상 관찰에 기계적 설명 제공 — 방사형 간섭이 응력장을 확대한다는 기전으로, 임상 문헌의 IT-1차 안정성-골 응력 상충관계와 거시형태를 연결.
  - ▸ 출발(`yang-2024-implant-diameter-tapered-stress-insertion`) 세줄: In vitro 삽입 실험 + 3D 명시적 FEA(Nobel Biocare 병렬벽 2종·테이퍼 2종, Ø3.5·4.3mm, PU 폼): 정규화 삽입 토크는 테이퍼 설계가 지배(β₂=0.93), 원시 삽입 토크는 직경이 더 크게 기여(β₁=0.78). 테이퍼가 유효 접촉압도 지배(β₂=0.97); 테이퍼 임플란트는 병렬벽 대비 나사산에서 더 멀리 압축 응력을 분산; FEA는 2D-DIC로 검증, 전 회귀모델 R²≥0.77. 테이퍼 임플란트가 높은 IT를 내는 임상 관찰에 기계적 설명 제공 — 방사형

- `gehrke-2026-influence-reduced-cortical-bone-compression` [implants] (HIGH-no-target, '뒤집' · 뒤집음)
  - **근거 문장**: 임상적으로는 이 모델에서 IT가 낮은 디자인이 오히려 더 잘 치유됐으나, 3 mm 비임상 규격·21일 토끼 모델이며 저자가 압축 감소만으로 개선 효과를 단일 인과 귀속하지 못하고 치유챔버 고유의 혈전 안정성·핍토탁시스·접촉유도 효과와 구분하지 못하므로 토크-안정성 관계를 뒤집기보다 정밀화하는 결과임.
  - ▸ 출발(`gehrke-2026-influence-reduced-cortical-bone-compression`) 세줄: 체외+체내 결합 전임상 연구: 상용 순수 티타늄(grade IV) 프로토타입 임플란트 40개(직경 3 × 길이 6 mm)를 Control(일반 원통형 거시형태) vs Test(치유챔버 보유 거시형태)로 배분, 폴리우레탄 합성골 블록에서 삽입토크 (Insertion Torque, IT) 측정(그룹당 n = 10) 후 토끼 경골에서 21일 관찰(5마리, 1개체 내 짝설계, 그룹당 n = 10). Test군이 IT를 유의하게 낮췄으나(5.70 ± 0.85 vs 8.01 ± 0.82 Ncm, p < 0.

- `s41598-021-90142-5` [implants] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: This PRISMA-compliant systematic review compiled all quantitative in vivo evidence (25 studies: 1 human post-mortem, 24 animal) relating micromotion at the bone-implant interface to osseointegration outcomes. The search covered PubMed, Scopus, and Web of Science through November 2020. While osseointegrated implants exhibited significantly lower mean micromotion (112±176 µm) than non-osseointegrate
  - ▸ 출발(`s41598-021-90142-5`) 세줄: 25편의 생체 내 연구(인간 1, 동물 24)를 체계적으로 검토하여 마이크로모션 크기와 골유착 결과의 관계를 분석함 (PROSPERO CRD42020196686). 골유착된 임플란트의 평균 마이크로모션은 112±176 µm, 비골유착은 349±231 µm로 유의한 차이(p<0.001)이나, 범위가 15–750 µm vs 30–750 µm로 광범위하게 겹쳐 보편적 임계값은 없음. 임상적 함의: 150 µm '금기준'은 오해이며, HA 코팅·나사설계·공극형상(임플란트 요인)과 부하빈도·휴지기간·관찰기

- `s41598-021-90142-5` [implants] (SOFT→brizuela-velasco-2015-insertion-torque-isq-micromobility, 'challenges the' · 도전)
  - **근거 문장**: This systematic review directly challenges the widely cited 150 µm "gold standard" micromotion limit by compiling all quantitative in vivo evidence. It reinforces [[implants/isq/brizuela-velasco-2015-insertion-torque-isq-micromobility]] and [[implants/isq/javed-2013-primary-stability-osseointegration-factors-influence]] by showing micromotion thresholds are context-dependent, not universal.
  - ▸ 출발(`s41598-021-90142-5`) 세줄: 25편의 생체 내 연구(인간 1, 동물 24)를 체계적으로 검토하여 마이크로모션 크기와 골유착 결과의 관계를 분석함 (PROSPERO CRD42020196686). 골유착된 임플란트의 평균 마이크로모션은 112±176 µm, 비골유착은 349±231 µm로 유의한 차이(p<0.001)이나, 범위가 15–750 µm vs 30–750 µm로 광범위하게 겹쳐 보편적 임계값은 없음. 임상적 함의: 150 µm '금기준'은 오해이며, HA 코팅·나사설계·공극형상(임플란트 요인)과 부하빈도·휴지기간·관찰기
  - ▸ 대상(`brizuela-velasco-2015-insertion-torque-isq-micromobility`) 세줄: 체외 연구(n=19, Klockner Essential Cone 임플란트, 소갈비뼈): 같은 시편에서 삽입 토크(IT)·Osstell ISQ·100 N 부하 하 미세운동을 Questar 현미경(2 µm 분해능)으로 동시 측정. 수직 ISQ vs 미세운동: 역 선형(r=0.91, R²≈0.83, p<0.0001), 수평 r=0.86; IT vs 미세운동: 역 지수 곡선(R²=0.78), 30–34 N·cm 임계값 미만 급증; IT vs ISQ: 직접 유의 상관(R²=0.73 수직, 0.62 수평).

- `s41598-021-90142-5` [implants] (AMBIG→javed-2013-primary-stability-osseointegration-factors-influence, 'challenges the' · 도전)
  - **근거 문장**: This systematic review directly challenges the widely cited 150 µm "gold standard" micromotion limit by compiling all quantitative in vivo evidence. It reinforces [[implants/isq/brizuela-velasco-2015-insertion-torque-isq-micromobility]] and [[implants/isq/javed-2013-primary-stability-osseointegration-factors-influence]] by showing micromotion thresholds are context-dependent, not universal.
  - ▸ 출발(`s41598-021-90142-5`) 세줄: 25편의 생체 내 연구(인간 1, 동물 24)를 체계적으로 검토하여 마이크로모션 크기와 골유착 결과의 관계를 분석함 (PROSPERO CRD42020196686). 골유착된 임플란트의 평균 마이크로모션은 112±176 µm, 비골유착은 349±231 µm로 유의한 차이(p<0.001)이나, 범위가 15–750 µm vs 30–750 µm로 광범위하게 겹쳐 보편적 임계값은 없음. 임상적 함의: 150 µm '금기준'은 오해이며, HA 코팅·나사설계·공극형상(임플란트 요인)과 부하빈도·휴지기간·관찰기

- `walter-2022-two-types-two-piece-dental-implants` [implants] (SOFT→juan-montesinos-2022-platform-switching-conventional-sr-ma, 'whereas' · 반면(대조))
  - **근거 문장**: - [[implants/mbl/juan-montesinos-2022-platform-switching-conventional-sr-ma]] — SR+MA pooling platform switching against **conventional/matching** platform (MD 0.255 mm less bone loss, p<0.05; PD difference NS). Complementary rather than competing: that meta-analysis pools PS vs non-PS, whereas **both arms here are PS**, so its effect size is not tested or challenged by this paper.
  - ▸ 출발(`walter-2022-two-types-two-piece-dental-implants`) 세줄: 단일센터 무작위대조임상시험(Randomized Controlled Clinical Trial, RCT) 8년 추적(환자 64명, 임플란트 98개; 취리히대학교 스위스) — 고정성 보철(Fixed Restoration)을 지지하는 비매칭(non-matching) 임플란트-abutment 접합부를 가진 두 2피스(two-piece) 시스템 비교: S1 OsseoSpeed TX(Dentsply Sirona) vs S2 Straumann Bone Level SLActive(Straumann AG); 평균
  - ▸ 대상(`juan-montesinos-2022-platform-switching-conventional-sr-ma`) 세줄: SR+MA (9편, 플랫폼 스위칭(PS) 475 vs 일반 462 임플란트, PRISMA, 다중 데이터베이스, 랜덤효과 메타분석): PS vs 일반 플랫폼의 임플란트 주위 결과 비교. PS에서 임플란트 주위 변연골 소실 유의하게 적음 (MD 0.255 mm, p<0.05); 탐침 깊이는 PS에서 0.082 mm 더 증가했으나 비유의 (p>0.05); 1개 연구 제거 민감도 분석에서 탐침 깊이 차이는 유의(MD 0.190 mm). PS의 변연골 보존 이점 확인; 탐침 깊이 결과는 추가 연구 필요; 

- `kniha-2023-thermal-osteonecrosis-implant-removal-rat` [implants/osteotomy-thermal] (HIGH-no-target, 'contrary to' · 상반된 결과)
  - **근거 문장**: - **Ca/P ratio**: increased, contrary to osteoporosis pattern (where Ca/P drops) — reflects thermal denaturization pattern
  - ▸ 출발(`kniha-2023-thermal-osteonecrosis-implant-removal-rat`) 세줄: In vivo 쥐 경골 연구 (48마리, 96개 미니나사, 2–4°C·48–50°C 각 1분) — EDX 무기질 조성, TEM 골세포 형태, ISQ (임플란트 안정성 지수, Implant Stability Quotient), 방사선 골높이를 수술 직후·7일에 측정해 열폭발적제거 후보 임계값 탐색. 50°C/1분에서 비가역적 골세포 괴사 (TEM: 공 소강), EDX 칼슘·인산염·나트륨·황 유의 증가(p < 0.01); 냉각 중에서는 2°C가 가장 심한 손상; ISQ 감소·방사선 골소실 증가 경향이

- `einafshar-2024-importance-precision-cortical-bone-drilling` [implants/osteotomy-thermal] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Resolved contradictory literature on spindle speed: higher speed consistently raises MT while reducing MTF in this validated model framework.
  - ▸ 출발(`einafshar-2024-importance-precision-cortical-bone-drilling`) 세줄: 소 피질골 시편 + DEFORM-3D V6.02 3D 유한요소해석 (Finite Element Analysis, FEA) 통합 연구: 드릴 초기온도 (Initial Temperature, IT)·직경·끝각 (Point Angle)·스핀들 속도 (225–2700 rpm)·이송속도 (0.5–3 mm/s) 4개 변수가 최대 온도 (Maximum Temperature, MT)·최대 추력 (Maximum Thrust Force, MTF)에 미치는 영향 예측. IT 25 → 5°C 강하 시 MT −26.14

- `al-amri-2016-crestal-bone-loss-submerged` [implants/mbl] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: **Supersession check: no.** No page held in this wiki overturns this review's clinical bottom line; the later pooled result reaches the same practical reading. No `superseded_by` is set.
  - ▸ 출발(`al-amri-2016-crestal-bone-loss-submerged`) 세줄: 메타분석 없는 체계적 문헌고찰 (Systematic Review, SR; 총 13편 = 인체 6편 + 동물 7편, 모두 대학병원 시행; 1986년–2015년 10월 검색; 사우디아라비아 킹사우드대학교) — 침습식 (Submerged) vs 비침습식 (Nonsubmerged) 치과 임플란트 주변 치조정골소실 (Crestal Bone Loss, CBL) 평가, 중점질문을 "치조정골 위치 (Crestal) 및 악골내 (Subcrestal) 식립이 치조정골 수준에 영향을 미치는가?"로 설정. 침습식과 비

- `ceddia-2025-finite-element-analysis-of-implant` [implants/isq] (HIGH-no-target, 'counter to' · 반대)
  - **근거 문장**: - Demonstrates that ISQ increases slightly with inclination under horizontal load — counter to intuitive concern about instability
  - ▸ 출발(`ceddia-2025-finite-element-analysis-of-implant`) 세줄: Cyroth 임플란트(4 mm×15 mm)를 D2·D3 폴리우레탄 블록에 0°·15°·20° 경사 식립 후, 유한요소분석(FEA) 미세운동→ISQ 방정식 결과를 Osstell RFA 실측치와 비교한 in vitro 연구. FEA ISQ 오차 D3 1.27%, D2 2.86%; 경사 증가 시 ISQ 소폭 상승(D2 60.96→61.10); 피질골 응력 55.4→68.4 MPa(20°), 피크 임플란트 응력 220.2 MPa — 소성변형 한계(130 MPa) 미만. FEA로 다양한 경사 조건 ISQ 

- `naughton-2023-safemount-osstell-transducer-torque-isq` [implants/isq] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - Demonstrated hand tightening yields significantly lower ISQ than 6 Ncm calibrated torque (p<.001), contradicting Kästel 2019
  - ▸ 출발(`naughton-2023-safemount-osstell-transducer-torque-isq`) 세줄: 체외 폴리우레탄 뼈 블록 연구 (임플란트 7종, 56개, D1–D4 골질): 스마트팩 조임 방법 4종 비교 — 수동, 플라스틱 마운트, SafeMount, 정확한 토크 렌치 6 Ncm. 수동 조임이 정확한 토크 렌치 대비 유의하게 낮은 임플란트 안정성 지수 (Implant Stability Quotient, ISQ) 산출 (계수 −2.05, p<.001); SafeMount와 표준 플라스틱 마운트는 대조군과 유의차 없음. 골밀도가 ISQ 변이의 36%를 차지해 가장 큰 영향 인자였고, 술자는 6%

- `troiano-2018-early-late-failure-submerged` [implants/survival] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: - **Moustafa Ali et al. 2018** (`moustafa-ali-2018-submerged-vs-nonsubmerged-implant`, *Int J Prosthodont* 2018;31(1):15-22, [10.11607/ijp.5315](https://doi.org/10.11607/ijp.5315)) — **typed edge: `contradicts`** (added in the finalize pass, once both batch siblings had landed). The pair: **bone level converges almost exactly** — Moustafa Ali pools 6 RCTs for MD **0.12 mm** more MBL with submerged
  - ▸ 출발(`troiano-2018-early-late-failure-submerged`) 세줄: 체계적 고찰 + 메타분석 + 시험순차분석(Trial Sequential Analysis, TSA) — PubMed·Scopus·Embase·Web of Science에서 즉시 로딩을 제외하고 매몰형(Submerged) 대 비매몰형(Non-submerged) 치유를 직접 비교한 전향적 무작위·비무작위 대조군 연구 11편. 비매몰형 치유에서 조기 임플란트 실패(Early Implant Failure, EIF)율이 2% 더 높았음. 만기(Late) 실패(식립 6개월 이후)는 두 방식에서 차이가 없었으나

- `guarnieri-2025-analysis-risk-factors-related-early` [implants/survival] (SOFT→wahlberg-2025-multicenter-early-implant-failures-part-2-patient, 'disagree' · 불일치)
  - **근거 문장**: - [[implants/survival/wahlberg-2025-multicenter-early-implant-failures-part-2-patient]] - smoking not significant for failure (OR 1.61, 0.88-2.94); the two retrospective cohorts disagree on significance.
  - ▸ 출발(`guarnieri-2025-analysis-risk-factors-related-early`) 세줄: 후향적 단일 개인의원 코호트 (이탈리아 트레비소; 환자 392명, 임플란트 930개, 2000-2020): 일반화추정방정식 (Generalized Estimating Equation, GEE)으로 조기 임플란트 실패 (지대주 연결 전 또는 연결 시점)의 환자·수술·임플란트 요인을 분석. 임플란트 단위 조기 실패율 5.8%; 유의 요인 7개 (남성 OR 1.54, 흡연, 방사선·항암치료 이력, 상악 구치부 OR 2.26 [1.32-3.86], 비매몰형 치유 (non-submerged), 임플란트 디
  - ▸ 대상(`wahlberg-2025-multicenter-early-implant-failures-part-2-patient`) 세줄: 후향적 다기관 코호트 (스웨덴 전문센터 3곳; 환자 1,875명, 임플란트 4,670개; 2007·2017 코호트): 환자 단위 다변량 로지스틱 회귀로 1년 이내 조기 실패·합병증 위험인자 분석. 조기 실패는 노출된 임플란트 나사선 (OR 3.47), 환자당 식립 임플란트 수 (임플란트 1개당 OR 1.27), 음식 알레르기 (OR 2.64)와 독립적으로 연관; 흡연은 조기 실패에서 비유의 (OR 1.61, 95% CI 0.88-2.94, p=0.12)였고 조기 합병증에서만 유의 (OR 2.30,

- `hamdi-2025-surface-pretreatments-sclerotic-dentin-bond-sr` [resin-bonding] (HIGH-no-target, 'conflicting result' · 상충 결과)
  - **근거 문장**: **Inconsistency**: studies reported conflicting results even within the same pretreatment category.
  - ▸ 출발(`hamdi-2025-surface-pretreatments-sclerotic-dentin-bond-sr`) 세줄: SR (8편, in vitro): NCCL 경화상아질 전처리 — EDTA·NaOCl 효과 없거나 열등; 37% 인산 연장(15–90초) ± 샌드블라스팅 잠재적 향상. 증거 수준 낮음, 대부분 높은 비뚤림 위험 — 가이드라인 수립 불충분. 현재 최선 권고: NCCL 경화상아질 → 37% 인산 연장 적용 ± 기계적 거칠기 부여 후 복합레진 접착. ---

- `miroshnychenko-2023-analgesics-acute-dental-pain` [drug/analgesics] (SOFT→di-spirito-2022-endodontic-pain-management-overview, 'unlike' · 다름)
  - **근거 문장**: - [[drug/analgesics/di-spirito-2022-endodontic-pain-management-overview]] — endodontic pain pharmacologic management overview; complementary adult context where pulpitis pain IS covered, unlike this pediatric review's extraction-only evidence.
  - ▸ 출발(`miroshnychenko-2023-analgesics-acute-dental-pain`) 세줄: - 소아(≤ 12세) 발치 후 급성 치통의 경구 진통제에 관한 체계적 문헌고찰 및 메타분석 (Systematic Review and Meta-Analysis, SRMA): 무작위대조시험 (Randomized Controlled Trial, RCT) 6편(연구당 45–201명, 평균 연령 5.5–9.3세), 2022년 ADA(미국치과협회) 소아 급성 치통 임상지침의 근거. - 이부프로펜과 아세트아미노펜은 위약보다 낫지만 서로 간 차이는 사소했고, 이부프로펜(5 mg/kg)+아세트아미노펜(15 mg/
  - ▸ 대상(`di-spirito-2022-endodontic-pain-management-overview`) 세줄: 체계적 고찰 개요(Healthcare 2022)와 기술적 요인 서술 고찰 통합: 근관 술후통증(환자의 2.5–60%, 6–12시간 최고조) 약물·비약물 관리 포괄. NSAIDs(ibuprofen ± APAP) 1차 약물치료; 코르티코스테로이드(dexamethasone)는 NSAID 보조제로 추가 이득; 술전 예방투여가 술후 반응투여보다 우월. 기구의 근첨 외 이탈·세정액 농도/용량·단일 vs 다회 방문 등 기술적 요인도 통증에 영향; 진통 목적 항생제 사용은 근거 없음.

- `al-moraissi-2021-hierarchy-different-treatments-myogenous-temporomandibular` [tmj] (HIGH-far→zhang-2026-nonpharmacological-myogenic-tmd-nma, 'contradict' · 반박·충돌)
  - **근거 문장**: [[tmj/zhang-2026-nonpharmacological-myogenic-tmd-nma]] (41 RCTs, search to Oct 2025, nonpharmacological only) ranks photobiomodulation first for pain (SUCRA 88.9%), manual therapy second (79.9%), and finds occlusal splint and exercise not significant versus conventional care. This 2021 NMA differs in three ways: it includes injections, BTX-A, ozone and hypnosis; its search ended in 2018, before mu
  - ▸ 출발(`al-moraissi-2021-hierarchy-different-treatments-myogenous-temporomandibular`) 세줄: 체계적 문헌고찰 + 빈도론적 네트워크 메타분석 (Network Meta-Analysis, NMA) 52개 RCT, 성인 근육성 측두하악장애 (Myogenous Temporomandibular Disorders, M-TMD) — 상담치료, 교합장치, 도수치료, 레이저, 건침, 국소마취제 (Local Anesthesia, LA)·보툴리눔독소 A (Botulinum Toxin-A, BTX-A) 주사, 근이완제, 최면·이완, 오존, 위약/무치료 비교 (검색 2018년 8월까지). 대부분의 치료가 위약보다

- `honnef-2022-stabilization-splints-signs-symptoms-muscular-tmd` [tmj] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: A positive splint effect on muscular TMD could be neither confirmed nor refuted; splints are not shown to be superior to alternatives.
  - ▸ 출발(`honnef-2022-stabilization-splints-signs-symptoms-muscular-tmd`) 세줄: 근원성 측두하악장애 (Temporomandibular Disorders, TMD)에서 안정화 스플린트 (Stabilization Splint)를 다른 치료와 비교한 체계적 문헌고찰 (Systematic Review, SR); 6개 데이터베이스와 회색문헌 검색, 10편 포함 (초록에 메타분석 언급 없음). 스플린트군 (n = 160)은 압통역치·저작 시 통증·개구량·자발통·촉진통에서 다른 치료군 (n = 209)과 동등하다고 보고됨; 비뚤림위험 낮음 5편·일부 우려 5편; 모든 결과에서 근거 확실성

- `honnef-2022-stabilization-splints-signs-symptoms-muscular-tmd` [tmj] (HIGH-no-target, '반박' · 반박)
  - **근거 문장**: 스플린트의 긍정적 효과는 확인도 반박도 불가하며, 다른 치료 대비 우월성은 입증되지 않음.
  - ▸ 출발(`honnef-2022-stabilization-splints-signs-symptoms-muscular-tmd`) 세줄: 근원성 측두하악장애 (Temporomandibular Disorders, TMD)에서 안정화 스플린트 (Stabilization Splint)를 다른 치료와 비교한 체계적 문헌고찰 (Systematic Review, SR); 6개 데이터베이스와 회색문헌 검색, 10편 포함 (초록에 메타분석 언급 없음). 스플린트군 (n = 160)은 압통역치·저작 시 통증·개구량·자발통·촉진통에서 다른 치료군 (n = 209)과 동등하다고 보고됨; 비뚤림위험 낮음 5편·일부 우려 5편; 모든 결과에서 근거 확실성

- `honnef-2022-stabilization-splints-signs-symptoms-muscular-tmd` [tmj] (HIGH-no-target, 'refut' · 반증)
  - **근거 문장**: This systematic review (Cranio 2022; [DOI](https://doi.org/10.1080/08869634.2022.2047510); source: PubMed, PMID 35311479) asked whether stabilization splints improve signs and symptoms of muscular-origin TMD compared with other treatments. Ten articles were included after searching six databases and gray literature. Splints (n = 160) were reported to be as effective as other treatments (n = 209) a
  - ▸ 출발(`honnef-2022-stabilization-splints-signs-symptoms-muscular-tmd`) 세줄: 근원성 측두하악장애 (Temporomandibular Disorders, TMD)에서 안정화 스플린트 (Stabilization Splint)를 다른 치료와 비교한 체계적 문헌고찰 (Systematic Review, SR); 6개 데이터베이스와 회색문헌 검색, 10편 포함 (초록에 메타분석 언급 없음). 스플린트군 (n = 160)은 압통역치·저작 시 통증·개구량·자발통·촉진통에서 다른 치료군 (n = 209)과 동등하다고 보고됨; 비뚤림위험 낮음 5편·일부 우려 5편; 모든 결과에서 근거 확실성

- `boulatar-2026-effectiveness-occlusal-stabilization-splint-myogenous` [tmj] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: No supersession and no contradiction: the positive but low-certainty conclusion is consistent with the held conditional-adjunct view.
  - ▸ 출발(`boulatar-2026-effectiveness-occlusal-stabilization-splint-myogenous`) 세줄: 근육성 측두하악장애 (Myogenous Temporomandibular Disorders, TMD)에서 교합안정장치 (Stabilization Splint) 효과를 본 체계적 문헌고찰 (PRISMA; MEDLINE·Web of Science, 최종 검색 2022년 5월), RCT 10편·539명·평균 추적 6개월. 대부분의 시험이 통증(10편)·개구량(5편)·두통(2편)·삶의 질(4편)에서 기저치 대비 호전을 보고했으나, 초록에는 통합 효과추정치가 없고 근거 질은 낮음 (중등도-높은 비뚤림 위험,

- `ahmad-2021-low-level-laser-therapy-temporomandibular` [tmj] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: Trial verdicts were split: 18 studies showed LLLT efficacious for pain, 12 showed similar efficacy to placebo, controls, or other interventions, and 4 showed varied effects. Secondary outcomes responded variably. The authors conclude that LLLT appears efficient in diminishing TMD pain, is non-invasive and reversible with few adverse effects, yet also concede that no conclusive validation exists fo
  - ▸ 출발(`ahmad-2021-low-level-laser-therapy-temporomandibular`) 세줄: 측두하악장애 (Temporomandibular Disorders, TMD) 환자에서 저출력레이저치료 (Low-Level Laser Therapy, LLLT)를 평가한 무작위대조시험 (Randomized Controlled Trial, RCT) 37편(2000~2020년 6월, PubMed·Science Direct 2개 DB)의 메타분석 없는 체계적 문헌고찰 (Systematic Review, SR; J Med Life 2021). 18편은 LLLT가 TMD 통증에 효과적, 12편은 위약·대조군과

- `christidis-2024-psychological-treatments-temporomandibular-disorder-pain` [tmj] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: No supersession: no held page's bottom line is overturned. No contradiction identified.
  - ▸ 출발(`christidis-2024-psychological-treatments-temporomandibular-disorder-pain`) 세줄: 유병 통증성 측두하악장애 (Temporomandibular Disorders, TMD)에 대한 심리 치료를 다룬 체계적 문헌고찰·메타분석 (PROSPERO CRD42022320106): 서술적 종합 RCT 18편, 메타분석 RCT 6편. 서술적 종합에서는 심리 치료가 표준 치료와 통증 면에서 동등해 보였고, 메타분석에서는 심리+표준+수기 치료 병행이 상담+표준 치료보다 통증 감소가 유의하게 컸다 (매우 낮은 근거 확실성). 심리 치료는 대체가 아닌 유망한 추가 치료이며, 메타분석 신호는 RCT 6

- `abrahamsson-2020-treatment-of-temporomandibular-joint-luxation` [tmj] (HIGH-no-target, 'Refut' · 반증)
  - **근거 문장**: - **Refutes the prolotherapy-for-luxation claim on controlled evidence**: across three placebo-armed trials (Mustafa 2018, Cömert Kiliç 2016, Refai 2011) dextrose was not consistently superior to placebo for mouth opening, pain or luxation frequency, and no concentration outperformed another.
  - ▸ 출발(`abrahamsson-2020-treatment-of-temporomandibular-joint-luxation`) 세줄: 메타분석 없는 체계적 리뷰 (systematic review without meta-analysis) — 무작위대조시험 (randomized controlled trial, RCT)만 포함하고 PubMed·Cochrane Library·Web of Science를 inception부터 2018년 3월 26일까지 검색, 초록 113건 → 전문 9편 → 최종 **RCT 8편·환자 338명**(급성 수동복원 3편 185명 / 재발성 탈구 주사 5편 153명). **수술 기법을 평가한 RCT는 0편**이

- `dinsdale-2025-effectiveness-conservative-interventions-temporomandibular-disorder` [tmj] (HIGH-no-target, 'overturn' · 결론 뒤집음)
  - **근거 문장**: - No supersession: no held page's bottom line is overturned.
  - ▸ 출발(`dinsdale-2025-effectiveness-conservative-interventions-temporomandibular-disorder`) 세줄: 성인 측두하악장애 (Temporomandibular Disorder, TMD)에서 비약물 보존 치료가 운동공포 (Kinesiophobia)와 통증 파국화 (Pain Catastrophizing)에 미치는 효과를 본 체계적 문헌고찰 (메타분석 없음; 12편, 815명, 평균 42.2세, 여성 85%, 대부분 근막·통증형 TMD). 인지행동치료 (Cognitive Behavioural Therapy, CBT), 통증 신경과학 교육 (Pain Neuroscience Education, PNE)+운동, 
