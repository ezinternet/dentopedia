---
title: "A Comparative Investigation of the Quality of Radiographs Produced by Portable Handheld and Fixed X-Ray Units"
authors: Débora Costa Ruiz, Matheus L. Oliveira, Rocharles Cavalcante Fontenele, Deborah Queiroz Freitas, Francisco Haiter-Neto
year: 2025
doi: 10.1590/0103-644020256319
category: [radiology]
source_collection: pubmed-text
full_text: true
pmid: "41172496"
pmcid: "PMC12551989"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12551989/
text_path: /Users/oracleneo/llm-wiki/papers/ruiz-2025-handheld-fixed-xray-image-quality-comparison.txt
text_filename: ruiz-2025-handheld-fixed-xray-image-quality-comparison.txt
---

## Why Ingested

[[radiology/geibel-2025-mobile-handheld-radiography-quality-nursing-home]] evaluates real-world clinical-quality-criteria outcomes for portable/handheld dental radiography in a nursing-home population; this paper adds the complementary controlled, objective in-vitro benchmark (ImageJ gray-value analysis of brightness, noise, uniformity, contrast) isolating equipment-intrinsic effects (handheld vs fixed, platform-mounted to eliminate hand-movement variability) across two CMOS sensor systems. Together they let the wiki distinguish "does handheld radiography look diagnostically acceptable in practice" from "what specifically differs at the pixel/gray-value level and why."

## Three-line Summary

In-vitro comparative study (acrylic block + aluminum step-wedge, 2 CMOS sensor systems, 6 exposures/condition) found handheld portable intraoral X-ray equipment produced significantly higher brightness and lower contrast than fixed equipment regardless of sensor (p<0.0001), sensor-dependent noise effects (p<0.05), and no significant uniformity difference (p>0.05).

(incomplete)

(incomplete)

## 세줄요약

체외(in-vitro) 비교연구(아크릴 블록 + 알루미늄 스텝웨지, CMOS 센서 2종, 조건당 6회 촬영)에서 휴대형(handheld) 구강내 X선 장비는 센서 종류와 무관하게 고정형(fixed) 장비보다 밝기(brightness)는 유의하게 높고 대비(contrast)는 유의하게 낮았으며(p<0.0001), 노이즈(noise) 영향은 센서에 따라 달랐고(p<0.05) 균일도(uniformity)는 유의한 차이가 없었다(p>0.05).

(incomplete)

(incomplete)

## 1. Document Information

- Journal: Brazilian Dental Journal, volume 36, e236319 (2025)
- Article type: original research (in-vitro comparative study)
- Retrieved via PubMed Central full text (PMC12551989); no PDF artifact retained per Step 1-T pathway
- Funding source / conflicts of interest: not stated in the retrieved text excerpt

## 2. Key Contributions

- First objective, ImageJ-based gray-value quantification (rather than subjective/examiner-rated assessment) comparing handheld portable vs fixed intraoral X-ray equipment across two different CMOS sensor systems (Digora Toto, Snapshot).
- Isolates equipment-intrinsic image-quality effects from operator hand-movement/fatigue by mounting the handheld unit on a stable platform — a methodological control not present in prior subjective-evaluation studies.
- Demonstrates that noise direction (increase vs decrease with handheld equipment) is sensor-dependent, implicating CMOS sensor sensitivity, image-processing algorithms, scintillator materials, and detector electronics as interacting variables rather than handheld equipment having a uniform noise effect.
- Provides step-wedge-based objective contrast quantification (% contrast variation formula) as a reusable method for future handheld-vs-fixed comparisons.
- Explicitly reconciles statistically significant objective differences with the clinical literature showing no compromise in caries diagnostic accuracy, framing the gap between statistical and clinical significance.

## 3. Methodology and Architecture

- **Design**: in-vitro experimental comparative study, no human/animal subjects.
- **Equipment compared**: Eagle X-ray handheld portable unit (Alliage, Sao Paulo, Brazil), 60 kVp / 2.5 mA / 0.45 s, mounted on a stable platform to remove hand-movement variability; vs Focus fixed intraoral X-ray unit (Instrumentarium, Tuusula, Finland), 60 kVp / 7 mA / 0.16 s. Exposure times were pilot-selected by two dentomaxillofacial radiologists (5 years' experience) to yield closely matched mAs products (1.125 mAs handheld vs 1.12 mAs fixed).
- **Sensors**: size-2 CMOS (Digora Toto system, Scanora software, Soredex) and size-1 CMOS (SnapShot system, Cliniview software, Instrumentarium Imaging), tested separately.
- **Brightness/noise/uniformity phantom**: 30 x 40 x 30 mm acrylic block; 6 radiographs per sensor per equipment (24 total: 6 x 2 equipment x 2 systems). Images exported as 8-bit TIFF, analyzed in ImageJ (NIH). Brightness/noise from a central ROI covering 16% of radiograph area (mean and SD of gray values). Uniformity from a central 4x4 mm ROI plus four symmetric peripheral 4x4 mm ROIs, averaging their SDs; ROI placement standardized via ImageJ macros.
- **Contrast phantom**: aluminum step-wedge (6 steps, 2–12 mm thickness), same equipment/systems/parameters (24 radiographs total). A vertical centering line and horizontal dividing line were drawn; 4x4 mm ROIs placed on the 10 mm step (ROI1) and 4 mm step (ROI2); % contrast variation = (Mean ROI1 − Mean ROI2) / Mean ROI1 × 100.
- **Statistics**: Student's t-test, alpha = 5%, power analysis at 95% for all variables, SPSS 25.0.
- All exposures used a fully charged handheld unit (battery-charge-dependent tube-voltage drift was deliberately excluded as a variable, per prior literature on battery effects).

## 4. Key Results and Benchmarks

Mean ± SD by sensor and equipment:

- **Digora Toto**: brightness — handheld 65.41 (0.86) vs fixed 57.66 (1.04), p<0.0001; noise — handheld 14.48 (0.24) vs fixed 13.10 (0.27), p<0.0001 (handheld higher); uniformity — handheld 9.48 (0.23) vs fixed 9.53 (0.12), p=0.661 (NS); contrast — handheld 31.85% (0.04) vs fixed 32.99% (0.03), p<0.0001 (handheld lower).
- **Snapshot**: brightness — handheld 85.38 (0.19) vs fixed 68.95 (0.27), p<0.0001; noise — handheld 1.05 (0.02) vs fixed 1.12 (0.01), p=0.001 (handheld lower); uniformity — handheld 1.00 (0.08) vs fixed 1.03 (0.00), p=0.445 (NS); contrast — handheld 42.81% (0.18) vs fixed 47.69% (0.02), p<0.0001 (handheld lower).
- Summary pattern: handheld equipment → higher brightness and lower contrast vs fixed, regardless of sensor (both p<0.0001); noise effect direction is sensor-dependent (higher with Digora Toto, lower with Snapshot, both p<0.05); uniformity not significantly different for either sensor (p>0.05).
- No subgroup analyses beyond the two sensor systems (study design is a 2x2 equipment x sensor comparison, not a subgroup-stratified clinical study).

## 5. Limitations and Future Work

- In-vitro phantom study (acrylic block, aluminum step-wedge) — no anatomical structures or human subjects; authors note this was a deliberate choice to minimize variability from anatomical density/shape differences, consistent with prior gray-value-analysis methodology, but it limits direct extrapolation to diagnostic accuracy.
- Handheld unit was platform-mounted, not genuinely handheld — isolates equipment-intrinsic effects but excludes the real-world effect of operator hand movement/fatigue from supporting a 2.5–5 kg device through multiple exposures.
- All exposures used a fully charged handheld battery; battery-management effects during routine (non-fully-charged) clinical use were not evaluated, despite prior literature showing reduced tube voltage as battery charge decreases — flagged explicitly as needed future research.
- Only one exposure time/parameter set per equipment type was tested; effect of extended exposure time on relative image quality was not evaluated (proposed future work).
- Whether software-based brightness/contrast post-processing can compensate for the handheld equipment's inherent brightness/contrast profile was not tested (proposed future work).
- Diagnostic-outcome literature on handheld equipment remains concentrated on proximal caries detection; root resorption, root fracture, and periodontal bone loss diagnostic performance with handheld equipment remain understudied, so the clinical significance of the measured contrast/brightness/noise differences for those specific diagnostic tasks is not established by this or prior work.

## 6. Related Work

- Nitschke et al. (cited): used a subjective geometric-distortion evaluation (examiner assessment of periodontal ligament space, lamina dura, periradicular bone, alveolar crest, pulp chamber, root canals, dental crowns) and reported no meaningful handheld-vs-fixed differences; the present study's objective software-based gray-value analysis is framed as complementary rather than contradictory, each capturing a distinct dimension of radiographic quality.
- Prior literature (cited, unnamed in excerpt) on PSP-plate brightness increasing over prolonged use without compromising caries-lesion diagnosis, used to support the argument that statistically significant brightness/contrast/noise differences may not translate into clinically significant diagnostic differences.
- Prior diagnostic-outcome studies (cited, unnamed in excerpt) finding that radiographic diagnosis of proximal caries lesions was not compromised by handheld equipment despite gray-value differences.
- Prior battery-charge study (cited, unnamed in excerpt) showing reduced tube voltage as handheld-unit battery charge decreases, motivating the fully-charged-battery control condition here.

## 7. Glossary

- **CMOS sensor**: Complementary Metal-Oxide-Semiconductor digital radiographic image sensor.
- **ROI**: Region of Interest — a defined image area used for gray-value/statistical measurement in ImageJ.
- **Brightness (gray-value analysis)**: mean gray value within a defined ROI, indexing overall image lightness.
- **Noise**: standard deviation of gray values within a defined ROI, indexing pixel-to-pixel variability/graininess.
- **Uniformity**: consistency of gray-value SD between a central ROI and symmetric peripheral ROIs, indexing spatial evenness of exposure/response across the image.
- **Contrast (step-wedge method)**: percentage difference in mean gray value between two step-wedge thickness ROIs, indexing the image's ability to differentiate radiographic densities.
- **mAs**: milliampere-seconds, the product of tube current (mA) and exposure time (s), a standard radiographic exposure-dose parameter.
- **kVp**: kilovolt peak, the peak voltage applied across an X-ray tube, determining photon energy/beam quality.
