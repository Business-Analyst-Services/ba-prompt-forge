---
name: ba-requirements-governance-and-traceability
description: 'Use when the user is working on requirements governance & traceability and needs traceability matrix, decision log, information governance artefacts. Maintain control of requirements and decisions: traceability from business need through to test, a disciplined decision log, change control support and consistency checking across artefacts. Produces a reviewable first draft for project governance, auditors, and the delivery team relying on a single source of truth.'
license: CC-BY-4.0
---

# Master – Requirements Governance & Traceability

Derived from `BT-05-M` in the BA Prompt Forge library
(Business/Tech BA / Requirements Governance & Traceability, scored 19/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing requirements governance & traceability work and needs one of:
- Traceability Matrix
- Decision Log
- Information Governance Artefacts

The audience for whatever you produce is: **Project governance, auditors, and the delivery team relying on a single source of truth**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[LIST — needs, requirements, stories, designs, tests]`
3. `[DESCRIBE OR 'STANDARD']`
4. `[BASELINED ON DATE / NOT YET]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- traceability matrix structure and population from pasted artefacts (need → requirement → story → test, with gaps flagged)
- decision log entries from meeting notes (decision, date, decider, rationale, alternatives rejected, impacts)
- scope creep review of new requests against the baseline (within scope / beyond scope / ambiguous, with recommended action)
- cross-artefact consistency check flagging contradictions

Format the output exactly as follows:

> Structured, evidence-based business analysis writing aligned to BABOK good practice. Use clear headings, numbered requirements and tables where they aid scanning. Plain English; expand every acronym on first use; no marketing language. Every requirement traces forward to verification and back to a business need; orphans in either direction are findings, not footnotes.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example trace row: "BN-03 → FR-014, FR-015 → ST-041 → UAT-C12, UAT-C13 (covered). Gap example: FR-022 has no source business need — flagged as potential scope creep, action: confirm with sponsor or remove from baseline."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
