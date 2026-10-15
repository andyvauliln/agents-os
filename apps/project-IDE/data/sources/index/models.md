# Agent OS: Models index (v0.2)

The platforms and models the system may use, their status, and what routes to each one [2.18.6]. It is a view of [11.11] `models.config.json` (D-011), written by hand for now. File format and the lookup rule: see data-schemas.md, `schema-models-config`. Adding a platform or model: see how-to/add-platform-or-model.md.

## Platforms and models
<!-- k: id=idx-models-platforms applies=[2.18.6],[11.11],name:models.config.link.json sources=D-011,in-20260929-1455,D-056 status=decided -->
The owner's list (first input, vision §9), with the platform and model keys [11.11] uses.

| Platform | Model | Status | Default effort | Use for |
|---|---|---|---|---|
| Claude Code (`claude-code`) | `opus-5.5` | default | xhigh | thinking, planning, intelligent tasks, main agents, analysis, improvements |
| Claude Code (`claude-code`) | `sonnet-5.5` | supported | medium | unimportant tasks |
| Cursor (`cursor`) | `composer-2.5` | supported | not set | easy jobs, data handling, light analysis, filtering; mostly workers and sub-agents; work that uses many tokens but needs little intelligence |
| OpenRouter (`openrouter`) | free models in rotation | supported, not connected yet | - | unimportant things |
| Codex (`codex`) | not named | later | - | - |
| Kimi (`kimi`) | Kimi 3 | later | - | - |

The platform and model can also be part of an agent's name (e.g. `opus55` in the prediction-market domain's names), so agents that differ only by model can run side by side.

## Who routes to each model
<!-- k: id=idx-models-routes applies=[2.18.6],[11.11] sources=D-011,D-029,D-032,derived,D-056 status=proposed -->
A job's own `model` wins; `model: route` takes `routes[name]`, else `defaults_by_type[type]` from [11.11]. Agents and jobs: see agents.md and workers.md.

| Model | Type defaults ([11.11]) | Named routes | Jobs that name it | Agents whose name carries it |
|---|---|---|---|---|
| `opus-5.5` | `main`, `domain`, `si` | `pm-strategy-1.momentum-v1.opus55-test` (data-schemas.md example) | `system-self-improvement`, `knowledge-sync` ([11.10]); `domain-self-improvement` ([19.2.1]); `strategy-self-improvement` ([21.2.1]); `main-run` ([27.4]) | `pm-strategy-1-agent.opus55-test`, `pm-strategy-1.momentum-v1.opus55-test`, `pm-strategy-1.momentum-v2.opus55-test` |
| `sonnet-5.5` | `support` | `news-digest` | `news-digest` ([11.10]); `election-night-check` ([19.2.1]); `compare-variants` ([21.2.1]) | `pm-strategy-1.momentum-v2.sonnet55-test` |
| `composer-2.5` | `sub`, `worker` | - | - | - |

- **Jobs with `model: route`:** `domain-session` ([19.2.1]) resolves to `opus-5.5` by type `domain`. `strategy-session` ([21.2.1]) and `close-before-resolution` ([27.4]) have no clear route yet (see Open). `scripts-review` ([11.10]) is on Codex, which is `later`, so the job is off.
- **Scripts** (`platform: none`) use no model.
- **Type defaults vs job models:** the knowledge agent is type `support` (`sonnet-5.5`) but its job names `opus-5.5`; `news-digest` is type `sub` (`composer-2.5`) but has the named route `sonnet-5.5`.

## Open questions
<!-- k: id=idx-models-open applies=[2.18.6],[11.11] sources=in-20260929-2130,in-20260929-2132,derived,D-056 status=open -->
- **Type names:** [11.11] routes by `main`, `domain`, `si`, `sub`, `worker`, `support`, while the agent config types are `system`, `domain` and the types each domain defines (`strategy` and `variant` in the prediction-market domain). There is no default for the system agent or a strategy agent, and `main` is presumably the agent at the lowest level (a variant in the prediction-market domain).
- **Default effort:** [11.11] gives `opus-5.5` effort `xhigh` (owner's first input), but the owner later asked for "opus 5.5 medium" as the default when picking a model on the page (in-20260929-2130), and the page's Routes example uses `medium` for `main`, `high` for `si`.
- **Sub-agent default:** [11.11] says `sub` = `composer-2.5`; the page's Routes example says `sub` = `sonnet-5.5`.
- **More models:** the page's model pickers offer `fable-5.1` and `haiku-4.5` too (the owner asked for "fable, opus 5.5, sonnet 5.5, haiku", in-20260929-2132); neither is in [11.11] yet.
- **Routes for skills, workflows and commands:** which name a `skill`, `workflow` or `command` job is routed by (its job id or its owner agent) is open (data-schemas.md, `schema-models-config`).

## Changelog
- v0.2 (2026-10-07): neutral wording for agent types and model names; the copy-trading agent removed from the `composer-2.5` row (D-056, D-058).
- v0.1 (2026-09-30): created from file-tree.md v1.16, vision.md v0.19, tools/tabs.py and the owner inputs (D-033).
