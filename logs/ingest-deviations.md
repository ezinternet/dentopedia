# Ingest Deviations

Logged by subagents at deviation time. `deviation-audit.py` flags types with ≥3 occurrences as SOP revision candidates.

| date | stem | type | description |
|------|------|------|-------------|
| 2026-07-07 | ji-2018-three-key-factors-influencing-bacterial | other | PMC9379084 get_full_text_article returned empty body; built page from structured abstract (full_text:false) |
| 2026-07-08 | cunha-2025-class-iii-surgery-first-aligner-fixed-ohrqol | other | PMC full_text field (32716 chars) truncated mid-Discussion section before Conclusions; used Abstract to confirm bottom-line conclusion. No missing Results tables — all 5 tables captured before truncation point. |
| 2026-07-08 | gok-2025-clear-aligner-z-spring-anterior-crossbite-mixed-dentition | other | PMC full_text empty, built from structured abstract |
| 2026-07-08 | panda-2025-clear-aligner-braces-class-iii-comparison | other | PMC full_text only ~6.7k chars but contains complete Methods/Results/Discussion/Conclusion (headers appear stripped to single letters e.g. 'I','MM','R','D','C' by extraction) — treated as full_text:true, genuinely short/concise paper not truncated retrieval |
