---
name: ba-showcase-and-desk-check-pack
description: Use when the user is working on operational readiness & transition and needs showcases, dev walkthroughs, desk checks. Design the showcase session and desk check scripts that let the business validate the build against their needs. Produces a reviewable first draft for business smes and stakeholders attending.
license: CC-BY-4.0
---

# Showcase & Desk Check Pack

Derived from `BT-04-D2` in the BA Prompt Forge library
(Business/Tech BA / Operational Readiness & Transition, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing operational readiness & transition work and needs one of:
- Showcases
- Dev walkthroughs
- Desk checks

The audience for whatever you produce is: **Business SMEs and stakeholders attending; BA facilitating**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[PASTE FEATURES/STORIES]`
3. `[BUSINESS SMEs / SUPPORT / SPONSOR]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Design the showcase session and desk check scripts that let the business validate the build against their needs. Draft both packs. Ensure scenarios cover the highest-risk and highest-frequency paths first, and say why you ranked them so.

Format the output exactly as follows:

> Showcase: agenda; demo scenarios in business language (scenario, persona, data setup, steps, expected outcome, requirement/story reference); anticipated questions with suggested answers. Desk check scripts: numbered steps a business SME can follow unaided, expected result per step, pass/fail capture, defect logging instructions.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example demo scenario: "Scenario 3 – Customer lodges a request with photos (persona: small business owner, mobile). Data: synthetic customer C-TEST-04. Steps: lodge → triage queue → officer assignment. Expected: request visible to triage within 60s with photos attached. Refs: ST-021, ST-025."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
