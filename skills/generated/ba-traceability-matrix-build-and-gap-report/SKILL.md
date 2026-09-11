---
name: ba-traceability-matrix-build-and-gap-report
description: Use when the user is working on requirements governance & traceability and needs traceability matrix. Build the traceability matrix from the pasted artefacts and report every gap. Produces a reviewable first draft for ba and test lead (fix gaps).
license: CC-BY-4.0
---

# Traceability Matrix Build & Gap Report

Derived from `BT-05-D1` in the BA Prompt Forge library
(Business/Tech BA / Requirements Governance & Traceability, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing requirements governance & traceability work and needs one of:
- Traceability Matrix

The audience for whatever you produce is: **BA and test lead (fix gaps); governance (assurance)**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[PASTE BUSINESS NEEDS]`
3. `[PASTE REQUIREMENTS/STORIES]`
4. `[PASTE TEST CASES OR 'NONE YET']`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Build the traceability matrix from the pasted artefacts and report every gap. Build matrix and gap report. Do not force-fit doubtful links — mark them 'UNCERTAIN — CONFIRM' instead.

Format the output exactly as follows:

> Matrix: business need ID → requirement ID(s) → story ID(s) → test ID(s), one row per requirement. Gap report: needs with no requirements; requirements with no source need (potential scope creep); requirements with no test coverage; tests with no requirement. Each gap: severity and recommended action.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example gap finding: "Requirement FR-018 (bulk reassignment of cases) has no test coverage. Severity: high — go-live function. Action: test lead to add scenario; trace once created. Orphan test UAT-C30 references a retired requirement — retire or re-link."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
