---
name: file-tree-explorer-sync
description: How the File Tree page (artifact), its data and the docs stay in sync; build, test and publish steps; page modes; the Apply changes button (a page comment wakes the thread)
metadata:
  type: project
---
The File Tree page: artifact https://claude.ai/artifact/72v2Uppt6jpfXLCjKNX9xs. Source /mnt/project-files/vision/explorer/file-tree-explorer.html; republish by url with `files: {"file-tree.data.json": ...}`. State 2026-10-09: artifact version 52 / data v46 / file-tree.md v1.34 / 406 nodes + 1479 scanned real files, every repo file incl. vision/, texts in real-files.json published next to the data (REPO_DIR = fresh clone; researches in agents/trading/researches/, D-061). Capabilities {db, sample, user, comments}: a non-empty set is a full set, so restate all four on every publish that passes capabilities.

**Build (ide-build):** copy the finished page into vision/explorer/ FIRST (the data embeds the page source for [53.1.1]); `cd vision/tools; python3 parse.py $S/parsed.json; DATA_VERSION=N python3 enrich.py $S/parsed.json $S/ftdN.json`; copy to vision/file-tree.data.json, vision/explorer/ and $S/explorer/; `build_map.py --stale` / `--set json` (BY=knowledge-base-agent) / `--confirm ids` until (many nodes: one worker per subtree) "fresh, 0 missing or stale, 0 orphans" (can take >120s, use timeout); `node check_page.js <dir> <shots|-> n-0 n-...` (ids need the `n-` prefix) must print "page ok"; publish.

**Page features:** How it works = each node's `{name}.index.md` without the file's extension (mirror tree vision/tree/agent-os/..., drafts keep theirs next to the draft: index_files.DRAFTS/DRAFT_DIRS), plus an empty `.meta.json` shown on the Details tab; metadata rows in the tree (switch "metadata", localStorage `ftx-idx`); md files open in Read view; File tab shows drafts via enrich CLAUDE_DRAFTS and VISION_FILES (scripts, overrides, page source, server files in vision/server/); the data file shows itself read-only (content_self); long files show 3,000 lines at a time. D-044: a Delete button (not on the root) with an optional note for Claude; deleted rows stay struck through until the sync (OV `deleted`, `was`, `delete_note`, `cleanup` sync|claude-code). No statuses on the page for now (owner): only a "changed" tag (edits, notes, new/deleted, requests waiting, `worked` marks from server runs) until the sync.

**Three modes:** on claude.ai: window.claude db (collections nodes, changes, inputs) + sample for the ask box; on the owner's server (apps/project-IDE/server/, D-042/D-043): no window.claude, `api/health` answers, the page uses a db shim over `api/store/*` (page-store files), write-through, ask box → `api/agent` (Claude Code via Agent SDK, SSE, Allow/Refuse); anywhere else: "view only".

**Apply changes (D-046):** the top button sends one page comment to Claude (comments.sendToClaude; the thread's artifact watch wakes this session) and saves an `inputs` doc kind `apply` (count, items, sent_to_claude, thread or not_sent). Treat that wake as "sync the file tree": run ide-sync + ide-build, publish, clear the store, mark the apply input processed LAST (processed_at), then ArtifactComments reply in that thread and resolve it. On the server it is one Claude Code run in the root chat (no worked marks).

**When the owner says "sync the file tree":** ide-sync: read the page store (ArtifactData on the link; on the server the page-store folder), save each input word for word with its answer, write edits into files (how_md word for word, by: owner, then --confirm), knowledge-intake the rest, rebuild, republish, mark inputs processed, delete folded nodes docs.

**Why:** docs are the single source. The page reaches Claude only through a comment sent to Claude (comments capability); mcp send_message was blocked 2026-09-29, don't retry. Related: [[github-sync-plan]].

**Voice (D-060):** server `voice.py` + route `api/voice`, models rotated per `server.config.json`; button only on the owner server. Key value only in `/mnt/project-files/.secrets/test/.env` (outside vision/, never copied to the repo; api.groq.com is blocked from the cloud machine).
