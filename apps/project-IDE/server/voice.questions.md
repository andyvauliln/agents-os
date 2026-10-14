# Questions: voice.py

## Open questions for the owner

None open.

## The owner's questions

### 2026-09-30: Can Claude voice input be used on the page?

> jsut curious if we can use claude voice texting in the ui if yes then how?

Claude's own voice mode cannot be used by the page. On the owner's server the request box and the delete note box have a microphone button: it records up to five minutes, `voice.py` sends the recording to Groq's speech-to-text models (it tries the next model on a rate limit or an error), and the text is added to the box to check before sending. On claude.ai the button is hidden, because the page gets no microphone there, so the device's own dictation is the way. This changed later: at first only the device's dictation was offered; the microphone button came on 2026-10-09.

### 2026-09-30: How to use voice input

> рщц

This was "how" typed in the Russian keyboard layout. On the owner's server, press the microphone button next to the box, speak, press it again to stop, then check the text and send it. Anywhere else, use the device's dictation: the mic on the keyboard on a phone, Fn twice on a Mac, Win+H on Windows; Russian works too.
