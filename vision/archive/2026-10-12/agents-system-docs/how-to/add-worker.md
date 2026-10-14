# Agent OS: Add a worker or sub-agent (v0.2)

How to add a worker (a script that collects data) or a sub-agent (an AI run that pre-analyses data), run it as a job, and wire its output to the agents that read it. Job fields: see [11.10] and data-schemas.md. Linking: see add-or-change-link.md.

## Steps
<!-- k: id=howto-add-worker-steps applies=[2.11.2],[2.18.2],[2.18.3],[16.1],[14.2],[31],[11.10],[19.2.1],[21.2.1],[27.4],[27.3],[16.2],[16.3],[35.2],[10.1.1],[19.1.1],[21.1.1] sources=D-007,D-008,D-020,D-029,D-031,in-20260929-1452,in-20260930-0938 status=proposed -->
1. **Check what exists.** Look in `index/workers.md` [2.18.2] and in the links index [16.1] `links.index.json` (who reads which file). If a job already produces the data, link its output instead and skip to step 6 (vision §5.11).
2. **Decide where it lives.** Agent-local in the agent's own `scripts/` (like [31]) when one agent needs it; shared when two or more do, in the nearest level both share: their domain's `scripts/` for agents of one domain, the system's [14.2] `scripts/workers/` for agents of different domains. When a second agent needs an agent-local worker, move it there (promotion rule, conventions.md `conv-promotion`).
3. **Write the script** as `[name].worker.[py|js]`. It writes dated files plus a stable `latest.*`: a shared worker to `data/workers/[worker]/` [16.2] with logs in `logs/workers/[worker]/` [15.3]; an agent-local one to the agent's `data/[worker]/` (like [35.2]) and its `logs/`. Keys come only through `load-secret` [14.1], never from the code.
4. **Or write a sub-agent** instead: `.claude/agents/[subagent-name].md` in the level that owns it (system [10.1.1], domain [19.1.1], or a level its domain defines, like [21.1.1]). Its name must be unique (check [2.18.1] and [2.18.3]). It writes to `data/subagents/[name]/latest.md` [16.3] and logs to [15.4]; its model comes from [11.11].
5. **Add a job** to the owning agent's workers file: [11.10] `system.workers.json` for a shared worker, else the agent's own ([19.2.1], [21.2.1], [27.4]). Set `id`, `type` (`script`, or `subagent`, `skill`, `workflow`, `command`), `run`, `schedule` (`every 15m`, `cron 0 22 * * 1-5`, `once 2026-11-03 20:00`, `after [job-id]` or `manual`), `run_on`, `platform` (`none` for a script), `model` (`route` = from [11.11]), `outputs`, `secret_keys` (names only, `local` jobs only), `timeout`, `retries` (D-029).
6. **Link the output into each reader.** Add one entry to each reader's links file (like [27.3]): `to` e.g. `data/[worker-name].link.json`, `from` e.g. `@system/data/workers/[worker-name]/latest.json`, `why`, `required`. Relink runs by itself after the edit.
7. **Restart on change if needed.** If a reader must react at once, add the linked path to its main-run job's `on_change` (like [27.4]). Otherwise the new data waits for its next run.
8. **List it** in `index/workers.md` [2.18.2], and a new sub-agent in `index/subagents.md` [2.18.3].

## Checks
<!-- k: id=howto-add-worker-checks applies=[2.11.2],[2.18.2],[16.1],[11.10],[27.4],[27.3] sources=D-027,D-029,D-031 status=proposed -->
- The scheduler lists the job with a next run in [16.1] `scheduler-state.json`; its first run succeeds and logs to the owner agent's `logs/jobs/[job-id]/`.
- The output folder has a fresh `latest.*` file.
- Every reader's link exists and shows as ok in the links index [16.1].
- No second job collects the same source ([2.18.2]).
- `secret_keys` hold key names only, and no `cloud`, `desktop` or `github-actions` job has any.

## Changelog
- v0.2 (2026-10-07): neutral examples; `polymarket-prices` is now the prediction-market domain's worker [19.3.5]; step 2 follows the promotion rule: the nearest level both agents share (D-056, D-058).
- v0.1 (2026-09-30): created from file-tree.md v1.15, vision.md v0.19 and the owner inputs (D-033).
