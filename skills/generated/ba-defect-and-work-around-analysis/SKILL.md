---
name: ba-defect-and-work-around-analysis
description: 'Use when the user is working on defect & work-around analysis and needs defect analysis, defect change assessment, requirement updates, end-state process maps. Analyse the defect and its work-around from a business standpoint: impact, root cause hypotheses, options for resolution, and the flow-on changes to existing requirements and processes when a fix lands. Produces a reviewable first draft for product owner, support teams and the delivery team fixing the defect.'
license: CC-BY-4.0
---

# Master – Defect & Work-around Analysis

Derived from `BB-05-M` in the BA Prompt Forge library
(Business BA / Defect & Work-around Analysis, scored 19/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing defect & work-around analysis work and needs one of:
- Defect Analysis
- Defect Change Assessment
- Requirement Updates
- End-state Process Maps

The audience for whatever you produce is: **Product owner, support teams and the delivery team fixing the defect**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[DESCRIBE DEFECT, SYSTEM, ERROR BEHAVIOUR]`
3. `[DESCRIBE OR 'NONE']`
4. `[DESCRIBE]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- defect analysis (symptom, affected process step, business impact, urgency rating with rationale)
- work-around assessment (steps, cost, risk, sustainability)
- change assessment for the proposed fix (which requirements and process maps change, regression risk)
- updated requirement wording and end-state process description

Format the output exactly as follows:

> Structured, evidence-based business analysis writing aligned to BABOK good practice. Use clear headings, numbered requirements and tables where they aid scanning. Plain English; expand every acronym on first use; no marketing language. Separate the technical fault, the business impact, and the work-around cost. Quantify impact where possible (work delayed, rework hours, compliance exposure).

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example impact framing: "In business terms: invoice recalculations for customers with retrospective account adjustments show the pre-adjustment figure. ~120 customer accounts/month affected; each requires a 20-minute manual correction and one outbound call. Compliance exposure: issuing incorrect invoices breaches [POLICY REF]."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
