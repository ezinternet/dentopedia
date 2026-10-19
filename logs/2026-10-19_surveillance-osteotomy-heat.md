# 골경화증/Osteotomy Heat Surveillance — 2026-10-19

PubMed queries:
- "osteotomy heat generation dental implant drill irrigation" (60 total, 15 retrieved)
- "thermal osteonecrosis implant drilling temperature bone" (30 total, 15 retrieved)

## Already Ingested (skip)
- tur-2025 (tur-2025-scais-cip-guided-conventional-drill-diameter-heat)
- woods-2022 (woods-2022-does-irrigating-while-drilling-decrease)
- gedik-2025 (gedik-2025-four-drill-systems-ceramic-heat-osteotomy)
- gokce-uckun-2025 (gokce-uckun-2025-guided-surgery-cold-irrigation-temperature)
- de-lima-2026 (de-lima-2026-osseodensification-vs-conventional-drilling-exvivo)

## New Papers — Queue for Ingest (PMC full text available)

| Priority | Stem | PMID | DOI | Key Finding |
|---|---|---|---|---|
| HIGH | shobair-2026-heat-generation-guided-osteotomy-irrigation-route | 42283381 | 10.1111/clr.70147 | CLOR: internal irrigation ΔT 0.84°C vs external 2.45°C vs none 13.31°C (bilayered) |
| HIGH | paessens-2025-irrigation-bur-size-speed-thermographic-heat-osteotomy | 40521678 | 10.1111/clr.14462 | CLOR: irrigation OR 177.5, step-size OR 9.9, speed OR 4.9/400rpm for ≥47°C |
| HIGH | almohammadi-2025-single-vs-sequential-drills-bone-density-heat | 41316251 | 10.1186/s12903-025-07377-1 | BMC: single drill lower heat in D1/D2 but higher in D3/D4 |
| MED | komu-2026-osseodensification-conventional-drilling-d3-heat-stability | 41990877 | 10.1016/j.jormas.2026.102808 | OD ISQ 77.3 vs CD 74.7; Tmax OD 42.7°C vs CD 37.4°C non-irrigated D3 |
| MED | tur-2026-guided-conventional-pilot-drill-thermal-evaluation | 42432641 | 10.1186/s12903-026-09215-4 | Larger pilot drill (2.8mm) in guided surgery needs irrigation even with sequential |
| MED | balkanlioglu-2026-osteotomy-depth-diameter-d1-cadcam-temperature | 42090571 | 10.11607/jomi.11735 | Depth η²=0.82 > diameter η²=0.17; all <47°C with irrigation D1-like |
| LOW | baris-2025-dry-cooling-peltier-osteotomy-heat | 40722017 | 10.1186/s12903-025-06593-z | Dry cooling (Peltier) DC-LP: ΔT 2.0°C vs saline SC-HP: 5.5°C |

## Ingest Instructions
All papers are open-access PMC. Use PubMed MCP `get_full_text_article`:
```
mcp__8ed3ab32...__get_full_text_article(pmid="<PMID>")
```
Save text → papers/{stem}.txt, then write sources/{stem}.md + wiki/{category}/{stem}.md.
Category: bone-biology/ or implants/osseodensification/ depending on focus.
