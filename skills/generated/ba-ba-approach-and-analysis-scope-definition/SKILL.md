---
name: ba-ba-approach-and-analysis-scope-definition
description: Use when the user is working on ba engagement planning & estimation and needs ba plan. Draft the BA approach and scope so every stakeholder knows what analysis happens, when, to what depth, and why. Produces a reviewable first draft for pm and steering (endorsement), ba team (execution).
license: CC-BY-4.0
---

# BA Approach & Analysis Scope Definition

Derived from `LB-01-D1` in the BA Prompt Forge library
(Lead BA / BA Engagement Planning & Estimation, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing ba engagement planning & estimation work and needs one of:
- BA Plan

The audience for whatever you produce is: **PM and steering (endorsement), BA team (execution)**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[PROGRAM/PROJECT, NUMBER OF BAs AND WORKSTREAMS, DELIVERY METHOD]`
3. `[DESCRIBE]`
4. `[LIST]`
5. `[WHERE AMBIGUITY IS HIGHEST]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Draft the BA approach and scope so every stakeholder knows what analysis happens, when, to what depth, and why. Draft approach and scope. Challenge any area where the user's stated depth doesn't match its risk.

Format the output exactly as follows:

> Approach per phase: analysis objective; techniques (workshops, story mapping, decomposition level); deliverables and their consumers; governance/sign-off points. Scope table: area; in/out; analysis depth (light-touch / standard / deep) with justification tied to risk; deliberate exclusions with the risk accepted. One-page summary up front for the PM.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example scope row: "Area: billing calculation rules | In scope — deep (regulatory exposure, history of defects) | Deliverables: rules catalogue, calculation FRs | Consumer: build vendor + testers. Deliberate exclusion: partner commission rules (unchanged; risk accepted: regression suite covers)."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
