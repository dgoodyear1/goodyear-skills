---
name: agent-employee-framework
description: "Set up a new AI agent (Claude, Grok, or any agentic tool) the way you'd onboard an employee, not configure a tool: name it, define a spend cap instead of a long permission list, set a numbered-list approval cadence, and draw the short list of things that always need a human. Use whenever standing up a new autonomous agent, deciding how much authority to give one, or troubleshooting an agent setup that's either too slow (over-approved) or too risky (under-constrained)."
---

# Agent Employee Framework

A way to decide how much authority to give an AI agent that doesn't collapse into either extreme — a permission list so long it's obsolete the day you write it, or full autonomy with no real constraint at all.

The core move: stop asking "what is this agent allowed to do" and start asking "what does a bad week cost, and can I afford it." Cap the cost. Leave the authority wide open underneath that cap.

## When this applies

- Standing up a new agent (Claude, Grok, or any agentic tool) for a real recurring job
- An existing agent setup feels bottlenecked — every action needs a separate approval, defeating the point of automating it
- An existing agent setup feels risky — it has broad access and no clear cap on how bad a mistake could get
- Deciding how much to trust an agent as it earns a track record

## Step 1 — name it before you configure it

Give the agent a name and a one-sentence mission before writing a single permission. This is not cosmetic. "The leasing script" gets treated with permanent suspicion because scripts don't have judgment. "Lindsay, whose job is moving leads to leases with no stale applicants," gets instructions that describe a role instead of enumerating actions — and role-shaped instructions produce better agent behavior than action lists do.

Ask the user for the job in one sentence: what does this agent exist to accomplish, not what tasks does it perform.

## Step 2 — set the spend cap, not the permission list

Do not start by listing what the agent can and cannot do. Start with one question: what does a genuinely bad week of this agent's work cost, in dollars, tokens, or usage budget — and is that number acceptable?

Set that number explicitly. This becomes the actual safety mechanism. A permission list always has a gap nobody thought of; a spend cap is legible and bounds the damage regardless of which gap gets hit. If the agent burns through its cap doing something wrong, that's the signal to fix the instructions — cheap, fast, and it happened on a knowable schedule instead of showing up as a surprise bill.

## Step 3 — leave authority wide open under the cap

Inside the spend cap and inside the agent's defined lane, give it real authority — not "draft this for me to send," but "send this unless it's on the escalation list." An agent that can only draft never actually saves time; the review step becomes the bottleneck.

## Step 4 — the five things that always escalate, no matter how much trust has built up

Regardless of the spend cap or how long the agent has run cleanly, these get a human step every time:

1. Anything filed with a government agency
2. Payroll
3. Approving or paying a bill
4. Any owner/client-facing number the agent didn't get from the human first
5. Entering a credential, or bypassing a second-factor/security step

Keep this list short — five items, not fifty. A long list is the permission-enumeration trap wearing a different hat. If something doesn't clearly belong on this list, it defaults to the agent's own authority under Step 3, not to a new line item here.

## Step 5 — the numbered-list approval cadence

For anything that needs a human but doesn't need to block the agent's other work: batch it into a numbered list with a deadline, not a one-at-a-time chat approval.

The agent presents: "Here are 5 things needing your call, respond by [time]." The human clears it by typing back numbers (or a quick decision per line). Silence past the deadline is treated as approval on genuinely low-stakes items and as an automatic escalation-hold on anything touching money or a relationship — never silent-approval on the Step 4 list.

This is the mechanism that makes wide authority safe without making the human the bottleneck: review happens in batches, on a cadence the human controls, instead of continuously.

## Step 6 — set cadence to protect the budget, not to feel responsive

Continuous or high-frequency agent runs feel more responsive. They mostly burn the usage budget on noise. Pick a cadence matched to how fast the underlying business actually needs to react — twice a day is enough for most operational pipelines — and treat "always on" as a cost decision, not a default.

## Guardrails

- Never let an agent bypass a security step (2FA, credential entry) to save time, even once it has a long clean track record. That's exactly the category of shortcut that looks fine until it isn't.
- Don't backfill the Step 4 list reactively after every near-miss — five stable categories, applied consistently, beats a growing list of specific incidents.
- A new agent (or a newly-expanded role for an existing one) starts with a lower spend cap and a shorter leash on Step 3, earning wider authority as it accumulates a real track record — not granted all at once because the framework exists.

## Model guidance

- **Sonnet** for the setup conversation (Steps 1-4) and ongoing cadence tuning.
- Use **AskUserQuestion** or ask directly for Step 2's number and Step 4's list — never assume a cap or an escalation category on the user's behalf.
