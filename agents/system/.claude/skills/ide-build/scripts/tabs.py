"""Field guides (Example tab) and custom tabs (editable tables) for the File Tree explorer.
Imported by enrich.py. Each field: key, values (type or allowed values), example, meaning."""

def F(key, values, example, meaning):
    return {"key": key, "values": values, "example": example, "meaning": meaning}

SYSTEM_CONFIG = [
 F("schema_version", "integer", "1", "Version of this file's shape. Bumped when sections or keys change (see data-schemas.md [2.14])."),
 F("defaults.timezone", "IANA zone", "\"UTC\"", "Time zone for schedules, quiet hours and log timestamps."),
 F("defaults.log_level", "debug | info | warn | error", "\"info\"", "Minimum level written to logs."),
 F("defaults.run_timeout_sec", "seconds", "600", "A run that takes longer is stopped and logged as timed out."),
 F("defaults.by_agent_type.<type>.allowed_actions", "list", "[\"create_test_agent\"]", "What each agent type may do. Types: system, domain, strategy, main, sub, support, si."),
 F("defaults.by_agent_type.<type>.memory", "true | false", "true", "Whether that type keeps memory between runs."),
 F("modes.default_mode", "test | live", "\"test\"", "Mode every new agent and service starts in. Stays test until the owner approves live."),
 F("modes.kill_switch", "true | false", "false", "The general stop switch: when true, every outside action is refused before it happens. Checked before every action; a domain adds its own meaning (the prediction-market domain: refuse orders, close positions)."),
 F("modes.live_allowlist", "list of agent names", "[]", "Only agents listed here can ever act live, and only with the owner's approval (in the prediction-market domain also a funded, owner-approved account)."),
 F("schedules.<agent type>", "schedule string", "\"every 15m\"", "Default schedule for a new agent's main run, per agent type (main, domain, si, ...). Each job's own schedule is in its agent's workers file (D-029)."),
 F("schedules.max_concurrent_runs", "integer", "4", "How many jobs may run at the same time on the local scheduler."),
 F("schedules.quiet_hours", "null | {from, to}", "{\"from\": \"01:00\", \"to\": \"06:00\"}", "No AI jobs start in this window (scripts still run)."),
 F("schedules.allowed_run_on", "list", "[\"local\", \"cloud\"]", "Where jobs may run at all. A job asking for anything else is refused."),
 F("schedules.max_ai_cost_usd_per_day", "number", "20", "When today's AI job cost reaches this, AI jobs pause until tomorrow."),
 F("triggers.important", "list of path patterns", "[\"data/**/latest.json\"]", "A change to a matching file cancels the current run and restarts it."),
 F("triggers.debounce_sec", "seconds", "30", "Wait this long after a change before reacting, so bursts count once."),
 F("triggers.min_restart_gap_sec", "seconds", "120", "Shortest time between two restarts of the same agent."),
 F("triggers.max_restarts_per_hour", "integer", "6", "After this many restarts in an hour, further changes wait for the next run."),
 F("triggers.on_unimportant", "wait_next_run", "\"wait_next_run\"", "What happens when an unimportant file changes."),
 F("notifications.channels", "list", "[\"ui\"]", "Where alerts go (UI first; Telegram or email later)."),
 F("notifications.events.<event>", "low | medium | high", "\"high\"", "Severity per event: agent_error, promotion_proposed, kill_switch, live_action; a domain adds its own (the prediction-market domain: live_trade, risk_limit_hit)."),
]

DOMAIN_CONFIG = [  # [19.2.4] prediction-market-agents.config.json: the trading settings that left [11.1] (D-058)
 F("schema_version", "integer", "1", "Version of this file's shape (see trading-data-schemas.md [19.6.9])."),
 F("currency", "ISO code", "\"USD\"", "Currency for capital, risk caps and PnL."),
 F("risk.domain.max_total_live_usd", "number", "500", "Hard cap on all live capital across the domain's agents."),
 F("risk.domain.max_daily_loss_usd", "number", "50", "When today's total loss reaches this, live trading stops for the day."),
 F("risk.domain.drawdown_stop_pct", "percent", "15", "Stop live trading when the drawdown from the peak reaches this."),
 F("risk.per_agent.max_capital_usd", "number", "100", "Most capital one agent may use. An agent config may only lower it."),
 F("risk.per_agent.max_position_pct", "percent", "5", "Largest single position as a share of the agent's capital."),
 F("risk.per_agent.max_open_positions", "integer", "10", "Most positions one agent may hold at once."),
 F("risk.per_agent.max_orders_per_hour", "integer", "20", "Rate limit on orders per agent."),
 F("accounts[].id / venue / mode", "text / polymarket... / test | live", "\"acct-pm-test-1\", \"polymarket\", \"test\"", "One trading account per entry."),
 F("accounts[].funded / approved_by_owner", "true | false", "false, false", "Live needs both: money in the account and the owner's approval in the UI."),
 F("accounts[].assigned_agent / max_capital_usd", "agent name / number", "\"pm-strategy-1.momentum-v1.opus55-test\", 0", "Which agent may use it, and how much."),
 F("accounts[].secret_keys", "list of .env key names", "[\"POLYMARKET_ACCT1_*\"]", "Which keys in .secrets/[mode]/.env belong to this account (D-027). Never the values."),
 F("venues / fees_bps / market_filters", "list / number / object", "[\"polymarket\"], 0, {\"min_volume_usd\": 10000}", "Per-venue settings of the domain. Risk here can only be tighter than the domain caps."),
 F("kill_switch", "true | false", "false", "The order stop switch: when true, orders are refused, positions are closed and the accounts are set back to unfunded. The system's general stop switch [11.1] stops every outside action, orders included. The name is our proposal."),
 F("notifications.events.<event>", "low | medium | high", "\"high\"", "The domain's own events: live_trade, risk_limit_hit."),
]

WORKERS_CONFIG = [
 F("schema_version", "integer", "1", "Version of this file's shape (D-029)."),
 F("agent", "agent name", "\"prediction-market-agents\"", "The agent that owns these jobs. The file is named after it: [name].workers.json."),
 F("defaults", "object", "{\"timezone\": \"UTC\", \"run_on\": \"local\", \"platform\": \"claude-code\", \"model\": \"route\"}", "Values every job gets unless it sets its own."),
 F("jobs[].id", "text, unique in the file", "\"main-run\"", "The job's name. Logs go to the agent's logs/jobs/[id]/."),
 F("jobs[].enabled", "true | false", "true", "Off = the job stays in the file but never runs. Turn off to pause; never delete to pause."),
 F("jobs[].purpose", "text", "\"Trade on 24h momentum\"", "What the job is for, in one line."),
 F("jobs[].type", "script | agent | subagent | skill | workflow | command", "\"subagent\"", "script = a plain program. agent = the agent's own session (its CLAUDE.md) in its folder. subagent, skill, workflow, command = run that one thing."),
 F("jobs[].run", "command or name", "\"python scripts/get-polymarket-data.worker.py\" or \"pm-self-improvement-agent\"", "For a script, the command line. Otherwise the name of the sub-agent, skill, workflow or /command."),
 F("jobs[].schedule", "every N(m|h|d) | cron ... | once DATE TIME | after JOB | manual", "\"every 15m\", \"cron 0 22 * * 1-5\", \"once 2026-11-03 20:00\"", "When it runs. once runs a single time on that date, then shows as done. after runs when that job succeeds. manual runs only from the UI or a command."),
 F("jobs[].timezone", "IANA zone", "\"America/New_York\"", "Time zone for cron and once. Default from defaults, then system.config.json."),
 F("jobs[].run_on", "local | cloud | desktop | github-actions", "\"local\"", "local = headless on the scheduler's machine (files, links, test secrets). cloud = the platform's cloud (fresh repo copy, no local files, no secrets; Claude Code routines at most hourly). desktop = Claude desktop task, only while the app is open. github-actions = scheduled workflow."),
 F("jobs[].platform", "none | claude-code | cursor | codex", "\"claude-code\"", "Which coding agent runs an AI job. none for plain scripts. Cursor and Codex can take jobs later without changing anything else."),
 F("jobs[].model / effort", "route | model name / low ... max", "\"route\", \"high\"", "route = the model from models.config.json [11.11]. A name here overrides it for this job only."),
 F("jobs[].prompt", "text | @path", "\"@docs/prompts/main-run.md\"", "What the AI run is asked to do. @path reads the prompt from a file in the workspace."),
 F("jobs[].workspace", "folder", "\"agents/prediction-market-agents\"", "Folder the run starts in, so it picks up that level's .claude/. Default: the owner agent's folder."),
 F("jobs[].allowed_tools / permission_mode / max_turns", "list / default | acceptEdits | plan / integer", "[\"Read\", \"Grep\", \"Bash(python scripts/*)\"], \"acceptEdits\", 30", "Limits for a headless AI run. run-job turns them into the platform's flags."),
 F("jobs[].max_cost_usd", "number", "2", "Stop the run when it has cost this much. The daily cap is in system.config.json schedules."),
 F("jobs[].on_change", "list of paths", "[\"data/news-digest.link.md\"]", "Also run when one of these files changes. For the main run this cancels and restarts the current run."),
 F("jobs[].inputs / outputs", "lists of paths", "[\"data/get-polymarket-data/latest.json\"]", "What it reads and writes. Outputs are stable latest.* files so others can link them."),
 F("jobs[].secret_keys", "list of .env key names", "[\"POLYMARKET_ACCT1_*\"]", "Keys load-secret passes to this job (D-027). Only for local jobs."),
 F("jobs[].timeout / retries / concurrency", "duration / integer / skip | queue | restart", "\"10m\", 2, \"skip\"", "Kill after timeout; retry on failure; what to do if the last run is still going."),
 F("jobs[].mode", "test | live", "\"test\"", "live needs owner approval and a live-allowed agent. Cloud, desktop and GitHub jobs are always test."),
 F("jobs[].notify", "never | failure | always", "\"failure\"", "When the owner is told about a run (channels in system.config.json)."),
]

LINKS_CONFIG = [
 F("schema_version", "integer", "1", "Version of this file's shape (D-031)."),
 F("agent", "agent name", "\"pm-strategy-1.momentum-v1.opus55-test\"", "The agent that owns these links. The file is named after it: [name].links.json."),
 F("links[].enabled", "true | false", "true", "Off = relink removes the symlink but the entry stays, so it is easy to turn back on."),
 F("links[].to", "path in this agent's folders", "\"data/news-digest.link.md\"", "Where the link appears: inside this agent's configs/, scripts/, logs/, data/, docs/, tests/ or research/, never in subagents.link/. The name carries .link."),
 F("links[].from", "@system/... | @domain/... | @strategy/... | @[name]/... | agents/...", "\"@system/data/subagents/news-digest/latest.md\"", "The real file it points at. @domain and @strategy are this agent's own; @[name] is any domain or agent by its unique name, so another domain's or agent's files work too. Never .secrets/ or .claude/."),
 F("links[].why", "text", "\"use the news digest when deciding\"", "What the agent uses it for."),
 F("links[].required", "true | false", "true", "true: if the file is missing, relink reports an error and the main run does not start. false: a warning, and the link appears once the file exists."),
 F("links[].added_by / added", "who / date", "\"pm-strategy-1-self-improvement-agent\", \"2026-10-02\"", "create-agent, the agent itself, its SI sub-agent or the owner."),
]

MODELS_CONFIG = [
 F("platforms.<platform>.status", "default | supported | supported-not-connected | later", "\"default\"", "Whether a platform can be used now."),
 F("platforms.<platform>.secret_keys", "list of .env key names", "[\"ANTHROPIC_API_KEY\"]", "Keys needed to call it (D-027)."),
 F("models.<model>.platform", "platform name", "\"claude-code\"", "Which platform serves this model."),
 F("models.<model>.effort", "low | medium | high | xhigh", "\"medium\"", "How hard the model thinks; more effort costs more and takes longer."),
 F("defaults_by_type.<type>", "model name", "\"opus-5.5\"", "Model used when an agent/sub-agent/worker has no own route. Types: main, domain, si, sub, worker, support."),
 F("routes.<name>", "model name", "\"sonnet-5.5\"", "Route for one named agent, sub-agent or worker. Wins over defaults_by_type."),
]

AGENT_CONFIG = [
 F("agent.name", "unique agent name", "\"pm-strategy-1.momentum-v1.opus55-test\"", "The agent's permanent ID (D-012). Never renamed or reused."),
 F("agent.type", "system | domain | strategy | variant", "\"variant\"", "Which level the agent is (D-022)."),
 F("agent.domain / strategy", "text", "\"prediction-markets\", \"strategy-1\"", "Where it sits."),
 F("agent.parent", "agent name | null", "null", "The agent this one was cloned from. Test to live creates a new agent with parent = the test agent."),
 F("mode", "test | live", "\"test\"", "Requested mode. Live still needs the live allowlist and an owner-approved account."),
 F("capital_and_risk.max_capital_usd / max_position_pct", "number / percent", "100, 3", "Only tighter than system.config.json risk caps, never looser."),
 F("secret_keys", "list of .env key names", "[\"POLYMARKET_ACCT1_*\"]", "Keys this agent's scripts may receive from load-secret (D-027)."),
 F("strategy.<param>", "strategy specific", "\"momentum_window_h\": 24", "The strategy's own knobs. A change = a new variant (v+1)."),
]

TESTS_CONFIG = [
 F("schema_version", "integer", "1", "Shape version."),
 F("level", "agent name", "\"pm-strategy-1.momentum-v1.opus55-test\"", "Which agent/level these tests belong to."),
 F("kind", "agents | scripts", "\"scripts\"", "agents = prompt and sub-agent behaviour; scripts = code."),
 F("tests[].id", "t-[agents|scripts]-NNN", "\"t-scripts-001\"", "Unique within the level; never reused."),
 F("tests[].name", "text", "\"make-buy respects max position size\"", "What the test checks, in plain words."),
 F("tests[].target / file", "paths", "\"scripts/make-buy.decision.js\", \"tests/scripts/t-scripts-001.test.js\"", "What is tested, and the test itself."),
 F("tests[].enabled", "true | false", "true", "The owner can switch a test on or off from the UI."),
 F("tests[].schedule", "manual | on_change | interval:[x] | before_promote", "\"on_change\"", "When it runs."),
 F("tests[].owner", "agent name | owner", "\"pm-strategy-1-self-improvement-agent\"", "Who keeps it up to date."),
 F("tests[].last_run / last_result / last_duration_ms / fail_count", "time / success | fail | error | skipped | never / ms / integer", "\"2026-09-29T10:00:00Z\", \"fail\", 420, 1", "Written back by run-tests after each run."),
 F("tests[].notes / next_action", "text", "\"fix the cap check, then re-run\"", "What went wrong and what should happen next."),
]

RESEARCH_INDEX = [
 F("schema_version / level", "integer / agent name", "1, \"pm-strategy-1-agent\"", "Shape version and owner level."),
 F("items[].id / slug", "r-NNNN / text", "\"r-0001\", \"momentum-window-length\"", "Unique id and folder name part."),
 F("items[].topic / question", "text", "\"signal tuning\", \"Does 6h beat 24h?\"", "What was asked."),
 F("items[].status", "planned | running | done | abandoned", "\"done\"", "Where the research is."),
 F("items[].started / finished", "time", "\"2026-09-20T09:00:00Z\"", "When it ran."),
 F("items[].ran_by / requested_by", "agent name | owner", "\"pm-strategy-1-self-improvement-agent\", \"owner\"", "Who did it, who asked."),
 F("items[].folder", "path", "\"research/r-0001-momentum-window-length/\"", "Where its README and artifacts are."),
 F("items[].results_summary", "text", "\"6h window: higher hit rate\"", "The answer in a sentence or two."),
 F("items[].decisions[]", "{decision, by, approved_by, date, decision_ref}", "{\"decision\": \"create v2\"}", "What was decided because of it."),
 F("items[].links / related / tags", "lists", "{\"variants\": [\"...-v2-...\"]}", "Files used, what it led to, and search tags."),
]

SETTINGS_JSON = [
 F("model", "opus | sonnet | haiku | full model id", "\"opus\"", "Default model for sessions at this level (routes in models.config.json can override for runs)."),
 F("permissions.deny", "list of rules", "[\"Read(**/.secrets/live/**)\"]", "What Claude Code may never do here. Live secrets are always denied (D-027)."),
 F("permissions.allow", "list of rules", "[\"Bash(node scripts/*)\"]", "What runs without asking."),
 F("env", "object", "{\"AGENT_OS_ENV\": \"test\"}", "Environment variables for sessions at this level."),
 F("hooks.<Event>", "list of matcher + command", "PostToolUse (Edit|Write) -> relink if a configs/*.links.json changed; run-tests on_change", "Scripts that run on Claude Code events. The relink hook keeps links in step with the links file (D-031)."),
 F("statusLine / outputStyle", "command / style name", "\"concise\"", "What the session shows and how it answers."),
]

SECRETS_INDEX = [
 F("<key or prefix>", "object", "\"POLYMARKET_ACCT1_*\"", "One entry per key group in the .env files. Never a value."),
 F("kind", "wallet | api-key | token", "\"wallet\"", "What sort of secret it is."),
 F("env", "test | live", "\"test\"", "Which file it is in."),
 F("used_by", "list", "[\"acct-pm-test-1\"]", "Accounts, platforms or workers that need it."),
 F("created / rotate_by", "dates", "\"2026-09-29\", \"2026-12-29\"", "When to replace it; the notifier warns before."),
]

PACKAGE_JSON = [
 F("name", "agent name", "\"pm-strategy-1.momentum-v1.opus55-test\"", "Same as the folder name."),
 F("private", "true", "true", "Never published to npm."),
 F("type", "module", "\"module\"", "Scripts use import/export."),
 F("scripts.start / test", "commands", "\"./start.sh\", \"node scripts/run-tests.system.link.js\"", "npm start runs the agent; npm test runs all its tests."),
 F("dependencies", "package: version", "{\"zod\": \"^3.23.0\"}", "JS libraries its own scripts need."),
]

SUBAGENT_MD = [
 F("name", "unique name", "\"news-digest\"", "How it is called; unique across the system (D-012)."),
 F("description", "text", "\"Reads new market news...\"", "When Claude should use it. Written as a trigger."),
 F("tools", "list", "Read, Grep, WebFetch, Write", "Tools it may use."),
 F("memory", "project | local | none", "project", "Where it keeps memory: .claude/agent-memory/ or agent-memory-local/."),
 F("(body)", "Markdown", "Read ... Write ...", "Its instructions."),
]

RUNS_JSONL = [
 F("run", "r-YYYYMMDD-HHMM", "\"r-20260929-1000\"", "Run id."),
 F("agent / mode", "agent name / test | live", "\"...-test\", \"test\"", "Who ran and in which mode."),
 F("started / duration_s", "time / seconds", "\"2026-09-29T10:03:12Z\", 88", "When and how long."),
 F("trigger", "interval | important_change | manual", "\"important_change\"", "Why it ran."),
 F("inputs", "list of path@time", "[\"data/polymarket-prices.link.json@...\"]", "Exactly which data it read."),
 F("decisions[]", "{market, action, size_usd, reason}", "{\"action\": \"buy_yes\"}", "What it decided and why."),
 F("cost_usd / status", "number / ok | error | cancelled", "0.41, \"ok\"", "What it cost and how it ended."),
]

ENV_COLUMNS = [
 {"key": "name", "label": "Variable", "kind": "text"},
 {"key": "purpose", "label": "What it is for", "kind": "text"},
 {"key": "used_by", "label": "Used by", "kind": "text"},
 {"key": "required", "label": "Required", "kind": "bool"},
 {"key": "format", "label": "Format (no real values)", "kind": "text"},
]
ENV_ROWS = [
 {"name": "AGENT_OS_ENV", "purpose": "Which secrets file load-secret reads: test or live", "used_by": "load-secret", "required": True, "format": "test | live"},
 {"name": "ANTHROPIC_API_KEY", "purpose": "Claude API for agents and sub-agents run headless", "used_by": "run-agent, run-tests", "required": True, "format": "sk-ant-..."},
 {"name": "POLYMARKET_ACCT1_API_KEY", "purpose": "Polymarket CLOB API key for test account 1", "used_by": "acct-pm-test-1, polymarket-exec", "required": True, "format": "uuid"},
 {"name": "POLYMARKET_ACCT1_API_SECRET", "purpose": "Secret paired with the API key", "used_by": "acct-pm-test-1", "required": True, "format": "base64"},
 {"name": "POLYMARKET_ACCT1_API_PASSPHRASE", "purpose": "Passphrase paired with the API key", "used_by": "acct-pm-test-1", "required": True, "format": "text"},
 {"name": "POLYMARKET_ACCT1_WALLET_PRIVATE_KEY", "purpose": "Signs orders for the account's wallet", "used_by": "acct-pm-test-1", "required": True, "format": "0x + 64 hex"},
 {"name": "GROQ_API_KEY", "purpose": "Groq speech to text for voice input in the project IDE (D-060); test file only", "used_by": "apps/project-IDE/server/voice.py", "required": False, "format": "gsk_..."},
 {"name": "OPENROUTER_API_KEY", "purpose": "Other models via OpenRouter (not connected yet)", "used_by": "models.config.json", "required": False, "format": "sk-or-..."},
 {"name": "NOTIFY_TELEGRAM_BOT_TOKEN", "purpose": "Alerts to Telegram (later)", "used_by": "notifier", "required": False, "format": "123:ABC..."},
]

ENV_FAKE = {
 "AGENT_OS_ENV": "test",
 "ANTHROPIC_API_KEY": "sk-ant-api03-XXXXXXXXXXXXXXXXXXXX",
 "POLYMARKET_ACCT1_API_KEY": "00000000-0000-0000-0000-000000000000",
 "POLYMARKET_ACCT1_API_SECRET": "ZmFrZS1zZWNyZXQtZXhhbXBsZQ==",
 "POLYMARKET_ACCT1_API_PASSPHRASE": "example-passphrase",
 "POLYMARKET_ACCT1_WALLET_PRIVATE_KEY": "0x" + "0" * 63 + "1",
 "GROQ_API_KEY": "gsk_XXXXXXXXXXXXXXXXXXXXXXXX",
 "OPENROUTER_API_KEY": "",
 "NOTIFY_TELEGRAM_BOT_TOKEN": "",
}

def env_rows(num):
    if num == "47.2.1":
        return [dict(r, used_by=r["used_by"].replace("test", "live")) for r in ENV_ROWS if r["name"] not in ("OPENROUTER_API_KEY", "GROQ_API_KEY")]
    return ENV_ROWS

def env_fields(num):
    live = num == "47.2.1"
    out = []
    for r in env_rows(num):
        ex = "live" if (live and r["name"] == "AGENT_OS_ENV") else ENV_FAKE.get(r["name"], "")
        out.append(F(r["name"], r["format"] + (" (required)" if r["required"] else " (optional, may be empty)"), ex or "(empty)",
                     r["purpose"] + ". Used by " + r["used_by"] + "."))
    return out

def env_example(num):
    live = num == "47.2.1"
    rows = env_rows(num)
    lines = [f"# .secrets/{'live' if live else 'test'}/.env  (git-ignored, chmod 600)",
             "# FAKE values for illustration. Real values are typed into the local file only.", ""]
    groups = [("Mode", lambda n: n == "AGENT_OS_ENV"), ("Claude", lambda n: n.startswith("ANTHROPIC")),
              ("Polymarket account 1 (" + ("acct-pm-live-1" if live else "acct-pm-test-1") + ")", lambda n: n.startswith("POLYMARKET_ACCT1")),
              ("Optional", lambda n: True)]
    done = set()
    for title, pick in groups:
        names = [r["name"] for r in rows if r["name"] not in done and pick(r["name"])]
        if not names: continue
        lines.append("# " + title)
        for nm in names:
            v = "live" if (live and nm == "AGENT_OS_ENV") else ENV_FAKE.get(nm, "")
            lines.append(f"{nm}={v}")
            done.add(nm)
        lines.append("")
    return {"lang": "dotenv", "title": f".secrets/{'live' if live else 'test'}/.env with fake values",
            "body": "\n".join(lines).rstrip() + "\n",
            "note": "Every variable from the Variables tab, one KEY=value per line. Values here are fake; this page never stores real ones."}

def example_for(n):
    if (n["num"] or "") in ("47.1.1", "47.2.1"):
        return env_example(n["num"])
    if (n["num"] or "") in JOBS:
        return jobs_example(n["num"])
    if (n["num"] or "") in LINKS:
        return links_example(n["num"])
    return None

def table(tab_id, title, columns, rows, note):
    return {"id": tab_id, "title": title, "type": "table", "columns": columns, "rows": rows, "note": note}

def fields_for(n):
    name, num, path = n["name"], n["num"] or "", n["path"]
    if num == "11.1": return SYSTEM_CONFIG
    if num == "19.2.4": return DOMAIN_CONFIG
    if name.endswith(".workers.json") and not (n.get("link") or n.get("is_link")): return WORKERS_CONFIG
    if name.endswith(".links.json") and not (n.get("link") or n.get("is_link")): return LINKS_CONFIG
    if num == "11.11": return MODELS_CONFIG
    if num == "27.2": return AGENT_CONFIG
    if name == "tests.config.json": return TESTS_CONFIG
    if name == "index.json" and "/research/" in path: return RESEARCH_INDEX
    if name == "settings.json": return SETTINGS_JSON
    if num == "47.3": return SECRETS_INDEX
    if num in ("47.1.1", "47.2.1"): return env_fields(num)
    if name == "package.json": return PACKAGE_JSON
    if name == "[subagent-name].md" or name.endswith("-agent.md"): return SUBAGENT_MD
    if name.startswith("runs.jsonl"): return RUNS_JSONL
    return None

# ---- domain agents: Overview (capabilities table) + Agents tab (built live on the page from the tree)
CAP_COLUMNS = [
 {"key": "capability", "label": "Capability", "kind": "text"},
 {"key": "what", "label": "What it does", "kind": "text"},
 {"key": "status", "label": "Status", "kind": "select", "options": ["implemented", "in progress", "planned", "idea"]},
 {"key": "related", "label": "Related agents, skills, scripts, workers", "kind": "text"},
 {"key": "notes", "label": "Notes", "kind": "text"},
]
def cap(capability, what, related, status="planned", notes=""):
    return {"capability": capability, "what": what, "status": status, "related": related, "notes": notes}
CAPS = {
 "10": [
  cap("Manage all domains", "Oversees every domain agent: health, resources, what each is working on.", "subagents.link/ in every content folder, one link per domain (D-030)"),
  cap("Create new agents", "Turns owner input into a new agent: scaffold the folder, register it in the index and UI, link its docs.", "scripts/system [14.1]; agents index; sys-docs-agent [10.1.1.2]"),
  cap("Develop the system", "Builds and updates shared scripts, workers, configs and docs every agent uses.", "scripts [14]; configs [11]; docs [2]"),
  cap("Run shared workers", "Runs data-collection workers on their schedule and keeps their output clean.", "system.workers.json [11.10]; scripts/workers [14.2]"),
  cap("Schedule every agent's jobs", "One scheduler runs every job from every agent's workers file on time, locally or in the cloud, and shows them by domain.", "scheduler, run-job [14.1]; configs/subagents.link [11.2]; scheduler-state [16.1]"),
  cap("Keep every link right", "Builds every file link from each agent's links file plus the child links, removes stale ones, checks them and keeps an index of who reads what.", "relink, check-links [14.1]; [name].links.json in every configs/ [11.13]; links index [16.1]"),
  cap("Model and platform routing", "Keeps the list of models/platforms and routes each agent to its model.", "models.config.json [11.11]"),
  cap("Answer owner questions", "Answers questions about system state and acts on owner comments.", "sys-knowledge-agent [10.1.1.2]"),
  cap("Keep the knowledge base current", "Files every owner input and system change into the docs, keeps the knowledge map and the How it works summaries of every file and folder in line (D-033).", "sys-knowledge-agent [10.1.1.2]; skills [10.1.2.1], [10.1.2.2]; docs [2]"),
  cap("System self-improvement", "Reads logs, data, research and owner comments; proposes and tests improvements at system level.", "sys-self-improvement-agent [10.1.1.1]; research [10.9]; tests [10.8]"),
  cap("Run tests", "Runs tests from tests.config.json, writes results; before_promote tests gate promotion.", "run-tests [14.1]; tests [10.8]"),
  cap("Safety and secrets", "Test/live separation, kill switch, keys loaded only at execution time.", "load-secret [14.1]; .secrets [47]; settings.json [10.1.6]"),
  cap("Logs and analytics", "Collects logs and performance per agent for the UI.", "logs [15]; data [16]; trading-ui [45]"),
 ],
 "19": [
  cap("Own the prediction-market domain", "Responsible for Polymarket (first) and later other prediction markets: domain health and coverage.", "CLAUDE.md [19.1.5]"),
  cap("Find and create strategies", "Finds, creates and updates strategy agents and their self-improvement sub-agents.", "strategy agents [21]; skills [19.1.2]"),
  cap("Compare and promote variants", "Compares variants of each strategy and proposes promotion or retirement; the owner approves.", "research [19.13]; tests [19.12]; strategy agents [21]"),
  cap("Domain self-improvement", "Reads domain logs, data, research and owner comments; improves domain rules and strategies.", "pm-self-improvement-agent [19.1.1.2]", "planned", "sub-agent is proposed"),
  cap("Domain data and workers", "Decides which Polymarket workers the domain needs and runs them as its own jobs.", "prediction-market-agents.workers.json [19.2.1] (markets-catalog, polymarket-prices [19.3.5])"),
  cap("Answer owner questions", "Explains what the domain and its strategies are doing and why.", "CLAUDE.md [19.1.5]; docs [19.6]"),
  cap("Domain docs", "Keeps the domain's own docs and file links up to date.", "docs [19.6]"),
  cap("Domain tests", "Keeps prompt and script tests for the domain level.", "tests [19.12]"),
 ],
}
AGENT_INFO = {
 "10": {"level": "system", "keywords": []},
 "19": {"level": "domain", "keywords": ["polymarket", "pm-"]},
}
def agent_for(n):
    return AGENT_INFO.get(n["num"] or "")

def custom_tabs_for(n):
    num, name = n["num"] or "", n["name"]
    if num in CAPS:
        return [table("capabilities", "Capabilities", CAP_COLUMNS, CAPS[num],
            "What this agent can do and should do. Add a row for anything new; saving it also updates related files.")]
    if num == "47.1.1":
        return [table("variables", "Variables", ENV_COLUMNS, ENV_ROWS,
            "The variables test/.env must have. Values are never stored on this page: fill them in the local file (or later in the trading UI [45]). A script can write .env.example from this table.")]
    if num == "47.2.1":
        return [table("variables", "Variables", ENV_COLUMNS, env_rows("47.2.1"),
            "Same names as test/.env with live values, owner only (D-027). Names only here, never values.")]
    if name == "tests.config.json":
        kind = "agents" if "/agents/" in n["path"] else "scripts"
        rows = ([{"id": "t-agents-001", "name": "refuses to trade when the kill switch is on", "enabled": True, "schedule": "before_promote", "last_result": "success", "next_action": ""}]
                if kind == "agents" else
                [{"id": "t-scripts-001", "name": "make-buy respects max position size", "enabled": True, "schedule": "on_change", "last_result": "fail", "next_action": "fix the cap check in make-buy, then re-run"}])
        return [table("tests", "Tests", [
            {"key": "id", "label": "Id", "kind": "text"}, {"key": "name", "label": "What it checks", "kind": "text"},
            {"key": "enabled", "label": "On", "kind": "bool"},
            {"key": "schedule", "label": "When", "kind": "select", "options": ["manual", "on_change", "interval:1h", "before_promote"]},
            {"key": "last_result", "label": "Last result", "kind": "select", "options": ["never", "success", "fail", "error", "skipped"]},
            {"key": "next_action", "label": "Next action", "kind": "text"}], rows,
            "Example rows. When the agent exists, run-tests fills Last result.")]
    if num in JOBS:
        t = table("jobs", "Jobs", JOB_COLUMNS, JOBS[num],
            "Every job this agent runs. Turn one off with On, change When, Where, Platform or Model in the row, and open Details for the prompt, workspace, tools and limits. Saving updates the file.")
        t["layout"] = "jobs"
        return [t]
    if num in LINKS:
        return [table("links", "Links", LINK_COLUMNS, LINKS[num],
            "Every file this agent links, where it appears and where it comes from: the system, its own domain or strategy, another domain, or any agent by name. Saving updates the links file; relink then builds the links. Child links (subagents.link/) are built from the folder tree and not listed.")]
    if num == "11.11":
        return [table("routes", "Routes", [
            {"key": "who", "label": "Agent / sub-agent / worker", "kind": "text"},
            {"key": "model", "label": "Model", "kind": "select", "options": ["fable-5.1", "opus-5.5", "sonnet-5.5", "haiku-4.5", "composer-2.5"]},
            {"key": "effort", "label": "Effort", "kind": "select", "options": ["low", "medium", "high", "xhigh"]}],
            [{"who": "defaults: main", "model": "opus-5.5", "effort": "medium"}, {"who": "defaults: si", "model": "opus-5.5", "effort": "high"},
             {"who": "defaults: sub", "model": "sonnet-5.5", "effort": "medium"}, {"who": "news-digest", "model": "sonnet-5.5", "effort": "low"}],
            "Which model each thing runs on. A named route wins over the type default.")]
    return []

# ---- jobs files (D-029): one per agent, same format everywhere; the Jobs tab edits these rows
AI_TYPES = ["agent", "subagent", "skill", "workflow", "command"]
JOB_COLUMNS = [
 {"key": "enabled", "label": "On", "kind": "bool", "main": True},
 {"key": "id", "label": "Job", "kind": "text", "main": True},
 {"key": "purpose", "label": "Purpose", "kind": "text", "main": True},
 {"key": "type", "label": "Type", "kind": "select", "options": ["script"] + AI_TYPES, "main": True},
 {"key": "run", "label": "Runs", "kind": "text", "main": True},
 {"key": "schedule", "label": "When", "kind": "text", "main": True},
 {"key": "run_on", "label": "Where", "kind": "select", "options": ["local", "cloud", "desktop", "github-actions"], "main": True},
 {"key": "platform", "label": "Platform", "kind": "select", "options": ["none", "claude-code", "cursor", "codex"], "main": True},
 {"key": "model", "label": "Model", "kind": "select", "options": ["route", "fable-5.1", "opus-5.5", "sonnet-5.5", "haiku-4.5", "composer-2.5"], "main": True, "ai": True},
 {"key": "effort", "label": "Effort", "kind": "select", "options": ["low", "medium", "high", "xhigh", "max"], "ai": True},
 {"key": "prompt", "label": "Prompt (text, or @file)", "kind": "long", "ai": True},
 {"key": "workspace", "label": "Workspace (folder it runs in)", "kind": "text", "ai": True},
 {"key": "allowed_tools", "label": "Allowed tools", "kind": "text", "ai": True},
 {"key": "permission_mode", "label": "Permission mode", "kind": "select", "options": ["default", "acceptEdits", "plan"], "ai": True},
 {"key": "max_turns", "label": "Max turns", "kind": "text", "ai": True},
 {"key": "max_cost_usd", "label": "Max cost per run (USD)", "kind": "text", "ai": True},
 {"key": "on_change", "label": "Also runs when these change", "kind": "text"},
 {"key": "outputs", "label": "Writes", "kind": "text"},
 {"key": "secret_keys", "label": "Secret keys (names only)", "kind": "text"},
 {"key": "timeout", "label": "Timeout", "kind": "text"},
 {"key": "retries", "label": "Retries", "kind": "text"},
 {"key": "concurrency", "label": "If the last run is still going", "kind": "select", "options": ["skip", "queue", "restart"]},
 {"key": "mode", "label": "Mode", "kind": "select", "options": ["test", "live"]},
 {"key": "notify", "label": "Tell the owner", "kind": "select", "options": ["never", "failure", "always"]},
]
def job(id, purpose, type, run, schedule, run_on="local", platform=None, model="", **kw):
    ai = type != "script"
    r = {"enabled": kw.pop("enabled", True), "id": id, "purpose": purpose, "type": type, "run": run, "schedule": schedule,
         "run_on": run_on, "platform": platform or ("claude-code" if ai else "none"), "model": (model or "route") if ai else ""}
    for c in JOB_COLUMNS:
        r.setdefault(c["key"], "")
    r.update({k: ("" if v is None else v) for k, v in kw.items()})
    if not r["mode"]: r["mode"] = "test"
    if not r["notify"]: r["notify"] = "failure"
    if not r["concurrency"]: r["concurrency"] = "skip"
    return r
JOB_FILES = {  # num -> (agent name, workspace)
 "11.10": ("system", "agents/system"),
 "19.2.1": ("prediction-market-agents", "agents/trading/prediction-market"),
 "21.2.1": ("strategy-1-agent", "agents/trading/prediction-market/strategy-1-agent"),
 "27.4": ("pm-strategy-1.momentum-v1.opus55-test", "agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test"),
}
JOBS = {
 "11.10": [
  job("relink", "Rebuild links when any links file changes, plus one full run a day", "script", "node scripts/system/relink.system.js --changed", "cron 0 4 * * *",
      on_change="agents/**/configs/*.links.json", concurrency="queue", timeout="5m"),
  job("check-links", "Find broken, missing or upward links and any link into .secrets", "script", "node scripts/system/check-links.system.js", "cron 0 * * * *", timeout="5m"),
  job("news-digest", "Digest of the news the domains follow", "subagent", "news-digest", "every 6h", model="sonnet-5.5", effort="low",
      prompt="Summarise the news from the last 6 hours that the domains follow (for the prediction-market domain: what could move its markets). Write data/subagents/news-digest/latest.md.",
      allowed_tools="Read, WebSearch, WebFetch, Write(data/subagents/news-digest/**)", permission_mode="acceptEdits", max_turns="20", max_cost_usd="0.5",
      outputs="data/subagents/news-digest/latest.md", timeout="15m"),
  job("system-self-improvement", "Review system logs, costs and owner comments; open research items", "subagent", "sys-self-improvement-agent", "cron 0 3 * * *",
      model="opus-5.5", effort="high", prompt="@docs/prompts/system-si.md", allowed_tools="Read, Grep, Glob, Write(research/**)", permission_mode="acceptEdits",
      max_turns="40", max_cost_usd="3", timeout="45m"),
  job("knowledge-sync", "File every new owner input and system change into the knowledge base, then refresh the stale How it works summaries (D-033)", "subagent", "sys-knowledge-agent", "cron 30 2 * * *",
      model="opus-5.5", effort="medium", on_change="agents/**, agents/system/docs/inputs/**", concurrency="queue",
      prompt="Run the knowledge-intake skill for every input in docs/inputs/index.json and every page input with status new that is not processed yet, and for every change since the last run (git log). Then run file-index until build-map --stale is empty. Report what changed.",
      allowed_tools="Read, Grep, Glob, Edit, Write(docs/**), Bash(python3 scripts/system/build-map.system.py*)", permission_mode="acceptEdits", max_turns="60", max_cost_usd="3",
      outputs="docs/index/knowledge-map.json, every [name].index.md", timeout="45m"),
  job("scripts-review", "Weekly review of shared scripts by a second platform", "command", "/review-scripts", "cron 0 9 * * 5", run_on="cloud", platform="codex",
      enabled=False, prompt="Review scripts/ for bugs and risky code. Report only; change nothing.", permission_mode="plan", max_turns="20", timeout="30m", notify="always"),
 ],
 "19.2.1": [
  job("domain-session", "Check domain health, strategies and owner comments", "agent", "", "every 4h", effort="high", prompt="@docs/prompts/domain-session.md",
      allowed_tools="Read, Grep, Glob, Bash(node scripts/*), Write(data/**), Write(docs/**)", permission_mode="acceptEdits", max_turns="40", max_cost_usd="2", timeout="30m"),
  job("markets-catalog", "Catalogue of Polymarket markets the domain cares about", "script", "python scripts/markets-catalog.worker.py", "every 1h",
      outputs="data/markets-catalog/latest.json", timeout="5m", retries="1"),
  job("polymarket-prices", "Prices and volume for all active Polymarket markets", "script", "python scripts/polymarket-prices.worker.py", "every 5m",
      outputs="data/polymarket-prices/latest.json", timeout="2m", retries="2"),
  job("domain-self-improvement", "Compare strategies across the domain; propose new ones", "subagent", "pm-self-improvement-agent", "cron 0 2 * * *",
      model="opus-5.5", effort="high", prompt="@docs/prompts/domain-si.md", permission_mode="acceptEdits", max_turns="50", max_cost_usd="4", timeout="60m"),
  job("election-night-check", "One-off: list positions on US election markets that resolve tonight", "skill", "polymarket-resolution-check", "once 2026-11-03 20:00",
      timezone="America/New_York", model="sonnet-5.5", effort="medium", prompt="Check every open position on US election markets and report which resolve tonight and the risk on each.",
      max_turns="20", max_cost_usd="1", notify="always"),
 ],
 "21.2.1": [
  job("strategy-session", "Compare today's variants and write the daily summary", "agent", "", "cron 0 23 * * *", effort="high", prompt="@docs/prompts/strategy-session.md",
      permission_mode="acceptEdits", max_turns="30", max_cost_usd="2", timeout="30m"),
  job("compare-variants", "Side-by-side report of every variant's results", "workflow", "compare-variants", "after strategy-session", model="sonnet-5.5", effort="medium",
      outputs="data/variant-report/latest.md", max_turns="20", timeout="20m"),
  job("strategy-self-improvement", "Try improvements as new test variants", "subagent", "pm-strategy-1-self-improvement-agent", "cron 30 3 * * *",
      model="opus-5.5", effort="xhigh", prompt="@docs/prompts/strategy-si.md", allowed_tools="Read, Grep, Glob, Bash(node ../../../system/scripts/system/create-agent.system.js *)",
      permission_mode="acceptEdits", max_turns="60", max_cost_usd="5", timeout="90m"),
 ],
 "27.4": [
  job("main-run", "Trade on 24h momentum (test mode)", "agent", "", "every 15m", model="opus-5.5", effort="high", prompt="@docs/prompts/main-run.md",
      allowed_tools="Read, Bash(node scripts/*), Bash(python scripts/*), Write(data/**)", permission_mode="acceptEdits", max_turns="30", max_cost_usd="1",
      on_change="data/polymarket-prices.link.json", concurrency="restart", timeout="10m", secret_keys="POLYMARKET_ACCT1_*"),
  job("get-polymarket-data", "Market details for this agent's markets", "script", "python scripts/get-polymarket-data.worker.py", "every 15m",
      outputs="data/get-polymarket-data/latest.json", timeout="3m", retries="2"),
  job("clean-data", "Clean and normalise the fetched data", "script", "node scripts/clean-data.system.js", "after get-polymarket-data", timeout="2m"),
  job("close-before-resolution", "One-off: close open positions before the market resolves", "command", "/close-before-resolution", "once 2026-10-31 18:00",
      timezone="UTC", prompt="Close every open position on markets that resolve within the next hour. Test mode only.", max_turns="15", max_cost_usd="0.5", notify="always"),
 ],
}
# The owner turned every system job off on the page (2026-10-09, in-20261009-1040): they stay in the file and never run until turned on.
for _r in JOBS["11.10"]:
    _r["enabled"] = False
LIST_KEYS = ("allowed_tools", "on_change", "outputs", "secret_keys")
NUM_KEYS = ("max_turns", "retries", "max_cost_usd")
def job_json(r, defaults):
    o = {}
    for c in JOB_COLUMNS:
        k, v = c["key"], r.get(c["key"])
        if v in ("", None) or (k in defaults and defaults[k] == v): continue
        if k in LIST_KEYS: v = [x.strip() for x in str(v).split(",") if x.strip()]
        elif k in NUM_KEYS:
            try: v = float(v) if "." in str(v) else int(v)
            except ValueError: pass
        o[k] = v
    if "enabled" not in o: o = {"enabled": r.get("enabled", False), **o}
    return o
def jobs_example(num):
    import json
    agent, ws = JOB_FILES[num]
    defaults = {"timezone": "UTC", "run_on": "local", "workspace": ws, "mode": "test", "notify": "failure", "concurrency": "skip", "permission_mode": "default"}
    doc = {"schema_version": 1, "agent": agent, "defaults": defaults, "jobs": [job_json(r, defaults) for r in JOBS[num]]}
    return {"lang": "json", "title": "Example: " + agent + ".workers.json (built from the Jobs tab rows)", "body": json.dumps(doc, indent=2, ensure_ascii=False),
            "note": "Values that match defaults are left out of each job. Runtime state (last run, result, next run) is not in this file: the scheduler keeps it in data/system/scheduler-state.json."}

# ---- links files (D-031): one per agent, same format everywhere; the Links tab edits these rows
LINK_COLUMNS = [
 {"key": "enabled", "label": "On", "kind": "bool"},
 {"key": "to", "label": "Link in this agent", "kind": "text"},
 {"key": "from", "label": "Points at", "kind": "text"},
 {"key": "why", "label": "Why", "kind": "text"},
 {"key": "required", "label": "Required", "kind": "bool"},
 {"key": "added_by", "label": "Added by", "kind": "text"},
]
def link(to, frm, why, required=True, added_by="create-agent", enabled=True):
    return {"enabled": enabled, "to": to, "from": frm, "why": why, "required": required, "added_by": added_by}
RELINK = link("scripts/relink.system.link.js", "@system/scripts/system/relink.system.js", "rerun after editing this file")
TEST_RUNNERS = [link("tests/agents/run-tests.system.link.js", "@system/scripts/system/run-tests.system.js", "run the agent tests next to their config"),
                link("tests/scripts/run-tests.system.link.js", "@system/scripts/system/run-tests.system.js", "run the script tests next to their config")]
LINK_FILES = {"11.13": "system", "19.2.3": "prediction-market-agents", "21.2.3": "strategy-1-agent", "27.3": "pm-strategy-1.momentum-v1.opus55-test"}
LINKS = {
 "11.13": [
  *TEST_RUNNERS,
 ],
 "19.2.3": [
  link("data/news-digest.link.md", "@system/data/subagents/news-digest/latest.md", "news for the domain session", required=False),
  link("docs/safety.link.md", "@system/docs/safety.md", "hard limits every domain follows"),
  *TEST_RUNNERS,
  RELINK,
 ],
 "21.2.3": [
  link("data/markets-catalog.link.json", "@domain/data/markets-catalog/latest.json", "compare variants market by market"),
  link("docs/trading-metrics.link.md", "@domain/docs/trading-metrics.md", "how variants are compared and promoted"),
  *TEST_RUNNERS,
  RELINK,
 ],
 "27.3": [
  link("configs/system.config.link.json", "@system/configs/system.config.json", "global modes, the stop switch, triggers"),
  link("configs/prediction-market-agents.config.link.json", "@domain/configs/prediction-market-agents.config.json", "its domain's risk limits, accounts and venues"),
  link("configs/models.config.link.json", "@system/configs/models.config.json", "its model route"),
  link("data/polymarket-prices.link.json", "@domain/data/polymarket-prices/latest.json", "price input for make-buy"),
  link("data/news-digest.link.md", "@system/data/subagents/news-digest/latest.md", "news context for the main run", required=False),
  link("data/markets-catalog.link.json", "@domain/data/markets-catalog/latest.json", "which markets it may trade"),
  link("scripts/risk-check.decision.link.js", "@domain/scripts/decisions/risk-check.decision.js", "its domain's shared risk gate"),
  link("scripts/run-tests.system.link.js", "@system/scripts/system/run-tests.system.js", "run both kinds of tests"),
  link("tests/agents/run-tests.system.link.js", "@system/scripts/system/run-tests.system.js", "run the agent tests next to their config"),
  link("tests/scripts/run-tests.system.link.js", "@system/scripts/system/run-tests.system.js", "run the script tests next to their config"),
  RELINK,
  link("logs/polymarket-prices.worker.link.log", "@domain/logs/jobs/polymarket-prices/latest.log", "see when prices are stale", required=False),
  link("docs/safety.link.md", "@system/docs/safety.md", "rules it may never break"),
  link("docs/agent-architecture.link.md", "@system/docs/common/agent-architecture.md", "how agents work inside"),
  link("docs/trading-safety.link.md", "@domain/docs/trading-safety.md", "money rules it may never break"),
  link("docs/trading-agent-architecture.link.md", "@domain/docs/common/trading-agent-architecture.md", "how a trading agent runs"),
 ],
}
def links_example(num):
    import json
    agent = LINK_FILES[num]
    doc = {"schema_version": 1, "agent": agent,
           "links": [dict(r, added="2026-10-02" if r["added_by"] not in ("create-agent", "owner") else "2026-09-29") for r in LINKS[num]]}
    return {"lang": "json", "title": "Example: " + agent + ".links.json (built from the Links tab rows)", "body": json.dumps(doc, indent=2, ensure_ascii=False),
            "note": "relink turns every enabled entry into a relative symlink at `to`. @domain and @strategy are this agent's own; @[name] finds any domain or agent by its unique name. Child links (subagents.link/) are not listed."}
