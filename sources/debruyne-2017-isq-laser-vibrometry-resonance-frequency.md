---
title: "ISQ calculation evaluation of in vitro laser scanning vibrometry-captured resonance frequency"
authors: Stijn Debruyne, Nicolas Grognard, Gino Verleye, Korneel Van Massenhove, Dimitrios Mavreas, Bart Vande Vannet
year: 2017
doi: 10.1186/s40729-017-0105-3
category: [implants/isq]
pdf_path: /Users/oracleneo/llm-wiki/papers/debruyne-2017-isq-laser-vibrometry-resonance-frequency.pdf
pdf_filename: debruyne-2017-isq-laser-vibrometry-resonance-frequency.pdf
source_collection: external
---

## Why Ingested

ISQ는 Osstell 기기가 측정 공명주파수(Resonance Frequency, RF)를 비공개 다항식 계수(a,b,c,d,e)로 변환해 산출하는데, 이 변환 알고리즘 자체가 옳은지 독립적으로 검증된 적이 없었다. 본 in-vitro 연구는 레이저 도플러 진동측정법(Laser Doppler Vibrometry, LDV)으로 RF를 독립 포착한 뒤 Osstell 알고리즘으로 ISQ를 역산하여 기기 직접 측정값과 비교(r=0.99)함으로써 그 알고리즘의 정확성을 확인한다. 이는 [[implants/isq/bhandarkar-2023-rfa-mathematical-modeling-implant-stability]]의 RFA 수학적 모델링을 실험적으로 보강하고, [[implants/isq/herrero-climent-2013-osstell-isq-reliability-icc]]의 ISQ 신뢰도(reliability) 논의에 측정 변환 단계의 타당도(validity) 근거를 더한다.

## One-line Summary

In-vitro study (20 resin-imbedded test implants; Straumann TL, Ankylos, 3i Certain) capturing resonance frequency by laser Doppler vibrometry and recomputing ISQ with the Osstell algorithm — indirect (LDV-derived) vs direct (Osstell IDx) ISQ correlated at r=0.99 with a clinically negligible mean difference (~0.09–0.54 ISQ units), validating the Osstell ISQ calculation algorithm.

## 한줄요약

시험관내(in-vitro) 연구 — 레진에 매립한 시험 임플란트 20개(스트라우만 TL·앵킬로스·3i Certain)를 레이저 도플러 진동측정법(LDV)으로 공명주파수를 잡아 Osstell 알고리즘으로 ISQ를 역산한 결과, 기기 직접측정 ISQ와 r=0.99로 일치하고 평균차도 임상적으로 무시할 수준(~0.09~0.54 ISQ)이어서 Osstell의 ISQ 산출 알고리즘이 타당함을 확인.

## 1. Document Information

- **Title**: ISQ calculation evaluation of in vitro laser scanning vibrometry-captured resonance frequency
- **Authors**: Stijn Debruyne, Nicolas Grognard, Gino Verleye, Korneel Van Massenhove, Dimitrios Mavreas, Bart Vande Vannet
- **Journal**: International Journal of Implant Dentistry, 2017;3:44
- **DOI**: 10.1186/s40729-017-0105-3
- **Year**: 2017 (received 11 April 2017, accepted 28 September 2017)
- **Study type**: in-vitro (laboratory bench study)
- **Affiliations**: Katholieke Hoge School Brugge-Oostende (Mechanics); Kliniek Royal, Ostend; Vrije Universiteit Brussel (Orthodontics); Ghent University

## 2. Key Contributions

1. **Independent validation of the proprietary Osstell ISQ algorithm.** The Osstell ISQ value is computed from a measured maximum resonance frequency (RF) via a confidential 4th-order polynomial `ISQ = e·f⁴ + d·f³ + c·f² + b·f + a` whose coefficients (a–e) are Osstell trade secrets. This study is the first to capture RF by a fully independent method (laser Doppler vibrometry) and feed it through that same algorithm to check whether the resulting ISQ matches the device's own output.
2. **Establishes a reproducible laboratory RFA platform.** A bench method combining resin-imbedded implants + Osstell IDx electromagnetic excitation + non-contact LDV detection + FFT signal processing is engineered as a future tool to isolate and study the implant–Smartpeg complex stiffness, which is normally confounded by bone and bone–implant stiffness in clinical RFA.
3. **Confirms cross-device ISQ bias.** Reinforces prior reports that older wired Osstell devices underestimate ISQ relative to Osstell Mentor/IDx (~9 ISQ clinical difference, ~10 ISQ cadaver difference), meaning ISQ values across device generations cannot be pooled without correction in systematic reviews.

## 3. Methodology and Architecture

- **Test implants (3 systems):** Straumann SLA tissue-level (RN 3.3×12, RN 3.3×4.1, WN 4.8×8), Ankylos Cell Plus B-type (4.5×8, 4.5×9.5), Biomet 3i Full Osseotite Tapered Certain (4.0×13).
- **Imbedding:** implants set in Duromod B dual-component polyurethane resin in a bar-shaped silicon mould (16×2.5×3 cm), 5 implants per bar, system-specific mounts for correct vertical positioning. Full coronal imbedding simulates total osseointegration; partial imbedding (concept) allows separating implant vs Smartpeg deflection.
- **Smartpeg:** fresh system-specific Smartpeg torqued to 8 Ncm (Straumann #04, Ankylos #16, 3i #15).
- **Excitation:** Osstell IDx cabled probe positioned at the coronal Smartpeg by a fixed stand; identical probe position used for both indirect and direct recordings.
- **Indirect (LDV) measurement:** portable laser vibrometer (Polytec PDV 100, class 2, λ=640 nm; range 20 mm/s, sensitivity 5 mm/s) aimed at a flat face of the Smartpeg hexagon. Output → ADC/frontend (Brüel & Kjær 3160-A-4/2) → Pulse Labshop software; speed v(t) converted to RF via autospectrum. Measurement window 31.25 ms; FFT span 0–12.58 kHz, 400 intervals → 32 Hz resolution. Each session averaged 1000 measurements; done in fivefold, mean fed into the Osstell algorithm.
- **Direct measurement:** Osstell IDx device ISQ read off the display at the same probe position.
- **Counts:** per implant configuration, 25 indirect + 5 direct measurements.
- **Statistics (SPSS 22.0):** Shapiro-Wilk (normality), paired t-test + Wilcoxon signed-rank (agreement), Pearson r (linear correlation); α=0.05.

## 4. Key Results and Benchmarks

- **Correlation:** Pearson r = 0.990 (p < 0.001) between indirect (LDV-derived) and direct (IDx) ISQ — abstract reports r = 0.99 for the tested systems.
- **Agreement:** mean indirect ISQ ~0.535 units higher than direct; NOT significantly different from 0 (paired t = 2.018, df = 19, p = 0.058; Wilcoxon Z = 1.867, p = 0.062). Abstract cites a "clinically rejectable" mean difference of 0.09 ISQ units.
- **Distribution:** both ISQ datasets non-normal (Shapiro-Wilk indirect p = 0.05, direct p = 0.02), negatively skewed.
- **Representative Table 2 values (mean indirect ISQ / mean direct ISQ):** Ankylos 4.5×9.5 ≈ 85–89 / 85–90; Straumann 3.3×12 ≈ 64.5–65.6 / 64–65; Straumann 4.1×10 ≈ 79.6–80.0 / 80; Straumann 4.8×8 ≈ 77.2–80.7 / 75–79. RF ranged ~5.0 kHz (low-ISQ Straumann) to ~8.6 kHz (high-ISQ Ankylos).
- **Conclusion:** the Osstell ISQ-calculation algorithm is correct; the bench method is valid for future implant–Smartpeg stiffness research. Clinically, it adds proof that ISQ from older (wired) Osstell devices is biased/underestimated (at least for Straumann TL SLA implants), so cross-device ISQ comparisons need correction.

## 5. Limitations and Future Work

- **In-vitro only.** Implants imbedded in homogeneous polyurethane resin, not bone — surrounding-bone and bone–implant stiffness (two of the three RFA stiffness entities) are deliberately held constant, so the study validates the measurement/calculation chain, not clinical bone behavior.
- **Algorithm coefficients undisclosed.** The Osstell polynomial coefficients (a–e) were supplied under a no-publication agreement, so the validation is reproducible only with proprietary access; the formula itself cannot be independently re-derived from the paper.
- **Small sample / non-normal data.** n = 20 implant configurations in the agreement analysis; ISQ distributions were non-normal.
- **Stated purpose is enabling future work**, not yet executing the implant–Smartpeg stiffness study the platform is built for (partial-imbedding deflection separation is presented only as a concept, Fig. 1).

## 6. Related Work

- Meredith et al. (1997) — origin of resonance frequency analysis for implant stability (rabbit tibia; quantitative implant–tissue interface).
- Valderrama et al. (2007) — clinical trial showing ~9 ISQ difference between two RFA devices.
- Tözüm et al. (2010) — human cadaver study, ~10 ISQ difference between Osstell device generations.
- Barewal, Bischof, Huwiler, Han, Bornstein, Guler — clinical secondary-stability ISQ datasets for Straumann TL RN SLA implants (Table 1), illustrating wired-vs-Mentor device divergence.

## 7. Glossary

- **ISQ (Implant Stability Quotient):** unitless 0–100 index of implant stability derived from resonance frequency via the Osstell algorithm.
- **RFA (Resonance Frequency Analysis):** non-invasive implant stability test based on the resonance frequency of an excited transducer mounted on the implant.
- **RF (Resonance Frequency):** the natural vibration frequency (kHz) of the implant–Smartpeg complex; the raw input to the ISQ formula.
- **Smartpeg:** small aluminium transducer rod (screw + hexagon + magnet) screwed into the implant; vibrated by the Osstell device's electromagnetic pulses.
- **Osstell IDx / Mentor:** commercial RFA devices; both use the same ISQ-calculation algorithm. Older wired Osstell devices used a different scale and yield lower ISQ.
- **Laser Doppler Vibrometry (LDV):** non-contact optical method measuring surface vibration velocity via the Doppler phase shift of a backscattered laser beam.
- **FFT (Fast Fourier Transformation):** time-domain v(t) → frequency-domain spectrum conversion; autospectrum used here to extract the maximum RF.
