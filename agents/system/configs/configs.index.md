---
about: agent-os/agents/system/configs/
basis: 3c4a47633d3d
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T19:42:37Z
---
# configs/

## What it is

The system's settings folder. It holds the settings that hold for every agent, the choice of AI model for every agent, the system agent's own jobs and links, and one link to each domain's settings folder. All of it is plain JSON files people can open and edit.

## Who looks after it

The system's support helpers write the shared settings; the owner changes jobs from the File Tree page and approves changes to the modes, the stop switch and the live list.

## When and how it changes

When a system-wide setting, a model choice, a system job or a system link changes; and when a domain is added or removed, which adds or removes its link.

## Who uses it, and when

Every agent at the start of each run reads the shared settings and the model choice through its own links; the scheduler reads the jobs; the File Tree page shows all of it.

## Where it is mentioned

Every agent's own settings folder, which has the same kind of files; each domain's own config; the rules for merging settings; the File Tree page.

## Related knowledge

- Settings merge from here, then the domain's config, then the agent's own, then the owner's overrides; a lower layer may only tighten a limit.
- Each agent keeps its own settings, jobs and links in its own settings folder; only what every agent shares lives here.
- The exact shape of the files, and which settings are shared, are still open.

## Keep in mind

- When a setting applies to one agent or one domain only, put it in that agent's or domain's own settings, not here.
- When a key is needed, list its name only; never write its value.
