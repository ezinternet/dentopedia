#!/usr/bin/env bash
# slides/*.md (Marp) -> lectures/{stem}.html (standalone, self-contained deck)
#
# lectures/ is a dedicated top-level output folder (parallel to interactives/),
# not mixed into interactives/. Marp export alone has no frontmatter comment
# block, so this script injects one right after export so
# scripts/build-lectures-index.py can catalog it.
#
# 실행: bash scripts/export-slides.sh   (repo 루트 기준, 새/변경 슬라이드 있을 때 수동 실행)
set -euo pipefail
cd "$(dirname "$0")/.."

for f in slides/*.md; do
  [ -f "$f" ] || continue
  stem=$(basename "$f" .md)
  out="lectures/${stem}.html"

  meta=$(python3 -c "
import re, json
text = open('$f', encoding='utf-8').read()
m = re.search(r'^---\n(.*?)\n---', text, re.S)
fm = {}
for line in m.group(1).split('\n'):
    km = re.match(r'^([a-zA-Z_]+):\s*(.*)$', line)
    if km and km.group(1) not in fm:
        fm[km.group(1)] = km.group(2).strip().strip('\"')
print(json.dumps({
    'title': fm.get('title', '$stem'),
    'date': fm.get('date', '2026-01-01'),
    'status': fm.get('status', 'draft'),
    'audience': fm.get('audience') or fm.get('event') or '기타',
    'duration': fm.get('duration', ''),
    'agenda': fm.get('agenda', ''),
}))
")
  title=$(python3 -c "import json,sys; print(json.loads(sys.argv[1])['title'])" "$meta")
  date=$(python3 -c "import json,sys; print(json.loads(sys.argv[1])['date'])" "$meta")
  status=$(python3 -c "import json,sys; print(json.loads(sys.argv[1])['status'])" "$meta")
  audience=$(python3 -c "import json,sys; print(json.loads(sys.argv[1])['audience'])" "$meta")
  duration=$(python3 -c "import json,sys; print(json.loads(sys.argv[1])['duration'])" "$meta")
  agenda=$(python3 -c "import json,sys; print(json.loads(sys.argv[1])['agenda'] or '-')" "$meta")

  npx --yes @marp-team/marp-cli "$f" -o "${out}.tmp" --html
  {
    printf '<!--\n---\ntitle: "%s"\ntype: lecture\ndate: %s\nstatus: %s\naudience: "%s"\nduration: "%s"\nagenda: %s\nnote: "Marp deck export — source: %s. Regenerate: bash scripts/export-slides.sh"\n---\n-->\n' \
      "$title" "$date" "$status" "$audience" "$duration" "$agenda" "$f"
    cat "${out}.tmp"
  } > "$out"
  rm -f "${out}.tmp"
  echo "wrote $out"
done
