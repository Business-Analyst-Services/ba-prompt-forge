---
name: ba-backlog-management-agile
description: 'Use when the user is working on backlog management (agile) and needs epics, features, user stories, acceptance criteria. Keep the delivery backlog healthy on cadence: break epics into features and stories, write acceptance criteria, refine and prioritise, and keep items meeting the Definition of Ready. Produces a reviewable first draft for product owner, scrum team and stakeholders reading the backlog.'
license: CC-BY-4.0
---

# Master – Agile Backlog Management

Derived from `BT-02-M` in the BA Prompt Forge library
(Business/Tech BA / Backlog Management (Agile), scored 19/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing backlog management (agile) work and needs one of:
- Epics
- Features
- User Stories
- Acceptance Criteria

The audience for whatever you produce is: **Product owner, scrum team and stakeholders reading the backlog**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[TEAM, CADENCE, TOOL e.g. Jira]`
3. `[PASTE OR DESCRIBE]`
4. `[PASTE OR 'STANDARD']`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- epic → feature → story breakdowns
- acceptance criteria for pasted stories
- refinement review of pasted backlog items flagging vagueness, missing criteria, oversized stories with suggested splits
- MoSCoW or WSJF prioritisation with one-line rationale each. After drafting stories, self-critique for vague criteria and missing edge cases, then fix them

Format the output exactly as follows:

> Structured, evidence-based business analysis writing aligned to BABOK good practice. Use clear headings, numbered requirements and tables where they aid scanning. Plain English; expand every acronym on first use; no marketing language. Stories in 'As a [role], I want [capability], so that [outcome]' with Given/When/Then acceptance criteria — minimum 3 happy-path and 2 edge-case criteria per story. INVEST principles applied.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example story: "As a case officer, I want expired supporting documents flagged on the user's worklist, so that I can request updates before payments are interrupted. AC1 (Given/When/Then): Given a case with a supporting document expiring in ≤14 days, when I open the user's worklist, then the case shows an 'expiring' badge with days remaining."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
