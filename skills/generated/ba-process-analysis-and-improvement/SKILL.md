---
name: ba-process-analysis-and-improvement
description: 'Use when the user is working on process analysis & improvement and needs as-is process maps, to-be process maps, gap analysis. Analyse and improve the business process end-to-end: capture the as-is accurately, diagnose pain points to root cause, design a to-be that resolves them, and produce the gap analysis between the two. Produces a reviewable first draft for process owners and performers (validation), improvement sponsors (decisions), delivery team (implementation).'
license: CC-BY-4.0
---

# Master – Process Analysis & Improvement

Derived from `BB-07-M` in the BA Prompt Forge library
(Business BA / Process Analysis & Improvement, scored 19/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing process analysis & improvement work and needs one of:
- As-Is Process Maps
- To-Be Process Maps
- Gap Analysis

The audience for whatever you produce is: **Process owners and performers (validation), improvement sponsors (decisions), delivery team (implementation)**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[PROCESS NAME AND PURPOSE]`
3. `[ROLES, INCLUDING AGENTS/EXTERNAL PARTIES]`
4. `[LIST]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- as-is process narrative from the user's description with pain points annotated at the step where they occur
- root cause analysis of key pain points
- to-be process that addresses each pain point, with the change and its rationale marked per step
- gap analysis table (as-is step, to-be step, change type, impact on people/process/technology, transition need)

Format the output exactly as follows:

> Structured, evidence-based business analysis writing aligned to BABOK good practice. Use clear headings, numbered requirements and tables where they aid scanning. Plain English; expand every acronym on first use; no marketing language. Process steps numbered with role, trigger, input, action, output and decision points; note handoffs and systems touched. Structure suitable for direct conversion to BPMN swimlanes.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example step format: "7. [Case Officer] Reviews the current supporting document in the case management system; if the document has expired → go to step 8 (request an updated document), else → step 9. Pain point: expired documents detected on average 6 days late (PP-3)."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
