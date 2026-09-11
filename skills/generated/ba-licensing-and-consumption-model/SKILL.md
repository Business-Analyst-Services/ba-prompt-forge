---
name: ba-licensing-and-consumption-model
description: Use when the user is working on platform design & infrastructure and needs licensing & consumption model definitions, cost forecast structure. Model how licensing and consumption costs scale with usage so commercial decisions and forecasts are grounded. Produces a reviewable first draft for finance and procurement (forecasting), architects (design-to-cost).
license: CC-BY-4.0
---

# Licensing & Consumption Model

Derived from `TB-04-D2` in the BA Prompt Forge library
(Technical BA / Platform Design & Infrastructure, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing platform design & infrastructure work and needs one of:
- Licensing & consumption model definitions
- cost forecast structure

The audience for whatever you produce is: **Finance and procurement (forecasting), architects (design-to-cost)**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[LIST WITH LICENSING BASIS IF KNOWN — PER USER, PER CORE, CONSUMPTION]`
3. `[USERS, TRANSACTIONS, STORAGE, GROWTH]`
4. `[TERM, COMMITTED SPEND, TRUE-UP RULES]`
5. `[UNIT PRICE]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Model how licensing and consumption costs scale with usage so commercial decisions and forecasts are grounded. Draft the model. Never invent dollar figures; build the structure and flag every input finance must supply.

Format the output exactly as follows:

> Per product: licensing construct explained plainly; cost drivers; scaling behaviour (linear/step/tiered); scenario table (current, +25% growth, +50%, peak) with formula structure rather than invented unit prices — use [UNIT PRICE] placeholders; watch-outs (true-up exposure, egress fees, minimum commitments, licence audits). Consolidated forecast structure ready for finance to populate.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example scenario row: "Product: document AI service | Construct: consumption (per 1,000 pages) | Current: 4.2M pages/yr → [UNIT PRICE] × 4,200 | +25% growth: 5.25M pages | Step risk: tier boundary at 5M pages — unit price drops 12% above it, consider committed tier | Watch-out: re-processing during migration counts as consumption (est. one-off 1.8M pages)."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
