---
name: ba-ba-engagement-planning-and-estimation
description: 'Use when the user is working on ba engagement planning & estimation and needs ba plan, ba estimates & assumptions, resource forecasts, raid inputs. Define the BA approach, effort and resourcing across the project or program: analysis scope, approach and techniques per phase, estimates with assumptions, resource forecasts, and RAID inputs for the engagement. Produces a reviewable first draft for project/program manager (plan integration), resource managers (forecast), the ba team (their roadmap).'
license: CC-BY-4.0
---

# Master – BA Engagement Planning & Estimation

Derived from `LB-01-M` in the BA Prompt Forge library
(Lead BA / BA Engagement Planning & Estimation, scored 19/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing ba engagement planning & estimation work and needs one of:
- BA Plan
- BA Estimates & Assumptions
- Resource Forecasts
- RAID Inputs

The audience for whatever you produce is: **Project/program manager (plan integration), resource managers (forecast), the BA team (their roadmap)**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[PROGRAM/PROJECT, NUMBER OF BAs AND WORKSTREAMS, DELIVERY METHOD]`
3. `[SCOPE SUMMARY, TIMEFRAME, KNOWN CONSTRAINTS]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- BA approach summary (analysis needed per phase, techniques, deliverables, governance touchpoints)
- analysis scope definition (in/out, depth per area, justification)
- estimates (range + confidence per package, assumptions log with impact-if-wrong)
- resource forecast by sprint/month with skills mix
- RAID inputs specific to analysis (e.g. SME availability, requirements churn)

Format the output exactly as follows:

> Structured, evidence-based business analysis writing aligned to BABOK good practice. Use clear headings, numbered requirements and tables where they aid scanning. Plain English; expand every acronym on first use; no marketing language. Estimates as ranges with confidence and named assumptions; the plan distinguishes what analysis is needed from who does it; resourcing tied to skills, not just headcount.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example RAID input: "Risk: operations SMEs available <2 days/wk during the annual peak (Jul-Aug) — elicitation slips ~3 wks. Mitigation: front-load operations workshops to June; fallback: recorded walkthrough sessions. Owner: Lead BA."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
