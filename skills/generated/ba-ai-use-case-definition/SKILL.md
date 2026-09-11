---
name: ba-ai-use-case-definition
description: Use when the user is working on ai transformation and needs ai use case definitions. Define the candidate AI use case rigorously enough for a governance forum to assess it. Produces a reviewable first draft for ai governance forum and the business owner.
license: CC-BY-4.0
---

# AI Use Case Definition

Derived from `BT-01-D1` in the BA Prompt Forge library
(Business/Tech BA / AI Transformation, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing ai transformation work and needs one of:
- AI use case definitions

The audience for whatever you produce is: **AI governance forum and the business owner**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[DESCRIBE — e.g. summarising case correspondence, triaging incoming requests, drafting field reports]`
3. `[DESCRIBE, FLAG PERSONAL OR SENSITIVE DATA]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Define the candidate AI use case rigorously enough for a governance forum to assess it. Draft the definition. Challenge the use case where the value hypothesis is weak or a non-AI fix would do.

Format the output exactly as follows:

> Sections: problem and current cost; proposed AI capability; users and workflow fit; value hypothesis with measurable success criteria; data used (classification, residency, consent basis); human-in-the-loop model; risk assessment (accuracy, bias, privacy, workforce) with residual risk rating; out-of-scope declarations.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example success criterion: "90% of AI-generated summaries rated 'accurate and complete' by case officers on a 50-case sample, with zero instances of fabricated case facts; officer review time per file reduced ≥30% against baseline."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
