---
name: ba-solution-analysis-and-design-support
description: 'Use when the user is working on solution analysis & design support and needs solution options assessment, regulatory & policy compliance assessments, business rules. Assess solution options and compliance needs so design decisions are made with clear business analysis: option assessments, regulatory and policy compliance assessments, and the business rules the solution must honour. Produces a reviewable first draft for solution designers, architects, design authority and business owners.'
license: CC-BY-4.0
---

# Master – Solution Analysis & Design Support

Derived from `BT-07-M` in the BA Prompt Forge library
(Business/Tech BA / Solution Analysis & Design Support, scored 19/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing solution analysis & design support work and needs one of:
- Solution Options Assessment
- Regulatory & Policy Compliance Assessments
- Business Rules

The audience for whatever you produce is: **Solution designers, architects, design authority and business owners**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[DESCRIBE]`
3. `[LIST OR 'TO BE GENERATED']`
4. `[PRIVACY / INFORMATION SECURITY / SECTOR REGULATION / ACCESSIBILITY / RECORDS — LIST KNOWN]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- solution options assessment (criteria and weights, option scores with rationale, sensitivity check, recommendation)
- compliance assessment (obligation, requirement it creates, solution behaviour, gap, remediation)
- business rules extraction and categorisation (constraint / computation / derivation / inference) with ambiguity flags

Format the output exactly as follows:

> Structured, evidence-based business analysis writing aligned to BABOK good practice. Use clear headings, numbered requirements and tables where they aid scanning. Plain English; expand every acronym on first use; no marketing language. Options assessed against weighted criteria agreed before scoring; compliance findings cite the specific obligation and the specific solution behaviour.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example option commentary: "Option B – Configure existing CRM case module: Fit 4/5 (meets 9 of 10 Must-Haves; gap: field mobility offline mode). Cost: low-medium (licence already held). Risk: medium — CRM roadmap uncertainty. Evidence: vendor demo 3/7, config spike results."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
