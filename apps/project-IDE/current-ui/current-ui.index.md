---
about: agent-os/apps/project-IDE/current-ui/
basis: b1808b1ee264
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T19:42:37Z
---
# current-ui/

## What it is

The File Tree page as the owner uses it now: `file-tree-explorer.html`, the page itself, `file-tree.data.json`, the one data file it loads, and `real-files.json`, the text of every file, which the page loads the first time a file is opened. The build writes the two data files here from the files on disk. It is published on claude.ai at a fixed link, and the owner's server serves this same folder; the project IDE agent rebuilds the data, checks the page on a desktop and a phone width and publishes it again after every round that changes a file, a folder or a metadata file.

## Who looks after it

It is written by project-ide-agent and ide-build.

## When and how it changes

It changes when the page or its data is built again.

## Who uses it, and when

It is read by the owner, `apps/project-IDE/server/server.py` and project-ide-agent.

## Where it is mentioned

It is described in `apps/project-IDE/docs/README.md` and its folder's How it works file `apps/project-IDE/project-IDE.index.md`.

## Related knowledge

It links to `apps/project-IDE/current-ui/file-tree-explorer.html` and `apps/project-IDE/current-ui/file-tree.data.json`. It is read by `apps/project-IDE/server/server.py`. It is written by `agents/system/.claude/skills/ide-build/SKILL.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `apps/docs/README.md` (section "The project IDE") and `apps/project-IDE/docs/README.md` (section "The three places the page runs").

## Keep in mind


