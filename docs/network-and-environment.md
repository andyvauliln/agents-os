# Network and environment

## The browser
1. The state has two parts that the runtime fills: network and environment.
2. network has a group for each kind of request: html, scripts (our scripts), claude.ai (the scripts of the claude.ai artifact page, such as its database), api (the database calls), state, file code (code that the timeline downloads as text), packages, styles. Other requests go in other.
3. Each request has url, start (ms after the page opened), ms (download time), size (bytes), count, and parallel (what downloaded at the same time).
4. The state lists the requests that the page expects. Each has used_for (what the page uses it for) and expected: true. A request that is not in the list gets expected: false.
5. A request that this page load did not ask for (yet) has no values: count is 0.
6. environment has browser (name, version, system, screen, processor cores, memory, graphics card, connection and more), browser data (the storages and how much they use, also the claude.ai database: its versions and the call log of this page), browser api, document (title, elements, focus, fonts and more), window (sizes, scroll, origin and more), event listeners, timers, observers, connections, devices, permissions, subscriptions, background services and other.
   - event listeners: each element (or window, document) that has listeners, each event, how many, and who added them: the call that was running, or the page.
   - timers: the timeouts that wait, the intervals and the animation frames, with who added them.
   - observers: MutationObserver, ResizeObserver, IntersectionObserver and PerformanceObserver, with what they watch and who added them.
   - connections: the open WebSocket, EventSource and BroadcastChannel connections.
   - devices: how many cameras, microphones and speakers, the battery, gamepads, and which device APIs the browser has.
   - permissions: the state of each permission (granted, denied or prompt).
   The runtime finds listeners, timers, observers and connections because it wraps the browser functions that add them, before other code of the page runs. Code that ran before the runtime (the scripts of claude.ai) is not in these lists.
7. Each call writes network and environment into the state when it starts and when it ends. So the Changes of a block show what the block loaded and what changed around the page. expected-state-change does not check network and environment.
8. Block 1, Network, shows every request in its group: the url, the size, the time (in the version that this page loaded, now, and the difference), what downloaded in parallel, expected and used for. Click a request to see its code. A file on another address (cdnjs, Google Fonts) runs on the page, but the browser can stop the page from downloading it as text. Then the request shows why, and a link that opens the file. Environment is next to it. A yellow value is not the same as in the version that this page loaded.
9. When you save a version, it keeps network and environment as they are. The next page load shows the difference.

## The server
1. environment.server is the machine where the agent works and makes the state. The generator (gen/make_state.py) writes it each time it makes the state.
2. It has machine (os, arch, cpu_cores, memory_gb), runtimes (python, node, git), repo (the branch, and where it is pushed) and agent (its name, where it works, and the command that makes the state).
3. It has no secrets: no addresses, no keys and no paths of the user.
4. The Environment tab of the state view has two tabs: Browser (what the page finds in the browser) and Server (environment.server).
5. The network of the server, the agent and MCP is not in the state yet (see vision.md).