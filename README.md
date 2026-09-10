# goodyear-skills

Six Claude skills pulled out of actually running things. Each one exists because
a real problem needed solving twice, which is the only good reason to build a system.

Free. MIT. No signup.

| Skill | What it does | Written up |
|---|---|---|
| **lovable-freedom** | Migrates a Lovable project into private ownership — your GitHub repo, your host, your domain, with every Lovable-specific dependency stripped out so nothing can be locked, priced, or taken away. | [Migrate off Lovable and own your site](https://daltongoodyear.com/journal/migrate-off-lovable-own-your-site) |
| **site-completion-audit** | Audits any website for the gap between what it *promises* and what it *does* — features that are conceptual rather than functional, placeholder text in production, broken trust signals, SEO/accessibility defects — then hands back a numbered runbook of prompts that fix them. | [The website audit checklist](https://daltongoodyear.com/journal/website-audit-checklist-small-business-owners) |
| **voice-guardrails** | Stops AI-written prose from reading like AI. Forbidden openers, forbidden phrases, forbidden structural moves, a voice-definition scaffold, and a read-aloud litmus test. Constraints, not encouragement. | [Stop AI writing from sounding like AI](https://daltongoodyear.com/journal/stop-ai-writing-sounding-like-ai-checklist) |
| **credit-file-audit** | Audits every credit file you and your business entities have — personal plus each LLC, DBA, or sole prop — finds provable reporting errors, and generates targeted dispute letters. Ships a standard-library tool that computes FCRA fall-off dates and flags duplicate or mismatched tradelines. | [Why multi-entity owners should audit their credit files](https://daltongoodyear.com/journal/audit-credit-files-multiple-business-entities) |
| **account-access-playbook** | Controls who can post as a business across Facebook Page, Instagram (via a Meta Business Portfolio), Eventbrite-style ticketing platforms, and your own site admin — the real access tiers, the invite flow's dead ends, and the fix for a genuine Meta connected-asset removal deadlock. | [Who can post as your business right now?](https://daltongoodyear.com/journal/who-can-post-as-your-business-access-playbook) |
| **agent-employee-framework** | Decides how much authority to give an AI agent — Claude, Grok, or any agentic tool — by naming it before configuring it, setting a spend cap instead of a permission list, defining five categories that always escalate, and running a numbered-list batch-approval cadence. | [Give your AI agent a budget, not a leash](https://daltongoodyear.com/journal/give-ai-agent-budget-not-a-leash) |

## Install

Add the marketplace, then install the plugin:

```
/plugin marketplace add dgoodyear1/goodyear-skills
/plugin install goodyear-skills@goodyear-skills
```

Or drop any single skill straight into your project by copying its folder into `.claude/skills/`.

## Using a skill

Skills load themselves when the work matches. You can also call one directly:

```
Use the site-completion-audit skill on example.com
```

## Notes

- `site-completion-audit` keeps a per-site profile under `profiles/` so each re-run is a diff against the last one. A blank `_template.md` is included; the real profiles are not.
- `voice-guardrails` asks you to define your own voice first. It deliberately will not imitate a named living writer, and it will not invent experience or numbers to make a draft sound lived-in.

## License

MIT — see [LICENSE](LICENSE). Use them, fork them, ship them in your own work.
