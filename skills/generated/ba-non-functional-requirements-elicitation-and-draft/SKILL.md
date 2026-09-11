---
name: ba-non-functional-requirements-elicitation-and-draft
description: Use when the user is working on functional requirements analysis & refinement and needs non-functional requirements. Elicit and draft a measurable NFR set appropriate to a system of this type. Produces a reviewable first draft for business owners (targets), architects and testers (verification).
license: CC-BY-4.0
---

# Non-Functional Requirements Elicitation & Draft

Derived from `BB-06-D2` in the BA Prompt Forge library
(Business BA / Functional Requirements Analysis & Refinement, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing functional requirements analysis & refinement work and needs one of:
- Non-Functional Requirements

The audience for whatever you produce is: **Business owners (targets), architects and testers (verification)**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[DESCRIBE]`
3. `[USERS, PEAK LOADS, GROWTH IF KNOWN]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Elicit and draft a measurable NFR set appropriate to a system of this type. Ask me the checklist questions I can answer now, then draft the NFRs from the user's answers. Do not silently invent targets — every unvalidated number gets the '[PROPOSED — VALIDATE]' flag.

Format the output exactly as follows:

> First: a checklist of NFR categories (performance, capacity, availability, recoverability, security, privacy, data residency, accessibility WCAG 2.2 AA, auditability, usability, supportability, compliance) with 2-3 elicitation questions each. Then: drafted NFRs with measurable targets and rationale, marking targets '[PROPOSED — VALIDATE]'.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example NFR: "NFR-A01 (Accessibility): All public-facing screens shall conform to WCAG 2.2 AA, verified by audit before go-live. NFR-S03 (Auditability): the system shall record user, timestamp and before/after values for every change to a case decision field, retained for 7 years [PROPOSED — VALIDATE retention with Records]."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
