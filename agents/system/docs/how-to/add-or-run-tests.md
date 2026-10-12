# Agent OS: Add or run tests (v0.2)

How to add a test to any level and run it. Every level has `tests/agents/` (behaviour of its `CLAUDE.md` and sub-agents) and `tests/scripts/` (its code), each with a `tests.config.json` and a runner link (D-025). Fields: see data-schemas.md. This runbook is [2.11.7] in the file tree.

## Steps
<!-- k: id=howto-add-or-run-tests-steps applies=[2.11.7],name:tests.config.json,name:run-tests.system.link.js,name:[test-id].test.md,name:[test-id].test.[js|py],[34.2],[14.1],[10.8],[19.12],[21.12],[49] sources=D-025,in-20260929-2036,in-20260929-2059 status=proposed -->
1. **Pick the level and the kind:** system [10.8], domain [19.12] or a level its domain defines (like [21.12] or [49]); `agents` for prompt and sub-agent behaviour, `scripts` for code.
2. **Write the test file** in that folder. Agent test: `tests/agents/[test-id].test.md` with the target, the fixtures, how it runs, the expected behaviour and how it is graded. Script test: `tests/scripts/[test-id].test.js` or `.py`, run with node or pytest on fixture data, with no network and no secrets. IDs are `t-agents-NNN` or `t-scripts-NNN`, unique in the level and never reused.
3. **Add an entry** to that folder's `tests.config.json`: `id`, `name`, `target`, `file`, `enabled`, `schedule` (`manual`, `on_change`, `interval:[x]` or `before_promote`), `owner`, `notes`. Leave the state fields to run-tests.
4. **Run it** with the runner link in that folder: `node tests/agents/run-tests.system.link.js --id t-agents-001` or `node tests/scripts/run-tests.system.link.js --id t-scripts-001`. Without `--id` it runs every enabled test of that kind; `--schedule on_change` narrows it.
5. **Read the result.** run-tests writes `last_run`, `last_result` (`success`, `fail`, `error`, `skipped` or `never`), `last_duration_ms` and `fail_count` back into the config, and appends one line per test to the level's `logs/tests.jsonl` (like [34.2]).
6. **If it fails,** write `next_action` (what should be done next) and `notes`.
7. **To run both kinds for a level:** `node scripts/run-tests.system.link.js` [30.2]. The scheduler, `before_promote` and `npm test` use this one.
8. **Turn a test on or off** from the UI or by editing `enabled`.

How an agent test runs: run-tests copies the fixtures into a temporary copy of the level's folder and starts Claude Code headless there (`claude -p` with the scenario), with the mode forced to test and no secrets. Script checks grade it first; a judge sub-agent only for fuzzy expectations.

## Checks
<!-- k: id=howto-add-or-run-tests-checks applies=[2.11.7],name:tests.config.json,[34.2],[2.11.4] sources=D-025,D-056 status=proposed -->
- The test is in `tests.config.json` with a unique id, a target and a schedule.
- After a run, `last_run` and `last_result` are set and `logs/tests.jsonl` has a matching line.
- A failing test has a `next_action`.
- Agent tests ran in test mode, with no secrets and no live actions.
- Before a promotion every enabled test passes (see promote-to-live.md).

## Changelog
- v0.2 (2026-10-07): neutral wording for the levels and for live actions (D-056, D-058).
- v0.1 (2026-09-30): created from file-tree.md v1.15, vision.md v0.19 and the owner inputs (D-033).
