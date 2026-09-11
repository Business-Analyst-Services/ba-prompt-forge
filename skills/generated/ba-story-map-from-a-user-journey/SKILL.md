---
name: ba-story-map-from-a-user-journey
description: 'Use when the user is working on user story mapping & slicing and needs story maps, walking skeleton, release slices. Build the story map: backbone, stories, walking skeleton and release slices. Produces a reviewable first draft for squad (build sequencing) and stakeholders (scope conversations).'
license: CC-BY-4.0
---

# Story Map from a User Journey

Derived from `AB-02-D1` in the BA Prompt Forge library
(Agile BA / User Story Mapping & Slicing, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing user story mapping & slicing work and needs one of:
- Story Maps
- Walking Skeleton
- Release Slices

The audience for whatever you produce is: **Squad (build sequencing) and stakeholders (scope conversations)**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[SQUAD NAME, PRODUCT/SYSTEM, CADENCE e.g. 2-week sprints, TOOL e.g. Jira]`
3. `[PASTE OR 'STANDARD']`
4. `[PASTE JOURNEY / PROCESS NOTES]`
5. `[LIST]`
6. `[N RELEASES OR 'PROPOSE']`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Build the story map: backbone, stories, walking skeleton and release slices. Draft the map. List the assumptions you made about journey order and persona goals for me to verify.

Format the output exactly as follows:

> Backbone as ordered user activities (verb phrases, user's perspective); under each activity, stories ordered by necessity; walking skeleton row marked (thinnest end-to-end path); release slice lines with the value statement per release. Render as an indented text map plus a Mermaid diagram. Flag backbone gaps where the user's journey notes skipped steps.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example walking-skeleton note: "Skeleton path: lodge (web form, no attachments) → appears in triage queue → manual severity → assign. Excludes: attachments, auto-severity, alerts — the journey completes end-to-end, which is the skeleton test."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
