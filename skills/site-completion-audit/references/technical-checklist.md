# Technical checklist — SEO / AEO / GEO / a11y / CWV

Applies to every site type. `site-types.md` adds to it; nothing here is optional.

Standards current as of **August 2026**. Re-verify the dated items each run; they move.

## Crawl & index
- [ ] `robots.txt` exists, allows what you want crawled, references the sitemap — **read the sitemap URL character by character.** A one-letter typo in the domain silently hides the whole site from crawler discovery and is invisible to everyone who works there.
- [ ] `sitemap.xml` complete; `lastmod` reflects **real** modification dates (a request-time timestamp gets discounted by Google); drop `changefreq` and `priority` — Google ignores both
- [ ] **Canonical on every route equals its own absolute URL.** Interior pages canonicalizing to the homepage is a silent de-indexing bug and the single most common failure on SPA frameworks. Check every route, not a sample.
- [ ] No route returns an empty body to a non-JS fetcher
- [ ] Titles unique, no doubled brand suffix
- [ ] Meta descriptions unique and using the available length
- [ ] `og:image` on every route; OG and Twitter tags not inherited from the homepage
- [ ] No orphan pages — everything in the sitemap reachable from navigation
- [ ] No duplicate URLs answering the same question (cannibalization). Programmatic location or topic pages are the usual offender — list every slug competing for one query.
- [ ] **Every number on the site reconciles.** Collect each count, price, rating and statistic into one table and compare. Contradictory figures across pages damage human trust and AI citation equally, and nobody inside the org ever notices.
- [ ] `og:image` is per-page, not one generic file reused sitewide
- [ ] A garbage URL (`/definitely-not-a-page-xyz123`) returns a real 404, not the same shell as real pages

## Structured data
- [ ] `Organization` / `NGO` sitewide — the entity anchor. `legalName`, `url`, `logo`, `sameAs`, `nonprofitStatus`, `taxID`, `founder`, `address`, `contactPoint`
- [ ] `BreadcrumbList` wherever visual breadcrumbs appear — same data source, so they can't diverge
- [ ] `Article` on content pages — `author`, `datePublished`, `dateModified`, `publisher`
- [ ] `MedicalWebPage` + `MedicalCondition` on health content — no rich result, but `reviewedBy` and `lastReviewed` encode the trust signals raters and LLMs read
- [ ] `Person` on author/reviewer bios
- [ ] `WebSite` + `SearchAction` — only if search actually exists
- [ ] **Do NOT build `FAQPage` or `HowTo`.** FAQ rich results ended 7 May 2026; API support removed August 2026. HowTo retired earlier. Cosmetic now.
- [ ] Markup matches visible content exactly — a mismatch risks a manual action

## E-E-A-T / YMYL (health, legal, financial content)
The highest-leverage and most-skipped section.
- [ ] Author byline on every page, linking to a substantive bio
- [ ] **Named reviewer with credentials** — for health content produced by a non-clinical org this is the single most important signal
- [ ] Never display "Last reviewed" without naming who reviewed it. An unverifiable review claim is worse than none.
- [ ] `datePublished` and a visible `Last reviewed`, on a stated cycle
- [ ] Citations **hyperlinked** to primary sources (PubMed, PMC, GeneReviews, NIH/NINDS, CDC, FDA). A bare source category ("PubMed; clinicaltrials.gov") is not a citation.
- [ ] `/editorial-policy` — sourcing standards, evidence grading, review cadence, correction process, AI-use policy
- [ ] Conflict-of-interest and funding disclosure
- [ ] Medical disclaimer on **every** page a patient might carry into a clinical encounter, not just the encyclopedic ones
- [ ] No page relies on templated boilerplate repeated verbatim across many URLs — that's the pattern Google's scaled-content-abuse policy targets

**Consequence of getting this wrong:** no discrete "health penalty" exists. The real mechanisms are algorithmic demotion at the next core update (recoverable only at the following one — months of suppressed traffic), manual actions for scaled content abuse or misleading functionality (a non-functional symptom checker qualifies), and loss of AI citation, which correlates with the top-10 ranking you no longer hold.

## AEO / GEO
- [ ] Every page leads with a self-contained, quotable answer in the first one or two sentences
- [ ] That opening sentence doubles as the meta description
- [ ] Descriptive H2/H3 per subtopic — headings are what AI answers extract
- [ ] Definition sentences an LLM can lift and attribute
- [ ] Topical depth across **question variations**, not just head terms. Pages ranking for the main query plus at least one fan-out variation showed 161% higher AI-Overview citation odds; 76.1% of AIO-cited pages rank in Google's top 10. Classic ranking is still the dominant input.
- [ ] Chatbots are a different surface — only ~12% of ChatGPT/Gemini/Copilot citations rank in Google's top 10 (Perplexity ~28.6%). Favors deep canonical pages over head-term chasing.
- [ ] Facts as text, never locked in images or PDFs
- [ ] An AI-facing entity page (one, not two) with canonical descriptions, citation guidance, and disambiguation from sibling entities — linked from the footer, not orphaned
- [ ] `llms.txt` — **no official support from Google, OpenAI, or Anthropic.** Ship 20 lines because it's free; budget nothing against it.

### Crawler posture, if you want to be cited
| Vendor | Token | Purpose | Set to |
|---|---|---|---|
| OpenAI | `OAI-SearchBot` | ChatGPT search citations | Allow |
| OpenAI | `ChatGPT-User` | User-initiated fetches | Allow |
| OpenAI | `GPTBot` | Training only | Values call — no citation effect |
| Anthropic | `Claude-SearchBot` | Search relevance | Allow |
| Anthropic | `Claude-User` | User-initiated fetches | Allow |
| Anthropic | `ClaudeBot` | Training only | Values call |
| Perplexity | `PerplexityBot` | Surfaces and links you | Allow |
| Google | `Google-Extended` | Gemini grounding; blocking does NOT affect Search or AIO ranking | Allow to be groundable |
| Apple | `Applebot` | Siri/Spotlight/Safari | Allow |
| Apple | `Applebot-Extended` | Training only | Values call |
| Microsoft | `Bingbot` | Bing + Copilot | Allow |

Verify bots by published IP JSON, not UA string. **Check the WAF** — most "AI blocks" are accidental Cloudflare rules, not robots.txt. Avoid `nosnippet` and `max-snippet`; they suppress AI-Overview inclusion.

## Trust & compliance
- [ ] Legal status claim matches evidence (EIN, registration, determination date)
- [ ] Donation path works end to end, or Donate is removed from nav
- [ ] Every form: real endpoint, success state, error state, labeled inputs, spam protection
- [ ] Privacy policy describes what the site **actually** does — read the code, don't boilerplate it
- [ ] Terms of use, medical disclaimer, correction process
- [ ] Financial transparency: 990, annual report, or an honest statement of where you are
- [ ] Real humans named with real photos
- [ ] Physical address, phone, real contact email — no "(placeholder)"

### Google Ad Grants ($10k/mo) — eligibility gates
- Own 501(c)(3), or coverage under a sponsor's IRS **group exemption** using your own EIN. **Fiscally sponsored orgs without their own determination and not under a group exemption are not eligible.** Validation is via **Goodstack** (no longer TechSoup).
- Hospitals and healthcare *providers* are ineligible; their charitable foundations, and health *information/education* charities, are eligible.
- Site: HTTPS sitewide, substantial unique mission content, **no broken links or 404s**, **working donation and contact forms**, mission and EIN stated, mobile-responsive and fast, **minimal non-mission commercial activity**, no AdSense or affiliate links.
- Ongoing: ≥5% account CTR monthly (two consecutive misses = deactivation), valid conversion tracking with ≥1/month, conversion-based Smart Bidding, ≥2 sitelinks, ≥2 ad groups per campaign, specific geo-targeting, no single-word or overly generic keywords, annual survey.

## Crisis safety (any site touching mental health)
- [ ] Crisis resource on **every** page, not just the crisis articles — check pathways, calming pages, grief pages, and anything with an emotional title first; those are the ones that get missed
- [ ] 988 (call **and** text), "Text HOME to 741741", and **911** all named explicitly. "Contact your local emergency number" is not good enough.
- [ ] Numbers are tappable `tel:` and `sms:` links
- [ ] Every crisis link resolves — test them, don't assume
- [ ] No string-concatenation bugs in crisis copy (`988to`, `741741or`). Grep for a digit immediately followed by a lowercase letter.

## Accessibility — WCAG 2.2 AA
New in 2.2 at AA: **2.4.11 Focus Not Obscured**, **2.5.7 Dragging Movements**, **2.5.8 Target Size (24×24 CSS px)**, **3.3.8 Accessible Authentication**. Level A adds 3.2.6 Consistent Help and 3.3.7 Redundant Entry. 4.1.1 Parsing was removed.

Top failures on a React/Tailwind site, in WebAIM Million order:
1. Low contrast — `text-gray-400/500` on white, `text-white/60` on overlays. Fix at the token level.
2. Icon-only buttons with no accessible name
3. Missing or wrong `alt`
4. Unlabeled form inputs — placeholder is not a label
5. `focus:outline-none` with no replacement ring
6. Sticky header obscuring focus (2.4.11) — `scroll-margin-top`
7. Targets under 24×24 (2.5.8) — footer link lists, icon rows
8. `<div onClick>` instead of `<button>`
9. Custom modals/dropdowns — no focus trap, no Escape, no focus return
10. SPA route changes not announced; missing `<html lang>`, skip link, heading order

**Legal:** ADA Title II (WCAG 2.1 AA) covers state/local government, **not nonprofits** — and DOJ extended its deadlines in an April 2026 interim rule (50k+ entities to 26 Apr 2027, smaller to 26 Apr 2028), currently under challenge. Nonprofits are still exposed via **Title III** as places of public accommodation — no DOJ web regulation, but courts apply WCAG AA by consent decree, and there were 8,667 federal Title III filings in 2025. Also Section 504/508 flow-down if federal funds are involved. Target 2.2 AA; it's a superset.

## Core Web Vitals
LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1, at the **75th percentile of field data** (CrUX / Search Console). INP is still the responsiveness metric; there is no successor.

The Soft Navigations API is in its final origin trial (Chrome 147–149) and soft navigations are **not yet counted**. So on an SPA only the initial load is scored today — which makes first paint disproportionately important.

- **LCP** — client-only rendering delays the LCP candidate behind JS download → parse → hydrate. Prerender/SSR the content routes, preload the hero with `fetchpriority="high"`, never lazy-load it, self-host fonts with `font-display: swap`, split routes.
- **INP** — one giant hydration task; un-memoized context providers re-rendering on every keystroke; unvirtualized lists; synchronous third-party scripts. Use `startTransition`/`useDeferredValue` on filter and search inputs, `React.memo`, stable context values, `scheduler.yield()` to break up >50ms tasks.
- **CLS** — images without `width`/`height` or `aspect-ratio`, fonts swapping without metric-matched fallbacks, banners injected above the fold, skeleton→content swaps.

Lighthouse cannot measure INP. Use field data for the real number.
