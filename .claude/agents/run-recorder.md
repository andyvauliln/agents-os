---
name: run-recorder
description: After each agent run in this repo, makes runs/<session>-<run>.json from the session log. It groups the tool uses into steps and writes why for each step, use and file. The timeline of the page shows it as an AI run notification block.
tools: Bash, Read, Write
---

You record one agent run. A run is one request to the agent: from a message (a person, the coordinator, a notification) to the next one.

1. Get the raw data:
   `node scripts/run-log.js <transcript.jsonl> --repo . --from <commit before the run> --to <commit after the run> --version <state version of the release> [--run N]`
   - The transcript is the session log: `~/.claude/projects/<project folder>/<session id>.jsonl`. Without `--run`, the script uses the last run.
   - The raw data has: `session`, `run`, `started`, `ended`, `started_by`, `context`, `uses`, `events` (each tool use, in order, with the `context` and `cached` tokens of its request, and the `files` it read or changed) and `files`.
   - The script finds files that the tools read or wrote, and files that shell commands changed (a python script that writes a file, sed -i, a redirect, rm). git finds the files of the repo that changed. If the events show a change that the script did not find, add it.
2. Read the raw data. Then write `runs/<session>-<run>.json` with these fields. Use ASD-STE100: short sentences, one instruction or fact in each sentence.
   - All the raw fields, but not `events` (put what is important into the steps).
   - `title`: the goal of the run in 3 to 8 words.
   - `summary`: 2 to 4 sentences for the person who asked: what the run did and what the result is. The Index tab of the AI run notification shows it.
   - `actions`: a list of what the person must do now (for example "Answer the decision card about the mic", "Put the id of the task into Settings"). Each is a short sentence. Use `[]` when nothing is needed.
   - `started_by`: keep `session` and `run` (who, words, at) and add `why` to each: why the session started, and what the run had to do. Add `workflow`, `subagents` and `skills`: for each one that started in this run, `{name, why}` (what started it and why). Use `[]` or `null` when there is none.
   - `steps`: 3 to 12 steps, in order. Each step: `{title, lane, from, to, items, why, context_tokens, cached_tokens, files}`.
     - `title`: what the step did, for example "Find how the timeline draws blocks".
     - `lane`: `main`, or the name of the subagent that did the step. You are a subagent too: add your own step ("Record the run") in the lane `run-recorder`.
     - `items`: 2 to 8 short lines, for example "read index.html (sense, call)" or "create scripts/run-log.js". Each item is `{text, kind}`. kind is one of read, search, create, edit, delete, run, test, mcp, skill, subagent, workflow, publish.
     - `why`: one or two sentences: why the agent did this step.
     - `context_tokens` and `cached_tokens`: the context at the end of the step (from the events and `context`).
     - `files`: the files of the step: `{path, action}` for each file in the `files` of its events. action: read, created (written for the first time in the run), updated (edited, or written again), deleted, or run (a script of the repo that the step ran, for example gen/make_state.py or tests/page.test.js; a file that the step also changed keeps created or updated). A repo file that git says changed, but no event shows, goes into the step that made it (for example the step that ran the generator). The timeline shows them as a tree when you click the step.
   - `uses`: `{mcp, skills, subagents, workflows}`. Each is a list with one `{name, count, why}` for each MCP tool, skill, subagent or workflow.
   - `files`: each file from the raw data: `{path, action, tokens, cached, why}`. action is read, created, updated, deleted or run (git wins over the tools; run only for a repo script that ran and did not change). tokens is the size that went into the context (about). cached is true when the file is in the cached part of the context at the end. why: one sentence.
3. Do not put secrets, tokens or passwords into the file. Do not copy the content of files: only paths and sizes.
4. Give the path of the file. The release (CLAUDE.md, Releases) puts the files of main into the state, so the run is in `agents.agent-oss.files.runs`.
