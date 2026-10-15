# Questions: 2026-10-15-0925-notes-and-runs-panel.md

## Open questions for the owner

From the plan: One panel for AI notes and runs, with a page for every run.

1. **Who writes the summary and the tags of a run?** This choice sets the cost and covers terminal runs. Recommended: Claude Haiku writes them after each run. The cost is about one cent for each run.
2. **How do we make a pull request?** A merge acts outside this server. Recommended: the owner presses a button for one run. The server moves the commits of the run to a new branch and opens the pull request. The owner signs in `gh` on the server one time. NOTES: already github connected, so we should work i guesss always in a worktree or in a cloud to handle several notes, in a notification i can selecte it default locally, after i press pull request, yes merge could be outside, also i want some control buttons about what to do in a process, like auto merge, do all tests or only related to this feature, check for bugs,make report etc,
3. **Does git keep the run records?** Transcripts can hold private text. Recommended: no. The run records stay in the logs folder, and git does not keep that folder.
4. **Which terminal runs does the list show?** Recommended: the 50 newest Claude Code sessions in all folders of this repository. NOTES: for now let's make 10 default, and i can change it with a show more, also they should be sorted by that last one was done, first if there some block where ai can't do something without me involved
5. **Which statuses does a note have?**  Notes:  statuses: transcribing, ready, planing, working, done, failed, cancelled, need human, need manual test, in main. something like this
6. **Can we install the browser libraries on this server?** Without them, no browser test of the page can run here. Recommended: the owner runs `sudo npx playwright install-deps chromium` one time.



## The owner's questions

## Taken into the plan

- Questions 1, 2, 4, 5 and 6 are answered. The second version of the plan uses the answers.
- Question 3 has no answer. The plan uses the recommended answer: the run records stay out of git.
- Two new open questions are in the plan: the defaults of the send options, and the worktree folder.
