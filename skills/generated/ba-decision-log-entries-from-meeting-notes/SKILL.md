---
name: ba-decision-log-entries-from-meeting-notes
description: Use when the user is working on requirements governance & traceability and needs decision log. Extract and formalise every decision into audit-ready decision log entries. Produces a reviewable first draft for governance forums and future team members needing the 'why'.
license: CC-BY-4.0
---

# Decision Log Entries from Meeting Notes

Derived from `BT-05-D2` in the BA Prompt Forge library
(Business/Tech BA / Requirements Governance & Traceability, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing requirements governance & traceability work and needs one of:
- Decision Log

The audience for whatever you produce is: **Governance forums and future team members needing the 'why'**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[PASTE]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Extract and formalise every decision into audit-ready decision log entries. Extract the entries. Where the notes imply but do not state a decision, put it in the 'not decided' table with a question to close it out.

Format the output exactly as follows:

> Per decision: ID; date; decision statement (one sentence, unambiguous); decision maker and forum; rationale; alternatives considered and why rejected; requirements/artefacts impacted; follow-up actions. Separate table for items discussed but NOT decided, to prevent phantom decisions.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example entry: "D-014 | 15/07/2026 | Decision: service requests older than 7 years will be archived, not migrated | Decider: Data Governance Board | Rationale: retention schedule [REF]; migration cost | Alternatives rejected: full history migration (cost), purge (breaches retention) | Impacts: REQ-M-07 updated; migration scope catalogue v3 | Action: archive access procedure to be defined (A-22)."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
