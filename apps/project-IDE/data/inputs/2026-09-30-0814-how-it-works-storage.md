# in-20260930-0814: Is How it works generated every time?
- At: 2026-09-30T08:14:01Z · Where: thread: Interactive file tree UI · Source: chat · Ref: cmsg_01Sk8xdkWKCz34CUCfVMyQbxF155h1CEV5SB5ftKh6Loaz
- Categories: question, ui
- Summary: The owner asked whether the How it works text is generated on every visit, whether it is saved, and when.

## Raw input
~~~text
and how does it works "how it works" it ll just generate every time we go this tab? do we save it at all? and in what time then?
~~~

## Answer (given in chat)
~~~text
No, it doesn't regenerate every time. It's written once and then saved.

- **When it's written:** the first time anyone opens How it works on a file that has no explanation yet. Claude writes it then, using the model picked in the Send box.
- **Where it's saved:** in the page's own store, together with the time it was written and a fingerprint of that file's data. After that, everyone who opens the tab sees the saved text with no new call. The tab shows "Written <date> from this page's data".
- **When it's rewritten:** only when you press Rewrite. If the file's notes, fields or content change later, the tab says the notes changed and the button becomes "Rewrite with the latest notes". It never rewrites on its own.

These explanations stay on the page and aren't copied into file-tree.md when we sync. I can also write all 261 in one go if you'd rather not wait on first open.
~~~

## Processed into
- answered in chat
