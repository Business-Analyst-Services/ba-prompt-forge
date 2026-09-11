---
name: ba-interface-specification
description: Use when the user is working on integration, data & migration and needs interface specifications, integration mappings. Draft a complete interface specification for designer/developer consumption. Produces a reviewable first draft for integration designers and developers.
license: CC-BY-4.0
---

# Interface Specification

Derived from `TB-02-D1` in the BA Prompt Forge library
(Technical BA / Integration, Data & Migration, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing integration, data & migration work and needs one of:
- Interface specifications
- integration mappings

The audience for whatever you produce is: **Integration designers and developers; reviewed by data owners**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[SOURCE SYSTEM]`
3. `[TARGET SYSTEM]`
4. `[WHY DATA MOVES]`
5. `[TRIGGER, FREQUENCY, VOLUMES IF KNOWN]`
6. `[TBC — OWNER]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Draft a complete interface specification for designer/developer consumption. Draft the specification. Mark unknowns '[TBC — OWNER]' rather than inventing values, and list the questions that close them.

Format the output exactly as follows:

> Sections: purpose and business context; interaction model (trigger, direction, sync/async expectation with rationale, frequency, latency requirement); data payload with field-level source-to-target mapping and transformation rules; volumes (average/peak) and growth; error handling and retry expectations (what the business needs to happen on failure, including idempotency needs); monitoring and alerting needs; assumptions and open questions.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example mapping row: "Source: LEGACY.CUST.TRADING_NM (varchar 60) → Target: customer.trading_name (varchar 120) | Transform: trim, title-case, strip legacy '*' suffix flags into a separate status field | Rule ref: TR-11 | Notes: 3% of records exceed 60 chars and are truncated in legacy [DATA QUALITY FLAG]."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
