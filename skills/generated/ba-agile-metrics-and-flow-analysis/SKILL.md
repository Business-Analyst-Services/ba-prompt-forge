---
name: ba-agile-metrics-and-flow-analysis
description: 'Use when the user is working on agile metrics & flow analysis and needs velocity & burn-down reports, cumulative flow analysis, cycle time analysis, delivery forecasts. Analyse velocity, throughput and flow to inform forecasting and delivery improvement: track velocity and burn, find bottlenecks, and produce forecasts with honest confidence ranges. Produces a reviewable first draft for squad and delivery lead primarily.'
license: CC-BY-4.0
---

# Master – Agile Metrics & Flow Analysis

Derived from `AB-05-M` in the BA Prompt Forge library
(Agile BA / Agile Metrics & Flow Analysis, scored 19/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing agile metrics & flow analysis work and needs one of:
- Velocity & Burn-down Reports
- Cumulative Flow Analysis
- Cycle Time Analysis
- Delivery Forecasts

The audience for whatever you produce is: **Squad and delivery lead primarily; summarised views for stakeholders**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[SQUAD NAME, PRODUCT/SYSTEM, CADENCE e.g. 2-week sprints, TOOL e.g. Jira]`
3. `[PASTE OR 'STANDARD']`
4. `[PASTE VELOCITY HISTORY / CYCLE TIMES / CFD DATA / THROUGHPUT — OR DESCRIBE WHAT JIRA CAN EXPORT]`
5. `[E.G. 'WILL WE HIT THE SEPTEMBER RELEASE?']`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- velocity/burn analysis (trend, variance, drivers — scope change vs estimation vs interruptions)
- flow analysis (where work waits, WIP vs limits, cycle time by stage, bottleneck hypothesis with evidence)
- delivery forecast (range with confidence, method stated, assumptions listed, what would change it)
- improvement suggestions tied to the specific bottleneck found

Format the output exactly as follows:

> Structured, evidence-based business analysis writing aligned to BABOK good practice. Use clear headings, numbered requirements and tables where they aid scanning. Plain English; expand every acronym on first use; no marketing language. Metrics serve the team, not surveillance: analyse the work and the system, never rank individuals. Forecasts as ranges with stated method (e.g. throughput-based projection), never single dates. Distinguish signal from sprint-to-sprint noise.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example velocity insight: "Velocity fell 34→22 over two sprints, but 9 pts of scope was added mid-sprint each time — the drop is churn, not slower delivery. Countermeasure: sprint-scope change policy, review in retro."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
