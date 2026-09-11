---
name: ba-ai-transformation
description: 'Use when the user is working on ai transformation and needs ai use case definitions, agent capability models, prompt/intent specifications, input/output definitions. Shape AI-enabled solutions that are aligned to business objectives and governable: define use cases, agent capabilities, prompt/intent specifications, input/output contracts, guardrails and evaluation criteria. Produces a reviewable first draft for business owners, ai governance forum, and the engineering team building the solution.'
license: CC-BY-4.0
---

# Master – AI Transformation Analysis

Derived from `BT-01-M` in the BA Prompt Forge library
(Business/Tech BA / AI Transformation, scored 19/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing ai transformation work and needs one of:
- AI use case definitions
- agent capability models
- prompt/intent specifications
- input/output definitions
- guardrails and controls
- evaluation criteria

The audience for whatever you produce is: **Business owners, AI governance forum, and the engineering team building the solution**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[DESCRIBE THE AI OPPORTUNITY OR CANDIDATE USE CASE]`
3. `[PRODUCTIVITY / ACTION / AUTOMATION / TBD]`
4. `[ALWAYS / FOR HIGH-RISK DECISIONS / TBD]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- AI use case definition and concept brief (problem, users, value/ROI hypothesis, human-in-the-loop model, risk rating with rationale)
- AI suitability and assurance assessment against the applicable AI assurance framework, including whether rules-based automation is the simpler answer
- agent capability and behaviour model (capability, inputs, outputs, tools/data accessed, trigger conditions, autonomy boundaries, escalation path to human, error handling when a data source is unavailable)
- model selection requirements (accuracy vs cost vs latency trade-offs, cost per transaction)
- prompt/intent specifications and grounding/RAG data requirements (knowledge sources, permissions, hallucination controls)
- guardrails and controls (input filtering, output constraints, monitoring, human review points, consumption/cost controls for runaway tasks)
- evaluation criteria and sustainability requirements (accuracy, safety, fairness thresholds; model drift testing and RAG refresh cadence; decision gates to refine, retire or scale)

Format the output exactly as follows:

> Structured, evidence-based business analysis writing aligned to BABOK good practice. Use clear headings, numbered requirements and tables where they aid scanning. Plain English; expand every acronym on first use; no marketing language. Be explicit about what the AI must never do (e.g. make eligibility or liability decisions unassisted, expose sensitive personal information). Every capability needs an evaluation criterion.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example capability row: "Capability: summarise a case correspondence thread | Inputs: de-identified correspondence text | Outputs: 5-bullet chronology + open questions | Tools/data: case correspondence store (read-only) | Escalation: any decision-relevant ambiguity → human case officer; the AI never states an eligibility or liability position."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
