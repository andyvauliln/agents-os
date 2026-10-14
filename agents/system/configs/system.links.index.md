---
about: agent-os/agents/system/configs/system.links.json
node: n-11.13
basis: 3e452ccd7924
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
---
# system.links.json

## What it is

The list of the files the system agent links in from other folders: for each link, which file, from where, where it appears and why. It also sets the format every agent uses for its own list. The system's list is short; most links belong to the agents at the lowest levels.

## Who looks after it

The script that creates agents writes the first version. After that the agent itself, its self-improvement helper and the owner edit it.

## When and how it changes

When the agent needs a file from somewhere else, or no longer needs one. Relink then turns the list into links.

## Who uses it, and when

Relink and the link check read it every time they run; the index of all links and the dashboard show who links what.

## Where it is mentioned

The links files of every other agent, the rules for links, and the relink script.

## Related knowledge

- Links point at single files only, never at keys and never into an AI setup folder.
- Child links are not listed here; relink makes them from the folders.
- Still open: whether the links themselves are saved in git or rebuilt after every download.

## Keep in mind

- When you add or change a link, edit this list and run relink; never make a link by hand.
- When a link would point at a key or into an AI setup folder, don't add it.
