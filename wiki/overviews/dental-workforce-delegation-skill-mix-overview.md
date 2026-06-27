---
title: "Overview: Dental Workforce Delegation & Skill-Mix"
type: synthesis
category: overviews
date: 2026-06-27
confidence: synthesis
source_collection: synthesis
source_papers:
  - wiki/practice-management/chen-2024-dental-hygienist-autonomy-care-utilization.md
  - wiki/practice-management/bozia-2021-dental-hygienist-scope-practice-radiology.md
  - wiki/practice-management/vu-2024-caregivers-perceptions-dental-therapists.md
tags: [workforce, skill-mix, delegation, dental-hygienist, dental-therapist, scope-of-practice, practice-management, overview]
---

> [!summary] 한국어 핵심요약
> - **핵심 주장**: 치과 보조인력(dental hygienist, DH / dental therapist, DT)에게 업무를 위임(delegation)·기능배분(skill-mix)하면 특히 의료취약지(provider-shortage area)에서 접근성(access)이 늘지만, 자율성 수준은 "용량"처럼 작용해 트레이드오프(trade-off)를 동반한다 — 적정량은 예방을 늘리고 과량은 치료 이용을 줄인다.
> - **비단조성(non-monotonic) 핵심 근거**: Chen 2024(MEPS 2001–2014, 이중차분 difference-in-differences)는 *중간(moderate)* 수준의 DH 자율성은 예방치료(preventive care) 증가로 전체 방문을 늘리지만, *최고(highest)* 수준 자율성은 치료(treatment) 이용을 줄인다고 보고. 단순한 "자율성↑ = 진료↑" 프레임으로는 놓치는 패턴.
> - **취약지 레버리지**: Chen 2024의 두 효과(예방↑·치료↓) 모두 치과의료 취약지에서 더 크게 나타났고, 방문·업무가 DH 쪽으로 재배분됨 — 위임은 접근성 격차 도구로서 가장 큰 효과를 취약지에서 낸다.
> - **규제는 국가·관할권마다 천차만별**: Bozia 2021(전 세계 단면조사, 31개국 중 26개국 응답, 응답률 84%) — DH의 구내 방사선촬영(intraoral radiography)을 78%의 국가가 허용하나, 42%는 치과의사 의뢰(referral) 선행을 요구, 46%는 DH의 방사선 진단(radiographic diagnosis)을 금지, 27%만 장비 단독 소유 허용.
> - **부분 위임이 표준**: "촬영은 되지만 진단·의뢰·소유는 제한"처럼 한 업무 안에서도 권한이 쪼개진다. 촬영+의뢰+진단+소유 4가지 전부 허용은 5개국(19%)뿐.
> - **관할권 내 변동**: 미국 50개 주·캐나다 주(province)처럼 연방국가는 같은 나라 안에서도 주별로 DH 범위가 다름 — "국가 단위"로 단정할 수 없음.
> - **Bozia 수치 주의(caveat)**: 초록(abstract)은 촬영 78%·진단금지 46%로, 본문(body)은 촬영 77%·진단가능 50%로 보고하는 경미한 불일치가 있다. 본 종합은 초록 수치를 주로 인용하되 이 불일치를 명시한다.
> - **대중 수용은 존재하되 조건부**: Vu 2024(단면조사, 보호자 caregiver n=202) — 보호자들은 DT가 유치·영구치 수복, 유치 발치, 응급처치를 수행하는 데 수용적(여럿 p<0.001)이나, 그 시술이 치과의사 감독(dentist supervision) 하에 이뤄져야 한다는 데 강하게 동의(p<0.001).
> - **인지도 격차**: Vu 2024는 DT의 교육·업무범위·인력통합에 대한 대중 인식이 낮아 공개 홍보(public awareness)가 필요하다고 지적 — 위임 확대의 사회적 전제조건.
> - **임상·운영 시사점**: ① 위임은 예방업무부터, 자율성은 적정선까지(과도한 자율성은 치료접근 저하 위험), ② 취약지에 우선 배치, ③ 감독구조 명시는 임상 안전이자 환자 신뢰 요건, ④ 우리 관할권의 실제 법적 범위를 먼저 확인(국가·주별 상이), ⑤ DT/DH 역할에 대한 환자 커뮤니케이션을 병행. 한국 맥락의 규제 경계는 [[practice-management/ha-2023-dentist-issues-constitutional-court-decisions]] 참조.

## One-line Summary

Across an econometric difference-in-differences study (Chen 2024), a worldwide regulatory survey (Bozia 2021), and a caregiver-acceptance survey (Vu 2024), delegating tasks to dental auxiliaries (hygienists, therapists) expands access — most in provider-shortage areas — but the autonomy level behaves like a dose with a trade-off (moderate autonomy raises preventive care, the highest autonomy lowers treatment use), scope is regulated very differently across jurisdictions (and even within federal countries), and public acceptance exists but is conditional on dentist supervision.

## 한줄요약

세 편(이중차분 경제학 연구 Chen 2024, 전 세계 규제 단면조사 Bozia 2021, 보호자 수용도 조사 Vu 2024)을 종합하면, 치과 보조인력(DH·DT)에 대한 업무위임은 특히 취약지에서 접근성을 늘리지만 자율성 수준은 트레이드오프를 동반하고(적정=예방↑, 최고=치료↓), 업무범위 규제는 관할권마다(연방국가는 주별로도) 크게 다르며, 대중 수용은 존재하되 치과의사 감독을 조건으로 한다.

## Thesis

The three papers triangulate a single workforce question — *what happens when tasks move from the dentist to auxiliary providers (dental hygienists, DH; dental therapists, DT)?* — from three non-overlapping angles: utilization economics, regulatory mapping, and public acceptance. Read together they support one thesis with three qualifications:

**Delegation expands access, but it is dose-dependent, jurisdiction-bound, and acceptance-conditional.**

1. **Dose-dependent (Chen 2024).** Autonomy is not a monotonic "more is better" lever. A *moderate* increase in hygienist autonomy raises total dental visits by increasing preventive care, while the *highest* autonomy tier is associated with a *decrease* in dental treatment utilization. Both effects are larger in provider-shortage areas, where visits and tasks reallocate toward hygienists. So the access dividend is real, but pushing autonomy to its maximum can erode the treatment side of utilization.

2. **Jurisdiction-bound (Bozia 2021).** The legal authority to perform even a single delegated task — oral radiography — varies enormously: 78% of surveyed countries permit DHs to take intraoral radiographs, but 42% require a dentist referral first, 46% bar DHs from radiographic diagnosis, and only 27% allow DHs to independently own equipment. Authority is split *within* a task (taking ≠ indicating ≠ diagnosing ≠ owning), and within federal countries it differs by state/province. Any delegation plan is only as real as the local statute.

3. **Acceptance-conditional (Vu 2024).** Caregivers are receptive to midlevel DTs performing restorations, primary-tooth extractions, and emergency care (several associations p<0.001), but both informed and uninformed respondents strongly agree (p<0.001) those procedures should occur under dentist supervision — and public awareness of DT education and scope is low. Social licence for delegation is present but tethered to supervision and contingent on communication.

## Evidence Map

| Paper | Design | n | Key finding | Confidence |
|---|---|---|---|---|
| [[practice-management/chen-2024-dental-hygienist-autonomy-care-utilization]] | Difference-in-differences on MEPS 2001–2014, DHPPI-coded state regulation | National U.S. survey panel (MEPS) | Non-monotonic: *moderate* DH autonomy → ↑ total visits via ↑ preventive care; *highest* autonomy → ↓ treatment use; both effects larger in provider-shortage areas; tasks/visits shift to hygienists | retrospective (abstract-only; effect sizes/CIs not retrieved) |
| [[practice-management/bozia-2021-dental-hygienist-scope-practice-radiology]] | Worldwide cross-sectional survey (27-item questionnaire to IFDH/EDHF associations) | 26/31 countries responding (84%) | 78% permit DHs to take intraoral radiographs; 42% require dentist referral; 46% bar DH radiographic diagnosis; 27% allow DH equipment ownership; full task set in 5 countries (19%); scope varies by country and by state/province | cross-sectional (descriptive only) |
| [[practice-management/vu-2024-caregivers-perceptions-dental-therapists]] | Cross-sectional caregiver survey (validated DT-integration instrument), urban teaching hospital | 202 caregivers | Receptive to DT-performed primary/permanent restorations, primary extractions, emergency care (several p<0.001); strong agreement procedures be under dentist supervision (p<0.001); public-awareness gap | cross-sectional (abstract-only) |

*Caveat on Bozia 2021:* the abstract and body disagree slightly — abstract reports 78% take / 46% may-not-diagnose, body reports 77% take / 50% may-diagnose. The table and bullets above quote the abstract figures; treat the take-rate as ~77–78% and the diagnosis-bar as ~46–50%.

## Clinical Decision Points

- **What to delegate first.** The cleanest access gain in Chen 2024 comes through *preventive* care (cleanings, exams) routed to hygienists, and Bozia 2021 shows oral *radiography* is widely (≈77–78% of countries) a delegable task. Start delegation with preventive and diagnostic-support tasks where the evidence and the regulatory permission are strongest; reserve operative/surgical tasks for where local statute and supervision allow (cf. the DT restoration/extraction items in Vu 2024).
- **Autonomy-level trade-off (dose, not switch).** Treat autonomy as a tunable dose. Moderate hygienist autonomy buys more preventive visits; maximal autonomy is associated with *reduced* treatment utilization (Chen 2024). Calibrate scope expansion to a level that adds prevention without detaching patients from needed dentist-delivered treatment.
- **Supervision requirement.** Public acceptance is explicitly conditional: caregivers want DT procedures done under dentist supervision (p<0.001, Vu 2024), and many jurisdictions already encode this — e.g., 42% of countries require a dentist referral before a DH radiograph and 46% bar DH radiographic diagnosis (Bozia 2021). Build an explicit supervision/referral structure into any delegation model; it is simultaneously a patient-trust and a regulatory requirement.
- **Shortage-area leverage.** The utilization effects of DH autonomy are *larger* in provider-shortage areas, where care reallocates to hygienists (Chen 2024). Direct delegation capacity toward underserved/shortage settings, where it yields the greatest marginal access.
- **Public-communication need.** Awareness of midlevel-provider education and scope is low (Vu 2024). Pair any skill-mix expansion with patient-facing communication explaining who the auxiliary is, what they are trained and licensed to do, and the supervising dentist's role.
- **Verify your own jurisdiction first.** Scope is not uniform across or even within countries (Bozia 2021 documents state/province variation in the US, Canada, Switzerland, Australia). Confirm the exact legal scope in your jurisdiction before designing a delegation workflow — for the Korean regulatory boundary, see [[practice-management/ha-2023-dentist-issues-constitutional-court-decisions]].

## Gaps & Future Research

- **Effect sizes are missing.** Chen 2024 and Vu 2024 are ingested abstract-only — point estimates, confidence intervals, and the mechanism behind the *highest-autonomy → less treatment* counter-effect (substitution? referral friction? measurement?) are not captured. Full-text extraction is needed to quantify the dose-response curve.
- **Quality vs. quantity of care.** All three papers address *whether* and *how much* care is delivered under delegation; none in this set measures clinical *outcomes* or safety of auxiliary-delivered procedures. The trade-off analysis needs outcome data, not just utilization counts.
- **Dental therapists vs. dental hygienists.** Chen and Bozia concern DH scope; Vu concerns DT acceptance. Evidence on DT *utilization and outcomes* (not just perceptions) is thin here.
- **Caregiver vs. patient, pediatric vs. adult.** Vu 2024 samples caregivers of pediatric medical patients at one urban teaching hospital — generalizability to adult patients, other settings, and self-deciding patients is unestablished.
- **Bozia reporting discrepancy.** The abstract-vs-body mismatch (take 77 vs 78%, diagnosis-bar 46 vs 50%) is unresolved without the underlying dataset; future syntheses should source the primary tables.
- **Korea-specific data.** None of the three papers is Korean (Korea did not respond to the Bozia survey). The interaction of these international findings with Korean constitutional scope-of-practice jurisprudence is an open question — see [[practice-management/ha-2023-dentist-issues-constitutional-court-decisions]].

## Related Papers

- [[practice-management/chen-2024-dental-hygienist-autonomy-care-utilization]] — utilization-economics evidence: the dose-dependent, shortage-amplified effect of DH autonomy on care volume and mix.
- [[practice-management/bozia-2021-dental-hygienist-scope-practice-radiology]] — regulatory map: how one delegated task (oral radiography) is legally split and varies across 26 jurisdictions.
- [[practice-management/vu-2024-caregivers-perceptions-dental-therapists]] — public-acceptance side: caregiver receptivity to midlevel DTs, conditional on dentist supervision.
- [[practice-management/ha-2023-dentist-issues-constitutional-court-decisions]] — regulatory framing: Korean constitutional jurisprudence on who may deliver dental care; the legal-boundary counterpart to the workforce-delegation evidence synthesized here.
