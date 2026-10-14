---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/CLAUDE.md
node: n-24.5
basis: f54d8c1b6d17
written: 2026-10-07T19:03:05Z
by: knowledge-base-agent
---
# CLAUDE.md

## Summary

The trading agent's own prompt: who it is, its strategy, its run loop, its allowed actions and where its config and docs live. Every run starts Claude Code in the variant's folder with it (proposed). It is the system's common prompt, plus the domain's trading layer `common/trading-prompt.md`, plus this agent's part; whether the shared parts are imported from linked copies or copied in at creation is open. It asks for the agent's probability (`prob`) on each trade, for calibration (proposed).

## Keep in mind

- When you want to change this prompt, make a new test variant with a new name; never edit the prompt of a running variant.
- When you write how the agent trades, send every order through the decision scripts (`scripts/*.decision.*`), never directly.
- When you add a risk limit, put it in config and code, not only in this prompt: outside text can carry prompt injection.
