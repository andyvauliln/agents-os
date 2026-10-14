---
about: agent-os/agents/system/.claude/skills/ide-build/scripts/check_page.js
basis: 83bc69f4a57e
written: 2026-10-14T15:04:45Z
by: project-ide-agent
confirmed: 2026-10-14T15:07:13Z
---
# check_page.js

## Summary

The page check before publishing: it opens the page with a stand-in for claude.ai on a desktop and a phone width, opens each item it is given by its path in the address, opens How it works and File, and fails on an error, a missing tab, an address that does not open its item, or a page wider than the phone. It can save screenshots. It needs Node and Playwright.

## Keep in mind

- When a check fails, fix it before you publish; never publish a failing page.
