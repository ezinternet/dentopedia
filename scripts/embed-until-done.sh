#!/usr/bin/env bash
#
# embed-until-done.sh — run `qmd embed` repeatedly until the backlog is empty.
#
# WHY: On large backlogs (2,000+ docs) the qmd HTTP daemon expires its session
# mid-run and exits 0 WITHOUT finishing — exit-0 does NOT mean complete. The only
# reliable "done" signal is the message "All content hashes already have embeddings".
# See memory: qmd-embed-multipass.
#
# Usage:
#   bash scripts/embed-until-done.sh          # foreground
#   bash scripts/embed-until-done.sh &        # background, then carry on working
#
set -euo pipefail

export PATH="/opt/homebrew/bin:$PATH"

DONE_MARKER="All content hashes already have embeddings"
MAX_PASSES="${MAX_PASSES:-40}"   # safety cap so a broken daemon can't loop forever

cd "$(dirname "$0")/.."

# Make sure the index is current before embedding.
qmd update || true

pass=0
while (( pass < MAX_PASSES )); do
  pass=$((pass + 1))
  echo "── embed pass ${pass} ──"
  out="$(qmd embed 2>&1 || true)"
  echo "$out"
  if grep -qF "$DONE_MARKER" <<<"$out"; then
    echo "✅ embed complete after ${pass} pass(es)."
    exit 0
  fi
  echo "…backlog remains, retrying in 5s"
  sleep 5
done

echo "⚠️  hit MAX_PASSES=${MAX_PASSES} without seeing the done marker — check the qmd daemon."
exit 1
