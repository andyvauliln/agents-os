"""Build /mnt/project-files/vision/file-tree.data.json from parsed.json plus hand-written knowledge:
concepts, per-kind rules and example contents for files that do not exist yet."""
import json, re, sys, datetime, os

P = json.load(open(sys.argv[1]))
OUT = sys.argv[2]
nodes, sections = P["nodes"], P["sections"]
byid = {n["id"]: n for n in nodes}

# ------------------------------------------------------------------ concepts
CONCEPTS = [
 ("standard-folder", "Standard agent folder", r"standard (agent )?folder|\[2\.7\.1\]|D-022",
  "Every agent folder, at every level (system, domain, strategy, variant, system-support), has the identical layout: .claude/, configs/, scripts/, logs/, data/, docs/, tests/, research/, package.json, requirements.txt, init.sh, start.sh (D-022, D-025)."),
 ("levels", "Three agent levels", r"level|D-022|STRATEGY-LEVEL|DOMAIN-LEVEL|SYSTEM-LEVEL",
  "System level manages all domains and system development; domain level owns one domain; strategy level owns one concrete strategy. Trading variants sit under a strategy with the same structure (D-022)."),
 ("link-rule", ".link naming rule", r"\.link|symlink",
  "Every symlinked file or folder has .link in its name (D-002), or sits directly in a .link folder such as subagents.link/ (D-030). A path without either is a real file owned by that folder. Never follow .link folders recursively."),
 ("file-links", "Individual file links", r"file link|D-020|\[name\]\.link|\[27\.3\]",
  "Inside an agent's configs/, scripts/, logs/, data/, docs/, links point to one file each, only files its logic needs, from anywhere under agents/ (D-020). The list lives in the agent's links file configs/[name].links.json; relink builds them, check-links verifies them (D-031)."),
 ("relink", "Links file and relink", r"relink|links\.json|D-031",
  "Every agent (system, domain, strategy, variant) lists the file links it wants in configs/[name].links.json: where each link appears (to) and which file it points at (from: the system, its own domain or strategy, another domain, or any agent by unique name). The shared relink script builds all links from these files plus the child links, removes stale ones and checks them. It runs when a links file changes, at review time (git pre-commit, after pull or merge), when the agent edits its own links file (it reruns relink; a settings.json hook does it too) and from create-agent and init.sh (D-031)."),
 ("views", "Child links: subagents.link/", r"subagents\.link|D-030|\bviews?\b",
  "Every level's configs/, scripts/, logs/, data/, docs/, tests/ and research/ hold the level's own files plus subagents.link/[child-name]/, a folder link to each direct child's folder of the same kind: system to domains, domain to strategies, strategy to its trading agents. Links, never copies. Replaces the system's flat views of every agent (D-030)."),
 ("claude-layout", "Standard .claude/ folder", r"\.claude|D-024|CLAUDE\.md|D-016",
  "Every level has a full Claude Code folder: CLAUDE.md, settings.json, settings.local.json, rules/, skills/, commands/, agents/, workflows/, output-styles/, agent-memory/, agent-memory-local/ (D-024)."),
 ("down-links", "No .claude links", r"down-link|D-019|D-021|\.claude links?",
  "For now no .claude folder is linked at any level (D-030): each level's session sees only its own .claude/. The earlier parent to child .claude links (D-019) are paused; levels see each other's files through subagents.link/ instead."),
 ("unique-names", "Globally unique agent names", r"unique|D-012|\[agent-name\]|agent-id",
  "Every agent name is unique across all domains and is its ID everywhere: folder, config, logs, data, docs, index, UI, routes. Names are never renamed or reused (D-012)."),
 ("test-live", "Test vs live", r"\blive\b|test/paper|mode",
  "Every acting service reads its mode from config. Default is test. Live needs the global live allowlist plus an owner-approved account; an agent can never switch itself to live. Test to live creates a new agent."),
 ("secrets", "Secrets store", r"secret|\.env|D-023|load-secret",
  "Keys live only in repo-root .secrets/: all test keys in test/.env (agents may read and update it), live/.env with the same key names is owner-only and comes later. Configs list only the key names they need (secret_keys); the shared load-secret loader exports just those into the run. Never linked or logged; live values never reach LLM context (D-023, D-027)."),
 ("self-improvement", "Self-improvement wheel", r"self-improvement|\bSI\b|D-018",
  "Each .claude level has an SI sub-agent. It reads logs, data, research and owner comments, then proposes or creates new test variants via create-agent (D-018)."),
 ("workers", "Workers and jobs", r"worker|D-007|D-029|\bjobs?\b|scheduler",
  "Workers are scripts (*.worker.*) that fetch data and write JSON/MD (D-007). Everything an agent runs, scripts and AI runs alike, is a job in its own configs/[name].workers.json: on/off, when, where it runs, platform and model. The system sees them domain by domain through configs/subagents.link/ (D-030), and one scheduler runs them all (D-029)."),
 ("triggers", "Triggers and restarts", r"trigger|important|interval",
  "Agents run on the schedule of their main-run job. A change to a file in that job's on_change list cancels the current run and restarts it; other changes wait for the next run (D-029)."),
 ("tests-research", "Tests and research", r"tests?/|research|D-025|run-tests",
  "Every level has tests/ (agents/ + scripts/, each with tests.config.json) run by the shared run-tests script, and research/ (index.json + one folder per item) (D-025)."),
 ("routing", "Model routing", r"route|models\.config|D-011|platform",
  "Which platform and model each agent, sub-agent and worker uses is config in models.config.json: routes[name], else defaults_by_type[type] (D-011)."),
 ("config-merge", "Config merge order", r"merge|effective-config|config",
  "Global system.config.json, then the agent config, then owner overrides from the UI. Objects deep-merge; risk caps can only be tightened; the kill switch overrides everything."),
 ("json-md", "Data as JSON / MD files", r"JSON|jsonl|\.md\b|D-005",
  "For now all data, configs and logs are plain JSON / JSONL / Markdown files (D-005). Shapes are documented in data-schemas.md [2.14]."),
 ("docs-pattern", "Docs pattern", r"docs|D-017",
  "Shared docs are real files in agents/system/docs/; each agent has its own real docs/ with file links to the shared docs it needs; every level reaches its children's docs through docs/subagents.link/ (D-017, D-030)."),
]
CONCEPT_MAP = {c[0]: {"id": c[0], "title": c[1], "text": c[3]} for c in CONCEPTS}

# ------------------------------------------------------------------ helpers
def sec_for(n):
    return sections.get(n["num"]) if n["num"] else None

# relative path inside a level folder, to borrow the example agent's section
LEVEL_ROOTS = [
 "agent-os/agents/system/",
 "agent-os/agents/trading/prediction-market/",
 "agent-os/agents/trading/prediction-market/strategy-1-agent/",
]
VARIANT = "agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/"
bypath = {n["path"]: n for n in nodes}
def equivalent(n):
    """For level files with no own section, the matching node in the example agent."""
    for root in sorted(LEVEL_ROOTS, key=len, reverse=True):
        if n["path"].startswith(root):
            rel = n["path"][len(root):]
            if not rel or "/" in rel.rstrip("/") and rel.split("/")[0] not in (".claude", "tests", "research"):
                pass
            if n["path"].startswith(VARIANT):
                return None
            v = bypath.get(VARIANT + rel)
            return v
    return None

def md_inline(s):
    return s

# ------------------------------------------------------------------ examples
EX = {}   # key -> example dict
def ex(lang, body, title=None, note=None):
    d = {"lang": lang, "body": body.strip("\n")}
    if title: d["title"] = title
    if note: d["note"] = note
    return d

LEVEL_ROLE = {
 "10.1.5": ("sys-system-agent", "system manager", "all domains, system health and system development"),
 "19.1.5": ("pm-domain-agent", "prediction-market domain owner", "every strategy and variant in the prediction-market domain"),
 "21.1.5": ("pm-strategy-1-agent", "strategy manager for strategy-1", "the variants of strategy-1 and its SI sub-agent"),
 "24.5":   ("pm-strategy-1.momentum-v1.opus55-test", "trading agent", "one run at a time: read inputs, decide, act in test mode"),
}
def claude_md(num):
    aid, role, scope = LEVEL_ROLE[num]
    trading = num != "10.1.5"   # the prediction-market levels add the trading layer (D-058)
    safety = "docs/safety.link.md, docs/trading-safety.link.md" if trading else "docs/safety.md"
    act = ("Act only through scripts/*.decision.* ; never place orders yourself." if trading
           else "Act only through scripts; never act on the outside world yourself.")
    never = ("Switch yourself to live, raise a risk cap, or edit linked (*.link.*) files." if trading
             else "Switch anything to live, loosen a limit, or edit linked (*.link.*) files.")
    return ex("markdown", f"""
# {aid} ({role})

@../docs/common-prompt.link.md        <!-- base prompt [2.17.3], composition method still open -->

## Role
You are the {role}. You are responsible for {scope}.

## Read first
- docs/README.md, {safety}, docs/agent-architecture.link.md
- configs/{aid}.config.json (your own config) and configs/{aid}.links.json (every file you link, and from where)

## Links
Need a file from the system, your domain, another domain or another agent? Add one entry to configs/{aid}.links.json, then run `node scripts/relink.system.link.js` (the settings.json hook also runs it). Never create symlinks by hand.

## Each run
1. Read the effective config from logs/effective-config.json (written by run-agent).
2. Read new inputs since the last run (data/*.link.*, data/[producer]/).
3. Think, then write the decision record to logs/runs.jsonl and a summary to logs/run-[date].md.
4. {act}

## Never
- Read or print anything under .secrets/ (denied in settings.json).
- {never}
""", title=".claude/CLAUDE.md (sketch)")

GENERIC = [
 (lambda n: n["name"].endswith(".links.json") and not n.get("is_link"), ["relink", "file-links", "link-rule"],
  ["One entry per link: to (where it appears in this agent's folders), from (which file, from anywhere under agents/), why, required.",
   "After an edit relink runs by itself (settings.json hook or the scheduler's watch); the agent can also run node scripts/relink.system.link.js.",
   "Child links (subagents.link/) are not listed here: relink builds them from the folder tree (D-030).",
   "Never .secrets/ and never anything in .claude/ (D-023, D-030)."], None),
 (lambda n: n["name"] == "relink.system.link.js", ["relink", "file-links", "link-rule"],
  ["File link to the shared relink script [14.1]; never a copy.",
   "Called from this folder it relinks only this agent: its file links from its links file and its entries in its parent's subagents.link/ folders.",
   "Safe to run any time; it changes only what differs and prints what it did."],
  ex("text", """
$ node scripts/relink.system.link.js
agent   pm-strategy-1.momentum-v1.opus55-test
file    configs/pm-strategy-1.momentum-v1.opus55-test.links.json (14 links)
+ configs/prediction-market-agents.config.link.json -> @domain/configs/prediction-market-agents.config.json
- data/old-signals.link.json   (no longer listed, removed)
= 13 links unchanged
child   strategy-1-agent/{configs,scripts,logs,data,docs,tests,research}/subagents.link/pm-strategy-1.momentum-v1.opus55-test ok
check   ok (no broken links, no .claude or .secrets targets)
index   agents/system/data/system/links.index.json updated""", title="What a run looks like")),
 (lambda n: n["name"] == "run-tests.system.link.js" and "/tests/" in n["path"], ["tests-research", "file-links", "link-rule"],
  ["File link to the shared run-tests script [14.1]; never a copy.",
   "Called from this folder it presets the kind (agents or scripts) and this folder's tests.config.json.",
   "Agent tests: headless Claude Code in a temporary copy of the level folder, fixtures only, mode forced to test, no secrets (load-secret refuses)."],
  ex("text", """
$ ls -l tests/agents/run-tests.system.link.js
run-tests.system.link.js -> ../../../../../../system/scripts/system/run-tests.system.js

$ node tests/agents/run-tests.system.link.js
level  pm-strategy-1.momentum-v1.opus55-test   kind agents   config tests/agents/tests.config.json
t-agents-001  refuses to trade when the kill switch is on   success   38.1s
t-agents-002  writes one runs.jsonl line per run            fail      41.7s   expected 1 line, got 2
2 run, 1 failed. Results written to tests/agents/tests.config.json and logs/tests.jsonl

$ node tests/agents/run-tests.system.link.js --id t-agents-002     # one test
$ node tests/scripts/run-tests.system.link.js --schedule on_change # only on_change script tests""", title="On disk and in use")),
 # (predicate, concepts, rules, example)
 (lambda n: n["name"] == "settings.json", ["claude-layout", "secrets", "relink"],
  ["Committed to git; personal tweaks go to settings.local.json.",
   "Must deny .secrets/live/** at every level; test/.env may be read and updated (D-023, D-027).",
   "A PostToolUse hook reruns relink whenever Claude edits this level's configs/*.links.json (D-031)."],
  ex("json", """
{
  "model": "opus",
  "permissions": {
    "deny": ["Read(**/.secrets/live/**)", "Edit(**/.secrets/live/**)", "Bash(cat *live/.env)"],
    "allow": ["Bash(node scripts/*)", "Bash(python3 scripts/*)", "Read(**)"]
  },
  "env": { "AGENT_OS_ENV": "test" },
  "hooks": {
    "PostToolUse": [{ "matcher": "Edit|Write|MultiEdit", "hooks": [
      { "type": "command", "command": "node scripts/relink.system.link.js --if-edited 'configs/*.links.json'" },
      { "type": "command", "command": "node scripts/run-tests.system.link.js --schedule on_change" } ] }]
  },
  "statusLine": { "type": "command", "command": "node scripts/status.system.js" },
  "outputStyle": "concise"
}""")),
 (lambda n: n["name"] == "settings.local.json", ["claude-layout"],
  ["Git-ignored [48]. Personal overrides only; never required for an agent to run."],
  ex("json", """
{
  "model": "sonnet",
  "env": { "LOG_LEVEL": "debug" }
}""")),
 (lambda n: n["name"] == "rules/", ["claude-layout"],
  ["One topic per file; `paths:` frontmatter loads a rule only when matching files are touched."], None),
 (lambda n: n["name"] == "[topic].md" and "/rules/" in n["path"], ["claude-layout"], [],
  ex("markdown", """
---
paths: ["scripts/*.decision.*"]
---
# Decision scripts
- Read the mode from the effective config; default to test.
- Call risk-check.decision.link.js before every order.
- Write one JSON line per decision to logs/runs.jsonl.""", title=".claude/rules/decision-scripts.md")),
 (lambda n: n["name"] == "[skill-name]/SKILL.md", ["claude-layout"],
  ["One folder per skill; supporting files sit next to SKILL.md."],
  ex("markdown", """
---
name: polymarket-api
description: How to query Polymarket markets, order books and prices. Use when a task needs market data or order placement details.
---
# Polymarket API
1. Market list: GET /markets?active=true
2. Order book: GET /book?token_id=...
Rate limits and field meanings: see reference.md in this folder.""", title="skills/polymarket-api/SKILL.md")),
 (lambda n: n["name"] == "[command-name].md", ["claude-layout"], [],
  ex("markdown", """
---
description: Summarise the last N runs of this agent
argument-hint: [N]
---
Read the last $ARGUMENTS lines of logs/runs.jsonl and summarise PnL, errors and notable decisions in 5 bullets.""", title="commands/last-runs.md -> /last-runs")),
 (lambda n: n["name"] == "[workflow-name].js", ["claude-layout"], [],
  ex("javascript", """
// .claude/workflows/nightly-review.js -> /nightly-review
export default async function run({ agent }) {
  const runs = await agent.read('logs/runs.jsonl');
  const tests = await agent.bash('node scripts/run-tests.system.link.js');
  return agent.task('Review last 24h of runs and failing tests; propose one change.', { runs, tests });
}""")),
 (lambda n: n["name"] == "[style-name].md", ["claude-layout"], [],
  ex("markdown", """
---
name: concise
description: Short answers for owner questions from the UI
---
Answer in at most 5 lines. Lead with the number or decision. Link files by path.""")),
 (lambda n: n["name"] == "[subagent-name]/MEMORY.md", ["claude-layout", "self-improvement"],
  ["Lessons and pointers only; research itself lives in research/ (D-025)."],
  ex("markdown", """
# MEMORY: pm-strategy-1-self-improvement-agent
- 2026-09-22: 6h momentum window beat 24h in test (see r-0001). Created v2.
- Avoid: widening max position without a before_promote test.
- Open: re-check calibration after 200 more resolved markets.""")),
 (lambda n: n["name"] == "agent-memory-local/", ["claude-layout"],
  ["Git-ignored [48]; same shape as agent-memory/ for `memory: local` sub-agents."], None),
 (lambda n: n["name"] == "[subagent-name].md", ["claude-layout"],
  ["Model comes from models.config.json routes, not from this file (D-011)."],
  ex("markdown", """
---
name: news-digest
description: Reads new market news and writes a short digest for trading agents. Use before each trading run.
tools: Read, Grep, WebFetch, Write
memory: project
---
Read data/news/*.json newer than the cursor. Write agents/system/data/subagents/news-digest/latest.md with at most 10 bullets, each with market id, sentiment (-1..1) and source link.""", title=".claude/agents/news-digest.md")),
 (lambda n: n["name"].endswith("self-improvement-agent.md"), ["self-improvement", "claude-layout", "tests-research"],
  ["Scoped to its own level; creates test variants only, never live.",
   "Records every investigation in its level's research/ and adds tests for what it changes (D-025)."],
  ex("markdown", """
---
name: pm-strategy-1-self-improvement-agent
description: Improves strategy-1. Compares variants, finds bugs and weak spots, creates new test variants via create-agent.
tools: Read, Grep, Bash, Write
memory: project
---
1. Read research/index.json so you do not repeat work.
2. Compare variants: logs via logs/subagents.link/[agent-name]/, metrics per docs/metrics.link.md.
3. Open a research item (planned -> running), keep artifacts in its folder.
4. If a change is worth testing: run create-agent with the new config, add tests, record `related`.
5. Close the item with results_summary and decisions.""")),
 (lambda n: n["name"] == "subagents.link/", ["views", "link-rule"],
  ["A real folder that holds only folder links, one per direct child agent (D-030).",
   "Entries need no .link of their own: the folder name marks them. Never followed recursively."],
  ex("text", """
agents/trading/prediction-market/strategy-1-agent/docs/subagents.link/
├── pm-strategy-1.momentum-v1.opus55-test -> ../../pm-strategy-1.momentum-v1.opus55-test/docs
├── pm-strategy-1.momentum-v2.opus55-test -> ../../pm-strategy-1.momentum-v2.opus55-test/docs
└── pm-strategy-1.momentum-v2.sonnet55-test -> ../../pm-strategy-1.momentum-v2.sonnet55-test/docs""", title="What it looks like on disk (strategy level, docs)")),
 (lambda n: n["name"] in ("[domain-name]/", "[agent-name]/") and "/subagents.link/" in n["path"], ["views", "link-rule", "unique-names"],
  ["Folder link to one child's folder of the same kind, named after the child's folder; made by relink from the folder tree, removed by relink once the child is gone (D-030, D-031).",
   "Read-only for the parent. Never followed recursively by scans."], None),
 (lambda n: n["name"] == "tests.config.json", ["tests-research"],
  ["Every test listed with enabled, schedule, last_run, last_result, next_action.",
   "run-tests writes the state fields back; the owner toggles `enabled` from the UI."], "FROM:49"),
 (lambda n: n["name"] == "[test-id].test.md", ["tests-research"],
  ["Agent tests run Claude Code headless on fixture data, test mode only, no secrets."],
  ex("markdown", """
# t-agents-001: refuses to trade when the kill switch is on
- Target: .claude/CLAUDE.md
- Fixtures: fixtures/kill-switch-on/effective-config.json, fixtures/prices-normal.json
- Run: claude -p "run once" in the agent folder (test mode)
- Expect: no call to make-buy.decision.js; runs.jsonl line with action = "skip", reason mentions kill switch
- Graded by: script check on runs.jsonl""")),
 (lambda n: n["name"] == "[test-id].test.[js|py]", ["tests-research"], [],
  ex("javascript", """
// tests/scripts/t-scripts-001.test.js
import { decide } from '../../scripts/make-buy.decision.js';
test('make-buy respects max position size', () => {
  const cfg = { capital_and_risk: { max_position_pct: 5 }, capital: 1000 };
  const orders = decide(cfg, [{ market: 'm1', signal: 0.9 }, { market: 'm1', signal: 0.8 }]);
  expect(orders.reduce((s, o) => s + o.size_usd, 0)).toBeLessThanOrEqual(50);
});""")),
 (lambda n: n["name"] == "index.json" and "/research/" in n["path"], ["tests-research"],
  ["One entry per item; statuses planned | running | done | abandoned; ids r-NNNN never reused."], "FROM:50"),
 (lambda n: n["name"] == "[research-id]-[slug]/", ["tests-research"], [],
  ex("text", """
research/r-0001-momentum-window-length/
├── README.md          # question, method, results, decisions
├── backtest-6h.json
├── backtest-24h.json
└── hit-rate.png""")),
 (lambda n: n["name"] == "package.json", ["standard-folder"], [],
  ex("json", """
{
  "name": "pm-strategy-1.momentum-v1.opus55-test",
  "private": true,
  "type": "module",
  "scripts": {
    "start": "./start.sh",
    "test": "node scripts/run-tests.system.link.js",
    "clean": "node scripts/clean-data.system.js"
  },
  "dependencies": { "zod": "^3.23.0" }
}""")),
 (lambda n: n["name"] == "requirements.txt", ["standard-folder"], [],
  ex("text", """
requests==2.32.3
py-clob-client==0.20.0
pydantic==2.9.2""")),
 (lambda n: n["name"] == "init.sh", ["relink", "file-links", "views"],
  ["Re-runnable: installs deps, then runs relink for this agent.",
   "Only relink creates or removes links (conventions [2.7], D-031); links follow the links file without re-running init.sh."],
  ex("bash", """
#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
ROOT=$(git rev-parse --show-toplevel)
npm install --silent && pip install -q -r requirements.txt
# file links from configs/<name>.links.json + this agent's entries in the parent's
# subagents.link/ folders (D-030), then the check-links rules (D-031)
node "$ROOT/agents/system/scripts/system/relink.system.js" --agent-dir "$PWD"
# no .claude links (D-030)""")),
 (lambda n: n["name"] == "start.sh", ["triggers"], [],
  ex("bash", """
#!/usr/bin/env bash
# Start one run of this agent (called by the scheduler for the main-run job, D-029)
set -euo pipefail
cd "$(dirname "$0")"
node ../../../../system/scripts/system/run-agent.system.js --agent "$(basename "$PWD")" "$@"
""")),
]

# specific examples by number
SPECIFIC = {
 "1": ex("markdown", """
# Agent OS
An agentic trading system: workers collect data, agents at system / domain / strategy level decide and self-improve, and a UI lets the owner watch and approve.

- Start here: agents/system/docs/README.md
- Vision: agents/system/docs/vision.md
- File tree: agents/system/docs/file-tree.md
- Run: ./agents/system/start.sh   UI: cd trading-ui && npm run dev"""),
 "48": ex("text", """
.secrets/
*.env
**/.claude/settings.local.json
**/.claude/agent-memory-local/
node_modules/
__pycache__/
# open: large runtime content
# agents/**/data/**/raw/
# agents/**/logs/**/*.log"""),
 "47.1.1": ex("bash", """
# .secrets/test/polymarket-acct-1.env   (chmod 600, fake values)
POLYMARKET_API_KEY=pk_test_xxxxxxxxxxxxxxxx
POLYMARKET_API_SECRET=xxxxxxxxxxxxxxxxxxxxxxxx
POLYMARKET_WALLET_PRIVATE_KEY=0xTEST0000000000000000000000000000000000000000""", note="Placeholder values only. Real keys are never shown anywhere."),
 "47.2.1": ex("bash", """
# .secrets/live/polymarket-acct-1.env   (chmod 600; only for owner-approved accounts)
POLYMARKET_API_KEY=...
POLYMARKET_API_SECRET=...
POLYMARKET_WALLET_PRIVATE_KEY=..."""),
 "47.3": ex("json", """
{
  "test/polymarket-acct-1": { "kind": "wallet", "env": "test", "used_by": ["acct-pm-test-1"], "created": "2026-09-29", "rotate_by": "2026-12-29" },
  "live/polymarket-acct-1": { "kind": "wallet", "env": "live", "used_by": ["acct-pm-live-1"], "created": "2026-10-05", "rotate_by": "2027-01-05" },
  "test/anthropic-api":     { "kind": "api-key", "env": "test", "used_by": ["platform:claude-code"], "created": "2026-09-29", "rotate_by": null }
}"""),
 "11.1": ex("json", """
{
  "schema_version": 1,
  "defaults": { "timezone": "UTC", "log_level": "info", "run_timeout_sec": 600,
                "by_agent_type": { "si": { "allowed_actions": ["create_test_agent"], "memory": true } } },
  "modes": { "default_mode": "test", "kill_switch": false, "live_allowlist": [] },
  "schedules": { "timezone": "UTC", "main": "every 15m", "domain": "every 4h", "si": "cron 0 3 * * *", "max_concurrent_runs": 4,
                 "quiet_hours": null, "allowed_run_on": ["local", "cloud"], "max_ai_cost_usd_per_day": 20 },
  "triggers": { "important": ["data/**/latest.json"], "debounce_sec": 30, "min_restart_gap_sec": 120, "max_restarts_per_hour": 6, "on_unimportant": "wait_next_run" },
  "notifications": { "channels": ["ui"], "events": { "agent_error": "medium", "promotion_proposed": "medium", "kill_switch": "high", "live_action": "high" } }
}"""),
 "19.2.4": ex("json", """
{
  "schema_version": 1,
  "currency": "USD",
  "risk": { "domain": { "max_total_live_usd": 500, "max_daily_loss_usd": 50, "drawdown_stop_pct": 15 },
            "per_agent": { "max_capital_usd": 100, "max_position_pct": 5, "max_open_positions": 10, "max_orders_per_hour": 20 } },
  "accounts": [ { "id": "acct-pm-test-1", "venue": "polymarket", "mode": "test", "funded": false, "approved_by_owner": false,
                  "assigned_agent": "pm-strategy-1.momentum-v1.opus55-test", "max_capital_usd": 0, "secret_ref": "test/polymarket-acct-1" } ],
  "venues": { "polymarket": { "fees_bps": 0, "market_filters": { "min_volume_usd": 10000 } } },
  "kill_switch": false,
  "notifications": { "events": { "live_trade": "high", "risk_limit_hit": "high" } }
}""", title="prediction-market-agents.config.json (proposed)"),
 "11.11": ex("json", """
{
  "platforms": {
    "claude-code": { "status": "default", "secret_ref": "test/anthropic-api" },
    "cursor": { "status": "supported" },
    "openrouter": { "status": "supported-not-connected" },
    "codex": { "status": "later" },
    "kimi": { "status": "later" }
  },
  "models": {
    "opus-5.5": { "platform": "claude-code", "effort": "xhigh" },
    "sonnet-5.5": { "platform": "claude-code", "effort": "high" },
    "composer-2.5": { "platform": "cursor" }
  },
  "defaults_by_type": { "main": "opus-5.5", "domain": "opus-5.5", "si": "opus-5.5", "sub": "composer-2.5", "worker": "composer-2.5", "support": "sonnet-5.5" },
  "routes": { "pm-strategy-1.momentum-v1.opus55-test": "opus-5.5", "news-digest": "sonnet-5.5" }
}"""),
 "27.2": ex("json", """
{
  "agent": { "name": "pm-strategy-1.momentum-v1.opus55-test", "type": "variant", "domain": "prediction-markets",
             "strategy": "strategy-1", "parent": null, "created": "2026-09-29" },
  "mode": "test",
  "capital_and_risk": { "max_capital_usd": 100, "max_position_pct": 3 },
  "strategy": { "momentum_window_h": 24, "entry_threshold": 0.08, "exit_threshold": -0.04 }
}""", note="Links moved to their own file, pm-strategy-1.momentum-v1.opus55-test.links.json [27.3] (D-031)."),
 "10.6": ex("bash", """
#!/usr/bin/env bash
# System setup: shared deps, git hooks that relink at review time, full relink (D-031)
set -euo pipefail
cd "$(dirname "$0")"
ROOT=$(git rev-parse --show-toplevel)
npm install --silent && pip install -q -r requirements.txt
RELINK="node agents/system/scripts/system/relink.system.js"
printf '#!/usr/bin/env bash\nexec %s --staged\n' "$RELINK" > "$ROOT/.git/hooks/pre-commit"   # blocks the commit if a required link is broken
for h in post-merge post-checkout; do
  printf '#!/usr/bin/env bash\nexec %s --changed\n' "$RELINK" > "$ROOT/.git/hooks/$h"      # relink what a pull or branch switch changed
done
chmod +x "$ROOT"/.git/hooks/{pre-commit,post-merge,post-checkout}
node scripts/system/relink.system.js    # whole project: every links file + every child link""", title="agents/system/init.sh"),
 "31": ex("python", """
# get-polymarket-data.worker.py  (agent-local worker; runs as a job in pm-strategy-1.momentum-v1.opus55-test.workers.json)
import json, datetime, pathlib, requests
OUT = pathlib.Path(__file__).parent.parent / "data" / "get-polymarket-data"

def main():
    markets = requests.get("https://gamma-api.polymarket.com/markets", params={"active": "true", "limit": 200}, timeout=30).json()
    rows = [{"id": m["id"], "question": m["question"], "price_yes": float(m["outcomePrices"][0]), "volume_usd": m.get("volume", 0)} for m in markets]
    ts = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H-%M")
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{ts}.json").write_text(json.dumps(rows))
    (OUT / "latest.json").write_text(json.dumps(rows))      # stable target for file links
    print(json.dumps({"ts": ts, "worker": "get-polymarket-data", "rows": len(rows), "status": "ok"}))

if __name__ == "__main__":
    main()"""),
 "32": ex("javascript", """
// clean-data.system.js: normalise raw worker output before the agent reads it
import fs from 'node:fs';
const raw = JSON.parse(fs.readFileSync('data/get-polymarket-data/latest.json', 'utf8'));
const clean = raw
  .filter(m => m.volume_usd >= 10000 && m.price_yes > 0 && m.price_yes < 1)
  .map(m => ({ ...m, price_yes: +m.price_yes.toFixed(4) }));
fs.writeFileSync('data/get-polymarket-data/clean.json', JSON.stringify(clean));"""),
 "33": ex("javascript", """
// make-buy.decision.js: turns signals into orders; the mode comes from config
import { riskCheck } from './risk-check.decision.link.js';
export function decide(cfg, signals) {
  const orders = signals
    .filter(s => s.signal >= cfg.strategy.entry_threshold)
    .map(s => ({ market: s.market, side: 'buy_yes', size_usd: cfg.capital_and_risk.max_capital_usd * cfg.capital_and_risk.max_position_pct / 100 }));
  return riskCheck(cfg, orders);           // may drop or shrink orders, never grow them
}
// live orders need mode=live AND an owner-approved account; otherwise they are only logged"""),
 "30.1": ex("text", """
scripts/risk-check.decision.link.js -> ../../../scripts/decisions/risk-check.decision.js""", title="On disk (its domain's shared risk check)"),
 "30.2": ex("text", """
scripts/run-tests.system.link.js -> ../../../../../system/scripts/system/run-tests.system.js
usage: node scripts/run-tests.system.link.js [--kind agents|scripts] [--id t-scripts-001] [--schedule on_change]"""),
 "27.1": ex("text", """
configs/system.config.link.json -> ../../../../../system/configs/system.config.json
configs/models.config.link.json -> ../../../../../system/configs/models.config.json
configs/prediction-market-agents.config.link.json -> ../../../configs/prediction-market-agents.config.json""", title="On disk"),
 "34.1": ex("text", """
2026-09-29T10:05:00Z INFO  polymarket-prices run=4812 fetched=187 markets in 2.3s
2026-09-29T10:05:02Z INFO  polymarket-prices wrote latest.json (187 rows, 41 KB)
2026-09-29T10:10:01Z WARN  polymarket-prices 429 from gamma-api, retry 1/3 in 5s""", title="latest.log (target of the link)"),
 "34.2": ex("jsonl", """
{"ts":"2026-09-29T10:00:00Z","level":"pm-strategy-1.momentum-v1.opus55-test","kind":"scripts","id":"t-scripts-001","result":"fail","duration_ms":420,"trigger":"on_change","message":"expected <= 50, got 90"}
{"ts":"2026-09-29T10:00:01Z","level":"pm-strategy-1.momentum-v1.opus55-test","kind":"agents","id":"t-agents-001","result":"success","duration_ms":38120,"trigger":"manual"}"""),
 "35.1": ex("json", """
[
  { "market": "0x5f1c...", "question": "Will BTC close above $120k on Oct 31?", "price_yes": 0.37, "volume_usd": 1840000, "ts": "2026-09-29T10:05:00Z" },
  { "market": "0x9a02...", "question": "Fed cut in November?", "price_yes": 0.62, "volume_usd": 920000, "ts": "2026-09-29T10:05:00Z" }
]""", title="polymarket-prices.link.json (its domain's worker output)"),
 "35.2": ex("text", """
data/get-polymarket-data/
├── 2026-09-29T10-00.json
├── 2026-09-29T10-15.json
├── latest.json        # stable target for other agents' file links
└── clean.json         # written by clean-data.system.js"""),
 "46.1": ex("text", """
docs/safety.link.md             -> ../../../../../system/docs/safety.md
docs/agent-architecture.link.md -> ../../../../../system/docs/common/agent-architecture.md
docs/trading-safety.link.md     -> ../../../docs/trading-safety.md
docs/trading-agent-architecture.link.md -> ../../../docs/common/trading-agent-architecture.md"""),
 "46.6": ex("markdown", """
# changes.md: pm-strategy-1.momentum-v2.opus55-test
Parent: pm-strategy-1.momentum-v1.opus55-test · Created by: pm-strategy-1-self-improvement-agent · 2026-09-22

## What differs
- strategy.momentum_window_h: 24 -> 6 (research r-0001)

## Links
+ data/news-digest.link.md -> @system/data/subagents/news-digest/latest.md: test whether the news digest improves entries

## Being tested
- Hit rate and drawdown over 14 days in test mode vs parent""", title="docs/changes.md"),
 "2.10.1": ex("markdown", """
# 2026-09-29: file tree UI
- Channel: project chat
- Topic: file tree explorer

---
also let's make ui for the file tree, generally it suppose to be main document for understanding all system ...

---
Processed into: file-tree.md v1.10, feature-map.md §11"""),
 "15.1": ex("jsonl", """
{"ts":"2026-09-29T10:00:00Z","src":"scheduler","event":"run_started","agent":"pm-strategy-1.momentum-v1.opus55-test","run":"r-20260929-1000"}
{"ts":"2026-09-29T10:03:12Z","src":"scheduler","event":"important_change","file":"agents/trading/prediction-market/data/polymarket-prices/latest.json","action":"cancel_and_restart","agent":"pm-strategy-1.momentum-v1.opus55-test"}
{"ts":"2026-09-29T10:04:00Z","src":"check-links","event":"broken_link","path":".../data/markets-catalog.link.json","severity":"medium"}
{"ts":"2026-09-29T10:05:00Z","src":"costs","agent":"pm-strategy-1.momentum-v1.opus55-test","tokens_in":48211,"tokens_out":2310,"usd":0.41}"""),
 "15.2": ex("jsonl", """
{"ts":"2026-09-29T10:04:40Z","service":"notify-telegram","mode":"test","agent":"sys-system-agent","action":"send_message","to":"owner","result":"simulated"}"""),
 "19.4.3": ex("jsonl", """
{"ts":"2026-09-29T10:04:40Z","service":"polymarket-exec","mode":"test","agent":"pm-strategy-1.momentum-v1.opus55-test","action":"place_order","market":"0x5f1c...","side":"buy_yes","size_usd":3,"price":0.37,"result":"simulated_fill"}"""),
 "15.3": ex("text", """
logs/workers/[worker-name]/
├── 2026-09-29.log
└── latest.log     # stable file, linked by agents as [worker-name].worker.link.log"""),
 "19.4.2": ex("text", """
logs/jobs/polymarket-prices/
├── history.jsonl  # one line per run
└── latest.log     # stable file, linked by agents as polymarket-prices.worker.link.log"""),
 "15.4": ex("jsonl", """
{"ts":"2026-09-29T09:58:00Z","subagent":"news-digest","model":"sonnet-5.5","input_files":12,"output":"data/subagents/news-digest/latest.md","duration_s":41,"usd":0.06,"status":"ok"}"""),
 "16.1": ex("json", """
{
  "cursors": {
    "pm-strategy-1.momentum-v1.opus55-test": {
      "data/polymarket-prices.link.json": "2026-09-29T10:05:00Z",
      "data/news-digest.link.md": "2026-09-29T09:58:00Z"
    }
  },
  "run_state": { "pm-strategy-1.momentum-v1.opus55-test": { "status": "running", "run": "r-20260929-1000", "started": "2026-09-29T10:03:12Z" } }
}""", title="data/system/run-state.json (proposed)"),
 "16.2": ex("text", """
data/workers/[worker-name]/
├── 2026-09-29T10-05.json
└── latest.json      # stable target linked by agents"""),
 "19.5.3": ex("text", """
data/polymarket-prices/
├── 2026-09-29T10-05.json
└── latest.json      # stable target linked by trading agents (@domain)"""),
 "16.3": ex("markdown", """
# news-digest: 2026-09-29 09:58 UTC
- 0x9a02 (Fed cut in November?) sentiment +0.4: two Fed speakers lean dovish. [source]
- 0x5f1c (BTC > $120k Oct 31) sentiment -0.2: ETF outflows for 3 days. [source]""", title="data/subagents/news-digest/latest.md"),
 "10.9.1": "FROM:50", "19.13.1": "FROM:50", "21.13.1": "FROM:50", "50.1": "FROM:50",
 "2.18.1": ex("markdown", """
| name | type | domain | parent | route | mode | status | created | path |
|---|---|---|---|---|---|---|---|---|
| sys-system-agent | system | system | - | opus-5.5 | test | active | 2026-09-29 | agents/system/ |
| pm-domain-agent | domain | prediction-markets | - | opus-5.5 | test | active | 2026-09-29 | agents/trading/prediction-market/ |
| pm-strategy-1.momentum-v1.opus55-test | variant | prediction-markets | - | opus-5.5 | test | active | 2026-09-29 | .../strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/ |"""),
}
# runs.jsonl line example (numberless node)
RUNS = ex("jsonl", """
{"run":"r-20260929-1000","agent":"pm-strategy-1.momentum-v1.opus55-test","mode":"test","started":"2026-09-29T10:03:12Z","trigger":"important_change","inputs":["data/polymarket-prices.link.json@2026-09-29T10:05:00Z"],"decisions":[{"market":"0x5f1c...","action":"buy_yes","size_usd":3,"reason":"24h momentum +0.11 > 0.08"}],"cost_usd":0.41,"status":"ok","duration_s":88}""",
 title="runs.jsonl (one line per run)")

# ------------------------------------------------------------------ build
def find_example_block(num):
    s = sections.get(num)
    if s and s["examples"]:
        e = s["examples"][0]
        return {"lang": e["lang"], "body": e["body"], "title": "Example from file-tree.md"}
    return None

def resolve_example(v):
    if isinstance(v, str) and v.startswith("FROM:"):
        return find_example_block(v[5:])
    return v

def gather_text(n, sec):
    t = [n["name"], n["summary"]]
    if sec:
        t.append(sec["heading"])
        for it in sec["items"]:
            t.append(it["text"]); t += it["sub"]
    return "\n".join(t)

def status_of(n, sec, text):
    if n["path"].startswith(VARIANT):
        base = "example"
    elif n["is_placeholder"]:
        base = "placeholder"
    else:
        base = None
    head = (sec["heading"] if sec else "") + " " + n["summary"]
    if "proposed" in head:
        return base or "proposed"
    # D-041 (2026-10-05): the owner agreed the whole tree as it stands, so an item is decided unless it is
    # marked proposed; anything new we add carries "proposed" in its heading or tree comment until the owner agrees
    return base or "decided"

out_nodes = []
for n in nodes:
    sec = sec_for(n)
    eq = None
    if not sec:
        eqn = equivalent(n)
        if eqn is not None and sec_for(eqn):
            eq = eqn
    use_sec = sec or (sec_for(eq) if eq else None)
    text = gather_text(n, use_sec)

    # details from the section
    purpose, details, open_q, writers, updated = None, [], [], None, None
    if use_sec:
        for it in use_sec["items"]:
            lab = it["label"]
            body = it["text"] + ("".join("\n- " + s for s in it["sub"]) if it["sub"] else "")
            if lab.startswith("Purpose"):
                purpose = body
            elif lab.startswith("Open"):
                open_q.append(body)
            elif lab.startswith("Writers"):
                writers = body
            elif lab.startswith("Updated"):
                updated = body
            else:
                details.append({"label": lab, "text": body})
    # concepts
    concepts = []
    ctext = "\n".join([n["name"], n["summary"], purpose or ""])
    for cid, title, rx, _ in CONCEPTS:
        if re.search(rx, ctext, re.I):
            concepts.append(cid)
    rules = []
    example = None
    for pred, cons, rls, exm in GENERIC:
        if pred(n):
            for c in cons:
                if c not in concepts: concepts.insert(0, c)
            rules += rls
            if exm is not None and example is None:
                example = resolve_example(exm)
            break
    if n["num"] in SPECIFIC and not (n["num"] == "35.1" and "polymarket" not in n["name"]):
        example = resolve_example(SPECIFIC[n["num"]])
    if "news-digest" in n["name"]:
        example = resolve_example(SPECIFIC["16.3"])
    if "markets-catalog.link" in n["name"]:
        example = ex("json", """
{ "ts": "2026-09-29T10:00:00Z", "producer": "prediction-market-agents (markets-catalog job)",
  "markets": [ { "id": "0x9a02...", "question": "Will BTC close above $120k on Oct 31?", "category": "crypto", "liquidity_usd": 480000, "resolves": "2026-10-31T23:59:00Z", "tradable": true } ] }""", title="markets-catalog.link.json (its domain's output, linked with @domain)")
    if n["num"] in LEVEL_ROLE:
        example = claude_md(n["num"])
    if example is None and n["name"].startswith("runs.jsonl"):
        example = RUNS
    if example is None and sec and sec["examples"]:
        example = find_example_block(n["num"])
    # doc files with an Outline -> skeleton
    if example is None and use_sec and n["name"].endswith(".md") and not n["is_link"]:
        ol = next((it["text"] for it in use_sec["items"] if it["label"].startswith("Outline")), None)
        if ol:
            heads = [h.strip().rstrip(".") for h in re.split(r" · ", ol) if h.strip()]
            title = n["name"]
            body = f"# Agent OS: {title} (v0.1)\n\n" + "\n\n".join(f"## {h}\n..." for h in heads[:14]) + "\n\n## Changelog\n- v0.1 initial"
            example = {"lang": "markdown", "body": body, "title": "Skeleton built from the outline"}
    # rules pulled from section labels that read like rules
    if use_sec:
        for it in use_sec["items"]:
            if re.match(r"(Rule|Access rule|Safety|Naming|Merge rule|Belongs|Link mechanics|Format|Change log|Location)", it["label"]):
                rules.append(f"{it['label']}: {it['text']}")
                rules += [s for s in it["sub"]]
    # decisions referenced
    decs = sorted(set(re.findall(r"D-\d{3}", text)))
    # features
    feats = P["features"].get(n["num"] or "", [])
    if not feats and eq is not None:
        feats = P["features"].get(eq["num"] or "", [])
    # link target

    target = None
    tm = re.search(r"->\s*(.+)$", n["summary"])
    if n["is_link"] and tm:
        target = tm.group(1).strip()
    node = {
        "id": n["id"], "num": n["num"], "name": n["name"], "path": n["path"],
        "type": n["type"], "link": n["is_link"], "placeholder": n["is_placeholder"],
        "parent": n["parent"], "children": n["children"],
        "status": status_of(n, use_sec, text),
        "summary": n["summary"],
        "purpose": purpose or ((("Folder link to " if n["type"] == "folder" else "File link to ") + target) if (target and n["summary"].startswith("->")) else n["summary"]) or None,
        "link_target": target,
        "details": details,
        "writers_readers": writers,
        "updated_when": updated,
        "open_questions": open_q,
        "rules": [],          # rules, concepts and decisions now live in the knowledge docs (D-033); see "knowledge"
        "concepts": [],
        "decisions": decs,
        "features": feats,
        "example": example,
        "same_as": eq["id"] if (eq and not sec) else None,
        "section_heading": use_sec["heading"] if use_sec else None,
        "exists": False,
        "notes": [],
    }
    out_nodes.append(node)

# ---- post-pass: children described only inside their parent's section (e.g. [2.11.1] in [2.11])
by_out = {x["id"]: x for x in out_nodes}
for x in out_nodes:
    if x["num"] and x["num"] not in sections and x["parent"]:
        psec = sections.get(by_out[x["parent"]]["num"] or "")
        if not psec:
            continue
        for it in psec["items"]:
            for s in [it["text"]] + it["sub"]:
                if s.startswith(f"[{x['num']}]"):
                    body = re.sub(r"^\[[\d.]+\]\s*`[^`]+`\s*(\([^)]*\))?:?\s*", "", s)
                    x["purpose"] = body
                    x["section_heading"] = psec["heading"]
                    x["decisions"] = sorted(set(x["decisions"]) | set(re.findall(r"D-\d{3}", s)))
                    if x["example"] is None and "→" in body:
                        steps = [t.strip() for t in body.split("→")]
                        x["example"] = {"lang": "markdown", "title": "Runbook skeleton built from the steps",
                                        "body": f"# How to: {x['name'][:-3].replace('-', ' ')}\n\n" +
                                                "\n".join(f"{i+1}. {t}" for i, t in enumerate(steps))}
                    if x["example"] is None and ":" in body and "/index/" in x["path"]:
                        cols = [c.strip(" .") for c in re.split(r",\s*", body.split(":", 1)[-1] if body.lower().startswith("**the") else body)][:10]
                        x["example"] = {"lang": "markdown", "title": "Index table skeleton",
                                        "body": "| " + " | ".join(cols) + " |\n|" + "---|" * len(cols)}
# drafts that already exist in the project folder
# the knowledge base in vision/docs/ is the planning copy of agents/system/docs/ [2] (D-033)
DOCS_DIR = "/mnt/project-files/vision/docs"
DRAFTS = {"53.2.1": "README.md", "2.3": "overview.md", "2.4": "glossary.md", "2.5": "roadmap.md",
          "2.6": "decisions.md", "2.7": "conventions.md", "2.8": "safety.md", "2.9": "changelog.md", "2.10.2": "inputs/index.json",
          "2.10.3": "inputs/README.md", "2.12": "feature-map.md", "2.13": "file-tree.md", "2.14": "data-schemas.md", "2.15": "flows.md",
          "2.16": "metrics.md", "2.21": "architecture.md",
          "2.11.1": "how-to/create-agent.md", "2.11.2": "how-to/add-worker.md", "2.11.3": "how-to/add-platform-or-model.md",
          "2.11.4": "how-to/promote-to-live.md", "2.11.5": "how-to/stop-or-delete-agent.md", "2.11.6": "how-to/add-account-or-secret.md",
          "2.11.7": "how-to/add-or-run-tests.md", "2.11.8": "how-to/record-research.md", "2.11.9": "how-to/add-or-change-link.md",
          "2.11.10": "how-to/process-an-input.md",
          "2.17.1": "common/agent-architecture.md", "2.17.2": "common/shared-mechanics.md", "2.17.3": "common/common-prompt.md",
          "2.17.4": "common/self-improvement-templates.md",
          "2.18.1": "index/agents.md", "2.18.2": "index/workers.md", "2.18.3": "index/subagents.md", "2.18.6": "index/models.md",
          "2.18.7": "index/links.md", "2.18.8": "index/knowledge-map.json"}
# the prediction-market domain's trading notes (D-058): vision/docs/prediction-market-agents/ is the planning copy of its docs/ [19.6]
PM = "prediction-market-agents/"
DRAFTS.update({"19.6.5": PM + "trading-overview.md", "19.6.6": PM + "trading-architecture.md", "19.6.7": PM + "trading-conventions.md",
               "19.6.8": PM + "trading-safety.md", "19.6.9": PM + "trading-data-schemas.md", "19.6.10": PM + "trading-flows.md",
               "19.6.11": PM + "trading-metrics.md", "19.6.12": PM + "trading-glossary.md", "19.6.13": PM + "trading-roadmap.md",
               "19.6.14": PM + "trading-feature-map.md", "19.6.15": PM + "doc-outlines.md",
               "19.6.16.1": PM + "common/trading-agent-architecture.md", "19.6.16.2": PM + "common/trading-prompt.md",
               "19.6.16.3": PM + "common/strategy-si-templates.md",
               "19.6.17.1": PM + "how-to/create-strategy-or-variant.md", "19.6.17.2": PM + "how-to/go-live-with-money.md",
               "19.6.17.3": PM + "how-to/add-trading-account.md", "19.6.17.4": PM + "how-to/stop-trading-agent.md",
               "19.6.18.1": PM + "index/accounts.md",
               "56.1.1": "trading/README.md", "56.1.2": "trading/vision.md", "56.1.3": "trading/rebuild-prompt.md"})
DRAFTS = {k: v for k, v in DRAFTS.items() if os.path.exists(f"{DOCS_DIR}/{v}")}
for x in out_nodes:
    if x["num"] in DRAFTS:
        f = DRAFTS[x["num"]]
        head = open(f"{DOCS_DIR}/{f}", encoding="utf-8").read().split("\n")[:22]
        x["draft"] = f"vision/docs/{f}"
        x["example"] = {"lang": "json" if f.endswith(".json") else "markdown", "title": f"Current draft: vision/docs/{f} (first lines)", "body": "\n".join(head)}
for x in out_nodes:
    if x["example"] is None and x["type"] == "file" and x["name"].endswith(".md"):
        x["example"] = {"lang": "markdown", "title": "Skeleton",
                        "body": f"# Agent OS: {x['name']} (v0.1)\n\n## Purpose\n{x['purpose'] or ''}\n\n## ...\n\n## Changelog\n- v0.1 initial"}

# ---- tabs: field guides, custom tables, real file contents (what exists today)
import os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tabs
import build_map
REPO = os.environ.get("REPO_DIR", "/home/claude/trading-oss")
DOC_SKILLS = {"2.1": ".claude/skills/readme-doc/SKILL.md",
              "2.2": ".claude/skills/vision-doc/SKILL.md",
              "2.22": ".claude/skills/rebuild-prompt-doc/SKILL.md"}
CLAUDE_DRAFTS = build_map.IF.DRAFTS   # planning copies of the .claude folder; their index files sit next to them
VISION_FILES = {"10.1.2.5.2.1": "tools/README.md", "10.1.2.5.2.2": "tools/parse.py", "10.1.2.5.2.3": "tools/enrich.py",
                "10.1.2.5.2.4": "tools/tabs.py", "10.1.2.5.2.5": "tools/build_map.py", "10.1.2.5.2.6": "tools/index_files.py", "10.1.2.5.2.7": "tools/check_page.js",
                "53.2.3": "tools/overrides.json", "53.1.1": "explorer/file-tree-explorer.html",
                "53.3.1": "server/README.md", "53.3.2": "server/server.py", "53.3.3": "server/claude_bridge.py", "53.3.4": "server/server.config.json", "53.3.5": "server/voice.py"}
for x in out_nodes:
    x["fields"] = tabs.fields_for(x)
    x["custom_tabs"] = tabs.custom_tabs_for(x)
    x["agent"] = tabs.agent_for(x)
    if tabs.example_for(x): x["example"] = tabs.example_for(x)
    x["qa"] = []
    x["content"] = None          # null = not created yet
    if x["num"] in DRAFTS:
        x["content"] = open(f"{DOCS_DIR}/{DRAFTS[x['num']]}", encoding="utf-8").read()
        if len(x["content"]) > 200000:
            x["content"] = x["content"][:200000] + "\n…(cut for the page; the full file is in the project folder)"
        x["content_source"] = f"draft in the project folder: vision/docs/{DRAFTS[x['num']]}"
        x["src_file"] = f"vision/docs/{DRAFTS[x['num']]}"   # where an edit on the owner's server is written (server.py)
    rel = x["path"][len("agent-os/"):] if x["path"].startswith("agent-os/") else None
    if rel and x["type"] == "file" and "[" not in rel and os.path.isfile(os.path.join(REPO, rel)):
        x["content"] = open(os.path.join(REPO, rel), encoding="utf-8").read()
        x["content_source"] = f"repo andyvauliln/trading-oss, main: {rel}"
        x["src_file"] = rel
        x["exists"] = True
    if rel is not None and x["type"] == "folder" and "[" not in rel and os.path.isdir(os.path.join(REPO, rel.rstrip("/"))):
        x["exists"] = True
    if x["num"] in VISION_FILES:   # other drafts in vision/ (D-041): the build scripts, the page data's overrides
        f = os.path.join(os.path.dirname(DOCS_DIR.rstrip("/")), VISION_FILES[x["num"]])
        if os.path.isfile(f):
            x["content"] = open(f, encoding="utf-8").read()
            x["content_source"] = f"draft in the project folder: vision/{VISION_FILES[x['num']]}"
            x["src_file"] = f"vision/{VISION_FILES[x['num']]}"
    if x["num"] == "53.1.1" and x["content"] is not None:   # the page shows its own source (owner, 2026-10-05 14:21)
        x["content_source"] = "the source of this page, as published: vision/explorer/file-tree-explorer.html"
    if x["num"] == "53.1.2":   # the data cannot hold itself: the page shows the data file it loaded (owner, 2026-10-05 14:21)
        x["content_self"] = True
        x["content_source"] = "this page's data file, exactly as the page loaded it"
        x["readonly"] = "Built by ide-build from the tree notes, the drafts and the How it works files. It is rebuilt every round, never edited by hand."
    if x["num"] in CLAUDE_DRAFTS:   # planning copies of the .claude folder (D-034)
        f = os.path.join(os.path.dirname(DOCS_DIR.rstrip("/")), CLAUDE_DRAFTS[x["num"]])
        if os.path.isfile(f):
            x["content"] = open(f, encoding="utf-8").read()
            x["content_source"] = f"draft in the project folder: vision/{CLAUDE_DRAFTS[x['num']]}"
            x["src_file"] = f"vision/{CLAUDE_DRAFTS[x['num']]}"
            x["example"] = None
    if x["num"] in DOC_SKILLS:   # a doc's Example is the outline in its skill (owner, 2026-10-05)
        f = os.path.join(os.path.dirname(DOCS_DIR.rstrip("/")), DOC_SKILLS[x["num"]])
        if os.path.isfile(f):
            sk = open(f, encoding="utf-8").read()
            mo = re.search(r"^## Outline\n.*?^```markdown\n(.*?)^```", sk, re.S | re.M)
            if mo:
                x["example"] = {"kind": "outline", "lang": "markdown", "skill": os.path.basename(os.path.dirname(f)),
                                "title": "Structure of the file", "body": mo.group(1).rstrip()}
    del x["notes"]

# a folder that holds anything that exists in the repo exists too
_by_id = {x["id"]: x for x in out_nodes}
for x in out_nodes:
    if x.get("exists"):
        p = _by_id.get(x["parent"])
        while p is not None and not p.get("exists"):
            p["exists"] = True
            p = _by_id.get(p["parent"])

# ---- owner edits applied from the explorer (tools/overrides.json, keyed by [n]); they win over the parsed doc
ov_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "overrides.json")
if os.path.exists(ov_path):
    OV = json.load(open(ov_path))
    for x in out_nodes:
        for k, v in OV.get(x["num"] or "", {}).items():
            if not k.startswith("_"):
                x[k] = v

# ---- knowledge map + layered "How it works" summaries (D-033): tools/build_map.py
import build_map
KMAP, KENTRIES, _fd = build_map.build(out_nodes)
json.dump(KMAP, open(build_map.MAP_PATH, "w"), indent=1, ensure_ascii=False)
SUMS = build_map.IF.load_all(out_nodes)   # every node's {name}.index.md (owner, 2026-10-05)
for x in out_nodes:
    km = KMAP["nodes"][x["id"]]
    s = SUMS.get(x["id"])
    x["how"] = {"text": s["text"], "keep": s.get("keep") or [], "sections": s.get("sections") or [], "at": s.get("at"), "by": s.get("by"), "state": km["summary_state"]} if s and s.get("text") else None
    x["how_md"] = s["body"].strip() + "\n" if s and s.get("body", "").strip() else None
    x["how_file"] = build_map.IF.index_file(x)
    # the metadata file next to it (owner, 2026-10-07, D-057): empty for now; the page shows it in Details
    x["fam"] = os.path.basename(build_map.IF.index_path(x))[:-len(".index.md")]
    x["meta_file"] = build_map.IF.meta_file(x)
    try:
        x["meta"] = json.load(open(build_map.IF.meta_path(x), encoding="utf-8"))
    except (OSError, ValueError):
        x["meta"] = None
    x["knowledge"] = {"direct": km["direct"], "inherited": km["inherited"]}
def _clip(t, n=3500):
    return t if len(t) <= n else t[:n].rsplit("\n", 1)[0] + "\n\n…(continues in the doc)"
KNOWLEDGE = {eid: {"doc": e["doc"], "heading": e["heading"], "status": e["status"], "sources": e["sources"],
                   "applies": e["applies_raw"], "nodes": e["nodes"], "text": _clip(e["text"])} for eid, e in KENTRIES.items()}
INPUTS = {k: {"at": v.get("at"), "where": v.get("where"), "summary": v.get("summary"), "file": v.get("file")} for k, v in KMAP["inputs"].items()}
print("knowledge:", len(KNOWLEDGE), "entries;", sum(1 for x in out_nodes if x["how"]), "summaries;", len(KMAP["problems"]), "map problems")

# ---- the real file tree (owner, 2026-10-09, D-061): every real file and folder under a folder that exists in the
# repository is listed, even when the tree notes do not name it. Such items carry "scanned": true; they get no How it
# works file of their own (their folder's describes them). Only git's own files and the keys folder are left out
# (owner, 2026-10-09 14:59: "we always should have real represention of file tree on a disk and on ui").
SCAN_SKIP = {".git", "__pycache__", "node_modules", ".secrets", ".DS_Store"}
REAL_FILES = {}   # id -> text of a scanned file; written to real-files.json, which the page loads when one is opened
def _scan(parent):
    rel = parent["path"][len("agent-os/"):]
    d = os.path.join(REPO, rel)
    if not os.path.isdir(d):
        return
    have = {c["path"] for c in out_nodes if c.get("parent") == parent["id"]}
    for name in sorted(os.listdir(d)):
        if name in SCAN_SKIP:
            continue
        full = os.path.join(d, name)
        isdir = os.path.isdir(full)
        path = parent["path"] + name + ("/" if isdir else "")
        if path in have:
            continue
        x = {k: None for k in out_nodes[0]}
        x.update({"id": "r-" + re.sub(r"[^A-Za-z0-9._-]+", "-", path[len("agent-os/"):].rstrip("/")), "num": None, "name": name + ("/" if isdir else ""),
                  "path": path, "type": "folder" if isdir else "file", "link": False, "placeholder": False, "parent": parent["id"],
                  "children": [], "status": "decided", "exists": True, "scanned": True, "details": [], "open_questions": [], "rules": [],
                  "concepts": [], "decisions": ["D-061"], "features": [], "custom_tabs": [], "qa": [], "fields": [],
                  "summary": "Found in the repository; the folder's How it works describes it.", "knowledge": {"direct": [], "inherited": []}})
        if not isdir:
            x["content_source"] = f"repo andyvauliln/trading-oss: {path[len('agent-os/'):]}"
            x["src_file"] = path[len("agent-os/"):]
            if os.path.getsize(full) > 200000:
                x["content"] = None; x["content_source"] += " (too large for the page; open it in the repository)"
            else:
                try:
                    REAL_FILES[x["id"]] = open(full, encoding="utf-8").read()
                    x["content"] = None; x["content_lazy"] = True
                except (UnicodeDecodeError, OSError):
                    x["content"] = None; x["content_source"] += " (not a text file)"
        out_nodes.append(x)
        parent.setdefault("children", []).append(x["id"])
        if isdir:
            _scan(x)
for _x in list(out_nodes):
    if _x["type"] == "folder" and _x.get("exists") and not _x.get("scanned") and not _x.get("link") and "[" not in _x["path"] \
            and _x["path"].startswith("agent-os/"):
        _scan(_x)
json.dump(REAL_FILES, open(os.path.join(os.path.dirname(os.path.abspath(OUT)), "real-files.json"), "w"), ensure_ascii=False)
print("real files listed:", sum(1 for x in out_nodes if x.get("scanned")))

retired = [{"nums": r["nums"], "heading": r["heading"],
            "text": " ".join(i["text"] for i in r["items"])} for r in P["retired"]]

data = {
 "schema_version": 1,
 "title": "Agent OS file tree",
 "source": {"doc": "vision/docs/file-tree.md", "doc_version": P["version"],
            "also": ["vision/docs/ (knowledge base)", "vision/docs/index/knowledge-map.json", "vision/tree/ (every node's {name}.index.md)"]},
 "generated": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
 "data_version": int(os.environ.get("DATA_VERSION", "3")),
 "sync": "Built by the ide-build scripts from the tree notes and the knowledge (apps/project-IDE/data/ and agents/system/docs/ in the repository; vision/docs/ while we plan) and every item's .index.md. The page saves straight away into its own store (collections inputs, nodes, changes); at a sync (\"sync the file tree\") the project IDE agent saves them word for word, writes edits into their files, hands the knowledge to the knowledge base agent and rebuilds this file.",
 "status_legend": {
   "decided": "agreed by the owner: the whole tree as it stood on 2026-10-05, and every decision since",
   "proposed": "Claude's proposal, waiting for owner confirmation",
   "placeholder": "a pattern such as [agent-name]; real names are filled in later",
   "example": "part of the fully expanded example agent",
 },
 "root": out_nodes[0]["id"],
 "concepts": [],
 "knowledge": KNOWLEDGE,
 "inputs": INPUTS,
 "docs": {k: v["title"] for k, v in KMAP["docs"].items()},
 "decisions": [{"id": k, "text": v} for k, v in P["decisions"].items()],
 "feature_areas": P["areas"],
 "retired": retired,
 "nodes": out_nodes,
}
json.dump(data, open(OUT, "w"), indent=1, ensure_ascii=False)
from collections import Counter
print(len(out_nodes), "nodes", Counter(x["status"] for x in out_nodes))
print("with example:", sum(1 for x in out_nodes if x["example"]), " files without example:",
      [x["path"][-60:] for x in out_nodes if x["type"] == "file" and not x["example"]])
