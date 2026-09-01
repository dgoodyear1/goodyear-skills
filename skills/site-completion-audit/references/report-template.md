# Report structure

Write in this order. The order is the argument.

## 1. Header
Site, date, method (how many URLs, how fetched, what could not be verified), next scheduled re-audit.

## 2. Diff — on any re-run, this comes first
CLOSED / REGRESSED / STILL OPEN (with age) / NEW. Verify closures on the live site.

## 3. TL;DR
Six to nine numbered findings in consequence order. Lead with one honest sentence about what's genuinely good — then the things carrying legal, safety or credibility risk. Every finding carries a verbatim quote or a specific URL. No sentence that could describe any website.

## 4. The core finding
**One architectural insight, not a list.** What single pattern explains most of the individual defects? Give it its own heading, support it with a table of "what it's called" against "what it actually is", and end with the one decision that resolves the whole class. This is the section the user is paying for.

## 5. Severity ledger
`# | Finding | Severity P0–P3 | Effort XS/S/M/L | Class`. Every numbered finding recurs by number in the detail below. Classes: Safety, Legal, Integrity, Function, SEO, E-E-A-T, IA, Content, Conversion, Polish, Missing.

## 6. Detail by priority
**P0 — fix before sending another person to this site.** Safety, legal, integrity only. Verbatim evidence and a specific remedy each. Where the fix needs a fact only the owner has, state the decision required rather than guessing.

**P1 — what is conceptual and reads as real.** The vapor. Also, explicitly: **what is genuinely strong and should be protected.** Naming the good work specifically is what makes the criticism land.

**P2 — SEO / AEO / GEO.** Lead with whatever is actively hurting today. Say which recommendations you're declining to make, and why.

**P3 — what doesn't exist yet.** Full section specs, not "add a press page".

## 7. Type-specific sections
Ad Grants eligibility, local SEO, booking funnel, accessibility, governance — only what's real for this site.

## 8. Sequenced plan
Sprint 0 is a few hours and mostly deletion, requiring no decisions and no dependencies. Each sprint gets a duration and a one-line theme.

## 9. Appendix
Every source URL, grouped.

## Voice
Direct. No hedging, no consultant padding, no "consider potentially exploring". Say what's broken, quote it, say what to do. Warm toward the person, unsparing about the site. Assume they built this, are proud of parts of it, and asked precisely because they want the truth.
