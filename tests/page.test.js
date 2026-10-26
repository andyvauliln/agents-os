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
    await page.goto(`http://localhost:${server.address().port}/`);
    await page.evaluate(() => window.agentOS.ready);

    // boot: version 1 from state.json, index-view rendered (page html and styles from the state), then header-view: only the State view button
    assert.ok(await page.evaluate(() => !!window.__docs['commits/c000001']));
    assert.equal(await page.locator('#header-view button').count(), 3);
    assert.ok(await page.isVisible('#timeline-button[aria-label="Timeline"] svg'));
    assert.ok(await page.isVisible('#docs-button[aria-label="Docs"] svg'));
    assert.ok(await page.isVisible('#state-button[aria-label="State view"] svg'));
    assert.equal(await page.isHidden('#state-view'), true);
    // every rule of the page styles in index-view html is read by the browser (a broken rule drops the rest)
    assert.ok(await page.evaluate(() => document.querySelector('#index-view style').sheet.cssRules.length) > 150);
    const boot = await page.evaluate(() => window.agentOS.calls.map(c => c.name));
    assert.deepEqual(boot.sort(), ['extension.functions.get-state', 'extension.functions.render', 'extension.functions.render', 'loadState', 'local.init', 'local.init']);

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
    await page.evaluate(() => window.agentOS.os.call('extension.functions.unmount', { view_path: 'extension.views.step-view' }));

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
    assert.deepEqual(stepKinds.slice(0, 4), ['Open the page', 'Run index.html', 'Load the state', 'Start the page']);
    assert.equal(await page.isHidden('#step-view'), true);
    assert.equal(await page.isChecked('#tl-track'), false);

    // a click on a block shows it under the header: Details first when it changed nothing; with tracking off the click is not a block
    const before = await blockNames();
    await page.locator('#tl-strip .tl-step').first().click();
    await page.waitForFunction(() => (document.querySelector('#step-view #st-title .tl-kind') || {}).textContent === 'Open the page');
    assert.equal((await tl()).selected, 'open');
    assert.equal((await stv()).tab, 'details');
    // a click on the chosen block again hides it, and so does the close button
    await page.locator('#tl-strip .tl-step').first().click();
    await page.waitForFunction(() => document.querySelector('#step-view').hidden);
    assert.equal((await tl()).selected, null);
    await page.locator('#tl-strip .tl-step').first().click();
    await page.waitForSelector('#step-view #st-title .tl-kind');
    await page.click('#st-close');
    await page.waitForFunction(() => document.querySelector('#step-view').hidden);
    assert.equal((await tl()).selected, null);
    await page.locator('#tl-strip .tl-step').first().click();
    await page.waitForSelector('#step-view #st-title .tl-kind');
    await page.click('#st-tab-state');
    await page.waitForFunction(() => /There is no state yet/.test(document.querySelector('#tl-detail').textContent));
    assert.deepEqual(await blockNames(), before);
    assert.ok(await page.evaluate(() => document.querySelector('#header-view').compareDocumentPosition(document.querySelector('#step-view')) & Node.DOCUMENT_POSITION_FOLLOWING));

    // the Details tab: the steps before the first call show their parts
    await page.click('#st-tab-details');
    await page.waitForSelector('#tl-detail .tl-part');
    assert.equal((await stv()).tab, 'details');
    // block 1 lists every file the page downloaded: index.html, state-core.js, the runtime script, then the rest
    const openParts = await page.$$eval('#tl-detail .tl-part .tl-name', els => els.map(x => x.textContent));
    assert.deepEqual(openParts.slice(0, 3), ['Download index.html', 'Load state-core.js', 'The runtime script']);
    assert.ok(openParts.some(n => /^Download codemirror/.test(n)) && openParts.includes('Download state.json'), openParts.join(' | '));
    // a part opens on click: index.html shows its html, state-core.js its code, the runtime script what it did and its code
    const part = name => page.locator('#tl-detail .tl-part', { has: page.locator('.tl-name', { hasText: name }) });
    await part('Download index.html').locator('.tl-call-head').click();
    await part('Download index.html').locator('.tl-code').waitFor();
    assert.match(await part('Download index.html').locator('.tl-code').first().evaluate(e => e.cm.getValue()), /<div id="index-view"><\/div>/);
    await part('Load state-core.js').locator('.tl-call-head').click();
    await part('Load state-core.js').locator('.tl-code').waitFor();
    assert.match(await part('Load state-core.js').locator('.tl-code').first().evaluate(e => e.cm.getValue()), /StateCore/);
    await part('The runtime script').locator('.tl-call-head').click();
    assert.match(await part('The runtime script').locator('.tl-code').first().evaluate(e => e.cm.getValue()), /window\.agentOS = \{/);
    await part('Download index.html').locator('.tl-call-head').click();
    assert.equal(await part('Download index.html').locator('.tl-code').count(), 0);
    await page.click('#tl-next');
    await page.waitForFunction(() => document.querySelector('#st-title .tl-kind').textContent === 'Run index.html');
    assert.match(await page.textContent('#tl-detail'), /a name for this page load: s\w+/);
    // block 2 runs the runtime script
    await part('Run the runtime script').locator('.tl-call-head').click();
    assert.match(await part('Run the runtime script').locator('.tl-table').textContent(), /loadState/);
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
    assert.match(await page.textContent('#tl-flows-list'), /First enter4 blocks: index\.html, runtime, loadState, extension\.functions\.render/);
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
    assert.match(await page.textContent('#pos'), /^v1 just now$/);
    // the top bar has only icon buttons and the filter; the version, the path and the status are in the bottom bar
    assert.equal(await page.evaluate(() => [...document.querySelectorAll('#state-view .sv-bar .sv-group button')].filter(b => b.textContent.trim()).length), 0);
    assert.equal(await page.locator('#state-view .sv-foot #pos').count(), 1);
    assert.equal(await page.locator('#state-view .sv-bar #path').count(), 0);
    // the filter shows only the paths that have the text; a switch hides files, views or functions
    const shownText = () => page.evaluate(() => [...document.querySelectorAll('#sv-editor .CodeMirror-line')].map(l => l.textContent).join('\n'));
    const hiddenMarks = () => page.evaluate(() => document.querySelector('.CodeMirror').CodeMirror.getAllMarks().filter(m => m.replacedWith && m.replacedWith.classList.contains('sv-hidden')).length);
    // (the state tests left some switches off)
    for (const kind of ['files', 'views', 'functions']) {
      if (await page.evaluate(k => window.agentOS.state.extension.views['state-view']['ui-data'].filter_kinds[k], kind)) continue;
      await page.click(`#sv-switches [data-input*="${kind}"]`);
      await page.waitForFunction(k => window.agentOS.state.extension.views['state-view']['ui-data'].filter_kinds[k], kind);
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
    // files off: the match is in a file, so it hides
    await page.click('#sv-switches [data-input*="files"]');
    await page.waitForFunction(() => !window.agentOS.state.extension.views['state-view']['ui-data'].filter_kinds.files);
    assert.equal(await page.getAttribute('#sv-switches [data-input*="files"]', 'aria-checked'), 'false');
    assert.doesNotMatch(await shownText(), /render-steps/);
    await page.click('#sv-switches [data-input*="files"]');
    await page.waitForFunction(() => window.agentOS.state.extension.views['state-view']['ui-data'].filter_kinds.files);
    await page.press('#sv-filter-input', 'Escape');
    await page.waitForFunction(() => window.agentOS.state.extension.views['state-view']['ui-data'].filter === '');
    assert.equal(await hiddenMarks(), 0);
    // without text, functions off hides every functions object
    await page.click('#sv-switches [data-input*="functions"]');
    await page.waitForFunction(() => !window.agentOS.state.extension.views['state-view']['ui-data'].filter_kinds.functions);
    assert.ok(await hiddenMarks() > 0);
    await page.click('#sv-switches [data-input*="functions"]');
    await page.waitForFunction(() => window.agentOS.state.extension.views['state-view']['ui-data'].filter_kinds.functions);
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
    assert.equal(JSON.parse(await page.evaluate(() => window.__docs['commits/c000001'].state)).extension.views['state-view']['ui-data'].md_theme, 'reader');
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
    const commit = await page.evaluate(() => window.__docs['commits/c000002']);
    assert.ok(commit.paths.includes('added extension.data.x'), commit.paths.join(', '));
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
    const c3 = await page.evaluate(() => window.__docs['commits/c000003']);
    assert.ok(c3.state.includes('// shared by all apps'));
    assert.doesNotThrow(() => JSON.parse(c3.state.replace('// shared by all apps', '')));
    assert.ok(c3.paths.every(p => p.includes('.ui-data.')), c3.paths.join(', '));
    const fixedSave = await page.evaluate(() => window.agentOS.calls.filter(c => c.name === 'local.save').pop());
    assert.equal(fixedSave.output.fixed, true);

    // no function reported errors, and the editor still shows the comment after the live state synced in
    const errs = await page.evaluate(() => { const out = []; (function walk(o, p) { if (!o || typeof o !== 'object') return; if (Array.isArray(o.errors) && o.errors.length) out.push(p + ': ' + o.errors.join('; ')); Object.keys(o).forEach(k => k !== 'output' && walk(o[k], p + '.' + k)); })(window.agentOS.state, ''); return out; });
    assert.deepEqual(errs, []);
    assert.ok(await page.evaluate(() => document.querySelector('.CodeMirror').CodeMirror.getValue().includes('// shared by all apps')));

    // a newer version saved somewhere else runs here without a reload
    await page.evaluate(() => {
      const head = window.agentOS.history.commits[window.agentOS.history.commits.length - 1];
      const st = JSON.parse(head.state.replace('// shared by all apps', ''));
      st.extension.data.from_elsewhere = true;
      window.__docs['commits/c000004'] = { n: 4, parent: 3, at: new Date().toISOString(), state: JSON.stringify(st, null, 2), summary: { added: 1, updated: 0, deleted: 0 }, paths: ['added extension.data.from_elsewhere'] };
      window.__listeners.forEach(f => f());
    });
    await page.waitForFunction(() => window.agentOS.state.extension.data.from_elsewhere === true);
    await page.waitForFunction(() => /^v4 /.test(document.querySelector('#pos') && document.querySelector('#pos').textContent));
    assert.equal(await page.evaluate(() => window.agentOS.history.commits.length), 4);

    // every call, with its parent, is in the stored call log
    await page.waitForFunction(() => Object.keys(window.__docs).some(k => k.startsWith('calls/') && window.__docs[k].items.some(i => i.name === 'loadNewerVersion')), null, { timeout: 5000 });
    const log = await page.evaluate(() => Object.entries(window.__docs).find(([k]) => k.startsWith('calls/'))[1]);
    const names = new Set(log.items.map(i => i.name));
    // (the log keeps the newest 400 calls: after that many, the first ones, like loadState, are not in it)
    assert.ok(log.count <= 400 ? names.has('loadState') : log.items.length === 400, 'loadState or 400 items');
    for (const n of ['loadNewerVersion', 'extension.functions.render', 'local.open.state-view', 'local.save', 'local.toggle-changes', 'local.step', 'local.edit', 'local.refresh', 'local.open-viewer', 'local.close-viewer', 'runTest']) assert.ok(names.has(n), n);
    assert.ok(log.items.every(i => i.ok && i.at && typeof i.ms === 'number'), JSON.stringify(log.items.filter(i => !i.ok).slice(0, 3)));

    // the Reload button of the timeline: the page loads again, the timeline opens and replays from the first step
    await page.click('#timeline-button');
    await Promise.all([page.waitForNavigation(), page.click('#tl-reload')]);
    await page.waitForSelector('#tl-strip .tl-step.on');
    const replay = await page.evaluate(() => window.agentOS.state.extension.views['timeline-view']['ui-data']);
    await page.waitForSelector('#step-view #st-title .tl-kind');
    assert.equal(replay.playing, true);
    assert.equal(replay.selected, 'open');
    assert.equal(await page.evaluate(() => window.agentOS.state.extension.views['header-view']['ui-data'].timeline_open), true);
    assert.equal(await page.evaluate(() => sessionStorage.getItem('agent-os.timeline-replay')), null);
    await page.waitForFunction(() => window.agentOS.state.extension.views['timeline-view']['ui-data'].selected === 'runtime', null, { timeout: 5000 });
    // the replay goes on past the blocks that were there when it started (the page was still starting)
    await page.waitForFunction(() => (document.querySelector('#st-title .tl-kind') || {}).textContent === 'Start the page', null, { timeout: 8000 });
    assert.deepEqual(errors, []);
  } finally {
    await browser.close();
    server.close();
  }
});
