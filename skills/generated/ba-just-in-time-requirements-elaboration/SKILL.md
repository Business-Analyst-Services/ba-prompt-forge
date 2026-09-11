---
name: ba-just-in-time-requirements-elaboration
description: 'Use when the user is working on just-in-time requirements elaboration and needs definition of ready compliance, elaborated user stories, acceptance criteria, example/bdd scenarios. Progressively elaborate requirements on cadence so stories are ready ahead of each sprint: manage Definition of Ready compliance, elaborate just-in-time (right detail now, defer the rest), and run spikes for uncertainty. Produces a reviewable first draft for squad (build and test from the stories), product owner (readiness decisions).'
license: CC-BY-4.0
---

# Master – Just-in-Time Requirements Elaboration

Derived from `AB-03-M` in the BA Prompt Forge library
(Agile BA / Just-in-Time Requirements Elaboration, scored 19/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing just-in-time requirements elaboration work and needs one of:
- Definition of Ready Compliance
- Elaborated User Stories
- Acceptance Criteria
- Example/BDD Scenarios

The audience for whatever you produce is: **Squad (build and test from the stories), product owner (readiness decisions)**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[SQUAD NAME, PRODUCT/SYSTEM, CADENCE e.g. 2-week sprints, TOOL e.g. Jira]`
3. `[PASTE OR 'STANDARD']`
4. `[E.G. STORIES FOR NEXT 1-2 SPRINTS]`
5. `[PASTE OR REFERENCE]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- readiness assessment of pasted stories against the DoR (met/not met per criterion, blocking gaps, who can close each)
- story elaboration (description, business rules, acceptance criteria, BDD example scenarios with data)
- 'now vs later' analysis — what detail is needed this sprint vs deferrable
- spike definitions (question to answer, timebox, done-means, decision the outcome feeds)

Format the output exactly as follows:

> Structured, evidence-based business analysis writing aligned to BABOK good practice. Use clear headings, numbered requirements and tables where they aid scanning. Plain English; expand every acronym on first use; no marketing language. Elaborate only what the next sprint needs — flag over-elaboration as waste. BDD scenarios in Given/When/Then with concrete example data, covering happy, negative and boundary cases.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example now-vs-later call: "Now (blocks sprint): which document types trigger the flag. Later (defer to r2 elaboration): bulk-clear behaviour — not in this sprint's stories, elaborating now is waste."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
