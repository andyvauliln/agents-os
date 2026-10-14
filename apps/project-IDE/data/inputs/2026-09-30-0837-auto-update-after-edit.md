# in-20260930-0837: Do summaries update after an edit?
- At: 2026-09-30T08:37:31Z · Where: thread: Interactive file tree UI · Source: chat · Ref: cmsg_01Sk8xdkWKCz34CUCfVMyQbx6b2VeifgXrXE1ts4MJoxyy
- Categories: question, process
- Summary: The owner asked whether editing a file automatically updates its metadata and the summaries of the page and the folders above it.

## Raw input
~~~text
if we for example edit file any how and his metadata ll summary for the page and folders updates automaticly?
~~~

## Answer (given in chat)
~~~text
Not yet. The only thing that updates automatically is the edit itself. Here's what happens today when you edit a file:

- **The file's content:** saved and shown right away.
- **Its description, purpose and rules:** they stay as they were unless the draft changed them too. Saving new content on the File tab doesn't rewrite them.
- **Its How it works:** marked out of date, with a Rewrite button. It doesn't rewrite itself.
- **The folders above it:** the folder's How it works is marked out of date only if a file's name, description or status changes, and only one or two levels down. A content-only edit doesn't mark it at all. The Contents cards do show the new descriptions right away.

What I'd suggest instead:
- When a file's content is saved, Claude checks whether its description, purpose and rules still fit the new content. If they don't, it offers a draft you can save.
- Every How it works above that file, up to the top, gets marked out of date and rewrites itself the next time someone opens it. That way nothing is rewritten for folders nobody looks at.

Want me to build that?
~~~

## Processed into
- answered in chat
