---
name: ba-to-be-design-and-gap-analysis
description: Use when the user is working on process analysis & improvement and needs to-be process maps, gap analysis. Design the to-be process and quantify the gap from the as-is. Produces a reviewable first draft for improvement sponsor (decision) and delivery/change teams (planning).
license: CC-BY-4.0
---

# To-Be Design & Gap Analysis

Derived from `BB-07-D2` in the BA Prompt Forge library
(Business BA / Process Analysis & Improvement, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing process analysis & improvement work and needs one of:
- To-Be Process Maps
- Gap Analysis

The audience for whatever you produce is: **Improvement sponsor (decision) and delivery/change teams (planning)**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[PASTE]`
3. `[LIST]`
4. `[BUDGET, SYSTEMS THAT CANNOT CHANGE, POLICY/LEGISLATIVE CONSTRAINTS]`
5. `[CHANGED]`
6. `[NEW]`
7. `[REMOVED]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Design the to-be process and quantify the gap from the as-is. Draft to-be and gap analysis. Respect the user's constraints — do not design changes to systems I flagged as fixed.

Format the output exactly as follows:

> To-be in the same numbered format as the as-is, with each change marked '[CHANGED]', '[NEW]' or '[REMOVED]' and mapped to the pain point it resolves. Gap analysis table: as-is step → to-be step; change type; impact on people, process, technology; effort magnitude; transition/change-management need. Close with implementation risks and a phased rollout suggestion.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example gap row: "As-is step 7 (manual document expiry check) → To-be step 6 (system flags expiry 14 days ahead) | Change type: automated | Impact: Case Officers stop daily manual checks (~30 min/day); technology: new scheduled job + alert | Transition need: update work instruction WI-114, brief team leaders".

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
