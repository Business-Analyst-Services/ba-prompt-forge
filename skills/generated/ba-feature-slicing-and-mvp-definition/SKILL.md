---
name: ba-feature-slicing-and-mvp-definition
description: Use when the user is working on user story mapping & slicing and needs sliced user stories, mvp/mmp definitions, slice sequencing. Slice the feature vertically, define the thinnest valuable slice, and set MVP/MMP boundaries. Produces a reviewable first draft for product owner (scope decisions) and squad (build).
license: CC-BY-4.0
---

# Feature Slicing & MVP Definition

Derived from `AB-02-D2` in the BA Prompt Forge library
(Agile BA / User Story Mapping & Slicing, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing user story mapping & slicing work and needs one of:
- Sliced User Stories
- MVP/MMP Definitions
- Slice Sequencing

The audience for whatever you produce is: **Product owner (scope decisions) and squad (build)**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[SQUAD NAME, PRODUCT/SYSTEM, CADENCE e.g. 2-week sprints, TOOL e.g. Jira]`
3. `[PASTE OR 'STANDARD']`
4. `[PASTE FEATURE + REQUIREMENTS/RULES]`
5. `[DEADLINE, DEPENDENCIES, COMPLIANCE MUSTS]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Slice the feature vertically, define the thinnest valuable slice, and set MVP/MMP boundaries. Draft slices and MVP. Mark compliance-driven items that cannot be descoped regardless of value logic.

Format the output exactly as follows:

> Slicing options table: slice; user value delivered; deliberately excluded; effort feel (S/M/L); dependency/risk notes. Recommended sequence with rationale. MVP definition: in/out table with one-line rationale each; explicitly test each 'in' against 'would the release still be valuable without it?'. Each slice restated as user stories with acceptance criteria.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example slice row: "Slice B – Lodge with attachments: Value: customers stop emailing photos separately; Excluded: virus-scan queue UI (ops handle via existing tool); Effort: M; Risk: file-size limits need infra confirmation. MVP test: valuable without it? Yes — so slice B is r2, not MVP."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
