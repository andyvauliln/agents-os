# Vision

This vision comes only from the inputs of the owner (inputs.json). Each part names the inputs it comes from.

## The goal
Agent OS is a page and an agent that work on one state. The agent builds the page. The page shows everything that the agent and the page do, so that the owner can see, understand and direct each change. (m00, m04, m40)
The first state (m00) names the product Slide: an extension with profiles and apps (for example an Instagram Slide app), a connection to the agent, MCP from the agent to the extension, and shared storage. Agent OS is the base for it.

## Principles
1. Everything is state. The views, the functions, the files of the agent, the network, the environment and the metadata of each file and folder are in one JSON state. The page renders only from it. (m00, m06, m45, c06, c50)
2. Every call is visible and tested. Each function has its input, output, imports, tests, expected changes, docs, pseudo code and performance. After each run, the state shows what happened. (m04, c06, c10, c14, c17)
3. Each change has a version and a reason. Each save is a version. Each agent change comes with the request, the session and an explanation of how each part worked before and how it works now. (m04, m40)
4. One state view, many representations. Full State is the whole state. Each other tab is a filter or a view of the same state. With Only changes, each tab shows only what one block changed or touched. (m48, m69, c37, c48)
5. Readable for a person. Icons, time ago, "..." for long text with a preview, formatted and colored code, md as a page with themes, a viewer for each kind of file. (m21, m23, m49, m50, c03, c43)
6. Do only what the owner asks. Name each new field and tell why. (m02, m07)

## What works now (v48)
- The state, the versions, the runtime and the tracked calls.
- The state view with 12 tabs, Only changes, tags of agent runs, and the timeline.
- Agent runs as AI run notifications, with Index, Details and Steps.
- Network and environment from code (Browser and Server).
- The recorder (outside claude.ai), notes, Send to Claude.
- The device sizes, one main view at a time, the docs.

## Next
These come from inputs that are not done yet (status open or partly in inputs.json).
1. Improvements tab: what an agent run can do better, from the analysis of the runs and the collected inputs. It shows only those changes in the state view. (m69)
2. Performance: also memory and cost, for each function, flow, agent and skill. (m69, c50)
3. Network: the requests of the server, the agent and MCP, next to those of the browser. (m69)
4. Functions tab: a tree split into agent and extension, each function marked local or public. (m69)
5. Views tab: the rendered view with the tabs html, data, functions, state and requests. A Page that you can click, with a copy of the state, as the viewer does. (m20, m69)
6. Metadata and views for each file, kind of file and folder, in the state. (c50)
7. Video tab. (m69)
8. The microphone on claude.ai: the owner must choose what the page does when it is blocked (a dictation box, a clear message, or as it is). (m72, m73)
9. The Slide extension: the header with brand, connections (apps, agent, MCP, storage), model chip, notifications, apps and theme; extension.data, common_app_storage and apps. (m00)
10. Run on another server with saves: a local store for the versions, so that saves stay after a reload. (m76)

## How the work goes
1. The owner writes a request: a message, a page comment, or a note from the page (Send to Claude).
2. The agent does only that request. It changes the generator, tests the page, records the run and saves a new version.
3. The page shows the new version at once, with the run and the changes. The owner reads it in the state view and comments on the page.