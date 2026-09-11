---
name: ba-release-plan-and-scope-sequencing
description: Use when the user is working on iteration & release planning support and needs release plans, release scope definitions. Draft a release plan that unlocks value earliest and survives contact with dependencies. Produces a reviewable first draft for product owner and stakeholders.
license: CC-BY-4.0
---

# Release Plan & Scope Sequencing

Derived from `AB-04-D1` in the BA Prompt Forge library
(Agile BA / Iteration & Release Planning Support, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing iteration & release planning support work and needs one of:
- Release Plans
- Release Scope Definitions

The audience for whatever you produce is: **Product owner and stakeholders; roadmap consumers**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[SQUAD NAME, PRODUCT/SYSTEM, CADENCE e.g. 2-week sprints, TOOL e.g. Jira]`
3. `[PASTE OR 'STANDARD']`
4. `[PASTE WITH ROUGH SIZES]`
5. `[LIST]`
6. `[WHAT THE BUSINESS NEEDS EARLIEST]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Draft a release plan that unlocks value earliest and survives contact with dependencies. Draft the plan. Show one alternative sequencing and why you rejected it.

Format the output exactly as follows:

> Per release: name/date; contents (features with one-line value each); the value headline ('after this release, users can...'); entry dependencies; risks. Sequencing rationale section: why this order (value, dependency, risk-burn-down). Confidence per release date (high/medium/low with the driver). Mermaid timeline diagram.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example release entry: "R1 (30 Sep — confidence: medium, driver: API spike outcome): lodge + triage + assign. Value headline: customers lodge digitally end-to-end; phone channel remains. Entry dependency: penetration test slot booked by 1 Sep."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
