---
name: ba-sprint-capacity-and-dependency-inputs
description: Use when the user is working on iteration & release planning support and needs sprint/iteration plans, dependency registers. Prepare the capacity and dependency inputs that make sprint planning a 30-minute decision. Produces a reviewable first draft for squad and product owner in sprint planning.
license: CC-BY-4.0
---

# Sprint Capacity & Dependency Inputs

Derived from `AB-04-D2` in the BA Prompt Forge library
(Agile BA / Iteration & Release Planning Support, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing iteration & release planning support work and needs one of:
- Sprint/Iteration Plans
- Dependency Registers

The audience for whatever you produce is: **Squad and product owner in sprint planning**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[SQUAD NAME, PRODUCT/SYSTEM, CADENCE e.g. 2-week sprints, TOOL e.g. Jira]`
3. `[PASTE OR 'STANDARD']`
4. `[PASTE STORIES WITH ESTIMATES]`
5. `[POINTS/DAYS, LEAVE, MEETINGS, SUPPORT LOAD]`
6. `[LIST KNOWN]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Prepare the capacity and dependency inputs that make sprint planning a 30-minute decision. Draft the inputs. Flag overcommitment explicitly if candidates exceed capacity — do not quietly stretch the numbers.

Format the output exactly as follows:

> Capacity calculation shown (raw minus leave, ceremonies, support allowance — state the buffer %); candidate scope vs capacity table with a clear cut-line; per candidate: DoR status and dependencies with owner and needed-by date; sprint goal options (2-3 drafts) each tied to the scope above its cut-line; risks to the sprint with mitigations.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example capacity calc: "Raw 80 pts → minus leave (J.S. 1 wk: −8) → minus ceremonies/support allowance 15% (−12) → planning capacity 60 pts, cut-line drawn at 56 pts (7% buffer). Candidates total 71 pts → 15 pts must fall below the line — decision for PO, options listed."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
