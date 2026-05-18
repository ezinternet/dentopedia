---
title: "Deep learning and clustering approaches for dental implant size classification based on periapical radiographs"
authors: Ji-Hyun Park, Hong Seok Moon, Hoi-In Jung, JaeJoon Hwang, Yoon-Ho Choi, Jong-Eun Kim
year: 2023
doi: 10.1038/s41598-023-42385-7
category: [digital-workflow]
pdf_path: /Users/oracleneo/llm-wiki/papers/park-2023-deep-learning-implant-size-classification.pdf
pdf_filename: park-2023-deep-learning-implant-size-classification.pdf
source_collection: external
---

## One-line Summary
Sci Rep 2023;13:16856: DL (VGG16) + clustering (k-means++) for implant diameter/length classification from periapical radiographs — DL accuracy >0.994, AUC >0.975; clustering accuracy >0.983 across 9 implant size groups.

## 1. Key Results
- Periapical radiographs; 9 implant size groups (diameter × length combinations)
- DL (VGG16, fine-tuned): accuracy >0.994; AUC-ROC >0.975; sensitivity >0.950
- Clustering (k-means++ on 3 landmark coordinates): accuracy >0.983; AUC >0.947
- Statistically significant improvement after model tuning vs baseline
- Both models showed reliable performance; multicenter validation needed

## 2. Clinical Implications
- AI can identify implant size from routine periapical radiographs — useful for maintenance/complication management
- Critical when patient records are unavailable (implant manufacturer identification)
- DL outperforms clustering but both exceed clinical usefulness threshold
- Prerequisite for AI-assisted complication management systems
