---
name: ba-transition-requirements-and-readiness-checklist
description: 'Use when the user is working on operational readiness & transition and needs system transition plan, operational readiness support. Define what must be true before go-live: transition requirements plus a verifiable readiness checklist. Produces a reviewable first draft for readiness leads (execution) and go-live decision forum (go/no-go).'
license: CC-BY-4.0
---

# Transition Requirements & Readiness Checklist

Derived from `BT-04-D1` in the BA Prompt Forge library
(Business/Tech BA / Operational Readiness & Transition, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing operational readiness & transition work and needs one of:
- System Transition Plan
- Operational Readiness support

The audience for whatever you produce is: **Readiness leads (execution) and go-live decision forum (go/no-go)**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[DESCRIBE]`
3. `[LIST]`
4. `[DATES, BLACKOUT PERIODS, PARALLEL RUN?]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Define what must be true before go-live: transition requirements plus a verifiable readiness checklist. Draft requirements and checklist. Flag the items most commonly missed (access provisioning lead times, support knowledge articles, external party comms).

Format the output exactly as follows:

> Requirements grouped: process transition, data cutover, access and security, training and comms, support readiness, business continuity/rollback. Checklist table: item; readiness criterion (verifiable); owner; evidence required; due date relative to go-live; status. Include go/no-go criteria and rollback triggers.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example rollback trigger: "Trigger R2: >5% of service requests failing to save in the first 4 business hours → invoke rollback step 6 (re-point DNS to legacy form, comms template C-2 to customers, incident bridge stood up). Decision holder: Service Owner."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
