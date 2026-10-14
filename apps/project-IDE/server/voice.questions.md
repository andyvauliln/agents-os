# Questions: voice.py

## Open questions for the owner

None open.

## The owner's questions

### 2026-09-30: Can I use Claude voice input on the page?

> jsut curious if we can use claude voice texting in the ui if yes then how?

The page cannot use the voice mode of Claude.

On the owner's server, the request box and the delete note box have a microphone button. It works like this:

1. It records for a maximum of five minutes.
2. `voice.py` sends the recording to the speech-to-text models of Groq. If a model gives a rate limit or an error, it tries the next model.
3. The page adds the text to the box. You check it before you send it.

On claude.ai, the page hides the button, because it gets no microphone there. Use the dictation of your device.

This changed later: at first, we offered only the dictation of the device. The microphone button came on 2026-10-09.

Docs improved: apps/project-IDE/server/voice.index.md.

### 2026-09-30: How do I use voice input?

> рщц

This was "how", typed with the Russian keyboard layout.

On the owner's server, do these steps:

1. Push the microphone button next to the box.
2. Speak.
3. Push the button again to stop.
4. Check the text and send it.

On other devices, use the dictation of the device:

1. On a phone, use the microphone on the keyboard.
2. On a Mac, push Fn two times.
3. On Windows, push Win+H.

Russian also works.

Docs improved: apps/project-IDE/server/voice.index.md.
