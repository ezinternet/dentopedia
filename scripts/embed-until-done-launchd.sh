#!/usr/bin/env bash
#
# embed-until-done-launchd.sh — launchd wrapper around embed-until-done.sh.
#
# WHY: A single `qmd embed` pass expires its daemon session after ~30min/~300 chunks,
# and a foreground/session-bound loop dies when its parent session tears down. Running
# under launchd detaches the work from any Claude Code / terminal session and, with
# KeepAlive={SuccessfulExit:false}, relaunches automatically until the loop finally
# exits 0 (the "All content hashes already have embeddings" done marker).
#
# Managed by: ~/Library/LaunchAgents/com.llmwiki.embed-until-done.plist
# Tracked copy of that plist: .claude/scripts/com.llmwiki.embed-until-done.plist
#   (launchd only reads ~/Library/LaunchAgents — the in-repo copy is the versioned
#    master; edit it there, then re-install with the cp below.)
#
# Install:    cp .claude/scripts/com.llmwiki.embed-until-done.plist ~/Library/LaunchAgents/
#             launchctl load -w ~/Library/LaunchAgents/com.llmwiki.embed-until-done.plist
# Stop it:    launchctl unload ~/Library/LaunchAgents/com.llmwiki.embed-until-done.plist
# Watch it:   tail -f logs/embed-until-done.log
# Is it on?:  launchctl list | grep embed
#
# NOTE: only ONE `qmd embed` may run at a time — two concurrent embeds deadlock on the
# index and make zero progress. Check with `pgrep -f "qmd.js embed"` before starting a
# manual pass while this agent is loaded.
#
set -euo pipefail
export PATH="/opt/homebrew/bin:$PATH"
cd /Users/oracleneo/llm-wiki
exec bash scripts/embed-until-done.sh
