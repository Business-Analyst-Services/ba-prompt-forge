---
name: ba-spike-definition-and-outcome-record
description: Use when the user is working on just-in-time requirements elaboration and needs spike outcomes, decision records, de-risked stories. Define a sharp spike before it runs, and turn its findings into a decision record afterwards. Produces a reviewable first draft for squad (running the spike), product owner (accepting the decision).
license: CC-BY-4.0
---

# Spike Definition & Outcome Record

Derived from `AB-03-D2` in the BA Prompt Forge library
(Agile BA / Just-in-Time Requirements Elaboration, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing just-in-time requirements elaboration work and needs one of:
- Spike Outcomes
- Decision Records
- De-risked Stories

The audience for whatever you produce is: **Squad (running the spike), product owner (accepting the decision)**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[SQUAD NAME, PRODUCT/SYSTEM, CADENCE e.g. 2-week sprints, TOOL e.g. Jira]`
3. `[PASTE OR 'STANDARD']`
4. `[WHAT WE DON'T KNOW]`
5. `[IDS]`
6. `[E.G. 2 DAYS]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Define a sharp spike before it runs, and turn its findings into a decision record afterwards. Draft whichever half I ask for. Reject spike questions that are really two questions — split them.

Format the output exactly as follows:

> Spike definition: the question (answerable, singular); why it blocks delivery; method (what will be tried/read/tested); timebox; 'done means' (the artefact or answer produced); decision the outcome feeds. Outcome record: what was learned (facts vs judgement); answer to the question; decision recommended; stories now unblocked and how their scope/estimates change.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example spike definition: "Question: can the legacy API return document end-dates in bulk (≤2s for 500 cases)? Blocks: ST-214, ST-215. Method: call the test endpoint with production-like synthetic volume. Timebox: 1 day. Done means: measured latency figures + yes/no. Feeds: build vs nightly-batch decision."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
