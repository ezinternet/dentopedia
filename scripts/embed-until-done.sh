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
#   bash scripts/embed-until-done.sh          # foreground, all collections
#   bash scripts/embed-until-done.sh &        # background, then carry on working
#   bash scripts/embed-until-done.sh -c wiki  # scope to one collection (args pass through
#                                             # to `qmd embed`) — e.g. embed searchable wiki
#                                             # pages first, defer the long sources/ docs
#
set -euo pipefail

export PATH="/opt/homebrew/bin:$PATH"

DONE_MARKER="All content hashes already have embeddings"
MAX_PASSES="${MAX_PASSES:-40}"   # safety cap so a broken daemon can't loop forever

cd "$(dirname "$0")/.."

# Make sure the index is current before embedding.
qmd update || true

# Per-pass output goes to a temp file via `tee` so it STREAMS to stdout/the log live,
# instead of being swallowed by `out="$(qmd embed ...)"` and dumped only after the pass
# ends. That swallowing made `tail -f logs/embed-until-done.log` look frozen for ~30min
# at a time, then vomit a whole pass at once — it read as a hang, and the only way to see
# real progress was `qmd status`. We still need the full text to grep for the done marker,
# hence tee (stream) + grep the file (detect), rather than a command substitution.
tmp="$(mktemp -t embed-until-done)"
trap 'rm -f "$tmp"' EXIT

pass=0
while (( pass < MAX_PASSES )); do
  pass=$((pass + 1))
  echo "── embed pass ${pass} ──"
  # `|| true` on the pipeline: a failed pass must not kill the loop (set -e is on) —
  # session expiry IS the normal per-pass ending and we simply retry.
  qmd embed "$@" 2>&1 | tee "$tmp" || true
  if grep -qF "$DONE_MARKER" "$tmp"; then
    echo "✅ embed complete after ${pass} pass(es)."
    exit 0
  fi
  echo "…backlog remains, retrying in 5s"
  sleep 5
done

echo "⚠️  hit MAX_PASSES=${MAX_PASSES} without seeing the done marker — check the qmd daemon."
exit 1
