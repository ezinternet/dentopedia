# launchd agents — versioned copies

launchd only ever reads `~/Library/LaunchAgents/`. The `.plist` files here are the
**versioned masters**: edit them here, then `cp` to `~/Library/LaunchAgents/` and
re-`load`. They exist so a machine migration or a lost `~/Library` is a `cp` away from
recovery instead of a reconstruction from memory.

Keep each tracked copy **byte-identical** to its live counterpart — `diff` is the check
that the copy is still a real backup:

```bash
for p in .claude/scripts/*.plist; do diff "$p" ~/Library/LaunchAgents/"$(basename "$p")"; done
plutil -lint .claude/scripts/*.plist
```

## Inventory

| Label | Wrapper | Runs |
|---|---|---|
| `com.llmwiki.ingest-watcher` | [`ingest-watcher.sh`](ingest-watcher.sh) | fswatch on wiki root → auto-ingest each new PDF |
| `com.llmwiki.weekly-digest` | [`weekly-digest.sh`](weekly-digest.sh) | 매주 월 09:00 주간 근거 다이제스트 생성 |
| `com.llmwiki.qmd-cleanup` | *(none — `qmd cleanup` directly)* | 매주 월 10:00 고아 벡터 청소 — CLAUDE.md *Searching the Wiki* 참조 |
| `com.llmwiki.embed-until-done` | [`../../scripts/embed-until-done-launchd.sh`](../../scripts/embed-until-done-launchd.sh) | qmd 임베딩 백로그를 다 소진할 때까지 재실행 |
| `com.oracleneo.qmd-mcp` | *(none — see below)* | QMD 검색 데몬, HTTP MCP on port 8181 |

이 표가 **가동 중인 전부**여야 한다. 세는 것이 확인이다 — 눈대중하지 말고:

```bash
ls ~/Library/LaunchAgents/com.llmwiki.*.plist ~/Library/LaunchAgents/com.oracleneo.*.plist \
  | xargs -n1 basename | sort > /tmp/live
ls *.plist | sort > /tmp/tracked
diff /tmp/live /tmp/tracked   # 차이가 있으면 이 표도 낡았다
```

*(2026-07-17: 이 표는 처음 작성될 때 `qmd-cleanup`을 빠뜨린 채 4종으로 들어왔다 —
그 잡은 브랜치가 갈라진 뒤에 main에 추가됐고, 표는 기억으로 쓰였기 때문이다. 라이브는
줄곧 5종이었다. 표를 고칠 때마다 위 `diff`를 돌릴 것.)*

Each wrapper's header comment carries its own install / stop / watch / is-it-loaded
commands. Per-agent notes below cover only what a wrapper comment can't.

## `com.oracleneo.qmd-mcp` — no wrapper in this repo

This agent has **no script in the repo to document**: its `ProgramArguments` executes the
Homebrew-installed binary `/opt/homebrew/bin/qmd` (a symlink into
`/opt/homebrew/lib/node_modules/@tobilu/qmd/`) directly. The plist copy here is the whole
of what this repo can version — a fresh machine also needs the qmd install itself, via
[`../../scripts/setup-qmd.sh`](../../scripts/setup-qmd.sh).

**Do not casually unload or restart it.** It serves the QMD daemon on `localhost:8181`,
which every wiki lookup depends on (CLAUDE.md *Searching the Wiki*); dropping it breaks
search for every session on this machine until it comes back.

```
Install:    cp .claude/scripts/com.oracleneo.qmd-mcp.plist ~/Library/LaunchAgents/
            launchctl load -w ~/Library/LaunchAgents/com.oracleneo.qmd-mcp.plist
Stop it:    launchctl unload ~/Library/LaunchAgents/com.oracleneo.qmd-mcp.plist   # breaks wiki search
Watch it:   tail -f ~/.cache/qmd/mcp-launchd.log ~/.cache/qmd/mcp-launchd.err.log
Is it on?:  launchctl list | grep qmd-mcp
            lsof -nP -iTCP:8181 -sTCP:LISTEN     # the daemon actually listening
```

The plist pins `QMD_EMBED_MODEL` to the Qwen3 embedding GGUF. It must match the model the
existing index was embedded with — changing it silently invalidates
`~/.cache/qmd/index.sqlite` and forces a full re-embed.

## Load state ≠ tracked state

A plist being versioned here says nothing about whether launchd is running it. As of
2026-07-16, `com.llmwiki.ingest-watcher` is **not loaded** (present in
`~/Library/LaunchAgents/`, absent from `launchctl list`) — ingests are run on demand
instead. Check reality, never assume:

```bash
launchctl list | grep -E 'llmwiki|qmd-mcp'
```
