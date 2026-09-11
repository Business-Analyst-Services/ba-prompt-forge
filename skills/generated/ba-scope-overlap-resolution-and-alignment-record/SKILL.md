---
name: ba-scope-overlap-resolution-and-alignment-record
description: Use when the user is working on cross-stream scope & dependency coordination and needs scope alignment records, cross-stream impact assessments. Analyse the overlap, recommend a single-owner resolution, and draft the alignment record that prevents relitigating. Produces a reviewable first draft for the two stream leads and the program forum ratifying it.
license: CC-BY-4.0
---

# Scope Overlap Resolution & Alignment Record

Derived from `LB-04-D2` in the BA Prompt Forge library
(Lead BA / Cross-Stream Scope & Dependency Coordination, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing cross-stream scope & dependency coordination work and needs one of:
- Scope Alignment Records
- Cross-stream Impact Assessments

The audience for whatever you produce is: **The two stream leads and the program forum ratifying it**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[PROGRAM/PROJECT, NUMBER OF BAs AND WORKSTREAMS, DELIVERY METHOD]`
3. `[DESCRIBE — e.g. both streams writing requirements for the same interface]`
4. `[SUMMARISE]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Analyse the overlap, recommend a single-owner resolution, and draft the alignment record that prevents relitigating. Draft analysis and record. If the split option creates a fragile seam, say so plainly even if it is the politically easy answer.

Format the output exactly as follows:

> Analysis: what each stream actually needs (beneath their position); options (A owns / B owns / split with defined seam) with consequences each; recommendation with the ownership rule stated crisply. Alignment record: decision; rationale; ownership rule; consultation duty; artefacts to update; review trigger. Impact assessment for whichever stream cedes scope.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example ownership recommendation: "Recommend: Stream B owns the case–billing interface spec end-to-end (they own the consuming system's behaviour); Stream A holds a 5-day review SLA. Split option rejected: the seam falls mid-payload where both streams would own half a mapping table — fragile."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
