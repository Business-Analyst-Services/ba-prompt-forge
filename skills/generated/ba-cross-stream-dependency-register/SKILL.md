---
name: ba-cross-stream-dependency-register
description: Use when the user is working on cross-stream scope & dependency coordination and needs dependency registers. Build the cross-stream dependency register and expose the chains that threaten the program. Produces a reviewable first draft for stream leads (management), program leadership (the watch-list).
license: CC-BY-4.0
---

# Cross-Stream Dependency Register

Derived from `LB-04-D1` in the BA Prompt Forge library
(Lead BA / Cross-Stream Scope & Dependency Coordination, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing cross-stream scope & dependency coordination work and needs one of:
- Dependency Registers

The audience for whatever you produce is: **Stream leads (management), program leadership (the watch-list)**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[PROGRAM/PROJECT, NUMBER OF BAs AND WORKSTREAMS, DELIVERY METHOD]`
3. `[PASTE STREAM SCOPES/MILESTONES]`
4. `[LIST WHAT'S ALREADY KNOWN]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Build the cross-stream dependency register and expose the chains that threaten the program. Build the register from the user's inputs and infer likely missing dependencies from the stream scopes — marking inferred rows 'INFERRED — CONFIRM'.

Format the output exactly as follows:

> Register: ID; what is needed; from-stream → to-stream; type (artefact / decision / data / resource); needed-by; current status; criticality; risk if late and who feels it. Then the analysis: critical chains (dependencies of dependencies) as a Mermaid diagram; circular dependencies flagged; the 5 dependencies leadership should watch, with why.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example register row: "D-07: finalised charging-rule ruling | From: Policy stream → To: Billing stream | Type: decision | Needed by: 15 Aug | Status: at risk (policy team consulting until 10 Aug) | Criticality: high — blocks 3 sprints of billing build | Felt by: billing squad idle or building on assumption."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
