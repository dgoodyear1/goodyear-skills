#!/usr/bin/env python3
"""
Credit File Audit -- fall-off calculator and duplicate/discrepancy flagger.

Standard library only. Takes the tradeline table (one row per tradeline, across every
file pulled -- personal and every business entity) as a CSV and does two things a
spreadsheet won't do for you automatically:

1. Computes the FCRA fall-off date for every negative tradeline (date of first
   delinquency + 7 years), and flags anything close to fall-off as a hold rather than
   a dispute target -- disputing something about to age off on its own is wasted effort.
2. Flags likely duplicates and discrepancies: the same creditor + account last-4
   appearing more than once (possible double-reporting across entities or bureaus),
   and balances that disagree across rows for what looks like the same tradeline.

It does NOT file disputes, contact bureaus, or determine whether a flag is actually an
error -- that always requires the original document. It only tells you where to look
first.

CSV columns expected (header row required, extra columns ignored):
    creditor, entity, bureau, account_last4, date_opened, dofd, chargeoff_date,
    original_principal, current_balance, status

Any of date_opened / dofd / chargeoff_date may be blank. Dates: YYYY-MM-DD.

Usage:
    python3 falloff_and_duplicates.py tradelines.csv --report report.json
"""
from __future__ import annotations
import argparse, csv, json, sys
from datetime import date, timedelta
from pathlib import Path

FALLOFF_YEARS = 7
DOFD_TO_CHARGEOFF_DAYS = 180  # typical issuer practice; used only to sanity-check, never to invent a date
SOON_WINDOW_DAYS = 180


def parse_date(s: str):
    s = (s or "").strip()
    if not s:
        return None
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%m-%d-%Y"):
        try:
            from datetime import datetime
            return datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    return None


def add_years(d: date, years: int) -> date:
    try:
        return d.replace(year=d.year + years)
    except ValueError:
        # Feb 29 on a non-leap target year
        return d.replace(month=3, day=1, year=d.year + years)


def load_rows(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = []
        for i, raw in enumerate(reader):
            row = {(k or "").strip().lower(): (v or "").strip() for k, v in raw.items()}
            row["_row"] = i + 2  # 1-indexed + header
            rows.append(row)
        return rows


def analyze(rows: list[dict], today: date) -> dict:
    falloffs, duplicates, discrepancies = [], [], []

    for row in rows:
        dofd = parse_date(row.get("dofd", ""))
        chargeoff = parse_date(row.get("chargeoff_date", ""))
        note = None
        effective_dofd = dofd
        if effective_dofd is None and chargeoff is not None:
            effective_dofd = chargeoff - timedelta(days=DOFD_TO_CHARGEOFF_DAYS)
            note = ("no DOFD given -- estimated from charge-off date minus "
                    f"{DOFD_TO_CHARGEOFF_DAYS} days; pull the original DOFD before relying on this")
        if effective_dofd is None:
            continue

        falloff = add_years(effective_dofd, FALLOFF_YEARS)
        days_out = (falloff - today).days
        entry = {
            "row": row["_row"],
            "creditor": row.get("creditor", ""),
            "entity": row.get("entity", ""),
            "bureau": row.get("bureau", ""),
            "account_last4": row.get("account_last4", ""),
            "dofd_used": effective_dofd.isoformat(),
            "dofd_source": "reported" if dofd else "estimated_from_chargeoff",
            "falloff_date": falloff.isoformat(),
            "days_until_falloff": days_out,
            "status": "already_past_falloff" if days_out < 0 else
                      ("closing_soon" if days_out <= SOON_WINDOW_DAYS else "open"),
        }
        if note:
            entry["note"] = note
        falloffs.append(entry)

        # sanity check: reported chargeoff far from the DOFD-implied window is itself a re-aging lead
        if dofd and chargeoff:
            implied = dofd + timedelta(days=DOFD_TO_CHARGEOFF_DAYS)
            drift_days = abs((chargeoff - implied).days)
            if drift_days > 120:
                discrepancies.append({
                    "row": row["_row"], "creditor": row.get("creditor", ""),
                    "kind": "chargeoff_date_drift",
                    "detail": (f"charge-off is {drift_days} days from the "
                               f"DOFD+{DOFD_TO_CHARGEOFF_DAYS}-day expectation -- "
                               "worth checking for re-aging"),
                })

    # duplicate / discrepancy pass: same creditor + last4 appearing more than once
    by_key: dict[tuple, list[dict]] = {}
    for row in rows:
        key = (row.get("creditor", "").strip().lower(), row.get("account_last4", "").strip())
        if not key[0] or not key[1]:
            continue
        by_key.setdefault(key, []).append(row)

    for (creditor, last4), group in by_key.items():
        if len(group) < 2:
            continue
        entities = {g.get("entity", "") for g in group}
        bureaus = {g.get("bureau", "") for g in group}
        balances = {g.get("current_balance", "") for g in group}
        duplicates.append({
            "creditor": creditor, "account_last4": last4,
            "appears_on_rows": [g["_row"] for g in group],
            "distinct_entities": sorted(x for x in entities if x),
            "distinct_bureaus": sorted(x for x in bureaus if x),
            "balance_agreement": "consistent" if len(balances) <= 1 else "MISMATCHED",
            "detail": ("same creditor + last-4 appears on multiple rows -- check for "
                       "duplicate reporting or wrong-entity attribution before assuming "
                       "these are genuinely separate accounts"),
        })

    falloffs.sort(key=lambda e: e["days_until_falloff"])
    return {
        "analyzed_at": today.isoformat(),
        "row_count": len(rows),
        "falloff_schedule": falloffs,
        "possible_duplicates": duplicates,
        "date_discrepancies": discrepancies,
        "summary": {
            "already_past_falloff": sum(1 for e in falloffs if e["status"] == "already_past_falloff"),
            "closing_within_6mo": sum(1 for e in falloffs if e["status"] == "closing_soon"),
            "possible_duplicate_groups": len(duplicates),
        },
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv_path", type=Path)
    ap.add_argument("--report", type=Path, default=Path("falloff_report.json"))
    a = ap.parse_args()

    if not a.csv_path.exists():
        print(f"error: {a.csv_path} not found", file=sys.stderr)
        return 2

    rows = load_rows(a.csv_path)
    if not rows:
        print("error: no rows found -- check the CSV has a header row", file=sys.stderr)
        return 2

    result = analyze(rows, date.today())
    a.report.write_text(json.dumps(result, indent=2), encoding="utf-8")

    s = result["summary"]
    print(f"{result['row_count']} tradelines analyzed -> {a.report}")
    print(f"  {s['already_past_falloff']} already past fall-off (should not still be reporting -- dispute these first)")
    print(f"  {s['closing_within_6mo']} falling off within 6 months (hold -- don't spend effort disputing these)")
    print(f"  {s['possible_duplicate_groups']} possible duplicate/multi-entity groups -- see report for details")
    if s["already_past_falloff"]:
        print("\n  Anything past its fall-off date and still on your report is a strong, "
              "fast dispute -- the date alone is often enough.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
