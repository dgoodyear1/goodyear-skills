# Account Access Playbook

A Claude skill for controlling who can post as a business — Facebook Page, Instagram (via a Meta Business Portfolio), Eventbrite or similar ticketing platforms, and your own site admin. Built for any small business or nonprofit with rotating staff, volunteers, or contractors touching its public accounts.

## Install

Drop `SKILL.md` into your skills directory (`~/.claude/skills/account-access-playbook/` for Claude Code / Claude Desktop), or point your marketplace config at this repo.

## What it does

Walks through mapping every account surface a business has, matching each person to the narrowest access tier that fits their job, granting it through the platforms' real invite flow (not the dead-end buttons both Meta and several ticketing tools bury in their UI), and logging every change so nobody has to reconstruct "who has access to what" from memory six months later.

It also documents the fix for a real, reproducible Meta bug: a Facebook Page and its connected Instagram account refuse removal of a shared person until the *other* asset removes them first — a genuine deadlock. The fix is removing the person from the Business Portfolio itself, not the individual asset.

## Worked example

Invoke the skill and say "someone left, remove their Facebook and Instagram access" or "add a new volunteer to our socials, content only." It runs the interview, recommends the access tier, and walks the actual grant or removal steps — including the deadlock fix if you hit it.

## The full system

This skill covers the method. **The One-Person Business Systems Map** — the full access-level decision matrix, exact invite paths per platform, a departure checklist, and the log template — is free with your email at [daltongoodyear.com/vault](https://daltongoodyear.com/vault).

## License

MIT.
