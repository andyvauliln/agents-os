# Agent OS: Shared mechanics (v0.2)

The mechanics every agent shares: when runs start and restart, test and live modes, links and relink, logging, and how configs are merged. What an agent holds inside is in agent-architecture.md. The full safety rules are in safety.md (trading adds its own in the prediction-market domain's `trading-safety.md`), the naming and link rules in conventions.md, and the file formats in data-schemas.md.

## Triggers and cancel-and-restart
<!-- k: id=common-mech-triggers applies=[2.17.2],[27.4],[11.1],[14.1] sources=in-20260929-1455 status=decided -->
Agents run on an interval, or when an important file they watch changes. An important change cancels the current run (if one is going) and starts a new one with the new information. An unimportant change waits for the next scheduled run. Which files are important is set per agent.

### How the scheduler does it
<!-- k: id=common-mech-scheduler applies=[2.17.2],name:*.workers.json,[11.1],[14.1],[16.1],[15.1] sources=D-029,D-030 status=proposed -->
- The interval is the `schedule` of the agent's main-run job in its workers file (like [27.4]); the important files are that job's `on_change` list, with `concurrency: restart`.
- Global rules sit in [11.1] `triggers` (debounce, minimum gap between restarts, maximum restarts per hour, `on_unimportant: "wait_next_run"`) and defaults in [11.1] `schedules`.
- One central `scheduler` [14.1] finds every workers file by scanning `agents/**/configs/*.workers.json` (real files only), runs due jobs through `run-job`, watches `on_change` files, keeps state in [16.1] `scheduler-state.json` and logs to [15.1].

## Test and live modes
<!-- k: id=common-mech-modes applies=[2.17.2],[11.1],[27.2] sources=in-20260929-1455,D-056 status=decided -->
Every service that performs an action has a test mode and a live mode and takes the mode from configuration. The mode is also part of the agent's name. Only the owner approves taking an agent live. Trading adds its own rules in the prediction-market domain's `trading-safety.md` (an account with money).

### Going live
<!-- k: id=common-mech-going-live applies=[2.17.2],[11.1],[27.2],[27.4],[47.2.1],[14.1] sources=D-012,D-023,D-027,D-029,D-056 status=proposed -->
- The default mode is `test` ([11.1] `modes.default_mode`). Live needs both the global `live_allowlist` and an owner-approved run; an agent can never switch itself to live.
- Going live creates a new agent (`...-live`, `parent` = the test agent); names never change. Steps: how-to/promote-to-live.md.
- The stop switch in [11.1] `modes` overrides everything and is checked before every action.
- `cloud`, `desktop` and `github-actions` jobs are always test; agent tests always force test mode.
- Trading adds its own rules in the prediction-market domain's `trading-safety.md` (an owner-approved account, the order stop switch).

## Links and relink
<!-- k: id=common-mech-links applies=[2.17.2],name:*.links.json,name:relink.system.link.js,path:agents/**/subagents.link/*,[14.1],[16.1] sources=D-002,D-020,D-030,D-031 status=decided -->
- Every symlink has `.link` in its name, or sits directly in a `.link` folder such as `subagents.link/` (D-002, D-030).
- An agent's links are individual file links, one per file its logic needs, listed in its own links file `configs/[name].links.json` (D-020, D-031).
- Child links `subagents.link/[child-name]/` are the only folder links; relink builds them from the folder tree (D-030).
- Only the shared `relink` script [14.1] creates or removes links; `init.sh` and everything else call it. It also runs the `check-links` rules and writes the links index [16.1].
- Links are read-only for the agent. Tools never follow `.link` folders recursively. Nothing links into `.secrets/` or any `.claude/`.

### When relink runs
<!-- k: id=common-mech-relink-when applies=[2.17.2],[14.1],[11.10],[10.6],name:settings.json,name:relink.system.link.js,name:init.sh sources=D-031,in-20260930-1153 status=proposed -->
The owner asked for three moments: when a links file changes, when changes are reviewed, and when an agent edits its own links file. Proposed mechanics:
1. **A links file changes:** the `relink` job in [11.10] watches `agents/**/configs/*.links.json` and runs `--changed`, plus one full run a day.
2. **Review time:** git hooks installed by the system `init.sh` [10.6]: `pre-commit` runs `--staged` and blocks the commit if a required link is broken; `post-merge` and `post-checkout` run `--changed`. The owner approving a change in the UI runs it too.
3. **The agent itself:** after editing its links file it runs `node scripts/relink.system.link.js`, and a `PostToolUse` hook in its `.claude/settings.json` does the same.
4. **Setup and removal:** `create-agent`, every `init.sh` and stop-or-delete.

## Logging
<!-- k: id=common-mech-logging applies=[2.17.2],[15],[15.1],[15.2],[15.3],[15.4],[34],[34.1],[34.2] sources=D-009,D-014,D-020,D-025,D-029 status=decided -->
- **Shared logs by source** in the system's `logs/`: [15.1] system (scheduler, triggers, relink and link checks, errors, costs), [15.2] services (test and live actions), [15.3] shared workers, [15.4] sub-agents; plus `subagents.link/` down to each domain's logs.
- **Each agent's own logs** are real files in its `logs/` (like [34]): runs, decisions, cost, `effective-config.json`, `tests.jsonl` [34.2], and each job's runs in `logs/jobs/[job-id]/`. It links only the shared log files it needs (like [34.1]).
- Secret values are never logged; loggers redact anything `load-secret` resolved.
- The log format and retention are still open.

## Config merge order
<!-- k: id=common-mech-config-merge applies=[2.17.2],[11.1],[19.2.4],[27.2],[34],[14.1] sources=D-006,D-014,D-029,D-056,D-058 status=proposed -->
- Lowest to highest: global [11.1] `system.config.json`, then the domain's own config where it has one (like [19.2.4]), then the agent's own config (like [27.2]), then the owner's overrides (stop, pause, approve).
- Objects deep-merge by key; arrays and single values are replaced by the higher layer.
- Jobs come only from each agent's own workers file; routes come from [11.11] unless a job names its model.
- Safety exceptions: a lower layer can only tighten a limit; live needs the allowlist and an owner-approved run; the stop switch overrides everything; secrets appear in no config, only key names or refs.
- At run start `run-agent` [14.1] writes the merged result to the agent's `logs/effective-config.json`. Configs are read at the start of each run, so a shared change applies from every agent's next run.
- Trading adds its own rules in the prediction-market domain's `trading-safety.md` (the domain config layer, risk caps, accounts).

## Open questions
<!-- k: id=common-mech-open applies=[2.17.2],[15],[34],[16.1],[10],[11.13] sources=derived status=open -->
- Log format (JSONL plus an MD run summary?) and retention ([15], [34]).
- How is "new since the last run" tracked: file times or a cursor per agent in [16.1]?
- Should changes to shared configs need owner approval before they reach live agents ([10])?
- Commit the symlinks to git, or rebuild them after every clone and pull ([11.13])?

## Changelog
- v0.2 (2026-10-07): trading parts moved to the prediction-market domain's `trading-safety.md` (D-056, D-058); the kill switch is now the general stop switch; the config merge order names a domain's own config.
- v0.1 (2026-09-30): created from file-tree.md v1.15, vision.md v0.19 and the owner inputs (D-033).
