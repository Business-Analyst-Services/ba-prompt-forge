---
name: ba-raw-notes-business-needs-statements
description: Use when the user is working on business needs assessments (initial and high level requirements) and needs business needs statements, discovery notes. Convert the raw notes into clean, attributed business needs statements ready for validation. Produces a reviewable first draft for stakeholders who will validate the needs.
license: CC-BY-4.0
---

# Raw Notes → Business Needs Statements

Derived from `BB-02-D2` in the BA Prompt Forge library
(Business BA / Business Needs Assessments (Initial and High Level Requirements), scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing business needs assessments (initial and high level requirements) work and needs one of:
- Business Needs Statements
- Discovery Notes

The audience for whatever you produce is: **Stakeholders who will validate the needs; the delivery team consuming them downstream**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[PASTE MEETING NOTES / TRANSCRIPT / EMAIL THREADS]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Convert the raw notes into clean, attributed business needs statements ready for validation. Draft the table. Do not invent needs that lack support in the notes — flag gaps instead.

Format the output exactly as follows:

> Table: ID; needs statement ('The business needs the ability to X so that Y'); type (explicit / implied / needs clarification); source (who said it / which note); suggested validation question. Separate section for decisions, actions and parking-lot items.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example row: "BN-04 | The business needs the ability to lodge service requests from a mobile device so that requests arrive within agreed timeframes | Type: explicit | Source: J. Chen, field ops workshop 12/7 | Validation question: does this extend to third parties without a registered account?"

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
