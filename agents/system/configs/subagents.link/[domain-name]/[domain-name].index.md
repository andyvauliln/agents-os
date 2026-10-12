---
about: agent-os/agents/system/configs/subagents.link/[domain-name]/
node: n-11.2.1
basis: 2c81af3b9662
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
confirmed: 2026-10-09T10:03:12Z
---
# [domain-name]/

## What it is

A link to one domain's settings folder, named after the domain, for example `prediction-market/` for the prediction-market domain inside `trading/`. Through it the system sees that domain's settings and jobs without keeping a copy.

## Who looks after it

Nobody edits it. The shared relink script creates it when a domain is added and removes it when the domain is gone.

## When and how it changes

Only when a domain is added or removed. Relink then makes or deletes the link; it is never made by hand.

## Who uses it, and when

The system agent, the dashboard and the self-improvement helpers, whenever they read the settings or jobs of one domain. They read through it and never write.

## Where it is mentioned

The system's settings folder, the rules for child links, and the same kind of link in every level's other folders.

## Related knowledge

- Every level has these child links in each of its folders, so the system reaches any agent one level at a time.
- The link name carries no `.link` of its own; the folder around it marks it as a link.

## Keep in mind

- When a domain is added or removed, run relink; never make or delete the link by hand.
