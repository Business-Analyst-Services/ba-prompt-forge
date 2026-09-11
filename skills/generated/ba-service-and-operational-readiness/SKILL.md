---
name: ba-service-and-operational-readiness
description: 'Use when the user is working on service & operational readiness and needs support procedures, service transition assessments, support readiness checklists, service models. Ensure the system, network and platform have an operational support model and are ready for production: support models, SLAs/OLAs, incident and event management, vendor responsibilities, environment governance and handover. Produces a reviewable first draft for service management, support teams, vendors and the service transition approver.'
license: CC-BY-4.0
---

# Master – Service & Operational Readiness

Derived from `TB-06-M` in the BA Prompt Forge library
(Technical BA / Service & Operational Readiness, scored 19/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing service & operational readiness work and needs one of:
- Support procedures
- service transition assessments
- support readiness checklists
- service models

The audience for whatever you produce is: **Service management, support teams, vendors and the service transition approver**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[DESCRIBE SYSTEM/PLATFORM]`
3. `[INTERNAL TEAMS, VENDORS, SERVICE DESK TOOL e.g. ServiceNow]`
4. `[DATE]`
5. `[SUPPORT SCOPE IF KNOWN]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- support model (L1-L3 responsibilities, escalation paths, hours, incident vs request flows, ITSM tool integration needs)
- SLA and OLA definitions (service, measure, target, measurement method, reporting)
- vendor responsibility RACI with escalation and contract reference points
- service transition assessment (criteria, evidence, gaps, risk rating)
- support readiness checklist and handover pack contents (procedures, known errors, FAQs, training)

Format the output exactly as follows:

> Structured technical-BA writing: requirements numbered and testable, expressed as needs and constraints rather than design decisions (pre-solution) or as precise specifications (post-solution). Tables over prose where possible; expand acronyms on first use. Support model expressed as who does what at L1/L2/L3 with unambiguous boundaries; SLAs measurable; readiness items verifiable with evidence.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example SLA row: "Service: service request portal | Measure: availability, business hours (7am–7pm Mon–Sat) | Target: 99.5% monthly | Measurement: synthetic monitoring, excludes approved change windows | Reporting: monthly service review. Backing OLA: platform team restores hosting within 2 hours (P1)."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
