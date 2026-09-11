---
name: ba-work-allocation-plan
description: Use when the user is working on ba team leadership & work allocation and needs work allocation plans. Allocate packages to BAs with explicit rationale, balanced load and managed risk. Produces a reviewable first draft for lead ba (decision), then discussed with each ba.
license: CC-BY-4.0
---

# Work Allocation Plan

Derived from `LB-02-D1` in the BA Prompt Forge library
(Lead BA / BA Team Leadership & Work Allocation, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing ba team leadership & work allocation work and needs one of:
- Work Allocation Plans

The audience for whatever you produce is: **Lead BA (decision), then discussed with each BA**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[PROGRAM/PROJECT, NUMBER OF BAs AND WORKSTREAMS, DELIVERY METHOD]`
3. `[LIST WITH SKILL NEEDS AND EFFORT]`
4. `[ROLE-LABELLED BAs: LEVEL, STRENGTHS, CURRENT LOAD, DEVELOPMENT GOALS]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Allocate packages to BAs with explicit rationale, balanced load and managed risk. Draft the allocation. Where a stretch assignment carries delivery risk, propose the support structure that makes it safe.

Format the output exactly as follows:

> Allocation table: package; allocated BA (role label); rationale (skills fit / load / development stretch); load check (% allocated vs capacity); risk flags (key-person dependency, stretch without support, competing deadlines) with mitigations (pairing, review points). Unallocated remainder and options if demand exceeds supply.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example allocation row: "Package: integration requirements → Senior BA-2 (rationale: interface spec experience, 60% loaded). Risk: single person with this skill — mitigation: mid BA-4 pairs 1 day/wk for succession. Development note: stretch for BA-4, review at sprint 3."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
