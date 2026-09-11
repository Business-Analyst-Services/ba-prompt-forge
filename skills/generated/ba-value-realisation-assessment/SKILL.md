---
name: ba-value-realisation-assessment
description: Use when the user is working on benefits realisation & kpi management and needs value realisation assessments, kpi reports. Assess realised value against plan, explain variances, and recommend optimisation actions. Produces a reviewable first draft for sponsor and steering committee.
license: CC-BY-4.0
---

# Value Realisation Assessment

Derived from `BB-01-D2` in the BA Prompt Forge library
(Business BA / Benefits Realisation & KPI Management, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing benefits realisation & kpi management work and needs one of:
- Value Realisation Assessments
- KPI Reports

The audience for whatever you produce is: **Sponsor and steering committee**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[PASTE]`
3. `[PASTE KPI ACTUALS / EXTRACT]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Assess realised value against plan, explain variances, and recommend optimisation actions. Draft the assessment (max 2 pages equivalent). Where data is insufficient to judge a benefit, say so explicitly rather than inferring success.

Format the output exactly as follows:

> Short report: RAG summary table per benefit; variance analysis; root causes distinguished from symptoms; prioritised recommendations with owner and effort estimate.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example variance line: "Benefit B2 – Reduced manual rework: AMBER. Target 30% reduction; actual 12%. Root cause: exception queue still routed to legacy team (process, not system). Recommendation: extend auto-routing rules to exception types 3–5; owner: Ops Improvement; effort: low."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
