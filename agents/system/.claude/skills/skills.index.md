---
about: agent-os/agents/system/.claude/skills/
basis: 2fb602858499
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# skills/

## What it is

The system level's skills: each one a folder with a `SKILL.md` that tells an agent how to do one job well. The main one is `change-plan`, which every AI follows for every change: plan it, show it to the owner, build it, then move its knowledge home. The knowledge base agent's skills save and sort every input (`knowledge-intake`), write every metadata file (`file-index`), write each level's docs (`vision-doc`, `readme-doc`, `readme-asd-doc`, `rebuild-prompt-doc`) and `CLAUDE.md` (`claude-md-doc`), and find the questions only the owner can answer (`make-questions`). The project IDE agent's skills build and publish the File Tree page (`ide-build`, with the build scripts inside it) and bring back what the owner leaves on it (`ide-sync`). `[skill-name]/` is the pattern for further skills.

## Who looks after it

It is written by the owner, knowledge-base-agent and change-plan.

## When and how it changes

It changes when a skill is added, renamed or removed.

## Who uses it, and when

It is read by Claude Code started in agents/system/, knowledge-base-agent and project-ide-agent.

## Where it is mentioned

It is described in `agents/system/docs/README.md` and its folder's How it works file `agents/system/.claude/.claude.index.md`.

## Related knowledge

It is read by `agents/system/.claude/agents/knowledge-base-agent.md`, `agents/system/.claude/agents/project-ide-agent.md` and `agents/system/CLAUDE.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `agents/system/docs/README.md` (section "Each agent's AI setup") and `agents/system/docs/rebuild-prompt.md` (section "The standard .claude/ folder").

## Keep in mind


