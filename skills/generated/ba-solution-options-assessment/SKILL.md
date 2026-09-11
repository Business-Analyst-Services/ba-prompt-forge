---
name: ba-solution-options-assessment
description: Use when the user is working on solution analysis & design support and needs solution options assessment. Produce an options assessment that makes the trade-offs explicit and recommends defensibly. Produces a reviewable first draft for design authority / steering committee deciding.
license: CC-BY-4.0
---

# Solution Options Assessment

Derived from `BT-07-D1` in the BA Prompt Forge library
(Business/Tech BA / Solution Analysis & Design Support, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing solution analysis & design support work and needs one of:
- Solution Options Assessment

The audience for whatever you produce is: **Design authority / steering committee deciding**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[STATE THE DESIGN QUESTION]`
3. `[LIST 2-4 OPTIONS WITH A LINE EACH]`
4. `[WHAT MATTERS MOST — COST/SPEED/RISK/CAPABILITY]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Produce an options assessment that makes the trade-offs explicit and recommends defensibly. Propose criteria and weights from the user's priorities, ask the user to confirm, then assess. State every assumption behind a score.

Format the output exactly as follows:

> Criteria table (criterion, weight, why it matters) agreed first; option-by-criterion assessment with evidence-based commentary, not bare scores; cost/risk/benefit summary per option including 'do nothing'; sensitivity note (does the recommendation flip if a weight changes?); recommendation with conditions.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example sensitivity note: "Recommendation (Option B) holds unless 'time to deliver' weight rises above 30% — at that point Option C (SaaS point solution) scores higher. Decision is NOT sensitive to cost weighting within ±10pp."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
