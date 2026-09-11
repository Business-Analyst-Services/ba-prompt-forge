---
name: ba-uat-scenarios-and-scripts-from-requirements
description: Use when the user is working on testing & requirements validation support and needs uat support. Produce UAT scenarios and step-by-step scripts business users can execute unaided. Produces a reviewable first draft for business smes executing uat.
license: CC-BY-4.0
---

# UAT Scenarios & Scripts from Requirements

Derived from `BT-09-D1` in the BA Prompt Forge library
(Business/Tech BA / Testing & Requirements Validation Support, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing testing & requirements validation support work and needs one of:
- UAT Support

The audience for whatever you produce is: **Business SMEs executing UAT; test lead tracking coverage**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[PASTE]`
3. `[BUSINESS ROLES]`
4. `[NOTES — e.g. masked production data only]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Produce UAT scenarios and step-by-step scripts business users can execute unaided. Draft catalogue and scripts. Then self-review: list requirements with thin coverage and edge cases you could not derive without more information.

Format the output exactly as follows:

> Scenario catalogue first (ID, title, requirement refs, priority, type: happy/negative/edge). Then scripts: preconditions and test data needs (flag privacy constraints on production-like data); numbered steps in plain business language; expected result per step; pass/fail and evidence capture instructions.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example script step: "Step 4: Select 'Add attachment' and choose file 'site-photo-1.jpg' (desktop: from TestData folder). Expected: thumbnail appears with green tick; 'Remove' link visible. If the upload spinner persists >30s → record FAIL, screenshot, continue from step 6."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
