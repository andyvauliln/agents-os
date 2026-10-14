# in-20261012-stage1: CLAUDE.md for the system, the docs at every level, stage one
- At: 2026-10-12 · Where: thread "Interactive file tree UI" · Source: chat
- Categories: docs, structure, ui, skills, process
- Summary: The owner wants Claude Code started in the system folder to know the project and its stage from CLAUDE.md; the docs at every level written fresh from all information; README also in ASD-STE100; metadata tabs only for metadata files that exist; prediction-market emptied to folders for stage two.

## Raw input
~~~text
Я хочу что бы в следующий раз на claude code in mine workspace i can run claude from system и он знал что это сейчас за проект, на какой он стадии, so basicly it should be it CLAUDE.md structure

Дальше он должен получить

Project Vision

Project Readme

System Vision

System Readme

File Tree (for now just simple paths without metdata later maybe we add additional data to it but for now just file tree wihtout metadata )

IDE (Need make full documentation about  this) 

Текущая стадия 

нам нужно закончить ide project, пройтись по всем файлам и папкам написать кастомные вью, сделать правильно всю метадату и закончить все все файлы по дукументации, докумнтация на уровне в целом, документация для system domain, документация на traiding general, мы пока не трогаем prediction market domain или что нибудь еще. "Давай пока даже удалим все файлы от туда оставим только папки, для стратегии и для предикшен это уже пойдет на вторую стадию"

CLAUDE.md relateded things

Rules from memory

What to do after every input or update

Should know when and how to update documentations files

so make sure all of this files exist, created even empty, keep them empty for now if you add

agent-oss/docs/(README.md, vision.md, reverse-prompt.md + they metadata)

agent-oss/docs/agents/system/docs(README.md, vision.md, reverse-prompt.md + they metadata)

agent-oss/docs/agents/system/CLAUDE.md + metadata

agent-oss/docs/agents/trading/docs/(README.md, vision.md, reverse-prompt.md + they metadata)

agent-oss/apps/docs/(README.md, vision.md, reverse-prompt.md + they 

agent-oss/apps/project-ide/docs/(README.md, vision.md, reverse-prompt.md + they metadata)

agent-oss/docs/agents/trading/prediction-markets/strategy-1/strategy-1.v1.Claude-Opus5.5/empty (delete everything  in prediction-market and leave only folders)

so also should be metadata for all files in a system created or empty, like at least index.md and metadata.json 

move by merging all another documentaion files to the vision folder, pick best from both version if exist, or you can move it to whatever you want i just need that after took all available for now information and fill of this all files i mention new updated version, for every type of the doc files and for writing metadata shoulв be use as a skill, we maybe already have them but revise them

also make one more skill and one more type of documentation document  ASD-STE100 it's also total how it works to compare later README.md where we do all overview and how it works with a  ASD-STE100 version , so make both versions for README, should be seen in a file tree tabs as well if available, also now i can see that in a tree file or folder tabs, i can see example and question tabs that suppose to be representation of metadata files but they not exist but i still have this tabs make sure that all files and folders medata files be real repressenation on a tabs, for now no need add it to every files just for main docs files and for .env i guess, later we add where it ll need more
~~~

## Answer
~~~text
Plan written: plans/2026-10-12-claude-md-stage-one.md. Built on the recommended defaults while the owner's answer on them is open (rebuild-prompt.md name, current prediction-market folder names, docs/ at the top).
Done 2026-10-12: agents/system/CLAUDE.md (stage one, reading order, rules, round, doc-update table); vision, README, README.asd and rebuild prompt written fresh at five levels (docs/, agents/system/docs/, agents/trading/docs/, apps/docs/, apps/project-IDE/docs/), each with How it works, Details, Example and Questions files; skills vision-doc, readme-doc, rebuild-prompt-doc, file-index revised, readme-asd-doc and claude-md-doc new; docs/file-tree.md built plain; every found file outside vision/ has its two metadata files; prediction-market emptied to folders (files moved to vision/archive/2026-10-12/prediction-market/, not deleted); older docs moved to vision/archive/2026-10-12/; page tabs show only for real files, new ASD-STE100 tab. Page v62, data v57.
~~~

## Processed into
- plans/2026-10-12-claude-md-stage-one.md (built on defaults)
- D-064
