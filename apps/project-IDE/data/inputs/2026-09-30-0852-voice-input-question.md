# in-20260930-0852: Can the UI use Claude voice input?
- At: 2026-09-30T08:52:56Z · Where: thread: Interactive file tree UI · Source: chat · Ref: cmsg_01Sk8xdkWKCz34CUCfVMyQbxPknA97Fao3fEtLyUugvZAG
- Categories: question, ui
- Summary: The owner asked whether Claude voice input can be used in the UI, and how.

## Raw input
~~~text
jsut curious if we can use claude voice texting in the ui if yes then how?
~~~

## Answer (given in chat)
~~~text
Good question. I'll check what voice input the page can actually use, then answer.

Not Claude's own voice mode. Pages like this one can't use it: the page can ask Claude in text, but it gets no audio or voice access. There are still two ways to talk to it:

1. **Your device's dictation, which works today with no changes.** Tap the Send box and use the mic on your phone keyboard. On a Mac, press Fn twice. On Windows, press Win+H. Your speech becomes text in the box and you press Send.
2. **A mic button in the Send box, which I can add.** It would use the browser's built-in speech-to-text: Chrome and Edge send the audio to Google, Safari to Apple, and Claude only gets the text. I can't confirm from here that the page's frame allows the microphone, so the button would hide itself wherever it doesn't work.

I'd use option 1 for now. Want me to add the mic button anyway?
~~~

## Processed into
- answered in chat
