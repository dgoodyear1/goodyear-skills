---
name: site-completion-audit
description: Audit any website for completion gaps — features that are conceptual rather than functional, placeholder text shipped to production, broken trust signals, SEO/AEO/GEO defects, crisis-safety failures, and accessibility problems — then turn the findings into a numbered runbook of copy-paste prompts that actually fix them. Works on any site; keeps a per-site profile and baseline so every re-run is a diff. Use when the user asks to audit a site, check what's not finished, find gaps, review a site for launch readiness, run an SEO/AEO/GEO audit, or run the routine site check on any of their properties.
---

# Site Completion Audit

Find the gap between what a website **promises** and what it **does** — then hand back the prompts that close it.

Most audits check whether pages load. This one checks whether pages are honest: whether the quiz computes, the tracker tracks, the download downloads, the donate button takes money, and the claims are true.

## What this produces, every time

Four artifacts. Not three, not one — the report alone is a wish list.

1. **A gap report** — `Website-Audit-YYYY-MM-DD.md`, severity-ranked, every finding carrying its verbatim evidence. Structure: `references/report-template.md`.
2. **A runbook** — `Runbook.md`, a numbered sequence of self-contained copy-paste prompts. Structure and the mandatory safety preamble: `references/runbook-template.md`.
3. **Tracker artifacts** — a findings board and a step runner, published so they outlive the session.
4. **An updated profile and baseline** — `profiles/<domain>.md`, so the next run is a diff rather than a repeat.

Then: write what changed to project memory, and offer a recurring schedule.

## Phase 0 — Load or build the site profile

Look for `profiles/<domain>.md`. Profile files live in `profiles/`:

| Profile | What it is |
|---|---|
| `_template.md` | Start here. Copy it to `profiles/<domain>.md` for each site you audit. |

No real site profiles ship with this skill. Build your own as you go — the profile is
what turns every re-run into a diff instead of a fresh wall of text.

**If no profile exists, build one first** by running the infrastructure detection in `references/infra-detection.md`, then pick a site type from `references/site-types.md`. The site type decides half the checklist — a lodging business and a health nonprofit fail in completely different ways, and auditing one against the other's checklist wastes everyone's time.

Never skip this. An audit that assumes the wrong host, the wrong rendering mode, or the wrong site type produces confident wrong advice.

## Phase 1 — Establish the baseline

Read the previous audit and the profile's baseline section. **Everything downstream is a diff.** On a re-run, the first four sections of the report are:

- **CLOSED** — verified fixed. Verify on the live site; a merged pull request is not proof.
- **REGRESSED** — was fixed, is broken again.
- **STILL OPEN** — with age in days. Over 90 days, ask directly whether it's actually going to happen.
- **NEW** — appeared since last time.

An audit with no diff is half an audit.

## Phase 2 — Crawl

Fetch `robots.txt` and `sitemap.xml` first. Then every sitemap URL, or a representative sample if there are more than ~150. Fan out across page clusters using parallel subagents so no single context holds the whole crawl.

Also probe what a site of this type *should* have and see what 404s. The list is per-type — see `references/site-types.md`.

**Use WebFetch. Never use curl or bash to fetch web content.** DNS lookups via node's `dns` module are fine and are how infrastructure gets detected.

Two traps to check for before believing any of it:
- **A garbage-URL control.** Fetch `/this-page-definitely-does-not-exist-xyz123`. If it returns the same shell as real pages, the whole site is soft-404ing and your page-by-page findings are worthless. Say so and stop.
- **An empty-body result is a finding, not a failure.** A client-rendered SPA returns nothing to a crawler. That's what Google, an LLM, a link preview, and a JS-disabled visitor see. Report it as the headline, and mark everything you couldn't read as UNVERIFIED rather than absent.

## Phase 3 — Classify every page

| State | Meaning |
|---|---|
| **FUNCTIONAL** | Does what it says |
| **PARTIAL** | Works, but a promise on the page is unmet |
| **STUB** | Real UI, no behavior behind it |
| **VAPOR** | Describes a capability that does not exist |
| **MISSING** | Linked or expected, returns 404 |
| **UNVERIFIED** | Couldn't be read — say what check would resolve it |

## Phase 4 — Hunt the tells

Grep every fetched page for all of these.

**Future-tense vapor:** "coming soon", "future versions", "will be able to", "we plan to", "in development", "this page will grow", "as we grow", "over time this will", "to be added", "not yet available", "under construction"

**Editor notes shipped to production:** "placeholder", "TODO", "lorem", "FUTURE PHOTO", "Add file at:", "swap this box", "[bracketed instruction]", "(placeholder)", any `build-id` or internal meta tag

**Unmet promises** — the highest-value category, and the one no automated tool catches. Read what the page *claims about itself*, then check it:
- a button whose label implies computation — Calculate, Generate, Suggest, Match, Analyze, Estimate, Instant — with no described result state
- "download" or "export" with no file
- "save", "track", "log", "remember" with no persistence
- "personalized", "adaptive", "tailored", "instant", "for you" on a page that never asks a question
- "interactive" on static text
- "living", "updated regularly", "growing" on undated content
- one tool claiming to read data from another tool that stores nothing

**Numbers that don't reconcile.** Collect every count, price, rating and statistic across the whole site into one table and compare them. Sites accumulate contradictory numbers — "40+ properties" on one page and "85 listings" on another and "95+ doors" in llms.txt. Contradiction damages both human trust and AI citation, and nobody notices it from inside.

**Facts with no source:** dollar figures, percentages, testimonials with no attribution, statistics with no date, legal status claims with no registration number, license references with no license number.

## Phase 5 — Technical SEO / AEO / GEO

Full checklist in `references/technical-checklist.md`. The items that matter most and get missed most:

- **Canonical tags pointing at the homepage** from interior pages, or absent entirely
- **The sitemap reference in robots.txt actually resolving** — check the domain character by character; a typo here silently hides the whole site
- **JSON-LD presence** by page type, matched to site type
- **Trust layer on YMYL content** — health, legal, financial: author byline, named reviewer with credentials, publication and review dates, linked primary sources, editorial policy
- `sitemap.xml` `lastmod` values that are real, not generated at request time
- Duplicate or doubled titles; a single generic `og:image` reused sitewide
- Rendering coverage — fetch without JS and find routes returning an empty body
- Content cannibalization: multiple URLs competing for the same query

## Phase 6 — Trust, safety, and money

Scope by site type, but always:

- Legal status and licence claims vs. evidence
- The money path, end to end — donate or checkout or booking. Follow it to the actual processor and name it.
- Every form: real endpoint, success state, labeled inputs, privacy disclosure
- Privacy policy and terms that describe what the site actually does
- **Crisis safety**, on any site touching mental health, veterans, health, grief, or addiction: is the crisis resource on *every* page or only some? Are the numbers correct, complete, and tappable? Check the emotionally-loaded pages *first* — the calming page, the grief page, the "I'm scared" page. Those are the ones that get missed, and they are the ones that matter.

## Phase 7 — Deliver

Write the report, then generate the runbook from it, then publish the boards, then update the profile and baseline. `references/runbook-template.md` governs the runbook — read it before writing a single prompt, because the prompt format is the deliverable that actually changes the site.

## Rules that make this audit worth reading

**Quote exact strings.** "The page has placeholder text" is worthless. `"Future versions of this panel can use AI to sort grants by best guess of fit"` is actionable. Every finding carries the verbatim string and the URL.

**Find the pattern, not just the instances.** Twelve broken tools is a list. "Nothing on this site persists a single byte about the user, so every tool that promises memory is lying" is a finding. The architectural read is the whole value.

**Rank by consequence, not by effort.** A misspelled crisis phone number outranks a missing meta description enormously, even though both are one-line fixes.

**Separate legal and safety from polish.** An unbacked charity-status claim next to a donate button is a regulatory issue. A dead social icon is housekeeping. Never let them share a bullet list.

**Name what's good, specifically.** An audit that only lists failures gets discounted, and the user stops reading. If the town pages are genuinely well-written human prose, say so and quote a line. It also tells them which standard to hold the rest of the site to.

**Never fabricate a finding.** If a page is client-rendered and you cannot verify its behavior, mark it UNVERIFIED and name the check that would resolve it. One false positive costs more trust than three misses.

**Don't recommend dead tactics.** Verify current standards every run; they move. As of August 2026: FAQPage and HowTo rich results are retired. `llms.txt` has no official support from Google, OpenAI, or Anthropic. Fiscally sponsored orgs without their own determination can't get Google Ad Grants. Re-check all of these each time.

**Ask before assuming the user is technical.** Default to assuming they are not. The runbook format exists because of that.

## References

- `references/infra-detection.md` — DNS, host, builder and rendering-mode fingerprints
- `references/site-types.md` — the type presets and what each one changes
- `references/technical-checklist.md` — the full checklist with 2026 standards
- `references/report-template.md` — report structure and voice
- `references/runbook-template.md` — **the runbook format and the mandatory safety preamble**
- `references/prompt-craft.md` — how to write prompts that survive contact with a real repo
- `profiles/` — per-site profiles and baselines
