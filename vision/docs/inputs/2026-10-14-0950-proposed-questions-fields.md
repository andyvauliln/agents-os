# Input 2026-10-14 09:50: when proposed happens, when questions are made, why the fields

- From: the owner, in the thread "Interactive file tree UI"
- Date: 2026-10-14

## Raw input
~~~text
1. An agent writes its idea with status `proposed`. It names the idea in its reply to the owner and gives its recommendation. when it's happening i am not unerstand still, about question in which stages or when  (now or in new version) we generate questions,  and i still not understand purpose of fields
~~~

## Answer
~~~text
Proposed happens whenever an agent fills a gap the owner did not fill (a plan, a default, its own idea), the same now and in the new version; the owner's yes makes it decided. No script makes questions: an agent writes one when it meets a choice only the owner can make while writing a doc (Still open + x.questions.md) or changing an item; same in the new version, any item can get one, answered mainly on the page. The Details fields answer what an agent must know before a change (what is it, is it safe, who works with it, what else must change, why, what applies from above). Today almost none are filled or read. Proposed: keep only about, status, secret, generated_by, related, update_with, sources; fill them everywhere and check them in the build. Waiting for the owner's yes or no.
~~~

## Processed into
- docs/metadata.md sections 6.2, 15.3, 18.2
