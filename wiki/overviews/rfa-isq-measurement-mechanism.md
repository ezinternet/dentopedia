---
title: "RFA/ISQ Measurement Mechanism — Why Stiffness Becomes Frequency, and Why Frequency Is Not Wobble"
authors: Synthesis (Damian Lee)
year: 2026
date: 2026-07-17
doi: N/A
source: N/A
category: overviews
evidence_level: synthesis
pdf_path: N/A
pdf_filename: N/A
source_collection: synthesis
tags: [isq, rfa, osstell, smartpeg, resonance-frequency, biomechanics, mechanism, effective-length, stiffness, overview]
source_wiki:
  - wiki/implants/isq/meredith-1996-quantitative-stability-implant-tissue-rfa.md
  - wiki/implants/isq/sennerby-2008-implant-stability-resonance-frequency-analysis.md
  - wiki/implants/isq/bhandarkar-2023-rfa-mathematical-modeling-implant-stability.md
  - wiki/implants/isq/chatvaratthana-2017-cortical-bone-crestal-buccolingual-isq.md
  - wiki/implants/isq/sennerby-2015-two-different-implant-designs-drilling.md
relations:
  - type: extends
    target: implants-isq-stability-ladder
---

## 한국어 핵심요약

> [!summary] 한국어 핵심요약
> - 이 페이지는 `implants/isq/`의 **기전 축**이다 — "왜 강성이 주파수가 되고, 그 주파수가 왜 ISQ인가". 기존 [[overviews/implants-isq-stability-ladder]]가 경험적 사실로 나열한 관찰들(치조정 피질골 지배·MBL↔ISQ·동요 검출 실패)의 **원인**에 해당한다.
> - **핵심 등식**: f = (1/2π)√(k/m). 강성 k↑ → 공진주파수 f↑ → 임플란트 안정성 지수(Implant Stability Quotient, ISQ)↑. 질량 m↑ → f↓. *이 식 자체는 일반 진동역학이며 보유 논문의 주장이 아니다 — 아래 "기전 추론의 경계" 참조.*
> - **"픽스쳐의 강성"이 아니다.** 티타늄의 탄성계수는 식립 당일이나 6개월 뒤나 동일한데 ISQ는 그 사이 올라간다. ISQ를 움직이는 것은 픽스쳐가 아니라 **임플란트-골 시스템의 굽힘 강성(bending stiffness)** 이다.
> - **강성의 3분해** (Debruyne 2017): 임플란트-스마트펙(SmartPeg) 복합체 강성 / 주변골 강성 / 골-임플란트 계면 강성. 임상 공명주파수분석(Resonance Frequency Analysis, RFA)에서 변하는 것은 뒤의 둘뿐이다.
> - **ISQ 결정 3대 인자** (Sennerby 2008): 골의 기계적 특성 / 임플란트-골 접촉 강도 / 유효 노출 길이(Effective Length, EL). EL↑ → ISQ↓. 셋 중 어느 것도 "티타늄이 얼마나 단단한가"가 아니다.
> - **주파수 ≠ 진폭 (이 페이지의 중심 명제).** 공진주파수가 높다는 것은 더 **빠르게** 진동한다는 뜻이지 더 **많이** 흔들린다는 뜻이 아니다. Bhandarkar 2023의 2자유도(2-DOF) 모델은 강성↑ → 공진주파수↑ **그리고 공진점 미세변위(micro-displacement)↓** 를 동시에 낸다 — 단단한 임플란트는 **빠르고 작게** 떨고, 무른 임플란트는 **느리고 크게** 흔들린다.
> - **실측 대역** (Debruyne 2017): 공명주파수(Resonance Frequency, RF) 약 5.0 kHz(저 ISQ Straumann) ~ 8.6 kHz(고 ISQ Ankylos). 초당 5,000~8,600회 왕복 — 눈에도 손끝에도 감지되지 않는다. ISQ 측정이 "흔들어보기"와 근본적으로 다른 검사인 이유.
> - **ISQ는 kHz가 아니다.** Osstell 비공개 4차 다항식 `ISQ = e·f⁴ + d·f³ + c·f² + b·f + a`로 변환한 값(계수는 영업비밀)이므로 "ISQ 1점 = 몇 Hz" 같은 선형 환산은 성립하지 않는다. 단 레이저 도플러 진동측정법(Laser Doppler Vibrometry, LDV)으로 RF를 독립 포착해 같은 알고리즘에 넣은 값이 기기 직접값과 r=0.990 — **변환 알고리즘 자체는 검증되었다** (Debruyne 2017).
> - **기전이 설명하는 관찰 ① — 치조정 지배**: 치조정 피질골 두께 r=0.885, 6·9 mm 깊이와 해면골은 전 깊이 무상관 (Chatvaratthana 2017, 전향 n=19). 굽힘 강성은 지지점 근처가 지배하기 때문이며, 원 논문 스스로 "RFA는 전체 골량이 아니라 변연골 강성을 잰다"로 결론한다.
> - **기전이 설명하는 관찰 ② — MBL이 ISQ를 떨어뜨리는 경로**: Meredith 1996의 노출 고정체 높이 ↔ 공진주파수 r=0.94(p<0.01)가 EL 축 그 자체다. 골 흡수 → 지지점 하강 → EL↑ → f↓ → ISQ↓. 임플란트가 약해진 것이 아니라 **지렛대가 길어진 것**이다.
> - **기전이 설명하는 한계 — 동요도 검출 실패**: Osstell RFA는 동요 임플란트를 신뢰성 있게 감별하지 못했고, 안정성 판정은 ISQ ≥47에서만 가능했다 (Nedir 2004, 전향 n=106). 주파수는 진폭이 아니므로 **ISQ를 동요도(mobility) 대용으로 쓰면 안 된다.**
> - **기기 세대 주의**: 구형 유선 Osstell은 Mentor/IDx 대비 ISQ를 약 9–10 과소평가 — 세대 간 ISQ 비교·풀링에는 보정이 필요하다 (Debruyne 2017).
> - **임상 한 줄**: ISQ가 낮다는 것은 "임플란트가 헐겁다"가 아니라 **"이 시스템이 무르게 운다"** 는 뜻이다. 원인은 골질·계면 미성숙·지지 레벨 하강 셋 중 하나이고, 셋의 처치는 각각 다르다.
> - 기전 4편(Meredith 1996·Sennerby 2008·Bhandarkar 2023·Debruyne 2017)의 개별 내용은 [확인]. 기전→관찰 연결은 각 논문 위에 얹은 **종합 추론**이며 별도 검증 연구가 있는 것은 아니다.

## Three-line Summary

Mechanism synthesis of 4 spine papers (Meredith 1996 origin in-vitro/in-vivo; Sennerby 2008 narrative review by the RFA inventor; Bhandarkar 2023 2-DOF engineering model; Debruyne 2017 laser-vibrometry validation) answering a question the ISQ threshold literature assumes rather than states: why does interface stiffness become a frequency, and what does that frequency physically mean?

The chain is stiffness → resonance frequency → ISQ, but the stiffness is that of the implant–bone *system* (Debruyne's three entities: implant–SmartPeg complex, surrounding bone, bone–implant interface; Sennerby's three determinants: bone mechanical properties, implant–bone contact strength, effective length), never the titanium fixture's own modulus — which does not change while ISQ climbs; measured RF runs ~5.0–8.6 kHz and is converted to ISQ by a proprietary 4th-order polynomial validated at r=0.990 against independent laser-Doppler capture.

Frequency is not amplitude: a higher resonance frequency means faster vibration, and Bhandarkar's model shows stiffer systems simultaneously exhibit *lower* micro-displacement at the resonance peak — so ISQ must never be read as a mobility test (Nedir 2004: Osstell could not reliably identify mobile implants; stability determinable only at ISQ ≥47).

## 세줄요약

기전 종합 4편(Meredith 1996 원조 체외·생체내; Sennerby 2008 RFA 발명자 내러티브 종설; Bhandarkar 2023 2자유도 공학 모델; Debruyne 2017 레이저 진동측정 검증): ISQ 임계값 문헌이 전제만 하고 서술하지 않는 질문 — 계면 강성은 왜 주파수가 되며, 그 주파수는 물리적으로 무엇인가 — 에 답한다.

사슬은 강성 → 공명주파수 → ISQ이나 그 강성은 임플란트-골 **시스템**의 것이지(Debruyne 3분해: 임플란트-SmartPeg 복합체·주변골·골-임플란트 계면 / Sennerby 3대 인자: 골 기계적 특성·임플란트-골 접촉 강도·유효 노출 길이) 티타늄 픽스쳐 자체의 탄성계수가 아니다 — 후자는 ISQ가 상승하는 동안 변하지 않는다; 실측 RF는 약 5.0–8.6 kHz이고 비공개 4차 다항식으로 ISQ 변환되며 그 알고리즘은 독립 레이저 포착 대비 r=0.990으로 검증되었다.

주파수는 진폭이 아니다 — 공진주파수가 높다는 것은 빠른 진동을 뜻하며, Bhandarkar 모델에서 강성이 높은 시스템은 공진점 미세변위가 오히려 **더 작다**; 따라서 ISQ를 동요도 검사로 읽으면 안 된다 (Nedir 2004: Osstell은 동요 임플란트를 신뢰성 있게 감별 못함, 안정성 판정은 ISQ ≥47에서만 가능).

## Summary

Every ISQ threshold in this wiki — `≥70 at placement`, `≥65 after 4–6 weeks`, `≥54 for immediate loading` — rests on an unstated physical claim: that a number derived from a vibration frequency tracks the biological event we care about (osseointegration). The [[overviews/implants-isq-stability-ladder]] page organises the *empirical* answer across three axes (device, threshold, variables). This page supplies the **fourth, mechanistic axis**: why the chain works at all, and — equally important — what the mechanism forbids us from reading into ISQ.

The clinical payoff is not academic. Three of the ladder's headline observations (crestal cortical dominance, MBL lowering ISQ, RFA failing to detect mobility) look like unrelated empirical facts until the mechanism is stated, at which point they are all the same fact seen from different angles.

## The Core Chain

**Stiffness → resonance frequency → ISQ.**

For a mass–spring system the natural frequency rises with stiffness `k` and falls with mass `m` (`f = (1/2π)√(k/m)`). Bhandarkar 2023 instantiates exactly this for a dental implant as a **2-degree-of-freedom mass–spring–damper model**, with `k` and `c` derived from finite element analysis (FEA) of an implant embedded in cortical + trabecular bone, swept 5–15 kHz in MATLAB with FFT extraction of the resonance peak. The model recovers a clinically typical implant's resonance frequency inside that band and reproduces the clinical observation: better bone quality and higher bone-to-implant contact (BIC) → higher resonance frequency → higher ISQ.

Meredith 1996 established the same chain empirically and is its origin: implants embedded in self-curing PMMA and measured *during polymerisation* showed resonance frequency **rising as the surrounding material stiffened** — a bench proxy for bone maturation — with in-vivo measurements correlating well with the in-vitro data.

### Which stiffness? — the load-bearing correction

The chain is routinely paraphrased as "a stiffer fixture reads higher." That paraphrase is wrong in a way that matters. **Titanium's elastic modulus is identical on placement day and six months later**, yet ISQ climbs across that interval. The fixture is not what changes.

Two independent decompositions in the held literature say what does:

| Source | Decomposition |
|---|---|
| [[implants/isq/debruyne-2017-isq-laser-vibrometry-resonance-frequency]] | Three RFA stiffness entities: **implant–SmartPeg complex** / **surrounding bone** / **bone–implant interface**. (The study deliberately embeds implants in homogeneous polyurethane resin to hold the latter two constant and isolate the measurement chain — which is why it validates the algorithm, not clinical bone behaviour.) |
| [[implants/isq/sennerby-2008-implant-stability-resonance-frequency-analysis]] | Three ISQ determinants: **bone mechanical properties** / **implant–bone contact strength** / **effective exposed length (EL)**, with EL↑ → ISQ↓. |

Neither list contains "how stiff the titanium is." The fixture contributes through its **exposed length and macro-design**, i.e. through the geometry of the beam, not the material of the beam.

### Frequency is not amplitude

This is the distinction the whole page exists to make, and it is the one clinicians most often collapse.

- **Frequency** = cycles per second = how *fast* = musical pitch.
- **Amplitude** = displacement per cycle = how *far* = musical loudness.

They are orthogonal axes. Tightening a guitar string (stiffness↑) raises its **pitch**; plucking it harder raises its **loudness** and leaves pitch untouched. Osstell excites the SmartPeg with magnetic pulses and reads the frequency at which it rings — it listens to pitch, not volume. `f = (1/2π)√(k/m)` contains no amplitude term.

And the relationship is not merely "independent" — Bhandarkar 2023 reports that at the resonance peak, higher stiffness yields **lower** micro-displacement. [[implants/isq/sennerby-2015-two-different-implant-designs-drilling]] empirically confirms this direction from the bench side: applying a standardized 15 N lateral force to the same implants after RFA measurement shows that higher ISQ co-occurs with **lower lateral displacement (μm)** and lower flex constant (μm/N). Critically, this correlation collapsed between implant designs in high-density bone — bone quality dominated fixture geometry when stiffness was already high. So:

| System | Vibration speed | Vibration amplitude |
|---|---|---|
| Dense bone / mature interface | fast (RF↑ → ISQ↑) | **small** |
| Soft bone / immature interface | slow (RF↓ → ISQ↓) | **large** |

A high-ISQ implant is one that vibrates **fast and small**. Reading high ISQ as "moves a lot" inverts the physics.

### The numbers, and why they are invisible

Debruyne 2017 measured RF spanning **~5.0 kHz** (low-ISQ Straumann) to **~8.6 kHz** (high-ISQ Ankylos). Five kHz is five thousand round trips per second — undetectable by eye or fingertip. That is precisely why RFA is not a refined version of percussion or wiggling: it interrogates a regime the hand cannot reach.

Two caveats travel with those numbers:

1. **ISQ ≠ kHz.** The device converts RF via a proprietary 4th-order polynomial, `ISQ = e·f⁴ + d·f³ + c·f² + b·f + a`, whose coefficients Osstell holds as trade secrets. No linear "X Hz per ISQ point" conversion exists. Debruyne 2017's contribution is that capturing RF by a fully independent method (laser Doppler vibrometry) and feeding it through that same algorithm reproduces the device's own output at **r=0.990 (p<0.001)**, mean difference ~0.09–0.54 ISQ units, not significantly different from zero (paired t p=0.058) — the conversion step is valid.
2. **The two anchor values come from different implant systems and therefore different SmartPegs.** Do not draw a single RF→ISQ curve through them. SmartPegs are system-specific, and the `m` term above is why that is not arbitrary bureaucracy.

## What the Mechanism Explains

The value of stating the mechanism is that several separately-catalogued empirical findings collapse into one.

| Empirical observation | Source | Mechanistic reading |
|---|---|---|
| Crestal cortical thickness r=0.885 with ISQ; buccolingual cortical at 3 mm r=0.535; **6 mm, 9 mm, and cancellous bone at every depth uncorrelated** | [[implants/isq/chatvaratthana-2017-cortical-bone-crestal-buccolingual-isq]] | Bending stiffness is dominated by support near the fulcrum. Bone far below the crest barely enters `k`. The paper reaches the same conclusion independently: RFA measures marginal bone stiffness, not overall bone quantity. |
| Resonance frequency ↔ exposed fixture height, r=0.94 (p<0.01) | [[implants/isq/meredith-1996-quantitative-stability-implant-tissue-rfa]] | The EL axis in its purest form — same fixture, same material, frequency moved purely by where the support sits. |
| Marginal bone loss lowers ISQ | [[implants/isq/sennerby-2008-implant-stability-resonance-frequency-analysis]] | Resorption drops the fulcrum → EL↑ → f↓ → ISQ↓. The implant did not weaken; the lever got longer. |
| RFA could not reliably identify mobile implants; stability determinable only at ISQ ≥47 | [[implants/isq/nedir-2004-predicting-osseointegration-primary-stability-rfa]] | Frequency is not amplitude. A test that reads pitch is not a test that reads wobble. This is a *prediction* of the mechanism, not an anomaly in the device. |
| Diameter influences ISQ more than length | [[overviews/implant-macrogeometry-length-diameter-primary-stability-overview]] | Diameter changes the beam's cross-section at the crest, where `k` is decided; apical length extends the beam below the fulcrum, where it is not. |

### 기전 추론의 경계 (scope of what is claimed here)

The `f = (1/2π)√(k/m)` framing and the beam/fulcrum language are **general vibration and beam mechanics, not claims from a held paper.** Bhandarkar 2023 supplies a mass–spring–damper model of an implant, which is the held-paper anchor for the modelling approach; it does not publish a fulcrum analysis of crestal cortical dominance. The right-hand column of the table above is therefore **synthesis-grade reasoning applied to observations each paper independently reports** — it is how the held findings cohere, not an additional finding with its own evidence. Anyone citing this page should cite the left column's papers for the facts and treat the mechanism as the reading, per Rule #4's boundary between clinical reasoning and citable factual claims.

## What the Mechanism Does NOT License

- **ISQ is not a mobility test.** Nedir 2004 is the direct evidence; the mechanism explains why this is structural rather than a device defect. A clinically mobile implant may still return a number.
- **ISQ below ~47 is not a finer-grained measurement of "worse."** Nedir 2004 found stability reliably determinable only at ISQ ≥47 — below that the reading is not a smaller value on the same scale, it is out of the instrument's competent range.
- **ISQ does not read apical bone.** Chatvaratthana 2017's null results at 6 and 9 mm are not underpowering; they are what the mechanism predicts. Do not use ISQ to reason about apical engagement.
- **ISQ across device generations is not comparable.** Older wired Osstell devices underestimate ISQ by ~9–10 units versus Mentor/IDx; systematic reviews cannot pool them uncorrected (Debruyne 2017).
- **A high ISQ does not license inference about bone quality on its own.** The three stiffness entities are summed in one number; the same ISQ can arise from different combinations. Bhandarkar 2023 explicitly supports interpreting ISQ with bone-quality context rather than in isolation.

## Related overviews

- [[overviews/implants-isq-stability-ladder]] — the empirical 3-axis spine (device · threshold · variables); this page is its mechanism axis
- [[overviews/isq-loading-threshold]] — ISQ threshold matrix for loading decisions
- [[overviews/implant-macrogeometry-length-diameter-primary-stability-overview]] — diameter > length, the empirical finding this mechanism explains
- [[overviews/high-insertion-torque-primary-stability-crestal-bone-overview]] — why insertion torque (IT) is not an ISQ substitute; complementary measurement axis
- [[overviews/sinus-lift-isq-loading-timing]] — ISQ trajectories after sinus elevation
- [[overviews/implant-design-bone-quality-stress-fea]] — FEA of design × bone quality; the stress side of the same biomechanics

## Related Papers

**기전 spine (mechanism spine)**
- [[implants/isq/meredith-1996-quantitative-stability-implant-tissue-rfa]] — origin of RFA (Bristol): exposed-height r=0.94, PMMA-polymerisation stiffness → frequency rise, in-vivo concordance; reports raw kHz, sets no thresholds
- [[implants/isq/sennerby-2008-implant-stability-resonance-frequency-analysis]] — the RFA inventor's own synthesis: three ISQ determinants including EL; stability dip
- [[implants/isq/bhandarkar-2023-rfa-mathematical-modeling-implant-stability]] — 2-DOF mass-spring-damper model, FEA-derived k and c, 5–15 kHz sweep + FFT: stiffness↑ → resonance↑ and micro-displacement↓
- [[implants/isq/debruyne-2017-isq-laser-vibrometry-resonance-frequency]] — LDV-captured RF through the Osstell algorithm vs direct IDx: r=0.990; three stiffness entities; RF ~5.0–8.6 kHz; cross-generation ~9–10 ISQ bias
- [[implants/isq/sennerby-2015-two-different-implant-designs-drilling]] — bench study (bovine bone, n=18 pairs) simultaneously measuring RFA + direct lateral displacement (15 N, μm) + flex constant (μm/N): empirical bridge confirming that higher ISQ co-occurs with lower fixture lateral displacement; correlation collapsed in high-density bone

**기전이 설명하는 관찰 (mechanism-explained observations)**
- [[implants/isq/chatvaratthana-2017-cortical-bone-crestal-buccolingual-isq]] — crestal cortical r=0.885; nothing at 6/9 mm; cancellous irrelevant at every depth
- [[implants/isq/nedir-2004-predicting-osseointegration-primary-stability-rfa]] — RFA not reliable for mobility; ISQ ≥47 floor; protocol-specific ISQi cut-offs (DL ≥49 / IL ≥54)

**측정 신뢰도 (measurement reliability — mechanism-adjacent)**
- [[implants/isq/zix-2008-osstell-periotest-implant-stability-clinical]] — Osstell ICC 0.99 vs Periotest 0.88; RFA is the more precise of the two
- [[implants/isq/kastel-2019-smartpeg-torque-isq-rfa]] — SmartPeg torque ≥10 Ncm required; the SmartPeg is part of the measured system, not a neutral probe

확신도 등급:
- 기전 4편의 개별 내용 = [확인] (본 세션에서 각 wiki 페이지 직접 판독).
- Chatvaratthana 2017 · Nedir 2004 수치 = [확인] (본 세션에서 wiki 페이지 직접 판독).
- 기전 → 관찰 연결(위 "What the Mechanism Explains" 표 우측 열) = 종합 추론. 각 좌측 논문은 [확인]이나 연결 자체를 검증한 연구는 보유하고 있지 않다.
