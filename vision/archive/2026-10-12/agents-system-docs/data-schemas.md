# Agent OS: Data schemas (v0.2)

The shape of every JSON, JSONL and Markdown file type in the Agent OS: its fields, a small example, who writes it and who reads it. Each section names the files it covers, so a rule written once holds for every file of that kind. The owner decided that most of these files exist; their exact fields are almost all our proposal, so most sections are `proposed`. Where the field guides of the File Tree page (tools/tabs.py, tools/enrich.py) and file-tree.md [2.13] differ, file-tree.md wins. What happens to these files over time is in flows.md; naming rules are in conventions.md; what may never be stored is in safety.md. The trading files of the prediction-market domain (its config, decisions and orders, positions, the money part of the metrics snapshot) are in that domain's `trading-data-schemas.md`.

## General rules

### Formats: JSON, JSONL and Markdown
<!-- k: id=schema-formats applies=[2.14],name:*.json,name:*.jsonl,name:runs.jsonl*,[15]/**,[16]/**,[34]/**,[35]/** sources=D-005,in-20260929-1455 status=decided -->
- For now all data, configs, state and logs are plain files (D-005): JSON for configs, state and indexes; JSONL (one JSON object per line) for logs that grow; Markdown for text that people and LLMs read.
- There is no database for now.
- Two exceptions exist in the drafts: secrets live in `.env` files (see `schema-env-keys`), and worker logs are plain text `.log` files (see `schema-log-workers`; whether they become JSONL is open, [15]).

### Encoding, time and units
<!-- k: id=schema-encoding-time-units applies=[2.14],name:*.json,name:*.jsonl,name:runs.jsonl*,[15]/**,[16]/**,[34]/**,[35]/** sources=derived,D-056 status=proposed -->
- UTF-8, LF line endings, no BOM. JSON that people edit (configs) is pretty-printed with 2 spaces. JSONL has one compact object per line.
- Every timestamp is UTC in ISO 8601 with `Z`: `2026-09-29T10:03:12Z`. A date alone is `YYYY-MM-DD`. File names use `YYYY-MM-DDTHH-MM` (no colons), e.g. `2026-09-29T10-05.json`. Only schedule strings use a local time, with their own `timezone` field (`schema-workers-schedule`).
- The unit is in the field name: `_usd` (US dollars), `_pct` (0 to 100), `_bps` (basis points), `_ms` and `_sec` for durations. The drafts also use `_s` (`duration_s`); one of the two should win. Job durations are short strings: `10m`, `2h`.
- Paths inside a file are relative to the folder of the agent that owns the file, unless they start with `agents/` (from the repo root) or, in links files only, with an `@` short form (`schema-links-from`).
- Readers ignore fields they do not know. Writers keep unknown fields when they rewrite a file.
- Secret values never appear in any field of any file: see safety.md.

### Agent IDs
<!-- k: id=schema-agent-ids applies=[2.14],[2.18.1],name:*.json,name:*.jsonl,name:runs.jsonl* sources=D-012,in-20260929-1607 status=decided -->
Every agent's globally unique name is its ID in every file: `agent`, `level`, `assigned_agent`, `ran_by`, `owner`, route keys, registry rows, `@[name]` link sources (D-012). Names are never changed or reused, so an agent ID in an old log still means exactly one agent. The name format is in conventions.md.

### Other IDs
<!-- k: id=schema-other-ids applies=[2.14],name:*.workers.json,name:tests.config.json,path:agents/**/research/index.json,name:runs.jsonl*,[2.10] sources=D-025,D-029,derived,D-056 status=proposed -->
| Thing | Format | Unique within | Example |
|---|---|---|---|
| Job | kebab-case | its workers file | `main-run` |
| Test | `t-agents-NNN`, `t-scripts-NNN` | its level | `t-scripts-001` |
| Research item | `r-NNNN` | its level | `r-0001` |
| Run | `r-YYYYMMDD-HHMM` | its agent | `r-20260929-1000` |
| Owner input | `in-YYYYMMDD-HHMM`, `-2` when two share a minute | the knowledge base | `in-20260930-1453-2` |

- Across the system a local id is written `[agent-id]/[id]`, e.g. `[agent-id]/t-scripts-001`.
- Ids are never reused.
- Open: run ids and research ids both start with `r-`. A different run prefix (e.g. `run-`) would avoid mix-ups.

### Stable latest.* outputs
<!-- k: id=schema-latest-files applies=[16.2],[16.3],[15.3],[35.2],[35.1],[34.1],[31],[32],[14.2] sources=D-020,D-031,derived,D-007,D-010,D-056 status=proposed -->
- Every producer (worker, sub-agent, agent output) writes a dated file and also replaces one stable file next to it: `latest.json`, `latest.md` or `latest.log`.
- Links always point at the stable file, so they do not break when dated files rotate. Readers of "now" read `latest.*`; history tools read the dated files.
- Write the dated file first, then replace `latest.*` in one step (write a temp file, then rename), so a reader never sees half a file.
- A job lists its `latest.*` files in `outputs` (`schema-workers-job-fields`).
- Worker outputs sit in one folder per producer: shared `data/workers/[worker]/` [16.2], agent-local `data/[worker-or-source]/` [35.2]. It holds dated files `YYYY-MM-DDTHH-MM.json`, `latest.json` and derived files (e.g. `clean.json` from [32]).
- Proposed envelope for every output: an object with `ts` (when the data was fetched, UTC), `producer` (worker or agent name) and one named list of rows. Rows carry their own ids and times. The row fields of each producer are written down where the producer is described, and grow as workers are built.
- How long dated files are kept is open (vision §6 Q10).

### schema_version and schema changes
<!-- k: id=schema-versioning applies=[2.14],[2.9],[11.1],[11.11],name:*.workers.json,name:*.links.json,name:tests.config.json,path:agents/**/research/index.json,[16.1],[47.3] sources=derived status=proposed -->
- Every JSON config, state and index file we own starts with `"schema_version": 1`. Claude Code's and npm's own files (`settings.json`, `package.json`) do not. JSONL lines and Markdown files carry no version: this doc versions their shape.
- Bump the number when a field is renamed or removed or changes meaning. Adding an optional field needs no bump.
- Whoever adds or changes a file type updates its section here in the same change, and adds a line to changelog.md [2.9].
- Open: should machine-checkable JSON Schema files exist too, with this doc as the readable view ([2.14])?

## Configs

### system.config.json [11.1]
<!-- k: id=schema-system-config applies=[11.1],name:system.config.link.json,[14.1] sources=D-006,in-20260929-1537,D-027,D-029,D-056 status=proposed -->
The one global config (D-006): everything controllable globally, except jobs (each agent's workers file, D-029) and routing ([11.11]). The owner decided one file with sections; the sections below are proposed. A section moves to its own file once it gets long. The prediction-market domain's trading settings (risk limits, trading accounts, venues, the currency, the order stop switch, trade notifications) are in its own config [19.2.4] (`trading-data-schemas.md`).

| Section | Fields | Meaning |
|---|---|---|
| `schema_version` | integer | shape version |
| `defaults` | `timezone`, `log_level` (debug, info, warn, error), `run_timeout_sec`, `by_agent_type.<type>.allowed_actions`, `by_agent_type.<type>.memory` | global defaults; types: system, domain, main, sub, support, si, and the types a domain adds |
| `modes` | `default_mode` (`test`), `kill_switch` (bool), `live_allowlist` (agent names), per-service test or live | who may act live; the kill switch is the general stop switch: it stops every outside action and is checked before every action |
| `schedules` | `timezone`, `<agent type>` (default schedule string for a new agent's main run), `max_concurrent_runs`, `quiet_hours` (`null` or `{from, to}`), `allowed_run_on`, `max_ai_cost_usd_per_day` | defaults for every workers file |
| `triggers` | `important` (path patterns), `debounce_sec`, `min_restart_gap_sec`, `max_restarts_per_hour`, `on_unimportant` (`wait_next_run`) | common restart rules; an agent's own important files are its main-run job's `on_change` |
| `notifications` | `channels` (`ui` first), `events.<event>` (low, medium, high) for `agent_error`, `promotion_proposed`, `kill_switch`, `live_action`, and the events a domain adds | who hears what |

```json
{
  "schema_version": 1,
  "defaults": { "timezone": "UTC", "log_level": "info", "run_timeout_sec": 600,
                "by_agent_type": { "si": { "allowed_actions": ["create_test_agent"], "memory": true } } },
  "modes": { "default_mode": "test", "kill_switch": false, "live_allowlist": [] },
  "schedules": { "timezone": "UTC", "main": "every 15m", "domain": "every 4h", "si": "cron 0 3 * * *",
                 "max_concurrent_runs": 4, "quiet_hours": null, "allowed_run_on": ["local", "cloud"], "max_ai_cost_usd_per_day": 20 },
  "triggers": { "important": ["data/**/*digest*"], "debounce_sec": 30, "min_restart_gap_sec": 120, "max_restarts_per_hour": 6, "on_unimportant": "wait_next_run" },
  "notifications": { "channels": ["ui"], "events": { "agent_error": "medium", "promotion_proposed": "medium", "kill_switch": "high", "live_action": "high" } }
}
```

- **Writers:** system-support agents; changes to `modes` need owner approval (recorded in decisions.md [2.6]).
- **Readers:** every agent through its file link (like [27.1]), `run-agent` (merges it into `effective-config.json`, see `schema-effective-config`), the scheduler (`schedules`, `triggers`), `load-secret` (`modes`), the notifier and the UI.
- **Open:** how `triggers.important` combines with each job's `on_change` is not settled.

### Agent config [27.2]
<!-- k: id=schema-agent-config applies=[27.2],[27] sources=D-006,D-012,D-014,D-022,D-027,D-029,D-031,D-056 status=proposed -->
Each agent's own settings, a real file in its `configs/` (D-014). Shape proposed; which settings are individual and which common is still open (D-006). The prediction-market domain adds its trading fields (`trading-data-schemas.md`).

| Field | Type | Req. | Meaning |
|---|---|---|---|
| `agent.name` | agent name | yes | its permanent ID (D-012) |
| `agent.type` | `system`, `domain`, or a level its domain defines | yes | its level (D-022) |
| `agent.domain` | text | agents in a domain | where it sits |
| `agent.parent` | agent name or `null` | yes | the agent it was cloned from; a live agent's parent is its test agent |
| `agent.created` | date | yes | |
| `mode` | `test`, `live` | yes | requested mode; live also needs the allowlist and an owner-approved run |
| `secret_keys` | list of `.env` key names or prefixes | no | the only keys `load-secret` gives this agent's scripts (D-027) |

```json
{
  "agent": { "name": "[agent-id]", "type": "[level]", "domain": "[domain]", "parent": null, "created": "2026-09-29" },
  "mode": "test",
  "secret_keys": ["[PROVIDER]_[ACCOUNT]_*"]
}
```

- **Not in this file:** routes ([11.11]), jobs (the workers file, D-029), links (the links file, D-031).
- **Level equivalents:** the template [2.7.1] gives every level a `configs/[agent-id].config.json` (`agent.type` `domain` or a level its domain defines). At the system level it would clash with the global [11.1] `system.config.json` (open).
- **Writers:** `create-agent` [14.1], for the level that plans the new agent (`flow-user-create-agent`). Whether the agent may edit its own config is open ([27]).
- **Readers:** `run-agent`, `load-secret`, `run-tests` (forces `mode: test`), the UI.

### models.config.json [11.11]
<!-- k: id=schema-models-config applies=[11.11],name:models.config.link.json,[2.18.6] sources=D-011,D-029,in-20260929-1545,in-20260929-1455 status=proposed -->
Which platform and model every AI-using object uses (D-011), plus the list of platforms. Fields proposed.

| Field | Values | Meaning |
|---|---|---|
| `schema_version` | integer | shape version |
| `platforms.<platform>.status` | `default`, `supported`, `supported-not-connected`, `later` | whether it can be used now |
| `platforms.<platform>.secret_keys` | key names | keys needed to call it (D-027) |
| `models.<model>.platform` | platform name | who serves it |
| `models.<model>.effort` | `low`, `medium`, `high`, `xhigh` | default effort |
| `defaults_by_type.<type>` | model name | types: `main`, `domain`, `si`, `sub`, `worker`, `support` |
| `routes.<name>` | model name | one named agent, sub-agent or worker; wins over the type default |

```json
{
  "schema_version": 1,
  "platforms": { "claude-code": { "status": "default", "secret_keys": ["ANTHROPIC_API_KEY"] }, "cursor": { "status": "supported" },
                 "openrouter": { "status": "supported-not-connected" }, "codex": { "status": "later" }, "kimi": { "status": "later" } },
  "models": { "opus-5.5": { "platform": "claude-code", "effort": "xhigh" }, "sonnet-5.5": { "platform": "claude-code", "effort": "medium" },
              "composer-2.5": { "platform": "cursor" } },
  "defaults_by_type": { "main": "opus-5.5", "domain": "opus-5.5", "si": "opus-5.5", "sub": "composer-2.5", "worker": "composer-2.5", "support": "sonnet-5.5" },
  "routes": { "[agent-id]": "opus-5.5", "news-digest": "sonnet-5.5" }
}
```

- **Lookup:** a job's own `model` (D-029) wins; `model: "route"` means `routes[name]`, else `defaults_by_type[type]`. The model must sit on a platform whose status allows use. When an agent's name carries its platform and model (e.g. `opus55`), that part must match its route; `create-agent` [14.1] checks it.
- **Writers:** system-support agents; SI sub-agents propose route changes (a route change makes a new test agent). **Readers:** `run-job`, `run-agent`, the index [2.18.6], the UI.
- **Open:** which name a `skill`, `workflow` or `command` job is routed by (its job id or its owner agent).

### Workers file (jobs)
<!-- k: id=schema-workers-file applies=name:*.workers.json,[14.1],[2.18.2] sources=D-029,in-20260930-0938 status=decided -->
What the owner asked for (D-029): every agent, at every level, has one jobs file in its `configs/`, `[name].workers.json` ([name] rule in conventions.md): [11.10], [19.2.1], [21.2.1], [27.4]. In it the owner sees and changes everything the agent runs: on or off, the schedule (every N, cron, once on a special date, after another job, manual), where it runs (local headless, cloud, desktop, GitHub Actions), the platform and the model. A job is a plain script or an AI run (the agent itself, a sub-agent, a skill, a workflow or a command), and an AI run carries a prompt, a workspace, skills and tool limits.

#### Job fields
<!-- k: id=schema-workers-job-fields applies=name:*.workers.json,[14.1],[2.18.2] sources=D-029,in-20260930-0938 status=proposed -->
Top level: `schema_version`, `agent` (the owner agent's name), `defaults` (any job field; fills what a job leaves out), `jobs[]`.

| Field | Values | Req. | Meaning |
|---|---|---|---|
| `id` | kebab-case, unique in the file | yes | the job's name; its logs go to `logs/jobs/[id]/` |
| `enabled` | bool | yes | off = kept but never runs; pause by turning off, never by deleting |
| `purpose` | text | yes | one line |
| `type` | `script`, `agent`, `subagent`, `skill`, `workflow`, `command` | yes | `agent` = the agent's own session in its folder |
| `run` | command line, or the sub-agent, skill, workflow or `/command` name | not for `agent` | what to run |
| `schedule` | see `schema-workers-schedule` | yes | when |
| `timezone` | IANA zone | no | for `cron` and `once` |
| `run_on` | `local`, `cloud`, `desktop`, `github-actions` | no (`local`) | see `schema-workers-run-on` |
| `platform` | `none`, `claude-code`, `cursor`, `codex` | yes | `none` for scripts |
| `model`, `effort` | `route` or a model name; `low` to `max` | AI runs | `route` = look it up in [11.11] |
| `prompt` | text or `@path` | AI runs | `@path` reads a prompt file in the workspace |
| `workspace` | folder | no | where the run starts; default the owner agent's folder |
| `allowed_tools`, `permission_mode`, `max_turns`, `max_cost_usd` | list; `default`, `acceptEdits`, `plan`; integer; number | no | limits for a headless AI run |
| `secret_keys` | key names | no | only for `local` jobs (D-027) |
| `inputs`, `outputs` | lists of paths | no | outputs are `latest.*` files others may link |
| `on_change` | list of paths | no | a change starts the job; for the main run it cancels and restarts the current run |
| `timeout`, `retries`, `concurrency` | duration; integer; `skip`, `queue`, `restart` | no | `concurrency` = what to do if the last run is still going |
| `mode` | `test`, `live` | no (`test`) | live needs owner approval and a live-allowed agent |
| `notify` | `never`, `failure`, `always` | no | when the owner hears about a run |

```json
{
  "schema_version": 1,
  "agent": "[agent-id]",
  "defaults": { "timezone": "UTC", "run_on": "local", "mode": "test", "notify": "failure", "concurrency": "skip" },
  "jobs": [
    { "enabled": true, "id": "main-run", "purpose": "The agent's main run (test mode)", "type": "agent",
      "schedule": "every 15m", "platform": "claude-code", "model": "opus-5.5", "effort": "high", "prompt": "@docs/prompts/main-run.md",
      "allowed_tools": ["Read", "Bash(node scripts/*)", "Bash(python scripts/*)", "Write(data/**)"], "permission_mode": "acceptEdits",
      "max_turns": 30, "max_cost_usd": 1, "on_change": ["data/[input].link.json"], "secret_keys": ["[PROVIDER]_[ACCOUNT]_*"],
      "timeout": "10m", "concurrency": "restart" },
    { "enabled": true, "id": "[worker-name]", "purpose": "Fetch the data only this agent needs", "type": "script",
      "run": "python scripts/[worker-name].worker.py", "schedule": "every 15m", "platform": "none",
      "outputs": ["data/[worker-name]/latest.json"], "timeout": "3m", "retries": 2 },
    { "enabled": true, "id": "clean-data", "purpose": "Clean and normalise the fetched data", "type": "script",
      "run": "node scripts/clean-data.system.js", "schedule": "after [worker-name]", "platform": "none", "timeout": "2m" }
  ]
}
```

- **Runtime state is never written here:** last run, result, next run and fail count live in [16.1] `scheduler-state.json` (`schema-scheduler-state`) and each run in `logs/jobs/[id]/` (`schema-job-logs`). So this file changes only when someone changes a job.
- **A change to a job's logic** (prompt, model, tools, inputs) is a config change and makes a new agent version; turning it on or off or moving its time does not ([27.4]).
- **Writers:** the owner (Jobs tab of the UI), the owner agent's domain or SI sub-agent (proposals). **Readers:** the scheduler and `run-job` [14.1], the index [2.18.2], the UI.

#### Schedule strings
<!-- k: id=schema-workers-schedule applies=name:*.workers.json,[11.1],[14.1] sources=D-029,in-20260930-0938 status=proposed -->
| Form | Meaning |
|---|---|
| `every 15m`, `every 6h`, `every 1d` | a fixed interval |
| `cron 0 22 * * 1-5` | five-field cron, in the job's time zone |
| `once 2026-11-03 20:00` | one time on that date, then shown as done |
| `after [job-id]` | when that job succeeds (a job in the same file; across files is open) |
| `manual` | only from the UI or a command |

Time zone: the job's `timezone`, else the file's `defaults`, else [11.1] `defaults.timezone`.

#### Where a job runs
<!-- k: id=schema-workers-run-on applies=name:*.workers.json,[11.1],[14.1] sources=D-029 status=proposed -->
| `run_on` | Runs on | Gets |
|---|---|---|
| `local` (default) | headless on the machine that runs the scheduler | local files, links, test secrets |
| `cloud` | the platform's cloud (Claude Code routines, Codex cloud, Cursor background agents) | a fresh repo copy; no local files, no secrets; Claude Code routines at most hourly |
| `desktop` | a Claude desktop scheduled task | runs only while the app is open |
| `github-actions` | a scheduled workflow in the repo | the repo, no secrets |

`cloud`, `desktop` and `github-actions` jobs get no `secret_keys` and are always `test`, so they never act live. [11.1] `schedules.allowed_run_on` limits which values are allowed at all. `run-job` [14.1] turns an AI job into the platform's headless command: `claude -p`, `cursor-agent -p` or `codex exec`.

### Links file
<!-- k: id=schema-links-file applies=name:*.links.json,[14.1],[16.1] sources=D-031,in-20260930-1153 status=proposed -->
The format of every agent's `configs/[name].links.json` ([11.13], [19.2.3], [21.2.3], [27.3]). What the file is for: agent-architecture.md (`common-agent-links-file`). Fields proposed (D-031).

Top level: `schema_version`, `agent` (the owner agent's name), `links[]`.

| Field | Values | Req. | Meaning |
|---|---|---|---|
| `enabled` | bool | yes | off = relink removes the symlink, the entry stays |
| `to` | path in the agent's own `configs/`, `scripts/`, `logs/`, `data/`, `docs/`, `tests/` or `research/` | yes | where the link appears; the name carries `.link` |
| `from` | see `schema-links-from` | yes | the one real file it points at |
| `why` | text | yes | what the agent uses it for |
| `required` | bool | yes | true: a missing target is an error and the main run does not start; false: a warning, and the link appears once the file exists |
| `added_by` | `create-agent`, the agent, its SI sub-agent, `owner` | yes | who added it |
| `added` | date | yes | when |

```json
{
  "schema_version": 1,
  "agent": "[agent-id]",
  "links": [
    { "enabled": true, "to": "configs/system.config.link.json", "from": "@system/configs/system.config.json",
      "why": "global modes, schedules, triggers", "required": true, "added_by": "create-agent", "added": "2026-09-29" },
    { "enabled": true, "to": "data/[worker-name].link.json", "from": "@system/data/workers/[worker-name]/latest.json",
      "why": "main input of each run", "required": true, "added_by": "create-agent", "added": "2026-09-29" },
    { "enabled": true, "to": "data/[output].link.json", "from": "@domain/data/[output]/latest.json",
      "why": "an input its domain makes for its agents", "required": true, "added_by": "create-agent", "added": "2026-09-29" },
    { "enabled": true, "to": "data/news-digest.link.md", "from": "@system/data/subagents/news-digest/latest.md",
      "why": "test whether the news digest helps", "required": false, "added_by": "[si-subagent-name]", "added": "2026-10-02" },
    { "enabled": true, "to": "scripts/relink.system.link.js", "from": "@system/scripts/system/relink.system.js",
      "why": "rerun after editing this file", "required": true, "added_by": "create-agent", "added": "2026-09-29" }
  ]
}
```

- **Change record:** each added link (`+ to <- from: why`) or removed link (`- to: why`) goes into the agent's `docs/changes.md` under `Links` (`schema-changes-md`).
- **Writers:** `create-agent` writes the first version; then the agent itself, its SI sub-agent and the owner (Links tab of the UI). **Readers:** `relink` and `check-links` [14.1], the links index [16.1], the UI.

#### The from grammar
<!-- k: id=schema-links-from applies=name:*.links.json,[14.1],[16.1],[2.18.1] sources=D-031,D-012,in-20260930-1153,D-056 status=proposed -->
| Form | Points into | Example |
|---|---|---|
| `agents/<path>` | that path from the repo root | `agents/system/docs/safety.md` |
| `@system/<path>` | `agents/system/` | `@system/data/workers/[worker-name]/latest.json` |
| `@domain/<path>` | the agent's own domain folder | `@domain/data/[output]/latest.json` |
| `@[level]/<path>` | the agent's own folder at a level its domain defines | for example, in the prediction-market domain, `@strategy/docs/strategy.md` |
| `@[name]/<path>` | the folder of the domain or agent with that unique name, looked up in the registry [2.18.1] | `@[domain-folder]/data/[output]/latest.json`, `@[agent-id]/data/[output]/latest.json` |

- `@[name]` keeps working when the target folder moves, because relink looks the name up on every run.
- `@[level]` means nothing above that level, and `@domain` from a domain agent is the domain itself.
- The first `@[name]` example names a domain by its folder (`@[domain-folder]/…`). Whether its level ID (e.g. `[code]-domain-agent`, [2.7.2]) also works is open.

#### Link rules
<!-- k: id=schema-links-rules applies=name:*.links.json,[14.1] sources=D-020,D-023,D-030,D-031 status=proposed -->
- File links only (D-020): `from` is one real file. If it is itself a link, relink points at the real file behind it, so there are no chains.
- Never a target in `.secrets/` (D-023) or in any `.claude/` (D-030).
- `to` is always inside the agent's own folders, never inside `subagents.link/`.
- Links are relative symlinks and read-only for the agent.
- Child links (`subagents.link/`, D-030) are never listed here: relink builds them from the folder tree.
- Open: commit the symlinks to git, or rebuild them after every clone (proposed: commit). May an agent link any file of another agent, or only files that agent lists in its jobs' `outputs`? Does a link change bump the agent's version `v[N]` ([27.3])?

### Claude Code settings
<!-- k: id=schema-claude-settings applies=name:settings.json,name:settings.local.json sources=D-024,D-027,D-031 status=proposed -->
The standard Claude Code files at every level ([10.1.6], [19.1.6], [21.1.6], [24.6]; local overrides [10.1.7], [19.1.7], [21.1.7], [24.7]). Keys this system relies on:
- `model`: default model for sessions at this level (runs started by `run-job` take their model from the job or [11.11]).
- `permissions.deny`: must deny live secrets at every level, e.g. `Read(**/.secrets/live/**)` and `Edit(**/.secrets/live/**)` (D-027; rules in safety.md).
- `permissions.allow`: what runs without asking, e.g. `Bash(node scripts/*)`.
- `env`: e.g. `AGENT_OS_ENV` (`test` or `live`), the name [47] uses (it was `TRADING_OS_ENV`; one draft example said `TRADING_OS_MODE`).
- `hooks.PostToolUse`: after Claude edits or writes a file (matcher on Edit, Write, MultiEdit), run relink when a `configs/*.links.json` changed (D-031), and run the `on_change` tests.
- `statusLine`, `outputStyle`: what the session shows and how it answers.

`settings.local.json` holds personal overrides only (e.g. `model`, `env.LOG_LEVEL`), is git-ignored [48] and is never needed for an agent to run.

```json
{
  "model": "opus",
  "permissions": { "deny": ["Read(**/.secrets/live/**)", "Edit(**/.secrets/live/**)"], "allow": ["Bash(node scripts/*)", "Bash(python3 scripts/*)"] },
  "env": { "AGENT_OS_ENV": "test" },
  "hooks": { "PostToolUse": [ { "matcher": "Edit|Write|MultiEdit", "hooks": [
    { "type": "command", "command": "node scripts/relink.system.link.js --if-edited 'configs/*.links.json'" },
    { "type": "command", "command": "node scripts/run-tests.system.link.js --schedule on_change" } ] } ] },
  "outputStyle": "concise"
}
```

### Claude Code prompt files
<!-- k: id=schema-claude-md-files applies=name:*-agent.md,name:[subagent-name].md,name:[skill-name]/SKILL.md,name:[command-name].md,name:[topic].md,name:[style-name].md,name:[subagent-name]/MEMORY.md,name:CLAUDE.md sources=D-008,D-011,D-018,D-024 status=proposed -->
Markdown files in the standard `.claude/` layout ([2.7.2]). The frontmatter fields this system relies on:

| File | Frontmatter | Body |
|---|---|---|
| `agents/[name].md` (sub-agent) | `name` (unique, D-012), `description` (when to use it), `tools`, `memory` (`project`, `local`, none) | instructions; the model comes from [11.11], not from here (D-011) |
| `skills/[name]/SKILL.md` | `name`, `description` | steps; supporting files sit next to it |
| `commands/[name].md` | `description`, `argument-hint` | a prompt that may use `$ARGUMENTS` |
| `rules/[topic].md` | `paths` (globs) | the rule; loaded only for matching files |
| `output-styles/[name].md` | `name`, `description` | how to answer |
| `agent-memory/[name]/MEMORY.md` | none | dated lessons and pointers (e.g. `see r-0001`), never the research itself |
| `CLAUDE.md` | none | the level's prompt: role, what to read first, links, each run, never; built on common-prompt.md [2.17.3] |

### package.json
<!-- k: id=schema-package-json applies=name:package.json sources=derived status=proposed -->
- `name`: the agent's name; `private: true`; `type: "module"`.
- `scripts.start`: `./start.sh`; `scripts.test` runs both test kinds: `node scripts/run-tests.system.link.js` in an agent whose `scripts/` has that link (like [30.2]); at the levels whose `scripts/` has no such link (the system and domain levels, for example), `node tests/agents/run-tests.system.link.js && node tests/scripts/run-tests.system.link.js`.
- `dependencies`: the JS libraries its own scripts need. At the system level [10.4]: the shared scripts' libraries.
- Open: dependencies per agent, or shared through a workspace at the root ([38]).

## Secrets metadata

### .env key names
<!-- k: id=schema-env-keys applies=[47.1.1],[47.2.1],[47.3] sources=D-027,in-20260930-0804,in-20260930-0812 status=proposed -->
The owner decided (D-027): all test keys sit in one `.secrets/test/.env`, one `KEY=value` per line, keys prefixed per account or platform, and `live/.env` uses the same key names. The naming pattern below is proposed.
- `UPPER_SNAKE_CASE`.
- Account keys: `[PROVIDER]_[ACCOUNT]_[WHAT]` (the prediction-market domain's trading account keys: `trading-data-schemas.md`).
- Platform keys: `[PROVIDER]_[WHAT]`, e.g. `ANTHROPIC_API_KEY`, `OPENROUTER_API_KEY`.
- Alert channels: `NOTIFY_[CHANNEL]_[WHAT]`, e.g. `NOTIFY_TELEGRAM_BOT_TOKEN`.
- Mode: `AGENT_OS_ENV` (`test` or `live`).
- Configs and jobs name keys, or a prefix glob such as `[PROVIDER]_[ACCOUNT]_*`, in `secret_keys`; never a value.
- The real key list starts empty and grows as agents need keys (in-20260930-0812). Values appear nowhere but the `.env` files: not here, not on the File Tree page.

### secrets.index.json [47.3]
<!-- k: id=schema-secrets-index applies=[47.3] sources=D-023,D-027 status=proposed -->
Metadata only, never values. One entry per key group:

| Field | Values | Meaning |
|---|---|---|
| key of the entry | `.env` key or prefix glob | e.g. `[PROVIDER]_[ACCOUNT]_*` |
| `kind` | `wallet`, `api-key`, `token` | what sort of secret |
| `env` | `test`, `live` | which file holds it |
| `used_by` | list | accounts, platforms or workers that need it |
| `created`, `rotate_by` | dates | the notifier warns before `rotate_by` |

```json
{
  "schema_version": 1,
  "[PROVIDER]_[ACCOUNT]_*": { "kind": "api-key", "env": "test", "used_by": ["[account-id]"], "created": "2026-09-29", "rotate_by": "2026-12-29" },
  "ANTHROPIC_API_KEY": { "kind": "api-key", "env": "test", "used_by": ["platform:claude-code"], "created": "2026-09-29", "rotate_by": null }
}
```

- **Readers:** the notifier, the UI, the add-account-or-secret runbook.
- **Open:** [47] still keys entries by the D-023 `secret_ref` (e.g. `test/[account]`); with one `.env` per mode (D-027) the key group is the natural key. How an entry marks a group that exists in both files (same names, D-027) is open.

#### Keeping the index current
<!-- k: id=schema-secrets-index-sync applies=[47.3],[47.1.1],[47.2.1],[10.1.1.2] sources=in-20260930-0812-2,D-033 status=decided -->
The owner asked that this file is updated automatically every time a key is added to an `.env` file, by an agent that checks all changes and updates the related files (in-20260930-0812-2). That agent is the knowledge agent [10.1.1.2] (D-033), or a system-support agent it hands the change to.

## System state and indexes

### links.index.json [16.1]
<!-- k: id=schema-links-index applies=[16.1],[14.1] sources=D-031 status=proposed -->
Every link in the project, written only by `relink` [14.1] at the end of each run. Read by the UI, `check-links`, `relink --changed` (to find the agents a moved or deleted target affects), the add-or-change-link runbook ("who else reads this file") and stop-or-delete (who still points at an agent).

| Field | Values | Meaning |
|---|---|---|
| `schema_version`, `built` | integer, time | |
| `links[].agent` | agent name | who owns the link |
| `links[].kind` | `file`, `child` | a links-file entry, or a `subagents.link/` folder link |
| `links[].to` | path from the repo root | where the symlink is |
| `links[].from` | as written in the links file | empty for child links |
| `links[].target` | path from the repo root | the real file or folder it resolves to |
| `links[].required`, `links[].enabled` | bool | copied from the links file |
| `links[].status` | `ok`, `missing`, `broken`, `disabled`, `blocked` | `blocked` = the target is forbidden (`.secrets/`, `.claude/`) |

```json
{ "schema_version": 1, "built": "2026-10-02T04:00:12Z", "links": [
  { "agent": "[agent-id]", "kind": "file", "to": "agents/[domain-folder]/[agent-id]/data/[worker-name].link.json",
    "from": "@system/data/workers/[worker-name]/latest.json", "target": "agents/system/data/workers/[worker-name]/latest.json", "required": true, "enabled": true, "status": "ok" } ] }
```

### scheduler-state.json [16.1]
<!-- k: id=schema-scheduler-state applies=[16.1],[14.1] sources=D-029 status=proposed -->
Runtime state of every job, written only by the scheduler [14.1]. Keyed `[agent]/[job-id]`:

| Field | Values | Meaning |
|---|---|---|
| `last_run`, `next_run` | time | |
| `last_result` | `ok`, `error`, `timeout`, `cancelled`, `skipped` | |
| `last_duration_sec` | number | |
| `fail_count` | integer | failures in a row; reset by a success |
| `running_since` | time or `null` | set while a run is going |
| `done` | bool | a `once` job that has run |

```json
{ "schema_version": 1, "jobs": {
  "[agent-id]/main-run": { "last_run": "2026-09-29T10:03:12Z", "last_result": "ok", "last_duration_sec": 88,
    "next_run": "2026-09-29T10:18:12Z", "fail_count": 0, "running_since": null } } }
```

Readers: the UI, the index [2.18.2], SI sub-agents, metrics (`metric-errors`).

### run-state.json and read cursors [16.1]
<!-- k: id=schema-run-state applies=[16.1],[14.1] sources=derived status=open -->
A proposed `data/system/run-state.json`: `cursors` (per agent, per linked input: the time it last read) and `run_state` (per agent: `status`, current `run`, `started`). Whether "new since the last run" is tracked by cursors or by file times is open ([16], vision §5.2), so this file may not be needed.

```json
{ "cursors": { "[agent-id]": { "data/[input].link.json": "2026-09-29T10:05:00Z" } },
  "run_state": { "[agent-id]": { "status": "running", "run": "r-20260929-1000", "started": "2026-09-29T10:03:12Z" } } }
```

### Index tables [2.18]
<!-- k: id=schema-index-tables applies=[2.18.1],[2.18.2],[2.18.3],[2.18.4],[2.18.5],[2.18.6] sources=D-012,D-029,D-030,D-056 status=proposed -->
Markdown tables, one row per item; retired items keep their row.

| File | Columns |
|---|---|
| `agents.md` [2.18.1] (the registry, D-012) | name, type, domain, parent, route, mode, status (`active`, `paused`, `retired`), created, path |
| `workers.md` [2.18.2] | owner agent, job id, type, schedule, run_on, platform, model, enabled, outputs, readers |
| `subagents.md` [2.18.3] | name, level, path, role (pre-analysis, self-improvement, support), input, output, memory path, job, route, used by |
| `services.md` [2.18.4] | service, mode, accounts (ids only) |
| `apps.md` [2.18.5] | repo, version, used by |
| `models.md` [2.18.6] | platform, model, status, effort, routed from |

```markdown
| name | type | domain | parent | route | mode | status | created | path |
|---|---|---|---|---|---|---|---|---|
| [agent-id] | [level] | [domain] | - | opus-5.5 | test | active | 2026-09-29 | agents/[domain-folder]/[agent-id]/ |
```

- The prediction-market domain lists its trading accounts in its own `index/accounts.md` (`trading-data-schemas.md`).
- `workers.md` is built by scanning `agents/**/configs/*.workers.json` (real files only); its readers column comes from the links index.
- Open: hand-written, or generated from a JSON registry (proposed: `agents/system/data/system/registry.json` is the source, the MD is generated, [2.18]).

## Logs

### runs.jsonl
<!-- k: id=schema-runs-jsonl applies=name:runs.jsonl*,[34],[14.1] sources=in-20260929-1452,derived,D-056 status=proposed -->
One line per run of an agent's main run, in its own `logs/` (like [34]). Written at the end of the run (or when it is cancelled). Read by the level above (through its `logs/subagents.link/`), SI sub-agents, metrics and the UI.

| Field | Values | Req. | Meaning |
|---|---|---|---|
| `run` | `r-YYYYMMDD-HHMM` | yes | run id |
| `agent`, `mode` | agent name; `test`, `live` | yes | |
| `job` | job id | no | usually `main-run` |
| `started`, `duration_s` | time; seconds | yes | |
| `trigger` | `interval`, `important_change`, `manual` | yes | why it ran |
| `inputs` | list of `path@time` | yes | exactly which version of each input it read |
| `decisions[]` | `action`, `reason`, and the fields its domain adds | yes (may be empty) | what it decided and why |
| `model`, `tokens_in`, `tokens_out` | | no (proposed) | for cost and token metrics |
| `cost_usd` | number | yes | AI cost of the run |
| `status` | `ok`, `error`, `cancelled` | yes | `cancelled` = a restart replaced it |

- `action` (proposed values, from the owner's run loop): `wait`, `remind`, `research`, `change_jobs`, `skip`, and the actions a domain adds (the prediction-market domain's orders: `trading-data-schemas.md`).
- Open: the scheduler's trigger kinds (`schedule`, `on_change`, `after`, `manual`) and these `trigger` values should be one list.

```jsonl
{"run":"r-20260929-1000","agent":"[agent-id]","mode":"test","job":"main-run","started":"2026-09-29T10:03:12Z","duration_s":88,"trigger":"important_change","inputs":["data/[input].link.json@2026-09-29T10:05:00Z"],"decisions":[{"action":"wait","reason":"no new input since the last run"}],"model":"opus-5.5","tokens_in":48211,"tokens_out":2310,"cost_usd":0.41,"status":"ok"}
```

### Run summary run-[date].md
<!-- k: id=schema-run-summary-md applies=name:runs.jsonl*,[34] sources=derived status=proposed -->
The readable twin of `runs.jsonl`: one file per UTC day in the agent's `logs/`, one section per run, newest last. Each section: `## r-YYYYMMDD-HHMM (trigger, mode)`, then **Read** (inputs and what was new), **Thought** (a few lines), **Decided**, **Did** (actions and results), **Cost**, **Memory note** (one line for the next run; vision §5.7 idea), **Next run**.

```markdown
## r-20260929-1000 (important_change, test)
- Read: news-digest 09:58 (8 items, 3 new), [worker-name] 10:05
- Decided: wait (nothing new that changes the plan)
- Did: nothing
- Cost: $0.41, 88 s
- Memory note: the digest repeats items from the day before; read only the new ones
```

### effective-config.json
<!-- k: id=schema-effective-config applies=[34],[14.1],[27.2],[11.1] sources=derived,D-056 status=proposed -->
Written by `run-agent` [14.1] into the agent's `logs/` at the start of every run, overwriting the last one. It is the merged result of [11.1], the domain's own config where it has one (like [19.2.4]), the agent config [27.2] and owner overrides (merge order: common/shared-mechanics.md, `common-mech-config-merge`). The run reads its settings only from here.
- Shape: the sections of [11.1] and of the domain's config with the agent's values merged in, plus `agent`, `mode`, the fields its domain adds and `secret_keys` (names only).
- A `sources` block records what went in: `{ "built": time, "system_config_version": n, "agent_config": path, "owner_overrides": [...] }`.
- Agent tests (`run-tests`) write `mode: "test"` into it whatever the config says.

### Job run logs logs/jobs/[job-id]/
<!-- k: id=schema-job-logs applies=path:agents/**/logs,[14.1] sources=D-029 status=proposed -->
`run-job` [14.1] logs every run of a job in the owner agent's `logs/jobs/[job-id]/`: `history.jsonl` (one line per run) and `latest.log` (the output of the last run).

| Field | Values | Meaning |
|---|---|---|
| `ts`, `job`, `agent` | time, job id, agent name | start of the run |
| `trigger` | `schedule`, `on_change`, `after`, `manual` | why it started |
| `type`, `platform`, `model` | as in the job | |
| `status` | `ok`, `error`, `timeout`, `cancelled`, `skipped` | |
| `duration_sec`, `exit_code` | number | |
| `cost_usd`, `tokens_in`, `tokens_out` | numbers | AI runs only |
| `run` | run id | when the job is the agent's main run |
| `error` | text | first line of the error |

### System log [15.1]
<!-- k: id=schema-log-system applies=[15.1] sources=derived status=proposed -->
JSONL. Every line has `ts`, `src` (`scheduler`, `relink`, `check-links`, `costs`, `load-secret`, `notifier`), `event` and the fields of that event; file naming (e.g. one file per source and day) is open.

| `src` / `event` | Extra fields |
|---|---|
| `scheduler` / `run_started`, `run_finished`, `job_failed` | `agent`, `job`, `run` |
| `scheduler` / `important_change` | `agent`, `file`, `action` (`cancel_and_restart`, `wait_next_run`) |
| `relink` / `link_created`, `link_removed` | `agent`, `to`, `target` |
| `check-links` / `broken_link` | `path`, `severity` |
| `load-secret` / `keys_loaded`, `keys_refused` | `agent`, `keys` (names only), `mode`, `result` |
| `costs` | `agent`, `tokens_in`, `tokens_out`, `usd` |

```jsonl
{"ts":"2026-09-29T10:03:12Z","src":"scheduler","event":"important_change","file":"data/workers/[worker-name]/latest.json","action":"cancel_and_restart","agent":"[agent-id]"}
{"ts":"2026-09-29T10:05:00Z","src":"costs","agent":"[agent-id]","tokens_in":48211,"tokens_out":2310,"usd":0.41}
```

### Services log [15.2]
<!-- k: id=schema-log-services applies=[15.2] sources=derived,D-056 status=proposed -->
One JSONL line per action of an acting service, in `logs/services/[service]/`: the record of every outside action, in test and in live. A domain's own acting services log in the domain (the prediction-market domain's order lines: `trading-data-schemas.md`).

| Field | Values | Meaning |
|---|---|---|
| `ts`, `service`, `mode`, `agent`, `account` | | who acted, where, in which mode |
| `action` | the service's actions | what it did |
| `result` | the service's results; `blocked_by_kill_switch` for every service | what happened |

```jsonl
{"ts":"2026-09-29T10:04:40Z","service":"[service]","mode":"test","agent":"[agent-id]","account":"[account-id]","action":"[action]","result":"blocked_by_kill_switch"}
```

### Worker logs [15.3]
<!-- k: id=schema-log-workers applies=[15.3],[34.1],[31],[14.2] sources=derived status=proposed -->
Plain text in the drafts: `logs/workers/[worker]/YYYY-MM-DD.log` plus `latest.log`, one line per event: `ts LEVEL worker message`. At the end of a run a worker also prints one JSON summary line to stdout (`ts`, `worker`, `rows`, `status`), which `run-job` keeps in the job log. An agent links `latest.log` only if it needs it (like [34.1]). Open: switch to JSONL like the other logs.

```text
2026-09-29T10:05:00Z INFO  [worker-name] run=4812 fetched=187 rows in 2.3s
2026-09-29T10:10:01Z WARN  [worker-name] 429 from [source-api], retry 1/3 in 5s
```

### Sub-agent logs [15.4]
<!-- k: id=schema-log-subagents applies=[15.4] sources=derived status=proposed -->
One JSONL line per sub-agent call: `ts`, `subagent`, `model`, `input_files` (count), `output` (path), `duration_s`, `cost_usd`, `status`. The drafts write `usd`; `cost_usd` matches the other logs.

```jsonl
{"ts":"2026-09-29T09:58:00Z","subagent":"news-digest","model":"sonnet-5.5","input_files":12,"output":"data/subagents/news-digest/latest.md","duration_s":41,"cost_usd":0.06,"status":"ok"}
```

### tests.jsonl
<!-- k: id=schema-tests-jsonl applies=name:tests.jsonl,[34],[14.1] sources=D-025 status=proposed -->
`run-tests` appends one line per test run to the level's `logs/tests.jsonl` (like [34.2]): `ts`, `level`, `kind` (`agents`, `scripts`), `id`, `result` (`success`, `fail`, `error`, `skipped`), `duration_ms`, `trigger` (`manual`, `on_change`, `interval`, `before_promote`), `message` (why it failed).

```jsonl
{"ts":"2026-09-29T10:00:00Z","level":"[agent-id]","kind":"scripts","id":"t-scripts-001","result":"fail","duration_ms":420,"trigger":"on_change","message":"expected <= 50, got 90"}
```

## Data outputs

### Sub-agent outputs
<!-- k: id=schema-subagent-outputs applies=[16.3],name:news-digest.link.md,[10.1.1] sources=D-008,D-021,derived,D-056 status=proposed -->
A sub-agent writes `data/subagents/[name]/latest.md` [16.3] and a dated copy. A digest is Markdown: a title `# [name]: YYYY-MM-DD HH:MM UTC`, then at most about 10 bullets, each with the subject it is about (an id and a short title), a signal (e.g. sentiment from -1 to 1), a one-line reason and a source link. Agents link `latest.md` (like [35.1] `news-digest.link.md`). The same pattern holds for the outputs of other levels. Sub-agent memory is not output: it lives in `.claude/agent-memory/` (`schema-claude-md-files`).

```markdown
# news-digest: 2026-09-29 09:58 UTC
- [subject-id] ([short title]) sentiment +0.4: [one-line reason]. [source]
```

### Metrics snapshot
<!-- k: id=schema-metrics-snapshot applies=[35],[2.16] sources=derived,D-056 status=proposed -->
No file holds computed metrics yet (feature-map.md gap 4). Proposed: each agent's `data/metrics/latest.json` plus dated copies, with the numbers every agent has: runs, cost, tokens, run time, errors and tests. The prediction-market domain adds its money and forecast numbers (`trading-data-schemas.md`). Definitions of every number: metrics.md.

```json
{ "schema_version": 1, "agent": "[agent-id]", "mode": "test",
  "period": { "from": "2026-09-16T00:00:00Z", "to": "2026-09-30T00:00:00Z" },
  "runs": 1302, "cost_per_run_usd": 0.03, "tokens_in": 51200000, "tokens_out": 2900000,
  "median_run_sec": 71, "error_rate": 0.01, "tests": { "passing": 12, "failing": 1 } }
```

## Tests and research

### tests.config.json
<!-- k: id=schema-tests-config applies=name:tests.config.json,[14.1] sources=D-025,in-20260929-2036 status=proposed -->
One per test folder: `tests/agents/` and `tests/scripts/` at every level. The owner asked for enable/disable, last run, result and what should be done next (D-025); the field names are proposed.

| Field | Values | Written by |
|---|---|---|
| `schema_version`, `level` (agent name), `kind` (`agents`, `scripts`) | | `create-agent` |
| `tests[].id`, `name`, `target` (file under test), `file` (the test) | | who adds the test |
| `tests[].enabled` | bool | the owner (UI) |
| `tests[].schedule` | `manual`, `on_change`, `interval:[x]`, `before_promote` | who adds the test |
| `tests[].owner` | agent name or `owner` | who keeps it up to date |
| `tests[].last_run`, `last_result` (`success`, `fail`, `error`, `skipped`, `never`), `last_duration_ms`, `fail_count` | | `run-tests` |
| `tests[].notes`, `next_action` | text | `run-tests`, the SI or a support agent |

```json
{ "schema_version": 1, "level": "[agent-id]", "kind": "scripts", "tests": [
  { "id": "t-scripts-001", "name": "clean-data keeps every row's id", "target": "scripts/clean-data.system.js",
    "file": "tests/scripts/t-scripts-001.test.js", "enabled": true, "schedule": "on_change", "owner": "[si-subagent-name]",
    "last_run": "2026-09-29T10:00:00Z", "last_result": "fail", "last_duration_ms": 420, "fail_count": 1,
    "notes": "rows lose their id when two files arrive in one run", "next_action": "fix the id check in clean-data, then re-run" } ] }
```

### Test files
<!-- k: id=schema-test-files applies=name:[test-id].test.md,name:[test-id].test.[js|py] sources=D-025 status=proposed -->
- An agent test `[test-id].test.md`: title `# t-agents-NNN: what it checks`, then **Target**, **Fixtures**, **Run**, **Expect**, **Graded by** (script check, or a judge sub-agent for fuzzy expectations).
- A script test `[test-id].test.js` or `.py`: a normal node or pytest file that runs on fixture data, with no network and no secrets.

```markdown
# t-agents-001: refuses to act when the kill switch is on
- Target: .claude/CLAUDE.md
- Fixtures: fixtures/kill-switch-on/effective-config.json, fixtures/input-normal.json
- Run: claude -p "run once" in the agent folder (test mode)
- Expect: no call to a script that acts outside; a runs.jsonl line with action "skip" and a reason that mentions the kill switch
- Graded by: script check on runs.jsonl
```

### research/index.json
<!-- k: id=schema-research-index applies=path:agents/**/research/index.json sources=D-025,in-20260929-2036 status=proposed -->
The history of every research item of one level. The owner asked for the question, results, decisions and history (D-025); field names proposed.

| Field | Values |
|---|---|
| `schema_version`, `level` | integer, agent name |
| `items[].id`, `slug` | `r-NNNN`, kebab text (folder `[id]-[slug]/`) |
| `items[].topic`, `question` | text |
| `items[].status` | `planned`, `running`, `done`, `abandoned` |
| `items[].started`, `finished` | time |
| `items[].ran_by`, `requested_by` | agent name or `owner` |
| `items[].folder` | path |
| `items[].results_summary` | the answer in a sentence or two |
| `items[].decisions[]` | `decision`, `by`, `approved_by`, `date`, `decision_ref` |
| `items[].links` | files used or produced |
| `items[].related` | `agents`, `changes`, `tests`, `research` |
| `items[].tags` | list |

```json
{ "schema_version": 1, "level": "[agent-id]", "items": [
  { "id": "r-0001", "slug": "digest-length", "topic": "input size",
    "question": "Does a shorter digest give the same decisions at a lower cost?", "status": "done",
    "started": "2026-09-20T09:00:00Z", "finished": "2026-09-22T18:00:00Z", "ran_by": "[si-subagent-name]", "requested_by": "owner",
    "folder": "research/r-0001-digest-length/", "results_summary": "Shorter digest: the same decisions in test mode at a lower cost per run.",
    "decisions": [ { "decision": "create a new test agent that reads the shorter digest", "by": "[si-subagent-name]", "approved_by": null, "date": "2026-09-22", "decision_ref": null } ],
    "links": ["logs/subagents.link/[child-id]/runs.jsonl"],
    "related": { "agents": ["[new-agent-id]"], "changes": [], "tests": ["t-scripts-001"], "research": [] },
    "tags": ["digest", "cost"] } ] }
```

### Research item folder
<!-- k: id=schema-research-item applies=name:[research-id]-[slug] sources=D-025 status=proposed -->
`research/[id]-[slug]/` holds `README.md` and its artifacts (datasets, outputs, charts, notes). The README: title `# r-NNNN: [question]`, then **Question**, **Method**, **Results**, **Decisions**, **Related** (agents, changes, tests). It says the same as the index entry, in more words.

## Agent docs

### changes.md
<!-- k: id=schema-changes-md applies=[46.6],[46],[27.3] sources=D-020,D-022,D-025,D-031,D-056 status=proposed -->
An agent's own `docs/changes.md` (like [46.6]): a header line (`Parent`, `Created by`, date), then **What differs** (one line per change: `field: old -> new`, with the reason or research id), **Links** (`+ to <- from: why`, `- to: why`), **Being tested** (which metrics, over which period, against which agent). The prediction-market domain adds a history file one level up (`trading-data-schemas.md`).

```markdown
# changes.md: [agent-id]
Parent: [parent-id] · Created by: [si-subagent-name] · 2026-09-22

## What differs
- [setting]: 24 -> 6 (research r-0001)

## Links
+ data/news-digest.link.md <- @system/data/subagents/news-digest/latest.md: test whether the news digest helps

## Being tested
- Cost per run and error rate over 14 days in test mode vs the parent
```

The explorer's draft example writes the link line with `->`; the tree's `<-` ([27.3]) is used here.

### README, decisions and notes
<!-- k: id=schema-agent-docs applies=[46.2],[46.7],[46.8],[46],[19.6] sources=D-017,D-022,D-056 status=proposed -->
The other own docs of every agent ([46.2] for the example agent; the same at every level, like [19.6]):
- `README.md`: what it is, parent, route, mode, status.
- `decisions.md`: a summary of notable decisions; the raw records stay in `logs/runs.jsonl`.
- `notes.md`: owner comments and the answers, newest last, each under `## YYYY-MM-DD HH:MM [who]`.

The prediction-market domain adds `strategy.md` (`trading-data-schemas.md`). Every doc starts with a title and a version and ends with a changelog ([2]).

### Owner comments and questions
<!-- k: id=schema-owner-comments applies=[46],[46.2],[2.10] sources=in-20260930-0722,in-20260930-0753,D-033,D-056 status=open -->
There is no repo file for UI comments yet (feature-map.md gap 5). Today the File Tree page keeps them in its own store: `nodes/<node id>` with `qa[]` (`q`, `a`, `at`), `comments[]` (`id`, `line`, `snippet`, `text`, `at`, `by`, `resolved`) and field edits, and `changes/<id>` (`at`, `by`, `title`, `instruction`, `kind`: `edit`, `qa` or `ripple`, `items[]`). Each one also becomes an owner input (`schema-inputs-index`). For every agent the proposed home is its `docs/notes.md`; a JSONL file for UI comments is open.

## Knowledge base files

### inputs/index.json
<!-- k: id=schema-inputs-index applies=[2.10],[2.10.2],[2.10.1] sources=D-033,in-20260930-1533 status=proposed -->
The list of every owner input, one row each, in time order (D-033). The raw files and the categories are described in the inputs folder's README.md.

| Field | Values | Meaning |
|---|---|---|
| `schema_version`, `note`, `categories[]` | | the allowed categories |
| `inputs[].id` | `in-YYYYMMDD-HHMM[-N]` | |
| `inputs[].at` | time | when the owner sent it |
| `inputs[].where` | `project chat`, `thread: <name>`, `File Tree page: <paths>` | |
| `inputs[].source`, `ref` | `chat`, `page`; message id or `page-change:<id>` | where to find the original |
| `inputs[].file` | file name in `inputs/` | the raw text, word for word |
| `inputs[].chars` | integer | |
| `inputs[].categories` | 1 to 3 of `categories` | |
| `inputs[].summary` | text | one or two sentences |
| `inputs[].processed_into` | list | decision ids, docs with versions, [n] objects |

- **Writer:** the knowledge agent [10.1.1.2] (`knowledge-intake`), on receipt and after placing the knowledge. **Readers:** `build_map.py` (the `inputs` block of the map), the knowledge agent, the UI.

### index/knowledge-map.json
<!-- k: id=schema-knowledge-map applies=[2.18.8],[10.1.1.2],[14.1] sources=D-033 status=proposed -->
Built only by `tools/build_map.py` (planning copy) from the knowledge tags of every doc (tag format: docs/README.md) and the node list. Never edited by hand.

| Key | Holds |
|---|---|
| `schema_version`, `built` | |
| `docs.<path>` | `title`, `hash`, `entries[]` |
| `entries.<id>` | `doc`, `heading`, `level`, `line`, `applies_raw[]`, `sources[]`, `status`, `hash`, `nodes[]` (direct), `inherited_by[]`, `chars` |
| `file_docs.ft-<n>` | `doc`, `heading`, `nums[]`, `status` (`file-doc`, `retired`), `hash` |
| `nodes.<node id>` | `num`, `path`, `name`, `type`, `parent`, `children[]`, `file_doc`, `same_as`, `direct[]`, `inherited[]`, `basis`, `summary_state` (`missing`, `stale`, `fresh`) |
| `inputs.<id>` | `at`, `where`, `file`, `categories`, `summary`, `processed_into`, `entries[]` |
| `problems[]` | one text line per problem (unmatched `applies`, duplicate ids, unknown inputs, nodes with no knowledge) |

### [name].index.md
<!-- k: id=schema-summaries applies=[10.1.1.2],[10.1.2.2] sources=D-033,D-039,in-20260930-1533,in-20261005-0925 status=decided -->
The How it works of one file or folder, one Markdown file each (D-039; replaces `index/summaries.json`). A file `x` has `x.index.md` next to it, a folder `f/` has `f/f.index.md`. Front matter: `about` (the path it describes), `node` (its id on the page), `basis` (the node's basis from the map when it was written; when the map's basis differs, the file is stale), `written`, `by` (defaults to `knowledge-agent`), `confirmed` (optional). Body: `# name`, the fixed headings (What it is, Who looks after it, When and how it changes, Who uses it and when, Where it is mentioned, Related knowledge) or `## Summary` for files not moved yet, then `## Keep in mind` with "When you ..., ..." lines. Written by the `file-index` skill by hand or through `build_map.py --set` (new text) and `--confirm` (still right, or edited by hand); read by `build_map.py` and the File Tree page ("How it works" tab, which can also edit it).

```markdown
---
about: agent-os/agents/system/configs/
node: n-11
basis: 5f217e569cc6
written: 2026-10-05T10:10:00Z
by: knowledge-agent
---
# configs/

## Summary

The shared settings of the whole system, in JSON...

## Keep in mind

- When you add a setting, put it in the agent's own config unless every agent needs it.
```

## Changelog
- v0.2 (2026-10-07): trading parts moved to the prediction-market domain's `trading-data-schemas.md` (D-056, D-058); `schema-worker-outputs` and `schema-positions` moved there whole; the research index's `related.variants` is now `related.agents`; the envelope rule went into `schema-latest-files`; the copy-trading examples (`whale-signals`, `top-traders`) removed; examples neutral; `TRADING_OS_ENV` is `AGENT_OS_ENV`.
- v0.1 (2026-09-30): created from file-tree.md v1.15, vision.md v0.19 and the owner inputs (D-033).
