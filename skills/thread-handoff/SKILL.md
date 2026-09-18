---
name: thread-handoff
description: Pack a long thread into a short baton any model can run. Use when Dalton says handoff, baton, new chat, bring this to Grok, bring this to Claude, paste into GPT, thread too long, compact, recap for pickup, or context is fat.
---

# Thread handoff (baton)

Agnostic means the paper does not care who reads it. Same block works in Claude, GPT, Grok chat, or Grok Bot.

Do not summarize the universe. Write a baton the next model can run without this chat and without your brand name in the instructions.

## When to fire

- Thread feels slow, repetitive, or overnight-stale
- He says handoff / new chat / wrap this / bring this to Grok / bring this to Claude
- He is leaving one product and opening another
- You are about to give a giant recap instead of doing the job

## Output only this

Plain markdown. No tool XML. No "As an AI". No product UI tips.

1. **Baton title** — 6 words
2. **Carry to** — one room he will paste into (Claude chat / Claude Code / Grok.com / Grok Bot / GPT)
3. **Rooms** — one line. What stays in which room. Drive `/AIOS` is memory.
4. **Locked decisions** — bullets. No history.
5. **Open jobs** — max 7. Each line = job + room + next human click
6. **Do not** — 3 lines
7. **Paste prompt** — a fenced block he copies as the first message in the next chat

Cap the whole baton at ~400 words.
Save to Drive `/AIOS` as `baton-YYYY-MM-DD.md` when Drive write works. Offer GitHub `dgoodyear1/goodyear-skills` only if write works.

## Paste prompt rules

The fenced block must stand alone. Assume the next model has never seen this thread.

Must include:

- Follow tool-router if the skill is installed. If it is not, still obey the room line.
- Drive `/AIOS` is memory (`commitments.md`, `log.md`, latest `baton-*.md`, `room-map-2026-09-17.md`).
- Repos by `owner/name` only.
- Staffy / 50-bot roster stays asleep.
- Do not send email. Do not checkout. Do not merge. He clicks those.
- Start on open job 1 unless he names another.

Must not include:

- Full CLAUDE.md
- GROK-BOT-SYSTEM-CONTEXT
- API keys
- A lecture about which company made the model

## Direction cheat

| He is leaving | He is going | Carry |
|---|---|---|
| Claude | Grok.com | Decisions + open jobs. No Claude-task IDs. |
| Claude | Grok Bot | One click-job only. Timebox 10 min. 15% Ultra cap. |
| Grok.com | Claude chat | The thick pack / PDF / conversation. |
| Grok.com | Claude Code | Repo, path, what the PR should do. He merges. |
| Anywhere | GPT | Same baton. GPT will not have Drive. Paste the baton text itself. |

## Rules

- No 50-bot roster. No full system-prompt dump.
- Name repos `dgoodyear1/...`
- Next model starts job 1 unless he picks another.
- If he says "bring this to Grok" you are the leaving model. Write the baton for Grok.com unless he said Bot.
- If he pastes a baton in, do not rewrite it first. Do job 1.
