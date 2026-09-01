# Hosting reference: choosing and configuring the new home

All three options below are free for a personal/brand site, deploy automatically on
every `git push`, and fully deliver "ownership" (the user's repo + their host + their
domain). The Lovable app is a static Vite build (`npm run build` → `dist/`), so any
static host works.

## Quick recommendation

- **Default: Vercel.** Simplest path, best DX, one-click GitHub import, auto-detects
  Vite. If the user has used it before, stay here — zero learning curve.
- **Cloudflare Pages** — pick this if the user wants to consolidate everything under
  Cloudflare (especially if their images already live on Cloudflare R2, or Cloudflare
  already manages their DNS). One dashboard for DNS + images + hosting.
- **Netlify** — pick this if they want built-in form handling (handy for a contact /
  "book me to speak" form) without wiring up a separate service.

Don't over-optimize this choice; the ownership win is identical across all three. Go
with what the user already knows unless they have a specific reason to switch.

## Vercel

**Import:** Add New → Project → Import the GitHub repo → accept the Vite defaults
(build `npm run build`, output `dist`) → Deploy. Live `*.vercel.app` URL in ~60s.

**Custom domain:** Project → Settings → Domains → add the apex domain and `www`.
Vercel shows the DNS records (an `A` record for the apex, usually `76.76.21.21`, and
a `CNAME` for `www` → `cname.vercel-dns.com`; follow whatever Vercel actually
displays). It auto-issues SSL once DNS resolves.

**SPA routing:** if deep links 404, add `vercel.json` with a rewrite of all routes to
`/index.html`.

## Cloudflare Pages

**Import:** Workers & Pages → Create → Pages → Connect to Git → pick the repo →
framework preset **Vite**, build `npm run build`, output `dist` → Save and Deploy.

**Custom domain:** Pages project → Custom domains → add the domain. If Cloudflare
already manages the DNS zone, it wires the records automatically — this is the big
convenience if the user is already on Cloudflare.

**SPA routing:** add a `public/_redirects` file containing `/*  /index.html  200`.

## Netlify

**Import:** Add new site → Import an existing project → pick the repo → build
`npm run build`, publish directory `dist` → Deploy.

**Custom domain:** Site configuration → Domain management → add domain, then either
point DNS at Netlify or use Netlify DNS. Auto-SSL via Let's Encrypt.

**SPA routing:** add a `public/_redirects` file with `/*  /index.html  200`.

## DNS cutover notes (applies to any host)

- Find where the domain's DNS currently lives before starting: the registrar
  (GoDaddy, Namecheap, Google Domains/Squarespace, etc.) or Cloudflare.
- The record pointing at Lovable is the one to change — repoint it at the new host
  using the values the host displays.
- Propagation is usually minutes but can take a couple hours. The old site keeps
  serving until the record flips, so there's no downtime window.
- Keep the Lovable project alive until the real domain is confirmed on the new host;
  then remove the domain from Lovable and retire the project.
