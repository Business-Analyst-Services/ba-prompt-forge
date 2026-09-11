---
name: ba-feature-and-functional-requirements-draft
description: Use when the user is working on functional requirements analysis & refinement and needs feature definition, functional requirements. Draft the feature definitions and numbered functional requirements for the pasted needs. Produces a reviewable first draft for stakeholders for sign-off.
license: CC-BY-4.0
---

# Feature & Functional Requirements Draft

Derived from `BB-06-D1` in the BA Prompt Forge library
(Business BA / Functional Requirements Analysis & Refinement, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing functional requirements analysis & refinement work and needs one of:
- Feature Definition
- Functional Requirements

The audience for whatever you produce is: **Stakeholders for sign-off; delivery team for build**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[PASTE]`
3. `[PASTE OR 'NONE PROVIDED']`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Draft the feature definitions and numbered functional requirements for the pasted needs. Draft features, requirements and business rules. Flag every place you had to assume, as 'ASSUMPTION:' inline.

Format the output exactly as follows:

> Per feature: ID, name, description, business need served, out-of-scope notes. Requirements: 'FR-xx: The system shall...' each atomic and testable, with source need referenced. Extract any business rules from the user's material into a separate categorised table (constraint / computation / derivation / inference).

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example: "FR-014: The system shall prevent submission of a service request unless event date, location and requester contact are provided (source: BN-02). Business rule BR-03 (constraint): a service request cannot be lodged more than 48 hours after the requester becomes aware of a reportable event [AMBIGUOUS — confirm the policy or regulatory basis]."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
