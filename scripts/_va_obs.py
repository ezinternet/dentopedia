#!/usr/bin/env python3
"""Print top-15 observation-tier overviews by score.
Run from repo root: python3 scripts/_va_obs.py
"""
import sys, importlib.util
from pathlib import Path

REPO = Path(__file__).parent.parent
spec = importlib.util.spec_from_file_location("_ova", REPO / "scripts" / "overview-volatility-audit.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

stem_to_path, meta = mod.build_page_index()
commits = mod.collect_overview_commits()
git_ok = bool(commits)
if git_ok:
    window = mod.git_history_window()
    if window:
        mod.CAP["age_days"] = window

rows = []
for p in sorted(mod.OVERVIEWS_DIR.glob("*.md")):
    fm = meta.get(p.stem) or mod.read_frontmatter(p)
    rel = str(p.relative_to(mod.WIKI_ROOT))
    thesis_dt, churn = mod.analyze_history(commits.get(rel, []))
    rows.append(mod.score_overview(p, fm, meta, thesis_dt, churn, git_ok))

rows.sort(key=lambda r: r["score"], reverse=True)
obs = [r for r in rows if r["score"] < mod.TIER_ORANGE]
print(f"Observation tier: {len(obs)} overviews")
print("\nTop 15 by score:")
for r in obs[:15]:
    print(f"  {r['score']:5.1f}  {r['stem']}")
