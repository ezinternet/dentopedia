---
title: "Comparison and ranking of interventions for temporomandibular disorders-myofascial pain syndrome: a Bayesian network meta-analysis based on randomized controlled trials"
authors: "Ma et al."
year: 2026
date: 2026-04-20
doi: "10.1186/s12903-026-08373-9"
source: ma-2026-comparison-ranking-interventions-tmd.md
category: [tmj]
confidence: sr+ma
source_collection: pubmed-text
full_text: true
pmid: "42010612"
pmcid: "PMC13270680"
text_path: /Users/oracleneo/llm-wiki/papers/ma-2026-comparison-ranking-interventions-tmd.txt
text_filename: ma-2026-comparison-ranking-interventions-tmd.txt
tags: [tmd-mps, myofascial-pain, network-meta-analysis, lidocaine-injection, ischemic-compression, prp, botulinum-toxin, sucra, cinema]
relations:
  - type: extends
    target: haggman-henrikson-2017-pharmacological-orofacial-pain-sr-ma
  - type: refines
    target: saini-2024-botulinum-toxin-tmd-sr-ma
  - type: applies-to
    target: menendez-torre-2023-dry-needling-vs-manual-therapy-tmd-nma
---

## Three-line Summary

Bayesian random-effects NMA (PROSPERO-registered) of 14 RCTs (n=674 adults with TMD-myofascial pain syndrome, 14 intervention nodes vs basic treatment), Chinese authorship (Gansu University of Chinese Medicine); English-language RCTs published through June 2025.

Lidocaine injection (SUCRA 91.7%) and ischemic compression (88.7%) ranked highest for short-term pain relief; PRP and laser therapy also significantly beat basic treatment; oral muscle relaxant pharmacotherapy did not show significant additional benefit; BTX injection crossed the null.

Certainty of evidence for the top two interventions was very low (CINeMA) due to network sparsity (5/14 nodes single-trial, no direct RCT vs basic treatment) and high risk of bias in 9/14 trials — rankings should generate hypotheses, not drive treatment-pathway priority.

## 세줄요약

PROSPERO 등록 베이지안 랜덤효과 네트워크 메타분석 (14 RCT, TMD 근막통증증후군 성인 674명, 14개 중재 노드 vs 기본치료, 간쑤중의약대학 저자팀): 2025년 6월까지 영어 RCT 포함.

리도카인 주사(SUCRA 91.7%)·허혈성압박(88.7%)이 단기 통증 완화 순위 1·2위; PRP·레이저도 기본치료 대비 유의; 경구 근이완제는 추가 효과 없음; 보툴리눔 독소는 신뢰구간이 영점을 포함.

상위 2개 중재의 CINeMA 확실성은 매우낮음 — 네트워크 희박성(단일 시험 노드 5/14개, 기본치료와 직접 비교 RCT 없음)과 14편 중 9편의 고위험 편향이 원인; 이 순위는 우선 RCT 가설 생성용이지 치료 경로 결정 근거가 아님.

## Summary

This Bayesian network meta-analysis, authored entirely by a team from Gansu University of Chinese Medicine (China), synthesizes 14 RCTs (674 adults) comparing 14 distinct intervention categories for temporomandibular disorder–myofascial pain syndrome (TMD-MPS): physical therapies (laser, TENS, manual therapy), appliance-based therapies (bite plate, oral appliance), and pharmacological/injection therapies (lidocaine injection, muscle-relaxant pharmacotherapy, platelet-rich plasma, botulinum toxin injection), plus acupuncture and biofeedback, against a pooled "basic treatment" (BT) reference node (sham/placebo + minimal conservative pharmacotherapy). Lidocaine injection and ischemic compression topped the SUCRA rankings for short-term (0–4 week) analgesia, but the paper is notably self-critical: it explicitly downgrades these top two interventions to "very low" certainty via CINeMA because neither has ever been directly compared to BT in a trial — their apparent superiority rests entirely on indirect evidence through a sparse network, and 9 of 14 included trials carried high risk of bias. This makes the paper as much a methodological caution against over-reading NMA rankings as it is a positive-findings paper.

## Key Contributions

- Extends TMD pharmacotherapy evidence from oral drugs (NSAIDs, muscle relaxants — covered by [[tmj/haggman-henrikson-2017-pharmacological-orofacial-pain-sr-ma]]) into the injectable/procedural domain (lidocaine injection, PRP, botulinum toxin injection), ranked head-to-head against physical and appliance therapies within a single coherent network.
- Demonstrates a "muscle relaxant pharmacotherapy" node showed no significant advantage over the BT reference (which itself already includes minimal conservative pharmacotherapy) — i.e., escalating from minimal to full-dose oral muscle relaxants did not show NMA-detectable extra benefit in this evidence set.
- Rigorously applies CINeMA on top of SUCRA, providing a model of how to report NMA rankings without overstating clinical certainty — directly useful for reading other TMD NMA pages in this wiki with appropriate skepticism.
- Transparently reports that planned sensitivity analyses (excluding high-RoB studies; varying BT composition) could not be run because the network was too sparse — an explicit limitation rather than a suppressed one.

## Methodology

- Design: Bayesian random-effects network meta-analysis (gemtc/rjags, R 4.4.0); PRISMA-NMA reported; PROSPERO-registered (CRD420251070432).
- Search: PubMed, Embase, Cochrane Library, Web of Science, inception–June 2025; English-language RCTs only; no grey literature.
- Population: adults ≥18y, DC/TMD (or equivalent clinical/trigger-point) diagnosis of TMD-MPS.
- 14 intervention nodes vs. BT reference (pooled sham/placebo + minimal conservative pharmacotherapy): laser treatment, bite plate, oral appliance, lidocaine injection, acupuncture, TENS, biofeedback, manual therapy, muscle-relaxant pharmacotherapy, ischemic compression, botulinum toxin injection, platelet-rich plasma, oral appliance+lidocaine injection.
- Primary outcome: change in pain intensity (VAS/NRS) at 0–4 weeks post-treatment, as SMD (95% CrI).
- Quality: Cochrane RoB 2 (5 domains); certainty via CINeMA (6 domains, high/moderate/low/very low).

## Results

- 14 RCTs, n=674, from Iran, Turkey, Italy, Brazil, Sweden, Spain, Poland, Lithuania (2010–2024); >70% female in most trials; RoB 2 — 9/14 high risk, 5/14 some concerns, 0 low risk.
- Statistically significant vs. BT (SMD, 95% CrI): lidocaine injection −2.37 (−3.67, −0.90); ischemic compression −2.21 (−3.63, −0.75); PRP −1.45 (−2.21, −0.56); laser therapy −0.91 (−1.58, −0.13). Not significant vs. BT: bite plate, oral appliance, oral appliance+lidocaine injection, acupuncture, TENS, manual therapy, muscle-relaxant pharmacotherapy, botulinum toxin injection, biofeedback.
- SUCRA: lidocaine injection 91.7% > ischemic compression 88.7% > PRP 68.6% > TENS 67.5% > oral appliance+lidocaine injection 66.6% > botulinum toxin injection 66.5% ... BT 10.7%, biofeedback 11.2% lowest.
- CINeMA certainty: laser therapy and PRP = Low (single small RCT each, n=41/n=58); lidocaine injection, ischemic compression, TENS, oral appliance+lidocaine, botulinum toxin injection = Very low (no direct trial vs. BT and/or null-crossing CrI and/or high RoB).
- No significant node-splitting inconsistency detected; convergence diagnostics acceptable (PSRF mostly <1.20).
- Authors' explicit caution: lidocaine injection and ischemic compression's top rankings should generate hypotheses for priority head-to-head RCTs, **not** be translated directly into treatment-pathway priority.

## Related Papers

- [[tmj/haggman-henrikson-2017-pharmacological-orofacial-pain-sr-ma]] — extends: that NMA covers oral pharmacotherapy (NSAIDs, cyclobenzaprine, clonazepam) for TMD/BMS broadly; this paper covers injectable/procedural pharmacotherapy specifically for the myofascial-pain subtype, and adds a "muscle relaxant pharmacotherapy" node showing no added benefit over minimal conservative treatment.
- [[tmj/saini-2024-botulinum-toxin-tmd-sr-ma]] and [[tmj/zhu-2020-btx-painful-tmd-sr-ma]] — refines: those standalone BTX SR+MAs report significant pain benefit; this NMA's BTI-vs-BT comparison crosses the null (very low certainty), a more conservative estimate once compared within a broader intervention network with correct uncertainty propagation.
- [[tmj/menendez-torre-2023-dry-needling-vs-manual-therapy-tmd-nma]] — applies-to: both are TMD NMAs; this paper's acupuncture/manual-therapy/TENS nodes provide a complementary non-injectable comparison set within the same MPS-focused evidence pool.
- [[overviews/tmd-management-evidence-ladder]] — axis 3 (pharmacotherapy) and axis 2 (non-pharmacological conservative care): this paper's sparse-network/very-low-certainty top rankings reinforce the overview's general caution that most TMD intervention pooled estimates should be read as hypothesis-generating rather than decisive, echoing the Fuentes-Barría 2026 interpretability caveat already logged there for arthrocentesis meta-analyses.
