# Writing prompts that survive contact with a real repo

## Self-contained, always
The person pasting has not read the audit. State the current broken state — **with verbatim strings** — before the fix. "Fix the canonical tags" is useless. "At least `/grants`, `/faq` and `/for-ai` emit `<link rel=\"canonical\" href=\"https://example.org\">`, which is the signature of a default in index.html that only some routes override" gives the model somewhere to start.

## Structure
1. **Context** — what's broken now, quoted exactly, with URLs
2. **Tasks** — numbered, each independently verifiable
3. **Constraints** — what not to touch, which patterns to match
4. **Acceptance criteria** — a checkable list, not a vibe
5. **Verify** — a concrete command or walkthrough, output pasted back

## Model selection
- **Opus** where a wrong call is expensive: reconnaissance, database schema and access rules, architecture, security, anything touching legal wording or money.
- **Sonnet** for high-volume mechanical work against a clear spec: string deletions, content pages, schema across many files, accessibility remediation.
- Say which, in the step, with the literal `/model` command.

## Things that go wrong without an explicit instruction
- The model invents a reviewer, an EIN, a statistic, a date, or a media contact. Forbid it by name.
- The model emits schema for content that isn't on the page — which risks a manual penalty. State that markup must match visible content.
- The model "helpfully" pushes to main, or force-pushes, or discards another session's uncommitted work. The safety preamble covers this; never omit it.
- The model builds `FAQPage` or `HowTo` schema out of habit. Both are retired; say so.
- The model migrates a framework because it's newer. Require a reasoned recommendation and a STOP before any migration.
