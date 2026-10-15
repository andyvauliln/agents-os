# in-20261005-0710: What Example and How it works show for every file; wrapped lines in edit mode
- At: 2026-10-05T07:10:48Z · Where: thread "Interactive file tree UI" · Source: chat · Ref: cmsg_01Sk8xdkWKCz34CUCfVMyQbx1UC2sEV7ULXmq3YGpXQuBW
- Categories: ui, docs-knowledge
- Summary: Starting with vision.md, the owner asked that a file's Example show the structure of the file and what goes in each section; Questions and File stay as they are; How it works shows only simple, labelled answers for a newcomer (the responsible skill, how and when the file is updated, when AI uses or updates it, where it is mentioned, related knowledge). Long lines in edit mode should wrap to the screen. The rule goes where future files and the vision skill will use it.

## Raw input
~~~text
let's start from the vision, so Example should contain structure of the file and what should be in every section, question, file same, in how it works, i want to know only things like, for example? for this file responsible skill ..., how this file updated and when, when for example ai ll use it or update it, where is file mention, what knowledge also relates to this files etc, just name of section and easy understandable view on how it works if for example people first time see this project and what to know how it works here. Also when i do edit on a file and in edit mode i have long rows to the right which is hard to read can we make length of rows base on screen. And add this input where it should be for further file creation and for skill that responsible for managing and creating vision
~~~

## Processed into
- D-036 (decisions.md).
- `.claude/agents/knowledge-base-agent.md`: new section "How every file shows on the File Tree page" (Example = structure; How it works = What it is, Who looks after it, When and how it changes, Who uses it and when, Where it is mentioned, Related knowledge, Keep in mind; Questions and File unchanged; every doc skill gets an Outline and an "Its page on the File Tree" section).
- `.claude/skills/vision-doc/SKILL.md`: Chapters became the Outline (shown as the Example); new section "Its page on the File Tree"; steps refresh the panel.
- `.claude/skills/knowledge-summarise/SKILL.md`: the fixed-heading format (`sections`).
- vision.md's How it works written under the fixed headings; file-tree.md [2.2] made plain.
- Tools: build_map `--set` stores `sections`; enrich passes them and takes a doc's Example from its skill's Outline (DOC_SKILLS). Page v20: How it works shows only the headings, keep lines and the owner's own waiting messages and changes for files in the new format; Example renders the outline; the editor wraps long lines to the screen with a gutter that numbers each real line once.
