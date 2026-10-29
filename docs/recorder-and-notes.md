# Recorder and notes

## Record
The footer at the bottom of the page is recorder-view. The red button at its right records.
1. Click it one time to record audio (the microphone). Click it two times to open its menu: 1 Record audio, 2 Record video (a screen, a window or a tab that you choose, with its sound and the microphone), 3 Notes. A click on the button or out of the menu, or Escape, closes the menu.
2. Or use the keys (not while you type in a field or an editor): push Arrow Up two times to record audio. Push Arrow Up and Arrow Down at the same time to record video.
3. While it records, the button is a stop button, and the header shows the kind and the time (for example "Audio 00:12").
4. While it records, you are in select mode. The element under the pointer has a red frame. Click an element to select it: the page does not get the click. A timeline block or a view part has a purple frame, and its path shows above it: the view in the state, then the elements down to it, and the block (for example "extension.views.timeline-view › #tl-strip > button.tl-step:nth-of-type(3) (block 3: Run index.html)").
5. To stop, click the button, push the same keys again, or stop the sharing of the browser.
6. The card above the button plays the recording and lists the elements that you selected, with their time. Save file saves it (webm). On claude.ai, you confirm the download. The close button forgets the recording. The recording is in the memory of the page only, not in the state.
7. The browser asks you to let the page use the microphone or the screen. If it does not let the page record, a red note above the button tells why.
8. The ui-data of recorder-view keeps: recording ("", audio or video), started_at, selected (the last path), selections (each {at, path}), result (kind, time, size, type), error and menu_open. The calls of the record button are timeline blocks only when Track state is on.
9. Hold the button for 4 seconds to open the Notes page (notes-view), or click Notes in the menu. It shows between the header and the footer, as the other views do. Click × to close it. When you release the button after the 4 seconds, it does not record.

## Notes
1. Each recording is a note when it stops. You can also write a note: type it in "Write a note" and click Add note.
2. A note shows its text (a note that you wrote, or a recording after Transcribe) in a box where you can change it. A recording without text shows its player.
3. The buttons of a note:
   - Transcribe (a recording): puts the text that the browser heard while it recorded into the note. If there is no text, a message tells why.
   - Send now: the note goes to Claude in this Claude session, as a comment of the page that is sent to Claude. Only editors of the page can send. It works on claude.ai.
   - Send now new session: the note starts a new Claude Code session, through the task in settings.new_session_task and the Claude Code Remote connector.
   - Delete: the note goes, with its recording.
4. Under the text: the box, the view path of the note and Show state. The view path is the view of the first element that you selected while it recorded, or the view that was open (state view, docs view, else the header). Show state shows the ui-data of that view under the note. Click Hide state to hide it.
5. Check the boxes of notes, then click Send selected (at the bottom) to send them together to Claude in this session.
6. Settings (the gear button): Transcription is Browser (the default) or Off. With Browser, the browser turns what the microphone hears into text while you record (Chrome sends the sound to its speech service). Language is the language to hear (for example en-US); empty is the language of the browser. New session task is the id of the scheduled task (trig_...) that Send now new session starts: a task that starts a new session at each run.
7. On claude.ai, the frame of the page cannot use the microphone or the screen, so it cannot record or transcribe there. Text notes and sending work there. Recording and transcription work when you open the page from the repo on your computer.
8. The ui-data of notes-view keeps notes (each {id, kind, at, time, text, view_path, selections, file}), settings ({transcribe, lang, new_session_task}), settings_open and message. The recordings and the heard texts are in the memory of the page (os.refs.notes); on claude.ai a recording is also a file of the page (file, served at /_blob/<file>). The notes stay when you save the state.

## The microphone on claude.ai
1. On claude.ai, the page runs in a frame of the artifact. The frame does not have the permission to use the microphone or the screen.
2. So the browser does not ask you. The record button shows "The browser did not let the page record the microphone: Permission denied" at once.
3. The capabilities of an artifact have no microphone. The page cannot change this.
4. Recording and transcription work when you open the page from the repo on your computer (python3 -m http.server in the folder of the repo).
5. On claude.ai you can still dictate with the dictation of your system (for example Fn Fn on a Mac, Win+H on Windows) into "Write a note".
6. A choice is open: what the page does when the microphone is blocked (see vision.md).