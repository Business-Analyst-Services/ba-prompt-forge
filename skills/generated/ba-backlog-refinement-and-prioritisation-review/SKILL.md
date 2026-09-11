---
name: ba-backlog-refinement-and-prioritisation-review
description: Use when the user is working on backlog management (agile) and needs refined backlog, prioritisation. Review the pasted backlog for readiness and produce a defensible prioritisation. Produces a reviewable first draft for product owner and delivery lead.
license: CC-BY-4.0
---

# Backlog Refinement & Prioritisation Review

Derived from `BT-02-D2` in the BA Prompt Forge library
(Business/Tech BA / Backlog Management (Agile), scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing backlog management (agile) work and needs one of:
- Refined backlog
- prioritisation

The audience for whatever you produce is: **Product owner and delivery lead**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[PASTE STORIES/ITEMS]`
3. `[CAPACITY, DEADLINES, DEPENDENCIES]`
4. `[MoSCoW / WSJF / VALUE-EFFORT]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Review the pasted backlog for readiness and produce a defensible prioritisation. Deliver both tables and a short list of themes (recurring quality problems) to fix at the source.

Format the output exactly as follows:

> Readiness table: item; issues found (vague, untestable, too large, missing criteria); suggested fix or split. Prioritisation table: item; priority; one-sentence rationale; dependencies; risk if deferred. Flag items that appear to be scope creep against the stated project scope.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example review row: "Item J-231: vague — 'improve search'. Issues: no acceptance criteria, outcome unmeasurable. Fix: restate as 'search returns a customer by trading name, legal name or registration number within 2s' + 3 ACs. Priority: Should (supports intake efficiency; not blocking go-live). Deferral risk: continued manual lookups (~10 min/officer/day)."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
