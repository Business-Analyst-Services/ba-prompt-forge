---
name: ba-artefact-peer-review-senior-ba-lens
description: 'Use when the user is working on requirements quality assurance & review and needs peer review records, review outcomes. Review the artefact as a senior BA would: specific findings, prioritised, with rewrites — calibrated to develop the author. Produces a reviewable first draft for the artefact author.'
license: CC-BY-4.0
---

# Artefact Peer Review (Senior BA lens)

Derived from `LB-03-D1` in the BA Prompt Forge library
(Lead BA / Requirements Quality Assurance & Review, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing requirements quality assurance & review work and needs one of:
- Peer Review Records
- Review Outcomes

The audience for whatever you produce is: **The artefact author; review record kept for assurance**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[PROGRAM/PROJECT, NUMBER OF BAs AND WORKSTREAMS, DELIVERY METHOD]`
3. `[PASTE THE ARTEFACT]`
4. `[PASTE OR 'STANDARD REQUIREMENTS QUALITY CRITERIA']`
5. `[FOR FEEDBACK CALIBRATION]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Review the artefact as a senior BA would: specific findings, prioritised, with rewrites — calibrated to develop the author. Run the review. Every 'blocker' must state the concrete downstream failure it would cause.

Format the output exactly as follows:

> Summary verdict (fit for sign-off / minor rework / material rework) with the one-sentence reason. Findings table: location; issue; severity (blocker/major/minor); why it matters downstream (test, build, governance); suggested rewrite. Then the top 3 issues to fix first. Close with what the author did well (specific, not token) and one growth theme.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example finding: "Location: FR-041 | Issue: 'system should handle errors appropriately' — untestable | Severity: blocker | Downstream: tester cannot derive cases; vendor will interpret cheapest | Rewrite: 'When the payment file fails validation, the system shall quarantine the file, alert the payments queue within 5 minutes, and log the failure reason.'"

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
