# Agent Employee Framework

A Claude skill for deciding how much authority to give an AI agent — Claude, Grok, or any agentic tool — without either over-approving every action or leaving it dangerously unconstrained.

## Install

Drop `SKILL.md` into your skills directory (`~/.claude/skills/agent-employee-framework/` for Claude Code / Claude Desktop), or point your marketplace config at this repo.

## What it does

Walks through naming an agent and giving it a one-sentence mission before configuring anything, setting a spend cap (dollars, tokens, or usage budget) as the actual safety mechanism instead of a long permission list, defining the five categories that always need a human regardless of trust built up elsewhere, and setting up a numbered-list batch-approval cadence so wide authority doesn't turn the human into a bottleneck.

## Worked example

Invoke the skill and say "I'm setting up a new agent to handle [job]" or "help me decide how much authority to give my agent." It runs the naming and mission step, helps set the spend cap, defines the escalation list, and proposes an approval cadence.

## The full system

This skill covers the method. **The Agent Employee Framework** — the full spend-cap worksheet, the escalation-list template, the numbered-list approval cadence templates, and a worked example — is available at [daltongoodyear.com/journal](https://daltongoodyear.com/journal).

## License

MIT.
