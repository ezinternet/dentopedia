# 논쟁 레이더 백필 후보 — 2026-07-18

명시적 충돌 표현이 있으나 그 쌍에 `relations:` 타입 엣지가 (어떤 타입이든) 없는 후보. **이 목록은 신호일 뿐 — 두 페이지를 읽고 판단해 엣지를 단다.**

**카드 읽는 법**: 각 카드는 `출발페이지 —[충돌유형·한글뜻]→ 대상페이지` 형태다. 아래에 (1) **근거 문장**(위키 본문에서 충돌 표현이 나온 실제 문장), (2) **양쪽 페이지의 `## 세줄요약`**(한국어)을 붙여, 페이지를 열지 않고도 두 논문이 각각 무엇을 주장하는지·정말 충돌하는지 한글로 판단할 수 있게 했다. 충돌 유형 한글뜻은 표현 매칭 기반 근사치이며, **최종 판단은 사람/LLM 몫**이다. (reinforces가 맞는 경우도 있으니 키워드를 그대로 엣지로 옮기지 말 것 — 2026-07-17 전수 검토에서 contradicts 계열로 지목된 122건 중 실제 contradicts는 1건이었다.)

**대상은 키워드에 가장 가까운 링크로 특정한다.** 같은 줄의 나머지 링크는 충돌 표현의 대상이라는 근거가 없어 Tier 2(`AMBIG→`)로 강등된다 — 버리지 않으니 진짜 대상이 강등됐다면 Tier 2에서 찾을 수 있다.

- Tier 1 (대상 지목됨, actionable): **6**
- Tier 2 (대상 불명/soft, review): **1**
- (억제됨) 이미 typed 엣지가 있어 제외: **224** · 부정문 제외: **77** · 검토·불필요 대장: **397** · 동일 줄 비최근접으로 Tier 2 강등: **1**

## Tier 1 — 판단 후 엣지 달 후보 (page → 지목된 target)

### oral-medicine

- `nonaka-2023-saliva-diagnostics-salivaomics-exosomics-liquid-biopsy`  —[뒤집 · 뒤집음]→  **`tsuchiya-2023-covid-19-oral-sequelae-gustatory-saliva`**
  - **근거 문장**: 기존 위키에는 침(saliva)이 질병의 *결과물*(COVID 후유증)로만 나타난다 — [[oral-medicine/tsuchiya-2023-covid-19-oral-sequelae-gustatory-saliva]]. 이 JADA 리뷰는 침을 *진단 매체*로 뒤집는 관점(salivaomics·exosomics·liquid biopsy)을 도입해, 침샘 기능/구강건조 라인([[oral-medicine/poudel-2026-xerostomia-dental-treatment-outcomes-sr]])과 대비되는 "침의 진단적 활용" 축을 새로 연다. Wong 그룹(UCLA)의 salivaomics 프레임워크 원전으로, 향후 침 바이오마커 overview의 앵커.
  - ▸ 출발(`nonaka-2023-saliva-diagnostics-salivaomics-exosomics-liquid-biopsy`) 세줄: 전문가 서술 리뷰(JADA 2023, Wong/UCLA 그룹) — 침 진단(saliva diagnostics)을 살리바오믹스(salivaomics)·침 엑소좀학(saliva exosomics)·침 액체생검(saliva liquid biopsy) 세 축으로 분류, 침·혈장 단백질체 20–30% 중첩으로 전신 바이오마커의 침샘 이송 가능성 지지. 전기화학 센서 EFIRM(Electric Field–Induced Release and Measurement)은 추출·증폭 없이 40–50 µL 침에서 폐암
  - ▸ 대상(`tsuchiya-2023-covid-19-oral-sequelae-gustatory-saliva`) 세줄: 내러티브 리뷰(약 90편 이상 연구, 코로나19 환자·완치자 총 6만5천여 명 종합) — 미각장애(ageusia/dysgeusia)와 침분비저하(xerostomia/hyposalivation) 등 구강 후유증의 지속 기간·유병률 종합. 미각장애는 완치 후 3주~12개월 추적에서 1~45%, 침분비저하는 2~40%에서 지속되고 서로 상관관계가 있으며; 지리적 구배(동아시아 3.8% vs 중동 20.6%)가 미각장애에서 뚜렷함. 타액선·미뢰의 ACE2/TRPV1 수용체 발현과 감염 유발 아연결핍이라는


### oral-microbiology

- `momeni-2024-intraspecies-interactions-streptococcus-mutans`  —[대비되는 · 대비]→  **`lueyar-2023-dynamic-interactions-between-candida-albicans`**
  - **근거 문장**: 기존 S. mutans 페이지들([[oral-microbiology/bowen-2011-streptococcus-mutans-glucosyltransferases]], [[oral-microbiology/klein-2012-mutans-protein-synthesis-mixed-species-biofilm]])은 단일 균주 또는 종간(interspecies) 상호작용에 집중했으나, 같은 종 내 여러 유전형(genotype) 간 상호작용이 우식원성에 미치는 영향은 공백이었다. 본 논문(Momeni 2024)은 임상 분리주 G09·G18의 co-culture가 biofilm 산도·구조·집락화를 상승시킴을 in vitro/in vivo로 보여, "다수 S. mutans 유전형 = ECC 위험인자"라는 역학 관찰의
  - ▸ 출발(`momeni-2024-intraspecies-interactions-streptococcus-mutans`) 세줄: 8년 종단 코호트에서 선정된 고위험 아동 1명의 환자 매칭 임상 S. mutans 두 유전형(G09·G18)을 대상으로 한 In vitro CLSM 바이오필름 + In vivo 초파리 집락화 연구 (+ 후향적 중첩 연관 분석, n=78). G09·G18 공동 배양 시 단독 배양 대비 9/10 아동 및 전체 집단에서 유의하게 낮은 바이오필름 pH(산도 증가), CLSM 세포 밀도·두께 약 2배 증가, in vivo 집락화 강화 — 각 균주는 서로 겹치지 않는 공간 영역 차지(G18: 평탄한 "law
  - ▸ 대상(`lueyar-2023-dynamic-interactions-between-candida-albicans`) 세줄: Zürich in-vitro 8종 상연골상 (supragingival) 바이오필름 모델 (3회·삼중, CFU + FISH/CLSM) — 개별 연쇄상구균 종이 *C. albicans*에 미치는 영향 분석. 연쇄상구균 종 다양성 증가 → *C. albicans* CFU 감소 (*S. gordonii* + *S. mutans* 최저, p<0.01); *S. mutans* + mitis군 단일종 → 균사형 (hypha) 유도, mitis 다종 공존 → 효모형 (yeast) 회귀. 구강 연쇄상구균 군집 복


### overviews

- `bone-regeneration-socket-biology-and-arp-critique`  —[반박 · 반박]→  **`araujo-2009-ridge-alterations-flap-vs-flapless`**
  - **근거 문장**: | [[bone-regeneration/ridge-preservation/araujo-2009-ridge-alterations-flap-vs-flapless]] | animal (dog, split-mouth) | **"Flapless = ridge 보존" myth 반박**. flap 유무가 ridge 흡수 크기를 의미있게 바꾸지 않음. Flapless 의 가치는 vascular preservation 가설 아닌 술자·환자 부담 감소 |
  - ▸ 출발(`bone-regeneration-socket-biology-and-arp-critique`) 세줄: 발치와 자연 치유 생물학 + ARP 한계·과잉치료 비판 5축 종합 — do-ARP 페이지의 대응쌍: 협측골 흡수는 다발골(bundle bone) 의존으로 생물학적 불가피(Araujo 2005), 협설폭 1년 ~50% 감소의 2/3이 첫 3개월 발생(Schropp 2003). ARP는 차원 보존이지 골 질 향상이 아님 — 6개월 신생골 16%·잔류 이종골 32%(Poli 2017); ARP 후 임플란트 실패 단일 유의 예측인자 = 순수골 결합(Pristine Bone Engagement, PBE) 
  - ▸ 대상(`araujo-2009-ridge-alterations-flap-vs-flapless`) 세줄: 개 5마리 이분구강 (Split-mouth) 디자인: 전층 판막 (Full-thickness Flap) 거상 발치 vs 판막없는 발치 (Flapless Extraction), 6개월 조직형태계측 비교 — "flapless 발치가 치조제를 보존한다"는 임상 가설 검증. 양 군 모두 치조제 흡수 발생, 흡수 크기에 유의한 군 간 차이 없음 — 다발골 (Bundle Bone) 소실은 발치 방법과 무관하게 발생. Flapless 발치는 치조제 보존의 충분 조건이 아님 — 적극적 치조제 보존술 (Alveo

- `treatment-planning-decision-variability-overview`  —[contradict · 반박·충돌]→  **`zhang-2025-intentional-replantation-periapical-periodontitis-prognosis-sr-ma`**
  - **근거 문장**: - [[endodontics/zhang-2025-intentional-replantation-periapical-periodontitis-prognosis-sr-ma]] — intentional replantation: success 0.78, 8-year survival 0.63, 31/39 high risk of bias; the number that contradicts the "88–98%" used to justify referral
  - ▸ 출발(`treatment-planning-decision-variability-overview`) 세줄: 6편 종합(+SDM 2편) — 위키의 182개 결정 사다리가 전부 전제하는 것을 되묻는다: 같은 치아를 보면 같은 계획이 나오는가? 아니다. 근관치료 후 근단주위염 치아에서 일반의 발치율 17.03% vs 근관전문의 5.3%(OR 4.37, p<0.001), 인용된 별도 데이터셋에서도 5.63% vs 14.69%로 **약 3배 격차가 독립 재현**됐다. 중등도 병소(OR 7.26)·간접수복물(OR 2.12)·부적절 근충(OR 1.81)이 일반의를 발치로 미는 동안 전문의는 병소 크기에 반응하지 않
  - ▸ 대상(`zhang-2025-intentional-replantation-periapical-periodontitis-prognosis-sr-ma`) 세줄: 체계적 문헌고찰(Systematic Review, SR)+메타분석(Meta-Analysis, MA)(PROSPERO CRD42023460388; PRISMA 2020) — 근단치주염(periapical periodontitis) 치아에 대한 의도적 재식(Intentional Replantation, IR: 발치 후 구강외 처치·재식립)의 전체 예후 및 예후인자를 다룬 연구 39편(보고서 49편, 환자 2,215명, 치아 2,305개; 2024년 6월까지 검색)을 QUIPS 도구로 편향위험 평가하며

- `tmd-management-evidence-ladder`  —[뒤집 · 뒤집음]→  **`tenorio-2026-ultrasonography-tmj-rheumatoid-arthritis-scoping-review`**
  - **근거 문장**: | [[tmj/tenorio-2026-ultrasonography-tmj-rheumatoid-arthritis-scoping-review]] | sr (5편/154명) | 성인 RA는 삼출에 강하고(단일연구 92.4%) 디스크·골에 약함(72%·53%) — **JIA와 최적 표적이 뒤집힘**; 술자 의존성이 최대 한계 |
  - ▸ 출발(`tmd-management-evidence-ladder`) 세줄: TMD 34편(SR+MA·가이드라인 27 + 편측저작·과두·이명 5 + TMJ OA 운동 전향 1 + MPS NMA 1)을 역학·비약물 보존·약물·만성통증 NMA·관절천자·이갈이·BTX·OA·QoL/VD·편측저작 10축으로 정리. 최고 근거 치료(Yao 2023 BMJ NMA, 233 RCT): CBT+운동·하악 가동화(RD 36%)·수기 트리거포인트(32%); 교합 중재 미지지(Cochrane 2024 Singh); 약물 낮은 근거; 관절천자 단독 우월성 미입증(Valenzuela-Fuenzal
  - ▸ 대상(`tenorio-2026-ultrasonography-tmj-rheumatoid-arthritis-scoping-review`) 세줄: 이 스코핑 리뷰(PRISMA-ScR 준수, OSF 사전등록)는 류마티스 관절염(Rheumatoid Arthritis, RA) 환자의 측두하악관절(Temporomandibular Joint, TMJ) 침범을 평가하는 초음파(Ultrasonography, US)의 근거를 지도화한다 — 88건 스크리닝 중 단 5편(RA 환자 총 154명, 대부분 여성, 중등도~고도 질병활성도)만 포함 기준을 충족했다. 포함된 연구들에서 US는 관절삼출(joint effusion), 활막비후(synovial thicke


### sinus-lift/lateral

- `sartori-2003-msfa-bio-oss-10year-case-report`  —[상충 · 상충]→  **`rogova-2025-histomorphometric-non-decalcified-bone-substitute-sr`**
  - **근거 문장**: - [[bone-regeneration/rogova-2025-histomorphometric-non-decalcified-bone-substitute-sr]] — histomorphometry 방법론 SR — 평가 방법 차이로 inter-study 결과 상충 가능.
  - ▸ 출발(`sartori-2003-msfa-bio-oss-10year-case-report`) 세줄: 단일 환자 증례보고: Bio-Oss 단독 상악동거상술 (Maxillary Sinus Floor Augmentation, MSFA) 후 8개월·2년·10년 시점 연속 트레핀 생검 (Trephine Biopsy) 조직형태계측 — 인체 장기 MSFA 리모델링 궤적을 기록한 매우 드문 연구. 골조직 (골수강 포함) 비율 29.8% → 69.7% → 86.7%로 단조 증가; Bio-Oss 입자 ~70% → ~30% → ~13%로 점진적 감소 — 10년에 걸친 완만하지만 진행적인 흡수 시사. Mordenfe
  - ▸ 대상(`rogova-2025-histomorphometric-non-decalcified-bone-substitute-sr`) 세줄: 방법론 체계적 문헌고찰(PCC 프레임워크, 118편, 2015–2024): 이식재를 사용한 골재생 비탈회 플라스틱 포매 조직형태계측 연구의 방법론 분포 지도 작성. 동물모델: rat > rabbit > sheep > dog > mini-pig; 주요 염색: toluidine blue; 가장 흔한 단일 평가지표: 신생골 형성률(NB%); 표준 부지표: 잔존 이식재(RG%)·입자 골유착률(OI%)·골임플란트 접촉률(BIC)·광화부착속도(Mineral Apposition Rate, MAR, calcei


## Tier 2 — 대상 식별 필요 / soft signal (review only)

- `nonaka-2023-saliva-diagnostics-salivaomics-exosomics-liquid-biopsy` [oral-medicine] (AMBIG→poudel-2026-xerostomia-dental-treatment-outcomes-sr, '뒤집' · 뒤집음)
  - **근거 문장**: 기존 위키에는 침(saliva)이 질병의 *결과물*(COVID 후유증)로만 나타난다 — [[oral-medicine/tsuchiya-2023-covid-19-oral-sequelae-gustatory-saliva]]. 이 JADA 리뷰는 침을 *진단 매체*로 뒤집는 관점(salivaomics·exosomics·liquid biopsy)을 도입해, 침샘 기능/구강건조 라인([[oral-medicine/poudel-2026-xerostomia-dental-treatment-outcomes-sr]])과 대비되는 "침의 진단적 활용" 축을 새로 연다. Wong 그룹(UCLA)의 salivaomics 프레임워크 원전으로, 향후 침 바이오마커 overview의 앵커.
  - ▸ 출발(`nonaka-2023-saliva-diagnostics-salivaomics-exosomics-liquid-biopsy`) 세줄: 전문가 서술 리뷰(JADA 2023, Wong/UCLA 그룹) — 침 진단(saliva diagnostics)을 살리바오믹스(salivaomics)·침 엑소좀학(saliva exosomics)·침 액체생검(saliva liquid biopsy) 세 축으로 분류, 침·혈장 단백질체 20–30% 중첩으로 전신 바이오마커의 침샘 이송 가능성 지지. 전기화학 센서 EFIRM(Electric Field–Induced Release and Measurement)은 추출·증폭 없이 40–50 µL 침에서 폐암
