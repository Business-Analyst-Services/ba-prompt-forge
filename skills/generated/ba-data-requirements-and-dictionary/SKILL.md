---
name: ba-data-requirements-and-dictionary
description: Use when the user is working on data & reporting analysis and needs data requirements, data mapping. Produce a business data dictionary and requirements table for the fields in scope. Produces a reviewable first draft for data owners for validation.
license: CC-BY-4.0
---

# Data Requirements & Dictionary

Derived from `BB-04-D1` in the BA Prompt Forge library
(Business BA / Data & Reporting Analysis, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing data & reporting analysis work and needs one of:
- Data Requirements
- Data Mapping

The audience for whatever you produce is: **Data owners for validation; engineers for implementation**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[PASTE FIELD LIST, FORM, OR API EXTRACT]`
3. `[DESCRIBE]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Produce a business data dictionary and requirements table for the fields in scope. Draft the dictionary, then list the top data-quality and privacy risks (e.g. health information exposure in reporting) with mitigations.

Format the output exactly as follows:

> Table: field name (standardised snake_case suggestion); business definition; data type; allowable values; validation rules; example value; data classification (public / internal / personal / health information); source system; quality rule. Flag ambiguous fields rather than guessing definitions.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example dictionary row: "Field: date_of_event | Definition: date the reported event occurred, as advised | Type: date (not future-dated) | Allowable: ≤ today | Validation: must be ≤ case lodgement date | Example: 2026-05-14 | Classification: personal | Source: request form Q3 | Quality rule: reject future dates at entry".

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
