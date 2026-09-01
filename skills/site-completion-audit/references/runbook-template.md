# The runbook

The report says what's wrong. The runbook is what actually gets it fixed. Treat it as the primary deliverable.

## The format, non-negotiable

**Every step is one thing to copy and one place to paste it.** The user should never have to assemble anything, remember anything, or read an instruction that says "see prompt 1.2".

Each step has:

1. A **number** and a short **name**
2. A **destination tag**: `COWORK` (a new chat in the Claude desktop app) or `CLAUDE CODE` (Terminal)
3. A **model**: Opus or Sonnet, for Claude Code steps
4. **What this does**, in one plain sentence a non-developer understands
5. **How to start it** — the literal mechanics, every time. How to open Terminal. `cd` by dragging the folder onto the window. `/model opus`. Assume nothing, repeat yourself.
6. **The prompt itself**, in one block, with the safety preamble already inside it

Then a reusable **"check and merge a pull request"** step the user returns to after every PR.

## Rules

- **Bake the preamble into every Claude Code prompt.** Never reference it, never ask them to paste two things.
- **Browser click-work is not an exception.** Convert it into a COWORK prompt that walks one click at a time and waits for the user's answer between steps. Disconnecting a platform, changing repo visibility, creating a database, editing DNS — all of these become prompts.
- **Ask, don't guess, when a fact belongs to the user.** Legal status, EIN, media contact, licence number, whether an event is real. Have the prompt stop and ask, and forbid shipping a placeholder in the meantime.
- **Forbid fabrication explicitly, in every prompt.** "Do not invent a reviewer." "Omit `taxID` entirely rather than emitting a placeholder." "Do not emit Event schema for events that don't exist." A model will fill a gap with plausible content unless told not to.
- **Order by dependency, safety first.** Safety, then ownership, then deletions, then truth, then architecture, then everything that depends on it. Where a step reads a file an earlier step wrote, say so.
- **One prompt per coherent work unit** — big enough to be worth a session, small enough to verify in one pass.
- **Every prompt ends by asking what couldn't be finished** and what's blocking.
- **No parallel sessions on the same repo.** Say it plainly; the collisions are silent until merge.

## The safety preamble

Paste this verbatim at the top of every CLAUDE CODE prompt in the runbook.

```
=== START OF SAFETY BLOCK — this is part of the prompt, do not remove ===

Before doing anything else, run this orientation and report back. Make NO changes yet.

I am not a developer. Explain things in plain language, go one step at a time, and
stop and ask me whenever you need a decision. Never assume — if something is
ambiguous, ask.

SAFETY CHECK — I run other Claude Code sessions on other repos, and sometimes on this one.
1. Run `git fetch --all --prune`
2. Run `git status --porcelain`. If there is ANY uncommitted or untracked change that
   you did not make, STOP and show it to me. Do not stash it, discard it, or commit it.
3. Run `git branch --show-current` and `git log --oneline -5`
4. Run `git log --oneline HEAD..origin/main`. If my local copy is behind, tell me
   before you branch.
5. Run `gh pr list --state open` so we don't duplicate work another session started.

THEN ORIENT (still no changes):
6. Print the repo structure two levels deep, plus package.json, the build config, and
   index.html.
7. Show me how routes are defined, and how each page's title, description, canonical
   link, Open Graph tags and JSON-LD are set.
8. Confirm the build command, and that the build succeeds right now.

RULES FOR THIS WHOLE SESSION:
- Create ONE new branch off the latest origin/main. Tell me its name. Never commit to main.
- Never use --force, `git reset --hard`, or `git checkout .`. If you want to throw
  something away, stop and ask me first.
- Match the existing component patterns and styling conventions. Read neighbouring
  files before you write new ones.
- After each phase: summarise what changed in plain language, run the build, and WAIT
  for me to say "go" before continuing.
- At the end: push the branch and open a pull request against main with a clear
  description. Do NOT merge it. I will merge it myself.
- Never invent content, credentials, a legal status, a person's name, a medical
  reviewer, a statistic, or a date to fill a gap. If you don't have it, ask me or
  leave it out and tell me.

=== END OF SAFETY BLOCK — the actual task follows ===
```

## The Cowork preamble

For COWORK steps:

```
You are helping me with [SITE NAME] ([DOMAIN]).

First, read my project memory — call project_memory_read and read the site's audit note.

Important: I am not technical. Walk me through this ONE SMALL STEP AT A TIME. Tell me
exactly what to click or type, then STOP and ask me what I see before giving me the
next step. Do not give me a numbered list of ten things at once. If you can drive my
Chrome browser directly, do that instead and narrate what you're doing.

Here is the task:
```

## The merge step

Include this once, and tell the user it's the one they reuse after every pull request.

```
[Cowork preamble]

Claude Code just opened a pull request on my [DOMAIN] repo and I need to check it
before merging. Merging deploys it live to the real website within about a minute, so I
want to be careful.

Pull request number: [PASTE]
What it was supposed to do: [PASTE THE ONE-LINE SUMMARY]

Walk me through this one step at a time, waiting for me after each:
1. Where to find the preview link on the pull request page, and what a preview
   deployment is.
2. Which specific pages on that preview I should click through given what this PR
   changed. Give me a checklist and tell me what "correct" looks like for each.
3. How to check the build passed, and what to do if it shows a red X.
4. How to merge it, and what happens next.
5. How to confirm it went live, and roughly how long to wait.
6. How to undo it if something looks wrong after merging — I want the escape hatch
   before I click, not after.

If anything looks wrong, tell me to stop and we'll fix it before merging rather than
merging and patching.
```

## Generating the runbook mechanically

Write each step body to `steps/NN.body` and its metadata to `steps/NN.meta` as
`DESTINATION|MODEL|NAME|WHAT IT DOES|HOW TO START`, then assemble with a short script
that prepends the right preamble. This keeps the preamble identical everywhere and lets
the same source produce both the markdown runbook and the step-runner artifact.
