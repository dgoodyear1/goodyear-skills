# Credit File Audit

A Claude skill that audits every credit file a person and their business entities have — personal plus each LLC, DBA, or sole prop — finds provable reporting errors, and generates targeted dispute letters. Not a credit repair pitch: accurate negative information isn't disputed, and the skill says so plainly.

## Install

Drop `SKILL.md` and `scripts/` into your skills directory (`~/.claude/skills/credit-file-audit/` for Claude Code / Claude Desktop, or your project's skill path), or point your marketplace config at this repo.

## Worked example

```
python3 scripts/falloff_and_duplicates.py tradelines.csv --report report.json
```

Given a tradeline table (one row per account, across every file you pulled), it computes the FCRA fall-off date for every negative item, flags anything already past its fall-off date that shouldn't still be reporting, and flags same-creditor/same-account rows that show up more than once across entities or bureaus — the two checks a spreadsheet won't do for you automatically.

Then invoke the skill itself in a Claude session ("audit my credit files") and it runs the full interview → gather → table → taxonomy → dispute → track workflow end to end.

## The full system

This skill covers the method. The full **Credit File Audit Pack** adds the tradeline table template, ready-to-send dispute letters for all seven error types, a response tracker, and a worked example carried start to finish — [daltongoodyear.com/journal](https://daltongoodyear.com/journal).

## License

MIT.
