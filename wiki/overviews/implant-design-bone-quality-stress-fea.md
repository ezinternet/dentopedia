---
title: "Overview: Implant Macro-Design × Bone Quality → Peri-Implant Stress (FEA Synthesis)"
authors: synthesis (llm-wiki)
year: 2026
date: 2026-06-10
type: synthesis
category: [overviews]
tags: [FEA, finite-element-analysis, stress-distribution, bone-quality, bone-density, thread-design, taper, crestal-stress, macrogeometry, von-mises]
source_papers:
  - wiki/implants/premnath-2012-stress-distribution-bone-density-fea.md
  - wiki/implants/leblebicioglu-kurtulus-2022-fea-implant-design-bone-density-stress.md
  - wiki/implants/hussein-2019-thread-depth-implant-shape-stress-mandible-fea.md
  - wiki/implants/chang-2024-optimization-implant-design-bone-quality-fea.md
  - wiki/implants/ozturk-2026-stress-distribution-anterior-implant-fea.md
---

## 한국어 핵심요약

> [!summary] 한국어 핵심요약
> - 유한요소분석(Finite Element Analysis, FEA) 5편 종합 — 임플란트 거시설계(macro-design) × 골질(bone quality)이 임플란트 주위 응력에 미치는 영향. 임상시험이 풀 수 없는 "하중이 어디로 가는가"에 답.
> - 불변 사실 1: 응력은 모든 모델에서 임플란트 경부의 치조정 피질골(crestal cortical bone)에 집중 — 설계·골밀도와 무관(Premnath 2012, Hussein 2019, Leblebicioğlu 2022).
> - 불변 사실 2: 골밀도가 낮을수록 주위 응력·임플란트 변위↑, D4가 최악 — 해면골 탄성계수↓ + 피질골 두께↓ → 응력·미세동요(micromotion) 동시 증가(Leblebicioğlu 2022, Chang 2024).
> - 불변 사실 3: 거시설계는 응력을 재분배할 뿐 치조정 집중을 없애지는 못함.
> - 핵심 레버: 나사(thread) 기하·body 형태가 가장 최적화 가능한 handle이며 효과는 골질 의존적 — 깊은 나사가 D3/D4에서 치조정 응력 ~40%·변위 ≥9% 감소, D2에서는 거의 무변화(Chang 2024).
> - 테이퍼(taper)는 trade-off: 일차 안정성(primary stability)을 높이나 모든 밀도에서 peak von Mises 응력↑(Hussein 2019) → 저밀도골 선택은 순수 이득이 아님.
> - 나사형 > 원통형이 치조정에 더 하중, 원통형이 D3/D4에서 상대적으로 더 잘 분산(Premnath 2012).
> - 임상 결정점: ①설계 무관 치조정 응력 집중 예상 → 과하중 회피·C/I비 관리·교합 scheme으로 치조정 보호 ②D3/D4에서 나사 설계가 최고 수율 레버 ③테이퍼는 즉시하중 의도·골밀도와 함께 저울질 ④FEA는 옵션 순위용이지 생존 예측용이 아님.
> - 한계(caveat): 전부 in silico — 균질·등방성 골, 정적 단일하중, 이상화된 골유착. FEA는 응력을 순위·국소화할 뿐 생존을 예측하지 않음; 저밀도골이 왜 더 실패하는지를 설명하는 mechanistic prior로 다룰 것.
> - Gap: 순환·피로 하중 미반영, 환자별 이방성 거의 미시뮬, FEA 응력→임상 변연골 소실/실패 검증 chain 없음.

## Three-line Summary

Synthesis of 5 FEA studies: peri-implant stress concentrates universally at the crestal cortical bone around the implant neck regardless of design or bone density (Premnath 2012, Hussein 2019, Leblebicioğlu 2022); bone density reduction from D1 to D4 raises peri-implant stress and implant displacement proportionally — D4 cancellous modulus reduction increases both stress and micromotion simultaneously (Leblebicioğlu 2022, Chang 2024) — and macro-design redistributes but never abolishes this crestal concentration.

Thread depth/geometry is the most optimizable lever and its payoff is bone-quality-dependent: deeper threads reduce crestal stress ~40% and displacement ≥9% in D3/D4 but show negligible change in D2 (Chang 2024); threaded designs load the crest more than cylindrical but cylindrical distributes more favorably in D3/D4 (Premnath 2012); taper raises peak von Mises stress across all densities versus cylindrical (Hussein 2019), making it a stability-vs-crestal-stress trade-off rather than a pure win in soft bone.

FEA ranks and localizes stress but does not predict clinical survival — treat these as mechanistic priors explaining why low-density bone shows higher implant failure rates; gaps include no cyclic/fatigue loading simulation, no patient-specific anisotropic bone, and no validated chain from FEA crestal stress to clinical marginal bone loss.

## 세줄요약

5편 유한요소분석(Finite Element Analysis, FEA) 종합: 임플란트 주위 응력은 모든 모델에서 설계·골밀도 무관하게 임플란트 경부 치조정 피질골에 집중(Premnath 2012·Hussein 2019·Leblebicioğlu 2022); 골밀도가 낮아질수록(D4 최악) 응력과 임플란트 변위가 비례 증가하며, 해면골 탄성계수 저하 + 피질골 두께 감소 → 응력·미세동요(micromotion) 동시 악화(Leblebicioğlu 2022·Chang 2024) — macro-design은 재분배할 뿐 치조정 집중을 없애지 못함.

나사(thread) 기하가 가장 최적화 가능한 레버이며 효과는 골질 의존적: 깊은 나사가 D3/D4 치조정 응력 ~40%·변위 ≥9% 감소(D2는 무변화; Chang 2024), 나사형 > 원통형이 치조정에 더 하중하나 원통형이 D3/D4에서 분산 유리(Premnath 2012), 테이퍼(taper)는 모든 밀도에서 peak von Mises 응력↑(Hussein 2019) → 1차 안정성 이득 vs 치조정 응력 증가의 trade-off.

FEA는 응력을 순위·국소화할 뿐 임상 생존을 예측하지 않음 — 저밀도골 실패 증가의 기전적 선행 근거로 활용하고 임상/SR 근거와 함께 판단; 순환·피로 하중·이방성 골 미시뮬·FEA 응력→변연골소실/실패 검증 chain 부재가 현재 주요 갭이다.

## Thesis
Finite element analysis answers a question clinical trials cannot resolve cleanly: *where* does load go, and *how* does implant macro-design redistribute it as bone quality degrades? Five FEA studies converge on three invariants and one lever.

The invariants: (1) **stress concentrates at the crestal cortical bone around the implant neck** — universally, regardless of design or density (Premnath 2012, Hussein 2019, Leblebicioğlu 2022); (2) **lower bone density raises peri-implant stress and implant displacement** — D4 bears the highest stress, and falling cancellous modulus increases both stress and micromotion (Leblebicioğlu 2022, Chang 2024); (3) **macro-design redistributes but never abolishes crestal concentration**.

The lever: **thread geometry and body shape are the optimizable handles, and their payoff is bone-quality-dependent.** Deeper threads cut crestal stress ~40% and displacement ≥9% in D3/D4 but barely move D2 (Chang 2024). Threaded designs load the crest more than cylindrical, which distribute relatively better in D3/D4 (Premnath 2012); tapered bodies show higher peak von Mises stress than cylindrical across all densities (Hussein 2019). This makes taper a **trade-off** — it aids primary stability (Heimes 2023, macrogeometry review) yet raises functional crestal stress, so the soft-bone design choice is not a pure win. [미검증]

Caveat: every input here is in silico (homogeneous/isotropic bone, static single-load, idealized osseointegration). FEA ranks and localizes stress; it does not predict survival. Treat these as mechanistic priors that explain *why* low-density bone fails more (per [[overviews/bone-quality-implant-risk-modification-overview]]), not as outcome evidence. [확인]

## Evidence Map

| Paper | Model | Variables | Key finding | Confidence |
|---|---|---|---|---|
| Premnath 2012 | 3D FEA, 8 models | threaded vs cylindrical × D1–D4 | crestal stress universal; threaded > cylindrical; cylindrical better distributes in D3/D4 | in-vitro |
| Leblebicioğlu 2022 | 3D FEA | 2 thread designs × 4 bone types × abutment angle, 30° 200 N | D4 highest stress; ↓trabecular density + ↓cortical thickness → ↑stress; thread/angle modulate | in-vitro |
| Hussein 2019 | 3D FEA, mandible | tapered vs cylinder × thread depth | crestal cortical peak; tapered > cylinder peak von Mises (all bone types) | in-vitro |
| Chang 2024 | 3D FEA, optimization | thread pitch/depth × D2/D3/D4 | deeper thread cuts crestal stress ~40% & displacement ≥9% in D3/D4; negligible in D2 | in-vitro |
| Öztürk 2026 | 3D FEA, anterior | bone availability × load angle × restoration | scenario-dependent stress for single anterior implant | in-vitro |

## Clinical Decision Points
1. **Expect crestal cortical stress concentration regardless of design** — protect the crest (avoid overload, control C/I ratio, occlusal scheme per [[overviews/implant-occlusion-loading-biomechanics-overview]]). [확인]
2. **In D3/D4 bone, thread design is the highest-yield design lever.** Deeper-threaded designs reduce crestal stress and micromotion where it matters; in D2 the choice is nearly stress-neutral. [미검증]
3. **Taper is a trade-off, not a free win.** It boosts primary stability but raises peak crestal stress — weigh against immediate-loading intent and bone density. [미검증]
4. **Use FEA to rank options, not to predict survival.** Pair these priors with clinical/SR evidence on osseodensification, undersizing, and loading timing. [확인]

## Gaps & Future Research
- Static single-load models; cyclic/fatigue loading and dynamic micromotion under-modeled.
- Idealized bone material properties; patient-specific anisotropy rarely simulated.
- No direct link from FEA stress magnitude to clinical marginal bone loss or failure — the validation chain is missing.
- Thread-depth optimization (Chang 2024) needs experimental/clinical confirmation.

## Related overviews
- [[overviews/bone-quality-implant-risk-modification-overview]] — the clinical risk axis these FEA priors mechanistically explain.
- [[overviews/implants-isq-stability-ladder]] — the measurement layer (ISQ) for primary stability.
- [[overviews/implant-occlusion-loading-biomechanics-overview]] — loading-phase occlusal biomechanics (complementary lens).
- [[overviews/osseodensification-clinical-applications]] — the soft-bone preparation solution.

## Related Papers
- [[implants/premnath-2012-stress-distribution-bone-density-fea]] — threaded vs cylindrical × D1–D4.
- [[implants/leblebicioglu-kurtulus-2022-fea-implant-design-bone-density-stress]] — design × bone density × abutment angle.
- [[implants/hussein-2019-thread-depth-implant-shape-stress-mandible-fea]] — taper vs cylinder peak stress.
- [[implants/chang-2024-optimization-implant-design-bone-quality-fea]] — thread-depth optimization per bone quality.
- [[implants/ozturk-2026-stress-distribution-anterior-implant-fea]] — anterior single-implant scenarios.
- [[implants/heimes-2023-macrogeometry-primary-stability-implants-narrative-review]] — macrogeometry-stability counterpart to the stress trade-off.
