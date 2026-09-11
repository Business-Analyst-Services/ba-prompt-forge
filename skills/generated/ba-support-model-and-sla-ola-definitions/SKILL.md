---
name: ba-support-model-and-sla-ola-definitions
description: Use when the user is working on service & operational readiness and needs service models, sla and ola definitions. Define the L1-L3 support model and the SLA/OLA set for the service. Produces a reviewable first draft for service management (ownership), vendors (agreement), business (expectations).
license: CC-BY-4.0
---

# Support Model & SLA/OLA Definitions

Derived from `TB-06-D1` in the BA Prompt Forge library
(Technical BA / Service & Operational Readiness, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing service & operational readiness work and needs one of:
- Service models
- SLA and OLA definitions

The audience for whatever you produce is: **Service management (ownership), vendors (agreement), business (expectations)**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[DESCRIBE]`
3. `[LIST WITH CURRENT RESPONSIBILITIES]`
4. `[WHEN MUST IT WORK, IMPACT OF OUTAGE]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Define the L1-L3 support model and the SLA/OLA set for the service. Draft the model and tables. Mark targets '[PROPOSED — VALIDATE]' and flag SLA/OLA mismatches.

Format the output exactly as follows:

> Support model: tier; owner (team/vendor); responsibilities; what escalates and when; hours; tooling (ITSM queues/assignment groups). Incident severity definitions with business-impact anchors and target response/restore per severity. SLA table: service; measure; target; measurement method; exclusions; reporting cadence. OLA table for internal dependencies underpinning each SLA. Gaps where a vendor contract does not back an SLA are flagged.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example severity anchor: "Sev 1: no customer can lodge a service request, or the payment run is at risk — response 15 min, restore target 4 hrs, exec comms hourly. Sev 3: single-user or cosmetic issue with a work-around — response 1 business day."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
