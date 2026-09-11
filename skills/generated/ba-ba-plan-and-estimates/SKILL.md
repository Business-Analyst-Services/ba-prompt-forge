---
name: ba-ba-plan-and-estimates
description: Use when the user is working on sizing, estimation, dependency and prioritisation management and needs ba plan, estimates, assumptions, resource forecasts. Draft the BA plan with estimated effort and an explicit assumptions log. Produces a reviewable first draft for pm (planning), resource managers (forecast), ba team (execution).
license: CC-BY-4.0
---

# BA Plan & Estimates

Derived from `BT-06-D1` in the BA Prompt Forge library
(Business/Tech BA / Sizing, Estimation, Dependency and Prioritisation Management, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing sizing, estimation, dependency and prioritisation management work and needs one of:
- BA Plan
- Estimates
- Assumptions
- Resource Forecasts

The audience for whatever you produce is: **PM (planning), resource managers (forecast), BA team (execution)**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[DESCRIBE PHASES/DELIVERABLES EXPECTED]`
3. `[WHO, AVAILABILITY]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Draft the BA plan with estimated effort and an explicit assumptions log. Draft the plan. Challenge scope items that look under- or over-invested relative to their risk.

Format the output exactly as follows:

> Plan table: phase; BA activities; deliverables; approach/techniques; effort estimate (range, confidence); dependencies; risks. Resource forecast by week/sprint. Assumptions log: assumption; impact if wrong; validation owner. Include elicitation availability of stakeholders as an explicit planning risk.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example assumption entry: "A-03: Vendor API documentation is current and complete. Impact if wrong: interface analysis re-work, +5–8 days. Validation: request doc version + change log from vendor by [DATE]; owner: Tech BA."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
