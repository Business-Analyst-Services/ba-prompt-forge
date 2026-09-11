---
name: ba-ai-guardrails-and-evaluation-criteria
description: Use when the user is working on ai transformation and needs guardrails and controls, evaluation criteria. Specify the guardrails, controls and evaluation criteria that make this AI use case safe to operate. Produces a reviewable first draft for engineering (implementation), risk and governance (assurance).
license: CC-BY-4.0
---

# AI Guardrails & Evaluation Criteria

Derived from `BT-01-D2` in the BA Prompt Forge library
(Business/Tech BA / AI Transformation, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing ai transformation work and needs one of:
- Guardrails and controls
- evaluation criteria

The audience for whatever you produce is: **Engineering (implementation), risk and governance (assurance)**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[PASTE USE CASE DEFINITION]`
3. `[LOW/MEDIUM/HIGH]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Specify the guardrails, controls and evaluation criteria that make this AI use case safe to operate. Draft both tables scaled to the risk rating. Mark thresholds '[PROPOSED — VALIDATE WITH BUSINESS OWNER]'.

Format the output exactly as follows:

> Guardrails table: control; type (input / behavioural / output / monitoring / human review); what it prevents; how implemented; how tested. Evaluation criteria table: dimension (accuracy, groundedness, privacy leakage, fairness, tone); measure; threshold; test method; frequency (pre-release vs ongoing). Include an incident/rollback trigger list.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example guardrail row: "Control: output constraint — the assistant must refuse to state or imply an eligibility or liability position | Type: behavioural | Prevents: unauthorised decision-making | Implemented: system prompt rule + output classifier | Tested: red-team set of 40 decision-baiting inputs, 100% refusal required."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
