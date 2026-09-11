---
name: ba-reporting-requirements-specification
description: Use when the user is working on data & reporting analysis and needs reporting requirements, kpi definitions. Specify the reports and KPIs so a BI developer could build them without re-eliciting. Produces a reviewable first draft for report consumers for validation.
license: CC-BY-4.0
---

# Reporting Requirements Specification

Derived from `BB-04-D2` in the BA Prompt Forge library
(Business BA / Data & Reporting Analysis, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing data & reporting analysis work and needs one of:
- Reporting Requirements
- KPI Definitions

The audience for whatever you produce is: **Report consumers for validation; BI/reporting developers for build**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[WHO NEEDS TO KNOW WHAT, TO MAKE WHICH DECISION]`
3. `[DESCRIBE]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Specify the reports and KPIs so a BI developer could build them without re-eliciting. Draft the specification for each report I describe. Challenge me where a report has no clear decision attached to it.

Format the output exactly as follows:

> Per report: name; business purpose and decision supported; audience and access restrictions (note privacy constraints on personal and sensitive data); KPIs and measures with formulas; dimensions and filters; frequency and latency; data sources; wireframe description in words.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example report spec fragment: "Report: Weekly Case Intake Aging | Purpose: identify cases approaching the decision deadline so team leaders can reprioritise | Audience: case team leaders (no sensitive personal data displayed) | KPIs: count by days-to-deadline band (0–3, 4–7, 8+) | Dimensions: team, channel, case type | Frequency: weekly Monday 8am | Latency: data as at Sunday midnight".

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
