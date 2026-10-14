---
about: agent-os/agents/system/configs/system.config.json
node: n-11.1
basis: 0e084038141c
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
---
# system.config.json

## What it is

The one file of settings that hold for the whole system and every agent: default values, test or live mode with the list of agents allowed to act live, the general stop switch, schedule defaults, what counts as an important change, and notifications. Jobs and the choice of AI model are kept in their own files, and a domain's own settings, such as the prediction-market domain's trading settings, in that domain's config.

## Who looks after it

The system's support helpers write it. Changes to the modes, the stop switch and the live list need the owner's approval.

## When and how it changes

When a setting for the whole system changes. A section that grows long moves into a file of its own.

## Who uses it, and when

Every agent at the start of each run, merged with its domain's settings and its own into the settings it actually uses. Every script that acts checks the stop switch before each action; the dashboard shows the values.

## Where it is mentioned

Each agent's own settings file and its link to this file, each domain's own config, the rules for merging settings, the safety rules and the dashboard.

## Related knowledge

- A lower level's settings can only make a limit stricter, never looser.
- No agent can switch itself to live: live needs the live list here, the owner's approval and the stop switch off.
- The sections and their fields are still a proposal.

## Keep in mind

- When you add a setting, put it here only if it holds for every agent; a domain's setting goes in the domain's config, one agent's in its own.
- When you change the modes, the stop switch or the live list, get the owner's approval first.
- When a key is needed, write only its name, never its value.
