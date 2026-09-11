# Roadmap

## Shipped

- 126 prompts as structured fields, schema-validated
- Ten prompt frameworks with a per-framework fidelity report
- Prompt-to-skill conversion; all 126 pre-built
- Deterministic scoring with a declared machine/judgement split, enforced in CI
- Master decomposition into 188 testable single-task units
- Three hand-written skills: router, scorer, forge
- Contribution, credit, upvoting and impact, all GitHub-native

## Next

**Regression tests for unit prompts.** Units exist so prompts can be tested;
nothing yet runs them. A test would be a fixture of synthetic input plus
assertions on the output shape — does the KPI table have all nine columns, is
every unverified value flagged `[TBC]`. Shape assertions are cheap and catch real
regressions when a prompt is edited.

**Close the seven flagged gaps.** `contexts/delivery-contexts.yml` records seven
areas the source catalogue never decomposed: procuring AI products, stakeholder
engagement for system updates, story sizing and estimation, agile testing
support, BI requirements governance, agent requirement traceability, agent
evaluation. Each is a known hole.

**A second scorer.** Every score in `library/` is the original author's
self-assessment, checked by machine on six criteria. An independent pass on the
four judgement criteria would be the first real external validation.

## Under consideration

**A hosted front end.** The GitHub-native approach was chosen deliberately —
credit in a field, votes as reactions, impact as files — because it works from
day one with nothing to run. A hosted app would add ranking that combines votes
with field-report outcomes, search across services, and per-prompt usage
telemetry.

It would also add hosting, moderation and an account system, and it would move
the credit record out of the prompt file. Worth doing when enough contributions
and field reports exist that ranking them is a real problem. Not yet.

**Impact tracking beyond self-report.** Field reports are voluntary and
self-selected, which makes them better than rubric scores and still weak
evidence. Stronger would be a structured before/after: time to first usable
draft, edits required, whether the artefact passed review unchanged. That needs
people willing to measure their own work — a bigger ask than a pull request.

**Multi-language.** The prompts are British-English and BABOK-aligned. The field
structure would survive translation; the worked examples would need rewriting per
locale, not translating.

## Not planned

**More prompts for their own sake.** 126 across 42 services is already past the
point where browsing works. The router handles the volume; more volume without a
decomposition gap to fill makes routing harder and the library worse.

**Prompts for non-BA work.** The rubric assumes an analyst producing a reviewable
artefact for a named audience. General-purpose prompt libraries exist and are
better at being general-purpose.
