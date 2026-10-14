---
about: agent-os/agents/system/docs/how-to/
node: n-2.11
basis: 7f01275fa2d4
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
---
# how-to/

## Summary

The step-by-step runbooks that agents and the owner follow for recurring operations, the same for any agent; they make "create a new agent based on this input" repeatable. They cover an agent's life (create it, promote it to live with the owner's approval, stop or delete it), what it uses (add a worker or job, add or change a link, add a platform or model, add a key or account), its quality and history (add or run tests, record research), and the knowledge base itself (process an input). A domain adds its own steps in its own runbooks, as the prediction-market domain does for trading. Every runbook except the input flow is still a proposal.

## Keep in mind

- When you change a process here, change the matching script in `scripts/` in the same change, so the steps and the code stay in line.
