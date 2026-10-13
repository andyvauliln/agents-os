# What happens to every file in vision/

- Input: in-20261013-vision-files (2026-10-13). Goes with the plan [2026-10-13-leave-vision.md](2026-10-13-leave-vision.md).
- Status: proposed, waiting for the owner's go. Nothing has moved yet.
- Made by comparing each of the 1748 files in git under `vision/` with the file at its new place, byte for byte. Empty files and old versions in the archive are counted per folder; every other file has its own line.

## In short

| What happens | Files |
|---|---|
| Deleted: old versions, backups, pointers, caches, empty files. Git history keeps them. | 614 |
| Kept for stage two: prediction-market files with text and their metadata, in the IDE sources. | 472 |
| Deleted here, because the same file already sits at its real place (most are How it works and Details files next to their items). | 353 |
| Moved to its real place: no copy there yet. | 198 |
| Deleted: the older system and trading docs, replaced by the new docs at five levels. | 106 |
| Made by the build at the new place; deleted here. | 3 |
| Its content goes into other files first, then it moves. | 1 |
| Replaces an older copy at its real place. | 1 |

## Where things go

- `apps/project-IDE/data/`: inputs, decisions, changelog, plans, memory, overrides. Its `sources/` folder holds the knowledge notes the docs were written from, and the prediction-market files and metadata for stage two.
- `apps/project-IDE/current-ui/`: the page. `apps/project-IDE/server/`: the server.
- `agents/system/.claude/`: skills and helper agents. `agents/system/.claude/skills/ide-build/scripts/`: the build tools.
- `agents/system/docs/how-to/`: the how-to guides.

## To check before we delete

- The older system docs (102 files in `archive/2026-10-12/agents-system-docs/`, 30 with text), the old `.claude/docs` drafts and the old trading notes are marked delete, because the new docs at five levels were written from them. I checked the 30 with text: 29 are the same as the notes in `vision/docs/`, which move to `apps/project-IDE/data/sources/`. The 30th, `inputs-vision.md` (every requirement from your inputs), exists only in the archive, so it moves to the sources too.

## Every file

```text
└── vision/
    ├── .claude/
    │   ├── agents/
    │   │   ├── agents.index.md  —  delete · same copy already at agents/system/.claude/agents/agents.index.md
    │   │   ├── agents.meta.json  —  delete · same copy already at agents/system/.claude/agents/agents.meta.json
    │   │   ├── knowledge-base-agent.index.md  —  delete · same copy already at agents/system/.claude/agents/knowledge-base-agent.index.md
    │   │   ├── knowledge-base-agent.md  —  delete · same copy already at agents/system/.claude/agents/knowledge-base-agent.md (then fix its vision/ paths)
    │   │   ├── knowledge-base-agent.meta.json  —  delete · same copy already at agents/system/.claude/agents/knowledge-base-agent.meta.json
    │   │   ├── project-ide-agent.index.md  —  delete · same copy already at agents/system/.claude/agents/project-ide-agent.index.md
    │   │   ├── project-ide-agent.md  —  delete · same copy already at agents/system/.claude/agents/project-ide-agent.md (then fix its vision/ paths)
    │   │   └── project-ide-agent.meta.json  —  delete · same copy already at agents/system/.claude/agents/project-ide-agent.meta.json
    │   ├── knowledge/
    │   │   └── sources/
    │   │       ├── readme.md  —  move → apps/project-IDE/data/sources/readme.md
    │   │       ├── rebuild-prompt.md  —  move → apps/project-IDE/data/sources/rebuild-prompt.md
    │   │       └── vision.md  —  move → apps/project-IDE/data/sources/vision.md
    │   ├── memory/
    │   │   ├── agent-os-trading-domain.md  —  move → apps/project-IDE/data/memory/agent-os-trading-domain.md
    │   │   ├── apps-docs-clones-forks.md  —  move → apps/project-IDE/data/memory/apps-docs-clones-forks.md
    │   │   ├── claude-folder-docs-layout.md  —  move → apps/project-IDE/data/memory/claude-folder-docs-layout.md
    │   │   ├── file-family-plan.md  —  move → apps/project-IDE/data/memory/file-family-plan.md
    │   │   ├── file-tree-explorer-sync.md  —  move → apps/project-IDE/data/memory/file-tree-explorer-sync.md
    │   │   ├── full-context-for-ai.md  —  move → apps/project-IDE/data/memory/full-context-for-ai.md
    │   │   ├── general-system-plan.md  —  move → apps/project-IDE/data/memory/general-system-plan.md
    │   │   ├── github-sync-plan.md  —  move → apps/project-IDE/data/memory/github-sync-plan.md
    │   │   ├── human-docs-style.md  —  move → apps/project-IDE/data/memory/human-docs-style.md
    │   │   ├── knowledge-intake-every-input.md  —  move → apps/project-IDE/data/memory/knowledge-intake-every-input.md
    │   │   ├── MEMORY.md  —  move → apps/project-IDE/data/memory/MEMORY.md
    │   │   ├── planned-items-are-real-files.md  —  move → apps/project-IDE/data/memory/planned-items-are-real-files.md
    │   │   ├── README.md  —  move → apps/project-IDE/data/memory/README.md
    │   │   └── stage-one.md  —  move → apps/project-IDE/data/memory/stage-one.md
    │   ├── skills/
    │   │   ├── change-plan/
    │   │   │   ├── SKILL.index.md  —  delete · same copy already at agents/system/.claude/skills/change-plan/SKILL.index.md (then fix its vision/ paths)
    │   │   │   ├── SKILL.md  —  delete · same copy already at agents/system/.claude/skills/change-plan/SKILL.md (then fix its vision/ paths)
    │   │   │   └── SKILL.meta.json  —  delete · same copy already at agents/system/.claude/skills/change-plan/SKILL.meta.json (then fix its vision/ paths)
    │   │   ├── claude-md-doc/
    │   │   │   ├── SKILL.index.md  —  delete · same copy already at agents/system/.claude/skills/claude-md-doc/SKILL.index.md
    │   │   │   ├── SKILL.md  —  delete · same copy already at agents/system/.claude/skills/claude-md-doc/SKILL.md
    │   │   │   └── SKILL.meta.json  —  delete · same copy already at agents/system/.claude/skills/claude-md-doc/SKILL.meta.json
    │   │   ├── file-index/
    │   │   │   ├── SKILL.index.md  —  delete · same copy already at agents/system/.claude/skills/file-index/SKILL.index.md
    │   │   │   ├── SKILL.md  —  delete · same copy already at agents/system/.claude/skills/file-index/SKILL.md
    │   │   │   └── SKILL.meta.json  —  delete · same copy already at agents/system/.claude/skills/file-index/SKILL.meta.json
    │   │   ├── ide-build/
    │   │   │   ├── ide-build.index.md  —  delete · same copy already at agents/system/.claude/skills/ide-build/ide-build.index.md (then fix its vision/ paths)
    │   │   │   ├── ide-build.meta.json  —  delete · same copy already at agents/system/.claude/skills/ide-build/ide-build.meta.json (then fix its vision/ paths)
    │   │   │   ├── SKILL.index.md  —  delete · same copy already at agents/system/.claude/skills/ide-build/SKILL.index.md (then fix its vision/ paths)
    │   │   │   ├── SKILL.md  —  delete · same copy already at agents/system/.claude/skills/ide-build/SKILL.md (then fix its vision/ paths)
    │   │   │   └── SKILL.meta.json  —  delete · same copy already at agents/system/.claude/skills/ide-build/SKILL.meta.json (then fix its vision/ paths)
    │   │   ├── ide-sync/
    │   │   │   ├── SKILL.index.md  —  delete · same copy already at agents/system/.claude/skills/ide-sync/SKILL.index.md (then fix its vision/ paths)
    │   │   │   ├── SKILL.md  —  delete · same copy already at agents/system/.claude/skills/ide-sync/SKILL.md (then fix its vision/ paths)
    │   │   │   └── SKILL.meta.json  —  delete · same copy already at agents/system/.claude/skills/ide-sync/SKILL.meta.json (then fix its vision/ paths)
    │   │   ├── knowledge-intake/
    │   │   │   ├── SKILL.index.md  —  delete · same copy already at agents/system/.claude/skills/knowledge-intake/SKILL.index.md (then fix its vision/ paths)
    │   │   │   ├── SKILL.md  —  delete · same copy already at agents/system/.claude/skills/knowledge-intake/SKILL.md (then fix its vision/ paths)
    │   │   │   └── SKILL.meta.json  —  delete · same copy already at agents/system/.claude/skills/knowledge-intake/SKILL.meta.json (then fix its vision/ paths)
    │   │   ├── readme-asd-doc/
    │   │   │   ├── SKILL.index.md  —  delete · same copy already at agents/system/.claude/skills/readme-asd-doc/SKILL.index.md
    │   │   │   ├── SKILL.md  —  delete · same copy already at agents/system/.claude/skills/readme-asd-doc/SKILL.md
    │   │   │   └── SKILL.meta.json  —  delete · same copy already at agents/system/.claude/skills/readme-asd-doc/SKILL.meta.json
    │   │   ├── readme-doc/
    │   │   │   ├── SKILL.index.md  —  delete · same copy already at agents/system/.claude/skills/readme-doc/SKILL.index.md
    │   │   │   ├── SKILL.md  —  delete · same copy already at agents/system/.claude/skills/readme-doc/SKILL.md
    │   │   │   └── SKILL.meta.json  —  delete · same copy already at agents/system/.claude/skills/readme-doc/SKILL.meta.json
    │   │   ├── rebuild-prompt-doc/
    │   │   │   ├── SKILL.index.md  —  delete · same copy already at agents/system/.claude/skills/rebuild-prompt-doc/SKILL.index.md
    │   │   │   ├── SKILL.md  —  delete · same copy already at agents/system/.claude/skills/rebuild-prompt-doc/SKILL.md
    │   │   │   └── SKILL.meta.json  —  delete · same copy already at agents/system/.claude/skills/rebuild-prompt-doc/SKILL.meta.json
    │   │   ├── vision-doc/
    │   │   │   ├── SKILL.index.md  —  delete · same copy already at agents/system/.claude/skills/vision-doc/SKILL.index.md
    │   │   │   ├── SKILL.md  —  delete · same copy already at agents/system/.claude/skills/vision-doc/SKILL.md
    │   │   │   └── SKILL.meta.json  —  delete · same copy already at agents/system/.claude/skills/vision-doc/SKILL.meta.json
    │   │   ├── skills.index.md  —  delete · same copy already at agents/system/.claude/skills/skills.index.md
    │   │   └── skills.meta.json  —  delete · same copy already at agents/system/.claude/skills/skills.meta.json
    │   ├── .claude.index.md  —  delete · same copy already at agents/system/.claude/.claude.index.md
    │   └── .claude.meta.json  —  delete · same copy already at agents/system/.claude/.claude.meta.json
    ├── archive/
    │   ├── 2026-10-12/
    │   │   ├── agents-system-docs/
    │   │   │   ├── common/
    │   │   │   │   ├── agent-architecture.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── agent-architecture.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── agent-architecture.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── common-prompt.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── common-prompt.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── common-prompt.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── common.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── common.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── self-improvement-templates.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── self-improvement-templates.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── self-improvement-templates.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── shared-mechanics.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── shared-mechanics.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   └── shared-mechanics.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── how-to/
    │   │   │   │   ├── add-account-or-secret.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── add-account-or-secret.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── add-account-or-secret.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── add-or-change-link.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── add-or-change-link.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── add-or-change-link.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── add-or-run-tests.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── add-or-run-tests.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── add-or-run-tests.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── add-platform-or-model.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── add-platform-or-model.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── add-platform-or-model.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── add-worker.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── add-worker.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── add-worker.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── create-agent.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── create-agent.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── create-agent.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── how-to.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── how-to.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── process-an-input.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── process-an-input.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── process-an-input.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── promote-to-live.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── promote-to-live.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── promote-to-live.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── record-research.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── record-research.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── record-research.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── stop-or-delete-agent.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── stop-or-delete-agent.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   └── stop-or-delete-agent.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── index/
    │   │   │   │   ├── agents.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── agents.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── agents.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── apps.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── apps.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── apps.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── index.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── index.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── links.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── links.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── links.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── models.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── models.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── models.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── services.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── services.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── services.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── subagents.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── subagents.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── subagents.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── workers.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   ├── workers.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   │   └── workers.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── architecture.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── architecture.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── architecture.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── conventions.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── conventions.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── conventions.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── data-schemas.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── data-schemas.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── data-schemas.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── feature-map.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── feature-map.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── feature-map.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── flows.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── flows.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── flows.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── glossary.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── glossary.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── glossary.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── metrics.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── metrics.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── metrics.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── overview.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── overview.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── overview.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── roadmap.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── roadmap.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── roadmap.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── safety.index.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── safety.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── safety.meta.json  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   └── (the rest)  —  delete · 3 files (the same file moves from archive/2026-10-12/claude-docs/)
    │   │   ├── claude-docs/
    │   │   │   ├── CLAUDE.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── inputs-vision.index.md  —  move → apps/project-IDE/data/sources/inputs-vision.index.md
    │   │   │   ├── inputs-vision.md  —  move → apps/project-IDE/data/sources/inputs-vision.md
    │   │   │   ├── inputs-vision.meta.json  —  move → apps/project-IDE/data/sources/inputs-vision.meta.json
    │   │   │   ├── README.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── rebuild-prompt.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   └── vision.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   ├── prediction-market/
    │   │   │   ├── .claude/
    │   │   │   │   ├── settings.json  —  stage two → apps/project-IDE/data/sources/prediction-market/files/.claude/settings.json
    │   │   │   │   └── settings.local.json  —  stage two → apps/project-IDE/data/sources/prediction-market/files/.claude/settings.local.json
    │   │   │   ├── configs/
    │   │   │   │   ├── prediction-market-agents.config.json  —  stage two → apps/project-IDE/data/sources/prediction-market/files/configs/prediction-market-agents.config.json
    │   │   │   │   ├── prediction-market-agents.links.json  —  stage two → apps/project-IDE/data/sources/prediction-market/files/configs/prediction-market-agents.links.json
    │   │   │   │   └── prediction-market-agents.workers.json  —  stage two → apps/project-IDE/data/sources/prediction-market/files/configs/prediction-market-agents.workers.json
    │   │   │   ├── docs/
    │   │   │   │   ├── common/
    │   │   │   │   │   ├── strategy-si-templates.md  —  stage two → apps/project-IDE/data/sources/prediction-market/files/docs/common/strategy-si-templates.md
    │   │   │   │   │   ├── trading-agent-architecture.md  —  stage two → apps/project-IDE/data/sources/prediction-market/files/docs/common/trading-agent-architecture.md
    │   │   │   │   │   └── trading-prompt.md  —  stage two → apps/project-IDE/data/sources/prediction-market/files/docs/common/trading-prompt.md
    │   │   │   │   ├── how-to/
    │   │   │   │   │   ├── add-trading-account.md  —  stage two → apps/project-IDE/data/sources/prediction-market/files/docs/how-to/add-trading-account.md
    │   │   │   │   │   ├── create-strategy-or-variant.md  —  stage two → apps/project-IDE/data/sources/prediction-market/files/docs/how-to/create-strategy-or-variant.md
    │   │   │   │   │   ├── go-live-with-money.md  —  stage two → apps/project-IDE/data/sources/prediction-market/files/docs/how-to/go-live-with-money.md
    │   │   │   │   │   └── stop-trading-agent.md  —  stage two → apps/project-IDE/data/sources/prediction-market/files/docs/how-to/stop-trading-agent.md
    │   │   │   │   ├── index/
    │   │   │   │   │   └── accounts.md  —  stage two → apps/project-IDE/data/sources/prediction-market/files/docs/index/accounts.md
    │   │   │   │   ├── doc-outlines.md  —  stage two → apps/project-IDE/data/sources/prediction-market/files/docs/doc-outlines.md
    │   │   │   │   ├── trading-architecture.md  —  stage two → apps/project-IDE/data/sources/prediction-market/files/docs/trading-architecture.md
    │   │   │   │   ├── trading-conventions.md  —  stage two → apps/project-IDE/data/sources/prediction-market/files/docs/trading-conventions.md
    │   │   │   │   ├── trading-data-schemas.md  —  stage two → apps/project-IDE/data/sources/prediction-market/files/docs/trading-data-schemas.md
    │   │   │   │   ├── trading-feature-map.md  —  stage two → apps/project-IDE/data/sources/prediction-market/files/docs/trading-feature-map.md
    │   │   │   │   ├── trading-flows.md  —  stage two → apps/project-IDE/data/sources/prediction-market/files/docs/trading-flows.md
    │   │   │   │   ├── trading-glossary.md  —  stage two → apps/project-IDE/data/sources/prediction-market/files/docs/trading-glossary.md
    │   │   │   │   ├── trading-metrics.md  —  stage two → apps/project-IDE/data/sources/prediction-market/files/docs/trading-metrics.md
    │   │   │   │   ├── trading-overview.md  —  stage two → apps/project-IDE/data/sources/prediction-market/files/docs/trading-overview.md
    │   │   │   │   ├── trading-roadmap.md  —  stage two → apps/project-IDE/data/sources/prediction-market/files/docs/trading-roadmap.md
    │   │   │   │   └── trading-safety.md  —  stage two → apps/project-IDE/data/sources/prediction-market/files/docs/trading-safety.md
    │   │   │   ├── research/
    │   │   │   │   └── index.json  —  stage two → apps/project-IDE/data/sources/prediction-market/files/research/index.json
    │   │   │   ├── strategy-1-agent/
    │   │   │   │   ├── .claude/
    │   │   │   │   │   ├── settings.json  —  stage two → apps/project-IDE/data/sources/prediction-market/files/strategy-1-agent/.claude/settings.json
    │   │   │   │   │   └── settings.local.json  —  stage two → apps/project-IDE/data/sources/prediction-market/files/strategy-1-agent/.claude/settings.local.json
    │   │   │   │   ├── configs/
    │   │   │   │   │   ├── strategy-1-agent.links.json  —  stage two → apps/project-IDE/data/sources/prediction-market/files/strategy-1-agent/configs/strategy-1-agent.links.json
    │   │   │   │   │   └── strategy-1-agent.workers.json  —  stage two → apps/project-IDE/data/sources/prediction-market/files/strategy-1-agent/configs/strategy-1-agent.workers.json
    │   │   │   │   ├── pm-strategy-1.momentum-v1.opus55-test/
    │   │   │   │   │   ├── .claude/
    │   │   │   │   │   │   ├── settings.json  —  stage two → apps/project-IDE/data/sources/prediction-market/files/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/settings.json
    │   │   │   │   │   │   └── settings.local.json  —  stage two → apps/project-IDE/data/sources/prediction-market/files/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/settings.local.json
    │   │   │   │   │   ├── configs/
    │   │   │   │   │   │   ├── models.config.link.json  —  stage two → apps/project-IDE/data/sources/prediction-market/files/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/configs/models.config.link.json
    │   │   │   │   │   │   ├── pm-strategy-1.momentum-v1.opus55-test.config.json  —  stage two → apps/project-IDE/data/sources/prediction-market/files/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/configs/pm-strategy-1.momentum-v1.opus55-test.config.json
    │   │   │   │   │   │   ├── pm-strategy-1.momentum-v1.opus55-test.links.json  —  stage two → apps/project-IDE/data/sources/prediction-market/files/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/configs/pm-strategy-1.momentum-v1.opus55-test.links.json
    │   │   │   │   │   │   ├── pm-strategy-1.momentum-v1.opus55-test.workers.json  —  stage two → apps/project-IDE/data/sources/prediction-market/files/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/configs/pm-strategy-1.momentum-v1.opus55-test.workers.json
    │   │   │   │   │   │   ├── prediction-market-agents.config.link.json  —  stage two → apps/project-IDE/data/sources/prediction-market/files/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/configs/prediction-market-agents.config.link.json
    │   │   │   │   │   │   └── system.config.link.json  —  stage two → apps/project-IDE/data/sources/prediction-market/files/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/configs/system.config.link.json
    │   │   │   │   │   ├── data/
    │   │   │   │   │   │   ├── markets-catalog.link.json  —  stage two → apps/project-IDE/data/sources/prediction-market/files/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/data/markets-catalog.link.json
    │   │   │   │   │   │   └── polymarket-prices.link.json  —  stage two → apps/project-IDE/data/sources/prediction-market/files/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/data/polymarket-prices.link.json
    │   │   │   │   │   ├── research/
    │   │   │   │   │   │   └── index.json  —  stage two → apps/project-IDE/data/sources/prediction-market/files/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/research/index.json
    │   │   │   │   │   ├── tests/
    │   │   │   │   │   │   ├── agents/
    │   │   │   │   │   │   │   └── tests.config.json  —  stage two → apps/project-IDE/data/sources/prediction-market/files/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/tests/agents/tests.config.json
    │   │   │   │   │   │   └── scripts/
    │   │   │   │   │   │       └── tests.config.json  —  stage two → apps/project-IDE/data/sources/prediction-market/files/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/tests/scripts/tests.config.json
    │   │   │   │   │   └── package.json  —  stage two → apps/project-IDE/data/sources/prediction-market/files/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/package.json
    │   │   │   │   ├── research/
    │   │   │   │   │   └── index.json  —  stage two → apps/project-IDE/data/sources/prediction-market/files/strategy-1-agent/research/index.json
    │   │   │   │   ├── tests/
    │   │   │   │   │   ├── agents/
    │   │   │   │   │   │   └── tests.config.json  —  stage two → apps/project-IDE/data/sources/prediction-market/files/strategy-1-agent/tests/agents/tests.config.json
    │   │   │   │   │   └── scripts/
    │   │   │   │   │       └── tests.config.json  —  stage two → apps/project-IDE/data/sources/prediction-market/files/strategy-1-agent/tests/scripts/tests.config.json
    │   │   │   │   └── package.json  —  stage two → apps/project-IDE/data/sources/prediction-market/files/strategy-1-agent/package.json
    │   │   │   ├── tests/
    │   │   │   │   ├── agents/
    │   │   │   │   │   └── tests.config.json  —  stage two → apps/project-IDE/data/sources/prediction-market/files/tests/agents/tests.config.json
    │   │   │   │   └── scripts/
    │   │   │   │       └── tests.config.json  —  stage two → apps/project-IDE/data/sources/prediction-market/files/tests/scripts/tests.config.json
    │   │   │   ├── package.json  —  stage two → apps/project-IDE/data/sources/prediction-market/files/package.json
    │   │   │   └── (the rest)  —  delete · 501 files (empty prediction-market file or its empty metadata)
    │   │   ├── trading-docs/
    │   │   │   ├── README.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   ├── rebuild-prompt.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   │   └── vision.md  —  delete · older system and trading docs, replaced by the docs at five levels
    │   │   └── tree/
    │   │       ├── agent-os/
    │   │       │   └── agents/
    │   │       │       └── trading/
    │   │       │           └── prediction-market/
    │   │       │               ├── .claude/
    │   │       │               │   ├── agent-memory/
    │   │       │               │   │   └── [subagent-name]/
    │   │       │               │   │       ├── MEMORY.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/agent-memory/[subagent-name]/MEMORY.index.md
    │   │       │               │   │       └── MEMORY.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/agent-memory/[subagent-name]/MEMORY.meta.json
    │   │       │               │   ├── agents/
    │   │       │               │   │   ├── [subagent-name].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/agents/[subagent-name].index.md
    │   │       │               │   │   ├── [subagent-name].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/agents/[subagent-name].meta.json
    │   │       │               │   │   ├── pm-self-improvement-agent.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/agents/pm-self-improvement-agent.index.md
    │   │       │               │   │   └── pm-self-improvement-agent.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/agents/pm-self-improvement-agent.meta.json
    │   │       │               │   ├── commands/
    │   │       │               │   │   ├── [command-name].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/commands/[command-name].index.md
    │   │       │               │   │   └── [command-name].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/commands/[command-name].meta.json
    │   │       │               │   ├── output-styles/
    │   │       │               │   │   ├── [style-name].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/output-styles/[style-name].index.md
    │   │       │               │   │   └── [style-name].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/output-styles/[style-name].meta.json
    │   │       │               │   ├── rules/
    │   │       │               │   │   ├── [topic].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/rules/[topic].index.md
    │   │       │               │   │   └── [topic].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/rules/[topic].meta.json
    │   │       │               │   ├── skills/
    │   │       │               │   │   └── [skill-name]/
    │   │       │               │   │       ├── SKILL.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/skills/[skill-name]/SKILL.index.md
    │   │       │               │   │       └── SKILL.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/skills/[skill-name]/SKILL.meta.json
    │   │       │               │   ├── workflows/
    │   │       │               │   │   ├── [workflow-name].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/workflows/[workflow-name].index.md
    │   │       │               │   │   └── [workflow-name].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/workflows/[workflow-name].meta.json
    │   │       │               │   ├── CLAUDE.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/CLAUDE.index.md
    │   │       │               │   ├── CLAUDE.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/CLAUDE.meta.json
    │   │       │               │   ├── settings.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/settings.index.md
    │   │       │               │   ├── settings.local.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/settings.local.index.md
    │   │       │               │   ├── settings.local.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/settings.local.meta.json
    │   │       │               │   └── settings.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/settings.meta.json
    │   │       │               ├── configs/
    │   │       │               │   ├── prediction-market-agents.config.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/configs/prediction-market-agents.config.index.md
    │   │       │               │   ├── prediction-market-agents.links.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/configs/prediction-market-agents.links.index.md
    │   │       │               │   ├── prediction-market-agents.links.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/configs/prediction-market-agents.links.meta.json
    │   │       │               │   ├── prediction-market-agents.workers.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/configs/prediction-market-agents.workers.index.md
    │   │       │               │   └── prediction-market-agents.workers.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/configs/prediction-market-agents.workers.meta.json
    │   │       │               ├── docs/
    │   │       │               │   ├── common/
    │   │       │               │   │   ├── strategy-si-templates.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/common/strategy-si-templates.index.md
    │   │       │               │   │   ├── trading-agent-architecture.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/common/trading-agent-architecture.index.md
    │   │       │               │   │   └── trading-prompt.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/common/trading-prompt.index.md
    │   │       │               │   ├── how-to/
    │   │       │               │   │   ├── add-trading-account.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/how-to/add-trading-account.index.md
    │   │       │               │   │   ├── create-strategy-or-variant.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/how-to/create-strategy-or-variant.index.md
    │   │       │               │   │   ├── go-live-with-money.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/how-to/go-live-with-money.index.md
    │   │       │               │   │   └── stop-trading-agent.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/how-to/stop-trading-agent.index.md
    │   │       │               │   ├── index/
    │   │       │               │   │   └── accounts.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/index/accounts.index.md
    │   │       │               │   ├── doc-outlines.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/doc-outlines.index.md
    │   │       │               │   ├── README.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/README.index.md
    │   │       │               │   ├── README.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/README.meta.json
    │   │       │               │   ├── rebuild-prompt.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/rebuild-prompt.index.md
    │   │       │               │   ├── rebuild-prompt.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/rebuild-prompt.meta.json
    │   │       │               │   ├── trading-architecture.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/trading-architecture.index.md
    │   │       │               │   ├── trading-conventions.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/trading-conventions.index.md
    │   │       │               │   ├── trading-data-schemas.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/trading-data-schemas.index.md
    │   │       │               │   ├── trading-feature-map.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/trading-feature-map.index.md
    │   │       │               │   ├── trading-flows.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/trading-flows.index.md
    │   │       │               │   ├── trading-glossary.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/trading-glossary.index.md
    │   │       │               │   ├── trading-metrics.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/trading-metrics.index.md
    │   │       │               │   ├── trading-overview.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/trading-overview.index.md
    │   │       │               │   ├── trading-roadmap.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/trading-roadmap.index.md
    │   │       │               │   ├── trading-safety.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/trading-safety.index.md
    │   │       │               │   ├── vision.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/vision.index.md
    │   │       │               │   └── vision.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/vision.meta.json
    │   │       │               ├── research/
    │   │       │               │   ├── index.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/research/index.index.md
    │   │       │               │   └── index.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/research/index.meta.json
    │   │       │               ├── scripts/
    │   │       │               │   ├── markets-catalog.worker.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/scripts/markets-catalog.worker.index.md
    │   │       │               │   ├── markets-catalog.worker.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/scripts/markets-catalog.worker.meta.json
    │   │       │               │   ├── polymarket-prices.worker.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/scripts/polymarket-prices.worker.index.md
    │   │       │               │   ├── relink.system.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/scripts/relink.system.link.index.md
    │   │       │               │   └── relink.system.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/scripts/relink.system.link.meta.json
    │   │       │               ├── strategy-1-agent/
    │   │       │               │   ├── .claude/
    │   │       │               │   │   ├── agent-memory/
    │   │       │               │   │   │   └── [subagent-name]/
    │   │       │               │   │   │       ├── MEMORY.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/agent-memory/[subagent-name]/MEMORY.index.md
    │   │       │               │   │   │       └── MEMORY.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/agent-memory/[subagent-name]/MEMORY.meta.json
    │   │       │               │   │   ├── agents/
    │   │       │               │   │   │   ├── [subagent-name].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/agents/[subagent-name].index.md
    │   │       │               │   │   │   ├── [subagent-name].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/agents/[subagent-name].meta.json
    │   │       │               │   │   │   ├── pm-strategy-1-self-improvement-agent.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/agents/pm-strategy-1-self-improvement-agent.index.md
    │   │       │               │   │   │   └── pm-strategy-1-self-improvement-agent.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/agents/pm-strategy-1-self-improvement-agent.meta.json
    │   │       │               │   │   ├── commands/
    │   │       │               │   │   │   ├── [command-name].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/commands/[command-name].index.md
    │   │       │               │   │   │   └── [command-name].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/commands/[command-name].meta.json
    │   │       │               │   │   ├── output-styles/
    │   │       │               │   │   │   ├── [style-name].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/output-styles/[style-name].index.md
    │   │       │               │   │   │   └── [style-name].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/output-styles/[style-name].meta.json
    │   │       │               │   │   ├── rules/
    │   │       │               │   │   │   ├── [topic].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/rules/[topic].index.md
    │   │       │               │   │   │   └── [topic].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/rules/[topic].meta.json
    │   │       │               │   │   ├── skills/
    │   │       │               │   │   │   └── [skill-name]/
    │   │       │               │   │   │       ├── SKILL.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/skills/[skill-name]/SKILL.index.md
    │   │       │               │   │   │       └── SKILL.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/skills/[skill-name]/SKILL.meta.json
    │   │       │               │   │   ├── workflows/
    │   │       │               │   │   │   ├── [workflow-name].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/workflows/[workflow-name].index.md
    │   │       │               │   │   │   └── [workflow-name].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/workflows/[workflow-name].meta.json
    │   │       │               │   │   ├── CLAUDE.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/CLAUDE.index.md
    │   │       │               │   │   ├── CLAUDE.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/CLAUDE.meta.json
    │   │       │               │   │   ├── settings.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/settings.index.md
    │   │       │               │   │   ├── settings.local.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/settings.local.index.md
    │   │       │               │   │   ├── settings.local.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/settings.local.meta.json
    │   │       │               │   │   └── settings.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/settings.meta.json
    │   │       │               │   ├── configs/
    │   │       │               │   │   ├── strategy-1-agent.links.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/configs/strategy-1-agent.links.index.md
    │   │       │               │   │   ├── strategy-1-agent.links.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/configs/strategy-1-agent.links.meta.json
    │   │       │               │   │   ├── strategy-1-agent.workers.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/configs/strategy-1-agent.workers.index.md
    │   │       │               │   │   └── strategy-1-agent.workers.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/configs/strategy-1-agent.workers.meta.json
    │   │       │               │   ├── docs/
    │   │       │               │   │   ├── README.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/docs/README.index.md
    │   │       │               │   │   ├── README.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/docs/README.meta.json
    │   │       │               │   │   ├── rebuild-prompt.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/docs/rebuild-prompt.index.md
    │   │       │               │   │   ├── rebuild-prompt.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/docs/rebuild-prompt.meta.json
    │   │       │               │   │   ├── vision.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/docs/vision.index.md
    │   │       │               │   │   └── vision.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/docs/vision.meta.json
    │   │       │               │   ├── pm-strategy-1.momentum-v1.opus55-test/
    │   │       │               │   │   ├── .claude/
    │   │       │               │   │   │   ├── agent-memory/
    │   │       │               │   │   │   │   └── [subagent-name]/
    │   │       │               │   │   │   │       ├── MEMORY.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/agent-memory/[subagent-name]/MEMORY.index.md
    │   │       │               │   │   │   │       └── MEMORY.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/agent-memory/[subagent-name]/MEMORY.meta.json
    │   │       │               │   │   │   ├── agents/
    │   │       │               │   │   │   │   ├── [subagent-name].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/agents/[subagent-name].index.md
    │   │       │               │   │   │   │   └── [subagent-name].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/agents/[subagent-name].meta.json
    │   │       │               │   │   │   ├── commands/
    │   │       │               │   │   │   │   ├── [command-name].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/commands/[command-name].index.md
    │   │       │               │   │   │   │   └── [command-name].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/commands/[command-name].meta.json
    │   │       │               │   │   │   ├── output-styles/
    │   │       │               │   │   │   │   ├── [style-name].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/output-styles/[style-name].index.md
    │   │       │               │   │   │   │   └── [style-name].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/output-styles/[style-name].meta.json
    │   │       │               │   │   │   ├── rules/
    │   │       │               │   │   │   │   ├── [topic].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/rules/[topic].index.md
    │   │       │               │   │   │   │   └── [topic].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/rules/[topic].meta.json
    │   │       │               │   │   │   ├── skills/
    │   │       │               │   │   │   │   └── [skill-name]/
    │   │       │               │   │   │   │       ├── SKILL.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/skills/[skill-name]/SKILL.index.md
    │   │       │               │   │   │   │       └── SKILL.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/skills/[skill-name]/SKILL.meta.json
    │   │       │               │   │   │   ├── workflows/
    │   │       │               │   │   │   │   ├── [workflow-name].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/workflows/[workflow-name].index.md
    │   │       │               │   │   │   │   └── [workflow-name].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/workflows/[workflow-name].meta.json
    │   │       │               │   │   │   ├── CLAUDE.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/CLAUDE.index.md
    │   │       │               │   │   │   ├── CLAUDE.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/CLAUDE.meta.json
    │   │       │               │   │   │   ├── settings.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/settings.index.md
    │   │       │               │   │   │   ├── settings.local.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/settings.local.index.md
    │   │       │               │   │   │   ├── settings.local.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/settings.local.meta.json
    │   │       │               │   │   │   └── settings.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/settings.meta.json
    │   │       │               │   │   ├── configs/
    │   │       │               │   │   │   ├── models.config.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/configs/models.config.link.index.md
    │   │       │               │   │   │   ├── models.config.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/configs/models.config.link.meta.json
    │   │       │               │   │   │   ├── pm-strategy-1.momentum-v1.opus55-test.config.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/configs/pm-strategy-1.momentum-v1.opus55-test.config.index.md
    │   │       │               │   │   │   ├── pm-strategy-1.momentum-v1.opus55-test.config.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/configs/pm-strategy-1.momentum-v1.opus55-test.config.meta.json
    │   │       │               │   │   │   ├── pm-strategy-1.momentum-v1.opus55-test.links.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/configs/pm-strategy-1.momentum-v1.opus55-test.links.index.md
    │   │       │               │   │   │   ├── pm-strategy-1.momentum-v1.opus55-test.links.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/configs/pm-strategy-1.momentum-v1.opus55-test.links.meta.json
    │   │       │               │   │   │   ├── pm-strategy-1.momentum-v1.opus55-test.workers.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/configs/pm-strategy-1.momentum-v1.opus55-test.workers.index.md
    │   │       │               │   │   │   ├── pm-strategy-1.momentum-v1.opus55-test.workers.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/configs/pm-strategy-1.momentum-v1.opus55-test.workers.meta.json
    │   │       │               │   │   │   ├── prediction-market-agents.config.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/configs/prediction-market-agents.config.link.index.md
    │   │       │               │   │   │   ├── system.config.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/configs/system.config.link.index.md
    │   │       │               │   │   │   └── system.config.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/configs/system.config.link.meta.json
    │   │       │               │   │   ├── data/
    │   │       │               │   │   │   ├── markets-catalog.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/data/markets-catalog.link.index.md
    │   │       │               │   │   │   ├── markets-catalog.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/data/markets-catalog.link.meta.json
    │   │       │               │   │   │   ├── news-digest.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/data/news-digest.link.index.md
    │   │       │               │   │   │   ├── news-digest.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/data/news-digest.link.meta.json
    │   │       │               │   │   │   ├── polymarket-prices.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/data/polymarket-prices.link.index.md
    │   │       │               │   │   │   └── polymarket-prices.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/data/polymarket-prices.link.meta.json
    │   │       │               │   │   ├── docs/
    │   │       │               │   │   │   ├── agent-architecture.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/docs/agent-architecture.link.index.md
    │   │       │               │   │   │   ├── agent-architecture.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/docs/agent-architecture.link.meta.json
    │   │       │               │   │   │   ├── changes.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/docs/changes.index.md
    │   │       │               │   │   │   ├── changes.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/docs/changes.meta.json
    │   │       │               │   │   │   ├── decisions.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/docs/decisions.index.md
    │   │       │               │   │   │   ├── decisions.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/docs/decisions.meta.json
    │   │       │               │   │   │   ├── notes.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/docs/notes.index.md
    │   │       │               │   │   │   ├── notes.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/docs/notes.meta.json
    │   │       │               │   │   │   ├── README.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/docs/README.index.md
    │   │       │               │   │   │   ├── README.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/docs/README.meta.json
    │   │       │               │   │   │   ├── rebuild-prompt.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/docs/rebuild-prompt.index.md
    │   │       │               │   │   │   ├── rebuild-prompt.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/docs/rebuild-prompt.meta.json
    │   │       │               │   │   │   ├── safety.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/docs/safety.link.index.md
    │   │       │               │   │   │   ├── safety.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/docs/safety.link.meta.json
    │   │       │               │   │   │   ├── strategy.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/docs/strategy.index.md
    │   │       │               │   │   │   ├── strategy.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/docs/strategy.meta.json
    │   │       │               │   │   │   ├── trading-agent-architecture.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/docs/trading-agent-architecture.link.index.md
    │   │       │               │   │   │   ├── trading-safety.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/docs/trading-safety.link.index.md
    │   │       │               │   │   │   ├── vision.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/docs/vision.index.md
    │   │       │               │   │   │   └── vision.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/docs/vision.meta.json
    │   │       │               │   │   ├── logs/
    │   │       │               │   │   │   ├── polymarket-prices.worker.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/logs/polymarket-prices.worker.link.index.md
    │   │       │               │   │   │   ├── polymarket-prices.worker.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/logs/polymarket-prices.worker.link.meta.json
    │   │       │               │   │   │   ├── run-[date].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/logs/run-[date].index.md
    │   │       │               │   │   │   ├── run-[date].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/logs/run-[date].meta.json
    │   │       │               │   │   │   ├── runs.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/logs/runs.index.md
    │   │       │               │   │   │   ├── runs.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/logs/runs.meta.json
    │   │       │               │   │   │   ├── tests.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/logs/tests.index.md
    │   │       │               │   │   │   └── tests.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/logs/tests.meta.json
    │   │       │               │   │   ├── research/
    │   │       │               │   │   │   ├── index.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/research/index.index.md
    │   │       │               │   │   │   └── index.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/research/index.meta.json
    │   │       │               │   │   ├── scripts/
    │   │       │               │   │   │   ├── clean-data.system.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/scripts/clean-data.system.index.md
    │   │       │               │   │   │   ├── clean-data.system.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/scripts/clean-data.system.meta.json
    │   │       │               │   │   │   ├── get-polymarket-data.worker.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/scripts/get-polymarket-data.worker.index.md
    │   │       │               │   │   │   ├── get-polymarket-data.worker.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/scripts/get-polymarket-data.worker.meta.json
    │   │       │               │   │   │   ├── make-buy.decision.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/scripts/make-buy.decision.index.md
    │   │       │               │   │   │   ├── make-buy.decision.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/scripts/make-buy.decision.meta.json
    │   │       │               │   │   │   ├── relink.system.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/scripts/relink.system.link.index.md
    │   │       │               │   │   │   ├── relink.system.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/scripts/relink.system.link.meta.json
    │   │       │               │   │   │   ├── risk-check.decision.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/scripts/risk-check.decision.link.index.md
    │   │       │               │   │   │   ├── risk-check.decision.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/scripts/risk-check.decision.link.meta.json
    │   │       │               │   │   │   ├── run-tests.system.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/scripts/run-tests.system.link.index.md
    │   │       │               │   │   │   └── run-tests.system.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/scripts/run-tests.system.link.meta.json
    │   │       │               │   │   ├── tests/
    │   │       │               │   │   │   ├── agents/
    │   │       │               │   │   │   │   ├── [test-id].test.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/tests/agents/[test-id].test.index.md
    │   │       │               │   │   │   │   ├── [test-id].test.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/tests/agents/[test-id].test.meta.json
    │   │       │               │   │   │   │   ├── run-tests.system.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/tests/agents/run-tests.system.link.index.md
    │   │       │               │   │   │   │   ├── run-tests.system.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/tests/agents/run-tests.system.link.meta.json
    │   │       │               │   │   │   │   ├── tests.config.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/tests/agents/tests.config.index.md
    │   │       │               │   │   │   │   └── tests.config.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/tests/agents/tests.config.meta.json
    │   │       │               │   │   │   └── scripts/
    │   │       │               │   │   │       ├── [test-id].test.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/tests/scripts/[test-id].test.index.md
    │   │       │               │   │   │       ├── [test-id].test.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/tests/scripts/[test-id].test.meta.json
    │   │       │               │   │   │       ├── run-tests.system.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/tests/scripts/run-tests.system.link.index.md
    │   │       │               │   │   │       ├── run-tests.system.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/tests/scripts/run-tests.system.link.meta.json
    │   │       │               │   │   │       ├── tests.config.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/tests/scripts/tests.config.index.md
    │   │       │               │   │   │       └── tests.config.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/tests/scripts/tests.config.meta.json
    │   │       │               │   │   ├── init.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/init.index.md
    │   │       │               │   │   ├── init.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/init.meta.json
    │   │       │               │   │   ├── package.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/package.index.md
    │   │       │               │   │   ├── package.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/package.meta.json
    │   │       │               │   │   ├── requirements.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/requirements.index.md
    │   │       │               │   │   ├── requirements.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/requirements.meta.json
    │   │       │               │   │   ├── start.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/start.index.md
    │   │       │               │   │   └── start.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/start.meta.json
    │   │       │               │   ├── research/
    │   │       │               │   │   ├── index.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/research/index.index.md
    │   │       │               │   │   └── index.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/research/index.meta.json
    │   │       │               │   ├── scripts/
    │   │       │               │   │   ├── relink.system.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/scripts/relink.system.link.index.md
    │   │       │               │   │   └── relink.system.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/scripts/relink.system.link.meta.json
    │   │       │               │   ├── tests/
    │   │       │               │   │   ├── agents/
    │   │       │               │   │   │   ├── [test-id].test.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/tests/agents/[test-id].test.index.md
    │   │       │               │   │   │   ├── [test-id].test.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/tests/agents/[test-id].test.meta.json
    │   │       │               │   │   │   ├── run-tests.system.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/tests/agents/run-tests.system.link.index.md
    │   │       │               │   │   │   ├── run-tests.system.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/tests/agents/run-tests.system.link.meta.json
    │   │       │               │   │   │   ├── tests.config.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/tests/agents/tests.config.index.md
    │   │       │               │   │   │   └── tests.config.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/tests/agents/tests.config.meta.json
    │   │       │               │   │   └── scripts/
    │   │       │               │   │       ├── [test-id].test.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/tests/scripts/[test-id].test.index.md
    │   │       │               │   │       ├── [test-id].test.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/tests/scripts/[test-id].test.meta.json
    │   │       │               │   │       ├── run-tests.system.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/tests/scripts/run-tests.system.link.index.md
    │   │       │               │   │       ├── run-tests.system.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/tests/scripts/run-tests.system.link.meta.json
    │   │       │               │   │       ├── tests.config.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/tests/scripts/tests.config.index.md
    │   │       │               │   │       └── tests.config.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/tests/scripts/tests.config.meta.json
    │   │       │               │   ├── init.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/init.index.md
    │   │       │               │   ├── init.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/init.meta.json
    │   │       │               │   ├── package.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/package.index.md
    │   │       │               │   ├── package.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/package.meta.json
    │   │       │               │   ├── requirements.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/requirements.index.md
    │   │       │               │   ├── requirements.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/requirements.meta.json
    │   │       │               │   ├── start.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/start.index.md
    │   │       │               │   └── start.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/start.meta.json
    │   │       │               ├── tests/
    │   │       │               │   ├── agents/
    │   │       │               │   │   ├── [test-id].test.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/tests/agents/[test-id].test.index.md
    │   │       │               │   │   ├── [test-id].test.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/tests/agents/[test-id].test.meta.json
    │   │       │               │   │   ├── run-tests.system.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/tests/agents/run-tests.system.link.index.md
    │   │       │               │   │   ├── run-tests.system.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/tests/agents/run-tests.system.link.meta.json
    │   │       │               │   │   ├── tests.config.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/tests/agents/tests.config.index.md
    │   │       │               │   │   └── tests.config.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/tests/agents/tests.config.meta.json
    │   │       │               │   └── scripts/
    │   │       │               │       ├── [test-id].test.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/tests/scripts/[test-id].test.index.md
    │   │       │               │       ├── [test-id].test.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/tests/scripts/[test-id].test.meta.json
    │   │       │               │       ├── run-tests.system.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/tests/scripts/run-tests.system.link.index.md
    │   │       │               │       ├── run-tests.system.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/tests/scripts/run-tests.system.link.meta.json
    │   │       │               │       ├── tests.config.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/tests/scripts/tests.config.index.md
    │   │       │               │       └── tests.config.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/tests/scripts/tests.config.meta.json
    │   │       │               ├── init.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/init.index.md
    │   │       │               ├── init.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/init.meta.json
    │   │       │               ├── package.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/package.index.md
    │   │       │               ├── package.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/package.meta.json
    │   │       │               ├── requirements.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/requirements.index.md
    │   │       │               ├── requirements.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/requirements.meta.json
    │   │       │               ├── start.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/start.index.md
    │   │       │               └── start.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/start.meta.json
    │   │       └── (the rest)  —  delete · 68 files (old versions; git history keeps them)
    │   ├── 2026-09-30/  —  delete · 4 files (old versions; git history keeps them)
    │   ├── 2026-10-01/  —  delete · 1 file (old versions; git history keeps them)
    │   ├── 2026-10-05/  —  delete · 10 files (old versions; git history keeps them)
    │   ├── 2026-10-06/  —  delete · 12 files (old versions; git history keeps them)
    │   ├── 2026-10-07/  —  delete · 5 files (old versions; git history keeps them)
    │   └── 2026-10-09/  —  delete · 4 files (old versions; git history keeps them)
    ├── docs/
    │   ├── common/
    │   │   ├── agent-architecture.md  —  move → apps/project-IDE/data/sources/common/agent-architecture.md
    │   │   ├── common-prompt.md  —  move → apps/project-IDE/data/sources/common/common-prompt.md
    │   │   ├── self-improvement-templates.md  —  move → apps/project-IDE/data/sources/common/self-improvement-templates.md
    │   │   └── shared-mechanics.md  —  move → apps/project-IDE/data/sources/common/shared-mechanics.md
    │   ├── how-to/
    │   │   ├── add-account-or-secret.md  —  move → agents/system/docs/how-to/add-account-or-secret.md
    │   │   ├── add-or-change-link.md  —  move → agents/system/docs/how-to/add-or-change-link.md
    │   │   ├── add-or-run-tests.md  —  move → agents/system/docs/how-to/add-or-run-tests.md
    │   │   ├── add-platform-or-model.md  —  move → agents/system/docs/how-to/add-platform-or-model.md
    │   │   ├── add-worker.md  —  move → agents/system/docs/how-to/add-worker.md
    │   │   ├── create-agent.md  —  move → agents/system/docs/how-to/create-agent.md
    │   │   ├── process-an-input.md  —  move → agents/system/docs/how-to/process-an-input.md
    │   │   ├── promote-to-live.md  —  move → agents/system/docs/how-to/promote-to-live.md
    │   │   ├── record-research.md  —  move → agents/system/docs/how-to/record-research.md
    │   │   └── stop-or-delete-agent.md  —  move → agents/system/docs/how-to/stop-or-delete-agent.md
    │   ├── index/
    │   │   ├── agents.md  —  move → apps/project-IDE/data/sources/index/agents.md
    │   │   ├── knowledge-map.json  —  delete · the build makes it at apps/project-IDE/data/knowledge-map.json
    │   │   ├── links.md  —  move → apps/project-IDE/data/sources/index/links.md
    │   │   ├── models.md  —  move → apps/project-IDE/data/sources/index/models.md
    │   │   ├── subagents.md  —  move → apps/project-IDE/data/sources/index/subagents.md
    │   │   └── workers.md  —  move → apps/project-IDE/data/sources/index/workers.md
    │   ├── inputs/
    │   │   ├── 2026-09-29-1444-repo-update-error.md  —  move → apps/project-IDE/data/inputs/2026-09-29-1444-repo-update-error.md
    │   │   ├── 2026-09-29-1445-trading-oss-repo-only.md  —  move → apps/project-IDE/data/inputs/2026-09-29-1445-trading-oss-repo-only.md
    │   │   ├── 2026-09-29-1450-setup-ok-continue.md  —  move → apps/project-IDE/data/inputs/2026-09-29-1450-setup-ok-continue.md
    │   │   ├── 2026-09-29-1452-vision-brief-v01.md  —  move → apps/project-IDE/data/inputs/2026-09-29-1452-vision-brief-v01.md
    │   │   ├── 2026-09-29-1455-folder-layout-workflow.md  —  move → apps/project-IDE/data/inputs/2026-09-29-1455-folder-layout-workflow.md
    │   │   ├── 2026-09-29-1501-detail-docs-root.md  —  move → apps/project-IDE/data/inputs/2026-09-29-1501-detail-docs-root.md
    │   │   ├── 2026-09-29-1506-add-feature-map.md  —  move → apps/project-IDE/data/inputs/2026-09-29-1506-add-feature-map.md
    │   │   ├── 2026-09-29-1509-file-tree-in-docs.md  —  move → apps/project-IDE/data/inputs/2026-09-29-1509-file-tree-in-docs.md
    │   │   ├── 2026-09-29-1514-more-docs-question.md  —  move → apps/project-IDE/data/inputs/2026-09-29-1514-more-docs-question.md
    │   │   ├── 2026-09-29-1520-docs-additions-link-naming.md  —  move → apps/project-IDE/data/inputs/2026-09-29-1520-docs-additions-link-naming.md
    │   │   ├── 2026-09-29-1528-agents-system-configs.md  —  move → apps/project-IDE/data/inputs/2026-09-29-1528-agents-system-configs.md
    │   │   ├── 2026-09-29-1537-two-config-types.md  —  move → apps/project-IDE/data/inputs/2026-09-29-1537-two-config-types.md
    │   │   ├── 2026-09-29-1545-workers-subagents-logs-data.md  —  move → apps/project-IDE/data/inputs/2026-09-29-1545-workers-subagents-logs-data.md
    │   │   ├── 2026-09-29-1607-unique-agent-names.md  —  move → apps/project-IDE/data/inputs/2026-09-29-1607-unique-agent-names.md
    │   │   ├── 2026-09-29-1616-system-as-domain.md  —  move → apps/project-IDE/data/inputs/2026-09-29-1616-system-as-domain.md
    │   │   ├── 2026-09-29-1623-docs-same-pattern.md  —  move → apps/project-IDE/data/inputs/2026-09-29-1623-docs-same-pattern.md
    │   │   ├── 2026-09-29-1630-domain-owner-si-subagents.md  —  move → apps/project-IDE/data/inputs/2026-09-29-1630-domain-owner-si-subagents.md
    │   │   ├── 2026-09-29-1649-claude-links-parent-to-child.md  —  move → apps/project-IDE/data/inputs/2026-09-29-1649-claude-links-parent-to-child.md
    │   │   ├── 2026-09-29-1656-individual-file-links.md  —  move → apps/project-IDE/data/inputs/2026-09-29-1656-individual-file-links.md
    │   │   ├── 2026-09-29-1658-no-domain-strategy-links.md  —  move → apps/project-IDE/data/inputs/2026-09-29-1658-no-domain-strategy-links.md
    │   │   ├── 2026-09-29-1703-identical-level-folders.md  —  move → apps/project-IDE/data/inputs/2026-09-29-1703-identical-level-folders.md
    │   │   ├── 2026-09-29-1706-secrets-store.md  —  move → apps/project-IDE/data/inputs/2026-09-29-1706-secrets-store.md
    │   │   ├── 2026-09-29-2025-standard-claude-layout.md  —  move → apps/project-IDE/data/inputs/2026-09-29-2025-standard-claude-layout.md
    │   │   ├── 2026-09-29-2036-tests-research-per-level.md  —  move → apps/project-IDE/data/inputs/2026-09-29-2036-tests-research-per-level.md
    │   │   ├── 2026-09-29-2044-file-tree-explorer-ui.md  —  move → apps/project-IDE/data/inputs/2026-09-29-2044-file-tree-explorer-ui.md
    │   │   ├── 2026-09-29-2059-test-runner-script.md  —  move → apps/project-IDE/data/inputs/2026-09-29-2059-test-runner-script.md
    │   │   ├── 2026-09-29-2128-remove-save-as-note.md  —  move → apps/project-IDE/data/inputs/2026-09-29-2128-remove-save-as-note.md
    │   │   ├── 2026-09-29-2130-model-effort-picker.md  —  move → apps/project-IDE/data/inputs/2026-09-29-2130-model-effort-picker.md
    │   │   ├── 2026-09-29-2132-model-dropdown-options.md  —  move → apps/project-IDE/data/inputs/2026-09-29-2132-model-dropdown-options.md
    │   │   ├── 2026-09-29-2147-sync-button-missing.md  —  move → apps/project-IDE/data/inputs/2026-09-29-2147-sync-button-missing.md
    │   │   ├── 2026-09-30-0722-tabs-per-object.md  —  move → apps/project-IDE/data/inputs/2026-09-30-0722-tabs-per-object.md
    │   │   ├── 2026-09-30-0744-tree-search-changed-tab.md  —  move → apps/project-IDE/data/inputs/2026-09-30-0744-tree-search-changed-tab.md
    │   │   ├── 2026-09-30-0752-gitignore-runtime-local.md  —  move → apps/project-IDE/data/inputs/2026-09-30-0752-gitignore-runtime-local.md
    │   │   ├── 2026-09-30-0753-editable-file-tab.md  —  move → apps/project-IDE/data/inputs/2026-09-30-0753-editable-file-tab.md
    │   │   ├── 2026-09-30-0804-env-variables-view.md  —  move → apps/project-IDE/data/inputs/2026-09-30-0804-env-variables-view.md
    │   │   ├── 2026-09-30-0812-live-env-mirror-test.md  —  move → apps/project-IDE/data/inputs/2026-09-30-0812-live-env-mirror-test.md
    │   │   ├── 2026-09-30-0812-secrets-index-auto-sync.md  —  move → apps/project-IDE/data/inputs/2026-09-30-0812-secrets-index-auto-sync.md
    │   │   ├── 2026-09-30-0814-how-it-works-storage.md  —  move → apps/project-IDE/data/inputs/2026-09-30-0814-how-it-works-storage.md
    │   │   ├── 2026-09-30-0819-changed-and-sync.md  —  move → apps/project-IDE/data/inputs/2026-09-30-0819-changed-and-sync.md
    │   │   ├── 2026-09-30-0830-folder-status-tabs.md  —  move → apps/project-IDE/data/inputs/2026-09-30-0830-folder-status-tabs.md
    │   │   ├── 2026-09-30-0832-readme-content-edit.md  —  move → apps/project-IDE/data/inputs/2026-09-30-0832-readme-content-edit.md
    │   │   ├── 2026-09-30-0837-auto-update-after-edit.md  —  move → apps/project-IDE/data/inputs/2026-09-30-0837-auto-update-after-edit.md
    │   │   ├── 2026-09-30-0839-rewrite-related-on-edit.md  —  move → apps/project-IDE/data/inputs/2026-09-30-0839-rewrite-related-on-edit.md
    │   │   ├── 2026-09-30-0852-voice-input-question.md  —  move → apps/project-IDE/data/inputs/2026-09-30-0852-voice-input-question.md
    │   │   ├── 2026-09-30-0856-voice-input-how.md  —  move → apps/project-IDE/data/inputs/2026-09-30-0856-voice-input-how.md
    │   │   ├── 2026-09-30-0905-domain-agent-tabs.md  —  move → apps/project-IDE/data/inputs/2026-09-30-0905-domain-agent-tabs.md
    │   │   ├── 2026-09-30-0919-claude-code-scheduled-jobs.md  —  move → apps/project-IDE/data/inputs/2026-09-30-0919-claude-code-scheduled-jobs.md
    │   │   ├── 2026-09-30-0938-per-agent-jobs-file.md  —  move → apps/project-IDE/data/inputs/2026-09-30-0938-per-agent-jobs-file.md
    │   │   ├── 2026-09-30-1045-subagents-link-template.md  —  move → apps/project-IDE/data/inputs/2026-09-30-1045-subagents-link-template.md
    │   │   ├── 2026-09-30-1153-links-config-relink.md  —  move → apps/project-IDE/data/inputs/2026-09-30-1153-links-config-relink.md
    │   │   ├── 2026-09-30-1208-save-broken-agent-23.md  —  move → apps/project-IDE/data/inputs/2026-09-30-1208-save-broken-agent-23.md
    │   │   ├── 2026-09-30-1453-how-metadata-made.md  —  move → apps/project-IDE/data/inputs/2026-09-30-1453-how-metadata-made.md
    │   │   ├── 2026-09-30-1453-strategy-prefixed-variants.md  —  move → apps/project-IDE/data/inputs/2026-09-30-1453-strategy-prefixed-variants.md
    │   │   ├── 2026-09-30-1533-knowledge-agent-base.md  —  move → apps/project-IDE/data/inputs/2026-09-30-1533-knowledge-agent-base.md
    │   │   ├── 2026-09-30-1603-keep-in-mind-section.md  —  move → apps/project-IDE/data/inputs/2026-09-30-1603-keep-in-mind-section.md
    │   │   ├── 2026-09-30-1841-qa-is-knowledge.md  —  move → apps/project-IDE/data/inputs/2026-09-30-1841-qa-is-knowledge.md
    │   │   ├── 2026-10-01-0800-human-docs-like-a-book.md  —  move → apps/project-IDE/data/inputs/2026-10-01-0800-human-docs-like-a-book.md
    │   │   ├── 2026-10-01-0845-claude-folder-docs-and-skills.md  —  move → apps/project-IDE/data/inputs/2026-10-01-0845-claude-folder-docs-and-skills.md
    │   │   ├── 2026-10-01-0853-new-agent-not-in-file-tree.md  —  move → apps/project-IDE/data/inputs/2026-10-01-0853-new-agent-not-in-file-tree.md
    │   │   ├── 2026-10-01-0908-vision-no-references-no-history.md  —  move → apps/project-IDE/data/inputs/2026-10-01-0908-vision-no-references-no-history.md
    │   │   ├── 2026-10-01-1037-vision-comments-and-answers.md  —  move → apps/project-IDE/data/inputs/2026-10-01-1037-vision-comments-and-answers.md
    │   │   ├── 2026-10-05-0710-file-page-example-and-how-it-works.md  —  move → apps/project-IDE/data/inputs/2026-10-05-0710-file-page-example-and-how-it-works.md
    │   │   ├── 2026-10-05-0735-readme-same-way.md  —  move → apps/project-IDE/data/inputs/2026-10-05-0735-readme-same-way.md
    │   │   ├── 2026-10-05-0908-md-read-view.md  —  move → apps/project-IDE/data/inputs/2026-10-05-0908-md-read-view.md
    │   │   ├── 2026-10-05-0925-github-sync-index-files.md  —  move → apps/project-IDE/data/inputs/2026-10-05-0925-github-sync-index-files.md
    │   │   ├── 2026-10-05-1024-index-next-to-drafts.md  —  move → apps/project-IDE/data/inputs/2026-10-05-1024-index-next-to-drafts.md
    │   │   ├── 2026-10-05-1041-repo-layout-ide.md  —  move → apps/project-IDE/data/inputs/2026-10-05-1041-repo-layout-ide.md
    │   │   ├── 2026-10-05-1043-repo-layout-project-ide.md  —  move → apps/project-IDE/data/inputs/2026-10-05-1043-repo-layout-project-ide.md
    │   │   ├── 2026-10-05-1254-update-tree-to-repo-layout.md  —  move → apps/project-IDE/data/inputs/2026-10-05-1254-update-tree-to-repo-layout.md
    │   │   ├── 2026-10-05-1403-index-files-in-tree-and-knowledge-flow.md  —  move → apps/project-IDE/data/inputs/2026-10-05-1403-index-files-in-tree-and-knowledge-flow.md
    │   │   ├── 2026-10-05-1421-page-files-shown-empty.md  —  move → apps/project-IDE/data/inputs/2026-10-05-1421-page-files-shown-empty.md
    │   │   ├── 2026-10-05-1433-page-on-another-server-and-page-notes.md  —  move → apps/project-IDE/data/inputs/2026-10-05-1433-page-on-another-server-and-page-notes.md
    │   │   ├── 2026-10-05-1452-server-page-with-claude-code-agent.md  —  move → apps/project-IDE/data/inputs/2026-10-05-1452-server-page-with-claude-code-agent.md
    │   │   ├── 2026-10-05-1517-ide-into-apps-server-code-run-from-system.md  —  move → apps/project-IDE/data/inputs/2026-10-05-1517-ide-into-apps-server-code-run-from-system.md
    │   │   ├── 2026-10-05-1545-delete-button-and-changed-status.md  —  move → apps/project-IDE/data/inputs/2026-10-05-1545-delete-button-and-changed-status.md
    │   │   ├── 2026-10-06-1007-delete-researches.md  —  move → apps/project-IDE/data/inputs/2026-10-06-1007-delete-researches.md
    │   │   ├── 2026-10-06-1009-delete-apps-example-repo-trading-ui.md  —  move → apps/project-IDE/data/inputs/2026-10-06-1009-delete-apps-example-repo-trading-ui.md
    │   │   ├── 2026-10-06-1011-delete-name-index-pattern.md  —  move → apps/project-IDE/data/inputs/2026-10-06-1011-delete-name-index-pattern.md
    │   │   ├── 2026-10-06-1013-delete-no-root-claude-md.md  —  move → apps/project-IDE/data/inputs/2026-10-06-1013-delete-no-root-claude-md.md
    │   │   ├── 2026-10-06-1016-delete-system-subagent-pattern.md  —  move → apps/project-IDE/data/inputs/2026-10-06-1016-delete-system-subagent-pattern.md
    │   │   ├── 2026-10-06-1017-apply-changes-button.md  —  move → apps/project-IDE/data/inputs/2026-10-06-1017-apply-changes-button.md
    │   │   ├── 2026-10-06-1129-why-nested-files-hidden-without-search.md  —  move → apps/project-IDE/data/inputs/2026-10-06-1129-why-nested-files-hidden-without-search.md
    │   │   ├── 2026-10-06-1140-docs-folders-to-common-root-level.md  —  move → apps/project-IDE/data/inputs/2026-10-06-1140-docs-folders-to-common-root-level.md
    │   │   ├── 2026-10-06-1144-only-claude-docs-moves-up.md  —  move → apps/project-IDE/data/inputs/2026-10-06-1144-only-claude-docs-moves-up.md
    │   │   ├── 2026-10-06-1243-vision-vs-readme.md  —  move → apps/project-IDE/data/inputs/2026-10-06-1243-vision-vs-readme.md
    │   │   ├── 2026-10-06-1259-vision-readme-rebuild-prompt.md  —  move → apps/project-IDE/data/inputs/2026-10-06-1259-vision-readme-rebuild-prompt.md
    │   │   ├── 2026-10-06-1611-one-file-per-tab.md  —  move → apps/project-IDE/data/inputs/2026-10-06-1611-one-file-per-tab.md
    │   │   ├── 2026-10-06-1729-views-changes-json.md  —  move → apps/project-IDE/data/inputs/2026-10-06-1729-views-changes-json.md
    │   │   ├── 2026-10-06-2047-ide-full-context.md  —  move → apps/project-IDE/data/inputs/2026-10-06-2047-ide-full-context.md
    │   │   ├── 2026-10-06-2104-tests-one-job-file-set.md  —  move → apps/project-IDE/data/inputs/2026-10-06-2104-tests-one-job-file-set.md
    │   │   ├── 2026-10-06-2143-plans-features-general-system.md  —  move → apps/project-IDE/data/inputs/2026-10-06-2143-plans-features-general-system.md
    │   │   ├── 2026-10-06-2206-apps-docs-clones-forks.md  —  move → apps/project-IDE/data/inputs/2026-10-06-2206-apps-docs-clones-forks.md
    │   │   ├── 2026-10-07-0852-agents-rebuild-prompt.md  —  move → apps/project-IDE/data/inputs/2026-10-07-0852-agents-rebuild-prompt.md
    │   │   ├── 2026-10-07-0904-agent-os-metadata.md  —  move → apps/project-IDE/data/inputs/2026-10-07-0904-agent-os-metadata.md
    │   │   ├── 2026-10-07-1947-github-publish.md  —  move → apps/project-IDE/data/inputs/2026-10-07-1947-github-publish.md
    │   │   ├── 2026-10-09-0940-trading-folder.md  —  move → apps/project-IDE/data/inputs/2026-10-09-0940-trading-folder.md
    │   │   ├── 2026-10-09-1019-voice-input.md  —  move → apps/project-IDE/data/inputs/2026-10-09-1019-voice-input.md
    │   │   ├── 2026-10-09-1040-apply-jobs-off.md  —  move → apps/project-IDE/data/inputs/2026-10-09-1040-apply-jobs-off.md
    │   │   ├── 2026-10-09-1230-researches-real-tree.md  —  move → apps/project-IDE/data/inputs/2026-10-09-1230-researches-real-tree.md
    │   │   ├── 2026-10-09-1455-merge-pr-2.md  —  move → apps/project-IDE/data/inputs/2026-10-09-1455-merge-pr-2.md
    │   │   ├── 2026-10-09-1458-where-is-vision.md  —  move → apps/project-IDE/data/inputs/2026-10-09-1458-where-is-vision.md
    │   │   ├── 2026-10-09-1459-real-tree-always.md  —  move → apps/project-IDE/data/inputs/2026-10-09-1459-real-tree-always.md
    │   │   ├── 2026-10-09-1714-metadata-switch-real-files.md  —  move → apps/project-IDE/data/inputs/2026-10-09-1714-metadata-switch-real-files.md
    │   │   ├── 2026-10-09-1938-inputs-check-and-inputs-vision.md  —  move → apps/project-IDE/data/inputs/2026-10-09-1938-inputs-check-and-inputs-vision.md
    │   │   ├── 2026-10-09-2005-edit-in-read-view.md  —  move → apps/project-IDE/data/inputs/2026-10-09-2005-edit-in-read-view.md
    │   │   ├── 2026-10-09-2219-project-ide-on-server.md  —  move → apps/project-IDE/data/inputs/2026-10-09-2219-project-ide-on-server.md
    │   │   ├── 2026-10-12-claude-md-stage-one.md  —  move → apps/project-IDE/data/inputs/2026-10-12-claude-md-stage-one.md
    │   │   ├── 2026-10-12-metadata-on-disk.md  —  move → apps/project-IDE/data/inputs/2026-10-12-metadata-on-disk.md
    │   │   ├── 2026-10-12-planned-are-real-files.md  —  move → apps/project-IDE/data/inputs/2026-10-12-planned-are-real-files.md
    │   │   ├── 2026-10-12-pull-tree-mismatch.md  —  move → apps/project-IDE/data/inputs/2026-10-12-pull-tree-mismatch.md
    │   │   ├── 2026-10-12-secrets-in-tree.md  —  move → apps/project-IDE/data/inputs/2026-10-12-secrets-in-tree.md
    │   │   ├── 2026-10-13-disk-tree-empty-filter.md  —  move → apps/project-IDE/data/inputs/2026-10-13-disk-tree-empty-filter.md
    │   │   ├── 2026-10-13-edit-block-in-place.md  —  move → apps/project-IDE/data/inputs/2026-10-13-edit-block-in-place.md
    │   │   ├── 2026-10-13-leave-vision.md  —  move → apps/project-IDE/data/inputs/2026-10-13-leave-vision.md
    │   │   ├── 2026-10-13-planned-logic.md  —  move → apps/project-IDE/data/inputs/2026-10-13-planned-logic.md
    │   │   ├── index.json  —  replace → apps/project-IDE/data/inputs/index.json (that copy is older)
    │   │   └── README.md  —  delete · same copy already at apps/project-IDE/data/inputs/README.md
    │   ├── prediction-market-agents/
    │   │   ├── common/
    │   │   │   ├── strategy-si-templates.md  —  move → apps/project-IDE/data/sources/prediction-market/common/strategy-si-templates.md
    │   │   │   ├── trading-agent-architecture.md  —  move → apps/project-IDE/data/sources/prediction-market/common/trading-agent-architecture.md
    │   │   │   └── trading-prompt.md  —  move → apps/project-IDE/data/sources/prediction-market/common/trading-prompt.md
    │   │   ├── how-to/
    │   │   │   ├── add-trading-account.md  —  move → apps/project-IDE/data/sources/prediction-market/how-to/add-trading-account.md
    │   │   │   ├── create-strategy-or-variant.md  —  move → apps/project-IDE/data/sources/prediction-market/how-to/create-strategy-or-variant.md
    │   │   │   ├── go-live-with-money.md  —  move → apps/project-IDE/data/sources/prediction-market/how-to/go-live-with-money.md
    │   │   │   └── stop-trading-agent.md  —  move → apps/project-IDE/data/sources/prediction-market/how-to/stop-trading-agent.md
    │   │   ├── index/
    │   │   │   └── accounts.md  —  move → apps/project-IDE/data/sources/prediction-market/index/accounts.md
    │   │   ├── doc-outlines.md  —  move → apps/project-IDE/data/sources/prediction-market/doc-outlines.md
    │   │   ├── trading-architecture.md  —  move → apps/project-IDE/data/sources/prediction-market/trading-architecture.md
    │   │   ├── trading-conventions.md  —  move → apps/project-IDE/data/sources/prediction-market/trading-conventions.md
    │   │   ├── trading-data-schemas.md  —  move → apps/project-IDE/data/sources/prediction-market/trading-data-schemas.md
    │   │   ├── trading-feature-map.md  —  move → apps/project-IDE/data/sources/prediction-market/trading-feature-map.md
    │   │   ├── trading-flows.md  —  move → apps/project-IDE/data/sources/prediction-market/trading-flows.md
    │   │   ├── trading-glossary.md  —  move → apps/project-IDE/data/sources/prediction-market/trading-glossary.md
    │   │   ├── trading-metrics.md  —  move → apps/project-IDE/data/sources/prediction-market/trading-metrics.md
    │   │   ├── trading-overview.md  —  move → apps/project-IDE/data/sources/prediction-market/trading-overview.md
    │   │   ├── trading-roadmap.md  —  move → apps/project-IDE/data/sources/prediction-market/trading-roadmap.md
    │   │   ├── trading-safety.md  —  move → apps/project-IDE/data/sources/prediction-market/trading-safety.md
    │   │   └── trading-vision-notes.md  —  move → apps/project-IDE/data/sources/prediction-market/trading-vision-notes.md
    │   ├── architecture.md  —  move → apps/project-IDE/data/sources/architecture.md
    │   ├── changelog.md  —  delete · same copy already at apps/project-IDE/data/changelog.md
    │   ├── conventions.md  —  move → apps/project-IDE/data/sources/conventions.md
    │   ├── data-schemas.md  —  move → apps/project-IDE/data/sources/data-schemas.md
    │   ├── decisions.md  —  delete · same copy already at apps/project-IDE/data/decisions.md
    │   ├── feature-map.md  —  move → apps/project-IDE/data/sources/feature-map.md
    │   ├── file-tree.md  —  extract each item's number, decisions and notes into its Details file, then move → apps/project-IDE/data/sources/file-tree-notes.md
    │   ├── flows.md  —  move → apps/project-IDE/data/sources/flows.md
    │   ├── glossary.md  —  move → apps/project-IDE/data/sources/glossary.md
    │   ├── metrics.md  —  move → apps/project-IDE/data/sources/metrics.md
    │   ├── overview.md  —  move → apps/project-IDE/data/sources/overview.md
    │   ├── README.md  —  move → apps/project-IDE/data/sources/README.md
    │   ├── roadmap.md  —  move → apps/project-IDE/data/sources/roadmap.md
    │   ├── safety.md  —  move → apps/project-IDE/data/sources/safety.md
    │   └── vision.md  —  move → apps/project-IDE/data/sources/vision.md
    ├── explorer/
    │   ├── file-tree-explorer.html  —  delete · same copy already at apps/project-IDE/current-ui/file-tree-explorer.html
    │   ├── file-tree.data.json  —  delete · the build makes it at apps/project-IDE/current-ui/file-tree.data.json
    │   └── real-files.json  —  delete · the build makes it at apps/project-IDE/current-ui/real-files.json
    ├── plans/
    │   ├── 2026-10-06-2143-general-system.md  —  move → apps/project-IDE/data/plans/2026-10-06-2143-general-system.md
    │   ├── 2026-10-06-2206-apps-docs-clones-forks.md  —  move → apps/project-IDE/data/plans/2026-10-06-2206-apps-docs-clones-forks.md
    │   ├── 2026-10-07-0904-agent-os.md  —  move → apps/project-IDE/data/plans/2026-10-07-0904-agent-os.md
    │   ├── 2026-10-09-0940-trading-folder.md  —  move → apps/project-IDE/data/plans/2026-10-09-0940-trading-folder.md
    │   ├── 2026-10-09-1019-voice-input.md  —  move → apps/project-IDE/data/plans/2026-10-09-1019-voice-input.md
    │   ├── 2026-10-09-1938-inputs-vision.md  —  move → apps/project-IDE/data/plans/2026-10-09-1938-inputs-vision.md
    │   ├── 2026-10-12-claude-md-stage-one.md  —  move → apps/project-IDE/data/plans/2026-10-12-claude-md-stage-one.md
    │   ├── file-set.md  —  move → apps/project-IDE/data/plans/file-set.md
    │   ├── github-sync.md  —  move → apps/project-IDE/data/plans/github-sync.md
    │   ├── index.json  —  move → apps/project-IDE/data/plans/index.json
    │   └── server-ide.md  —  move → apps/project-IDE/data/plans/server-ide.md
    ├── server/
    │   ├── claude_bridge.py  —  delete · same copy already at apps/project-IDE/server/claude_bridge.py
    │   ├── README.md  —  delete · same copy already at apps/project-IDE/server/README.md
    │   ├── server.config.json  —  delete · same copy already at apps/project-IDE/server/server.config.json (then fix its vision/ paths)
    │   ├── server.py  —  delete · same copy already at apps/project-IDE/server/server.py
    │   └── voice.py  —  delete · same copy already at apps/project-IDE/server/voice.py
    ├── tools/
    │   ├── build_map.py  —  delete · same copy already at agents/system/.claude/skills/ide-build/scripts/build_map.py (then fix its vision/ paths)
    │   ├── check_page.js  —  delete · same copy already at agents/system/.claude/skills/ide-build/scripts/check_page.js (then fix its vision/ paths)
    │   ├── enrich.py  —  delete · same copy already at agents/system/.claude/skills/ide-build/scripts/enrich.py (then fix its vision/ paths)
    │   ├── index_files.py  —  delete · same copy already at agents/system/.claude/skills/ide-build/scripts/index_files.py (then fix its vision/ paths)
    │   ├── materialize.py  —  move → agents/system/.claude/skills/ide-build/scripts/materialize.py
    │   ├── overrides.json  —  delete · same copy already at apps/project-IDE/data/overrides.json (then fix its vision/ paths)
    │   ├── parse.py  —  delete · same copy already at agents/system/.claude/skills/ide-build/scripts/parse.py (then fix its vision/ paths)
    │   ├── README.md  —  delete · same copy already at agents/system/.claude/skills/ide-build/scripts/README.md (then fix its vision/ paths)
    │   └── tabs.py  —  delete · same copy already at agents/system/.claude/skills/ide-build/scripts/tabs.py (then fix its vision/ paths)
    ├── tree/
    │   ├── agent-os/
    │   │   ├── .secrets/
    │   │   │   ├── live/
    │   │   │   │   ├── .env.index.md  —  delete · same copy next to its item: .secrets/live/.env.index.md
    │   │   │   │   ├── .env.meta.json  —  delete · same copy next to its item: .secrets/live/.env.meta.json
    │   │   │   │   ├── live.index.md  —  delete · same copy next to its item: .secrets/live/live.index.md
    │   │   │   │   └── live.meta.json  —  delete · same copy next to its item: .secrets/live/live.meta.json
    │   │   │   ├── test/
    │   │   │   │   ├── .env.index.md  —  delete · same copy next to its item: .secrets/test/.env.index.md
    │   │   │   │   ├── .env.meta.json  —  delete · same copy next to its item: .secrets/test/.env.meta.json
    │   │   │   │   ├── test.index.md  —  delete · same copy next to its item: .secrets/test/test.index.md
    │   │   │   │   └── test.meta.json  —  delete · same copy next to its item: .secrets/test/test.meta.json
    │   │   │   ├── .secrets.index.md  —  delete · same copy next to its item: .secrets/.secrets.index.md
    │   │   │   ├── .secrets.meta.json  —  delete · same copy next to its item: .secrets/.secrets.meta.json
    │   │   │   ├── secrets.index.index.md  —  delete · same copy next to its item: .secrets/secrets.index.index.md
    │   │   │   └── secrets.index.meta.json  —  delete · same copy next to its item: .secrets/secrets.index.meta.json
    │   │   ├── agents/
    │   │   │   ├── system/
    │   │   │   │   ├── .claude/
    │   │   │   │   │   ├── agent-memory-local/
    │   │   │   │   │   │   ├── agent-memory-local.index.md  —  delete · same copy next to its item: agents/system/.claude/agent-memory-local/agent-memory-local.index.md
    │   │   │   │   │   │   └── agent-memory-local.meta.json  —  delete · same copy next to its item: agents/system/.claude/agent-memory-local/agent-memory-local.meta.json
    │   │   │   │   │   ├── agent-memory/
    │   │   │   │   │   │   ├── [subagent-name]/
    │   │   │   │   │   │   │   ├── MEMORY.index.md  —  delete · same copy next to its item: agents/system/.claude/agent-memory/[subagent-name]/MEMORY.index.md
    │   │   │   │   │   │   │   └── MEMORY.meta.json  —  delete · same copy next to its item: agents/system/.claude/agent-memory/[subagent-name]/MEMORY.meta.json
    │   │   │   │   │   │   ├── agent-memory.index.md  —  delete · same copy next to its item: agents/system/.claude/agent-memory/agent-memory.index.md
    │   │   │   │   │   │   └── agent-memory.meta.json  —  delete · same copy next to its item: agents/system/.claude/agent-memory/agent-memory.meta.json
    │   │   │   │   │   ├── agents/
    │   │   │   │   │   │   ├── sys-self-improvement-agent.index.md  —  delete · same copy next to its item: agents/system/.claude/agents/sys-self-improvement-agent.index.md
    │   │   │   │   │   │   └── sys-self-improvement-agent.meta.json  —  delete · same copy next to its item: agents/system/.claude/agents/sys-self-improvement-agent.meta.json
    │   │   │   │   │   ├── commands/
    │   │   │   │   │   │   ├── [command-name].index.md  —  delete · same copy next to its item: agents/system/.claude/commands/[command-name].index.md
    │   │   │   │   │   │   ├── [command-name].meta.json  —  delete · same copy next to its item: agents/system/.claude/commands/[command-name].meta.json
    │   │   │   │   │   │   ├── commands.index.md  —  delete · same copy next to its item: agents/system/.claude/commands/commands.index.md
    │   │   │   │   │   │   └── commands.meta.json  —  delete · same copy next to its item: agents/system/.claude/commands/commands.meta.json
    │   │   │   │   │   ├── output-styles/
    │   │   │   │   │   │   ├── [style-name].index.md  —  delete · same copy next to its item: agents/system/.claude/output-styles/[style-name].index.md
    │   │   │   │   │   │   ├── [style-name].meta.json  —  delete · same copy next to its item: agents/system/.claude/output-styles/[style-name].meta.json
    │   │   │   │   │   │   ├── output-styles.index.md  —  delete · same copy next to its item: agents/system/.claude/output-styles/output-styles.index.md
    │   │   │   │   │   │   └── output-styles.meta.json  —  delete · same copy next to its item: agents/system/.claude/output-styles/output-styles.meta.json
    │   │   │   │   │   ├── rules/
    │   │   │   │   │   │   ├── [topic].index.md  —  delete · same copy next to its item: agents/system/.claude/rules/[topic].index.md
    │   │   │   │   │   │   ├── [topic].meta.json  —  delete · same copy next to its item: agents/system/.claude/rules/[topic].meta.json
    │   │   │   │   │   │   ├── rules.index.md  —  delete · same copy next to its item: agents/system/.claude/rules/rules.index.md
    │   │   │   │   │   │   └── rules.meta.json  —  delete · same copy next to its item: agents/system/.claude/rules/rules.meta.json
    │   │   │   │   │   ├── skills/
    │   │   │   │   │   │   ├── [skill-name]/
    │   │   │   │   │   │   │   ├── SKILL.index.md  —  delete · same copy next to its item: agents/system/.claude/skills/[skill-name]/SKILL.index.md
    │   │   │   │   │   │   │   └── SKILL.meta.json  —  delete · same copy next to its item: agents/system/.claude/skills/[skill-name]/SKILL.meta.json
    │   │   │   │   │   │   └── ide-build/
    │   │   │   │   │   │       └── scripts/
    │   │   │   │   │   │           ├── build_map.index.md  —  delete · same copy next to its item: agents/system/.claude/skills/ide-build/scripts/build_map.index.md
    │   │   │   │   │   │           ├── build_map.meta.json  —  delete · same copy next to its item: agents/system/.claude/skills/ide-build/scripts/build_map.meta.json
    │   │   │   │   │   │           ├── check_page.index.md  —  delete · same copy next to its item: agents/system/.claude/skills/ide-build/scripts/check_page.index.md
    │   │   │   │   │   │           ├── check_page.meta.json  —  delete · same copy next to its item: agents/system/.claude/skills/ide-build/scripts/check_page.meta.json
    │   │   │   │   │   │           ├── enrich.index.md  —  delete · same copy next to its item: agents/system/.claude/skills/ide-build/scripts/enrich.index.md
    │   │   │   │   │   │           ├── enrich.meta.json  —  delete · same copy next to its item: agents/system/.claude/skills/ide-build/scripts/enrich.meta.json
    │   │   │   │   │   │           ├── index_files.index.md  —  delete · same copy next to its item: agents/system/.claude/skills/ide-build/scripts/index_files.index.md
    │   │   │   │   │   │           ├── index_files.meta.json  —  delete · same copy next to its item: agents/system/.claude/skills/ide-build/scripts/index_files.meta.json
    │   │   │   │   │   │           ├── parse.index.md  —  delete · same copy next to its item: agents/system/.claude/skills/ide-build/scripts/parse.index.md
    │   │   │   │   │   │           ├── parse.meta.json  —  delete · same copy next to its item: agents/system/.claude/skills/ide-build/scripts/parse.meta.json
    │   │   │   │   │   │           ├── README.index.md  —  delete · same copy next to its item: agents/system/.claude/skills/ide-build/scripts/README.index.md
    │   │   │   │   │   │           ├── README.meta.json  —  delete · same copy next to its item: agents/system/.claude/skills/ide-build/scripts/README.meta.json
    │   │   │   │   │   │           ├── scripts.index.md  —  delete · same copy next to its item: agents/system/.claude/skills/ide-build/scripts/scripts.index.md
    │   │   │   │   │   │           ├── scripts.meta.json  —  delete · same copy next to its item: agents/system/.claude/skills/ide-build/scripts/scripts.meta.json
    │   │   │   │   │   │           ├── tabs.index.md  —  delete · same copy next to its item: agents/system/.claude/skills/ide-build/scripts/tabs.index.md
    │   │   │   │   │   │           └── tabs.meta.json  —  delete · same copy next to its item: agents/system/.claude/skills/ide-build/scripts/tabs.meta.json
    │   │   │   │   │   ├── workflows/
    │   │   │   │   │   │   ├── [workflow-name].index.md  —  delete · same copy next to its item: agents/system/.claude/workflows/[workflow-name].index.md
    │   │   │   │   │   │   ├── [workflow-name].meta.json  —  delete · same copy next to its item: agents/system/.claude/workflows/[workflow-name].meta.json
    │   │   │   │   │   │   ├── workflows.index.md  —  delete · same copy next to its item: agents/system/.claude/workflows/workflows.index.md
    │   │   │   │   │   │   └── workflows.meta.json  —  delete · same copy next to its item: agents/system/.claude/workflows/workflows.meta.json
    │   │   │   │   │   ├── settings.index.md  —  delete · same copy next to its item: agents/system/.claude/settings.index.md
    │   │   │   │   │   ├── settings.local.index.md  —  delete · same copy next to its item: agents/system/.claude/settings.local.index.md
    │   │   │   │   │   ├── settings.local.meta.json  —  delete · same copy next to its item: agents/system/.claude/settings.local.meta.json
    │   │   │   │   │   └── settings.meta.json  —  delete · same copy next to its item: agents/system/.claude/settings.meta.json
    │   │   │   │   ├── configs/
    │   │   │   │   │   ├── subagents.link/
    │   │   │   │   │   │   ├── [domain-name]/
    │   │   │   │   │   │   │   ├── [domain-name].index.md  —  delete · same copy next to its item: agents/system/configs/subagents.link/[domain-name]/[domain-name].index.md
    │   │   │   │   │   │   │   └── [domain-name].meta.json  —  delete · same copy next to its item: agents/system/configs/subagents.link/[domain-name]/[domain-name].meta.json
    │   │   │   │   │   │   ├── subagents.link.index.md  —  delete · same copy next to its item: agents/system/configs/subagents.link/subagents.link.index.md
    │   │   │   │   │   │   └── subagents.link.meta.json  —  delete · same copy next to its item: agents/system/configs/subagents.link/subagents.link.meta.json
    │   │   │   │   │   ├── configs.index.md  —  delete · same copy next to its item: agents/system/configs/configs.index.md
    │   │   │   │   │   ├── configs.meta.json  —  delete · same copy next to its item: agents/system/configs/configs.meta.json
    │   │   │   │   │   ├── models.config.index.md  —  delete · same copy next to its item: agents/system/configs/models.config.index.md
    │   │   │   │   │   ├── models.config.meta.json  —  delete · same copy next to its item: agents/system/configs/models.config.meta.json
    │   │   │   │   │   ├── system.config.index.md  —  delete · same copy next to its item: agents/system/configs/system.config.index.md
    │   │   │   │   │   ├── system.config.meta.json  —  delete · same copy next to its item: agents/system/configs/system.config.meta.json
    │   │   │   │   │   ├── system.links.index.md  —  delete · same copy next to its item: agents/system/configs/system.links.index.md
    │   │   │   │   │   ├── system.links.meta.json  —  delete · same copy next to its item: agents/system/configs/system.links.meta.json
    │   │   │   │   │   ├── system.workers.index.md  —  delete · same copy next to its item: agents/system/configs/system.workers.index.md
    │   │   │   │   │   └── system.workers.meta.json  —  delete · same copy next to its item: agents/system/configs/system.workers.meta.json
    │   │   │   │   ├── data/
    │   │   │   │   │   ├── subagents.link/
    │   │   │   │   │   │   ├── [domain-name]/
    │   │   │   │   │   │   │   ├── [domain-name].index.md  —  delete · same copy next to its item: agents/system/data/subagents.link/[domain-name]/[domain-name].index.md
    │   │   │   │   │   │   │   └── [domain-name].meta.json  —  delete · same copy next to its item: agents/system/data/subagents.link/[domain-name]/[domain-name].meta.json
    │   │   │   │   │   │   ├── subagents.link.index.md  —  delete · same copy next to its item: agents/system/data/subagents.link/subagents.link.index.md
    │   │   │   │   │   │   └── subagents.link.meta.json  —  delete · same copy next to its item: agents/system/data/subagents.link/subagents.link.meta.json
    │   │   │   │   │   ├── subagents/
    │   │   │   │   │   │   └── [subagent]/
    │   │   │   │   │   │       ├── [subagent].index.md  —  delete · same copy next to its item: agents/system/data/subagents/[subagent]/[subagent].index.md
    │   │   │   │   │   │       └── [subagent].meta.json  —  delete · same copy next to its item: agents/system/data/subagents/[subagent]/[subagent].meta.json
    │   │   │   │   │   ├── system/
    │   │   │   │   │   │   ├── system.index.md  —  delete · same copy next to its item: agents/system/data/system/system.index.md
    │   │   │   │   │   │   └── system.meta.json  —  delete · same copy next to its item: agents/system/data/system/system.meta.json
    │   │   │   │   │   ├── workers/
    │   │   │   │   │   │   └── [worker]/
    │   │   │   │   │   │       ├── [worker].index.md  —  delete · same copy next to its item: agents/system/data/workers/[worker]/[worker].index.md
    │   │   │   │   │   │       └── [worker].meta.json  —  delete · same copy next to its item: agents/system/data/workers/[worker]/[worker].meta.json
    │   │   │   │   │   ├── data.index.md  —  delete · same copy next to its item: agents/system/data/data.index.md
    │   │   │   │   │   └── data.meta.json  —  delete · same copy next to its item: agents/system/data/data.meta.json
    │   │   │   │   ├── docs/
    │   │   │   │   │   ├── subagents.link/
    │   │   │   │   │   │   ├── [domain-name]/
    │   │   │   │   │   │   │   ├── [domain-name].index.md  —  delete · same copy next to its item: agents/system/docs/subagents.link/[domain-name]/[domain-name].index.md
    │   │   │   │   │   │   │   └── [domain-name].meta.json  —  delete · same copy next to its item: agents/system/docs/subagents.link/[domain-name]/[domain-name].meta.json
    │   │   │   │   │   │   ├── subagents.link.index.md  —  delete · same copy next to its item: agents/system/docs/subagents.link/subagents.link.index.md
    │   │   │   │   │   │   └── subagents.link.meta.json  —  delete · same copy next to its item: agents/system/docs/subagents.link/subagents.link.meta.json
    │   │   │   │   │   ├── docs.index.md  —  delete · same copy next to its item: agents/system/docs/docs.index.md
    │   │   │   │   │   ├── docs.meta.json  —  delete · same copy next to its item: agents/system/docs/docs.meta.json
    │   │   │   │   │   ├── README.asd.index.md  —  delete · same copy next to its item: agents/system/docs/README.asd.index.md
    │   │   │   │   │   ├── README.asd.meta.json  —  delete · same copy next to its item: agents/system/docs/README.asd.meta.json
    │   │   │   │   │   ├── README.index.md  —  delete · same copy next to its item: agents/system/docs/README.index.md
    │   │   │   │   │   ├── README.meta.json  —  delete · same copy next to its item: agents/system/docs/README.meta.json
    │   │   │   │   │   ├── rebuild-prompt.index.md  —  delete · same copy next to its item: agents/system/docs/rebuild-prompt.index.md
    │   │   │   │   │   ├── rebuild-prompt.meta.json  —  delete · same copy next to its item: agents/system/docs/rebuild-prompt.meta.json
    │   │   │   │   │   ├── vision.index.md  —  delete · same copy next to its item: agents/system/docs/vision.index.md
    │   │   │   │   │   └── vision.meta.json  —  delete · same copy next to its item: agents/system/docs/vision.meta.json
    │   │   │   │   ├── logs/
    │   │   │   │   │   ├── services/
    │   │   │   │   │   │   └── [service]/
    │   │   │   │   │   │       ├── [service].index.md  —  delete · same copy next to its item: agents/system/logs/services/[service]/[service].index.md
    │   │   │   │   │   │       └── [service].meta.json  —  delete · same copy next to its item: agents/system/logs/services/[service]/[service].meta.json
    │   │   │   │   │   ├── subagents.link/
    │   │   │   │   │   │   ├── [domain-name]/
    │   │   │   │   │   │   │   ├── [domain-name].index.md  —  delete · same copy next to its item: agents/system/logs/subagents.link/[domain-name]/[domain-name].index.md
    │   │   │   │   │   │   │   └── [domain-name].meta.json  —  delete · same copy next to its item: agents/system/logs/subagents.link/[domain-name]/[domain-name].meta.json
    │   │   │   │   │   │   ├── subagents.link.index.md  —  delete · same copy next to its item: agents/system/logs/subagents.link/subagents.link.index.md
    │   │   │   │   │   │   └── subagents.link.meta.json  —  delete · same copy next to its item: agents/system/logs/subagents.link/subagents.link.meta.json
    │   │   │   │   │   ├── subagents/
    │   │   │   │   │   │   └── [subagent]/
    │   │   │   │   │   │       ├── [subagent].index.md  —  delete · same copy next to its item: agents/system/logs/subagents/[subagent]/[subagent].index.md
    │   │   │   │   │   │       └── [subagent].meta.json  —  delete · same copy next to its item: agents/system/logs/subagents/[subagent]/[subagent].meta.json
    │   │   │   │   │   ├── system/
    │   │   │   │   │   │   ├── system.index.md  —  delete · same copy next to its item: agents/system/logs/system/system.index.md
    │   │   │   │   │   │   └── system.meta.json  —  delete · same copy next to its item: agents/system/logs/system/system.meta.json
    │   │   │   │   │   ├── workers/
    │   │   │   │   │   │   └── [worker]/
    │   │   │   │   │   │       ├── [worker].index.md  —  delete · same copy next to its item: agents/system/logs/workers/[worker]/[worker].index.md
    │   │   │   │   │   │       └── [worker].meta.json  —  delete · same copy next to its item: agents/system/logs/workers/[worker]/[worker].meta.json
    │   │   │   │   │   ├── logs.index.md  —  delete · same copy next to its item: agents/system/logs/logs.index.md
    │   │   │   │   │   └── logs.meta.json  —  delete · same copy next to its item: agents/system/logs/logs.meta.json
    │   │   │   │   ├── research/
    │   │   │   │   │   ├── [research-id]-[slug]/
    │   │   │   │   │   │   ├── [research-id]-[slug].index.md  —  delete · same copy next to its item: agents/system/research/[research-id]-[slug]/[research-id]-[slug].index.md
    │   │   │   │   │   │   └── [research-id]-[slug].meta.json  —  delete · same copy next to its item: agents/system/research/[research-id]-[slug]/[research-id]-[slug].meta.json
    │   │   │   │   │   ├── subagents.link/
    │   │   │   │   │   │   ├── [domain-name]/
    │   │   │   │   │   │   │   ├── [domain-name].index.md  —  delete · same copy next to its item: agents/system/research/subagents.link/[domain-name]/[domain-name].index.md
    │   │   │   │   │   │   │   └── [domain-name].meta.json  —  delete · same copy next to its item: agents/system/research/subagents.link/[domain-name]/[domain-name].meta.json
    │   │   │   │   │   │   ├── subagents.link.index.md  —  delete · same copy next to its item: agents/system/research/subagents.link/subagents.link.index.md
    │   │   │   │   │   │   └── subagents.link.meta.json  —  delete · same copy next to its item: agents/system/research/subagents.link/subagents.link.meta.json
    │   │   │   │   │   ├── index.index.md  —  delete · same copy next to its item: agents/system/research/index.index.md
    │   │   │   │   │   ├── index.meta.json  —  delete · same copy next to its item: agents/system/research/index.meta.json
    │   │   │   │   │   ├── research.index.md  —  delete · same copy next to its item: agents/system/research/research.index.md
    │   │   │   │   │   └── research.meta.json  —  delete · same copy next to its item: agents/system/research/research.meta.json
    │   │   │   │   ├── scripts/
    │   │   │   │   │   ├── subagents.link/
    │   │   │   │   │   │   ├── [domain-name]/
    │   │   │   │   │   │   │   ├── [domain-name].index.md  —  delete · same copy next to its item: agents/system/scripts/subagents.link/[domain-name]/[domain-name].index.md
    │   │   │   │   │   │   │   └── [domain-name].meta.json  —  delete · same copy next to its item: agents/system/scripts/subagents.link/[domain-name]/[domain-name].meta.json
    │   │   │   │   │   │   ├── subagents.link.index.md  —  delete · same copy next to its item: agents/system/scripts/subagents.link/subagents.link.index.md
    │   │   │   │   │   │   └── subagents.link.meta.json  —  delete · same copy next to its item: agents/system/scripts/subagents.link/subagents.link.meta.json
    │   │   │   │   │   ├── system/
    │   │   │   │   │   │   ├── system.index.md  —  delete · same copy next to its item: agents/system/scripts/system/system.index.md
    │   │   │   │   │   │   └── system.meta.json  —  delete · same copy next to its item: agents/system/scripts/system/system.meta.json
    │   │   │   │   │   ├── workers/
    │   │   │   │   │   │   ├── workers.index.md  —  delete · same copy next to its item: agents/system/scripts/workers/workers.index.md
    │   │   │   │   │   │   └── workers.meta.json  —  delete · same copy next to its item: agents/system/scripts/workers/workers.meta.json
    │   │   │   │   │   ├── scripts.index.md  —  delete · same copy next to its item: agents/system/scripts/scripts.index.md
    │   │   │   │   │   └── scripts.meta.json  —  delete · same copy next to its item: agents/system/scripts/scripts.meta.json
    │   │   │   │   ├── tests/
    │   │   │   │   │   ├── agents/
    │   │   │   │   │   │   ├── [test-id].test.index.md  —  delete · same copy next to its item: agents/system/tests/agents/[test-id].test.index.md
    │   │   │   │   │   │   ├── [test-id].test.meta.json  —  delete · same copy next to its item: agents/system/tests/agents/[test-id].test.meta.json
    │   │   │   │   │   │   ├── agents.index.md  —  delete · same copy next to its item: agents/system/tests/agents/agents.index.md
    │   │   │   │   │   │   ├── agents.meta.json  —  delete · same copy next to its item: agents/system/tests/agents/agents.meta.json
    │   │   │   │   │   │   ├── run-tests.system.link.index.md  —  delete · same copy next to its item: agents/system/tests/agents/run-tests.system.link.index.md
    │   │   │   │   │   │   ├── run-tests.system.link.meta.json  —  delete · same copy next to its item: agents/system/tests/agents/run-tests.system.link.meta.json
    │   │   │   │   │   │   ├── tests.config.index.md  —  delete · same copy next to its item: agents/system/tests/agents/tests.config.index.md
    │   │   │   │   │   │   └── tests.config.meta.json  —  delete · same copy next to its item: agents/system/tests/agents/tests.config.meta.json
    │   │   │   │   │   ├── scripts/
    │   │   │   │   │   │   ├── [test-id].test.index.md  —  delete · same copy next to its item: agents/system/tests/scripts/[test-id].test.index.md
    │   │   │   │   │   │   ├── [test-id].test.meta.json  —  delete · same copy next to its item: agents/system/tests/scripts/[test-id].test.meta.json
    │   │   │   │   │   │   ├── run-tests.system.link.index.md  —  delete · same copy next to its item: agents/system/tests/scripts/run-tests.system.link.index.md
    │   │   │   │   │   │   ├── run-tests.system.link.meta.json  —  delete · same copy next to its item: agents/system/tests/scripts/run-tests.system.link.meta.json
    │   │   │   │   │   │   ├── scripts.index.md  —  delete · same copy next to its item: agents/system/tests/scripts/scripts.index.md
    │   │   │   │   │   │   ├── scripts.meta.json  —  delete · same copy next to its item: agents/system/tests/scripts/scripts.meta.json
    │   │   │   │   │   │   ├── tests.config.index.md  —  delete · same copy next to its item: agents/system/tests/scripts/tests.config.index.md
    │   │   │   │   │   │   └── tests.config.meta.json  —  delete · same copy next to its item: agents/system/tests/scripts/tests.config.meta.json
    │   │   │   │   │   ├── subagents.link/
    │   │   │   │   │   │   ├── [domain-name]/
    │   │   │   │   │   │   │   ├── [domain-name].index.md  —  delete · same copy next to its item: agents/system/tests/subagents.link/[domain-name]/[domain-name].index.md
    │   │   │   │   │   │   │   └── [domain-name].meta.json  —  delete · same copy next to its item: agents/system/tests/subagents.link/[domain-name]/[domain-name].meta.json
    │   │   │   │   │   │   ├── subagents.link.index.md  —  delete · same copy next to its item: agents/system/tests/subagents.link/subagents.link.index.md
    │   │   │   │   │   │   └── subagents.link.meta.json  —  delete · same copy next to its item: agents/system/tests/subagents.link/subagents.link.meta.json
    │   │   │   │   │   ├── tests.index.md  —  delete · same copy next to its item: agents/system/tests/tests.index.md
    │   │   │   │   │   └── tests.meta.json  —  delete · same copy next to its item: agents/system/tests/tests.meta.json
    │   │   │   │   ├── CLAUDE.index.md  —  delete · same copy next to its item: agents/system/CLAUDE.index.md
    │   │   │   │   ├── CLAUDE.meta.json  —  delete · same copy next to its item: agents/system/CLAUDE.meta.json
    │   │   │   │   ├── init.index.md  —  delete · same copy next to its item: agents/system/init.index.md
    │   │   │   │   ├── init.meta.json  —  delete · same copy next to its item: agents/system/init.meta.json
    │   │   │   │   ├── package.index.md  —  delete · same copy next to its item: agents/system/package.index.md
    │   │   │   │   ├── package.meta.json  —  delete · same copy next to its item: agents/system/package.meta.json
    │   │   │   │   ├── requirements.index.md  —  delete · same copy next to its item: agents/system/requirements.index.md
    │   │   │   │   ├── requirements.meta.json  —  delete · same copy next to its item: agents/system/requirements.meta.json
    │   │   │   │   ├── start.index.md  —  delete · same copy next to its item: agents/system/start.index.md
    │   │   │   │   ├── start.meta.json  —  delete · same copy next to its item: agents/system/start.meta.json
    │   │   │   │   ├── system.index.md  —  delete · same copy next to its item: agents/system/system.index.md
    │   │   │   │   └── system.meta.json  —  delete · same copy next to its item: agents/system/system.meta.json
    │   │   │   ├── trading/
    │   │   │   │   ├── docs/
    │   │   │   │   │   ├── docs.index.md  —  delete · same copy next to its item: agents/trading/docs/docs.index.md
    │   │   │   │   │   ├── docs.meta.json  —  delete · same copy next to its item: agents/trading/docs/docs.meta.json
    │   │   │   │   │   ├── README.asd.index.md  —  delete · same copy next to its item: agents/trading/docs/README.asd.index.md
    │   │   │   │   │   ├── README.asd.meta.json  —  delete · same copy next to its item: agents/trading/docs/README.asd.meta.json
    │   │   │   │   │   ├── README.index.md  —  delete · same copy next to its item: agents/trading/docs/README.index.md
    │   │   │   │   │   ├── README.meta.json  —  delete · same copy next to its item: agents/trading/docs/README.meta.json
    │   │   │   │   │   ├── rebuild-prompt.index.md  —  delete · same copy next to its item: agents/trading/docs/rebuild-prompt.index.md
    │   │   │   │   │   ├── rebuild-prompt.meta.json  —  delete · same copy next to its item: agents/trading/docs/rebuild-prompt.meta.json
    │   │   │   │   │   ├── vision.index.md  —  delete · same copy next to its item: agents/trading/docs/vision.index.md
    │   │   │   │   │   └── vision.meta.json  —  delete · same copy next to its item: agents/trading/docs/vision.meta.json
    │   │   │   │   ├── prediction-market/
    │   │   │   │   │   ├── .claude/
    │   │   │   │   │   │   ├── agent-memory-local/
    │   │   │   │   │   │   │   ├── agent-memory-local.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/agent-memory-local/agent-memory-local.index.md
    │   │   │   │   │   │   │   └── agent-memory-local.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/agent-memory-local/agent-memory-local.meta.json
    │   │   │   │   │   │   ├── agent-memory/
    │   │   │   │   │   │   │   ├── agent-memory.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/agent-memory/agent-memory.index.md
    │   │   │   │   │   │   │   └── agent-memory.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/agent-memory/agent-memory.meta.json
    │   │   │   │   │   │   ├── agents/
    │   │   │   │   │   │   │   ├── agents.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/agents/agents.index.md
    │   │   │   │   │   │   │   └── agents.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/agents/agents.meta.json
    │   │   │   │   │   │   ├── commands/
    │   │   │   │   │   │   │   ├── commands.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/commands/commands.index.md
    │   │   │   │   │   │   │   └── commands.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/commands/commands.meta.json
    │   │   │   │   │   │   ├── output-styles/
    │   │   │   │   │   │   │   ├── output-styles.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/output-styles/output-styles.index.md
    │   │   │   │   │   │   │   └── output-styles.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/output-styles/output-styles.meta.json
    │   │   │   │   │   │   ├── rules/
    │   │   │   │   │   │   │   ├── rules.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/rules/rules.index.md
    │   │   │   │   │   │   │   └── rules.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/rules/rules.meta.json
    │   │   │   │   │   │   ├── skills/
    │   │   │   │   │   │   │   ├── skills.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/skills/skills.index.md
    │   │   │   │   │   │   │   └── skills.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/skills/skills.meta.json
    │   │   │   │   │   │   ├── workflows/
    │   │   │   │   │   │   │   ├── workflows.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/workflows/workflows.index.md
    │   │   │   │   │   │   │   └── workflows.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/workflows/workflows.meta.json
    │   │   │   │   │   │   ├── .claude.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/.claude.index.md
    │   │   │   │   │   │   └── .claude.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/.claude/.claude.meta.json
    │   │   │   │   │   ├── configs/
    │   │   │   │   │   │   ├── subagents.link/
    │   │   │   │   │   │   │   ├── [agent-name]/
    │   │   │   │   │   │   │   │   ├── [agent-name].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/configs/subagents.link/[agent-name]/[agent-name].index.md
    │   │   │   │   │   │   │   │   └── [agent-name].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/configs/subagents.link/[agent-name]/[agent-name].meta.json
    │   │   │   │   │   │   │   ├── subagents.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/configs/subagents.link/subagents.link.index.md
    │   │   │   │   │   │   │   └── subagents.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/configs/subagents.link/subagents.link.meta.json
    │   │   │   │   │   │   ├── configs.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/configs/configs.index.md
    │   │   │   │   │   │   └── configs.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/configs/configs.meta.json
    │   │   │   │   │   ├── data/
    │   │   │   │   │   │   ├── markets-catalog/
    │   │   │   │   │   │   │   ├── markets-catalog.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/data/markets-catalog/markets-catalog.index.md
    │   │   │   │   │   │   │   └── markets-catalog.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/data/markets-catalog/markets-catalog.meta.json
    │   │   │   │   │   │   ├── polymarket-prices/
    │   │   │   │   │   │   │   └── polymarket-prices.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/data/polymarket-prices/polymarket-prices.index.md
    │   │   │   │   │   │   ├── subagents.link/
    │   │   │   │   │   │   │   ├── [agent-name]/
    │   │   │   │   │   │   │   │   ├── [agent-name].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/data/subagents.link/[agent-name]/[agent-name].index.md
    │   │   │   │   │   │   │   │   └── [agent-name].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/data/subagents.link/[agent-name]/[agent-name].meta.json
    │   │   │   │   │   │   │   ├── subagents.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/data/subagents.link/subagents.link.index.md
    │   │   │   │   │   │   │   └── subagents.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/data/subagents.link/subagents.link.meta.json
    │   │   │   │   │   │   ├── data.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/data/data.index.md
    │   │   │   │   │   │   └── data.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/data/data.meta.json
    │   │   │   │   │   ├── docs/
    │   │   │   │   │   │   ├── common/
    │   │   │   │   │   │   │   └── common.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/common/common.index.md
    │   │   │   │   │   │   ├── how-to/
    │   │   │   │   │   │   │   └── how-to.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/how-to/how-to.index.md
    │   │   │   │   │   │   ├── index/
    │   │   │   │   │   │   │   └── index.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/index/index.index.md
    │   │   │   │   │   │   ├── subagents.link/
    │   │   │   │   │   │   │   ├── [agent-name]/
    │   │   │   │   │   │   │   │   ├── [agent-name].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/subagents.link/[agent-name]/[agent-name].index.md
    │   │   │   │   │   │   │   │   └── [agent-name].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/subagents.link/[agent-name]/[agent-name].meta.json
    │   │   │   │   │   │   │   ├── subagents.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/subagents.link/subagents.link.index.md
    │   │   │   │   │   │   │   └── subagents.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/subagents.link/subagents.link.meta.json
    │   │   │   │   │   │   ├── docs.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/docs.index.md
    │   │   │   │   │   │   └── docs.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/docs/docs.meta.json
    │   │   │   │   │   ├── logs/
    │   │   │   │   │   │   ├── jobs/
    │   │   │   │   │   │   │   └── [job-id]/
    │   │   │   │   │   │   │       └── [job-id].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/logs/jobs/[job-id]/[job-id].index.md
    │   │   │   │   │   │   ├── services/
    │   │   │   │   │   │   │   └── [service]/
    │   │   │   │   │   │   │       └── [service].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/logs/services/[service]/[service].index.md
    │   │   │   │   │   │   ├── subagents.link/
    │   │   │   │   │   │   │   ├── [agent-name]/
    │   │   │   │   │   │   │   │   ├── [agent-name].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/logs/subagents.link/[agent-name]/[agent-name].index.md
    │   │   │   │   │   │   │   │   └── [agent-name].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/logs/subagents.link/[agent-name]/[agent-name].meta.json
    │   │   │   │   │   │   │   ├── subagents.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/logs/subagents.link/subagents.link.index.md
    │   │   │   │   │   │   │   └── subagents.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/logs/subagents.link/subagents.link.meta.json
    │   │   │   │   │   │   ├── logs.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/logs/logs.index.md
    │   │   │   │   │   │   └── logs.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/logs/logs.meta.json
    │   │   │   │   │   ├── research/
    │   │   │   │   │   │   ├── [research-id]-[slug]/
    │   │   │   │   │   │   │   ├── [research-id]-[slug].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/research/[research-id]-[slug]/[research-id]-[slug].index.md
    │   │   │   │   │   │   │   └── [research-id]-[slug].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/research/[research-id]-[slug]/[research-id]-[slug].meta.json
    │   │   │   │   │   │   ├── subagents.link/
    │   │   │   │   │   │   │   ├── [agent-name]/
    │   │   │   │   │   │   │   │   ├── [agent-name].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/research/subagents.link/[agent-name]/[agent-name].index.md
    │   │   │   │   │   │   │   │   └── [agent-name].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/research/subagents.link/[agent-name]/[agent-name].meta.json
    │   │   │   │   │   │   │   ├── subagents.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/research/subagents.link/subagents.link.index.md
    │   │   │   │   │   │   │   └── subagents.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/research/subagents.link/subagents.link.meta.json
    │   │   │   │   │   │   ├── research.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/research/research.index.md
    │   │   │   │   │   │   └── research.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/research/research.meta.json
    │   │   │   │   │   ├── scripts/
    │   │   │   │   │   │   ├── decisions/
    │   │   │   │   │   │   │   ├── decisions.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/scripts/decisions/decisions.index.md
    │   │   │   │   │   │   │   └── decisions.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/scripts/decisions/decisions.meta.json
    │   │   │   │   │   │   ├── subagents.link/
    │   │   │   │   │   │   │   ├── [agent-name]/
    │   │   │   │   │   │   │   │   ├── [agent-name].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/scripts/subagents.link/[agent-name]/[agent-name].index.md
    │   │   │   │   │   │   │   │   └── [agent-name].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/scripts/subagents.link/[agent-name]/[agent-name].meta.json
    │   │   │   │   │   │   │   ├── subagents.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/scripts/subagents.link/subagents.link.index.md
    │   │   │   │   │   │   │   └── subagents.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/scripts/subagents.link/subagents.link.meta.json
    │   │   │   │   │   │   ├── scripts.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/scripts/scripts.index.md
    │   │   │   │   │   │   └── scripts.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/scripts/scripts.meta.json
    │   │   │   │   │   ├── strategy-1-agent/
    │   │   │   │   │   │   ├── .claude/
    │   │   │   │   │   │   │   ├── agent-memory-local/
    │   │   │   │   │   │   │   │   ├── agent-memory-local.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/agent-memory-local/agent-memory-local.index.md
    │   │   │   │   │   │   │   │   └── agent-memory-local.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/agent-memory-local/agent-memory-local.meta.json
    │   │   │   │   │   │   │   ├── agent-memory/
    │   │   │   │   │   │   │   │   ├── agent-memory.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/agent-memory/agent-memory.index.md
    │   │   │   │   │   │   │   │   └── agent-memory.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/agent-memory/agent-memory.meta.json
    │   │   │   │   │   │   │   ├── agents/
    │   │   │   │   │   │   │   │   ├── agents.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/agents/agents.index.md
    │   │   │   │   │   │   │   │   └── agents.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/agents/agents.meta.json
    │   │   │   │   │   │   │   ├── commands/
    │   │   │   │   │   │   │   │   ├── commands.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/commands/commands.index.md
    │   │   │   │   │   │   │   │   └── commands.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/commands/commands.meta.json
    │   │   │   │   │   │   │   ├── output-styles/
    │   │   │   │   │   │   │   │   ├── output-styles.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/output-styles/output-styles.index.md
    │   │   │   │   │   │   │   │   └── output-styles.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/output-styles/output-styles.meta.json
    │   │   │   │   │   │   │   ├── rules/
    │   │   │   │   │   │   │   │   ├── rules.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/rules/rules.index.md
    │   │   │   │   │   │   │   │   └── rules.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/rules/rules.meta.json
    │   │   │   │   │   │   │   ├── skills/
    │   │   │   │   │   │   │   │   ├── skills.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/skills/skills.index.md
    │   │   │   │   │   │   │   │   └── skills.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/skills/skills.meta.json
    │   │   │   │   │   │   │   ├── workflows/
    │   │   │   │   │   │   │   │   ├── workflows.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/workflows/workflows.index.md
    │   │   │   │   │   │   │   │   └── workflows.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/workflows/workflows.meta.json
    │   │   │   │   │   │   │   ├── .claude.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/.claude.index.md
    │   │   │   │   │   │   │   └── .claude.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/.claude/.claude.meta.json
    │   │   │   │   │   │   ├── configs/
    │   │   │   │   │   │   │   ├── subagents.link/
    │   │   │   │   │   │   │   │   ├── [agent-name]/
    │   │   │   │   │   │   │   │   │   ├── [agent-name].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/configs/subagents.link/[agent-name]/[agent-name].index.md
    │   │   │   │   │   │   │   │   │   └── [agent-name].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/configs/subagents.link/[agent-name]/[agent-name].meta.json
    │   │   │   │   │   │   │   │   ├── subagents.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/configs/subagents.link/subagents.link.index.md
    │   │   │   │   │   │   │   │   └── subagents.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/configs/subagents.link/subagents.link.meta.json
    │   │   │   │   │   │   │   ├── configs.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/configs/configs.index.md
    │   │   │   │   │   │   │   └── configs.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/configs/configs.meta.json
    │   │   │   │   │   │   ├── data/
    │   │   │   │   │   │   │   ├── subagents.link/
    │   │   │   │   │   │   │   │   ├── [agent-name]/
    │   │   │   │   │   │   │   │   │   ├── [agent-name].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/data/subagents.link/[agent-name]/[agent-name].index.md
    │   │   │   │   │   │   │   │   │   └── [agent-name].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/data/subagents.link/[agent-name]/[agent-name].meta.json
    │   │   │   │   │   │   │   │   ├── subagents.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/data/subagents.link/subagents.link.index.md
    │   │   │   │   │   │   │   │   └── subagents.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/data/subagents.link/subagents.link.meta.json
    │   │   │   │   │   │   │   ├── data.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/data/data.index.md
    │   │   │   │   │   │   │   └── data.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/data/data.meta.json
    │   │   │   │   │   │   ├── docs/
    │   │   │   │   │   │   │   ├── subagents.link/
    │   │   │   │   │   │   │   │   ├── [agent-name]/
    │   │   │   │   │   │   │   │   │   ├── [agent-name].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/docs/subagents.link/[agent-name]/[agent-name].index.md
    │   │   │   │   │   │   │   │   │   └── [agent-name].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/docs/subagents.link/[agent-name]/[agent-name].meta.json
    │   │   │   │   │   │   │   │   ├── subagents.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/docs/subagents.link/subagents.link.index.md
    │   │   │   │   │   │   │   │   └── subagents.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/docs/subagents.link/subagents.link.meta.json
    │   │   │   │   │   │   │   ├── docs.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/docs/docs.index.md
    │   │   │   │   │   │   │   └── docs.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/docs/docs.meta.json
    │   │   │   │   │   │   ├── logs/
    │   │   │   │   │   │   │   ├── subagents.link/
    │   │   │   │   │   │   │   │   ├── [agent-name]/
    │   │   │   │   │   │   │   │   │   ├── [agent-name].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/logs/subagents.link/[agent-name]/[agent-name].index.md
    │   │   │   │   │   │   │   │   │   └── [agent-name].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/logs/subagents.link/[agent-name]/[agent-name].meta.json
    │   │   │   │   │   │   │   │   ├── subagents.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/logs/subagents.link/subagents.link.index.md
    │   │   │   │   │   │   │   │   └── subagents.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/logs/subagents.link/subagents.link.meta.json
    │   │   │   │   │   │   │   ├── logs.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/logs/logs.index.md
    │   │   │   │   │   │   │   └── logs.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/logs/logs.meta.json
    │   │   │   │   │   │   ├── pm-strategy-1.momentum-v1.opus55-test/
    │   │   │   │   │   │   │   ├── .claude/
    │   │   │   │   │   │   │   │   ├── agent-memory-local/
    │   │   │   │   │   │   │   │   │   ├── agent-memory-local.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/agent-memory-local/agent-memory-local.index.md
    │   │   │   │   │   │   │   │   │   └── agent-memory-local.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/agent-memory-local/agent-memory-local.meta.json
    │   │   │   │   │   │   │   │   ├── agent-memory/
    │   │   │   │   │   │   │   │   │   ├── agent-memory.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/agent-memory/agent-memory.index.md
    │   │   │   │   │   │   │   │   │   └── agent-memory.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/agent-memory/agent-memory.meta.json
    │   │   │   │   │   │   │   │   ├── agents/
    │   │   │   │   │   │   │   │   │   ├── agents.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/agents/agents.index.md
    │   │   │   │   │   │   │   │   │   └── agents.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/agents/agents.meta.json
    │   │   │   │   │   │   │   │   ├── commands/
    │   │   │   │   │   │   │   │   │   ├── commands.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/commands/commands.index.md
    │   │   │   │   │   │   │   │   │   └── commands.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/commands/commands.meta.json
    │   │   │   │   │   │   │   │   ├── output-styles/
    │   │   │   │   │   │   │   │   │   ├── output-styles.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/output-styles/output-styles.index.md
    │   │   │   │   │   │   │   │   │   └── output-styles.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/output-styles/output-styles.meta.json
    │   │   │   │   │   │   │   │   ├── rules/
    │   │   │   │   │   │   │   │   │   ├── rules.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/rules/rules.index.md
    │   │   │   │   │   │   │   │   │   └── rules.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/rules/rules.meta.json
    │   │   │   │   │   │   │   │   ├── skills/
    │   │   │   │   │   │   │   │   │   ├── skills.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/skills/skills.index.md
    │   │   │   │   │   │   │   │   │   └── skills.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/skills/skills.meta.json
    │   │   │   │   │   │   │   │   ├── workflows/
    │   │   │   │   │   │   │   │   │   ├── workflows.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/workflows/workflows.index.md
    │   │   │   │   │   │   │   │   │   └── workflows.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/workflows/workflows.meta.json
    │   │   │   │   │   │   │   │   ├── .claude.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/.claude.index.md
    │   │   │   │   │   │   │   │   └── .claude.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/.claude/.claude.meta.json
    │   │   │   │   │   │   │   ├── configs/
    │   │   │   │   │   │   │   │   ├── configs.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/configs/configs.index.md
    │   │   │   │   │   │   │   │   └── configs.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/configs/configs.meta.json
    │   │   │   │   │   │   │   ├── data/
    │   │   │   │   │   │   │   │   ├── get-polymarket-data/
    │   │   │   │   │   │   │   │   │   ├── get-polymarket-data.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/data/get-polymarket-data/get-polymarket-data.index.md
    │   │   │   │   │   │   │   │   │   └── get-polymarket-data.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/data/get-polymarket-data/get-polymarket-data.meta.json
    │   │   │   │   │   │   │   │   ├── data.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/data/data.index.md
    │   │   │   │   │   │   │   │   └── data.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/data/data.meta.json
    │   │   │   │   │   │   │   ├── docs/
    │   │   │   │   │   │   │   │   ├── docs.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/docs/docs.index.md
    │   │   │   │   │   │   │   │   └── docs.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/docs/docs.meta.json
    │   │   │   │   │   │   │   ├── logs/
    │   │   │   │   │   │   │   │   ├── logs.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/logs/logs.index.md
    │   │   │   │   │   │   │   │   └── logs.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/logs/logs.meta.json
    │   │   │   │   │   │   │   ├── research/
    │   │   │   │   │   │   │   │   ├── [research-id]-[slug]/
    │   │   │   │   │   │   │   │   │   ├── [research-id]-[slug].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/research/[research-id]-[slug]/[research-id]-[slug].index.md
    │   │   │   │   │   │   │   │   │   └── [research-id]-[slug].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/research/[research-id]-[slug]/[research-id]-[slug].meta.json
    │   │   │   │   │   │   │   │   ├── research.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/research/research.index.md
    │   │   │   │   │   │   │   │   └── research.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/research/research.meta.json
    │   │   │   │   │   │   │   ├── scripts/
    │   │   │   │   │   │   │   │   ├── scripts.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/scripts/scripts.index.md
    │   │   │   │   │   │   │   │   └── scripts.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/scripts/scripts.meta.json
    │   │   │   │   │   │   │   ├── tests/
    │   │   │   │   │   │   │   │   ├── agents/
    │   │   │   │   │   │   │   │   │   ├── agents.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/tests/agents/agents.index.md
    │   │   │   │   │   │   │   │   │   └── agents.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/tests/agents/agents.meta.json
    │   │   │   │   │   │   │   │   ├── scripts/
    │   │   │   │   │   │   │   │   │   ├── scripts.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/tests/scripts/scripts.index.md
    │   │   │   │   │   │   │   │   │   └── scripts.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/tests/scripts/scripts.meta.json
    │   │   │   │   │   │   │   │   ├── tests.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/tests/tests.index.md
    │   │   │   │   │   │   │   │   └── tests.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/tests/tests.meta.json
    │   │   │   │   │   │   │   ├── pm-strategy-1.momentum-v1.opus55-test.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/pm-strategy-1.momentum-v1.opus55-test.index.md
    │   │   │   │   │   │   │   └── pm-strategy-1.momentum-v1.opus55-test.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/pm-strategy-1.momentum-v1.opus55-test.meta.json
    │   │   │   │   │   │   ├── research/
    │   │   │   │   │   │   │   ├── [research-id]-[slug]/
    │   │   │   │   │   │   │   │   ├── [research-id]-[slug].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/research/[research-id]-[slug]/[research-id]-[slug].index.md
    │   │   │   │   │   │   │   │   └── [research-id]-[slug].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/research/[research-id]-[slug]/[research-id]-[slug].meta.json
    │   │   │   │   │   │   │   ├── subagents.link/
    │   │   │   │   │   │   │   │   ├── [agent-name]/
    │   │   │   │   │   │   │   │   │   ├── [agent-name].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/research/subagents.link/[agent-name]/[agent-name].index.md
    │   │   │   │   │   │   │   │   │   └── [agent-name].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/research/subagents.link/[agent-name]/[agent-name].meta.json
    │   │   │   │   │   │   │   │   ├── subagents.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/research/subagents.link/subagents.link.index.md
    │   │   │   │   │   │   │   │   └── subagents.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/research/subagents.link/subagents.link.meta.json
    │   │   │   │   │   │   │   ├── research.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/research/research.index.md
    │   │   │   │   │   │   │   └── research.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/research/research.meta.json
    │   │   │   │   │   │   ├── scripts/
    │   │   │   │   │   │   │   ├── subagents.link/
    │   │   │   │   │   │   │   │   ├── [agent-name]/
    │   │   │   │   │   │   │   │   │   ├── [agent-name].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/scripts/subagents.link/[agent-name]/[agent-name].index.md
    │   │   │   │   │   │   │   │   │   └── [agent-name].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/scripts/subagents.link/[agent-name]/[agent-name].meta.json
    │   │   │   │   │   │   │   │   ├── subagents.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/scripts/subagents.link/subagents.link.index.md
    │   │   │   │   │   │   │   │   └── subagents.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/scripts/subagents.link/subagents.link.meta.json
    │   │   │   │   │   │   │   ├── scripts.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/scripts/scripts.index.md
    │   │   │   │   │   │   │   └── scripts.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/scripts/scripts.meta.json
    │   │   │   │   │   │   ├── tests/
    │   │   │   │   │   │   │   ├── agents/
    │   │   │   │   │   │   │   │   ├── agents.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/tests/agents/agents.index.md
    │   │   │   │   │   │   │   │   └── agents.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/tests/agents/agents.meta.json
    │   │   │   │   │   │   │   ├── scripts/
    │   │   │   │   │   │   │   │   ├── scripts.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/tests/scripts/scripts.index.md
    │   │   │   │   │   │   │   │   └── scripts.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/tests/scripts/scripts.meta.json
    │   │   │   │   │   │   │   ├── subagents.link/
    │   │   │   │   │   │   │   │   ├── [agent-name]/
    │   │   │   │   │   │   │   │   │   ├── [agent-name].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/tests/subagents.link/[agent-name]/[agent-name].index.md
    │   │   │   │   │   │   │   │   │   └── [agent-name].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/tests/subagents.link/[agent-name]/[agent-name].meta.json
    │   │   │   │   │   │   │   │   ├── subagents.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/tests/subagents.link/subagents.link.index.md
    │   │   │   │   │   │   │   │   └── subagents.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/tests/subagents.link/subagents.link.meta.json
    │   │   │   │   │   │   │   ├── tests.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/tests/tests.index.md
    │   │   │   │   │   │   │   └── tests.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/tests/tests.meta.json
    │   │   │   │   │   │   ├── strategy-1-agent.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/strategy-1-agent.index.md
    │   │   │   │   │   │   └── strategy-1-agent.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/strategy-1-agent/strategy-1-agent.meta.json
    │   │   │   │   │   ├── tests/
    │   │   │   │   │   │   ├── agents/
    │   │   │   │   │   │   │   ├── agents.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/tests/agents/agents.index.md
    │   │   │   │   │   │   │   └── agents.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/tests/agents/agents.meta.json
    │   │   │   │   │   │   ├── scripts/
    │   │   │   │   │   │   │   ├── scripts.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/tests/scripts/scripts.index.md
    │   │   │   │   │   │   │   └── scripts.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/tests/scripts/scripts.meta.json
    │   │   │   │   │   │   ├── subagents.link/
    │   │   │   │   │   │   │   ├── [agent-name]/
    │   │   │   │   │   │   │   │   ├── [agent-name].index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/tests/subagents.link/[agent-name]/[agent-name].index.md
    │   │   │   │   │   │   │   │   └── [agent-name].meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/tests/subagents.link/[agent-name]/[agent-name].meta.json
    │   │   │   │   │   │   │   ├── subagents.link.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/tests/subagents.link/subagents.link.index.md
    │   │   │   │   │   │   │   └── subagents.link.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/tests/subagents.link/subagents.link.meta.json
    │   │   │   │   │   │   ├── tests.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/tests/tests.index.md
    │   │   │   │   │   │   └── tests.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/tests/tests.meta.json
    │   │   │   │   │   ├── prediction-market.index.md  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/prediction-market.index.md
    │   │   │   │   │   └── prediction-market.meta.json  —  stage two → apps/project-IDE/data/sources/prediction-market/metadata/prediction-market.meta.json
    │   │   │   │   ├── researches/
    │   │   │   │   │   ├── prediction-market-research/
    │   │   │   │   │   │   ├── prediction-market-research.index.md  —  delete · same copy next to its item: agents/trading/researches/prediction-market-research/prediction-market-research.index.md
    │   │   │   │   │   │   └── prediction-market-research.meta.json  —  delete · same copy next to its item: agents/trading/researches/prediction-market-research/prediction-market-research.meta.json
    │   │   │   │   │   ├── self-improving-agents/
    │   │   │   │   │   │   ├── self-improving-agents.index.md  —  delete · same copy next to its item: agents/trading/researches/self-improving-agents/self-improving-agents.index.md
    │   │   │   │   │   │   └── self-improving-agents.meta.json  —  delete · same copy next to its item: agents/trading/researches/self-improving-agents/self-improving-agents.meta.json
    │   │   │   │   │   ├── trding-agents-arhiteches/
    │   │   │   │   │   │   ├── trding-agents-arhiteches.index.md  —  delete · same copy next to its item: agents/trading/researches/trding-agents-arhiteches/trding-agents-arhiteches.index.md
    │   │   │   │   │   │   └── trding-agents-arhiteches.meta.json  —  delete · same copy next to its item: agents/trading/researches/trding-agents-arhiteches/trding-agents-arhiteches.meta.json
    │   │   │   │   │   ├── researches.index.md  —  delete · same copy next to its item: agents/trading/researches/researches.index.md
    │   │   │   │   │   └── researches.meta.json  —  delete · same copy next to its item: agents/trading/researches/researches.meta.json
    │   │   │   │   ├── trading.index.md  —  delete · same copy next to its item: agents/trading/trading.index.md
    │   │   │   │   └── trading.meta.json  —  delete · same copy next to its item: agents/trading/trading.meta.json
    │   │   │   ├── agents.index.md  —  delete · same copy next to its item: agents/agents.index.md
    │   │   │   └── agents.meta.json  —  delete · same copy next to its item: agents/agents.meta.json
    │   │   ├── apps/
    │   │   │   ├── docs/
    │   │   │   │   ├── docs.index.md  —  delete · same copy next to its item: apps/docs/docs.index.md
    │   │   │   │   ├── docs.meta.json  —  delete · same copy next to its item: apps/docs/docs.meta.json
    │   │   │   │   ├── README.asd.index.md  —  delete · same copy next to its item: apps/docs/README.asd.index.md
    │   │   │   │   ├── README.asd.meta.json  —  delete · same copy next to its item: apps/docs/README.asd.meta.json
    │   │   │   │   ├── README.index.md  —  delete · same copy next to its item: apps/docs/README.index.md
    │   │   │   │   ├── README.meta.json  —  delete · same copy next to its item: apps/docs/README.meta.json
    │   │   │   │   ├── rebuild-prompt.index.md  —  delete · same copy next to its item: apps/docs/rebuild-prompt.index.md
    │   │   │   │   ├── rebuild-prompt.meta.json  —  delete · same copy next to its item: apps/docs/rebuild-prompt.meta.json
    │   │   │   │   ├── vision.index.md  —  delete · same copy next to its item: apps/docs/vision.index.md
    │   │   │   │   └── vision.meta.json  —  delete · same copy next to its item: apps/docs/vision.meta.json
    │   │   │   ├── project-IDE/
    │   │   │   │   ├── current-ui/
    │   │   │   │   │   ├── current-ui.index.md  —  delete · same copy next to its item: apps/project-IDE/current-ui/current-ui.index.md
    │   │   │   │   │   ├── current-ui.meta.json  —  delete · same copy next to its item: apps/project-IDE/current-ui/current-ui.meta.json
    │   │   │   │   │   ├── file-tree-explorer.index.md  —  delete · same copy next to its item: apps/project-IDE/current-ui/file-tree-explorer.index.md
    │   │   │   │   │   ├── file-tree-explorer.meta.json  —  delete · same copy next to its item: apps/project-IDE/current-ui/file-tree-explorer.meta.json
    │   │   │   │   │   ├── file-tree.data.index.md  —  delete · same copy next to its item: apps/project-IDE/current-ui/file-tree.data.index.md
    │   │   │   │   │   └── file-tree.data.meta.json  —  delete · same copy next to its item: apps/project-IDE/current-ui/file-tree.data.meta.json
    │   │   │   │   ├── data/
    │   │   │   │   │   ├── archive/
    │   │   │   │   │   │   ├── [date]/
    │   │   │   │   │   │   │   ├── [date].index.md  —  delete · same copy next to its item: apps/project-IDE/data/archive/[date]/[date].index.md
    │   │   │   │   │   │   │   └── [date].meta.json  —  delete · same copy next to its item: apps/project-IDE/data/archive/[date]/[date].meta.json
    │   │   │   │   │   │   ├── archive.index.md  —  delete · same copy next to its item: apps/project-IDE/data/archive/archive.index.md
    │   │   │   │   │   │   └── archive.meta.json  —  delete · same copy next to its item: apps/project-IDE/data/archive/archive.meta.json
    │   │   │   │   │   ├── inputs/
    │   │   │   │   │   │   ├── index.index.md  —  delete · same copy next to its item: apps/project-IDE/data/inputs/index.index.md
    │   │   │   │   │   │   ├── index.meta.json  —  delete · same copy next to its item: apps/project-IDE/data/inputs/index.meta.json
    │   │   │   │   │   │   ├── inputs.index.md  —  delete · same copy next to its item: apps/project-IDE/data/inputs/inputs.index.md
    │   │   │   │   │   │   ├── inputs.meta.json  —  delete · same copy next to its item: apps/project-IDE/data/inputs/inputs.meta.json
    │   │   │   │   │   │   ├── README.index.md  —  delete · same copy next to its item: apps/project-IDE/data/inputs/README.index.md
    │   │   │   │   │   │   ├── README.meta.json  —  delete · same copy next to its item: apps/project-IDE/data/inputs/README.meta.json
    │   │   │   │   │   │   ├── YYYY-MM-DD-HHMM-[topic].index.md  —  delete · same copy next to its item: apps/project-IDE/data/inputs/YYYY-MM-DD-HHMM-[topic].index.md
    │   │   │   │   │   │   └── YYYY-MM-DD-HHMM-[topic].meta.json  —  delete · same copy next to its item: apps/project-IDE/data/inputs/YYYY-MM-DD-HHMM-[topic].meta.json
    │   │   │   │   │   ├── memory/
    │   │   │   │   │   │   ├── [note].index.md  —  delete · same copy next to its item: apps/project-IDE/data/memory/[note].index.md
    │   │   │   │   │   │   ├── [note].meta.json  —  delete · same copy next to its item: apps/project-IDE/data/memory/[note].meta.json
    │   │   │   │   │   │   ├── memory.index.md  —  delete · same copy next to its item: apps/project-IDE/data/memory/memory.index.md
    │   │   │   │   │   │   └── memory.meta.json  —  delete · same copy next to its item: apps/project-IDE/data/memory/memory.meta.json
    │   │   │   │   │   ├── page-store/
    │   │   │   │   │   │   ├── page-store.index.md  —  delete · same copy next to its item: apps/project-IDE/data/page-store/page-store.index.md
    │   │   │   │   │   │   └── page-store.meta.json  —  delete · same copy next to its item: apps/project-IDE/data/page-store/page-store.meta.json
    │   │   │   │   │   ├── plans/
    │   │   │   │   │   │   ├── [plan].index.md  —  delete · same copy next to its item: apps/project-IDE/data/plans/[plan].index.md
    │   │   │   │   │   │   ├── [plan].meta.json  —  delete · same copy next to its item: apps/project-IDE/data/plans/[plan].meta.json
    │   │   │   │   │   │   ├── plans.index.md  —  delete · same copy next to its item: apps/project-IDE/data/plans/plans.index.md
    │   │   │   │   │   │   └── plans.meta.json  —  delete · same copy next to its item: apps/project-IDE/data/plans/plans.meta.json
    │   │   │   │   │   ├── sources/
    │   │   │   │   │   │   ├── [doc].index.md  —  delete · same copy next to its item: apps/project-IDE/data/sources/[doc].index.md
    │   │   │   │   │   │   ├── [doc].meta.json  —  delete · same copy next to its item: apps/project-IDE/data/sources/[doc].meta.json
    │   │   │   │   │   │   ├── sources.index.md  —  delete · same copy next to its item: apps/project-IDE/data/sources/sources.index.md
    │   │   │   │   │   │   └── sources.meta.json  —  delete · same copy next to its item: apps/project-IDE/data/sources/sources.meta.json
    │   │   │   │   │   ├── changelog.index.md  —  delete · same copy next to its item: apps/project-IDE/data/changelog.index.md
    │   │   │   │   │   ├── changelog.meta.json  —  delete · same copy next to its item: apps/project-IDE/data/changelog.meta.json
    │   │   │   │   │   ├── data.index.md  —  delete · same copy next to its item: apps/project-IDE/data/data.index.md
    │   │   │   │   │   ├── data.meta.json  —  delete · same copy next to its item: apps/project-IDE/data/data.meta.json
    │   │   │   │   │   ├── decisions.index.md  —  delete · same copy next to its item: apps/project-IDE/data/decisions.index.md
    │   │   │   │   │   ├── decisions.meta.json  —  delete · same copy next to its item: apps/project-IDE/data/decisions.meta.json
    │   │   │   │   │   ├── file-tree.index.md  —  delete · same copy next to its item: apps/project-IDE/data/file-tree.index.md
    │   │   │   │   │   ├── file-tree.meta.json  —  delete · same copy next to its item: apps/project-IDE/data/file-tree.meta.json
    │   │   │   │   │   ├── knowledge-map.index.md  —  delete · same copy next to its item: apps/project-IDE/data/knowledge-map.index.md
    │   │   │   │   │   ├── knowledge-map.meta.json  —  delete · same copy next to its item: apps/project-IDE/data/knowledge-map.meta.json
    │   │   │   │   │   ├── overrides.index.md  —  delete · same copy next to its item: apps/project-IDE/data/overrides.index.md
    │   │   │   │   │   ├── overrides.meta.json  —  delete · same copy next to its item: apps/project-IDE/data/overrides.meta.json
    │   │   │   │   │   ├── README.index.md  —  delete · same copy next to its item: apps/project-IDE/data/README.index.md
    │   │   │   │   │   └── README.meta.json  —  delete · same copy next to its item: apps/project-IDE/data/README.meta.json
    │   │   │   │   ├── docs/
    │   │   │   │   │   ├── docs.index.md  —  delete · same copy next to its item: apps/project-IDE/docs/docs.index.md
    │   │   │   │   │   ├── docs.meta.json  —  delete · same copy next to its item: apps/project-IDE/docs/docs.meta.json
    │   │   │   │   │   ├── README.asd.index.md  —  delete · same copy next to its item: apps/project-IDE/docs/README.asd.index.md
    │   │   │   │   │   ├── README.asd.meta.json  —  delete · same copy next to its item: apps/project-IDE/docs/README.asd.meta.json
    │   │   │   │   │   ├── README.index.md  —  delete · same copy next to its item: apps/project-IDE/docs/README.index.md
    │   │   │   │   │   ├── README.meta.json  —  delete · same copy next to its item: apps/project-IDE/docs/README.meta.json
    │   │   │   │   │   ├── rebuild-prompt.index.md  —  delete · same copy next to its item: apps/project-IDE/docs/rebuild-prompt.index.md
    │   │   │   │   │   ├── rebuild-prompt.meta.json  —  delete · same copy next to its item: apps/project-IDE/docs/rebuild-prompt.meta.json
    │   │   │   │   │   ├── vision.index.md  —  delete · same copy next to its item: apps/project-IDE/docs/vision.index.md
    │   │   │   │   │   └── vision.meta.json  —  delete · same copy next to its item: apps/project-IDE/docs/vision.meta.json
    │   │   │   │   ├── server/
    │   │   │   │   │   ├── claude_bridge.index.md  —  delete · same copy next to its item: apps/project-IDE/server/claude_bridge.index.md
    │   │   │   │   │   ├── claude_bridge.meta.json  —  delete · same copy next to its item: apps/project-IDE/server/claude_bridge.meta.json
    │   │   │   │   │   ├── README.index.md  —  delete · same copy next to its item: apps/project-IDE/server/README.index.md
    │   │   │   │   │   ├── README.meta.json  —  delete · same copy next to its item: apps/project-IDE/server/README.meta.json
    │   │   │   │   │   ├── server.config.index.md  —  delete · same copy next to its item: apps/project-IDE/server/server.config.index.md
    │   │   │   │   │   ├── server.config.meta.json  —  delete · same copy next to its item: apps/project-IDE/server/server.config.meta.json
    │   │   │   │   │   ├── server.index.md  —  delete · same copy next to its item: apps/project-IDE/server/server.index.md
    │   │   │   │   │   ├── server.meta.json  —  delete · same copy next to its item: apps/project-IDE/server/server.meta.json
    │   │   │   │   │   ├── server.py.index.md  —  delete · same copy next to its item: apps/project-IDE/server/server.py.index.md
    │   │   │   │   │   ├── server.py.meta.json  —  delete · same copy next to its item: apps/project-IDE/server/server.py.meta.json
    │   │   │   │   │   ├── voice.index.md  —  delete · same copy next to its item: apps/project-IDE/server/voice.index.md
    │   │   │   │   │   └── voice.meta.json  —  delete · same copy next to its item: apps/project-IDE/server/voice.meta.json
    │   │   │   │   ├── project-IDE.index.md  —  delete · same copy next to its item: apps/project-IDE/project-IDE.index.md
    │   │   │   │   └── project-IDE.meta.json  —  delete · same copy next to its item: apps/project-IDE/project-IDE.meta.json
    │   │   │   ├── temp/
    │   │   │   │   ├── temp.index.md  —  delete · same copy next to its item: apps/temp/temp.index.md
    │   │   │   │   └── temp.meta.json  —  delete · same copy next to its item: apps/temp/temp.meta.json
    │   │   │   ├── trading-ui/
    │   │   │   │   ├── trading-ui.index.md  —  delete · same copy next to its item: apps/trading-ui/trading-ui.index.md
    │   │   │   │   └── trading-ui.meta.json  —  delete · same copy next to its item: apps/trading-ui/trading-ui.meta.json
    │   │   │   ├── apps.index.md  —  delete · same copy next to its item: apps/apps.index.md
    │   │   │   └── apps.meta.json  —  delete · same copy next to its item: apps/apps.meta.json
    │   │   ├── docs/
    │   │   │   ├── docs.index.md  —  delete · same copy next to its item: docs/docs.index.md
    │   │   │   ├── docs.meta.json  —  delete · same copy next to its item: docs/docs.meta.json
    │   │   │   ├── file-tree.index.md  —  delete · same copy next to its item: docs/file-tree.index.md
    │   │   │   ├── file-tree.meta.json  —  delete · same copy next to its item: docs/file-tree.meta.json
    │   │   │   ├── README.asd.index.md  —  delete · same copy next to its item: docs/README.asd.index.md
    │   │   │   ├── README.asd.meta.json  —  delete · same copy next to its item: docs/README.asd.meta.json
    │   │   │   ├── README.index.md  —  delete · same copy next to its item: docs/README.index.md
    │   │   │   ├── README.meta.json  —  delete · same copy next to its item: docs/README.meta.json
    │   │   │   ├── rebuild-prompt.index.md  —  delete · same copy next to its item: docs/rebuild-prompt.index.md
    │   │   │   ├── rebuild-prompt.meta.json  —  delete · same copy next to its item: docs/rebuild-prompt.meta.json
    │   │   │   ├── vision.index.md  —  delete · same copy next to its item: docs/vision.index.md
    │   │   │   └── vision.meta.json  —  delete · same copy next to its item: docs/vision.meta.json
    │   │   ├── .gitignore.index.md  —  delete · same copy next to its item: .gitignore.index.md
    │   │   ├── .gitignore.meta.json  —  delete · same copy next to its item: .gitignore.meta.json
    │   │   ├── agent-os.index.md  —  delete · same copy next to its item: agent-os.index.md
    │   │   ├── agent-os.meta.json  —  delete · same copy next to its item: agent-os.meta.json
    │   │   ├── README.index.md  —  delete · same copy next to its item: README.index.md
    │   │   └── README.meta.json  —  delete · same copy next to its item: README.meta.json
    │   └── .index.lock  —  delete · lock file of the build
    ├── feature-map.md  —  delete · "Moved:" pointer, nothing in it
    ├── file-tree.data.json  —  delete · old copy of the page data
    ├── file-tree.md  —  delete · "Moved:" pointer, nothing in it
    ├── overview.md  —  delete · "Moved:" pointer, nothing in it
    └── vision.md  —  delete · "Moved:" pointer, nothing in it
```
