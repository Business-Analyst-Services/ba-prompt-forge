---
name: ba-quality-framework-and-review-cadence
description: 'Use when the user is working on requirements quality assurance & review and needs quality framework, review cadence, quality checklists. Define the quality framework: checklists per artefact type, review levels, and a cadence the team can sustain. Produces a reviewable first draft for the ba team (daily use), governance (assurance model).'
license: CC-BY-4.0
---

# Quality Framework & Review Cadence

Derived from `LB-03-D2` in the BA Prompt Forge library
(Lead BA / Requirements Quality Assurance & Review, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing requirements quality assurance & review work and needs one of:
- Quality Framework
- Review Cadence
- Quality Checklists

The audience for whatever you produce is: **The BA team (daily use), governance (assurance model)**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[PROGRAM/PROJECT, NUMBER OF BAs AND WORKSTREAMS, DELIVERY METHOD]`
3. `[LIST]`
4. `[NUMBERS/LEVELS]`
5. `[WHAT'S GONE WRONG BEFORE]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Define the quality framework: checklists per artefact type, review levels, and a cadence the team can sustain. Draft the framework. Justify every mandatory review step by the failure it prevents — cut any that can't be justified.

Format the output exactly as follows:

> Per artefact type: quality checklist (5-8 criteria, each testable, mapped where relevant to the pain I described). Review model: what gets self-checked vs peer-reviewed vs lead-reviewed, with the trigger (risk, author level, artefact criticality) — not blanket review of everything. Cadence and turnaround expectations; sign-off record structure; lightweight metrics (findings per artefact trending down).

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example review-trigger rule: "Lead review required only when: artefact feeds a go/no-go or procurement decision; author is <6 months in practice; or prior artefact from this package had a blocker. Everything else: peer review. (Prevents: review bottleneck at the lead — last program lost ~4 days/artefact.)"

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
