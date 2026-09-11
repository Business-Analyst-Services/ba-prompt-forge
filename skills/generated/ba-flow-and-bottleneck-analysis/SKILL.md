---
name: ba-flow-and-bottleneck-analysis
description: Use when the user is working on agile metrics & flow analysis and needs cumulative flow analysis, cycle time reports, bottleneck assessments. Find where work actually gets stuck, and test whether the data supports the squad's intuition. Produces a reviewable first draft for squad (owns the fixes) and delivery lead.
license: CC-BY-4.0
---

# Flow & Bottleneck Analysis

Derived from `AB-05-D1` in the BA Prompt Forge library
(Agile BA / Agile Metrics & Flow Analysis, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing agile metrics & flow analysis work and needs one of:
- Cumulative Flow Analysis
- Cycle Time Reports
- Bottleneck Assessments

The audience for whatever you produce is: **Squad (owns the fixes) and delivery lead**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[SQUAD NAME, PRODUCT/SYSTEM, CADENCE e.g. 2-week sprints, TOOL e.g. Jira]`
3. `[PASTE OR 'STANDARD']`
4. `[PASTE CYCLE TIME PER STAGE / CFD EXPORT / TICKET TIMESTAMPS]`
5. `[LIST BOARD COLUMNS]`
6. `[WHAT THE SQUAD SAYS IS SLOW]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Find where work actually gets stuck, and test whether the data supports the squad's intuition. Run the analysis. Where the data contradicts the squad's felt pain, say so and explain the gap.

Format the output exactly as follows:

> Cycle time by stage (median and 85th percentile — not averages alone); wait time vs work time split where data allows; WIP analysis against limits; bottleneck hypothesis with the evidence for it and one alternative explanation considered; 2-3 countermeasures matched to the specific bottleneck type (WIP limit, policy change, skill spread), each with 'how we'd know it worked'.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example bottleneck finding: "Median cycle time in 'Waiting for Test': 4.1 days (85th pct: 9 days) vs 'In Test' work time 0.5 days — the constraint is queueing, not testing effort. Alternative considered: environment contention (rejected — env free 87% of window). Countermeasure: WIP limit of 2 on dev-complete; signal: waiting-median <1.5 days within 3 sprints."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
