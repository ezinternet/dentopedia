---
title: "Assessment of microbiota diversity in dental unit waterline contamination"
authors: Dang Y, Zhang Q, Wang J, Wang Q, Han M, Niu Y, Li H, Li X
year: 2022
doi: 10.7717/peerj.12723
category: [infection-control]
source_collection: pubmed-text
full_text: true
pmid: "35036099"
pmcid: "PMC8743008"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8743008/
text_path: /Users/oracleneo/llm-wiki/papers/dang-2022-assessment-microbiota-diversity-dental-unit.txt
text_filename: dang-2022-assessment-microbiota-diversity-dental-unit.txt
---

## Why Ingested

쓰리웨이 시린지(air/water syringe, three-way syringe)의 물 오염도를 정량화한 논문. [[infection-control/samaranayake-2024-dental-unit-waterlines-disinfection]]가 DUWL 오염을 서술적으로 종합했다면, 본 연구는 60개 유니트의 air/water syringe 출수를 배양+16S 시퀀싱으로 실측해 "시린지 물에 실제로 무엇이 얼마나 있는가"를 구체 수치로 보강한다. suck-back(역흡입)과 anti-retraction valve 실패라는 시린지 오염 기전을 확장.

## Three-line Summary

Cross-sectional study of 60 dental chair units (350 water samples culture + 16S sequencing of air/water syringe water) measuring DUWL contamination.

Median 166 CFU/mL (range 0–3,816,000); only 42.6% below the 100 CFU/mL threshold; Proteobacteria dominant (>85%), with Pseudomonas (31%) and Acinetobacter (7.6%) among 7 potential human pathogens.

Air/water syringe output water is heavily and variably contaminated; suck-back and anti-retraction valve failure drive specialty-dependent community differences, requiring validated disinfection.

## 세줄요약

60개 치과 유니트(배양 350검체 + air/water syringe 물 16S 시퀀싱)의 치과 유니트 수관(DUWL) 오염 횡단연구.

중앙값 166 CFU/mL(범위 0–3,816,000), 100 CFU/mL 기준 만족은 42.6%뿐; 프로테오박테리아 우세(>85%), 슈도모나스(31%)·아시네토박터(7.6%) 포함 잠재 병원체 7속 검출.

쓰리웨이(air/water) 시린지 출수는 심하게·불균일하게 오염 — 역흡입(suck-back)과 역류방지밸브 실패가 진료과별 균총 차이를 유발, 검증된 소독 프로토콜 필요.

## 1. Document Information

- **Journal**: PeerJ, 2022 Jan 6; 10:e12723
- **Type**: Cross-sectional microbiological study (culture + 16S rDNA high-throughput sequencing)
- **Authors**: Yun Dang, Qian Zhang, Jing Wang, Qian Wang, Meng Han, Yuting Niu, Hua Li, Xiue Li (Peking University School of Stomatology)
- **DOI**: [10.7717/peerj.12723](https://doi.org/10.7717/peerj.12723)

## 2. Key Contributions

1. Quantified DUWL bacterial load across 60 dental chair units in three specialties, sampling high-speed handpieces, **air/water syringes**, and mouth-rinse outlets.
2. Applied 16S rDNA sequencing (not just culture) specifically to **air/water syringe** water (60 × 250-mL samples), revealing community structure culture alone misses.
3. Showed only 42.6% of samples met the 100 CFU/mL standard; max 3,816,000 CFU/mL.
4. Identified 7 potential human-pathogenic genera and specialty-specific enrichment (periodontics distinct).

## 3. Methodology and Architecture

- 60 DCUs: 19 periodontics, 21 endodontics, 20 prosthodontics; municipal feed water (China standard <100 CFU/mL).
- Outlets alcohol-disinfected; lines flushed 2 min before / 30 s after daily practice.
- 350 × 5-mL culture samples (BHI, 48 h, 37 °C, 5% CO₂); threshold 100 CFU/mL.
- 60 × 250-mL air/water syringe samples → filtered 0.2 μm → DNA; 17 high-quality DNA → 16S V3–V4 (Illumina MiSeq PE250); OTUs at 97%.
- Stats: Kruskal–Wallis (across specialties), Wilcoxon signed-rank (before/after), PCoA/ADONIS, LEfSe.

## 4. Key Results and Benchmarks

- Median 166 (31.5, 672.5) CFU/mL; range 0–3,816,000; 42.6% below 100 CFU/mL.
- By specialty: periodontics 335 CFU/mL > prosthodontics 141 > endodontics 79 (H=27.441, P<0.01).
- Before vs after daily practice: no significant difference (192 vs 160 CFU/mL, Z=−1.626, P=0.104) — flushing alone insufficient because suck-back reintroduces contamination.
- Proteobacteria >85%. Genera >5%: Pseudomonas 31.08%, Curvibacter 10.93%, Sphingobium 9.61%, Acinetobacter 7.64%, Acidovorax 5.95%.
- 7 potential pathogens >1%: Pseudomonas, Acinetobacter (21% in prosthodontics), Ochrobactrum, Sphingomonas, Methylobacterium, Rhizobium, Brevundimonas.
- Alpha-diversity similar across specialties (P>0.05); beta-diversity (community structure) differs — periodontics separate.

## 5. Limitations and Future Work

- Single dental hospital; municipal-water feed (results may differ with bottled/purified feed).
- Only 17 of 60 samples yielded sequenceable DNA.
- Culture may underestimate viable-but-non-culturable bacteria.
- No clinical-infection outcome; disinfection efficacy not tested here.

## 6. Related Work

- Reinforces [[infection-control/samaranayake-2024-dental-unit-waterlines-disinfection]] (DUWL biofilm amplification, suck-back).
- Mechanistically linked to [[infection-control/ji-2018-three-key-factors-influencing-bacterial]] (anti-retraction valve / water source / disinfection).
- Air-side counterpart [[infection-control/dudding-2022-clinical-observational-analysis-aerosol-emissions]] (3-in-1 syringe aerosol).

## 7. Glossary

- **DUWL**: dental unit waterline — narrow-bore tubing supplying handpieces, air/water syringes, cup fillers.
- **Suck-back / retraction**: negative pressure at instrument release drawing oral fluids back into the line.
- **Anti-retraction valve**: one-way valve preventing suck-back; degrades over months of use.
- **OTU / 16S rDNA sequencing**: culture-independent taxonomic profiling of bacterial communities.
- **CFU/mL**: colony-forming units per mL; CDC threshold 500, EU/China 100.
