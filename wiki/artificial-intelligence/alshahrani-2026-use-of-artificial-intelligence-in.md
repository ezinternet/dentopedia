---
title: "Use of Artificial Intelligence in Diagnosing Vertical Root Fractures—A Systematic Review"
authors: Alshahrani Abdulmajeed Saeed, Alelyani Ahmed Ali, Jabali Ahmad, Al Malwi Ahmed Abdullah, Alroomy Riyadh, Shaiban Amal S., Almnea Raid Abdullah, Mehta Vini, Al Moaleem Mohammed M., Duong Tim, Leung Yiu Yan
year: 2026
date: 2026-01-27
doi: 10.3390/diagnostics16030406
source: alshahrani-2026-use-of-artificial-intelligence-in.md
category: artificial-intelligence
evidence_level: sr
source_collection: pubmed-text
full_text: true
pmid: "41681724"
pmcid: "PMC12896978"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12896978/
text_path: /Users/oracleneo/llm-wiki/papers/alshahrani-2026-use-of-artificial-intelligence-in.txt
text_filename: alshahrani-2026-use-of-artificial-intelligence-in.txt
tags: [vertical-root-fracture, artificial-intelligence, deep-learning, CNN, CBCT, periapical-radiography, panoramic-radiography, diagnostic-accuracy, QUADAS-2, GRADE, systematic-review]
relations:
  - type: extends
    target: mun-2024-deep-learning-cracked-tooth-extraction-panoramic
  - type: extends
    target: patel-2022-present-status-future-directions-vertical
---

## 한국어 핵심요약

> [!summary] 한국어 핵심요약
> - 수직치근파절 (Vertical Root Fracture, VRF)의 인공지능 (Artificial Intelligence, AI) 진단을 치근단·파노라마·CBCT에서 평가한 체계적 문헌고찰 (Systematic Review, SR) 10편; 이질성이 커서 메타분석 없이 서술적 종합.
> - CBCT 기반 AI가 정확도 91.4–97.8%, 특이도 90.7–100%로 가장 우수하며 GRADE 중간 확실성.
> - 치근단 모델은 발치 후 (ex vivo) 조건에서 정확도 최대 95.7%이나 낮은 확실성; 파노라마 모델은 가장 낮은 성능 (낮은 확실성).
> - 파노라마 예: Fukuda 2020 재현율 0.75·정밀도 0.93이나 VRF 검출률 20%·위양성 20건; Mun 2024 민감도 90.43%·특이도 60.77%.
> - 일부 연구는 사람 판독자와 비교: Yang 2023 (CBCT ResNet-50, 환자 14명)은 방사선과 전문의 2명보다 민감도가 높고 특이도는 낮았다 (민감도 94.5%, 특이도 73.2%).
> - 발치 후 연구는 성능을 과대평가하는 경향; 단일기관·소규모 데이터·외부 검증 부재로 과적합 위험.
> - 포함 연구가 모두 영상 AI는 아니다 (Chang 2024는 임상·시술 변수 기반 예측모델, Kapralos 2020은 디지털 감산 방사선술).
> - 위험도 평가 (QUADAS-2): Fukuda 2020·Chang 2024 고위험, Kositbowornchai 2013·Kapralos 2020 저위험.
> - 임상 takeaway: AI는 보조 도구이며 확진 영상은 CBCT; 워크플로 통합·임상 결과를 평가한 연구는 없다.
> - 본문 내부 불일치 주의: 초록은 Cochrane·2025년 1월까지, 방법 절은 Embase·2025년 7월까지로 서술.

## Three-line Summary

Systematic review (PRISMA 2020, PROSPERO CRD420251134312; QUADAS-2 + GRADE; 10 studies, 2013–2025; narrative synthesis because heterogeneity precluded meta-analysis) of AI-based vertical root fracture (VRF) detection on periapical, panoramic and CBCT images.

CBCT-based AI had the highest accuracy (91.4–97.8%) and specificity (90.7–100%) with moderate GRADE certainty; periapical models reached up to 95.7% accuracy but only in ex vivo settings (low certainty); panoramic models were weakest (e.g., recall 0.75 with 20 false positives; specificity 60.8%) with low certainty.

Most evidence is ex vivo or single-centre with small datasets and no external validation; AI is a promising adjunct, CBCT remains the confirmatory modality, and none of the included studies assessed clinical workflow impact.

## 세줄요약

수직치근파절 (Vertical Root Fracture, VRF)의 AI 진단을 치근단·파노라마·CBCT 영상에서 평가한 체계적 문헌고찰 10편 (PRISMA 2020, QUADAS-2, GRADE; 이질성이 커서 메타분석 불가, 서술적 종합).

CBCT 기반 AI가 정확도 91.4–97.8%, 특이도 90.7–100%로 최고 (GRADE 중간 확실성); 치근단 모델은 발치 후 (ex vivo) 조건에서 정확도 최대 95.7%, 파노라마 모델은 재현율 0.75·위양성 20건 등으로 가장 낮음 (둘 다 낮은 확실성).

근거 대부분이 발치 후·단일기관·소규모 데이터이고 외부 검증이 없어, AI는 보조 도구 수준이며 확진은 여전히 CBCT; 임상 워크플로 영향을 평가한 연구는 0편.

## Summary

This PRISMA 2020 systematic review (PROSPERO CRD420251134312) searched PubMed, Embase, Web of Science and Scopus and included 10 studies on AI detection of vertical root fractures on periapical radiographs, panoramic radiographs and CBCT. CNN architectures (DenseNet, ResNet, DetectNet) predominated, with older probabilistic neural networks in two ex vivo studies. CBCT-based models achieved the highest accuracy (91.4–97.8%) and specificity (90.7–100%), rated moderate certainty by GRADE; periapical and panoramic models were rated low certainty, the former reaching up to 95.7% accuracy in controlled ex vivo conditions and the latter showing the lowest performance. Heterogeneity in models, modalities, preprocessing and metrics precluded pooling, and the authors judged AI to be an adjunct for early screening with CBCT as the confirmatory modality.

## Key Contributions

- First SR dedicated to AI for VRF across periapical, panoramic and CBCT imaging.
- Modality ranking CBCT > periapical > panoramic with per-modality GRADE certainty (moderate / low / low).
- Shows ex vivo results overstate real-world performance and highlights overfitting risk from small datasets.
- Documents the absence of any study on clinical workflow, usability or decision-support outcomes.

## Methodology

Systematic review following PRISMA 2020, registered in PROSPERO; four databases (PubMed, Embase, Web of Science, Scopus) plus reference-list screening; two independent screeners with a third for disagreements (18/258 title-abstract and 2/13 full-text discrepancies, all resolved by consensus). Flow: 404 records, 146 duplicates removed, 258 screened, 13 full texts, 10 included. Risk of bias with QUADAS-2; certainty with GRADE; structured narrative synthesis (no meta-analysis). Reference standards were stereomicroscope/micro-CT for ex vivo studies and consensus for retrospective/in vivo series. Source-text note: the Abstract names the Cochrane Library and "January 2025" while Methods name Embase and "July 2025"; both are reproduced here as written.

## Results

| Study | Modality / setting | Model | Key result |
|---|---|---|---|
| Fukuda 2020 | Panoramic, 300 images | CNN (DetectNet) | recall 0.75, precision 0.93, F 0.83; VRF detection rate 20%, 20 false positives |
| Hu 2022 | CBCT | Pretrained CNNs | manual ROI 97.8% accuracy (AUC 0.99); automatic ROI 91.4% (AUC 0.96) |
| Abdelazim 2024 | Periapical, ex vivo | 5-CNN ensemble | DenseNet121/169 sens 89.4%/87.2%, spec 93.6%, AUC 0.98 |
| Ozsari 2025 | Periapical | DenseNet–Inception | accuracy ~0.80, kappa 0.60 |
| Yang 2023 | CBCT, in vivo, 14 patients | ResNet-50 | sens 94.5%, spec 73.2%, AUC 0.929; sensitivity above two oral radiologists |
| Mun 2024 | Panoramic | ResNet-50 | sens 90.43%, spec 60.77%, accuracy 75.84%, AUC 0.825 |
| Kositbowornchai 2013 | Periapical, ex vivo | PNN | sens 97.2–98.0%, spec 60.0–90.5%, accuracy 88.3–95.7% |
| Johari 2017 | Periapical vs CBCT, ex vivo | PNN | periapical accuracy 70.0%; CBCT accuracy 96.6%, spec 100% |
| Chang 2024 | Clinical/procedural variables (non-imaging) | DNN vs SVM | accuracy 80.7%, recall 93.7%, F1 86.7% |
| Kapralos 2020 | Periapical, root-filled teeth | Digital subtraction radiography | AUC 0.73 vs conventional lower |

GRADE: CBCT-based AI moderate certainty; periapical low; panoramic low. The reported CBCT range (91.4–97.8% accuracy, 90.7–100% specificity) does not encompass Yang 2023's in vivo CBCT specificity of 73.2%, and the Abstract's panoramic sensitivity range (0.45–0.75) does not match Mun 2024's 90.43% sensitivity reported in the body, so the range summaries should be read with the per-study table.

## Clinical Insights

- For a suspected VRF, AI on periapical or panoramic images is at best a screening aid; the high sensitivity/low specificity pattern (Mun 2024, Yang 2023) suggests triage toward CBCT rather than diagnosis, consistent with [[artificial-intelligence/mun-2024-deep-learning-cracked-tooth-extraction-panoramic]].
- The CBCT accuracy figures come mainly from ex vivo or small single-centre datasets with manual ROI cropping; they do not show that AI overcomes the clinical CBCT limitations (artefacts from intracanal materials, indirect bone-loss signs) described in [[cracked-tooth/patel-2022-present-status-future-directions-vertical]].
- No held evidence yet supports AI changing treatment decisions or outcomes for VRF.

## Related Papers

- [[artificial-intelligence/mun-2024-deep-learning-cracked-tooth-extraction-panoramic]] — included in this SR as a panoramic study; the SR places it among weakest-performing modality models and adds periapical/CBCT context.
- [[cracked-tooth/patel-2022-present-status-future-directions-vertical]] — narrative review stating CBCT cannot reliably show the fracture line itself; this SR adds the AI-assisted perspective (moderate-certainty only for CBCT).
- [[cracked-tooth/patel-2025-position-statement-longitudinal-cracks-fractures]] — ESE consensus defining VRF-NRFT/VRF-RFT and recommending selective CBCT; context for where AI would sit.
- [[cracked-tooth/eraslan-2026-artificial-intelligence-cracked-tooth-diagnosis]] — language-model benchmark in cracked tooth diagnosis; a text-based AI contrast to the image-based AI here.
- [[cracked-tooth/kindaro-2025-diagnostic-accuracy-detect-cracked-teeth]] — non-AI visual crack-detection tools, QUADAS-2 diagnostic accuracy.
- [[cracked-tooth/hernando-2026-diagnostic-methods-dental-cracks-systematic-review]] — SR of conventional crack diagnostic methods; this page is the AI-specific counterpart for VRF.
- [[artificial-intelligence/albano-2024-artificial-intelligence-radiographic-caries-detection]] — another QUADAS-2 AI imaging SR with the same "promising but heterogeneous, no pooling" pattern.
- [[overviews/cracked-tooth-syndrome-overview]] — cracked tooth syndrome synthesis.
- [[overviews/ai-dentistry-reviews-2024-2025-synthesis]] — AI dentistry review synthesis.
- [[overviews/cbct-diagnostic-performance-overview]] — CBCT diagnostic performance overview.
