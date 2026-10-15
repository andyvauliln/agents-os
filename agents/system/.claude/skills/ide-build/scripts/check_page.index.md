---
about: agent-os/agents/system/.claude/skills/ide-build/scripts/check_page.js
basis: 522d19e12243
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-15T11:08:51Z
---
# check_page.js

## What it is

The page check before publishing: it opens the page with a stand-in for claude.ai on a desktop and a phone width, opens each item it is given by its path in the address, opens How it works and File, and fails on an error, a missing tab, an address that does not open its item, or a page wider than the phone. It can save screenshots. It needs Node and Playwright.

## Who looks after it

It is written by the owner and project-ide-agent.

## When and how it changes

It changes when the page gains a tab or a mode that must be checked, or the check rules change.

## Who uses it, and when

It is read by ide-build and project-ide-agent.

## Where it is mentioned

It is described in `agents/system/.claude/skills/ide-build/SKILL.md` and its folder's How it works file `agents/system/.claude/skills/ide-build/scripts/scripts.index.md`.

## Related knowledge

It reads `apps/project-IDE/current-ui/file-tree-explorer.html`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `agents/system/CLAUDE.md` (section "The File Tree page"), `docs/metadata.md`, `agents/system/docs/README.md` (section "The project IDE"), `apps/project-IDE/docs/README.md` (section "How the page is built and checked") and `agents/system/.claude/skills/ide-build/scripts/README.md`.

## Keep in mind

- When a check fails, fix it before you publish; never publish a failing page.
- When `PLAYWRIGHT`, `CHROMIUM` or `PLAYWRIGHT_LIBS` are not set, it reads them from `.playwright.env` at the top of the repository, which `./init.sh` writes on each machine; run `./init.sh` again when the check cannot find its browser.
