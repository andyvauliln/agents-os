---
about: agent-os/agents/system/.claude/skills/ide-build/scripts/check_page.js
node: n-10.1.2.5.2.7
basis: d449cc64734e
written: 2026-10-05T13:25:49Z
by: knowledge-base-agent
confirmed: 2026-10-07T19:02:04Z
---
# check_page.js

## Summary

The page check before publishing: it opens the page with a stand-in for claude.ai on a desktop and a phone width, opens How it works and File for the items it is given, and fails on an error, a missing tab or a page wider than the phone. It can save screenshots. It needs Node and Playwright.

## Keep in mind

- When a check fails, fix it before you publish; never publish a failing page.
