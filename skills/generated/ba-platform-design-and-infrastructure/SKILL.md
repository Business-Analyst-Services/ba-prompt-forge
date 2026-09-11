---
name: ba-platform-design-and-infrastructure
description: 'Use when the user is working on platform design & infrastructure and needs platform architecture inputs, environment topology definitions, hosting & deployment model definitions, compute & workload placement. Provide the analysis that platform design decisions need: hosting model, environment strategy, compute and workload placement, network topology and connectivity, licensing and consumption modelling, and solution dependencies. Produces a reviewable first draft for platform architects and infrastructure engineers (decisions), finance (consumption models), governance (residency and compliance).'
license: CC-BY-4.0
---

# Master – Platform Design & Infrastructure Analysis

Derived from `TB-04-M` in the BA Prompt Forge library
(Technical BA / Platform Design & Infrastructure, scored 19/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing platform design & infrastructure work and needs one of:
- Platform architecture inputs
- environment topology definitions
- hosting & deployment model definitions
- compute & workload placement
- network topology & connectivity specifications
- licensing & consumption model definitions

The audience for whatever you produce is: **Platform architects and infrastructure engineers (decisions), finance (consumption models), governance (residency and compliance)**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[DESCRIBE]`
3. `[TRANSACTION VOLUMES, CONCURRENCY, PROCESSING TYPES, VARIABILITY]`
4. `[OTHER — EXISTING CLOUD AGREEMENTS, ON-PREM DEPENDENCIES, BUDGET]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- hosting model analysis (cloud/on-prem/hybrid options against data sensitivity, dependencies, latency, residency, continuity)
- environment strategy (environments needed, prod-likeness, data per environment, footprint vs cost)
- compute and workload placement inputs (volumes, concurrency, processing types, variability → placement considerations)
- network topology and connectivity requirements (communication paths, internal/external access, partner connectivity, security boundary expectations)
- licensing and consumption model (drivers, scaling scenarios, cost forecast structure)
- dependency register with contract/vendor constraints

Format the output exactly as follows:

> Structured technical-BA writing: requirements numbered and testable, expressed as needs and constraints rather than design decisions (pre-solution) or as precise specifications (post-solution). Tables over prose where possible; expand acronyms on first use. Capture the business inputs that answer design questions ('should this be serverless or containerised', 'full cloud vs hybrid', 'can data and processing stay in the required jurisdiction') rather than making architecture decisions; present options with trade-offs for architects to decide.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example placement input: "Workload: annual billing batch | Volume: 280k accounts over 6 nights, CPU-heavy calculation | Variability: annual peak (July), quiet the rest of the year | Placement consideration: burstable/scheduled compute rather than year-round dedicated capacity; feeds the design question 'dedicated batch compute vs autoscaling'."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
