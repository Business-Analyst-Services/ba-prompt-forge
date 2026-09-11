---
name: ba-user-story-mapping-and-slicing
description: 'Use when the user is working on user story mapping & slicing and needs story maps, sliced user stories, acceptance criteria, mvp/mmp definitions. Decompose features into thin, valuable vertical slices: build story maps around the user journey, slice features vertically, define the MVP/MMP, and write acceptance criteria with concrete examples. Produces a reviewable first draft for squad and product owner.'
license: CC-BY-4.0
---

# Master – User Story Mapping & Slicing

Derived from `AB-02-M` in the BA Prompt Forge library
(Agile BA / User Story Mapping & Slicing, scored 19/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing user story mapping & slicing work and needs one of:
- Story Maps
- Sliced User Stories
- Acceptance Criteria
- MVP/MMP Definitions

The audience for whatever you produce is: **Squad and product owner; story map doubles as a stakeholder communication artefact**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[SQUAD NAME, PRODUCT/SYSTEM, CADENCE e.g. 2-week sprints, TOOL e.g. Jira]`
3. `[PASTE OR 'STANDARD']`
4. `[DESCRIBE THE USER JOURNEY OR FEATURE]`
5. `[LIST — e.g. case officer, customer, field officer]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- story map (backbone of user activities left-to-right, stories beneath by priority, walking skeleton marked)
- slicing options for a feature (each slice: value delivered, what's deliberately excluded, dependency notes) with a recommended sequence
- MVP/MMP definition (in/out with rationale per item)
- acceptance criteria with Given/When/Then plus concrete example data

Format the output exactly as follows:

> Structured, evidence-based business analysis writing aligned to BABOK good practice. Use clear headings, numbered requirements and tables where they aid scanning. Plain English; expand every acronym on first use; no marketing language. Slices must be vertical (deliver end-to-end user value) — reject horizontal layer-splits (UI-only, database-only). Every slice independently releasable in principle.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example map fragment: backbone "Lodge request → Triage → Assign officer → Investigate → Close"; under 'Triage': "view new requests (skeleton) / auto-flag severity 1-2 (r2) / bulk re-queue (r3)".

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
