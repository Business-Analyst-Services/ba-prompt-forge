---
name: ba-operational-readiness-checklist-and-handover-pack
description: Use when the user is working on service & operational readiness and needs support readiness checklists, handover pack, support procedures. Produce the readiness checklist gating service transition and define the handover pack contents. Produces a reviewable first draft for service transition approver (gate), support teams (receivers).
license: CC-BY-4.0
---

# Operational Readiness Checklist & Handover Pack

Derived from `TB-06-D2` in the BA Prompt Forge library
(Technical BA / Service & Operational Readiness, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing service & operational readiness work and needs one of:
- Support readiness checklists
- handover pack
- support procedures

The audience for whatever you produce is: **Service transition approver (gate), support teams (receivers)**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[DESCRIBE]`
3. `[LIST]`
4. `[DATE]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Produce the readiness checklist gating service transition and define the handover pack contents. Draft checklist and pack definition. Rank the items by 'pain if missing at 2am during a Sev-1' and say why.

Format the output exactly as follows:

> Checklist grouped: support model in place; monitoring and alerting live; runbooks and procedures published; known errors and workarounds documented; access and licences provisioned; training delivered; DR tested; vendor support activated. Each item: verifiable criterion; owner; evidence; due date; status. Handover pack: document; purpose; author; acceptance criterion for the receiving team.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example checklist row: "Item: known errors documented | Criterion: all Sev 2+ defects deferred to post-go-live have a knowledge article with work-around, linked in ServiceNow | Owner: Support Transition Lead | Evidence: article list export | Due: go-live minus 5 days. (2am Sev-1 pain rank: #1 — without these, L1 escalates everything.)"

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
