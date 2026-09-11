---
name: ba-cross-stream-scope-and-dependency-coordination
description: 'Use when the user is working on cross-stream scope & dependency coordination and needs dependency registers, scope alignment records, cross-stream impact assessments. Coordinate requirements scope, dependencies and impacts across teams and workstreams: map boundaries, find overlaps and gaps, maintain the dependency register, and assess cross-stream impacts of changes. Produces a reviewable first draft for stream leads and pms.'
license: CC-BY-4.0
---

# Master – Cross-Stream Scope & Dependency Coordination

Derived from `LB-04-M` in the BA Prompt Forge library
(Lead BA / Cross-Stream Scope & Dependency Coordination, scored 19/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing cross-stream scope & dependency coordination work and needs one of:
- Dependency Registers
- Scope Alignment Records
- Cross-stream Impact Assessments

The audience for whatever you produce is: **Stream leads and PMs; escalation summaries for program leadership**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[PROGRAM/PROJECT, NUMBER OF BAs AND WORKSTREAMS, DELIVERY METHOD]`
3. `[LIST WORKSTREAMS AND THEIR SCOPE IN ONE LINE EACH]`
4. `[WHERE OVERLAPS OR GAPS ARE SUSPECTED]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- scope boundary map (per stream: owns / consumes / explicitly not covered) with overlap and gap findings
- dependency register (item, from-stream, to-stream, type, needed-by, status, risk if late)
- cross-stream impact assessment for a proposed change (streams affected, requirement/artefact impacts, effort, sequencing consequence)
- alignment session designs and the record of what was agreed

Format the output exactly as follows:

> Structured, evidence-based business analysis writing aligned to BABOK good practice. Use clear headings, numbered requirements and tables where they aid scanning. Plain English; expand every acronym on first use; no marketing language. Boundaries stated as ownership rules ('stream A owns customer master data requirements; stream B consumes'); every overlap resolved to a single owner with a consultation duty, and recorded.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example ownership rule: "Stream A (Case Management) OWNS customer master data requirements; Stream B (Billing) CONSUMES and must be consulted on changes touching registration-number validation. Not covered by either: partner portal data — GAP, escalated."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
