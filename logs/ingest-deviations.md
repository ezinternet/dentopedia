# Ingest Deviations

Logged by subagents at deviation time. `deviation-audit.py` flags types with ≥3 occurrences as SOP revision candidates.

| date | stem | type | description |
|------|------|------|-------------|
| 2026-07-07 | ji-2018-three-key-factors-influencing-bacterial | other | PMC9379084 get_full_text_article returned empty body; built page from structured abstract (full_text:false) |
| 2026-07-08 | cunha-2025-class-iii-surgery-first-aligner-fixed-ohrqol | other | PMC full_text field (32716 chars) truncated mid-Discussion section before Conclusions; used Abstract to confirm bottom-line conclusion. No missing Results tables — all 5 tables captured before truncation point. |
| 2026-07-08 | gok-2025-clear-aligner-z-spring-anterior-crossbite-mixed-dentition | other | PMC full_text empty, built from structured abstract |
| 2026-07-08 | panda-2025-clear-aligner-braces-class-iii-comparison | other | PMC full_text only ~6.7k chars but contains complete Methods/Results/Discussion/Conclusion (headers appear stripped to single letters e.g. 'I','MM','R','D','C' by extraction) — treated as full_text:true, genuinely short/concise paper not truncated retrieval |
| 2026-07-09 | felisati-2012-late-recovery-foreign-body-sinusitis | other | PMC4544220 get_full_text_article returned empty full_text field (BMJ Case Reports); built sources+wiki from structured abstract only, full_text:false |
| 2026-07-10 | zhang-2026-in-vivo-models-dual-biofunctional-coatings | other | DOI conflict/cross-stem duplicate: same paper already ingested as zhang-2025-dual-biofunctional-implant-coatings-in-vivo-sr (doi was null, missed by Step0 grep). Confirmed via PDF metadata (Subject field carries DOI 10.1016/j.jdsr.2026.02.002, JDSR 62(2026) 81-91) and identical title/authors/16-study content. Skipped new page creation; deleted duplicate PDF copy; backfilled doi field on existing sources+wiki pages. |
| 2026-07-10 | cesar-2024-dental-zirconia-15years-material-processing | other | PMC batch(치과재료 추세): Cesar 2024 DOI 10.1016/j.dental.2024.02.026 already ingested under this stem; skipped re-ingest, only Cuzic 2025 newly added |
| 2026-07-10 | cosola-2026-customized-3d-printed-titanium-subperiosteal-implants-sr-ma | other | JOMS full text paywalled; page built from structured abstract only, full_text:false |
| 2026-07-10 | shirani-2026-computer-assisted-vs-freehand-implant-placement-sr-ma | other | Quintessence full text paywalled; page built from structured abstract only, full_text:false |
| 2026-07-10 | yeung-2023-functional-neuroplasticity-denture-rehabilitation-fmri | other | kept complete-denture: intervention is edentulous denture/implant-overdenture rehabilitation (8/9 studies complete-edentulous) but measured outcome is brain fMRI neuroplasticity — no neuroscience folder exists; classified by procedure per CLAUDE.md |
