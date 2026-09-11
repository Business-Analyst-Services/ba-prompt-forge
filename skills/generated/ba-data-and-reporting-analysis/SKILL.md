---
name: ba-data-and-reporting-analysis
description: 'Use when the user is working on data & reporting analysis and needs data requirements, data mapping, reporting requirements, kpi definitions. Define the business data, information and reporting requirements for this initiative: what data is needed, what it means, where it comes from, and what reports and KPIs it must feed. Produces a reviewable first draft for business data owners, reporting teams and the data engineering team.'
license: CC-BY-4.0
---

# Master – Data & Reporting Analysis

Derived from `BB-04-M` in the BA Prompt Forge library
(Business BA / Data & Reporting Analysis, scored 19/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing data & reporting analysis work and needs one of:
- Data Requirements
- Data Mapping
- Reporting Requirements
- KPI Definitions

The audience for whatever you produce is: **Business data owners, reporting teams and the data engineering team**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[DESCRIBE]`
3. `[LIST, e.g. core case management system, billing system, request intake channel, data warehouse]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- data requirements catalogue (entity, element, business definition, classification incl. personal/health info, quality expectation)
- source-to-target data mapping tables
- reporting requirements (report, purpose, audience, KPIs, dimensions, frequency, access restrictions)
- KPI definitions
- for data warehouse / BI work: a business question catalogue (what/why/how/when/who per question), MECE validation of question themes, business logic and refresh-frequency definitions, and BI technical specification structure (sources, joins, logic — flagged for peer review via validation queries)

Format the output exactly as follows:

> Structured, evidence-based business analysis writing aligned to BABOK good practice. Use clear headings, numbered requirements and tables where they aid scanning. Plain English; expand every acronym on first use; no marketing language. Business language first; add technical detail (types, validation) only after meaning is agreed. Where the data includes personal or otherwise sensitive information, flag the classification per element.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example element row: "Entity: Request | Element: request_severity | Definition: initial severity band assigned at lodgement (1–4) per triage matrix | Classification: internal | Quality expectation: mandatory at creation, single value, revalidated at assessment".

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
