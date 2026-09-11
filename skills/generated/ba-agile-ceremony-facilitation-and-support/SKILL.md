---
name: ba-agile-ceremony-facilitation-and-support
description: 'Use when the user is working on agile ceremony facilitation & support and needs refinement session outputs, sprint planning inputs, showcase materials, retrospective actions. Support and contribute to sprint ceremonies so the squad stays aligned and informed: prepare refinement sessions, support sprint planning and goal setting, and support showcases and retrospectives. Produces a reviewable first draft for the squad (developers, testers, product owner) and attending stakeholders.'
license: CC-BY-4.0
---

# Master – Agile Ceremony Facilitation & Support

Derived from `AB-01-M` in the BA Prompt Forge library
(Agile BA / Agile Ceremony Facilitation & Support, scored 19/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing agile ceremony facilitation & support work and needs one of:
- Refinement Session Outputs
- Sprint Planning Inputs
- Showcase Materials
- Retrospective Actions

The audience for whatever you produce is: **The squad (developers, testers, product owner) and attending stakeholders**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[SQUAD NAME, PRODUCT/SYSTEM, CADENCE e.g. 2-week sprints, TOOL e.g. Jira]`
3. `[PASTE OR 'STANDARD']`
4. `[REFINEMENT / SPRINT PLANNING / SHOWCASE / RETROSPECTIVE]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- refinement session prep (candidate stories with open questions, assumptions and dependency notes; DoR check per story)
- sprint planning inputs (prioritised backlog summary, capacity check, draft sprint goal options)
- showcase pack (storyboard, demo scenarios in business language, anticipated questions)
- retrospective support (theme analysis of the user's notes, candidate actions with owners, follow-through check on last retro's actions)

Format the output exactly as follows:

> Structured, evidence-based business analysis writing aligned to BABOK good practice. Use clear headings, numbered requirements and tables where they aid scanning. Plain English; expand every acronym on first use; no marketing language. Ceremony materials are working artefacts: short, scannable, timeboxed agendas; questions framed to drive decisions in the session, not afterwards.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example refinement item: "ST-214 'Flag expiring documents': DoR — acceptance criteria MISSING; Open question: does 'expiring' mean 14 or 28 days (blocks test design — ask the product owner); Assumption: worklist badge only, no email; Dependency: document expiry date reliably populated (data quality check DQ-7)."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
