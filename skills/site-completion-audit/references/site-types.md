# Site types

The type decides half the checklist. Pick one in Phase 0 and audit against it. A lodging business and a health nonprofit fail in completely different ways.

Everything in `technical-checklist.md` applies to every type. This file is what gets *added*.

---

## nonprofit-health (YMYL)
*Health information, patient support, rare disease, mental health.*

**Expected pages:** /about, /programs, /donate, /contact, /privacy, /terms, /financials or annual report, /press, /roadmap, /editorial-policy, /medical-review-board, /team or /board

**Adds to the checklist:**
- **E-E-A-T is the ceiling on everything.** Author byline on every page; a named clinical reviewer with credentials; published and last-reviewed dates; citations hyperlinked to primary sources (PubMed, PMC, GeneReviews, NIH/NINDS, CDC, FDA); an editorial policy naming the sourcing standard, review cadence, correction process, and AI-use policy.
- **Never display "Last reviewed" without naming the reviewer.** An unverifiable review claim is worse than none.
- Medical disclaimer on every page a patient might carry into a clinical appointment — not just the encyclopedic ones.
- Charity status claim vs. evidence: EIN, determination date, or a named fiscal sponsor. An unbacked claim next to a solicitation is a regulator issue.
- Working donation path with a named processor.
- Financial transparency: Form 990, annual report, or an honest statement of where they are.
- **Crisis safety** — see the block below. Always P0.
- Google Ad Grants eligibility, if they'd want the $10k/month: own 501(c)(3) or group-exemption coverage (fiscal sponsorship alone does **not** qualify); no broken links; working donation and contact forms; minimal non-mission commercial activity.
- Schema: `Organization`/`NGO`, `Article` + `MedicalWebPage` with `reviewedBy` and `lastReviewed`, `MedicalCondition`, `Person`, `BreadcrumbList`.

## nonprofit-general
As above, minus the medical review layer. Keep: charity status, donation path, financial transparency, board and staff named, privacy and terms, press and roadmap. Apply the crisis block if the population served is at elevated risk (veterans, first responders, recovery, youth, domestic violence, housing insecurity).

## commercial-local (hospitality, service business, trades)
*Short-term rentals, property management, contractors, clinics, restaurants.*

**Expected pages:** /about, /contact, /services, location pages, /privacy, /terms, /cancellation or refund policy, /reviews

**Adds to the checklist:**
- **NAP consistency** — name, address and phone identical everywhere they appear, and matching the Google Business Profile.
- Google Business Profile linked from `/contact`, not just the homepage. Embedded map. Hours.
- **Licence and registration numbers actually stated**, not just "you can verify our licence" with a link to a search page. Make the visitor's job zero.
- The booking or quote path followed end to end. Name the platform. Check the handoff for tonal and visual breaks, and whether prices appear.
- Cancellation, refund and deposit policies reachable before checkout.
- **Programmatic location pages** — if there are many, sample at least three and say honestly whether they are distinct human prose or one template with swapped nouns. Then check for cannibalization: multiple slugs competing for the same query is endemic here.
- **Number reconciliation is critical** — property counts, review counts and star ratings drift apart across pages fast.
- Per-page `og:image`. A single generic image reused sitewide means every share of every listing looks identical.
- Schema: `LocalBusiness` and its subtype (`LodgingBusiness`, `VacationRental`, `Hotel`), `Product` + `Offer` where a price shows, `AggregateRating` + `Review` where ratings show, `BreadcrumbList`, `Organization`, `WebSite` + `SearchAction`, `Event`.
- Conversion instrumentation: is anything actually tracked?

## personal-brand
*Author, speaker, consultant, portfolio.*

Adds: `Person` schema with `sameAs`; a real bio and headshot; a working contact or booking path; a press or speaking page with a downloadable kit; `Article`/`BlogPosting` with bylines and dates; an RSS feed; consistent identity across linked profiles. Watch for an empty blog in the nav — worse than no blog.

## saas-product
Adds: pricing page with real prices; a status page; docs; a changelog; security and compliance pages; `SoftwareApplication` and `Offer` schema; signup flow followed end to end; trial and cancellation terms stated.

---

## The crisis block

Apply to any site touching mental health, veterans or first responders, grief, chronic or serious illness, caregiving, addiction, or youth.

- A crisis resource on **every** page, not only the crisis articles.
- **Check the emotionally-loaded pages first** — the calming page, the grief page, the "I'm scared" page, the password gate. Those are where it's missing, and those are where it matters.
- All routes named explicitly and correctly, as tappable `tel:` and `sms:` links:
  - General: **988** (call or text), **Text HOME to 741741**, **911**
  - Veterans: **988 then press 1**, **text 838255**
  - "Contact your local emergency number" is not good enough. Name 911.
- Every crisis link resolves. Test them; do not assume.
- No string-concatenation bugs in crisis copy. Grep for a digit immediately followed by a letter — `988to`, `741741or`.
- If the site is gated, under construction, or behind a password, **the crisis resource belongs on the gate page**. A locked door is what an at-risk visitor actually meets.
- Crisis findings are always P0 and always lead the report.
