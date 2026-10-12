# Agent OS: Create an agent (v0.2)

How to create a new agent and plug it into the system. The steps are the same at every level: a domain or any level a domain defines below it (D-022). A domain may add its own steps: for example, the prediction-market domain's `how-to/create-strategy-or-variant.md` covers its strategies and their variants, which a strategy's self-improvement (SI) sub-agent usually makes (D-032). The `create-agent` script [14.1] does most of the work; this runbook says what it must do and what to check afterwards. Naming rules: see conventions.md. Folder layout: see architecture.md and file-tree.md [2.7.1].

## Steps
<!-- k: id=howto-create-agent-steps applies=[2.11.1],[14.1],[4],[2.18.1],[11.11],[27.2],[27.3],[27.4],[40],[41],[46.2],[49.1.1],[49.2.1],[50.1] sources=D-012,D-022,D-024,D-025,D-029,D-030,D-031,D-032,in-20260929-1455,in-20260930-1453-2,D-056 status=proposed -->
1. **Start from an input.** Either an owner input ("create a new agent based on this input", from the UI or the chat; process it first, see process-an-input.md) or a proposal from an SI sub-agent.
2. **Pick the level and the parent.** A domain goes directly under `agents/` [4]. Any other agent goes under its parent, at a level its domain defines.
3. **Name it and check the name.** Follow conventions.md [2.7] and the name format of its domain. `create-agent` [14.1] rejects a malformed name and any name already in the registry [2.18.1], retired ones included, then reserves the name (D-012).
4. **Scaffold the standard folder** [2.7.1]: `.claude/` in the standard layout [2.7.2] (`CLAUDE.md` built on common/common-prompt.md [2.17.3]; `settings.json` that denies `.secrets/live/**` and holds the relink hook), `configs/`, `scripts/`, `logs/`, `data/`, `docs/`, `tests/` (`agents/` and `scripts/`, each with an empty `tests.config.json` and a runner link `run-tests.system.link.js`), `research/` with an empty `index.json`, `package.json`, `requirements.txt`, `init.sh`, `start.sh` (D-024, D-025).
5. **Write its own config** `configs/[agent-name].config.json` (like [27.2]): `agent` (name, type, domain, parent), `mode: test`, its own settings and the fields its domain adds, and `secret_keys` (key names only) if its scripts need keys. A new version sets `parent` to the agent it was cloned from.
6. **Write its links file** `configs/[agent-name].links.json` (like [27.3]): one entry per file its logic needs, plus the default entry for `scripts/relink.system.link.js` (D-031). Format: [11.13] and data-schemas.md.
7. **Run `./init.sh`** (like [40]). It installs the dependencies and runs `relink --agent [agent-name]` [14.1], which builds the agent's file links and its entry in each of its parent's `subagents.link/` folders (D-030, D-031).
8. **Write its docs** in `docs/` (like [46]): `README.md` (what it is, parent, route, mode), `changes.md` (what differs from the parent and what is being tested), `decisions.md`, `notes.md`, and any doc its domain adds.
9. **Set its route** in [11.11] `models.config.json`: an entry in `routes`, or leave it to `defaults_by_type`. If its name carries a platform and model, they must match the route.
10. **Write its jobs file** `configs/[agent-name].workers.json` (like [27.4], format [11.10]) with at least the main run: `type: agent`, a `schedule` (e.g. `every 15m`) and `on_change` for the files whose change must restart the run (D-029). The parent sees it through its `configs/subagents.link/`.
11. **Stay in test mode and run the tests:** `node scripts/run-tests.system.link.js` [30.2] runs both kinds (see add-or-run-tests.md).
12. **Register it:** add a row to `index/agents.md` [2.18.1] (status active, mode test, created date, path) and show it in the UI.
13. **First run:** the scheduler [14.1] starts the main-run job, or the owner runs `./start.sh` [41] by hand.

## Checks
<!-- k: id=howto-create-agent-checks applies=[2.11.1],[2.18.1],[11.11],[27.2],[27.3],[27.4],[16.1],[21.2.2.1],[21.3.1.1],[21.4.1.1],[21.5.1.1],[21.6.1.1],[21.12.3.1],[21.13.3.1] sources=D-012,D-025,D-029,D-030,D-031,D-032,D-056 status=proposed -->
- The name is new in [2.18.1] and matches the format in conventions.md and its domain's.
- Every part of the standard folder exists, including both `tests.config.json` files, both runner links and `research/index.json`.
- `node scripts/relink.system.link.js --check` exits 0: every required link exists, the agent has an entry in each of its parent's `subagents.link/` folders (like [21.2.2.1], [21.3.1.1], [21.4.1.1], [21.5.1.1], [21.6.1.1], [21.12.3.1], [21.13.3.1] for an agent under [21]), and no link points into `.secrets/` or any `.claude/`.
- The config says `mode: test` and holds key names only, never values.
- The main-run job is in the jobs file, and the scheduler shows its next run in [16.1] `scheduler-state.json`.
- Every enabled test shows `last_result: success`.
- `docs/README.md` and `docs/changes.md` are filled in, and the registry row exists.

## Changelog
- v0.2 (2026-10-07): trading parts moved to the prediction-market domain's `how-to/create-strategy-or-variant.md` (D-056, D-058).
- v0.1 (2026-09-30): created from file-tree.md v1.15, vision.md v0.19 and the owner inputs (D-033). Includes D-032: variant names start with the strategy ID; the strategy's SI sub-agent is the usual creator of variants.
