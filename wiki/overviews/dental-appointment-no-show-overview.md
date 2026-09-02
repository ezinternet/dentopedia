---
title: "Overview: Dental Appointment No-Shows & Non-Attendance"
type: synthesis
category: overviews
date: 2026-06-27
evidence_level: synthesis
source_collection: synthesis
source_papers:
  - wiki/practice-management/alkhurayji-2024-factors-patient-failure-attend-dental.md
  - wiki/practice-management/khries-2024-identifying-barriers-pediatric-dental-appointments.md
  - wiki/practice-management/alabdulkarim-2022-predicting-no-shows-dental-appointments.md
  - wiki/practice-management/bhatia-2018-pediatric-dental-appointments-no-show-rates-reasons.md
  - wiki/practice-management/samohyl-2021-non-attendance-dental-preventive-care-students.md
  - wiki/practice-management/prasad-2012-sms-reminder-dental-attendance-rct.md
  - wiki/practice-management/nelson-2011-text-vs-voice-reminder-pediatric-dental-rct.md
  - wiki/behavioral-dentistry/communication-relationship/currie-2021-promoting-regular-dental-attendance-problem.md
  - wiki/behavioral-dentistry/communication-relationship/okyere-boadu-2025-patient-challenges-dental-care-ghana.md
tags: [no-show, non-attendance, practice-management, appointment, reminder, sms, access-barriers, overview]
---

> [!summary] 한국어 핵심요약
> - **결론(thesis)**: 치과 미내원(No-show / Did-Not-Attend, DNA)은 무작위 사고가 아니라 **예측 가능한 환자·행동·사회적 패턴**이다. 보험이 작동하는 세팅에서는 비용(cost)보다 **망각·일정·가족 행동**이 핵심 동인이며, 가장 효과적 대책은 "차단(block)"이 아니라 **선별(flag) → 리마인더(reminder) → 슬롯 설계(slot design)**의 운영 사다리다.
> - **두 개의 다른 인구를 구분하라**: 이 페이지의 수치 대부분은 **예약은 했으나 안 온** 환자(appointment-level DNA)의 것이다. **애초에 정기 내원을 안 하는** 환자(문제지향적 내원자, problem-orientated attender — 영국 성인 약 1/3)를 정기 내원으로 전환시키는 문제는 별개이며, 그 중재 근거는 8개 데이터베이스를 뒤져 **단 3편**, 전부 재현 불가 보고 수준이다 (Currie 2021 체계적 문헌고찰, Systematic Review, SR). 리마인더로는 이 층을 못 푼다.
> - **유병 범위(prevalence range)**: 보고된 미내원율은 소아 44% (Khries) ~ 52% (Bhatia), 성인 단일 치과 노쇼율 42.7% (Alabdulkarim 196,018건) 까지로, 의과 1차진료보다 현저히 높다.
> - **고위험 프로필(predictor profile)**: 미혼·여성·35세 이하·초진·오전 슬롯 (Alkhurayji n=1,364). 다만 환자 특성과 요일/시간 간 통계적 유의 연관은 없었음(descriptive skew only).
> - **리드타임(lead time)이 최강 예측인자**: 머신러닝(Machine Learning, ML) 모델에서 예약-진료 간격(lead time) 제거 시 AUC가 7.5~7.9% 하락 — 단일 변수 중 가장 강력. 사전 노쇼 이력(prior no-show history)이 2위.
> - **ML 예측 성능(prediction angle)**: 최고 모델 AUC 0.718, F1 66.5% (vs 노쇼율 42.7% 베이스라인). 노쇼 이력을 **이진 시퀀스(binary sequence, 예: 1,0,0,1,0)**로 표현하는 방식이 핵심 기여, 다른 치과로 일반화도 확인.
> - **세대 간 전이(parental driver)**: 부모 자신의 예방진료 기피가 자녀 비참여의 **가장 강한 독립 예측인자** — 모(母) AOR 4.19, 부(父) AOR 3.41 (Samohyl). 노쇼는 치아 특이적 문제가 아니라 일반 건강행동 trait.
> - **사회경제적 지위(SES) 역설**: Bhatia에서 최상위가 아닌 **상-중류층이 노쇼율 최고(58.8%)** — 비용이 아니라 바쁜 일정·우선순위 저하 시사. (주의: 초록은 SES p<0.05 주장하나 표는 p=0.142 — 유의성 불일치, 시사적으로만 해석)
> - **리마인더 선호(reminder preference)**: 환자가 가장 원한 대책은 **전날 치과의사의 전화(48.3%)** > 예약카드(25.9%) > 문자(SMS, 23.8%) > 이메일(2%) (Bhatia). 단순 자동 SMS가 환자 선호 1순위는 아니라는 점 주목.
> - **리마인더 효과(이제 RCT 근거 추가)**: SMS 리마인더는 무(無)리마인더 대비 정시 내원을 79.2% vs 35.5%로 크게 높였다(Prasad RCT, n=206). 그러나 채널 비교에서는 **음성 전화가 SMS보다 우수**했다(노쇼 8.2% vs 17.7%, 보정 OR 2.12; Nelson RCT, n=318) — 환자 선호(전화)와 일치. 즉 "리마인더는 효과 있으나 채널이 중요"하며, 두 RCT 모두 단일기관·비교군 상이라 cross-trial 결론은 신중히.
> - **구조적 장벽(structural barrier)**: 보험 85%여도 소아 미내원 44% — 비용은 주동인 아님. 대중교통 의존(public transport)은 유의한 상관(p=0.002), 직원 의사소통 오류(staff miscommunication) 10.3%가 행정적 장벽 1위 (Khries).
> - **"비용은 주동인이 아니다"의 경계조건(boundary condition)**: 이 명제는 **보험·공적 지불이 작동하는 세팅**에서만 성립한다. 보편적 보장이 없는 가나 교육병원에서는 내원 전 장벽을 겪은 55.4% 중 **비용과 예약 가용성을 100%가 지목**했고, 비용→지연→질환 악화→더 큰 비용→회피 강화의 **악순환 고리(cascade)**가 질적 자료로 기록됐다 (Okyere Boadu 2025, n=130). 즉 비용은 "무관"한 게 아니라 **지불 구조가 먼저 흡수했을 때만 후순위**로 밀린다.
> - **진료 중 장벽도 미내원을 만든다**: 치과불안 (Dental Anxiety) 77%, 긴 대기 63.2%, **불충분한 의사소통 40.2%**, 치료계획·비용 투명성 부재 20.7% (Okyere Boadu 2025) — Khries의 직원 의사소통 오류(10.3%)와 같은 축이며, 리마인더가 아니라 **상담·고지 설계**로 푸는 문제다.
> - **임상·운영 takeaway**: ① 고위험군(초진·짧은 리드타임·과거 노쇼·기억 의존)을 **선별**, ② 환자 선호 채널로 **리마인더**(전화 우선), ③ 무차별 오버부킹 대신 **고위험 슬롯 단축**, ④ 가족·교통·예방진료 미수진 등 **구조·세대 장벽**을 동시에 공략. 단일 슬롯 차단보다 다층 운영 설계가 답.

## Three-line Summary

Synthesis of 9 studies (1 large ML retrospective, 1 adult retrospective, 4 cross-sectional including 2 pediatric, 2 reminder RCTs, and 1 systematic review): dental no-show rates are 42.7–52% (higher than primary-care medicine), driven by forgetfulness, scheduling conflicts, and parental behavior rather than cost **wherever a payer absorbs the fee** (44% non-attendance despite 85% insurance coverage, Khries 2024; highest-SES group had the highest rate, Bhatia 2018) — but where coverage is absent, cost and appointment availability were named by 100% of barrier-affected patients (Okyere Boadu 2025, Ghana).

The strongest predictors in ML modeling are lead time (booking-to-visit interval; removing it drops AUC 7.5–7.9%) and prior no-show history (binary sequence representation is the key ML feature); overall model AUC 0.718 / F1 66.5% (Alabdulkarim 2022, 196,018 appointments); parental avoidance of preventive care is the strongest independent predictor of adolescent non-attendance (maternal AOR 4.19, Samohyl 2021).

Clinical bottom line: apply an operational ladder — flag high-risk patients (new visit, long lead time, prior no-show, memory-reliant), deliver patient-preferred reminders (voice beats SMS: no-show 8.2% vs 17.7%, OR 2.12, Nelson 2011 RCT; SMS vs none raised on-time attendance 79% vs 36%, Prasad 2012), shorten high-risk slots rather than blindly overbooking, and address structural/intergenerational barriers — while recognising that this whole ladder acts only on patients who already booked; converting problem-orientated (pain-only) attenders to regular attendance is a separate problem whose intervention literature contains just 3 poorly-reported studies (Currie 2021 SR).

## 세줄요약

9편 종합(ML 후향 1, 성인 후향 1, 단면 4편, 리마인더 RCT 2, 체계적 문헌고찰 1): 치과 미내원율 42.7~52% — **지불자가 비용을 흡수한 세팅에서는** 비용이 아닌 망각·일정·부모 행동에 좌우되는 예측 가능한 패턴(보험 85% 있어도 미내원 44%, Khries 2024; 최상위 SES가 최고 노쇼율, Bhatia 2018). 단 보장이 없는 세팅에서는 비용·예약 가용성을 장벽 경험자 100%가 지목했다(Okyere Boadu 2025, 가나).

가장 강한 예측인자: 리드타임(제거 시 AUC 7.5~7.9% 하락)과 과거 노쇼 이력(이진 시퀀스 표현이 핵심); ML AUC 0.718(Alabdulkarim 2022, 196,018건); 부모의 예방진료 기피가 청소년 미내원 최강 독립 예측인자(모 AOR 4.19, Samohyl 2021).

임상 결론: 운영 사다리 — 위험 선별(초진·긴 리드타임·과거 노쇼·기억 의존) → 리마인더(음성>SMS: 노쇼 8.2% vs 17.7%, OR 2.12, Nelson 2011 RCT; SMS vs 무 = 정시 79% vs 36%, Prasad 2012) → 고위험 슬롯 단축 → 구조·세대 장벽 공략. 단 이 사다리는 **이미 예약한 환자**에게만 작동한다 — 통증 시에만 오는 환자를 정기 내원으로 바꾸는 중재는 근거가 3편뿐이다(Currie 2021).

## Thesis

Dental did-not-attend (DNA) is **not random noise but a socially and behaviorally patterned, partly predictable event**, and dentistry is structurally vulnerable to it because dental visits are long (~36–49 min vs ~17 min for primary care), so a no-show wastes a large, non-recoverable block of chair time and blind overbooking is impractical (Alabdulkarim).

A scope note before the claims: **this page is about two different populations, and only the first is well covered here.** Six of the nine studies describe *appointment-level* non-attendance — the patient booked and did not come. Currie 2021 covers the other population, the *problem-orientated attender* who books only in pain (about one-third of UK adults) and therefore never enters the no-show denominator at all; its finding is that the intervention literature for converting them is essentially empty (3 poorly-reported studies across eight databases). Every rung of the operational ladder below acts on the first population. Do not read a reminder-and-slot protocol as an answer to the second.

Across these studies three claims are robust:

1. **Cost is rarely the dominant driver — where a payer absorbs it.** Pediatric non-attendance ran 44% despite 85% insurance coverage (Khries), and the highest-SES, not lowest-SES, group had the highest no-show rate in Bhatia (58.8%) — pointing to time, prioritization, forgetfulness, and family scheduling rather than financial access. **The boundary condition matters**: in a Ghanaian teaching hospital without comparable coverage, cost and appointment availability were named by 100% of the 55.4% who hit a pre-visit barrier, and the qualitative data traced a cost → delay → worse disease → higher cost → reinforced avoidance cascade (Okyere Boadu 2025, n=130). Cost is not irrelevant; it is *demoted* once a payer absorbs it, and it returns to first place when that structure is missing. Read the Saudi/Jordanian/Indian findings as conditional on their payment context, not as a universal law.
2. **The strongest signals are behavioral, not demographic.** In the ML model, **lead time (booking-to-visit interval) was the single strongest predictor** and **prior no-show history second** (Alabdulkarim); reliance on memory to track appointments was the robust significant correlate in Bhatia (p=0.024); and a **parent's own avoidance of preventive care** was the strongest independent predictor of an adolescent's non-attendance (Samohyl, maternal AOR 4.19 / paternal AOR 3.41). Demographic skews (single, female, ≤35y, new-patient, morning-slot — Alkhurayji) describe *who* misses but did not reach statistical significance against scheduling dimensions.
3. **The fix is an operational ladder, not a single lever.** Flag high-risk appointments, deliver patient-preferred reminders, shorten (don't blindly overbook) high-risk slots, and address the structural/intergenerational barriers that no reminder will fix.

## Evidence Map

| Paper | Design | n | Key finding | Confidence |
|---|---|---|---|---|
| Alabdulkarim 2022 | Retrospective ML model development/validation (Riyadh, 2019) | 196,018 appts (42.7% no-show) | Best model AUC 0.718 / F1 66.5%; **lead time** strongest predictor (−7.5–7.9% AUC if removed), prior no-show history second; novel **binary-sequence** history feature; generalized to 2nd clinic (RF AUC 0.748) | retrospective |
| Alkhurayji 2024 | Retrospective secondary analysis of missed-appt records (Riyadh military) | 1,364 no-show records | No-show profile: **single 56.2%, female 60.7%, ≤35y 67.3%, new-patient, morning slot**; but no significant association between patient characteristics and day/time (all p≈0.5–0.97); recommends evening + walk-in slots | retrospective |
| Khries 2024 | Cross-sectional questionnaire (pediatric, Jordan) | 265 children <12y | **44% missed despite 85% insured**; significant correlates: child age (p=0.0041), public-transport use (p=0.002); top barriers family/social commitments 15.5%, forgetfulness 11.2%, staff miscommunication 10.3% | cross-sectional |
| Bhatia 2018 | Cross-sectional questionnaire (pediatric, Navi Mumbai) | 294 parents | **52% missed**; forgetfulness/exams top reasons; **memory-reliance** significant (p=0.024); upper-middle SES highest no-show (58.8%); **48.3% prefer dentist phone-call reminder** > card 25.9% > SMS 23.8% > email 2% | cross-sectional |
| Samohyl 2021 | Cross-sectional school survey, student-parent linked (Slovakia) | 515 students + 681 parents | **Parental avoidance is the strongest independent predictor** of adolescent non-attendance (mother AOR 4.19, father AOR 3.41); skipping pediatric ↔ dental care co-occurs (AOR 5.14); male, older, incomplete-family, low-income, home-stress cluster | cross-sectional |
| Prasad 2012 | Controlled trial, SMS reminder vs none (dental OPD, India) | 206 (test 96 / control 110) | **SMS reminder → on-time attendance 79.2% vs 35.5%** — reminders work vs no reminder; allocation method not fully recoverable (likely quasi-RCT) | rct |
| Nelson 2011 | RCT, SMS text vs voice reminder (pediatric dental, U. Washington) | 318 dyads | **Voice reminder beat SMS** (no-show 8.2% vs 17.7%; adjusted OR 2.12, p=.04) — channel matters; matches patient preference for a call | rct |
| Currie 2021 | Systematic review, 8 databases, interventions to convert problem-orientated attenders | **3 studies** | The *other* population: pain-only attenders (~1/3 of UK adults) never enter the no-show denominator. Only 3 interventions found (anxiety clinic, free-update campaign, Scotland free check-up policy), all too poorly reported to replicate; **no intervention can be recommended**. Four design targets: communication, relationship, awareness of silent disease, cost/access | sr |
| Okyere Boadu 2025 | Mixed-methods cross-sectional (teaching hospital OPD, Kumasi, Ghana) | 130 | **The cost boundary condition**: of the 55.4% with a pre-visit barrier, cost and appointment availability were named by **100%** (insurance 72.2%, anxiety 63.9%); in-visit — anxiety 77%, waits 63.2%, **inadequate communication 40.2%**, cost/plan transparency deficit 20.7%; qualitative cost→delay→worse disease→higher cost cascade | cross-sectional |

> [!note] Bhatia SES caveat
> Bhatia's abstract reports socioeconomic status as a significant correlate of missing (p<0.05), but the SES results table reports p=0.142 (not significant) — an internal inconsistency. Treat the SES association as **suggestive only**; the robust significant correlate in that study is method-of-remembering (memory-reliance, p=0.024).

## Clinical Decision Points

An operational ladder — apply in order; each rung addresses a different layer of risk.

**1. Identify who is high-risk (profile + behavior).**
- Demographic skew (descriptive, from Alkhurayji): single, female, ≤35y, **new/initial-visit**, morning-slot patients.
- Behavioral high-risk markers (the stronger signals): **short lead time and a history of prior no-shows** (Alabdulkarim); **tracking appointments by memory alone** (Bhatia, p=0.024); a family where the **parent avoids their own preventive care** (Samohyl).
- Pediatric-specific: reliance on **public transport** (Khries, p=0.002); the highest-risk pediatric profile is young, memory-reliant, higher-SES, male, with prior broken appointments (Bhatia).

**2. Predict / flag at the appointment level.**
- A deployable per-appointment predictor is feasible: ML reached **AUC 0.718, F1 66.5%** vs a 42.7% no-show baseline, and generalized across clinics (Alabdulkarim).
- Encode **prior no-show history as a binary sequence** (1=attended, 0=missed, e.g. 1,0,0,1,0) rather than a collapsed average — this improved logistic-regression AUC by 2–5%.
- **Lead time is the top feature**: the longer the booking-to-visit interval, the higher the risk — so long-lead and high-history appointments are the ones to flag.

**3. Reminder strategy — match the channel to patient preference.**
- Patients' stated preference hierarchy (Bhatia): **dentist phone call the day before (48.3%) > appointment card (25.9%) > SMS (23.8%) > email (2%)**. A personal call, not a default automated SMS, was the #1 preferred lever.
- **Reminders work (RCT evidence), but channel matters.** An SMS reminder vs none raised on-time attendance to **79.2% vs 35.5%** (Prasad) — so *any* reminder beats none; but head-to-head, **voice reminders outperformed SMS** (no-show 8.2% vs 17.7%, adjusted OR 2.12; Nelson), converging with the stated preference for a call. Default to a personal/voice reminder for high-risk appointments and reserve SMS as the scalable baseline; both trials are single-setting with different comparators, so treat the channel ranking as directional.
- Establish the reminder/recall mechanism **at the first visit** (Bhatia), since new-patient visits are over-represented among misses (Alkhurayji).
- Because memory-reliance is a significant correlate (Bhatia), any external reminder displaces the single highest-risk tracking method.

**4. Scheduling / capacity design — shorten, don't blindly overbook.**
- For flagged high-risk appointments, **shorten the slot duration** to cap the cost of an absence rather than aggressively overbook (Alabdulkarim) — appropriate because dental slots are long and overbooking disrupts following patients.
- Offer **evening appointments and walk-in slots** to recover chair time and reach the working/busy high-SES segment (Alkhurayji); morning/early (<10 AM) slots are the most missed (Alkhurayji, Alabdulkarim).
- Reduce wait times and shorten follow-up gaps (Khries administrative barriers).

**5. Address structural and intergenerational barriers (no reminder fixes these).**
- Fix **staff miscommunication** (10.3% of pediatric barriers, the #1 administrative barrier — Khries) with a clear, explicitly-communicated cancellation/no-show policy.
- For families dependent on **public transport**, consider scheduling around transit access (Khries).
- Engage the **parent's own preventive-care behavior** as a lever for the child's recall attendance, and recognize that a family skipping pediatric care will likely skip dental care too (Samohyl) — target the family unit, not just the patient.
- Extend recall/entitlement beyond the pediatric cutoff age, since the just-turned-adult group loses the under-18 free check-up entitlement yet has high need (Samohyl).
- **Treat the consultation itself as a structural barrier.** Inadequate communication (40.2%) and absent treatment-plan/cost transparency (20.7%) were measurable in-visit challenges independent of the fee itself (Okyere Boadu) — the patient-side counterpart of Khries's staff-miscommunication finding. Jargon-free explanation and an up-front written cost estimate are the levers patients themselves named.
- **Where cost is not absorbed by a payer, price structure is the first lever, not the last.** Payment plans and staged treatment address the cost→delay→worse-disease→higher-cost cascade documented qualitatively in Okyere Boadu; a reminder sent to a patient who cannot pay changes nothing.

**6. Know the ceiling — none of the above reaches the patient who never books.**
- The ladder above operates on booked appointments. For **problem-orientated (pain-only) attenders**, the evidence base for conversion is 3 poorly-reported studies (Currie): a dental anxiety clinic, a free "dental update" open-house campaign, and Scotland's free check-up policy. No single intervention can be recommended, and none has been replicated.
- Currie's four design targets are the honest starting point for a locally-designed, locally-evaluated program: **dentist communication, the dentist–patient relationship, awareness of unrecognised (silent) disease, and cost/access**. Note the convergence — three of the four reappear as measured barriers in Okyere Boadu (communication 40.2%, transparency 20.7%, cost 60.9%), which is the strongest cross-study signal this page has for where to build.
- Do not expect a published recipe here; expect to run and measure your own.

## Gaps & Future Research

- **No true rate or relative risk.** Alkhurayji profiled only missed appointments with no attended-appointment comparator, so it yields a descriptive profile, not a no-show rate or relative risk. Reported "rates" (44%, 52%, 42.7%) come from different populations/definitions and are not directly comparable.
- **Cross-sectional, self-report, single-site dominance.** Six of the nine studies are cross-sectional or retrospective, and five of those are single-center (Riyadh military, Jordan hospital, Navi Mumbai college, Bratislava schools, Kumasi teaching hospital) with self-report bias and no longitudinal/causal inference; only Alabdulkarim used a second site for validation. Samohyl's non-attender group was small (n=57) and Okyere Boadu's n=130 was a 10-day consecutive-sample survey, making both hypothesis-generating.
- **Bhatia SES inconsistency unresolved** (abstract p<0.05 vs table p=0.142) — the role of SES in no-show, and the counter-intuitive high-SES-highest-rate finding, needs prospective confirmation.
- **Reminder-channel efficacy — partly answered, still thin.** Two RCTs now address it: SMS vs none works (Prasad, 79% vs 36%) and voice beat SMS head-to-head (Nelson, OR 2.12). But both are single-center with different comparators, neither tests app/push reminders, and there is no dental meta-analysis or cost-effectiveness comparison of call vs SMS vs app — so the channel ranking is directional, not settled.
- **ML deployment validation.** Alabdulkarim's model is developed/validated retrospectively on Saudi data; prospective deployment, fairness across demographic groups, and transferability to Korean clinic appointment systems are untested.
- **No Korean or Asian-clinic operational data** in this set beyond the Indian pediatric cohort — local appointment-system records (e.g. via clinic EMR) would let the binary-sequence/lead-time approach be re-validated domestically.
- **Conversion of pain-only attenders is the largest gap on the page, and it is now documented rather than merely suspected.** Currie searched eight databases and found three studies, all irreproducible as reported; no trial has tested a reminder, recall, or scheduling intervention *on this population*. Every attendance number above is conditional on the patient having booked.
- **The cost question is unresolved across payment systems.** The wiki holds one insured-setting cluster (cost demoted) and one uninsured-setting study (cost dominant), with no study varying coverage within one health system — so "cost is not the driver" cannot yet be stated unconditionally, and its transferability to the Korean National Health Insurance context, where dental coverage is partial, is untested.
- **No paper here measures whether fixing communication or cost transparency changes attendance.** Okyere Boadu measures these as perceived barriers, not as an intervention; the causal link from a jargon-free explanation or an up-front estimate to a lower no-show rate remains an assumption.

## Related Papers

- [[practice-management/alabdulkarim-2022-predicting-no-shows-dental-appointments]] — the quantitative engine of the synthesis: turns factor knowledge into a deployable per-appointment ML predictor (AUC 0.718); establishes lead time and prior no-show history (binary-sequence encoded) as the dominant signals.
- [[practice-management/alkhurayji-2024-factors-patient-failure-attend-dental]] — the adult-population descriptive profile (single/female/≤35y/new-patient/morning) and the evening+walk-in operational recommendation; note its no-show characteristics did not reach statistical significance against scheduling dimensions.
- [[practice-management/khries-2024-identifying-barriers-pediatric-dental-appointments]] — pediatric barrier taxonomy showing 44% non-attendance despite 85% insurance (cost ≠ driver); transport and staff-miscommunication as structural levers.
- [[practice-management/bhatia-2018-pediatric-dental-appointments-no-show-rates-reasons]] — pediatric 52% missed rate; the memory-reliance correlate, the reminder-preference hierarchy (dentist call > SMS), and the high-SES-highest-no-show paradox (carry the abstract-vs-table SES significance caveat).
- [[practice-management/samohyl-2021-non-attendance-dental-preventive-care-students]] — the intergenerational mechanism: parental avoidance independently predicts the adolescent's non-attendance (mother AOR 4.19 / father AOR 3.41), reframing no-show as a family/health-behavior trait rather than an individual patient failing.
- [[practice-management/prasad-2012-sms-reminder-dental-attendance-rct]] — the reminder-works RCT: SMS vs no reminder raised on-time attendance 79.2% vs 35.5%, supplying the intervention-efficacy evidence the factor studies lack.
- [[practice-management/nelson-2011-text-vs-voice-reminder-pediatric-dental-rct]] — the channel-comparison RCT: voice reminders beat SMS (OR 2.12), qualifying a blanket "send an SMS" recommendation and converging with the patient preference for a dentist call.
- [[behavioral-dentistry/communication-relationship/currie-2021-promoting-regular-dental-attendance-problem]] — the scope boundary and the highest-grade attendance evidence the wiki holds: an eight-database SR finding only 3 irreproducible studies on converting problem-orientated (pain-only) attenders, which is why the reminder/slot ladder cannot be sold as a fix for irregular attendance.
- [[behavioral-dentistry/communication-relationship/okyere-boadu-2025-patient-challenges-dental-care-ghana]] — the payment-context boundary on "cost is not the driver": without coverage, cost and appointment availability were named by 100% of barrier-affected patients, plus a cost→delay→worse-disease→higher-cost cascade and the in-visit communication (40.2%) / transparency (20.7%) barriers.

## Related Overviews

- [[overviews/patient-recall-retention-overview]] — the parent operating system: places this page's factor analysis as "layer 2" (making a booked visit happen) alongside risk-based recall intervals (layer 1) and the near-empty motivation literature (layer 3). Read that page for the recall-interval decisions this one deliberately does not cover.
- [[overviews/behavioral-dentistry-decision-ladder]] — the behaviour-change axis behind Currie's four design targets (motivational interviewing stratification, communication-skill framework).
