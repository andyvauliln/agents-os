# in-20261006-1729: views are custom interfaces per kind of file; changes as JSON; is schema.json part of the example?
- At: 2026-10-06T17:29:12Z · Where: thread "Interactive file tree UI" · Source: chat · Ref: thread cmsg_01Sk8xdkWKCz34CUCfVMyQbxP1hyoB8xVJjehy8MzA6ckj, message cmsg_01Sk8xdkWKCz34CUCfVMyQbxJrXUFtBjbaABs1KJUqa8Yi
- Categories: structure, ui, naming, question
- Summary: On the file-set definition: views are custom interfaces with their own logic for a kind of file (every SKILL.md gets one skill interface); shared templates are possible but not required. The changelog should be JSON so changes can later be followed by task, with the input, description and what logic changed. Asks whether schema.json is already covered by the examples or is additional.

## Raw input
~~~text
first of all custome views by type it's not just a tables and etc and yes we can have templates for this kind, but it's not nessessary, some times we ll need some custome logic around the table, so generally it's specific views for example like SKILL.md where i want that every skill have one interface with information, for change log i think also make json becase later i want move with changes and see what task what make changes and what was change, so there i want see input, description, what logic it changes and etc, about shema.json i think this kind of things we have in a examples or it's suppose to be additonal ?
~~~

## Answer
~~~text
I updated file-set.md. Views are now custom interfaces with their own logic, for one file or shared by a kind of file, so every SKILL.md gets one skill view. Changes are `.changelog.json`: each entry names the task, your message, the decision, what logic changed and the other files it touched.

On the schema: the Example is for reading and the schema is the rules a script checks, so they overlap. I'd keep it only for config files and build the Example's field notes from it.
~~~

Card: "Keep a format file for config and data files, then apply the set?" Schema, then go (recommended) / Example only, go / Not yet. Waiting for the owner.

## Processed into
- in progress: vision/plans/file-set.md (Views rewritten; Changes as .changelog.json with fields; the format file question)
