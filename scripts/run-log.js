#!/usr/bin/env node
// The raw data of one agent run, from a Claude Code session log (the .jsonl transcript).
// A run is one request: from a message to the agent (a person, the coordinator, a notification) to the next one.
//
//   node scripts/run-log.js <transcript.jsonl> [--run N] [--repo DIR --from REV --to REV] [--version N]
//
// Prints JSON: the session, the run, what started them, the context size, every tool use (events), the uses of
// MCP tools, skills, subagents and workflows, and the files (read, created, updated, deleted).
// It has no explanations: the run-recorder subagent (.claude/agents/run-recorder.md) groups the events into steps
// and writes why for each part, then saves runs/<session>-<run>.json.
'use strict';
const fs = require('fs'), cp = require('child_process'), path = require('path');

const args = process.argv.slice(2), opt = {};
for (let i = 1; i < args.length; i++) if (args[i].startsWith('--')) opt[args[i].slice(2)] = args[i + 1];
const file = args[0];
if (!file) { console.error('usage: run-log.js <transcript.jsonl> [--run N] [--repo DIR --from REV --to REV] [--version N]'); process.exit(1); }
const rows = fs.readFileSync(file, 'utf8').split('\n').filter(Boolean).map(l => { try { return JSON.parse(l); } catch (e) { return null; } }).filter(Boolean);

// Short names for long paths: the repo, the scratchpad, the memory and the project files.
const repo = opt.repo ? path.resolve(opt.repo) + '/' : null;
const short = p => String(p || '')
  .replace(repo || '\u0000', '')
  .replace(/^\/tmp\/claude-\d+\/[^/]+\/[0-9a-f-]{36}\/scratchpad\//, 'scratchpad/')
  .replace(/^\/tmp\/claude\/memory\//, 'memory/')
  .replace(/^\/mnt\/project-files\//, 'project-files/');
const textOf = c => typeof c === 'string' ? c : Array.isArray(c) ? c.filter(x => x && x.type === 'text').map(x => x.text).join('\n') : '';
const isResult = r => Array.isArray(r.message && r.message.content) && r.message.content.some(x => x && x.type === 'tool_result');
// The words of a request: a person's message in a wake, the person's words that a relay cites, the note of a relay,
// or the text. The session context at the top of the first request is not part of it.
const clean = t => t.replace(/<session-context[\s\S]*?<\/session-context[^>]*>/g, '');
const human = t => /<message([^>]*from="human"[^>]*)>([\s\S]*?)<\/message>/.exec(t);
const words = t => {
  t = clean(t);
  const m = human(t), x = m ? m[2] : (/<cited[^>]*>([\s\S]*?)<\/cited>/.exec(t) || /<note>([\s\S]*?)<\/note>/.exec(t) || /<summary>([\s\S]*?)<\/summary>/.exec(t)
    || /<message[^>]*>([\s\S]*?)<\/message>/.exec(t) || [t, t])[1];
  return x.replace(/<[^>]+>/g, ' ').replace(/&#39;/g, "'").replace(/&quot;/g, '"').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&')
    .replace(/\s+/g, ' ').trim().slice(0, 2000);
};
const who = t => {
  t = clean(t);
  const m = human(t);
  return m ? ((/author="([^"]+)"/.exec(m[1]) || [])[1] || 'a person') + ' (a message)'
    : /<relay from="coordinator"/.test(t) ? 'the coordinator (a relay)' + (/<cited/.test(t) ? ', with the words of the person' : '')
    : /<task-notification>/.test(t) ? 'a notification (a scheduled task)' : 'a message';
};

// The runs: each starts at a request that is not a tool result, a compaction summary or a system note.
const starts = [];
rows.forEach((r, i) => {
  if (r.type !== 'user' || r.isSidechain || isResult(r) || r.isCompactSummary) return;
  const t = textOf(r.message && r.message.content);
  if (/^\s*<system-note>/.test(t) && !/<wake|<relay|<task-notification/.test(t)) return;
  starts.push(i);
});
const runs = starts.map((s, k) => ({ from: s, to: k + 1 < starts.length ? starts[k + 1] : rows.length }))
  .filter(x => rows.slice(x.from, x.to).some(r => r.type === 'assistant'));
if (!runs.length) { console.error('no runs in ' + file); process.exit(1); }
const n = opt.run ? +opt.run : runs.length, run = runs[n - 1];
if (!run) { console.error('no run ' + n + ' (the session has ' + runs.length + ')'); process.exit(1); }
const part = rows.slice(run.from, run.to), first = rows[run.from];

// Context: the tokens the model read for each request (input + cache read + cache write); cached = cache read.
const seen = new Set(), requests = [];
part.forEach(r => {
  if (r.type !== 'assistant' || r.isSidechain) return;
  const u = r.message && r.message.usage, id = r.requestId || r.message.id;
  if (!u || seen.has(id)) return;
  seen.add(id);
  requests.push({ id, at: r.timestamp, context: (u.input_tokens || 0) + (u.cache_read_input_tokens || 0) + (u.cache_creation_input_tokens || 0), cached: u.cache_read_input_tokens || 0, output: u.output_tokens || 0 });
});
const compacted = part.some(r => r.type === 'system' && r.subtype === 'compact_boundary');

// Events: each tool use with its target and the size of its result.
const results = {};
// (an image goes into the context as about 1600 tokens, not as the length of its base64 text)
const isImage = c => Array.isArray(c) && c.some(y => y && y.type === 'image');
part.forEach(r => { if (isResult(r)) r.message.content.forEach(x => { if (x.type === 'tool_result') results[x.tool_use_id] = { chars: isImage(x.content) ? 6400 : JSON.stringify(x.content || '').length, error: !!x.is_error, at: r.timestamp }; }); });
const kindOf = (name, input) =>
  /^mcp__/.test(name) ? 'mcp' : name === 'Skill' ? 'skill' : name === 'Agent' || name === 'Task' ? 'subagent' : /workflow/i.test(name) ? 'workflow'
  : name === 'Read' ? 'read' : name === 'Write' ? 'write' : name === 'Edit' || name === 'NotebookEdit' ? 'edit' : name === 'Grep' || name === 'Glob' ? 'search'
  : name === 'Bash' ? (/^\s*(cd [^&]+&&\s*)?(cat|sed -n|head|tail|grep|wc|ls|find|diff)\b/.test(input.command || '') ? 'read' : 'run') : 'tool';
const targetOf = (name, input) => short(input.file_path || input.path || input.pattern || input.skill || input.subagent_type || input.url || input.collection || input.query ||
  (input.command ? input.command.split('\n')[0].slice(0, 160) : '') || (input.text ? input.text.slice(0, 80) : ''));
const events = [];
part.forEach(r => {
  if (r.type !== 'assistant' || r.isSidechain) return;
  const id = r.requestId || r.message.id;
  (r.message.content || []).forEach(x => {
    if (x.type !== 'tool_use') return;
    const input = x.input || {}, res = results[x.id] || {};
    // request: the number of the request (1 = the first of the run) that asked for this tool use; context and cached:
    // the tokens of that request
    events.push({ at: r.timestamp, tool: x.name, kind: kindOf(x.name, input), target: targetOf(x.name, input), result_chars: res.chars || 0, error: res.error || undefined,
      request: requests.findIndex(q => q.id === id) + 1, context: (requests.find(q => q.id === id) || {}).context, cached: (requests.find(q => q.id === id) || {}).cached, id: x.id });
  });
});

// Uses: MCP tools, skills, subagents, workflows.
const count = (list, key) => list.reduce((o, e) => { const k = key(e); o[k] = (o[k] || 0) + 1; return o; }, {});
const uses = {
  mcp: count(events.filter(e => e.kind === 'mcp'), e => e.tool.replace(/^mcp__/, '').replace('__', ' / ')),
  skills: count(events.filter(e => e.kind === 'skill'), e => e.target),
  subagents: count(events.filter(e => e.kind === 'subagent'), e => e.target || 'general-purpose'),
  workflows: count(events.filter(e => e.kind === 'workflow'), e => e.target || e.tool)
};

// Files: what the agent read (Read, and Bash commands that read), and what it wrote. In the repo, git says what was
// created, updated and deleted between --from and --to.
const files = {};
const fileRe = /(?:^|[\s'"=<>(])((?:\.?\.?\/)?[\w.@$-]*(?:\/[\w.@-]+)*\.(?:html|js|mjs|json|jsonl|md|py|png|txt|css|tpl|yaml|yml|sh))(?=$|[\s'";|&)<>:,])/g;
// The paths in a shell command; a relative path is read from the folder of its "cd" (variables like $S are left as they are).
const pathsIn = cmd => {
  const dir = (/^\s*cd\s+(\S+)/.exec(cmd) || [])[1], out = [];
  let m;
  fileRe.lastIndex = 0;
  while ((m = fileRe.exec(cmd))) {
    const p = m[1];
    if (/^\$/.test(p) || /^\d/.test(p)) continue;
    out.push(p.startsWith('/') || !dir ? p : path.join(dir, p));
  }
  return Array.from(new Set(out));
};
// Shell commands that change files: a python script that writes p = '...' or open('...', 'w'), sed -i, a redirect (>), rm. A relative
// path is from the folder of the last "cd" before it. Redirects, sed and rm are not looked for inside a heredoc.
const changedIn = cmd => {
  const out = [], abs = (p, at) => {
    let dir = null, m;
    const cd = /(?:^|&&|;|\n)\s*cd\s+(\S+)/g;
    while ((m = cd.exec(cmd)) && m.index < at) dir = m[1];
    return p.startsWith('/') || !dir || /^\$/.test(dir) ? p : path.join(dir, p);
  };
  let m;
  const py = /\bp\s*=\s*['"]([^'"]+)['"][\s\S]*?open\(p,\s*['"]w['"]\)/g;
  while ((m = py.exec(cmd))) out.push([abs(m[1], m.index), 'edited']);
  const py2 = /\bopen\(\s*['"]([^'"]+)['"],\s*['"]w['"]\)/g;
  while ((m = py2.exec(cmd))) out.push([abs(m[1], m.index), 'written']);
  const shell = cmd.replace(/<<-?\s*'?(\w+)'?[^\n]*\n[\s\S]*?\n\1\b/g, m => ' '.repeat(m.length));
  const sed = /\bsed -i\S*\s+(?:"[^"]*"|'[^']*')\s+([^\s;&|]+)/g;
  while ((m = sed.exec(shell))) out.push([abs(m[1], m.index), 'edited']);
  const to = /(?:^|\s)>{1,2}\s*([\w./-]+\.[A-Za-z]\w*)/g;
  while ((m = to.exec(shell))) out.push([abs(m[1], m.index), 'written']);
  const rm = /(?:^|&&|;|\n)\s*rm\s+(?:-\w+\s+)*([\w./*-]+)/g;
  while ((m = rm.exec(shell))) out.push([abs(m[1], m.index), 'deleted']);
  return out.filter(([p]) => !/^\$/.test(p));
};
const add = (p, action, tokens, at, e) => {
  const k = short(p), f = files[k] || (files[k] = { path: k, actions: [], tokens: 0 });
  // each tool use keeps the files it read or changed, so the steps can show their own files
  if (e) { e.files = e.files || []; if (!e.files.some(x => x.path === k && x.action === action)) e.files.push({ path: k, action, tokens: tokens || 0 }); }
  if (!f.actions.includes(action)) f.actions.push(action);
  f.tokens += tokens || 0;
  f.first = f.first || at;
  if (action === 'read') f.last_read = at;
};
events.forEach(e => {
  const ev = part.find(r => r.type === 'assistant' && (r.message.content || []).some(x => x.id === e.id));
  const input = ((ev.message.content || []).find(x => x.id === e.id) || {}).input || {};
  const tokens = Math.round(e.result_chars / 4);
  if (e.tool === 'Read') add(input.file_path, 'read', tokens, e.at, e);
  else if (e.tool === 'Write') add(input.file_path, 'written', Math.round((input.content || '').length / 4), e.at, e);
  else if (e.tool === 'Edit') add(input.file_path, 'edited', 0, e.at, e);
  else if (e.tool === 'Bash' && e.kind === 'read') { const ps = pathsIn(input.command || ''); ps.forEach(p => add(p, 'read', Math.round(tokens / ps.length), e.at, e)); }
  else if (e.tool === 'Bash') changedIn(input.command || '').forEach(([p, a]) => add(p, a, 0, e.at, e));
});
let git = null;
if (repo && opt.from && opt.to) {
  try {
    git = cp.execSync('git -C ' + JSON.stringify(repo) + ' diff --name-status ' + opt.from + ' ' + opt.to, { encoding: 'utf8' }).trim().split('\n').filter(Boolean).map(l => l.split('\t'));
    git.forEach(([s, p]) => { const f = files[p] || (files[p] = { path: p, actions: [], tokens: 0 }); f.git = s === 'A' ? 'created' : s === 'D' ? 'deleted' : 'updated'; });
  } catch (e) { git = { error: String(e.message || e).slice(0, 200) }; }
}
// What stays in the context: a file read in this run is in the cached part of the context for each request after it,
// until the session is compacted. So at the end, the files read after the last compaction are cached.
const lastAt = requests.length ? requests[requests.length - 1].at : null;
const cut = (part.filter(r => r.type === 'system' && r.subtype === 'compact_boundary').pop() || {}).timestamp || '';
Object.values(files).forEach(f => { f.cached = !!(f.last_read && lastAt && f.last_read < lastAt && f.last_read > cut); delete f.last_read; });

const sessionStart = rows.find(r => r.type === 'user' && !isResult(r) && !r.isCompactSummary);
const firstText = textOf(first.message && first.message.content);
console.log(JSON.stringify({
  session: first.sessionId,
  run: n,
  runs_in_session: runs.length,
  agent: 'Claude Code (main agent)',
  started: first.timestamp,
  ended: (part.filter(r => r.timestamp).pop() || first).timestamp,
  version: opt.version ? +opt.version : undefined,
  git: repo && opt.from && opt.to ? { from: opt.from, to: opt.to } : undefined,
  started_by: {
    session: { who: who(textOf(sessionStart.message.content)), words: words(textOf(sessionStart.message.content)).slice(0, 400), at: sessionStart.timestamp },
    run: { who: who(firstText), words: words(firstText), at: first.timestamp }
  },
  context: {
    at_start: requests.length ? requests[0].context : 0,
    at_end: requests.length ? requests[requests.length - 1].context : 0,
    peak: Math.max(0, ...requests.map(q => q.context)),
    cached_at_end: requests.length ? requests[requests.length - 1].cached : 0,
    output_tokens: requests.reduce((t, q) => t + q.output, 0),
    requests: requests.length,
    compacted
  },
  uses,
  events: events.map(({ id, ...e }) => e),
  files: Object.values(files).sort((a, b) => a.path < b.path ? -1 : 1)
}, null, 2));
