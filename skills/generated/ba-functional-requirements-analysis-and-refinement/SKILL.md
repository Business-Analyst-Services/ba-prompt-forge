---
name: ba-functional-requirements-analysis-and-refinement
description: Use when the user is working on functional requirements analysis & refinement and needs feature definition, functional requirements, non-functional requirements. Elaborate business needs into well-formed features, functional requirements and non-functional requirements across business and system layers, then quality-review them for ambiguity, testability, completeness and consistency. Produces a reviewable first draft for business stakeholders (validation), designers and developers (build), testers (verification).
license: CC-BY-4.0
---

# Master – Functional Requirements Analysis

Derived from `BB-06-M` in the BA Prompt Forge library
(Business BA / Functional Requirements Analysis & Refinement, scored 19/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing functional requirements analysis & refinement work and needs one of:
- Feature Definition
- Functional Requirements
- Non-Functional Requirements

The audience for whatever you produce is: **Business stakeholders (validation), designers and developers (build), testers (verification)**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[PASTE BUSINESS NEEDS STATEMENTS]`
3. `[NEW BUILD / CONFIGURING PRODUCT / ENHANCEMENT — NAME SYSTEM IF KNOWN]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- feature definitions (name, description, business need served, in/out of scope)
- functional requirements per feature ('The system shall...' with acceptance criteria)
- NFR set covering performance, availability, security, privacy, accessibility (WCAG 2.2 AA), auditability, usability
- a quality review pass flagging vague words, untestable items and gaps with suggested rewrites

Format the output exactly as follows:

> Structured, evidence-based business analysis writing aligned to BABOK good practice. Use clear headings, numbered requirements and tables where they aid scanning. Plain English; expand every acronym on first use; no marketing language. Requirements are atomic, testable, solution-agnostic unless configuring a named product, and uniquely numbered. NFRs use measurable targets, never 'fast' or 'user-friendly'.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example pair: "FR-031: The system shall allow a field officer to attach up to 10 photographs to a field observation, each up to 25MB. NFR-P02: 95% of observation submissions over the mobile network shall complete within 5 seconds [PROPOSED — VALIDATE]."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
