# 논쟁 레이더 백필 후보 — 2026-07-21

명시적 충돌 표현이 있으나 그 쌍에 `relations:` 타입 엣지가 (어떤 타입이든) 없는 후보. **이 목록은 신호일 뿐 — 두 페이지를 읽고 판단해 엣지를 단다.**

**카드 읽는 법**: 각 카드는 `출발페이지 —[충돌유형·한글뜻]→ 대상페이지` 형태다. 아래에 (1) **근거 문장**(위키 본문에서 충돌 표현이 나온 실제 문장), (2) **양쪽 페이지의 `## 세줄요약`**(한국어)을 붙여, 페이지를 열지 않고도 두 논문이 각각 무엇을 주장하는지·정말 충돌하는지 한글로 판단할 수 있게 했다. 충돌 유형 한글뜻은 표현 매칭 기반 근사치이며, **최종 판단은 사람/LLM 몫**이다. (reinforces가 맞는 경우도 있으니 키워드를 그대로 엣지로 옮기지 말 것 — 2026-07-17 전수 검토에서 contradicts 계열로 지목된 122건 중 실제 contradicts는 1건이었다.)

**대상은 키워드에 가장 가까운 링크로 특정한다.** 같은 줄의 나머지 링크는 충돌 표현의 대상이라는 근거가 없어 Tier 2(`AMBIG→`)로 강등된다 — 버리지 않으니 진짜 대상이 강등됐다면 Tier 2에서 찾을 수 있다.

- Tier 1 (대상 지목됨, actionable): **0**
- Tier 2 (대상 불명/soft, review): **5**
- (억제됨) 이미 typed 엣지가 있어 제외: **225** · 부정문 제외: **78** · 검토·불필요 대장: **406** · 동일 줄 비최근접으로 Tier 2 강등: **0**

## Tier 1 — 판단 후 엣지 달 후보 (page → 지목된 target)

## Tier 2 — 대상 식별 필요 / soft signal (review only)

- `radiology-category-synthesis-overview` [overviews] (SOFT→hasan-2022-prevalence-nutrient-canals-mandibular, 'Unlike' · 다름)
  - **근거 문장**: Nutrient canals (NCs) are radiolucent neurovascular channels visible on mandibular anterior IOPARs. Unlike MC variants, they carry vessels to alveolar bone rather than the IAN. [[radiology/hasan-2022-prevalence-nutrient-canals-mandibular]] (cross-sectional, n=200, India) compared four groups:
  - ▸ 출발(`radiology-category-synthesis-overview`) 세줄: 방사선학 53편은 5개 주제군 — 선량 최적화, CBCT 진단 성능, 이미지 아티팩트, 해부학적 변이, 방사선 감별진단 — 으로 구성되며 각 주제군에 별도 overview가 있다; 이분하악관(Bifid Mandibular Canal, BMC) 유병률은 CT/CBCT 환자 20.7%(Aung 2023 SR+MA, 40편, n=17,714), 영양관(Nutrient Canal, NC)은 당뇨(84%)·고혈압(66%)·치주염(52%) 군에서 건강 대조군(20%) 대비 유의하게 증가(Hasan 2022)
  - ▸ 대상(`hasan-2022-prevalence-nutrient-canals-mandibular`) 세줄: 단면연구(cross-sectional, n=200/800명 스크리닝, 인도, 10개월) — 하악 전치부 치근단방사선사진(IOPAR)에서 영양관(Nutrient Canal, NC) 유병률을 건강대조군·당뇨병(Diabetes Mellitus, DM)·고혈압(Hypertension, HTN)·만성치주염(Chronic Periodontitis) 4개 군에서 비교. 질환군에서 NC 유병률이 대조군 대비 유의하게 높음(DM 84% vs 대조군 20%, p=0.000004; HTN 66%, p=0.000003

- `local-anesthesia-category-synthesis-overview` [overviews] (HIGH-far→subramanian-2023-comparative-two-topical-anesthetic-agents-pediatric, 'contradict' · 반박·충돌)
  - **근거 문장**: [[local-anesthesia/subramanian-2023-comparative-two-topical-anesthetic-agents-pediatric]] provides a contrasting result in a different comparison (lidocaine vs benzocaine in a different pediatric age group) — the two papers are tagged `contradicts` in the wiki; the most likely explanation is methodological heterogeneity rather than a true effect.
  - ▸ 출발(`local-anesthesia-category-synthesis-overview`) 세줄: 국소마취 37편은 ① 하악 마취 효율 ladder, ② 완충·변형 마취제, ③ IANB 실패 해부학, ④ CCLAD·무침주사, ⑤ 전처치·표면마취, ⑥ 안전·합병증 6군으로 정리; 표준 IANB는 증상성 비가역 치수염(SIP)에서 자주 실패 → 4% articaine 협측침윤(RR 1.06, Saatchi 2025 SR+MA), 이부프로펜 >400 mg 전처치(위약 ~20% → ~79%; Khademi 2023 umbrella), 보충주사(RR 2.02, Rujirawan 2025 Network 

- `suture-wound-closure-decision-ladder` [overviews] (HIGH-no-target, '상반된' · 상반)
  - **근거 문장**: > - 고장력 — 술식 성능 순위(하악 4군 RCT n=40): 골증대 **CALF > DFI ≈ MPRI > PRI**(PRI 최저, 임상 2.60mm vs CALF 4.12mm, P<.001, Bahaa 2022). DFI 단독비교(Ogata 2013 RCT n=23)도 PRI보다 전진량↑(9.64 vs 7.13mm)·통증/부종↓. 단, ex-vivo(Raabe 2025)에서는 절개기법(MPRI vs MDT)이 아니라 **골막봉합(PS) 유무**가 이식재변위를 좌우(P<.001) — 기법보다 봉합이 이식재 안정성의 진짜 변수라는 상반된 층위의 결론.
  - ▸ 출발(`suture-wound-closure-decision-ladder`) 세줄: 23편 종합(RCT 10, SR 1, 전향적 2, case-report 2, in-vitro 5, 후향적 1, animal 1, narrative-review 1) — 봉합·창상폐쇄 결정은 단일 상류 변수인 창상 장력(wound tension)에 의해 정반대 최적화 목표를 가진 두 맥락으로 분기한다. 저장력 발치와: 봉합 유무는 결과에 무관 — 무봉합(sutureless)은 안전하며 초기 이환도 동등 이상(Takadoum 2022 완전 동등, Kumar/Sen trismus·부종 감소); 흡연자는

- `suture-wound-closure-decision-ladder` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: **회색지대**: ogata(임상: 기법선택이 전진량·이환도에 유의 영향)와 raabe(ex-vivo: 기법선택이 이식재변위·전진량에 무영향)는 서로 다른 기법쌍·다른 outcome을 측정하므로 frontmatter상 공식 `contradicts` 관계는 아니지만 방향이 엇갈린다 — 폐쇄 morbidity·전진량엔 기법이 영향을 주지만(임상), 이식재 자체의 안정성은 골막봉합 여부가 결정한다(ex-vivo). [미검증 — 두 결론을 통합한 단일 연구는 없음]
  - ▸ 출발(`suture-wound-closure-decision-ladder`) 세줄: 23편 종합(RCT 10, SR 1, 전향적 2, case-report 2, in-vitro 5, 후향적 1, animal 1, narrative-review 1) — 봉합·창상폐쇄 결정은 단일 상류 변수인 창상 장력(wound tension)에 의해 정반대 최적화 목표를 가진 두 맥락으로 분기한다. 저장력 발치와: 봉합 유무는 결과에 무관 — 무봉합(sutureless)은 안전하며 초기 이환도 동등 이상(Takadoum 2022 완전 동등, Kumar/Sen trismus·부종 감소); 흡연자는

- `hygienist-periodontal-instrumentation-scaling-overview` [overviews] (HIGH-far→vadvadgi-2024-comparing-effectiveness-traditional-periodontal, 'contradict' · 반박·충돌)
  - **근거 문장**: | [[periodontics/vadvadgi-2024-comparing-effectiveness-traditional-periodontal]] | RCT (n=120) — **data-quality caveat** | 1 · effectiveness | Surgery numerically > hygienist SRP on PPD/CAL; SRP better tolerated. **Narrative text contradicts tables ("illustrative only") — cite direction, not point estimates** |
  - ▸ 출발(`hygienist-periodontal-instrumentation-scaling-overview`) 세줄: 치위생사 스케일링·치주기구조작 14편을 네 전선 — 효과성·적응증, 술자 인체공학, 에어로졸·감염관리, 체어사이드 안전 2건 — 으로 종합. 핵심 적응증 경계: 저위험 건강 성인의 루틴 스케일링·폴리싱은 치주 이득이 거의 없으나(Lamont, Cochrane 고신뢰, n=1,711), 진단된 치주염의 치료적 스케일링·치근활택술(SRP)은 크고 실제 진료에서 재현되는 이득(Tomasi, DH 95명, 치주낭 폐쇄 ~69–72%, 다회 내원 대비 비열등·시술시간 ~17%↓). 술자측: 압전형 초음파 
