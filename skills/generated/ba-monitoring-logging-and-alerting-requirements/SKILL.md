---
name: ba-monitoring-logging-and-alerting-requirements
description: Use when the user is working on operational engineering & observability and needs monitoring requirements, alerting requirements, logging requirements. Define what must be monitored, logged and alerted, grounded in business impact. Produces a reviewable first draft for operations engineers implementing.
license: CC-BY-4.0
---

# Monitoring, Logging & Alerting Requirements

Derived from `TB-03-D1` in the BA Prompt Forge library
(Technical BA / Operational Engineering & Observability, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing operational engineering & observability work and needs one of:
- Monitoring requirements
- alerting requirements
- logging requirements

The audience for whatever you produce is: **Operations engineers implementing; service management defining response**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[DESCRIBE]`
3. `[NOTES]`
4. `[E.G. SPLUNK]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Define what must be monitored, logged and alerted, grounded in business impact. Draft the tables. Flag over-alerting risks and any log content that would breach privacy expectations.

Format the output exactly as follows:

> Monitoring table: item; business reason; metric/signal; threshold; alert severity; who is notified; expected response and timeframe. Logging table: event; data captured; retention period; access restrictions (flag personal or sensitive data in logs as a privacy risk); audit obligation served. Alert hygiene rules: no alert without an owner and an action.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example log row: "Event: case document viewed | Captured: user id, case id, document id, timestamp (no document content in logs) | Retention: 7 years [CONFIRM with Records] | Access: security team + audit only | Obligation served: privacy audit trail. Alert-hygiene example: 'disk >80%' pages nobody — route to the weekly capacity report instead; alerts page only when a human must act now."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
