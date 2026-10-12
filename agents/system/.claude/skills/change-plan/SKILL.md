---
name: change-plan
description: Plan every change request before building it - write the plan, show it to the owner, build it step by step, then move each piece of its knowledge into the file that owns it and archive the plan. Use it for every request that changes the system, its structure, its code or its docs, from the owner, from the File Tree page or from an agent's own improvement.
---

# Change plan

The main way the system is developed. A change goes from a request to a plan, from the plan to the build, and from the build into the knowledge, where the next AI finds it. The plan is the working document of one change; once the change is built, the plan is history and the knowledge lives in the files it belongs to.

## When

- Every change request: an owner message that asks for a change, a request sent from the File Tree page, an improvement an agent wants to make to the system.
- Not for a question the docs can answer (that goes through `knowledge-intake` only), and not for a small fix that changes no behaviour: a typo, a broken link, a rebuild of the page.
- A request that grows while you work: the new part gets its own plan.

## Where plans live

- One file per request in `apps/project-IDE/data/plans/` (while we plan: `vision/plans/`), named after the request's time and subject: `YYYY-MM-DD-HHMM-<subject>.md`. Plans written before this skill keep their names.
- `plans/index.json` lists every plan: `id`, `title`, `status`, `inputs` (the owner's messages it answers), `decisions`, `files` (what it touches), `created`, `updated`.
- A distributed plan moves to `archive/plans/`. Never edit an archived plan; a later change to the same thing gets a new plan.

## Status

`draft` (being written) → `waiting` (shown to the owner) → `approved` (the owner said go) → `building` → `built` → `distributed` (its knowledge is in its homes) → archived. A plan can also be `dropped`, with the reason.

## The outline of a plan

Write it for the owner: plain words, real examples, a recommended default for every choice.

```markdown
# Plan: <what changes, in a few words>

Status: waiting · Request: <input ids> · Updated: <date>

## The request
What the owner asked, in a few lines, with their key words quoted.

## What it is for
The goal in one paragraph: the problem it solves and what is better after.

## What exists today
The parts of the system it touches, as they are now, briefly.

## The change
One section per part of the change: what it is, names and formats, a worked example.

## Choices for the owner
Each open choice with the options and the recommended default. The build follows the defaults unless the owner says otherwise.

## Steps
Numbered, in build order, each with the check that shows it is done.

## What it touches
Every file, agent, skill, doc, index list and feature that must change, from `build_map.py --context` and each file's Details (`update_with`).

## Where the knowledge goes once built
For each piece of knowledge: the file that will own it (a feature, a note, a skill, a How it works file), what the README says about it in short, the sentence the vision needs if any, and what the rebuild prompt needs exactly.

## Log
- <date time>: what happened (drafted, shown, approved, step n done, distributed).
```

## Steps

1. **Save the request.** Run `knowledge-intake` step 1 for the owner's message, so their words are stored before anything else.
2. **Write the plan** with status `draft`. Read the context of everything it touches first (`build_map.py --context <node>`, the levels above included). Add its row to `plans/index.json`.
3. **Show it.** Set `waiting`. Tell the owner in a few lines what it changes, with a link to the plan; put each choice that changes their goal on a decision card with your recommendation. For a big change, show one worked example first.
4. **On the owner's go,** set `approved` and record the decisions in `decisions.md` with the plan named in their status.
5. **Build** step by step. Run each step's check before the next. Tick the step and add a log line. Set `building`, then `built`.
6. **Distribute.** Move every piece of knowledge to the home the plan names, with `knowledge-intake` (write, ripple, record), refresh the How it works files with `file-index`, then the vision, the README and the rebuild prompt, in that order, at the level that changed and every level above it. Set `distributed`.
7. **Archive** the plan to `archive/plans/` and update its row. From now on the knowledge lives only in its homes.
8. **Later changes** to the same thing start from those homes, not from the archived plan: a new request, a new plan, and the files and features it touches updated again.

## Rules

- Nothing is built without a plan the owner has seen, except the small fixes above.
- A plan is a working document, not knowledge. The docs may mention a plan only as a proposal that waits for the owner.
- Decided means the owner decided. Everything else in a plan is a proposal until they say go.
- Never write a secret value in a plan.
- Keep the plan true while you build: when a step changes, change the plan and log why.

## Checks before you finish

- The plan's status and log match what happened.
- Every piece of knowledge in "Where the knowledge goes" is in its home, and `build_map.py --stale` prints nothing.
- The plan's row in `plans/index.json` is current.
