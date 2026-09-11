---
name: ba-availability-dr-and-performance-requirements
description: Use when the user is working on operational engineering & observability and needs availability requirements, dr/backup expectations, performance and scalability requirements. Define availability, disaster recovery, backup and performance requirements with business justification. Produces a reviewable first draft for platform/infrastructure teams (design), business owners (target sign-off).
license: CC-BY-4.0
---

# Availability, DR & Performance Requirements

Derived from `TB-03-D2` in the BA Prompt Forge library
(Technical BA / Operational Engineering & Observability, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing operational engineering & observability work and needs one of:
- Availability requirements
- DR/backup expectations
- performance and scalability requirements

The audience for whatever you produce is: **Platform/infrastructure teams (design), business owners (target sign-off)**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[LIST WITH CRITICALITY]`
3. `[USERS, PEAKS, SEASONALITY]`
4. `[PASTE OR 'NONE']`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Define availability, disaster recovery, backup and performance requirements with business justification. Ask me the impact-of-outage questions you need, then draft. Show the cost-vs-availability trade-off where targets look expensive.

Format the output exactly as follows:

> Availability: target per business function and time period (business hours vs after hours), justified by consequence of outage. DR: RTO and RPO per function with justification; recovery scenarios to test. Backup: frequency, retention, restore-test expectation. Performance: response-time targets per key transaction; throughput at peak; scalability expectation (growth, spike handling). Every number marked '[PROPOSED — VALIDATE WITH BUSINESS OWNER]' unless I supplied it.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example DR line: "Function: case payment processing | RTO: 4 business hours | RPO: 15 minutes | Justification: a missed Thursday payment run affects ~9,000 recipients dependent on that income — reputational and hardship impact | Test: annual failover exercise with payment file replay [PROPOSED — VALIDATE]."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
