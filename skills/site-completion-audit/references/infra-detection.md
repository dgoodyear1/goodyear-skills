# Infrastructure detection

Do this before the content audit. Auditing a site without knowing what serves it produces confident wrong advice — recommending a platform migration to someone who already migrated, or blaming a host that isn't in the path.

## 1. DNS — where does it actually point?

Use node's `dns` module (this is a name lookup, not web fetching):

```js
node -e '
const dns=require("dns").promises;
(async()=>{ for(const h of ["example.com","www.example.com"]){
  console.log("### "+h);
  for(const [l,f] of [["A",x=>dns.resolve4(x)],["CNAME",x=>dns.resolveCname(x)],
                      ["NS",x=>dns.resolveNs(x)],["TXT",x=>dns.resolveTxt(x)]]){
    try{console.log("  "+l+": "+JSON.stringify(await f(h)))}catch(e){console.log("  "+l+": -")}
  }}})();'
```

**Reading the answers:**

| Signal | Means |
|---|---|
| A `76.76.21.21` or `216.198.79.1`, or CNAME `*.vercel-dns-*.com` | **Vercel** |
| CNAME `*.pages.dev` | Cloudflare Pages |
| CNAME `*.netlify.app`, A `75.2.60.5` | Netlify |
| NS `*.ns.cloudflare.com` | DNS at Cloudflare |
| NS `ns1/ns2.dns-parking.com` | DNS at Hostinger |
| NS `*.domaincontrol.com` | DNS at GoDaddy |
| `*.lovable.app` resolving and serving the site | still hosted on Lovable |
| TXT `replit-verify=`, `netlify=`, stale verifications | leftovers from platforms no longer used — flag for deletion |
| TXT `resend-domain-verification=`, `google-site-verification=` | active services worth noting |

Also fetch `<project>.lovable.app`, `<project>.vercel.app` etc. A 404 there while the real domain works is good evidence the old platform is out of the path.

**Compare siblings.** If the user owns several domains, list them together. Inconsistency (one on Cloudflare DNS, one on Hostinger) is worth surfacing even though it isn't a defect.

## 2. Builder fingerprints

WebFetch converts to markdown and strips `<script>` tags, so absence of a script is *not* evidence. Look for what survives:

- `robots.txt` disallowing `/.lovable`, `/_next`, `/__nuxt` — names the builder outright
- `og:image` or other assets on `*.r2.dev`, `*.lovableproject.com`, `*.builder.io`
- A `<meta name="generator">` value
- An internal build-id meta tag shipped to production
- Footer badges: "Edit with Lovable", "Made with Framer", "Powered by …"

To read raw HTML properly you need either the repo or a browser with JS execution. If neither is available, say what you could and could not determine.

## 3. Rendering mode — the single most consequential detail

Fetch several pages and ask whether the body text came back.

| Observation | Diagnosis |
|---|---|
| Full body text, per-route titles and meta differ correctly | Static generation or SSR. Good. |
| Empty body, identical title on every URL | **Client-rendered SPA with no prerendering.** This is the headline finding — crawlers, LLMs, link previews and JS-disabled visitors all see nothing. |
| Full body on most routes, empty on a few | Not a coverage gap. Almost always a component touching `window`/`document`/`localStorage`/`matchMedia` during the build render, throwing, and falling back to the shell. Name the routes; the fix is a `typeof` guard or a move into `useEffect`. |
| Different content for a bot user-agent | A UA-gated prerender service. Note the fragility. |

**Always run the garbage-URL control**: fetch `/this-page-definitely-does-not-exist-xyz123`. If it returns the same shell as real pages, every URL is a soft 404 and no page-level finding is trustworthy. Report that and stop the content audit.

## 4. From the repo, if you have it

`package.json`, `vite.config.ts`, and the root config files settle rendering definitively:

| Fingerprint | Framework |
|---|---|
| `@react-router/dev`, `react-router.config.ts`, `app/routes.ts` | React Router v7 framework mode |
| `vite-react-ssg` dep, `"build": "vite-react-ssg build"` | vite-react-ssg |
| `vike` / `vike-react`, `+Page.tsx` | Vike |
| `@tanstack/react-start`, `routeTree.gen.ts` | TanStack Start |
| `astro.config.mjs` | Astro |
| `next` dep, `app/**/page.tsx` | Next.js |
| `vite-prerender-plugin`, `react-snap`, a `postbuild` script | a prerender bolt-on |
| committed `.vercel/output/`, or `api/` + a catch-all rewrite | Vercel Build Output API or a render function |

Then `npm run build` and count emitted `.html` files. Roughly one per route means build-time static generation; one means runtime rendering.

## 5. Backend and data

- Check the user's connected accounts (Supabase, Cloudflare, etc.) for a project belonging to this site. **Absence is a finding** — a site with forms and no database is a site whose forms go nowhere.
- Where a database exists, check row-level security on every table. Confirm policies are actually restrictive, not merely present. `using (true)` is not security.
- Never let a service-role or secret key be reachable from client code. On Vite, that means never `VITE_`-prefixed.

## 6. What to write into the profile

Host, DNS provider, builder, rendering mode, backend, sibling properties, stale records to clean up, and anything you could not determine plus the check that would settle it.
