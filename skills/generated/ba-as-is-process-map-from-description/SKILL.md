---
name: ba-as-is-process-map-from-description
description: Use when the user is working on process analysis & improvement and needs as-is process maps. Convert the user's rough description into a structured as-is process map ready for stakeholder validation. Produces a reviewable first draft for process performers who will validate it step by step.
license: CC-BY-4.0
---

# As-Is Process Map (from description)

Derived from `BB-07-D1` in the BA Prompt Forge library
(Business BA / Process Analysis & Improvement, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing process analysis & improvement work and needs one of:
- As-Is Process Maps

The audience for whatever you produce is: **Process performers who will validate it step by step**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[PASTE INTERVIEW NOTES OR DESCRIPTION]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Convert the user's rough description into a structured as-is process map ready for stakeholder validation. Draft the map. List every step where the user's description was ambiguous or incomplete as targeted validation questions.

Format the output exactly as follows:

> Output: start and end points; numbered steps each with role (swimlane), action, system used, inputs/outputs; decision points as questions with each path; parallel activities noted; handoffs highlighted; pain points and delays annotated where they occur. Then provide the same flow as Mermaid flowchart code with swimlane-style role prefixes.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example decision point: "D2: Is the customer registered? If YES → step 5 (link the request to the customer record). If NO → step 5a [Registration Team] creates a provisional customer record (handoff — known delay: 1–2 days, PP-1)."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
