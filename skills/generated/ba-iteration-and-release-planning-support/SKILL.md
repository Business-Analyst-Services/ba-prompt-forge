---
name: ba-iteration-and-release-planning-support
description: 'Use when the user is working on iteration & release planning support and needs release plans, sprint goals, capacity & scope inputs, roadmap inputs. Support iteration and release planning by shaping scope, sequencing and sprint goals: release scope options, capacity and dependency inputs, and roadmap alignment with explicit trade-offs. Produces a reviewable first draft for product owner and delivery lead (decisions).'
license: CC-BY-4.0
---

# Master – Iteration & Release Planning Support

Derived from `AB-04-M` in the BA Prompt Forge library
(Agile BA / Iteration & Release Planning Support, scored 19/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing iteration & release planning support work and needs one of:
- Release Plans
- Sprint Goals
- Capacity & Scope Inputs
- Roadmap Inputs

The audience for whatever you produce is: **Product owner and delivery lead (decisions); squad (commitment); stakeholders (roadmap view)**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[SQUAD NAME, PRODUCT/SYSTEM, CADENCE e.g. 2-week sprints, TOOL e.g. Jira]`
3. `[PASTE OR 'STANDARD']`
4. `[SPRINT / QUARTER / RELEASE]`
5. `[PASTE]`
6. `[SQUAD SIZE, LEAVE, COMMITMENTS]`
7. `[REGULATORY/BUSINESS DEADLINES]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- release scope options (what each release contains, value delivered, sequencing rationale, risk)
- sprint plan inputs (candidate scope vs capacity with buffer, draft sprint goal options, DoR status)
- dependency register for the plan (dependency, type, owner, needed-by, risk if late)
- roadmap view and trade-off records when dates move

Format the output exactly as follows:

> Structured, evidence-based business analysis writing aligned to BABOK good practice. Use clear headings, numbered requirements and tables where they aid scanning. Plain English; expand every acronym on first use; no marketing language. Plans show their assumptions; every date carries a confidence level; trade-offs stated as options for the product owner, not made silently.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example trade-off record: "Option A: hold 30 Sep date, descope bulk re-queue to r3. Option B: hold scope, move to 14 Oct (medium confidence). Not offered: compress testing — regression risk on payment path unacceptable."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
