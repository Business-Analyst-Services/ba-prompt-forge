---
name: ba-dependency-map-and-prioritisation
description: Use when the user is working on sizing, estimation, dependency and prioritisation management and needs prioritisation, dependency management. Map dependencies and produce a defensible priority order. Produces a reviewable first draft for delivery leads and prioritisation forum.
license: CC-BY-4.0
---

# Dependency Map & Prioritisation

Derived from `BT-06-D2` in the BA Prompt Forge library
(Business/Tech BA / Sizing, Estimation, Dependency and Prioritisation Management, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing sizing, estimation, dependency and prioritisation management work and needs one of:
- Prioritisation
- Dependency management

The audience for whatever you produce is: **Delivery leads and prioritisation forum**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[PASTE REQUIREMENTS/FEATURES/WORK ITEMS]`
3. `[DATES, TEAMS, TECHNICAL DEPENDENCIES]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Map dependencies and produce a defensible priority order. Deliver map, diagram and prioritisation. Flag circular or fragile dependency chains explicitly.

Format the output exactly as follows:

> Dependency table: item; depends on; dependency type; criticality; risk if late; owner. Then a Mermaid dependency diagram. Prioritisation: MoSCoW (or the user's chosen lens) with one-sentence rationale each, deferral risk, and descope alternatives for contested Must-Haves. Highlight the critical path.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example dependency row: "Item: billing calculation stories | Depends on: finalised charging-rule ruling (Policy team) | Type: needs-before | Criticality: high — blocks 3 sprints of build | Risk if late: delivery slips past the annual billing cycle | Owner: Policy Lead. (Critical path: charging ruling → billing stories → billing-cycle testing.)"

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
