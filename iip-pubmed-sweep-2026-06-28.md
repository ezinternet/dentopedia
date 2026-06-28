# IIP (Immediate Implant Placement) — PubMed sweep ingest queue

- **Date**: 2026-06-28
- **Source**: PubMed MCP (SR/MA 112건 + RCT 136건 hits; 최근 고근거 17편 선별)
- **Scope note**: 사실상 PubMed-grade sweep. OpenAlex·Semantic Scholar·KoreaMed는 이 세션 fetch 미작동으로 비-MEDLINE·아시아 확장 미완.
- **Step 0 dedup**: 17편 중 6편 기존 위키 존재 → 재ingest 금지. NEW 11편(OA 5 / abstract-only 6).

## A. NEW · OA — 즉시 ingest (PMC 전문)

| stem | 논문 | 저널 | 유형 | category | DOI / PMID / PMC |
|---|---|---|---|---|---|
| zadikian-2026-open-healing-immediate-implant-mucosa | Open-healing+경점막 임시보철, peri-implant 점막 안정 (12편/438) | BMC Oral Health | sr+ma | immediate-implant/esthetic-soft-tissue | 10.1186/s12903-026-08105-z / 41862887 / PMC13126965 |
| pannuti-2026-loading-timing-edentulous-maxilla-pro | 무치악 상악 로딩시점 PRO/ClinRO scoping (5편) | Clin Oral Implants Res | sr | immediate-implant | 10.1111/clr.14451 / 41732074 / PMC12930122 |
| behfarnia-2025-anatomic-immediate-implant-mandibular-posterior | 하악구치 IIP 해부(IAC거리·설측천공) (12편) | BMC Oral Health | sr+ma | immediate-implant | 10.1186/s12903-025-06861-y / 41430227 / PMC12723949 |
| askinekinci-2026-bic-surface-immediate-implant-stability | BIC 접촉면적-1차 안정성 파일럿 (n=30) | Sci Rep | rct | immediate-implant | 10.1038/s41598-026-48697-8 / 41974820 / PMC13230908 |
| wu-2026-immediate-provisionalization-natural-crown-frc | 자연치관+FRC 스플린트 즉시 임시 (n=20) | BMC Oral Health | rct | immediate-implant/esthetic-soft-tissue | 10.1186/s12903-026-08156-2 / 41877071 / PMC13134079 |

## B. NEW · abstract-only — stub ingest 선택 (전문 도서관 필요)

| stem | 논문 | 저널(출판사) | 유형 | category | DOI / PMID |
|---|---|---|---|---|---|
| tamim-2025-custom-healing-abutment-immediate-implant | Custom healing abutment 효과 (6편) | J Prosthet Dent (Elsevier) | sr+ma | immediate-implant/esthetic-soft-tissue | 10.1016/j.prosdent.2025.09.038 / 41102038 |
| ji-2025-socket-shield-vs-conventional-esthetic-nma | Socket shield vs 전통 심미존 network MA (19편/760) | J Prosthet Dent (Elsevier) | sr+ma | immediate-implant/socket-shield | 10.1016/j.prosdent.2025.08.043 / 40940267 |
| lau-2025-cais-accuracy-immediate-implant-type1-sr-ma | static/dynamic CAIS 정확도 type-1 (15편) | J Prosthodont Res | sr+ma | immediate-implant | 10.2186/jpr.JPR_D_24_00257 / 40268423 |
| pliatkute-2025-prf-immediate-implant-gap-sr | PRF로 peri-implant gap·연조직 (7편) | Minerva Dent Oral Sci | sr | immediate-implant | 10.23736/S2724-6329.25.05171-X / 41378897 |
| khalifah-2026-double-expansion-ridge-split-narrow-rct | Double expansion vs ridge split 협소제 (40명/57임플란트) | Int J Oral Maxillofac Implants (Quintessence) | rct | immediate-implant | 10.11607/jomi.11388 / 40553084 |
| badawy-2026-socket-shield-delayed-ridge-change-rct | Socket shield(즉시식립無) 치조제 변화 (n=80) | Int J Oral Maxillofac Implants (Quintessence) | rct | immediate-implant/socket-shield | 10.11607/jomi.11311 / 40245309 |

## C. 이미 위키 존재 — 재ingest 금지 (Step 0 차단)

| 기존 stem | DOI |
|---|---|
| nava-2026-guided-surgery-immediate-implant-accuracy-nma | 10.1111/clr.70100 |
| atieh-2025-pre-extractive-vs-postextractive-immediate-molar | 10.1016/j.identj.2025.109316 |
| fan-2024-immediate-implant-ridge-preservation-comparative-sr-ma | 10.1097/MD.0000000000046832 |
| ebrahim-2026-vestibular-socket-therapy-immediate-implant-rct | 10.1186/s12903-026-08626-7 |
| abdelsameaa-2026-dentine-membrane-eprf-gbr-immediate-implant-rct | 10.1186/s12903-026-08582-2 |
| kwon-2026-thread-depth-guided-immediate-implant-isq-rct | 10.1111/cid.70145 |

## Finalize (Mac에서 실행)

```bash
export PATH="/opt/homebrew/bin:$PATH"
cd /Users/oracleneo/llm-wiki
python3 scripts/lint.py && python3 scripts/orphan-check.py && python3 scripts/ingest-rationale-lint.py
qmd update && qmd embed
git add papers/ sources/ wiki/ index.md && git commit -m "ingest: IIP PubMed sweep (5 OA papers)" && git push
```
