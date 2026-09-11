---
name: ba-migration-approach-and-reconciliation-requirements
description: Use when the user is working on integration, data & migration and needs migration requirements, data reconciliation requirements. Define migration scope, approach considerations and the reconciliation requirements that prove the migration succeeded. Produces a reviewable first draft for migration lead and data engineers.
license: CC-BY-4.0
---

# Migration Approach & Reconciliation Requirements

Derived from `TB-02-D2` in the BA Prompt Forge library
(Technical BA / Integration, Data & Migration, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing integration, data & migration work and needs one of:
- Migration requirements
- data reconciliation requirements

The audience for whatever you produce is: **Migration lead and data engineers; business owners signing off data completeness**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[SOURCE]`
3. `[TARGET]`
4. `[ENTITIES, VOLUMES, HISTORY DEPTH NEEDED]`
5. `[CUTOVER WINDOW, COEXISTENCE, REGULATORY RETENTION]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Define migration scope, approach considerations and the reconciliation requirements that prove the migration succeeded. Draft all sections. Call out the riskiest entities (quality, volume, transformation complexity) and why.

Format the output exactly as follows:

> Scope catalogue: entity; volume; migrate/archive/retire recommendation with rationale; quality concerns; retention obligation. Approach analysis: big bang vs phased vs parallel run — pros/cons against the user's constraints and a recommendation. Sequencing and dependency list. Reconciliation requirements: check; level (counts/financial totals/field-level sample); tolerance; timing; owner; evidence for sign-off.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example reconciliation row: "Check R-02: total approved case liability amounts by financial year, source vs target | Level: financial totals | Tolerance: $0 variance | Timing: post-load, pre-cutover sign-off | Owner: Finance data steward | Evidence: reconciliation report signed and attached to the cutover record."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
