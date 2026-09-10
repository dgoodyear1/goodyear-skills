---
name: account-access-playbook
description: "Grant, review, or revoke a person's access to a business's social and admin accounts (Meta Business Portfolio / Facebook Page / Instagram, ticketing platforms like Eventbrite, and your own site admin). Use whenever adding a new team member or volunteer to social accounts, removing someone who left, running a periodic access audit, or troubleshooting a 'cannot be removed — connected asset' error on Facebook or Instagram."
---

# Account Access Playbook

A structured way to control who can act as a business on its social and admin accounts — grant it deliberately, remove it cleanly, and keep a record so nobody has to reconstruct who has access to what from memory.

Built for any small business, nonprofit, or venue with rotating staff, volunteers, or contractors touching its public accounts — not just one platform.

## When this applies

- Someone new needs to post, moderate, or manage a business's social accounts
- Someone is leaving, or already left, and needs their access revoked
- A periodic "who actually has access to our stuff" review
- Facebook or Instagram is refusing to remove a person with an error like "this person cannot be removed because they are assigned access on the connected [asset] — please remove their access on the connected asset first" — a real deadlock, not a glitch, and Step 4 below is the fix

## Step 1 — map every surface, honestly

Before touching a setting, list every place someone outside the owner can act on the business's behalf. For most small operations:

- The social accounts — a Meta Business Portfolio typically owns both a Facebook Page and an Instagram account together
- A ticketing or booking platform, if the business runs events (Eventbrite, similar tools)
- The business's own website admin panel, if it has one
- **The one people forget:** anyone who still has an original shared login from before proper individual accounts existed

That last one matters most. A password typed into someone's phone years ago doesn't show up in any platform's access list or audit log — it just keeps working until it doesn't. If the business runs on a shared login instead of individually invited accounts, fix that first, ahead of everything below.

For each surface, open its actual people/team settings and read the current list — don't work from memory. There is almost always at least one name that surprises you.

## Step 2 — settle the access level before the person

Ask the business owner, one question at a time, before granting anything:

1. What does this person actually need to do — post, moderate comments/DMs, run ads, manage settings, see financials?
2. Full access, or a narrower role?

Then match to the platform's real tiers instead of defaulting everyone to full:

**Meta (Facebook Page + Instagram, assigned together from the Business Portfolio):**
- Full control — post, run ads, manage settings, add/remove people. Functionally equivalent to ownership. Reserve for people trusted to make a unilateral decision about the account's future.
- Partial / content — post, create events, reply to comments and DMs, view insights. No settings, no people.
- Content + ads — partial, plus ad spend, for anyone actually running paid campaigns.
- Messages-and-comments only — moderation. The one role that's name-searchable and needs no email invite.

**Eventbrite (or similar ticketing platforms):**
- Owner — one person only.
- Admin — everything, including payouts and financial visibility.
- Custom role — create/edit events with no financial access. Build this one; it's the role almost nobody bothers to set up, and the one that matters most for door staff, volunteers, and seasonal help.
- Check-in-only — cannot be combined with any other permission on most platforms. If someone needs check-in plus event setup, they need Admin or a custom combined role instead.

**Default rule:** narrowest role that lets the person do their actual job. Full/Admin access is not a gesture of trust — it's a decision that this person could, today, take over the account.

## Step 3 — grant it, watching for the interface's dead ends

**Meta specifically has two traps:**

- From a Page's own asset panel, "Assign people" only lists people already inside the business portfolio — it does not invite anyone new. The real invite flow is one level up: Business Settings → Users → People → Invite. Same intent, wrong door, if you start from the Page.
- The Page's own Settings → Page access just bounces back to Business Settings for a portfolio-owned Page. Don't spend time there.

Every invite (except Meta's comment/message-only moderator role) goes out by email, not name search. Get the person's email before starting on any platform.

**Note for accounts with several full-access people:** Meta requires a second full-control approver once a portfolio has three or more full-control users, for certain high-stakes actions. Keeping that list short keeps the account fast to operate.

## Step 4 — removing someone, and the deadlock fix

**Never try to remove a person asset-by-asset on Meta.** A Facebook Page and its connected Instagram account are linked. Removing from one while still assigned on the other produces a genuine circular error — each system tells you to remove the person from the other one first. You can loop on this indefinitely.

**The fix:** remove the person from the Business Portfolio itself, not from the individual Page or Instagram asset. Find their row in the portfolio's people list, open their detail panel, and remove them at that level — this strips Page, Instagram, and any connected ad account together in one action, because it revokes the membership the individual permissions depend on.

After removing, reload before concluding it failed — the detail panel doesn't always visually refresh on success.

For other platforms, removal is usually simpler and asset-by-asset is fine — the deadlock above is specifically a Meta connected-asset behavior.

## Step 5 — log it

One line per change: who, what level, which platform, what date, who approved it. Ninety seconds now saves a full reconstruction later — when someone new starts, when someone leaves, or if a platform or customer ever asks who had authority to act.

Write the change to wherever the business keeps its own operating record (a project doc, a shared sheet, a memory file) — the log matters more than where it lives.

## Guardrails

- Never enter a password on someone's behalf or create an account for them — every grant goes through the platform's own invite flow.
- Get the owner's explicit go-ahead for each specific person and access level before sending an invite. Don't infer intent from "add the new hire" — confirm level.
- Don't let a settings/access task turn into a public action as a side effect (e.g., Facebook's "Create a post?" prompt after some profile-adjacent changes) — decline anything that publishes.
- If a person's role is genuinely ambiguous, default to the narrowest tier and let them ask for more if the job requires it. Upgrading is a thirty-second follow-up; walking back an over-grant is a much harder conversation.

## Model guidance

- **Sonnet** handles the whole flow — this is a procedural, judgment-light task once the access level is settled.
- Use **AskUserQuestion** (or ask directly, one question at a time) for Step 2 — never guess an access level.
