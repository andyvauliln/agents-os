# Agent OS: Add or change a link (v0.2)

How an agent (or the owner, or its SI sub-agent) links a file it needs from anywhere: the system, its own domain or a level above it, another domain, or any other agent by its unique name (D-031). Links are listed in the agent's own links file and built by the shared `relink` script [14.1]; never by hand. Link rules: see conventions.md and common/shared-mechanics.md. Format: [11.13] and data-schemas.md.

## Steps
<!-- k: id=howto-add-or-change-link-steps applies=[2.11.9],name:*.links.json,name:relink.system.link.js,name:settings.json,[14.1],[16.1],[27.4],[46.2] sources=D-020,D-030,D-031,in-20260930-1153 status=proposed -->
1. **Find the file you need.** The index [2.18] lists every producer; the links index [16.1] `links.index.json` shows who already reads a file. Prefer a stable `latest.*` output over a dated file.
2. **Edit your own links file** `configs/[name].links.json` (like [27.3]). Add or change one entry:
   - `to`: where the link appears in your own `configs/`, `scripts/`, `logs/`, `data/`, `docs/`, `tests/` or `research/`, with `.link` in the name, e.g. `data/[output].link.json`;
   - `from`: the real file, as `@system/...`, `@domain/...` (your domain), `@strategy/...` (your strategy), `@[name]/...` (any domain or agent by name) or a path under `agents/`, e.g. `@[agent-id]/data/[output]/latest.json`;
   - `why`, `required`, `enabled`, `added_by`, `added`.
3. **Let relink run.** The `PostToolUse` hook in your `.claude/settings.json` or the scheduler's `relink` job runs it by itself; or run it yourself from your folder: `node scripts/relink.system.link.js`.
4. **Read its report:** each link added (`+`), removed (`-`) or unchanged (`=`), then `check ok`.
5. **If a change to that file must restart your main run at once,** add the link path to that job's `on_change` in your workers file (like [27.4]).
6. **Record it** in your `docs/changes.md` under `Links`: `+ to <- from: why` or `- to: why` (proposed format).
7. **To remove a link,** delete its entry or set `enabled: false`; relink then removes the symlink.

Never create or delete symlinks by hand, never link anything in `.secrets/` or any `.claude/`, and never put `to` inside `subagents.link/` (child links are built from the folder tree and are not listed).

## Checks
<!-- k: id=howto-add-or-change-link-checks applies=[2.11.9],name:*.links.json,[16.1],[46.2] sources=D-020,D-031 status=proposed -->
- The symlink exists at `to`, has `.link` in its name, is relative and points straight at the real file (no chains).
- `node scripts/relink.system.link.js --check` exits 0, and the links index [16.1] shows the link as ok.
- A `required` link's target exists; if it does not, the main run will not start.
- The change is in `changes.md`. Whether a link change makes a new version is still open ([27.3]).

## Changelog
- v0.2 (2026-10-07): neutral examples; the `whale-signals` example left with the copy-trading domain (D-056, D-058).
- v0.1 (2026-09-30): created from file-tree.md v1.15, vision.md v0.19 and the owner inputs (D-033).
