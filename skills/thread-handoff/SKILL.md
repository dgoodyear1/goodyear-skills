---
name: thread-handoff
description: Pack a long Grok or Claude thread into a short baton for a new chat. Use when Dalton says handoff, baton, new chat, thread too long, compact, recap for pickup, or context is fat.
---

# Thread handoff (baton)

Do not summarize the universe. Write a baton the next model can run without this chat.

## When to fire

- Thread feels slow, repetitive, or overnight-stale
- He says handoff / new chat / wrap this
- You are about to give a giant recap instead of doing the job

## Output only this

1. **Baton title** — 6 words
2. **Rooms** — one line (what is Claude vs Grok vs Bot vs Drive)
3. **Locked decisions** — bullets, no history
4. **Open jobs** — max 7, each with room + next click
5. **Do not** — 3 lines
6. **Paste prompt** — a block he copies into a new chat. Must include tool-router + paths.

Cap the whole baton at ~400 words. Save it to Drive `/AIOS` as `baton-YYYY-MM-DD.md` and offer GH only if write works.

## Rules

- No 50-bot roster. No full CLAUDE.md paste.
- Name repos by owner/name.
- Next model starts working the first open job unless he picks another.
