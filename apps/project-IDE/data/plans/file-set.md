# One file for every tab

What sits next to every file and folder, one file for each tab on the File Tree page. Status: building steps 1 and 2 (your go of 2026-10-07: clean names, and an empty metadata file for everything); the rest waits. Where its content goes once it is built is at the end.

## What it is for

With these files you can manage, analyse and view the system from the page, and every AI has all the context it needs to change something precisely. For any file it finds what the file is for, how it works, what depends on it, what must change with it and how, and what holds for it from every level above, so a change to one file reaches every related file, agent, skill, doc, index and piece of logic. Every question you ask lands in the docs, with an explanation of how exactly that thing works.

## Why vision.md has vision.md.index.md today

When How it works moved into its own files, we kept the whole file name, extension included, so that two files with the same name and different endings, such as `run.js` and `run.py`, could never share one How it works file. The tree has no such pair, so the extension only adds noise. Under the new rule the file is `vision.index.md`.

## The rule

Every tab is a file. A file's family shares its name without the last extension and sits next to it. A folder's family sits inside the folder and uses the folder's name.

For the file `vision.md`:

| Tab | File | Always there? | Written by | What it holds |
|---|---|---|---|---|
| How it works | `vision.index.md` | yes | the knowledge base agent; you can edit it on the page | the plain explanation under the fixed headings |
| File | `vision.md` | yes; until it is written the tab says so | whoever owns it | the file itself |
| Example | `vision.example.md` | only when useful | the knowledge base agent | a full example with every field explained, or a doc's outline |
| Questions | `vision.questions.md` | only when there are questions | agents add open questions; your answers on the page or in chat close them | open questions, and every question you asked about it with the answer and where the docs now explain it |
| Changes | `vision.changelog.json` | after its first real change | the agent that makes the change | every real change: which task made it, from which of your messages, what logic it changed and why |
| Tests | `vision.tests.json` | for every code file, skill, agent and subagent | the agent that writes or changes it | its tests: what each checks, how to run it, when it runs and the last result |
| Details | `vision.meta.json` | yes | the build and the knowledge base agent | the metadata and the mapping, described below |
| one tab per view | `vision.{type}.{name}.view.html` | only when a file needs one | the project IDE agent | a custom interface for the file, with its own logic |

A folder has the same family inside it: `configs/configs.index.md`, `configs/configs.questions.md`, `configs/configs.changelog.json`, `configs/configs.meta.json` and any views. Its Contents tab is the folder listing itself, so it needs no file, and folders have no Example.

Here is the system's `configs/` folder under the new rule:

```text
configs/
├── configs.index.md                 How it works of the folder
├── configs.meta.json                Details of the folder
├── system.workers.json              File
├── system.workers.index.md          How it works
├── system.workers.example.md        Example: a full jobs file with every field explained
├── system.workers.questions.md      Questions: which machine runs the local scheduler, ...
├── system.workers.changelog.json    Changes
├── system.workers.meta.json         Details
├── system.config.json
├── system.config.index.md
├── system.config.example.md
├── system.config.meta.json
└── ...
```

The Jobs tab of `system.workers.json` is the jobs view every jobs file shares (see Views), so the file needs no view of its own.

While we plan, these files sit in the planning copy of the tree, as the How it works files do now. After the GitHub sync they sit next to the real files.

## Naming rules

1. The family name is the file name without its last extension: `vision.md` gives `vision`, `system.workers.json` gives `system.workers`, `README.md` gives `README`. A name with no extension stays whole: `.env` gives `.env.index.md`, `.gitignore` gives `.gitignore.index.md`.
2. If two files in one folder would share a family name, such as `run.js` and `run.py`, both keep their extension: `run.js.index.md` and `run.py.index.md`. There is no such pair today.
3. The endings `.index.md`, `.example.md`, `.questions.md`, `.changelog.json`, `.tests.json`, `.meta.json` and `.view.html` (and `.schema.json`, if you keep it) are reserved. No ordinary file may end with them, and family files have no families of their own.
4. In the tree, family files fold into their file as tabs. The switch that shows the index files today will show the whole family.

## Views

A view is a custom interface for a file or folder, with its own logic: not just a table, but whatever that kind of file needs. Every skill, for example, gets the same skill view: what the skill is for, when it runs, which agents use it, its steps, the files it reads and writes, and its latest changes, with the parts you can change editable in place.

- **Its name.** `{type}` is the kind of thing the view is for: skill, jobs, links, variables, tests, agent, doc and so on. `{name}` is added only when there are two views of the same kind. A view for one file sits next to it, such as `system.workers.jobs.view.html`, and a second one would be `system.workers.jobs.by-schedule.view.html`. The tab takes its label from the view's own title.
- **Shared views, when useful.** When every file of a kind should look the same, the view is written once instead of next to each file, in the project IDE: `apps/project-IDE/views/skill.view.html` shows on every `SKILL.md`, and `jobs.view.html` on every `*.workers.json`. A short list beside them, `views.json`, says which files each kind covers. Shared views are a convenience, not a rule. A file can have its own view, and its own view wins over a shared one of the same kind and name.
- **What a view gets.** The page shows the view in a closed frame and hands it the file, its whole family (How it works, Questions, Changes, Details) and, to read only, the related files its Details list. Its logic can be anything the interface needs: filters, checks, totals, buttons. When you change something in a view, it hands the edit back, and the edit waits like any page edit until the sync. A view cannot reach the internet or any secret.
- **Today's custom tabs become shared views:** Jobs, Links, Variables, Tests, Model routes and Capabilities, and the agent folders' Overview and Agents. A new skill view comes with them.

## The metadata file (Details tab)

`vision.meta.json` holds everything about the file that is neither its content nor its explanation. The Details tab shows it in plain words, with the related files as links and the decisions by their titles, not their codes.

- **What it is for:** the one line shown under the title.
- **Kind:** file, folder, file link or folder link, and where a link points.
- **State:** written, not written yet, or a name pattern. For agents also whether it is decided, proposed or an idea; the page shows no statuses for now.
- **Handling:** kept in git or ignored; secret (values never shown, only names); generated, and by which script, so nobody edits it by hand.
- **Who writes it and who reads it:** people, agents and scripts.
- **When it changes:** what makes it change.
- **Mapping:** the related files and how each relates: reads, writes, links to, same format as, built from, documented in, checked by, tested by. Also where its knowledge comes from (the decisions, your messages and the notes it rests on) and the features it serves.
- **What must change with it:** for each related file, agent, skill, doc, index list or piece of logic, what to update and how when this file changes. An AI walks this list before it finishes any change.
- **Applies from above:** the knowledge from every level above that holds for this file, built by the script, so an AI working on a skill deep inside a strategy's helper knows the rules of its strategy, its domain and the system.
- **Views:** which views apply, its own and the shared ones.
- **How it works check:** what the How it works was written from, when, by whom, and when it was last confirmed. This moves out of the header of the `.index.md`, so that file becomes plain text you can read and edit.
- **Tree number:** today's number, for agents only, until paths alone are enough.

Example for `system.workers.json`:

```json
{
  "about": "The list of every job the system agent runs, on a schedule or on demand.",
  "kind": "file",
  "state": "not written yet",
  "status": "decided",
  "git": "tracked",
  "secret": false,
  "generated_by": null,
  "writers": ["the owner, on the page or the dashboard", "domain and self-improvement agents propose changes"],
  "readers": ["scheduler", "run-job", "the jobs index", "the page"],
  "changes_when": "a job is added, changed, rescheduled, paused or removed",
  "related": [
    {"path": "agents/trading/prediction-market/configs/prediction-market-agents.workers.json", "how": "same format as"},
    {"path": "agents/system/scripts/system/", "how": "read by (scheduler, run-job)"},
    {"path": "agents/system/docs/data-schemas.md", "how": "documented in"}
  ],
  "sources": {
    "decisions": ["D-029", "D-030", "D-033"],
    "inputs": ["in-20260930-0938"],
    "notes": ["schema-workers-file", "flow-scheduler"]
  },
  "update_with": [
    {"path": "agents/system/docs/data-schemas.md", "how": "a new or renamed job field goes into the jobs format"},
    {"path": "agents/system/scripts/system/", "how": "scheduler and run-job read every field; a new field needs their support"},
    {"path": "agents/system/docs/index/workers.md", "how": "a new or removed job is listed or retired there"}
  ],
  "inherits": ["arch-jobs", "conv-agent-config-files", "safe-live-gate"],
  "features": ["Data collection (workers)", "Subscriptions and triggers"],
  "views": ["jobs (shared view)"],
  "how_it_works": {"basis": "44733a45820b", "written": "2026-10-05T10:34:15Z", "by": "knowledge-base-agent", "confirmed": "2026-10-06T10:52:16Z"},
  "tree_number": "11.10"
}
```

## Changes, as JSON

`vision.changelog.json` lists every real change to the file, newest first. Each entry says which task made it, so you can later follow one task through every file it touched, or start from a file and see what changed it and why. The first entries come from the decision log and your saved messages.

```json
[
  {
    "change": "chg-20260930-0938-jobs-per-agent",
    "at": "2026-09-30T09:38:40Z",
    "task": {"kind": "thread", "title": "Interactive file tree UI"},
    "by": "knowledge-base-agent",
    "input": {"id": "in-20260930-0938", "quote": "so generally i want that every agent has config with scheduling, so there i can see, change schedule, turn off ..."},
    "decision": "D-029",
    "description": "Every agent got a jobs file in this format, and the scheduler finds them all.",
    "logic_changed": [
      "Jobs are kept per agent instead of in one system list.",
      "The scheduler finds every jobs file by looking through all agents' configs folders."
    ],
    "parts_changed": ["the whole file: a new format"],
    "other_files": ["agents/trading/prediction-market/configs/prediction-market-agents.workers.json"],
    "commit": null
  }
]
```

- **change:** one name for the whole change, the same in every file it touched, so the page can step from one of those files to the next.
- **task:** what made the change: a thread, a request from the page, a job run, or a Claude Code session on your server, with a link back.
- **by:** the agent or person who made it.
- **input:** your message behind it, by its record and in your words. It is empty when no message asked for the change, such as a job run or an automatic fix.
- **decision:** the decision it carries out, if there is one.
- **description:** what changed, in one plain sentence.
- **logic_changed:** how the behaviour changed, in plain sentences.
- **parts_changed:** the sections, fields or jobs that changed.
- **other_files:** the other files the same change touched.
- **commit:** the git commit, once the repository is in use.

The Changes tab shows the entries as a timeline, and from any entry it opens the other files of the same change.

## Tests

Every code file, skill, agent and subagent has a Tests file, `x.tests.json`, shown in a Tests tab. Docs and settings files have none for now.

```json
{
  "schema_version": 1,
  "tests": [
    {
      "id": "t-relink-001",
      "checks": "refuses to make a link into .secrets/",
      "kind": "script",
      "run": "node agents/system/tests/scripts/t-relink-001.test.js",
      "params": {"agent": "pm-strategy-1.momentum-v1.opus55-test"},
      "expect": "exits with an error and makes no link",
      "when": "on_change",
      "last": {"result": "never", "at": null, "log": null}
    }
  ]
}
```

- **kind:** `script` for code; `agent` or `skill` for a run in test mode with a prompt, where `run` holds the prompt instead of a command.
- **run** and **params:** how to start it, so the same test can run with other inputs.
- **expect:** what a pass looks like, in plain words.
- **when:** by hand, when the file changes, before a variant is promoted, or on an interval.
- **last:** the latest result, its time and the log, written by the test runner.

The test code itself stays where tests live today, in the level's `tests/` folder, one test per file; the Tests file points to it. The level's test list is built from the Tests files of everything at that level (my default).

The Tests tab has its own view: every test with what it checks, when it runs and its last result, a Run button for one test and one for all, and the result and log opening in place. On your server, Run starts the test at once and shows the result as it comes. On claude.ai the page cannot run code, so Run sends the run to Claude as a request.

## One job per code file

Every code file holds one runnable thing, such as one function, one endpoint, one script or one worker, with one purpose. It may take parameters, but it never mixes several jobs. Related things are grouped in a folder, one per file, each with its own How it works and metadata. A shared helper is no exception: it is one function in its own file.

Our own build scripts break this today. For example, the script that builds the knowledge map also lists stale How it works files, prints a file's context, confirms texts and writes new ones. Under the rule it becomes a folder:

```text
build-map/
├── build-map.index.md        How it works of the folder
├── build.py                  builds the knowledge map
├── stale.py                  lists stale How it works files
├── context.py                prints a file's whole context
├── confirm.py                keeps a How it works text that is still right
├── set.py                    writes new How it works texts
└── read-tags.py              reads the knowledge tags, used by the others
```

Each of these files has its own family (How it works, Details, Tests and the rest), left out above.

## The format file, beside the example or not

You asked whether `.schema.json` is already covered by the examples. Partly. The Example is for reading: a filled-in file with every field explained. A schema is for checking: the exact rules (which fields must be there, their types and the allowed values) that a script tests before it runs, and that a view uses for its dropdowns and checks. Today those rules are hidden in the page's own code, such as the allowed values in the Jobs table, and in the notes on data formats, where no script can use them.

My suggestion: keep a schema only for config and data files, as the one place for those rules, and build the field explanations in the Example from it, so the two never disagree. Without it, the Example carries the field notes and nothing checks a file automatically.

I don't suggest a notes file, because what you leave on the page goes into your inputs and ends up in How it works, Questions or Changes. I don't suggest a tests file per file either, because tests have their own config.

## Where the details live then

Today most of what these files would hold sits in one long notes file about the tree, with a section per file. My default: the family files become the one place for each file's details, and that long file becomes an overview built from them, so nothing is written twice.

## The work, once you say go

1. Rename the How it works files of the 195 files (`vision.md.index.md` becomes `vision.index.md`; the 161 folders already have the right name), and move their headers into the metadata files.
2. Write a metadata file for all 356 files and folders from what we know now.
3. Move the 207 examples and 71 open questions into `.example.md` and `.questions.md` files.
4. Start a changes file for every file a decision touched, from the decision log and your saved messages, and make every agent that changes a file add its entry from then on.
5. Turn the eight custom tabs into shared views, add the skill view and the tests view, and make the page build its tabs from the family files. First check that a view can run inside the page on claude.ai and on your server.
6. Write a Tests file for every code file, skill, agent and subagent, from the tests already planned.
7. Split our build scripts and the server code into one job per file.
8. Rebuild the tree overview from the family files.
9. Update the rules to match: the How it works skill, the knowledge base agent, the project IDE agent with its build and sync skills, the tools and the page.
10. Rebuild, check every tab on phone and desktop, and publish.

## Where this goes once it is built

This file is a plan. It sits with the other plans in the planning notes, which hold proposals waiting for your go, and the docs mention it only as a proposal. Once it is built, its content moves into the knowledge the usual way, one fact in one place, and this file goes to the archive:

- **The mechanism in full** (the files of a family, the naming rules, views, Details, Changes, Tests and the format files) becomes a note of its own next to the other notes agents read, because every file in the project follows it. Its name, `file-family.md`, is my proposal.
- **The short rules** (the reserved endings, one job per code file) go into the conventions note with the other naming rules.
- **The steps agents follow** go into the skills that do the work: the How it works skill, and the IDE's build and sync skills.
- **The README** describes it in a short paragraph in its project IDE part and gives the path to that note.
- **The vision** says it in a sentence: every file explains itself to you and to every AI.
- **The rebuild prompt** carries every exact format, because an AI must rebuild it from there.

The same rule holds for any mechanism this big: the detail lives in its own note or skill, the README gives a short view with the path, and the vision keeps only the idea.

## Log

- 2026-10-07 09:04: your go for the clean names and empty metadata files; steps 1 and 2 are built under `2026-10-07-0904-agent-os.md`.
