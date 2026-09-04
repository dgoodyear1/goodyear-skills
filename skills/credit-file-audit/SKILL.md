---
name: credit-file-audit
description: "Audit every credit file (personal + each business entity) line by line, find provable reporting errors, generate targeted dispute letters, and track responses. Use for credit report review, disputes, charge-off cleanup, or pre-mortgage credit prep."
---

# Credit File Audit

Find and fix **provable errors** across every credit file a person and their entities have. This is not a credit repair pitch. Accurate negative information cannot be removed and should never be disputed — disputing accurate items wastes time, can backfire near a mortgage application, and is what predatory firms sell. The goal is a complete, correct picture and a short list of genuine, documented errors.

## When this applies

Strongest when the person has:
- Multiple business entities, especially ones formed years apart or abandoned
- Business credit cards personally guaranteed (the balances land on both business and personal files)
- Charge-offs whose balances grew substantially from original principal
- A mortgage, loan, or job with a credit screen coming up

## Step 1 — Interview first, one question at a time

Do NOT start pulling or analyzing until this is answered. Ask each separately and wait:

1. What entities have you ever had credit under? Every LLC, DBA, sole prop — including dissolved ones and ones you barely used.
2. Which accounts did you personally guarantee?
3. What's the deadline driving this — a mortgage, a job, a loan, or just cleanup?
4. Do you have any original statements, agreements, or charge-off notices? Even one is useful.
5. Has anything already been disputed, and what happened?

Write the answers into memory as you go — do not batch them.

## Step 2 — Gather every file

Direct them to pull, and tell them these are free:

**Personal:** annualcreditreport.com — all three bureaus (Equifax, Experian, TransUnion). Pull all three; they often disagree, and the disagreement is where errors surface.

**Business, per entity:** Dun & Bradstreet (D&B) at dnb.com, Experian Business at experian.com/small-business, Equifax Business. Each entity needs its own pull.

**Supporting records worth digging up:**
- IRS Wage & Income transcripts for the charge-off years — reveals whether a 1099-C was issued, which changes what should be reporting
- Old statements showing original principal before fees and interest
- Any settlement or charge-off letters

Have them upload what they get. Read the actual documents; do not work from memory or summary.

## Step 3 — Build the master table

One row per tradeline, across every file. Include:

| Field | Why it matters |
|---|---|
| Creditor + account number (last 4) | Duplicate detection |
| Which file(s) it appears on | Personal, and/or which entity |
| Which bureaus report it | Disagreement between bureaus is a lead |
| Date opened | Re-aging detection |
| **Date of first delinquency (DOFD)** | Drives the 7-year fall-off. Most commonly wrong field. |
| Charge-off date | Should be ~180 days after DOFD |
| Original principal vs current balance | Fee and interest inflation |
| Current status and balance | Should match across bureaus |
| Computed fall-off date | DOFD + 7 years |

Deliver this as an XLSX so they can hand it to a lender or attorney.

## Step 4 — Run the script, then the taxonomy by hand

`scripts/falloff_and_duplicates.py` takes that table as a CSV and does the arithmetic and cross-referencing a human skips under time pressure: computes every fall-off date, flags anything already past its fall-off date that shouldn't still be reporting, and flags same-creditor/same-account-last-4 rows that show up more than once across entities or bureaus.

```
python3 scripts/falloff_and_duplicates.py tradelines.csv --report report.json
```

It does not decide anything — it points at rows worth a document check. Then run every flagged row, and everything else, against the taxonomy:

1. **Duplicate reporting** — same debt appearing twice. Common when an account is reported by both the original creditor and a collector, or under both an entity and the person. Same account number appearing twice with different balances is a hard flag.
2. **Wrong entity attribution** — reported under an entity that never held the account, or under a personal file where no personal guarantee existed. Requires the original agreement to prove.
3. **Re-aging** — DOFD reported later than it actually was, which illegally extends the 7-year clock. Compare against original statements. This is one of the most consequential and most winnable errors.
4. **Balance discrepancies** — the balance disagrees between bureaus, or grew after charge-off. Most issuers stop accruing interest at charge-off; a balance that kept climbing afterward is a flag worth raising.
5. **Status errors** — reported open when settled or paid, balance shown when a 1099-C was issued, or "charged off" persisting after a settlement.
6. **Accounts that shouldn't be there at all** — belonging to someone else, a mixed file, or an account never opened.
7. **Missing accounts** — good history not reporting. Adding it helps as much as removing bad.

Flag only what is **provable from a document**, and say plainly which document proves it.

## Step 5 — Write the disputes

One letter per error, per bureau. Never a scattershot "dispute everything" letter — those get flagged as frivolous and accomplish nothing.

Each letter must contain:
- The specific tradeline and account
- The specific field that is wrong
- What it should say instead
- The document that proves it, attached
- A clear request: correct or delete

File online where possible (each bureau has a dispute portal) — faster and creates a record. The bureau generally has 30 days to investigate.

Also send a direct dispute to the **furnisher** (the creditor itself), not only the bureau. Furnisher disputes carry their own obligations and sometimes work when bureau disputes don't.

## Step 6 — Track and follow through

Build a tracker: error, tradeline, bureau, date filed, response due, outcome, next step.

- Verified as accurate → accept it and move on. Do not re-dispute the same item.
- Corrected → confirm the correction actually appears on a fresh pull.
- Deleted → confirm on all three bureaus; deletions sometimes land on one and not the others.
- No response in 30 days → that itself is a violation worth escalating to the CFPB at consumerfinance.gov/complaint.

## Guardrails — state these plainly to the user

- **Accurate negative information cannot be removed.** Anyone promising otherwise is selling something. Settling a debt changes its status to settled with a zero balance; the tradeline still stays until fall-off.
- **Do not dispute in the 90 days before a mortgage application.** An in-progress dispute can force a manual underwriting downgrade on FHA loans and complicate others.
- **Never claim identity theft or fraud on a debt that is genuinely theirs.** That is a false statement on a federal form, not a strategy.
- **Charge-offs decay.** Scoring weights recency heavily, so a four-year-old charge-off already hurts far less than a fresh one. Time is doing real work.
- **Adding good beats removing bad.** A secured card paid in full monthly, and separately-built business credit under an EIN, move the number faster than most dispute campaigns.

## What to deliver

1. The master tradeline table as an XLSX
2. A one-page plain-English summary: what's accurate, what's disputable, what the real fall-off dates are
3. Dispute letters, ready to send, one per error
4. The tracker
5. A short "stop doing this" list of anything they're currently paying for that can't work

## Model guidance

- **Opus** — the interview, the error analysis, and the dispute letters. Getting the error class and the proof right is what decides whether a dispute works.
- **Sonnet** — building the table, the XLSX, the tracker, and follow-up letters.
