---
name: ba-operational-engineering-and-observability
description: 'Use when the user is working on operational engineering & observability and needs monitoring requirements, alerting requirements, event management, logging requirements. Define monitoring, logging, alerting and operational support requirements: what needs watching, what events matter, availability and resilience needs, DR/backup expectations, and performance/scalability requirements. Produces a reviewable first draft for operations engineers, platform teams, service management.'
license: CC-BY-4.0
---

# Master – Operational Engineering & Observability

Derived from `TB-03-M` in the BA Prompt Forge library
(Technical BA / Operational Engineering & Observability, scored 19/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing operational engineering & observability work and needs one of:
- Monitoring requirements
- alerting requirements
- event management
- logging requirements
- support models
- operational dashboards

The audience for whatever you produce is: **Operations engineers, platform teams, service management; business owners validating targets**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[DESCRIBE]`
3. `[WHAT BREAKS FOR WHOM WHEN THIS FAILS]`
4. `[E.G. SPLUNK, SERVICENOW — OR 'TBD']`
5. `[PASTE OR 'TO BE DEFINED']`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- monitoring requirements (what to monitor, why it matters to the business, threshold, alert severity, response expectation)
- logging and audit requirements (event, data captured, retention, privacy constraints on logged personal data)
- availability and resilience requirements (uptime targets by business period, failure scenarios and tolerance)
- DR and backup requirements (RTO/RPO per business function with justification, recovery scenarios)
- performance and scalability requirements (load, peaks — e.g. seasonal volume spikes — growth, response-time targets)
- operational dashboard definitions

Format the output exactly as follows:

> Structured technical-BA writing: requirements numbered and testable, expressed as needs and constraints rather than design decisions (pre-solution) or as precise specifications (post-solution). Tables over prose where possible; expand acronyms on first use. Requirements derive from business impact: every alert traces to a business consequence and a response expectation; availability and RTO/RPO targets are business-justified, not aspirational.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example monitoring row: "Monitor: service request intake API availability | Business reason: primary intake channel — an outage creates compliance exposure | Signal: synthetic lodgement every 5 min | Threshold: 2 consecutive failures | Severity: P1, on-call platform engineer paged | Response: restore or invoke the phone-channel contingency within 30 min."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
