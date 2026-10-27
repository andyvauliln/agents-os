// Drives index.html in Chromium with Playwright, against a fake db, and checks each tracked call.
// Run: node --test tests/  (set CM_DIR to a local codemirror@5.65.16 package to work offline,
// and JSB_DIR to a local js-beautify@1.15.1 package: by default <CM_DIR>/../../jsb/package)
const test = require('node:test');
const assert = require('node:assert/strict');
const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('playwright');

const root = path.join(__dirname, '..');

function serve() {
  const server = http.createServer((req, res) => {
    const file = path.join(root, decodeURIComponent(req.url.split('?')[0]).replace(/^\/$/, '/index.html'));
    if (!file.startsWith(root) || !fs.existsSync(file)) { res.writeHead(404); return res.end(); }
    res.writeHead(200, { 'content-type': file.endsWith('.js') ? 'application/javascript' : file.endsWith('.json') ? 'application/json' : 'text/html' });
    fs.createReadStream(file).pipe(res);
  });
  return new Promise(r => server.listen(0, () => r(server)));
}

// A small stand-in for the page's db capability: commits/<id> and calls/<id> documents in memory.
function fakeDb() {
  window.__docs = {};
  const snap = (id, d) => ({ id, exists: !!d, data: () => d && JSON.parse(JSON.stringify(d)), metadata: {} });
  const doc = p => ({ id: p.split('/').pop(), path: p,
    get: async () => snap(p.split('/').pop(), window.__docs[p]),
    set: async d => { window.__docs[p] = JSON.parse(JSON.stringify(d)); } });
  const collection = c => {
    let order = null;
    const q = {
      orderBy(f) { order = f; return q; },
      async get() {
        const docs = Object.keys(window.__docs).filter(k => k.startsWith(c + '/')).map(k => window.__docs[k]);
        if (order) docs.sort((a, b) => a[order] - b[order]);
        return { docs: docs.map(d => snap('', d)), size: docs.length, empty: !docs.length };
      },
      doc: id => doc(c + '/' + id),
      onSnapshot(next) { (window.__listeners = window.__listeners || []).push(() => q.get().then(next)); return () => {}; }
    };
    return q;
  };
  window.claude = { use: async name => (name === 'db' ? { doc, collection } : null) };
}

// Fake media for the record button: a tone for the microphone, a canvas that changes color for the screen.
function fakeMedia() {
  const tone = () => { const ac = new AudioContext(), o = ac.createOscillator(), d = ac.createMediaStreamDestination(); o.connect(d); o.start(); return d.stream; };
  navigator.mediaDevices.getUserMedia = async () => tone();
  navigator.mediaDevices.getDisplayMedia = async () => {
    const c = document.createElement('canvas'), g = c.getContext('2d');
    c.width = 160; c.height = 100;
    let i = 0;
    setInterval(() => { g.fillStyle = 'hsl(' + (i++ * 20 % 360) + ',70%,50%)'; g.fillRect(0, 0, 160, 100); }, 50);
    return c.captureStream(20);
  };
}

test('page: boots from state, renders the header, runs state tests, saves and steps history', async () => {
  const server = await serve();
  const browser = await chromium.launch();
  try {
    const page = await browser.newPage();
    const errors = [];
    page.on('pageerror', e => errors.push(e.message));
    if (process.env.CM_DIR) {
      // claude.ai's page policy lets scripts load from cdnjs but not stylesheets, so stylesheets fail here too.
      await page.route('https://cdnjs.cloudflare.com/**', route => {
        if (route.request().url().endsWith('.css')) return route.abort();
        if (route.request().url().includes('/js-beautify/1.15.1/')) {
          const jsb = process.env.JSB_DIR || path.join(process.env.CM_DIR, '..', '..', 'jsb', 'package');
          return route.fulfill({ body: fs.readFileSync(path.join(jsb, 'js', 'lib', route.request().url().split('1.15.1/')[1].replace('.min.js', '.js'))), contentType: 'application/javascript' });
        }
        const f = route.request().url().split('5.65.16/')[1];
        const local = f === 'codemirror.min.js' ? 'lib/codemirror.js' : f === 'codemirror.min.css' ? 'lib/codemirror.css' : f.replace('.min.js', '.js');
        route.fulfill({ body: fs.readFileSync(path.join(process.env.CM_DIR, local)), contentType: f.endsWith('.css') ? 'text/css' : 'application/javascript' });
      });
      await page.route('https://fonts.googleapis.com/**', route => route.fulfill({ body: '' }));
    }
    await page.addInitScript(fakeDb);
    await page.addInitScript(fakeMedia);
    await page.goto(`http://localhost:${server.address().port}/`);
    await page.evaluate(() => window.agentOS.ready);

    // a saved version as the page reads it: a big state is kept gzipped (stateGz)
    const commitDoc = id => page.evaluate(async id => {
      const c = window.__docs['commits/' + id];
      if (!c || typeof c.state === 'string') return c;
      const bin = atob(c.stateGz), u = Uint8Array.from(bin, ch => ch.charCodeAt(0));
      const state = await new Response(new Blob([u]).stream().pipeThrough(new DecompressionStream('gzip'))).text();
      return Object.assign({}, c, { state, stateGz: undefined });
    }, id);

    // boot: version 1 from state.json, index-view rendered (page html and styles from the state), then header-view: only the State view button
    assert.ok(await page.evaluate(() => !!window.__docs['commits/c000001']));
    // (the state is bigger than a database document can hold: it is saved gzipped, and reads back the same)
    assert.equal(typeof (await page.evaluate(() => window.__docs['commits/c000001'].stateGz)), 'string');
    assert.equal((await commitDoc('c000001')).state, await page.evaluate(() => window.agentOS.history.commits[0].state));
    assert.equal(await page.locator('#header-view button').count(), 3);
    assert.ok(await page.isVisible('#timeline-button[aria-label="Timeline"] svg'));
    assert.ok(await page.isVisible('#docs-button[aria-label="Docs"] svg'));
    assert.ok(await page.isVisible('#state-button[aria-label="State view"] svg'));
    assert.equal(await page.isHidden('#state-view'), true);
    // every rule of the page styles in index-view html is read by the browser (a broken rule drops the rest)
    assert.ok(await page.evaluate(() => document.querySelector('#index-view style').sheet.cssRules.length) > 150);
    const boot = await page.evaluate(() => window.agentOS.calls.map(c => c.name));
    // (index-view renders header-view and recorder-view; recorder-view draws itself in its init, and after the start)
    assert.deepEqual(boot.sort(), ['extension.functions.get-state', 'extension.functions.render', 'extension.functions.render', 'extension.functions.render', 'loadState', 'local.init', 'local.init', 'local.init', 'local.refresh', 'local.refresh']);

    // outputs and performance are filled in on the functions that ran
    const init = await page.evaluate(() => window.agentOS.state.extension.views['index-view'].functions['local.init']);
    assert.equal(init.performance.count, 1);
    assert.deepEqual(init.errors, []);
    // output is what a function returned: get-state returns the JSON state, render returns nothing
    assert.deepEqual(Object.keys(init.calls['extension.functions.get-state'].output).sort(), ['functions', 'html', 'ui-data']);
    assert.deepEqual(init.calls['extension.functions.render'].output, {});
    assert.match(init.code, /^import ctx from 'ctx';\n\nasync function init\(\) \{/);
    assert.deepEqual(init.imports, { ctx: 'index.html' });

    // the tests written in the state pass, each checked against the state after it ran
    const results = await page.evaluate(() => window.agentOS.os.runTests());
    assert.ok(results.length >= 12, results.length);
    assert.deepEqual(results.filter(r => !r.ok), []);
    await page.evaluate(() => window.agentOS.os.call('extension.functions.unmount', { view_path: 'extension.views.state-view' }));
    await page.evaluate(() => window.agentOS.os.call('extension.functions.unmount', { view_path: 'extension.views.docs-view' }));
    await page.evaluate(() => window.agentOS.os.call('extension.functions.unmount', { view_path: 'extension.views.timeline-view' }));
    // (and no block chosen: the tests chose some)
    await page.evaluate(() => window.agentOS.os.call('extension.views.step-view.functions.local.close', {}));
    // (and the filter of State changes back to empty, on All: the tests changed them)
    await page.evaluate(async () => {
      const os = window.agentOS.os;
      await os.call('extension.views.step-view.functions.local.filter', { text: '' });
      await os.call('extension.views.step-view.functions.local.filter-kind', { kind: 'all' });
    });
    await page.evaluate(() => window.agentOS.os.call('extension.functions.unmount', { view_path: 'extension.views.step-view' }));

    // the record button, at the bottom right: one click records audio, two clicks record video
    const rec = () => page.evaluate(() => window.agentOS.state.extension.views['recorder-view']['ui-data']);
    const recording = mode => page.waitForFunction(m => window.agentOS.state.extension.views['recorder-view']['ui-data'].recording === m, mode);
    await page.waitForSelector('#recorder-view #rec-button[aria-label="Record"]');
    const rb = await page.locator('#rec-button').boundingBox(), vp = page.viewportSize();
    assert.ok(rb.x + rb.width > vp.width - 40 && rb.y + rb.height > vp.height - 40, 'bottom right');
    await page.click('#rec-button');
    await recording('audio');
    assert.equal(await page.getAttribute('#rec-button', 'aria-label'), 'Stop recording');
    // the timer is in the header
    await page.waitForFunction(() => { const t = document.querySelector('#header-view #rec-timer'); return !t.hidden && /^Audio \d\d:\d\d$/.test(t.textContent); });
    // select mode: a click selects the element (the page does not get it) and its path shows above it
    await page.click('#docs-button');
    await page.waitForFunction(() => window.agentOS.state.extension.views['recorder-view']['ui-data'].selected === 'extension.views.header-view › #docs-button');
    assert.equal(await page.evaluate(() => window.agentOS.state.extension.views['header-view']['ui-data'].docs_open), false);
    await page.waitForSelector('.rec-label:not([hidden])');
    assert.equal(await page.textContent('.rec-label'), 'extension.views.header-view › #docs-button');
    // a click on the button stops it: the card plays it and lists what was selected
    await page.click('#rec-button');
    await page.waitForSelector('#rec-card audio');
    assert.match(await page.textContent('#rec-card .rec-sel'), /^\d\d:\d\dextension\.views\.header-view › #docs-button$/);
    assert.equal((await rec()).result.kind, 'audio');
    assert.ok(await page.evaluate(() => document.querySelector('#rec-timer').hidden));
    assert.ok(await page.evaluate(() => document.querySelector('.rec-label').hidden));
    // the keys: Arrow Up two times records audio; Arrow Up and Arrow Down together stop it, and again record video
    await page.keyboard.press('ArrowUp');
    await page.keyboard.press('ArrowUp');
    await recording('audio');
    const upDown = async () => { await page.keyboard.down('ArrowUp'); await page.keyboard.down('ArrowDown'); await page.keyboard.up('ArrowDown'); await page.keyboard.up('ArrowUp'); };
    await upDown();
    await recording('');
    await upDown();
    await recording('video');
    await upDown();
    await recording('');
    await page.waitForSelector('#rec-card video');
    // two clicks: video
    await page.dblclick('#rec-button');
    await recording('video');
    await page.waitForFunction(() => /^Video /.test(document.querySelector('#rec-timer').textContent));
    await page.click('#rec-button');
    await recording('');
    // the close button forgets the recording
    await page.click('#rec-close');
    await page.waitForSelector('#rec-card', { state: 'detached' });
    assert.equal((await rec()).result, null);

    // the docs button lists the docs folder of the agent; a click shows a doc
    await page.click('#docs-button');
    assert.equal(await page.locator('#docs-view .doc-link').count(), 4);
    await page.click('#docs-view .doc-link:has-text("render-steps.md")');
    assert.equal(await page.textContent('#docs-view .doc h2'), 'How the page renders from the state');
    assert.equal(await page.evaluate(() => window.agentOS.state.extension.views['docs-view']['ui-data'].selected), 'render-steps.md');
    assert.ok(await page.locator('#docs-view .doc pre.code').count() >= 5);
    assert.match(await page.textContent('#docs-view .doc pre.code >> nth=1'), /^import os from 'os';\nimport ctx from 'ctx';\n\nasync function render\(\{ view_path \}\) \{/);
    await page.click('#docs-view .doc-link:has-text("how-it-works.md")');
    assert.ok(await page.isVisible('#docs-view .doc .diagram svg'));
    assert.equal(await page.locator('#docs-view .doc .diagram svg text.num').count(), 7);
    await page.click('#docs-button');
    assert.equal(await page.isHidden('#docs-view'), true);

    // the timeline: its blocks at the top of the page, above the header; nothing chosen yet
    const tl = () => page.evaluate(() => window.agentOS.state.extension.views['timeline-view']['ui-data']);
    const stv = () => page.evaluate(() => window.agentOS.state.extension.views['step-view']['ui-data']);
    const blockNames = () => page.$$eval('#tl-strip .tl-step .tl-step-name', els => els.map(x => x.textContent));
    await page.click('#timeline-button');
    await page.waitForSelector('#tl-strip .tl-step');
    assert.ok(await page.evaluate(() => document.querySelector('#timeline-view').compareDocumentPosition(document.querySelector('#header-view')) & Node.DOCUMENT_POSITION_FOLLOWING));
    const stepKinds = await page.$$eval('#tl-strip .tl-step .tl-kind', els => els.map(x => x.textContent));
    // the last agent run comes first (runs/ of the repo), then the page start
    assert.deepEqual(stepKinds.slice(0, 5), ['Agent run', 'Network', 'Run index.html', 'Load the state', 'Start the page']);
    assert.equal(await page.isHidden('#step-view'), true);
    assert.equal(await page.isChecked('#tl-track'), false);

    // the Agent run block opens on Details: the timeline of the agent, what started each part, the context, the files
    const runs = await page.evaluate(() => Object.keys(window.agentOS.state.agents['agent-oss'].files.runs).sort());
    const lastRun = await page.evaluate(n => JSON.parse(window.agentOS.state.agents['agent-oss'].files.runs[n]), runs[runs.length - 1]);
    await page.locator('#tl-strip .tl-step').first().click();
    await page.waitForSelector('#tl-detail .ar-lanes');
    assert.equal((await tl()).selected, 'run:runs/' + runs[runs.length - 1]);
    assert.equal((await stv()).tab, 'details');
    assert.equal(await page.textContent('#st-title .tl-name'), 'session ' + lastRun.session.slice(0, 8) + ' · run ' + lastRun.run);
    assert.match(await page.textContent('#tl-detail .ar-card.start'), new RegExp('Run ' + lastRun.run));
    assert.equal(await page.locator('#tl-detail .ar-card:not(.start)').count(), lastRun.steps.length);
    // a subagent has its own lane: its name, and a line that tells what it is and which steps are its own
    const subLanes = [...new Set(lastRun.steps.map(x => x.lane || 'main'))].filter(l => l !== 'main');
    assert.equal(await page.locator('#tl-detail .ar-lane.sub').count(), subLanes.length);
    if (subLanes.length) assert.match(await page.textContent('#tl-detail .ar-lane.sub .ar-branch'), new RegExp('^' + subLanes[0] + ' is a subagent'));
    // the MCP, skill, subagent and workflow uses are in the Details
    assert.deepEqual(await page.$$eval('#tl-detail .ar-why:not(.ar-info) dt', els => els.map(x => x.textContent)),
      ['What started this session', 'What started this run', 'What started this workflow', 'What started the subagents', 'What started the skills', 'MCP use', 'Skill use', 'Subagents', 'Workflow', 'Context']);
    // no step chosen: the whole run, in two tabs: Changes and Reads
    assert.match(await page.textContent('#tl-detail .ar-files .tl-detail-sub'), /^The whole run/);
    const changed = lastRun.files.filter(f => f.action !== 'read'), read = lastRun.files.filter(f => f.action === 'read');
    assert.match(await page.textContent('#tl-detail .ar-tabs [data-tab="changes"]'), /^Changes \(\d+\)$/);
    assert.equal(await page.getAttribute('#tl-detail .ar-tabs [data-tab="changes"]', 'aria-selected'), 'true');
    // the changed files are a tree of folders under Files/
    const top = changed.find(f => /^[^/]+\//.test(f.path)).path.split('/')[0];
    assert.equal(await page.locator('#tl-detail .ar-kv .kv-tree summary', { hasText: new RegExp('^' + top.replace('.', '\\.') + '/$') }).count(), 1);
    assert.ok(await page.locator('#tl-detail .ar-kv .kv-item.ar-item').count() >= new Set(changed.map(f => f.path)).size);
    // the buttons show only what the main agent, a subagent or an MCP call did
    assert.equal(await page.getAttribute('#tl-detail .ar-by [data-by="all"]', 'aria-pressed'), 'true');
    if (subLanes.length) {
      await page.click('#tl-detail .ar-by [data-by="subagent"]');
      assert.equal(await page.getAttribute('#tl-detail .ar-by [data-by="subagent"]', 'aria-pressed'), 'true');
      assert.ok((await page.$$eval('#tl-detail .ar-kv .kv-item', els => els.map(x => x.querySelector('.src') ? 1 : 0))).every(Boolean));
      await page.click('#tl-detail .ar-by [data-by="all"]');
    }
    // Reads: the files it read, and what came into its context
    await page.click('#tl-detail .ar-tabs [data-tab="reads"]');
    assert.equal(await page.getAttribute('#tl-detail .ar-tabs [data-tab="reads"]', 'aria-selected'), 'true');
    for (const f of read.slice(0, 3)) assert.ok((await page.$$eval('#tl-detail .ar-kv .kv-item', els => els.map(x => x.title))).some(t => t.startsWith(f.path)), f.path);
    // a click on an item shows why: who did it, in which steps
    await page.locator('#tl-detail .ar-kv .kv-item').first().click();
    await page.click('#tl-detail .ar-kv .kv-tabs button:has-text("Why")');
    assert.match(await page.textContent('#tl-detail .ar-kv .kv-main .ar-info'), /By.*Steps/s);
    await page.click('#tl-detail .ar-tabs [data-tab="changes"]');
    // a click on a step shows only that step: what it did, why, and its own files; a click again shows the whole run
    const k = lastRun.steps.findIndex(x => (x.files || []).filter(f => f.action !== 'read').length > 1);
    await page.click('#tl-detail .ar-card.step[data-step="' + k + '"]');
    assert.equal(await page.textContent('#tl-detail .ar-files .tl-detail-sub'), 'Step ' + (k + 1) + ': ' + lastRun.steps[k].title);
    assert.equal(await page.locator('#tl-detail .ar-card.step.on').count(), 1);
    assert.equal(await page.locator('#tl-detail .ar-items li').count(), lastRun.steps[k].items.length);
    const own = lastRun.steps[k].files.filter(f => f.action !== 'read');
    assert.deepEqual((await page.$$eval('#tl-detail .ar-kv .kv-item', els => els.map(x => x.title))).filter(t => !t.startsWith('mcp ') && / \((created|updated|deleted)\)$/.test(t)).map(t => t.replace(/ \(\w+\)$/, '')).sort(), [...new Set(own.map(f => f.path))].sort());
    await page.click('#tl-detail .ar-card.step[data-step="' + k + '"]');
    assert.match(await page.textContent('#tl-detail .ar-files .tl-detail-sub'), /^The whole run/);
    // its State changes: from the version before the run to the version it made (this page has only v1)
    await page.click('#st-tab-state');
    await page.waitForFunction(() => /The run made v\d+\./.test(document.querySelector('#tl-detail').textContent));
    await page.click('#st-close');
    await page.waitForFunction(() => document.querySelector('#step-view').hidden);

    // a click on a block shows it under the header, State changes first; with tracking off the click is not a block
    const before = await blockNames();
    await page.locator('#tl-strip .tl-step').nth(1).click();
    await page.waitForFunction(() => (document.querySelector('#step-view #st-title .tl-kind') || {}).textContent === 'Network');
    assert.equal((await tl()).selected, 'open');
    assert.equal((await stv()).tab, 'state');
    // a click on the chosen block again hides it, and so does the close button
    await page.locator('#tl-strip .tl-step').nth(1).click();
    await page.waitForFunction(() => document.querySelector('#step-view').hidden);
    assert.equal((await tl()).selected, null);
    await page.locator('#tl-strip .tl-step').nth(1).click();
    await page.waitForSelector('#step-view #st-title .tl-kind');
    await page.click('#st-close');
    await page.waitForFunction(() => document.querySelector('#step-view').hidden);
    assert.equal((await tl()).selected, null);
    await page.locator('#tl-strip .tl-step').nth(1).click();
    await page.waitForSelector('#step-view #st-title .tl-kind');
    assert.deepEqual(await blockNames(), before);
    assert.ok(await page.evaluate(() => document.querySelector('#header-view').compareDocumentPosition(document.querySelector('#step-view')) & Node.DOCUMENT_POSITION_FOLLOWING));

    // network and environment are in the state; block 1 shows what changed in them since the version this page loaded
    const st0 = await page.evaluate(() => window.agentOS.state);
    assert.equal(st0.network.scripts['state-core.js'].expected, true);
    assert.equal(typeof st0.network.scripts['state-core.js'].ms, 'number');
    assert.ok(st0.network.scripts['state-core.js'].size > 1000);
    assert.equal(st0.network.api['read the versions'].count, 1);
    assert.ok(st0.network.packages['codemirror.min.js'].count >= 1);
    assert.equal(st0.environment['browser data'].storages['local storage'].limit, 'about 5 MB (the usual limit of a browser)');
    assert.equal(typeof st0.environment.browser.viewport, 'string');
    assert.equal(st0.environment['browser data'].storages['claude.ai database']['versions (commits)'].documents, 1);
    assert.match(st0.environment['browser data'].storages['claude.ai database'].limits, /256 KB/);
    assert.equal(typeof st0.environment.browser.cpu_cores, 'number');
    assert.equal(typeof st0.environment.browser.gpu, 'string');
    // everything the code registered, with who added it
    const env0 = await page.evaluate(() => window.agentOS.state.environment);
    assert.ok(env0['event listeners']['#st-filter-input'].input.by.includes('local.init'), JSON.stringify(env0['event listeners']['#st-filter-input']));
    assert.ok(env0['event listeners'].document.keydown.count >= 1);
    assert.equal(env0.document.title, 'Agent OS');
    assert.ok(env0.document.elements > 50);
    assert.equal(typeof env0.window.history_length, 'number');
    assert.ok('timeouts waiting' in env0.timers && 'intervals' in env0.timers);
    assert.ok(Array.isArray(env0.connections));
    assert.ok('geolocation' in env0.permissions && 'battery' in env0.devices);
    // a listener added in a call is a change of that call
    await page.evaluate(() => window.agentOS.os.call('extension.views.step-view.functions.local.filter', { text: '' }));
    await page.evaluate(() => { window.__probe = () => {}; document.body.addEventListener('dblclick', window.__probe); });
    await page.evaluate(() => window.agentOS.os.call('extension.views.step-view.functions.local.filter', { text: '' }));
    assert.deepEqual(await page.evaluate(() => window.agentOS.state.environment['event listeners'].body.dblclick), { count: 1, by: ['the page (no call)'] });
    // its State changes: the same view as the other blocks, with which function changed what
    await page.waitForFunction(() => /changes? in the state, made by /.test(document.querySelector('#tl-detail').textContent));
    assert.match(await page.locator('#tl-detail .tl-code').first().evaluate(e => e.cm.getValue()), /"network"/);
    assert.match(await page.textContent('#tl-detail .tl-table'), /network\.scripts\.state-core\.js\.ms.*loadState/);
    // the filter of State changes works like the filter of the state view: text, then switches
    await page.fill('#st-filter-input', 'state-core');
    await page.waitForFunction(() => window.agentOS.state.extension.views['step-view']['ui-data'].filter === 'state-core');
    await page.waitForSelector('#tl-detail .sv-hidden');
    assert.ok((await page.$$eval('#tl-detail .tl-table tr', rows => rows.slice(1).map(r => r.textContent))).every(t => t.includes('state-core')));
    await page.fill('#st-filter-input', '');
    await page.waitForFunction(() => window.agentOS.state.extension.views['step-view']['ui-data'].filter === '');
    // buttons, not switches: one kind shows in its own view, a tree of all of them on the left, the chosen one on the right
    assert.deepEqual(await page.$$eval('#st-switches button', els => els.map(x => x.textContent.trim())), ['All', 'Files', 'Views', 'Functions', 'Network', 'Environment']);
    await page.click('#st-switches [data-input*="environment"]');
    await page.waitForSelector('#st-switches [data-input*="environment"][aria-pressed="true"]');
    assert.equal((await stv()).filter_kind, 'environment');
    await page.waitForSelector('#tl-detail .kv .kv-tree .kv-item');
    assert.ok((await page.$$eval('#tl-detail .kv-item', els => els.map(x => x.textContent))).includes('event listeners'));
    // a changed item opens first, on its Value; Changes shows what changed in it
    assert.ok(await page.locator('#tl-detail .kv-item.on.updated, #tl-detail .kv-item.on.added').count() === 1);
    assert.deepEqual(await page.$$eval('#tl-detail .kv-tabs button', els => els.map(x => x.textContent)), ['Value', 'Changes']);
    await page.click('#tl-detail .kv-tabs button:has-text("Changes")');
    await page.waitForSelector('#tl-detail .kv-main .st-legend');
    await page.locator('#tl-detail .kv-item', { hasText: /^document$/ }).click();
    assert.match(await page.textContent('#tl-detail .kv-head'), /^environment\.document/);
    await page.click('#st-switches [data-input*="all"]');
    await page.waitForSelector('#st-switches [data-input*="all"][aria-pressed="true"]');
    await page.waitForSelector('#tl-detail .st-legend');
    // updated values show the old value, as in the state view
    assert.ok(await page.$('#tl-detail .tl-code .was'));

    // its Details: Network (all requests, in groups) next to Environment
    await page.click('#st-tab-details');
    await page.waitForSelector('#tl-detail .tl-netenv .tl-panel');
    assert.equal((await stv()).tab, 'details');
    assert.deepEqual(await page.$$eval('#tl-detail .tl-netenv .tl-panel h3', els => els.map(x => x.textContent)), ['Network (all requests)', 'Environment']);
    const groups = await page.$$eval('#tl-detail .tl-netenv .tl-panel:first-child h4', els => els.map(x => x.textContent.split(' · ')[0]));
    for (const g of ['Html', 'Our scripts', 'API', 'State', 'Packages']) assert.ok(groups.includes(g), groups.join(' | '));
    const req = name => page.locator('#tl-detail .tl-req', { has: page.locator('.tl-req-top b', { hasText: new RegExp('^' + name.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '$') }) }).first();
    assert.match(await req('state-core.js').textContent(), /time: last — · now \d+ ms.*expected.*Used for: The library of the runtime/);
    assert.match(await req('read the versions').textContent(), /db\.collection\('commits'\)\.orderBy\('n'\)\.get\(\)/);
    // a request opens its code on click
    await req('state-core.js').locator('.tl-req-top').click();
    await req('state-core.js').locator('.tl-code').waitFor();
    assert.match(await req('state-core.js').locator('.tl-code').first().evaluate(e => e.cm.getValue()), /StateCore/);
    // a file the browser does not let the page download as text says why, with a link
    await page.route('https://cdnjs.cloudflare.com/**/xml.min.js', route => route.request().resourceType() === 'fetch' ? route.abort() : route.fallback());
    await req('xml.min.js').locator('.tl-req-top').click();
    await req('xml.min.js').locator('.tl-error').waitFor();
    assert.match(await req('xml.min.js').locator('.tl-error').textContent(), /did not let this page download this file as text.*cdnjs\.cloudflare\.com.*Open the file in a new tab/);
    assert.match(await req('xml.min.js').locator('.tl-error a').getAttribute('href'), /^https:\/\/cdnjs\.cloudflare\.com\/.*xml\.min\.js$/);
    assert.match(await page.textContent('#tl-detail .tl-netenv .tl-panel:last-child'), /browser data \/ storages \/ local storage|storages \/ local storage \/ limit/);
    const part = name => page.locator('#tl-detail .tl-part', { has: page.locator('.tl-name', { hasText: name }) });
    await page.click('#tl-next');
    await page.waitForFunction(() => document.querySelector('#st-title .tl-kind').textContent === 'Run index.html');
    assert.match(await page.textContent('#tl-detail'), /a name for this page load: s\w+/);
    // block 2 runs the runtime script; it changed nothing in the state, so it opens on Details
    assert.equal((await stv()).tab, 'details');
    await part('Run the runtime script').locator('.tl-call-head').click();
    assert.match(await part('Run the runtime script').locator('.tl-table').textContent(), /loadState/);
    assert.match(await part('Run the runtime script').locator('.tl-code').first().evaluate(e => e.cm.getValue()), /window\.agentOS = \{/);
    // each part says what happens and why, and shows the lines of index.html that do it
    assert.match(await part('Note the start time').textContent(), /What happens The runtime writes down when it started.*Why Only the timeline uses it/);
    await part('Note the start time').locator('.tl-call-head').first().click();
    await part('Note the start time').locator('.tl-code').first().waitFor();
    assert.match(await part('Note the start time').locator('.tl-file-head').first().textContent(), /^index\.html, line \d+/);
    assert.match(await part('Note the start time').locator('.tl-code').first().evaluate(e => e.cm.getValue()), /var startedAt=performance\.now\(\);/);
    await part('Create the call tracker').locator('.tl-call-head').click();
    assert.match(await part('Create the call tracker').locator('.tl-table').textContent(), /extension\.functions\.render/);
    // Build os: each part of os opens with the functions that use it and its code, the runtime's call() too
    await part('Build os').locator('.tl-call-head').first().click();
    const osCall = page.locator('#tl-detail .tl-more .tl-part', { has: page.locator(':scope > .tl-call-head .tl-name', { hasText: /^os\.call$/ }) });
    await osCall.locator(':scope > .tl-call-head').click();
    assert.match(await osCall.locator(".tl-table").textContent(), /extension\.functions\.render\d+ times/);
    assert.match(await osCall.locator('.tl-code').first().evaluate(e => e.cm.getValue()), /function call\(name, input, viewPath, parent, via\)/);

    // the replay moves to the next block every 1.6 s
    assert.equal((await tl()).selected, 'runtime');
    await page.click('#tl-play');
    await page.waitForFunction(() => window.agentOS.state.extension.views['timeline-view']['ui-data'].selected !== 'runtime', null, { timeout: 5000 });
    assert.equal((await tl()).playing, true);
    await page.click('#tl-play');
    await page.waitForFunction(() => !window.agentOS.state.extension.views['timeline-view']['ui-data'].playing);
    assert.deepEqual(await blockNames(), before);

    // the blocks button hides the row of blocks
    await page.click('#tl-blocks');
    await page.waitForFunction(() => document.querySelector('#tl-strip').hidden);
    await page.click('#tl-blocks');
    await page.waitForFunction(() => !document.querySelector('#tl-strip').hidden);
    // Flows: the saved flows; First enter plays the first 4 blocks and stops
    await page.click('#tl-flows');
    await page.waitForSelector('#tl-flows-list:not([hidden]) .tl-flow');
    assert.match(await page.textContent('#tl-flows-list'), /First enter4 blocks: network, runtime, loadState, extension\.functions\.render/);
    await page.click('#tl-flows-list .tl-flow button');
    await page.waitForFunction(() => document.querySelector('#tl-flows-list').hidden);
    assert.equal((await tl()).selected, 'open');
    assert.match(await page.textContent('#tl-pos'), /^First enter: block 1 of 4/);
    await page.waitForFunction(() => /^First enter: block 4 of 4/.test(document.querySelector('#tl-pos').textContent), null, { timeout: 8000 });
    await page.waitForFunction(() => !window.agentOS.state.extension.views['timeline-view']['ui-data'].playing);
    assert.equal(await page.textContent('#st-title .tl-kind'), 'Start the page');

    // Track the timeline: what you do in the timeline is added as blocks
    await page.click('#tl-track');
    await page.waitForFunction(() => window.agentOS.state.extension.views['timeline-view']['ui-data'].track_timeline === true);
    assert.ok((await blockNames()).includes('local.toggle-tracking'));
    await page.locator('#tl-strip .tl-step').first().click();
    await page.waitForFunction(() => Array.from(document.querySelectorAll('#tl-strip .tl-step-name')).some(x => x.textContent === 'local.select'));
    await page.click('#tl-track');
    await page.waitForFunction(() => window.agentOS.state.extension.views['timeline-view']['ui-data'].track_timeline === false);
    assert.equal((await blockNames()).includes('local.select'), false);

    // the block of the Timeline click: State changes shows the state cut down to what it changed, and who changed it
    if (!(await tl()).show_changes) await page.click('#tl-changes');
    await page.locator('#tl-strip .tl-step', { has: page.locator('.tl-step-name', { hasText: 'local.open.timeline-view' }) }).last().click();
    await page.click('#st-tab-state');
    await page.waitForSelector('#tl-detail .st-legend');
    assert.match(await page.locator('#tl-detail .tl-code').first().evaluate(e => e.cm.getValue()), /"timeline_open": true/);
    assert.ok(await page.locator('#tl-detail .tl-code .chg-updated').count() > 0);
    assert.match(await page.locator('#tl-detail .tl-table').textContent(), /extension\.views\.header-view\.ui-data\.timeline_openfalse {2}→ {2}truelocal\.open\.timeline-view/);
    // its Details: each call says what it does and why it ran, its name opens its code, and what it changed
    await page.click('#st-tab-details');
    await page.locator('#tl-detail .tl-call').first().waitFor();
    assert.deepEqual((await page.locator('#tl-detail .tl-call .tl-name').allTextContents()).slice(0, 2), ['local.open.timeline-view', 'extension.functions.render']);
    assert.match(await page.locator('#tl-detail .tl-call').first().textContent(), /Why it ran You clicked a button of header-view/);
    await page.locator('#tl-detail .tl-call').first().locator('.tl-call-head').first().click();
    assert.match(await page.locator('#tl-detail .tl-call').first().locator('.tl-code').first().evaluate(e => e.cm.getValue()), /async function openTimelineView/);
    assert.ok((await page.locator('#tl-detail .tl-change').allTextContents()).includes('extension.views.header-view.ui-data.timeline_open' + 'false  →  true'));
    await page.click('#tl-changes');
    await page.waitForFunction(() => !document.querySelector('#tl-detail .tl-change'));
    assert.equal((await tl()).show_changes, false);
    await page.click('#tl-changes');
    await page.locator('#tl-detail .tl-change').first().waitFor();
    // closing the timeline closes the block's view too
    await page.click('#timeline-button');
    assert.equal(await page.isHidden('#timeline-view'), true);
    assert.equal(await page.isHidden('#step-view'), true);

    // open the state view from the header: icon buttons, the view path, the version time as "ago"
    await page.click('#state-button');
    await page.waitForSelector('#state-view .CodeMirror');
    assert.equal(await page.getAttribute('#state-button', 'aria-pressed'), 'true');
    assert.equal(await page.evaluate(() => window.agentOS.state.extension.views['header-view']['ui-data'].state_open), true);
    assert.equal(await page.textContent('#path'), 'extension/views/state-view');
    assert.match(await page.textContent('#pos'), /^v1 (just now|\d+ min ago)$/);
    // the top bar: the kind buttons and Changes on the left, the filter and Show empty, then icon buttons, older and newer at the end
    assert.deepEqual(await page.$$eval('#state-view .sv-bar #sv-switches button', els => els.map(b => b.textContent.trim())), ['All', 'Files', 'Views', 'Functions', 'Changes']);
    assert.deepEqual(await page.$$eval('#state-view .sv-bar #sv-right button', els => els.map(b => b.id)), ['collapse', 'save', 'older', 'newer']);
    assert.equal(await page.evaluate(() => [...document.querySelectorAll('#state-view .sv-bar #sv-right button')].filter(b => b.textContent.trim()).length), 0);
    assert.equal(await page.locator('#state-view .sv-foot #pos').count(), 1);
    assert.equal(await page.locator('#state-view .sv-bar #path').count(), 0);
    // the filter shows only the paths that have the text; a switch hides files, views or functions
    const shownText = () => page.evaluate(() => [...document.querySelectorAll('#sv-editor .CodeMirror-line')].map(l => l.textContent).join('\n'));
    const hiddenMarks = () => page.evaluate(() => document.querySelector('.CodeMirror').CodeMirror.getAllMarks().filter(m => m.replacedWith && m.replacedWith.classList.contains('sv-hidden')).length);
    const svd = () => page.evaluate(() => window.agentOS.state.extension.views['state-view']['ui-data']);
    // (the state tests left another kind on, and Show empty off)
    if ((await svd()).filter_kind !== 'all') {
      await page.click('#sv-switches [data-input*="all"]');
      await page.waitForFunction(() => window.agentOS.state.extension.views['state-view']['ui-data'].filter_kind === 'all');
    }
    if (!(await svd()).show_empty) {
      await page.click('#sv-empty');
      await page.waitForFunction(() => window.agentOS.state.extension.views['state-view']['ui-data'].show_empty);
    }
    // (and the filter text)
    await page.fill('#sv-filter-input', '');
    await page.waitForFunction(() => window.agentOS.state.extension.views['state-view']['ui-data'].filter === '');
    assert.equal(await page.locator('#sv-results').count(), 0);
    assert.equal(await hiddenMarks(), 0);
    await page.fill('#sv-filter-input', 'docs/render-steps');
    await page.waitForFunction(() => window.agentOS.state.extension.views['state-view']['ui-data'].filter === 'docs/render-steps');
    await page.locator('#sv-editor .sv-hidden').first().waitFor();
    let shown = await shownText();
    assert.match(shown, /"agents"/);
    assert.match(shown, /"render-steps\.md"/);
    assert.doesNotMatch(shown, /"extension"/);
    assert.match(await page.textContent('#sv-editor .sv-hidden'), /^⋯ \d+ lines?$/);
    // Functions: only functions show, so the match in a file hides
    await page.click('#sv-switches [data-input*="functions"]');
    await page.waitForFunction(() => window.agentOS.state.extension.views['state-view']['ui-data'].filter_kind === 'functions');
    assert.equal(await page.getAttribute('#sv-switches [data-input*="functions"]', 'aria-pressed'), 'true');
    assert.equal(await page.getAttribute('#sv-switches [data-input*="all"]', 'aria-pressed'), 'false');
    assert.doesNotMatch(await shownText(), /render-steps/);
    await page.press('#sv-filter-input', 'Escape');
    await page.waitForFunction(() => window.agentOS.state.extension.views['state-view']['ui-data'].filter === '');
    // without text, Functions shows only the functions objects; Files only the files
    shown = await shownText();
    assert.match(shown, /"local\.init"/);
    assert.doesNotMatch(shown, /^ {8}"ui-data": \{|"render-steps\.md"/m);
    await page.click('#sv-switches [data-input*="files"]');
    await page.waitForFunction(() => window.agentOS.state.extension.views['state-view']['ui-data'].filter_kind === 'files');
    shown = await shownText();
    assert.match(shown, /"render-steps\.md"/);
    assert.doesNotMatch(shown, /"local\.init"/);
    await page.click('#sv-switches [data-input*="all"]');
    await page.waitForFunction(() => window.agentOS.state.extension.views['state-view']['ui-data'].filter_kind === 'all');
    assert.equal(await hiddenMarks(), 0);
    // Show empty off hides the entries with an empty value ({} here)
    assert.match(await shownText(), /"connection": \{\}/);
    await page.click('#sv-empty');
    await page.waitForFunction(() => window.agentOS.state.extension.views['state-view']['ui-data'].show_empty === false);
    assert.equal(await page.isChecked('#sv-empty'), false);
    assert.doesNotMatch(await shownText(), /"connection": \{\}/);
    await page.click('#sv-empty');
    await page.waitForFunction(() => window.agentOS.state.extension.views['state-view']['ui-data'].show_empty);
    assert.equal(await hiddenMarks(), 0);

    // the editor follows the live state: ui-data and runtime fills show up, comments stay
    shown = await page.evaluate(() => JSON.parse(document.querySelector('.CodeMirror').CodeMirror.getValue()));
    assert.equal(shown.extension.views['header-view']['ui-data'].state_open, true);
    assert.equal(shown.extension.views['state-view']['ui-data'].version, 'v1');

    // long strings show "…"; html opens in the html viewer, rendered with the view's ui-data
    const marks = await page.evaluate(() => document.querySelector('.CodeMirror').CodeMirror.getAllMarks().filter(m => m.replacedWith).map(m => m.replacedWith.title));
    assert.ok(marks.includes('agents/agent-oss/files/.claude/settings.json') && marks.includes('agents/agent-oss/files/.claude/CLAUDE.md') && marks.includes('agents/agent-oss/files/docs/how-it-works.md'), marks.join(' | '));
    // the pointer on "..." shows the start of the text
    await page.evaluate(() => document.querySelector('.CodeMirror').CodeMirror.getAllMarks().find(m => m.replacedWith && m.replacedWith.title === 'agents/agent-oss/files/.claude/CLAUDE.md')
      .replacedWith.dispatchEvent(new MouseEvent('mouseenter')));
    assert.match(await page.textContent('.long-tip:not([hidden])'), /^# Agent OS/);
    assert.ok(await page.evaluate(() => document.querySelector('.CodeMirror').CodeMirror.getAllMarks().filter(m => m.replacedWith).every(m => m.replacedWith.textContent === '"..."')));

    // code opens in the viewer on its own
    await page.evaluate(() => document.querySelector('.CodeMirror').CodeMirror.getAllMarks().find(m => m.replacedWith && m.replacedWith.title.startsWith('extension/views/state-view/functions/local.save/code'))
      .replacedWith.dispatchEvent(new MouseEvent('mousedown', { bubbles: true, cancelable: true })));
    await page.waitForSelector('#sv-viewer:not([hidden]) .sv-viewer-body.code-only');
    assert.match(await page.evaluate(() => document.querySelector('#sv-viewer-code .CodeMirror').CodeMirror.getValue()), /^import os from 'os';\nimport ctx from 'ctx';\nimport core from 'state-core';\n\nasync function save\(\) \{/);
    await page.click('#sv-viewer-close');
    await page.evaluate(() => document.querySelector('.CodeMirror').CodeMirror.getAllMarks().find(m => m.replacedWith && m.replacedWith.title.startsWith('extension/views/header-view/html'))
      .replacedWith.dispatchEvent(new MouseEvent('mousedown', { bubbles: true, cancelable: true })));
    await page.waitForSelector('#sv-viewer:not([hidden]) #sv-viewer-code .CodeMirror');
    // the view runs in the viewer with a copy of the state: its buttons work, and its ui-data shows below it
    const frame = page.frameLocator('#sv-viewer-view');
    await frame.locator('#header-view #state-button[aria-pressed="true"]').waitFor();
    await page.waitForFunction(() => /"state_open": true/.test(document.getElementById('sv-viewer-state').textContent));
    await frame.locator('#state-button').click();
    await frame.locator('#state-button[aria-pressed="false"]').waitFor();
    await page.waitForFunction(() => /after local\.open\.state-view/.test(document.getElementById('sv-viewer-state-head').textContent));
    assert.equal(await page.textContent('#sv-viewer-state .chg-updated'), '  "state_open": false');
    await frame.locator('#docs-button').click();
    await frame.locator('#docs-view .doc-link').first().waitFor();
    // the copy changed, the live state did not
    assert.equal(await page.evaluate(() => window.agentOS.state.extension.views['header-view']['ui-data'].state_open), true);
    assert.equal(await page.evaluate(() => window.agentOS.state.extension.views['header-view']['ui-data'].docs_open), false);
    assert.equal(await page.evaluate(() => window.agentOS.state.extension.views['state-view']['ui-data'].viewer_path), 'extension/views/header-view/html');
    // editing the html starts the view again with the new html
    await page.evaluate(() => { const cm = document.querySelector('#sv-viewer-code .CodeMirror').CodeMirror; cm.setValue(cm.getValue().replace('aria-label="Docs"', 'aria-label="Docs" data-edited="yes"')); });
    await frame.locator('#docs-button[data-edited="yes"]').waitFor();
    await page.click('#sv-viewer-close');

    // an md file opens as a document you edit in place; its sections fold
    await page.evaluate(() => document.querySelector('.CodeMirror').CodeMirror.getAllMarks().find(m => m.replacedWith && m.replacedWith.title === 'agents/agent-oss/files/docs/state-view.md')
      .replacedWith.dispatchEvent(new MouseEvent('mousedown', { bubbles: true, cancelable: true })));
    await page.waitForSelector('#sv-viewer-doc:not([hidden]) .md-page h2');
    assert.equal(await page.textContent('.md-page h2'), 'The state view');
    assert.equal(await page.isHidden('#sv-viewer-code'), true);
    // themes: a button switches the theme and keeps it in ui-data (the state tests left it on black)
    assert.equal(JSON.parse((await commitDoc('c000001')).state).extension.views['state-view']['ui-data'].md_theme, 'reader');
    await page.click('#md-themes [data-md-theme="reader"]');
    assert.equal(await page.getAttribute('#sv-viewer-doc', 'data-md-theme'), 'reader');
    assert.equal(await page.locator('#md-themes:not([hidden]) .md-theme').count(), 6);
    await page.click('#md-themes [data-md-theme="black"]');
    assert.equal(await page.getAttribute('#sv-viewer-doc', 'data-md-theme'), 'black');
    assert.equal(await page.getAttribute('#md-themes [data-md-theme="black"]', 'aria-pressed'), 'true');
    assert.equal(await page.evaluate(() => window.agentOS.state.extension.views['state-view']['ui-data'].md_theme), 'black');
    await page.waitForFunction(() => getComputedStyle(document.getElementById('sv-viewer-doc')).backgroundColor === 'rgb(0, 0, 0)');
    await page.click('#md-themes [data-md-theme="reader"]');
    await page.click('.md-sec >> nth=0 >> .md-fold');
    assert.equal(await page.isHidden('.md-sec >> nth=0 >> .md-body'), true);
    await page.click('.md-sec >> nth=0 >> .md-fold');
    assert.equal(await page.isVisible('.md-sec >> nth=0 >> .md-body'), true);
    await page.click('.md-sec >> nth=0 >> h3 .md-t');
    await page.keyboard.press('End');
    await page.keyboard.type(' now');
    await page.keyboard.press('Enter');
    await page.keyboard.type('A new line');
    const md = await page.evaluate(() => document.querySelector('#sv-viewer-code .CodeMirror').CodeMirror.getValue());
    assert.match(md, /\n## Open the state view now\nA new line\n1\. Click the State button/);
    await page.click('#sv-viewer-close');
    assert.match(await page.evaluate(() => document.querySelector('.CodeMirror').CodeMirror.getValue()), /Open the state view now\\nA new line/);
    assert.equal(await page.isHidden('#sv-viewer'), true);

    // edit extension.data and save: a new version, and the border flashes green
    await page.evaluate(() => {
      const cm = document.querySelector('.CodeMirror').CodeMirror;
      const line = cm.getValue().split('\n').findIndex(l => l.trim() === '"data": {},');
      const ch = cm.getLine(line).indexOf('{}') + 1;
      cm.replaceRange('"x": 1', { line, ch });
    });
    await page.waitForFunction(() => window.agentOS.state.extension.views['state-view']['ui-data'].unsaved === true);
    assert.match(await page.textContent('#status'), /Unsaved/);
    await page.click('#save');
    await page.waitForFunction(() => window.agentOS.history.commits.length === 2);
    assert.ok(await page.isVisible('#sv-editor.saved'));
    const commit = await commitDoc('c000002');
    // (a version also keeps network and environment as they were when it was saved)
    assert.equal(JSON.parse(commit.state).extension.data.x, 1);
    assert.ok(JSON.parse(commit.state).network.scripts['state-core.js'].ms >= 0);
    assert.equal(JSON.parse(commit.state).extension.views['state-view']['ui-data'].current_state_version, 2);
    assert.match(await page.textContent('#pos'), /^v2 just now$/);

    // changes view and history steps
    await page.click('#changes');
    const added = await page.evaluate(() => { const cm = document.querySelector('.CodeMirror').CodeMirror; let n = 0; cm.eachLine(l => { if (/chg-added/.test(l.bgClass || '')) n++; }); return n; });
    assert.ok(added >= 1, 'added lines marked');
    await page.focus('#changes');
    await page.keyboard.press('ArrowLeft');
    assert.match(await page.textContent('#pos'), /^v1 /);
    await page.keyboard.press('ArrowRight');
    assert.match(await page.textContent('#pos'), /^v2 /);

    // comments are kept, a slip is fixed on save, and Cmd+S saves from anywhere
    await page.click('#changes');
    await page.evaluate(() => {
      const cm = document.querySelector('.CodeMirror').CodeMirror;
      const line = cm.getValue().split('\n').findIndex(l => l.includes('"common_app_storage": {}'));
      cm.replaceRange('// shared by all apps\n    ', { line, ch: cm.getLine(line).indexOf('"common') });
      const apps = cm.getValue().split('\n').findIndex(l => l.includes('"apps": {}'));
      cm.replaceRange(',', { line: apps, ch: cm.getLine(apps).length });
    });
    await page.waitForFunction(() => window.agentOS.state.extension.views['state-view']['ui-data'].fixable === true);
    assert.match(await page.textContent('#status'), /save fixes them/);
    await page.focus('#changes');
    await page.keyboard.press('Meta+s');
    await page.waitForFunction(() => window.agentOS.history.commits.length === 3);
    const c3 = await commitDoc('c000003');
    assert.match(c3.state, /^[ \t]*\/\/ shared by all apps[ \t]*$/m);
    assert.doesNotThrow(() => JSON.parse(c3.state.replace(/^[ \t]*\/\/ shared by all apps[ \t]*$/m, '')));
    assert.ok(c3.paths.filter(p => !/ (network|environment)\./.test(p)).every(p => p.includes('.ui-data.')), c3.paths.join(', '));
    // the call log keeps a short form of a long output; the function's output in the state is whole
    const fixedSave = await page.evaluate(() => window.agentOS.state.extension.views['state-view'].functions['local.save'].output);
    assert.equal(fixedSave.fixed, true);

    // no function reported errors, and the editor still shows the comment after the live state synced in
    const errs = await page.evaluate(() => { const out = []; (function walk(o, p) { if (!o || typeof o !== 'object') return; if (Array.isArray(o.errors) && o.errors.length) out.push(p + ': ' + o.errors.join('; ')); Object.keys(o).forEach(k => k !== 'output' && walk(o[k], p + '.' + k)); })(window.agentOS.state, ''); return out; });
    assert.deepEqual(errs, []);
    assert.match(await page.evaluate(() => document.querySelector('.CodeMirror').CodeMirror.getValue()), /^[ \t]*\/\/ shared by all apps[ \t]*$/m);

    // a newer version saved somewhere else runs here without a reload; the open views stay open
    if (!(await page.evaluate(() => window.agentOS.state.extension.views['header-view']['ui-data'].timeline_open))) await page.click('#timeline-button');
    await page.waitForSelector('#tl-strip .tl-step');
    await page.evaluate(() => {
      const head = window.agentOS.history.commits[window.agentOS.history.commits.length - 1];
      const st = JSON.parse(head.state.replace(/^[ \t]*\/\/ shared by all apps[ \t]*$/m, ''));
      st.extension.data.from_elsewhere = true;
      st.agents['agent-oss'].files.docs['state-view.md'] += '\nA new line from main.';
      // as saved: the views closed
      st.extension.views['header-view']['ui-data'].timeline_open = false;
      const source = { git: '0123456789abcdef', branch: 'main', message: 'Add a line', request: 'add a line', session: 'https://claude.ai/code/test',
        explain: [{ part: 'state-view.md', before: 'It had no last line.', now: 'It has a last line.' }] };
      window.__docs['commits/c000004'] = { n: 4, parent: 3, at: new Date().toISOString(), state: JSON.stringify(st, null, 2), summary: { added: 1, updated: 1, deleted: 0 }, paths: ['added extension.data.from_elsewhere'], source };
      window.__listeners.forEach(f => f());
    });
    await page.waitForFunction(() => window.agentOS.state.extension.data.from_elsewhere === true);
    await page.waitForFunction(() => /^v4 /.test(document.querySelector('#pos') && document.querySelector('#pos').textContent));
    assert.equal(await page.evaluate(() => window.agentOS.history.commits.length), 4);
    assert.equal(await page.evaluate(() => window.agentOS.state.extension.views['header-view']['ui-data'].timeline_open), true);
    // the timeline shows a New version block: State changes from v3 to v4, then where it came from, before and now, and the file side by side
    const newer = page.locator('#tl-strip .tl-step', { has: page.locator('.tl-step-name', { hasText: /^loadNewerVersion$/ }) }).last();
    await newer.waitFor();
    assert.match(await newer.textContent(), /New version.*\d+ changes?/);
    await newer.click();
    await page.waitForFunction(() => (document.querySelector('#st-title .tl-kind') || {}).textContent === 'New version');
    assert.equal((await stv()).tab, 'state');
    await page.waitForSelector('#tl-detail .st-legend');
    assert.match(await page.locator('#tl-detail .tl-code').first().evaluate(e => e.cm.getValue()), /"from_elsewhere": true/);
    assert.match(await page.textContent('#tl-detail'), /from v3 to v4/);
    // a long text shows as "...", as in the state view: a click opens it in the viewer
    const long = page.locator('#tl-detail .tl-code .long').first();
    await long.waitFor();
    await long.dispatchEvent('mousedown');
    // (the viewer is the file viewer: a file shows by its kind, with its size)
    await page.waitForSelector('.tl-viewer .fv .fv-body');
    assert.match(await page.textContent('.tl-viewer .fv-title span'), /\d+ lines? · [\d.]+ KB/);
    await page.keyboard.press('Escape');
    await page.waitForSelector('.tl-viewer', { state: 'detached' });
    // Files: the tree of all the files on the left; the changed file opens first, with File and Changes tabs
    await page.click('#st-switches [data-input*="files"]');
    await page.waitForSelector('#tl-detail .kv-tree');
    assert.ok(await page.locator('#tl-detail .kv-tree summary', { hasText: /^docs\/$/ }).count() === 1);
    assert.equal(await page.textContent('#tl-detail .kv-item.on'), 'state-view.md');
    assert.deepEqual(await page.$$eval('#tl-detail .kv-tabs button', els => els.map(x => x.textContent)), ['File', 'Changes']);
    // the file viewer: an md file reads as a page with its contents on the left; Source shows its text
    await page.waitForSelector('#tl-detail .fv.fv-md .md-page');
    assert.match(await page.textContent('#tl-detail .fv .md-page'), /A new line from main\./);
    assert.equal(await page.textContent('#tl-detail .fv-badge'), 'MD');
    assert.ok(await page.locator('#tl-detail .fv-side .fv-sym').count() >= 3);
    await page.click('#tl-detail .fv-seg button:has-text("Source")');
    assert.match(await page.locator('#tl-detail .fv .fv-code').evaluate(e => e.cm.getValue()), /A new line from main\./);
    await page.click('#tl-detail .fv-seg button:has-text("Read")');
    await page.waitForSelector('#tl-detail .fv .md-page');
    // md: the six theme buttons of the state view; a click sets state-view ui-data.md_theme and the look of the page
    assert.equal(await page.locator('#tl-detail .fv .md-theme').count(), 6);
    await page.click('#tl-detail .fv .md-theme[data-md-theme="sepia"]');
    await page.waitForFunction(() => document.querySelector('#tl-detail .fv-doc').dataset.mdTheme === 'sepia');
    assert.equal(await page.evaluate(() => window.agentOS.state.extension.views['state-view']['ui-data'].md_theme), 'sepia');
    assert.equal(await page.getAttribute('#tl-detail .fv .md-theme[data-md-theme="sepia"]', 'aria-pressed'), 'true');
    await page.click('#tl-detail .fv .md-theme[data-md-theme="reader"]');
    await page.waitForFunction(() => document.querySelector('#tl-detail .fv-doc').dataset.mdTheme === 'reader');
    // Full screen: the file viewer covers the page; Escape gives it back its place
    await page.click('#tl-detail .fv-full-btn');
    await page.waitForSelector('#tl-detail .fv.fv-full');
    assert.deepEqual(await page.$eval('#tl-detail .fv.fv-full', e => { const r = e.getBoundingClientRect(); return [r.left, r.top, r.width, r.height]; }), await page.evaluate(() => [0, 0, innerWidth, innerHeight]));
    await page.keyboard.press('Escape');
    await page.waitForSelector('#tl-detail .fv.fv-full', { state: 'detached' });
    assert.ok(await page.locator('#tl-detail .kv').count() === 1, 'Escape leaves the step open');
    await page.click('#tl-detail .kv-tabs button:has-text("Changes")');
    await page.waitForSelector('#tl-detail .kv-main .tl-files');
    assert.ok(await page.locator('#tl-detail .kv-main .tl-files .tl-file').nth(1).locator('.chg-added').count() > 0);
    // a file the block did not change has only its File tab
    await page.locator('#tl-detail .kv-item', { hasText: /^index\.html$/ }).click();
    assert.deepEqual(await page.$$eval('#tl-detail .kv-tabs button', els => els.map(x => x.textContent)), ['File']);
    // code has its outline (here the ids and scripts of index.html); a click on it goes to the line; Find marks the matches
    await page.waitForSelector('#tl-detail .fv.fv-html .fv-side .fv-sym');
    assert.ok((await page.$$eval('#tl-detail .fv-sym-name', els => els.map(x => x.textContent))).includes('div#index-view'));
    await page.locator('#tl-detail .fv-sym', { hasText: 'div#index-view' }).first().click();
    await page.fill('#tl-detail .fv-find', 'agentOS');
    assert.match(await page.textContent('#tl-detail .fv-count'), /^\d+ match/);
    await page.press('#tl-detail .fv-find', 'Enter');
    assert.match(await page.textContent('#tl-detail .fv-count'), /^1 of \d+/);
    // a json file is a tree
    await page.locator('#tl-detail .kv-item', { hasText: /^owner-draft\.jsonc$/ }).click();
    await page.waitForSelector('#tl-detail .fv.fv-json .jv-row');
    assert.ok(await page.locator('#tl-detail .jv-key').count() > 3);
    // a function has the tab Pseudo code: its docs, then numbered lines with keywords
    await page.click('#st-switches [data-input*="functions"]');
    await page.locator('#tl-detail .kv-item', { hasText: /^get-state$/ }).click();
    assert.deepEqual(await page.$$eval('#tl-detail .kv-tabs button', els => els.map(x => x.textContent)), ['Function', 'Pseudo code']);
    await page.click('#tl-detail .kv-tabs button:has-text("Pseudo code")');
    await page.waitForSelector('#tl-detail .fv-pseudo .ps-line');
    assert.equal(await page.locator('#tl-detail .ps-line').count(), 4);
    assert.deepEqual(await page.$$eval('#tl-detail .ps-kw', els => els.map(x => x.textContent)), ['READ', 'IF', 'THROW', 'RETURN']);
    assert.equal(await page.locator('#tl-detail .ps-line').nth(2).locator('.ps-guide').count(), 1);
    assert.match(await page.textContent('#tl-detail .ps-docs'), /Returns the JSON state/);
    await page.click('#st-switches [data-input*="all"]');
    await page.waitForSelector('#tl-detail .st-legend');
    await page.click('#st-tab-details');
    await page.waitForSelector('#tl-detail .tl-explain');
    assert.match(await page.textContent('#tl-detail .tl-part'), /git commit 0123456 \(Add a line\)/);
    assert.match(await page.textContent('#tl-detail .tl-explain'), /state-view\.mdIt had no last line\.It has a last line\./);
    const filePart = part('docs/state-view.md');
    assert.match(await filePart.textContent(), /This file was updated/);
    await filePart.locator('.tl-call-head').click();
    await filePart.locator('.tl-files .tl-code').nth(1).waitFor();
    assert.ok(await filePart.locator('.tl-files .tl-code').nth(1).locator('.chg-added').count() > 0);
    await page.click('#st-close');

    // every call, with its parent, is in the stored call log
    await page.waitForFunction(() => Object.keys(window.__docs).some(k => k.startsWith('calls/') && window.__docs[k].items.some(i => i.name === 'loadNewerVersion')), null, { timeout: 5000 });
    const log = await page.evaluate(() => Object.entries(window.__docs).find(([k]) => k.startsWith('calls/'))[1]);
    const names = new Set(log.items.map(i => i.name));
    // (the log keeps the newest calls: at most 400, and at most 240 KB; the first ones, like loadState, can be cut)
    assert.ok(names.has('loadState') || log.items.length < log.count, 'loadState, or a log that was cut');
    assert.ok(JSON.stringify(log).length <= 240000);
    // the log is the newest calls of the page, in order, without a gap
    const all = await page.evaluate(() => window.agentOS.calls.map(c => c.id));
    assert.deepEqual(log.items.map(i => i.id), all.slice(all.indexOf(log.items[0].id), all.indexOf(log.items[0].id) + log.items.length));
    for (const n of ['loadNewerVersion', 'extension.functions.render', 'local.refresh']) assert.ok(names.has(n), n);
    assert.ok(log.items.every(i => i.ok && i.at && typeof i.ms === 'number'), JSON.stringify(log.items.filter(i => !i.ok).slice(0, 3)));

    // the Reload button of the timeline: the page loads again, the timeline opens and replays from the first step,
    // the last agent run
    // (the timeline stayed open after the new version)
    assert.equal(await page.isHidden('#timeline-view'), false);
    await Promise.all([page.waitForNavigation(), page.click('#tl-reload')]);
    await page.waitForSelector('#tl-strip .tl-step.on');
    const replay = await page.evaluate(() => window.agentOS.state.extension.views['timeline-view']['ui-data']);
    await page.waitForSelector('#step-view #st-title .tl-kind');
    assert.equal(replay.playing, true);
    assert.match(replay.selected, /^run:runs\//);
    assert.equal(await page.evaluate(() => window.agentOS.state.extension.views['header-view']['ui-data'].timeline_open), true);
    assert.equal(await page.evaluate(() => sessionStorage.getItem('agent-os.timeline-replay')), null);
    await page.waitForFunction(() => window.agentOS.state.extension.views['timeline-view']['ui-data'].selected === 'runtime', null, { timeout: 6000 });
    // the replay goes on past the blocks that were there when it started (the page was still starting)
    await page.waitForFunction(() => (document.querySelector('#st-title .tl-kind') || {}).textContent === 'Start the page', null, { timeout: 8000 });
    assert.deepEqual(errors, []);
  } finally {
    await browser.close();
    server.close();
  }
});
