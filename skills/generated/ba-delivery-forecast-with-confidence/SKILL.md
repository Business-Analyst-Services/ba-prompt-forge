---
name: ba-delivery-forecast-with-confidence
description: Use when the user is working on agile metrics & flow analysis and needs delivery forecasts, confidence assessments. Forecast when the remaining scope will complete, as a defensible range. Produces a reviewable first draft for delivery lead and stakeholders asking 'when will it be done?'.
license: CC-BY-4.0
---

# Delivery Forecast with Confidence

Derived from `AB-05-D2` in the BA Prompt Forge library
(Agile BA / Agile Metrics & Flow Analysis, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing agile metrics & flow analysis work and needs one of:
- Delivery Forecasts
- Confidence Assessments

The audience for whatever you produce is: **Delivery lead and stakeholders asking 'when will it be done?'**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[SQUAD NAME, PRODUCT/SYSTEM, CADENCE e.g. 2-week sprints, TOOL e.g. Jira]`
3. `[PASTE OR 'STANDARD']`
4. `[ITEMS/POINTS REMAINING]`
5. `[PASTE THROUGHPUT/VELOCITY PER SPRINT, LAST 6+ SPRINTS]`
6. `[DATE]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Forecast when the remaining scope will complete, as a defensible range. Produce the forecast. If the user's history is under 4 sprints, say the forecast is low-confidence and what to do instead.

Format the output exactly as follows:

> Method stated up front (e.g. throughput range projection using best/typical/worst recent sprints); forecast as three dates (optimistic / likely / conservative) with the percentile logic; assumptions list (scope stability, team stability, no major holidays — flag any that are already false); scope-vs-date trade-off table ('to hit [DATE], descope to X'); what new information would most change the forecast.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example forecast: "Remaining 84 items. Throughput last 6 sprints: 9-14/sprint. Optimistic (best 3 avg, 13.7): 6.1 sprints → 18 Nov. Likely (median 11): 7.6 → 2 Dec. Conservative (worst 3 avg, 9.3): 9 → 16 Dec. Assumption now false: squad loses 1 dev from Sprint 42 — rerun with adjusted throughput."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
