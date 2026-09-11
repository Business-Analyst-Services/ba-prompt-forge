---
name: ba-fix-change-assessment-and-requirement-updates
description: Use when the user is working on defect & work-around analysis and needs defect change assessment, requirement updates, end-state process maps. Assess the ripple effect of the fix and draft the updated requirements and end-state process narrative. Produces a reviewable first draft for delivery team, testers and the documentation owner.
license: CC-BY-4.0
---

# Fix Change Assessment & Requirement Updates

Derived from `BB-05-D2` in the BA Prompt Forge library
(Business BA / Defect & Work-around Analysis, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing defect & work-around analysis work and needs one of:
- Defect Change Assessment
- Requirement Updates
- End-state Process Maps

The audience for whatever you produce is: **Delivery team, testers and the documentation owner**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[DESCRIBE]`
3. `[PASTE]`
4. `[PASTE OR DESCRIBE]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Assess the ripple effect of the fix and draft the updated requirements and end-state process narrative. Draft all three parts, then run a consistency check between the new requirements and the end-state process and flag contradictions.

Format the output exactly as follows:

> Impact table (artefact, current state, change required, regression risk); then redrafted requirements with tracked-change style 'was/now' wording; then the end-state process as a numbered step list with roles and decision points, ready for mapping.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example was/now requirement: "FR-112 WAS: 'The system shall display the customer's current account balance.' NOW: 'The system shall display the customer's current account balance including any retrospective adjustments applied in the current billing period, and shall show the adjustment date.' (Trigger: defect DF-208 fix.)"

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
