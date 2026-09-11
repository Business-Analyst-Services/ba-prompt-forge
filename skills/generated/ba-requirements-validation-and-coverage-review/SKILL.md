---
name: ba-requirements-validation-and-coverage-review
description: Use when the user is working on testing & requirements validation support and needs requirements validation, solution reviews. Validate that the test set genuinely proves the requirements, and that requirements remain internally consistent. Produces a reviewable first draft for test lead and ba (fixes).
license: CC-BY-4.0
---

# Requirements Validation & Coverage Review

Derived from `BT-09-D2` in the BA Prompt Forge library
(Business/Tech BA / Testing & Requirements Validation Support, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing testing & requirements validation support work and needs one of:
- Requirements Validation
- Solution Reviews

The audience for whatever you produce is: **Test lead and BA (fixes); governance (assurance)**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[PASTE]`
3. `[PASTE OR 'NONE']`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Validate that the test set genuinely proves the requirements, and that requirements remain internally consistent. Run the review and deliver findings. Rank by risk to business outcome, not by count.

Format the output exactly as follows:

> Findings table: finding; type (coverage gap / untestable requirement / orphan test / ambiguity / contradiction); location; severity; recommended fix with suggested rewrite where applicable. Summary heat map by requirement area.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example finding: "Finding F-07 (coverage gap, severity: high): FR-018 bulk reassignment has no UAT scenario, and its only SIT case tests ≤10 cases while the requirement allows 500. Fix: add volume scenario at 500 cases with the timing target from NFR-P04."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
