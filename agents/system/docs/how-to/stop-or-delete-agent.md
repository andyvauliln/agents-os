# Agent OS: Stop or delete an agent (v0.2)

How to stop, retire or delete an agent. The owner can stop and delete agents from the UI (vision §12). Names are never reused, so a deleted agent stays in the registry as retired (D-012).

## Steps
<!-- k: id=howto-stop-or-delete-agent-steps applies=[2.11.5],[27.4],[11.1],[46],[14.1],[16.1],[2.18.1],path:agents/**/subagents.link/*,name:*.links.json sources=D-012,D-029,D-030,D-031,in-20260929-1455,D-056 status=proposed -->
1. **Stop it.** Set `enabled: false` on its jobs in its workers file (like [27.4]); the owner can do this from the UI. This stops new runs. If every outside action must stop at once, the general stop switch in [11.1] `modes` does that.
2. **Domain steps.** Do the stop steps the agent's domain adds (for example, the prediction-market domain's `how-to/stop-trading-agent.md` closes positions and unfunds the account).
3. **To retire without deleting,** set its status to `paused` or `retired` in `index/agents.md` [2.18.1] and stop here.
4. **To delete, archive the agent folder.** Its own logs, data, docs [46], tests and research go with it. Where archives are kept is still open.
5. **Run relink for the project:** from `agents/system/`, `node scripts/system/relink.system.js` (the scheduler's `relink` job also picks the change up). It removes the agent's entries from its parent's `subagents.link/` folders (D-030) and warns about every agent whose links file still points at its files (D-031).
6. **Fix every warned reader:** point its links file entry at another file, set it to `enabled: false`, or remove it.
7. **Update the registry** [2.18.1]: status `retired`; the name stays reserved for ever. Remove its jobs from `index/workers.md` and its sub-agents from `index/subagents.md`.

## Checks
<!-- k: id=howto-stop-or-delete-agent-checks applies=[2.11.5],[16.1],[2.18.1],path:agents/**/subagents.link/* sources=D-012,D-030,D-031,D-056 status=proposed -->
- No job of the agent runs any more ([16.1] `scheduler-state.json`).
- No `subagents.link/` entry points at its folders.
- `node scripts/system/relink.system.js --check` exits 0, and the links index [16.1] shows no link to its files.
- The registry row says `retired`, and the archive keeps its docs for history.

## Changelog
- v0.2 (2026-10-07): trading parts moved to the prediction-market domain's `how-to/stop-trading-agent.md` (D-056, D-058).
- v0.1 (2026-09-30): created from file-tree.md v1.15, vision.md v0.19 and the owner inputs (D-033).
