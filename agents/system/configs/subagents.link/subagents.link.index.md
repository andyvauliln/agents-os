---
about: agent-os/agents/system/configs/subagents.link/
node: n-11.2
basis: df2ab74c0c6c
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
confirmed: 2026-10-09T10:03:12Z
---
# subagents.link/

## What it is

One link per domain, each pointing at that domain's settings folder. It lets the system read the settings and jobs of every domain from one place, one domain at a time.

## Who looks after it

The relink script keeps it in step with the folders: one link for each domain that exists, none for domains that are gone.

## When and how it changes

When a domain is added or removed. Relink adds or removes its link.

## Who uses it, and when

The system agent and the dashboard when they show or check the settings and jobs of all domains; the self-improvement helpers when they compare domains.

## Where it is mentioned

The system's settings folder, the rules for child links, and the description of how a parent sees its children.

## Related knowledge

Every level has the same kind of folder in each of its own folders, so each level sees the one below it. The links are read-only.

## Keep in mind

- When you need a domain's settings, read them through this folder; never copy them into the system's folder.
