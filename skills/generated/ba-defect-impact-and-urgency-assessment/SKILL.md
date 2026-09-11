---
name: ba-defect-impact-and-urgency-assessment
description: Use when the user is working on defect & work-around analysis and needs defect analysis. Translate the technical defect into a business impact and urgency assessment that supports a prioritisation decision. Produces a reviewable first draft for product owner and prioritisation forum.
license: CC-BY-4.0
---

# Defect Impact & Urgency Assessment

Derived from `BB-05-D1` in the BA Prompt Forge library
(Business BA / Defect & Work-around Analysis, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing defect & work-around analysis work and needs one of:
- Defect Analysis

The audience for whatever you produce is: **Product owner and prioritisation forum; business stakeholders affected**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[PASTE DEFECT TICKET / ERROR DESCRIPTION]`
3. `[DESCRIBE]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Translate the technical defect into a business impact and urgency assessment that supports a prioritisation decision. Draft the assessment. Where impact data is missing, state what evidence would settle it.

Format the output exactly as follows:

> One page: what is broken in business terms; who is affected and how often; measurable impact (delay, rework, financial, compliance/regulatory exposure); risk if unresolved for 30/90/180 days; recommended priority with rationale.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example urgency line: "Recommended priority: High. Rationale: customer notice accuracy affected (compliance), effort compounds at ~40 hrs/month, and the work-around (manual recalculation in a spreadsheet) introduces its own error risk. Not Critical: no safety impact and a work-around exists."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
