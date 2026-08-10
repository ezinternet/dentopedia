# 논쟁 레이더 백필 후보 — 2026-07-19

명시적 충돌 표현이 있으나 그 쌍에 `relations:` 타입 엣지가 (어떤 타입이든) 없는 후보. **이 목록은 신호일 뿐 — 두 페이지를 읽고 판단해 엣지를 단다.**

**카드 읽는 법**: 각 카드는 `출발페이지 —[충돌유형·한글뜻]→ 대상페이지` 형태다. 아래에 (1) **근거 문장**(위키 본문에서 충돌 표현이 나온 실제 문장), (2) **양쪽 페이지의 `## 세줄요약`**(한국어)을 붙여, 페이지를 열지 않고도 두 논문이 각각 무엇을 주장하는지·정말 충돌하는지 한글로 판단할 수 있게 했다. 충돌 유형 한글뜻은 표현 매칭 기반 근사치이며, **최종 판단은 사람/LLM 몫**이다. (reinforces가 맞는 경우도 있으니 키워드를 그대로 엣지로 옮기지 말 것 — 2026-07-17 전수 검토에서 contradicts 계열로 지목된 122건 중 실제 contradicts는 1건이었다.)

**대상은 키워드에 가장 가까운 링크로 특정한다.** 같은 줄의 나머지 링크는 충돌 표현의 대상이라는 근거가 없어 Tier 2(`AMBIG→`)로 강등된다 — 버리지 않으니 진짜 대상이 강등됐다면 Tier 2에서 찾을 수 있다.

- Tier 1 (대상 지목됨, actionable): **1**
- Tier 2 (대상 불명/soft, review): **2**
- (억제됨) 이미 typed 엣지가 있어 제외: **225** · 부정문 제외: **77** · 검토·불필요 대장: **405** · 동일 줄 비최근접으로 Tier 2 강등: **0**

## Tier 1 — 판단 후 엣지 달 후보 (page → 지목된 target)

### drug/anticoagulants

- `tang-2025-chitosan-antibacterial-hemostatic-sponge-extraction`  —[counterpoint · 반대 논점]→  **`dinkova-2025-local-hemostasis-oral-surgery-review`**
  - **근거 문장**: [[drug/anticoagulants/guardieiro-2023-chitosan-cellulose-hemostasis-dapt-rct]] establishes chitosan dressings as a local hemostatic option in antithrombotic patients at the human-RCT level; this paper adds the preclinical/materials layer beneath that claim — an antibacterial-modified chitosan variant (quaternized carboxymethyl chitosan/polydopamine, QCD) tested against a commercial gelatin sponge 
  - ▸ 출발(`tang-2025-chitosan-antibacterial-hemostatic-sponge-extraction`) 세줄: 항응고 처치된 흰쥐(rat) 발치 모델과 in vitro 실험으로 평가한 4급 암모늄화 카르복시메틸 키토산/폴리도파민 복합 지혈 스폰지(Quaternized Carboxymethyl Chitosan/Polydopamine, QCD) 연구 — 제목과 달리 항응고 환자를 대상으로 한 임상연구가 아니다. 쥐 모델에서 QCD는 출혈량 0.011 ± 0.001 g, 지혈시간 59.667 ± 4.163초로 상용 젤라틴 스폰지(0.019 ± 0.001 g, 87.000 ± 4.082초)보다 우수했고, 4급 암
  - ▸ 대상(`dinkova-2025-local-hemostasis-oral-surgery-review`) 세줄: 서술적 고찰(51편, 1990–2023): 현대 구강외과의 생체재료·술식 기반 국소지혈제 전반 검토; 표준 환자 및 항응고·항혈소판 고위험 환자 포함. 산화셀룰로오스·젤라틴 스폰지 표준 증례 85% 이상 지혈, 트라넥삼산(TXA) 구강세정 50–60% 출혈 감소, 피브린 실란트 고위험 환자 70–90% 효과, 혈전색전 위험 증가 없음. 표준화 프로토콜 부재, 나노소재·중증 전신질환 환자 근거 부족 — 위험도·가용성 기반 선택 필요.


## Tier 2 — 대상 식별 필요 / soft signal (review only)

- `suture-wound-closure-decision-ladder` [overviews] (HIGH-no-target, '상반된' · 상반)
  - **근거 문장**: > - 고장력 — 술식 성능 순위(하악 4군 RCT n=40): 골증대 **CALF > DFI ≈ MPRI > PRI**(PRI 최저, 임상 2.60mm vs CALF 4.12mm, P<.001, Bahaa 2022). DFI 단독비교(Ogata 2013 RCT n=23)도 PRI보다 전진량↑(9.64 vs 7.13mm)·통증/부종↓. 단, ex-vivo(Raabe 2025)에서는 절개기법(MPRI vs MDT)이 아니라 **골막봉합(PS) 유무**가 이식재변위를 좌우(P<.001) — 기법보다 봉합이 이식재 안정성의 진짜 변수라는 상반된 층위의 결론.
  - ▸ 출발(`suture-wound-closure-decision-ladder`) 세줄: 23편 종합(RCT 10, SR 1, 전향적 2, case-report 2, in-vitro 5, 후향적 1, animal 1, narrative-review 1) — 봉합·창상폐쇄 결정은 단일 상류 변수인 창상 장력(wound tension)에 의해 정반대 최적화 목표를 가진 두 맥락으로 분기한다. 저장력 발치와: 봉합 유무는 결과에 무관 — 무봉합(sutureless)은 안전하며 초기 이환도 동등 이상(Takadoum 2022 완전 동등, Kumar/Sen trismus·부종 감소); 흡연자는

- `suture-wound-closure-decision-ladder` [overviews] (HIGH-no-target, 'contradict' · 반박·충돌)
  - **근거 문장**: **회색지대**: ogata(임상: 기법선택이 전진량·이환도에 유의 영향)와 raabe(ex-vivo: 기법선택이 이식재변위·전진량에 무영향)는 서로 다른 기법쌍·다른 outcome을 측정하므로 frontmatter상 공식 `contradicts` 관계는 아니지만 방향이 엇갈린다 — 폐쇄 morbidity·전진량엔 기법이 영향을 주지만(임상), 이식재 자체의 안정성은 골막봉합 여부가 결정한다(ex-vivo). [미검증 — 두 결론을 통합한 단일 연구는 없음]
  - ▸ 출발(`suture-wound-closure-decision-ladder`) 세줄: 23편 종합(RCT 10, SR 1, 전향적 2, case-report 2, in-vitro 5, 후향적 1, animal 1, narrative-review 1) — 봉합·창상폐쇄 결정은 단일 상류 변수인 창상 장력(wound tension)에 의해 정반대 최적화 목표를 가진 두 맥락으로 분기한다. 저장력 발치와: 봉합 유무는 결과에 무관 — 무봉합(sutureless)은 안전하며 초기 이환도 동등 이상(Takadoum 2022 완전 동등, Kumar/Sen trismus·부종 감소); 흡연자는
