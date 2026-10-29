import json, os, re

# Run from the repo: python3 gen/make_state.py.
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
exec(open(REPO + '/gen/style_part.py').read())          # STYLE: the page styles (index-view html)

def fn(docs, code="", calls=None, tests=None, imports=None, expected=None, input_=None):
    # Each import line of the code has an entry in imports that says where it comes from.
    found = {}
    for m in re.finditer(r"^import \w+ from '([^']+)';$", code, re.M):
        found[m.group(1)] = WHERE[m.group(1)]
    found.update(imports or {})
    return {
        "input": input_ if input_ is not None else {},
        "output": {},
        "imports": found,
        "tests": tests or {},
        "expected-state-change": expected or {},
        "docs": docs,
        "performance": {},
        "code": code,
        "calls": calls or {},
    }

def sig(name, params, body):
    """A function as it looks in code: import lines for what it uses, then async function name({ params }) { body }."""
    body = re.sub(r"const core = imports\['state-core'\], ", "const ", body)
    body = re.sub(r"const core = imports\['state-core'\];\n", "", body)
    assert "imports[" not in body, name
    uses = [("os", r"\bos\."), ("ctx", r"\bctx\."), ("core", r"\bcore\."), ("CodeMirror", r"\bCodeMirror\b"), ("js_beautify", r"\bjs_beautify\b"), ("html_beautify", r"\bhtml_beautify\b")]
    lines = ["import %s from '%s';" % (n, MODULE[n]) for n, rx in uses if re.search(rx, body)]
    p = '{ ' + ', '.join(params) + ' }' if params else ''
    head = '\n'.join(lines) + '\n\n' if lines else ''
    return head + 'async function ' + name + '(' + p + ') {\n' + '\n'.join(('  ' + l) if l else '' for l in body.strip('\n').split('\n')) + '\n}'

# The libraries are files of the repo (vendor/), not minified; the page loads them from its own files.
CM = "vendor/codemirror/5.65.16/"
CM_SCRIPTS = ["lib/codemirror.js", "mode/javascript/javascript.js", "mode/xml/xml.js", "mode/css/css.js", "mode/htmlmixed/htmlmixed.js", "mode/markdown/markdown.js",
              "addon/fold/foldcode.js", "addon/fold/foldgutter.js", "addon/fold/brace-fold.js", "addon/edit/matchbrackets.js", "addon/edit/closebrackets.js"]
CORE_SRC = open(REPO + '/state-core.js').read()
SV = "extension.views.state-view"
DV = "extension.views.docs-view"
HV = "extension.views.header-view"
TV = "extension.views.timeline-view"
NV = "extension.views.notes-view"
P = SV + ".ui-data"
CORE = SV + ".functions.local.init.imports.state-core"   # the one copy of state-core's source
CM_URLS = SV + ".functions.local.init.imports.codemirror" # the one list of CodeMirror's script URLs
MODULE = {"os": "os", "ctx": "ctx", "core": "state-core", "CodeMirror": "codemirror", "js_beautify": "js-beautify", "html_beautify": "js-beautify"}
# js-beautify formats code for reading: beautify.js gives js_beautify, beautify-html.js gives html_beautify (it uses the other two).
JSB = "vendor/js-beautify/1.15.1/"
WHERE = {"os": "index.html", "ctx": "index.html", "state-core": CORE, "codemirror": CM_URLS,
         "js-beautify": [JSB + "beautify.js", JSB + "beautify-css.js", JSB + "beautify-html.js"]}

# ---------- styles: formatted to read, CodeMirror's base styles inline (from vendor/; the page keeps all its styles in index-view) ----------
cm_css = re.sub(r"/\*.*?\*/", "", open(REPO + "/" + CM + "lib/codemirror.css").read(), flags=re.S)
cm_css = re.sub(r"\}\s*", "}\n", re.sub(r"\s+", " ", cm_css)).strip()
STYLE = STYLE.replace("__CMCSS__", cm_css)
STYLE = STYLE.replace("[hidden]{display:none!important}", "[hidden]{display:none!important}\nhtml,body{height:100%;margin:0}")
STYLE = STYLE.replace("#header-view{position:sticky;", "#header-view{gap:8px;position:sticky;")
STYLE = STYLE.replace(".cm-s-agent .cm-tag{color:var(--accent)}", """.cm-s-agent .cm-tag{color:var(--accent)}
.cm-s-agent .cm-keyword{color:var(--atom);font-weight:500}
.cm-s-agent .cm-def{color:var(--accent);font-weight:500}
.cm-s-agent .cm-variable{color:var(--fg)}
.cm-s-agent .cm-variable-2{color:var(--accent)}
.cm-s-agent .cm-variable-3,.cm-s-agent .cm-type{color:var(--num)}
.cm-s-agent .cm-property{color:var(--key)}
.cm-s-agent .cm-operator{color:var(--muted)}
.cm-s-agent .cm-string-2{color:var(--warn)}
.cm-s-agent .cm-builtin,.cm-s-agent .cm-qualifier{color:var(--num)}
.cm-s-agent .cm-meta{color:var(--muted)}""")
STYLE = STYLE.replace("#sv-viewer-code,#sv-viewer-view{", """#docs-view{flex:1;min-height:0;padding-block:12px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
.docs{height:100%;display:grid;grid-template-columns:220px 1fr;gap:12px}
@media (max-width:640px){.docs{grid-template-columns:1fr}}
.docs-list{display:flex;flex-direction:column;gap:4px;min-width:0}
.doc-link{text-align:left;padding:7px 10px;border-radius:7px;border:1px solid transparent;background:none;color:var(--fg);cursor:pointer;font:13px var(--mono)}
.doc-link[aria-current="true"]{background:var(--sel);border-color:var(--accent);color:var(--accent)}
.doc{overflow:auto;background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:16px 20px;line-height:1.55;font-size:14px}
.doc h2{margin:0 0 12px;font-size:18px}
.doc h3{margin:18px 0 8px;font-size:15px}
.doc p{margin:0 0 6px}
.doc .item{padding-left:14px;position:relative}
.doc .item::before{content:"•";position:absolute;left:2px;color:var(--muted)}
.doc .step{padding-left:4px}
.doc .code{margin:6px 0 12px;padding:10px 12px;background:var(--gutter);border:1px solid var(--line);border-radius:8px;font:12px/1.55 var(--mono);overflow:auto;white-space:pre}
.diagram{margin:8px 0 16px}
.diagram svg{width:100%;height:auto;max-width:780px;display:block}
.diagram .box{fill:var(--panel);stroke:var(--line);stroke-width:1.2}
.diagram .group{fill:var(--bg);stroke:var(--line);stroke-width:1.2}
.diagram .key{fill:var(--sel);stroke:var(--accent);stroke-width:1.2}
.diagram text{fill:var(--fg);font:12px var(--sans)}
.diagram .title{font-weight:600;font-size:13px}
.diagram .mono{font:11px var(--mono);fill:var(--muted)}
.diagram .flow{stroke:var(--accent);stroke-width:1.4;fill:none}
.diagram .num{fill:var(--accent);font-weight:600}
.diagram .head{fill:var(--accent)}
.sv-bar{flex-wrap:nowrap;gap:12px}
.sv-bar .st-kinds{flex:none;flex-wrap:nowrap}
.sv-sep{width:1px;height:22px;background:var(--line);margin:0 2px;flex:none}
.sv-check{display:flex;align-items:center;gap:6px;flex:none;font:13px var(--sans);color:var(--fg);cursor:pointer;white-space:nowrap}
.sv-check input{width:15px;height:15px;margin:0;accent-color:var(--accent);cursor:pointer}
.sv-group{display:flex;gap:8px;align-items:center;flex:none}
.sv-filter{position:relative;flex:1;min-width:120px;max-width:560px;margin:0 auto}
#sv-filter-input,#st-filter-input{width:100%;box-sizing:border-box;height:34px;padding:0 12px 0 32px;border:1px solid var(--line);border-radius:9px;background:var(--panel) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='none' stroke='%238b95a5' stroke-width='1.6' stroke-linecap='round'%3E%3Ccircle cx='7' cy='7' r='4.5'/%3E%3Cpath d='m10.5 10.5 3 3'/%3E%3C/svg%3E") no-repeat 10px 50%;color:var(--fg);font:13px var(--sans);outline:none}
#sv-filter-input:focus,#st-filter-input:focus{border-color:var(--accent);box-shadow:0 0 0 3px var(--sel)}
.sv-filter{display:flex;gap:12px;align-items:center}
#sv-filter-input,#st-filter-input{flex:1;min-width:80px}
.st-filter{flex:none;max-width:none;margin:10px 0 0;flex-wrap:wrap}
.sv-switches{display:flex;gap:10px;flex:none}
.sv-switch{display:flex;align-items:center;gap:6px;border:0;background:none;padding:0;color:var(--muted);font:12px var(--sans);cursor:pointer}
.sv-switch[aria-checked="true"]{color:var(--fg)}
.sv-track{position:relative;width:26px;height:15px;border-radius:8px;background:var(--line);transition:background .15s}
.sv-track::after{content:"";position:absolute;top:2px;left:2px;width:11px;height:11px;border-radius:50%;background:#fff;transition:transform .15s}
.sv-switch[aria-checked="true"] .sv-track{background:var(--accent)}
.sv-switch[aria-checked="true"] .sv-track::after{transform:translateX(11px)}
.sv-switch:focus-visible{outline:2px solid var(--accent);outline-offset:3px;border-radius:4px}
.sv-hidden{color:var(--muted);font:11px var(--sans);background:var(--gutter);border-radius:4px;padding:0 6px}
.sv-foot{display:flex;align-items:center;gap:12px;min-height:22px;padding-top:2px;flex-wrap:wrap}
.sv-foot .status{margin-left:auto}
@media (max-width:1100px){.sv-bar{flex-wrap:wrap}.sv-filter{order:3;flex-basis:100%;max-width:none}.sv-bar .st-kinds{flex-wrap:wrap}.sv-group#sv-right{margin-left:auto}}
@media (max-width:1100px){.sv-bar .st-kinds{flex:1 1 0;min-width:0}}
@media (max-width:640px){.sv-filter{flex-wrap:wrap}.sv-checks{flex-wrap:wrap}}
#st-filter{order:0;flex-basis:auto}
#st-filter .st-kinds{flex-wrap:wrap;flex:1 1 auto;min-width:0}
#timeline-view{flex:0 1 auto;min-height:0;overflow:auto;display:flex;flex-direction:column;gap:6px;padding-block:10px 8px;border-bottom:1px solid var(--line);background:var(--gutter);padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
.sv-checks{display:flex;gap:12px;align-items:center;flex:none}
#state-view > #tl-detail{min-height:240px}
.sv-block{font:12px var(--sans);color:var(--muted)}
.sv-block b{color:var(--fg);font-weight:600}
.tl-step.pin-left{position:sticky;left:0;z-index:2;opacity:1}
.tl-step.pin-right{position:sticky;right:0;z-index:2;opacity:1}
.tl-step.pin-left,.tl-step.pin-right{box-shadow:0 2px 10px rgba(0,0,0,.14)}
.tl-step.pin-left.on,.tl-step.pin-right.on{box-shadow:0 0 0 3px var(--sel),0 2px 10px rgba(0,0,0,.14)}
#notes-view{flex:1;min-height:0;display:flex;flex-direction:column;padding-block:12px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
.notes-bar{display:flex;align-items:center;gap:8px;font:600 16px var(--sans)}
.notes-bar b{margin-right:auto}
.notes-bar .btn{width:36px;padding:0;display:inline-grid;place-items:center}
.notes-settings{display:flex;flex-wrap:wrap;gap:12px 20px;align-items:center;margin:10px 0 0;padding:10px 12px;border:1px solid var(--line);border-radius:12px;background:var(--panel);font:13px var(--sans)}
.notes-settings label{display:flex;gap:8px;align-items:center}
.notes-settings select,.notes-settings input{height:30px;padding:0 8px;border:1px solid var(--line);border-radius:8px;background:var(--bg);color:var(--fg);font:13px var(--sans)}
.notes-settings p{flex-basis:100%;margin:0;color:var(--muted);font-size:12px}
.notes-add{display:flex;gap:8px;align-items:flex-end;margin:10px 0 0}
.notes-add textarea{flex:1;min-height:44px;max-height:30vh;resize:vertical;box-sizing:border-box;padding:8px 10px;border:1px solid var(--line);border-radius:10px;background:var(--panel);color:var(--fg);font:14px/1.45 var(--sans)}
.notes-msg{margin:8px 0 0;padding:6px 10px;border-radius:8px;background:var(--sel);font:13px var(--sans)}
.notes-list{flex:1;min-height:0;overflow:auto;margin:10px 0;padding:10px;border:1.5px solid var(--line);border-radius:16px;display:flex;flex-direction:column;gap:10px}
.notes-empty{margin:auto;color:var(--muted);font:14px var(--sans)}
.note{border:1.5px solid var(--line);border-radius:14px;padding:10px 12px;background:var(--panel)}
.note-top{display:flex;gap:16px;align-items:flex-start;flex-wrap:wrap}
.note-body{flex:1 1 280px;min-width:0}
.note-text{width:100%;min-height:72px;resize:vertical;box-sizing:border-box;padding:8px 10px;border:1px solid var(--line);border-radius:10px;background:var(--bg);color:var(--fg);font:14px/1.45 var(--sans)}
.note-media audio,.note-media video{display:block;width:100%;max-height:240px;border-radius:8px}
.note-gone{color:var(--muted);font:13px var(--sans)}
.note-actions{display:flex;flex-direction:column;gap:6px;align-items:stretch}
.note-actions .btn,.note-view .btn,.notes-foot .btn,.notes-add .btn{height:30px;padding:0 12px;font:13px var(--sans);white-space:nowrap;width:auto}
.note-view{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:10px;font:13px var(--sans)}
.note-view label{display:flex;gap:8px;align-items:center}
.note-view code{font:12px var(--mono)}
.note-meta{margin-left:auto;color:var(--muted);font:11px var(--mono)}
.note-state{margin:8px 0 0 26px;max-height:260px;overflow:auto;padding:8px 10px;border-radius:8px;background:var(--gutter);font:12px/1.5 var(--mono);white-space:pre}
.notes-foot{display:flex;justify-content:flex-end}
.rec-menu{display:flex;flex-direction:column;gap:2px;padding:4px;background:var(--panel);border:1px solid var(--line);border-radius:12px;box-shadow:0 10px 30px rgba(0,0,0,.2)}
.rec-menu button{display:flex;gap:10px;align-items:center;border:0;background:none;color:var(--fg);font:13px var(--sans);padding:8px 12px;border-radius:8px;cursor:pointer;text-align:left}
.rec-menu button:hover,.rec-menu button:focus-visible{background:var(--sel);outline:none}
.rec-menu button span{flex:none;width:18px;height:18px;border-radius:50%;display:grid;place-items:center;font:700 10px var(--mono);background:var(--gutter);color:var(--muted)}
.tl-bar{display:flex;align-items:center;gap:8px;flex-wrap:wrap;position:relative}
.tl-flows{position:absolute;top:calc(100% + 6px);right:0;z-index:8;width:min(420px,100%);background:var(--panel);border:1px solid var(--line);border-radius:10px;box-shadow:0 12px 32px rgba(0,0,0,.16);padding:6px}
.tl-flows-head{font:600 11px var(--sans);text-transform:uppercase;letter-spacing:.05em;color:var(--muted);padding:6px 8px}
.tl-flow{display:flex;gap:10px;align-items:center;padding:6px 8px;border-radius:8px}
.tl-flow:hover{background:var(--sel)}
.tl-flow-text{display:flex;flex-direction:column;gap:2px;min-width:0;font:13px var(--sans)}
.tl-flow-text span{font:11px var(--mono);color:var(--muted);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.tl-none{padding:10px 8px;color:var(--muted);font-size:13px}
.st-bar .st-close{margin-left:auto}
.tl-explain{display:grid;grid-template-columns:minmax(110px,.55fr) 1fr 1fr;gap:1px;background:var(--line);border:1px solid var(--line);border-radius:8px;overflow:hidden;margin:8px 0 4px}
.tl-explain>div{background:var(--panel);padding:8px 10px;font:13px/1.45 var(--sans)}
.tl-explain>.tl-side-head{font:600 11px var(--sans);text-transform:uppercase;letter-spacing:.05em;color:var(--muted);background:var(--gutter)}
.tl-explain>.tl-side-part{font-weight:600}
.tl-explain>.tl-side-before{background:var(--del-bg)}
.tl-explain>.tl-side-now{background:var(--add-bg)}
.tl-files{display:grid;grid-template-columns:1fr 1fr;gap:8px;min-width:0}
.tl-netenv{display:grid;grid-template-columns:minmax(0,3fr) minmax(0,2fr);gap:12px;align-items:start;margin-top:6px}
.tl-panel{border:1px solid var(--line);border-radius:12px;padding:12px;background:var(--panel);min-width:0}
.tl-panel h3{margin:0 0 4px;font:600 14px var(--sans)}
.tl-panel h4{margin:14px 0 6px;font:600 11px var(--sans);text-transform:uppercase;letter-spacing:.05em;color:var(--muted)}
.tl-req{border:1px solid var(--line);border-radius:9px;padding:8px 10px;margin:0 0 6px;background:var(--bg);min-width:0}
.tl-req.can-open>.tl-req-top{cursor:pointer}
.tl-req-top{display:flex;gap:8px;align-items:baseline;min-width:0}
.tl-req-top b{font:600 13px var(--mono);white-space:nowrap}
.tl-req-url{font:11px var(--mono);color:var(--muted);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;min-width:0}
.tl-chips{display:flex;flex-wrap:wrap;gap:6px;margin-top:6px}
.tl-chip{font:11px var(--mono);padding:2px 6px;border-radius:5px;background:var(--gutter);color:var(--fg)}
.tl-chip.bad{background:var(--del-bg)}.tl-chip.good{background:var(--add-bg)}.tl-chip.quiet{color:var(--muted)}
.tl-used{font:12px/1.4 var(--sans);color:var(--muted);margin-top:5px}
.tl-env-row{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.3fr);gap:8px;padding:4px 0;border-bottom:1px dashed var(--line);font:12px var(--mono)}
.tl-env-row>span:first-child{color:var(--muted);overflow-wrap:anywhere}
.tl-env-row>span:last-child{overflow-wrap:anywhere}
.tl-env-row.changed>span:last-child{background:var(--upd-bg);border-radius:4px;padding:0 4px}
.tl-was{display:block;color:var(--muted);font-size:11px}
@media (max-width:760px){.tl-netenv{grid-template-columns:1fr}}
.ar-head{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin:4px 0 10px}
.ar-lanes{overflow-x:auto;padding:4px 2px 10px;min-width:0}
.ar-lane{display:flex;gap:10px;align-items:flex-start;min-height:20px}
.ar-lane+.ar-lane{margin-top:10px}
.ar-lane-name{flex:none;width:92px;font:600 11px var(--sans);text-transform:uppercase;letter-spacing:.05em;color:var(--muted);padding-top:8px}
.ar-lane-name b{display:block;text-transform:none;letter-spacing:0;font:600 12px var(--mono);color:#7c3aed;overflow-wrap:anywhere;margin-top:2px}
.ar-branch{flex:none;min-height:44px;border-top:2px dashed #a78bfa;margin-top:18px;padding:8px 10px 0 0;box-sizing:border-box}
.ar-branch span{display:block;font:12px/1.45 var(--sans);color:var(--muted);max-width:560px}
.ar-card.step.sub{border-color:#c4b5fd;background:color-mix(in srgb,#7c3aed 5%,var(--panel))}
.ar-card li.src-mcp,.ar-card li.src-skill,.ar-card li.src-workflow,.ar-card li.src-subagent{font-weight:600}
.ar-card li.src-mcp::marker{color:#2563eb}.ar-card li.src-skill::marker{color:#15803d}.ar-card li.src-workflow::marker{color:#c2410c}.ar-card li.src-subagent::marker{color:#7c3aed}
.tl-chip.src-mcp{background:#dbeafe;color:#1d4ed8}.tl-chip.src-skill{background:#dcfce7;color:#15803d}.tl-chip.src-workflow{background:#ffedd5;color:#c2410c}.tl-chip.src-subagent{background:#ede9fe;color:#6d28d9}
@media (prefers-color-scheme:dark){.tl-chip.src-mcp{background:#172554;color:#93c5fd}.tl-chip.src-skill{background:#052e16;color:#86efac}.tl-chip.src-workflow{background:#431407;color:#fdba74}.tl-chip.src-subagent{background:#2e1065;color:#c4b5fd}}
.st-kind.src-mcp{border-left:4px solid #2563eb}.st-kind.src-skill{border-left:4px solid #15803d}.st-kind.src-workflow{border-left:4px solid #c2410c}.st-kind.src-subagent{border-left:4px solid #7c3aed}.st-kind.src-main{border-left:4px solid var(--accent)}
.ar-tabs{display:flex;gap:0;border-bottom:1px solid var(--line);margin:10px 0}
#recorder-view{flex:none;margin-top:auto;position:relative;z-index:60;display:flex;justify-content:flex-end;align-items:center;padding-block:6px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-bottom:max(6px,env(safe-area-inset-bottom,0px));background:var(--panel);border-top:1px solid var(--line)}
.rec-pop{position:absolute;right:max(16px,env(safe-area-inset-right,0px));bottom:calc(100% + 8px);display:flex;flex-direction:column;align-items:flex-end;gap:10px;pointer-events:none}
.rec-pop>*{pointer-events:auto}
.rec-btn{width:52px;height:52px;border-radius:50%;border:0;background:#dc2626;color:#fff;display:grid;place-items:center;cursor:pointer;box-shadow:0 6px 18px rgba(0,0,0,.25)}
.rec-btn:hover{background:#b91c1c}
.rec-btn:focus-visible{outline:3px solid var(--accent);outline-offset:3px}
.rec-btn[aria-pressed="true"]{animation:rec-pulse 1.4s infinite}
@keyframes rec-pulse{0%{box-shadow:0 0 0 0 rgba(220,38,38,.6)}70%{box-shadow:0 0 0 14px rgba(220,38,38,0)}100%{box-shadow:0 0 0 0 rgba(220,38,38,0)}}
.rec-card{width:min(400px,calc(100vw - 40px));max-height:60vh;overflow:auto;box-sizing:border-box;background:var(--panel);border:1px solid var(--line);border-radius:14px;box-shadow:0 10px 30px rgba(0,0,0,.2);padding:10px 12px;font:13px var(--sans);color:var(--fg)}
.rec-card-head{display:flex;align-items:center;gap:8px}
.rec-card-head span{color:var(--muted);flex:1;font:12px var(--mono)}
.rec-card-head .btn{height:30px;font:13px var(--sans);padding:0 10px;white-space:nowrap}
#rec-close{width:30px;padding:0}
#rec-save{width:auto}
.rec-card video,.rec-card audio{display:block;width:100%;margin:8px 0;border-radius:8px}
.rec-sel{margin:4px 0 2px;padding:0;list-style:none;font:12px/1.5 var(--mono)}
.rec-sel li{display:flex;gap:8px;padding:2px 0;border-top:1px dashed var(--line)}
.rec-sel span{color:var(--muted);flex:none}
.rec-sel code{overflow-wrap:anywhere;font:inherit}
.rec-error{max-width:min(360px,calc(100vw - 40px));background:#fee2e2;color:#991b1b;border-radius:10px;padding:8px 10px;font:12px/1.4 var(--sans)}
.rec-timer{display:inline-flex;align-items:center;gap:6px;font:600 13px var(--mono);color:#dc2626;margin-left:auto;padding:0 6px}
.rec-timer::before{content:"";width:9px;height:9px;border-radius:50%;background:#dc2626;animation:rec-blink 1s infinite}
@keyframes rec-blink{50%{opacity:.2}}
.rec-hover{position:fixed;z-index:59;pointer-events:none;border:2px solid #dc2626;border-radius:4px;background:rgba(220,38,38,.06);box-sizing:border-box}
.rec-hover.picked{border-color:#7c3aed;background:rgba(124,58,237,.08)}
.rec-label{position:fixed;z-index:61;pointer-events:none;max-width:min(680px,calc(100vw - 8px));box-sizing:border-box;background:#111827;color:#fff;font:12px/18px var(--mono);padding:2px 8px;border-radius:6px;overflow-wrap:anywhere}
html.rec-select,html.rec-select *{cursor:crosshair!important}
html.rec-select #recorder-view,html.rec-select #recorder-view *{cursor:pointer!important}
.ar-tabs button{font:600 13px var(--sans);border:0;border-bottom:2px solid transparent;background:none;color:var(--muted);padding:6px 14px;cursor:pointer;margin-bottom:-1px}
.ar-tabs button[aria-selected="true"]{color:var(--accent);border-bottom-color:var(--accent)}
.ar-by{margin-bottom:10px}
.ar-views{margin:2px 0 12px}
.ar-views button{font-size:14px;padding:8px 18px}
.ar-index{border:1px solid var(--line);border-radius:14px;background:var(--panel);padding:14px 16px;margin-bottom:12px}
.ar-index h3{margin:0 0 6px;font:600 16px var(--sans)}
.ar-summary{margin:0 0 10px;font:14px/1.55 var(--sans);max-width:900px}
.ar-actions{border-radius:10px;padding:8px 12px;background:var(--add-bg);font:13px/1.5 var(--sans);margin-bottom:10px}
.ar-actions.need{background:#fef3c7;color:#78350f}
.ar-actions ol{margin:4px 0 0;padding-left:20px}
@media (prefers-color-scheme:dark){.ar-actions.need{background:#422006;color:#fde68a}}
.ar-scope{display:flex;align-items:center;gap:10px}
.ar-scope .btn,.ar-to-details{height:26px;width:auto;padding:0 10px;font:12px var(--sans)}
.ar-legend{display:flex;gap:12px;margin:4px 0 8px;font:12px var(--mono)}
.ar-key::before{content:"";display:inline-block;width:9px;height:9px;border-radius:2px;margin-right:5px;vertical-align:-1px;background:currentColor}
.ar-key.added{color:#15803d}.ar-key.updated{color:#b45309}.ar-key.deleted{color:#b91c1c}.ar-key.read{color:#2563eb}
.kv-item.read{color:#2563eb;background:color-mix(in srgb,#2563eb 7%,transparent)}
.kv-item.on.read{color:#fff;background:var(--accent)}
.tl-chip.read{background:#dbeafe;color:#1d4ed8}
.ar-flow{list-style:none;margin:14px 0 0;padding:0 0 0 6px}
.ar-flow-step{position:relative;padding:0 0 14px 34px;border-left:2px solid var(--line);margin-left:12px}
.ar-flow-step:last-child{border-left-color:transparent}
.ar-flow-step.sub{border-left-style:dashed;border-left-color:#a78bfa}
.ar-flow-head{display:flex;flex-wrap:wrap;align-items:center;gap:8px;width:100%;border:0;background:none;color:var(--fg);text-align:left;padding:0;cursor:pointer;font:13px var(--sans)}
.ar-flow-head b{font-weight:600}
.ar-flow-num{position:absolute;left:-14px;top:-2px;width:26px;height:26px;border-radius:50%;display:grid;place-items:center;background:var(--accent);color:#fff;font:700 12px var(--mono)}
.ar-flow-step.sub .ar-flow-num{background:#7c3aed}
.ar-flow-step.on .ar-flow-num{box-shadow:0 0 0 4px var(--sel)}
.ar-flow-meta{margin-left:auto;color:var(--muted);font:11px var(--mono)}
.ar-flow-why{margin:4px 0 0;color:var(--muted);font:13px/1.45 var(--sans);max-width:900px}
.ar-flow-step.on{background:linear-gradient(90deg,var(--sel),transparent 70%);border-radius:0 10px 10px 0}
.ar-flow-files{display:flex;flex-wrap:wrap;gap:6px;margin:6px 0}
.tl-chip.ar-file.added{background:var(--add-bg)}.tl-chip.ar-file.updated{background:var(--upd-bg)}.tl-chip.ar-file.deleted{background:var(--del-bg)}.tl-chip.ar-file.read{background:#dbeafe;color:#1d4ed8}
.kv-item.ar-item{display:flex;align-items:center;gap:6px}
.ar-item-name{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis}
.ar-srcs{display:flex;gap:3px;flex:none}
.ar-srcs .tl-chip{font-size:10px;padding:0 5px;line-height:16px}
.kv-item.on .ar-srcs .tl-chip{background:rgba(255,255,255,.25);color:#fff}
.ar-card{flex:none;width:230px;border:1px solid var(--line);border-radius:12px;background:var(--panel);padding:9px 11px;font:12px/1.4 var(--sans)}
.ar-card.start{width:170px;border-color:var(--accent);text-align:center}
.st-kinds{display:flex;flex-wrap:wrap;gap:6px;align-items:center}
.st-kind{font:13px var(--sans);border:1px solid var(--line);background:var(--panel);color:var(--fg);border-radius:9px;height:34px;padding:0 12px;cursor:pointer}
.st-kind:hover{border-color:var(--accent)}
.st-kind[aria-pressed="true"]{background:var(--accent);border-color:var(--accent);color:#fff}
.kv{display:grid;grid-template-columns:minmax(200px,300px) minmax(0,1fr);gap:12px;align-items:start}
@media (max-width:760px){.kv{grid-template-columns:1fr}}
.kv-tree{border:1px solid var(--line);border-radius:12px;background:var(--panel);padding:8px 6px;max-height:620px;overflow:auto;font:12px/1.5 var(--mono)}
.kv-tree summary{cursor:pointer;padding:2px 4px;font-weight:600;white-space:nowrap}
.kv-item{display:block;width:100%;text-align:left;border:0;background:none;color:var(--fg);font:12px/1.5 var(--mono);padding:2px 4px;border-radius:6px;cursor:pointer;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.kv-item:hover{background:var(--sel)}
.kv-item.on{background:var(--accent);color:#fff}
.kv-item.added,.kv-tree summary.added{color:#15803d}.kv-item.updated,.kv-tree summary.updated{color:#b45309}.kv-item.deleted{color:#b91c1c;text-decoration:line-through}
.kv-item.on.added,.kv-item.on.updated,.kv-item.on.deleted{color:#fff}
.kv-main{min-width:0;display:flex;flex-direction:column;gap:8px}
.kv-head{display:flex;flex-wrap:wrap;gap:6px;align-items:center;font:12px var(--mono);overflow-wrap:anywhere}
.kv-tabs{display:flex;gap:4px}
.kv-tabs button{font:13px var(--sans);border:1px solid var(--line);background:var(--panel);color:var(--fg);border-radius:8px;padding:4px 12px;cursor:pointer}
.kv-tabs button[aria-selected="true"]{background:var(--accent);border-color:var(--accent);color:#fff}
.tl-viewer{position:fixed;inset:24px;z-index:30;display:flex;flex-direction:column;gap:8px;background:var(--bg);border:1px solid var(--line);border-radius:14px;box-shadow:0 12px 40px rgba(0,0,0,.25);padding:12px}
.tl-viewer-bar{display:flex;gap:8px;align-items:center;font:12px var(--mono);overflow-wrap:anywhere}
.tl-viewer-bar span{flex:1}
.tl-viewer .fv{flex:1;min-height:0}
.tl-viewer .fv-body{height:auto;flex:1;min-height:0}
.fv{display:flex;flex-direction:column;border:1px solid var(--line);border-radius:14px;background:var(--panel);overflow:hidden;box-shadow:0 1px 2px rgba(0,0,0,.04)}
.fv .fv-badge.fv-badge-pseudo{background:#7c3aed;font-size:14px}
.ps-body{padding:14px 16px 18px;overflow:auto;max-height:620px}
.ps-docs{margin:0 0 12px;padding:10px 12px;border-left:3px solid var(--accent);background:var(--gutter);border-radius:0 8px 8px 0;font:13px/1.55 var(--sans);color:var(--fg)}
.ps-lines{margin:0;padding:0;list-style:none;counter-reset:ps;font:13px/1.75 var(--mono)}
.ps-line{display:flex;align-items:baseline;counter-increment:ps;border-radius:6px;padding:0 8px 0 0}
.ps-line:hover{background:var(--sel)}
.ps-line::before{content:counter(ps);flex:none;width:34px;text-align:right;padding-right:12px;color:var(--muted);font-size:11px}
.ps-guide{flex:none;width:20px;align-self:stretch;border-left:1px solid var(--line);margin-left:6px}
.ps-kw{flex:none;font-weight:700;font-size:11px;letter-spacing:.04em;padding:1px 6px;border-radius:5px;margin-right:8px}
.ps-flow{background:#ede9fe;color:#6d28d9}.ps-call{background:#dbeafe;color:#1d4ed8}.ps-exit{background:#fee2e2;color:#b91c1c}.ps-act{background:#dcfce7;color:#15803d}
@media (prefers-color-scheme:dark){.ps-flow{background:#2e1065;color:#c4b5fd}.ps-call{background:#172554;color:#93c5fd}.ps-exit{background:#450a0a;color:#fca5a5}.ps-act{background:#052e16;color:#86efac}}
.ps-text{flex:1;min-width:0;overflow-wrap:anywhere;color:var(--fg)}
.ps-name{font:inherit;color:var(--accent);background:none}
.ps-str{font:inherit;color:#15803d;background:none}
.fv.fv-full{position:fixed;inset:0;z-index:40;border-radius:0;border:0}
.fv.fv-full .fv-body{flex:1;height:auto;min-height:0}
.fv-head{display:flex;flex-wrap:wrap;align-items:center;gap:10px;padding:10px 12px;border-bottom:1px solid var(--line);background:var(--gutter)}
.fv-badge{flex:none;display:grid;place-items:center;min-width:38px;height:28px;padding:0 6px;border-radius:7px;font:700 10px/1 var(--mono);letter-spacing:.04em;color:#fff;background:#64748b}
.fv-badge-js,.fv-badge-mjs,.fv-badge-cjs{background:#d4a017;color:#1f1a00}.fv-badge-ts{background:#2f74c0}.fv-badge-html,.fv-badge-htm{background:#e4572e}
.fv-badge-css{background:#2965f1}.fv-badge-json,.fv-badge-jsonc,.fv-badge-jsonl{background:#16a34a}.fv-badge-md{background:#7c3aed}.fv-badge-py{background:#3572a5}.fv-badge-sh{background:#334155}
.fv-size{flex:1 1 auto;min-width:0;font:11px var(--mono);color:var(--muted);white-space:nowrap}
.fv-icon{width:30px;padding:0;display:inline-grid;place-items:center}
.fv-seg button.fv-icon{width:32px;height:26px;padding:0;display:inline-grid;place-items:center}
.fv-style{height:30px;padding:0 8px;border:1px solid var(--line);border-radius:8px;background:var(--panel);color:var(--fg);font:12px var(--sans);cursor:pointer}
.fv-style:hover{border-color:var(--accent)}
.fv-seg{display:flex;padding:2px;border:1px solid var(--line);border-radius:9px;background:var(--panel)}
.fv-seg button{border:0;background:none;color:var(--muted);font:500 12px var(--sans);padding:5px 12px;border-radius:7px;cursor:pointer}
.fv-seg button[aria-pressed="true"]{background:var(--accent);color:#fff}
.fv-tools{display:flex;align-items:center;gap:6px;flex-wrap:wrap}
.fv-find{height:30px;width:170px;max-width:42vw;box-sizing:border-box;padding:0 10px;border:1px solid var(--line);border-radius:8px;background:var(--panel);color:var(--fg);font:12px var(--sans);outline:none}
.fv-find:focus{border-color:var(--accent);box-shadow:0 0 0 3px var(--sel)}
.fv-count{font:11px var(--mono);color:var(--muted);min-width:0}
.fv-btn{height:30px;padding:0 10px;border:1px solid var(--line);border-radius:8px;background:var(--panel);color:var(--fg);font:12px var(--sans);cursor:pointer}
.fv-btn:hover{border-color:var(--accent)}
.fv-btn[aria-pressed="true"]{background:var(--sel);border-color:var(--accent)}
.fv-body{display:grid;grid-template-columns:220px minmax(0,1fr);height:560px;min-height:0}
.fv-body.no-side{grid-template-columns:minmax(0,1fr)}
.fv-side{overflow:auto;border-right:1px solid var(--line);padding:6px 4px;background:var(--panel)}
.fv-side-head{font:600 10px var(--sans);text-transform:uppercase;letter-spacing:.06em;color:var(--muted);padding:4px 8px 6px}
.fv-sym{display:flex;align-items:center;gap:6px;width:100%;border:0;background:none;color:var(--fg);text-align:left;font:12px/1.5 var(--mono);padding:3px 8px;border-radius:6px;cursor:pointer}
.fv-sym:hover{background:var(--sel)}
.fv-sym-icon{flex:none;width:18px;height:18px;display:grid;place-items:center;border-radius:5px;font:700 10px var(--mono);background:var(--gutter);color:var(--accent)}
.fv-fn .fv-sym-icon{color:#7c3aed}.fv-class .fv-sym-icon{color:#d97706}.fv-id .fv-sym-icon{color:#e4572e}.fv-sel .fv-sym-icon{color:#2965f1}.fv-const .fv-sym-icon{color:#0f766e}
.fv-sym-name{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.fv-sym-line{flex:none;font-size:10px;color:var(--muted)}
.fv-code{min-width:0;min-height:0}
.fv-code .CodeMirror{height:100%}
.fv-flash{background:var(--sel)!important;transition:background-color .6s}
.cm-fv-hit{background:#fde68a;color:#111;border-radius:2px}
.fv-doc{overflow:auto;min-height:0;background:var(--panel);color:var(--fg)}
.fv-doc .md-page{padding:36px 28px 80px}
.fv-md .fv-h .fv-sym-name{font-family:var(--sans)}
.md-code{font:.88em var(--mono);background:var(--gutter);border:1px solid var(--line);border-radius:5px;padding:.05em .35em}
.fv-json{overflow:auto;min-height:0;padding:8px 0;font:12.5px/1.65 var(--mono)}
.jv-row{display:flex;align-items:baseline;gap:2px;padding-right:12px;white-space:nowrap;border-radius:4px}
.jv-row.jv-open{cursor:pointer}
.jv-row:hover{background:var(--sel)}
.jv-caret{flex:none;width:14px;color:var(--muted);font-size:10px}
.jv-key{color:var(--accent);font-weight:600}
.jv-colon{color:var(--muted)}
.jv-str{color:#15803d;white-space:pre}.jv-num{color:#2563eb}.jv-bool{color:#9333ea}.jv-null{color:var(--muted);font-style:italic}
.jv-sum{color:var(--muted);font-size:11px;margin-left:4px}
.jv-hit{background:#fef3c7}
@media (max-width:760px){.fv-body{grid-template-columns:1fr;height:auto}.fv-side{max-height:160px;border-right:0;border-bottom:1px solid var(--line)}.fv-code,.fv-doc,.fv-json{height:480px}}
@media (max-width:640px){.tl-viewer{inset:8px}}
.ar-card.step{cursor:pointer}
.ar-card.step:hover{border-color:var(--accent)}
.ar-card.step.on{border-color:var(--accent);box-shadow:0 0 0 2px var(--accent)}
.ar-items{margin:4px 0 6px;padding-left:18px;font:13px/1.5 var(--sans)}
.ar-items .tl-chip{margin-right:4px}
.ar-card b{display:block;font:600 13px var(--sans);margin-bottom:4px}
.ar-card ul{margin:0;padding-left:16px}
.ar-card li{margin:1px 0;overflow-wrap:anywhere}
.ar-card .tl-used{margin-top:6px}
.ar-gap{flex:none}
.ar-why{display:grid;grid-template-columns:minmax(120px,210px) minmax(0,1fr);gap:4px 12px;font:13px/1.45 var(--sans);margin:6px 0 4px}
.ar-why>dt{color:var(--accent);font-weight:600}
.ar-why>dd{margin:0}
.ar-files{border:1px solid var(--accent);border-radius:12px;padding:10px 12px;margin-top:10px}
@media (max-width:640px){.ar-why{grid-template-columns:1fr}.ar-lane-name{width:64px}}
.tl-files>*{min-width:0}
@media (max-width:640px){.tl-explain,.tl-files{grid-template-columns:1fr}.tl-explain>.tl-side-head{display:none}.tl-explain>.tl-side-before::before{content:"Before: ";font-weight:600}.tl-explain>.tl-side-now::before{content:"Now: ";font-weight:600}}
.tl-check{display:flex;align-items:center;gap:6px;font:12px var(--sans);color:var(--muted);cursor:pointer;white-space:nowrap}
.tl-check input{margin:0;accent-color:var(--accent)}
.st-bar{display:flex;align-items:center;gap:12px;flex-wrap:wrap}
.st-title{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap;min-width:0;flex:1}
.st-title .tl-kind{font-size:16px}
.st-title .tl-name{font:12px var(--mono);color:var(--accent)}
.st-legend{display:flex;gap:12px;font:11px var(--mono);color:var(--muted);margin:8px 0 0}
.st-legend span::before{content:"";display:inline-block;width:10px;height:10px;border-radius:2px;margin-right:5px;vertical-align:-1px}
.st-legend .added::before{background:var(--add)}.st-legend .updated::before{background:var(--upd)}.st-legend .deleted::before{background:var(--del)}
.tl-time{font:11px var(--mono);color:var(--muted);min-width:52px}
.tl-kind{font-weight:600;white-space:nowrap}
.tl-count{font:11px var(--mono);color:var(--warn);white-space:nowrap}
.tl-ms{margin-left:auto;font:11px var(--mono);color:var(--muted);white-space:nowrap}
.tl-text{margin:-4px 0 8px 62px;font-size:12px;color:var(--muted)}
.tl-call{padding-left:calc(var(--depth) * 16px)}
.tl-call-head{display:flex;gap:8px;align-items:baseline;font:12px var(--mono);min-width:0}
.tl-call-head .tl-name{color:var(--fg);font-weight:500}
.tl-input{color:var(--muted);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;min-width:0}
.tl-call-head .tl-ms{margin-left:auto}
.tl-call.bad .tl-name,.tl-error{color:var(--bad)}
.tl-error{font:11px var(--mono);padding-left:8px}
.tl-changes{margin:4px 0 2px;padding:0;list-style:none;display:flex;flex-direction:column;gap:2px}
.tl-change{display:grid;grid-template-columns:minmax(0,auto) minmax(0,1fr);gap:10px;font:11px/1.5 var(--mono);padding:2px 8px;border-radius:5px}
.tl-change.added{background:var(--add-bg)}.tl-change.updated{background:var(--upd-bg)}.tl-change.deleted{background:var(--del-bg)}
.tl-path{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.tl-val{color:var(--muted);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.tl-tabs{display:flex;gap:2px;padding:3px;border-radius:9px;background:var(--gutter);border:1px solid var(--line)}
.tl-tab{border:0;background:none;color:var(--muted);font:500 12px var(--sans);padding:5px 12px;border-radius:6px;cursor:pointer}
.tl-tab[aria-selected="true"]{background:var(--panel);color:var(--fg);box-shadow:0 1px 3px rgba(0,0,0,.12)}
.tl-pos{font:12px var(--mono);color:var(--muted);white-space:nowrap}
.tl-strip{display:flex;gap:10px;overflow-x:auto;padding:4px 2px 6px;position:relative;scroll-snap-type:x proximity;flex:none}
.tl-step{position:relative;flex:none;width:168px;display:flex;flex-direction:column;gap:3px;text-align:left;padding:10px 12px;border:1px solid var(--line);border-radius:10px;background:var(--panel);color:var(--fg);cursor:pointer;font:12px var(--sans);scroll-snap-align:center;transition:border-color .15s,box-shadow .15s,transform .15s}
.tl-step:hover{border-color:var(--accent);transform:translateY(-1px)}
.tl-step::after{content:"";position:absolute;right:-11px;top:50%;width:10px;height:2px;background:var(--line)}
.tl-step:last-child::after{display:none}
.tl-step.past{opacity:.72}
.tl-step.on{border-color:var(--accent);box-shadow:0 0 0 3px var(--sel);opacity:1}
.tl-step.fixed{background:var(--gutter)}
.tl-step.bad{border-color:var(--bad)}
.tl-step-top{display:flex;align-items:center;gap:8px}
.tl-step-n{display:grid;place-items:center;min-width:20px;height:20px;padding:0 4px;box-sizing:border-box;border-radius:10px;background:var(--gutter);border:1px solid var(--line);font:600 10px var(--mono);color:var(--muted)}
.tl-step.on .tl-step-n{background:var(--accent);border-color:var(--accent);color:var(--on-accent)}
.tl-step .tl-kind{font-size:13px}
.tl-step-name{font:11px var(--mono);color:var(--accent);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.tl-step-meta{display:flex;gap:8px;font:11px var(--mono);color:var(--muted)}
.tl-detail{flex:1;min-height:0;overflow:auto;background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:14px 16px}
.tl-detail-head{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}
.tl-detail-head .tl-kind{font-size:16px}
.tl-detail-head .tl-name{font:12px var(--mono);color:var(--accent)}
.tl-detail-head .tl-time{margin-left:auto}
.tl-detail .tl-text{margin:4px 0 12px}
.tl-detail-sub{font:600 11px var(--sans);text-transform:uppercase;letter-spacing:.06em;color:var(--muted);margin-bottom:8px}
.tl-inside{display:flex;flex-direction:column;gap:6px;border-left:2px solid var(--sel);padding-left:10px}
.tl-part .tl-call-head{width:100%;border:0;background:none;color:inherit;font:12px var(--mono);text-align:left;padding:0}
button.tl-call-head{width:100%;border:0;background:none;color:inherit;font:12px var(--mono);text-align:left;padding:0;cursor:pointer}
.tl-call.can-open > .tl-call-head .tl-name::after{content:"▸";display:inline-block;margin-left:8px;color:var(--muted);transition:transform .15s}
.tl-call.open > .tl-call-head .tl-name::after{transform:rotate(90deg)}
.tl-call.can-open > .tl-call-head:hover .tl-name{color:var(--accent)}
.tl-say{font:12.5px/1.5 var(--sans);color:var(--muted);margin:2px 0 0 26px}
.tl-say b{font-weight:600;color:var(--fg);margin-right:4px}
.tl-call .tl-changes{margin-left:26px}
.tl-inside .tl-call + .tl-call{border-top:1px dashed var(--line);padding-top:8px}
.tl-more{margin:8px 0 4px 26px}
.tl-more:empty{display:none}
.tl-file{border:1px solid var(--line);border-radius:8px;overflow:hidden;margin-top:8px}
.tl-file:first-child{margin-top:0}
.tl-file-head{font:11px var(--mono);color:var(--muted);padding:6px 10px;background:var(--gutter);border-bottom:1px solid var(--line)}
.tl-code .CodeMirror{font:12px/1.55 var(--mono);background:var(--panel)}
.tl-group > .tl-detail-sub{margin:12px 0 6px}
.tl-group > .tl-detail-sub:first-child{margin-top:4px}
.tl-table{border-collapse:collapse;font:12px var(--mono);width:100%}
.tl-table th,.tl-table td{text-align:left;padding:4px 10px 4px 0;border-bottom:1px solid var(--line);vertical-align:top}
.tl-table th{color:var(--accent);font-weight:500;white-space:nowrap}
.tl-table td{color:var(--fg);word-break:break-word}
.tl-part-text{font:12.5px/1.5 var(--sans);color:var(--muted);margin:2px 0 0 26px}
.tl-sub-n{min-width:18px;color:var(--muted);font-size:10px}
.tl-detail.anim .tl-call{animation:tl-in .35s ease-out both;animation-delay:calc(var(--i) * 90ms)}
@keyframes tl-in{from{opacity:0;transform:translateX(-6px)}to{opacity:1;transform:none}}
.tl-detail.anim .tl-more .tl-call{animation:none}
@media (prefers-reduced-motion:reduce){.tl-detail.anim .tl-call{animation:none}}
:root{--read:"Inter",system-ui,-apple-system,"Segoe UI",sans-serif}
.sv-viewer-body.doc-mode{grid-template-columns:1fr;grid-template-rows:1fr}
.doc-mode #sv-viewer-code,.doc-mode .sv-viewer-side{display:none}
#sv-viewer-doc{min-height:0;overflow:auto;border:1px solid var(--line);border-radius:10px;background:var(--panel);color:var(--fg);transition:background-color .2s,color .2s}
[data-md-theme]{--md-font:var(--read);--md-head:var(--read);--md-size:17px;--md-lh:1.7;--md-measure:68ch}
[data-md-theme="reader"]{--panel:#fbf8f1;--gutter:#f2ede2;--fg:#27241f;--muted:#8b8274;--line:#e7e0d2;--accent:#a04a1c;--sel:#f1e4c9;--bg:#f5f0e5;
  --md-font:"Literata",Georgia,"Times New Roman",serif;--md-head:"Literata",Georgia,serif;--md-size:19px;--md-lh:1.68;--md-measure:64ch}
[data-md-theme="white"]{--panel:#ffffff;--gutter:#f5f5f5;--fg:#111111;--muted:#6e6e6e;--line:#e6e6e6;--accent:#2450d8;--sel:#e7edfd;--bg:#fafafa}
[data-md-theme="black"]{--panel:#000000;--gutter:#0e0e0e;--fg:#ececec;--muted:#8c8c8c;--line:#262626;--accent:#ffffff;--sel:#262f45;--bg:#0a0a0a}
[data-md-theme="sepia"]{--panel:#f4ecd8;--gutter:#ebdfc3;--fg:#5b4636;--muted:#8f7a63;--line:#e0d1b0;--accent:#8b4513;--sel:#e8d5a8;--bg:#efe4cb;
  --md-font:"Literata",Georgia,serif;--md-head:"Literata",Georgia,serif;--md-size:19px;--md-lh:1.68;--md-measure:64ch}
[data-md-theme="night"]{--panel:#1a1d24;--gutter:#22262f;--fg:#d9d2c3;--muted:#8a8476;--line:#2d313b;--accent:#e2a75e;--sel:#3a3326;--bg:#15181e;
  --md-font:"Literata",Georgia,serif;--md-head:"Literata",Georgia,serif;--md-size:19px;--md-lh:1.7;--md-measure:64ch}
[data-md-theme="mono"]{--panel:#f7f7f1;--gutter:#ecece4;--fg:#222222;--muted:#777777;--line:#dcdcd2;--accent:#c2410c;--sel:#fde5cc;--bg:#f0f0e8;
  --md-font:var(--mono);--md-head:var(--mono);--md-size:15px;--md-lh:1.75;--md-measure:74ch}
.md-page{max-width:var(--md-measure,68ch);margin:0 auto;padding:52px 32px 120px 44px;font-family:var(--md-font,var(--read));font-size:var(--md-size,17px);line-height:var(--md-lh,1.7);color:var(--fg);font-feature-settings:"kern","liga";text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased;hyphens:auto;overflow-wrap:break-word}
.md-page h2{font-family:var(--md-head,var(--read));font-size:1.85em;line-height:1.2;font-weight:700;letter-spacing:-.02em;margin:0 0 1.1em;text-wrap:balance}
.md-page h3,.md-page h4{position:relative;font-family:var(--md-head,var(--read));font-size:1.22em;line-height:1.35;font-weight:650;letter-spacing:-.01em;margin:2.1em 0 .6em;text-wrap:balance}
.md-page p{text-wrap:pretty}
.md-themes{--ring:var(--accent);display:flex;gap:6px;margin-left:auto;margin-right:4px}
.md-theme{width:34px;height:28px;padding:0;border:1px solid var(--line);border-radius:7px;background:var(--panel);color:var(--fg);font:600 12px/1 var(--md-font);cursor:pointer;transition:box-shadow .12s,transform .12s}
.md-theme:hover{transform:translateY(-1px)}
.md-theme[aria-pressed="true"]{box-shadow:0 0 0 2px var(--ring)}
@media (max-width:640px){.md-theme{width:28px}.md-themes{gap:4px}}
.md-page h4{font-size:18px;margin-top:28px}
.md-page p{margin:0 0 10px}
.md-item{position:relative;padding-left:24px}
.md-item::before{content:"";position:absolute;left:7px;top:.7em;width:6px;height:6px;border-radius:50%;background:var(--accent);opacity:.75}
p.md-step{display:flex;gap:12px;margin-bottom:8px}
.md-num{flex:none;min-width:1.7em;text-align:right;color:var(--accent);font-weight:600;font-variant-numeric:tabular-nums}
.md-step .md-t{flex:1;min-width:0}
.md-t{outline:none;border-radius:4px;transition:background-color .12s,box-shadow .12s}
.md-t[contenteditable]:hover{background:var(--gutter);box-shadow:0 0 0 3px var(--gutter)}
.md-t[contenteditable]:focus{background:var(--sel);box-shadow:0 0 0 3px var(--sel)}
.md-t:empty::before{content:"Type here";color:var(--muted)}
.md-fold{position:absolute;left:-30px;top:50%;width:24px;height:24px;margin-top:-12px;padding:0;border:0;border-radius:6px;background:none;color:var(--muted);cursor:pointer;display:grid;place-items:center;opacity:.55;transition:opacity .12s,background-color .12s}
.md-sec:hover .md-fold,.md-fold:focus-visible,.md-sec.folded .md-fold{opacity:1}
.md-fold:hover{background:var(--gutter);color:var(--fg)}
.md-fold::before{content:"";width:7px;height:7px;border-right:1.7px solid currentColor;border-bottom:1.7px solid currentColor;transform:translateY(-2px) rotate(45deg);transition:transform .15s}
.md-sec.folded .md-fold::before{transform:translateX(-2px) rotate(-45deg)}
.md-sec.folded > .md-body{display:none}
.md-sec.folded > :first-child .md-t::after{content:" …";color:var(--muted)}
.md-page pre.code{margin:10px 0 18px;padding:14px 16px;background:var(--gutter);border:1px solid var(--line);border-radius:10px;font:13px/1.6 var(--mono);overflow:auto;white-space:pre;outline:none;tab-size:2}
.md-page pre.code:focus{border-color:var(--accent)}
.md-page .diagram{margin:14px 0 22px}
@media (max-width:640px){.md-page{padding:28px 16px 80px 36px;font-size:calc(var(--md-size,17px) - 1px)}.md-page h2{font-size:1.6em}}
.sv-viewer-side{min-height:0;display:grid;grid-template-rows:1fr minmax(0,38%);gap:8px}
.code-only .sv-viewer-side{display:none}
.sv-viewer-state{min-height:0;display:flex;flex-direction:column;gap:4px;border:1px solid var(--line);border-radius:10px;background:var(--panel);padding:8px 10px}
#sv-viewer-state{margin:0;overflow:auto;font:12px/1.5 var(--mono)}
#sv-viewer-state .bad{color:var(--bad,#c0322b)}
.long-tip{position:fixed;z-index:20;margin:0;width:min(560px,calc(100vw - 32px));max-height:300px;overflow:hidden;padding:6px 0;background:var(--panel);color:var(--fg);border:1px solid var(--line);border-radius:8px;box-shadow:0 6px 20px rgba(0,0,0,.18);pointer-events:none}
.long-tip .CodeMirror{height:auto;background:transparent;font:11px/1.5 var(--mono)}
.long-tip .CodeMirror-lines{padding:0}
.long-tip .CodeMirror pre.CodeMirror-line{padding:0 10px}
.why-tip{position:fixed;z-index:20;max-width:min(440px,calc(100vw - 32px));padding:8px 12px;background:var(--panel);color:var(--fg);border:1px solid var(--line);border-radius:8px;box-shadow:0 6px 20px rgba(0,0,0,.18);font:12px/1.5 var(--sans);white-space:pre-wrap;pointer-events:none}
.md-page .chg-added,.md-page .chg-deleted{margin-left:-12px;padding-left:12px;border-radius:2px}
.md-page .chg-deleted{text-decoration:line-through;text-decoration-color:var(--del)}
.long-tip .tip-more{padding:2px 10px 0;font:11px var(--sans);color:var(--muted)}
#sv-viewer-code,#sv-viewer-view{""")
assert "\\" not in STYLE.replace("\\u2022", ""), "no backslashes in a template"
STYLE = STYLE.replace("\\u2022", "•")

def svg(paths):
    return ('<svg viewBox="0 0 16 16" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.6" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + paths + '</svg>')

I_DOCS = svg('<path d="M4 1.5h5.5L12.5 4.5v10h-8.5z"/><path d="M9.5 1.5v3h3M6 8h4.5M6 10.5h4.5"/>')
I_TIMELINE = svg('<path d="M4 2v12"/><circle cx="4" cy="4" r="1.6"/><circle cx="4" cy="8.5" r="1.6"/><circle cx="4" cy="13" r="1.1"/><path d="M7.5 4h6M7.5 8.5h4.5"/>')
I_STATE = svg('<path d="M6 2.5C4 2.5 4.5 5 4.5 6.5S3 8 3 8s1.5 0 1.5 1.5S4 13.5 6 13.5M10 2.5c2 0 1.5 2.5 1.5 4S13 8 13 8s-1.5 0-1.5 1.5.5 4-1.5 4"/>')
I_DEVICE = svg('<rect x="1.5" y="2.5" width="9.5" height="7" rx="1"/><path d="M4 12.5h4M6 9.5v3"/><rect x="10" y="5.5" width="4.5" height="8" rx="1"/>')
I_RELOAD = svg('<path d="M13 8a5 5 0 1 1-1.5-3.5"/><path d="M12 1.8v3h-3"/>')
I_PLAY = svg('<path d="M5 3.2v9.6L12.5 8z" fill="currentColor"/>')
I_PAUSE = svg('<path d="M5.5 3.5v9M10.5 3.5v9"/>')
I_OLDER = svg('<path d="M10 3 5 8l5 5"/>')
I_NEWER = svg('<path d="m6 3 5 5-5 5"/>')
I_COLLAPSE = svg('<path d="m4 2 4 4 4-4M4 14l4-4 4 4"/>')
I_SAVE = svg('<path d="M3 2.5h8l2.5 2.5v8.5h-10.5z"/><path d="M5.5 2.5v3h4.5v-3M5.5 13.5v-4h5v4"/>')
I_FLOWS = svg('<circle cx="3" cy="4" r="1.3"/><path d="M4.5 4h2.5a2 2 0 0 1 2 2v4a2 2 0 0 0 2 2h2.5"/><path d="m12 10 2 2-2 2"/>')
I_CLOSE = svg('<path d="m4 4 8 8M12 4l-8 8"/>')
I_GEAR = svg('<circle cx="8" cy="8" r="2.2"/><path d="M8 1.5v2M8 12.5v2M1.5 8h2M12.5 8h2M3.4 3.4l1.4 1.4M11.2 11.2l1.4 1.4M3.4 12.6l1.4-1.4M11.2 4.8l1.4-1.4"/>')
# the buttons of the file viewer
FV_ICONS = {
    "read": svg('<path d="M2 3.5c2-.8 4-.8 6 .5v9.5c-2-1.3-4-1.3-6-.5zM14 3.5c-2-.8-4-.8-6 .5v9.5c2-1.3 4-1.3 6-.5z"/>'),
    "source": svg('<path d="m5.5 4.5-3.5 3.5 3.5 3.5M10.5 4.5l3.5 3.5-3.5 3.5"/>'),
    "tree": svg('<path d="M3 2.5v9.5h3M3 6.5h3"/><rect x="6.5" y="4.8" width="7" height="3.4" rx="1"/><rect x="6.5" y="10.3" width="7" height="3.4" rx="1"/>'),
    "side": svg('<rect x="2" y="2.5" width="12" height="11" rx="1.5"/><path d="M6 2.5v11M3.6 5.5h1M3.6 8h1"/>'),
    "copy": svg('<rect x="5.5" y="5.5" width="8" height="8.5" rx="1.5"/><path d="M10.5 5.5V3a1 1 0 0 0-1-1H3a1 1 0 0 0-1 1v6.5a1 1 0 0 0 1 1h2.5"/>'),
    "done": svg('<path d="m3 8.5 3 3 7-7"/>'),
    "fail": svg('<path d="m4 4 8 8M12 4l-8 8"/>'),
    "wrap": svg('<path d="M2 4h12M2 8h9.5a2.5 2.5 0 0 1 0 5H8M2 12h3"/><path d="m9.5 11-1.8 2 1.8 2"/>'),
    "full": svg('<path d="M2.5 6V2.5H6M10 2.5h3.5V6M13.5 10v3.5H10M6 13.5H2.5V10"/>'),
    "exit": svg('<path d="M6 2.5V6H2.5M13.5 6H10V2.5M10 13.5V10h3.5M2.5 10H6v3.5"/>'),
    "open": svg('<path d="m4 6 4-4 4 4M4 10l4 4 4-4"/>'),
    "close": svg('<path d="m4 2 4 4 4-4M4 14l4-4 4 4"/>'),
}
FV_ICONS_JS = "{ " + ", ".join(k + ": '" + v + "'" for k, v in FV_ICONS.items()) + " }"
I_REC = '<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><circle cx="12" cy="12" r="7" fill="currentColor"/></svg>'
I_STOP = '<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><rect x="6.5" y="6.5" width="11" height="11" rx="2" fill="currentColor"/></svg>'

# Each view is between the header (and the timeline when it is open) and the footer with the record button
# (recorder-view): it scrolls in that space.
# The Device button: all the views show at the width of a phone or a tablet. index-view is then the screen of the
# device: its fixed parts (the record button, Notes, a full screen file) stay in it, and each @media (max-width)
# rule also works at that width, as an @container rule.
STYLE = STYLE.replace("button{font:inherit}", """button{font:inherit}
#docs-view,#state-view,#notes-view{overflow:auto}
#docs-view{display:flex;flex-direction:column;gap:8px}
#docs-view .docs{flex:1;min-height:0;height:auto}
.view-bar{display:flex;justify-content:flex-end}
.tl-pos{margin-right:auto}
.tl-only{display:inline-flex;gap:6px}
.tl-only .st-kind::before{content:"";display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:6px;vertical-align:1px}
.tl-only-ai::before{background:#7c3aed}
.tl-only-ui::before{background:#0284c7}
#tl-strip .tl-step.ai{border-left:4px solid #7c3aed}
#tl-strip .tl-step.ui{border-left:4px solid #0284c7}
#tl-strip .tl-step.pin-left,#tl-strip .tl-step.pin-right{width:196px;padding:12px 14px;border-width:2px 2px 2px 5px;opacity:1;box-shadow:0 4px 16px rgba(0,0,0,.2)}
#tl-strip .tl-step.pin-left.on,#tl-strip .tl-step.pin-right.on{box-shadow:0 0 0 3px var(--sel),0 4px 16px rgba(0,0,0,.2)}
#tl-strip .tl-step.pin-left .tl-kind,#tl-strip .tl-step.pin-right .tl-kind{font-size:14px;font-weight:600}
@media (max-width:640px){#tl-strip{gap:8px}#tl-strip .tl-step{width:70px;padding:6px 7px;gap:2px}#tl-strip .tl-step::after{right:-9px;width:8px}#tl-strip .tl-step.pin-left,#tl-strip .tl-step.pin-right{width:84px;padding:7px 8px}#tl-strip .tl-time,#tl-strip .tl-step-name,#tl-strip .tl-step-meta{display:none}#tl-strip .tl-step .tl-kind{font-size:11px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}#tl-strip .tl-step.pin-left .tl-kind,#tl-strip .tl-step.pin-right .tl-kind{font-size:12px}}
#index-view[data-device]{container-type:inline-size;transform:translateZ(0);margin-inline:auto;max-width:100%;overflow:auto;background:var(--bg);box-shadow:0 0 0 1px var(--line),0 12px 40px rgba(0,0,0,.14)}
#index-view[data-device="mobile"]{width:390px}
#index-view[data-device="tablet"]{width:820px}
body:has(#index-view[data-device]){background:var(--gutter)}
.dev-pick{position:relative;display:inline-flex}
.dev-menu{position:absolute;top:calc(100% + 6px);right:0;z-index:70;min-width:170px;display:flex;flex-direction:column;gap:2px;padding:4px;background:var(--panel);border:1px solid var(--line);border-radius:12px;box-shadow:0 10px 30px rgba(0,0,0,.2)}
.dev-menu button{display:flex;gap:10px;align-items:center;border:0;background:none;color:var(--fg);font:13px var(--sans);padding:8px 12px;border-radius:8px;cursor:pointer;text-align:left}
.dev-menu button:hover,.dev-menu button:focus-visible{background:var(--sel);outline:none}
.dev-menu button[aria-checked="true"]{color:var(--accent);font-weight:600}
.dev-menu small{margin-left:auto;font:11px var(--mono);color:var(--muted)}""", 1)
def with_container(css):
    out, i = [], 0
    while True:
        j = css.find("@media (max-width:", i)
        if j < 0: out.append(css[i:]); return "".join(out)
        k, depth = css.index("{", j), 0
        for m in range(k, len(css)):
            depth += {"{": 1, "}": -1}.get(css[m], 0)
            if depth == 0: break
        block = css[j:m + 1]
        out.append(css[i:m + 1] + "\n@container " + block[len("@media "):])
        i = m + 1
STYLE = with_container(STYLE)

# ---------- html of the views ----------
index_html = """<div id="index-view">
""" + STYLE + """
<section id="timeline-view" hidden></section>
<header id="header-view"></header>
<main id="docs-view" hidden></main>
<main id="state-view" hidden></main>
<main id="notes-view" hidden></main>
<footer id="recorder-view"></footer>
</div>"""

header_html = """<header id="header-view">
  <span class="dev-pick">
    <button class="btn" id="device-button"
            data-call="local.toggle-device-menu"
            aria-pressed="${d.device !== 'desktop'}" aria-expanded="${d.device_open}" aria-haspopup="menu"
            aria-label="Device: ${d.device}" title="Device: ${d.device}">
      """ + I_DEVICE + """
    </button>
    ${d.device_open ? `<div class="dev-menu" id="device-menu" role="menu" aria-label="Device">
      ${[['mobile', 'Mobile', '390 px'], ['tablet', 'Tablet', '820 px'], ['desktop', 'Desktop', 'full']].map(x => `<button role="menuitemradio" aria-checked="${d.device === x[0]}" data-call="local.set-device" data-input='{"device":"${x[0]}"}'>${x[1]}<small>${x[2]}</small></button>`).join('')}
    </div>` : ''}
  </span>
  <button class="btn" id="docs-button"
          data-call="local.open.docs-view"
          aria-pressed="${d.docs_open}" aria-label="Docs" title="Docs">
    """ + I_DOCS + """
  </button>
  <button class="btn" id="state-button"
          data-call="local.open.state-view"
          aria-pressed="${d.state_open}" aria-label="State view" title="State view">
    """ + I_STATE + """
  </button>
  <span class="rec-timer" id="rec-timer" role="timer" hidden></span>
</header>"""

# The footer of the page: the record button at its right, and above it the card of the last recording and the menu.
recorder_html = """<footer id="recorder-view">
  <div class="rec-pop">
  ${d.error ? `<div class="rec-error" id="rec-error" role="alert">${e(d.error)}</div>` : ''}
  ${d.result ? `<section class="rec-card" id="rec-card" aria-label="Last recording">
    <div class="rec-card-head">
      <b>${d.result.kind === 'video' ? 'Video' : 'Audio'}</b><span>${e(d.result.time)} · ${e(d.result.size)}</span>
      <button class="btn" id="rec-save" data-call="local.save">Save file</button>
      <button class="btn" id="rec-close" data-call="local.clear" aria-label="Close" title="Close">""" + I_CLOSE + """</button>
    </div>
    <div id="rec-media"></div>
    ${d.selections.length ? `<ol class="rec-sel">${d.selections.map(x => `<li><span>${e(x.at)}</span><code>${e(x.path)}</code></li>`).join('')}</ol>` : ''}
  </section>` : ''}
  ${d.menu_open && !d.recording ? `<div class="rec-menu" id="rec-menu" role="menu" aria-label="Record">
    <button role="menuitem" data-call="local.start" data-input='{"mode":"audio"}'><span>1</span>Record audio</button>
    <button role="menuitem" data-call="local.start" data-input='{"mode":"video"}'><span>2</span>Record video</button>
    <button role="menuitem" data-call="local.open-notes"><span>3</span>Notes</button>
  </div>` : ''}
  </div>
  <button class="rec-btn" id="rec-button" aria-pressed="${!!d.recording}"
          aria-label="${d.recording ? 'Stop recording' : 'Record'}"
          title="${d.recording ? 'Stop' : 'Click: record audio. Double-click: the menu (audio, video, notes). Keys: Arrow Up two times (audio), Arrow Up and Arrow Down together (video). Hold 4 s: Notes.'}">
    ${d.recording ? '""" + I_STOP + """' : '""" + I_REC + """'}
  </button>
</footer>"""

# The Notes page: a view between the header and the footer. Each recording is a note; you can also write one. A note can go to Claude.
# (d.picked and d.shown come from local.refresh: the notes that are checked, and the notes that show their view state.)
notes_html = """<main id="notes-view">
  <div class="notes-bar">
    <b>Notes</b>
    <button class="btn" id="notes-settings-button" data-call="local.toggle-settings" aria-pressed="${!!d.settings_open}" aria-label="Settings" title="Settings">""" + I_GEAR + """</button>
    <button class="btn" id="notes-close" data-call="local.close" aria-label="Close" title="Close">""" + I_CLOSE + """</button>
  </div>
  ${d.settings_open ? `<section class="notes-settings" id="notes-settings" aria-label="Settings">
    <label>Transcription
      <select id="notes-transcribe">
        <option value="browser" ${d.settings.transcribe === 'browser' ? 'selected' : ''}>Browser (default)</option>
        <option value="off" ${d.settings.transcribe === 'off' ? 'selected' : ''}>Off</option>
      </select>
    </label>
    <label>Language <input id="notes-lang" value="${e(d.settings.lang)}" placeholder="browser language" size="16"></label>
    <label>New session task <input id="notes-task" value="${e(d.settings.new_session_task)}" placeholder="trig_..." size="22"></label>
    <p>Browser: while you record, the browser turns what the microphone hears into text (Chrome sends the sound to its speech service). Transcribe puts the text into the note. New session task: the id of the scheduled task that Send now new session starts (it starts a new session at each run).</p>
  </section>` : ''}
  <div class="notes-add">
    <textarea id="notes-new" placeholder="Write a note" aria-label="A new note"></textarea>
    <button class="btn" id="notes-add">Add note</button>
  </div>
  ${d.message ? `<div class="notes-msg" id="notes-msg" role="status">${e(d.message)}</div>` : ''}
  <div class="notes-list" id="notes-list">
    ${d.notes.length ? d.notes.map(n => `<article class="note" data-id="${e(n.id)}">
      <div class="note-top">
        <div class="note-body">${n.kind === 'text' || n.text ? `<textarea class="note-text" data-id="${e(n.id)}" aria-label="The text of the note">${e(n.text)}</textarea>` : `<div class="note-media" data-id="${e(n.id)}"></div>`}</div>
        <div class="note-actions">
          ${n.kind === 'text' ? '' : `<button class="btn" data-call="local.transcribe" data-input='${e(JSON.stringify({ id: n.id }))}'>Transcribe</button>`}
          <button class="btn" data-call="local.send" data-input='${e(JSON.stringify({ ids: [n.id] }))}'>Send now</button>
          <button class="btn" data-call="local.send" data-input='${e(JSON.stringify({ ids: [n.id], new_session: true }))}'>Send now new session</button>
          <button class="btn" data-call="local.delete" data-input='${e(JSON.stringify({ id: n.id }))}'>Delete</button>
        </div>
      </div>
      <div class="note-view">
        <label><input type="checkbox" class="note-pick" data-call="local.pick" data-input='${e(JSON.stringify({ id: n.id }))}' ${(d.picked || []).includes(n.id) ? 'checked' : ''}> view path: <code>${e(n.view_path.split('.').join('/'))}</code></label>
        <button class="btn" data-call="local.show-state" data-input='${e(JSON.stringify({ id: n.id }))}' aria-pressed="${(d.shown || []).includes(n.id)}">${(d.shown || []).includes(n.id) ? 'Hide state' : 'Show state'}</button>
        <span class="note-meta">${n.kind === 'text' ? 'text' : e(n.kind + ' ' + n.time)} · ${e(new Date(n.at).toLocaleString([], { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' }))}</span>
      </div>
      ${(d.shown || []).includes(n.id) ? `<pre class="note-state" data-id="${e(n.id)}"></pre>` : ''}
    </article>`).join('') : '<p class="notes-empty">No notes yet. Record, or write a note above.</p>'}
  </div>
  <div class="notes-foot">
    <button class="btn" id="notes-send-selected" data-call="local.send" data-input='${e(JSON.stringify({ ids: d.picked || [] }))}' ${(d.picked || []).length ? '' : 'disabled'}>Send selected</button>
  </div>
</main>"""

docs_html = """<main id="docs-view">
<div class="view-bar">
  <button class="btn" id="docs-close" data-call="local.close" aria-label="Close" title="Close">""" + I_CLOSE + """</button>
</div>
<div class="docs">
  <nav class="docs-list">
    <div class="path">${e(d.path)}</div>
    ${d.docs.map(name => `
    <button class="doc-link"
            data-call="local.open-doc" data-input='${e(JSON.stringify({ name }))}'
            aria-current="${name === d.selected}">${e(name)}</button>`).join('')}
  </nav>
  <article class="doc">
    ${d.content.split('```').map((part, i) => i % 2
      ? (part.startsWith('svg')
          ? `<figure class="diagram">${part.slice(3)}</figure>`
          : `<pre class="code">${e(part.replace(/^[a-z]*\\n/, '').replace(/\\n$/, ''))}</pre>`)
      : part.split('\\n').map(line =>
          line.startsWith('# ') ? `<h2>${e(line.slice(2))}</h2>` :
          line.startsWith('## ') ? `<h3>${e(line.slice(3))}</h3>` :
          line.startsWith('- ') ? `<p class="item">${e(line.slice(2))}</p>` :
          /^[0-9]+[.] /.test(line) ? `<p class="step">${e(line)}</p>` :
          line.trim() ? `<p>${e(line)}</p>` : '').join('')).join('')}
  </article>
</div>
</main>"""
# The template is JavaScript inside backticks: '\\n' above becomes '\n' in the state, which the template reads as a newline.
# A doc is markdown: # and ## headings, - items, 1. steps, ``` code blocks, and ```svg blocks for diagrams.

timeline_html = """<section id="timeline-view">
  <div class="tl-bar">
    <button class="btn" id="tl-prev" data-call="local.next" data-input='{"delta":-1}' aria-label="Block before" title="Block before">
      """ + I_OLDER + """
    </button>
    <button class="btn primary" id="tl-play" data-call="local.play" aria-pressed="${d.playing}"
            aria-label="${d.playing ? 'Pause' : 'Replay'}" title="${d.playing ? 'Pause' : 'Replay the blocks'}">
      ${d.playing ? '""" + I_PAUSE + """' : '""" + I_PLAY + """'}
    </button>
    <button class="btn" id="tl-next" data-call="local.next" data-input='{"delta":1}' aria-label="Next block" title="Next block">
      """ + I_NEWER + """
    </button>
    <span class="tl-pos" id="tl-pos"></span>
    <span class="tl-only" role="group" aria-label="Show">
      <button class="st-kind tl-only-ai" id="tl-runs" data-call="local.show" data-input='{"only":"runs"}'
              aria-pressed="${d.show === 'runs'}" title="${d.show === 'runs' ? 'Show all the blocks' : 'Show only the AI runs'}">AI runs</button>
      <button class="st-kind tl-only-ui" id="tl-ui" data-call="local.show" data-input='{"only":"ui"}'
              aria-pressed="${d.show === 'ui'}" title="${d.show === 'ui' ? 'Show all the blocks' : 'Show only the UI blocks'}">UI</button>
    </span>
    <button class="btn" id="tl-reload" data-call="local.reload" aria-label="Restart" title="Restart: reload the page and show the last AI run notification">
      """ + I_RELOAD + """
    </button>
    <button class="btn" id="tl-flows" data-call="local.toggle-flows"
            aria-pressed="${d.flows_open}" aria-label="Flows" title="Saved flows">
      """ + I_FLOWS + """
    </button>
    <div class="tl-flows" id="tl-flows-list" ${d.flows_open ? '' : 'hidden'}>
      <div class="tl-flows-head">Saved flows</div>
      ${d.flows.map(f => `
      <div class="tl-flow">
        <button class="btn primary" data-call="local.play-flow" data-input='${e(JSON.stringify({ name: f.name }))}' aria-label="Play ${e(f.name)}" title="Play this flow">
          """ + I_PLAY + """
        </button>
        <div class="tl-flow-text"><b>${e(f.name)}</b><span>${f.steps.length} blocks: ${e(f.steps.join(', '))}</span></div>
      </div>`).join('') || '<div class="tl-none">No saved flows.</div>'}
    </div>
    <button class="btn" id="tl-close" data-call="local.close" aria-label="Close" title="Close the timeline">""" + I_CLOSE + """</button>
  </div>
  <div class="tl-strip" id="tl-strip"></div>
</section>"""

state_html = """<main id="state-view">
<div class="sv-bar">
  <div class="st-kinds" id="sv-switches" role="group" aria-label="Show">
    <button class="btn" id="timeline-button"
            data-call="local.toggle-timeline"
            aria-pressed="${d.timeline_open}" aria-label="Timeline" title="Show or hide the timeline">
      """ + I_TIMELINE + """
    </button>
    <span class="sv-sep"></span>
    ${[['all', 'All'], ['files', 'Files'], ['views', 'Views'], ['functions', 'Functions'], ['network', 'Network'], ['environment', 'Environment']].map(([kind, label]) => `
    <button class="st-kind" aria-pressed="${d.filter_kind === kind}" data-call="local.filter-kind" data-input='{"kind":"${kind}"}'
            title="${kind === 'all' ? 'Show all' : 'Show only ' + kind + ', as a tree'}">${label}</button>`).join('')}
    <span class="sv-sep"></span>
    <button class="st-kind" id="changes"
            data-call="local.toggle-changes"
            aria-pressed="${d.changes && !d.details}" title="Show only what the chosen block changed (or the version, after Older or Newer)">Changes</button>
    <button class="st-kind" id="details"
            data-call="local.toggle-details"
            aria-pressed="${d.details}" title="What happens inside the chosen block">Details</button>
  </div>
  <div class="sv-filter">
    <input id="sv-filter-input" type="search" value="${e(d.filter)}" placeholder="Filter paths"
           autocomplete="off" spellcheck="false" aria-label="Filter">
    <span class="sv-checks" id="sv-checks">
      <label class="sv-check" title="Show the entries with an empty value: {}, [], &quot;&quot; or null">
        <input type="checkbox" id="sv-empty" data-call="local.toggle-empty" ${d.show_empty ? 'checked' : ''}> Show empty
      </label>
      <label class="sv-check" title="Add what you do in the state view and the timeline as blocks of the timeline">
        <input type="checkbox" id="sv-track" data-call="local.toggle-tracking" ${d.track_state ? 'checked' : ''}> Track state
      </label>
    </span>
  </div>
  <div class="sv-group" id="sv-right">
    <button class="btn" id="collapse"
            data-call="local.collapse-all"
            aria-label="Collapse all" title="Collapse all">
      """ + I_COLLAPSE + """
    </button>
    <button class="btn primary" id="save"
            data-call="local.save"
            ${!d.unsaved || (d.error && !d.fixable) ? 'disabled' : ''}
            aria-label="Save" title="Save (Cmd+S)">
      """ + I_SAVE + """
    </button>
    <span class="sv-sep"></span>
    <button class="btn" id="older"
            data-call="local.step" data-input='{"delta":-1}'
            ${d.position <= 0 ? 'disabled' : ''}
            aria-label="Older version" title="Older version (&larr;)">
      """ + I_OLDER + """
    </button>
    <button class="btn" id="newer"
            data-call="local.step" data-input='{"delta":1}'
            ${d.position >= d.current_state_version - (d.unsaved ? 0 : 1) ? 'disabled' : ''}
            aria-label="Newer version" title="Newer version (&rarr;)">
      """ + I_NEWER + """
    </button>
    <span class="sv-sep"></span>
    <button class="btn" id="sv-close" data-call="local.close" aria-label="Close" title="Close">""" + I_CLOSE + """</button>
  </div>
</div>
<div id="sv-editor"></div>
<div class="tl-detail" id="tl-detail" hidden></div>
<div class="sv-foot" id="sv-foot">
  <span class="pos" id="pos"><b>${e(d.version)}</b> ${e(d.version_ago)}</span>
  <span class="sv-block" id="sv-block"></span>
  <span class="path" id="path">${e(d.path)}</span>
  <span class="status ${d.error && !d.fixable ? 'bad' : ''}" id="status" role="status">
    ${d.error ? (d.fixable ? 'JSON has slips, save fixes them' : 'Invalid JSON: ' + e(d.error)) : d.unsaved ? 'Unsaved' : ''}
  </span>
</div>
<div id="sv-viewer" class="sv-viewer" hidden>
  <div class="sv-viewer-bar">
    <span class="path" id="sv-viewer-path"></span>
    <div class="md-themes" id="md-themes" role="group" aria-label="Theme" hidden>
      ${['reader', 'white', 'black', 'sepia', 'night', 'mono'].map(name => `
      <button class="md-theme" data-md-theme="${name}"
              data-call="local.set-md-theme" data-input='{"theme":"${name}"}'
              aria-pressed="${name === d.md_theme}" title="${name[0].toUpperCase() + name.slice(1)}" aria-label="${name} theme">Aa</button>`).join('')}
    </div>
    <button class="btn" id="sv-viewer-close"
            data-call="local.close-viewer"
            aria-label="Close" title="Close">
      """ + I_CLOSE + """
    </button>
  </div>
  <div class="sv-viewer-body">
    <div id="sv-viewer-code"></div>
    <div id="sv-viewer-doc" hidden></div>
    <div class="sv-viewer-side">
      <iframe id="sv-viewer-view" title="The view, working"></iframe>
      <div class="sv-viewer-state">
        <div class="path" id="sv-viewer-state-head"></div>
        <pre id="sv-viewer-state"></pre>
      </div>
    </div>
  </div>
</div>
</main>"""

# ---------- code of the functions ----------
INIT = sig("init", [], r"""
const core = imports['state-core'], v = 'extension.views.state-view', d = os.get(v + '.ui-data'), H = os.history.commits;
const R = os.refs['state-view'] = { cm: null, draft: null, base: H[H.length - 1].state, timer: null, setting: false, shownEditable: false, long: [], hide: [], bad: null, viewer: null, viewerCm: null, block: null, onBlock: false };
Object.assign(d, { current_state_version: H[H.length - 1].n, position: H.length - 1, changes: false, unsaved: false, error: '', fixable: false, viewer_path: '' });

R.cm = CodeMirror(ctx.root.querySelector('#sv-editor'), {
  value: '', mode: { name: 'javascript', json: true }, theme: 'agent', lineNumbers: true, indentUnit: 2, tabSize: 2,
  foldGutter: true, gutters: ['CodeMirror-linenumbers', 'CodeMirror-foldgutter'], matchBrackets: true, autoCloseBrackets: true
});
// Keys get their own color, empty keys and {} a quieter one.
R.cm.addOverlay(core.keyOverlay);
R.cm.on('change', () => {
  if (R.setting) return;
  clearTimeout(R.timer);
  R.timer = setTimeout(() => os.call('local.edit', {}, v).catch(console.error), 250);
});

// Arrow keys step through versions; Cmd+S / Ctrl+S saves from anywhere, on any keyboard layout.
if (!os.refs.keys) {
  os.refs.keys = true;
  document.addEventListener('keydown', e => {
    const r = os.refs['state-view'];
    if (!r || e.altKey || e.metaKey || e.ctrlKey || (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight')) return;
    if ((r.cm.hasFocus() && r.shownEditable) || /^(INPUT|TEXTAREA)$/.test(e.target.tagName) || r.viewer) return;
    e.preventDefault();
    os.call('local.step', { delta: e.key === 'ArrowLeft' ? -1 : 1 }, v).catch(console.error);
  });
  document.addEventListener('keydown', e => {
    const r = os.refs['state-view'];
    if (!(e.metaKey || e.ctrlKey) || e.code !== 'KeyS') return;
    e.preventDefault();
    if (r && r.cm.getValue() !== r.base && r.shownEditable) os.call('local.save', {}, v).catch(console.error);
  }, true);
}
// Typing in the filter shows only the paths that have the text; Escape clears it.
const input = ctx.root.querySelector('#sv-filter-input');
input.addEventListener('input', () => {
  clearTimeout(R.filterTimer);
  R.filterTimer = setTimeout(() => os.call('local.filter', { text: input.value }, v).catch(console.error), 120);
});
input.addEventListener('keydown', e => {
  if (e.key !== 'Escape') return;
  input.value = '';
  os.call('local.filter', { text: '' }, v).catch(console.error);
});
// The timeline renders with the state view, before the watch: its blocks are ready when local.refresh runs. The
// Timeline button shows or hides it.
if (!os.mounted('extension.views.timeline-view')) await ctx.call('extension.functions.render', { view_path: 'extension.views.timeline-view' });
// local.refresh runs after each call, so the view always shows the state.
os.watch(v, 'local.refresh');
setTimeout(() => R.cm && R.cm.refresh(), 0);
""")

REFRESH = sig("refresh", ["after"], r"""
const core = imports['state-core'], v = 'extension.views.state-view', view = os.get(v), d = view['ui-data'];
const R = os.refs['state-view'], cm = R.cm, H = os.history.commits, T = os.refs['timeline-view'], cur = T && T.current;
// Typing that local.edit has not picked up yet: leave the editor alone.
if (R.shownEditable && cm.getValue() !== (R.draft === null ? R.base : R.draft)) return;
// A newly chosen block of the timeline: the view shows it, at the version of the block. Older and Newer leave the
// block (local.step), and the view shows the versions.
if (cur && cur.id !== R.block) {
  R.block = cur.id;
  R.onBlock = true;
  const at = H.findIndex(c => c.n === T.versionOf(cur));
  if (R.draft === null) d.position = at >= 0 ? at : H.length - 1;
}
const head = H[H.length - 1], atDraft = R.draft !== null && d.position === H.length;
d.current_state_version = head.n;
d.version = atDraft ? 'draft' : 'v' + H[d.position].n;
d.version_ago = atDraft ? '' : core.ago(H[d.position].at);
const editable = atDraft || (R.draft === null && d.position === H.length - 1);

// What the editor shows: the draft, the live state (newest version), or an older version.
let text, edits = null;
if (atDraft) {
  text = R.draft;
} else if (editable) {
  // The newest version follows the live state; comments and layout stay, only changed values are rewritten.
  const p = core.patchText(R.base, os.get());
  text = p.text;
  // (A key that patchText adds goes at the end of its object, so the order of keys is not compared.)
  if (core.diff(core.parseJsonc(text), os.get()).length) text = JSON.stringify(os.get(), null, 2);
  else if (cm.getValue() === R.base) edits = p.edits;
  R.base = text;
} else {
  text = H[d.position].state;
}

R.setting = true;
if (cm.getValue() !== text) {
  if (edits) cm.operation(() => edits.forEach(x => cm.replaceRange(x.insert, cm.posFromIndex(x.from), cm.posFromIndex(x.to))));
  if (cm.getValue() !== text) {
    // The folded objects stay folded when the text is set again (the live state changes after each call).
    const keep = [], marks = cm.getAllMarks().filter(m => m.__isFold);
    if (marks.length) {
      let sp = {};
      try { sp = core.spans(cm.getValue()); } catch (e) {}
      const objs = Object.keys(sp).filter(k => sp[k].obj);
      marks.forEach(m => {
        const f = m.find(), at = f && cm.indexFromPos(f.from);
        let best = null, size = Infinity;
        if (f) objs.forEach(k => { const r = sp[k]; if (r.start < at && at <= r.end && r.end - r.start < size) { size = r.end - r.start; best = k; } });
        if (best) keep.push(best);
      });
    }
    cm.setValue(text);
    cm.clearHistory();
    if (keep.length) {
      let sp = {};
      try { sp = core.spans(text); } catch (e) {}
      cm.operation(() => keep.forEach(k => { const r = sp[k]; if (r && r.obj) cm.foldCode(CodeMirror.Pos(cm.posFromIndex(r.start).line, 0), { rangeFinder: CodeMirror.fold.brace, widget: '…' }, 'fold'); }));
    }
  }
}
R.setting = false;
R.shownEditable = editable;
cm.setOption('readOnly', editable ? false : 'nocursor');
cm.getWrapperElement().classList.toggle('CodeMirror-readonly', !editable);

if (R.bad !== null) { cm.removeLineClass(R.bad, 'background', 'bad-line'); R.bad = null; }
const at = /line (\d+)/.exec(d.error) || /position (\d+)/.exec(d.error);
if (d.error && at) {
  R.bad = /line/.test(at[0]) ? +at[1] - 1 : cm.posFromIndex(+at[1]).line;
  cm.addLineClass(R.bad, 'background', 'bad-line');
}

// Long strings, and strings of more than one line, show as "..." (a text of only {} or [] shows as it is). A click opens the text in the viewer;
// the pointer on it shows its start, in the colors of its kind (the preview of the timeline).
R.long.forEach(m => m.clear());
R.long = [];
let spans = {};
try { spans = core.spans(text); } catch (e) {}
Object.keys(spans).forEach(k => {
  const r = spans[k], p = JSON.parse(k).join('/');
  if (r.obj || text[r.start] !== '"' || (r.end - r.start < 90 && !text.slice(r.start, r.end).includes('\\n')) || core.emptyText(text.slice(r.start, r.end))) return;
  const w = document.createElement('span');
  w.className = 'long';
  w.textContent = '"..."';
  w.title = p;
  w.addEventListener('mouseenter', () => {
    let value = '';
    try { value = JSON.parse(text.slice(r.start, r.end)); } catch (e) {}
    if (T) T.showTip(w, value, p);
  });
  w.addEventListener('mouseleave', () => T && T.hideTip());
  w.addEventListener('mousedown', e => {
    e.preventDefault();
    if (T) T.hideTip();
    os.call('local.open-viewer', { path: p }, v).catch(console.error);
  });
  R.long.push(cm.markText(cm.posFromIndex(r.start), cm.posFromIndex(r.end), { replacedWith: w, atomic: true }));
});

// The filter: with text, only the entries whose path has it show, with the first and last lines of the objects
// around them; the hidden lines fold into "⋯ N lines". Show empty off hides the entries with an empty value
// without a mark.
R.hide.forEach(m => m.clear());
R.hide = [];
const hide = (a, b, quiet) => {
  const from = quiet && a > 0 ? CodeMirror.Pos(a - 1, cm.getLine(a - 1).length) : CodeMirror.Pos(a, 0), to = CodeMirror.Pos(b, cm.getLine(b).length);
  let opts = { collapsed: true };
  if (!quiet) {
    const w = document.createElement('span');
    w.className = 'sv-hidden';
    w.textContent = '⋯ ' + (b - a + 1) + (b > a ? ' lines' : ' line');
    opts = { replacedWith: w };
  }
  try {
    R.hide.push(cm.markText(from, to, opts));
  } catch (e) {
    // A fold that crosses the hidden lines: open the folds, then hide.
    cm.getAllMarks().filter(m => m.__isFold).forEach(m => m.clear());
    R.hide.push(cm.markText(from, to, opts));
  }
};
// state-core finds the lines to hide; the changes of a block use the same filter text.
core.filterLines(text, spans, d.filter, 'all', { hideEmpty: d.show_empty === false }).forEach(([a, b, why]) => hide(a, b, why === 'empty'));

// The buttons, the filter switches and the bottom bar are drawn again from ui-data (the filter input stays, so
// typing goes on); the viewer opens and closes with ui-data.viewer_path.
const tmp = document.createElement('div');
tmp.innerHTML = os.template(view.html, d);
['#sv-switches', '#sv-checks', '#sv-right', '#sv-foot'].forEach(sel => {
  const el = tmp.querySelector(sel);
  ctx.root.querySelector(sel).replaceWith(el);
  os.bind(el, v);
});
const input = ctx.root.querySelector('#sv-filter-input');
if (document.activeElement !== input && input.value !== d.filter) input.value = d.filter;
ctx.root.querySelector('#sv-viewer').hidden = !d.viewer_path;
ctx.root.querySelector('#sv-viewer-path').textContent = d.viewer_path;
// md files show in the theme that ui-data names; its button is pressed.
const themes = ctx.root.querySelector('#md-themes');
themes.hidden = !/\.md$/.test(d.viewer_path);
themes.querySelectorAll('[data-md-theme]').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.mdTheme === d.md_theme)));
ctx.root.querySelector('#sv-viewer-doc').dataset.mdTheme = d.md_theme;

// The chosen block, in the bottom bar.
const el = (tag, cls, txt) => { const x = document.createElement(tag); if (cls) x.className = cls; if (txt !== undefined) x.textContent = txt; return x; };
const blockEl = ctx.root.querySelector('#sv-block');
blockEl.textContent = '';
if (cur && R.onBlock) {
  blockEl.appendChild(el('b', '', 'Block ' + T.number + ': ' + cur.label));
  blockEl.appendChild(document.createTextNode(' ' + cur.name + ' · ' + (cur.when || T.since(cur.ms))));
}
// The pane under the bar: Details of the chosen block, the changes (of the block, or of the version after Older or
// Newer), or one kind as a tree. All without Changes is the editor.
const kind = d.filter_kind || 'all', inPane = !!(d.details || d.changes || kind !== 'all'), pane = ctx.root.querySelector('#tl-detail');
const editorEl = ctx.root.querySelector('#sv-editor'), wasHidden = editorEl.hidden;
editorEl.hidden = inPane;
pane.hidden = !inPane;
// (the editor does not draw while it is hidden: it draws again when it shows)
if (wasHidden && !inPane) cm.refresh();
if (!inPane) { R.paneKey = null; pane.textContent = ''; return; }
const key = [cur && cur.id, R.onBlock, d.position, d.details, d.changes, kind].join(':'), keep = R.paneKey === key ? pane.scrollTop : 0;
pane.textContent = '';
// A newly chosen block shows its calls one after the other.
pane.classList.toggle('anim', R.paneKey !== key);
R.paneKey = key;
if (!T || !cur) pane.appendChild(el('p', 'tl-text', 'The timeline has no blocks yet.'));
else if (d.details) {
  pane.appendChild(el('p', 'tl-text', cur.text));
  pane.appendChild(el('div', 'tl-detail-sub', 'What happens inside this block'));
  const inside = el('div', 'tl-inside');
  T.drawDetails(inside);
  pane.appendChild(inside);
} else if (d.changes && R.onBlock) T.drawChanges(pane, kind);
else if (d.changes) {
  const p = core.pairAt(d.position, H, R.draft), at = x => x >= H.length ? 'the draft' : H[x].n;
  T.drawPair(pane, kind, T.pairFrom(core.stripRuntime(p.before), core.stripRuntime(p.after), d.position ? at(d.position - 1) : 'nothing', at(d.position)));
} else {
  // one kind, as it is in the state on screen
  let full = os.get();
  try { if (atDraft) full = core.parseJsonc(R.draft); else if (!editable) full = core.parseJsonc(H[d.position].state); } catch (e) {}
  T.kindView(pane, kind, { before: {}, after: {}, full, fullBefore: null, rows: [], head: d.version, state: true });
}
pane.scrollTop = keep;
""")

EDIT = sig("edit", [], r"""
const core = imports['state-core'], d = os.get('extension.views.state-view.ui-data'), R = os.refs['state-view'], H = os.history.commits;
clearTimeout(R.timer);
const text = R.cm.getValue();
// Text back to what was saved is no draft (a comment counts as a change).
R.draft = text === R.base ? null : text;
// (a draft is no block: Changes shows what the draft changes)
if (R.draft !== null) R.onBlock = false;
d.unsaved = R.draft !== null;
d.position = d.unsaved ? H.length : H.length - 1;
d.error = '';
d.fixable = false;
try {
  core.parseJsonc(text);
} catch (e) {
  d.error = e.message;
  try { core.parseJsonc(core.autofix(text)); d.fixable = true; } catch (_) {}
}
""")

STEP = sig("step", ["delta"], r"""
// Older and Newer go through the versions: the view leaves the chosen block.
const d = os.get('extension.views.state-view.ui-data'), R = os.refs['state-view'], H = os.history.commits;
const last = H.length - (R.draft === null ? 1 : 0);
d.position = Math.max(0, Math.min(last, d.position + (+delta || 0)));
R.onBlock = false;
""")

TOGGLE = sig("toggleChanges", [], r"""
// Changes: what the chosen block changed (or the version on screen, after Older or Newer). It leaves Details.
const d = os.get('extension.views.state-view.ui-data');
d.changes = d.details ? true : !d.changes;
d.details = false;
""")

TOGGLE_DETAILS = sig("toggleDetails", [], r"""
// Details: what happens inside the chosen block (its parts, its calls, an agent run in lanes).
const d = os.get('extension.views.state-view.ui-data');
d.details = !d.details;
""")

TOGGLE_TIMELINE = sig("toggleTimeline", [], r"""
// The Timeline button: shows or hides the timeline above the header. It keeps its blocks when it is hidden.
const d = os.get('extension.views.state-view.ui-data');
d.timeline_open = !d.timeline_open;
if (!os.mounted('extension.views.timeline-view')) await ctx.call('extension.functions.render', { view_path: 'extension.views.timeline-view' });
""")

TOGGLE_TRACK = sig("toggleTracking", [], r"""
// Track state: what you do in the state view and the timeline is added as blocks of the timeline.
const d = os.get('extension.views.state-view.ui-data');
d.track_state = !d.track_state;
""")

COLLAPSE = sig("collapseAll", [], r"""
const cm = os.refs['state-view'].cm;
cm.operation(() => {
  for (let l = cm.lastLine(); l > 0; l--) {
    if (CodeMirror.fold.brace(cm, CodeMirror.Pos(l, 0))) cm.foldCode(CodeMirror.Pos(l, 0), { rangeFinder: CodeMirror.fold.brace, widget: '…' }, 'fold');
  }
});
""")


OPEN_VIEWER = sig("openViewer", ["path"], r"""
const d = os.get('extension.views.state-view.ui-data'), R = os.refs['state-view'];
const keys = String(path).split('/'), last = keys[keys.length - 1], isHtml = last === 'html', isCode = last === 'code';
// The value as it is on screen (an older version shows its own).
let shown;
try { shown = core.parseJsonc(R.cm.getValue()); } catch (e) { shown = os.get(); }
const value = keys.reduce((o, k) => (o && typeof o === 'object' ? o[k] : undefined), shown);
if (typeof value !== 'string') throw new Error('Nothing to show at ' + path);
d.viewer_path = path;
R.viewer = { keys, original: value, editable: R.shownEditable && !d.changes, id: '', text: null, timer: null };
const box = ctx.root.querySelector('#sv-viewer');
if (!R.viewerCm) {
  R.viewerCm = CodeMirror(box.querySelector('#sv-viewer-code'), { theme: 'agent', lineNumbers: true, indentUnit: 2, tabSize: 2, matchBrackets: true });
  R.viewerCm.on('change', () => R.viewer && R.viewer.show());
}
R.viewerCm.setOption('mode', isHtml ? 'htmlmixed' : isCode ? 'javascript' : /\.json$/.test(last) ? { name: 'javascript', json: true } : 'text/plain');
R.viewerCm.setOption('lineWrapping', !isCode);
const isMd = /\.md$/.test(last), body = box.querySelector('.sv-viewer-body'), docBox = box.querySelector('#sv-viewer-doc');
body.classList.toggle('code-only', !isHtml);
body.classList.toggle('doc-mode', isMd);
docBox.hidden = !isMd;
docBox.textContent = '';

// html: the view runs next to its code, with a copy of the state that has the html from the editor.
// Its buttons work. What they change stays in the copy; the view's ui-data shows below it after each action.
const name = keys[keys.length - 2];
const run = () => {
  const copy = JSON.parse(JSON.stringify(shown));
  R.viewer.text = R.viewerCm.getValue();
  keys.slice(0, -1).reduce((o, k) => o[k], copy)[last] = R.viewer.text;
  R.viewer.id = name + '-' + Date.now();
  os.preview(box.querySelector('#sv-viewer-view'), copy, keys.slice(0, -1).join('.'), R.viewer.id);
};
// It starts at once, and again a moment after you stop typing.
R.viewer.show = () => {
  if (!isHtml || R.viewerCm.getValue() === R.viewer.text) return;
  clearTimeout(R.viewer.timer);
  if (R.viewer.id) R.viewer.timer = setTimeout(run, 400);
  else run();
};
if (!os.refs.preview) {
  os.refs.preview = true;
  window.addEventListener('message', e => {
    const r = os.refs['state-view'], m = e.data;
    if (!r || !r.viewer || !m || m.agentOSPreview !== r.viewer.id) return;
    const changed = m.changes.map(c => c.split(' ')[1]).filter(p => p.startsWith(r.viewer.keys.slice(0, -1).join('.') + '.ui-data.')).map(p => p.split('.').pop());
    document.getElementById('sv-viewer-state-head').textContent = 'ui-data of ' + r.viewer.keys[r.viewer.keys.length - 2] + (m.call ? ', after ' + m.call : '');
    const pre = document.getElementById('sv-viewer-state');
    pre.textContent = '';
    JSON.stringify(m.uiData, null, 2).split('\n').forEach(line => {
      const row = document.createElement('div'), key = (/^  "([^"]+)":/.exec(line) || [])[1];
      row.textContent = line;
      if (key && changed.includes(key)) row.className = 'chg-updated';
      pre.appendChild(row);
    });
    if (m.error) {
      const row = document.createElement('div');
      row.className = 'bad';
      row.textContent = m.error;
      pre.appendChild(row);
    }
  });
}
document.getElementById('sv-viewer-state-head').textContent = '';
document.getElementById('sv-viewer-state').textContent = '';
R.viewerCm.setValue(value);
R.viewerCm.setOption('readOnly', R.viewer.editable ? false : 'nocursor');
R.viewer.show();

// md: the text shows as a document that you edit in place. Each line is one block; a heading folds its section.
// The viewer's editor keeps the markdown, so closing the viewer puts the edits into the state editor.
if (isMd) {
  const parts = core.mdParse(value), folded = new Set(), editable = R.viewer.editable;
  const save = () => R.viewerCm.setValue(core.mdText(parts));
  const caret = el => {
    const s = getSelection();
    if (!s.rangeCount || !el.contains(s.focusNode)) return el.textContent.length;
    const r = document.createRange();
    r.selectNodeContents(el);
    r.setEnd(s.focusNode, s.focusOffset);
    return r.toString().length;
  };
  const place = (el, at) => {
    el.focus();
    const r = document.createRange(), node = el.firstChild;
    if (node) r.setStart(node, Math.min(at, node.length)); else r.setStart(el, 0);
    r.collapse(true);
    getSelection().removeAllRanges();
    getSelection().addRange(r);
  };
  const draw = focus => {
    const top = docBox.scrollTop, page = document.createElement('article');
    page.className = 'md-page';
    let into = page;
    parts.forEach((part, pi) => {
      if (part.kind === 'svg') {
        const fig = document.createElement('figure');
        fig.className = 'diagram';
        fig.innerHTML = part.text;
        into.appendChild(fig);
        return;
      }
      if (part.kind === 'code') {
        const pre = document.createElement('pre');
        pre.className = 'code';
        pre.textContent = part.text;
        if (editable) {
          pre.contentEditable = 'plaintext-only';
          pre.spellcheck = false;
          pre.addEventListener('input', () => { part.text = pre.textContent; save(); });
        }
        into.appendChild(pre);
        return;
      }
      part.lines.forEach((raw, li) => {
        const line = core.mdLine(raw);
        // Empty lines only make space, except the new one that you type into.
        if (line.type === 'blank' && !(focus && focus[0] === pi && focus[1] === li)) return;
        if (line.type === 'blank') line.type = 'p';
        const heading = line.type[0] === 'h', row = document.createElement(heading ? 'h' + (+line.type[1] + 1) : 'p');
        row.className = 'md-' + line.type;
        if (line.type === 'step') {
          const n = document.createElement('span');
          n.className = 'md-num';
          n.textContent = line.mark.trim();
          row.appendChild(n);
        }
        const t = document.createElement('span');
        t.className = 'md-t';
        t.textContent = line.text;
        t.dataset.at = pi + ':' + li;
        row.appendChild(t);
        if (line.type === 'h1') {
          page.appendChild(row);
          into = page;
        } else if (heading) {
          // The section is this heading and everything up to the next heading.
          const sec = document.createElement('section'), fold = document.createElement('button'), key = line.text;
          sec.className = 'md-sec' + (folded.has(key) ? ' folded' : '');
          fold.className = 'md-fold';
          fold.type = 'button';
          fold.title = 'Fold or open this section';
          fold.setAttribute('aria-expanded', String(!folded.has(key)));
          fold.addEventListener('mousedown', e => e.preventDefault());
          fold.addEventListener('click', () => {
            if (folded.has(key)) folded.delete(key); else folded.add(key);
            sec.classList.toggle('folded', folded.has(key));
            fold.setAttribute('aria-expanded', String(!folded.has(key)));
          });
          row.prepend(fold);
          sec.appendChild(row);
          into = document.createElement('div');
          into.className = 'md-body';
          sec.appendChild(into);
          page.appendChild(sec);
        } else {
          into.appendChild(row);
        }
        if (!editable) return;
        t.contentEditable = 'plaintext-only';
        t.addEventListener('input', () => { parts[pi].lines[li] = line.mark + t.textContent.replace(/\n/g, ' '); save(); });
        t.addEventListener('keydown', e => {
          const lines = parts[pi].lines;
          if (e.key === 'Enter') {
            // Enter starts a new block of the same kind after this one (a new item, the next step, a paragraph).
            e.preventDefault();
            const at = caret(t), text = t.textContent;
            lines[li] = line.mark + text.slice(0, at);
            lines.splice(li + 1, 0, (line.type === 'item' ? '- ' : line.type === 'step' ? (parseInt(line.mark, 10) + 1) + '. ' : '') + text.slice(at));
            save();
            draw([pi, li + 1, 0]);
          } else if (e.key === 'Backspace' && caret(t) === 0 && !String(getSelection())) {
            // Backspace at the start: first the mark goes (the block becomes a paragraph), then the block joins the one before.
            if (line.mark) {
              e.preventDefault();
              lines[li] = t.textContent;
              save();
              draw([pi, li, 0]);
            } else if (li > 0) {
              e.preventDefault();
              if (!lines[li - 1].trim()) {
                lines.splice(li - 1, 1);
                save();
                draw([pi, li - 1, 0]);
              } else {
                const end = core.mdLine(lines[li - 1]).text.length;
                lines[li - 1] += t.textContent;
                lines.splice(li, 1);
                save();
                draw([pi, li - 1, end]);
              }
            }
          }
        });
      });
    });
    docBox.textContent = '';
    docBox.appendChild(page);
    docBox.scrollTop = top;
    const el = focus && docBox.querySelector('[data-at="' + focus[0] + ':' + focus[1] + '"]');
    if (el) place(el, focus[2]);
  };
  draw(null);
}
box.hidden = false;
setTimeout(() => R.viewerCm.refresh(), 0);
""")

CLOSE_VIEWER = sig("closeViewer", [], r"""
const core = imports['state-core'], d = os.get('extension.views.state-view.ui-data'), R = os.refs['state-view'];
let applied = false;
// Edited html or code goes back into the state editor as an unsaved change.
if (R.viewer && R.viewer.editable && R.viewerCm.getValue() !== R.viewer.original) {
  const text = R.cm.getValue(), r = core.spans(text)[JSON.stringify(R.viewer.keys)];
  if (r) {
    R.cm.replaceRange(JSON.stringify(R.viewerCm.getValue()), R.cm.posFromIndex(r.start), R.cm.posFromIndex(r.end));
    applied = true;
  }
}
d.viewer_path = '';
if (R.viewer) clearTimeout(R.viewer.timer);
R.viewer = null;
ctx.root.querySelector('#sv-viewer-view').srcdoc = '';
ctx.root.querySelector('#sv-viewer').hidden = true;
if (applied) await ctx.call('local.edit', {});
""")

SAVE = sig("save", [], r"""
const core = imports['state-core'], v = 'extension.views.state-view', R = os.refs['state-view'], cm = R.cm, H = os.history;
clearTimeout(R.timer);
let text = cm.getValue(), fixed = false, next;
if (text === R.base) throw new Error('Nothing to save');
// Broken JSON is repaired first; the repaired text is what gets saved.
try {
  next = core.parseJsonc(text);
} catch (e) {
  text = core.autofix(text);
  next = core.parseJsonc(text);
  fixed = true;
}
const head = H.commits[H.commits.length - 1];
// The new version records this view as it is after saving (the text may hold older ui-data).
const d = core.getPath(next, v + '.ui-data');
if (d) {
  Object.assign(d, { current_state_version: head.n + 1, position: H.commits.length, version: 'v' + (head.n + 1), version_ago: 'just now', unsaved: false, error: '', fixable: false, viewer_path: os.get(v + '.ui-data.viewer_path') });
  text = core.patchText(text, next).text;
}
const c = await H.put(core.makeCommit(head, text, new Date().toISOString()));
os.replace(next);
R.draft = null;
// (the new version is on screen: Changes shows what it changed)
R.onBlock = false;
R.base = text;
R.setting = true;
if (cm.getValue() !== text) { const cur = cm.getCursor(); cm.setValue(text); cm.setCursor(cur); }
R.setting = false;
// Saved: the editor's border turns green for a moment.
const box = ctx.root.querySelector('#sv-editor');
box.classList.remove('saved');
void box.offsetWidth;
box.classList.add('saved');
setTimeout(() => box.classList.remove('saved'), 2000);
await ctx.call('extension.functions.render', { view_path: 'extension.views.header-view' });
return { version: c.n, changes: c.paths.slice(0, 50), fixed };
""")

FILTER = sig("filter", ["text"], r"""
// local.refresh shows in the editor only the paths that have the text.
const d = os.get('extension.views.state-view.ui-data');
d.filter = String(text || '');
""")

FILTER_KIND = sig("filterKind", ["kind"], r"""
// local.refresh shows only this kind, as a tree (all shows the editor). It leaves Details.
const d = os.get('extension.views.state-view.ui-data');
if (!['all', 'files', 'views', 'functions', 'network', 'environment'].includes(kind)) throw new Error('No kind ' + kind);
d.filter_kind = kind;
d.details = false;
""")

TOGGLE_EMPTY = sig("toggleEmpty", [], r"""
// local.refresh hides the entries with an empty value ({}, [], "" or null) when show_empty is false.
const d = os.get('extension.views.state-view.ui-data');
d.show_empty = !d.show_empty;
""")

SET_MD_THEME = sig("setMdTheme", ["theme"], r"""
const d = os.get('extension.views.state-view.ui-data');
const names = ['reader', 'white', 'black', 'sepia', 'night', 'mono'];
if (!names.includes(theme)) throw new Error('No theme ' + theme + '. Themes: ' + names.join(', '));
d.md_theme = theme;
""")

TL_INIT = sig("init", [], r"""
// The timeline draws itself after every call (local.refresh), and now. A replay of an earlier render stops.
const old = os.refs['timeline-view'];
if (old && old.timer) clearInterval(old.timer);
os.refs['timeline-view'] = { parts: new Set(), files: {}, steps: [], end: null, timer: null, shown: undefined };
os.watch('extension.views.timeline-view', 'local.refresh');
await ctx.call('local.refresh', { after: 'local.init' });
// After the Restart button: the state view shows the last AI run notification (no block chosen).
let replay = location.hash === '#timeline-replay';
try { replay = replay || sessionStorage.getItem('agent-os.timeline-replay') === '1'; sessionStorage.removeItem('agent-os.timeline-replay'); } catch (e) {}
if (location.hash === '#timeline-replay') try { history.replaceState(null, '', location.pathname + location.search); } catch (e) {}
if (replay) await ctx.call('local.select', { id: null });
""")

TL_RELOAD = sig("reload", [], r"""
// Restart: reloads the page, so the history starts again. The timeline opens again on the last AI run notification.
if (os.get('extension.views.state-view.ui-data.unsaved')) throw new Error('The state has unsaved changes. Save them first.');
try { sessionStorage.setItem('agent-os.timeline-replay', '1'); } catch (e) { location.hash = 'timeline-replay'; }
location.reload();
""")

TL_REFRESH = sig("refresh", ["after"], r"""
const v = 'extension.views.timeline-view', sv = 'extension.views.state-view', d = os.get(v + '.ui-data'), R = os.refs['timeline-view'];
const svd = os.get(sv + '.ui-data') || {};
// The timeline shows above the header when the Timeline button of the state view is on. Hidden, it still keeps the
// blocks: the state view shows the chosen block.
ctx.root.hidden = !(os.mounted(sv) && svd.timeline_open);
// The bar is drawn again from ui-data.
const tmp = document.createElement('div');
tmp.innerHTML = os.template(os.get(v + '.html'), d);
const bar = tmp.querySelector('.tl-bar');
ctx.root.querySelector('.tl-bar').replaceWith(bar);
os.bind(bar, v);

// The calls of this page load, from the runtime's call log. A call that a different call made goes inside it.
// What you do in the timeline, in the state view (clicks, the replay) and with the record button is a block only
// when Track state (ui-data.track_state of the state view) is on.
const mine = r => [v + '.', sv + '.', 'extension.views.recorder-view.'].some(p => String(r.related && r.related.fn).indexOf(p) === 0);
const recs = os.calls, kids = {}, tops = [], byIdMap = {};
recs.forEach(r => {
  byIdMap[r.id] = r;
  const p = r.related && r.related.parent;
  if (typeof p === 'number') (kids[p] = kids[p] || []).push(r);
  else if (svd.track_state || !mine(r)) tops.push(r);
});
const byId = (a, b) => a.id - b.id, t0 = performance.timeOrigin;
const el = (tag, cls, text) => { const x = document.createElement(tag); if (cls) x.className = cls; if (text !== undefined) x.textContent = text; return x; };
const since = ms => '+' + (ms / 1000).toFixed(2) + 's';
const short = x => { const s = x === undefined ? '' : JSON.stringify(x); return s && s.length > 90 ? s.slice(0, 87) + '...' : s; };
const what = r => {
  const via = r.input && r.input.via, rel = r.related || {};
  if (r.name === 'loadState') return ['Load the state', 'Reads ' + rel.commits + (rel.commits === 1 ? ' saved version' : ' saved versions') + ' from the ' + rel.store + ' store. The newest, v' + rel.head + ', is the live state.'];
  if (r.name === 'loadNewerVersion') {
    const vv = versionsOf(r), src = vv && vv.head.source;
    return ['New version', 'v' + (r.input && r.input.head) + (src ? ' from git commit ' + String(src.git).slice(0, 7) + ': ' + src.message : ' was saved in a different place') + '. It runs here now.'];
  }
  if (r.name === 'runTest') return ['Test', (r.input.fn || '') + ': ' + (r.input.test || '')];
  if (via === 'start') return ['Start the page', 'Renders index-view. Its local.init renders the views in it.'];
  if (via === 'click') return ['Click', 'A button of ' + String(r.input.view || '').split('.').pop() + ' calls this function.'];
  if (via === 'watch') return ['Watch', 'Runs after a call, because its view watches the state.'];
  return ['Call', 'Code called this function.'];
};
const changesOf = r => (r.related && r.related.stateChanges) || [];
// A new version: the version that ran before it (from) and the new one (head), read once.
R.versions = R.versions || {};
const versionsOf = r => {
  const H = (os.history && os.history.commits) || [], head = r.input && r.input.head;
  const from = r.input && typeof r.input.from === 'number' ? r.input.from : head - 1, key = from + '>' + head;
  if (!R.versions[key]) {
    const a = H.find(c => c.n === from), b = H.find(c => c.n === head);
    if (!a || !b) return null;
    const before = core.stripRuntime(core.parseJsonc(a.state)), after = core.stripRuntime(core.parseJsonc(b.state));
    R.versions[key] = { from: a, head: b, before, after, changes: core.diff(before, after) };
  }
  return R.versions[key];
};
const countAll = r => changesOf(r).length + (kids[r.id] || []).reduce((n, k) => n + countAll(k), 0);
const changeList = r => {
  const list = el('ul', 'tl-changes');
  changesOf(r).forEach(c => {
    const li = el('li', 'tl-change ' + c.type);
    li.appendChild(el('span', 'tl-path', c.path));
    li.appendChild(el('span', 'tl-val', c.type === 'added' ? short(c.after) : c.type === 'deleted' ? short(c.before) : short(c.before) + '  →  ' + short(c.after)));
    list.appendChild(li);
  });
  return list;
};
// Why a call ran: a click, the page start, a watch after a call, or the call it ran inside.
const why = r => {
  const via = r.input && r.input.via, p = r.related && r.related.parent, view = String((r.input && r.input.view) || '').split('.').pop();
  if (via === 'start') return 'The page starts: the runtime calls it for index-view.';
  if (via === 'click') return 'You clicked a button of ' + view + ' (its data-call is ' + r.name + ').';
  if (via === 'watch') return view + ' watches the state, so it runs after every call. This time after ' + ((r.input.input && r.input.input.after) || (byIdMap[p] && byIdMap[p].name) || 'a call') + '.';
  if (r.name === 'runTest') return 'os.runTests() runs the tests written in the state.';
  if (r.name === 'loadState') return 'The runtime loads the state when the page opens, before anything is drawn.';
  if (r.name === 'loadNewerVersion') return 'A newer version was saved somewhere else, and the runtime follows the newest version.';
  if (typeof p === 'number' && byIdMap[p]) return byIdMap[p].name + (byIdMap[p].input && byIdMap[p].input.view ? ' of ' + byIdMap[p].input.view.split('.').pop() : '') + ' calls it.';
  return 'Code called it.';
};
const fnDef = r => { const path = r.related && r.related.fn; const def = path && os.get(path); return def && typeof def === 'object' ? { path, def } : null; };
const callRow = (r, depth, n) => {
  const f = fnDef(r), key = 'call:' + r.id;
  const row = el('div', 'tl-call' + (r.ok ? '' : ' bad') + (f && f.def.code ? ' can-open' : ''));
  row.style.setProperty('--depth', depth);
  row.style.setProperty('--i', Math.min(n || 0, 24));
  const head = el(f && f.def.code ? 'button' : 'div', 'tl-call-head');
  if (n !== undefined) head.appendChild(el('span', 'tl-sub-n', String(n + 1)));
  head.appendChild(el('span', 'tl-name', r.name));
  const input = r.input && r.input.input;
  if (input && typeof input === 'object' && Object.keys(input).length) head.appendChild(el('span', 'tl-input', short(input)));
  head.appendChild(el('span', 'tl-ms', r.ms + ' ms'));
  row.appendChild(head);
  const say = (label, text) => { const x = el('div', 'tl-say'); x.appendChild(el('b', '', label)); x.appendChild(document.createTextNode(text)); row.appendChild(x); };
  if (f && f.def.docs) say('What it does ', f.def.docs);
  say('Why it ran ', why(r));
  if (r.error) row.appendChild(el('div', 'tl-error', r.error));
  ((r.related && r.related.errors) || []).filter(x => x !== 'threw: ' + r.error).forEach(x => row.appendChild(el('div', 'tl-error', x)));
  if (changesOf(r).length) { say('What it changed ', ''); row.appendChild(changeList(r)); }
  else say('What it changed ', 'nothing in the state.');
  if (!(f && f.def.code)) return row;
  // A click on the name shows the function's code from the state.
  const body = el('div', 'tl-more');
  row.appendChild(body);
  const show = () => {
    const open = R.parts.has(key);
    row.classList.toggle('open', open);
    head.setAttribute('aria-expanded', String(open));
    body.textContent = '';
    if (open) body.appendChild(code(f.path + '.code', f.def.code, 'js', 1));
  };
  head.addEventListener('click', () => { if (R.parts.has(key)) R.parts.delete(key); else R.parts.add(key); show(); });
  show();
  return row;
};
// What happens inside a step: its call, then every call inside it, in the order they started.
const inside = (r, box, from) => {
  let n = from || 0;
  box.appendChild(callRow(r, 0, n++));
  const walk = (p, depth) => (kids[p.id] || []).sort(byId).forEach(k => { box.appendChild(callRow(k, depth, n++)); walk(k, depth + 1); });
  walk(r, 1);
};

// What happens inside the steps before the first call, from the browser's timings and the runtime.
const kb = n => n ? (n / 1024).toFixed(1) + ' KB' : '';
const res = end => performance.getEntriesByType('resource').filter(e => e.name.split('?')[0].endsWith(end)).shift();
const nav = performance.getEntriesByType('navigation')[0];
const load = tops.find(r => r.name === 'loadState');
const runtime = Array.from(document.scripts).find(s => !s.src && s.textContent.indexOf('agentOS') >= 0);
const coreFile = res('/state-core.js'), seed = res('/state.json');
const session = (load && load.input && load.input.session) || '?';
// What a part shows when it opens: a file, a table, or the runtime's run.
const getText = url => R.files[url] || (R.files[url] = fetch(url).then(r => { if (!r.ok) throw new Error(url + ': HTTP ' + r.status); return r.text(); }));
// A code box: colored, with line numbers, read only. js and html are formatted to read; code that keeps its own
// line numbers (first) is shown as it is written.
const code = (label, text, mode, first) => {
  const box = el('div', 'tl-file');
  let shown = text;
  try {
    if (mode === 'js' && !first) shown = js_beautify(text, { indent_size: 2, max_preserve_newlines: 2 });
    if (mode === 'html' && !first) shown = html_beautify(text, { indent_size: 2, indent_scripts: 'normal', max_preserve_newlines: 2 });
  } catch (e) { shown = text; }
  box.appendChild(el('div', 'tl-file-head', label + '  ·  ' + text.split('\n').length + ' lines  ·  ' + kb(text.length) + (shown !== text ? '  ·  formatted to read' : '')));
  const host = el('div', 'tl-code');
  box.appendChild(host);
  const cm = CodeMirror(host, {
    value: shown, readOnly: true, lineNumbers: true, theme: 'agent', firstLineNumber: first || 1,
    mode: mode === 'html' ? 'htmlmixed' : mode === 'json' ? { name: 'javascript', json: true } : mode === 'text' ? null : 'javascript'
  });
  cm.setSize(null, Math.min(420, cm.lineCount() * 19 + 10));
  host.cm = cm;
  // CodeMirror measures itself once the box is on the page.
  setTimeout(() => cm.refresh());
  return box;
};
// The state cut down to the changes, as the state view shows it: key colors, folds, added green, updated yellow
// (with the old value), deleted red. The filter text of the state view hides the other lines.
// Long strings, and strings of more than one line, show as "...", as in the state view: the pointer on it shows its
// start, a click opens the whole text in the viewer.
const preview = (path, text) => {
  if (R.viewerBox) R.viewerBox.remove();
  const v = el('div', 'tl-viewer'), bar = el('div', 'tl-viewer-bar'), close = el('button', 'btn', '×');
  bar.appendChild(el('span', '', path));
  close.setAttribute('aria-label', 'Close');
  close.addEventListener('click', () => { v.remove(); R.viewerBox = null; });
  bar.appendChild(close);
  v.appendChild(bar);
  // a file shows in the file viewer; html and code of a view or a function, as code
  const name = /\.\w+$/.test(path) ? path : /(^|\/)html$/.test(path) ? path + '.html' : /(^|\/)code$/.test(path) ? path + '.js' : path + '.txt';
  v.appendChild(fileView(name, text));
  document.body.appendChild(v);
  R.viewerBox = v;
  const esc = e => { if (e.key === 'Escape') { v.remove(); R.viewerBox = null; document.removeEventListener('keydown', esc); } };
  document.addEventListener('keydown', esc);
};
// The preview of a long text (the pointer on "..."): its first lines in the colors of its kind (md, js, html, css,
// json). An updated text shows its changes: the lines it lost red, the lines it got green, from a little before the
// first change. The state view uses it too.
R.showTip = (anchor, value, path, before) => {
  // (one preview on the page, also after the timeline renders again)
  R.tip = document.querySelector('body > .long-tip');
  if (!R.tip) {
    R.tip = el('div', 'long-tip');
    R.tip.hidden = true;
    document.body.appendChild(R.tip);
  }
  const max = 16, now = String(value), lines = [], cls = [];
  if (typeof before === 'string' && before !== now) {
    const A = before.split('\n'), B = now.split('\n'), ld = lineDiff(before, now);
    let i = 0, j = 0;
    while (i < A.length || j < B.length) {
      if (i < A.length && ld.del.has(i)) { lines.push(A[i++]); cls.push('chg-deleted'); }
      else if (j < B.length && ld.add.has(j)) { lines.push(B[j++]); cls.push('chg-added'); }
      else { lines.push(B[j]); cls.push(''); i++; j++; }
    }
  } else now.split('\n').forEach(l => { lines.push(l); cls.push(''); });
  const first = Math.max(0, cls.findIndex(c => c) - 3), shown = lines.slice(first, first + max), marks = cls.slice(first, first + max);
  const mode = /\.md$/.test(path) ? 'markdown' : /\.html?$|(^|\/)html$/.test(path) ? 'htmlmixed' : /\.css$/.test(path) ? 'css'
    : /\.jsonc?$/.test(path) ? { name: 'javascript', json: true } : /\.m?js$|(^|\/)code$/.test(path) ? 'javascript' : null;
  R.tip.textContent = '';
  R.tip.hidden = false;
  const cm = CodeMirror(R.tip, { value: shown.join('\n'), mode, theme: 'agent', readOnly: 'nocursor', lineWrapping: true });
  marks.forEach((c, l) => { if (c) cm.addLineClass(l, 'background', c); });
  const rest = (first ? first + ' lines before' : '') + (lines.length > first + max ? (first ? ', ' : '') + (lines.length - first - max) + ' lines after' : '');
  if (rest) R.tip.appendChild(el('div', 'tip-more', '… ' + rest));
  cm.refresh();
  const b = anchor.getBoundingClientRect(), t = R.tip.getBoundingClientRect();
  R.tip.style.left = Math.max(8, Math.min(b.left, innerWidth - t.width - 8)) + 'px';
  R.tip.style.top = (b.bottom + 6 + t.height < innerHeight ? b.bottom + 6 : Math.max(8, b.top - 6 - t.height)) + 'px';
};
R.hideTip = () => document.querySelectorAll('body > .long-tip, body > .why-tip').forEach(t => { t.hidden = true; });
const longTexts = (cm, text, marks) => {
  let spans = {};
  try { spans = core.spans(text); } catch (e) { return; }
  Object.keys(spans).forEach(k => {
    const r = spans[k], p = JSON.parse(k).join('/');
    if (r.obj || text[r.start] !== '"' || (r.end - r.start < 90 && !text.slice(r.start, r.end).includes('\\n')) || core.emptyText(text.slice(r.start, r.end))) return;
    let value = '';
    try { value = JSON.parse(text.slice(r.start, r.end)); } catch (e) {}
    // an updated text: the old text, for its changes
    const line = cm.posFromIndex(r.start).line, m = (marks || []).find(x => x.type === 'updated' && x.from <= line && line <= x.to);
    const w = el('span', 'long', '"..."');
    w.title = p;
    w.addEventListener('mouseenter', () => R.showTip(w, value, p, m && m.before));
    w.addEventListener('mouseleave', R.hideTip);
    w.addEventListener('mousedown', e => { e.preventDefault(); R.hideTip(); preview(p, value); });
    cm.markText(cm.posFromIndex(r.start), cm.posFromIndex(r.end), { replacedWith: w, atomic: true });
  });
};
// (opts.all: no filter, for one item of a kind view)
const stateBox = (label, cv, opts) => {
  const sd = (opts && opts.all) ? {} : svd;
  const box = el('div', 'tl-file');
  box.appendChild(el('div', 'tl-file-head', label + '  ·  ' + cv.text.split('\n').length + ' lines  ·  ' + kb(cv.text.length)));
  const host = el('div', 'tl-code');
  box.appendChild(host);
  const cm = CodeMirror(host, {
    value: cv.text, readOnly: true, lineNumbers: true, theme: 'agent', mode: { name: 'javascript', json: true },
    foldGutter: true, gutters: ['CodeMirror-linenumbers', 'CodeMirror-foldgutter']
  });
  cm.addOverlay(core.keyOverlay);
  longTexts(cm, cv.text, cv.marks);
  cv.marks.forEach(m => {
    for (let l = m.from; l <= m.to; l++) cm.addLineClass(l, 'background', 'chg-' + m.type);
    if (m.type === 'updated') {
      const was = JSON.stringify(m.before), long = typeof m.before === 'string' && (m.before.length > 80 || m.before.includes('\n'));
      const w = el('span', 'was', 'was ' + (long ? '"..."' : was));
      if (long) {
        // the pointer on it shows the changes; a click opens the old text
        const path = m.path.join('/');
        w.title = 'Click to open the old text';
        w.style.cursor = 'pointer';
        w.addEventListener('mouseenter', () => R.showTip(w, typeof m.after === 'string' ? m.after : '', path, m.before));
        w.addEventListener('mouseleave', R.hideTip);
        w.addEventListener('mousedown', e => { e.preventDefault(); R.hideTip(); preview('was', m.before); });
      }
      cm.setBookmark(CodeMirror.Pos(m.to, cm.getLine(m.to).length), { widget: w });
    }
  });
  let hidden = 0;
  core.filterLines(cv.text, null, sd.filter, {}).forEach(([a, b]) => {
    hidden += b - a;
    cm.markText(CodeMirror.Pos(a, 0), CodeMirror.Pos(b, cm.getLine(b).length), { replacedWith: el('span', 'sv-hidden', '⋯ ' + (b - a + 1) + (b > a ? ' lines' : ' line')) });
  });
  cm.setSize(null, Math.min(520, (cm.lineCount() - hidden) * 19 + 10));
  host.cm = cm;
  setTimeout(() => cm.refresh());
  return box;
};
// A row of a table of changes shows when its path has the text of the filter of the state view.
const passes = keys => {
  const q = String(svd.filter || '').trim().toLowerCase();
  return !q || keys.join('/').toLowerCase().includes(q);
};
// The lines of the runtime script that do something: the line that matches, with the comment lines above it.
// With a brace after the match, the whole block up to its closing brace.
const src = runtime ? runtime.textContent : '';
const linesOf = (re, block) => {
  const all = src.split('\n');
  let at = all.findIndex(l => re.test(l));
  if (at < 0) return null;
  let from = at;
  while (from > 0 && /^\s*\/\//.test(all[from - 1])) from--;
  let to = at;
  if (block) { let depth = 0; for (let i = at; i < all.length; i++) { for (const ch of all[i]) { if (ch === '{') depth++; else if (ch === '}') depth--; } if (depth <= 0) { to = i; break; } } }
  // Line numbers in index.html: the runtime script starts after the lines before it.
  return getText(location.href).catch(() => document.documentElement.outerHTML).then(html => {
    const before = (html.slice(0, Math.max(0, html.indexOf(src.slice(0, 200)))).match(/\n/g) || []).length;
    return { text: all.slice(from, to + 1).join('\n'), first: from + before + 1 };
  });
};
const snippet = (re, block) => Promise.resolve(linesOf(re, block)).then(s => s ? code('index.html, line ' + s.first, s.text, 'js', s.first) : el('div', 'tl-part-text', 'Not found in the runtime script.'));
const table = rows => {
  const tb = el('table', 'tl-table');
  rows.forEach(r => { const tr = el('tr'); r.forEach((c, i) => tr.appendChild(el(i ? 'td' : 'th', '', c === undefined ? '' : String(c)))); tb.appendChild(tr); });
  return tb;
};
const at = ms => typeof ms === 'number' ? since(ms) : '';
const render = tops.find(r => r.input && r.input.via === 'start');
const run = () => table([
  [at(os.started), 'The runtime script starts. It makes the session id, the call tracker and os, in under 1 ms.'],
  [at(load && Date.parse(load.at) - t0), 'loadState: downloads state.json, connects to the database, reads the saved versions and parses the newest (' + (load ? load.ms : '?') + ' ms).'],
  [at(load && Date.parse(load.at) - t0 + load.ms), 'The state is loaded: v' + (load && load.related ? load.related.head : '?') + '.'],
  [at(render && Date.parse(render.at) - t0), 'start() calls extension.functions.render for index-view (' + (render ? render.ms : '?') + ' ms, ' + (render ? 1 + countCalls(render) : '?') + ' calls).'],
  [at(render && Date.parse(render.at) - t0 + render.ms), 'follow() starts listening to the commits collection for newer versions.']
]);
const countCalls = r => (kids[r.id] || []).reduce((n, k) => n + 1 + countCalls(k), 0);
const history = os.history || { commits: [] };
// What each part of os is for.
const OS_DOCS = {
  get: 'Reads a value of the state by its path, for example get("extension.views.header-view.ui-data"). With no path, it gives the whole state.',
  set: 'Writes a value into the state at a path.',
  replace: 'Replaces the whole state. The state view uses it to show a saved version.',
  clone: 'Makes a deep copy of a value.',
  call: 'Calls a function of the state by its name. It records the call in os.calls, checks what it changed against its expected-state-change, and then runs the watchers. Inside a function, ctx.call does the same with that function as the parent, so most functions use ctx.call.',
  template: "Fills a view's html with its ui-data: ${d.x} is a ui-data value, ${e(x)} escapes it.",
  mounted: 'Says if a view is on the page.',
  setMounted: 'Marks a view as on or off the page. Off also removes its watcher and its refs.',
  watch: 'Makes a function of a view run after every call, so the view can draw itself again.',
  bind: 'Makes every button with data-call in an element call that function when it is clicked, with its data-input.',
  runTests: 'Runs the tests written in the state and checks each one.',
  calls: 'The records of every call of this page load. The timeline is drawn from them.',
  started: 'When the runtime started, in ms after the page opened.',
  preview: 'Runs one view in a frame with a copy of the state: its buttons work and nothing is saved.',
  history: 'The saved versions read from the database (commits), and whether this page can save.',
  refs: 'Things a view keeps that are not state: editors, timers, which blocks are open.'
};
// The functions in the state whose code uses os.<name>.
const codes = [];
(function walk(o, p) {
  if (!o || typeof o !== 'object') return;
  if (typeof o.code === 'string' && o.code) codes.push([p, o.code]);
  Object.keys(o).forEach(k => walk(o[k], p ? p + '.' + k : k));
})(os.get(), '');
// The code of a part of os: the function itself, then the runtime functions it calls.
const osCode = k => {
  const x = os[k];
  if (typeof x !== 'function') return JSON.stringify(x, (key, val) => val instanceof Set ? Array.from(val) : val, 2) || String(x);
  let out = x.toString();
  (out.match(/\b[a-zA-Z_]\w*(?=\()/g) || []).filter((n, i, a) => a.indexOf(n) === i && n !== 'function').forEach(n => {
    const at = src.indexOf('function ' + n + '(');
    if (at < 0) return;
    let depth = 0, i = src.indexOf('{', at);
    for (; i < src.length; i++) { if (src[i] === '{') depth++; else if (src[i] === '}' && --depth === 0) break; }
    out += '\n\n// the runtime\'s ' + n + '(), in index.html\n' + src.slice(at, i + 1);
  });
  return out;
};
const osList = () => {
  const box = el('div', 'tl-inside');
  Object.keys(os).forEach((k, n) => {
    const users = codes.filter(([p, c]) => new RegExp('\\bos\\.' + k + '\\b').test(c)).map(([p]) => p.replace(/\.code$/, ''));
    const times = p => os.calls.filter(r => r.related && r.related.fn === p).length;
    box.appendChild(partRow({
      name: 'os.' + k,
      text: (OS_DOCS[k] || '') + '  Used by ' + (users.length ? users.length + (users.length === 1 ? ' function' : ' functions') : 'no function in the state') + '.',
      more: () => {
        const b = el('div');
        if (users.length) b.appendChild(table([['used by', 'ran on this page load']].concat(users.map(p => [p, times(p) + (times(p) === 1 ? ' time' : ' times')]))));
        b.appendChild(code('os.' + k, osCode(k), 'js'));
        return b;
      }
    }, n, 'os:' + k));
  });
  return box;
};
// Each part says what happens and why. Opened, it shows where it happens and what it made.
const group = (...xs) => Promise.all(xs.map(x => typeof x === 'function' ? x() : x)).then(nodes => { const b = el('div', 'tl-group'); nodes.forEach(n => n && b.appendChild(n)); return b; });
const label = text => el('div', 'tl-detail-sub', text);
// Which lines are only in a (deleted) and only in b (added): the longest common lines stay.
const lineDiff = (a, b) => {
  const A = a.split('\n'), B = b.split('\n'), del = new Set(), add = new Set();
  let s = 0, e = 0;
  while (s < A.length && s < B.length && A[s] === B[s]) s++;
  while (e < A.length - s && e < B.length - s && A[A.length - 1 - e] === B[B.length - 1 - e]) e++;
  const a2 = A.slice(s, A.length - e), b2 = B.slice(s, B.length - e), N = a2.length, M = b2.length;
  if (N * M > 4e6) { a2.forEach((x, i) => del.add(s + i)); b2.forEach((x, j) => add.add(s + j)); return { del, add }; }
  const L = Array.from({ length: N + 1 }, () => new Int32Array(M + 1));
  for (let i = N - 1; i >= 0; i--) for (let j = M - 1; j >= 0; j--) L[i][j] = a2[i] === b2[j] ? L[i + 1][j + 1] + 1 : Math.max(L[i + 1][j], L[i][j + 1]);
  let i = 0, j = 0;
  while (i < N && j < M) {
    if (a2[i] === b2[j]) { i++; j++; } else if (L[i + 1][j] >= L[i][j + 1]) del.add(s + i++); else add.add(s + j++);
  }
  while (i < N) del.add(s + i++);
  while (j < M) add.add(s + j++);
  return { del, add };
};
// A file before and now, side by side: red lines are only before, green lines are only now.
const sideCode = (path, from, head, a, b) => {
  const mode = /\.html$/.test(path) ? 'html' : /\.js$/.test(path) ? 'js' : /\.jsonc?$/.test(path) ? 'json' : 'text';
  const diff = lineDiff(a || '', b || ''), g = el('div', 'tl-files');
  const L = x => typeof x === 'number' ? 'v' + x : x;
  const left = code(L(from) + (a === undefined ? ': not there' : ''), a || '', mode, 1), right = code(L(head) + (b === undefined ? ': deleted' : ''), b || '', mode, 1);
  const mark = (box, lines, cls) => {
    const cm = box.querySelector('.tl-code').cm, first = Math.min(...lines);
    lines.forEach(l => cm.addLineClass(l, 'background', cls));
    if (lines.size) setTimeout(() => cm.scrollIntoView({ line: first, ch: 0 }, 60));
  };
  mark(left, diff.del, 'chg-deleted');
  mark(right, diff.add, 'chg-added');
  g.appendChild(left);
  g.appendChild(right);
  return g;
};
// The source of a version explains each part: how it worked before, how it works now.
const sideBySide = list => {
  const g = el('div', 'tl-explain');
  ['Part', 'Before', 'Now'].forEach(h => g.appendChild(el('div', 'tl-side-head', h)));
  list.forEach(x => {
    g.appendChild(el('div', 'tl-side-part', x.part));
    g.appendChild(el('div', 'tl-side-before', x.before));
    g.appendChild(el('div', 'tl-side-now', x.now));
  });
  return g;
};
// The files of the agents, as path -> text.
const filesOf = st => {
  const out = {}, agents = (st && st.agents) || {}, names = Object.keys(agents);
  const flat = (o, p) => Object.keys(o || {}).forEach(k => {
    const x = o[k], q = p ? p + '/' + k : k;
    if (x && typeof x === 'object') flat(x, q); else out[q] = String(x);
  });
  names.forEach(a => flat(agents[a] && agents[a].files, names.length > 1 ? a : ''));
  return out;
};
const newerParts = r => {
  const vv = versionsOf(r);
  if (!vv) return [{ name: 'The versions', what: 'The two versions are not in the history of this page.' }];
  const src = vv.head.source, from = vv.from.n, head = vv.head.n, fa = filesOf(vv.before), fb = filesOf(vv.after);
  const changed = Array.from(new Set(Object.keys(fa).concat(Object.keys(fb)))).filter(k => fa[k] !== fb[k])
    .map(k => ({ path: k, type: !(k in fa) ? 'added' : !(k in fb) ? 'deleted' : 'updated' }));
  const parts = [
    { name: 'Where it came from',
      what: src ? 'A Claude Code session changed the files of ' + (src.branch || 'main') + ', made git commit ' + String(src.git).slice(0, 7) + ' (' + src.message + ') and saved v' + head + '.'
        : 'v' + head + ' was saved in a different place, for example by Save in the state view of a different tab. It has no source.',
      why: 'An open page runs the newest version. You do not have to reload it. The page that ran v' + from + ' now runs v' + head + '.',
      more: () => table([['version', 'v' + from + ' → v' + head], ['saved', new Date(vv.head.at).toLocaleString()]]
        .concat(src ? [['git commit', src.git], ['branch', src.branch], ['message', src.message], ['request', src.request], ['session', src.session]] : [])) }
  ];
  if (src && Array.isArray(src.explain) && src.explain.length) parts.push({ name: 'How it worked before, how it works now',
    what: 'The session that made v' + head + ' wrote this for each part that changed.',
    why: 'You can see what is different without reading the code.',
    body: sideBySide(src.explain) });
  parts.push({ name: 'The files that changed',
    what: changed.length ? changed.length + (changed.length === 1 ? ' file' : ' files') + ' of main changed: ' + changed.map(c => c.path + ' (' + c.type + ')').join(', ') + '.' : 'No file changed.',
    why: 'The state keeps the files of main. Click a file below to see it in v' + from + ' and in v' + head + ', side by side.' });
  changed.forEach(c => parts.push({ name: c.path,
    what: 'This file was ' + c.type + '. Red lines are only in v' + from + '. Green lines are only in v' + head + '.',
    more: () => sideCode(c.path, from, head, fa[c.path], fb[c.path]) }));
  parts.push({ name: 'The parts of the state that changed',
    what: vv.changes.length + (vv.changes.length === 1 ? ' change' : ' changes') + ' from v' + from + ' to v' + head + '.',
    why: 'The State changes tab shows them in the state.',
    more: () => table([['path', 'change']].concat(vv.changes.map(c => [c.path.join('.'), c.type]))) });
  parts.push({ name: 'Run v' + head,
    what: 'The page runs v' + head + ': start() renders index-view again. Each view keeps its ui-data, so the views that were open stay open.',
    why: 'You see the new version at once, and the page stays as it was.' });
  return parts;
};
const partsOf = id => {
  const newer = tops.find(r => r.id === id && r.name === 'loadNewerVersion');
  if (newer) return newerParts(newer);
  if (id === 'runtime') return [
    { name: 'Run the runtime script', ms: os.started,
      what: 'The browser runs the runtime script of index.html' + (runtime ? ' (' + kb(runtime.textContent.length) + ')' : '') + '. These are the things it does, in order.',
      why: 'This script is the runtime: it loads the state and runs the functions in it. Everything after this comes from it.',
      more: () => group(label('What the runtime did on this page load'), run(), label('The runtime script'), code('The runtime script', src.trim(), 'js')) },
    { name: 'Note the start time', ms: os.started,
      what: 'The runtime writes down when it started: ' + Math.round(os.started) + ' ms after the page opened.',
      why: 'Only the timeline uses it. Every time on the timeline counts from the page opening, like the +' + (os.started / 1000).toFixed(2) + 's of this step.',
      more: () => group(label('Where it happens'), snippet(/startedAt=performance\.now/), label('The times the browser measured'), table(nav ? [['fetchStart', at(nav.fetchStart), 'The browser asks for index.html.'], ['responseStart', at(nav.responseStart), 'The first byte arrives.'], ['responseEnd', at(nav.responseEnd), 'index.html is downloaded.'],
        ['os.started', at(os.started), 'The runtime script starts.'], ['domInteractive', at(nav.domInteractive), 'The html is read.'], ['domContentLoaded', at(nav.domContentLoadedEventEnd), 'The scripts of the html have run.'], ['load', at(nav.loadEventEnd), 'Everything the html asked for is loaded.']]
        : [['os.started', at(os.started), 'The browser gives no timings for this page.']])) },
    { name: 'Make a session id',
      what: 'It makes a name for this page load: ' + session + '. Every load gets a new name.',
      why: 'The calls of this load are saved in the database under calls/' + session + ', so the calls of different loads, and of different people, do not mix.',
      more: () => group(label('Where it happens'), snippet(/var session=/), label('The first record saved under calls/' + session), code('calls/' + session + ': the first record', JSON.stringify(os.calls[0], null, 2), 'json')) },
    { name: 'Create the call tracker',
      what: 'It makes a recorder. From now on, every function that runs is written down: its name, its input, which function called it, how long it took and what it changed in the state. ' + os.calls.length + ' calls are recorded now.',
      why: 'The timeline you are looking at is drawn from these records. The newest 400 are also saved to the database 1.2 s after a call.',
      more: () => {
        const by = {};
        os.calls.forEach(r => { const b = by[r.name] = by[r.name] || [0, 0]; b[0]++; b[1] += r.ms || 0; });
        return group(label('Where it happens'), snippet(/var tracker=core\.createTracker/), label('What it recorded so far'), table([['call', 'times', 'ms in all']].concat(Object.keys(by).sort((a, b) => by[b][0] - by[a][0]).map(k => [k, by[k][0], by[k][1]]))));
      } },
    { name: 'Build os',
      what: "It makes os, the toolbox for the functions in the state: " + Object.keys(os).join(', ') + '.',
      why: "A function in the state cannot reach the page or the state by itself. It writes import os from 'os' and gets this toolbox: os.get reads the state, os.set changes it, os.call runs another function, os.bind wires buttons. Click one below to see what it is for, which functions use it and its code.",
      more: () => group(osList(), label('Where it happens'), snippet(/^var OS=\{/, true)) },
    { name: 'Load the state, then start',
      what: 'It runs three things, one after the other: loadState (the next step of the timeline), then start(), which renders index-view, then follow(), which listens for newer versions.',
      why: 'The page can be drawn only after the state is loaded, because everything on the page comes from the state.',
      more: () => group(label('Where it happens'), snippet(/^window\.agentOS=/), label('What happened on this page load'), run()) }
  ];
  if (id === (load && load.id)) {
    const rel = load.related || {};
    return [
      { name: 'Download state.json', ms: seed && seed.responseEnd,
        what: 'The runtime downloads state.json' + (seed && seed.decodedBodySize ? ' (' + kb(seed.decodedBodySize) + ')' : '') + ', the first version of the state.',
        why: 'It is used only when the database has no versions yet, so a new page starts with it. This page has ' + rel.commits + (rel.commits === 1 ? ' version' : ' versions') + ', so state.json is not used.',
        more: () => group(label('Where it happens'), snippet(/fetch\('state\.json'\)/), label('state.json'), () => getText('state.json').then(x => code('state.json', x, 'json'))) },
      { name: 'Connect to the database',
        what: rel.store === 'db'
          ? "claude.ai gives every artifact page an object, window.claude. claude.use('db') asks it for this page's own database: the page was published with the db capability, so it has one."
          : 'There is no window.claude here (claude.ai gives it only to artifact pages), so there is no database: the versions stay in memory and are lost on reload.',
        why: 'The versions and the call logs have to last after the page closes, and everyone who opens the page has to see the same ones. The database keeps two things: the versions (commits) and the call log of each page load (calls).',
        more: () => group(label('Where it happens'), snippet(/claude\.use\('db'\)/), label('How the runtime uses it'), table([
          ['window.claude', window.claude ? 'given by claude.ai' : 'missing'],
          ['store', rel.store],
          ['read the versions', "db.collection('commits').orderBy('n').get()"],
          ['save a version', "db.collection('commits').doc('c' + n).set(commit), now up to c" + String(rel.head).padStart(6, '0')],
          ['follow newer versions', "db.collection('commits').orderBy('n').onSnapshot(...)"],
          ['save the call log', "db.doc('calls/" + session + "').set({ session, started, count, items })"],
          ['can save', String(history.canWrite)]
        ])) },
      { name: 'Read the saved versions',
        what: 'It reads ' + rel.commits + (rel.commits === 1 ? ' version' : ' versions') + ' from the commits collection, in order.' + (rel.created ? ' None was saved, so state.json was saved as version 1.' : '') + (rel.writeError ? ' Saving failed: ' + rel.writeError + '.' : ''),
        why: 'Each Save of the state is one version. The newest is the state the page runs; the older ones are the history you step through in the state view.',
        more: () => group(label('Where it happens'), snippet(/list:function\(\)\{return apiCall\('read the versions'/), label('The versions'), table([['version', 'saved', 'added', 'updated', 'deleted']].concat(history.commits.slice().reverse().map(c => ['v' + c.n, new Date(c.at).toLocaleString(), (c.summary || {}).added, (c.summary || {}).updated, (c.summary || {}).deleted])))) },
      { name: 'Parse the newest version',
        what: 'v' + rel.head + ' is JSON text. It is read into the live state: an object in memory.',
        why: 'Functions read and change this object with os.get and os.set. It is saved as a new version only when you press Save in the state view.',
        more: () => { const st = os.get(); return group(label('Where it happens'), snippet(/live=core\.parseJsonc\(head\.state\)/), label('The parts of the state'), table([['part of the state', 'size']].concat(Object.keys(st).map(k => [k, kb(JSON.stringify(st[k]).length)])))); } }
    ];
  }
  return null;
};
const partRow = (p, n, key) => {
  const row = el('div', 'tl-call tl-part' + (p.more ? ' can-open' : ''));
  row.style.setProperty('--depth', 0);
  row.style.setProperty('--i', Math.min(n, 24));
  const head = el(p.more ? 'button' : 'div', 'tl-call-head');
  head.appendChild(el('span', 'tl-sub-n', String(n + 1)));
  head.appendChild(el('span', 'tl-name', p.name));
  if (typeof p.ms === 'number') head.appendChild(el('span', 'tl-ms', since(p.ms)));
  row.appendChild(head);
  const say = (lbl, text) => { const x = el('div', 'tl-say'); x.appendChild(el('b', '', lbl)); x.appendChild(document.createTextNode(text)); row.appendChild(x); };
  if (p.what) say('What happens ', p.what);
  if (p.why) say('Why ', p.why);
  if (p.text) row.appendChild(el('div', 'tl-part-text', p.text));
  if (p.body) row.appendChild(p.body);
  if (!p.more) return row;
  // A part opens on click and shows what is inside it; the page remembers which parts are open until it reloads.
  const body = el('div', 'tl-more');
  row.appendChild(body);
  const show = () => {
    const open = R.parts.has(key);
    row.classList.toggle('open', open);
    head.setAttribute('aria-expanded', String(open));
    body.textContent = '';
    if (!open) return;
    body.appendChild(el('div', 'tl-part-text', 'Loading…'));
    Promise.resolve().then(p.more).then(x => { body.textContent = ''; body.appendChild(x); }, e => { body.textContent = ''; body.appendChild(el('div', 'tl-error', String(e && e.message || e))); });
  };
  head.addEventListener('click', () => { if (R.parts.has(key)) R.parts.delete(key); else R.parts.add(key); show(); });
  show();
  return row;
};
// The details of a step: its parts, then its call with the calls inside it.
// The version this page loaded: its network and environment are the last values.
const loadedState = () => {
  const n = load && load.related && load.related.head, c = n && (os.history.commits || []).find(x => x.n === n);
  if (!c) return {};
  if (!R.loaded || R.loaded.n !== n) R.loaded = { n, state: core.parseJsonc(c.state) };
  return R.loaded.state;
};
const netEnvOf = st => ({ network: (st && st.network) || {}, environment: (st && st.environment) || {} });
function netEnvChanges() { return core.diff(netEnvOf(loadedState()), netEnvOf(os.get())); }
const ms = x => typeof x === 'number' ? x + ' ms' : '—';
const GROUPS = [['html', 'Html'], ['scripts', 'Our scripts'], ['claude.ai', 'claude.ai (scripts of the artifact page)'], ['api', 'API'], ['state', 'State'], ['file code', 'File code'], ['packages', 'Packages'], ['styles', 'Styles'], ['other', 'Other']];
const textKind = (g, k) => g === 'html' || /\.html$/.test(k) ? 'html' : /\.m?js$/.test(k) ? 'js' : /\.json$/.test(k) ? 'json' : /css/.test(k) ? 'text' : null;
const netPanel = () => {
  const box = el('section', 'tl-panel'), net = os.get('network') || {}, lastNet = loadedState().network || {};
  box.appendChild(el('h3', '', 'Network (all requests)'));
  box.appendChild(el('div', 'tl-used', 'Time: the value in the version this page loaded (v' + ((load && load.related && load.related.head) || '?') + '), now, and the difference. Expected: the state lists this request.'));
  const names = GROUPS.map(g => g[0]).concat(Object.keys(net).filter(g => !GROUPS.some(x => x[0] === g)));
  names.forEach(g => {
    const grp = net[g];
    if (!grp || typeof grp !== 'object' || !Object.keys(grp).length) return;
    box.appendChild(el('h4', '', ((GROUPS.find(x => x[0] === g) || [g, g])[1]) + ' · ' + Object.keys(grp).length));
    Object.keys(grp).forEach(k => {
      const x = grp[k] || {}, was = (lastNet[g] || {})[k] || {}, kind = g === 'api' ? null : textKind(g, k), key = 'net:' + g + ':' + k;
      const card = el('div', 'tl-req' + (kind && x.url ? ' can-open' : ''));
      const top = el('div', 'tl-req-top');
      top.appendChild(el('b', '', k));
      top.appendChild(el('span', 'tl-req-url', g === 'api' ? (x.what || '') : (x.url || '')));
      card.appendChild(top);
      const chips = el('div', 'tl-chips'), chip = (text, cls) => chips.appendChild(el('span', 'tl-chip' + (cls ? ' ' + cls : ''), text));
      if (!x.count) chip('not asked for on this page load', 'quiet');
      else {
        chip(x.size ? kb(x.size) : 'size not given', x.size ? '' : 'quiet');
        const d = typeof x.ms === 'number' && typeof was.ms === 'number' ? x.ms - was.ms : null;
        chip('time: last ' + ms(was.ms) + ' · now ' + ms(x.ms) + (d === null ? '' : ' · ' + (d > 0 ? '+' : d < 0 ? '−' : '±') + Math.abs(d) + ' ms'), d > 0 ? 'bad' : d < 0 ? 'good' : '');
        chip('at ' + since(x.start || 0));
        if (x.count > 1) chip(x.count + ' times');
        if (g !== 'api') chip(x.parallel && x.parallel.length ? 'in parallel with ' + x.parallel.join(', ') : 'alone', 'quiet');
      }
      chip(x.expected ? 'expected' : 'not expected', x.expected ? 'good' : 'bad');
      card.appendChild(chips);
      card.appendChild(el('div', 'tl-used', 'Used for: ' + (x.used_for || '— (write it in network.' + g + '.' + k + '.used_for)')));
      if (kind && x.url) {
        const body = el('div', 'tl-more'), show = () => {
          body.textContent = '';
          card.classList.toggle('open', R.parts.has(key));
          if (!R.parts.has(key)) return;
          body.appendChild(el('div', 'tl-part-text', 'Loading…'));
          textOf(g, x.url).then(t => { body.textContent = ''; body.appendChild(code(k, t, kind)); }, e => { body.textContent = ''; body.appendChild(cannotRead(x.url, e)); });
        };
        top.addEventListener('click', () => { if (R.parts.has(key)) R.parts.delete(key); else R.parts.add(key); show(); });
        card.appendChild(body);
        show();
      }
      box.appendChild(card);
    });
  });
  return box;
};
// The text of a request. A file of this page is asked for again by its path; index.html can also come from the page itself.
const sameOrigin = url => { try { return new URL(url, location.href).origin === location.origin; } catch (e) { return false; } };
const textOf = (g, url) => getText(url).catch(e => {
  if (!sameOrigin(url)) throw e;
  const path = new URL(url, location.href).pathname;
  return getText(path).catch(e2 => { if (g === 'html') return '<!DOCTYPE html>\n' + document.documentElement.outerHTML; throw e2; });
});
// Why the text is not shown: a file on another address can run here as a script, but the page may not download it as text.
const cannotRead = (url, e) => {
  const box = el('div', 'tl-error'), host = (() => { try { return new URL(url).host; } catch (x) { return url; } })();
  box.appendChild(el('div', '', sameOrigin(url)
    ? 'The page could not download this file as text (' + String(e && e.message || e) + ').'
    : 'The browser did not let this page download this file as text (' + String(e && e.message || e) + '). The file is on another address (' + host + '). claude.ai lets a page run scripts and styles from ' + host + ', but probably not download them as text.'));
  const a = el('a', '', 'Open the file in a new tab');
  a.href = url; a.target = '_blank'; a.rel = 'noopener';
  box.appendChild(a);
  return box;
};
const envPanel = () => {
  const box = el('section', 'tl-panel'), env = os.get('environment') || {}, lastEnv = loadedState().environment || {};
  box.appendChild(el('h3', '', 'Environment'));
  box.appendChild(el('div', 'tl-used', 'A yellow value is not the same as in the version this page loaded.'));
  const str = v => v === undefined ? '—' : typeof v === 'string' ? v : JSON.stringify(v);
  const rows = (o, was, p) => Object.keys(o || {}).forEach(k => {
    const v = o[k], w = was && typeof was === 'object' ? was[k] : undefined;
    if (v && typeof v === 'object' && !Array.isArray(v) && Object.keys(v).length) { rows(v, w, p ? p + ' / ' + k : k); return; }
    const row = el('div', 'tl-env-row' + (str(v) !== str(w) ? ' changed' : ''));
    row.appendChild(el('span', '', p ? p + ' / ' + k : k));
    const val = el('span', '', str(v));
    if (str(v) !== str(w)) val.appendChild(el('span', 'tl-was', 'was ' + str(w)));
    row.appendChild(val);
    box.appendChild(row);
  });
  Object.keys(env).forEach(g => {
    box.appendChild(el('h4', '', g));
    rows(env[g], lastEnv[g], '');
  });
  return box;
};
// Agent runs: each Claude Code run that changed the files of main keeps runs/<session>-<run>.json (made by the
// run-recorder subagent). The state has them in agents.<agent>.files.runs, as text.
const runsOf = st => {
  const out = [], agents = (st && st.agents) || {};
  Object.keys(agents).forEach(a => {
    const dir = agents[a] && agents[a].files && agents[a].files.runs;
    Object.keys(dir || {}).forEach(f => {
      if (!/\.json$/.test(f) || typeof dir[f] !== 'string') return;
      try { out.push(Object.assign({ file: 'runs/' + f }, JSON.parse(dir[f]))); } catch (e) {}
    });
  });
  return out.sort((x, y) => String(x.started) < String(y.started) ? -1 : 1);
};
const runStep = (run, ms) => ({ id: 'run:' + run.file, label: 'AI run notification', name: 'session ' + String(run.session).slice(0, 3) + ' · run ' + run.run,
  text: (run.title ? run.title + '. ' : '') + 'Asked by ' + ((run.started_by && run.started_by.run && run.started_by.run.who) || 'someone') + ': "' + ((run.started_by && run.started_by.run && run.started_by.run.words) || '').slice(0, 160) + '"',
  ms, fixed: true, run, when: new Date(run.ended || run.started).toLocaleString([], { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' }),
  // the state changes from the version before the run to the version it made; without them, the files it changed
  changes: (run.version && (versionsOf({ input: { head: run.version, from: run.version - 1 } }) || {}).changes || []).length || (run.files || []).filter(f => f.action && f.action !== 'read').length });
const tok = n => typeof n === 'number' ? (n >= 1000 ? (n / 1000).toFixed(1) + 'k' : String(n)) + ' tokens' : '';
// Who did a part of an agent run: the main agent, a subagent, an MCP call, a skill or a workflow. Each has its color.
const SOURCES = { main: { one: 'main agent', many: 'Main agent' }, subagent: { one: 'subagent', many: 'Subagents' }, mcp: { one: 'MCP', many: 'MCP' }, skill: { one: 'skill', many: 'Skills' }, workflow: { one: 'workflow', many: 'Workflows' } };
// An AI run notification (a run of the agent): three tabs. Index: the summary of the run and the actions for you.
// Details: what the run changed and read, as one tree, marked by who did it. Steps: the agent timeline in lanes, then
// the steps one by one. The tab and the chosen step are in os.refs.timeline-view (runView, runPick).
const runDetails = (run, box) => {
  const c = run.context || {}, steps = run.steps || [], laneOf = x => x.lane || 'main';
  const chip = (t, cls) => el('span', 'tl-chip' + (cls ? ' ' + cls : ''), t);
  if (!steps[R.runPick]) R.runPick = null;
  R.runView = ['index', 'details', 'steps'].includes(R.runView) ? R.runView : 'index';
  R.runBy = R.runBy || 'all';
  const byPath = {};
  (run.files || []).forEach(f => { byPath[f.path] = f; });
  // the text of a file before the run and after it, when the file is in the state (the files of the repo)
  const vv = run.version && versionsOf({ input: { head: run.version, from: run.version - 1 } });
  const textBefore = vv ? filesOf(vv.before) : {}, textAfter = vv ? filesOf(vv.after) : {};
  const GROUP = { mcp: 'MCP calls', skill: 'Skills', subagent: 'Subagents', workflow: 'Workflows', run: 'Commands and scripts', test: 'Commands and scripts', search: 'Searches', publish: 'Publishes' };
  // An MCP call that sends or writes something is a change; one that gets data is a read.
  const WRITES = /\b(post|send|set|write|update|create|delete|publish|edit|rename|resolve|react|commit|push|save|merge)/i;
  const entriesOf = list => {
    const out = {};
    list.forEach(i => {
      const x = steps[i], lane = laneOf(x) === 'main' ? null : laneOf(x), by = lane ? 'subagent' : 'main';
      (x.files || []).forEach(f => {
        const key = 'file:' + f.path, info = byPath[f.path] || {};
        const e = out[key] = out[key] || { key, type: 'file', path: f.path, tree: ['Files'].concat(String(f.path).split('/')), action: f.action, steps: [], src: new Set(), lanes: new Set(), tokens: info.tokens, cached: info.cached, why: f.why || info.why };
        // (read, then changed: it is changed; created, then updated in a later step: it is created; deleted at the end: it is deleted)
        if (f.action !== 'read') e.action = e.action === 'created' && f.action !== 'deleted' ? 'created' : f.action;
        if (!e.steps.includes(i)) e.steps.push(i);
        e.src.add(by);
        if (lane) e.lanes.add(lane);
      });
      (x.items || []).forEach((it, k) => {
        if (!it || typeof it !== 'object' || !GROUP[it.kind]) return;
        const changes = it.kind === 'publish' || (it.kind === 'mcp' && WRITES.test(it.text)), key = 'item:' + i + ':' + k;
        out[key] = { key, type: 'item', kind: it.kind, text: it.text, action: changes ? 'changed' : 'read', tree: [GROUP[it.kind], it.text], steps: [i], src: new Set([by].concat(SOURCES[it.kind] && it.kind !== 'main' ? [it.kind] : [])), lanes: new Set(lane ? [lane] : []) };
      });
    });
    return Object.values(out);
  };
  const srcChips = e => {
    const c2 = el('span', 'ar-srcs');
    e.lanes.forEach(l => c2.appendChild(chip(l, 'src src-subagent')));
    ['mcp', 'skill', 'workflow'].forEach(k => { if (e.src.has(k)) c2.appendChild(chip(SOURCES[k].one, 'src src-' + k)); });
    if (e.type === 'item' && e.kind === 'subagent' && !e.lanes.size) c2.appendChild(chip('subagent', 'src src-subagent'));
    return c2;
  };
  const all = entriesOf(steps.map((_, i) => i)), changed = all.filter(e => e.action !== 'read'), read = all.filter(e => e.action === 'read');
  const views = el('div', 'ar-tabs ar-views'), body = el('div', 'ar-view');
  views.setAttribute('role', 'tablist');
  [['index', 'Index'], ['details', 'Details'], ['steps', 'Steps']].forEach(([t, label]) => {
    const b = el('button', '', label);
    b.dataset.view = t;
    b.setAttribute('role', 'tab');
    b.addEventListener('click', () => { R.runView = t; show(); });
    views.appendChild(b);
  });
  box.appendChild(views);
  box.appendChild(body);

  // Index: the summary of the run and what you need to do, then where it came from, what it used and its context.
  const drawIndex = () => {
    const card = el('section', 'ar-index');
    card.appendChild(el('h3', '', run.title || 'Agent run'));
    const words = (run.started_by && run.started_by.run && run.started_by.run.words) || '';
    card.appendChild(el('p', 'ar-summary', run.summary || ((words ? 'Asked: "' + words.slice(0, 240) + (words.length > 240 ? '…' : '') + '". ' : '') +
      steps.length + ' steps, ' + changed.filter(e => e.type === 'file').length + ' files changed, ' + read.filter(e => e.type === 'file').length + ' files read' + (run.version ? ', made v' + run.version : '') + '.')));
    const acts = el('div', 'ar-actions' + (run.actions && run.actions.length ? ' need' : ''));
    acts.appendChild(el('b', '', run.actions && run.actions.length ? 'Actions for you' : 'No action needed'));
    if (!run.actions) acts.appendChild(el('span', 'tl-used', ' (this run did not record its actions)'));
    if (run.actions && run.actions.length) {
      const ol = el('ol');
      run.actions.forEach(x => ol.appendChild(el('li', '', typeof x === 'string' ? x : x.text)));
      acts.appendChild(ol);
    }
    card.appendChild(acts);
    const head = el('div', 'ar-head');
    [run.agent || 'Agent', 'session ' + String(run.session).slice(0, 8), 'run ' + run.run + (run.runs_in_session ? ' of ' + run.runs_in_session : ''),
     new Date(run.started).toLocaleString() + ' → ' + new Date(run.ended).toLocaleTimeString(), run.version ? 'made v' + run.version : 'no version',
     'context ' + tok(c.at_start) + ' → ' + tok(c.at_end), 'cached ' + tok(c.cached_at_end), c.compacted ? 'compacted in this run' : 'not compacted']
      .forEach(t => head.appendChild(chip(t)));
    card.appendChild(head);
    body.appendChild(card);
    // What started each part, and why.
    const dl = el('dl', 'ar-why'), sb = run.started_by || {};
    const row = (t, x) => {
      dl.appendChild(el('dt', '', t));
      const dd = el('dd');
      if (!x || (Array.isArray(x) && !x.length)) dd.textContent = 'Nothing.';
      else [].concat(x).forEach(y => dd.appendChild(el('div', '', typeof y === 'string' ? y : [y.name, y.who, y.words ? '"' + y.words + '"' : '', y.why].filter(Boolean).join(' · '))));
      dl.appendChild(dd);
    };
    row('What started this session', sb.session);
    row('What started this run', sb.run);
    row('What started this workflow', sb.workflow);
    row('What started the subagents', sb.subagents);
    row('What started the skills', sb.skills);
    // uses: {mcp, skills, subagents, workflows}, each a list of {name, count, why} (or counts by name: the raw data);
    // a flat list has a kind on each use
    const u = {};
    if (Array.isArray(run.uses)) run.uses.forEach(x => { const k = { mcp: 'mcp', skill: 'skills', subagent: 'subagents', workflow: 'workflows' }[x.kind] || x.kind; (u[k] = u[k] || []).push(x); });
    else Object.assign(u, run.uses);
    [['mcp', 'MCP use'], ['skills', 'Skill use'], ['subagents', 'Subagents'], ['workflows', 'Workflow']].forEach(([k, t]) => {
      const list = Array.isArray(u[k]) ? u[k] : Object.keys(u[k] || {}).map(n => ({ name: n, count: u[k][n] }));
      row(t, list.map(x => x.name + (x.count ? ' × ' + x.count : '') + (x.why ? ' · ' + x.why : '')));
    });
    row('Context', ['At the start ' + tok(c.at_start) + ', at the end ' + tok(c.at_end) + ', the most ' + tok(c.peak) + '.',
      tok(c.cached_at_end) + ' of the context at the end was cached (read from the cache, not sent again).', tok(c.output_tokens) + ' written by the agent in ' + (c.requests || 0) + ' requests.']);
    body.appendChild(dl);
  };

  // Details: the state as the run touched it. Files it changed (green added, yellow updated, red deleted) and what it
  // read (blue: files, commands and scripts, searches, the data of MCP calls, skills), with who did it. A chosen step
  // (Steps) shows only its part.
  const drawDetails = () => {
    const x = steps[R.runPick], list = x ? entriesOf([R.runPick]) : all;
    const sub = el('div', 'tl-detail-sub ar-scope', x ? 'Step ' + (R.runPick + 1) + ': ' + x.title : 'The whole run');
    if (x) {
      const wb = el('button', 'btn ar-whole', 'Whole run');
      wb.addEventListener('click', () => { R.runPick = null; show(); });
      sub.appendChild(wb);
    }
    body.appendChild(sub);
    const legend = el('div', 'ar-legend');
    [['added', 'added'], ['updated', 'updated'], ['deleted', 'deleted'], ['read', 'read']].forEach(([cls, t]) => legend.appendChild(el('span', 'ar-key ' + cls, t + ' ' + list.filter(e => (e.action === 'created' ? 'added' : e.action === 'changed' ? 'updated' : e.action) === cls).length)));
    body.appendChild(legend);
    // By who: the main agent, the subagents, or the MCP calls, skills and workflows. Each has its color.
    const count = k => k === 'all' ? list.length : list.filter(e => e.src.has(k)).length;
    if (R.runBy !== 'all' && !count(R.runBy)) R.runBy = 'all';
    const bys = el('div', 'st-kinds ar-by');
    bys.setAttribute('aria-label', 'By');
    ['all'].concat(Object.keys(SOURCES)).forEach(k => {
      if (k !== 'all' && !count(k)) return;
      const b = el('button', 'st-kind' + (k === 'all' ? '' : ' src-' + k), (k === 'all' ? 'All' : SOURCES[k].many) + ' ' + count(k));
      b.dataset.by = k;
      b.setAttribute('aria-pressed', String(R.runBy === k));
      b.addEventListener('click', () => { R.runBy = k; show(); });
      bys.appendChild(b);
    });
    body.appendChild(bys);
    const shown = list.filter(e => R.runBy === 'all' || e.src.has(R.runBy));
    if (!shown.length) { body.appendChild(el('p', 'tl-text', 'Nothing here.')); return; }
    let sel = shown.find(e => e.key === R.runSel) || shown.find(e => e.type === 'file' && e.action !== 'read' && textAfter[e.path] !== undefined) || shown[0];
    const grid = el('div', 'kv ar-kv'), tree = el('div', 'kv-tree'), main = el('div', 'kv-main');
    const root = {};
    shown.forEach(e => {
      let node = root;
      e.tree.slice(0, -1).forEach(d => { node = node[d + '/'] = node[d + '/'] || {}; });
      node[e.tree[e.tree.length - 1]] = e;
    });
    const buttons = [], CH = { created: 'added', updated: 'updated', deleted: 'deleted', changed: 'updated', read: 'read' };
    const draw = (node, into, depth) => Object.keys(node).sort((a, b) => (b.endsWith('/') - a.endsWith('/')) || (a < b ? -1 : 1)).forEach(k => {
      const e = node[k];
      if (!e.key) {
        const d = el('details');
        d.open = true;
        d.appendChild(el('summary', '', k)).style.paddingLeft = depth * 14 + 4 + 'px';
        draw(e, d, depth + 1);
        into.appendChild(d);
        return;
      }
      const b = el('button', 'kv-item ar-item ' + CH[e.action] + (e === sel ? ' on' : ''));
      b.style.paddingLeft = depth * 14 + 4 + 'px';
      b.title = (e.path || e.text) + ' (' + e.action + ')';
      b.appendChild(el('span', 'ar-item-name', k));
      b.appendChild(srcChips(e));
      b.addEventListener('click', () => { sel = e; R.runSel = e.key; buttons.forEach(y => y.classList.toggle('on', y === b)); drawMain(); });
      buttons.push(b);
      into.appendChild(b);
    });
    draw(root, tree, 0);
    grid.appendChild(tree);
    grid.appendChild(main);
    body.appendChild(grid);
    const drawMain = () => {
      main.textContent = '';
      const e = sel, before = e.type === 'file' ? textBefore[e.path] : undefined, after = e.type === 'file' ? textAfter[e.path] : undefined;
      const has = e.type === 'file' && (after !== undefined || before !== undefined);
      const tabs = (has ? ['File'] : []).concat(has && e.action !== 'read' && before !== after ? ['Changes'] : [], ['Why']);
      let tab = R.runSelTab;
      if (!tabs.includes(tab)) tab = tabs[0];
      const head = el('div', 'kv-head');
      head.appendChild(el('span', '', e.path || e.text));
      head.appendChild(chip(e.action, e.action === 'created' ? 'good' : e.action === 'deleted' ? 'bad' : e.action === 'read' ? 'read' : ''));
      if (e.kind && !SOURCES[e.kind]) head.appendChild(chip(e.kind, 'quiet'));
      head.appendChild(srcChips(e));
      main.appendChild(head);
      const bar = el('div', 'kv-tabs');
      bar.setAttribute('role', 'tablist');
      tabs.forEach(t => {
        const b = el('button', '', t);
        b.setAttribute('role', 'tab');
        b.setAttribute('aria-selected', String(t === tab));
        b.addEventListener('click', () => { R.runSelTab = t; drawMain(); });
        bar.appendChild(b);
      });
      main.appendChild(bar);
      if (tab === 'File') {
        if (after === undefined) main.appendChild(el('p', 'tl-text', 'The run deleted it. This is how it was.'));
        main.appendChild(fileView(e.path, after !== undefined ? after : before));
        return;
      }
      if (tab === 'Changes') { main.appendChild(sideCode(e.path, vv.from.n, vv.head.n, before, after)); return; }
      // Why: who did it, in which steps, and why
      const dl = el('dl', 'ar-why ar-info');
      const row = (t, v) => { if (!v) return; dl.appendChild(el('dt', '', t)); dl.appendChild(el('dd', '', v)); };
      row('What', e.type === 'file' ? 'The ' + (e.action === 'read' ? 'agent read this file' : 'agent ' + e.action + ' this file') + '.' : e.text);
      row('By', [e.src.has('main') ? 'the main agent' : '', ...Array.from(e.lanes).map(l => 'the subagent ' + l), ...['mcp', 'skill', 'workflow'].filter(k => e.src.has(k)).map(k => (k === 'mcp' ? 'an ' : 'a ') + SOURCES[k].one + ' call')].filter(Boolean).join(', '));
      row('Steps', e.steps.map(i => 'Step ' + (i + 1) + ': ' + steps[i].title).join(' · '));
      row('Why', e.why || e.steps.map(i => steps[i].why).filter(Boolean).join(' '));
      row('Size', e.tokens ? '≈ ' + tok(e.tokens) + (e.cached ? ', in the cached context at the end' : '') : '');
      main.appendChild(dl);
      if (e.type === 'file' && !has) main.appendChild(el('p', 'tl-used', 'This file is not in the state (it is not a file of the repo), so its text is not here.'));
    };
    drawMain();
    setTimeout(() => { const on = tree.querySelector('.kv-item.on'); if (on) tree.scrollTop = on.offsetTop - tree.offsetTop - 60; });
  };

  // Steps: the agent timeline (the start, then each step in its lane: main, or a subagent), then the steps one by one.
  // A click on a step opens it (what it did, why, its files) and chooses it for Details; a click again closes it.
  const drawSteps = () => {
    const lanesBox = el('div', 'ar-lanes');
    const lanes = Array.from(new Set(['main'].concat(steps.map(laneOf))));
    const subs = [].concat((run.started_by || {}).subagents || []).filter(Boolean);
    const pickStep = i => { R.runPick = R.runPick === i ? null : i; show(); };
    lanes.forEach((name, li) => {
      // The main agent is the first lane. A subagent (a helper agent that the main agent started) has its own lane.
      const lane = el('div', 'ar-lane' + (li ? ' sub' : '')), mine = steps.map((x, i) => laneOf(x) === name ? i : -1).filter(i => i >= 0);
      const ln = el('div', 'ar-lane-name');
      ln.appendChild(el('span', '', li ? 'Subagent' : 'Main agent'));
      if (li) ln.appendChild(el('b', '', name));
      lane.appendChild(ln);
      if (li === 0) {
        const st = el('div', 'ar-card start');
        st.appendChild(el('b', '', (run.agent || 'Agent') + ' start'));
        st.appendChild(el('div', '', 'Session ' + String(run.session).slice(0, 8) + ' · Run ' + run.run));
        lane.appendChild(st);
      } else {
        // A step sits in the column of its order. Before the first step of a subagent, a line tells what the subagent is.
        const sb = subs.find(x => String(x.name || '').includes(name)), line = el('div', 'ar-branch');
        line.style.width = 170 + mine[0] * 240 + 'px';
        line.appendChild(el('span', '', name + ' is a subagent: a helper agent with its own context, which the main agent started.' + (sb && sb.why ? ' ' + sb.why : '') +
          ' Its steps: ' + mine.map(i => 'Step ' + (i + 1)).join(', ') + ' →'));
        lane.appendChild(line);
      }
      steps.forEach((x, i) => {
        // (no empty columns before the first step of a subagent, or after the last step of a lane)
        if ((li && i < mine[0]) || i > mine[mine.length - 1]) return;
        if (laneOf(x) !== name) { lane.appendChild(el('div', 'ar-gap')).style.width = '230px'; return; }
        const card = el('div', 'ar-card step' + (li ? ' sub' : '') + (R.runPick === i ? ' on' : ''));
        card.dataset.step = i;
        card.tabIndex = 0;
        card.addEventListener('click', () => pickStep(i));
        card.appendChild(el('b', '', 'Step ' + (i + 1) + ': ' + x.title));
        // (a subagent step is short in its lane, so the lane stays low)
        const ul = el('ul');
        (x.items || []).forEach(it => {
          const li2 = el('li', '', typeof it === 'string' ? it : it.text);
          if (it && SOURCES[it.kind]) li2.className = 'src-' + it.kind;
          ul.appendChild(li2);
        });
        if (!li) card.appendChild(ul);
        else card.appendChild(el('div', 'tl-used', (x.items || []).length + ' actions · click to see them'));
        const meta = [x.from && x.to ? Math.round((Date.parse(x.to) - Date.parse(x.from)) / 1000) + ' s' : '', x.context_tokens ? 'context ' + tok(x.context_tokens) : ''].filter(Boolean).join(' · ');
        if (meta) card.appendChild(el('div', 'tl-used', meta));
        lane.appendChild(card);
      });
      lanesBox.appendChild(lane);
    });
    body.appendChild(lanesBox);
    // the steps one by one: a number on a line, the title, who did it, the time and the context; the open step shows
    // what it did, why, and the files it changed and read
    const flow = el('ol', 'ar-flow');
    steps.forEach((x, i) => {
      const on = R.runPick === i, li = el('li', 'ar-flow-step' + (laneOf(x) === 'main' ? '' : ' sub') + (on ? ' on' : ''));
      li.dataset.step = i;
      const top = el('button', 'ar-flow-head');
      top.appendChild(el('span', 'ar-flow-num', String(i + 1)));
      top.appendChild(el('b', '', x.title));
      top.appendChild(chip(laneOf(x) === 'main' ? 'main agent' : x.lane, laneOf(x) === 'main' ? 'src src-main' : 'src src-subagent'));
      const kinds = new Set((x.items || []).map(it => it && it.kind).filter(k => SOURCES[k]));
      kinds.forEach(k => top.appendChild(chip(SOURCES[k].one, 'src src-' + k)));
      top.appendChild(el('span', 'ar-flow-meta', [x.from ? new Date(x.from).toLocaleTimeString() : '', x.from && x.to ? Math.round((Date.parse(x.to) - Date.parse(x.from)) / 1000) + ' s' : '', x.context_tokens ? 'context ' + tok(x.context_tokens) : ''].filter(Boolean).join(' · ')));
      top.addEventListener('click', () => pickStep(i));
      li.appendChild(top);
      if (x.why) li.appendChild(el('p', 'ar-flow-why', x.why));
      if (on) {
        const ul = el('ul', 'ar-items');
        (x.items || []).forEach(it => {
          const r = el('li');
          if (it.kind) r.appendChild(chip(it.kind, SOURCES[it.kind] ? 'src src-' + it.kind : 'quiet'));
          r.appendChild(document.createTextNode(' ' + (typeof it === 'string' ? it : it.text)));
          ul.appendChild(r);
        });
        li.appendChild(ul);
        const files = el('div', 'ar-flow-files');
        entriesOf([i]).filter(e => e.type === 'file').forEach(e => files.appendChild(chip((e.action === 'read' ? 'read ' : e.action + ' ') + e.path, 'ar-file ' + CH2[e.action])));
        if (files.children.length) li.appendChild(files);
        const go = el('button', 'btn ar-to-details', 'See it in Details');
        go.addEventListener('click', () => { R.runView = 'details'; show(); });
        li.appendChild(go);
      }
      flow.appendChild(li);
    });
    body.appendChild(flow);
  };
  const CH2 = { created: 'added', updated: 'updated', deleted: 'deleted', read: 'read' };
  const show = () => {
    body.textContent = '';
    views.querySelectorAll('button').forEach(b => b.setAttribute('aria-selected', String(b.dataset.view === R.runView)));
    if (R.runView === 'index') drawIndex();
    else if (R.runView === 'details') drawDetails();
    else drawSteps();
  };
  show();
};
const details = (s, box) => {
  if (s.run) { runDetails(s.run, box); return; }
  if (s.id === 'open') {
    const grid = el('div', 'tl-netenv');
    grid.appendChild(netPanel());
    grid.appendChild(envPanel());
    box.appendChild(grid);
    return;
  }
  const parts = partsOf(s.id) || [];
  parts.forEach((p, n) => box.appendChild(partRow(p, n, s.id + ':' + n)));
  if (s.rec) inside(s.rec, box, parts.length);
};

// The steps: the browser opens the page, index.html runs, then each call that nothing else called.
const lastRun = runsOf(loadedState()).pop();
const steps = (lastRun ? [runStep(lastRun, 0)] : []).concat([
  { id: 'open', label: 'Network', name: 'network', text: 'Every request of this page load, and the environment of the page. The runtime keeps both in the state (network, environment), so each block shows what changed in them.', ms: 0, fixed: true, changes: netEnvChanges().length },
  { id: 'runtime', label: 'Run index.html', name: 'runtime', text: 'The runtime script of index.html sets up what the functions need.', ms: os.started, fixed: true }
]).concat(...tops.sort(byId).slice(-150).map(r => {
  const [label, text] = what(r);
  const vv = r.name === 'loadNewerVersion' && versionsOf(r), ms = Date.parse(r.at) - t0;
  const block = { id: r.id, label, name: r.name, text, ms, took: r.ms, ok: r.ok, changes: vv ? vv.changes.length : countAll(r), rec: r };
  // A new version that came with new agent runs: an Agent run block after it, for each run.
  if (!vv) return [block];
  const had = new Set(runsOf(vv.before).map(x => x.file));
  return [block].concat(runsOf(vv.after).filter(x => !had.has(x.file)).map(x => runStep(x, ms)));
}));
// AI runs or UI: only the AI run blocks, or only the other blocks (ui-data.show; all shows both).
// (when no block is of that kind, all show)
const only = steps.filter(s => !!s.run === (d.show === 'runs'));
if ((d.show === 'runs' || d.show === 'ui') && only.length) steps.splice(0, steps.length, ...only);
R.steps = steps.map(s => s.id);
R.names = steps.map(s => s.name);

// No block chosen: the last agent run (the first block, or the newest one that came with a new version), or the
// newest block when the state has no run.
const runAt = steps.map(s => !!s.run).lastIndexOf(true);
let pos = steps.findIndex(s => s.id === d.selected);
if (pos < 0) pos = runAt >= 0 ? runAt : steps.length - 1;
const cur = steps[pos], strip = ctx.root.querySelector('#tl-strip'), left = strip.scrollLeft;
// How many state changes each block made: a block with none opens on its Details. An agent run opens on its
// Details too: the timeline of the agent.
R.changes = {};
steps.forEach(s => { R.changes[s.id] = s.run ? 0 : s.changes || 0; });
const flowAt = R.flow ? R.flow.ids.indexOf(cur.id) : -1;
ctx.root.querySelector('#tl-pos').textContent = (flowAt >= 0 ? R.flow.name + ': block ' + (flowAt + 1) + ' of ' + R.flow.ids.length : 'Block ' + (pos + 1) + ' of ' + steps.length) + '  ' + (cur.when || since(cur.ms));
ctx.root.querySelector('#tl-prev').disabled = pos === 0;
ctx.root.querySelector('#tl-next').disabled = pos === steps.length - 1;
strip.textContent = '';
// The newest agent run stays in sight at the left and the newest block at the right when the row scrolls.
steps.forEach((s, i) => {
  const on = i === pos, pin = i === runAt ? ' pin-left' : i === steps.length - 1 && i > 0 ? ' pin-right' : '';
  const b = el('button', 'tl-step' + (s.run ? ' ai' : ' ui') + (s.fixed ? ' fixed' : '') + (s.ok === false ? ' bad' : '') + (on ? ' on' : '') + (i < pos ? ' past' : '') + pin);
  b.dataset.call = 'local.select';
  b.dataset.input = JSON.stringify({ id: s.id });
  b.setAttribute('aria-current', String(on));
  const top = el('span', 'tl-step-top');
  top.appendChild(el('span', 'tl-step-n', String(i + 1)));
  top.appendChild(el('span', 'tl-time', s.run ? core.ago(s.run.ended || s.run.started) : s.when || since(s.ms)));
  b.appendChild(top);
  // the two pinned blocks: Last agent run, and the newest block (Last click, ...)
  b.appendChild(el('span', 'tl-kind', pin ? 'Last ' + (s.run ? s.label : s.label.toLowerCase()) : s.label));
  b.appendChild(el('span', 'tl-step-name', s.name));
  const meta = el('span', 'tl-step-meta');
  if (s.took !== undefined) meta.appendChild(el('span', '', s.took + ' ms'));
  if (s.changes) meta.appendChild(el('span', 'tl-count', s.changes + (s.changes === 1 ? ' change' : ' changes')));
  b.appendChild(meta);
  strip.appendChild(b);
});
os.bind(strip, v);
strip.scrollLeft = left;
const onEl = strip.children[pos];
if (onEl && (onEl.offsetLeft < strip.scrollLeft || onEl.offsetLeft + onEl.offsetWidth > strip.scrollLeft + strip.clientWidth))
  strip.scrollTo({ left: onEl.offsetLeft - strip.clientWidth / 2 + onEl.offsetWidth / 2, behavior: R.shown === undefined ? 'auto' : 'smooth' });

// The state view shows the chosen block. It uses these.
R.current = cur;
R.since = since;
R.number = pos + 1;
// The version of a block: the version an agent run made, the version a new version or Load the state brought; the
// newest version for the other blocks.
R.versionOf = s => s.run ? s.run.version : s.rec && s.rec.name === 'loadNewerVersion' ? s.rec.input.head
  : s.rec && s.rec.name === 'loadState' ? s.rec.related.head : (((os.history && os.history.commits) || []).slice(-1)[0] || {}).n;
// Details: the parts of the block, then its call with the calls inside it.
R.drawDetails = box => details(cur, box);
// Two states as the changes view needs them: before, after, and the rows of the table (path, change).
R.pairFrom = (before, after, from, head) => {
  const changes = core.diff(before, after), L = x => typeof x === 'number' ? 'v' + x : x;
  return { before, after, full: after, fullBefore: before, from, head, count: changes.length, what: 'this version',
    intro: ' in the state from ' + L(from) + ' to ' + L(head) + '.', label: 'The state, only what changed from ' + L(from) + ' to ' + L(head),
    sub: 'What changed', cols: ['path', 'change'], rows: changes.map(c => ({ keys: c.path, type: c.type, row: [c.path.join('.'), c.type] })) };
};
// Changes of the state view: kind 'all' shows the state cut down to the changes, with a table; one kind (files,
// views, functions, network, environment) shows in its own view (kindView), a tree on the left.
R.drawPair = (box, kind, p) => {
  if (kind !== 'all') { kindView(box, kind, p); return; }
  box.appendChild(el('p', 'tl-text', p.count + (p.count === 1 ? ' change' : ' changes') + p.intro + ' A long text shows as "...": the pointer on it shows its start (an updated text: its changes), a click opens it.'));
  const legend = el('div', 'st-legend');
  ['added', 'updated', 'deleted'].forEach(k => legend.appendChild(el('span', k, k)));
  box.appendChild(legend);
  box.appendChild(stateBox(p.label, core.changesView(p.before, p.after)));
  box.appendChild(el('div', 'tl-detail-sub', p.sub));
  box.appendChild(table([p.cols].concat(p.rows.filter(r => passes(r.keys)).map(r => r.row))));
};
// One kind of the state as it is (no changes): its tree, from the state on screen.
R.kindView = (box, kind, p) => kindView(box, kind, p);
// The changes of the chosen block.
R.drawChanges = (box, kind) => {
  // Each block gives: the state before and after it (only what changed), the whole state after it (and before it,
  // when the page has it), and the rows of the table.
  let p = null;
  if (cur.run || (cur.rec && cur.rec.name === 'loadNewerVersion')) {
    const to = cur.run && cur.run.version, vv = cur.run ? to && versionsOf({ input: { head: to, from: to - 1 } }) : versionsOf(cur.rec);
    if (!vv) {
      box.appendChild(el('p', 'tl-text', !cur.run ? 'The two versions are not in the history of this page.'
        : to ? 'The run made v' + to + '. v' + (to - 1) + ' and v' + to + ' are not both in the history of this page.' : 'The run made no version.'));
      return;
    }
    p = { before: vv.before, after: vv.after, full: vv.after, fullBefore: vv.before, from: vv.from.n, head: vv.head.n, count: vv.changes.length, what: cur.run ? 'this run' : 'this version',
      intro: ' in the state from v' + vv.from.n + ' to v' + vv.head.n + (cur.run ? ', the version this run made.' : '.'),
      label: cur.run ? 'The state, only what the run changed' : 'The state, only what changed from v' + vv.from.n + ' to v' + vv.head.n,
      sub: 'What changed', cols: ['path', 'change'], rows: vv.changes.map(c => ({ keys: c.path, type: c.type, row: [c.path.join('.'), c.type] })), run: cur.run };
  } else {
    const list = [];
    if (cur.id === 'open') {
      // Network and environment, from the version this page loaded to now. By: the last call that changed the path.
      netEnvChanges().forEach(c => {
        const path = c.path.join('.'), by = recs.slice().reverse().find(r => changesOf(r).some(x => x.path === path || path.indexOf(x.path + '.') === 0));
        list.push({ type: c.type, path, before: core.brief(c.before), after: core.brief(c.after), by: by ? by.name : 'the runtime' });
      });
    }
    const walk = r => { changesOf(r).forEach(c => list.push(Object.assign({ by: r.name }, c))); (kids[r.id] || []).sort(byId).forEach(walk); };
    if (cur.rec) walk(cur.rec);
    if (!list.length) {
      const why = cur.id === 'open' ? 'Network and environment are the same as in the version this page loaded.'
        : cur.id === 'runtime' ? 'There is no state yet: the state is loaded in block 3, Load the state.'
        : cur.rec && cur.rec.name === 'loadState' ? 'This block loaded the state: v' + cur.rec.related.head + '. Before it, there was no state.'
        : 'This block changed nothing in the state.';
      box.appendChild(el('p', 'tl-text', why));
      return;
    }
    // A path is dotted and keys can hold dots ("local.init"): the keys are found in the live state.
    const keysOf = path => {
      const parts = path.split('.'), out = [];
      let x = os.get(), i = 0;
      while (i < parts.length) {
        let k = parts[i], j = i;
        while (x && typeof x === 'object' && !(k in x) && j < parts.length - 1) { j++; k += '.' + parts[j]; }
        if (!(x && typeof x === 'object' && k in x)) return out.concat(parts.slice(i));
        out.push(k); x = x[k]; i = j + 1;
      }
      return out;
    };
    const put = (o, keys, val) => { keys.slice(0, -1).forEach(k => { if (!o[k] || typeof o[k] !== 'object') o[k] = {}; o = o[k]; }); o[keys[keys.length - 1]] = val; };
    const drop = (o, keys) => { keys.slice(0, -1).forEach(k => { o = o && o[k]; }); if (o) delete o[keys[keys.length - 1]]; };
    const before = {}, after = {}, seen = {};
    list.forEach(c => {
      const keys = keysOf(c.path), key = keys.join('\u0000');
      if (!seen[key]) { seen[key] = true; if (c.type !== 'added') put(before, keys, c.before); }
      if (c.type === 'deleted') drop(after, keys); else put(after, keys, c.after);
    });
    p = { before, after, full: os.get(), fullBefore: null, from: 'before', head: 'after', count: list.length,
      intro: ' in the state, made by ' + Array.from(new Set(list.map(c => c.by))).join(', ') + '. Long values are shortened.',
      label: 'The state, only what this block changed', sub: 'Which function changed what', cols: ['path', 'change', 'by'],
      rows: list.map(c => ({ keys: keysOf(c.path), type: c.type, row: [c.path, c.type === 'added' ? short(c.after) : c.type === 'deleted' ? short(c.before) : short(c.before) + '  →  ' + short(c.after), c.by] })) };
  }
  R.drawPair(box, kind, p);
};
// One kind of the state in its own view. On the left, a tree of all its items (in the state after the block); a
// changed item has the color of its change. On the right, the chosen item in tabs: first its content (File, View,
// Function, Request or Value), then Changes when the block changed it. The filter text keeps only the items whose
// path has it. The chosen item and tab are kept in os.refs['timeline-view'].pick.
// The file viewer: each kind of file in its own view. md reads as a page (the look of the md viewer of the state
// view, with its theme) with its contents on the left; json is a tree that opens and closes; code has its outline
// (functions, classes, ids, selectors) on the left and the code on the right, with find, wrap and copy. md and json
// can show their source too. The mode of each kind of file is kept in os.refs['timeline-view'].fileMode.
const FILE_KINDS = {
  js: ['JavaScript', 'js'], mjs: ['JavaScript', 'js'], cjs: ['JavaScript', 'js'], ts: ['TypeScript', 'js'], html: ['HTML', 'html'], htm: ['HTML', 'html'],
  css: ['CSS', 'css'], json: ['JSON', 'json'], jsonc: ['JSON', 'json'], jsonl: ['JSON lines', 'json'], md: ['Markdown', 'md'], py: ['Python', 'code'],
  sh: ['Shell', 'code'], yaml: ['YAML', 'code'], yml: ['YAML', 'code'], txt: ['Text', 'code']
};
const fileKind = name => {
  const ext = (/\.([\w]+)$/.exec(name) || [])[1] || '';
  const [lang, kind] = FILE_KINDS[ext.toLowerCase()] || ['Text', 'code'];
  return { ext: ext || 'txt', lang, kind };
};
// The parts of a code file, with their lines: what the outline lists.
const outlineOf = (text, kind, ext) => {
  const out = [];
  text.split('\n').forEach((l, i) => {
    let m;
    const depth = Math.min(4, Math.floor((/^\s*/.exec(l)[0].length) / 2));
    if (kind === 'md') { if ((m = /^(#{1,4})\s+(.+)/.exec(l))) out.push({ line: i, depth: m[1].length - 1, name: m[2], type: 'h' }); return; }
    if (ext === 'py') { if ((m = /^\s*(def|class)\s+(\w+)/.exec(l))) out.push({ line: i, depth, name: m[2], type: m[1] === 'class' ? 'class' : 'fn' }); return; }
    if (kind === 'css') { if ((m = /^\s*([^{}\/@\s][^{}]*?|@[\w-]+[^{]*)\s*\{/.exec(l))) out.push({ line: i, depth, name: m[1].slice(0, 70), type: 'sel' }); return; }
    if (kind === 'html') {
      if ((m = /<(\w[\w-]*)[^>]*\sid="([^"]+)"/.exec(l))) out.push({ line: i, depth, name: m[1] + '#' + m[2], type: 'id' });
      else if ((m = /<(script|style)\b/.exec(l))) out.push({ line: i, depth, name: '<' + m[1] + '>', type: 'tag' });
      else if ((m = /<h([1-3])[^>]*>([^<]+)/.exec(l))) out.push({ line: i, depth, name: m[2], type: 'h' });
    }
    if (kind === 'js' || kind === 'html') {
      if ((m = /^\s*(?:export\s+)?(?:default\s+)?(?:async\s+)?function\s*\*?\s*([\w$]+)/.exec(l))) out.push({ line: i, depth, name: m[1] + '()', type: 'fn' });
      else if ((m = /^\s*(?:export\s+)?class\s+([\w$]+)/.exec(l))) out.push({ line: i, depth, name: m[1], type: 'class' });
      else if ((m = /^\s*(?:export\s+)?(?:const|let|var)\s+([\w$]+)\s*=\s*(?:async\s*)?(?:function\b|\([^)]*\)\s*=>|[\w$]+\s*=>)/.exec(l))) out.push({ line: i, depth, name: m[1] + '()', type: 'fn' });
      else if ((m = /^\s*(?:const|let|var)\s+([A-Z][A-Z0-9_]+)\s*=/.exec(l))) out.push({ line: i, depth, name: m[1], type: 'const' });
    }
  });
  return out;
};
// The buttons of the file viewer are icons; the name of a button is its title.
const FV_I = __FV_ICONS__;
const iconBtn = (cls, icon, label) => {
  const b = el('button', 'fv-btn fv-icon' + (cls ? ' ' + cls : ''));
  b.innerHTML = FV_I[icon];
  b.title = label;
  b.setAttribute('aria-label', label);
  return b;
};
const copyButton = text => {
  const b = iconBtn('fv-copy', 'copy', 'Copy');
  b.addEventListener('click', () => {
    const done = ok => { b.innerHTML = FV_I[ok ? 'done' : 'fail']; b.title = ok ? 'Copied' : 'Not copied'; setTimeout(() => { b.innerHTML = FV_I.copy; b.title = 'Copy'; }, 1400); };
    try { navigator.clipboard.writeText(text).then(() => done(true), () => done(false)); } catch (e) { done(false); }
  });
  return b;
};
// The code: CodeMirror with folds and the matching bracket. Find marks every match and goes to the next with Enter.
const codePane = (text, kind, outline, tools) => {
  const body = el('div', 'fv-body' + (outline.length ? '' : ' no-side'));
  const side = el('nav', 'fv-side'), host = el('div', 'fv-code');
  if (outline.length) {
    side.appendChild(el('div', 'fv-side-head', 'Functions · ' + outline.length));
    body.appendChild(side);
  }
  body.appendChild(host);
  const cm = CodeMirror(host, {
    value: text, readOnly: true, lineNumbers: true, theme: 'agent', matchBrackets: true, lineWrapping: !!(R.fileWrap),
    mode: kind === 'html' ? 'htmlmixed' : kind === 'json' ? { name: 'javascript', json: true } : kind === 'css' ? 'css' : kind === 'js' ? 'javascript' : null,
    foldGutter: kind === 'js' || kind === 'json' || kind === 'css', gutters: ['CodeMirror-linenumbers', 'CodeMirror-foldgutter']
  });
  cm.setSize(null, '100%');
  host.cm = cm;
  const go = line => {
    cm.scrollIntoView({ line, ch: 0 }, 120);
    cm.setCursor({ line, ch: 0 });
    cm.addLineClass(line, 'background', 'fv-flash');
    setTimeout(() => cm.removeLineClass(line, 'background', 'fv-flash'), 1200);
  };
  outline.forEach(o => {
    const b = el('button', 'fv-sym fv-' + o.type);
    b.style.paddingLeft = 8 + o.depth * 12 + 'px';
    b.appendChild(el('span', 'fv-sym-icon', { fn: 'ƒ', class: 'C', id: '#', tag: '<>', sel: '{}', h: 'H', const: 'K' }[o.type] || '·'));
    b.appendChild(el('span', 'fv-sym-name', o.name));
    b.appendChild(el('span', 'fv-sym-line', String(o.line + 1)));
    b.title = o.name + ', line ' + (o.line + 1);
    b.addEventListener('click', () => go(o.line));
    side.appendChild(b);
  });
  // find
  const find = el('input', 'fv-find');
  find.type = 'search';
  find.placeholder = 'Find';
  find.setAttribute('aria-label', 'Find in the file');
  const count = el('span', 'fv-count', '');
  let overlay = null, hits = [], at = -1;
  const mark = () => {
    if (overlay) cm.removeOverlay(overlay);
    const q = find.value;
    hits = [];
    at = -1;
    if (!q) { overlay = null; count.textContent = ''; return; }
    const low = q.toLowerCase();
    overlay = { token: st => { const i = st.string.toLowerCase().indexOf(low, st.pos); if (i === st.pos) { st.pos += q.length; return 'fv-hit'; } if (i < 0) st.skipToEnd(); else st.pos = i; return null; } };
    cm.addOverlay(overlay);
    cm.eachLine(h => { const n = cm.getLineNumber(h), t = h.text.toLowerCase(); let i = t.indexOf(low); while (i >= 0) { hits.push({ line: n, ch: i }); i = t.indexOf(low, i + low.length); } });
    count.textContent = hits.length ? hits.length + (hits.length === 1 ? ' match' : ' matches') : 'no match';
  };
  const next = back => {
    if (!hits.length) return;
    at = (at + (back ? -1 : 1) + hits.length) % hits.length;
    const h = hits[at];
    cm.setSelection(h, { line: h.line, ch: h.ch + find.value.length });
    cm.scrollIntoView(h, 120);
    count.textContent = (at + 1) + ' of ' + hits.length;
  };
  find.addEventListener('input', mark);
  find.addEventListener('keydown', e => { if (e.key === 'Enter') { e.preventDefault(); next(e.shiftKey); } });
  const wrap = iconBtn('fv-wrap', 'wrap', 'Wrap long lines');
  wrap.setAttribute('aria-pressed', String(!!R.fileWrap));
  wrap.addEventListener('click', () => { R.fileWrap = !R.fileWrap; cm.setOption('lineWrapping', R.fileWrap); wrap.setAttribute('aria-pressed', String(R.fileWrap)); });
  tools.appendChild(find);
  tools.appendChild(count);
  tools.appendChild(wrap);
  setTimeout(() => cm.refresh());
  return body;
};
// md: the page, as the md viewer of the state view draws it (its theme), with the contents on the left.
const inlineMd = (into, text) => {
  // `code`, **bold** and [text](link) in a line; the rest is text.
  const re = /`([^`]+)`|\*\*([^*]+)\*\*|\[([^\]]+)\]\(([^)\s]+)\)/g;
  let last = 0, m;
  while ((m = re.exec(text))) {
    if (m.index > last) into.appendChild(document.createTextNode(text.slice(last, m.index)));
    if (m[1] !== undefined) into.appendChild(el('code', 'md-code', m[1]));
    else if (m[2] !== undefined) into.appendChild(el('strong', '', m[2]));
    else { const a = el('a', '', m[3]); if (/^https?:/.test(m[4])) { a.href = m[4]; a.target = '_blank'; a.rel = 'noopener'; } into.appendChild(a); }
    last = re.lastIndex;
  }
  if (last < text.length) into.appendChild(document.createTextNode(text.slice(last)));
};
// The lines of a text before and now: the new lines (add), and the lines taken out before each line of now (gone).
const mdMarks = (before, now) => {
  const A = before.split('\n'), B = now.split('\n'), ld = lineDiff(before, now), gone = {};
  let i = 0, j = 0, wait = [];
  const put = () => { if (wait.length) { gone[j] = wait; wait = []; } };
  while (i < A.length || j < B.length) {
    if (i < A.length && ld.del.has(i)) wait.push(A[i++]);
    else if (j < B.length && ld.add.has(j)) { put(); j++; }
    else if (i < A.length && j < B.length) { put(); i++; j++; }
    else break;
  }
  put();
  return { add: ld.add, gone };
};
// The pointer on a changed part of a page: why it changed (one box on the page).
const whyTip = (row, why) => {
  if (!why) return;
  row.addEventListener('mouseenter', () => {
    let t = document.querySelector('body > .why-tip');
    if (!t) { t = el('div', 'why-tip'); document.body.appendChild(t); }
    t.textContent = why;
    t.hidden = false;
    const b = row.getBoundingClientRect(), r = t.getBoundingClientRect();
    t.style.left = Math.max(8, Math.min(b.left, innerWidth - r.width - 8)) + 'px';
    t.style.top = (b.bottom + 6 + r.height < innerHeight ? b.bottom + 6 : Math.max(8, b.top - 6 - r.height)) + 'px';
  });
  row.addEventListener('mouseleave', () => { const t = document.querySelector('body > .why-tip'); if (t) t.hidden = true; });
};
// ch (Changes): {before, why}. Then green rows are new or changed and red rows were taken out; the pointer on them shows why.
const mdPane = (text, outline, ch) => {
  const body = el('div', 'fv-body fv-md' + (outline.length ? '' : ' no-side'));
  const side = el('nav', 'fv-side'), doc = el('div', 'fv-doc');
  doc.dataset.mdTheme = os.get('extension.views.state-view.ui-data.md_theme') || 'reader';
  const page = el('article', 'md-page');
  const heads = [];
  const marks = ch ? mdMarks(ch.before, text) : { add: new Set(), gone: {} };
  const mark = (row, cls) => { row.classList.add(cls); whyTip(row, ch && ch.why); };
  const mdRow = raw => {
    const line = core.mdLine(raw);
    if (line.type === 'blank') return null;
    const heading = line.type[0] === 'h', row = el(heading ? 'h' + (+line.type[1] + 1) : 'p', 'md-' + line.type);
    if (line.type === 'step') row.appendChild(el('span', 'md-num', line.mark.trim()));
    const t = el('span', 'md-t');
    inlineMd(t, line.text);
    row.appendChild(t);
    return row;
  };
  const goneAt = j => (marks.gone[j] || []).forEach(raw => { const row = mdRow(raw); if (row) { mark(row, 'chg-deleted'); page.appendChild(row); } });
  // the line of the text where each part starts (``` is in a line)
  let at = 0;
  const raws = String(text).split('```'), starts = raws.map(r => { const s = at; at += r.split('\n').length - 1; return s; });
  core.mdParse(text).forEach((part, n) => {
    if (part.kind !== 'lines') {
      const from = starts[n], to = from + raws[n].split('\n').length - 1;
      let changed = false;
      for (let j = from; j <= to; j++) if (marks.add.has(j) || (marks.gone[j] && j > from)) changed = true;
      goneAt(from);
      const box = part.kind === 'svg' ? el('figure', 'diagram') : el('pre', 'code', part.text);
      if (part.kind === 'svg') box.innerHTML = part.text;
      if (changed) mark(box, 'chg-added');
      page.appendChild(box);
      return;
    }
    part.lines.forEach((raw, k) => {
      const j = starts[n] + k;
      // (the first and last lines of a part between two ``` are the lines of the ```: the code shows their changes)
      if ((k || !n) && (k < part.lines.length - 1 || n === raws.length - 1)) goneAt(j);
      const row = mdRow(raw);
      if (!row) return;
      if (marks.add.has(j)) mark(row, 'chg-added');
      if (row.tagName[0] === 'H') heads.push(row);
      page.appendChild(row);
    });
  });
  goneAt(text.split('\n').length);
  doc.appendChild(page);
  if (outline.length) {
    side.appendChild(el('div', 'fv-side-head', 'Contents'));
    outline.forEach((o, i) => {
      const b = el('button', 'fv-sym fv-h');
      b.style.paddingLeft = 8 + o.depth * 12 + 'px';
      b.appendChild(el('span', 'fv-sym-name', o.name));
      b.addEventListener('click', () => { const h = heads[i]; if (h) doc.scrollTop = h.offsetTop - 16; });
      side.appendChild(b);
    });
    body.appendChild(side);
  }
  body.appendChild(doc);
  return body;
};
// json: a tree. An object or a list shows how many it holds and opens on a click; the first two levels are open.
// A long text shows as "...", as in the state view. Find opens the parts that have the text and marks them.
const jsonPane = (value, tools) => {
  const body = el('div', 'fv-body no-side'), box = el('div', 'fv-json');
  body.appendChild(box);
  const q = { text: '' };
  const has = (v, k) => { const t = q.text; if (!t) return false; if (String(k).toLowerCase().includes(t)) return true; if (v && typeof v === 'object') return Object.keys(v).some(x => has(v[x], x)); return String(v).toLowerCase().includes(t); };
  const val = v => {
    if (v === null) return el('span', 'jv-null', 'null');
    if (typeof v === 'string') {
      if ((v.length > 90 || v.includes('\n')) && !core.emptyText(JSON.stringify(v))) {
        const w = el('span', 'long jv-str', '"..."');
        w.title = v.slice(0, 300);
        w.addEventListener('click', () => preview('text', v));
        return w;
      }
      return el('span', 'jv-str', JSON.stringify(v));
    }
    return el('span', typeof v === 'number' ? 'jv-num' : 'jv-bool', String(v));
  };
  const row = (k, v, depth, into) => {
    const r = el('div', 'jv-row');
    r.style.paddingLeft = depth * 16 + 8 + 'px';
    const open = v && typeof v === 'object';
    const caret = el('span', 'jv-caret', open ? '▸' : '');
    r.appendChild(caret);
    if (k !== null) { const key = el('span', 'jv-key', into.arr ? k : JSON.stringify(k).slice(1, -1)); r.appendChild(key); r.appendChild(el('span', 'jv-colon', ': ')); }
    const hit = q.text && (String(k).toLowerCase().includes(q.text) || (!open && String(v).toLowerCase().includes(q.text)));
    if (hit) r.classList.add('jv-hit');
    into.appendChild(r);
    if (!open) { r.appendChild(val(v)); return; }
    const n = Object.keys(v).length;
    r.appendChild(el('span', 'jv-sum', Array.isArray(v) ? '[ ' + n + (n === 1 ? ' item ]' : ' items ]') : '{ ' + n + (n === 1 ? ' key }' : ' keys }')));
    const kids = el('div', 'jv-kids');
    kids.arr = Array.isArray(v) ? true : null;
    into.appendChild(kids);
    let built = false;
    const set = on => {
      caret.textContent = on ? '▾' : '▸';
      kids.hidden = !on;
      if (on && !built) { built = true; Object.keys(v).forEach(x => row(x, v[x], depth + 1, kids)); }
    };
    r.classList.add('jv-open');
    r.addEventListener('click', e => { if (e.target.closest('.long')) return; set(kids.hidden); });
    set(q.text ? has(v, k) : depth < 2);
    r.setAll = set;
  };
  const draw = () => { box.textContent = ''; const root = el('div'); box.appendChild(root); row(null, value, 0, root); };
  draw();
  const find = el('input', 'fv-find');
  find.type = 'search';
  find.placeholder = 'Find keys and values';
  find.setAttribute('aria-label', 'Find in the JSON');
  find.addEventListener('input', () => { clearTimeout(find.t); find.t = setTimeout(() => { q.text = find.value.trim().toLowerCase(); draw(); }, 150); });
  const all = on => { const walk = () => box.querySelectorAll('.jv-open').forEach(r => { const k = r.nextElementSibling; if (k && k.hidden === on) r.setAll(on); }); for (let i = 0; i < (on ? 6 : 1); i++) walk(); };
  const ex = iconBtn('', 'open', 'Open all'), co = iconBtn('', 'close', 'Close all');
  ex.addEventListener('click', () => all(true));
  co.addEventListener('click', () => { draw(); box.querySelectorAll('.jv-open').forEach(r => { const k = r.nextElementSibling; if (k && !k.hidden && r !== box.querySelector('.jv-open')) r.setAll(false); }); });
  tools.appendChild(find);
  tools.appendChild(ex);
  tools.appendChild(co);
  return body;
};
const fileView = (name, text, ch) => {
  const fk = fileKind(name), box = el('div', 'fv fv-' + fk.kind);
  const head = el('div', 'fv-head'), tools = el('div', 'fv-tools');
  // the kind of the file, its size and its tokens (the name is in the path above the viewer)
  head.appendChild(el('span', 'fv-badge fv-badge-' + fk.ext.toLowerCase(), fk.ext.toUpperCase()));
  head.appendChild(el('span', 'fv-size', (kb(text.length) || '0 KB') + ' · ≈ ' + tok(Math.round(text.length / 4))));
  // md and json have a second mode: their source
  R.fileMode = R.fileMode || {};
  let parsed;
  if (fk.kind === 'json') {
    try { parsed = fk.ext === 'jsonl' ? text.split('\n').filter(l => l.trim()).map(l => JSON.parse(l)) : core.parseJsonc(text); } catch (e) {
      // a json with slips (a missing quote, a comma) is repaired as Save in the state view repairs it
      try { parsed = core.parseJsonc(core.autofix(text)); } catch (e2) { parsed = undefined; }
    }
  }
  const modes = fk.kind === 'md' ? ['Read', 'Source'] : fk.kind === 'json' && parsed !== undefined ? ['Tree', 'Source'] : [];
  const seg = el('div', 'fv-seg');
  const mode = () => modes.includes(R.fileMode[fk.kind]) ? R.fileMode[fk.kind] : modes[0];
  modes.forEach(m => {
    const b = iconBtn('', m.toLowerCase(), m);
    b.setAttribute('aria-pressed', String(m === mode()));
    b.addEventListener('click', () => { R.fileMode[fk.kind] = m; box.replaceWith(fileView(name, text, ch)); });
    seg.appendChild(b);
  });
  if (modes.length) head.appendChild(seg);
  head.appendChild(tools);
  const m = mode();
  // md: one select of the styles of the md viewer of the state view; a choice sets state-view ui-data.md_theme for both
  if (fk.kind === 'md' && m === 'Read') {
    const style = el('select', 'fv-style');
    style.title = 'Style';
    style.setAttribute('aria-label', 'Style of the page');
    ['reader', 'white', 'black', 'sepia', 'night', 'mono'].forEach(t => {
      const o = el('option', '', t[0].toUpperCase() + t.slice(1));
      o.value = t;
      style.appendChild(o);
    });
    style.value = os.get('extension.views.state-view.ui-data.md_theme') || 'reader';
    style.addEventListener('change', () => {
      const t = style.value;
      os.call('local.set-md-theme', { theme: t }, 'extension.views.state-view').then(() => {
        const doc = box.querySelector('.fv-doc');
        if (doc) doc.dataset.mdTheme = t;
      }).catch(console.error);
    });
    head.appendChild(style);
  }
  // Contents (md) and the functions (code): hidden until the button shows them
  const outline = fk.kind === 'json' && m === 'Tree' ? [] : outlineOf(text, fk.kind === 'md' ? 'md' : fk.kind, fk.ext);
  if (outline.length) {
    const side = iconBtn('fv-side-btn', 'side', fk.kind === 'md' && m === 'Read' ? 'Contents' : 'Functions');
    side.setAttribute('aria-pressed', String(!!R.fileSide));
    side.addEventListener('click', () => { R.fileSide = !R.fileSide; box.replaceWith(fileView(name, text, ch)); });
    head.appendChild(side);
  }
  const shown = R.fileSide ? outline : [];
  head.appendChild(copyButton(text));
  // Full screen: the viewer covers the page; the button or Escape gives it back its place.
  const full = iconBtn('fv-full-btn', R.fileFull ? 'exit' : 'full', R.fileFull ? 'Exit full screen' : 'Full screen');
  full.setAttribute('aria-pressed', String(!!R.fileFull));
  const setFull = on => {
    R.fileFull = on;
    box.classList.toggle('fv-full', on);
    full.innerHTML = FV_I[on ? 'exit' : 'full'];
    full.title = on ? 'Exit full screen' : 'Full screen';
    full.setAttribute('aria-label', full.title);
    full.setAttribute('aria-pressed', String(on));
    const cm = box.querySelector('.fv-code');
    if (cm && cm.cm) setTimeout(() => cm.cm.refresh());
  };
  full.addEventListener('click', () => setFull(!box.classList.contains('fv-full')));
  box.addEventListener('keydown', e => { if (e.key === 'Escape' && box.classList.contains('fv-full')) { e.stopPropagation(); setFull(false); } });
  box.tabIndex = -1;
  head.appendChild(full);
  box.appendChild(head);
  if (R.fileFull) { box.classList.add('fv-full'); setTimeout(() => box.focus()); }
  if (fk.kind === 'md' && m === 'Read') box.appendChild(mdPane(text, shown, ch && typeof ch.before === 'string' && ch.before !== text ? ch : null));
  else if (fk.kind === 'json' && m === 'Tree') box.appendChild(jsonPane(parsed, tools));
  else box.appendChild(codePane(text, fk.kind === 'md' ? 'code' : fk.kind, shown, tools));
  return box;
};
// The pseudo code of a function (its field pseudo): what the code does, step by step. Each line has its number; the
// keywords (IF, ELSE, FOR EACH, CALL, SET, RETURN, THROW...) have their colors; the lines inside a step are indented,
// with a guide line. The docs of the function are on top.
const PSEUDO_WORDS = /^(ELSE IF|IF|ELSE|FOR EACH|WHEN|WHILE|CALL|SET|READ|DRAW|WATCH|WAIT|RETURN|THROW|TRY|FIND|FILL|REPLACE|BIND|MARK|EMPTY|START|STOP|SHOW|HIDE|PUT|ADD|SKIP|KEEP|LEAVE|REMEMBER|RELOAD|RUN|CREATE|OPEN|CLOSE|FOLD|GIVE|AFTER|REMOVE|FORGET)\b/;
const pseudoView = (f, name) => {
  const box = el('div', 'fv fv-pseudo'), head = el('div', 'fv-head');
  head.appendChild(el('span', 'fv-badge fv-badge-pseudo', 'ƒ'));
  const text = typeof f.pseudo === 'string' ? f.pseudo : '';
  head.appendChild(el('span', 'fv-size', text ? (kb(text.length) || '0 KB') + ' · ≈ ' + tok(Math.round(text.length / 4)) : ''));
  if (text) head.appendChild(copyButton(text));
  box.appendChild(head);
  const body = el('div', 'ps-body');
  if (f.docs) body.appendChild(el('p', 'ps-docs', f.docs));
  if (!text) { body.appendChild(el('p', 'tl-text', 'This function has no pseudo code yet.')); box.appendChild(body); return box; }
  const list = el('ol', 'ps-lines');
  text.split('\n').forEach(line => {
    const depth = Math.floor(/^ */.exec(line)[0].length / 2), t = line.trim(), li = el('li', 'ps-line');
    for (let i = 0; i < depth; i++) li.appendChild(el('span', 'ps-guide'));
    const m = PSEUDO_WORDS.exec(t);
    const kw = m ? m[1] : '', group = /^(IF|ELSE IF|ELSE|FOR EACH|WHEN|WHILE|TRY|AFTER)$/.test(kw) ? 'flow' : /^(RETURN|THROW|STOP|SKIP|LEAVE)$/.test(kw) ? 'exit' : /^(CALL|RUN|RELOAD)$/.test(kw) ? 'call' : 'act';
    if (kw) li.appendChild(el('span', 'ps-kw ps-' + group, kw));
    const rest = el('span', 'ps-text');
    // a name of a function or a field (local.x, ui-data, a.b) shows as code
    const words = t.slice(kw.length).replace(/^:?\s*/, '').split(/(\b(?:local\.[\w.-]+|[\w-]+-view|ui-data|os\.[\w.]+|get-state|render|unmount)\b|"[^"]*")/);
    words.forEach((w, i) => { if (!w) return; rest.appendChild(i % 2 ? el('code', w.startsWith('"') ? 'ps-str' : 'ps-name', w) : document.createTextNode(w)); });
    li.appendChild(rest);
    list.appendChild(li);
  });
  body.appendChild(list);
  box.appendChild(body);
  return box;
};
// Why a run changed a file: the why of the file, then each step that changed it.
const whyOf = (run, path) => {
  if (!run) return '';
  const changes = x => x.path === path && x.action !== 'read', f = (run.files || []).find(changes);
  const steps = (run.steps || []).map((s, i) => (s.files || []).some(changes) ? 'Step ' + (i + 1) + ': ' + s.title + (s.why ? '. ' + s.why : '') : '').filter(Boolean);
  return [f && f.why].concat(steps).filter(Boolean).join('\n');
};
const KIND_TAB = { files: 'File', views: 'View', functions: 'Function', network: 'Request', environment: 'Value' };
const has = (o, keys) => keys.every(k => { if (!o || typeof o !== 'object' || !(k in o)) return false; o = o[k]; return true; });
const atKeys = (o, keys) => keys.reduce((x, k) => x && typeof x === 'object' ? x[k] : undefined, o);
const itemsOf = (o, kind) => {
  const out = [], x = o || {}, ext = x.extension || {};
  if (kind === 'files') Object.keys(x.agents || {}).forEach(a => {
    const walk = (dir, keys) => Object.keys(dir || {}).forEach(k => {
      if (dir[k] && typeof dir[k] === 'object') walk(dir[k], keys.concat(k)); else out.push({ tree: [a].concat(keys, k), keys: ['agents', a, 'files'].concat(keys, k) });
    });
    walk((x.agents[a] || {}).files, []);
  });
  if (kind === 'views') Object.keys(ext.views || {}).forEach(v => out.push({ tree: [v], keys: ['extension', 'views', v] }));
  if (kind === 'functions') {
    Object.keys(ext.functions || {}).forEach(f => out.push({ tree: ['shared functions', f], keys: ['extension', 'functions', f] }));
    Object.keys(ext.views || {}).forEach(v => Object.keys((ext.views[v] || {}).functions || {}).forEach(f => out.push({ tree: [v, f], keys: ['extension', 'views', v, 'functions', f] })));
  }
  if (kind === 'network') Object.keys(x.network || {}).forEach(g => Object.keys(x.network[g] || {}).forEach(n => out.push({ tree: [g, n], keys: ['network', g, n] })));
  if (kind === 'environment') Object.keys(x.environment || {}).forEach(k => out.push({ tree: [k], keys: ['environment', k] }));
  return out;
};
const kindView = (box, kind, p) => {
  const q = String(svd.filter || '').trim().toLowerCase();
  // All the items: in the state after the block, and the ones it deleted.
  const seen = {}, items = [];
  [p.full, p.fullBefore, p.before].forEach(o => itemsOf(o, kind).forEach(it => {
    const k = it.keys.join('\u0000');
    if (!seen[k]) { seen[k] = true; items.push(it); }
  }));
  // The change of an item: a change of the item itself, or of something in it (updated), or of what holds it.
  const prefix = (a, b) => a.length <= b.length && a.every((k, i) => k === b[i]);
  items.forEach(it => {
    const own = p.rows.find(r => r.keys.length === it.keys.length && prefix(r.keys, it.keys));
    const inner = p.rows.some(r => r.keys.length > it.keys.length && prefix(it.keys, r.keys));
    const outer = p.rows.filter(r => r.keys.length < it.keys.length && prefix(r.keys, it.keys)).pop();
    it.change = own ? own.type : inner ? 'updated' : outer ? (outer.type === 'updated' ? (has(p.after, it.keys) && !has(p.before, it.keys) ? 'added' : !has(p.after, it.keys) && has(p.before, it.keys) ? 'deleted' : 'updated') : outer.type) : null;
    if (it.change === 'updated' && p.fullBefore && JSON.stringify(atKeys(p.fullBefore, it.keys)) === JSON.stringify(atKeys(p.full, it.keys))) it.change = null;
  });
  const shown = items.filter(it => !q || it.keys.join('/').toLowerCase().includes(q) || it.tree.join('/').toLowerCase().includes(q));
  const changed = items.filter(it => it.change).length;
  box.appendChild(el('p', 'tl-text', p.state ? items.length + ' ' + kind + ' in the state of ' + p.head + '. Choose one on the left.'
    : items.length + ' ' + kind + ' in the state' + (p.fullBefore ? ' of v' + p.head : ' now') + '; ' + (p.what || 'this block') + ' changed ' + changed + '. Choose one on the left.'));
  if (!shown.length) { box.appendChild(el('p', 'tl-text', items.length ? 'No ' + kind + ' have the filter text.' : 'The state has no ' + kind + '.')); return; }
  R.pick = R.pick || {};
  const key = it => it.keys.join('\u0000');
  let pick = shown.find(it => key(it) === (R.pick[kind] || {}).key) || shown.find(it => it.change) || shown[0];
  const grid = el('div', 'kv'), tree = el('div', 'kv-tree'), main = el('div', 'kv-main');
  // The tree: a folder for each part of the paths; a folder that holds a change has its color.
  const root = {};
  shown.forEach(it => {
    let node = root;
    it.tree.slice(0, -1).forEach(d => { node = node[d + '/'] = node[d + '/'] || {}; });
    node[it.tree[it.tree.length - 1]] = it;
  });
  const buttons = [];
  const draw = (node, into, depth) => Object.keys(node).sort((a, b) => (b.endsWith('/') - a.endsWith('/')) || (a < b ? -1 : 1)).forEach(k => {
    const x = node[k];
    if (k.endsWith('/') && !x.keys) {
      const d = el('details');
      d.open = true;
      const sum = el('summary', '', k);
      sum.style.paddingLeft = depth * 14 + 4 + 'px';
      const all = []; (function c(n) { Object.values(n).forEach(y => y.keys ? all.push(y) : c(y)); })(x);
      if (all.some(y => y.change)) sum.classList.add('updated');
      d.appendChild(sum);
      draw(x, d, depth + 1);
      into.appendChild(d);
      return;
    }
    const b = el('button', 'kv-item' + (x.change ? ' ' + x.change : '') + (x === pick ? ' on' : ''), k);
    b.style.paddingLeft = depth * 14 + 4 + 'px';
    b.title = x.keys.join('.') + (x.change ? ' (' + x.change + ')' : '');
    b.addEventListener('click', () => { pick = x; R.pick[kind] = { key: key(x), tab: (R.pick[kind] || {}).tab }; buttons.forEach(y => y.classList.toggle('on', y === b)); drawMain(); });
    buttons.push(b);
    into.appendChild(b);
  });
  draw(root, tree, 0);
  grid.appendChild(tree);
  grid.appendChild(main);
  box.appendChild(grid);
  // the chosen item is in sight in the tree
  setTimeout(() => { const on = tree.querySelector('.kv-item.on'); if (on) tree.scrollTop = on.offsetTop - tree.offsetTop - 60; });
  const drawMain = () => {
    main.textContent = '';
    const it = pick, now = atKeys(p.full, it.keys), was = has(p.fullBefore, it.keys) ? atKeys(p.fullBefore, it.keys) : atKeys(p.before, it.keys);
    const value = now !== undefined ? now : was, tabs = [KIND_TAB[kind]].concat(kind === 'functions' ? ['Pseudo code'] : [], it.change ? ['Changes'] : []);
    let tab = (R.pick[kind] || {}).tab;
    if (!tabs.includes(tab)) tab = tabs[0];
    const head = el('div', 'kv-head');
    head.appendChild(el('span', '', kind === 'files' ? it.tree.join('/') : it.keys.join('.')));
    if (it.change) head.appendChild(el('span', 'tl-chip' + (it.change === 'added' ? ' good' : it.change === 'deleted' ? ' bad' : ''), it.change));
    main.appendChild(head);
    const bar = el('div', 'kv-tabs');
    bar.setAttribute('role', 'tablist');
    tabs.forEach(t => {
      const b = el('button', '', t);
      b.setAttribute('role', 'tab');
      b.setAttribute('aria-selected', String(t === tab));
      b.addEventListener('click', () => { R.pick[kind] = { key: key(it), tab: t }; drawMain(); });
      bar.appendChild(b);
    });
    main.appendChild(bar);
    const name = it.tree.join('/'), modeOf = path => /\.html$/.test(path) ? 'html' : /\.js$/.test(path) ? 'js' : /\.jsonc?$/.test(path) ? 'json' : 'text';
    const json = (label, v) => stateBox(label, { text: JSON.stringify(v === undefined ? null : v, null, 2), marks: [] }, { all: true });
    if (tab === 'Pseudo code') { main.appendChild(pseudoView(value || {}, it.tree[it.tree.length - 1])); return; }
    if (tab !== 'Changes') {
      if (now === undefined) main.appendChild(el('p', 'tl-text', 'This block deleted it. This is how it was.'));
      // an updated file: the text before it, and why the run changed it (the read mode of md shows the changes)
      const old = it.change === 'updated' ? (has(p.before, it.keys) ? atKeys(p.before, it.keys) : atKeys(p.fullBefore, it.keys)) : undefined;
      if (kind === 'files') main.appendChild(typeof value === 'string' ? fileView(name, value, typeof old === 'string' ? { before: old, why: whyOf(p.run, it.keys.slice(3).join('/')) } : null) : json(name, value));
      else if (kind === 'views') {
        const v = value || {};
        if (typeof v.html === 'string') main.appendChild(code('html', v.html, 'html', 1));
        main.appendChild(json('ui-data', v['ui-data']));
        main.appendChild(el('div', 'tl-used', 'functions: ' + (Object.keys(v.functions || {}).join(', ') || 'none')));
      } else if (kind === 'functions') {
        const f = Object.assign({}, value || {}), src = f.code;
        delete f.code;
        main.appendChild(typeof src === 'string' ? code('code', src, 'js', 1) : el('p', 'tl-text', 'No code: it runs its calls in order.'));
        main.appendChild(json('the other fields', f));
      } else main.appendChild(json(name, value));
      return;
    }
    // Changes: a text side by side (red lines only before, green lines only after); an object cut down to the changes.
    const before = has(p.before, it.keys) ? atKeys(p.before, it.keys) : undefined, after = has(p.after, it.keys) ? atKeys(p.after, it.keys) : undefined;
    const texts = (a, b, path) => (typeof a === 'string' || a === undefined) && (typeof b === 'string' || b === undefined) && (a !== undefined || b !== undefined) ? sideCode(path, p.from, p.head, a, b) : null;
    const whole = texts(before, after, name);
    if (whole) { main.appendChild(whole); return; }
    if (kind === 'views' || kind === 'functions') {
      const field = kind === 'views' ? 'html' : 'code', side = texts((before || {})[field], (after || {})[field], field + (kind === 'views' ? '.html' : '.js'));
      if (side && (before || {})[field] !== (after || {})[field]) { main.appendChild(el('div', 'tl-detail-sub', field)); main.appendChild(side); }
    }
    const legend = el('div', 'st-legend');
    ['added', 'updated', 'deleted'].forEach(k => legend.appendChild(el('span', k, k)));
    main.appendChild(legend);
    const wrap = x => x === undefined ? {} : x && typeof x === 'object' ? x : { value: x };
    main.appendChild(stateBox('What changed in ' + it.tree[it.tree.length - 1], core.changesView(wrap(before), wrap(after)), { all: true }));
  };
  drawMain();
};

// The replay moves to the next step while ui-data.playing is true.
if (d.playing && !R.timer) R.timer = setInterval(() => {
  if (!os.mounted(v)) { clearInterval(R.timer); R.timer = null; return; }
  os.call('local.next', { delta: 1 }, v).catch(console.error);
}, 1600);
if (!d.playing && R.timer) { clearInterval(R.timer); R.timer = null; }
""".replace("__FV_ICONS__", FV_ICONS_JS))

TL_SELECT = sig("select", ["id"], r"""
// Choosing a block stops the replay; the state view shows the block. id null chooses no block: the state view shows
// the last agent run.
const d = os.get('extension.views.timeline-view.ui-data'), R = os.refs['timeline-view'];
d.playing = false;
R.flow = null;
d.selected = id === undefined ? null : id;
""")

TL_NEXT = sig("next", ["delta"], r"""
// Moves delta blocks, inside the flow that plays if there is one (the arrow buttons leave the flow). The replay
// stops at the block that was the last when it started.
const d = os.get('extension.views.timeline-view.ui-data'), R = os.refs['timeline-view'];
if (R.flow && !d.playing) R.flow = null;
const ids = R.flow ? R.flow.ids : R.steps;
// (no block chosen: the block that shows, the last agent run)
let at = ids.indexOf(d.selected === null && R.current ? R.current.id : d.selected);
if (at < 0) at = R.flow ? -1 : ids.length - 1;
const to = Math.max(0, Math.min(ids.length - 1, at + (+delta || 0)));
d.selected = ids[to];
if (to === ids.length - 1 || (d.playing && ids[to] === R.end)) d.playing = false;
""")

TL_PLAY = sig("play", [], r"""
// Starts or stops the replay. From the last block, it starts again at the first. A paused flow goes on; after
// the end of a flow, the replay is of all the blocks.
const d = os.get('extension.views.timeline-view.ui-data'), R = os.refs['timeline-view'];
if (R.flow && !d.playing && d.selected === R.flow.ids[R.flow.ids.length - 1]) R.flow = null;
const ids = R.flow ? R.flow.ids : R.steps;
d.playing = !d.playing;
const at = ids.indexOf(d.selected);
if (d.playing && (at < 0 || at === ids.length - 1)) d.selected = ids[0];
// With Track state on, each move adds a block: the replay ends at the block that is the last now.
// Untracked, it goes on to the newest block: after a reload, the page is still starting when the replay starts.
if (d.playing) R.end = os.get('extension.views.state-view.ui-data.track_state') && !R.flow ? ids[ids.length - 1] : null;
""")

TL_SHOW = sig("show", ["only"], r"""
// The AI runs and UI buttons: only the AI run blocks (runs), or only the other blocks (ui). The pressed button
// again shows all the blocks.
if (only !== 'runs' && only !== 'ui') throw new Error('only is runs or ui, not ' + only);
const d = os.get('extension.views.timeline-view.ui-data');
d.show = d.show === only ? 'all' : only;
// (the chosen block can be one that does not show now: the last agent run, or the newest block, shows)
d.selected = null;
d.playing = false;
os.refs['timeline-view'].flow = null;
""")

TL_CLOSE = sig("close", [], r"""
// The close button: the timeline goes. The Timeline button of the state view shows it again.
os.get('extension.views.state-view.ui-data').timeline_open = false;
""")

TL_FLOWS = sig("toggleFlows", [], r"""
// Opens or closes the list of saved flows.
const d = os.get('extension.views.timeline-view.ui-data');
d.flows_open = !d.flows_open;
""")

TL_PLAY_FLOW = sig("playFlow", ["name"], r"""
// Plays a saved flow: its blocks, one after the other. A flow names its blocks; each is the first block with that
// name after the block before it.
const d = os.get('extension.views.timeline-view.ui-data'), R = os.refs['timeline-view'];
const flow = d.flows.find(f => f.name === name);
if (!flow) throw new Error('No flow ' + name + '. Flows: ' + d.flows.map(f => f.name).join(', '));
const names = R.names || [], ids = [];
let from = 0;
flow.steps.forEach(n => {
  const at = names.indexOf(n, from);
  if (at >= 0) { ids.push(R.steps[at]); from = at + 1; }
});
if (!ids.length) throw new Error('None of the blocks of ' + name + ' is in the timeline.');
R.flow = { name, ids };
R.end = ids[ids.length - 1];
d.flows_open = false;
d.selected = ids[0];
d.playing = ids.length > 1;
return { blocks: ids.length };
""")

MAIN_VIEWS = ["docs-view", "state-view", "notes-view"]   # the views between the header and the footer: one at a time

def open_view(name, flag):
    return sig("open" + "".join(w.capitalize() for w in name.split("-")), [], f"""
const d = os.get('extension.views.header-view.ui-data');
d.{flag} = !os.mounted('extension.views.{name}');
// One main view at a time: the one that is open closes.
if (d.{flag}) for (const o of {json.dumps([m for m in MAIN_VIEWS if m != name])})
  if (os.mounted('extension.views.' + o)) await ctx.call('extension.functions.unmount', {{ view_path: 'extension.views.' + o }});
d.docs_open = d.{flag} ? {str(name == 'docs-view').lower()} : d.docs_open;
d.state_open = d.{flag} ? {str(name == 'state-view').lower()} : d.state_open;
if (d.{flag}) await ctx.call('extension.functions.render', {{ view_path: 'extension.views.{name}' }});
else await ctx.call('extension.functions.unmount', {{ view_path: 'extension.views.{name}' }});
await ctx.call('extension.functions.render', {{ view_path: 'extension.views.header-view' }});
""")

REC_INIT = sig("init", [], r"""
// The record button and the keys work from now; a new init takes the place of the old one (its listeners go).
const v = 'extension.views.recorder-view', old = os.refs['recorder-view'];
if (old && old.off) old.off();
const R = os.refs['recorder-view'] = { keys: {}, lastUp: 0 };
const call = (name, input) => os.call(name, input || {}, v).catch(console.error);
const recording = () => !!os.get(v + '.ui-data.recording');
// The timer in the header: Audio or Video, and the time since the start.
R.drawTimer = () => {
  const d = os.get(v + '.ui-data'), t = document.getElementById('rec-timer');
  if (!t) return;
  t.hidden = !d.recording;
  if (!d.recording) return;
  const s = Math.max(0, Math.floor((Date.now() - d.started_at) / 1000));
  t.textContent = (d.recording === 'video' ? 'Video ' : 'Audio ') + String(Math.floor(s / 60)).padStart(2, '0') + ':' + String(s % 60).padStart(2, '0');
};
// The button: one click records audio, two clicks open the menu (audio, video, notes). While it records, a click stops
// it. While the menu is open, a click on the button or out of the menu closes it.
const menuOpen = () => !!os.get(v + '.ui-data.menu_open');
const onClick = e => {
  if (!e.target.closest) return;
  if (!e.target.closest('#rec-button')) {
    if (menuOpen() && !e.target.closest('#rec-menu')) call('local.toggle-menu', { open: false });
    return;
  }
  // (the click after a hold of 4 s does nothing)
  if (R.held) { R.held = false; return; }
  if (recording()) { clearTimeout(R.clickTimer); R.clickTimer = null; call('local.stop'); return; }
  if (R.clickTimer) { clearTimeout(R.clickTimer); R.clickTimer = null; call('local.toggle-menu', { open: true }); return; }
  R.clickTimer = setTimeout(() => { R.clickTimer = null; call(menuOpen() ? 'local.toggle-menu' : 'local.start', menuOpen() ? { open: false } : { mode: 'audio' }); }, 300);
};
// The keys: Arrow Up two times records audio; Arrow Up and Arrow Down at the same time record video. The same keys
// stop it. Not while you type in a field or an editor.
const typing = t => t && t.closest && t.closest('input, textarea, select, [contenteditable=""], [contenteditable="true"], .CodeMirror');
const onKeyDown = e => {
  if (e.key === 'Escape' && menuOpen()) { call('local.toggle-menu', { open: false }); return; }
  if ((e.key !== 'ArrowUp' && e.key !== 'ArrowDown') || typing(e.target)) return;
  R.keys[e.key] = true;
  if (e.repeat) return;
  if (R.keys.ArrowUp && R.keys.ArrowDown) {
    R.lastUp = 0;
    e.preventDefault();
    call(recording() ? 'local.stop' : 'local.start', { mode: 'video' });
  } else if (e.key === 'ArrowUp') {
    if (Date.now() - R.lastUp < 400) { R.lastUp = 0; e.preventDefault(); call(recording() ? 'local.stop' : 'local.start', { mode: 'audio' }); }
    else R.lastUp = Date.now();
  }
};
// Hold the button 4 s: the Notes page opens.
const onPress = e => {
  if (!e.target.closest || !e.target.closest('#rec-button') || e.button) return;
  clearTimeout(R.holdTimer);
  R.held = false;
  R.holdTimer = setTimeout(() => { R.holdTimer = null; R.held = true; call('local.open-notes'); }, 4000);
};
const onRelease = () => { clearTimeout(R.holdTimer); R.holdTimer = null; };
const onKeyUp = e => { delete R.keys[e.key]; };
const onBlur = () => { R.keys = {}; };
// Select mode, while it records: the element under the pointer has a red frame. A click selects it (the page does not
// get the click): it has a purple frame, and its path shows above it.
const box = (cls) => { const b = document.createElement('div'); b.className = cls; b.hidden = true; document.body.appendChild(b); return b; };
R.hover = box('rec-hover');
R.picked = box('rec-hover picked');
R.label = box('rec-label');
// (an icon selects its button; a part of a timeline block selects the block)
const target = e => {
  const t = e.target;
  if (!recording() || !t.closest || t.closest('#recorder-view')) return null;
  return t.closest('.tl-step') || (t.closest('svg') ? t.closest('svg').parentElement : t);
};
const frame = (el, b) => {
  const r = el.getBoundingClientRect();
  Object.assign(b.style, { left: r.left + 'px', top: r.top + 'px', width: r.width + 'px', height: r.height + 'px' });
};
R.place = () => {
  // (a view that draws itself again has a new element at the same place: it is found again by its selector)
  if (R.selectedEl && !R.selectedEl.isConnected && R.selectedSel) R.selectedEl = document.querySelector(R.selectedSel);
  const el = R.selectedEl, d = os.get(v + '.ui-data');
  const show = !!(d.recording && d.selected && el && el.isConnected);
  R.picked.hidden = R.label.hidden = !show;
  if (!show) return;
  frame(el, R.picked);
  R.label.textContent = d.selected;
  const r = el.getBoundingClientRect();
  R.label.style.left = Math.max(4, Math.min(r.left, innerWidth - R.label.offsetWidth - 4)) + 'px';
  R.label.style.top = (r.top > 30 ? r.top - 26 : Math.min(r.bottom + 4, innerHeight - 26)) + 'px';
};
// The path of an element: the view it is in (its path in the state), then the elements from the view down to it,
// and the block of the timeline when it is in one.
const partsOf = el => {
  const view = el.closest('[id$="-view"]'), parts = [];
  for (let x = el; x && x !== view; x = x.parentElement) {
    if (x.id) { parts.unshift('#' + x.id); break; }
    let s = x.tagName.toLowerCase();
    const cls = Array.from(x.classList).find(c => !/^(on|open|sub)$/.test(c));
    if (cls) s += '.' + cls;
    const same = x.parentElement ? Array.from(x.parentElement.children).filter(y => y.tagName === x.tagName) : [];
    if (same.length > 1) s += ':nth-of-type(' + (same.indexOf(x) + 1) + ')';
    parts.unshift(s);
  }
  return { view, parts };
};
const pathOf = el => {
  const { view, parts } = partsOf(el), block = el.closest('.tl-step'), kind = block && block.querySelector('.tl-kind');
  return (view ? 'extension.views.' + view.id : 'the page') + (parts.length ? ' › ' + parts.join(' > ') : '') +
    (block ? ' (block ' + (Array.from(block.parentElement.children).indexOf(block) + 1) + (kind ? ': ' + kind.textContent : '') + ')' : '');
};
const onOver = e => { const t = target(e); R.hover.hidden = !t; if (t) frame(t, R.hover); };
const hold = e => { if (target(e)) { e.preventDefault(); e.stopPropagation(); } };
const onSelect = e => {
  const t = target(e);
  if (!t) return;
  e.preventDefault();
  e.stopPropagation();
  const { view, parts } = partsOf(t);
  R.selectedEl = t;
  R.selectedSel = view ? (parts[0] && parts[0][0] === '#' ? '' : '#' + view.id + (parts.length ? ' > ' : '')) + parts.join(' > ') : null;
  call('local.select', { path: pathOf(t) });
};
const onScroll = () => { R.hover.hidden = true; R.place(); };
const on = [['click', onClick, false], ['pointerdown', onPress, false], ['pointerup', onRelease, false], ['pointercancel', onRelease, false], ['keydown', onKeyDown, true], ['keyup', onKeyUp, true], ['mouseover', onOver, true],
            ['pointerdown', hold, true], ['mousedown', hold, true], ['click', onSelect, true], ['scroll', onScroll, true]];
on.forEach(([n, f, c]) => document.addEventListener(n, f, c));
window.addEventListener('blur', onBlur);
R.off = () => {
  on.forEach(([n, f, c]) => document.removeEventListener(n, f, c));
  window.removeEventListener('blur', onBlur);
  clearInterval(R.tick);
  clearTimeout(R.holdTimer);
  [R.hover, R.picked, R.label].forEach(b => b.remove());
};
os.watch(v, 'local.refresh');
await ctx.call('local.refresh', { after: 'local.init' });
""")

REC_REFRESH = sig("refresh", ["after"], r"""
// The button, the error and the card of the last recording are drawn again from ui-data.
const v = 'extension.views.recorder-view', d = os.get(v + '.ui-data'), R = os.refs['recorder-view'] || {};
const t = document.createElement('template');
t.innerHTML = os.template(os.get(v + '.html'), d);
ctx.root.innerHTML = t.content.firstElementChild.innerHTML;
os.bind(ctx.root, v);
// The recording plays in the card. The file is in the memory of the page (os.refs), not in the state.
const media = ctx.root.querySelector('#rec-media');
if (media && R.url) {
  const m = document.createElement(d.result.kind === 'video' ? 'video' : 'audio');
  m.controls = true;
  m.src = R.url;
  media.appendChild(m);
}
// Select mode is on while it records.
document.documentElement.classList.toggle('rec-select', !!d.recording);
if (R.hover && !d.recording) R.hover.hidden = true;
if (R.place) R.place();
if (R.drawTimer) R.drawTimer();
""")

REC_START = sig("start", ["mode"], r"""
// Records audio (the microphone) or video (a screen, a window or a tab that you choose, with the sound of the tab and
// the microphone when the browser gives them).
const v = 'extension.views.recorder-view', d = os.get(v + '.ui-data'), R = os.refs['recorder-view'];
if (mode !== 'audio' && mode !== 'video') throw new Error('No mode ' + mode);
if (d.recording) throw new Error('It records already');
const md = navigator.mediaDevices, what = mode === 'audio' ? 'the microphone' : 'the screen';
d.error = '';
d.menu_open = false;
if (!md || !window.MediaRecorder || !(mode === 'audio' ? md.getUserMedia : md.getDisplayMedia)) {
  d.error = 'This browser cannot record ' + what + ' on this page.';
  return { recording: false, error: d.error };
}
let stream;
try {
  if (mode === 'audio') {
    stream = await md.getUserMedia({ audio: true });
    R.inputs = [stream];
  } else {
    const screen = await md.getDisplayMedia({ video: true, audio: true });
    const mic = await md.getUserMedia({ audio: true }).catch(() => null);
    const audio = screen.getAudioTracks().concat(mic ? mic.getAudioTracks() : []);
    // two sounds (the tab and the microphone) go into one track
    if (audio.length > 1) {
      R.ac = new AudioContext();
      const out = R.ac.createMediaStreamDestination();
      audio.forEach(a => R.ac.createMediaStreamSource(new MediaStream([a])).connect(out));
      stream = new MediaStream(screen.getVideoTracks().concat(out.stream.getAudioTracks()));
    } else stream = new MediaStream(screen.getVideoTracks().concat(audio));
    R.inputs = [screen, mic].filter(Boolean);
    // "Stop sharing" of the browser stops the recording too
    screen.getVideoTracks()[0].addEventListener('ended', () => { if (os.get(v + '.ui-data.recording')) os.call('local.stop', {}, v).catch(console.error); });
  }
} catch (e) {
  d.error = 'The browser did not let the page record ' + what + ': ' + (e && e.message || e);
  return { recording: false, error: d.error };
}
// Transcription (Settings of Notes): the browser turns what the microphone hears into text while it records.
const set = os.get('extension.views.notes-view.ui-data.settings') || {}, SR = window.SpeechRecognition || window.webkitSpeechRecognition;
R.heard = '';
R.heardError = set.transcribe === 'off' ? 'off' : SR ? '' : 'unsupported';
if (set.transcribe !== 'off' && SR) {
  const sr = R.sr = new SR();
  sr.lang = set.lang || navigator.language;
  sr.continuous = true;
  sr.onresult = ev => { for (let i = ev.resultIndex; i < ev.results.length; i++) if (ev.results[i].isFinal) R.heard += ev.results[i][0].transcript.trim() + ' '; };
  sr.onerror = ev => { R.heardError = ev.error; };
  // (the browser stops after a silence: it starts again while it records)
  sr.onend = () => { if (R.sr === sr && !/not-allowed|service-not-allowed/.test(R.heardError)) try { sr.start(); } catch (e) {} };
  try { sr.start(); } catch (e) { R.heardError = e.message; }
}
R.chunks = [];
R.rec = new MediaRecorder(stream);
R.rec.ondataavailable = x => { if (x.data && x.data.size) R.chunks.push(x.data); };
R.rec.start(1000);
if (R.url) URL.revokeObjectURL(R.url);
R.url = R.blob = R.selectedEl = null;
d.recording = mode;
d.started_at = Date.now();
d.selected = '';
d.selections = [];
d.result = null;
clearInterval(R.tick);
R.tick = setInterval(R.drawTimer, 250);
return { recording: mode };
""")

REC_STOP = sig("stop", [], r"""
// Stops the recording. The file stays in the memory of the page; the card shows it, with Save file.
const v = 'extension.views.recorder-view', d = os.get(v + '.ui-data'), R = os.refs['recorder-view'];
if (!d.recording) return { recording: false };
const rec = R.rec;
if (rec && rec.state !== 'inactive') await new Promise(done => { rec.onstop = done; rec.stop(); });
(R.inputs || []).forEach(x => x.getTracks().forEach(t => t.stop()));
if (R.ac) { R.ac.close(); R.ac = null; }
const sr = R.sr;
R.sr = null;
if (sr) { await new Promise(done => { sr.onend = done; try { sr.stop(); } catch (e) { done(); } setTimeout(done, 1500); }); }
clearInterval(R.tick);
const type = ((rec && rec.mimeType) || (d.recording === 'video' ? 'video/webm' : 'audio/webm')).split(';')[0];
R.blob = new Blob(R.chunks || [], { type });
R.url = URL.createObjectURL(R.blob);
const s = Math.round((Date.now() - d.started_at) / 1000);
d.result = { kind: d.recording, time: String(Math.floor(s / 60)).padStart(2, '0') + ':' + String(s % 60).padStart(2, '0'),
  size: R.blob.size >= 1048576 ? (R.blob.size / 1048576).toFixed(1) + ' MB' : Math.max(1, Math.round(R.blob.size / 1024)) + ' KB', type };
// The recording is a note too (Notes). Its view: the view of the first element that you selected, or the open view.
// (the recordings of the notes stay in os.refs.notes: the memory of a view goes when the view closes)
const notes = os.get('extension.views.notes-view.ui-data'), N = os.refs.notes = os.refs.notes || {};
N.files = N.files || {};
N.heard = N.heard || {};
const first = d.selections.map(x => x.path.split(' ')[0]).find(p => /^extension\.views\./.test(p));
const note = { id: 'n' + Date.now().toString(36), kind: d.recording, at: new Date(d.started_at).toISOString(), time: d.result.time, text: '',
  view_path: first || ['extension.views.state-view', 'extension.views.docs-view'].find(x => os.mounted(x)) || 'extension.views.header-view',
  selections: d.selections.slice(), file: '' };
N.files[note.id] = { blob: R.blob, url: URL.createObjectURL(R.blob) };
N.heard[note.id] = { text: R.heard.trim(), error: R.heardError };
// (on claude.ai the file goes into the files of the page, so the note keeps it after a reload)
const assets = window.claude && window.claude.use ? await window.claude.use('assets').catch(() => null) : null;
if (assets) try { note.file = (await assets.upload(R.blob)).id; } catch (e) {}
notes.notes.unshift(note);
d.recording = '';
return d.result;
""")

REC_SELECT = sig("select", ["path"], r"""
// Select mode: the element that you clicked. Its path shows above it, and goes into the list of this recording.
const d = os.get('extension.views.recorder-view.ui-data');
d.selected = String(path || '');
const s = d.recording ? Math.max(0, Math.floor((Date.now() - d.started_at) / 1000)) : 0;
d.selections.push({ at: String(Math.floor(s / 60)).padStart(2, '0') + ':' + String(s % 60).padStart(2, '0'), path: d.selected });
""")

REC_SAVE = sig("save", [], r"""
// Saves the last recording as a file (webm or mp4). On claude.ai, the page asks you to confirm the download.
const d = os.get('extension.views.recorder-view.ui-data'), R = os.refs['recorder-view'];
if (!R.blob || !d.result) throw new Error('No recording');
const name = 'agent-os-' + d.result.kind + '-' + new Date(d.started_at).toISOString().slice(0, 19).replace(/[:T]/g, '-') + (/mp4/.test(d.result.type) ? '.mp4' : '.webm');
const dl = window.claude && window.claude.use ? await window.claude.use('downloads') : null;
if (dl) {
  await dl.save({ filename: name, data: R.blob });
  return { saved: name };
}
const a = document.createElement('a');
a.href = R.url;
a.download = name;
document.body.appendChild(a);
a.click();
a.remove();
return { saved: name };
""")

REC_TOGGLE_MENU = sig("toggleMenu", ["open"], r"""
// Two clicks on the record button: the menu (Record audio, Record video, Notes). open: true or false; no open: the other.
const d = os.get('extension.views.recorder-view.ui-data');
d.menu_open = typeof open === 'boolean' ? open : !d.menu_open;
""")

REC_OPEN_NOTES = sig("openNotes", [], r"""
// The menu of the record button, or hold the record button 4 s: the Notes page opens. One main view at a time:
// docs-view or state-view closes.
os.get('extension.views.recorder-view.ui-data').menu_open = false;
const h = os.get('extension.views.header-view.ui-data');
let closed = false;
for (const o of ['docs-view', 'state-view'])
  if (os.mounted('extension.views.' + o)) { await ctx.call('extension.functions.unmount', { view_path: 'extension.views.' + o }); closed = true; }
h.docs_open = false;
h.state_open = false;
if (closed) await ctx.call('extension.functions.render', { view_path: 'extension.views.header-view' });
if (!os.mounted('extension.views.notes-view')) await ctx.call('extension.functions.render', { view_path: 'extension.views.notes-view' });
""")

def close_view(name, flag):
    return sig("close", [], f"""
// The close button of the view: it closes, and the button of the header is not pressed.
await ctx.call('extension.functions.unmount', {{ view_path: 'extension.views.{name}' }});
os.get('extension.views.header-view.ui-data').{flag} = false;
await ctx.call('extension.functions.render', {{ view_path: 'extension.views.header-view' }});
""")

NOTES_INIT = sig("init", [], r"""
// The Notes page: what you type goes to the state (Add note, the text of a note, Settings); the page draws again
// after each call.
const v = 'extension.views.notes-view', R = os.refs['notes-view'] = os.refs['notes-view'] || {};
R.picked = R.picked || [];
R.shown = R.shown || [];
const call = (name, input) => os.call(name, input, v).catch(console.error);
ctx.root.addEventListener('input', e => {
  const t = e.target;
  if (t.id === 'notes-new') R.draft = t.value;
  // (the text of a note is kept 400 ms after you stop typing)
  if (t.classList.contains('note-text')) { clearTimeout(R.editTimer); R.editTimer = setTimeout(() => call('local.edit', { id: t.dataset.id, text: t.value }), 400); }
});
ctx.root.addEventListener('change', e => {
  const t = e.target;
  if (t.id === 'notes-transcribe') call('local.set-settings', { transcribe: t.value });
  if (t.id === 'notes-lang') call('local.set-settings', { lang: t.value.trim() });
  if (t.id === 'notes-task') call('local.set-settings', { new_session_task: t.value.trim() });
});
ctx.root.addEventListener('click', e => {
  if (!e.target.closest || !e.target.closest('#notes-add')) return;
  const t = ctx.root.querySelector('#notes-new');
  if (t && t.value.trim()) call('local.add-text', { text: t.value });
});
os.watch(v, 'local.refresh');
await ctx.call('local.refresh', { after: 'local.init' });
""")

NOTES_REFRESH = sig("refresh", ["after"], r"""
// Draws the notes from ui-data. A recording plays in its note; Show state shows the ui-data of the note's view.
const v = 'extension.views.notes-view', d = os.get(v + '.ui-data'), R = os.refs['notes-view'] || {};
// (while you type the text of a note, the page does not draw again: the text box keeps its place)
if (after === 'local.edit') return;
const ids = d.notes.map(n => n.id);
R.picked = (R.picked || []).filter(id => ids.includes(id));
R.shown = (R.shown || []).filter(id => ids.includes(id));
const t = document.createElement('template');
t.innerHTML = os.template(os.get(v + '.html'), Object.assign({}, d, { picked: R.picked, shown: R.shown }));
ctx.root.innerHTML = t.content.firstElementChild.innerHTML;
os.bind(ctx.root, v);
const draft = ctx.root.querySelector('#notes-new');
if (draft && R.draft) draft.value = R.draft;
ctx.root.querySelectorAll('.note-media').forEach(box => {
  const n = d.notes.find(x => x.id === box.dataset.id), f = ((os.refs.notes || {}).files || {})[n.id], url = f ? f.url : n.file ? '/_blob/' + n.file : '';
  if (!url) { box.appendChild(Object.assign(document.createElement('p'), { className: 'note-gone', textContent: 'The recording was only in the memory of the page; it is not here after a reload.' })); return; }
  const m = document.createElement(n.kind === 'video' ? 'video' : 'audio');
  m.controls = true;
  m.src = url;
  box.appendChild(m);
});
ctx.root.querySelectorAll('.note-state').forEach(pre => {
  const n = d.notes.find(x => x.id === pre.dataset.id);
  pre.textContent = JSON.stringify(os.get(n.view_path + '.ui-data'), null, 2) || 'This view has no ui-data.';
});
""")

NOTES_TOGGLE_SETTINGS = sig("toggleSettings", [], r"""
const d = os.get('extension.views.notes-view.ui-data');
d.settings_open = !d.settings_open;
""")

NOTES_SET_SETTINGS = sig("setSettings", ["transcribe", "lang", "new_session_task"], r"""
// transcribe: browser (the default) or off. lang: the language to hear (for example en-US); empty: the language of
// the browser. new_session_task: the id of the scheduled task that Send now new session starts.
const d = os.get('extension.views.notes-view.ui-data');
if (transcribe !== undefined) {
  if (transcribe !== 'browser' && transcribe !== 'off') throw new Error('No transcription ' + transcribe);
  d.settings.transcribe = transcribe;
}
if (lang !== undefined) d.settings.lang = String(lang);
if (new_session_task !== undefined) d.settings.new_session_task = String(new_session_task);
return d.settings;
""")

NOTES_ADD_TEXT = sig("addText", ["text"], r"""
// Add note: a note that you write. Its view is the view that is open under the Notes page.
const d = os.get('extension.views.notes-view.ui-data'), R = os.refs['notes-view'] || {};
if (!String(text || '').trim()) throw new Error('The note has no text');
const note = { id: 'n' + Date.now().toString(36), kind: 'text', at: new Date().toISOString(), time: '', text: String(text),
  view_path: ['extension.views.state-view', 'extension.views.docs-view'].find(x => os.mounted(x)) || 'extension.views.header-view', selections: [], file: '' };
d.notes.unshift(note);
d.message = '';
R.draft = '';
return { id: note.id };
""")

NOTES_EDIT = sig("edit", ["id", "text"], r"""
// The text of a note, as you changed it.
const n = os.get('extension.views.notes-view.ui-data').notes.find(x => x.id === id);
if (!n) throw new Error('No note ' + id);
n.text = String(text);
""")

NOTES_TRANSCRIBE = sig("transcribe", ["id"], r"""
// Transcribe: the text that the browser heard while it recorded goes into the note, where you can change it.
const d = os.get('extension.views.notes-view.ui-data'), n = d.notes.find(x => x.id === id);
if (!n || n.kind === 'text') throw new Error('No recording ' + id);
const h = ((os.refs.notes || {}).heard || {})[id] || { text: '', error: 'gone' };
if (h.text) { n.text = h.text; d.message = ''; return { text: n.text }; }
d.message = {
  off: 'Transcription was off when you recorded (Settings).',
  unsupported: 'This browser cannot transcribe. Chrome and Edge can.',
  'not-allowed': 'The browser did not let the page use the microphone for the text.',
  'service-not-allowed': 'The browser did not let the page use its speech service.',
  gone: 'The text of this recording is not here any more: the browser keeps it only until the page reloads.'
}[h.error] || 'The browser heard no words in this recording' + (h.error ? ' (' + h.error + ')' : '') + '.';
return { text: '' };
""")

NOTES_SEND = sig("send", ["ids", "new_session"], r"""
// Send now: the notes go to Claude, in this Claude session (a comment of the page, sent to Claude). Send now new session:
// they start a new Claude Code session (the task in settings.new_session_task, through the Claude Code Remote connector).
const d = os.get('extension.views.notes-view.ui-data');
const list = (ids || []).map(id => d.notes.find(n => n.id === id)).filter(Boolean);
if (!list.length) throw new Error('No note to send');
const one = n => [(n.kind === 'text' ? 'Note' : (n.kind === 'video' ? 'Video note' : 'Audio note') + ' (' + n.time + ')') + ', ' + n.at,
  n.text || '(no text)', 'View: ' + n.view_path].concat(n.selections.map(x => 'Selected at ' + x.at + ': ' + x.path)).join('\n');
let text = (list.length > 1 ? list.length + ' notes' : 'A note') + ' from the Notes page of Agent OS:\n\n' + list.map(one).join('\n\n');
// (a comment holds at most 4 KB)
while (new TextEncoder().encode(text).length > 4000) text = text.slice(0, -200);
const use = async name => window.claude && window.claude.use ? await window.claude.use(name).catch(() => null) : null;
try {
  if (new_session) {
    const mcp = await use('mcp');
    if (!mcp) { d.message = 'Send now new session works on claude.ai, with the Claude Code Remote connector.'; return { sent: false }; }
    if (!d.settings.new_session_task) { d.message = 'No task for new sessions is set: put its id in Settings, New session task.'; return { sent: false }; }
    await mcp.callTool('Claude Code Remote', 'fire_trigger', { trigger_id: d.settings.new_session_task, text });
    d.message = list.length > 1 ? list.length + ' notes went to a new Claude session.' : 'The note went to a new Claude session.';
  } else {
    const c = await use('comments');
    if (!c) { d.message = 'Send now works on claude.ai.'; return { sent: false }; }
    const can = await c.canSendToClaude().catch(() => 'off');
    if (can !== 'available') {
      d.message = { writers_only: 'Only editors of the page can send to Claude.', no_session: 'No Claude session can get it now.' }[can] || 'Sending to Claude is off here.';
      return { sent: false };
    }
    const at = document.querySelector('#notes-view .note[data-id="' + list[0].id + '"]') || document.querySelector('#notes-view');
    await c.sendToClaude({ anchor: await c.anchorFor(at), text });
    d.message = list.length > 1 ? list.length + ' notes went to Claude.' : 'The note went to Claude.';
  }
} catch (e) {
  d.message = 'Not sent: ' + (e && (e.message || e.code) || e);
  return { sent: false };
}
return { sent: list.length };
""")

NOTES_DELETE = sig("deleteNote", ["id"], r"""
// Delete: the note goes, with its recording.
const d = os.get('extension.views.notes-view.ui-data'), N = os.refs.notes || {};
const n = d.notes.find(x => x.id === id);
if (!n) throw new Error('No note ' + id);
d.notes.splice(d.notes.indexOf(n), 1);
const f = (N.files || {})[id];
if (f) { URL.revokeObjectURL(f.url); delete N.files[id]; }
if (N.heard) delete N.heard[id];
if (n.file && window.claude && window.claude.use) {
  const assets = await window.claude.use('assets').catch(() => null);
  if (assets) try { await assets.delete(n.file); } catch (e) {}
}
""")

NOTES_PICK = sig("pick", ["id"], r"""
// The box of a note: checked notes go with Send selected. (The page keeps which, not the state.)
const R = os.refs['notes-view'];
R.picked = R.picked.includes(id) ? R.picked.filter(x => x !== id) : R.picked.concat(id);
return { picked: R.picked };
""")

NOTES_SHOW_STATE = sig("showState", ["id"], r"""
// Show state: the ui-data of the note's view shows under the note; again hides it. (The page keeps which, not the state.)
const R = os.refs['notes-view'];
R.shown = R.shown.includes(id) ? R.shown.filter(x => x !== id) : R.shown.concat(id);
return { shown: R.shown };
""")

NOTES_CLOSE = sig("close", [], r"""
await ctx.call('extension.functions.unmount', { view_path: 'extension.views.notes-view' });
""")

REC_CLEAR = sig("clear", [], r"""
// Closes the card of the last recording, and forgets the recording.
const d = os.get('extension.views.recorder-view.ui-data'), R = os.refs['recorder-view'] || {};
if (R.url) URL.revokeObjectURL(R.url);
R.url = R.blob = R.selectedEl = null;
d.result = null;
d.selections = [];
d.selected = '';
d.error = '';
""")

HEADER_INIT = sig("init", [], r"""
// Views that ui-data says are open are opened again.
const d = os.get('extension.views.header-view.ui-data');
// All the views show at the width of the device in ui-data: Mobile 390 px, Tablet 820 px, Desktop the full page.
const root = document.getElementById('index-view');
if (d.device && d.device !== 'desktop') root.dataset.device = d.device;
else delete root.dataset.device;
// While the device menu is open, a click out of it or Escape closes it. A new init takes the place of the old listeners.
const old = os.refs['header-view'];
if (old && old.off) old.off();
const close = () => os.call('local.toggle-device-menu', { open: false }, 'extension.views.header-view').catch(console.error);
const onDown = e => { if (d.device_open && !e.target.closest('.dev-pick')) close(); };
const onKey = e => { if (d.device_open && e.key === 'Escape') close(); };
document.addEventListener('pointerdown', onDown, true);
document.addEventListener('keydown', onKey);
os.refs['header-view'] = { off: () => { document.removeEventListener('pointerdown', onDown, true); document.removeEventListener('keydown', onKey); } };
// After the Reload button of the timeline, the state view opens again with the timeline.
let replay = location.hash === '#timeline-replay';
try { replay = replay || sessionStorage.getItem('agent-os.timeline-replay') === '1'; } catch (e) {}
if (replay) { d.state_open = true; os.get('extension.views.state-view.ui-data').timeline_open = true; }
// (one main view at a time: the state view, when both say open)
if (d.docs_open && d.state_open) d.docs_open = false;
if (d.docs_open && !os.mounted('extension.views.docs-view')) await ctx.call('extension.functions.render', { view_path: 'extension.views.docs-view' });
if (d.state_open && !os.mounted('extension.views.state-view')) await ctx.call('extension.functions.render', { view_path: 'extension.views.state-view' });
""")

HEADER_DEVICE_MENU = sig("toggleDeviceMenu", ["open"], r"""
// The Device button: the menu Mobile, Tablet, Desktop. open: true or false; no open: the other.
const d = os.get('extension.views.header-view.ui-data');
const next = typeof open === 'boolean' ? open : !d.device_open;
if (next === d.device_open) return;
d.device_open = next;
await ctx.call('extension.functions.render', { view_path: 'extension.views.header-view' });
""")

HEADER_SET_DEVICE = sig("setDevice", ["device"], r"""
// A device of the menu: all the views show at its width (local.init of header-view sets it on index-view).
if (!['mobile', 'tablet', 'desktop'].includes(device)) throw new Error('device is mobile, tablet or desktop, not ' + device);
const d = os.get('extension.views.header-view.ui-data');
d.device = device;
d.device_open = false;
await ctx.call('extension.functions.render', { view_path: 'extension.views.header-view' });
return { device };
""")

INDEX_INIT = sig("init", [], r"""
const view = await ctx.call('extension.functions.get-state', { path: 'extension.views.header-view' });
if (!view) throw new Error('No header-view in the state');
await ctx.call('extension.functions.render', { view_path: 'extension.views.header-view' });
await ctx.call('extension.functions.render', { view_path: 'extension.views.recorder-view' });
""")

DOCS_DRAW = r"""
// Draw the view again from ui-data: its root element takes the place of the one on the page.
const t = document.createElement('template');
t.innerHTML = os.template(os.get('extension.views.docs-view.html'), d);
const el = t.content.firstElementChild;
ctx.root.replaceWith(el);
os.bind(el, 'extension.views.docs-view');"""

DOCS_INIT = sig("init", [], r"""
// The list comes from the docs folder of the agent; the first doc opens if none is selected.
const d = os.get('extension.views.docs-view.ui-data'), folder = os.get('agents.agent-oss.files.docs') || {};
d.docs = Object.keys(folder);
if (!d.docs.includes(d.selected)) d.selected = d.docs[0] || '';
d.content = folder[d.selected] || '';""" + DOCS_DRAW)

OPEN_DOC = sig("openDoc", ["name"], r"""
const d = os.get('extension.views.docs-view.ui-data'), folder = os.get('agents.agent-oss.files.docs') || {};
if (!(name in folder)) throw new Error('No doc ' + name);
d.selected = name;
d.content = folder[name];""" + DOCS_DRAW)

GET_STATE = sig("getState", ["path"], r"""
// The JSON state: all of it, or the part at path.
const value = path ? os.get(path) : os.get();
if (value === undefined) throw new Error('Nothing at ' + path);
return os.clone(value);
""")

RENDER = sig("render", ["view_path"], r"""
const view = os.get(view_path);
if (!view) throw new Error('No view at ' + view_path);
// A view renders into the element whose id is its name.
const id = view_path.split('.').pop();
const root = document.getElementById(id);
if (!root) throw new Error('No element #' + id);
// Its html has one root element with the same id. That element takes the place of the empty one.
const t = document.createElement('template');
t.innerHTML = os.template(view.html || '', view['ui-data'] || {});
const el = t.content.firstElementChild;
if (!el || el.id !== id) throw new Error('The html of ' + id + ' must start with one element with id="' + id + '"');
root.replaceWith(el);
os.bind(el, view_path);
os.setMounted(view_path, true);
if (view.functions && view.functions['local.init']) await os.call('local.init', {}, view_path, ctx.id);
""")

UNMOUNT = sig("unmount", ["view_path"], r"""
const root = document.getElementById(view_path.split('.').pop());
root.innerHTML = '';
root.hidden = true;
os.setMounted(view_path, false);
""")

exec(open(REPO + '/gen/docs_part.py').read())           # DOCS: the docs folder in agents (shows the code above)

def V(path): return {"view_path": path}
# The docs are files of the repo too.
os.makedirs(REPO + '/docs', exist_ok=True)
for name, text in DOCS.items():
    open(REPO + '/docs/' + name, 'w').write(text)
def TREE(path):
    # The files of main, as a folder tree: a folder is an object, a file is its text. state.json is the state
    # itself, so it is not in it; a folder that holds only .gitkeep is an empty object.
    out = {}
    names = sorted(os.listdir(path), key=lambda n: (not n.startswith('.'), n.lower()))
    if os.path.basename(path) == 'docs': names = [n for n in DOCS] + [n for n in names if n not in DOCS]
    for n in names:
        full = path + '/' + n
        if n in ('.git', '.gitkeep', 'node_modules') or full == REPO + '/state.json': continue
        out[n] = TREE(full) if os.path.isdir(full) else open(full).read()
    return out
render_sv = {"extension.functions.render": V(SV)}
# Tests of the timeline start with no block chosen.
RV = "extension.views.recorder-view"
RP = RV + ".ui-data"
render_rv = {"extension.functions.render": V(RV)}
render_nv = {"extension.functions.render": V(NV)}
FRESH = {"extension.functions.render": V(TV), TV + ".functions.local.select": {"id": None}}
render_dv = {"extension.functions.render": V(DV)}
uses_core = {"state-core": CORE}
MAY = "may change"
DP = DV + ".ui-data"

CM_FILES = {"codemirror.js": "CodeMirror 5.65.16, the code editor: the state view and the code boxes of the timeline.",
  "javascript.js": "CodeMirror: colors for js and json.", "xml.js": "CodeMirror: colors for xml, used by htmlmixed.",
  "css.js": "CodeMirror: colors for css, used by htmlmixed.", "htmlmixed.js": "CodeMirror: colors for html (the html of the views).",
  "markdown.js": "CodeMirror: colors for md, in the preview of a long text.",
  "foldcode.js": "CodeMirror: folds objects in the state view.", "foldgutter.js": "CodeMirror: the fold arrows next to the line numbers.",
  "brace-fold.js": "CodeMirror: finds where an object starts and ends, for folding.", "matchbrackets.js": "CodeMirror: marks the bracket that matches.",
  "closebrackets.js": "CodeMirror: adds the closing bracket when you type one."}
def REQ(url, used_for): return {"url": url, "used_for": used_for, "expected": True}
NETWORK = {
  "html": {"index.html": REQ("index.html", "The page itself: a title, a small base style, an empty <div id=\"index-view\"> and 2 scripts. The second script is the runtime.")},
  "scripts": {"state-core.js": REQ("state-core.js", "The library of the runtime: paths in the state, templates, diffs, versions (commits) and the call tracker.")},
  "claude.ai": {
    "db.js": REQ("/_runtime/db.js", "The database of an artifact page: window.claude.use('db'). The versions and the call logs are in it."),
    "user.js": REQ("/_runtime/user.js", "From its name: who views the page."),
    "permissions.js": REQ("/_runtime/permissions.js", "From its name: what the page may do (its capabilities)."),
    "_comments.js": REQ("/_runtime/_comments.js", "From its name: the comments on the page."),
    "_translate.js": REQ("/_runtime/_translate.js", "From its name: translation of the page."),
    "_transforms.js": REQ("/_runtime/_transforms.js", "From its name: changes that claude.ai makes to the page when it loads.")},
  "api": {
    "connect to the database": {"what": "window.claude.use('db')", "used_for": "Gets the database of this page from claude.ai. The versions and the call logs are in it.", "expected": True},
    "read the versions": {"what": "db.collection('commits').orderBy('n').get()", "used_for": "Reads all saved versions when the page opens. The newest is the live state.", "expected": True},
    "follow new versions": {"what": "db.collection('commits').orderBy('n').onSnapshot(...)", "used_for": "Gets a new version as soon as it is saved, so an open page runs it.", "expected": True},
    "save the call log": {"what": "db.doc('calls/<session>').set(log)", "used_for": "Saves the newest 400 calls of this page load, 1.2 s after a call.", "expected": True},
    "save a version": {"what": "db.collection('commits').doc('cNNNNNN').set(version)", "used_for": "Saves the state as a new version when you click Save in the state view.", "expected": True},
    "save a version file": {"what": "assets.upload(state)", "used_for": "Saves the state of a new version as a file of the page when it is too big for one database document (256 KB). The version gets state_file, the id of the file.", "expected": True}},
  "state": {"state.json": REQ("state.json", "The first version of the state. The page uses it only when the database has no versions."),
            "version files": REQ("/_blob/", "The state of each version that has state_file: a file of the page, too big for one database document.")},
  "file code": {"index.html": REQ("index.html", "The timeline downloads index.html as text to show its code."),
                "state-core.js": REQ("state-core.js", "The timeline downloads state-core.js as text to show its code.")},
  "packages": dict([(p.split("/")[-1], REQ(CM + p, CM_FILES[p.split("/")[-1]])) for p in CM_SCRIPTS]
    + [("beautify.js", REQ(JSB + "beautify.js", "js-beautify 1.15.1: formats js in the code boxes of the timeline.")),
       ("beautify-css.js", REQ(JSB + "beautify-css.js", "js-beautify: formats css inside html.")),
       ("beautify-html.js", REQ(JSB + "beautify-html.js", "js-beautify: formats html in the code boxes of the timeline."))]),
  "styles": {"fonts.googleapis.com/css2": REQ("https://fonts.googleapis.com/css2", "The fonts of the page (Inter, Literata, JetBrains Mono). The @import in the style of index-view asks for it."),
             "font files (fonts.gstatic.com)": REQ("https://fonts.gstatic.com/", "The font files that css2 asks for.")}
}

state = {
  "agents": {
    "agent-oss": {
      "connection": {},
      "files": TREE(REPO)
    }
  },
  "network": NETWORK,
  "environment": {"browser": {}, "browser data": {}, "browser api": {}, "document": {}, "window": {}, "event listeners": {}, "timers": {}, "observers": {}, "connections": [], "devices": {}, "permissions": {}, "subscriptions": {}, "background services": {}, "other": {}},
  "extension": {
    "views": {
      "index-view": {
        "html": index_html,
        "ui-data": {},
        "functions": {
          "local.init": fn(
            "Runs when the page loads, after index-view is rendered: reads header-view and renders it, then renders the record button (recorder-view).",
            code=INDEX_INIT,
            calls={
              "extension.functions.get-state": {"input": {"path": HV}, "output": None},
              "extension.functions.render": {"input": V(HV), "output": None}
            },
            tests={"renders the header": {"input": {}, "expect": {"dom": ["#header-view #docs-button", "#header-view #state-button", "#recorder-view #rec-button"]}}}
          )
        }
      },
      "header-view": {
        "html": header_html,
        "ui-data": {"docs_open": False, "state_open": False, "device": "desktop", "device_open": False},
        "functions": {
          "local.init": fn("Runs after header-view is rendered: shows all the views at the width of ui-data.device, and opens docs-view and state-view again when ui-data says they are open. After the Reload button of the timeline, it opens the state view with the timeline.",
                           code=HEADER_INIT, expected={HV + ".ui-data.state_open": MAY, HV + ".ui-data.docs_open": MAY, P + ".timeline_open": MAY},
                           calls={"extension.functions.render": {"input": V(SV), "output": None}}),
          "local.toggle-device-menu": fn("The Device button: opens the menu Mobile, Tablet, Desktop, or closes it. A click out of the menu, or Escape, closes it.",
                           code=HEADER_DEVICE_MENU, input_={"open": True}, expected={HV + ".ui-data.device_open": MAY},
                           calls={"extension.functions.render": {"input": V(HV), "output": None}},
                           tests={"opens, then closes": {"before": {"local.toggle-device-menu": {"open": True}}, "input": {"open": False},
                                                         "expect": {"state": {HV + ".ui-data.device_open": False}, "dom-absent": ["#device-menu"]}}}),
          "local.set-device": fn("A device of the Device menu: all the views show at its width. Mobile is 390 px, Tablet is 820 px, Desktop is the full page.",
                           code=HEADER_SET_DEVICE, input_={"device": "mobile"}, expected={HV + ".ui-data.device": "input.device", HV + ".ui-data.device_open": MAY},
                           calls={"extension.functions.render": {"input": V(HV), "output": None}},
                           tests={"shows tablet": {"input": {"device": "tablet"},
                                                   "expect": {"state": {HV + ".ui-data.device": "tablet"}, "dom": ["#index-view[data-device=\"tablet\"]"]}},
                                  "shows mobile, then desktop": {"before": {"local.set-device": {"device": "mobile"}}, "input": {"device": "desktop"},
                                                                 "expect": {"state": {HV + ".ui-data.device": "desktop"}, "dom-absent": ["#index-view[data-device]", "#device-menu"]}}}),
          "local.open.docs-view": fn(
            "The Docs button: renders docs-view, or closes it when it is open, and keeps ui-data.docs_open in step. One main view at a time: the state view or Notes closes.",
            code=open_view("docs-view", "docs_open"),
            calls={"extension.functions.render": {"input": V(DV), "output": None}, "extension.functions.unmount": {"input": V(DV), "output": None}},
            expected={HV + ".ui-data.docs_open": MAY, HV + ".ui-data.state_open": MAY},
            tests={
              "opens the docs": {"before": {"extension.functions.unmount": V(DV)}, "input": {},
                                 "expect": {"state": {HV + ".ui-data.docs_open": True}, "dom": ["#docs-view .doc-link", "#docs-button[aria-pressed=\"true\"]"]}},
              "closes them when open": {"before": render_dv, "input": {},
                                        "expect": {"state": {HV + ".ui-data.docs_open": False}, "dom-absent": ["#docs-view .doc-link"]}}
            }),
          "local.open.state-view": fn(
            "The State button: renders state-view, or closes it when it is open, and keeps ui-data.state_open in step. One main view at a time: the docs or Notes close.",
            code=open_view("state-view", "state_open"),
            calls={"extension.functions.render": {"input": V(SV), "output": None}, "extension.functions.unmount": {"input": V(SV), "output": None}},
            expected={HV + ".ui-data.state_open": MAY, HV + ".ui-data.docs_open": MAY},
            tests={
              "opens the state view": {"before": {"extension.functions.unmount": V(SV)}, "input": {},
                                       "expect": {"state": {HV + ".ui-data.state_open": True}, "dom": ["#state-view .CodeMirror", "#state-button[aria-pressed=\"true\"]"]}},
              "closes it when open": {"before": render_sv, "input": {},
                                      "expect": {"state": {HV + ".ui-data.state_open": False}, "dom-absent": ["#state-view .CodeMirror"]}}
            })
        }
      },
      "docs-view": {
        "html": docs_html,
        "ui-data": {"path": "agents/agent-oss/files/docs", "docs": [], "selected": "", "content": ""},
        "functions": {
          "local.init": fn("Runs after docs-view is rendered: lists the docs folder and shows the selected doc.",
                           code=DOCS_INIT, expected={DP + ".docs": MAY, DP + ".selected": MAY, DP + ".content": MAY},
                           tests={"lists the docs": {"before": render_dv, "input": {}, "expect": {"dom": ["#docs-view .doc-link[aria-current=\"true\"]", "#docs-view .doc h2"]}}}),
          "local.close": fn("The close button of the docs: closes docs-view. The Docs button of the header is not pressed.",
                            code=close_view("docs-view", "docs_open"), expected={HV + ".ui-data.docs_open": False},
                            calls={"extension.functions.unmount": {"input": V(DV), "output": None}, "extension.functions.render": {"input": V(HV), "output": None}},
                            tests={"closes the docs": {"before": render_dv, "input": {}, "expect": {"state": {HV + ".ui-data.docs_open": False}, "dom-absent": ["#docs-view .doc-link"]}}}),
          "local.open-doc": fn("Shows one doc of the folder.", code=OPEN_DOC, input_={"name": "render-steps.md"},
                               expected={DP + ".selected": "input.name", DP + ".content": MAY},
                               tests={"opens render-steps.md": {"before": render_dv, "input": {"name": "render-steps.md"},
                                                                "expect": {"state": {DP + ".selected": "render-steps.md"}, "dom": ["#docs-view .doc .step", "#docs-view .doc pre.code"]}},
                                      "shows the diagram of how-it-works.md": {"before": render_dv, "input": {"name": "how-it-works.md"},
                                                                "expect": {"dom": ["#docs-view .doc .diagram svg"]}}})
        }
      },
      "timeline-view": {
        "html": timeline_html,
        "ui-data": {"selected": None, "playing": False, "show": "all", "flows_open": False,
                    "flows": [{"name": "First enter", "steps": ["network", "runtime", "loadState", "extension.functions.render"]}]},
        "functions": {
          "local.init": fn("Runs after timeline-view is rendered (the state view renders it): draws the timeline now and after every call. After the Restart button, it shows the last AI run notification.",
                           code=TL_INIT, calls={"local.refresh": {"input": {"after": "local.init"}, "output": None},
                                                "local.select": {"input": {"id": None}, "output": None}},
                           tests={"draws the blocks": {"before": {"extension.functions.render": V(TV)}, "input": {},
                                                       "expect": {"dom": ["#tl-strip .tl-step.fixed"]}}}),
          "local.refresh": fn("Draws the timeline from the runtime's call log: the page opening, index.html, then every call that nothing else called, as blocks in a row. What you do in the state view and the timeline is a block only when Track state is on. The last agent run stays at the left and the newest block at the right when the row scrolls. It shows only when the Timeline button of the state view is on. It keeps the chosen block for the state view, with how to draw its changes and its details. Runs after every call; after is the call that ran.",
                              code=TL_REFRESH, input_={"after": "local.step"},
                              tests={"draws the blocks": {"before": {"extension.functions.render": V(TV)}, "input": {"after": "test"},
                                                          "expect": {"dom": ["#tl-strip .tl-step .tl-kind", "#tl-pos"]}}}),
          "local.select": fn("Chooses a block: the state view shows it (its version, its changes, its details). It stops the replay. id null chooses no block: the state view shows the last agent run.",
                             code=TL_SELECT, input_={"id": "open"}, expected={TV + ".ui-data.selected": MAY, TV + ".ui-data.playing": MAY},
                             tests={"chooses block 2": {"before": FRESH, "input": {"id": "runtime"},
                                                         "expect": {"state": {TV + ".ui-data.selected": "runtime"}, "dom": ["#tl-strip .tl-step.on.fixed"]}},
                                    "chooses no block": {"before": dict(FRESH, **{"local.select": {"id": "open"}}), "input": {"id": None},
                                                         "expect": {"state": {TV + ".ui-data.selected": None}, "dom": ["#tl-strip .tl-step.on"]}}}),
          "local.next": fn("Moves delta blocks back (-1) or forward (1). The replay calls it with 1 and stops at the block that was the last when it started.",
                           code=TL_NEXT, input_={"delta": 1}, expected={TV + ".ui-data.selected": MAY, TV + ".ui-data.playing": MAY},
                           tests={"goes to the second block": {"before": dict(FRESH, **{"local.select": {"id": "open"}}), "input": {"delta": 1},
                                                               "expect": {"state": {TV + ".ui-data.selected": "runtime"}}}}),
          "local.reload": fn("The Restart button: reloads the page, so the history starts again. Then the timeline opens on the last AI run notification. It stops when the state has unsaved changes.",
                             code=TL_RELOAD),
          "local.show": fn("The AI runs and UI buttons: only runs shows only the AI run blocks, only ui shows only the other blocks. A click on the pressed button shows all the blocks again.",
                           code=TL_SHOW, input_={"only": "runs"}, expected={TV + ".ui-data.show": MAY, TV + ".ui-data.selected": MAY, TV + ".ui-data.playing": MAY},
                           tests={"shows only the UI blocks": {"before": {"extension.functions.render": V(TV)}, "input": {"only": "ui"},
                                                               "expect": {"state": {TV + ".ui-data.show": "ui"}, "dom": ["#tl-ui[aria-pressed=\"true\"]", "#tl-strip .tl-step.ui"], "dom-absent": ["#tl-strip .tl-step.ai"]}},
                                  "shows all again": {"before": {"extension.functions.render": V(TV), "local.show": {"only": "runs"}}, "input": {"only": "runs"},
                                                      "expect": {"state": {TV + ".ui-data.show": "all"}, "dom": ["#tl-runs[aria-pressed=\"false\"]", "#tl-strip .tl-step.ui"]}}}),
          "local.close": fn("The close button: closes the timeline. The Timeline button of the state view shows it again.",
                            code=TL_CLOSE, expected={P + ".timeline_open": MAY},
                            tests={"closes the timeline": {"before": {"extension.functions.render": V(TV)}, "input": {},
                                                           "expect": {"state": {P + ".timeline_open": False}}}}),
          "local.toggle-flows": fn("The Flows button: opens or closes the list of saved flows.",
                                   code=TL_FLOWS, expected={TV + ".ui-data.flows_open": "toggles"},
                                   tests={"opens the list": {"before": {"extension.functions.render": V(TV), "local.toggle-flows": {}}, "input": {},
                                                             "expect": {"dom": ["#tl-flows[aria-pressed]"]}}}),
          "local.play-flow": fn("Plays a saved flow of ui-data.flows: its blocks, one after the other, every 1.6 seconds. Each name in the flow is the first block with that name after the block before it. First enter is the page opening: its first 4 blocks.",
                                code=TL_PLAY_FLOW, input_={"name": "First enter"},
                                expected={TV + ".ui-data.selected": MAY, TV + ".ui-data.playing": MAY, TV + ".ui-data.flows_open": MAY},
                                tests={"plays First enter": {"before": FRESH, "input": {"name": "First enter"},
                                                             "expect": {"output": {"blocks": 4}, "state": {TV + ".ui-data.selected": "open", TV + ".ui-data.playing": True, TV + ".ui-data.flows_open": False}, "dom": ["#tl-strip .tl-step.on"]}}}),
          "local.play": fn("Starts or stops the replay: the next block shows every 1.6 seconds, up to the newest block. With Track state on, it stops at the block that was the newest when it started. From the last block, it starts again at the first. A paused flow goes on.",
                           code=TL_PLAY, expected={TV + ".ui-data.playing": "toggles", TV + ".ui-data.selected": MAY},
                           tests={"starts and stops": {"before": dict(FRESH, **{"local.select": {"id": "open"}, "local.play": {}}), "input": {},
                                                       "expect": {"state": {TV + ".ui-data.playing": False}, "dom": ["#tl-play[aria-pressed=\"false\"]"]}}})
        }
      },
      "state-view": {
        "html": state_html,
        "ui-data": {
          "path": "extension/views/state-view",
          "current_state_version": 1,
          "position": 0,
          "version": "v1",
          "version_ago": "",
          "changes": False,
          "details": False,
          "timeline_open": False,
          "track_state": False,
          "unsaved": False,
          "error": "",
          "fixable": False,
          "viewer_path": "",
          "md_theme": "reader",
          "filter": "",
          "filter_kind": "all",
          "show_empty": True
        },
        "functions": {
          "local.init": fn(
            "Runs after state-view is rendered: starts the editor at the newest version, renders the timeline (hidden until the Timeline button) and watches the state (local.refresh runs after each call).",
            code=INIT, calls={"extension.functions.render": {"input": V(TV), "output": None}},
            imports={"codemirror": [CM + f for f in CM_SCRIPTS],
                     "state-core": CORE_SRC},
            expected={P: MAY},
            tests={"starts at the newest version": {"before": render_sv, "input": {}, "expect": {"state": {P + ".unsaved": False, P + ".changes": False, P + ".viewer_path": ""}, "dom": ["#state-view .CodeMirror"]}}}
          ),
          "local.refresh": fn("Draws the view from ui-data and the state: the bar, the chosen block of the timeline (it goes to the version of the block), and what shows: the editor (draft, live state or an older version), or the pane with Details of the block, its Changes, or one kind as a tree. Runs after every call; after is the call that ran.",
                              code=REFRESH, imports=uses_core, input_={"after": "local.step"},
                              expected={P + ".current_state_version": MAY, P + ".version": MAY, P + ".version_ago": MAY, P + ".position": MAY},
                              tests={"names the version on screen": {"before": render_sv, "input": {"after": "test"}, "expect": {"dom": ["#state-view .sv-foot #pos b"]}}}),
          "local.edit": fn("Runs as you type: keeps the unsaved draft and checks the JSON.",
                           code=EDIT, imports=uses_core,
                           expected={P + ".unsaved": MAY, P + ".position": MAY, P + ".error": MAY, P + ".fixable": MAY},
                           tests={"nothing typed, nothing unsaved": {"before": render_sv, "input": {}, "expect": {"state": {P + ".unsaved": False, P + ".error": ""}}}}),
          "local.step": fn("Older and Newer: moves delta versions back (-1) or forward (1) in the history, and leaves the chosen block (Changes shows the changes of the version). Also runs on the arrow keys.",
                           code=STEP, input_={"delta": -1}, expected={P + ".position": MAY},
                           tests={"stops at the newest version": {"before": render_sv, "input": {"delta": 1}, "expect": {"state": {P + ".unsaved": False}, "dom": ["#newer[disabled]"]}}}),
          "local.toggle-changes": fn("Changes: shows only what the chosen block changed (or the version on screen, after Older or Newer): added green, updated yellow, deleted red, with a table of what changed. One kind shows as a tree. It leaves Details.",
                                     code=TOGGLE, expected={P + ".changes": "toggles", P + ".details": MAY},
                                     tests={"turns the changes view on": {"before": dict(render_sv, **{"local.filter-kind": {"kind": "all"}}), "input": {}, "expect": {"state": {P + ".changes": True}, "dom": ["#changes[aria-pressed=\"true\"]", "#tl-detail:not([hidden]) .st-legend, #tl-detail:not([hidden]) .tl-text"]}}}),
          "local.toggle-details": fn("Details: shows what happens inside the chosen block of the timeline (its parts, its calls, an agent run in lanes).",
                                     code=TOGGLE_DETAILS, expected={P + ".details": "toggles"},
                                     tests={"shows the details": {"before": dict(render_sv, **{TV + ".functions.local.select": {"id": "open"}}), "input": {},
                                                                  "expect": {"state": {P + ".details": True}, "dom": ["#details[aria-pressed=\"true\"]", "#tl-detail .tl-netenv .tl-panel"]}}}),
          "local.close": fn("The close button of the state view: closes state-view. The State button of the header is not pressed.",
                            code=close_view("state-view", "state_open"), expected={HV + ".ui-data.state_open": False},
                            calls={"extension.functions.unmount": {"input": V(SV), "output": None}, "extension.functions.render": {"input": V(HV), "output": None}},
                            tests={"closes the state view": {"before": render_sv, "input": {}, "expect": {"state": {HV + ".ui-data.state_open": False}, "dom-absent": ["#state-view .CodeMirror"]}}}),
          "local.toggle-timeline": fn("The Timeline button: shows or hides the timeline above the header. Hidden, the timeline still keeps its blocks for the state view.",
                                      code=TOGGLE_TIMELINE, expected={P + ".timeline_open": "toggles"},
                                      calls={"extension.functions.render": {"input": V(TV), "output": None}},
                                      tests={"shows the timeline": {"before": render_sv, "input": {},
                                                                    "expect": {"dom": ["#timeline-button[aria-pressed]", "#timeline-view .tl-step"]}}}),
          "local.toggle-tracking": fn("The Track state box: turns on or off that what you do in the state view and the timeline (clicks, the replay) is added as blocks of the timeline.",
                                      code=TOGGLE_TRACK, expected={P + ".track_state": "toggles"},
                                      tests={"tracks, then stops": {"before": dict(render_sv, **{"local.toggle-tracking": {}}), "input": {},
                                                                    "expect": {"state": {P + ".track_state": False}, "dom": ["#sv-track:not(:checked)"]}}}),
          "local.collapse-all": fn("Folds every object in the editor.", code=COLLAPSE,
                                   tests={"folds the editor": {"before": dict(render_sv, **{"local.filter-kind": {"kind": "all"}}), "input": {},
                                                               "expect": {"dom": [".CodeMirror-foldmarker"]}}}),
          "local.open-viewer": fn("Opens a long text in the viewer, where you can edit it. An md file shows as a document that you edit in place, with sections that fold. For html, the view runs on the right with a copy of the state: its buttons work, and its ui-data shows below it after each action.",
                                  code=OPEN_VIEWER, imports=uses_core, input_={"path": "extension/views/header-view/html"}, expected={P + ".viewer_path": "input.path"},
                                  tests={"opens header-view html": {"before": render_sv, "input": {"path": "extension/views/header-view/html"},
                                                                    "expect": {"state": {P + ".viewer_path": "extension/views/header-view/html"}, "dom": ["#sv-viewer:not([hidden]) #sv-viewer-view[srcdoc]", "#sv-viewer-code .CodeMirror"]}}}),
          "local.filter": fn("Shows only the entries whose path has the text, with the objects around them: in the editor the other lines fold into \"⋯ N lines\"; the trees and the table of the changes keep only those paths. Empty text shows all.",
                              code=FILTER, input_={"text": "header"}, expected={P + ".filter": "input.text"},
                              tests={"keeps header paths": {"before": render_sv, "input": {"text": "header-view"},
                                                            "expect": {"state": {P + ".filter": "header-view"}, "dom": ["#sv-editor .sv-hidden"]}}}),
          "local.filter-kind": fn("Shows only one kind: files, views, functions, network or environment, as a tree on the left and the chosen one on the right (File, View, Function, Request or Value; Pseudo code; Changes). all shows the editor. It leaves Details.",
                                   code=FILTER_KIND, input_={"kind": "functions"},
                                   expected={P + ".filter_kind": "input.kind", P + ".details": MAY},
                                   tests={"shows only functions": {"before": render_sv, "input": {"kind": "functions"},
                                                                   "expect": {"state": {P + ".filter_kind": "functions"}, "dom": ["#sv-switches [data-input*=\"functions\"][aria-pressed=\"true\"]", "#tl-detail .kv .kv-tree .kv-item"]}},
                                          "shows the files as a tree": {"before": dict(render_sv, **{"local.filter": {"text": ""}}), "input": {"kind": "files"},
                                                                        "expect": {"state": {P + ".filter_kind": "files"}, "dom": ["#tl-detail .kv .kv-tree summary", "#sv-editor[hidden]"]}}}),
          "local.toggle-empty": fn("Shows or hides the entries with an empty value: {}, [], \"\" or null (the Show empty box).",
                                   code=TOGGLE_EMPTY, expected={P + ".show_empty": "toggles"},
                                   tests={"hides empty values": {"before": render_sv, "input": {}, "expect": {"state": {P + ".show_empty": False}, "dom": ["#sv-empty:not(:checked)"]}}}),
          "local.set-md-theme": fn("Sets the theme that md files show in: reader (the default, for long reading), white, black, sepia, night or mono.",
                                   code=SET_MD_THEME, input_={"theme": "black"}, expected={P + ".md_theme": "input.theme"},
                                   tests={"switches to black": {"before": render_sv, "input": {"theme": "black"},
                                                                "expect": {"state": {P + ".md_theme": "black"}, "dom": ["#md-themes [data-md-theme=\"black\"][aria-pressed=\"true\"]", "#sv-viewer-doc[data-md-theme=\"black\"]"]}}}),
          "local.close-viewer": fn("Closes the viewer; edited html or code goes into the state editor as an unsaved change.",
                                   code=CLOSE_VIEWER, imports=uses_core,
                                   calls={"local.edit": {"input": {}, "output": None}},
                                   expected={P + ".viewer_path": ""},
                                   tests={"closes without changes": {"before": {"extension.functions.render": V(SV), "local.open-viewer": {"path": "extension/views/header-view/html"}}, "input": {},
                                                                     "expect": {"state": {P + ".viewer_path": "", P + ".unsaved": False}, "dom-absent": ["#sv-viewer:not([hidden])"]}}}),
          "local.save": fn("Saves the editor's text as a new version (fixing JSON slips first), flashes the editor border green, and renders the header from the new state. Returns the new version, what changed, and whether slips were fixed.",
                           code=SAVE, imports=uses_core,
                           calls={"extension.functions.render": {"input": V(HV), "output": None}},
                           expected={P + ".current_state_version": "changes", "*": MAY})
        }
      },
      "recorder-view": {
        "html": recorder_html,
        "ui-data": {"recording": "", "started_at": 0, "selected": "", "selections": [], "result": None, "error": "", "menu_open": False},
        "functions": {
          "local.init": fn("Runs after recorder-view is rendered: the record button (one click: audio, two clicks: the menu), the keys (Arrow Up two times: audio; Arrow Up and Arrow Down together: video), the timer in the header and the select mode.",
                           code=REC_INIT, calls={"local.refresh": {"input": {"after": "local.init"}, "output": None}},
                           tests={"draws the record button": {"before": render_rv, "input": {}, "expect": {"dom": ["#recorder-view #rec-button[aria-pressed=\"false\"]"]}}}),
          "local.refresh": fn("Draws the record button (a stop button while it records), the error and the card of the last recording from ui-data; the select mode is on while it records. Runs after every call.",
                              code=REC_REFRESH, input_={"after": "local.select"},
                              tests={"draws the button": {"before": render_rv, "input": {"after": "test"}, "expect": {"dom": ["#rec-button[aria-label=\"Record\"]"]}}}),
          "local.start": fn("Starts a recording: audio (the microphone) or video (a screen, a window or a tab, with sound). The button becomes a stop button, the timer shows in the header, and the select mode is on. With Transcription on (Settings of Notes), the browser turns what the microphone hears into text.",
                            code=REC_START, input_={"mode": "audio"}, expected={RP: MAY}),
          "local.stop": fn("Stops the recording. The card shows it, with the elements that you selected and Save file. The recording is also a new note of the Notes page.",
                           code=REC_STOP, expected={RP: MAY, NV + ".ui-data.notes": MAY},
                           tests={"does nothing when it does not record": {"before": render_rv, "input": {}, "expect": {"state": {RP + ".recording": ""}}}}),
          "local.select": fn("Select mode: keeps the path of the element that you clicked (its view, the elements down to it, and its block of the timeline), with the time in the recording.",
                             code=REC_SELECT, input_={"path": "extension.views.header-view › #docs-button"},
                             expected={RP + ".selected": "input.path", RP + ".selections": MAY},
                             tests={"keeps the path": {"before": render_rv, "input": {"path": "extension.views.header-view › #docs-button"},
                                                       "expect": {"state": {RP + ".selected": "extension.views.header-view › #docs-button"}}}}),
          "local.save": fn("Saves the last recording as a file (webm or mp4). On claude.ai, you confirm the download.", code=REC_SAVE),
          "local.toggle-menu": fn("Two clicks on the record button: opens the menu (1 Record audio, 2 Record video, 3 Notes). A click on the button or out of the menu, or Escape, closes it.",
                                  code=REC_TOGGLE_MENU, input_={"open": True}, expected={RP + ".menu_open": MAY},
                                  tests={"opens, then closes": {"before": dict(render_rv, **{"local.toggle-menu": {"open": True}}), "input": {"open": False},
                                                                "expect": {"state": {RP + ".menu_open": False}, "dom-absent": ["#rec-menu"]}}}),
          "local.open-notes": fn("Notes in the menu of the record button, or hold the record button 4 seconds: opens the Notes page.",
                                 code=REC_OPEN_NOTES, expected={RP + ".menu_open": MAY, HV + ".ui-data.docs_open": MAY, HV + ".ui-data.state_open": MAY}, calls={"extension.functions.render": {"input": V(NV), "output": None}},
                                 tests={"opens Notes": {"before": render_rv, "input": {}, "expect": {"dom": ["#notes-view .notes-bar"]}}}),
          "local.clear": fn("Closes the card of the last recording, and forgets the recording.",
                            code=REC_CLEAR, expected={RP: MAY},
                            tests={"closes the card": {"before": render_rv, "input": {}, "expect": {"state": {RP + ".result": None}, "dom-absent": ["#rec-card"]}}})
        }
      },
      "notes-view": {
        "html": notes_html,
        "ui-data": {"notes": [], "settings": {"transcribe": "browser", "lang": "", "new_session_task": ""}, "settings_open": False, "message": ""},
        "functions": {
          "local.init": fn("Runs after notes-view is rendered: Add note, the text of a note and Settings send what you type; the page draws again after each call.",
                           code=NOTES_INIT, calls={"local.refresh": {"input": {"after": "local.init"}, "output": None}},
                           tests={"draws the Notes page": {"before": render_nv, "input": {}, "expect": {"dom": ["#notes-view #notes-add", "#notes-view #notes-send-selected[disabled]"]}}}),
          "local.refresh": fn("Draws the notes from ui-data: a recording plays in its note (or its text shows), Show state shows the ui-data of the note's view. Runs after every call, but not while you type the text of a note.",
                              code=NOTES_REFRESH, input_={"after": "local.pick"}),
          "local.toggle-settings": fn("The Settings button: shows or hides the settings of transcription (Browser, the default, or Off; the language).",
                                      code=NOTES_TOGGLE_SETTINGS, expected={NV + ".ui-data.settings_open": "toggles"},
                                      tests={"opens, then closes": {"before": dict(render_nv, **{"local.toggle-settings": {}}), "input": {},
                                                                    "expect": {"state": {NV + ".ui-data.settings_open": False}, "dom-absent": ["#notes-settings"]}}}),
          "local.set-settings": fn("Changes the settings: transcribe (browser or off), lang (empty: the language of the browser) and new_session_task (the scheduled task of Send now new session).",
                                   code=NOTES_SET_SETTINGS, input_={"transcribe": "browser"}, expected={NV + ".ui-data.settings": MAY},
                                   tests={"keeps browser": {"before": render_nv, "input": {"transcribe": "browser"}, "expect": {"state": {NV + ".ui-data.settings.transcribe": "browser"}}}}),
          "local.add-text": fn("Add note: a note that you write, with the view that is open under the Notes page.",
                               code=NOTES_ADD_TEXT, input_={"text": "The Save button is too far."}, expected={NV + ".ui-data.notes": MAY, NV + ".ui-data.message": MAY}),
          "local.edit": fn("Keeps the text of a note as you change it.", code=NOTES_EDIT, input_={"id": "n1", "text": "A note"}, expected={NV + ".ui-data.notes": MAY}),
          "local.transcribe": fn("Transcribe: the text that the browser heard while it recorded goes into the note; you can change it. When there is no text, a message tells why.",
                                 code=NOTES_TRANSCRIBE, input_={"id": "n1"}, expected={NV + ".ui-data.notes": MAY, NV + ".ui-data.message": MAY}),
          "local.send": fn("Send now: the notes go to Claude in this Claude session, as a comment of the page sent to Claude. Send now new session (new_session: true): they start a new Claude Code session, through the task in settings.new_session_task. Send selected sends the checked notes.",
                           code=NOTES_SEND, input_={"ids": ["n1"]}, expected={NV + ".ui-data.message": MAY}),
          "local.delete": fn("Delete: the note goes, with its recording.", code=NOTES_DELETE, input_={"id": "n1"}, expected={NV + ".ui-data.notes": MAY}),
          "local.pick": fn("The box of a note: checks it for Send selected, or unchecks it.", code=NOTES_PICK, input_={"id": "n1"}),
          "local.show-state": fn("Show state: shows the ui-data of the note's view under the note; again hides it.", code=NOTES_SHOW_STATE, input_={"id": "n1"}),
          "local.close": fn("The close button: closes the Notes page.",
                            code=NOTES_CLOSE, calls={"extension.functions.unmount": {"input": V(NV), "output": None}},
                            tests={"closes": {"before": render_nv, "input": {}, "expect": {"dom-absent": ["#notes-view .notes-bar"]}}})
        }
      }
    },
    "functions": {
      "get-state": fn("Returns the JSON state: all of it, or the part at path (for example extension.views.header-view).",
                      code=GET_STATE, input_={"path": HV},
                      tests={"reads header-view": {"input": {"path": HV}, "expect": {"output-has": ["html", "ui-data", "functions"]}}}),
      "render": fn("Renders a view: puts its html (with its ui-data) into the element whose id is the view's name, wires its buttons, then runs its local.init.",
                   code=RENDER, input_=V(HV),
                   tests={"renders header-view": {"input": V(HV), "expect": {"dom": ["#header-view #state-button"]}}}),
      "unmount": fn("Empties a view's element and hides it.", code=UNMOUNT, input_=V(SV))
    },
    "data": {},
    "common_app_storage": {},
    "apps": {}
  }
}

# Each function has its pseudo code (gen/pseudo.py), after its docs.
exec(open(REPO + '/gen/pseudo.py').read())
def with_pseudo(fns, prefix):
    for name in list(fns):
        key = prefix + name
        assert key in PSEUDO, 'No pseudo code for ' + key
        f = fns[name]
        fns[name] = {k2: v2 for k, v in f.items() for k2, v2 in ([(k, v), ('pseudo', PSEUDO[key])] if k == 'docs' else [(k, v)])}
with_pseudo(state['extension']['functions'], '')
for vname, view in state['extension']['views'].items():
    with_pseudo(view.get('functions', {}), vname + '/')
assert len(PSEUDO) == len(state['extension']['functions']) + sum(len(v.get('functions', {})) for v in state['extension']['views'].values()), 'pseudo code for a function that is not there'

text = json.dumps(state, indent=2, ensure_ascii=False)
open(REPO + '/state.json', 'w').write(text + "\n")
print(len(text))
