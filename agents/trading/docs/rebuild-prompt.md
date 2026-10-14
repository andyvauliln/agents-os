# Rebuild trading: `agents/trading/`

## Your task

You are an AI coding agent, such as Claude Code, working in the Agent OS repository. The system is already built from its own prompt, `agents/system/docs/rebuild-prompt.md`: the top of the tree, `agents/system/`, `.secrets/`, the shared scripts, the skills and the project IDE in `apps/project-IDE/`. Your job is to build `agents/trading/` and its docs, and nothing else.

You build:

1. the folder `agents/trading/` with its How it works and Details files;
2. trading's docs in `agents/trading/docs/`: `vision.md`, `README.md`, `README.asd.md`, `rebuild-prompt.md` (this file), each with its metadata files;
3. the research folder `agents/trading/researches/`, restored as it is;
4. the prediction-market domain `agents/trading/prediction-market/` as empty folders, with the trading notes in its `docs/`.

"The same" means: the acceptance checks at the end all pass.

You never:

- write a key value anywhere, open or read a `.env` file, or put a key in a doc, a setting or a log; key names only;
- create a trading account, a funded account or anything that can place a live order;
- write files inside `agents/trading/prediction-market/` other than `.gitkeep`, or give it agents, settings, scripts or docs: the domain is built in stage two from its own prompt;
- push, merge or publish without the owner's go.

Work in the build order below. Run each step's check before the next step. When this prompt says a point is open, leave what "Do not build" says in its place and ask the owner if you need it.

## Trading in brief

Trading is the first kind of work the Agent OS does, and everything about it lives below `agents/trading/`, so the system level stays general and knows nothing about money, accounts, markets or orders. `agents/trading/` is a folder of trading domains, not an agent: it has no AI instructions, settings, scripts or jobs of its own. It holds trading's own docs, the research studies the trading domains start from, and the trading domains.

A trading domain is one area of trading, such as prediction markets. It is a full domain of the Agent OS: a direct child of the system agent, reached through the system's `subagents.link/` folders. It arranges its agents in three levels, each with the standard agent folder: the domain agent; strategy agents, one per way to make money; and trading agents, also called variants, the versions of a strategy that trade, each with one set of changes, one AI model and one mode.

Every trading agent starts in test mode. Only the owner gives an agent an account with real money, and every new strategy configuration starts only after the owner reads a report on it and approves it. A change to a running agent makes a new test version with a new name. Orders are placed only on blockchains for now; centralised exchanges and other apps are sources of information only. Every order is logged.

The first trading domain is prediction markets on Polymarket, in `agents/trading/prediction-market/`. In stage one, the current stage, it is its empty folders plus its `docs/`, which holds the trading notes; its other earlier files are kept in `vision/archive/2026-10-12/prediction-market/`. A later trading domain, such as copy trading, is a copy of it, made with `create-agent` when the owner asks.

## Ground rules

- **Safety.** No secret value anywhere. Keys are named in `.secrets/secrets.index.json` and their values live only in the git-ignored `.secrets/test/.env` and `.secrets/live/.env`, which you never open. Nothing you build can act outside the repository.
- **Formats.** Docs are Markdown. Settings and Details files are JSON, two-space indent, UTF-8, ending in a newline. No scripts are built at this level.
- **Names.** Folder and file names are lowercase with `-`, except the doc names `README.md`, `README.asd.md` and the research folders, which keep their names exactly as given, including `researches/` and `trding-agents-arhiteches/`.
- **Metadata next to every item.** Every file and folder you create has a How it works file (`[family].index.md`) and a Details file (`[family].meta.json`) next to it. The family is the file name without its last extension: `vision.md` gives `vision`, `README.asd.md` gives `README.asd`. A folder's metadata files sit inside it with the folder's name: `docs/docs.index.md`. Metadata files have no metadata of their own.
- **Example and Questions files.** Only the four docs in `agents/trading/docs/` also get `[family].example.md` (the doc's outline) and `[family].questions.md` (open questions for the owner about the doc).
- **Empty folders.** An empty folder holds one `.gitkeep`, so git keeps it. Remove the `.gitkeep` once the folder holds a real file.
- **Git.** Everything here is tracked. Nothing here is git-ignored.
- **Docs for people.** `vision.md`, `README.md` and `README.asd.md` contain no decision codes, input ids, `[n]` reference numbers or history. The owner is "the owner", and "they" as a pronoun.

## The repository tree

```text
agents/trading/
├── trading.index.md                         How it works of the folder
├── trading.meta.json                        Details of the folder
├── docs/                                    trading's own docs
│   ├── docs.index.md
│   ├── docs.meta.json
│   ├── vision.md                            why trading, what every trading domain shares, how a new one is made
│   ├── vision.index.md
│   ├── vision.meta.json
│   ├── vision.example.md                    the outline of vision.md
│   ├── vision.questions.md                  open questions about vision.md
│   ├── README.md                            every part of trading exactly, with each part's docs path
│   ├── README.index.md
│   ├── README.meta.json
│   ├── README.example.md
│   ├── README.questions.md
│   ├── README.asd.md                        README.md again in ASD-STE100
│   ├── README.asd.index.md
│   ├── README.asd.meta.json
│   ├── README.asd.example.md
│   ├── README.asd.questions.md
│   ├── rebuild-prompt.md                    this file
│   ├── rebuild-prompt.index.md
│   ├── rebuild-prompt.meta.json
│   ├── rebuild-prompt.example.md
│   └── rebuild-prompt.questions.md
├── researches/                              the research studies, restored as they are
│   ├── researches.index.md
│   ├── researches.meta.json
│   ├── prediction-market-research/          42 studies 01-34 and 50-57, _evidence/, _pipeline/
│   ├── self-improving-agents/               one study: 01-approaches-and-architectures.md
│   └── trding-agents-arhiteches/            README.md, index.html, specs/, diagrams/
└── prediction-market/                       the first trading domain: empty folders and the notes in docs/ (stage two)
    ├── .claude/
    │   ├── agent-memory/[subagent-name]/
    │   ├── agent-memory-local/
    │   ├── agents/
    │   ├── commands/
    │   ├── output-styles/
    │   ├── rules/
    │   ├── skills/[skill-name]/
    │   └── workflows/
    ├── configs/subagents.link/[agent-name]/
    ├── scripts/
    │   ├── decisions/
    │   └── subagents.link/[agent-name]/
    ├── logs/
    │   ├── jobs/[job-id]/
    │   ├── services/[service]/
    │   └── subagents.link/[agent-name]/
    ├── data/
    │   ├── markets-catalog/
    │   ├── polymarket-prices/
    │   └── subagents.link/[agent-name]/
    ├── docs/
    │   ├── common/
    │   ├── how-to/
    │   ├── index/
    │   └── subagents.link/[agent-name]/
    ├── tests/
    │   ├── agents/
    │   ├── scripts/
    │   └── subagents.link/[agent-name]/
    ├── research/
    │   ├── [research-id]-[slug]/
    │   └── subagents.link/[agent-name]/
    └── strategy-1-agent/                    one strategy: the same folders as the domain, without the domain's extra subfolders
        ├── .claude/ (the same eight folders)
        ├── configs/subagents.link/[agent-name]/
        ├── scripts/subagents.link/[agent-name]/
        ├── logs/subagents.link/[agent-name]/
        ├── data/subagents.link/[agent-name]/
        ├── docs/subagents.link/[agent-name]/
        ├── tests/{agents,scripts,subagents.link/[agent-name]}/
        ├── research/{[research-id]-[slug],subagents.link/[agent-name]}/
        └── pm-strategy-1.momentum-v1.opus55-test/   example trading agent; "momentum" is a placeholder
            ├── .claude/ (the same eight folders)
            ├── configs/
            ├── scripts/
            ├── logs/
            ├── data/get-polymarket-data/
            ├── docs/
            ├── tests/{agents,scripts}/
            └── research/[research-id]-[slug]/
```

Names in `[brackets]` are placeholders, created literally as folders with those names. In `prediction-market/` every leaf folder holds only a `.gitkeep`; there are 60 of them. The trading agent has no `subagents.link/`, because it has no children.

## Conventions

- **Trading agent names** (decided rule, proposed format): `[strategy-id].[own-name]-v[N].[platform-model]-[test|live]`, lowercase `a-z`, `0-9`, `-` and `.`, at most 64 characters. `[strategy-id]` is the strategy agent's ID without `-agent` and its suffixes. Example: `pm-strategy-1.momentum-v1.opus55-test`. A trading agent's folder is named after it.
- **Strategy agent IDs** (default, the owner may change it): `[domain-code]-[strategy]-agent.[platform-model]-[test|live]`, for example `pm-strategy-1-agent.opus55-test`. The strategy folder keeps its plain name, `strategy-1-agent/`; the ID lives in the strategy's settings.
- **New versions.** A changed setting, instruction or script makes a new trading agent and raises `v[N]`; a different model changes `[platform-model]`. Names are never changed or reused.
- **Decision scripts** (default): a trading domain adds the script kind `decision` to the system's `worker` and `system`: `[name].decision.[ext]`, shared ones in the domain's `scripts/decisions/`.
- **Trading notes** (default): a trading domain's notes take a `trading-` prefix, so a trading agent's links to the system's notes and to its domain's never share a name.
- **Child links.** In every level with children, each content folder holds `subagents.link/[child-name]/`, a folder link to the child's folder of the same kind. The system's own `subagents.link/` folders point straight at `agents/trading/prediction-market/`; `agents/trading/` adds no level of agents. The `relink` script builds these links in stage two; in stage one the `[agent-name]/` placeholder folders stand in for them.

### How it works file

Front matter, then the six headings, in this order, each with one to four plain sentences or a short list, then up to four "Keep in mind" lines:

```markdown
---
about: agent-os/agents/trading/docs/vision.md
node: n-56.1.2
written: 2026-10-12T00:00:00Z
by: knowledge-base-agent
---
# vision.md

## What it is
## Who looks after it
## When and how it changes
## Who uses it, and when
## Where it is mentioned
## Related knowledge

## Keep in mind

- When you ..., ...
```

The folder's own file may use one `## Summary` instead of the six headings.

### Details file

Every `.meta.json` has exactly these keys:

```json
{
  "schema_version": 1,
  "about": "Trading's vision: why trading has its own place and what every trading domain shares.",
  "kind": "file",
  "state": "written",
  "status": "decided",
  "git": "tracked",
  "secret": false,
  "generated_by": null,
  "writers": ["knowledge-base-agent with the vision-doc skill", "the owner, on the File Tree page"],
  "readers": ["the owner", "every trading domain agent"],
  "changes_when": "an input changes what every trading domain shares",
  "related": [{"path": "agents/trading/docs/README.md", "how": "same words in In short"}],
  "sources": {"decisions": ["D-059"], "inputs": ["in-20261012-stage1"], "notes": []},
  "update_with": [{"path": "agents/trading/docs/README.md", "how": "bring In short in line"}],
  "inherits": [],
  "features": [],
  "views": [],
  "how_it_works": {"written": "2026-10-12T00:00:00Z", "by": "knowledge-base-agent"},
  "tree_number": "56.1.2"
}
```

`kind` is `file` or `folder`; `state` is `written`, `not written yet` or `name pattern`; `status` is `decided`, `proposed` or `idea`; `git` is `tracked` or `ignored`.

## The parts

### The trading folder

Create `agents/trading/` with `trading.index.md` and `trading.meta.json`. Its How it works says: a folder of trading domains, not an agent; it holds `docs/`, `researches/` and `prediction-market/`; nothing about money goes above it; a new trading domain is a copy of the prediction-market domain made with `create-agent`. Do not create `.claude/`, `configs/`, `scripts/` or any other agent folder here.

Check: `ls -A agents/trading` shows exactly `docs`, `prediction-market`, `researches`, `trading.index.md`, `trading.meta.json`.

### Trading's docs

Create `agents/trading/docs/` with `docs.index.md` and `docs.meta.json`, then write the four docs in this order, each with the skill named. Read the skill first; its outline is the doc's outline.

1. `vision.md` with `vision-doc`, at the domain length (800 to 1,500 words, a little more is acceptable): in short; why trading has its own place; the concept; how trading should work; what every trading domain shares; how a new trading domain is made; examples; what the owner sees and does; where it stands and what comes next; principles; ideas we are still weighing; open questions; going deeper (the README's path only). No folder or file names outside "Going deeper".
2. `README.md` with `readme-doc`, 1,500 to 3,000 words: in short (the vision's words, then the status, then what the document is, with the vision's path); trading at a glance (a table of the parts and how they connect); how trading is laid out (the folder tree and the standard agent folder); the parts (trading's docs, research studies, the trading domains, what every trading domain holds, names, accounts and keys, test and live, metrics, making a new trading domain, the trading dashboard), each ending "Its docs: `path`"; where each part's docs are; still open in the design.
3. `README.asd.md` with `readme-asd-doc` (or, until that skill exists, the ASD-STE100 rules below): the same content and the same headings as `README.md`, rewritten in ASD-STE100 Simplified Technical English. First line: it is the ASD-STE100 version of `README.md`, and `README.md` is the source. Rules: one topic per sentence; descriptive sentences at most 25 words, procedural sentences at most 20 words; active voice; present tense; simple approved words; no idioms; one word for one meaning, with the names in `README.md` exactly; numbered steps for procedures; at most six sentences in a paragraph.
4. `rebuild-prompt.md` with `rebuild-prompt-doc`: this file.

For each doc write `[family].index.md`, `[family].meta.json`, `[family].example.md` (the headings of the doc, each with one line on what goes under it) and `[family].questions.md` (each open question with a line on why it matters, or "None open.").

The docs say only what every trading domain shares. A single domain's detail belongs in that domain's own docs.

Check: the four docs exist and are not empty; the headings of `README.md` and `README.asd.md` are the same apart from the title; `vision.md` contains no backticked path outside its last section; no doc contains `D-0`, `in-20` or a `[n]` reference number; every "Its docs:" path in `README.md` exists.

### The research studies

`agents/trading/researches/` holds research output, not something you write. Restore it exactly from the repository's history (`git checkout <commit> -- agents/trading/researches`), with every file and its metadata files. It contains:

- `prediction-market-research/`: 42 study files `01-…md` to `34-…md` and `50-…md` to `57-…md`; `_evidence/` with `E1` to `E9`, `S0-index.md`, `S0-strategy-list-established.json`, `S0-strategy-list-speculative.json`, `S1-discovery-candidates.json`, `strategies/` and `rows/` (one JSON per study); `_pipeline/` with the pipeline that wrote them.
- `self-improving-agents/`: `01-approaches-and-architectures.md`.
- `trding-agents-arhiteches/`: `README.md`, `index.html`, `specs/` (29 architecture specs) and `diagrams/`.

Never edit a study's content. If the history is not available, ask the owner; do not write studies yourself.

Check: `ls agents/trading/researches/prediction-market-research/[0-9]*.md | grep -v index | wc -l` prints `42`.

### The prediction-market domain (stage one: folders and the trading notes)

Create every folder under `agents/trading/prediction-market/` exactly as in the tree, and put one `.gitkeep` in each empty leaf folder. Copy the trading notes into its `docs/` as they are, each with its metadata files: the ten `trading-*.md` notes, `doc-outlines.md`, `trading-vision-notes.md`, `README-trading-parts.md`, `rebuild-prompt-trading-parts.md`, `common/` (three files), `how-to/` (four guides) and `index/accounts.md`. Create nothing else there: no settings or scripts. The domain is built in stage two from its own prompt, `agents/trading/prediction-market/docs/rebuild-prompt.md`, written from `vision/archive/2026-10-12/prediction-market/` and the notes in its `docs/`. Its folder names stay as they are until the owner decides otherwise.

Check: `find agents/trading/prediction-market -type f ! -name .gitkeep` prints nothing, and `find agents/trading/prediction-market -name .gitkeep | wc -l` prints `60`.

### What a trading domain will hold (stage two, for reference)

Do not build these now. They are listed so the docs you write describe them correctly:

- one trading settings file in the domain's `configs/` (in the prediction-market domain `prediction-market-agents.config.json`): risk limits for the domain, per agent and per venue; trading accounts with id, venue, mode, `funded`, `approved_by_owner`, assigned agent, maximum capital and key names; venues, fees, market filters, the currency, the order stop switch and trade alerts;
- the shared decision scripts in `scripts/decisions/`, which read the mode, the limits and both stop switches before every order;
- the order logs in `logs/services/[service]/`;
- the `trading-` notes, `common/`, `how-to/`, `index/` (the list of accounts) and `doc-outlines.md` in `docs/`;
- the domain's dashboard, planned in `apps/trading-ui/`, which stays empty.

## Build order

1. Confirm the system is built: `agents/system/docs/rebuild-prompt.md` and `agents/system/scripts/system/` exist. The `create-agent`, `relink` and `load-secret` scripts in that folder are needed only from stage two, when the domain gets agents, links and keys. Check: the file and the folder exist.
2. Create `agents/trading/` with its metadata files. Check: the folder check above.
3. Restore `agents/trading/researches/`. Check: 42 studies.
4. Create the prediction-market folders with their `.gitkeep` files. Check: 60 `.gitkeep`, no other file.
5. Create `agents/trading/docs/` with its metadata files. Check: both files parse or have front matter.
6. Write `vision.md`, then `README.md`, then `README.asd.md`, then `rebuild-prompt.md`. Check: the docs check above.
7. Write every doc's How it works, Details, Example and Questions files, then the folder's. Check: the metadata check below.
8. Run the project IDE build (the `ide-build` skill). Check: the page's tree and `git ls-files` list the same paths under `agents/trading/`.

The prediction-market domain's own prompt runs later, in stage two. Later trading domains each have their own prompt, made when the owner asks for the domain.

## Acceptance checks

- The tree under `agents/trading/` matches the tree above, path for path.
- Every `.meta.json` parses as JSON and has exactly the keys of the Details file.
- Every file and folder you created has its `.index.md` and `.meta.json`; the four docs also have `.example.md` and `.questions.md`.
- `agents/trading/prediction-market/` holds only `.gitkeep` files.
- `agents/trading/researches/` is the same as in the repository's history, byte for byte.
- No file under `agents/trading/` contains a key value, and nothing here reads a `.env` file.
- Nothing under `agents/trading/` can place an order or act outside the repository.
- The four docs agree with each other and with the system's docs; the `README.md` In short uses the vision's words.
- The project IDE builds, and its tree equals the files on disk.

## Do not build

- **Trading's own agent, settings, scripts or jobs** in `agents/trading/`: leave nothing; shared trading parts stay in a domain until two domains need them.
- **The prediction-market domain's files:** leave its empty folders and its notes as they are; stage two.
- **A second trading domain such as `agents/trading/copytrading/`:** leave nothing until the owner asks.
- **Renamed folders such as `strategy-1/strategy-1.v1.Claude-Opus5.5/`:** keep today's names until the owner decides.
- **The order stop switch's handling of open positions, live capital limits, success metrics, the trade-alert channel:** leave nothing; they are open.
- **An order executor and a ledger of positions:** ideas still weighed; leave nothing.
- **`apps/trading-ui/`:** leave it empty with its metadata files.
