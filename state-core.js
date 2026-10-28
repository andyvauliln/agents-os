// Pure logic for the Agent OS page: state paths, templates, diffs, the changes view, commits,
// history steps, test checks and the call log.
// Works in the browser (window.StateCore) and in Node (require) so it can be tested without a page.
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.StateCore = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  function isObj(v) { return v !== null && typeof v === 'object' && !Array.isArray(v); }
  function same(a, b) { return JSON.stringify(a) === JSON.stringify(b); }
  function pathText(path) { return path.join('.'); }

  // Every change between two states: objects are compared key by key, anything else as a whole value.
  function diff(before, after, path) {
    path = path || [];
    var out = [];
    if (isObj(before) && isObj(after)) {
      Object.keys(after).forEach(function (k) {
        var p = path.concat(k);
        if (!(k in before)) out.push({ type: 'added', path: p, after: after[k] });
        else out = out.concat(diff(before[k], after[k], p));
      });
      Object.keys(before).forEach(function (k) {
        if (!(k in after)) out.push({ type: 'deleted', path: path.concat(k), before: before[k] });
      });
      return out;
    }
    if (!same(before, after)) out.push({ type: 'updated', path: path, before: before, after: after });
    return out;
  }

  function summarize(changes) {
    var s = { added: 0, updated: 0, deleted: 0 };
    changes.forEach(function (c) { s[c.type]++; });
    return s;
  }

  // The state cut down to what changed, as JSON text, with the line range and kind of each change.
  // Kept keys follow the new state's order; deleted keys come back where they stood in the old one.
  function changesView(before, after) {
    var lines = [], marks = [];
    function keysOf(b, a) {
      var keys = Object.keys(a);
      Object.keys(b).forEach(function (k, i) {
        if (k in a) return;
        var prev = Object.keys(b).slice(0, i).reverse().find(function (x) { return keys.indexOf(x) >= 0; });
        keys.splice(prev === undefined ? 0 : keys.indexOf(prev) + 1, 0, k);
      });
      return keys;
    }
    function changed(b, a) { return !same(b, a); }
    function emitValue(value, indent, prefix, suffix, type, path, before) {
      var text = JSON.stringify(value, null, 2).split('\n');
      var from = lines.length;
      text.forEach(function (t, i) {
        lines.push((i === 0 ? indent + prefix : indent) + t + (i === text.length - 1 ? suffix : ''));
      });
      var mark = { type: type, path: path, from: from, to: lines.length - 1, before: before };
      if (type === 'updated') mark.after = value;
      marks.push(mark);
    }
    function emitObject(b, a, indent, path) {
      var keys = keysOf(b, a).filter(function (k) { return changed(b[k], a[k]) || !(k in a) || !(k in b); });
      keys.forEach(function (k, i) {
        var comma = i < keys.length - 1 ? ',' : '';
        var prefix = JSON.stringify(k) + ': ';
        var p = path.concat(k);
        if (!(k in b)) emitValue(a[k], indent, prefix, comma, 'added', p);
        else if (!(k in a)) emitValue(b[k], indent, prefix, comma, 'deleted', p);
        else if (isObj(b[k]) && isObj(a[k])) {
          lines.push(indent + prefix + '{');
          emitObject(b[k], a[k], indent + '  ', p);
          lines.push(indent + '}' + comma);
        } else emitValue(a[k], indent, prefix, comma, 'updated', p, b[k]);
      });
    }
    if (isObj(before) && isObj(after)) {
      lines.push('{');
      emitObject(before, after, '  ', []);
      lines.push('}');
    } else if (changed(before, after)) emitValue(after, '', '', '', 'updated', [], before);
    var empty = marks.length === 0;
    return { text: empty ? '{}' : lines.join('\n'), marks: marks, empty: empty };
  }

  // JSON with comments. Comments stay in the saved text; they are skipped when the text is read.
  function tokenize(text) {
    var toks = [], i = 0, n = text.length, j;
    while (i < n) {
      var c = text[i];
      if (/\s/.test(c)) { j = i; while (j < n && /\s/.test(text[j])) j++; toks.push({ t: 'ws', v: text.slice(i, j) }); i = j; continue; }
      if (c === '/' && text[i + 1] === '/') { j = text.indexOf('\n', i); if (j < 0) j = n; toks.push({ t: 'comment', v: text.slice(i, j) }); i = j; continue; }
      if (c === '/' && text[i + 1] === '*') { j = text.indexOf('*/', i + 2); j = j < 0 ? n : j + 2; toks.push({ t: 'comment', v: text.slice(i, j) }); i = j; continue; }
      if (c === '"' || c === "'") {
        j = i + 1;
        while (j < n && text[j] !== c && text[j] !== '\n') { if (text[j] === '\\') j++; j++; }
        var closed = j < n && text[j] === c;
        toks.push({ t: 'string', q: c, closed: closed, v: text.slice(i, closed ? j + 1 : j) }); i = closed ? j + 1 : j; continue;
      }
      if ('{}[]:,'.indexOf(c) >= 0) { toks.push({ t: c, v: c }); i++; continue; }
      j = i; while (j < n && !/[\s{}\[\]:,"'\/]/.test(text[j])) j++; if (j === i) j = i + 1;
      toks.push({ t: 'word', v: text.slice(i, j) }); i = j;
    }
    return toks;
  }
  function stripComments(text) {
    return tokenize(text).map(function (t) { return t.t === 'comment' ? t.v.replace(/[^\n]/g, ' ') : t.v; }).join('');
  }
  function parseJsonc(text) { return JSON.parse(stripComments(text)); }

  // Repairs the usual slips and keeps comments: trailing and doubled commas, missing commas,
  // unquoted keys, single quotes, unclosed strings, and brackets left open at the end.
  function autofix(text) {
    var toks = tokenize(text), out = [], stack = [];
    function next(k) { for (var m = k + 1; m < toks.length; m++) if (toks[m].t !== 'ws' && toks[m].t !== 'comment') return toks[m]; return null; }
    function ends(t) { return t && (t.t === 'string' || t.t === 'word' || t.t === '}' || t.t === ']'); }
    function starts(t) { return t && (t.t === 'string' || t.t === 'word' || t.t === '{' || t.t === '['); }
    toks.forEach(function (tok, k) {
      var v = tok.v, nx = next(k);
      if (tok.t === 'string') {
        var inner = tok.closed ? v.slice(1, -1) : v.slice(1);
        if (tok.q === "'") inner = inner.replace(/\\'/g, "'").replace(/(^|[^\\])"/g, '$1\\"');
        v = '"' + inner + '"';
      } else if (tok.t === 'word') {
        if (nx && nx.t === ':') v = JSON.stringify(v);
        else if (/^(True|TRUE)$/.test(v)) v = 'true';
        else if (/^(False|FALSE)$/.test(v)) v = 'false';
        else if (/^(None|undefined|NULL)$/.test(v)) v = 'null';
      } else if (tok.t === ',' && (!nx || nx.t === '}' || nx.t === ']' || nx.t === ',')) v = '';
      if (tok.t === '{' || tok.t === '[') stack.push(tok.t === '{' ? '}' : ']');
      if ((tok.t === '}' || tok.t === ']') && stack[stack.length - 1] === tok.t) stack.pop();
      out.push(v);
      if (ends(tok) && starts(nx)) out.push(',');
    });
    while (stack.length) out.push('\n' + stack.pop());
    return out.join('');
  }

  // Where each value sits in the text: path (as JSON) -> {from, start, end}; objects also list their members.
  function spans(text) {
    var pos = 0, sig = [], map = {}, i = 0;
    tokenize(text).forEach(function (t) { t.at = pos; pos += t.v.length; if (t.t !== 'ws' && t.t !== 'comment') sig.push(t); });
    function keyOf(t) { try { return t.t === 'string' ? JSON.parse('"' + t.v.slice(1, -1) + '"') : t.v; } catch (e) { return t.v.slice(1, -1); } }
    function value(path) {
      var t = sig[i];
      if (!t) return null;
      var rec = { from: t.at, start: t.at };
      if (t.t === '{') {
        i++; rec.obj = true; rec.members = [];
        while (sig[i] && sig[i].t !== '}') {
          if (sig[i].t === ',') { i++; continue; }
          var k = sig[i], key = keyOf(k); i++;
          if (sig[i] && sig[i].t === ':') i++;
          var r = value(path.concat(key));
          if (!r) break;
          r.from = k.at;
          rec.members.push({ key: key, keyStart: k.at, end: r.end });
        }
        rec.end = sig[i] ? sig[i].at + 1 : text.length; i++;
      } else if (t.t === '[') {
        i++; var n = 0;
        while (sig[i] && sig[i].t !== ']') { if (sig[i].t === ',') { i++; continue; } if (!value(path.concat(n++))) break; }
        rec.end = sig[i] ? sig[i].at + 1 : text.length; i++;
      } else { rec.end = t.at + t.v.length; i++; }
      map[JSON.stringify(path)] = rec;
      return rec;
    }
    value([]);
    return map;
  }

  // The kind of an entry, for the switches of a filter: files, views, functions, network or environment.
  function kindOf(p) {
    if (p[0] === 'agents' && p.length === 3 && p[2] === 'files') return 'files';
    if (p[0] === 'extension' && p[1] === 'views' && p.length === 3) return 'views';
    if (p[0] === 'extension' && p[p.length - 1] === 'functions' && (p.length === 2 || (p[1] === 'views' && p.length === 4))) return 'functions';
    if ((p[0] === 'network' || p[0] === 'environment') && p.length === 1) return p[0];
    return null;
  }

  // A text that holds only {} or [] (and spaces or line ends), as JSON text: "{}\n" is the text of an empty json file.
  var W = '(?:\\s|\\\\[nrt])*';
  var EMPTY_TEXT = new RegExp('^"' + W + '(?:\\{' + W + '\\}|\\[' + W + '\\])' + W + '"');
  function emptyText(json) { return EMPTY_TEXT.test(json) && json.length === json.match(EMPTY_TEXT)[0].length; }

  // The filter of a JSON text: with q, only the entries whose path has q show, with the first and last lines of the
  // objects around them. kinds is an object (a kind that is off, kinds[kind] === false, hides its entries) or the name of
  // one kind: then only the entries of that kind show ('all' shows all). opts.hideEmpty hides the entries with an empty
  // value ({}, [], "", null or a text of {} or []). Returns the hidden lines as [from, to]; lines hidden only for an empty value are
  // [from, to, 'empty'] (the state view hides them without a "⋯ N lines" mark).
  function filterLines(text, map, q, kinds, opts) {
    map = map || spans(text);
    q = String(q || '').trim().toLowerCase(); opts = opts || {};
    var only = typeof kinds === 'string' && kinds !== 'all' ? kinds : null;
    if (!kinds || typeof kinds !== 'object') kinds = {};
    var starts = [0], i;
    for (i = 0; i < text.length; i++) if (text.charCodeAt(i) === 10) starts.push(i + 1);
    function line(at) { var lo = 0, hi = starts.length - 1; while (lo < hi) { var mid = (lo + hi + 1) >> 1; if (starts[mid] <= at) lo = mid; else hi = mid - 1; } return lo; }
    var entries = Object.keys(map).map(function (k) { return [JSON.parse(k), map[k]]; });
    var off = entries.filter(function (e) { var k = kindOf(e[0]); return k && kinds[k] === false; }).map(function (e) { return e[1]; });
    var empty = opts.hideEmpty ? entries.filter(function (e) { var v = text.slice(e[1].start, e[1].end); return e[0].length && (/^(\{\s*\}|\[\s*\]|""|null)$/.test(v) || emptyText(v)); }).map(function (e) { return e[1]; }) : [];
    var kept = only ? entries.filter(function (e) { return kindOf(e[0]) === only; }) : null;
    var root = map['[]'];
    if (!entries.length || !root || (!q && !off.length && !only && !empty.length)) return [];
    var show = []; for (i = 0; i < starts.length; i++) show.push(!q && !only);
    show[line(root.from)] = show[line(root.end - 1)] = true;
    function inside(r, list) { return list.some(function (o) { return r.from >= o.from && r.end <= o.end; }); }
    function keep(p, r) {
      for (var l = line(r.from); l <= line(r.end - 1); l++) show[l] = true;
      for (var j = 1; j < p.length; j++) { var a = map[JSON.stringify(p.slice(0, j))]; show[line(a.from)] = show[line(a.end - 1)] = true; }
    }
    if (q) entries.forEach(function (e) {
      var p = e[0], r = e[1];
      if (!p.length || inside(r, off) || (kept && !inside(r, kept.map(function (k) { return k[1]; }))) || p.join('/').toLowerCase().indexOf(q) < 0) return;
      keep(p, r);
    });
    else if (kept) kept.forEach(function (e) { keep(e[0], e[1]); });
    off.forEach(function (o) { for (var l = line(o.from); l <= line(o.end - 1); l++) show[l] = false; });
    var quiet = [];
    empty.forEach(function (o) { for (var l = line(o.from); l <= line(o.end - 1); l++) { if (show[l]) quiet[l] = true; show[l] = false; } });
    var out = [], from = -1;
    for (var l = 0; l <= show.length; l++) {
      if (from >= 0 && (l === show.length || show[l] || !quiet[l] !== !quiet[from])) { out.push(quiet[from] ? [from, l - 1, 'empty'] : [from, l - 1]); from = -1; }
      if (l < show.length && !show[l] && from < 0) from = l;
    }
    return out;
  }

  // The colors of a JSON editor (a CodeMirror overlay): keys, empty keys, {} and a text of {} or [].
  // (a string is read once, as a whole: a long text in a line stays fast)
  var keyOverlay = {
    token: function (s) {
      if (s.peek() === '"') {
        var m = s.match(/^"(?:[^"\\]|\\.)*"/);
        if (!m) { s.skipToEnd(); return null; }
        var rest = s.string.slice(s.pos), colon = /^\s*:\s*/.exec(rest);
        if (colon) { var v = rest.slice(colon[0].length); return /^\{\s*\}/.test(v) || EMPTY_TEXT.test(v) ? 'key emptykey' : 'key'; }
        return emptyText(m[0]) ? 'emptyobj' : null;
      }
      if (s.match(/^\{\s*\}/)) return 'emptyobj';
      while (s.next() != null && !s.match(/^(?=["{])/, false)) {}
      return null;
    }
  };

  // The path of the innermost entry at a character offset, e.g. ["extension", "views", "state-view"].
  function pathAt(text, offset) {
    var map = spans(text), best = [], size = Infinity;
    Object.keys(map).forEach(function (k) {
      var r = map[k];
      if (r.from <= offset && offset <= r.end && r.end - r.from < size) { size = r.end - r.from; best = JSON.parse(k); }
    });
    return best;
  }

  // Edits that make the text hold the given state, keeping comments and layout everywhere else.
  function patchText(text, target) {
    var edits = [];
    diff(parseJsonc(text), target).forEach(function (c) {
      var m = spans(text), key = JSON.stringify(c.path), parent = m[JSON.stringify(c.path.slice(0, -1))], e = null;
      if (c.type === 'updated' && m[key]) e = { from: m[key].start, to: m[key].end, insert: JSON.stringify(c.after) };
      else if (c.type === 'added' && parent && parent.obj) {
        var ins = JSON.stringify(c.path[c.path.length - 1]) + ': ' + JSON.stringify(c.after);
        var last = parent.members[parent.members.length - 1];
        e = last ? { from: last.end, to: last.end, insert: ', ' + ins } : { from: parent.start + 1, to: parent.end - 1, insert: ins };
      } else if (c.type === 'deleted' && parent && parent.obj) {
        var idx = parent.members.findIndex(function (x) { return x.key === c.path[c.path.length - 1]; }), mem = parent.members[idx];
        if (idx > 0) e = { from: parent.members[idx - 1].end, to: mem.end, insert: '' };
        else if (parent.members.length > 1) e = { from: mem.keyStart, to: parent.members[1].keyStart, insert: '' };
        else e = { from: parent.start + 1, to: parent.end - 1, insert: '' };
      }
      if (e) { text = text.slice(0, e.from) + e.insert + text.slice(e.to); edits.push(e); }
    });
    return { text: text, edits: edits };
  }

  function ago(iso, now) {
    var s = Math.max(0, Math.round(((now || Date.now()) - new Date(iso).getTime()) / 1000));
    if (s < 45) return 'just now';
    if (s < 3600) return Math.round(s / 60) + ' min ago';
    if (s < 86400) return Math.round(s / 3600) + ' h ago';
    return Math.round(s / 86400) + ' d ago';
  }

  // A commit records the whole state as text, plus what changed against its parent
  // (outputs, timings and test results filled in by the runtime do not count as changes).
  function makeCommit(parent, text, at) {
    var state = stripRuntime(parseJsonc(text));
    var base = parent ? stripRuntime(parseJsonc(parent.state)) : {};
    var changes = diff(base, state);
    return {
      n: parent ? parent.n + 1 : 1,
      parent: parent ? parent.n : null,
      at: at,
      state: text,
      summary: summarize(changes),
      paths: changes.slice(0, 100).map(function (c) { return c.type + ' ' + pathText(c.path); })
    };
  }
  function commitId(n) { return 'c' + String(n).padStart(6, '0'); }

  // Positions run over the commits, then the unsaved draft if there is one.
  function historyLength(commits, draft) { return commits.length + (draft !== null ? 1 : 0); }
  function step(pos, delta, commits, draft) {
    var last = historyLength(commits, draft) - 1;
    return Math.max(0, Math.min(last, pos + delta));
  }
  function textAt(pos, commits, draft) {
    return pos < commits.length ? commits[pos].state : draft;
  }
  // What the changes view compares at a position: the version before it, and it.
  function pairAt(pos, commits, draft) {
    var after = textAt(pos, commits, draft);
    var before = pos === 0 ? '{}' : textAt(pos - 1, commits, draft);
    return { before: parseJsonc(before), after: parseJsonc(after) };
  }

  // Every call goes through track(): its name, input, result or error, time taken, and related data
  // the call adds with ctx.relate({...}) (commit numbers, paths, positions).
  function createTracker(opts) {
    opts = opts || {};
    var now = opts.now || function () { return new Date().toISOString(); };
    var clock = opts.clock || function () { return Date.now(); };
    var records = [], seq = 0;
    var keep = opts.brief || function (v) { return v === undefined ? null : v; };
    function finish(rec, t0) {
      rec.ms = clock() - t0;
      records.push(rec);
      if (opts.onRecord) opts.onRecord(rec, records);
      return rec;
    }
    function track(name, input, fn) {
      var rec = { id: ++seq, name: name, at: now(), input: input === undefined ? null : input, ok: true, output: null, error: null, related: {} };
      var ctx = { id: rec.id, relate: function (o) { Object.keys(o).forEach(function (k) { rec.related[k] = o[k]; }); } };
      var t0 = clock(), out;
      try { out = fn(ctx); } catch (e) { rec.ok = false; rec.error = String(e && e.message || e); finish(rec, t0); throw e; }
      if (out && typeof out.then === 'function') {
        return out.then(function (v) { rec.output = keep(v); finish(rec, t0); return v; },
          function (e) { rec.ok = false; rec.error = String(e && (e.message || e.code) || e); finish(rec, t0); throw e; });
      }
      rec.output = keep(out);
      finish(rec, t0);
      return out;
    }
    return { track: track, records: records };
  }

  // Markdown as the docs use it: ``` fences (code, or ```svg diagrams) between parts made of lines.
  // mdText(mdParse(text)) gives the same text back, so an edit changes only what was edited.
  function mdParse(text) {
    return String(text).split('```').map(function (part, i) {
      if (!(i % 2)) return { kind: 'lines', lines: part.split('\n') };
      if (part.indexOf('svg') === 0) return { kind: 'svg', head: 'svg', text: part.slice(3), tail: '' };
      var m = /^([a-z]*\n)?([\s\S]*?)(\n?)$/.exec(part);
      return { kind: 'code', head: m[1] || '', text: m[2], tail: m[3] };
    });
  }
  function mdText(parts) {
    return parts.map(function (p) { return p.kind === 'lines' ? p.lines.join('\n') : p.head + p.text + p.tail; }).join('```');
  }
  // One line of markdown: its mark ("# ", "## ", "### ", "- ", "1. ") and its text.
  function mdLine(raw) {
    var m = /^(#{1,3} |- |\d+\. )?([\s\S]*)$/.exec(raw), mark = m[1] || '';
    var type = !mark ? (raw.trim() ? 'p' : 'blank') : mark.charAt(0) === '#' ? 'h' + (mark.length - 1) : mark === '- ' ? 'item' : 'step';
    return { mark: mark, text: m[2], type: type };
  }

  function clone(v) { return v === undefined ? undefined : JSON.parse(JSON.stringify(v)); }
  function walk(v, path, fn) {
    fn(v, path);
    if (v !== null && typeof v === 'object') Object.keys(v).forEach(function (k) { walk(v[k], path.concat(k), fn); });
  }
  // Paths are dotted, and keys can hold dots ("local.init", "CLAUDE.md"):
  // when a segment does not exist, it is joined with the next one and tried again.
  function getPath(obj, path) {
    var parts = String(path).split('.'), v = obj, i = 0;
    while (i < parts.length) {
      if (v === null || typeof v !== 'object') return undefined;
      var k = parts[i], j = i;
      while (!(k in v) && j < parts.length - 1) { j++; k += '.' + parts[j]; }
      if (!(k in v)) return undefined;
      v = v[k]; i = j + 1;
    }
    return v;
  }
  function setPath(obj, path, value) {
    var parts = String(path).split('.');
    // Prefer a parent that already has the key (the key may hold dots); otherwise the last segment is the key.
    for (var i = 1; i < parts.length; i++) {
      var parent = getPath(obj, parts.slice(0, i).join('.')), key = parts.slice(i).join('.');
      if (isObj(parent) && key in parent) { parent[key] = value; return; }
    }
    var p = parts.length > 1 ? getPath(obj, parts.slice(0, -1).join('.')) : obj;
    if (!isObj(p)) throw new Error('No object at ' + parts.slice(0, -1).join('.'));
    p[parts[parts.length - 1]] = value;
  }

  // Fields the runtime fills in while functions run; they are not part of what the owner edits.
  function stripRuntime(state) {
    var copy = clone(state);
    walk(copy, [], function (v, path) {
      if (path[path.length - 2] !== 'functions' || !isObj(v)) return;
      delete v.output; delete v.performance; delete v.errors;
      if (isObj(v.calls)) Object.keys(v.calls).forEach(function (k) { if (isObj(v.calls[k])) delete v.calls[k].output; });
      if (isObj(v.tests)) Object.keys(v.tests).forEach(function (k) { if (isObj(v.tests[k])) delete v.tests[k].result; });
    });
    return copy;
  }

  // A small, JSON-safe version of a value for logs and output fields.
  function brief(v) {
    if (v === undefined || typeof v === 'function') return null;
    if (typeof v === 'string') return v.length > 200 ? { type: 'text', length: v.length } : v;
    if (v === null || typeof v !== 'object') return v;
    if (typeof Node !== 'undefined' && v instanceof Node) return { type: 'element', tag: v.nodeName };
    var text;
    try { text = JSON.stringify(v); } catch (e) { return { type: 'object' }; }
    return text.length > 600 ? { type: Array.isArray(v) ? 'list' : 'object', keys: Object.keys(v).slice(0, 30) } : JSON.parse(text);
  }

  // Fills a view's html: ${...} expressions see the view's ui-data as d, and e() escapes text.
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function template(html, data) { return new Function('d', 'e', 'return `' + html + '`;')(data, esc); }

  // Checks a run against a function's expected-state-change: {path: rule}. Rules: "changes", "toggles",
  // "input" (becomes the input), "input.name" (becomes that input parameter), "same", "may change", or a value the path must hold. A path "*" allows any change;
  // otherwise a change outside the listed paths is reported. Paths in `ignore` (what nested calls changed) are not counted.
  function checkStateChange(spec, before, after, input, ignore) {
    var fails = [], keys = Object.keys(spec || {});
    keys.forEach(function (p) {
      if (p === '*') return;
      var rule = spec[p], b = getPath(before, p), a = getPath(after, p);
      if (rule === 'may change') return;
      if (rule === 'changes' && same(a, b)) fails.push(p + ' did not change');
      else if (rule === 'toggles' && a !== !b) fails.push(p + ' did not toggle');
      else if (rule === 'input' && !same(a, input)) fails.push(p + ' is ' + JSON.stringify(a) + ', expected the input ' + JSON.stringify(input));
      else if (/^input\./.test(rule) && !same(a, getPath(input, rule.slice(6)))) fails.push(p + ' is ' + JSON.stringify(a) + ', expected ' + rule + ' ' + JSON.stringify(getPath(input, rule.slice(6))));
      else if (rule === 'same' && !same(a, b)) fails.push(p + ' changed');
      else if (['changes', 'toggles', 'input', 'same'].indexOf(rule) < 0 && !/^input\./.test(rule) && !same(a, rule)) fails.push(p + ' is ' + JSON.stringify(a) + ', expected ' + JSON.stringify(rule));
    });
    if (keys.indexOf('*') < 0) diff(before, after).forEach(function (c) {
      var p = pathText(c.path);
      if ((ignore || []).some(function (k) { return p === k || p.indexOf(k + '.') === 0; })) return;
      if (!keys.some(function (k) { return p === k || p.indexOf(k + '.') === 0; })) fails.push('unexpected change: ' + c.type + ' ' + p);
    });
    return fails;
  }

  // Checks a test's expect block: output (fields that must match), output-has (keys), dom / dom-absent (selectors),
  // state (paths that must hold these values after the run), state-changed (paths the run must have changed).
  function checkExpect(expect, out, hasDom, st) {
    var fails = [];
    st = st || {};
    if (expect.state) Object.keys(expect.state).forEach(function (p) {
      var v = st.get ? st.get(p) : undefined;
      if (!same(v, expect.state[p])) fails.push(p + ' is ' + JSON.stringify(v) + ', expected ' + JSON.stringify(expect.state[p]));
    });
    (expect['state-changed'] || []).forEach(function (p) {
      if (!(st.changed || []).some(function (c) { return c === p || c.indexOf(p + '.') === 0; })) fails.push(p + ' did not change');
    });
    if (expect.output !== undefined) Object.keys(expect.output).forEach(function (k) {
      if (!out || !same(out[k], expect.output[k])) fails.push('output.' + k + ' is ' + JSON.stringify(out && out[k]) + ', expected ' + JSON.stringify(expect.output[k]));
    });
    (expect['output-has'] || []).forEach(function (k) { if (!out || !(k in out)) fails.push('output has no ' + k); });
    (expect.dom || []).forEach(function (sel) { if (!hasDom(sel)) fails.push('no element ' + sel); });
    (expect['dom-absent'] || []).forEach(function (sel) { if (hasDom(sel)) fails.push('element still there: ' + sel); });
    return fails;
  }

  return {
    clone: clone, walk: walk, getPath: getPath, setPath: setPath, stripRuntime: stripRuntime,
    parseJsonc: parseJsonc, stripComments: stripComments, autofix: autofix,
    mdParse: mdParse, mdText: mdText, mdLine: mdLine,
    spans: spans, kindOf: kindOf, filterLines: filterLines, keyOverlay: keyOverlay, pathAt: pathAt, patchText: patchText, ago: ago, emptyText: emptyText,
    brief: brief, template: template, esc: esc, checkExpect: checkExpect, checkStateChange: checkStateChange,
    diff: diff, summarize: summarize, changesView: changesView,
    makeCommit: makeCommit, commitId: commitId,
    historyLength: historyLength, step: step, textAt: textAt, pairAt: pairAt,
    createTracker: createTracker
  };
});
