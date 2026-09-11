---
name: ba-sizing-estimation-dependency-and-prioritisation-management
description: 'Use when the user is working on sizing, estimation, dependency and prioritisation management and needs ba plan, estimates, assumptions, resource forecasts. Support definition and prioritisation of requirements and BA work based on business and technical needs and dependencies: BA planning, estimation with explicit assumptions, dependency mapping and prioritisation. Produces a reviewable first draft for project manager, delivery leads and resource managers.'
license: CC-BY-4.0
---

# Master – Sizing, Estimation & Prioritisation

Derived from `BT-06-M` in the BA Prompt Forge library
(Business/Tech BA / Sizing, Estimation, Dependency and Prioritisation Management, scored 19/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing sizing, estimation, dependency and prioritisation management work and needs one of:
- BA Plan
- Estimates
- Assumptions
- Resource Forecasts
- Prioritisation
- Dependency management

The audience for whatever you produce is: **Project manager, delivery leads and resource managers**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[DESCRIBE SCOPE]`
3. `[BA RESOURCES, AVAILABILITY]`
4. `[LIST]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- BA plan (activities, deliverables, approach, estimate range, dependencies per phase)
- estimation breakdowns with assumptions log
- dependency map (item, depends on, type, criticality, risk if late) plus a suggested sequence
- prioritisation using MoSCoW or value/effort with rationale and deferral risks

Format the output exactly as follows:

> Structured, evidence-based business analysis writing aligned to BABOK good practice. Use clear headings, numbered requirements and tables where they aid scanning. Plain English; expand every acronym on first use; no marketing language. Estimates always as ranges with confidence levels and stated assumptions; single-point estimates are not acceptable. Dependencies typed (needs-before / informs / shares-resource).

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example estimate row: "Phase: Elicitation & analysis | Activities: 6 workshops + synthesis | Deliverables: business needs statements, as-is maps | Estimate: 18–24 BA days (confidence: medium) | Assumption: SMEs available within 5 business days of request — if wrong, add 1 week elapsed per workshop."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
