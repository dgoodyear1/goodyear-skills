---
name: lovable-freedom
description: >-
  Migrate a Lovable project into private ownership — moving the code off Lovable
  into the user's own GitHub repo, hosting (Vercel/Cloudflare Pages/Netlify), and
  domain, and stripping out every Lovable-specific dependency so nothing can be
  locked, priced, or taken away. Use this skill WHENEVER the user wants to "own",
  "export", "get off", "escape", "migrate", "self-host", or "take out of" Lovable
  (or lovable.app / lovable.dev), wants "freedom from Lovable", asks to move a
  Lovable site to GitHub/Vercel, or wants to de-Lovable-ify / clean up a
  Lovable-built app — even if they don't name every step. Covers the full arc:
  GitHub connect, code cleanup, deploy, and DNS cutover, split between browser
  steps and code steps. Also applies to the same pattern for other AI site
  builders (Bolt, v0, Replit) since the mechanics are nearly identical.
---

# Lovable Transfer — privately own a Lovable project

## What this does and why it works

Lovable *feels* like a walled garden, but it isn't one. Every Lovable project is an
ordinary **Vite + React + TypeScript + Tailwind + shadcn/ui** codebase living in a
Git repo. The entire "freedom" problem reduces to one move: **get that repo into the
user's own GitHub account.** Once it's there, Lovable is optional — the user can host
anywhere, edit with anything, and delete the Lovable project without consequence.

So the mental model to hold: *we are not extracting or reverse-engineering anything.
We are relocating a normal web app and unplugging a few Lovable-specific cords.*

The work splits cleanly into two kinds of steps, and it helps the user to name which
is which as you go:
- **Browser steps** (clicking through Lovable, GitHub, the host, DNS) — a human with
  logged-in accounts has to do these, though an agent driving the browser can help.
- **Code steps** (removing Lovable deps, cleaning, enhancing) — done locally with
  Claude Code or an editor.

## The golden rule: never take the live site down

The site is probably already serving real traffic on a custom domain. Sequence the
work so a working version is always live. Specifically: **stand up and fully test the
new host before touching DNS.** DNS is the only step that feels irreversible, so it
goes last, and even it is revertible by flipping the record back. Do not delete the
Lovable project until the new host is confirmed live on the real domain — keep it as
a fallback for a week or so.

## The five phases

Walk the user through these in order. Confirm completion of each before moving on.

### Phase 0 — Accounts (browser)
Make sure the user has:
- A **GitHub account** (this is where ownership lives).
- An account on the target **host** — default recommendation **Vercel**, signed in
  *with GitHub* so they're linked. See `references/hosting.md` to choose a host if
  the user is unsure or wants Cloudflare Pages / Netlify instead.

If the user has none of these, that's fine — create them first; it's 10 minutes.

### Phase 1 — Code into the user's GitHub (browser, inside Lovable)
In the Lovable project: open the **GitHub** integration → **Connect GitHub** →
authorize → **Create Repository**. Lovable pushes the full source into a new repo
under the user's own account.

Verify the repo exists on github.com and contains the code. **This is the pivotal
moment — after this the user owns the source and everything else is safe and
reversible.** Celebrate it; it's the actual "freedom" milestone.

### Phase 2 — De-Lovable-ify the code (code step)
Clone the repo locally and remove Lovable coupling. The full, defensive checklist and
a ready-to-paste Claude Code prompt are in `references/code-cleanup.md`. In short:
- Remove the `lovable-tagger` Vite plugin (from `vite.config.ts` and `package.json`).
- Remove any `gptengineer.js` / `gpteng.co` script and "Edit with Lovable" badge from
  `index.html`.
- Bring images home: anything served from Lovable's R2 bucket (`*.r2.dev`) — including
  the OG/social image in the meta tags — gets downloaded into `/public` and the
  references repointed to the user's own domain.
- Strip Lovable branding from `README`/meta.
- Prove it still builds from scratch (`npm install && npm run build`) with zero
  Lovable dependencies. The clean build is the proof of independence.

### Phase 3 — Deploy to the new host (browser)
Import the GitHub repo into the host. Vercel/Netlify/Pages all auto-detect Vite
(build `npm run build`, output `dist`). Deploy, then **test everything on the
temporary host URL** (e.g. `*.vercel.app`) — this is the new site before it's on the
real domain. Host-specific notes: `references/hosting.md`.

### Phase 4 — Cut over the domain (browser — the careful one)
1. In the host, add the custom domain; it will show the required DNS records.
2. Find where the domain's DNS currently lives (registrar, or Cloudflare if the user
   uses R2). Update the record that points at Lovable so it points at the new host.
3. Wait for propagation (minutes–hours); the host auto-issues SSL. Confirm the real
   domain now serves the new site.
4. Only then: remove the custom domain from Lovable and retire/downgrade the project.

If anything looks wrong mid-cutover, revert the DNS record — the old Lovable site is
still there as a safety net until step 4.

## Optional: enhance while you're in there
Owning the repo is the moment to fix fundamentals the user couldn't easily touch on
Lovable — real SEO/OG tags, `sitemap.xml`, `robots.txt`, favicon, analytics they own,
and (for personal-brand/writing sites) an MDX blog. Keep the visual design intact
unless asked; enhancement means strengthening foundations, not redesigning. Offer
these; don't force them into the migration.

## How to run this with a user
- Establish where they are (do they have GitHub? a host account? is GitHub already
  connected?) before prescribing steps — don't repeat work they've done.
- Clearly hand off code steps to Claude Code / local editing, and offer to drive the
  browser for the click-through steps.
- Track the phases as a checklist so a returning user sees exactly what's left.
- The deliverable mindset: at the end, the user's site runs entirely on assets they
  control, and Lovable could vanish tomorrow with zero impact.

## Reference files
- `references/code-cleanup.md` — full de-Lovable-ify checklist + paste-ready Claude
  Code prompt.
- `references/hosting.md` — Vercel vs Cloudflare Pages vs Netlify, and per-host
  import/DNS specifics.
