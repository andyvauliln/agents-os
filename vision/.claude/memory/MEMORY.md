# Project Planning
- Goal: a thorough vision and overview of the system.
- Name and subject: the Agent OS, root `agent-os/` (renamed from trading-os 2026-10-07), for agents of any kind (D-054, D-056). GitHub repo keeps the name trading-oss until the owner renames it.
- [Trading lives in the prediction-market domain](agent-os-trading-domain.md): system level general; later trading domains copy pm; copy trading dropped (D-056, D-058, done 2026-10-07).
- Done 2026-10-09 (D-059, page v48): `agents/trading/` holds `prediction-market/` (copytrading later) and `docs/` with its 3 docs (planning copies vision/docs/trading/); system README and rebuild prompt general; removed trading text in vision/archive/2026-10-09/*-trading-parts.md for pm's own docs later.
- Repository: https://github.com/andyvauliln/trading-oss ONLY (not social_media_app).
- Published 2026-10-07: whole project pushed to branch `claude/project-thread-dj0xqs` under `vision/`, with `HANDOFF.md` at top, for continuing from another account. Keep token use low.
- [Planned items are real files](planned-items-are-real-files.md): materialize.py each build; PR #4 merged 2026-10-12.
- Project IDE on the owner's server (PR #3 merged to main 2026-10-12): `git pull`, then `python3 vision/server/server.py` from the repo top; serves the same page as the claude.ai artifact from the planning files. Request box/Apply changes need `claude-agent-sdk` + Claude Code signed in; mic needs GROQ_API_KEY in `.secrets/test/.env`. Full move into apps/project-IDE/ + agents/system/ not done (optional).

## Knowledge base (/mnt/project-files/vision/docs/, D-033)
- Start at docs/README.md (layers, tag format, flow). Layers: inputs/ (owner inputs word for word + index.json), file-tree.md (one section per [n] object), topic notes (overview, architecture, flows, data-schemas, conventions, safety, glossary, metrics, roadmap, how-to/, common/, feature-map; pm's trading- notes in docs/prediction-market-agents/), history (decisions.md D-001..D-059, changelog.md), index/ (lists; knowledge-map.json).
- How it works: one `{name}.index.md` per node in vision/tree/agent-os/... (D-039); every item has an empty `.meta.json`; metadata names carry no extension (D-057). The page switch is "metadata".
- Every level (system, domain, strategy, trading agent) gets vision, README and rebuild prompt; each rebuild prompt builds only its own folder (D-053).
- Helpers (planning copies): vision/.claude/agents/{knowledge-base-agent,project-ide-agent}.md, skills knowledge-intake, file-index, vision-doc, readme-doc, ide-build, ide-sync; tools vision/tools/ (README.md); draft vision/.claude/CLAUDE.md (no root CLAUDE.md, D-045); page source vision/explorer/.
- [Docs layout and order](claude-folder-docs-layout.md): docs in each agent's docs/ (D-047); vision, README, rebuild prompt (D-048).
- [Human docs style](human-docs-style.md): plain, book-like prose, no [n] refs or ids.
- [Every input goes through knowledge-intake](knowledge-intake-every-input.md): inputs, our answers and system changes.
- Workflow: file every owner input, record decisions as D-0xx, mark our ideas "proposed", keep status honest. Ask before committing. Call the owner "the owner" (they/them).
- Key decisions: system is a domain; one standard agent folder at every level; file links *.link.*; subagents.link/[child]/ (D-030); jobs in configs/[name].workers.json (D-029); links files built by relink (D-031); secrets in git-ignored .secrets/, one .env per mode, key names in secret_keys (D-023, D-027); variant names `[strategy-id].[own-name]-v[N].[platform-model]-[test|live]` (D-032); trading-ui in apps/ (D-045); Apply changes button starts the sync (D-046).
- Open for the owner: scheduler machine (D-029); symlinks or rebuild (D-031); v[N] placement (D-032); model defaults [11.11]; jobs [27.4]; D-058 defaults.
- [GitHub sync plan](github-sync-plan.md): repo = the file tree (D-041); IDE in apps/project-IDE/ (D-043).
- [One file per tab](file-family-plan.md): steps 1-2 done with empty files (2026-10-07); the rest waits.
- [Whole context for every AI](full-context-for-ai.md): the IDE's purpose (D-049).
- [General system plan](general-system-plan.md): plan every change (D-051); next is step 5, the docs at every level, system vision first as the example.
- [Apps](apps-docs-clones-forks.md): own docs; research clones in temp; forks (D-055).
- The thread "Interactive file tree UI" owns the File Tree page and the docs. [File tree explorer sync](file-tree-explorer-sync.md): if the owner says "sync the file tree" in project chat, forward to that thread.
