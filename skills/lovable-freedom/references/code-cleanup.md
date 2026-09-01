# De-Lovable-ify: code cleanup reference

The goal of the code phase is a repo that builds and runs with **zero Lovable
dependencies**, looks and behaves identically to the live site, and has stronger SEO
foundations. Below is the checklist, then a paste-ready Claude Code prompt that
executes it defensively (Lovable output varies between projects, so the prompt
recons first and asks before deleting anything ambiguous).

## Checklist

**Remove Lovable coupling**
- `lovable-tagger` — a dev-only Vite plugin (`componentTagger()`). Remove it from
  `vite.config.ts` and from `devDependencies` in `package.json`.
- `index.html` — remove any `<script>` from `gpteng.co` / `gptengineer.js` and any
  "Edit with Lovable" badge markup. Keep all legitimate meta tags.
- Search the whole repo (case-insensitive) for `lovable`, `gptengineer`, `gpteng`,
  `r2.dev`, and any `*.lovable.app` URLs. Resolve each hit.
- `README.md` — replace Lovable boilerplate with a real project README (name, stack,
  `npm install` / `npm run dev` / `npm run build`).

**Bring images home**
- Find images served from Lovable's Cloudflare R2 bucket (`*.r2.dev`), including the
  OG/Twitter preview image in `index.html`.
- Download them into `/public/images/` and repoint references to a local path
  (`/images/...`) or an absolute URL on the user's own domain for OG tags.
- Rationale: hotlinked R2 assets can break if Lovable purges them later. Owning the
  files removes that risk.

**Prove independence**
- Delete `node_modules` and `dist`, then `npm install && npm run build` from scratch.
  A clean build with no Lovable packages is the concrete proof the site is free.

**Enhance (optional, non-destructive)**
- Strong `<title>` + meta description; valid Open Graph + Twitter card tags pointing
  at the local OG image and the real domain.
- `public/robots.txt` (allow all, reference sitemap) and `public/sitemap.xml`.
- Favicon set. Alt text on images, labels on icon buttons (quick a11y wins).
- If the app uses client-side routing, add a host rewrite so deep links resolve
  (e.g. `vercel.json` rewriting all routes to `/index.html`).

## Paste-ready Claude Code prompt

Clone the repo, `cd` in, run `claude`, and paste this:

```
You are helping me fully own a website that was built on Lovable. This repo is a
Vite + React + TypeScript + Tailwind + shadcn/ui app. Goal: remove every Lovable
dependency/hook, keep the site visually and functionally identical, strengthen SEO,
and make it build cleanly for hosting on Vercel (or another static host).

Work in phases. After each phase, summarize what changed and WAIT for my "go".
Never force-push. Do all work on a new branch `own-it`.

PHASE 0 — RECON (read-only): create branch `own-it`; print the structure,
package.json, vite.config.ts, index.html; grep the whole repo case-insensitively for
"lovable", "gptengineer", "gpteng.co", "r2.dev", "lovable-tagger", and *.lovable.app
URLs; give me a table of file/line/match/proposed action. Then STOP.

PHASE 1 — REMOVE LOVABLE DEPS: remove lovable-tagger from vite.config.ts and
package.json; remove any gptengineer/gpteng script and Lovable badge from index.html
(keep real meta tags); replace README with a real one; remove any other Lovable
coupling without touching shadcn/Tailwind. Run npm install && npm run build; fix
breakage; show build output. STOP.

PHASE 2 — IMAGES HOME: find every *.r2.dev image (incl. OG meta image); download into
/public/images/; repoint references locally or to my real domain for OG; rebuild;
list what moved. STOP.

PHASE 3 — SEO/QUALITY (keep the design unchanged): solid title/description; valid
OG + Twitter tags to the local OG image and my domain; add robots.txt + sitemap.xml;
add favicon if missing; fix obvious alt-text/label a11y gaps; add per-route titles
only if it's a multi-route app (ask me first). Rebuild; show head before/after. STOP.

PHASE 4 — SHIP-READY: add vercel.json SPA rewrite only if the app uses client-side
routing; do a clean from-scratch build (rm node_modules dist; reinstall; build);
give me a changelog and the exact git commands to review, commit, push `own-it`, and
open a PR / merge.

Rules: ask before deleting anything ambiguous; preserve exact look/behavior; keep
commits small and labeled per phase.
```
