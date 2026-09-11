---
name: ba-epic-stories-breakdown-with-acceptance-criteria
description: Use when the user is working on backlog management (agile) and needs epics, features, user stories, acceptance criteria. Break the epic into sprint-ready user stories with complete acceptance criteria. Produces a reviewable first draft for scrum team (build and test) and product owner (prioritisation).
license: CC-BY-4.0
---

# Epic → Stories Breakdown with Acceptance Criteria

Derived from `BT-02-D1` in the BA Prompt Forge library
(Business/Tech BA / Backlog Management (Agile), scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing backlog management (agile) work and needs one of:
- Epics
- Features
- User Stories
- Acceptance Criteria

The audience for whatever you produce is: **Scrum team (build and test) and product owner (prioritisation)**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[PASTE EPIC DESCRIPTION AND ANY REQUIREMENTS]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Break the epic into sprint-ready user stories with complete acceptance criteria. Draft the breakdown, then review your own stories against INVEST and flag any that fail, with suggested fixes.

Format the output exactly as follows:

> Story map first (backbone activities, then stories beneath); each story: ID, title, 'As a / I want / so that', Given/When/Then criteria (3+ happy path, 2+ edge cases), dependencies, open questions. Keep each story independently deliverable and testable.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example split suggestion: "Story 'Manage supporting documents' fails INVEST (not small: covers flagging, requesting and recording). Split: S1 flag expiring documents on worklist; S2 generate document request letter; S3 record received document and clear flag."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
